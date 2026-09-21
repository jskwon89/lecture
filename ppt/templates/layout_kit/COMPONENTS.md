# 부품 목록

모든 부품은 `(s, box, …)`로 호출한다. `s`는 슬라이드, `box`는 그릴 영역(`Box`)이다.
견본은 `examples/component_catalog.pptx`, 조합 예시는 `examples/layout_examples.pptx`.

| 모듈 | 호출 | 설명 | 쓰인 예시 |
|---|---|---|---|
| `text` | `header(s,b,title,sub=None,bar=NAVY_F,tcol=NAVY,pt=None)` | 열 머리: 위쪽 막대 + 제목(+ 보조 줄). 머리 아래 남은 영역을 돌려준다. | 15 16 17 M3 |
| `text` | `meta(s,b,label,text,pt=12)` | '평가 대상  ···' 같은 한 줄 안내. 아래 남은 영역을 돌려준다. | 16 18 |
| `text` | `note(s,b,text,pt=11,col=FOOT,bold=False)` | 한 줄(또는 여러 줄) 글. 아래 남은 영역을 돌려준다. | 03 06 07 15 19 M1 M2 |
| `text` | `def_lines(s,b,defs,pt=12)` | 용어 정의 줄: [(용어, 설명)] | 06 10 18 |
| `text` | `items(s,b,its,pt=None,col=INK,gap=0.14,tail=None,rules=False,spread=False)` | 항목 목록. tail: 목록 끝 금색 강조 줄. spread=True면 영역 높이에 고르게 퍼뜨린다. | 15 16 |
| `text` | `numbered(s,b,its,hot=None,title_pt=13.5,desc_pt=12,dot=True)` | 번호 목록: [(제목, 설명)]. 영역 높이에 고르게 퍼뜨리고 사이에 선을 둔다. | 15 |
| `text` | `grid(s,b,its,cols=2,gap=0.30,title_pt=13,desc_pt=12)` | 번호 격자: [(제목, 설명)] → cols열 | 16 |
| `text` | `cols3(s,b,cols,main_pt=16,gap=None)` | 기준 열: [(라벨, 핵심, [보충])] → 열마다 위쪽 막대 + 라벨 + 핵심 + 보충 | 10 14 |
| `text` | `aligned_lists(s,b,heads,cols_items,pt=12.5)` | 좌우 대조 목록. heads=[(제목, 막대색, 표시 개수 또는 None)], cols_items=[[항목…],[항목…]] 같은 번째 항목끼리 높이를 맞춘다. | 09 |
| `text` | `issue_list(s,b,its,name_w=3.55,pt=13.5)` | 쟁점 목록: [(쟁점명, 질문)] → 번호 원 + 쟁점명 + 질문, 행 높이 고르게 | 11 |
| `text` | `toc(s,b,its,name_w=4.4)` | 목차: [(단원명, 다루는 것)] | 13 |
| `tables` | `row_table(s,b,rows,head_w=None,rules=True,name='row_table')` | 행머리글 표. rows=[(머리글, 결론, [보충], 한정)] 모든 행을 같은 높이로 두고, 넘치는 행만 키운다. 본문은 행 가운데. rules=True면 영역 위·아래에 마감선을 둔다(골격 선과 겹치면 자동 정리). | 01 08 10 14 M2 |
| `tables` | `num_table(s,b,cols,rows,total_col=None,first_w=1.55,head_h=0.42,row_h=0.70,num_pt=22)` | 수치 표. cols=[열 이름], rows=[[값…]]. total_col: 음영 칠 열 번호(예: 합계) | 06 |
| `tables` | `matrix(s,b,col_heads,rows,head_w=None,shade=None,style='rules',row_h=None,cell_pt=12.5,head_pt=13,align='c')` | 대조표. rows=[(행 머리, [칸…], 굵게 여부)] style='rules' : 위·머리 아래·아래 마감선이 있는 일반 표(설계 대조표) style='bars'  : 열 머리를 색 막대로 채운 형(두 입장 대조) shade: 옅은 음영을 칠할 칸 열 번호(0부터) | 12 19 M1 |
| `charts` | `grouped_bars(s,b,groups,xlabels,highlight=None,vmax=None,fmt=str)` | 묶음 세로 막대 + X축. groups={묶음 이름: [값…]}, xlabels=[연도…] highlight: 강조할 x 번호(금색). 영역 폭에 맞춰 막대 폭과 연도 표기(2018/’18)를 정한다. | 02 M1 |
| `charts` | `bars(s,b,its,colors=None,unit='%',vmax=None,value_pt=24,label_pt=12.5,max_bw=1.6,axis_note=None)` | 세로 막대(2~5개). its=[(라벨, 값)]. colors 미지정 시 마지막 막대만 남색, 나머지 회색. | 17 19 |
| `charts` | `hbars(s,b,its,color=NAVY_F,lcol=NAVY,label_w=None,pitch=0.33,pt=12,unit='%',vmax=100)` | 가로 막대 목록. its=[(라벨, 값)] 끝 y를 돌려준다. | 05 M3 |
| `charts` | `progress(s,b,its,highlight=-1,label_w=2.6,right_w=2.33,pitch=None)` | 진행 막대. its=[(라벨, 오른쪽 작은 글, 비율%)] | 07 |
| `charts` | `big_numbers(s,b,its,value_pt=30,label_w=None)` | 큰 숫자 나란히: [(라벨, 값 문자열)] | 07 M2 |
| `charts` | `before_after(s,b,its,unit='점')` | 전후 수치 칸: [(제목, 전, 후, 설명)] | 08 |
| `charts` | `change_rows(s,b,its,row_h=0.72)` | 전후 변화 행: [(이름, 전, 후, 변화, 강조)] | 17 |
| `flows` | `timeline(s,b,events,hot=-1,date_w=2.05,step=None)` | 세로 타임라인: [(날짜, 결론, 보충)] | 03 M3 |
| `flows` | `steps_h(s,b,steps,hot=-1,arrow_w=0.60)` | 가로 단계: [(단계명, 설명)] 위쪽 막대 + 화살표 | 03 |
| `flows` | `steps_v(s,b,steps,hot=None,pitch=None)` | 세로 단계(점과 축): [문장…] | 15 |
| `flows` | `tree(s,b,sources,branches,hot=0,hot_label=None)` | 분기 흐름도. sources=[(단계명, 설명)] 가로로 이어진 앞 단계, branches=[(머리, [항목], 바닥 글)] | 04 |
| `flows` | `stack_columns(s,b,cols,group_label=None,group_from=1)` | 누적 조합 열: [(제목, 보조 줄, [항목], 추가된 항목 수)] 마지막 열을 진하게, 추가 항목은 금색 '+' | 18 |
