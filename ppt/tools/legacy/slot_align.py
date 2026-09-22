#!/usr/bin/env python3
"""slot_align.py — 구분선 사이(슬롯) 수직 중앙 정렬 검수·보정 도구

프로젝트_지침 §6-3, §6-4, §9에 정의된 검수 절차를 그대로 구현한 것이다.
PDF로 렌더한 이미지를 픽셀로 재서, 가로 구분선 사이 내용의 위·아래 여백이
같아지도록 도형 y좌표를 옮긴다. 텍스트·글꼴·크기는 건드리지 않는다.

사용법
    python3 slot_align.py <파일.pptx>                 # 측정만
    python3 slot_align.py <파일.pptx> --fix           # 보정 후 <파일>_aligned.pptx 저장
    python3 slot_align.py <파일.pptx> --fix --rounds 3

필요 패키지: pillow, numpy / 외부 도구: soffice(LibreOffice), pdftoppm(poppler)

주의
- 슬라이드 폭의 50% 이상을 덮는 두께 12px 미만의 가로선을 '구분선'으로 본다
- 두 열 슬라이드는 구분선의 x범위로 열을 구분해 열마다 따로 잰다
- 보정 후에는 반드시 재렌더해 겹침·경계 이탈을 다시 확인한다(아래 check 함수)
"""
import argparse, os, re, shutil, subprocess, sys, tempfile, zipfile
import numpy as np
from PIL import Image

EMU = 914400
DPI = 150
SOFFICE = '/mnt/skills/public/pptx/scripts/office/soffice.py'
OFF = re.compile(r'<a:off x="(-?\d+)" y="(-?\d+)"/><a:ext cx="(\d+)" cy="(\d+)"')
SP = re.compile(r'<p:sp>.*?</p:sp>', re.S)


# ---------- 압축 해제 / 재압축 ----------

def unpack(pptx, dst):
    with zipfile.ZipFile(pptx) as z:
        z.extractall(dst)
        return [n for n in z.namelist() if not n.endswith('/')]


def repack(src_dir, names, out):
    """[Content_Types].xml을 첫 항목으로, 폴더 항목 없이 (지침 §6-4-1)"""
    order = ['[Content_Types].xml'] + [n for n in names if n != '[Content_Types].xml']
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        for n in order:
            z.write(os.path.join(src_dir, n), n)


