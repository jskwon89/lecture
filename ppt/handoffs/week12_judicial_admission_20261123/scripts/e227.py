_pre=open('e121.py').read().split('# ================= 35')[0].replace("Presentation('v120.pptx')","Presentation('v226.pptx')")
exec(_pre)
from pptx.dml.color import RGBColor
from pptx.util import Inches
sl=p.slides[38]; assert one(sl,'title').text_frame.text.startswith('미국')
for s in sl.shapes:
    if s.name in('box-bg','box-bar') and abs(s.left/I-6.75)<0.02:
        fill(s,'FBF5E6' if s.name=='box-bg' else 'C9A43A')
    if s.name=='box' and 'Addington' in s.text_frame.text:
        s.text_frame.paragraphs[0].runs[0].font.color.rgb=RGBColor.from_string('8A6A12')
sl=p.slides[40]; assert one(sl,'title').text_frame.text.startswith('유럽 40개국')
for s in sl.shapes:
    if s.name=='seg' and s.has_text_frame and s.text_frame.text.strip():
        v=int(s.text_frame.text); r=s.text_frame.paragraphs[0].runs[0]
        r.text=f'{v} ({v/40*100:.1f}%)'.replace('.0%','%') if v>2 else str(v)
        print(r.text, round(s.width/I,2))
p.save('v227.pptx')
for s in sl.shapes:
    if s.name=='h-value':
        q=s.text_frame.paragraphs[1]; q.runs[0].text=q.runs[0].text.replace('83%','82.5%')
    if s.name=='legend-label' and '영국' in s.text_frame.text:
        s.width=Inches(3.0); s.text_frame.paragraphs[0].runs[0].text='지역마다 다르다(영국, 1개국 · 2.5%)'
p.save('v227.pptx')
