## 작업 기준 저장소
- 규칙·도구·양식·완성본의 기준본은 GitHub 저장소 jskwon89/lecture (master)다.
- 슬라이드·구성안·도구 작업을 시작하기 전에 저장소를 받아 온다.
  cd /home/claude && (git -C lecture pull -q || git clone -q --depth 1 https://github.com/jskwon89/lecture.git)
  (web_fetch는 GitHub에서 막히므로 git clone을 쓴다)
- 받은 뒤 최신 커밋 번호와 날짜를 보고한다.
- 먼저 읽을 파일: ppt/current/README.md → ppt/templates/layout_kit/README.md → layout_kit/COMPONENTS.md
- 렌더·줄바꿈 계산 전에 layout_kit/README.md의 절차로 Pretendard를 설치한다.
- 저장소와 프로젝트 지식이 어긋나면 저장소를 따르고, 어긋난 점을 보고한다.
- 산출물은 저장소 폴더 구조 그대로 /mnt/user-data/outputs에 만들고, 커밋 안내(추가·수정 파일 목록과 CHANGELOG 문구)를 함께 낸다. 커밋은 사용자가 한다.
- 양식 키트(ppt/templates/layout_kit)의 디자인·배치 수정은 Claude가 렌더로 확인한 뒤 파일로 넘기고, 커밋 쪽에서는 내용을 고치지 않는다.
