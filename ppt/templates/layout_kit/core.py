"""양식 키트 공통 도구 — python-pptx 기반

ppt/tools/의 rowfit.py·pptlib.py를 그대로 불러 쓴다(복사본을 두지 않는다)."""
import os, sys
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
sys.path.insert(0, HERE)
import re
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from lxml import etree
from design import *
from rowfit import lh, text_w
from fit import wrap, fit
FITLOG=[]
def n_lines(t,pt,w,bold=False): return len(fit(t,pt,w,bold)[3])

prs=Presentation(); prs.slide_width=Inches(13.333); prs.slide_height=Inches(7.5)
BL=prs.slide_layouts[6]
LOG=[]

def R(t,pt,col,bold=False,hl=None,spc=0.0): return (t,pt,col,bold,hl,spc)
def rich(text,pt,col,bold):
    out=[]
    for part in re.split(r'(«[^»]+»)',text):
        if not part: continue
        out.append(R(part[1:-1] if part.startswith('«') else part,pt,col,bold))
    return out
def plain(t): return re.sub(r'[«»]','',t)

def _font(r,pt,color,bold,hl,spc=0.0):
    r.font.size=Pt(pt); r.font.bold=bold; r.font.color.rgb=RGBColor.from_string(color)
    rPr=r._r.get_or_add_rPr()
    if spc: rPr.set('spc',str(int(round(spc*100))))
    if hl:
        h=etree.Element(qn('a:highlight')); c=etree.SubElement(h,qn('a:srgbClr')); c.set('val',hl)
        rPr.insert(1,h)
    for tag in ('a:latin','a:ea','a:cs'):
        e=etree.SubElement(rPr,qn(tag)); e.set('typeface','Pretendard')

def tb(s,x,y,w,h,paras,anchor='t',align='l',autofit=True):
    # 한 가지 서식으로 된 문단은 끝줄 한두 글자를 막도록 자간·크기·줄 길이를 맞춘다
    wmin=w; newp=[]
    for runs,pct,aft in paras:
        if autofit and len(runs)==1 and len(runs[0][0])>6:
            t,pt,col,bold,hl,spc=runs[0]
            npt,nsp,nw,ln,how=fit(t,pt,w,bold)
            if how:
                FITLOG.append(f'{how:12s} {pt}->{npt}pt 자간{nsp:+.1f} 폭{w:.2f}->{nw:.2f} | {t[:30]}')
                if how=='balance': wmin=min(wmin,nw)
            runs=[(t,npt,col,bold,hl,nsp)]
            if len(ln)>1 and pct==118: pct=125
        newp.append((runs,pct,aft))
    paras=newp
    if wmin<w and align=='l': w=wmin
    elif wmin<w and align=='c': x+=(w-wmin)/2; w=wmin
    b=s.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h))
    tf=b.text_frame; tf.word_wrap=True
    for m in ('margin_left','margin_right','margin_top','margin_bottom'): setattr(tf,m,0)
    tf.vertical_anchor={'t':MSO_ANCHOR.TOP,'m':MSO_ANCHOR.MIDDLE,'b':MSO_ANCHOR.BOTTOM}[anchor]
    for i,(runs,pct,aft) in enumerate(paras):
        p=tf.paragraphs[0] if i==0 else tf.add_paragraph()
        p.alignment={'l':PP_ALIGN.LEFT,'c':PP_ALIGN.CENTER,'r':PP_ALIGN.RIGHT}[align]
        p.line_spacing=pct/100
        if aft: p.space_after=Pt(aft)
        for t,pt,col,bold,hl,spc in runs:
            r=p.add_run(); r.text=t; _font(r,pt,col,bold,hl,spc)
    return b
def T(s,x,y,w,text,pt,col,bold=False,align='l',anchor='t',h=None,spc=None):
    nl=n_lines(plain(text),pt,w,bold); pct=125 if nl>1 else 118
    hh=h if h else nl*lh(pt,pct)+0.04
    b=tb(s,x,y,w,hh,[(rich(text,pt,col,bold),pct,None)],anchor=anchor,align=align)
    if spc:
        for r in b.text_frame.paragraphs[0].runs: r._r.get_or_add_rPr().set('spc',str(spc))
    return nl*lh(pt,pct)

