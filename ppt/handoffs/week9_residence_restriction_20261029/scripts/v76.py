import copy
from pptx import Presentation
from pptx.opc.constants import RELATIONSHIP_TYPE as RT
A='{http://schemas.openxmlformats.org/drawingml/2006/main}'
R='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
P=Presentation('W9_merged_v75.pptx')
s8=P.slides[7]; s15=P.slides[9]
L=[sh for sh in s8.shapes if sh.name=='LINK'][0]
def set_text(el,rid=None):
    ps=el.findall('.//'+A+'p'); p=ps[0]
    rs=p.findall(A+'r')
    for r in rs[1:]: p.remove(r)
    rs[0].find(A+'t').text='▶ 영상'
    if rid:
        rs[0].find('.//'+A+'hlinkClick').set(R+'id',rid)
set_text(L._element)
new=copy.deepcopy(L._element)
rid=s15.part.relate_to('https://www.youtube.com/watch?v=RP0lrTsmouA',RT.HYPERLINK,is_external=True)
set_text(new,rid)
s15.shapes._spTree.append(new)
sh=s15.shapes[-1]
sh.left=int(9.0*914400); sh.width=int(3.33*914400); sh.top=int(6.02*914400)
P.save('W9_merged_v76.pptx')
