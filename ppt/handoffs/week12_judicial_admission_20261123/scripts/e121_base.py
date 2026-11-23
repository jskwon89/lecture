import copy
from pptx import Presentation
from pptx.util import Pt, Inches
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
p=Presentation('v120.pptx')
I=914400
def at(sl,name,x,y):
    for s in sl.shapes:
        if s.name==name and abs(s.left/I-x)<0.03 and abs(s.top/I-y)<0.03: return s
    raise Exception((name,x,y))
def one(sl,name): 
    r=[s for s in sl.shapes if s.name==name]; assert len(r)==1,(name,len(r)); return r[0]
def setp(sh, items, tmpl=None, sizes=None):
    """items: [(text, role)] role = 서식을 빌릴 기존 문단 번호"""
    src=(tmpl or sh).text_frame.paragraphs
    T=[copy.deepcopy(q._p) for q in src]
    body=sh.text_frame._txBody
    for q in list(sh.text_frame.paragraphs): body.remove(q._p)
    for text,role in items:
        e=copy.deepcopy(T[min(role,len(T)-1)]); body.append(e)
    for q,(text,role) in zip(sh.text_frame.paragraphs,items):
        for r in q.runs[1:]: r._r.getparent().remove(r._r)
        q.runs[0].text=text
        if sizes and role in sizes: q.runs[0].font.size=Pt(sizes[role])
def settext(sh,t,size=None):
    q=sh.text_frame.paragraphs[0]; q.runs[0].text=t
    if size: q.runs[0].font.size=Pt(size)
def fill(sh,hexv): sh.fill.solid(); sh.fill.fore_color.rgb=RGBColor.from_string(hexv)
def rm(sh): sh._element.getparent().remove(sh._element)
def script(n, addsrc=None):
    sl=p.slides[n-1]; lines=[]
    order=[s for s in sl.shapes if s.has_text_frame and s.name not in('chapter','next','title','source')]
    order.sort(key=lambda s:(0 if s.name=='message' else 1 if s.name=='chip-text' else 2, round(s.top/I,1), s.left))
    for s in order:
        for q in s.text_frame.paragraphs:
            if q.text.strip(): lines.append(q.text)
    tf=sl.notes_slide.notes_text_frame; ps=tf.paragraphs
    assert ps[0].text.startswith('[낭독 대본]')
    tm=copy.deepcopy(ps[1]._p); end=None
    for q in ps[1:]:
        t=q.text
        if t.startswith('[출처') or t.startswith('(v') or t.startswith('[이전'): end=q; break
        q._p.getparent().remove(q._p)
    lines=[lines[0],'']+lines[1:]+['']
    if addsrc and end is not None and end.text.startswith('[출처'):
        pass
    for t in lines:
        e=copy.deepcopy(tm); end._p.addprevious(e)
        from pptx.text.text import _Paragraph
        q=_Paragraph(e,end._parent)
        for r in q.runs[1:]: r._r.getparent().remove(r._r)
        if q.runs: q.runs[0].text=t
    if addsrc:
        for q in tf.paragraphs:
            if q.text.startswith('[출처와 확인 위치]'):
                e=copy.deepcopy(tm); q._p.addnext(e)
                qq=_Paragraph(e,q._parent)
                for r in qq.runs[1:]: r._r.getparent().remove(r._r)
                qq.runs[0].text=addsrc; break
def nxt(n,t): settext(one(p.slides[n-1],'next'),'다음 → '+t)

# ================= 35
sl=p.slides[34]
settext(one(sl,'message'),'2024년 검토안은 초기 입원을 최대 4주로 늘리고, 그 뒤의 계속 입원을 법원이 재판으로 결정하는 구조다.')
XS=[0.8,3.81,6.82,9.82]; TX=[0.98,3.99,6.99,10.0]
A=[('①','입원 신청','센터장·의사 등도 신청할 수 있게 넓힌다.'),
   ('②','초기 입원: 최대 4주','전문의 1명의 진단으로 2주, 다른 전문의 1명의 진단으로 2주 더 입원한다.'),
   ('③','위원회가 조사하고 재판 청구','입원적합성심사위원회가 조사한 뒤 법원에 재판을 청구한다.'),
   ('④','법원이 재판으로 결정','대면 재판이 원칙이고, 절차조력인이 환자의 입장을 대변한다.')]
