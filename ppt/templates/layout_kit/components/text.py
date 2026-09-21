"""글 부품: 열 머리, 항목 목록, 번호 목록, 정의 줄, 안내 줄, 3열 기준, 대조 목록, 쟁점 목록, 목차"""
from core import *

def header(s,b,title,sub=None,bar=NAVY_F,tcol=NAVY,pt=None):
    """열 머리: 위쪽 막대 + 제목(+ 보조 줄). 머리 아래 남은 영역을 돌려준다."""
    pt=pt or SZ['head']
    rect(s,b.x,b.y,b.w,0.05,bar)
    T(s,b.x,b.y+0.13,b.w,title,pt,tcol,True)
    y=b.y+0.13+lh(pt,118)
    if sub: T(s,b.x,y+0.04,b.w,sub,11,FOOT); y+=0.04+lh(11,118)
    return b.below(y,0.16)

def meta(s,b,label,text,pt=12):
    """'평가 대상  ···' 같은 한 줄 안내. 아래 남은 영역을 돌려준다."""
    tb(s,b.x,b.y,b.w,0.28,[([R(label+'   ',pt,GOLD_T,True),R(text,pt,SUB)],118,None)])
    return b.below(b.y+lh(pt,118),0.12)

def note(s,b,text,pt=11,col=FOOT,bold=False):
    """한 줄(또는 여러 줄) 글. 아래 남은 영역을 돌려준다."""
    h=T(s,b.x,b.y,b.w,text,pt,col,bold); return b.below(b.y+h,0.08)

def def_lines(s,b,defs,pt=12):
    """용어 정의 줄: [(용어, 설명)]"""
    y=b.y
    for term,desc in defs:
        h=n_lines(term+'  '+desc,pt,b.w)*lh(pt,125 if n_lines(term+'  '+desc,pt,b.w)>1 else 118)
        tb(s,b.x,y,b.w,h+0.04,[([R(term+'   ',pt,NAVY,True),R(desc,pt,SUB)],125 if h>0.3 else 118,None)])
        y+=h+0.07
    return b.below(y,0.06)

def items(s,b,its,pt=None,col=INK,gap=0.14,tail=None,rules=False,spread=False):
    """항목 목록. tail: 목록 끝 금색 강조 줄. spread=True면 영역 높이에 고르게 퍼뜨린다."""
    pt=pt or SZ['supp']
    hs=[n_lines(t,pt,b.w)*lh(pt,125 if n_lines(t,pt,b.w)>1 else 118) for t in its]
    th=lh(pt,118)+0.06 if tail else 0
    if spread:
        pad=max(0.06,(b.h-th-sum(hs))/(2*len(its)))
    else: pad=gap/2
    y=b.y
    for k,(t,h) in enumerate(zip(its,hs)):
        if rules and k: hline(s,b.x,y,b.w)
        tb(s,b.x,y+pad-0.035,b.w,h+0.05,[([R(t,pt,col)],125 if h>lh(pt,118)+0.01 else 118,None)])
        y+=h+2*pad
    if tail: T(s,b.x,y+0.02,b.w,tail,pt,GOLD_T,True); y+=th
    warn_fit('items',y-b.y,b.h)
    return y

def numbered(s,b,its,hot=None,title_pt=13.5,desc_pt=12,dot=True):
    """번호 목록: [(제목, 설명)]. 영역 높이에 고르게 퍼뜨리고 사이에 선을 둔다."""
    n=len(its); rh=b.h/n
    for i,(a,d) in enumerate(its):
        y=b.y+i*rh; h=lh(title_pt,118)+(0.04+n_lines(d,desc_pt,b.w-0.42)*lh(desc_pt,118) if d else 0)
        if i: hline(s,b.x,y,b.w)
        ty=y+(rh-h)/2
        hc=GOLD_F if hot==i else NAVY
        rect(s,b.x,ty+0.01,0.28,0.28,hc,None,shape=MSO_SHAPE.OVAL)
        tb(s,b.x,ty+0.01,0.28,0.28,[([R(str(i+1),11.5,WHITE,True)],100,None)],anchor='m',align='c',autofit=False)
        ps=[([R(a,title_pt,GOLD_T if hot==i else INK,True)],118,3)]
        if d: ps.append(([R(d,desc_pt,SUB)],118,None))
        tb(s,b.x+0.42,ty-0.02,b.w-0.42,h+0.08,ps)
        warn_fit('numbered 행',h+0.1,rh)
    return b.b

