import copy
from pptx import Presentation
from lxml import etree
A='{http://schemas.openxmlformats.org/drawingml/2006/main}'
P=Presentation('INPUT_user_edited_v74.pptx')
S=P.slides

def norm_runs(P):
    n=0
    for sl in P.slides:
        for p in sl.shapes._spTree.iter(A+'p'):
            prev=None;pk=None
            for ch in list(p):
                if ch.tag==A+'r':
                    rpr=ch.find(A+'rPr')
                    if rpr is not None:
                        for at in ('err','dirty','noProof'): rpr.attrib.pop(at,None)
                    k=etree.tostring(rpr) if rpr is not None else b''
                    if prev is not None and k==pk:
                        prev.find(A+'t').text=(prev.find(A+'t').text or '')+(ch.find(A+'t').text or '')
                        p.remove(ch); n+=1; continue
                    prev=ch;pk=k
                else:
                    if ch.tag!=A+'pPr': prev=None
    return n
print('merged',norm_runs(P))
def paras(i):
    for sh in S[i-1].shapes:
        if sh.has_text_frame:
            for p in sh.text_frame.paragraphs: yield sh,p
def rep(i,old,new,br_before=None):
    n=0
    for sh,p in paras(i):
        rs=p.runs; t=''.join(r.text for r in rs)
        if old not in t: continue
        a=t.index(old); b=a+len(old); pos=0
        for k,r in enumerate(rs):
            s,e=pos,pos+len(r.text); pos=e
            if e<=a or s>=b: continue
            # overlap
            if s<=a:
                r.text=r.text[:a-s]+new+(r.text[b-s:] if e>=b else '')
            else:
                r.text=r.text[b-s:] if e>b else ''
        n+=1
    assert n==1,(i,old,n)
def br_at(i,marker,ctx=None):
    for sh,p in paras(i):
        if ctx and ctx not in ''.join(r.text for r in p.runs): continue
        for r in p.runs:
            if marker in r.text:
                pre,post=r.text.split(marker,1)
                r.text=pre
                nr=copy.deepcopy(r._r); r._r.addnext(nr)
                nr.find(A+'t').text=marker+post
                br=etree.SubElement(p._p,A+'br'); 
                rpr=r._r.find(A+'rPr')
                if rpr is not None: br.append(copy.deepcopy(rpr))
                r._r.addnext(br)
                return
    raise Exception((i,marker))
def chip(i,new):
    for sh,p in paras(i):
        t=''.join(r.text for r in p.runs)
        if t.startswith('다음'):
            if new is None:
                sh._element.getparent().remove(sh._element); return
            rs=p.runs; rs[0].text='다음 → '+new
            for r in rs[1:]: r.text=''
            return
    raise Exception(i)
T={}
for k in range(len(S)):
    ts=[sh for sh in S[k].shapes if sh.has_text_frame and sh.text_frame.text.strip()]
    T[k+1]=max(ts,key=lambda sh:max([r.font.size or 0 for p in sh.text_frame.paragraphs for r in p.runs]+[0])).text_frame.text.replace('\n',' ')
for i in [27,28,29,31,32,39,61]: chip(i,T[i+1])
chip(45,'쟁점'); chip(62,None)
# page refs
rep(48,'(39·40쪽)','(38·39쪽)'); rep(50,'(39쪽)','(38쪽)'); rep(50,'(40쪽)','(39쪽)')
# TOC / divider / labels
rep(2,' · 전문위원 검토','')
for sh in list(S[40].shapes):
    if sh.has_text_frame and sh.text_frame.text.strip() in ('3','전문위원의 검토'): sh._element.getparent().remove(sh._element)
rep(61,'4-2 해외 · 주거명령','보충자료'); rep(62,'5 법리','보충자료')
# 52
rep(52,'답하는 것도 가능합니다','답하는 것도 가능합니다.'); rep(52,'작성합니다. ','작성합니다.'); br_at(52,'찬반을 선택해')
# punctuation / wording
rep(19,'얼마나 될까','얼마나 될까?'); rep(50,'더 무겁다','더 무겁다.')
rep(32,'돌봄시설이다  ㅡ 어린이집, 돌봄센터, 아동센터.','돌봄시설이다(한국의 어린이집·다함께돌봄센터·지역아동센터에 해당).')
rep(32,' <-> 한국의 의무교육',' 한국은 홈스쿨을 의무교육 취학으로 인정하지 않는다.')
rep(38,'전자감독. 임상','전자감독.임상'); br_at(38,'임상','보안시설이라'); rep(38,'문제를 다룸','문제를 다룬다.')
rep(39,'AP에 머물게 함','AP에 머물게 한다.')
rep(44,'외출/출입 제한 준수','외출·출입 제한 준수'); rep(44,'외출/출입에 비해','외출·출입 제한에 비해')
rep(44,'과잉금지가 아니라고 볼 수 있는가','과잉금지원칙에 위반되지 않는다고 볼 수 있는가?')
rep(27,'공·사립 초·중등학교나','이들 대상자는 공·사립 초·중등학교나')
rep(29,'세 미만 아동을 대상으로 한 성범죄자 전체에 대해 ','세 미만 아동을 추행한 성범죄자에 대해 ')
for sh in S[51].shapes:
    if sh.has_text_frame and sh.text_frame.text.startswith('자신의 찬반'):
        sh.width=int(11.73*914400); sh.top=int(6.12*914400)
    if sh.name=='HRULE' and abs(sh.top/914400-6.72)<0.02: sh.top=int(6.86*914400)
P.save('W9_merged_v75.pptx')
print('ok')