B=[('현행','입원 신청','보호입원은 보호의무자 2명, 행정입원은 전문의나 전문요원이 신청한다.'),
   ('현행','진단입원: 2주 이내','2주 안에 전문의 2명의 진단이 일치해야 계속 입원한다.'),
   ('현행','위원회가 서류로 심사','입원적합성심사위원회가 1개월 안에 결과를 통지한다.'),
   ('현행','법원의 심사 없음','병원장·지자체장이 최초 3개월까지 입원시킨다.')]
DY=0.24; DB=2.0
panels=[at(sl,'step-panel',x,2.36) for x in XS]; bars=[at(sl,'step-bar',x,2.36) for x in XS]; txts=[at(sl,'step-text',x,2.42) for x in TX]
arrows=[s for s in sl.shapes if s.name=='flow-arrow']
tree=panels[0]._element.getparent()
for i in range(4):
    for s in (panels[i],bars[i],txts[i]):
        e=copy.deepcopy(s._element); tree.append(e)
for s in arrows: tree.append(copy.deepcopy(s._element))
new=list(sl.shapes)[-(12+len(arrows)):]
for i in range(4):
    fill(panels[i],'FBF3DC'); fill(bars[i],'C2A648')
    for s in (panels[i],bars[i],txts[i]): s.top+=int(DY*I)
    setp(txts[i],[(A[i][0],0),(A[i][1],1),(A[i][2],2)],sizes={1:14.5,2:12})
for s in arrows: s.top+=int(DY*I)
k=0
for i in range(4):
    pn,br,tx=new[k],new[k+1],new[k+2]; k+=3
    fill(pn,'F2F4F8'); fill(br,'9AA3BD')
    for s in (pn,br,tx): s.top+=int((DY+DB)*I)
    pn.height=int(1.2*I); tx.height=int(1.14*I)
    setp(tx,[(B[i][1],1),(B[i][2],2)],sizes={1:13.5,2:12})
for s in new[12:]:
    s.top+=int((DY+DB-0.15)*I); fill(s,'9AA3BD')
lab=at(sl,'row-label',0.8,4.15); lab2=at(sl,'row-label',0.8,5.25)
for s,(t,y) in ((lab,('2024년 검토안',2.26)),(lab2,('현행 제도',4.26))):
    s.left=int(0.8*I); s.top=int(y*I); s.width=int(4*I); s.height=int(0.3*I)
    setp(s,[(t,0)]); s.text_frame.paragraphs[0].alignment=PP_ALIGN.LEFT
    from pptx.enum.text import MSO_ANCHOR
    s.text_frame.vertical_anchor=MSO_ANCHOR.MIDDLE
con=at(sl,'row-text',3.45,4.15)
con.left=int(0.8*I); con.top=int(5.86*I); con.width=int(11.73*I); con.height=int(0.46*I)
setp(con,[('달라지는 점: 지금은 법원을 거치지 않고 계속 입원이 정해진다. 검토안에서는 4주 뒤의 계속 입원을 법원이 재판으로 결정한다.',0)],sizes={0:13.5})
rm(at(sl,'row-text',3.45,5.25))
for s in [s for s in sl.shapes if s.name=='rule' and 4.1<s.top/I<5.3]: rm(s)
script(35,'(v121) 아래 칸을 검토안과 현행의 단계별 비교로 교체. 검토안: 신권철 2025 421쪽 표 Ⅴ-4(입원신청 확대, 초기 입원: 전문의 1인 진단 후 입원 2주 + 전문의 추가 1인 진단 후 입원 2주 연장, 입원적합성심사위원회 조사 및 법원에 재판 청구, 법원의 입원 연장 등 결정 재판·대면원칙·절차조력인). "최대 4주"는 2주+2주의 합산값. 표의 병원이송 단계(119구급대 이송, 경찰·보건소·국립정신병원 지원 검토)는 화면에서 생략. 현행: 덱 12~14쪽과 같은 내용(진단입원 2주, 입원적합성심사 1개월 이내 통지, 최초 3개월), 신청권자는 신권철 2025 표 Ⅴ-5. 확인일 2026-11-19')

