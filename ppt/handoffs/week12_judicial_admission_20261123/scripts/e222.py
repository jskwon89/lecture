_pre=open('e121.py').read().split('# ================= 35')[0].replace("Presentation('v120.pptx')","Presentation('v220.pptx')")
exec(_pre)
from pptx.util import Inches
sl=p.slides[6]; assert one(sl,'title').text_frame.text.startswith('보호입원:')
def rich(sh,paras_spec):
    """paras_spec: list of list of (text,kind); kind: H title, N normal, B bold"""
    tf=sh.text_frame; ps=tf.paragraphs
    tmpl_h=copy.deepcopy(ps[0].runs[0]._r); tmpl_n=None; tmpl_b=None
    for q in ps[1:]:
        for r in q.runs:
            if r.font.bold and tmpl_b is None and str(r.font.color.rgb)=='222633': tmpl_b=copy.deepcopy(r._r)
            if not r.font.bold and tmpl_n is None: tmpl_n=copy.deepcopy(r._r)
    ppr=[copy.deepcopy(q._p.pPr) if q._p.pPr is not None else None for q in ps]
    body=tf._txBody
    for q in list(ps): body.remove(q._p)
    from lxml import etree
    A='{http://schemas.openxmlformats.org/drawingml/2006/main}'
    for i,spec in enumerate(paras_spec):
        pe=etree.SubElement(body,A+'p')
        pp=ppr[min(i,len(ppr)-1)] if i==0 else ppr[min(1,len(ppr)-1)]
        if pp is not None: pe.append(copy.deepcopy(pp))
        for t,k in spec:
            r=copy.deepcopy({'H':tmpl_h,'N':tmpl_n,'B':tmpl_b}[k]); r.find(A+'t').text=t; pe.append(r)
cards=[s for s in sl.shapes if s.name=='step-text']
c2=[c for c in cards if c.text_frame.text.startswith('전문의 판단')][0]
c2.text_frame.paragraphs[0].runs[0].text='전문의 1명의 진단(두 요건 모두)'
c3=[c for c in cards if c.text_frame.text.startswith('진단입원')][0]
rich(c3,[[('진단입원','H')],[('병원장','B'),('이 입원시킨다','N')],[('정확한 진단을 위해 ','N'),('최대 2주','B')],[('이 기간에 ','N'),('다른 기관 전문의','B'),('가 추가로 진단한다','N')]])
c4=[c for c in cards if c.text_frame.text.startswith('치료입원')][0]
rich(c4,[[('치료입원','H')],[('병원장','B'),('이 입원시킨다','N')],[('서로 다른 기관의 전문의 ','N'),('2명 이상','B'),('의 소견 일치','N')],[('최초 입원일부터 ','N'),('3개월 이내','B')]])
settext(one(sl,'message'),'전문의 1명이 입원이 필요하다고 진단하면 병원장이 최대 2주 진단입원시킨다. 그동안 다른 기관 전문의가 추가로 진단해 2명 이상의 소견이 일치해야 치료입원으로 넘어간다.')
settext(one(sl,'after-label'),'필요한 진단')
at=one(sl,'after-text'); ps=at.text_frame.paragraphs
ps[0].runs[0].text='처음에는 전문의 1명의 진단으로 진단입원을 시작하고, 진단입원 중에 다른 기관 전문의가 추가로 진단해 2명 이상의 소견이 일치하면 치료입원으로 넘어간다.'
ps[1].runs[0].text='치료입원의 2명 가운데 1명 이상은 국공립 또는 지정 정신의료기관 소속이어야 한다.'
script(7)
p.save('v222.pptx')
