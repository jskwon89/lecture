_pre=open('e121.py').read().split('# ================= 35')[0].replace("Presentation('v120.pptx')","Presentation('v211.pptx')")
exec(_pre)
from pptx.util import Inches,Pt
from pptx.dml.color import RGBColor
def pos(s,x,y,w,h): s.left=Inches(x); s.top=Inches(y); s.width=Inches(w); s.height=Inches(h)
def T(n,start):
    sl=p.slides[n-1]; assert one(sl,'title').text_frame.text.startswith(start),one(sl,'title').text_frame.text; return sl
def find(sl,name,sub): return [s for s in sl.shapes if s.name==name and s.has_text_frame and sub in s.text_frame.text][0]
def paras(sh,items):
    # 기존 문단 서식을 유지하면서 글만 바꾼다(문단 수가 같을 때)
    ps=sh.text_frame.paragraphs; assert len(ps)==len(items),(len(ps),items)
    for q,t in zip(ps,items):
        for r in q.runs[1:]: r._r.getparent().remove(r._r)
        q.runs[0].text=t

# ---- 2 오늘 볼 것
sl=p.slides[1]
tb=[s for s in sl.shapes if getattr(s,'has_table',False) and s.has_table][0].table
def cell(c,t):
    q=c.text_frame.paragraphs[0]
    for r in q.runs[1:]: r._r.getparent().remove(r._r)
    q.runs[0].text=t
for r,pg in zip(list(tb.rows)[4:],['36쪽','43쪽','47쪽','51쪽']): cell(r.cells[2],pg)
cell(list(tb.rows)[4].cells[1],'독일 바이에른·프랑스·호주 뉴사우스웨일스주·미국')
cell(list(tb.rows)[5].cells[1],'헌재 결정, 과잉금지원칙')
cell(list(tb.rows)[6].cells[1],'타해 위험의 판단, 심사 기관의 유형, 법원의 업무량')

# ---- 17 책임·비용
sl=T(17,'지금은 누가')
c=find(sl,'cell-text','입원비도'); paras(c,['입원 결정의 책임','입원비를 지자체가 부담할 수 있다'])
m=one(sl,'meaning'); paras(m,[m.text_frame.paragraphs[0].text,m.text_frame.paragraphs[1].text,
 '행정·응급입원의 본인부담금은 국가와 지자체가 부담할 수 있다(제80조). 서울시는 2023년(11월 보고 기준) 행정입원 290건에 약 2억 4,400만 원을 지원했다. 지자체의 비용 부담 때문에 행정입원을 꺼린다는 지적이 있었다(2019).'])
script(17)

# ---- 21 임세원
sl=T(21,'임세원')
paras(find(sl,'step-text','② 퇴원 뒤'),['② 퇴원 뒤','치료가 이어지지 않음','2017년 1월에도 임 교수에게 진료를 받았다. 그 뒤 외래치료를 제대로 받지 않았다고 보도됐다.'])
paras(find(sl,'step-text','④ 2019.4'),['④ 2019.4','법 개정(임세원법)','퇴원 통보(2019.10 시행)와 외래치료지원(2020.4 시행)을 고쳤다.'])
for s in sl.shapes:
    y=s.top/I
    if s.name=='step-panel': s.height=Inches(1.68)
    elif s.name=='step-text': s.height=Inches(1.61)
    elif s.name=='flow-arrow': s.top=Inches(3.12)
    elif s.name=='rule' and abs(y-4.62)<0.02: s.top=Inches(4.22)
    elif s.name=='rule' and abs(y-5.60)<0.02: s.top=Inches(5.40)
    elif s.name in('row-label','row-text') and abs(y-4.62)<0.02: s.top=Inches(4.22); s.height=Inches(1.18)
    elif s.name in('row-label','row-text') and abs(y-5.62)<0.02: s.top=Inches(5.41); s.height=Inches(1.18)
r1=find(sl,'row-text','자·타해'); r2=find(sl,'row-text','보호의무자가')
setp(r1,[('자·타해 행동으로 입원한 환자는 본인이 동의하지 않아도 퇴원 사실을 센터에 알릴 수 있게 했다.',0),
 ('전에는 본인의 동의를 받아야 알릴 수 있었다. 개정 뒤에는 치료를 중단하면 증상이 급격히 나빠질 우려가 있다고 전문의가 진단하면, 본인에게 미리 알린 뒤 통보한다. 본인이 거부하면 정신건강심사위원회의 심사를 거쳐야 통보할 수 있다.',1),
 ('실적: 2021년 퇴원환자 약 37,000명 가운데 12,892명(35%)의 퇴원 사실이 통보됐다.',1)])
