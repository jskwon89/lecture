# 작업 에이전트 공통 안내 — Claude · GPT · 기타 도구

갱신: 2026-09-22

이 저장소에서 PPT·구성안·대본·도구 작업을 하는 모든 에이전트는 이 문서를 먼저 읽고 따른다. 각 도구의 지침 칸에는 "저장소를 받아 `ppt/AGENTS.md`를 먼저 읽는다"는 짧은 안내만 두고, 실제 작업 방식은 이 문서 한 곳에서 관리한다.

## 1. 기준
- 이 저장소(`jskwon89/lecture`, master)가 규칙·도구·양식·완성본의 유일한 기준본이다. 사용자의 현재 명시적 지시가 저장소 규칙보다 우선한다.
- 작업을 시작할 때마다 최신 master를 받고, 받은 커밋 번호와 날짜를 사용자에게 보고한다.
- 읽는 순서: `ppt/README.md`의 「작업 시작 순서」 → 디자인·배치 작업이면 `ppt/templates/layout_kit/README.md`와 `COMPONENTS.md`.
- 저장소와 다른 자료(프로젝트 지식, 대화에 붙인 옛 지침 등)가 어긋나면 저장소를 따르고, 어긋난 점을 보고한다.

## 2. 환경별로 저장소를 받는 방법
| 환경 | 방법 |
|---|---|
| Claude 채팅(claude.ai) | `cd /home/claude && (git -C lecture pull -q \|\| git clone -q --depth 1 https://github.com/jskwon89/lecture.git)` — GitHub 웹 조회는 막혀 있으므로 git을 쓴다. 산출물은 `/mnt/user-data/outputs`에 둔다 |
| Claude Code | 로컬 저장소에서 `git pull` 후 작업한다 |
| GPT | 사용 중인 GitHub 연동으로 master를 읽는다 |

## 3. 폰트와 렌더
- 줄바꿈 계산과 렌더 검수 전에 Pretendard v1.3.9를 설치한다. 폰트 파일은 Git에 넣지 않는다.
  ```bash
  curl -sL -o /tmp/p.zip https://github.com/orioncactus/pretendard/releases/download/v1.3.9/Pretendard-1.3.9.zip
  unzip -oq /tmp/p.zip -d /tmp/p && mkdir -p ~/.fonts && find /tmp/p -name "Pretendard-*.ttf" -exec cp {} ~/.fonts/ \; && fc-cache -f
  ```
- 렌더는 LibreOffice(`soffice --headless --convert-to pdf`)와 `pdftoppm`으로 한다. 렌더를 해 볼 수 없는 환경이면 그 사실을 보고에 적는다.

## 4. 산출물을 넘길 때
- 저장소 폴더 구조 그대로 파일을 만든다.
- 함께 넘길 것: 추가·수정·삭제 파일 목록, CHANGELOG 문구, 파일별 SHA-256 목록(`MANIFEST.sha256`).

## 5. 커밋할 때
- 넘겨받은 파일은 **바이트 그대로** 올린다. 다시 타이핑하거나, 요약하거나, 형식을 고쳐 쓰지 않는다. 코드 파일은 특히 그렇다.
- 올린 뒤 `sha256sum -c MANIFEST.sha256`으로 대조하고 결과를 기록한다.
- 코드를 올렸으면 실행해 확인한다. 양식 키트는 `python3 ppt/templates/layout_kit/examples.py`와 `catalog.py`가 오류 없이 끝나야 한다.
- `__pycache__`, `*.pyc`, 렌더 중간 파일은 올리지 않는다.
- 모든 변경은 `ppt/CHANGELOG.md`에 남긴다.

## 6. 역할 분담
- **양식 키트(`ppt/templates/layout_kit`)의 디자인·배치 수정**은 실제 렌더로 확인할 수 있는 에이전트(현재 Claude)가 하고, 커밋하는 쪽은 내용을 고치지 않고 반영한다.
- 다른 에이전트가 키트를 고쳐야 했다면 이유와 변경 내용을 CHANGELOG에 남기고, 다음 작업자는 그것을 받아 이어서 작업한다.
- 규칙 문서(`PPT_RULES.md` 등)의 변경은 사용자 승인 후 반영하고 `RULE_SOURCE_MAP.md`·CHANGELOG에 기록한다.

## 7. 각 도구의 지침 칸에 넣을 문안
```
작업 기준 저장소는 GitHub jskwon89/lecture (master)다.
작업을 시작하기 전에 최신본을 받아 ppt/AGENTS.md를 먼저 읽고, 그 문서의 방식대로 작업한다.
받은 커밋 번호와 날짜를 먼저 보고한다.
```
