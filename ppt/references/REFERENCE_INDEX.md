# PPT 최종·성숙 참조본 인덱스

새 PPT의 디자인·정보위계·밀도를 참고하기 위한 인덱스다.

## 사용 원칙

- 새 PPT를 설계할 때 가장 가까운 참조본을 먼저 확인한다.
- 참조본은 디자인과 화면 구성의 기준이지 사실관계의 절대 기준은 아니다.
- 현재 사용자 지시·`PPT_RULES.md`·원자료가 참조본보다 우선한다.
- `FINAL`은 사용자가 최종 확정한 것에만 사용한다.
- 최종 확정 여부가 불명확하거나 다른 과목의 덱이지만 디자인 참조 가치가 있으면 `MATURE_REFERENCE` 또는 `LEGACY_REFERENCE`로 둔다.

## 완성본 기반 콘텐츠 참조

| 문서 | 상태 | 주로 볼 것 |
|---|---|---|
| `COMPLETED_DECK_PATTERN_W2_W3_20260919.md` | **PRIMARY CONTENT REFERENCE** | 2·3주차 완성본에서 추출한 목차·내러티브·제목 문법·자료유형별 채우기·종합·보충자료 패턴. **새 주차 콘텐츠 설계 시 먼저 읽는다.** |
| `COMPARATIVE_EFFECT_SLIDE_DESIGN_LESSONS_20260919.md` | **PRIMARY CONTENT REFERENCE — comparative/effect sections** | 비교정책·효과자료에서 논제 선택지→처우유형→결과축 순으로 구조화하는 법, 한 장 한 논리, 최소근거 선택, 결합형 처우 분리, 최종 비교표의 근거수준 대칭화. |

## 현재 프로젝트형 참조

| 주제 | 경로 | 상태 | 주로 볼 것 |
|---|---|---|---|
| 2주차 사형제 v28(6) | `examples/w2_death_penalty_v28_6_parsed.md` | MATURE_REFERENCE (PRE-V8 GEOMETRY) | 제목·밴드의 역할·행머리글·출처·대본 구조·장 간 연결만 참고. **좌표·여백·색상값·각주 y·제목 pt는 참고 금지** |

## Git 바이너리 참조 덱

| 주제 | 경로 | 상태 | 주로 볼 것 |
|---|---|---|---|
| 범죄예방 최종 발표자료 | `legacy/crime_prevention_final.pptx` | LEGACY_REFERENCE | 완성 덱의 전반적 시각밀도·도해 사용·슬라이드 연결 |
| 합리적 선택·일상활동이론 | `legacy/rational_choice_routine_activity.pptx` | LEGACY_REFERENCE | 간결한 강의 덱의 제목·도식·본문 밀도 |

## 골격

- `../templates/skeleton_types_parsed.md` — 화면 유형별 승인 골격의 파싱본.
- 골격의 정확한 좌표·색·폰트는 `PPT_RULES.md`와 `tools/` 코드가 우선한다.

## 최종본 등록

경찰대학 「범죄·공공안전세미나Ⅱ」의 주차별 최종 PPTX/PDF/대본은 사용자가 **FINAL로 확정한 버전부터** `../finals/`에 순차 등록한다. 확정 전 파일을 FINAL로 부르지 않는다.

## 공개 저장소 주의

저장소가 public이므로 개인·민감정보, 배포권이 없는 원문, 폰트 파일은 등록하지 않는다.