setp(r2,[('보호의무자가 동의하지 않아도 외래치료를 청구할 수 있게 했다.',0),
 ('전에는 병원장이 보호의무자의 동의를 받아야 청구할 수 있었다. 개정 뒤에는 동의가 없어도 청구할 수 있고, 치료를 중단한 사람을 발견한 정신건강복지센터장도 지자체장에게 청구할 수 있다.',1),
 ('실적: 2020~2022년 외래치료지원은 전국에서 모두 116건이었다.',1)])
script(21)

# ---- 22 진주
sl=T(22,'진주')
cp=one(sl,'case-point'); paras(cp,[cp.text_frame.paragraphs[0].text,'보호입원은 가족이 문의했지만 절차가 시작되지 않았고, 경찰은 적극적인 보호조치를 하지 않았다.'])
script(22)

# ---- 23 공통점
sl=T(23,'세 사건의 공통점')
c=find(sl,'step-text','임세원 교수 사건'); ps=[q.text for q in c.text_frame.paragraphs]
paras(c,[ps[0],'① 2017년 1월 진료 뒤 치료가 이어지지 않았다.',ps[2]])
c=find(sl,'step-text','② 위험 신호'); ps=[q.text for q in c.text_frame.paragraphs]
paras(c,ps[:3]+['· 응급개입팀 확대: 5개 시도(2019) → 34개 팀(2023)'])
script(23)

# ---- 24 행정입원 미연계
sl=T(24,'의뢰 뒤')
settext(find(sl,'c-title','516건'),'전국 · 2019년 1~7월 · 의뢰 2,178건 중 이어지지 않은 516건의 이유')
script(24)

# ---- 26 부적합
sl=T(26,'입원적합성심사의 조사')
m=one(sl,'meaning'); paras(m,['부적합 사유는 증빙서류 미비가 33.6%로 가장 많았고, 치료 필요성과 자·타해 위험이 불명확한 경우가 20.8%였다.',m.text_frame.paragraphs[1].text])
script(26)

# ---- 35 반대 의견 + 장애인권리위원회
sl=T(35,'비자의입원 자체')
settext(one(sl,'message'),'당사자·가족단체는 누가 심사하는가와 관계없이 비자의입원 자체에 반대했고, 유엔 장애인권리위원회도 한국에 비자의입원 조항의 폐지를 권고했다.')
for s in sl.shapes:
    y=s.top/I
    if s.name=='step-panel' and y<3: s.height=Inches(2.00)
    elif s.name=='step-text' and y<3: s.height=Inches(1.94)
    elif s.name=='step-panel': pos(s,s.left/I,4.52,5.75,1.72)
    elif s.name=='step-bar' and y>4: s.top=Inches(4.52)
    elif s.name=='step-text': pos(s,s.left/I,4.58,5.38,1.66)
setp(find(sl,'step-text','이유 ①'),[('이유 · 공동대책위원회 2019.2, 한국정신장애인연합회 등 2026.10',0),('비자의입원은 낙인을 키우고 치료를 피하게 한다',1),
 ('2019 성명: 법원 판결에 의한 비자의입원은 정신질환자를 잠재적 범죄자로 보는 낙인을 키운다.',2),('2026 성명: 입원이 확대되면 낙인이 커지고, 치료를 피하게 된다.',2)])
setp(find(sl,'step-text','이유 ②'),[('유엔 장애인권리위원회 · 2022.9 · 한국에 대한 권고',0),('비자의입원을 허용하는 법 조항을 폐지하라',1),
 ('장애와 ‘인식된’ 자·타해 위험성을 근거로 입원시키는 조항이 대상이다.',2),('누가 심사하는가보다 입원의 근거를 문제 삼았다.',2)])
script(35)

# ---- 36 4장 표지 목차
sl=p.slides[35]; settext(find(sl,'toc-item','미국'),'미국: 응급 보호 뒤 법원이 결정하는 입원')

