"""표 부품: 행머리글 표, 수치 표, 대조표(선 마감형/머리 막대형)"""
from core import *

PAD_MIN=0.14
def row_table(s,b,rows,head_w=None,rules=True,name='row_table'):
    """행머리글 표. rows=[(머리글, 결론, [보충], 한정)]
    모든 행을 같은 높이로 두고, 넘치는 행만 키운다. 본문은 행 가운데.
    rules=True면 영역 위·아래에 마감선을 둔다(골격 선과 겹치면 자동 정리)."""
    hw=head_w or (2.45 if b.w>=9 else max(1.3,b.w*0.26))
    bx=b.x+hw+0.20; bw=b.r-bx
    blocks=[]
    for r in rows:
        head,concl=r[0],r[1]; supps=r[2] if len(r)>2 else (); lim=r[3] if len(r)>3 else None
        ps,bh=body_block(concl,supps,lim,w=bw)
        hn=n_lines(head,SZ['head'],hw-0.3,True)
        blocks.append((head,ps,max(bh,hn*lh(SZ['head'],118))))
    n=len(blocks); fixed={}
    while True:
        rest=[i for i in range(n) if i not in fixed]
        H=(b.h-sum(fixed.values()))/max(len(rest),1)
        over=[i for i in rest if blocks[i][2]+2*PAD_MIN>H]
        if not over: break
        for i in over: fixed[i]=blocks[i][2]+2*PAD_MIN
    hs=[fixed.get(i,H) for i in range(n)]
    LOG.append(f'{name} 행 높이 '+' / '.join(f'{h:.2f}' for h in hs)+(' ← 넘침' if sum(hs)>b.h+1e-6 else ''))
    if rules: hline(s,b.x,b.y,b.w,NAVY,1.5)
    y=b.y
    for i,((head,ps,ch),rh) in enumerate(zip(blocks,hs)):
        if i: hline(s,b.x,y,b.w)
        tb(s,b.x+0.15,y-0.025,hw-0.3,rh,[([R(head,SZ['head'],NAVY,True)],118,None)],anchor='m',align='c')
        tb(s,bx,y+(rh-ch)/2-0.035,bw,ch+0.05,ps)
        y+=rh
    if rules: hline(s,b.x,y,b.w,NAVY,1.5)
    return y

def num_table(s,b,cols,rows,total_col=None,first_w=1.55,head_h=0.42,row_h=0.70,num_pt=22):
    """수치 표. cols=[열 이름], rows=[[값…]]. total_col: 음영 칠 열 번호(예: 합계)"""
    cw=(b.w-first_w)/(len(cols)-1); xs=[b.x]+[b.x+first_w+i*cw for i in range(len(cols)-1)]
    ws=[first_w]+[cw]*(len(cols)-1)
    H=head_h+row_h*len(rows); warn_fit('num_table',H,b.h)
    if total_col is not None: rect(s,xs[total_col],b.y,ws[total_col],H,BAND)
    hline(s,b.x,b.y,b.w,NAVY,1.25,keep=True)
    for j,c in enumerate(cols): tb(s,xs[j],b.y,ws[j],head_h,[([R(c,13,NAVY,True)],118,None)],anchor='m',align='c')
    hline(s,b.x,b.y+head_h,b.w,NAVY,0.75,keep=True)
    for i,row in enumerate(rows):
        y=b.y+head_h+i*row_h
        if i: hline(s,b.x,y,b.w)
        for j,v in enumerate(row):
            tb(s,xs[j],y,ws[j],row_h,[([R(str(v),15 if j==0 else num_pt,NAVY if j in (0,total_col) else INK,True)],118,None)],anchor='m',align='c',autofit=False)
    hline(s,b.x,b.y+H,b.w,NAVY,1.25,keep=True)
    return b.y+H

def matrix(s,b,col_heads,rows,head_w=None,shade=None,style='rules',row_h=None,cell_pt=12.5,head_pt=13,align='c'):
    """대조표. rows=[(행 머리, [칸…], 굵게 여부)]
    style='rules' : 위·머리 아래·아래 마감선이 있는 일반 표(설계 대조표)
    style='bars'  : 열 머리를 색 막대로 채운 형(두 입장 대조)
    shade: 옅은 음영을 칠할 칸 열 번호(0부터)"""
    hw=head_w or (2.05 if b.w>=8 else 1.55)
    nc=len(col_heads); gap=0.0 if style=='rules' else 0.20
    cw=(b.w-hw-(0.15 if style=='bars' else 0)-gap*(nc-1))/nc
    xs=[b.x+hw+(0.15 if style=='bars' else 0)+j*(cw+gap) for j in range(nc)]
    head_h=0.46
    def ch(t,bold,pt): nl=n_lines(t,pt,cw-0.30,bold); return nl*lh(pt,125)
    need=[max(ch(c,r[2] if len(r)>2 else False,cell_pt if not (len(r)>2 and r[2]) else cell_pt+1) for c in r[1]) for r in rows]
    if row_h: hs=[max(row_h,n+0.3) for n in need]
    else:
        avail=b.h-head_h; hs=[n+0.3 for n in need]; extra=(avail-sum(hs))/len(rows)
        hs=[h+max(0,extra) for h in hs]
    H=head_h+sum(hs); warn_fit('matrix',H,b.h)
    if shade is not None: rect(s,xs[shade],b.y,cw,H,BAND)
    if style=='rules':
        hline(s,b.x,b.y,b.w,NAVY,1.25,keep=True)
        for j,h in enumerate(col_heads): tb(s,xs[j],b.y,cw,head_h,[([R(h,head_pt,NAVY,True)],118,None)],anchor='m',align='c')
        hline(s,b.x,b.y+head_h,b.w,NAVY,0.75,keep=True)
    else:
        for j,h in enumerate(col_heads):
            rect(s,xs[j],b.y+0.02,cw,head_h-0.04,NAVY_F)
            tb(s,xs[j]+0.1,b.y,cw-0.2,head_h,[([R(h,head_pt+0.5,WHITE,True)],118,None)],anchor='m',align='c')
    y=b.y+head_h
    for i,(r,rh) in enumerate(zip(rows,hs)):
        head,cells=r[0],r[1]; bold=r[2] if len(r)>2 else False
        if i or style=='bars': hline(s,b.x,y,b.w,keep=(style=='rules'))
        tb(s,b.x,y-0.025,hw,rh,[([R(head,SZ['head'] if style=='bars' else head_pt,NAVY,True)],125,None)],anchor='m',align='c')
        for j,c in enumerate(cells):
            pt=cell_pt+1 if bold else cell_pt
            tb(s,xs[j]+0.15,y,cw-0.30,rh,[(rich(c,pt,INK if (bold or style=='rules') else SUB,bold),125,None)],anchor='m',align=align)
        y+=rh
    if style=='rules': hline(s,b.x,y,b.w,NAVY,1.25,keep=True)
    return y