def render(pptx, workdir):
    subprocess.run([sys.executable, SOFFICE, '--headless', '--convert-to', 'pdf', pptx],
                   cwd=workdir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    pdf = os.path.join(workdir, os.path.splitext(os.path.basename(pptx))[0] + '.pdf')
    for f in os.listdir(workdir):
        if f.startswith('pg-'):
            os.remove(os.path.join(workdir, f))
    subprocess.run(['pdftoppm', '-jpeg', '-r', str(DPI), pdf, 'pg'], cwd=workdir,
                   stdout=subprocess.DEVNULL)
    imgs = {}
    for f in sorted(os.listdir(workdir)):
        if f.startswith('pg-') and f.endswith('.jpg'):
            n = int(f.split('-')[1].split('.')[0])
            imgs[n] = np.array(Image.open(os.path.join(workdir, f)).convert('L'))
    return imgs


# ---------- 도형 파싱 ----------

def shapes(xml):
    out = []
    for m in SP.finditer(xml):
        s = m.group(0)
        o = OFF.search(s)
        if not o:
            continue
        x, y, cx, cy = [int(v) / EMU for v in o.groups()]
        out.append(dict(x=x, y=y, cx=cx, cy=cy, yemu=int(o.group(2)),
                        raw=o.group(0), off=(o.start() + m.start(), o.end() + m.start()),
                        text=''.join(re.findall(r'<a:t>(.*?)</a:t>', s)),
                        is_band=('solidFill' in s.split('<a:bodyPr')[0]) and cy > 0.3 and cx > 3))
    return out


def rule_columns(sh):
    """가로 구분선(높이 0, 폭 2인치 이상)을 x·폭이 같은 것끼리 묶어 열로 만든다"""
    cols = {}
    for s in sh:
        if s['cy'] == 0 and s['cx'] >= 2.0:
            cols.setdefault((round(s['x'], 2), round(s['cx'], 2)), []).append(s['y'])
    return {k: sorted(v) for k, v in cols.items() if len(v) >= 2}


def ink_extent(img, y0, y1, x0, x1):
    a, b = int((y0 + 0.035) * DPI), int((y1 - 0.035) * DPI)
    c, d = int(x0 * DPI), int(min(x1, 13.33) * DPI)
    sub = img[a:b, c:d]
    if sub.size == 0:
        return None
    rows = (sub < 200).sum(1)
    rows = np.where(rows > 0.5 * (d - c), 0, rows)      # 남은 선 제거
    nz = np.nonzero(rows)[0]
    if len(nz) == 0:
        return None
    return (a + nz[0]) / DPI, (a + nz[-1]) / DPI


# ---------- 측정·보정 ----------

def page_map(dirname):
    """PDF 페이지 번호 → 슬라이드 XML 파일명. sldIdLst 순서를 따른다.
    슬라이드를 중간에 삽입하면 파일 번호와 표시 순서가 어긋나므로 반드시 이 매핑을 쓴다."""
    pres = open(os.path.join(dirname, 'ppt/presentation.xml'), encoding='utf-8').read()
    rels = open(os.path.join(dirname, 'ppt/_rels/presentation.xml.rels'), encoding='utf-8').read()
    rid2f = dict(re.findall(r'Id="(rId\d+)"[^>]*Target="slides/(slide\d+\.xml)"', rels))
    order = re.findall(r'<p:sldId [^>]*r:id="(rId\d+)"', pres)
    return {i + 1: rid2f[r] for i, r in enumerate(order) if r in rid2f}


def pass_once(dirname, imgs, fix, tol=0.03, verbose=True):
    pmap = page_map(dirname)
    moved = 0
    for n in sorted(imgs):
        p = os.path.join(dirname, 'ppt/slides/' + pmap.get(n, 'slide%d.xml' % n))
        if not os.path.exists(p):
            continue
        xml = open(p, encoding='utf-8').read()
        sh = shapes(xml)
        edits = []
        for (cx0, cw), ys in rule_columns(sh).items():
            for y0, y1 in zip(ys, ys[1:]):
                if y1 - y0 < 0.5:
                    continue
                e = ink_extent(imgs[n], y0, y1, cx0, cx0 + cw)
                if not e:
                    continue
                gt, gb = e[0] - y0, y1 - e[1]
                delta = (gb - gt) / 2
                if verbose and abs(delta) >= tol:
                    print(f'  {pmap.get(n, n)} p{n} x{cx0:.2f} {y0:.2f}~{y1:.2f}  위 {gt:.2f} 아래 {gb:.2f}  보정 {delta:+.2f}')
                if fix and abs(delta) >= tol:
                    for s in sh:
                        if s['cy'] == 0 and s['cx'] >= 2.0:
                            continue                      # 구분선은 옮기지 않는다
                        if not (cx0 - 0.06 <= s['x'] <= cx0 + cw + 0.06):
                            continue                      # 다른 열
                        if s['is_band'] and not (y0 < s['y'] and s['y'] + s['cy'] < y1):
                            continue                      # 슬롯 밖 밴드는 건드리지 않는다
                        if y0 + 0.01 < s['y'] + s['cy'] / 2 < y1 - 0.01:
                            edits.append((s, delta))
        if fix and edits:
            for s, delta in sorted(edits, key=lambda e: -e[0]['off'][0]):
                new = int(round(s['yemu'] + delta * EMU))
                a, b = s['off']
                xml = xml[:a] + s['raw'].replace(f'y="{s["yemu"]}"', f'y="{new}"', 1) + xml[b:]
            open(p, 'w', encoding='utf-8').write(xml)
            moved += len(edits)
            print(f'  -> {pmap.get(n, n)}: {len(edits)}개 도형 이동')
    return moved


def check(dirname, imgs):
    """겹침·경계 이탈·줄간격 값 집합 점검 (지침 §6-4)"""
    print('\n[점검]')
    pmap = page_map(dirname)
    lnsp = set()
    for n in sorted(imgs):
        p = os.path.join(dirname, 'ppt/slides/' + pmap.get(n, 'slide%d.xml' % n))
        if not os.path.exists(p):
            continue
        xml = re.sub(r'\s+', ' ', open(p, encoding='utf-8').read())
        lnsp |= set(re.findall(r'<a:lnSpc><a:spcPct val="(\d+)"/>', xml))
        items = []
        for sp in SP.findall(xml):
            m = re.search(r'<a:off x="(-?\d+)" y="(-?\d+)"/> ?<a:ext cx="(\d+)" cy="(\d+)"', sp)
            if not m:
                continue
            x, y, cx, cy = [int(v) / EMU for v in m.groups()]
            t = ' '.join(re.findall(r'<a:t>(.*?)</a:t>', sp))
            band = ('solidFill' in sp.split('<a:bodyPr')[0]) and cy > 0.3 and cx > 3
            items.append((x, y, cx, cy, t, band))
            if y < -0.01 or y + cy > 7.51 or x < -0.01 or x + cx > 13.34:
                print(f'  {pmap.get(n, n)} p{n} 경계 이탈: {t[:30]} (y={y:.2f} cy={cy:.2f})')
        for i, (x, y, cx, cy, t, band) in enumerate(items):
            if not band:
                continue
            for j, (x2, y2, cx2, cy2, t2, _) in enumerate(items):
                if j < i and t2.strip() and y2 + cy2 > y + 0.03 and y2 < y + cy - 0.03 \
                        and x2 < x + cx and x2 + cx2 > x:
                    print(f'  {pmap.get(n, n)} p{n} 밴드가 텍스트를 덮음: {t2[:35]}')
        # 빈 구간 — 아무 요소도 없는 세로 구간을 직접 잰다.
        # '마지막 요소 y'만 보면 각주(보통 6.90) 때문에 통과하고, '마지막 구분선 y'만 보면
        # 밴드나 그림으로 아래를 채운 장까지 걸린다. 실제 빈 구간을 재는 것이 정확하다.
        # 임계값 235 — 구분선 색 DCE0E8(약 224)이 JPEG에서 밝아지므로 225로는 선을 놓친다.
        on = (imgs[n] < 235).sum(1) > 0
        s = None
        for y in range(len(on)):
            if not on[y] and s is None:
                s = y
            elif on[y] and s is not None:
                if s / DPI > 2.3 and (y - s) / DPI > 0.9:
                    print(f'  {pmap.get(n, n)} p{n} 빈 구간 {s / DPI:.2f}~{y / DPI:.2f} ({(y - s) / DPI:.2f}인치)')
                s = None
        # 마지막 잉크 뒤 하단 여백 — 위 루프는 잉크 '사이'만 재므로 여기서 따로 잰다
        nz2 = np.nonzero(on)[0]
        if len(nz2) and nz2[-1] / DPI < 6.5 and n > 1:
            print(f'  {pmap.get(n, n)} p{n} 하단 여백 — 마지막 요소 y={nz2[-1] / DPI:.2f} (기준 6.5 이상)')
    print('  줄간격 값 집합:', lnsp, '(118000·125000 두 값이어야 함)')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pptx')
    ap.add_argument('--fix', action='store_true')
    ap.add_argument('--rounds', type=int, default=2)
    a = ap.parse_args()

    work = tempfile.mkdtemp()
    src = os.path.join(work, 'src')
    os.makedirs(src)
    names = unpack(a.pptx, src)
    cur = os.path.join(work, 'cur.pptx')
    repack(src, names, cur)

    for r in range(a.rounds if a.fix else 1):
        imgs = render(cur, work)
        print(f'\n=== {r + 1}회차 ===')
        moved = pass_once(src, imgs, a.fix)
        repack(src, names, cur)
        if not a.fix or moved == 0:
            break

    imgs = render(cur, work)
    pass_once(src, imgs, False)
    check(src, imgs)

    if a.fix:
        out = os.path.splitext(a.pptx)[0] + '_aligned.pptx'
        shutil.copy(cur, out)
        print('\n저장:', out)
        print('※ PowerPoint에서 한 번 열어 확인할 것. 파일 무결성 3원칙은 validate.py로 별도 점검')


if __name__ == '__main__':
    main()
