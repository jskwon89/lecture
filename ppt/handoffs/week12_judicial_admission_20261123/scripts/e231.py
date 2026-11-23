_pre=open('e121.py').read().split('# ================= 35')[0].replace("Presentation('v120.pptx')","Presentation('v230.pptx')")
exec(_pre)
from pptx.util import Inches,Pt
S=list(p.slides)
s16,s17,s18=S[15],S[16],S[17]
assert one(s17,'title').text_frame.text.startswith('2016년 헌재')
# 16쪽 아래 한 줄
m=copy.deepcopy(one(s17,'meaning')._element); s16.shapes._spTree.append(m)
ln=[x for x in s16.shapes if x._element is m][0]
ln.left=Inches(0.80); ln.top=Inches(6.66); ln.width=Inches(11.73); ln.height=Inches(0.40)
ps=ln.text_frame.paragraphs; ps[1]._p.getparent().remove(ps[1]._p)
ps[0].runs[0].text='헌재(2016)는 입원 판단에 독립적·중립적인 제3자가 필요하다고 보았다. 지금의 심사가 그 기준을 충족하는지가 쟁점 ①이다.'
ps[0].runs[0].font.size=Pt(13.5)
for x in s16.shapes:
    if x.name=='step-panel' and x.top/I>4: x.height=Inches(1.78)
    if x.name=='step-text' and x.top/I>4: x.height=Inches(1.72)
    if x.name=='rule' and abs(x.top/I-6.72)<0.02: x.top=Inches(7.10)
ln.top=Inches(6.56)
settext(one(s16,'next'),'다음 → '+one(s18,'title').text_frame.text)
# 이동
ids=p.slides._sldIdLst; L=list(ids); e=L[16]; ids.remove(e); list(ids)[-1].addnext(e)
settext(one(s17,'chapter'),'보충자료  2016년 헌재 결정')
for x in list(s17.shapes):
    if x.name in('next','chip','chip-text'): rm(x)
# 쪽 번호 -1
import re
def dec(t): return re.sub(r'(\d+)·(\d+)쪽',lambda m:f'{int(m.group(1))-1}·{int(m.group(2))-1}쪽',re.sub(r'· (\d+)쪽',lambda m:f'· {int(m.group(1))-1}쪽',t))
for s in p.slides:
    for x in s.shapes:
        if x.name=='chip-text' and '쪽' in x.text_frame.text: settext(x,dec(x.text_frame.text))
        if x.name=='meaning' and '20쪽의 번호다' in x.text_frame.text:
            for q in x.text_frame.paragraphs:
                for r in q.runs: r.text=r.text.replace('20쪽의 번호다','19쪽의 번호다')
        if x.name=='message' and x.text_frame.text.startswith('후견 관련 법원 절차'):
            settext(x,x.text_frame.text.replace('헌재 결정 뒤의 현행법','2016년 헌재 결정, 헌재 결정 뒤의 현행법'))
tb=[s for s in p.slides[1].shapes if getattr(s,'has_table',False) and s.has_table][0].table
rows=list(tb.rows)
def ct(c,t): c.text_frame.paragraphs[0].runs[0].text=t
ct(rows[1].cells[1],'현행 입원 절차와 법원이 관여하는 방식')
for r,pg in zip(rows[2:],['20쪽','27쪽','35쪽','44쪽','49쪽']): ct(r.cells[2],pg)
p.save('v231.pptx')
for i,s in enumerate(p.slides,1):
    for x in s.shapes:
        if x.name=='chip-text' and '쪽' in x.text_frame.text: print(i,x.text_frame.text)
    t=[x for x in s.shapes if x.name=='title']
    if i in(2,16,17,20,27,35,44,49,50,53,54,55) or i>60: print(i,t[0].text_frame.text if t else '')
