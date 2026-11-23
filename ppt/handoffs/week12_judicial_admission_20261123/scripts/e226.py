_pre=open('e121.py').read().split('# ================= 35')[0].replace("Presentation('v120.pptx')","Presentation('v225.pptx')")
exec(_pre)
from lxml import etree
A='{http://schemas.openxmlformats.org/drawingml/2006/main}'
sl=p.slides[15]; assert one(sl,'title').text_frame.text.startswith('현행 심사에서')
c=[s for s in sl.shapes if s.name=='step-text' and '환자의견진술서' in s.text_frame.text][0]
q=[q for q in c.text_frame.paragraphs if q.text.startswith('개정 뒤에는')][0]
assert len(q.runs)==1
r=q.runs[0]; t=r.text; k=t.index('환자가 입원 과정의')
r2=copy.deepcopy(r._r); r._r.addnext(r2)
r.text=t[:k]; r2.find(A+'t').text=t[k:]
rp=r2.find(A+'rPr'); rp.set('b','1')
sf=rp.find(A+'solidFill'); sf[0].set('val','1E2761')
h=etree.Element(A+'highlight'); c_=etree.SubElement(h,A+'srgbClr'); c_.set('val','FFE699'); sf.addnext(h)
p.save('v226.pptx')
