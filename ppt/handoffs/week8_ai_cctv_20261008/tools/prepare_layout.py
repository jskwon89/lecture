from pathlib import Path
import os
import json, math
from PIL import ImageFont

DEST=Path(os.environ.get('W8_BUNDLE_DIR',Path(__file__).resolve().parents[1]))
DATA=json.loads((DEST/'w8_content.json').read_text())
import subprocess
FONTS={bold:subprocess.check_output(['fc-match','-f','%{file}',f'Pretendard:style={style}'],text=True).strip() for bold,style in [(False,'Regular'),(True,'Bold')]}
assert all('Pretendard' in subprocess.check_output(['fc-scan','--format','%{family}',font],text=True) for font in FONTS.values()), 'Install Pretendard v1.3.9 first'
NAVY='#1E2761';INK='#222633';GRAY='#464D5C';LINE='#DCE0E8';BAND='#F2F4F8';GOLD='#A8871C'
MEASURE_DPI=720
def width(text,pt,bold=False):
    f=ImageFont.truetype(FONTS[bold],round(pt*MEASURE_DPI/72))
    return f.getlength(text)/MEASURE_DPI
def wrap(text,w,pt,bold=False):
    w *= .92  # reserve room for Office's East Asian spacing around Latin runs
    out=[]
    for para in text.split('\n'):
        if not para: out.append('');continue
        line=''
        for ch in para:
            if width(line+ch,pt,bold)>w and line:
                # prefer word boundaries, retain long Korean words intact when possible
                cut=line.rfind(' ')
                if cut>=len(line)*.55:
                    out.append(line[:cut]);line=line[cut+1:]+ch
                else:out.append(line);line=ch
            else:line+=ch
        out.append(line.strip())
    return '\n'.join(out)
def ht(text,pt):return len(text.split('\n'))*pt/72*(1.25 if '\n' in text else 1.18)+.055

