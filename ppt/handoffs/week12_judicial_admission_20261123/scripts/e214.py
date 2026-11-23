_pre=open('e121.py').read().split('# ================= 35')[0].replace("Presentation('v120.pptx')","Presentation('v213.pptx')")
exec(_pre)
from pptx.util import Inches,Pt
from pptx.dml.color import RGBColor
from lxml import etree
A='{http://schemas.openxmlformats.org/drawingml/2006/main}'
def pos(s,x,y,w,h): s.left=Inches(x); s.top=Inches(y); s.width=Inches(w); s.height=Inches(h)
def T(n,start):
    sl=p.slides[n-1]; assert one(sl,'title').text_frame.text.startswith(start); return sl
def find(sl,name,sub): return [s for s in sl.shapes if s.name==name and s.has_text_frame and sub in s.text_frame.text][0]
def paras(sh,items):
    ps=sh.text_frame.paragraphs; assert len(ps)==len(items)
    for q,t in zip(ps,items):
        for r in q.runs[1:]: r._r.getparent().remove(r._r)
        q.runs[0].text=t
def scale(sh,add):
    for q in sh.text_frame.paragraphs:
        for r in q.runs:
            if r.font.size: r.font.size=Pt(r.font.size.pt+add)
def retitle(old,new):
    for s in p.slides:
        for sh in s.shapes:
            if sh.has_text_frame and old in sh.text_frame.text and sh.name in('title','next','toc-item'):
                settext(sh,sh.text_frame.text.replace(old,new))
# ---- 5
sl=T(5,'서현역')
for s in sl.shapes:
    y=s.top/I
    if s.name=='step-panel': s.height=Inches(2.50)
    elif s.name=='step-text': s.height=Inches(2.43); scale(s,1.5)
    elif s.name=='flow-arrow': s.top=Inches(3.53)
    elif s.name=='rule' and abs(y-4.62)<0.02: s.top=Inches(5.08)
    elif s.name=='rule' and abs(y-5.48)<0.02: s.top=Inches(6.56)
    elif s.name in('row-label','row-text'): s.top=Inches(5.10); s.height=Inches(1.44); scale(s,2.0)
# ---- 16
sl=T(16,'현행 심사에서')
for s in list(sl.shapes):
    y=s.top/I
    if s.name=='rule' and abs(y-6.30)<0.02: rm(s)
    elif s.name=='step-panel' and y>4.5: s.top=Inches(4.72); s.height=Inches(1.90)
    elif s.name=='step-bar' and y>4.5: s.top=Inches(4.72)
    elif s.name=='flow-arrow': s.top=Inches(4.36)
c=find(sl,'step-text','환자의견진술서'); pos(c,0.98,4.78,11.37,1.84)
setp(c,[('정부의 보완(2026.3.30) · 입원적합성심사위원회 운영 규정 개정',0),('환자의견진술서 도입: 환자가 입원적합성심사위원회에 직접 의견을 적어 낸다',1),
 ('전에는 위원회가 서류로 심사했고, 환자의 의견은 대면조사를 신청한 경우에 조사원의 보고서로 전달됐다. 퇴원·처우개선 심사는 환자가 따로 청구해야 열린다.',2),
 ('개정 뒤에는 운영 규정에 환자의 의견진술권을 명시했다. 환자가 입원 과정의 상황과 퇴원 의사를 진술서에 직접 적어 내고, 환자의 직접 진술을 확인해야 하면 심사일을 다시 정할 수 있다.',2)])
script(16)
# ---- 17
sl=T(17,'지금은 누가')
retitle('지금은 누가 입원의 책임을 지고, 무엇으로 바꾸자는가','지금은 누가 입원의 책임과 부담을 지고, 무엇으로 바꾸자는가')
settext(find(sl,'col-head','하는 일'),'필요한 행위'); settext(find(sl,'col-head','함께 지는 책임'),'책임과 부담')
m=one(sl,'meaning'); ps=m.text_frame.paragraphs
paras(m,['사법입원제에서 법원으로 결정을 옮기는 것은 책임과 부담을 옮기는 것이라고 볼 수 있다.',ps[1].text,'행정·응급입원의 본인부담금은 국가와 지자체가 부담할 수 있다(제80조). '])
r=ps[1].runs[0]; r.font.bold=False; r.font.color.rgb=RGBColor.from_string('464D5C')
r3=ps[2].runs[0]; e=copy.deepcopy(r3._r); r3._r.addnext(e)
e.find(A+'t').text='지자체의 비용 부담 때문에 행정입원을 꺼린다는 지적이 있었다(2019).'
e.find(A+'rPr').find(A+'solidFill')[0].set('val','B38A1E')
script(17)
# ---- 18
sl=T(18,'사법입원제를 도입하면')
retitle('사법입원제를 도입하면 무엇이 바뀌는가','사법입원제의 방향과 대안')
settext(one(sl,'message'),'사법입원제는 지금 병원장·지자체장이 하는 입원 조치나 입원적합성심사위원회가 하는 심사를 법원이 맡게 하는 제도다. 법원 대신 독립된 심판원에 심사를 맡기자는 대안도 있다.')
rm(one(sl,'who'))
tree=one(sl,'title')._element.getparent()
row=[s for s in sl.shapes if 4.40<s.top/I<4.75 and s.name in('lane-label-bg','lane-label','cell','cell-bar','cell-text','flow-arrow')]
new=[]
for s in row:
    e=copy.deepcopy(s._element); tree.append(e); n=[q for q in sl.shapes if q._element is e][0]; n.top=Inches(s.top/I+0.82); new.append(n)
def nf(name,sub): return [s for s in new if s.name==name and s.has_text_frame and sub in s.text_frame.text][0]
paras(nf('lane-label','사법입원제'),['대안','심판원 심사'])
settext(nf('cell-text','안에 따라'),'의사의 증명서 등(호주 NSW)')
settext(nf('cell-text','현행과 같음'),'병원이 먼저 입원시킴')
paras(nf('cell-text','법원이 심사'),['독립된 심판원이 심사','법원은 불복 사건만 맡는다'])
for s in sl.shapes:
    y=s.top/I
    if s.name=='rule' and abs(y-5.28)<0.02: s.top=Inches(6.06)
    elif s.name=='rule' and abs(y-6.08)<0.02: rm(s)
for s in sl.shapes:
    if s.name in('after-label','after-text'): s.top=Inches(6.07); s.height=Inches(0.62)
script(18)
p.save('v214.pptx')
