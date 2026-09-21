"""부품 견본: 부품 하나를 한 장에 따로 그려 보관한다. 부품을 고를 때 이 덱을 본다."""
import os, sys
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from core import *
from components import *
from examples import AGE

def page(mod,name,sig):
    s,ry=frame(f'부품 · {mod}',name,band=sig)
    return s,body(ry,gap=0.25)

C=[]
def comp(f): C.append(f); return f

@comp
def _():
    s,b=page('text','header — 열 머리','header(s, box, 제목, 보조줄, bar=색)  → 머리 아래 남은 영역')
    L,Rr=split_h(b.take(1.2)[0],(1,1))
    header(s,L,'일반 소년법원','Traditional Juvenile Court, TJC',GRAYBAR); header(s,Rr,'소년약물치료법원','Juvenile Drug Treatment Court, JDTC',NAVY)
@comp
def _():
    s,b=page('text','meta · note · def_lines — 안내 줄과 정의 줄','meta(s, box, 라벨, 글) · note(s, box, 글) · def_lines(s, box, [(용어, 설명)])')
    b=meta(s,b,'연구대상','12~17세 · DSM-IV 약물남용 또는 의존 기준 충족 · 161명 · 네 조건에 무작위배정')
    b=note(s,b,'집계 기준  참여: 해당 요소에 실제 참석 · 분모는 모두 246명',11.5,SUB)
    def_lines(s,b,[('부정기형','장기와 단기를 정하여 선고하는 소년의 자유형'),('집행유예','선고한 형의 집행을 일정 기간 유예하는 결과')])
@comp
def _():
    s,b=page('text','items — 항목 목록','items(s, box, [항목…], tail=금색 끝줄, rules=구분선, spread=고르게)')
    L,Rr=split_h(b.take(2.4)[0],(1,1))
    items(s,L,['일반 소년법원 절차에서 사건을 처리한다','지역사회에 이미 존재하는 약물치료·상담·서비스를 이용할 수 있다','일부 법원은 JDTC와 비슷한 요소도 부분적으로 운영했다'],tail='치료가 없는 경로는 아니다')
    items(s,Rr,['생명권도 제한의 대상이 될 수 있다고 보았다','사형제도의 존재를 간접적으로 전제한다고 보았다','당시에도 형벌로서 기능을 하고 있다고 판단했다'],rules=True,spread=True)
@comp
def _():
    s,b=page('text','numbered · grid — 번호 목록과 번호 격자','numbered(s, box, [(제목, 설명)], hot=강조번호) · grid(s, box, [(제목, 설명)], cols=2)')
    L,Rr=split_h(b.take(2.4)[0],(45,55))
    numbered(s,L,[('약물 확보','반복 사용이 이어지면 약물을 계속 구해야 한다'),('돈·접근의 문제','약값을 마련하거나 공급자를 계속 찾아야 한다'),('범죄 역할의 확대','판매·운반에 가담하거나 다른 범죄에 연루될 수 있다')],hot=2)
    grid(s,Rr,[('맞춤형 치료 연결','평가 후 근거기반 치료를 개인별로 연결'),('가족 참여','보호자가 치료과정에 참여'),('법원 감독','정기 약물검사와 준수사항 확인'),('완료까지 추적','보상·제재와 수료 여부 확인')])
@comp
def _():
    s,b=page('text','cols3 — 기준 열','cols3(s, box, [(라벨, 핵심, [보충])], main_pt=16)')
    cols3(s,b,[('대상','형사책임이 가능한 14~18세 범죄소년',['소년법상 소년은 19세 미만이다']),('행위','마약류의 위법한 투약·사용',['적법한 의료적 사용은 구분한다']),('비교','무엇을 어느 시점에 우선할 것인가',[])])
@comp
def _():
    s,b=page('text','aligned_lists — 좌우 대조 목록','aligned_lists(s, box, [(제목, 색, 표시개수)], [[항목…], [항목…]])  같은 번째 항목끼리 높이를 맞춘다')
    aligned_lists(s,b.take(3.0)[0],[('다수의견 (합헌 7인)',NAVY_F,7),('반대의견 (위헌 2인)',GOLD_F,2)],[['생명권도 제한의 대상이 될 수 있다고 보았다','사형제도의 존재를 간접적으로 전제한다고 보았다'],['사형은 인간의 존엄과 가치에 반한다','생명 박탈은 기본권의 본질적 내용을 침해한다']])