SL=[]
for s in DATA['slides']:
    items=[];audit=[]
    def text(txt,x,y,w,pt=14,bold=False,color=INK,align='left',h=None,tag='body',do_wrap=True):
        t=wrap(txt,w-.035,pt,bold) if do_wrap else txt
        h=h or ht(t,pt)
        items.append(dict(type='text',text=t,x=x,y=y,w=w,h=h,pt=pt,bold=bold,color=color,align=align,tag=tag))
        return h
    def line(y,x=.8,w=11.73):items.append(dict(type='line',x=x,y=y,w=w,h=0,color=LINE))
    def rect(x,y,w,h,fill):items.append(dict(type='rect',x=x,y=y,w=w,h=h,fill=fill))
    kind=s['kind']
    if kind in ['cover','divider']:
        text('범죄·공공안전세미나Ⅱ',.8,.55,10,13,True,GRAY)
        text('8주차' if kind=='cover' else '질문에 따라 선택하는 자료',.8,1.5,10,16,True,NAVY)
        text(s['title'],.8,2.0,11.73,34,True,NAVY)
        y=3.12
        for row in s['rows']:
            line(y)
            text(row[0],.8,y+.25,2.1,13,True,NAVY)
            hh=text(row[1],3.15,y+.23,9.38,20 if kind=='cover' and y<3.3 else 14,True if y<3.3 else False,INK)
            y+=max(1.05,hh+.48)
        line(6.72)
    else:
        text(s['chapter'],.8,.40,5.70,12.5,True,GRAY,tag='kicker')
        if s['next_label']:text('다음  '+s['next_label'],6.60,.42,5.93,10.5,False,GRAY,'right',.28,'next')
        assert width(s['title'],27.5,True)<11.70,(s['page'],'long title')
        text(s['title'],.8,.70,11.73,27.5,True,NAVY,h=.70,tag='title',do_wrap=False)
        if s['band']:
            bt=wrap(s['band'],11.10,13,True)
            bh=.60 if '\n' not in bt else .85
            rect(.8,1.55,11.73,bh,BAND)
            text(bt,1.10,1.55+(bh-ht(bt,13))/2,11.10,13,True,NAVY,tag='band',do_wrap=False)
            top=2.25 if bh==.60 else 2.50
        else:top=1.52
        bottom=6.72
        belowH=sum(ht(wrap(t,11.73,12),12)+.10 for t in s['below'])
        end=bottom-belowH-.12 if s['below'] else bottom
        if kind=='toc':
            # Flat numbered rows retain the reference's academic agenda.
            dy=(end-top)/7
            for j,r in enumerate(s['rows']):
                y=top+j*dy;line(y)
                text(f'{j+1:02}',.86,y+.18,.55,13,True,GOLD)
                text(r[0],1.55,y+.16,3.48,14,True,NAVY)
                text(r[1],5.20,y+.16,7.28,12.5,False,GRAY)
        elif kind in ['rows','timeline','worksheet']:
            n=len(s['rows']);dy=(end-top)/n
            for j,r in enumerate(s['rows']):
                y=top+j*dy;line(y)
                lab=wrap(r[0],2.20,13,True)
                a=wrap(r[1],9.03,14,True);b=wrap(r[2],9.03,12.5)
                ah=ht(a,14);bhh=ht(b,12.5);g=.105;gh=ah+g+bhh
                assert gh<dy-.16,(s['page'],j,'row overflow',gh,dy)
                bodyy=y+(dy-gh)/2-.035;labely=y+(dy-ht(lab,13))/2-.025
                text(lab,.90,labely,2.25,13,True,NAVY,'center',do_wrap=False,tag='rowlabel')
                text(a,3.45,bodyy,9.08,14,True,INK,do_wrap=False,tag='conclusion')
                text(b,3.45,bodyy+ah+g,9.08,12.5,False,GRAY,do_wrap=False,tag='supplement')
                audit.append(dict(row=j+1,top=y,bottom=y+dy,label_top=labely,label_height=ht(lab,13),body_top=bodyy,body_height=gh,body_center_delta=-.035,label_center_delta=-.025))
        elif kind in ['columns','metrics']:
            n=len(s['rows']);gap=.30;cw=(11.73-gap*(n-1))/n
            line(top)
            for j,r in enumerate(s['rows']):
                x=.8+j*(cw+gap)
                text(r[0],x,top+.40,cw,13,True,NAVY)
                main=wrap(r[1],cw,22.5,True)
                hh=text(main,x,top+1.0,cw,22.5,True,NAVY,do_wrap=False)
                text(r[2],x,top+1.0+hh+.38,cw,14,False,INK)
        elif kind=='flow':
            n=len(s['rows']);gap=.36;cw=(11.73-gap*(n-1))/n
            line(top)
            for j,r in enumerate(s['rows']):
                x=.8+j*(cw+gap)
                text(f'{j+1:02}',x,top+.35,cw,13,True,GOLD)
                h=text(r[0],x,top+.95,cw,22.5,True,NAVY)
                text(r[1],x,top+1.22+h,cw,14,False,INK)
        elif kind in ['table','comparison']:
            k=len(s['headers']);n=len(s['rows'])+1
            widths={2:[2.70,9.03],3:[2.25,4.40,5.08],4:[2.15,3.45,2.05,4.08]}[k]
            if kind=='comparison':widths=[1.55,5.09,5.09]
            if s['page'] in [4,21,28,36,37]:widths=[2.35,4.47,4.91]
            values=[s['headers']]+s['rows']
            wrapped=[[wrap(t,widths[j]-.32,13 if i==0 or j==0 else 12.5,i==0 or j==0) for j,t in enumerate(row)] for i,row in enumerate(values)]
            headerh=.56
            minhs=[max(ht(t,13 if j==0 else 12.5)+.30 for j,t in enumerate(row)) for row in wrapped[1:]]
            available=end-top-headerh
            extra=(available-sum(minhs))/len(minhs)
            assert extra>=0,(s['page'],'table overflow',minhs,available)
            rowhs=[headerh]+[h+extra for h in minhs]
            items.append(dict(type='table',x=.8,y=top,w=11.73,h=end-top,widths=widths,rowhs=rowhs,values=wrapped))
        elif kind=='issues':
            dy=(end-top)/7
            for j,r in enumerate(s['rows']):
                y=top+j*dy;line(y)
                text(r[0],.92,y+(dy-ht(r[0],13))/2,2.55,13,True,NAVY)
                text(r[1],3.60,y+(dy-ht(r[1],13))/2,8.88,13,False,INK)
        elif kind=='chart':
            line(top)
            items.append(dict(type='chart',x=1.05,y=top+.20,w=11.20,h=end-top-.35,**s['chart']))
        else:raise ValueError(kind)
        if s['below']:
            y=end+.18
            for b in s['below']:y+=text(b,.8,y,11.73,12,False,GOLD,tag='scope')+.10
        line(6.72)
    SL.append({'id':s['id'],'page':s['page'],'kind':kind,'items':items,'row_audit':audit})
(Path(os.environ['W8_BUILD_DIR'])/'layout.json').write_text(json.dumps(SL,ensure_ascii=False,indent=2))
print('Measured',len(SL),'slides with Pretendard at 720dpi; row layouts',sum(bool(s['row_audit']) for s in SL))
