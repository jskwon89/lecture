# GPT PPT Layout Experiments

이 폴더는 GPT가 공통 Canonical을 더 안정적으로 구현하기 위한 **실험용 overlay**다.

## 적용 범위

- GPT가 실제 PPT 디자인·배치 작업을 할 때만 추가로 읽는다.
- Claude 및 다른 에이전트의 기본 경로에는 연결하지 않는다.
- `ppt/AGENTS.md`, `ppt/current/README.md`, `ppt/PPT_RULES.md`, `ppt/PPT_WORKFLOW.md`보다 아래 단계다.
- 공통 Canonical과 충돌하면 언제나 Canonical이 우선한다.

## 현재 실험 파일

- `GPT_LAYOUT_EXPERIMENT.md` — 승인된 콘텐츠를 실제 화면 구조로 옮길 때의 GPT 전용 선택 게이트

## 변경 이력

- 2026-09-22: GPT 생성 PPT에서 텍스트박스 기본 외곽선이 검은 네모 상자로 남는 문제를 막기 위해 `GPT_LAYOUT_EXPERIMENT.md`에 **텍스트박스 외곽선 제거 QA**를 추가했다.

## GPT 작업 프롬프트용 한 줄

> GPT는 실제 PPT 디자인·배치 작업에서 공통 Canonical을 읽은 뒤 추가로 `ppt/experiments/gpt/GPT_LAYOUT_EXPERIMENT.md`를 읽고 적용한다. Canonical과 충돌하면 Canonical이 우선한다.

## 승격 원칙

반복 작업에서 효과가 확인된 규칙만 사용자 승인 후 `PPT_WORKFLOW.md` 또는 `PPT_RULES.md`로 승격한다. 효과가 없거나 작업을 경직시키는 규칙은 이 실험 폴더에서만 수정·삭제한다.
