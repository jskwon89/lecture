#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""화면 정렬 실측 점검 — 지침 §8-2 4항(150dpi 렌더 여백 측정)의 자동화.

사용법:
    soffice --headless --convert-to pdf deck.pptx
    pdftoppm -jpeg -r 150 deck.pdf page
    python3 check_spacing.py page-*.jpg

보는 것:
  ① 구분선 사이 내용의 위·아래 여백 차          (허용 0.05인치)
  ② 마지막 구분선의 위치                        (기준 6.72인치)
  ③ 마지막 구분선과 각주 글자 사이              (기준 0.41인치 ±0.05)
  ④ 행머리글의 열 안 좌우 여백 차               (허용 0.05인치)
  ⑤ 행머리글의 세로 중심과 행 한가운데의 차     (허용 0.05인치)

판정은 잉크 밝기 200 미만, 구분선은 가로폭 70% 이상이 235 미만인 줄로 본다.
"""
import sys
import numpy as np
from PIL import Image

DPI = 150
HEAD_X0, HEAD_X1 = 0.80, 3.25        # 행머리글 열
LAST_RULE = 6.72
FOOT_GAP = 0.41        # 마지막 구분선(6.72)과 각주 글자 사이
TOL = 0.05


def rules_of(im):
    h, w = im.shape
    hit = [y for y in range(h) if (im[y] < 235).sum() > w * 0.7]
    merged = []
    for y in hit:
        if merged and y - merged[-1][-1] <= 2:
            merged[-1].append(y)
        else:
            merged.append([y])
    return [int(np.mean(m)) for m in merged]


def check(path, cols=False):
    im = np.array(Image.open(path).convert('L'))
    h, w = im.shape
    ink = [y for y in range(h) if im[y].min() < 200]
    rs = rules_of(im)
    bad = []
    print(f'\n[{path}]')
    if not rs:
        print('  구분선을 찾지 못했다. 열 구성 장이면 이 점검은 건너뛴다.')
        return []

    for a, b in zip(rs, rs[1:]):
        if cols:      # 열 구성 장(D·E)은 행 단위 점검을 적용하지 않는다
            break
        seg = [y for y in ink if a + 3 < y < b - 3]
        if not seg:
            continue
        up, dn = (min(seg) - a) / DPI, (b - max(seg)) / DPI
        mark = '' if abs(up - dn) <= TOL else '  ← 위아래 여백 차'
        if mark:
            bad.append(f'{path}: 구분선 {a/DPI:.2f}~{b/DPI:.2f} 여백 차 {abs(up-dn):.3f}')
        print(f'  여백 위 {up:.2f} / 아래 {dn:.2f}{mark}')

        # 행머리글 위치
        x0, x1 = int(HEAD_X0 * DPI), int(HEAD_X1 * DPI)
        hseg = [y for y in range(a + 3, b - 3) if im[y, x0:x1].min() < 200]
        if hseg:
            xs = [x for x in range(x0, x1) if im[min(hseg):max(hseg) + 1, x].min() < 200]
            lpad, rpad = (min(xs) - x0) / DPI, (x1 - max(xs)) / DPI
            if lpad < 0.03:   # 왼쪽 끝에서 시작하면 마무리 문장이다(행머리글이 아니다)
                continue
            dc = ((min(hseg) + max(hseg)) / 2 - (a + b) / 2) / DPI
            m2 = '' if abs(lpad - rpad) <= TOL and abs(dc) <= TOL else '  ← 행머리글 중심'
            if m2:
                bad.append(f'{path}: 행머리글 좌우차 {abs(lpad-rpad):.3f} 세로차 {dc:.3f}')
            print(f'    행머리글 좌 {lpad:.2f} / 우 {rpad:.2f} · 세로 중심차 {dc:+.3f}{m2}')

    if cols:   # 열 구성 장은 마지막 구분선이 없을 수 있어 위치 판정을 하지 않는다
        print('  선 위치(in):', ', '.join(f'{y/DPI:.2f}' for y in rs))
        return []

    last = rs[-1] / DPI
    m3 = '' if abs(last - LAST_RULE) <= TOL else '  ← 마지막 구분선 위치'
    if m3:
        bad.append(f'{path}: 마지막 구분선 {last:.2f} (기준 {LAST_RULE})')
    print(f'  마지막 구분선 {last:.2f}{m3}')

    foot = [y for y in ink if y / DPI > last + 0.05]
    if foot:
        gap = (min(foot) / DPI) - last
        m4 = '' if abs(gap - FOOT_GAP) <= TOL else '  ← 각주까지 간격'
        if m4:
            bad.append(f'{path}: 각주까지 {gap:.2f} (기준 {FOOT_GAP})')
        print(f'  각주까지 {gap:.2f}{m4}')
    return bad


if __name__ == '__main__':
    cols = '--cols' in sys.argv
    files = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not files:
        print(__doc__)
        sys.exit(1)
    bad = []
    for f in files:
        bad += check(f, cols)
    print('\n' + ('=' * 60))
    if bad:
        print('점검에서 걸린 항목')
        for b in bad:
            print(' -', b)
        sys.exit(1)
    print('모든 장이 허용 범위 안에 있다.')