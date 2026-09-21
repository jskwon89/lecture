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
