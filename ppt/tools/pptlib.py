import re, os
from xml.sax.saxutils import escape
 
E = 914400

# ── 팔레트 (제작 지침 5판 §1-3) ───────────────────────────────
NAVY       = '1E2761'   # 제목·행머리글·굵은 선·하단 밴드 면
FACE_NAVY  = '5A6699'   # 막대·도해 면 (위에 흰 글자)
FACE_GOLD  = 'C2A648'   # 막대·도해 면 (위에 흰 글자)
GOLD       = 'A8871C'   # 흰 바탕 위 금색 글자 — 한정 줄·칩·제한
INK        = '222633'   # 결론 줄
SUB        = '464D5C'   # 보충 줄·키커
FOOT       = '6E7686'   # 각주·우상단 단서
LINE       = 'DCE0E8'   # 얇은 가로 구분선
BAND       = 'F2F4F8'   # 상단 요약 밴드 면
WHITE      = 'FFFFFF'
RED        = 'C0392B'   # 주의·대비 표시선과 라벨에만 (면색 금지)
NEUTRAL    = 'C9CEDA'   # 도해의 중립 회색 면
COVER_L1, COVER_L2, COVER_L3 = '8A97BC', 'AFBBD9', 'C9D2E6'

PALETTE = {NAVY, FACE_NAVY, FACE_GOLD, GOLD, INK, SUB, FOOT, LINE, BAND,
           WHITE, RED, NEUTRAL, COVER_L1, COVER_L2, COVER_L3}

# ── 골격 좌표 (§1-1) ─────────────────────────────────────────
M_L, M_W = 0.80, 11.73          # 좌 여백 · 본문 폭
KICKER   = (0.80, 0.40, 5.70, 0.32)
CUE      = (6.60, 0.42, 5.93, 0.28)
TITLE    = (0.80, 0.70, 11.73, 0.70)
CHIP     = (6.60, 0.78, 5.93, 0.52)
BAND_BG  = (0.80, 1.55, 11.73)   # h는 한 행 0.60 · 두 행 0.85
BAND_TX  = (1.10, 1.55, 11.10)
HEAD_X, HEAD_W = 0.80, 2.45      # 행머리글
BODY_X, BODY_W = 3.45, 9.08      # 행 본문
NAVYBAND = (1.23, 6.29, 10.84, 0.50)
FOOTNOTE = (0.80, 7.02, 11.73, 0.33)
COL2 = ((0.80, 5.66), (6.87, 5.66))          # (x, w) 두 열 — 간격 0.41
COL3 = ((0.80, 3.71), (4.81, 3.71), (8.82, 3.71))   # 세 열 — 간격 0.30
SIZES = (27.5, 22.5, 13.0, 12.5, 12.0, 11.5, 10.5)  # 표준 생성 요소 기본 크기. 표지·구분 장·도식·큰 수치는 승인 예외 가능
FONT = ('<a:latin typeface="Pretendard" pitchFamily="34" charset="0"/>'
        '<a:ea typeface="Pretendard" pitchFamily="34" charset="-122"/>'
        '<a:cs typeface="Pretendard" pitchFamily="34" charset="-120"/>')
 
def emu(v): return str(int(round(v * E)))
 
def rpr(sz, color, bold=False, spc=None):
    b = ' b="1"' if bold else ''
    s = f' spc="{spc}"' if spc else ''
    return (f'<a:rPr lang="ko-KR" altLang="en-US" sz="{int(sz*100)}"{b}{s} dirty="0">'
            f'<a:solidFill><a:srgbClr val="{color}"/></a:solidFill>{FONT}</a:rPr>')
 
def run(text, sz, color, bold=False, spc=None):
    return f'<a:r>{rpr(sz, color, bold, spc)}<a:t>{escape(text)}</a:t></a:r>'
 
def para(runs, align=None, lnspc=118, spcaft=None):
    al = f' algn="{align}"' if align else ''
    ls = f'<a:lnSpc><a:spcPct val="{lnspc*1000}"/></a:lnSpc>' if lnspc else ''
    sa = f'<a:spcAft><a:spcPts val="{spcaft*100}"/></a:spcAft>' if spcaft else ''
    return f'<a:p><a:pPr marL="0" indent="0"{al}>{ls}{sa}<a:buNone/></a:pPr>{"".join(runs)}</a:p>'
 
