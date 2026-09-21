# layout_kit generated examples

이 폴더의 PPTX/JPG는 **생성 산출물**이다. 기준본은 상위 폴더의 Python 코드와 `COMPONENTS.md`다.

## 생성

```bash
python3 ppt/templates/layout_kit/catalog.py
python3 ppt/templates/layout_kit/examples.py
```

생성되는 덱:

- `component_catalog.pptx` — 부품 하나를 한 장씩 보여 주는 견본
- `layout_examples.pptx` — 기본 예시 19종 + 혼합 예시 M1~M3

Claude가 전달한 2026-09-22 패키지의 생성 산출물 식별값:

| 파일 | SHA-256 | 크기 |
|---|---|---:|
| component_catalog.pptx | `cd3239a77b264ed5739d37f1688981176325673ce3f9e5491dfc4d6437efe6ee` | 73,199 B |
| layout_examples.pptx | `971bd2f011ed970fab5c7aaaa74d3e5272c046c8cdcd25edbb0c91d327658228` | 92,576 B |
| component_catalog_overview.jpg | `9b2746c12ec94cdf4f0b67aa473ca5f655eb527cc4a14dcc833e134332ca4d5b` | 606,577 B |
| layout_examples_overview.jpg | `0f22470e63bbc29588ba384bbb139226e682c73f1f35ff98eeaaaf9f7405d607` | 1,039,661 B |

두 overview JPG는 `lecture_layout_kit.zip` 내부 사본보다 뒤 시각(17:42)에 압축 최상위에 함께 전달된 최신 미리보기 사본을 Git에 보존한다. PPTX 두 파일은 내부 패키지와 Git blob이 일치한다.

현재 Git에는 **코드와 생성된 바이너리 견본을 함께 보존**한다. Python 코드가 재현 가능한 소스 기준본이고, PPTX·JPG는 사람이 바로 열어 보고 고를 수 있는 시각 참조본이다. 코드가 바뀌면 위 스크립트로 바이너리를 다시 생성하고 함께 갱신한다.

## 사용 주의

`../CANONICAL_COMPATIBILITY.md`를 먼저 확인한다. 예시 덱의 디자인 값이 현재 `PPT_RULES.md`와 충돌하면 예시를 그대로 복사하지 않고 Canonical 값으로 보정한다.
