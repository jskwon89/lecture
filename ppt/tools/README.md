# PPT 제작·QA 도구

이 폴더의 코드는 `ppt/PPT_RULES.md`의 디자인·정렬·QA 규칙을 실제로 구현하거나 점검한다.

## 파일

- `pptlib.py` — 공통 팔레트·좌표·텍스트/도형 생성·기존 PPT XML 편집·노트 처리
- `rowfit.py` — Pretendard 실제 글자폭을 사용해 줄 수와 내용 높이를 계산
- `layout.py` — 행 내용 높이는 고정하고 남는 공간은 모든 행의 동일 위·아래 여백으로 배분
- `check_spacing.py` — 150dpi 렌더에서 여백·행머리글 중심·마지막 구분선·각주 간격을 실측

## 전제

- 검수 환경에 **Pretendard Regular/Bold**가 설치되어 있어야 한다.
- 폰트 파일 자체는 Git에 보관하지 않는다.
- `rowfit.py`의 폰트 경로가 실행환경과 다르면 경로만 맞추고 규칙값은 바꾸지 않는다.

## 기본 QA

```bash
soffice --headless --convert-to pdf deck.pptx
pdftoppm -jpeg -r 150 deck.pdf page
python3 ppt/tools/check_spacing.py page-*.jpg
python3 ppt/tools/check_spacing.py --cols page-4.jpg
```

자동 점검 통과만으로 완료하지 않는다. 전체 렌더를 눈으로 확인하고 `PPT_RULES.md`의 콘텐츠 자가점검도 함께 수행한다.