# ---- 38 프랑스
sl=T(38,'프랑스')
paras(find(sl,'box','경찰이 부른'),['의사의 진단서를 근거로 도지사가 결정한다. 입원할 병원의 정신과 의사는 이 진단서를 쓸 수 없다.','급박하면 시장이 먼저 임시 조치를 하고 24시간 안에 도지사에게 알린다.'])
mbg=one(sl,'meaning-bg'); m=one(sl,'meaning')
pos(mbg,0.80,6.10,11.73,0.58); pos(m,1.05,6.10,11.23,0.58)
setp(m,[('차이: 프랑스는 12일 안에 법원이 결정하고, 정부 검토안은 최대 4주 입원한 뒤에 재판한다(신권철 2025).',1),
        ('프랑스 법원은 2023년 정기 심사 81,512건 가운데 5,039건(6.2%)에서 입원을 해제했다.',1)],sizes={1:12.5})
for q in m.text_frame.paragraphs:
    for r in q.runs: r.font.color.rgb=RGBColor.from_string('1E2761')
script(38)

# ---- 43 5장 표지, 44·45·47 칩
sl=p.slides[42]; settext(find(sl,'toc-item','유엔'),'과잉금지원칙의 네 단계')
for n in (44,45,47):
    c=one(p.slides[n-1],'chip-text'); settext(c,c.text_frame.text.replace('55·58쪽','53·56쪽').replace('58쪽','56쪽'))
sl=T(45,'헌재 결정 뒤')
m=one(sl,'meaning'); m.top=Inches(5.80); m.height=Inches(0.84)
ps=[q.text for q in m.text_frame.paragraphs]
setp(m,[(ps[0],0),(ps[1],1),('유엔 자유권위원회(2023)와 고문방지위원회(2024)는 한국에 비자의입원에 대한 보호장치(사법심사 포함)를 보장하라고 권고했다.',1)])
nxt(45,'과잉금지원칙의 네 단계와 사법입원제'); script(45)

# ---- 48 6장 표지
sl=p.slides[47]
settext(find(sl,'toc-item','임상가'),'정신질환자의 타해 위험 판단: 평가도구의 폭력범죄 예측')
settext(find(sl,'toc-item','프랑스'),'심사하는 기관에 따라 달라지는가: 결정 기관의 유형과 비자의입원율')

# ---- 49 타해 위험 예측: 평가도구만
sl=T(49,'정신질환자의 타해')
for s in list(sl.shapes):
    if s.name.startswith(('def-','step-')) and s.left/I<6.5: rm(s)
settext(one(sl,'message'),'평가도구가 폭력 위험이 있다고 분류한 정신질환자 가운데, 1년 안에 실제로 폭력범죄를 저지른 사람은 11%였다.')
for s in sl.shapes:
    if s.name=='def-panel': pos(s,0.80,2.34,11.73,1.30)
    elif s.name=='def-bar': pos(s,0.80,2.34,0.06,1.30)
    elif s.name=='def-text': pos(s,1.04,2.34,11.3,1.30)
    elif s.name in('step-panel','step-bar','step-text'):
        i=0 if s.left/I<9 else 1; x=0.80+i*5.98
        if s.name=='step-panel': pos(s,x,3.78,5.75,1.70)
        elif s.name=='step-bar': pos(s,x,3.78,5.75,0.07)
        else: pos(s,x+0.18,3.85,5.39,1.63)
d=one(sl,'def-text')
setp(d,[('평가도구의 분류 · Fazel 등(2017) · 스웨덴 전국 자료',0),('조현병 스펙트럼·양극성장애 환자 75,158명을 진료·퇴원 뒤 1년 동안 추적했다.',1),
        ('분류: 계산한 1년 내 폭력범죄 확률이 5% 이상이면 폭력 위험 있음',1),('폭력: 공식 기록에 남은 폭력범죄(연구 대상 가운데 1%)',1)])
m=one(sl,'meaning'); pos(m,0.80,5.62,11.73,0.62)
r2=[s for s in sl.shapes if s.name=='rule' and abs(s.top/I-6.36)<0.02][0]; rm(r2)
setp(m,[('위험 있음으로 분류된 정신질환자 가운데 89%는 1년 안에 폭력범죄를 저지르지 않았다.',0)])
script(49)

# ---- 50 next
nxt(50,'법원의 업무량')

# ---- 52 법원의 업무량
sl=T(52,'법원의 업무량')
settext(one(sl,'message'),'사법정책연구원 연구(신권철 2025)는 2023년 실적을 바탕으로, 누가 먼저 심사하느냐에 따라 법원이 맡는 사건이 연간 약 6만 건에서 약 2천 건까지 달라진다고 추계했다.')
m=one(sl,'meaning')
paras(m,['추계 방법: ①은 2023년 최초 입원심사 약 3만 건과 연장심사 약 3만 건의 합, ②는 3만 건에서 심사 전에 퇴원하는 22%를 뺀 값, ③은 재심사 추정 607건과 인신보호청구 1,465건의 합이다.',
         '비자의입원 전체를 대상으로 한 연간 추계다. 대상을 타해 위험이 있는 사람으로 좁히면 사건 수는 이보다 적다.'])