def grid(s,b,its,cols=2,gap=0.30,title_pt=13,desc_pt=12):
    """번호 격자: [(제목, 설명)] → cols열"""
    rows=(len(its)+cols-1)//cols; gw=(b.w-gap*(cols-1))/cols; gh=b.h/rows
    for k,(a,d) in enumerate(its):
        x=b.x+(k%cols)*(gw+gap); y=b.y+(k//cols)*gh
        if k//cols: hline(s,x,y-0.08,gw)
        rect(s,x,y,0.28,0.28,NAVY,None,shape=MSO_SHAPE.OVAL)
        tb(s,x,y,0.28,0.28,[([R(str(k+1),11.5,WHITE,True)],100,None)],anchor='m',align='c',autofit=False)
        tb(s,x+0.40,y-0.02,gw-0.40,gh-0.1,[([R(a,title_pt,INK,True)],118,4),([R(d,desc_pt,SUB)],125,None)])
    return b.b

def cols3(s,b,cols,main_pt=16,gap=None):
    """기준 열: [(라벨, 핵심, [보충])] → 열마다 위쪽 막대 + 라벨 + 핵심 + 보충"""
    n=len(cols); gap=gap if gap is not None else (0.44 if n==3 else 0.41)
    cw=(b.w-gap*(n-1))/n; ends=[]
    for i,(lab,m,subs) in enumerate(cols):
        x=b.x+i*(cw+gap); rect(s,x,b.y,cw,0.05,NAVY_F)
        T(s,x,b.y+0.14,cw,lab,12.5,SUB,True)
        ps,h=body_block(m,subs,w=cw,cz=main_pt); tb(s,x,b.y+0.46,cw,h+0.1,ps)
        ends.append(b.y+0.46+h)
    return max(ends)

def aligned_lists(s,b,heads,cols_items,pt=12.5):
    """좌우 대조 목록. heads=[(제목, 막대색, 표시 개수 또는 None)], cols_items=[[항목…],[항목…]]
    같은 번째 항목끼리 높이를 맞춘다."""
    n=len(heads); gap=0.41; cw=(b.w-gap*(n-1))/n; xs=[b.x+i*(cw+gap) for i in range(n)]
    for c,(h,col,cnt) in enumerate(heads):
        rect(s,xs[c],b.y,cw,0.05,col); off=0
        if cnt:
            for k in range(cnt): rect(s,xs[c]+k*0.24,b.y+0.19,0.16,0.16,col)
            off=cnt*0.24+0.10
        T(s,xs[c]+off,b.y+0.13,cw-off,h,SZ['head'],NAVY,True)
    m=max(len(ci) for ci in cols_items)
    hs=[max(n_lines(ci[k],pt,cw)*lh(pt,125) for ci in cols_items if k<len(ci)) for k in range(m)]
    top=b.y+0.52; pad=(b.b-top-sum(hs))/(2*m); warn_fit('aligned_lists',top+sum(hs)+0.2*m-b.y,b.h)
    pad=max(pad,0.08); y=top
    for k in range(m):
        if k:
            for c in range(n): hline(s,xs[c],y,cw)
        for c in range(n):
            if k<len(cols_items[c]):
                t=cols_items[c][k]; nl=n_lines(t,pt,cw)
                tb(s,xs[c],y+pad-0.035,cw,hs[k]+0.05,[([R(t,pt,INK)],125 if nl>1 else 118,None)])
        y+=hs[k]+2*pad
    return y

def issue_list(s,b,its,name_w=3.55,pt=13.5):
    """쟁점 목록: [(쟁점명, 질문)] → 번호 원 + 쟁점명 + 질문, 행 높이 고르게"""
    qx=b.x+name_w+0.5; qw=b.r-qx
    def hh(t,w,bold): nl=n_lines(t,pt,w,bold); return nl*lh(pt,125 if nl>1 else 118)
    hs=[max(hh(a,name_w-0.55,True),hh(q,qw,False)) for a,q in its]
    pad=(b.h-sum(hs))/(2*len(its)); warn_fit('issue_list',sum(hs)+0.2*len(its),b.h)
    y=b.y
    for k,((a,q),h) in enumerate(zip(its,hs)):
        if k: hline(s,b.x,y,b.w)
        cy=y+pad+h/2
        rect(s,b.x+0.02,cy-0.16,0.32,0.32,NAVY,None,shape=MSO_SHAPE.OVAL)
        tb(s,b.x+0.02,cy-0.16,0.32,0.32,[([R(str(k+1),12.5,WHITE,True)],100,None)],anchor='m',align='c',autofit=False)
        tb(s,b.x+0.55,y+pad-0.035,name_w-0.55,h+0.05,[([R(a,pt,NAVY,True)],125 if hh(a,name_w-0.55,True)>0.3 else 118,None)],anchor='m')
        tb(s,qx,y+pad-0.035,qw,h+0.05,[([R(q,pt,INK)],125 if hh(q,qw,False)>0.3 else 118,None)],anchor='m')
        y+=h+2*pad
    return y

def toc(s,b,its,name_w=4.4):
    """목차: [(단원명, 다루는 것)]"""
    rh=b.h/len(its)
    for k,(a,d) in enumerate(its):
        y=b.y+k*rh
        if k: hline(s,b.x,y,b.w)
        tb(s,b.x,y,0.6,rh,[([R(str(k+1),22,GOLD_F,True)],118,None)],anchor='m',autofit=False)
        tb(s,b.x+0.65,y,name_w,rh,[([R(a,15,NAVY,True)],118,None)],anchor='m')
        tb(s,b.x+4.95,y,b.w-4.95,rh,[([R(d,13,SUB)],118,None)],anchor='m')
    return b.b
