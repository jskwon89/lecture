# 양식 키트 (layout_kit)

부품(그래프·표·흐름·글)을 따로 보관하고, 화면을 나눈 영역에 자유롭게 섞어 넣어 장을 만든다.

## 구조
```
layout_kit/
  design.py          색·글자 크기·여백 값 (디자인 값은 여기서만 바꾼다)
  core.py            골격 frame, 영역 Box, 화면 분할 split_h/split_v, 마무리 줄 closing/closing2,
                     각주 foot, 글상자 T/tb, 선 hline/vline, 면 rect, 저장 save(겹선 정리 포함)
  fit.py             끝줄 한두 글자 방지
  components/        부품 (모두 (s, box, 데이터…) 형태)
    text.py          header, meta, note, def_lines, items, numbered, grid, cols3,
                     aligned_lists, issue_list, toc
    tables.py        row_table, num_table, matrix(style='rules'|'bars')
    charts.py        grouped_bars, bars, hbars, progress, big_numbers, before_after, change_rows
    flows.py         timeline, steps_h, steps_v, tree, stack_columns
  catalog.py         부품 견본 덱 생성 (부품 하나를 한 장씩)
  examples.py        예시 장 19종 + 섞어 쓴 예시 3종
  examples/          component_catalog.pptx · layout_examples.pptx · 각 개요 이미지
  COMPONENTS.md      부품 목록과 호출 방법
```
`ppt/tools/`의 `rowfit.py`, `pptlib.py`를 불러 쓴다. 복사본을 두지 않는다.

## 한 장을 만드는 순서
```python
from core import *
from components import *

s, ry = frame('키커', '제목', cue='다음 장 핵심어', cite='연구자(연도)', band='상단 밴드 문장')
top = closing(s, '마무리 문장')                 # 하단 마무리 줄을 먼저 잡는다(없으면 end_rule(s))
left, right = split_h(body(ry, top - 0.12), (60, 40))   # 본문을 60:40으로 나눈다
matrix(s, left, ['집단 A', '집단 B'], [('행 머리', ['칸', '칸'])], shade=1)
bars(s, header(s, right, '그래프 제목'), [('A', 18), ('B', 50)])
foot(s, '출처')
save('out.pptx')
```
- 본문 영역: `body(ry, 아래 한계)` → `Box`
- 나누기: `split_h(box, (비율…))` 좌우, `split_v(box, (비율…))` 위아래, `box.take(높이)` 위에서 떼어 내기, `box.below(y)` y 아래 남은 영역
- 부품은 받은 영역 크기에 맞춰 스스로 배치한다. 영역이 모자라면 실행 기록에 `영역 부족`이 찍힌다.

## 자동 처리 규칙
1. 끝줄 한두 글자 방지: 자간(최대 -0.6pt) → 상자 폭 균형(최대 20% 축소) → 글자 0.5pt 축소 순. 폭 계산에 3% 여유.
2. 행 표 행 높이 균등, 본문은 행 가운데.
3. 겹선 금지: 사이에 글자 없이 0.35인치 안에 붙은 가로선·가로 막대 두 개는 위의 선을 지운다. 같은 높이의 선이 겹치면 하나만 남긴다. 남길 선은 `hline(..., keep=True)`.
4. 인용 표기(`cite`)는 제목 뒤 보통 굵기, 넘치면 밴드 끝 괄호. 제목 오른쪽 칩은 쓰지 않는다.
5. 형광펜 없음(사용자가 마지막에 직접 칠한다).
6. 묶음 막대의 X축 연도: 폭이 넉넉하면 2018, 좁으면 ’18, 더 좁으면 처음·끝·강조 연도만.

## 실행
```bash
curl -sL -o /tmp/p.zip https://github.com/orioncactus/pretendard/releases/download/v1.3.9/Pretendard-1.3.9.zip
unzip -oq /tmp/p.zip -d /tmp/p && mkdir -p ~/.fonts && find /tmp/p -name "Pretendard-*.ttf" -exec cp {} ~/.fonts/ \; && fc-cache -f
pip install python-pptx --break-system-packages
python3 ppt/templates/layout_kit/catalog.py     # 부품 견본
python3 ppt/templates/layout_kit/examples.py    # 예시 장 (인자로 '01' 'M1' 등 일부만 가능)
```
