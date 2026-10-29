# 자료조사·강의 PPT 지침 통합 반영 내역

기준일: 2026-10-29(한국시간)
기준 저장소: `jskwon89/lecture` · `master`
작업 시작 커밋: `08deb8977aa95be8f184632b7d0d159122d0d225` (2026-10-22)
작업 지시: 이번 작업에서 수정·정정한 지점과 방식을 총괄해 지침으로 정리하고 Git에 반영하되 중복을 피한다.

## 1. 읽는 순서와 단일 관리 위치

[자료조사·강의 PPT 작업 안내](../../current/README.md)에서 단계별 본문으로 이동한다. 기존 규칙을 복제한 새 종합 규칙집은 만들지 않았다. 실제 규칙은 조사 절차, 콘텐츠, 제작·검수, 학기 운영 문서에서 각각 관리한다.

## 2. 사용자 정정과 이번 반영

| 사용자 요청·작업에서 드러난 지점 | 반영·정리 위치 | 처리 |
|---|---|---|
| 기존 교수의 약물 이용 성범죄 논제를 그대로 사용 | INITIAL §1, 운영자료집 §3 | 확정 논제 보존. 자료 수급 편의로 입법 논제로 바꾸지 않음 |
| 반대의견을 찾는 과정이 시험의 핵심 | INITIAL §1, CONTENT §6 | 직접 반대 주장·인접 논거·구성 논증을 구별해 탐색 |
| 찬반을 모두 조사하므로 자기 입장·반론을 일률적으로 요구하지 않음 | 운영자료집 §3, WORKFLOW §9 | 이번 중간평가의 작성 방식과 평가표 교체 |
| 학부 수준의 간단한 다섯 평가항목 | 운영자료집 §3 | 논제·쟁점 이해 / 찬반 논거 정리 / 자료 적절성 / 논리 연결성 / 구성·전달력 |
| 논제·평가표·분량·제출양식을 PPT로 안내 | 운영자료집 §3, 학기 운영 정합성 문서 | 안내용 표 공개 범위를 명시하고 형식·마감 대조 |
| W9 뒤의 네 쟁점을 제한 필요/불필요 판단에 맞춤 | CONTENT §7, WORKFLOW §2-2, AUDIT §3-1 | 앞 자료→쟁점 근거를 재대조. 반대자에게 대안 선택·완성을 자동 요구하지 않음 |
| 내용에 기반한 쟁점 추가·수정, 중복·부적절 자료 검토 | AUDIT §3-1, 기존 CONTENT §2-3·§11 | 새 질문·실제 근거가 있는 제안만 분리. 네 개는 W9의 출발점 |
| Taylor의 단계별 연도·사실 확인 | CONTENT §2-2 | 청구·증거심리·심급별 판단과 증거의 기준 시점을 따로 확인 |
| Ortiz의 ‘심리 거부’를 이해할 수 있게 설명 | CONTENT §2-2 | 하급심 주문·이유, 상급심 심사 범위, 개별 법관 의견을 나눔 |
| 법령·판결·보고서의 원문 대조 | DOMESTIC §4-3·§8-3, CONTENT §4-5 | 문장·수치별 대조, 조문·법안 버전·시점 확인 |
| 확인 가능한 것은 진행하고 접근 안 되는 것은 링크 제공 | DOMESTIC §4-3 | 실제 열람 범위와 남은 질문·정확한 접근 경로 기록 |
| 주택/사람 분모, 단계별 사건 수, 연구 결과 해석 | CONTENT §8 | 관찰 시점·단위·선별 조건·측정 지표·표본 중복을 보존 |
| 영상 링크 재요청·주소·길이 | DOMESTIC §5-1 | 직접 재생 링크·길이·활용 구간·고정 ID로 관리 |
| 실제 강의안 쪽수와 수정 상태 확인 | WORKFLOW §2-2, 기존 CONTENT §1·§11 | 실제 표시 순서로 쪽수 확정. 제안/파일 반영/원문 확인을 구별 |
| 화면·대본·제목·말투·중복 처리 방식 | 기존 CONTENT §4-2-1–§4-2-3, SCREEN_FIRST_REVIEW | 재서술 없이 기존 규칙 연결. 제목 관련 잔여 충돌만 정정 |