@comp
def _():
    s,b=page('text','issue_list — 쟁점 목록','issue_list(s, box, [(쟁점명, 질문)])')
    issue_list(s,b.take(3.2)[0],[('책임을 묻는 방식','치료·재활 참여를 먼저 요구하는 것이 적절한가?'),('특별예방','재사용·재범을 줄이는 데 치료를 우선할 근거가 있는가?'),('일반예방','형사처벌 가능성이 낮아지면 다른 청소년의 사용이 늘어날 것인가?'),('치료 여건','필요한 치료를 실제로 제공하고 지속할 수 있는가?')])
@comp
def _():
    s,b=page('text','toc — 목차','toc(s, box, [(단원명, 다루는 것)])')
    toc(s,b.take(3.2)[0],[('청소년 마약류 사용과 현행 대응','논제의 범위 · 연령과 처리 경로'),('실태와 사용 맥락','단속 추이 · 주변 관계 · 도움 요청'),('형사처벌과 보호처분의 운영','처리 통계 · 형 선고 특례'),('주요 논거와 최종 판단','쟁점별 주장과 근거 · 최종 판단')])
@comp
def _():
    s,b=page('tables','row_table — 행머리글 표','row_table(s, box, [(머리글, 결론, [보충], 한정)])  행 높이 고르게 · 본문은 행 가운데')
    row_table(s,b,[('지원이 필요한 환경','가정의 보호를 받기 어렵다는 사정 자체를 이유로 시설처우를 선택하면 더 큰 자유 제한을 받을 수 있다.',['소년이 선택하지 않은 환경을 보호력 부족으로만 평가하지 말아야 한다는 취지다.']),('연구가 제시한 개선','집행기관 확충, 시설 확충, 보호·위탁기관 발굴을 제시했다.'),('논제와의 연결','연령 하향과 보호처분 작동은 서로 다른 정책과제다.',[],'이 자료로 효과의 크기는 말할 수 없다')])
@comp
def _():
    s,b=page('tables','num_table — 수치 표','num_table(s, box, [열 이름], [[값…]], total_col=음영 열)')
    num_table(s,b,['연도','부정기형','집행유예','소년부 송치','무죄','기타','합계'],[[2023,10,5,3,1,4,23],[2024,4,6,3,0,1,14]],total_col=6)
@comp
def _():
    s,b=page('tables',"matrix(style='rules') — 설계 대조표",'matrix(s, box, [열 머리], [(행 머리, [칸…])], shade=음영 열)  위·아래 마감선이 있는 표')
    matrix(s,b.take(2.6)[0],['집단 A · 함께 비교한 집단','집단 B · 실험 집단'],[('청소년에게 제공한 보상',['치료에 출석하면 보상','약물을 사용하지 않은 것이 확인되면 보상']),('부모에게 요청한 활동',['약물 문제와 대응에 관한 정보 교육','약물사용 확인과 보상 적용 방법 훈련'])],shade=1)
@comp
def _():
    s,b=page('tables',"matrix(style='bars') — 두 입장 대조표",'matrix(s, box, [입장…], [(행 머리, [칸…], 굵게)], style=\'bars\', align=\'l\')')
    matrix(s,b.take(3.4)[0],['치료·재활을 먼저 적용하는 입장','형사제재의 필요성을 강조하는 입장'],[('주장',['불참 사유를 먼저 확인하고 참여를 이어가야 한다','중대한 위반이 반복되면 처분을 바꿀 수 있어야 한다'],True),('근거·이유',['치료를 받으라는 요구만으로 참여가 보장되지는 않는다','보호관찰에는 처분 변경 절차가 있다'],False)],head_w=1.55,style='bars',cell_pt=13,align='l')
@comp
def _():
    s,b=page('charts','grouped_bars — 묶음 세로 막대','grouped_bars(s, box, {묶음: [값…]}, [x라벨…], highlight=강조 번호)  폭에 따라 2018 / ’18 / 처음·끝만 표기')
    grouped_bars(s,b.take(3.6)[0],AGE,list(range(2018,2026)),highlight=5,vmax=200)
@comp
def _():
    s,b=page('charts','bars — 세로 막대','bars(s, box, [(라벨, 값)], colors=[…], unit=\'%\', axis_note=주석)')
    L,Rr=split_h(b.take(3.2)[0],(1,1),0.8)
    bars(s,L,[('일반 소년법원',60),('소년약물치료법원',32)],axis_note='공식 법원 행정자료')
    bars(s,Rr,[('출석 보상',18),('단약 보상',50)],colors=[NAVY_F,NAVY])
@comp
def _():
    s,b=page('charts','hbars — 가로 막대','hbars(s, box, [(라벨, 값)], color=색, pitch=행 간격)')
    L,Rr=split_h(b,(1,1),0.8)
    hbars(s,L,[('텔레그램',50.0),('친구·또래',33.3),('유튜브·블로그 등 온라인 콘텐츠',16.7)])
    hbars(s,Rr,[('약국·병의원',64.5),('친구·선후배·직장동료',29.2),('온라인 플랫폼',10.6)],GRAYBAR,SUB)
