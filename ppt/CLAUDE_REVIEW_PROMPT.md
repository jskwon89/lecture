# Claude PPT 규칙 감사 프롬프트

Repository: `jskwon89/lecture`
Branch: `master`
Scope: `ppt/`

당신은 이 저장소에서 실제 PowerPoint를 제작하는 담당자 관점으로 **PPT 제작 규칙·도구·참조본의 독립 감사**를 수행한다. 규칙을 새로 취향대로 바꾸지 말고, 현재 Canonical이 기존 소스와 실제 제작도구를 빠짐없이 흡수했는지 검증한다.

## 1. 반드시 읽을 순서

1. `ppt/README.md`
2. `ppt/PPT_RULES.md`
3. `ppt/PPT_WORKFLOW.md`
4. `ppt/RULE_SOURCE_MAP.md`
5. `ppt/source_rules/guideline_v11_1_20260918.md`
6. `ppt/source_rules/standard_structure_v4_20260918.md`
7. `ppt/source_rules/ops_handbook_v4.md`
8. `ppt/source_rules/courseplan_reconciliation_20260901-2.md`
9. `ppt/tools/README.md`
10. `ppt/tools/pptlib.py`, `rowfit.py`, `layout.py`, `check_spacing.py`
11. `ppt/templates/skeleton_types_parsed.md`
12. `ppt/references/REFERENCE_INDEX.md`와 등록된 참조 덱(특히 `legacy/*.pptx`, `examples/w2_death_penalty_v28_6_parsed.md`)

## 2. 감사 목표

### A. 누락
- 기존 소스에 있었는데 `PPT_RULES.md`에서 빠진 강제규칙이 있는가.
- 화면 문안·제목·밴드·행·한정줄·출처·대본·노트·QA 중 빠진 영역이 있는가.
- 법령·판례·통계·여론조사·연구·사례별 검증 규칙이 빠지지 않았는가.

### B. 충돌
- `guideline_v11_1`의 과거 규칙과 현재 Canonical이 충돌하는 지점을 모두 찾는다.
- 특히 **제목 규칙**을 확인한다. 현재 Canonical은 다음이 최신이다.
  - 제목은 간결한 표제형 핵심내용을 우선한다.
  - 문맥상 자명한 대상·조건은 반복하지 않는다.
  - 주체는 필요할 때만 실제 행위의 주체를 쓴다.
  - 연구자가 만든 실험조건을 제도 자체의 행위처럼 쓰지 않는다.
- 이 최신 규칙을 과거 11.1판의 `주체를 반드시 맨 앞` 규칙으로 되돌리지 않는다.

### C. 실제 제작 가능성
- `PPT_RULES.md`의 디자인 숫자가 `pptlib.py`, `rowfit.py`, `layout.py`, `check_spacing.py`와 실제로 맞는가.
- `skeleton_types_parsed.md`의 유형 구조와 `ppt/tools/`의 좌표·색·행 규칙을 조합해 실제 덱을 만들 수 있는가. 원본 `skeleton_types.pptx`가 작업환경에 따로 있으면 추가 대조한다.
- 폰트 파일은 저장소에 없어도 되며, Pretendard Regular/Bold 설치가 전제임을 확인한다.

### D. 콘텐츠 품질
- 화면만 보아도 핵심 사실·작동방식·결과·논제 관계가 이해된다는 규칙이 충분히 강한가.
- 연구 장에서 대상/비교/결과의 위계를 분리하는 규칙이 구현 가능하게 쓰였는가.
- 비교집단의 실제 처우를 생략하지 않는가.
- %/%p/hazard/OR 등 통계량을 학생이 오해하지 않도록 설명하는가.
- 직접성이 낮은 연구를 핵심근거처럼 쓰지 않도록 되어 있는가.

### E. 참조 덱
- 참조 덱에서 실제로 반복되는 디자인 특성이 Canonical과 일치하는지 확인한다.
- 참조 덱의 오래된 문구나 예외를 규칙으로 승격하지 않는다.

## 3. 보고 형식

1. **PASS / NEEDS PATCH**
2. Canonical에서 잘 보존된 규칙
3. 누락 규칙 — 원문 파일·근거 위치와 함께
4. 충돌 규칙 — 어떤 문장이 어느 문장을 supersede하는지
5. 도구코드와 문서의 불일치
6. 참조 덱과 Canonical의 디자인 불일치
7. 수정이 필요한 경우 **구체적인 파일별 패치안**
8. 수정 후 Claude가 실제 PPT를 만들 때 읽을 최소 파일 세트

중요: 누락이나 충돌이 있더라도 임의로 `master`를 수정하지 말고, 먼저 감사 결과와 패치안을 보고한다.
