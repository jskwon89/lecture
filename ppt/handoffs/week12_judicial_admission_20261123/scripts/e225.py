_pre=open('e121.py').read().split('# ================= 35')[0].replace("Presentation('v120.pptx')","Presentation('v224.pptx')")
exec(_pre)
from pptx.util import Inches
sl=p.slides[6]; assert one(sl,'title').text_frame.text.startswith('보호입원:')
cards=[s for s in sl.shapes if s.name=='court-card']
c1=[c for c in cards if '①' in c.text_frame.text][0]; c2=[c for c in cards if '②' in c.text_frame.text][0]
c1.left=Inches(5.10); c1.width=Inches(4.68)
def put(c,lines):
    ps=c.text_frame.paragraphs
    for q,t in zip(ps,lines): q.runs[0].text=t
put(c1,['사법입원제 ① 입원 전 결정','진단입원 전에 법원이 개입한다. 병원장 대신 법원이 입원 여부와 기간을 처음부터 정한다(독일 바이에른).'])
put(c2,['사법입원제 ② 입원 후 심사','진단입원까지는 병원장이 시키고, 계속 입원을 법원이 정한다(프랑스, 정부 검토안).'])
lab=one(sl,'court-lead'); lab.width=Inches(4.15)
ps=lab.text_frame.paragraphs; ps[0].runs[0].text='사법입원제는 어느 단계에 법원이 개입하느냐에 따라 두 유형으로 나뉜다 →'; 
ps[1]._p.getparent().remove(ps[1]._p)
c2.left=Inches(9.90); c2.width=Inches(2.63)
script(7)
p.save('v225.pptx')
put(c2,['사법입원제 ② 입원 후 심사','진단입원까지는 병원장이, 계속 입원은 법원이 정한다(프랑스, 정부 검토안).'])
for s in sl.shapes:
    if s.name in('court-card','court-lead'): s.height=Inches(0.95)
    elif s.name=='rule' and abs(s.top/I-5.62)<0.02: s.top=Inches(5.74)
    elif s.name in('after-label','after-text'): s.top=Inches(5.80); s.height=Inches(0.90)
p.save('v225.pptx')
