# layout_kit import status

기준일: 2026-09-22

원본: 사용자 제공 `files(7).zip` 안의 `lecture_layout_kit.zip`

## Git에 등록 완료

- `README.md`
- `COMPONENTS.md`
- `design.py`
- `core.py`
- `fit.py`
- `catalog.py`
- `examples.py`
- `components/__init__.py`
- `components/text.py`
- `components/tables.py`
- `components/charts.py`
- `components/flows.py`
- `HANDOFF_FOR_COMMIT.md`
- `PROJECT_INSTRUCTIONS_BOOTSTRAP.md`
- `CANONICAL_COMPATIBILITY.md`
- `examples/README.md`

원본 Python·Markdown 구현은 커밋 단계에서 내용상 임의 수정하지 않았다. 현행 Canonical과 충돌하는 지점은 별도 호환성 문서에 기록했다.

## 생성 산출물

원본 묶음에는 다음 바이너리가 함께 있었다.

- `examples/component_catalog.pptx`
- `examples/layout_examples.pptx`
- `examples/component_catalog_overview.jpg`
- `examples/layout_examples_overview.jpg`

이 네 파일은 **생성물**이면서 동시에 사람이 바로 확인하는 시각 참조본이므로 Git에 바이너리로 함께 등록했다. `catalog.py`와 `examples.py`를 실행하면 두 PPTX를 다시 생성할 수 있고, 원본 묶음의 SHA-256은 `examples/README.md`에 기록했다.

## 로컬 실행 검증

- `catalog.py`: 실행 성공
- `examples.py`: 실행 성공
- 겹선 자동 제거 로그: 정상 동작 확인
- 예시 조합 중 1곳에서 `영역 부족 필요 0.57 / 가용 0.25` 경고 확인

따라서 키트는 사용 가능하되, 실제 강의덱 제작자는 `영역 부족` 로그를 확인하고 공간 부족 시 글자를 더 줄이기보다 장 분할·구성 변경을 우선한다.

## 사용 시작점

1. `ppt/current/README.md`
2. `ppt/templates/layout_kit/README.md`
3. `ppt/templates/layout_kit/CANONICAL_COMPATIBILITY.md`
4. `ppt/templates/layout_kit/COMPONENTS.md`

## Git binary commit

- `component_catalog.pptx`, `layout_examples.pptx`, 두 overview JPG를 `ppt/templates/layout_kit/examples/`에 실제 바이너리로 등록했다.
- binary commit: `3c91ce71a5351c165dcf575ce8be64b000f3b322`

## HANDOFF 재감사

- `HANDOFF_FOR_COMMIT.md`가 지정한 Python/Markdown 핵심 파일을 원 패키지와 Git blob SHA로 재대조했다.
- 초기 등록본 중 `core.py`, `catalog.py`, `examples.py`가 원 패키지와 달랐고, 2026-09-22 재감사에서 원본과 동일한 blob으로 복원했다.
- `ppt/tools/rowfit.py`와 `ppt/tools/pptlib.py`는 layout_kit 도입 직전 기준 commit `f291b786...`과 현재 master의 blob SHA가 동일하여 **변경되지 않았다**.
- `__pycache__` 파일은 Git에 없다.
- PPTX 두 파일은 원 패키지와 blob SHA가 일치한다.
- overview JPG는 압축 최상위에 별도 제공된 더 최신(17:42) 사본을 커밋했으며, 실제 SHA-256과 크기는 `examples/README.md`에 기록했다.

## lecture_layout_kit_fix 복구 및 HANDOFF §5 확인

대상: 사용자 제공 `lecture_layout_kit_fix.zip`

### 복구
- `ppt/templates/layout_kit/`의 HANDOFF 지정 파일을 fix 패키지 원본 기준으로 대조했다.
- `core.py`, `catalog.py`, `examples.py`는 fix 패키지 원본 blob과 일치하는 상태로 유지한다.
- overview JPG 2개는 이번 fix 패키지의 바이트로 교체했다.
- `ppt/AGENTS.md`, `source_verification_20260808.md`, `.gitignore`, `tools/legacy/slot_align.py`를 추가했다.
- `PROJECT_INSTRUCTIONS_BOOTSTRAP.md`와 저장소 내 `HANDOFF_FOR_COMMIT.md`는 삭제 대상으로 반영했다.
- `HANDOFF_FOR_COMMIT.md`와 `MANIFEST.sha256` 자체는 저장소에 커밋하지 않는다.

### HANDOFF §5 확인 결과
- `sha256sum -c MANIFEST.sha256` → **전 항목 OK**
- `python3 ppt/templates/layout_kit/examples.py` → **exit 0, 오류 없이 종료**
- `python3 ppt/templates/layout_kit/catalog.py` → **exit 0, 오류 없이 종료**
- `examples.py` 실행 로그에는 기존 예시 배치의 `items: 영역 부족 필요 0.57 / 가용 0.25` 경고 1건이 있었으나 실행 오류는 아니었다.
- 두 스크립트 실행으로 다시 생성된 PPTX는 검증용으로만 사용했고, 커밋 대상 바이너리는 fix 패키지 원본을 유지했다.

### 커밋 후 확인
- Git blob SHA를 fix 패키지에서 계산한 blob SHA와 대조한다.
- `__pycache__` / `*.pyc`가 저장소에 없는지 확인한다.
