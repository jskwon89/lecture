"""그래프 부품: 묶음 세로 막대, 세로 막대, 가로 막대, 진행 막대, 큰 숫자, 전후 수치, 전후 변화 행"""
from core import *

def grouped_bars(s,b,groups,xlabels,highlight=None,vmax=None,fmt=str):
    """묶음 세로 막대 + X축. groups={묶음 이름: [값…]}, xlabels=[연도…]
    highlight: 강조할 x 번호(금색). 영역 폭에 맞춰 막대 폭과 연도 표기(2018/’18)를 정한다."""
    ng=len(groups); nb=len(xlabels); gw=b.w/ng
    slot=gw*0.90/nb; bw=slot*0.82; gap=slot-bw
    full=text_w('2018',9.5)<=slot-0.02
    sparse=(not full) and text_w('’18',9.5)>slot-0.02   # 좁으면 처음·끝·강조 연도만 표기
    base=b.b-0.62; top=b.y+0.30
    vmax=vmax or max(max(v) for v in groups.values())*1.02
    for gi,(g,vals) in enumerate(groups.items()):
        gx=b.x+gi*gw+(gw-(nb*bw+(nb-1)*gap))/2
        for k,v in enumerate(vals):
            h=(base-top)*v/vmax; x=gx+k*(bw+gap); hot=k==highlight
            rect(s,x,base-h,bw,max(h,0.01),GOLD_F if hot else NAVY_F)
            tb(s,x-0.15,base-h-0.23,bw+0.30,0.22,[([R(fmt(v),11.5 if hot else 10.5,GOLD_T if hot else SUB,hot)],118,None)],align='c',autofit=False)
            lab=str(xlabels[k]); lab=lab if full else '’'+lab[-2:]
            if sparse and k not in (0,nb-1,highlight): lab=''
            if lab: tb(s,x-0.08,base+0.05,bw+0.16,0.20,[([R(lab,9.5,GOLD_T if hot else FOOT,hot)],118,None)],align='c',autofit=False)
        tb(s,b.x+gi*gw,base+0.27,gw,0.32,[([R(g,SZ['head'],NAVY,True)],118,None)],align='c')
        if gi: vline(s,b.x+gi*gw,base,0.24,SUB,0.75)
    hline(s,b.x,base,b.w,INK,1.0,keep=True)
    return b.b

def bars(s,b,its,colors=None,unit='%',vmax=None,value_pt=24,label_pt=12.5,max_bw=1.6,axis_note=None):
    """세로 막대(2~5개). its=[(라벨, 값)]. colors 미지정 시 마지막 막대만 남색, 나머지 회색."""
    n=len(its); colors=colors or [GRAYBAR]*(n-1)+[NAVY]
    slot=b.w/n; bw=min(max_bw,slot*0.62)
    nh=0.30 if axis_note else 0
    base=b.b-0.40-nh; top=b.y+lh(value_pt,118)+0.10
    vmax=vmax or max(v for _,v in its)
    for k,(lab,v) in enumerate(its):
        x=b.x+k*slot+(slot-bw)/2; h=(base-top)*v/vmax
        rect(s,x,base-h,bw,h,colors[k])
        tb(s,x-0.3,base-h-lh(value_pt,118)-0.06,bw+0.6,lh(value_pt,118)+0.02,[([R(f'{v:g}{unit}',value_pt,NAVY,True)],118,None)],align='c',anchor='b',autofit=False)
        tb(s,b.x+k*slot,base+0.08,slot,0.30,[([R(lab,label_pt,NAVY,True)],118,None)],align='c')
    hline(s,b.x,base,b.w,SUB,0.75,keep=True)
    if axis_note: T(s,b.x,b.b-nh+0.02,b.w,axis_note,11,FOOT)
    return b.b