INITIAL = WEEK_INITIAL_BUILD_PROTOCOL, CONTENT = PPT_CONTENT_RULES, DOMESTIC = DOMESTIC_FIRST_RESEARCH_PROTOCOL, WORKFLOW = PPT_WORKFLOW, AUDIT = PROPOSITION_ALIGNMENT_AUDIT_TEMPLATE. 모두 `ppt/` 아래의 Markdown 문서다.

## 3. 중복·충돌·적용 범위

- **기존 규칙 재사용:** 국내 우선 조사, 실제 논쟁에서 쟁점 도출, 화면 단독 이해, 전할 말→대본→화면, 같은 핵심어, 명사형 제목·메시지 띠, 방어문 처리, 페이지별 검수, 렌더 QA, 기능에 따른 중복 축소, 제안/실제 반영 상태 구별.
- **충돌 수정:** CONTENT §2-4와 WORKFLOW §5의 옛 제목 문구를 2026-10-22 현행 기준에 맞췄다. 양쪽 실제 논쟁 확인 게이트가 확정된 시험 논제 변경으로 이어지지 않도록 범위를 명시했다. 찬반 표현 제한에는 사용자 확정 논제·평가표의 입장 구별을 허용했다.
- **학기·과제 한정:** 이번 중간평가의 다섯 항목 각20점은 해당 과제에 적용한다. 분량·마감·평가 비율은 학기 운영 문서에서 관리한다. 기말 통합평가의 별도 기준을 사용자가 새로 확정했다고 기록하지 않으며, 이번 변경을 자동 확대하지 않았다.
- **W9 한정:** 쟁점 네 개를 모든 강의의 고정 개수로 만들지 않는다. v41 검토안은 검토 제안이다. 그 안의 페이지별 삭제·이동·정확한 쟁점 문구 전부를 사용자 확정으로 올리지 않았다.
- **검증 범위:** 이번 작업은 지침 통합이다. Taylor·Ortiz·Miller·AB 767 등의 날짜·결론·수치, 강의자료의 남은 원문 검증을 새로 완료한 것으로 표시하지 않았다.
- **자료 보존:** 공개 Git에는 원문 PDF·유료 문헌·피해자 세부정보·폰트·작업 임시파일을 추가하지 않았다. 기존 PPTX·계획서 PDF·디자인 도구는 수정하지 않았다.

## 4. 파일 목록

수정 13개:

- `ppt/AGENTS.md`
- `ppt/README.md`
- `ppt/current/README.md`
- `ppt/PPT_CONTENT_RULES.md`
- `ppt/PPT_WORKFLOW.md`
- `ppt/DOMESTIC_FIRST_RESEARCH_PROTOCOL.md`
- `ppt/WEEK_INITIAL_BUILD_PROTOCOL.md`
- `ppt/PROPOSITION_ALIGNMENT_AUDIT_TEMPLATE.md`
- `ppt/RULE_SOURCE_MAP.md`
- `ppt/PPT_RULES.md`
- `ppt/CHANGELOG.md`
- `ppt/source_rules/ops_handbook_v4.md`
- `ppt/source_rules/courseplan_reconciliation_20260901-2.md`

추가 3개:

- `ppt/handoffs/research_ppt_review_20261029/FILE_CHANGES.md` — 이 반영 내역
- `ppt/handoffs/research_ppt_review_20261029/VALIDATION.md` — 검증 범위와 결과
- `ppt/handoffs/research_ppt_review_20261029/MANIFEST.sha256` — 변경 문서 해시

삭제 파일 없음. 변경이력 문구는 [CHANGELOG의 2026-10-29 항목](../../CHANGELOG.md)에 기록했다.
