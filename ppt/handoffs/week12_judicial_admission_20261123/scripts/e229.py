_pre=open('e121.py').read().split('# ================= 35')[0].replace("Presentation('v120.pptx')","Presentation('v228.pptx')")
exec(_pre)
from pptx.util import Pt
from pptx.dml.color import RGBColor
from lxml import etree
A='{http://schemas.openxmlformats.org/drawingml/2006/main}'
sl=p.slides[16]; assert one(sl,'title').text_frame.text.startswith('2016년 헌재')
cs=sorted([s for s in sl.shapes if s.name=='step-text'],key=lambda s:s.left)
# 글자 크기 통일: 머리 12, 제목 15, 본문 13.5(본문 항목은 굵게 유지 여부 유지)
for c in cs:
    ps=c.text_frame.paragraphs
    for i,q in enumerate(ps):
        for r in q.runs:
            r.font.size=Pt(12 if i==0 else 15 if i==1 else 13.5)
# 강조
q=cs[1].text_frame.paragraphs[3]; r=q.runs[0]
r.font.bold=True; r.font.color.rgb=RGBColor.from_string('1E2761')
rp=r._r.find(A+'rPr'); sf=rp.find(A+'solidFill')
h=etree.Element(A+'highlight'); c_=etree.SubElement(h,A+'srgbClr'); c_.set('val','FFE699'); sf.addnext(h)
r.text='과잉금지원칙 중 침해의 최소성·법익의 균형성 위반'
# 4번 카드: 시기 바로잡기
ps=cs[3].text_frame.paragraphs
ps[0].runs[0].text='④ 같은 시기의 법 개정'
ps[1].runs[0].text='2016.5 공포 · 2017.5 시행'
ps[2].runs[0].text='1. 2주 진단입원, 전문의 2명 이상의 진단'
ps[3].runs[0].text='2. 입원적합성심사위원회 심사'
settext(one(sl,'message'),'헌재는 구법의 보호입원에 독립적·중립적인 제3자의 판단이 없다고 보았다. 진단입원과 입원적합성심사위원회는 이 결정보다 앞서 공포된 개정법이 도입했고, 헌재는 개정법이 문제를 해소했는지는 판단하지 않았다.')
m=one(sl,'meaning'); ps=m.text_frame.paragraphs
ps[1].runs[0].text='유엔 자유권위원회(2023)와 고문방지위원회(2024)는 한국에 사법심사를 포함한 보호장치를 보장하라고 권고했다.'
for r in ps[1].runs: r.font.size=Pt(13)
settext(one(sl,'chip-text'),'쟁점 ①·④ · 51·54쪽')
for s in p.slides:
    for x in s.shapes:
        if x.name=='chip-text' and ('52·55' in x.text_frame.text): settext(x,x.text_frame.text.replace('52·55','51·54'))
script(17)
p.save('v229.pptx')
for i,s in enumerate(p.slides,1):
    for x in s.shapes:
        if x.name=='chip-text' and '쪽' in x.text_frame.text: print(i,x.text_frame.text)
