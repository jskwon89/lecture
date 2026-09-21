"""글자 맞춤: 어절 단위 줄바꿈 실측 + 끝줄 한두 글자(고아 줄) 방지"""
from rowfit import _font
_S=4
def _w(s,pt,bold,spc=0.0):
    return _font(pt,bold).getlength(s)/_S/96.0 + len(s)*spc/72.0

def wrap(s,pt,w,bold=False,spc=0.0):
    """PowerPoint 한글 기본값처럼 어절(공백) 단위로 줄을 나눈다. 한 어절이 폭보다 길면 글자 단위."""
    w=w*SAFE
    words=s.split(' '); lines=[]; cur=''
    for wd in words:
        cand=wd if not cur else cur+' '+wd
        if _w(cand,pt,bold,spc)<=w: cur=cand; continue
        if cur: lines.append(cur); cur=''
        if _w(wd,pt,bold,spc)<=w: cur=wd; continue
        piece=''
        for ch in wd:
            if _w(piece+ch,pt,bold,spc)>w: lines.append(piece); piece=ch
            else: piece+=ch
        cur=piece
    lines.append(cur)
    return lines

SAFE=0.97             # 렌더러 차이를 감안한 폭 여유
ORPHAN_CHARS=4          # 끝줄이 이 글자 수 이하이면 고아 줄로 본다(공백·기호 제외)
ORPHAN_RATIO=0.18       # 또는 끝줄 폭이 상자 폭의 18% 미만
def is_orphan(lines,pt,w,bold,spc):
    if len(lines)<2: return False
    last=lines[-1]; core=[c for c in last if c not in ' .,·)」』]']
    return len(core)<=ORPHAN_CHARS or _w(last,pt,bold,spc)<w*ORPHAN_RATIO

SPC_STEPS=[0.0,-0.3,-0.6]     # 자간(pt) 조정 한도
SIZE_STEPS=[0.0,-0.5,-1.0]    # 글자 크기 조정 한도
def fit(s,pt,w,bold=False,allow_size=False):
    """반환: (pt, spc, width, lines, how). how = ''|'spc'|'size'|'balance'"""
    base=wrap(s,pt,w,bold)
    if not is_orphan(base,pt,w,bold,0): return pt,0.0,w,base,''
    # 1) 자간 → 2) 크기 순으로 줄 수를 하나 줄여 본다
    for dz in (SIZE_STEPS if allow_size else [0.0]):
        for sp in SPC_STEPS:
            if dz==0 and sp==0: continue
            ln=wrap(s,pt+dz,w,bold,sp)
            if len(ln)<len(base) and not is_orphan(ln,pt+dz,w,bold,sp):
                return pt+dz,sp,w,ln,('size' if dz else 'spc')
    # 3) 줄 수를 줄일 수 없으면 상자 폭을 좁혀 줄 길이를 고르게 나눈다
    best=None; ww=w
    while ww>w*0.80:
        ww-=0.04
        ln=wrap(s,pt,ww,bold)
        if len(ln)>len(base): break
        if not is_orphan(ln,pt,w,bold,0): best=(ww,ln)
    if best: return pt,0.0,best[0],best[1],'balance'
    # 4) 마지막으로 글자 크기를 0.5pt 줄여 본다
    for sp in SPC_STEPS:
        ln=wrap(s,pt-0.5,w,bold,sp)
        if len(ln)<len(base) and not is_orphan(ln,pt-0.5,w,bold,sp):
            return pt-0.5,sp,w,ln,'size'
    return pt,0.0,w,base,'orphan-left'