def hbars(s,b,its,color=NAVY_F,lcol=NAVY,label_w=None,pitch=0.33,pt=12,unit='%',vmax=100):
    """가로 막대 목록. its=[(라벨, 값)] 끝 y를 돌려준다."""
    lw=label_w or b.w*0.44; vw=0.72; bw=b.w-lw-vw-0.16
    y=b.y
    for name,v in its:
        nl=n_lines(name,pt,lw); rh=max(pitch,nl*lh(pt,125)+0.10)
        tb(s,b.x,y,lw,rh,[([R(name,pt,INK)],125 if nl>1 else 118,None)],anchor='m')
        rect(s,b.x+lw+0.08,y+rh/2-0.10,bw,0.20,'F2F4F8')
        rect(s,b.x+lw+0.08,y+rh/2-0.10,bw*v/vmax,0.20,color)
        tb(s,b.r-vw,y,vw,rh,[([R(f'{v:.1f}{unit}',12.5,lcol,True)],118,None)],anchor='m',align='r',autofit=False)
        y+=rh
    return y

def progress(s,b,its,highlight=-1,label_w=2.6,right_w=2.33,pitch=None):
    """진행 막대. its=[(라벨, 오른쪽 작은 글, 비율%)]"""
    n=len(its); pitch=pitch or min(0.50,b.h/n); hl=highlight%n if highlight is not None else None
    bx=b.x+label_w+0.05; bw=b.w-label_w-right_w-0.20
    for i,(lab,small,p) in enumerate(its):
        y=b.y+i*pitch; hot=i==hl
        tb(s,b.x,y,label_w,0.40,[([R(lab,SZ['concl'],GOLD_T if hot else INK,True)],118,None)],anchor='m')
        rect(s,bx,y+0.10,bw,0.20,'F2F4F8'); rect(s,bx,y+0.10,bw*p/100,0.20,GOLD_F if hot else NAVY_F)
        tb(s,b.r-right_w,y,right_w,0.40,[([R(small+'  ',12,SUB),R(f'{p:.1f}%',16,GOLD_T if hot else NAVY,True)],118,None)],anchor='m',align='r')
    return b.y+n*pitch

def big_numbers(s,b,its,value_pt=30,label_w=None):
    """큰 숫자 나란히: [(라벨, 값 문자열)]"""
    n=len(its); cw=b.w/n; h=min(b.h,0.62)
    for i,(lab,v) in enumerate(its):
        x=b.x+i*cw; lw=label_w or cw*0.55
        tb(s,x,b.y,lw,h,[([R(lab,SZ['concl'],INK,True)],118,None)],anchor='m')
        tb(s,x+lw,b.y,cw-lw,h,[([R(v,value_pt,NAVY,True)],118,None)],anchor='m')
    return b.y+h

def before_after(s,b,its,unit='점'):
    """전후 수치 칸: [(제목, 전, 후, 설명)]"""
    n=len(its); gap=0.30; cw=(b.w-gap*(n-1))/n; ends=[]
    for i,(h,a,c,d) in enumerate(its):
        x=b.x+i*(cw+gap); rect(s,x,b.y,cw,0.05,NAVY_F)
        T(s,x,b.y+0.15,cw,h,SZ['head'],NAVY,True)
        tb(s,x,b.y+0.50,cw,0.62,[([R(a+unit,22,FOOT,True),R('  →  ',20,GOLD_F,True),R(c+unit,30,NAVY,True)],118,None)],anchor='m')
        dh=T(s,x,b.y+1.20,cw,d,12,SUB); ends.append(b.y+1.20+dh)
    return max(ends)

def change_rows(s,b,its,row_h=0.72):
    """전후 변화 행: [(이름, 전, 후, 변화, 강조)]"""
    for i,(n_,a,c,d,hot) in enumerate(its):
        y=b.y+i*row_h
        if i: hline(s,b.x,y,b.w)
        tb(s,b.x,y,b.w*0.35,row_h,[([R(n_,SZ['concl'],NAVY if hot else INK,True)],118,None)],anchor='m')
        tb(s,b.x+b.w*0.35,y,b.w*0.41,row_h,[([R(a,14,FOOT),R('  →  ',14,FOOT),R(c,22,NAVY if hot else INK,True)],118,None)],anchor='m')
        tb(s,b.x+b.w*0.76,y,b.w*0.24,row_h,[([R(d,18,GOLD_T,True)],118,None)],anchor='m',align='r',autofit=False)
    return b.y+len(its)*row_h