def rect(s,x,y,w,h,fill=None,line=None,lw=0.75,shape=MSO_SHAPE.RECTANGLE):
    r=s.shapes.add_shape(shape,Inches(x),Inches(y),Inches(w),Inches(h))
    if fill: r.fill.solid(); r.fill.fore_color.rgb=RGBColor.from_string(fill)
    else: r.fill.background()
    if h<=0.06 and w>0.5: r.name='HBAR'
    if line: r.line.color.rgb=RGBColor.from_string(line); r.line.width=Pt(lw)
    else: r.line.fill.background()
    return r
def hline(s,x,y,w,color=LINE,lw=0.75,dash=False,keep=False):
    c=s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,Inches(x),Inches(y),Inches(x+w),Inches(y))
    c.name=('KEEP' if keep else 'HRULE')
    c.line.color.rgb=RGBColor.from_string(color); c.line.width=Pt(lw); return c
def vline(s,x,y,h,color=LINE,lw=0.75):
    c=s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,Inches(x),Inches(y),Inches(x),Inches(y+h))
    c.line.color.rgb=RGBColor.from_string(color); c.line.width=Pt(lw); return c

def frame(kicker,title,cue=None,cite=None,band=None,band_sub=None,chip=None):
    """cite: 연구자·연도·사건번호. 제목 폭에 들어가면 제목 뒤(보통 굵기)에,
    넘치면 밴드 문장 끝에 괄호로 붙인다. 오른쪽 끝 칩은 쓰지 않는다."""
    cite=cite or chip
    s=prs.slides.add_slide(BL)
    T(s,0.80,0.40,6.0,kicker,SZ['kicker'],SUB,True,spc=200)
    if cue: T(s,6.6,0.42,5.93,'다음 → '+cue,SZ['cue'],FOOT,align='r')
    runs=[R(title,SZ['title'],NAVY,True)]
    if cite:
        suf=(' ('+cite+')') if '—' in title else (' — '+cite)
        if text_w(title,SZ['title'],True)+text_w(suf,SZ['title'],False)<=M_W-0.1:
            runs.append(R(suf,SZ['title'],NAVY,False))
        elif band:
            band=band+' ('+cite+')'
        else:
            LOG.append(f'인용 표기 자리 없음: {title} / {cite}')
    if text_w(title,SZ['title'],True)>M_W: LOG.append(f'제목 폭 초과: {title}')
    tb(s,0.80,0.70,11.73,0.70,[(runs,118,None)],anchor='m')
    if band:
        nl=n_lines(plain(band),SZ['band'],11.1,True)+(n_lines(band_sub,12,11.1) if band_sub else 0)
        bh=0.60 if nl==1 else 0.88
        rect(s,M_L,1.55,M_W,bh,BAND); rect(s,M_L,1.55,0.06,bh,NAVY)
        ps=[(rich(band,SZ['band'],NAVY,True),125 if nl>1 else 118,None)]
        if band_sub: ps.append(([R(band_sub,12,SUB)],118,None))
        tb(s,1.10,1.55,11.2,bh,ps,anchor='m')
        ry=1.55+bh+0.10
    else: ry=1.52
    hline(s,M_L,ry,M_W,NAVY,1.5)
    return s,ry

def foot(s,t): T(s,0.80,FOOT_Y,11.73,t,SZ['foot'],FOOT)
def navyband(s,t):
    rect(s,1.23,6.29,10.84,0.50,NAVY)
    tb(s,1.43,6.29,10.44,0.50,[([R(t,13,WHITE,True)],118,None)],anchor='m',align='c')
def closing(s,text,pad=0.20,pt=None):
    pt=pt or SZ['close']
    nl=n_lines(plain(text),pt,M_W,True); pct=125 if nl>1 else 118; h=nl*lh(pt,pct)
    top=LAST_RULE-h-2*pad
    hline(s,M_L,top,M_W)
    tb(s,M_L,top+pad-0.035,M_W,h+0.05,[(rich(text,pt,NAVY,True),pct,None)])
    hline(s,M_L,LAST_RULE,M_W,NAVY,1.5)
    return top

def body_block(concl,supps=(),limit=None,w=BODY_W,cz=None):
    cz=cz or SZ['concl']
    ps=[];h=0
    specs=[(concl,cz,INK,True)]+[(x,SZ['supp'],SUB,False) for x in supps]
    if limit: specs.append((limit,SZ['limit'],GOLD_T,False))
    for k,(t,pt,col,b) in enumerate(specs):
        nl=n_lines(plain(t),pt,w,b); pct=125 if nl>1 else 118; last=k==len(specs)-1
        gap=PGAP if k==0 else 4
        ps.append((rich(t,pt,col,b),pct,None if last else gap)); h+=nl*lh(pt,pct)+(0 if last else gap/72)
    return ps,h