def sp_text(id_, name, x, y, w, h, paras, anchor="ctr"):
    """paras: list of para() strings"""
    return (f'<p:sp><p:nvSpPr><p:cNvPr id="{id_}" name="{name}"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="{emu(x)}" y="{emu(y)}"/><a:ext cx="{emu(w)}" cy="{emu(h)}"/></a:xfrm>'
            f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/><a:ln/></p:spPr>'
            f'<p:txBody><a:bodyPr wrap="square" lIns="0" tIns="0" rIns="0" bIns="0" rtlCol="0" anchor="{anchor}"/>'
            f'<a:lstStyle/>{"".join(paras)}</p:txBody></p:sp>')
 
def sp_rect(id_, name, x, y, w, h, fill):
    return (f'<p:sp><p:nvSpPr><p:cNvPr id="{id_}" name="{name}"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="{emu(x)}" y="{emu(y)}"/><a:ext cx="{emu(w)}" cy="{emu(h)}"/></a:xfrm>'
            f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:solidFill><a:srgbClr val="{fill}"/></a:solidFill><a:ln/></p:spPr></p:sp>')
 
def sp_line(id_, name, x, y, w, color="DCE0E8", wpt=0.75):
    return (f'<p:sp><p:nvSpPr><p:cNvPr id="{id_}" name="{name}"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="{emu(x)}" y="{emu(y)}"/><a:ext cx="{emu(w)}" cy="0"/></a:xfrm>'
            f'<a:prstGeom prst="line"><a:avLst/></a:prstGeom><a:ln w="{int(wpt*12700)}"><a:solidFill><a:srgbClr val="{color}"/></a:solidFill></a:ln></p:spPr>'
            f'<p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:endParaRPr lang="ko-KR"/></a:p></p:txBody></p:sp>')
 
# ---------- editing existing ----------
SP_RE = re.compile(r'<p:(?:sp|cxnSp)>.*?</p:(?:sp|cxnSp)>', re.S)
 
def shapes(xml):
    return list(SP_RE.finditer(xml))
 
def find_shape(xml, id_=None, name=None, contains=None):
    """returns match object of the first shape satisfying all given criteria"""
    for m in shapes(xml):
        s = m.group(0)
        if id_ is not None and not re.search(rf'<p:cNvPr id="{id_}" ', s): continue
        if name is not None and f'name="{name}"' not in s: continue
        if contains is not None and contains not in ''.join(re.findall(r'<a:t>([^<]*)</a:t>', s)): continue
        return m
    raise KeyError(f'shape not found id={id_} name={name} contains={contains!r}')
 
def sid(shape_xml):
    return int(re.search(r'<p:cNvPr id="(\d+)"', shape_xml).group(1))
 
def base_rpr(shape_xml):
    m = re.search(r'<a:rPr[^>]*>.*?</a:rPr>|<a:rPr[^>]*/>', shape_xml, re.S)
    return m.group(0) if m else None
 
def replace_paragraphs(shape_xml, paras):
    """replace entire paragraph list inside txBody"""
    return re.sub(r'(<a:lstStyle/>).*?(</p:txBody>)', lambda m: m.group(1) + ''.join(paras) + m.group(2), shape_xml, count=1, flags=re.S)
 
def set_text(xml, runs_spec, id_=None, name=None, contains=None, align=None, lnspc=None, spcaft=None, sz=None):
    """runs_spec: list of (text, opts) with opts keys bold/color/sz ; or a plain string
    keeps the first run's font size / color unless overridden; keeps first pPr (align/lnSpc) unless given"""
    m = find_shape(xml, id_, name, contains)
    s = m.group(0)
    b = base_rpr(s)
    bsz = int(re.search(r'sz="(\d+)"', b).group(1)) / 100 if b and 'sz=' in b else 12
    bcol = re.search(r'srgbClr val="([0-9A-Fa-f]{6})"', b)
    bcol = bcol.group(1) if bcol else '222633'
    bbold = 'b="1"' in b if b else False
    ppr = re.search(r'<a:pPr[^>]*>.*?</a:pPr>|<a:pPr[^>]*/>', s, re.S)
    ppr = ppr.group(0) if ppr else '<a:pPr marL="0" indent="0"><a:buNone/></a:pPr>'
    if align is not None:
        ppr = re.sub(r' algn="[^"]*"', '', ppr)
        ppr = ppr.replace('<a:pPr', f'<a:pPr algn="{align}"', 1)
    if lnspc is not None:
        ppr = re.sub(r'<a:lnSpc>.*?</a:lnSpc>', '', ppr)
        ppr = re.sub(r'(<a:pPr[^>]*>)', rf'\1<a:lnSpc><a:spcPct val="{lnspc*1000}"/></a:lnSpc>', ppr, 1)
        ppr = ppr.replace('/>', '></a:pPr>', 1) if ppr.endswith('/>') else ppr
    if spcaft is not None:
        ppr = re.sub(r'<a:spcAft>.*?</a:spcAft>', '', ppr)
        if '</a:pPr>' not in ppr: ppr = ppr[:-2] + '></a:pPr>'
        # insert after lnSpc if present else at start
        if '</a:lnSpc>' in ppr:
            ppr = ppr.replace('</a:lnSpc>', f'</a:lnSpc><a:spcAft><a:spcPts val="{spcaft*100}"/></a:spcAft>', 1)
        else:
            ppr = re.sub(r'(<a:pPr[^>]*>)', rf'\1<a:spcAft><a:spcPts val="{spcaft*100}"/></a:spcAft>', ppr, 1)
    if isinstance(runs_spec, str):
        runs_spec = [(runs_spec, {})]
    # allow multiple paragraphs: list of lists
    if runs_spec and isinstance(runs_spec[0], list):
        paras = []
        for pr in runs_spec:
            rs = [run(t, o.get('sz', sz or bsz), o.get('color', bcol), o.get('bold', bbold)) for t, o in pr]
            paras.append(f'<a:p>{ppr}{"".join(rs)}</a:p>')
    else:
        rs = [run(t, o.get('sz', sz or bsz), o.get('color', bcol), o.get('bold', bbold)) for t, o in runs_spec]
        paras = [f'<a:p>{ppr}{"".join(rs)}</a:p>']
    new = replace_paragraphs(s, paras)
    return xml[:m.start()] + new + xml[m.end():]
 
def move_shape(xml, dy=0, dx=0, id_=None, name=None, contains=None):
    m = find_shape(xml, id_, name, contains)
    s = m.group(0)
    def rep(mm):
        return f'<a:off x="{int(mm.group(1)) + int(dx*E)}" y="{int(mm.group(2)) + int(dy*E)}"/>'
    s2 = re.sub(r'<a:off x="(\d+)" y="(\d+)"/>', rep, s, count=1)
    return xml[:m.start()] + s2 + xml[m.end():]
 
def resize_shape(xml, h=None, w=None, id_=None, name=None, contains=None):
    m = find_shape(xml, id_, name, contains)
    s = m.group(0)
    def rep(mm):
        cx = emu(w) if w is not None else mm.group(1)
        cy = emu(h) if h is not None else mm.group(2)
        return f'<a:ext cx="{cx}" cy="{cy}"/>'
    s2 = re.sub(r'<a:ext cx="(\d+)" cy="(\d+)"/>', rep, s, count=1)
    return xml[:m.start()] + s2 + xml[m.end():]
 
def remove_shape(xml, id_=None, name=None, contains=None):
    m = find_shape(xml, id_, name, contains)
    return xml[:m.start()] + xml[m.end():]
 
def max_id(xml):
    return max(int(i) for i in re.findall(r'<p:cNvPr id="(\d+)"', xml))
 
def append_shapes(xml, shape_xmls):
    return xml.replace('</p:spTree>', ''.join(shape_xmls) + '</p:spTree>', 1)
 
def replace_body(xml, keep_ids, new_shapes):
    """remove all shapes not in keep_ids, then append new shapes"""
    def rep(m):
        return m.group(0) if sid(m.group(0)) in keep_ids else ''
    xml = SP_RE.sub(rep, xml)
    return append_shapes(xml, new_shapes)
 
def add_next_cue(xml, text):
    """우상단 연결 단서. 좌표·색은 §1-1·§1-3 고정값."""
    nid = max_id(xml) + 1
    p = para([run(text, 10.5, FOOT)], align='r', lnspc=118)
    x, y, w, h = CUE
    return append_shapes(xml, [sp_text(nid, 'NEXT', x, y, w, h, [p])])
 
# ---------- notes ----------
NOTES_TMPL = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:notes xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"><p:cSld><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr><p:sp><p:nvSpPr><p:cNvPr id="2" name="Slide Image Placeholder 1"/><p:cNvSpPr><a:spLocks noGrp="1" noRot="1" noChangeAspect="1"/></p:cNvSpPr><p:nvPr><p:ph type="sldImg"/></p:nvPr></p:nvSpPr><p:spPr/></p:sp><p:sp><p:nvSpPr><p:cNvPr id="3" name="Notes Placeholder 2"/><p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr><p:nvPr><p:ph type="body" idx="1"/></p:nvPr></p:nvSpPr><p:spPr/><p:txBody><a:bodyPr/><a:lstStyle/>{PARAS}</p:txBody></p:sp><p:sp><p:nvSpPr><p:cNvPr id="4" name="Slide Number Placeholder 3"/><p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr><p:nvPr><p:ph type="sldNum" sz="quarter" idx="10"/></p:nvPr></p:nvSpPr><p:spPr/><p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:fld id="{F7021451-1387-4CA6-816F-3879F97B5CBC}" type="slidenum"><a:rPr lang="en-US"/><a:t>{NUM}</a:t></a:fld><a:endParaRPr lang="en-US"/></a:p></p:txBody></p:sp></p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:notes>'''
NOTES_RELS = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="../slides/slide{N}.xml"/><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/notesMaster" Target="../notesMasters/notesMaster1.xml"/></Relationships>'''
 
def notes_paras(lines):
    out = []
    for ln in lines:
        if ln == '':
            out.append('<a:p><a:endParaRPr lang="ko-KR"/></a:p>')
        else:
            bold = ln.startswith('**')
            t = ln.strip('*')
            b = ' b="1"' if bold else ''
            out.append(f'<a:p><a:r><a:rPr lang="ko-KR" altLang="en-US"{b} dirty="0"/><a:t>{escape(t)}</a:t></a:r></a:p>')
    return ''.join(out)
 
def notes_backref_check(root, n_slides):
    """각 notesSlide가 자기 슬라이드를 역참조하는지 전수 확인 (§7 18항).
    불일치가 있으면 [(노트번호, 실제로 가리키는 슬라이드번호)] 를 돌려준다.
    LibreOffice 렌더와 validate.py는 이 불일치를 잡지 못하고 PowerPoint만 거부한다."""
    bad = []
    for i in range(1, n_slides + 1):
        p = f'{root}/ppt/notesSlides/_rels/notesSlide{i}.xml.rels'
        if not os.path.exists(p):
            continue
        r = open(p, encoding='utf-8').read()
        m = re.search(r'slides/slide(\d+)\.xml', r)
        if not m or int(m.group(1)) != i:
            bad.append((i, int(m.group(1)) if m else None))
    return bad


def fix_notes_backrefs(root, n_slides):
    """절대(/ppt/slides/slideN.xml)·상대(../slides/slideN.xml) 어느 형식이든
    자기 슬라이드를 가리키도록 고친다."""
    fixed = 0
    for i in range(1, n_slides + 1):
        p = f'{root}/ppt/notesSlides/_rels/notesSlide{i}.xml.rels'
        if not os.path.exists(p):
            continue
        r = open(p, encoding='utf-8').read()
        r2 = re.sub(r'Target="(?:\.\./|/ppt/)slides/slide\d+\.xml"',
                    f'Target="/ppt/slides/slide{i}.xml"', r)
        if r2 != r:
            open(p, 'w', encoding='utf-8').write(r2)
            fixed += 1
    return fixed


def write_notes(root, slide_n, page_n, lines):
    nfile = f'{root}/ppt/notesSlides/notesSlide{slide_n}.xml'
    rels = f'{root}/ppt/slides/_rels/slide{slide_n}.xml.rels'
    r = open(rels, encoding='utf-8').read()
    if 'notesSlide' not in r:
        r = r.replace('</Relationships>', f'<Relationship Id="rId9" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/notesSlide" Target="../notesSlides/notesSlide{slide_n}.xml"/></Relationships>')
        open(rels, 'w', encoding='utf-8').write(r)
        open(f'{root}/ppt/notesSlides/_rels/notesSlide{slide_n}.xml.rels', 'w', encoding='utf-8').write(NOTES_RELS.replace('{N}', str(slide_n)))
        ct = open(f'{root}/[Content_Types].xml', encoding='utf-8').read()
        if f'notesSlide{slide_n}.xml' not in ct:
            ct = ct.replace('</Types>', f'<Override PartName="/ppt/notesSlides/notesSlide{slide_n}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.notesSlide+xml"/></Types>')
            open(f'{root}/[Content_Types].xml', 'w', encoding='utf-8').write(ct)
    open(nfile, 'w', encoding='utf-8').write(NOTES_TMPL.replace('{PARAS}', notes_paras(lines)).replace('{NUM}', str(page_n)))

# ============================================================
# 골격 생성 — 제작 지침 5판 §1·§3
# 좌표를 직접 계산하지 말고 아래 함수를 쓴다.
# ============================================================

def slide_frame(next_id, kicker, title, cue=None, chip=None,
                band=None, band_sub=None, band_kind='top'):
    """한 장의 골격(키커·단서·제목·칩·밴드·남색 선)을 만든다.

    band_kind='top'  선언형 결론 → 상단 회색 밴드
    band_kind='bottom' 의문형 → 하단 남색 밴드
    band_kind=None   밴드 없음

    돌려주는 값: (도형 리스트, 다음 id, 본문 시작 y, 본문 끝 y)
    본문 끝 y는 각주가 있다고 보고 계산한다. 각주가 없으면 +0.35 해서 쓴다.
    """
    sid = next_id
    out = []
    x, y, w, h = KICKER
    out.append(sp_text(sid, 'KICKER', x, y, w, h,
                       [para([run(kicker, 12.5, SUB, bold=True, spc=200)])])); sid += 1
    if cue:
        x, y, w, h = CUE
        out.append(sp_text(sid, 'NEXT', x, y, w, h,
                           [para([run('다음 → ' + cue, 10.5, FOOT)], align='r')])); sid += 1
    x, y, w, h = TITLE
    if chip:
        w = 5.70                      # 칩이 있는 장은 제목 폭을 줄여 판정한다
    out.append(sp_text(sid, 'TITLE', x, y, w, h,
                       [para([run(title, 27.5, NAVY, bold=True)])])); sid += 1
    if chip:
        x, y, w, h = CHIP
        out.append(sp_text(sid, 'CHIP', x, y, w, h,
                           [para([run(chip, 13.0, GOLD, bold=True)], align='r')])); sid += 1

    if band_kind == 'top' and band:
        bh = 0.60 if not band_sub else 0.85
        bx, by, bw = BAND_BG
        out.append(sp_rect(sid, 'BANDBG', bx, by, bw, bh, BAND)); sid += 1
        ps = [para([run(band, 13.0, NAVY, bold=True)])]
        if band_sub:
            ps.append(para([run('— ' + band_sub, 11.5, SUB)]))
        tx, ty, tw = BAND_TX
        out.append(sp_text(sid, 'BANDTX', tx, ty, tw, bh, ps)); sid += 1
        ruley = by + bh + 0.10
    else:
        ruley = 1.52
    out.append(sp_line(sid, 'RULE', M_L, ruley, M_W, NAVY, 1.5)); sid += 1

    body_top = ruley + 0.20
    if band_kind == 'bottom' and band:
        nx, ny, nw, nh = NAVYBAND
        out.append(sp_rect(sid, 'NAVYBG', nx, ny, nw, nh, NAVY)); sid += 1
        out.append(sp_text(sid, 'NAVYTX', nx + 0.20, ny + 0.03, nw - 0.40, nh - 0.06,
                           [para([run(band, 12.5, WHITE, bold=True)], align='ctr')])); sid += 1
        body_bot = ny - 0.19
    else:
        body_bot = 6.72
    return out, sid, body_top, body_bot


def row(next_id, y, head, conclusion, supplements=(), limit=None,
        result=False, head_x=None, head_w=None, body_x=None, body_w=None,
        rule=True):
    """레거시 행 함수. 신규 제작에 사용하지 않는다.

    문자 수로 줄 수를 어림하므로 §7-4 ①의 실측 규칙과 맞지 않는다.
    신규 제작은 layout.layout_rows()를 사용한다.

    한 행 = 행머리글 + 결론 줄 + 보충 줄 (+ 금색 한정 줄).

    head        2~12자 명사구. 날짜·사건번호·표본 수는 여기 두지 않는다.
    conclusion  한 문장 40자 이내. 결과·판단 행이면 result=True로 한 급 올린다.
    supplements 보충 줄(문자열 리스트)
    limit       금색 한정 줄 — 이 자료로 말할 수 없는 것

    돌려주는 값: (도형 리스트, 다음 id, 다음 행의 y)
    """
    sid = next_id
    hx = HEAD_X if head_x is None else head_x
    hw = HEAD_W if head_w is None else head_w
    bx = BODY_X if body_x is None else body_x
    bw = BODY_W if body_w is None else body_w
    out = []
    if rule:
        out.append(sp_line(sid, f'RULE{sid}', M_L, y, M_W, LINE, 0.75)); sid += 1

    csz = 13.0 if result else 12.5
    ps = [para([run(conclusion, csz, INK, bold=True)],
               lnspc=125 if len(conclusion) > 50 else 118, spcaft=5)]
    for s in supplements:
        ps.append(para([run(s, 11.5, SUB)], lnspc=125 if len(s) > 55 else 118, spcaft=5))
    if limit:
        ps.append(para([run(limit, 12.0, GOLD)], lnspc=125 if len(limit) > 52 else 118))

    lines = 1 + sum(max(1, len(s) // 55 + 1) for s in supplements) + (1 if limit else 0)
    h = lines * 0.245 + 0.16                      # 상자 높이 = 내용 + 0.16 (§0-8)
    out.append(sp_text(sid, f'HEAD{sid}', hx, y + 0.06, hw, h - 0.06,
                       [para([run(head, 13.0, NAVY, bold=True)])], anchor='t')); sid += 1
    out.append(sp_text(sid, f'BODY{sid}', bx, y + 0.06, bw, h - 0.06, ps, anchor='t')); sid += 1
    return out, sid, y + h


def footnote(next_id, text):
    x, y, w, h = FOOTNOTE
    return [sp_text(next_id, 'FOOT', x, y, w, h,
                    [para([run(text, 10.5, FOOT)])])], next_id + 1


def audit(root, n_slides):
    """§7 점검표 가운데 파일에서 셀 수 있는 항목을 한 번에 확인한다."""
    import collections
    bad_color, sizes, spc, geoms, oob, pagenum = collections.Counter(), set(), set(), collections.Counter(), [], 0
    for i in range(1, n_slides + 1):
        s = open(f'{root}/ppt/slides/slide{i}.xml', encoding='utf-8').read()
        # 빈 단락의 endParaRPr에는 PowerPoint가 비가시 기본 검정(000000)을 넣을 수 있다.
        # 그 기본값만 제외하고, 실제 가시 텍스트/도형의 000000은 팔레트 밖 색으로 잡는다.
        visible = re.sub(r'<a:endParaRPr\\b.*?</a:endParaRPr>|<a:endParaRPr\\b[^>]*/>', '', s, flags=re.S)
        for c in re.findall(r'srgbClr val="([0-9A-Fa-f]{6})"', visible):
            if c.upper() not in PALETTE:
                bad_color[c.upper()] += 1
        sizes.update(int(v) / 100 for v in re.findall(r'sz="(\d+)"', s))
        spc.update(re.findall(r'spcPct val="(\d+)"', s))
        geoms.update(re.findall(r'prstGeom prst="(\w+)"', s))
        if 'normAutofit' in s:
            pagenum += 1
        for m in re.finditer(r'<a:off x="(-?\d+)" y="(-?\d+)"/><a:ext cx="(\d+)" cy="(\d+)"', s):
            x, y, cx, cy = (int(v) / E for v in m.groups())
            if x + cx > 13.36 or y + cy > 7.55:
                oob.append(i)
    return {
        '팔레트 밖 색': dict(bad_color),
        '글자 크기': sorted(sizes),
        '줄간격': sorted(spc),
        '도형': dict(geoms),
        '경계 이탈 장': sorted(set(oob)),
        'normAutofit 장수': pagenum,
        '노트 역참조 불일치': notes_backref_check(root, n_slides),
    }