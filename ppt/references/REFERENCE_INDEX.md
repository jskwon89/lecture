# PPT 최종·성숙 참조본 인덱스

갱신: 2026-09-21
새 PPT의 콘텐츠·정보위계·밀도와 강의 흐름을 참고하기 위한 인덱스다.

## 사용 원칙

- 새 PPT를 설계할 때 가장 가까운 참조본을 먼저 확인한다.
- 참조본은 디자인과 화면 구성의 기준이지 사실관계의 절대 기준은 아니다.
- 현재 사용자 지시·`PPT_RULES.md`·`PPT_CONTENT_RULES.md`·원자료가 참조본보다 우선한다.
- `FINAL`은 사용자가 최종 확정한 것에만 사용한다.
- 최종 확정 여부가 불명확하거나 다른 과목의 덱이지만 참조 가치가 있으면 `MATURE_REFERENCE` 또는 `LEGACY_REFERENCE`로 둔다.
- 최신 분석을 읽더라도 그 분석이 지적한 잔여 오류와 미검증 그래프를 자동으로 승인하지 않는다.

## 완성본 기반 콘텐츠 참조

| 문서 | 상태 | 주로 볼 것 |
|---|---|---|
| `COMPLETED_DECK_PATTERN_W2_W3_W4_20260921.md` | **CURRENT PRIMARY CONTENT REFERENCE** | 2·3주차 완성본과 4주차 최신61쪽의 목차·자료 유형·국내 사례·제도와 서비스·주장/근거·그래프·중복 관리. 새 주차 설계 시 먼저 읽는다. |
| `W4_REFERENCE_MANIFEST_20260921.md` | **CURRENT W4 SNAPSHOT / SOURCE INVENTORY** | 현재61쪽·7단원·4쟁점의 파일 해시와 61쪽별 역할. 실제 구현과 제안만 된 수정, 그래프 보류사항 구별. |
| `COMPLETED_DECK_PATTERN_W2_W3_20260919.md` | PRESERVED W2/W3 DETAIL / PREVIOUS PRIMARY | 기존 2·3주차 세부 분석은 보존한다. 전체 새 주차 적용은 위 최신 통합 분석을 먼저 보고, 이 문서는 상세 사례 확인에 쓴다. |
| `COMPARATIVE_EFFECT_SLIDE_DESIGN_LESSONS_20260919.md` | SUPPORTING CONTENT REFERENCE | 논제 선택지→처우유형→결과축, 한 장 한 논리, 결합형 분리. ‘근거수준 대칭’은 최신 콘텐츠 규칙에 따라 수치 비교와 논거 비교를 구별한다. |

국내 우선 조사: `../DOMESTIC_FIRST_RESEARCH_PROTOCOL.md`.
필수 적용규칙: `../PPT_CONTENT_RULES.md`.

## 현재 프로젝트형 참조

| 주제 | 경로·식별 | 상태 | 주로 볼 것 |
|---|---|---|---|
| 2주차 사형제 v28(6) | `examples/w2_death_penalty_v28_6_parsed.md` | MATURE_REFERENCE (PRE-V8 GEOMETRY) | 제목·밴드의 역할·행머리글·출처·대본 구조·장 간 연결만 참고. 좌표·여백·색상값·각주 y·제목 pt는 참고 금지. |
| 2주차 완성본50쪽 / 3주차 완성본85쪽 | 통합 분석 §0 및 W4 대장의 해시표 | COMPLETED-DECK CONTENT REFERENCES | 실제 강의 흐름·이론/법/사례/연구의 역할·종합 방식. 원본 파일이 Git에 자동 등록된 것으로 가정하지 않는다. |
| 4주차 최신61쪽 | `W4_REFERENCE_MANIFEST_20260921.md` | CURRENT REFERENCE SNAPSHOT | 국내 제도·사건·실행조건과 치료내용을 구체화하는 방식, 네 쟁점의 주장·근거 회수. 전면 사실검증 완료본은 아님. |
| 청소년/성인 접촉경로 별도1쪽 | 같은 대장의 §6 | DRAFT GRAPH — DATA QA HOLD | 그래프 제시 요구의 예시. 범주 합산·0값·출처 재확인 전에는 수치 참조로 사용하지 않는다. |

## Git 바이너리 참조 덱

| 주제 | 경로 | 상태 | 주로 볼 것 |
|---|---|---|---|
| 범죄예방 최종 발표자료 | `legacy/crime_prevention_final.pptx` | LEGACY_REFERENCE | 완성 덱의 전반적 시각밀도·도해 사용·슬라이드 연결 |
| 합리적 선택·일상활동이론 | `legacy/rational_choice_routine_activity.pptx` | LEGACY_REFERENCE | 간결한 강의 덱의 제목·도식·본문 밀도 |
| W4 제5장 시작 당시37쪽 | `../handoffs/week4_juvenile_drugs_20260919/artifacts/w4_ch1_v14.pptx` | HISTORICAL WORKING BASELINE | 당시 제작 경과만 참조. 현재7단원·61쪽의 목차로 사용하지 않는다. |

## 골격

- `../templates/skeleton_types_parsed.md` — 화면 유형별 승인 골격의 파싱본.
- 골격의 정확한 좌표·색·폰트는 `PPT_RULES.md`와 `tools/` 코드가 우선한다.
- 이번 콘텐츠·조사 업데이트는 도구 코드와 디자인 좌표를 바꾸지 않는다.

## 최종본 등록

경찰대학 「범죄·공공안전세미나Ⅱ」의 주차별 최종 PPTX/PDF/대본은 사용자가 FINAL로 확정한 버전부터 `../finals/`에 순차 등록한다. 확정 전 파일을 FINAL로 부르지 않는다. 페이지 대장에 이름을 기록한 것과 원본 바이너리를 Git에 업로드한 것은 구별한다.

## 공개 저장소 주의

저장소가 public이므로 개인·민감정보, 배포권이 없는 원문, 폰트 파일은 등록하지 않는다.