script(52)

# ---- 58 쟁점 ④ 근거
sl=T(58,'쟁점 ④')
NEW='[연구] 평가도구가 폭력 위험이 있다고 분류한 정신질환자 중 1년 안에 폭력범죄를 저지른 비율은 11%였다(Fazel, 2017).'
tb=[s for s in sl.shapes if getattr(s,'has_table',False) and s.has_table][0].table
k=0
for r in tb.rows:
    for c in r.cells:
        for q in c.text_frame.paragraphs:
            if 'Lidz' in q.text:
                for x in q.runs[1:]: x._r.getparent().remove(x._r)
                q.runs[0].text=NEW; k+=1
for q in sl.notes_slide.notes_text_frame.paragraphs:
    if 'Lidz' in q.text and q.text.startswith('[연구]'):
        for x in q.runs[1:]: x._r.getparent().remove(x._r)
        q.runs[0].text=NEW; k+=1
print('쟁점④ 교체',k)


# ==== 보정
sl=T(17,'지금은 누가'); m=one(sl,'meaning'); m.top=Inches(5.84)
ps=[q.text for q in m.text_frame.paragraphs]
paras(m,ps[:2]+['행정·응급입원의 본인부담금은 국가와 지자체가 부담할 수 있다(제80조). 서울시는 2023년 행정입원 290건에 약 2억 4,400만 원을 지원했다. 지자체의 비용 부담 때문에 행정입원을 꺼린다는 지적이 있었다(2019).'])
script(17)
sl=T(21,'임세원')
for s in sl.shapes:
    y=s.top/I
    if s.name=='step-panel': s.height=Inches(1.90)
    elif s.name=='step-text': s.height=Inches(1.83)
    elif s.name=='flow-arrow': s.top=Inches(3.23)
    elif s.name=='rule' and abs(y-4.22)<0.02: s.top=Inches(4.40)
    elif s.name=='rule' and abs(y-5.40)<0.02: s.top=Inches(5.50)
    elif s.name in('row-label','row-text') and abs(y-4.22)<0.02: s.top=Inches(4.41); s.height=Inches(1.08)
    elif s.name in('row-label','row-text') and abs(y-5.41)<0.02: s.top=Inches(5.51); s.height=Inches(1.08)
sl=T(23,'세 사건의 공통점')
c=find(sl,'step-text','임세원 교수 사건'); ps=[q.text for q in c.text_frame.paragraphs]
paras(c,[ps[0],'① 2017.1 진료 뒤 치료가 끊어졌다.',ps[2]]); script(23)
sl=T(38,'프랑스')
paras(find(sl,'box','입원할 병원의'),['의사의 진단서를 근거로 도지사가 결정한다.','급박하면 시장이 먼저 임시 조치를 하고 도지사에게 알린다.']); script(38)
for n in (45,52):
    for s in list(p.slides[n-1].shapes):
        if s.name=='rule' and 6.2<s.top/I<6.5: rm(s)
# ---- 46·51 → 보충자료
ids=p.slides._sldIdLst; L=list(ids)
assert one(p.slides[45],'title').text_frame.text.startswith('유엔의 권고') and one(p.slides[50],'title').text_frame.text.startswith('프랑스 법원은')
a,b=L[45],L[50]
for mv,lab in ((a,'보충자료  유엔의 권고'),(b,'보충자료  프랑스 법원의 해제 비율')):
    ids.remove(mv); list(ids)[-1].addnext(mv)
    last=p.slides[len(p.slides)-1]; settext(one(last,'chapter'),lab)
    for x in list(last.shapes):
        if x.name in('next','chip','chip-text'): rm(x)
d=[s for s in p.slides if any(x.name=='title' and x.text_frame.text=='보충자료' for x in s.shapes)][0]
settext([x for x in d.shapes if x.name=='message'][0],'후견 관련 법원 절차, 인신보호 구제 사건, 심사 업무량의 산식, 법원 심사의 대상, 유엔의 권고, 프랑스 법원의 해제 비율을 살펴본다.')
p.save('v212.pptx')
for i,s in enumerate(p.slides,1):
    t=[x for x in s.shapes if x.name=='title']
    if i>=43: print(i,t[0].text_frame.text if t else '')