def dedupe_rules(sl,gap=0.35):
    """내용 없이 붙어 있는 가로선 두 줄 가운데 위의 선을 지운다."""
    E=914400
    lines=[]; texts=[]
    for shp in sl.shapes:
        if shp.name in ('HRULE','HBAR'):
            lines.append((shp.top/E,shp.left/E,(shp.left+shp.width)/E,shp))
        elif shp.has_text_frame and shp.text_frame.text.strip():
            texts.append((shp.top/E,(shp.top+shp.height)/E,shp.left/E,(shp.left+shp.width)/E))
    removed=[]
    for ia,a in enumerate(lines):
        for ib,b in enumerate(lines):
            if a is b: continue
            d=b[0]-a[0]
            if not (0.001<d<gap or (abs(d)<=0.001 and ib<ia)): continue
            if min(a[2],b[2])-max(a[1],b[1])<0.3: continue
            between=abs(d)>0.001 and any(t[0]<b[0]-0.01 and t[1]>a[0]+0.01 and min(t[3],a[2])>max(t[2],a[1]) for t in texts)
            if not between and a[3] not in removed: removed.append(a[3])
    for shp in removed: shp._element.getparent().remove(shp._element)
    return len(removed)

def save(path):
    for k,sl in enumerate(prs.slides,1):
        n=dedupe_rules(sl)
        if n: LOG.append(f'{k:02d}장 겹선 {n}개 제거')
    for sl in prs.slides:
        for shp in sl.shapes:
            st=shp._element.find(qn('p:style'))
            if st is not None: shp._element.remove(st)
    prs.save(path)


# ---------- 영역 ----------
class Box:
    def __init__(s,x,y,w,h): s.x,s.y,s.w,s.h=x,y,w,h
    @property
    def r(s): return s.x+s.w
    @property
    def b(s): return s.y+s.h
    def below(s,y,gap=0.0):
        """y 아래 남은 영역"""
        return Box(s.x,y+gap,s.w,s.b-(y+gap))
    def take(s,h,gap=0.0):
        """위에서 h만큼 떼어 내고 (떼어 낸 영역, 남은 영역)을 돌려준다"""
        return Box(s.x,s.y,s.w,h), Box(s.x,s.y+h+gap,s.w,s.h-h-gap)
    def __repr__(s): return f'Box({s.x:.2f},{s.y:.2f},{s.w:.2f},{s.h:.2f})'

def body(ry,bottom=LAST_RULE,gap=0.20):
    """골격 아래 본문 영역"""
    return Box(M_L,ry+gap,M_W,bottom-ry-gap)

def split_h(b,ratios=(1,1),gap=0.41):
    """좌우로 나눈다. ratios=(6,4) → 60:40"""
    tot=sum(ratios); W=b.w-gap*(len(ratios)-1); out=[]; x=b.x
    for r in ratios:
        w=W*r/tot; out.append(Box(x,b.y,w,b.h)); x+=w+gap
    return out

def split_v(b,parts,gap=0.20):
    """위아래로 나눈다. parts 원소가 1 이하 실수면 비율, 1보다 크면... 모두 비율로 본다"""
    tot=sum(parts); H=b.h-gap*(len(parts)-1); out=[]; y=b.y
    for p in parts:
        h=H*p/tot; out.append(Box(b.x,y,b.w,h)); y+=h+gap
    return out

def warn_fit(name,need,have):
    if need>have+0.02: LOG.append(f'{name}: 영역 부족 필요 {need:.2f} / 가용 {have:.2f}')

def closing2(s,concl,supps=(),limit=None,pad=0.18):
    """마무리 줄(결론 + 보충 + 한정). 윗선 y를 돌려준다."""
    ps,h=body_block(concl,supps,limit,w=M_W,cz=SZ['close'])
    ps[0]=(rich(concl,SZ['close'],NAVY,True),ps[0][1],ps[0][2])
    top=LAST_RULE-h-2*pad
    hline(s,M_L,top,M_W); tb(s,M_L,top+pad-0.035,M_W,h+0.05,ps); hline(s,M_L,LAST_RULE,M_W,NAVY,1.5)
    return top
