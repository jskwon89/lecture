_pre=open('e121.py').read().split('# ================= 35')[0].replace("Presentation('v120.pptx')","Presentation('v212.pptx')")
exec(_pre)
from pptx.util import Inches,Pt
from pptx.dml.color import RGBColor
from lxml import etree
A='http://schemas.openxmlformats.org/drawingml/2006/main'
def T(n,start):
    sl=p.slides[n-1]; assert one(sl,'title').text_frame.text.startswith(start); return sl
def find(sl,name,sub): return [s for s in sl.shapes if s.name==name and s.has_text_frame and sub in s.text_frame.text][0]
def paras(sh,items):
    ps=sh.text_frame.paragraphs; assert len(ps)==len(items)
    for q,t in zip(ps,items):
        for r in q.runs[1:]: r._r.getparent().remove(r._r)
        q.runs[0].text=t
# 21
sl=T(21,'임세원')
for sub in ('자·타해','보호의무자가'):
    q=find(sl,'row-text',sub).text_frame.paragraphs[1]; r=q.runs[0]; t=r.text; k=t.index('있었다.')+4
    assert t.startswith('전에는')
    r2=copy.deepcopy(r._r); r._r.addnext(r2)
    r.text=t[:k]; r2.find('{%s}t'%A).text=t[k:]
    rp=r._r.find('{%s}rPr'%A); rp.set('b','1')
    sf=rp.find('{%s}solidFill'%A); sf[0].set('val','1E2761')
    h=etree.SubElement(rp,'{%s}highlight'%A); c=etree.SubElement(h,'{%s}srgbClr'%A); c.set('val','FFE699'); sf.addnext(h)
# 40
sl=T(40,'미국')
paras(find(sl,'box','①  응급 보호'),['①  응급 보호','위험한 정신질환자를 동의 없이 시설에 머물게 한다.','요건: 정신질환 때문에 자신이나 다른 사람에게 위험할 것(모든 주). 최대 기간은 72시간이 가장 흔하다.'])
script(40)
# 48
sl=T(48,'정신질환자의 타해')
m=one(sl,'meaning'); m.top=Inches(5.58); m.height=Inches(0.9)
setp(m,[('위험 있음으로 분류된 정신질환자 가운데 89%는 1년 안에 폭력범죄를 저지르지 않았다.',0),
        ('예측의 정확도: 위험한 사람과 그렇지 않은 사람을 구별하는 정도는 높았다(c 지수 0.89, 95% 신뢰구간 0.85~0.93). 실제로 폭력범죄를 저지른 사람의 62%가 위험 있음으로 분류돼 있었다.',1)])
script(48)
# 50
sl=T(50,'법원의 업무량')
m=one(sl,'meaning'); m.top=Inches(5.56); m.height=Inches(1.1)
setp(m,[('추계 방법: ① 2023년 최초 입원심사 약 3만 건 + 연장심사 약 3만 건',1),('② 최초 입원 약 3만 건 − 심사 전에 퇴원하는 22%(6,600건)',1),('③ 재심사 추정 607건 + 인신보호청구 1,465건',1),
        ('비자의입원 전체를 대상으로 한 연간 추계다. 대상을 타해 위험이 있는 사람으로 좁히면 사건 수는 이보다 적다.',1)])
script(50)
p.save('v213.pptx')