# ================= 36
sl=p.slides[35]
settext(one(sl,'message'),'네 안 모두 입원이 시작된 뒤에 법원이 심사한다. 차이는 법원이 언제 결정하고, 어디까지 심사하는가이다.')
C=[(1.02,['김상희안 · 2018.5','입원 6일째까지 결정','언제: 신고 뒤 72시간 안에 환자를 만나고, 입원 6일째까지 결정한다.','무엇을: 입원 초기의 심사만. 연장과 퇴원 청구는 정신건강심사위원회가 맡는다.']),
   (4.01,['윤일규안 · 2019.1','최대 2주 입원한 뒤 심사','언제: 최대 2주 입원한 뒤','무엇을: 계속 입원, 입원 연장, 외래치료명령']),
   (7.0,['김재경안 · 2019.7','1개월 안에 결과 통지','언제: 응급입원 3일 안에 신고를 받고, 1개월 안에 결과를 통지한다.','무엇을: 입원과 입원 연장']),
   (10.0,['정부 검토안 · 2024.10','초기 입원(최대 4주) 뒤 재판','언제: 2주 입원에 2주를 연장한 뒤','무엇을: 계속 입원. 입원적합성심사위원회가 청구한 사건만 심사한다.'])]
for x,t in C:
    s=at(sl,'step-text',x,2.41); setp(s,[(t[0],0),(t[1],1),(t[2],2),(t[3],2)])
setp(one(sl,'meaning'),[('공통점: 법원의 결정이 나오기 전에 입원이 먼저 시작된다.',0),
    ('차이: 윤일규안과 김재경안은 연장도 법원이 심사한다. 김상희안은 초기만 맡고, 정부 검토안은 연장 심사를 누가 맡는지 밝히지 않았다.',1)])
NT37='법원 심사의 대상: 정부는 누구를 대상으로 검토했는가'
nxt(36,NT37); script(36,'(v121) 칸을 언제·무엇을 두 줄로 통일하고 프랑스·현행 비교 줄을 삭제. 정부 검토안의 연장 심사 주체 미상: 신권철 2025 422~423쪽(입원연장심사를 법원이 담당하는지 명확한 내용이 나타나지 않음). 확인일 2026-11-19')

# ================= 37
sl=p.slides[36]
settext(one(sl,'title'),NT37)
settext(one(sl,'message'),'법무부는 2023년에 타해 우려가 큰 일부 중증 정신질환자를, 2024년 정부 검토안은 보호입원과 행정입원 전체를 대상으로 삼았다.')
for nm,x,y in (('step-panel',0.8,2.4),('step-bar',0.8,2.4),('step-text',1.02,2.47)): rm(at(sl,nm,x,y))
for (px,tx),(nx) in (((4.8,5.02),0.8),((8.79,9.01),6.79)):
    pn=at(sl,'step-panel',px,2.4); br=at(sl,'step-bar',px,2.4); t=at(sl,'step-text',tx,2.47)
    for s in (pn,br): s.left=int(nx*I); s.width=int(5.74*I)
    t.left=int((nx+0.22)*I); t.width=int(5.3*I)
t=at(sl,'step-text',1.02,2.47)
setp(t,[('법무부의 검토 발표 · 2023.8',0),('타해 우려가 큰 일부 중증 정신질환자',1),
        ('서현역 사건 다음 날, 법관의 결정으로 입원시키는 제도를 검토한다고 발표했다.',2),
        ('국무총리 담화(2023.8.23)가 밝힌 목적은 적기 치료였다.',2),
        ('법원이 언제 심사하는지는 발표에 나오지 않았다.',2)])
t=at(sl,'step-text',7.01,2.47)
setp(t,[('정부 검토안 · 2024.10',0),('보호입원과 행정입원 전체',1),
        ('보호입원과 행정입원을 구분하지 않고 같은 절차를 적용한다.',2),
        ('그 가운데 입원적합성심사위원회가 청구한 사건만 법원이 심사한다.',2),
        ('입원 사유가 타해 위험인지 치료 필요성인지로 대상을 나누지 않는다.',2)])
