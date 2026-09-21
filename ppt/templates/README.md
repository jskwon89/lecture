# PPT 골격 템플릿

현재 Git에는 `skeleton_types.pptx`의 **파싱 참조본**인 `skeleton_types_parsed.md`를 보관한다. 원본 PPTX의 화면 유형·문구·노트 구조를 확인할 때 사용한다.

사용 원칙:

1. 새 도형을 임의로 다시 그리기보다 가장 가까운 승인 골격 유형을 사용한다.
2. 글꼴·팔레트·기본 여백·정보위계를 유지한다.
3. 내용량에 따라 행 복제·삭제, 텍스트 상자 높이·구분선 위치 조정은 허용하되 `PPT_RULES.md`의 실측 규칙을 따른다.
4. 공간이 부족하면 글자를 임의로 줄이지 말고 슬라이드를 나눈다.
5. 골격과 Canonical이 충돌하면 Canonical이 우선한다.

## 현재 파일

- `skeleton_types_parsed.md` — 화면 유형 27장의 텍스트·노트 파싱본
- 실제 PPTX 바이너리는 현재 대화의 원본 자산으로 유지한다. Git에서 시각 검수할 때는 `ppt/references/legacy/`의 기존 PPTX와 함께 본다.

폰트 파일은 Git에 넣지 않는다.


## 범위 주의

`skeleton_types.pptx`의 **초반 승인 골격 구간**은 현행 좌표·색·폰트 기준의 실물 참조다. 뒤쪽에 함께 실린 2주차 원본 예시 장들은 과거 산출물의 사례이므로 **현행 좌표·여백·색상값을 역산하는 기준으로 쓰지 않는다.**

## 양식 키트

그래프·표·흐름·글 부품과 자동 배치 도구는 `layout_kit/`에 있다.

- 시작: `layout_kit/README.md`
- 부품 목록: `layout_kit/COMPONENTS.md`
- 현행 Canonical과의 관계: `layout_kit/CANONICAL_COMPATIBILITY.md`
- 부품 견본 생성: `layout_kit/catalog.py`
- 예시 장 생성: `layout_kit/examples.py`

키트는 **구성·배치 부품 라이브러리**이며, 색·글자크기·고정 좌표·출처표기·최종 QA는 `../PPT_RULES.md`가 우선한다. 키트와 Canonical이 충돌하면 `CANONICAL_COMPATIBILITY.md`에 기록된 대로 Canonical을 따른다.

예시 덱은 생성 스크립트의 산출물이다. Git에 바이너리 견본이 없거나 오래되었으면 `catalog.py` / `examples.py`를 실행해 최신 코드에서 다시 생성한다.