@comp
def _():
    s,b=page('charts','progress · big_numbers — 진행 막대와 큰 숫자','progress(s, box, [(라벨, 작은 글, %)]) · big_numbers(s, box, [(라벨, 값)])')
    y=progress(s,b.take(1.4)[0],[('첫 개별면담 참여','214/246명',87.0),('첫 집단훈련 참여','98/246명',39.8),('네 요소 전체 완수','47/246명',19.1)],pitch=0.46)
    big_numbers(s,Box(M_L+0.3,y+0.4,M_W-0.3,0.62),[('기존 서비스 + 추가개입','85.7%'),('기존 서비스','83.9%')])
@comp
def _():
    s,b=page('charts','before_after · change_rows — 전후 수치','before_after(s, box, [(제목, 전, 후, 설명)]) · change_rows(s, box, [(이름, 전, 후, 변화, 강조)])')
    y=before_after(s,b,[('예방지원 우선','3.7','4.2','처벌보다 예방 지원책이 우선되어야 한다는 인식'),('중대범죄 증가 인식','4.2','3.9','촉법소년이 중대한 범죄를 저지른다는 인식'),('제도 지식','5.5','6.3','관련 지식 7문항 평균')])
    change_rows(s,Box(M_L,y+0.35,7.0,1.5),[('일반 소년법원','52.0일','39.9일','−12.1일',False),('소년약물치료법원','63.7일','34.7일','−29.0일',True)])
@comp
def _():
    s,b=page('flows','timeline — 세로 타임라인','timeline(s, box, [(날짜, 결론, 보충)], hot=강조 번호)')
    timeline(s,b.take(2.4)[0],[('2004년 6월','소년과 어머니가 약물법원 참여에 동의했다','법원은 치료·검사 의무와 제재를 적은 합의를 승인했다'),('이후','대마검사에서 여러 차례 양성반응이 나왔다','치료프로그램 참여를 중단했다'),('2004년 12월','원심은 간접 형사적 법정모욕을 인정했다','치료 참여 의무를 따르지 않았다는 이유다')])
@comp
def _():
    s,b=page('flows','steps_h · steps_v — 가로 단계와 세로 단계','steps_h(s, box, [(단계, 설명)]) · steps_v(s, box, [문장…], hot=강조 번호)')
    y=steps_h(s,b,[('소년구금시설','10일 수용'),('중독 관련 입소시설','주거형 치료 배치까지 수용'),('주거형 치료','배치 명령')])
    steps_v(s,Box(M_L,y+0.5,6,2.0),['이미 마약을 사용하고 있었다','마약을 계속 구해야 하는 상황','판매·유통에도 가담','상담기관에서 개입'],hot=2)
@comp
def _():
    s,b=page('flows','tree — 분기 흐름도','tree(s, box, [(앞 단계, 설명)…], [(갈래 머리, [항목], 바닥 글)…], hot=강조 갈래)')
    tree(s,b.take(3.9)[0],[('경찰 송치','14~18세 범죄소년 사건'),('검사 판단','중대성 · 재범위험 · 치료 필요 검토')],[('① 조건부 기소유예',['연계모델 참여를 조건으로 공소를 제기하지 않는다'],'검찰 단계에서 끝나는 경로'),('② 소년부 송치',['판사가 보호처분을 심리한다'],'법원이 보호처분을 결정'),('③ 형사기소',['형사법원이 판단한다'],'정식 재판으로 책임을 묻는 경로')],hot=0)
@comp
def _():
    s,b=page('flows','stack_columns — 누적 조합 열','stack_columns(s, box, [(제목, 보조줄, [항목], 추가 항목 수)], group_label=묶음 표시)')
    stack_columns(s,b.take(3.4)[0],[('① 통상 가정법원','Family Court · n=42',['통상 가정법원 절차','지역사회 외래 치료'],0),('② 소년약물법원','Drug Court · n=38',['주 1회 법원 출석','정기 약물검사'],0),('③ + MST','Drug Court + MST · n=38',['②의 법원감독 유지','다체계치료 추가'],1),('④ + MST + CM','n=43',['③ 유지','유관관리 추가'],1)],group_label='소년약물법원 감독이 포함된 세 조건')

if __name__=='__main__':
    for f in C: f(); end_rule(prs.slides[-1])
    save(os.path.join(HERE,'examples','component_catalog.pptx'))
    print('\n'.join(l for l in LOG if '부족' in l or '넘침' in l))