script(37,'(v121) 세 법률안 칸 삭제, 두 칸 보완. 법무부 발표의 심사 시점 미정: 34쪽 노트(구체적 사전·사후 시한 미확정). 국무총리 담화 2023.8.23(적기에 치료가 이루어질 수 있도록). 확인일 2026-11-19')

# ================= 38 (40쪽 제목 변경 반영)
NT40='법원이 아닌 기관에 심사를 맡기자는 제안'
sl=p.slides[37]; t=at(sl,'step-text',5.02,2.57)
setp(t,[('반응 ② · 40쪽',0),(NT40,1),('새 심사기구를 만들자는 제안과 현행 입원적합성심사위원회를 보완하자는 제안',2),('인권위, 정제형, 학회, 김예지안',2)])
settext(one(sl,'meaning'),'법원이 아닌 기관을 제안한 의견(②)과 강제입원을 줄이자는 주장(③)은 사법입원제에 반대하는 논거가 된다.')
script(38)

# ================= 39
sl=p.slides[38]
L1=at(sl,'step-text',0.98,2.62); L2=at(sl,'step-text',0.98,4.54)
R1=at(sl,'step-text',6.97,2.62); R2=at(sl,'step-text',6.97,3.9); R3=at(sl,'step-text',6.97,5.18)
setp(L1,[('20대 국회 전문위원 검토 · 2018~2019',0),('부당한 입원·연장의 감소',1),
   ('지금의 두 위원회는 서류 위주로 심사해 환자가 직접 진술할 기회가 없다. 법원이 환자를 대면해 심사하면 부당한 입원과 연장이 줄어든다.',2),
   ('김상희안은 심사 기간을 1개월에서 6일로 줄인다.',2)])
setp(L2,[('이건수 · 2023 기고',0),('공정한 판단과 안전 보호',1),
   ('법원이 부당한 목적의 입원을 통제하고 의료적 판단의 한계를 보완한다. 인력·시설 부담이 있더라도 생명·신체 보호와 공정한 절차를 위해 도입하자고 주장했다.',2)])
setp(R3,[('준비되지 않은 기반',1),
   ('입원적합성심사위원회를 도입한 지 1년이고, 법원 심사를 뒷받침할 물적 토대가 갖춰지지 않았다(보건복지부 2019).',2)],tmpl=R1)
setp(R1,[('형식적 심사',1),
   ('판사는 정신건강 전문가가 아니어서 전문가 의견에 좌우될 수 있고, 맡는 사건이 많으면 심리가 형식에 그친다(국회 전문위원 검토 2019).',2)])
setp(R2,[('낙인과 치료 회피',1),
   ('입원 환경이 열악한데 법원의 결정까지 더해지면 낙인과 두려움이 커져, 치료를 늦추거나 피하게 된다(제철웅 2023, 공동대책위원회 2019).',2)])
nxt(39,NT40)
script(39,'(v121) 설명 문장을 구체화. 신권철 2025 233쪽(두 위원회 서면심사 위주·대면진술권 미보장, 윤일규안 검토: 부당한 강제입원·연장 감소 기대), 234쪽(김상희안 검토: 심사 기간 현행 1개월에서 6일로 단축 / 김재경안 검토: 판사는 정신건강 전문가가 아니어서 전문가 의견에 좌우될 가능성, 판사 1인당 사건이 많으면 심리 형식화), 235쪽(보건복지부: 입원적합성심사위원회 도입 1년, 물적 토대 미완비, 신중검토). 이건수·제철웅 기고는 이 쪽 노트의 기존 요약을 따름. 확인일 2026-11-19(올려 주신 PDF 직접 확인)')

