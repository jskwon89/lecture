_pre=open('e121.py').read().split('# ================= 35')[0].replace("Presentation('v120.pptx')","Presentation('v229.pptx')")
exec(_pre)
from lxml import etree
A='{http://schemas.openxmlformats.org/drawingml/2006/main}'
sl=p.slides[15]; assert one(sl,'title').text_frame.text.startswith('현행 심사에서')
c=[s for s in sl.shapes if s.name=='step-text' and '환자의견진술서' in s.text_frame.text][0]
q=[q for q in c.text_frame.paragraphs if q.text.startswith('전에는')][0]
assert len(q.runs)==1, len(q.runs)
r=q.runs[0]; t=r.text; a=t.index('위원회가'); b=t.index('전달됐다.')+len('전달됐다.')
r2=copy.deepcopy(r._r); r3=copy.deepcopy(r._r); r._r.addnext(r2); r2.addnext(r3)
r.text=t[:a]; r2.find(A+'t').text=t[a:b]; r3.find(A+'t').text=t[b:]
rp=r2.find(A+'rPr'); rp.set('b','1'); sf=rp.find(A+'solidFill'); sf[0].set('val','1E2761')
h=etree.Element(A+'highlight'); c_=etree.SubElement(h,A+'srgbClr'); c_.set('val','FFE699'); sf.addnext(h)
print([x.text for x in q.runs])
p.save('v230.pptx')
