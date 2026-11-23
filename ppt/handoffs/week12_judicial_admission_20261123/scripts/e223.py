_pre=open('e121.py').read().split('# ================= 35')[0].replace("Presentation('v120.pptx')","Presentation('v222.pptx')")
exec(_pre)
from pptx.util import Inches
sl=p.slides[6]; assert one(sl,'title').text_frame.text.startswith('보호입원:')
for s in list(sl.shapes):
    if s.name in('flow-line','both'): rm(s)
sign=one(sl,'flow-sign'); arr=[s for s in sl.shapes if s.name=='flow-arrow'][0]
e=copy.deepcopy(arr._element); sl.shapes._spTree.append(e)
na=[s for s in sl.shapes if s._element is e][0]; na.left=Inches(3.41); na.top=arr.top
rm(sign)
settext(one(sl,'message'),'보호의무자가 신청하면 전문의 1명이 두 요건을 진단하고, 병원장이 최대 2주 진단입원시킨다. 그동안 다른 기관 전문의가 추가로 진단해 2명 이상의 소견이 일치해야 치료입원으로 넘어간다.')
script(7)
p.save('v223.pptx')
for s in sl.shapes:
    if s.name=='rule' and abs(s.top/I-5.38)<0.02: s.top=Inches(4.80)
    elif s.name in('after-label','after-text'): s.top=Inches(4.90)
p.save('v223.pptx')
from pptx.util import Pt
for s in sl.shapes:
    if s.name=='step-panel': s.height=Inches(2.40)
    elif s.name=='step-text':
        s.height=Inches(2.34)
        for q in s.text_frame.paragraphs:
            for r in q.runs:
                if r.font.size: r.font.size=Pt(r.font.size.pt+1.5)
    elif s.name=='flow-arrow': s.top=Inches(3.70)
    elif s.name=='rule' and abs(s.top/I-4.80)<0.02: s.top=Inches(5.30)
    elif s.name in('after-label','after-text'): s.top=Inches(5.42)
p.save('v223.pptx')
for s in sl.shapes:
    if s.name=='step-panel': s.height=Inches(2.10)
    elif s.name=='step-text':
        s.height=Inches(2.04)
        for q in s.text_frame.paragraphs:
            for r in q.runs:
                if r.font.size: r.font.size=Pt(r.font.size.pt-1.5)
    elif s.name=='flow-arrow': s.top=Inches(3.55)
    elif s.name=='rule' and abs(s.top/I-5.30)<0.02: s.top=Inches(5.05)
    elif s.name in('after-label','after-text'): s.top=Inches(5.20); s.height=Inches(1.20)
for s in sl.shapes:
    if s.name in('after-label','after-text'):
        for q in s.text_frame.paragraphs:
            for r in q.runs:
                if r.font.size: r.font.size=Pt(r.font.size.pt+1.5)
p.save('v223.pptx')
