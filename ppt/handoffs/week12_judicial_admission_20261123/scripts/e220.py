_pre=open('e121.py').read().split('# ================= 35')[0].replace("Presentation('v120.pptx')","Presentation('v219.pptx')")
exec(_pre)
from pptx.util import Inches
S=p.slides
assert one(S[26],'title').text_frame.text.startswith('범죄자 집계')
# 2장 표지: 3번째 항목 삭제
c2=S[19]
for x in list(c2.shapes):
    if x.name in('toc-num','toc-item') and abs(x.top/I-4.71)<0.02: rm(x)
settext(one(c2,'message'),'필요한 보호가 이루어지지 않은 사례와 요건을 갖추지 않은 입원은 무엇을 보여주는가?')
# 6장 표지: 첫 항목으로 추가, 나머지 아래로
c6=S[47]
for x in c6.shapes:
    if x.name in('toc-num','toc-item'): x.top=Inches(x.top/I+0.58)
for x in c6.shapes:
    if x.name=='toc-num': settext(x,str(int(round((x.top/I-3.55)/0.58))+1))
src=[x for x in S[19].shapes if x.name=='title'][0]
ref_n=[x for x in c6.shapes if x.name=='toc-num'][0]; ref_i=[x for x in c6.shapes if x.name=='toc-item'][0]
for r,t in ((ref_n,'1'),(ref_i,'범죄자 집계에서 정신장애계가 차지한 비율')):
    e=copy.deepcopy(r._element); c6.shapes._spTree.append(e); n=[q for q in c6.shapes if q._element is e][0]; n.top=Inches(3.55); settext(n,t)
settext(one(c6,'message'),'범죄자 가운데 정신장애계의 비율은 어떠하고, 정신질환자의 타해 위험은 얼마나 정확히 판단되며, 법원이 심사하면 무엇이 달라지고 어떤 부담이 생기는가?')
settext(one(c6,'next'),'다음 → 범죄자 집계에서 정신장애계가 차지한 비율')
# 이동
ids=p.slides._sldIdLst; L=list(ids); mv=L[26]; ids.remove(mv); list(ids)[46].addnext(mv)
S=p.slides
m=S[47]; assert one(m,'title').text_frame.text.startswith('범죄자 집계')
settext(one(m,'chapter'),one(S[48],'chapter').text_frame.text)
settext(one(m,'next'),'다음 → 정신질환자의 타해 위험 예측은 얼마나 맞는가')
settext(one(S[25],'next'),'다음 → 국내 논의')
settext(one(S[38],'next'),'다음 → 미국: 응급 보호 뒤 법원이 결정하는 입원')
# 2쪽 표
tb=[s for s in S[1].shapes if getattr(s,'has_table',False) and s.has_table][0].table
for r,pg in zip(list(tb.rows)[3:7],['27쪽','35쪽','43쪽','47쪽']):
    r.cells[2].text_frame.paragraphs[0].runs[0].text=pg
for r in tb.rows: print([c.text for c in r.cells])
p.save('v220.pptx')
for i,s in enumerate(p.slides,1):
    if 19<=i<=50: print(i,one(s,'chapter').text_frame.text if [x for x in s.shapes if x.name=='chapter'] else '','|',one(s,'title').text_frame.text,'|',one(s,'next').text_frame.text)
S=p.slides
settext(one(S[37],'next'),'다음 → 미국: 응급 보호 뒤 법원이 결정하는 입원')
settext(one(S[38],'next'),'다음 → 해외 사례로 본 정신질환자 비자의입원 심사의 세 유형')
rows=list(tb.rows)
rows[2].cells[1].text_frame.paragraphs[0].runs[0].text='국내 사건과 입원·심사 통계'
rows[6].cells[1].text_frame.paragraphs[0].runs[0].text='범죄자 중 정신장애계, 타해 위험의 판단, 심사 기관의 유형, 법원의 업무량'
p.save('v220.pptx')
print([one(S[i],'next').text_frame.text for i in (37,38)])
c6=p.slides[46]
for x in c6.shapes:
    if x.name in('toc-num','toc-item'): x.top=Inches(x.top/I+0.30)
p.save('v220.pptx')
