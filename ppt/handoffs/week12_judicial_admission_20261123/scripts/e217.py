_pre=open('e121.py').read().split('# ================= 35')[0].replace("Presentation('v120.pptx')","Presentation('v216.pptx')")
exec(_pre)
def paras(sh,items):
    ps=sh.text_frame.paragraphs; assert len(ps)==len(items),(len(ps),items)
    for q,t in zip(ps,items):
        for r in q.runs[1:]: r._r.getparent().remove(r._r)
        q.runs[0].text=t
sl=p.slides[42]; assert one(sl,'title').text_frame.text.startswith('입원부터 법원')
OLD='입원부터 법원 심사까지 걸리는 기간'; NEW='입원한 뒤 법원이 결정하기까지 걸리는 기간'
for s in p.slides:
    for sh in s.shapes:
        if sh.has_text_frame and OLD in sh.text_frame.text and sh.name in('title','next'): settext(sh,sh.text_frame.text.replace(OLD,NEW))
c=[s for s in sl.shapes if s.name=='step-text' and '바이에른' in s.text_frame.text][0]
paras(c,['독일 바이에른 · 긴급입원','다음 날','다음 날 말까지 법원이 결정','결정이 없으면 퇴원'])
settext(one(sl,'message'),'먼저 입원한 사람의 입원 여부를 법원이 정하는 데, 바이에른은 다음 날까지, 프랑스는 12일까지 걸린다. 오스트리아는 4일 안에 법원이 환자를 만나 입원을 잠정적으로 허용할지 정한다.')
m=one(sl,'meaning'); ps=[q.text for q in m.text_frame.paragraphs]
paras(m,['법원이 심사하는 세 나라에서는 입원한 다음 날에서 12일 사이에 법원이 첫 결정을 한다. 한국의 1개월보다 훨씬 이르다.',ps[1]])
script(43)
p.save('v217.pptx')
