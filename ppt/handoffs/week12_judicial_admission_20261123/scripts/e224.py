_pre=open('e121.py').read().split('# ================= 35')[0].replace("Presentation('v120.pptx')","Presentation('v223.pptx')")
exec(_pre)
from pptx.util import Inches,Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
sl=p.slides[6]; assert one(sl,'title').text_frame.text.startswith('보호입원:')
for s in sl.shapes:
    if s.name=='step-panel': s.height=Inches(1.85)
    elif s.name=='step-text': s.height=Inches(1.79)
    elif s.name=='flow-arrow': s.top=Inches(3.42)
    elif s.name=='rule' and abs(s.top/I-5.05)<0.02: s.top=Inches(5.62)
    elif s.name in('after-label','after-text'):
        s.top=Inches(5.70); s.height=Inches(0.98)
        for q in s.text_frame.paragraphs:
            for r in q.runs:
                if r.font.size: r.font.size=Pt(r.font.size.pt-1.5)
def box(name,x,y,w,h,col=None,line=None,dash=False):
    b=sl.shapes.add_shape(MSO_SHAPE.RECTANGLE,Inches(x),Inches(y),Inches(w),Inches(h)); b.name=name
    if col: b.fill.solid(); b.fill.fore_color.rgb=RGBColor.from_string(col)
    else: b.fill.background()
    if line:
        b.line.color.rgb=RGBColor.from_string(line); b.line.width=Pt(1.25)
        if dash:
            from pptx.enum.dml import MSO_LINE
            b.line.dash_style=MSO_LINE.DASH
    else: b.line.fill.background()
    b.shadow.inherit=False
    return b
def text(b,lines,align=PP_ALIGN.LEFT):
    tf=b.text_frame; tf.word_wrap=True; tf.margin_left=tf.margin_right=Inches(0.12); tf.margin_top=tf.margin_bottom=Inches(0.04)
    tf.vertical_anchor=MSO_ANCHOR.MIDDLE
    for i,(t,sz,bold,col) in enumerate(lines):
        q=tf.paragraphs[0] if i==0 else tf.add_paragraph(); q.alignment=align
        r=q.add_run(); r.text=t; r.font.size=Pt(sz); r.font.bold=bold; r.font.name='Pretendard'; r.font.color.rgb=RGBColor.from_string(col)
Y=4.66; H=0.80
lab=box('court-lead',0.80,Y,6.40,H); text(lab,[('사법입원제는 이 단계의 결정을 법원이 맡게 한다 →',13.5,True,'8A6A12'),('어느 단계를 맡는지에 따라 두 유형으로 나뉜다.',11.5,False,'464D5C')],PP_ALIGN.RIGHT)
for x,w,t1,t2 in ((7.42,2.36,'사법입원제 ① 입원 전 결정','법원이 입원을 허용한다(독일 바이에른)'),
                  (10.13,2.40,'사법입원제 ② 입원 후 심사','법원이 계속 입원을 결정한다(프랑스, 정부 검토안)')):
    b=box('court-card',x,Y,w,H,'FBF3DC','C2A648',True)
    text(b,[(t1,11.5,True,'8A6A12'),(t2,11,False,'222633')])
script(7)
p.save('v224.pptx')
