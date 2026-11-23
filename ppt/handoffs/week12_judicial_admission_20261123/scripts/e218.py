_pre=open('e121.py').read().split('# ================= 35')[0].replace("Presentation('v120.pptx')","Presentation('v217.pptx')")
exec(_pre)
from pptx.util import Inches
def paras(sh,items):
    ps=sh.text_frame.paragraphs; assert len(ps)==len(items),(len(ps),items)
    for q,t in zip(ps,items):
        for r in q.runs[1:]: r._r.getparent().remove(r._r)
        q.runs[0].text=t
sl=p.slides[42]; assert one(sl,'title').text_frame.text.startswith('입원한 뒤 법원이')
for s in list(sl.shapes):
    if s.name in('step-panel','step-bar','step-text') and s.left/I<3: rm(s)
X=[0.80,4.80,8.79]; W=3.74
for s in sl.shapes:
    if s.name in('step-panel','step-bar','step-text'):
        x=s.left/I; i=0 if x<6 else 1 if x<9 else 2
        if s.name=='step-text': s.left=Inches(X[i]+0.24); s.width=Inches(W-0.48)
        else: s.left=Inches(X[i]); s.width=Inches(W)
settext(one(sl,'message'),'먼저 입원시키고 그 뒤에 심사하는 통상 절차를 비교하면, 오스트리아는 4일 안에 법원이 환자를 만나고 프랑스는 12일 안에 법원이 결정한다. 한국은 입원적합성심사위원회가 1개월 안에 결과를 통지한다.')
m=one(sl,'meaning'); ps=[q.text for q in m.text_frame.paragraphs]
setp(m,[('입원한 뒤에 법원이 심사하는 두 나라에서는 4일에서 12일 사이에 법원이 첫 결정을 한다. 한국의 1개월보다 훨씬 이르다.',0),(ps[1],1),
        ('독일 바이에른은 통상 절차에서 법원이 입원 전에 결정한다. 응급입원은 한국(3일 이내)과 바이에른(다음 날까지 법원 결정) 모두 별도의 절차다.',1)])
script(43)
p.save('v218.pptx')
