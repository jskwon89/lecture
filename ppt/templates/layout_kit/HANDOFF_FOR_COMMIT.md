# 커밋 안내 (layout_kit 추가)

## 1. 추가할 폴더 (이 묶음의 경로 그대로)
`ppt/templates/layout_kit/` 전체
- README.md, COMPONENTS.md
- design.py, core.py, fit.py, catalog.py, examples.py
- components/__init__.py, text.py, tables.py, charts.py, flows.py
- examples/component_catalog.pptx, component_catalog_overview.jpg, layout_examples.pptx, layout_examples_overview.jpg

기존 파일은 수정하지 않는다. `ppt/tools/`의 rowfit.py·pptlib.py는 그대로 둔다(키트가 불러 쓴다).
__pycache__ 폴더는 올리지 않는다.

## 2. 기존 문서에 추가할 내용
- `ppt/templates/README.md` 끝에:
  > ## 양식 키트
  > 그래프·표·흐름·글 부품과 자동 배치 도구는 `layout_kit/`에 있다. 부품 목록은 `layout_kit/COMPONENTS.md`, 견본은 `layout_kit/examples/`를 본다.
- `ppt/CHANGELOG.md`에:
  > 2026-09-22 · ppt/templates/layout_kit 추가 — 부품 27종(글 11 · 표 3 · 그래프 7 · 흐름 5 + 골격 도구), 예시 장 19종과 섞어 쓴 예시 3종, 부품 견본 덱, 끝줄 한두 글자 방지, 행 높이 균등, 겹선 제거, 인용 표기 제목 뒤 배치, 그래프 연도축

## 3. 현행 규칙과 어긋나는 점 (기록만 하고 판단은 사용자에게)
- 글자 크기·색: design.py(결론 14pt, 보충 12.5pt, 행머리글 14pt, 밴드 13.5pt, 구분선 C9CEDA, 금색 글자 8A6D10) ↔ PPT_RULES.md v1.5(12.5/11.5/13/13, DCE0E8, A8871C)
- `templates/README.md` 4항 "글자를 임의로 줄이지 말라" ↔ fit.py의 0.5pt 축소 단계
- 행 본문 위치: PPT_RULES 위쪽 기준 ↔ 키트 행 가운데
- 사건번호·연구자: PPT_RULES 제목 오른쪽 칩 ↔ 키트 제목 뒤 표기

## 4. 수정 분담
키트의 디자인·배치 수정은 Claude가 렌더로 확인한 뒤 파일로 넘긴다. 커밋할 때는 내용을 고치지 않는다. 다른 쪽에서 키트를 고쳤다면 CHANGELOG에 남긴다.