# ================= 40
sl=p.slides[39]
settext(one(sl,'title'),NT40)
settext(one(sl,'message'),'법원 대신 독립된 심사기구를 새로 만들자는 제안과, 현행 입원적합성심사위원회를 보완하자는 제안이 있었다.')
D=[(1.02,['국가인권위원회 · 2022.7','새 기구: 독립적인 준사법적 심사기구','입원적합성심사위원회와 정신건강심사위원회를 하나로 합치자.','서류가 아닌 대면 심사를 원칙으로 하자.']),
   (4.01,['정제형 변호사 · 2026.6','새 기구: 복지부 산하 정신건강심판위원회','독립적·중립적 기관으로 두 심사위원회를 하나로 합치자.','3명이 2주 안에 심사한다.','이유: 현행 심사의 독립성 부족, 서류 중심 심사']),
   (7.0,['대한신경정신의학회 · 2023','법원 또는 정신건강심판원(새 기구)','가족이 아니라 국가가 입원을 결정하자. 보호의무자 입원을 폐지하자.','이유: 환자의 건강·생명, 사회의 안전, 가족의 부담']),
   (10.0,['김예지안 · 2025.9','현행 기관의 보완: 지자체장의 결정과 입원적합성심사위원회의 심사','보호·동의입원을 폐지하고 행정입원으로 모은다.','가족이 맡던 입원 책임을 공공으로 옮기고, 입원적합성심사를 보완한다.','법원 심사는 사건 부담 때문에 형식적으로 흐를 수 있다고 보았다.'])]
for x,t in D:
    s=at(sl,'step-text',x,2.47); setp(s,[(t[0],0),(t[1],1)]+[(u,2) for u in t[2:]],sizes={1:14.5})
script(40,'(v121) 제목과 묶음을 새 기구 신설/현행 보완으로 정리하고 칸 순서를 인권위·정제형·학회·김예지안으로 변경. 정제형 100쪽(3인 구성·2주 안 심사), 김예지안(가족이 맡던 입원 책임을 공공으로, 현행 입원적합성심사 보완)은 이 쪽 노트의 기존 확인 기록을 따름. 확인일 2026-11-19')

# ================= 41
sl=p.slides[40]
settext(one(sl,'message'),'당사자·가족단체는 2019년 국회 공청회 성명과 2026년 발표에서 강제입원 축소와 지역사회 지원을 요구했고, 이유로 낙인과 치료 회피를 들었다.')
TL=at(sl,'step-text',0.98,2.42); TR=at(sl,'step-text',6.96,2.42); BL=at(sl,'step-text',0.98,4.46); BR=at(sl,'step-text',6.96,4.46)
setp(TL,[('요구 ① · 공동대책위원회 2019.2, 이한결 2026',0),('강제입원을 줄이거나 없애자',1),
   ('2019 성명: 윤일규안을 철회하고, 응급입원·응급치료 외의 강제입원·치료를 없애자.',2),
   ('2026 이한결(당사자 단체 경기우리도 이사장): 장애를 이유로 한 입원을 폐지하자. 법원 판단에 의한 입원에도 반대했다.',2)])
setp(TR,[('요구 ② · 공동대책위원회 2019.2, 한국정신장애인연합회 등 2026.10',0),('지역사회 지원을 늘리자',1),
   ('2019 성명: 동료지원·상담·재활과, 생활·취업·치료를 이어갈 서비스를 요구했다.',2),
   ('2026 성명: 지역사회 치료와 위기지원을 촉구했다.',2)],sizes={0:11.5})
setp(BL,[('이유 ① · 공동대책위원회 2019.2',0),('낙인',1),
   ('법원 판결에 의한 강제입원은 정신질환자를 잠재적 범죄자로 보는 낙인을 키운다.',2)])
setp(BR,[('이유 ② · 한국정신장애인연합회 등 2026.10',0),('치료 회피',1),
   ('입원이 확대되면 낙인이 커지고, 치료를 피하게 된다고 우려했다.',2)])
for s in sl.shapes:
    if s.name in('step-panel','step-bar','step-text'):
        y=s.top/I
        if y<3:
            if s.name!='step-bar': s.height+=int(0.36*I)
        else:
            s.top+=int(0.36*I)
            if s.name!='step-bar': s.height-=int(0.36*I)
script(41,'(v121) 칸을 발표 주체별에서 요구 2칸·이유 2칸으로 재배열. 내용은 기존 화면과 같은 자료(공대위 2019.2.8 성명, 이한결 2026, 한국정신장애인연합회 등 2026.10.15 성명). 확인일 2026-11-19')
p.save('v121.pptx')
