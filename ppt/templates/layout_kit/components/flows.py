"""흐름 부품: 타임라인, 가로 단계, 세로 단계, 분기 흐름도, 누적 조합 열"""
from core import *

def timeline(s,b,events,hot=-1,date_w=2.05,step=None):
    """세로 타임라인: [(날짜, 결론, 보충)]"""
    n=len(events); step=step or min(0.72,b.h/n); axx=b.x+date_w+0.20; tx=axx+0.40; tw=b.r-tx
    hot=hot%n if hot is not None else None
    vline(s,axx,b.y+0.13,step*(n-1),NAVY_F,1.5)
    for i,(d,c,sup) in enumerate(events):
        y=b.y+i*step
        tb(s,b.x,y,date_w,0.30,[([R(d,SZ['head'],NAVY,True)],118,None)],align='r')
        rect(s,axx-0.075,y+0.055,0.15,0.15,NAVY if i==hot else WHITE,NAVY,1.5,MSO_SHAPE.OVAL)
        ps,_=body_block(c,[sup] if sup else [],w=tw); tb(s,tx,y-0.035,tw,step,ps)
    return b.y+n*step

def steps_h(s,b,steps,hot=-1,arrow_w=0.60):
    """가로 단계: [(단계명, 설명)] 위쪽 막대 + 화살표"""
    n=len(steps); sw=(b.w-arrow_w*(n-1))/n; hot=hot%n if hot is not None else None; ends=[]
    for i,(a,d) in enumerate(steps):
        x=b.x+i*(sw+arrow_w)
        rect(s,x,b.y,sw,0.05,NAVY if i==hot else NAVY_F)
        ps,h=body_block(a,[d] if d else [],w=sw); tb(s,x,b.y+0.12,sw,h+0.1,ps); ends.append(b.y+0.12+h)
        if i<n-1: tb(s,x+sw,b.y+0.08,arrow_w,0.40,[([R('→',18,GOLD_F,True)],118,None)],align='c',autofit=False)
    return max(ends)

def steps_v(s,b,steps,hot=None,pitch=None):
    """세로 단계(점과 축): [문장…]"""
    n=len(steps); pitch=pitch or min(0.46,b.h/n); ax=b.x+0.14
    vline(s,ax,b.y+0.12,pitch*(n-1),NAVY_F,1.5)
    for i,t in enumerate(steps):
        y=b.y+i*pitch; h_=i==hot
        rect(s,ax-0.075,y+0.05,0.15,0.15,NAVY if h_ else WHITE,NAVY,1.5,MSO_SHAPE.OVAL)
        tb(s,ax+0.30,y,b.w-0.45,0.30,[([R(t,SZ['concl'],NAVY if h_ else INK,True)],118,None)])
    return b.y+n*pitch

def tree(s,b,sources,branches,hot=0,hot_label=None):
    """분기 흐름도. sources=[(단계명, 설명)] 가로로 이어진 앞 단계, branches=[(머리, [항목], 바닥 글)]"""
    n=len(sources); aw=0.75
    ws=[3.60]+[b.w-3.60-aw]*(n-1) if n==2 else [(b.w-aw*(n-1))/n]*n
    x=b.x; ny=b.y
    for i,(a,d) in enumerate(sources):
        rect(s,x,ny,ws[i],0.66,None,NAVY,1.0)
        tb(s,x+0.18,ny+0.06,ws[i]-0.36,0.54,[([R(a,SZ['concl'],NAVY,True)],118,2),([R(d,12,SUB)],118,None)],anchor='m')
        if i<n-1: tb(s,x+ws[i],ny+0.13,aw,0.40,[([R('→',18,NAVY_F,True)],118,None)],align='c',autofit=False)
        last_mid=x+ws[i]/2; x+=ws[i]+aw
    k=len(branches); cw=(b.w-0.41*(k-1))/k; bx=[b.x+i*(cw+0.41) for i in range(k)]
    jy=ny+0.66; cy=jy+0.50
    vline(s,last_mid,jy,0.25,NAVY_F,1.25); hline(s,bx[0]+cw/2,jy+0.25,bx[-1]-bx[0],NAVY_F,1.25,keep=True)
    for i in range(k): vline(s,bx[i]+cw/2,jy+0.25,0.25,NAVY_F,1.25)
    fy=b.b-0.40
    for i,(h,its,f) in enumerate(branches):
        rect(s,bx[i],cy,cw,0.44,GOLD_F if i==hot else NAVY_F)
        tb(s,bx[i],cy,cw,0.44,[([R(h,SZ['concl'],WHITE,True)],118,None)],anchor='m',align='c')
        tb(s,bx[i]+0.12,cy+0.60,cw-0.24,fy-cy-0.7,[([R(t,SZ['supp'],INK)],125,5) for t in its])
        hline(s,bx[i],fy,cw,keep=True)
        tb(s,bx[i],fy+0.10,cw,0.28,[([R(f,SZ['supp'],GOLD_T if i==hot else NAVY,True)],118,None)],align='c')
    if hot_label is not None: T(s,bx[hot],fy-0.34,cw-0.12,hot_label,12,GOLD_T,True,align='r')
    return b.b

def stack_columns(s,b,cols,group_label=None,group_from=1):
    """누적 조합 열: [(제목, 보조 줄, [항목], 추가된 항목 수)] 마지막 열을 진하게, 추가 항목은 금색 '+'"""
    n=len(cols); gap=0.31; cw=(b.w-gap*(n-1))/n; xs=[b.x+i*(cw+gap) for i in range(n)]
    y0=b.y
    if group_label:
        T(s,xs[group_from],b.y,b.r-xs[group_from],group_label,11,NAVY,True); y0=b.y+0.30
    for i,(h,sub,its,added) in enumerate(cols):
        x=xs[i]; last=i==n-1
        rect(s,x,y0,cw,0.05,NAVY if last else NAVY_F)
        tb(s,x,y0+0.13,cw,0.60,[([R(h,13.5,NAVY,True)],125,None)])
        T(s,x,y0+0.73,cw,sub,11,FOOT)
        hline(s,x,y0+1.01,cw,keep=True)
        y=y0+1.10
        for k,t in enumerate(its):
            hot=k>=len(its)-added
            tb(s,x,y,cw,0.28,[([R(('+ ' if hot else '')+t,12.5,GOLD_T if hot else INK,hot)],118,None)]); y+=0.28
    return b.b
