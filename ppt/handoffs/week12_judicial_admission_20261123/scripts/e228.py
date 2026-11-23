_pre=open('e121.py').read().split('# ================= 35')[0].replace("Presentation('v120.pptx')","Presentation('v227.pptx')")
exec(_pre)
from pptx.util import Inches
S=list(p.slides)
s16,s42,s43,s44,s45,s46=S[15],S[41],S[42],S[43],S[44],S[45]
assert one(s44,'title').text_frame.text.startswith('2016년 헌재') and one(s43,'title').text_frame.text=='법리'
# --- 합친 쪽(44)
settext(one(s44,'title'),'2016년 헌재 결정: 독립적·중립적인 제3자의 판단')
settext(one(s44,'message'),'헌재는 2016년 구법의 보호입원에 독립적·중립적인 제3자의 판단이 없다고 보았다. 현행법은 입원적합성심사위원회를 두어 답했고, 사법입원제는 그 제3자가 법원이어야 한다는 제안이다.')
settext(one(s44,'chapter'),one(s16,'chapter').text_frame.text)
settext(one(s44,'chip-text'),'쟁점 ①·④ · 52·55쪽')
cs=sorted([s for s in s44.shapes if s.name=='step-text'],key=lambda s:s.left)
for c in cs: print([q.text for q in c.text_frame.paragraphs])
def card(c,lines):
    ps=c.text_frame.paragraphs
    while len(c.text_frame.paragraphs)>len(lines):
        q=c.text_frame.paragraphs[-1]; q._p.getparent().remove(q._p)
    while len(c.text_frame.paragraphs)<len(lines):
        e=copy.deepcopy(c.text_frame.paragraphs[-1]._p); c.text_frame.paragraphs[-1]._p.addnext(e)
    for q,t in zip(c.text_frame.paragraphs,lines):
        for r in q.runs[1:]: r._r.getparent().remove(r._r)
        q.runs[0].text=t
card(cs[0],['① 헌재의 판단 · 2016.9','구법의 보호입원은 헌법불합치','가족 2명과 전문의 1명의 판단만으로 입원','입원을 통제하는 장치 부족'])
card(cs[1],['② 헌재가 든 이유','신체의 자유를 지나치게 제한','공정성을 담보할 장치와 불복제도 부족','침해의 최소성·법익의 균형성 위반'])
card(cs[2],['③ 헌재가 요구한 것','제3자의 판단','1. 입원 관계자로부터 독립적일 것','2. 중립적일 것','절차의 예로 진술 기회, 불복, 사법심사를 들었다.'])
card(cs[3],['④ 현행법의 답 · 2017.5 시행','현행 정신건강복지법','1. 전문의 2명 이상의 진단','2. 입원적합성심사위원회 심사'])
m=one(s44,'meaning')
card(m,['따질 것: 입원적합성심사위원회는 헌재가 요구한 독립적·중립적인 제3자인가, 그 제3자는 법원이어야 하는가?',
 '헌재는 개정법이 문제를 해소했는지에 대한 판단을 뒤로 남겼다(2014헌가9). 유엔 자유권위원회(2023)와 고문방지위원회(2024)는 한국에 사법심사를 포함한 보호장치를 보장하라고 권고했다.'])
script(44)
settext(one(s44,'next'),one(s16,'next').text_frame.text)
settext(one(s16,'next'),'다음 → 2016년 헌재 결정이 요구한 것: 독립적·중립적인 제3자의 판단')
settext(one(s42,'next'),'다음 → 연구와 운영')
# --- 이동
ids=p.slides._sldIdLst; L=list(ids)
e16,e43,e44,e45,e46=L[15],L[42],L[43],L[44],L[45]
ids.remove(e44); e16.addnext(e44)
for e,sl,lab in ((e45,s45,'보충자료  헌재 결정 뒤의 현행법'),(e46,s46,'보충자료  과잉금지원칙의 네 단계')):
    ids.remove(e); list(ids)[-1].addnext(e); settext(one(sl,'chapter'),lab)
    for x in list(sl.shapes):
        if x.name in('next','chip','chip-text'): rm(x)
p.part.drop_rel(e43.rId); ids.remove(e43)
# --- 장 번호
for sl in p.slides:
    for x in sl.shapes:
        if x.name=='chapter':
            t=x.text_frame.text
            if t.startswith('6  연구'): settext(x,'5'+t[1:])
            elif t.startswith('7  쟁점'): settext(x,'6'+t[1:])
            elif t in('6','7') and one(sl,'title').text_frame.text in('연구와 운영','쟁점과 최종 판단'): settext(x,str(int(t)-1))
        if x.name=='meaning' and '19쪽의 번호다' in x.text_frame.text:
            for q in x.text_frame.paragraphs:
                for r in q.runs: r.text=r.text.replace('19쪽의 번호다','20쪽의 번호다')
        if x.name=='message' and x.text_frame.text.startswith('후견 관련 법원 절차'):
            settext(x,'후견 관련 법원 절차, 인신보호 구제 사건, 심사 업무량의 산식, 법원 심사의 대상, 유엔의 권고, 프랑스 법원의 해제 비율, 헌재 결정 뒤의 현행법, 과잉금지원칙의 네 단계를 살펴본다.')
# --- 2쪽 표
tb=[s for s in p.slides[1].shapes if getattr(s,'has_table',False) and s.has_table][0].table
rows=list(tb.rows); assert '법리' in rows[5].cells[0].text
rows[5]._tr.getparent().remove(rows[5]._tr)
rows=list(tb.rows)
def ct(c,t): c.text_frame.paragraphs[0].runs[0].text=t
ct(rows[1].cells[1],'현행 입원 절차, 2016년 헌재 결정, 법원이 관여하는 방식')
for r,pg in zip(rows[2:],['21쪽','28쪽','36쪽','45쪽','50쪽']): ct(r.cells[2],pg)
ct(rows[5].cells[0],rows[5].cells[0].text.replace('6','5',1)); ct(rows[6].cells[0],rows[6].cells[0].text.replace('7','6',1))
p.save('v228.pptx')
for i,s in enumerate(p.slides,1):
    c=[x for x in s.shapes if x.name=='chapter']; t=[x for x in s.shapes if x.name=='title']; n=[x for x in s.shapes if x.name=='next']
    if i in(2,3,16,17,18,21,28,36,43,44,45,50,51,52,55,56) or i>56: print(i,c[0].text_frame.text if c else '','|',t[0].text_frame.text if t else '','|',n[0].text_frame.text if n else '')
print([c.text for r in tb.rows for c in r.cells])
print([x.text_frame.text for x in p.slides[2].shapes if x.name=='toc-item'])
