# CURRENT RULESET — READ THIS FIRST

기준일: 2026-09-22

이 폴더는 **현재 실제 작업에 적용할 규칙만 가리키는 진입점**이다. 규칙 본문을 중복 복사하지 않는다. 중복 복사본이 생기면 서로 다른 버전으로 갈라질 수 있기 때문이다.

## 현재 적용 순서

1. `../README.md` — 전체 진입점
2. `../PPT_CONTENT_RULES.md` — 최신 콘텐츠·조사 추가규칙
3. `../PPT_RULES.md` — Canonical v1.6 전문·디자인·QA
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


2026-09-22 사용자 승인으로 행 결론·보충 글자 크기, 본문 묶음의 행 내 배치, 제목 오른쪽 칩 미사용을 Canonical v1.6에 반영했다. `CANONICAL_COMPATIBILITY.md`의 승인 반영 표를 함께 확인하며, 이 세 항목을 이전 Canonical 값으로 되돌리지 않는다.
