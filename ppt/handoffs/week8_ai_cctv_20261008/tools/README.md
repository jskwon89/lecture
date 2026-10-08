# 8주차 생성·검수 도구

입력은 이 폴더의 상위 `w8_content.json`과 `research/source_registry.json`이다. 출력은 상위 `outputs/`와 세 개 Markdown 문서다.

## 실행 환경

- Python: Pillow, python-docx, lxml. Pretendard v1.3.9를 설치하고 fontconfig로 조회할 수 있어야 한다.
- Node.js 및 `@oai/artifact-tool` 2.8.77. `CODEX_PRIMARY_RUNTIME_NODE_MODULES`에 패키지가 있는 node_modules 경로를 설정한다.
- `PRESENTATION_SKILL_ROOT`: Codex presentations skill의 로컬 경로. 기본값은 `/root/.codex/skills/builtins/presentations`이며 finalizer와 검사기를 사용한다.
- `CODEX_PRIMARY_RUNTIME_PYTHON`, `RUNTIME_NODE`, `RUNTIME_NODE_MODULES`, `RUNTIME_BIN_DIR`, `RUNTIME_PYTHON`을 해당 실행환경에 맞춘다. 최종화 단계의 런타임 검사에 필요하다.

## 순서

`W8_BUNDLE_DIR`은 이 묶음의 절대 경로, `W8_BUILD_DIR`은 Git 밖의 임시 작업 폴더로 설정한다. 폴더를 먼저 만들고 다음을 차례로 실행한다.

```bash
python "$W8_BUNDLE_DIR/tools/build_documents.py"
python "$W8_BUNDLE_DIR/tools/prepare_layout.py"
node "$W8_BUNDLE_DIR/tools/build.mjs"
python "$W8_BUNDLE_DIR/tools/normalize_ooxml.py"
node "$W8_BUNDLE_DIR/tools/finalize.mjs"
```

PPT 작성은 JavaScript의 Artifact Tool로 한다. Python 정규화는 내보낸 OOXML의 명시적 글꼴·줄간격·셀 여백·테두리를 조정한다. 표와 차트를 이미지로 바꾸지 않는다. 원본 JSON의 내용을 바꾸는 단계는 없다.

최종화는 기존 PPTX와 finalization.json을 덮어쓰지 않는다. 재생성할 때는 이전 출력물을 별도 작업 폴더에 보존하고 출력 경로를 비운 뒤 실행한다. 바뀐 원본으로 출력만 생성하고 이전 검수 PASS를 재사용하지 않는다.

## 검수

LibreOffice로 PDF를 렌더링하고 PPT를 150dpi 이미지로 변환한 뒤 전 페이지를 직접 읽는다. 대본 DOCX도 모든 페이지를 읽는다. 저장소의 SCREEN_FIRST_REVIEW 절차에 따라 `qa/content_review.json`을 새로 검토하고 수정한다.

```bash
python "$W8_BUNDLE_DIR/tools/check_content_review.py" \
  "$W8_BUNDLE_DIR/w8_content.json" \
  "$W8_BUNDLE_DIR/qa/content_review.json"
```

이 검사는 해시·페이지 대응·실제 문구·미해결 항목의 연결만 확인한다. 사실관계·설명 적절성·시각 품질을 자동으로 인증하지 않는다. 렌더 이미지·PDF·캐시·폰트는 Git에 넣지 않는다.
