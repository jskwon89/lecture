# CURRENT RULESET — READ THIS FIRST

기준일: 2026-09-23

이 폴더는 **현재 실제 작업에 적용할 규칙만 가리키는 진입점**이다. 규칙 본문을 중복 복사하지 않는다. 중복 복사본이 생기면 서로 다른 버전으로 갈라질 수 있기 때문이다.

## 현재 적용 순서

1. `../README.md` — 전체 진입점
2. `../PPT_CONTENT_RULES.md` — 최신 콘텐츠·조사 추가규칙
3. `../PPT_RULES.md` — Canonical v1.7 전문·디자인·QA
4. `../PPT_WORKFLOW.md` — 실제 작업절차·하드게이트
5. `../RULE_SOURCE_MAP.md` — 충돌·우선순위·supersede
6. `../DOMESTIC_FIRST_RESEARCH_PROTOCOL.md` — 국내우선 조사
7. `../WEEK_RESEARCH_COVERAGE_TEMPLATE.md` — 12개 자료유형 + 통계 5축
8. `../PROPOSITION_ALIGNMENT_AUDIT_TEMPLATE.md` — 논제 정합성 중간감사
9. `../source_rules/standard_structure_v4_20260918.md` — 현행 표준구조 보조규칙
10. `../source_rules/ops_handbook_v4.md` — 과목 운영·논증·토론 보조규칙
11. `../source_rules/courseplan_reconciliation_20260901-2.md` — 평가·제출물 화면에서만 운영 정합성 확인
12. **실제 화면 부품·그래프·표·흐름을 만들 때** `../templates/layout_kit/README.md`와 `CANONICAL_COMPATIBILITY.md` — Canonical을 읽은 뒤 보조 구현도구로 사용

## 절대 적용하지 말 것

- `../archive/` 아래의 모든 파일은 **이력·감사용 창고**다.
- `guideline_v8`, `v9`, `v10`, `v11.1`의 본문에 ‘유일한 현행 지침’이라고 적혀 있어도 **현재 효력이 없다**.
- 과거 파일을 읽어야 할 때는 변경이력·결정근거 확인 목적으로만 연다.

## 현재 규칙의 한 문장 정의

> 현재 작업은 `PPT_CONTENT_RULES + PPT_RULES + PPT_WORKFLOW`를 핵심으로 하고, `standard_structure_v4` 등은 보조규칙으로 적용한다. 과거 guideline 버전은 적용하지 않는다.

## 양식 키트의 지위

`templates/layout_kit/`은 현행 규칙을 대체하지 않는 **구현 부품 라이브러리**다. 표·그래프·흐름·텍스트 부품과 예시 조합을 재사용할 수 있지만, 디자인 값이나 자동 맞춤이 Canonical과 충돌하면 `PPT_RULES.md`가 우선한다.


2026-09-22 사용자 승인으로 행 결론·보충 글자 크기, 본문 묶음의 행 내 배치, 제목 오른쪽 칩 미사용을 Canonical v1.7에 반영했다. `CANONICAL_COMPATIBILITY.md`의 승인 반영 표를 함께 확인하며, 이 세 항목을 이전 Canonical 값으로 되돌리지 않는다.

2026-09-23 사용자 승인으로 **화면 단독 이해·주체/행위 구체화 하드게이트**를 Canonical v1.7에 반영했다. 대본을 가리고도 한 장만으로 주체·행위·대상·조건·결과·논제 연결이 이해되지 않으면 HOLD한다. 원문이 특정하지 않은 사실을 추정해 구체화하지 않는다. 세부 절차는 `PPT_CONTENT_RULES.md` §4-1과 `PPT_WORKFLOW.md`의 SCRIPT-HIDDEN TEST를 따른다.


2026-09-23 사용자 승인으로 **주요 공개논의·사법판단 선행 스캔 하드게이트**를 추가했다. 신규 주차·전면 재구성·대규모 보강에서는 목차 전에 국회·정부·법원·경찰·인권위·전문기관 등의 토론회·공청회·숙의/공론화·경청회·공식 의견수렴·기관 권고/회신과 함께 **대법원·각급 법원 판결/결정 및 헌법재판소 결정**을 반드시 먼저 찾는다. 공개논의에서는 실제 입장·근거·반론·실행조건을, 사법판단에서는 사건번호·쟁점·주문·핵심 판시·논제 적용범위를 추출한다. 두 맵이 완성되기 전 목차를 최종 승인하지 않는다.


2026-09-23 사용자 승인으로 **페이지 로컬 메시지 우선·논제 연결 반복 금지**를 추가했다. 구성안에는 모든 장의 논제 역할을 기록하지만, 학생 화면에는 단원 시작·전환·종합 또는 자료를 판단축으로 회수하는 장에서만 논제 연결을 필요한 만큼 보인다. 상단·하단은 각 페이지 본문에서 직접 도출되는 핵심을 우선한다.
