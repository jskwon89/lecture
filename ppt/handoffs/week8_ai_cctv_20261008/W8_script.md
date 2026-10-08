# 8주차 낭독 대본

검토용 초안 v1 · PPT 쪽수와 동일한 순서

## 01 공공 CCTV의 실시간 AI 분석

카메라에 찍힌 얼굴이 경찰의 검색 명단과 연결되면, 영상은 사람을 찾아내는 수단이 됩니다. 기술이 제시한 후보는 신원 확인과 현장 조치로 이어질 수 있습니다. 오늘의 질문은 공공 CCTV를 이런 목적으로 실시간 분석하도록 허용할지, 허용한다면 어떤 범위와 절차를 둘지입니다.

추가 질문: 오늘 판단할 정책은 무엇인가?

다음 연결: 논제의 적용 범위를 알면 학습할 개념과 자료의 순서가 정해진다.

출처: [D01](https://www.humanrights.go.kr/base/board/read?boardManagementNo=24&boardNo=7609889&menuLevel=3&menuNo=91&page=1&searchCategory=&searchType=&searchWord=), [D02](https://gnews.gg.go.kr/briefing/brief_gongbo_view.do?BS_CODE=S017&number=67424), [F01](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5)

## 02 오늘 볼 것

실시간 분석의 기능을 구분하면, 어떤 변화에 법적 근거와 성능 평가가 필요한지 분명해집니다. 현장에서 얻은 성과와 시민이 겪은 부담, 국내외의 허용 조건을 함께 놓고 자신의 판단을 구성할 수 있습니다.

추가 질문: 학습 순서는 어떻게 연결되는가?

다음 연결: 학습 순서의 출발점은 누가 검색 대상이고 누가 입력 대상인지 구분하는 것이다.

출처: [D01](https://www.humanrights.go.kr/base/board/read?boardManagementNo=24&boardNo=7609889&menuLevel=3&menuNo=91&page=1&searchCategory=&searchType=&searchWord=), [F01](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5), [F05](https://www.met.police.uk/SysSiteAssets/media/downloads/force-content/met/advice/lfr/other-lfr-documents/live-facial-recognition-annual-report-2025.pdf)

## 03 영상 속 사람과 검색 명단의 연결

수사기관은 이미 알고 있는 용의자의 얼굴을 명단에 올리고, 그 사람이 카메라 앞을 지나는지 찾을 수 있습니다. 이때 시스템이 처리하는 영상에는 명단 밖의 통행인도 들어옵니다. 정책의 적용 범위는 찾으려는 사람과 실제로 얼굴을 처리하는 사람을 함께 포함합니다.

추가 질문: 누구를 찾고 누구의 얼굴을 처리하는가?

다음 연결: 같은 CCTV 영상도 찾으려는 대상에 따라 서로 다른 분석 기능을 사용한다.

출처: [F02](https://www.judiciary.uk/wp-content/uploads/2020/08/R-Bridges-v-CC-South-Wales-ors-Judgment.pdf), [F01](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5)

## 04 AI 관제의 세 가지 기능

파리 올림픽의 상황 탐지와 안양의 실종자 외형 검색은 서로 다른 질문을 기계에 맡깁니다. 하나는 무슨 상황이 발생했는지, 다른 하나는 이런 모습의 사람이 어디로 갔는지를 찾습니다. 얼굴 신원식별은 그 사람이 등록 명단 속 누구인지 묻습니다. 각 기능에서 필요한 정보와 오류의 종류도 달라집니다.

추가 질문: AI 관제는 모두 얼굴로 신원을 알아내는가?

다음 연결: 얼굴 신원식별의 기술 과정을 알면 후보 경보의 의미를 설명할 수 있다.

출처: [F15](https://www.legifrance.gouv.fr/juri/id/CONSTEXT000047602516), [S17](https://www.cnil.fr/en/2024-olympics-cnils-qa-your-privacy-and-freedoms), [D23](https://gonggam.korea.kr/newsContentView.es?b_list=9&code_cd=&content=&mid=a12605000000&nPage=1&news_id=a19b4b5e-fad6-4a3a-9120-5e9488c3a8d9&section_id=NCCD_CULTURE_TOTAL), [S04](https://gonggam.korea.kr/newsContentView.es?mid=a12603000000&news_id=a19b4b5e-fad6-4a3a-9120-5e9488c3a8d9&section_id=), [F02](https://www.judiciary.uk/wp-content/uploads/2020/08/R-Bridges-v-CC-South-Wales-ors-Judgment.pdf)

## 05 얼굴에서 경보까지

1:N은 한 얼굴을 여러 등록 얼굴과 비교한다는 뜻입니다. 시스템은 먼저 얼굴 영역을 찾아 수치로 표현하고, 명단의 얼굴과 유사도를 계산합니다. 운영자가 정한 경보 기준값을 넘으면 후보가 제시됩니다. 그 결과를 본 담당자는 실제 영상과 명단 사진을 대조해 후속 확인의 필요성을 판단합니다.

추가 질문: 1:N 대조는 어떤 순서로 작동하는가?

다음 연결: 유사도 문턱은 어떤 후보를 통과시키고 놓치는지와 연결된다.

출처: [F02](https://www.judiciary.uk/wp-content/uploads/2020/08/R-Bridges-v-CC-South-Wales-ors-Judgment.pdf)

## 06 오경보와 미탐지

오경보를 줄이는 설정과 대상자를 더 많이 찾아내는 설정은 함께 검토해야 합니다. 기준값을 높이면 닮은 정도가 낮은 후보가 걸러지지만, 촬영 각도나 화질 때문에 점수가 낮아진 실제 대상자도 빠질 수 있습니다. 따라서 운영 성능에는 잘못 울린 경보와 놓친 대상자에 관한 정보가 모두 필요합니다.

추가 질문: 경보를 더 엄격하게 만들면 무엇이 달라지는가?

다음 연결: 오류를 측정하는 기준은 얼굴 기록과 공통 시험이 발전해 온 역사에 연결된다.

출처: [F02](https://www.judiciary.uk/wp-content/uploads/2020/08/R-Bridges-v-CC-South-Wales-ors-Judgment.pdf), [F06](https://science.police.uk/site/assets/files/3396/frt-equitability-study_mar2023.pdf)

## 07 표준 기록에서 공통 시험으로

베르티용의 체계는 다시 잡힌 사람이 과거 기록 속 누구인지 찾기 위해 신체와 사진을 일정한 형식으로 남겼습니다. 초기 컴퓨터 연구에서는 사람이 특징점의 위치를 직접 입력했습니다. FERET는 공통 자료로 알고리즘을 시험하면서, 특정한 시연의 인상과 여러 기술을 같은 조건에서 비교하는 평가를 구분할 기반을 만들었습니다.

추가 질문: 자동 식별 이전에는 사람을 어떻게 다시 알아보았는가?

다음 연결: 알고리즘의 발전과 함께 국내에서는 영상 수집·통합·경보의 운영 기반이 확대됐다.

출처: [S06](https://www.nlm.nih.gov/exhibition/visibleproofs/galleries/biographies/bertillon.html), [S07](https://www.nationalacademies.org/read/27397/chapter/4), [S08](https://www.nist.gov/programs-projects/face-recognition-technology-feret)

## 08 카메라 설치에서 통합관제로

통합관제는 떨어져 있던 영상을 한곳에서 살펴보는 운영 변화입니다. 초기 방범 카메라 설치 때부터 설치 주체와 장소, 보관과 관리의 법적 기준이 논의됐습니다. 이후에는 영상을 모으는 데 더해 기계가 위험 징후를 먼저 알리는 기능이 등장했습니다. 영상의 수가 늘어나는 변화와 영상에 맡기는 판단이 늘어나는 변화가 함께 진행된 것입니다.

추가 질문: 국내 관제의 확장은 어떤 변화를 포함했는가?

다음 연결: 관제의 확장과 별도로 같은 시험에서 인식 성능의 변화를 측정할 수 있다.

출처: [S01](https://www.humanrights.go.kr/site/program/board/basicboard/view?boardid=554769&boardtypeid=24&currentpage=232&menuid=001004002001&pagesize=10), [S02](https://www.mois.go.kr/frt/bbs/type010/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000008&nttId=27953), [S03](https://mois.go.kr/frt/bbs/type010/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000008&nttId=40565)

## 09 사진 검색 성능의 향상

NIST는 2018년 보고에서 얼굴인식 성능이 크게 향상됐다고 설명했습니다. 제시된 같은 사진 검색 평가에서 미탐지율은 2014년 4%에서 2018년 0.2%로 낮아졌습니다. 거리의 운용 성과를 판단하려면 이 기술적 변화에 더해 실제 촬영 영상, 검색 명단, 경보 설정과 현장 대응을 확인해야 합니다.

추가 질문: 성능 발전은 어떤 시험 결과에서 확인됐는가?

다음 연결: 사진 시험의 향상은 실제 배치에서 후보가 조치로 이어지는 운영 질문을 남긴다.

출처: [S09](https://www.nist.gov/news-events/news/2018/11/nist-evaluation-shows-advance-face-recognition-softwares-capabilities)

## 10 체포 없이 끝난 ‘Snooper Bowl’

경기장에 기술을 설치해 얼굴을 대조하는 장면은 큰 관심을 끌었습니다. 그러나 당시 보도에 따르면 이 슈퍼볼 배치에서는 체포가 없었습니다. 후보를 화면에서 찾은 뒤에도 현장 인력이 그 사람을 다시 찾고 확인해야 했기 때문입니다. 대규모 공간에서 탐지 결과를 어디로, 얼마나 빨리 전달할지는 시스템의 운영 과제입니다.

추가 질문: 경보가 실제 체포까지 이어지려면 무엇이 필요한가?

다음 연결: 대규모 배치의 가능성은 국내에서 영상을 수집·처리할 법적 근거를 묻게 한다.

출처: [S10](https://www.deseret.com/2001/7/3/19594393/street-cameras-in-tampa-a-sign-of-big-brother/), [S22](https://www.deseret.com/2001/11/15/19616892/w-v-police-to-buy-snooper-bowl-devices/)

## 11 공개장소 CCTV 설치의 근거

공개된 장소의 CCTV 설치는 법에서 열거한 사유와 연결됩니다. 범죄 예방과 수사를 위해 필요한 경우가 그중 하나입니다. 공공기관의 설치 의견 수렴, 안내판, 안전성 확보도 같은 조문 체계에 들어 있습니다. 수집한 영상에서 얼굴 특징을 만들거나 다른 명단과 연결할 때에는 그 후속 처리의 목적과 근거를 더 확인하게 됩니다.

추가 질문: 공공장소에 CCTV를 설치할 법적 기준은 무엇인가?

다음 연결: 촬영한 영상에서 신원을 알아볼 특징정보를 생성하면 추가 처리 규정을 검토한다.

출처: [D14](https://www.law.go.kr/LSW//lsLawLinkInfo.do?chrClsCd=010202&lsId=011357&lsJoLnkSeq=900078586&print=print)

## 12 생체 특징정보와 공공기관의 예외

얼굴 사진을 보유하는 행위와 그 사진에서 신원을 알아볼 특징정보를 만드는 행위는 처리 내용을 따져야 합니다. 시행령은 식별 목적과 기술적 생성이라는 조건을 명시합니다. 동시에 공공기관이 법 제18조제2항의 특정 사유로 처리하는 경우를 제외하는 단서를 둡니다. 사용 목적과 기관, 해당 예외의 요건을 함께 확인해야 하는 이유입니다.

추가 질문: 얼굴 특징정보에는 어떤 규정과 예외가 적용되는가?

다음 연결: 생체정보의 처리 규정과 함께 관제센터에 부여된 분석 목적·권한을 확인한다.

출처: [D14](https://www.law.go.kr/LSW//lsLawLinkInfo.do?chrClsCd=010202&lsId=011357&lsJoLnkSeq=900078586&print=print), [D15](https://www.law.go.kr/LSW/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1034050143)

## 13 통합관제센터의 AI 분석 권한

2025년에 신설·시행된 이 조항은 통합관제센터와 AI 분석의 법적 기반을 명시합니다. 지방자치단체장은 재난과 각종 사고를 예방하고 대응하기 위해 영상을 분석하고 연계할 수 있습니다. 분석을 설계할 때에는 어떤 상황을 찾는지와 어떤 개인정보를 처리하는지가 이 목적과 연결되어야 합니다. 용의자의 신원 대조에는 명단의 근거와 후속 수사 절차도 함께 검토됩니다.

추가 질문: 관제센터의 AI 분석 권한은 어떤 목적에 연결되는가?

다음 연결: 정보 분석이 현장 접촉으로 이어지는 순간에는 경찰의 정지·질문 요건이 적용된다.

출처: [D38](https://www.law.go.kr/LSW/lsSideInfoP.do?docCls=jo&joBrNo=05&joNo=0074&lsiSeq=282883&urlMode=lsScJoRltInfoR), [D17](https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000278958)

## 14 경보 이후의 정지와 질문

경보를 본 경찰이 통행인을 멈춰 세우고 질문하는 순간에는 불심검문의 요건이 문제됩니다. 법은 수상한 행동과 주변 사정을 합리적으로 판단하도록 합니다. 경찰은 자신의 신분과 질문 이유를 설명해야 하고, 동행 요구에는 거절권이 있습니다. 현장의 판단 과정에서 영상과 사진의 동일성, 명단 정보의 신뢰성, 주변 사정을 확인할 필요가 생깁니다.

추가 질문: 경찰은 AI 경보 뒤 어떤 요건으로 정지·질문할 수 있는가?

다음 연결: 정지·질문 이후 신체를 구속하는 체포에는 별도의 영장과 법정 요건이 있다.

출처: [X01](https://law.go.kr/LSW/lsSideInfoP.do?docCls=jo&joBrNo=00&joNo=0003&lsiSeq=282479&urlMode=lsScJoRltInfoR), [F03](https://www.judiciary.uk/wp-content/uploads/2026/04/AC-2024-LON-001764-R-Thompson-and-Carlo-version-for-hand-down-21-04-2026.pdf)

## 15 영장에 의한 체포의 요건

영장에 의한 체포는 범죄 혐의가 있다고 의심할 상당한 이유와 정당한 이유 없는 출석 불응 또는 불응 우려를 요건으로 합니다. 경찰의 신청, 검사의 청구, 판사의 발부를 거칩니다. 거리에서 명단 속 대상자 후보가 발견되면, 경찰은 그 사람이 영장 대상자와 같은 사람인지 확인해야 합니다. 체포 경로마다 법정 요건이 있으므로 대상자를 찾는 과정과 강제처분의 근거를 각각 설명해야 합니다.

추가 질문: 영장 체포에서 누가 무엇을 결정하는가?

다음 연결: 제도적 단계는 국내 검색·출동 사례에서 담당자들의 실제 행동으로 구체화된다.

출처: [X02](https://www.law.go.kr/LSW/lsLinkCommonInfo.do?lsJoLnkSeq=1013583337)

## 16 외형 검색으로 찾은 안양의 실종자

이 수색에서 눈에 띄는 단서는 얼굴 정면 사진보다 모자와 지팡이 같은 외형입니다. 관제센터는 여러 영상에서 닮은 모습을 좁혔고, 경찰은 이동 경로를 바탕으로 현장 공간을 살폈습니다. 발견 장소는 아파트 지하 기계실이었습니다. 영상 검색이 담당자의 탐색 범위를 줄이고 실제 수색으로 이어진 국내 운영 사례입니다.

추가 질문: 외형 검색은 국내 수색에서 어떤 일을 맡았는가?

다음 연결: 실종자 외형 검색의 역할을 구분한 뒤 용의자 실시간 얼굴 대조의 실제 사례를 본다.

출처: [D23](https://gonggam.korea.kr/newsContentView.es?b_list=9&code_cd=&content=&mid=a12605000000&nPage=1&news_id=a19b4b5e-fad6-4a3a-9120-5e9488c3a8d9&section_id=NCCD_CULTURE_TOTAL), [S04](https://gonggam.korea.kr/newsContentView.es?mid=a12603000000&news_id=a19b4b5e-fad6-4a3a-9120-5e9488c3a8d9&section_id=)

## 17 수배자를 찾아낸 런던의 경보

런던경찰은 이미 수배 중인 Patel을 Dalston의 실시간 얼굴인식 배치로 찾아냈다고 발표했습니다. 사건 보도는 경보와 체포에서 끝나지 않고 유죄 인정과 선고일까지 연결합니다. 선고 내용은 징역 12개월에 집행유예 12개월입니다. 특정 배치의 결과를 평가할 때에도 발견, 체포, 재판 결과를 각각 기록하면 기술이 맡은 역할을 더 구체적으로 설명할 수 있습니다.

추가 질문: 실시간 경보가 실제 수배자 사건에서 어떤 결과로 이어졌는가?

다음 연결: 한 체포 사례의 경과와 함께 여러 배치를 합친 연간 운영의 단위도 살핀다.

출처: [S14](https://news.met.police.uk/news/child-sex-offender-identified-through-mets-live-facial-recognition-sentenced-505799)

## 18 런던경찰의 1년 운영 실적

이 보고서의 집계 기간은 2024년 9월 11일부터 2025년 9월 10일까지입니다. 얼굴 통과 약 314만 회와 경보 2,077건, 체포 962건이 보고됐습니다. 배치는 범죄다발지역 203회와 행사보안 4회로 구분됩니다. 통과는 반복을 포함한 횟수이고, 체포 건수에는 다른 시점의 동일인 체포가 포함될 수 있습니다.

추가 질문: 런던의 연간 기록은 어떤 단위로 무엇을 집계했는가?

다음 연결: 전체 실적 중 잘못된 경보가 시민에게 어떤 조치로 이어졌는지를 분리한다.

출처: [F05](https://www.met.police.uk/SysSiteAssets/media/downloads/force-content/met/advice/lfr/other-lfr-documents/live-facial-recognition-annual-report-2025.pdf)

## 19 오경보 뒤 실제 접촉

오경보 10건 중 6건에서는 경찰의 현장 접촉이 있었습니다. 보고서는 이 오경보 때문에 체포된 사례는 없었다고 기록합니다. 오인체포까지 이어지지 않더라도 통행인은 정지나 질문을 겪을 수 있습니다. 따라서 오류를 기록할 때에는 경보의 정확도와 시민에게 실제로 가해진 조치의 정도를 함께 남길 필요가 있습니다.

추가 질문: 잘못된 경보는 시민에게 어느 단계까지 영향을 미쳤는가?

다음 연결: 오경보 건수의 의미는 전체 경보와 통과 횟수 중 어떤 분모를 쓰는지에 달려 있다.

출처: [F05](https://www.met.police.uk/SysSiteAssets/media/downloads/force-content/met/advice/lfr/other-lfr-documents/live-facial-recognition-annual-report-2025.pdf)

## 20 분모가 바꾸는 오류 수치

같은 10건을 경보 전체로 나누면 약 0.48퍼센트이고, 얼굴 통과 전체로 나누면 100만 회당 약 3.18건입니다. 앞 수치는 경보를 받았을 때의 신뢰성을, 뒤 수치는 대량 처리에서 발생하는 오경보 빈도를 설명합니다. 미탐지율에는 명단 인물이 실제로 몇 번 지나갔는지라는 별도의 정답 자료가 필요합니다.

추가 질문: 같은 오류 건수인데 비율이 다른 이유는 무엇인가?

다음 연결: 측정 단위를 정하면 기존 수사와 비교할 추가 성과의 지표를 설계할 수 있다.

출처: [F05](https://www.met.police.uk/SysSiteAssets/media/downloads/force-content/met/advice/lfr/other-lfr-documents/live-facial-recognition-annual-report-2025.pdf)

## 21 추가 성과를 평가할 기록

체포 실적은 실제 활동의 산출을 보여 줍니다. 실시간 얼굴식별을 추가해서 무엇이 개선됐는지를 판단하려면 기존 수사에서 걸린 시간과 필요한 인력, 사건의 처리결과가 함께 있어야 합니다. 국내에서는 이 단계들을 연결한 공개 원표를 확보하지 못했습니다. 그러므로 도입 평가를 설계할 때부터 비교할 수단과 기록할 지표를 정하는 일이 남습니다.

추가 질문: 도입으로 더 얻은 성과는 어떻게 확인하는가?

다음 연결: 성과 비교에는 현장에서 반복적으로 필요한 인력과 비용이 포함된다.

출처: [F05](https://www.met.police.uk/SysSiteAssets/media/downloads/force-content/met/advice/lfr/other-lfr-documents/live-facial-recognition-annual-report-2025.pdf), [D39](https://record.council.jeju.kr/CLRecords/Files/FileAppendix/a12/A044556.pdf)

## 22 관제에는 지속적인 인력과 비용이 든다

제주 보고서의 2023년 전체 센터 예산은 약 117억 5,544만 원입니다. 인건비와 유지보수처럼 매년 반복되는 비용이 포함됩니다. 요원 101명과 상주 경찰 3명이라는 인력도 함께 기록돼 있습니다. 새 얼굴식별 기능의 예산을 짤 때에는 구매비에 더해 경보를 확인할 인력, 교육, 감독과 구제에 필요한 자원을 산정해야 합니다.

추가 질문: 새 기술의 비용 평가에는 어떤 운영 자원이 필요한가?

다음 연결: 운영 자원과 함께 실제 영상·명단·설정에 맞는 성능 시험을 구성해야 한다.

출처: [D39](https://record.council.jeju.kr/CLRecords/Files/FileAppendix/a12/A044556.pdf)

## 23 시험 조건과 배치 환경

얼굴인식은 알고리즘 이름만으로 성능을 설명하기 어렵습니다. 같은 시스템도 영상과 명단, 경보 기준값에 따라 다른 결과를 낼 수 있습니다. NPL의 평가와 NIST의 연구 설명은 과업과 조건별 결과를 구분합니다. 실제 배치에서는 시스템의 출력뿐 아니라 담당자의 확인 과정에서 어떤 오류가 걸러지고 남는지도 기록해야 합니다.

추가 질문: 도입 전에 어떤 조건에서 성능을 시험해야 하는가?

다음 연결: 사람이 후보를 확인하는 과정의 실패는 실제 오인체포 사건에서 드러난다.

출처: [F06](https://science.police.uk/site/assets/files/3396/frt-equitability-study_mar2023.pdf), [F07](https://www.nist.gov/news-events/news/2019/12/nist-study-evaluates-effects-race-age-sex-face-recognition-software), [F02](https://www.judiciary.uk/wp-content/uploads/2020/08/R-Bridges-v-CC-South-Wales-ors-Judgment.pdf)

## 24 잘못된 후보가 체포로 이어진 경로

Williams 사건은 범행 뒤 확보한 흐린 영상에서 얼굴을 검색한 수사입니다. 검색 후보를 넣은 사진 배열을 확인한 사람도 같은 범행 영상을 보았던 사람이었습니다. 같은 영상에서 출발한 판단이 여러 단계를 거치면서 체포의 근거로 연결됐습니다. 별개의 확인처럼 보이는 절차가 실제로 어떤 정보에 의존하는지 검토할 필요가 드러납니다.

추가 질문: 사람의 사진 확인은 어떤 정보에 의존했는가?

다음 연결: 잘못된 후보가 체포로 이어진 경로를 바탕으로 합의는 추가 수사 근거를 요구했다.

출처: [F08](https://www.aclu.org/press-releases/civil-rights-advocates-achieve-the-nations-strongest-police-department-policy-on-facial-recognition-technology), [S12](https://www.aclu.org/cases/williams-v-city-of-detroit-face-recognition-false-arrest?document=Settlement-Agreement), [S13](https://assets.aclu.org/live/uploads/2024/06/Final-Order-of-Dismissal-and-Settlement-Agreement.pdf)

## 25 독립된 수사 근거를 요구한 합의

2024년 합의는 얼굴 검색 이후의 절차를 구체적으로 바꿨습니다. 검색 결과만으로 사진 배열에 사람을 넣거나 체포 근거를 구성하는 일을 제한하고, 신뢰할 수 있는 독립된 근거를 요구했습니다. 사람이 최종 확인 버튼을 누르는 것에 더해, 그 사람이 판단할 때 어떤 추가 정보를 갖고 있는지가 중요한 설계 문제입니다.

추가 질문: 사람의 확인은 무엇을 추가해야 하는가?

다음 연결: 체포의 근거를 강화하는 통제와 별도로 체포 이전의 접촉 부담도 평가해야 한다.

출처: [S13](https://assets.aclu.org/live/uploads/2024/06/Final-Order-of-Dismissal-and-Settlement-Agreement.pdf), [S12](https://www.aclu.org/cases/williams-v-city-of-detroit-face-recognition-false-arrest?document=Settlement-Agreement)

## 26 체포 이전에도 생기는 부담

판결문은 Thompson이 자신의 형제로 오인되어 정지와 질문을 받고 신원을 증명하도록 요구받은 경험을 기록합니다. 오류의 부담은 체포 여부만으로 모두 표현되지 않습니다. 통행을 멈춘 시간, 요구받은 정보, 반복 접촉이 있었는지 같은 내용도 시민이 겪는 영향을 설명합니다. 이런 기록이 있어야 경보를 검토하는 절차의 실제 효과도 평가할 수 있습니다.

추가 질문: 잘못된 경보의 부담은 체포 전에도 발생하는가?

다음 연결: 오인접촉의 부담에 더해 정확히 찾은 사람에게 어떤 목적으로 사용했는지도 문제된다.

출처: [F03](https://www.judiciary.uk/wp-content/uploads/2026/04/AC-2024-LON-001764-R-Thompson-and-Carlo-version-for-hand-down-21-04-2026.pdf)

## 27 평화적 시위자를 찾아낸 얼굴인식

Glukhin은 정치적 메시지를 담은 판지 인형과 함께 지하철에서 평화적으로 시위했습니다. 당국은 그를 식별하고 찾아내 행정위반 절차로 처벌했습니다. 유럽인권재판소는 사생활과 표현의 자유 침해를 인정했습니다. 정확히 같은 사람을 찾았더라도, 어떤 행위를 대상으로 어느 정도의 정보처리를 사용할지는 별도의 비례 판단을 요구합니다.

추가 질문: 정확한 식별이라도 사용 목적에 따라 권리 문제가 생기는가?

다음 연결: 권리 침해에 이의를 제기하려면 삭제할 정보와 남길 판단 기록을 함께 설계한다.

출처: [F04](https://hudoc.echr.coe.int/app/conversion/pdf/?library=ECHR&id=001-225655&filename=CASE%20OF%20GLUKHIN%20v.%20RUSSIA.pdf)

## 28 삭제와 권리구제를 함께 설계하기

정보를 오래 남기면 다시 검색하거나 다른 목적으로 사용할 가능성이 커집니다. 반대로 잘못된 접촉에 관한 기록까지 즉시 사라지면 당사자가 어떤 판단을 받았는지 확인하기 어렵습니다. 원영상, 비교용 특징, 경보와 담당자 판단, 접근 이력을 구분하면 수집 최소화와 권리구제를 각각 뒷받침하는 보존 기준을 설계할 수 있습니다.

추가 질문: 빠른 삭제와 오류 구제를 어떻게 함께 보장하는가?

다음 연결: 개별 보호 설계는 국내 기관이 요구한 도입 전의 법적 근거와 영향평가에 연결된다.

출처: [F02](https://www.judiciary.uk/wp-content/uploads/2020/08/R-Bridges-v-CC-South-Wales-ors-Judgment.pdf), [F01](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5), [D37](https://www.humanrights.go.kr/webzine/webzineListAndDetail?boardNo=7608823&issueNo=7608811)

## 29 보호 입법 전 도입 중지 권고

인권위는 실시간 원격 얼굴인식에 대해 보호 입법과 엄격한 통제를 요구했습니다. 국무조정실은 개별적인 법적 근거가 없는 도입은 하지 않겠다고 회신했고, 인권위는 이를 수용으로 판단했습니다. 권고의 핵심은 최초 도입뿐 아니라 용도와 규모가 크게 바뀔 때에도 독립적으로 권리 영향을 검토하자는 것입니다.

추가 질문: 국내 인권기구와 정부 회신은 어떤 출발 조건을 제시했는가?

다음 연결: 도입을 유예하자는 권고와 함께 엄격한 조건 아래 활용하자는 국내 숙의 결과가 있다.

출처: [D01](https://www.humanrights.go.kr/base/board/read?boardManagementNo=24&boardNo=7609889&menuLevel=3&menuNo=91&page=1&searchCategory=&searchType=&searchWord=), [D37](https://www.humanrights.go.kr/webzine/webzineListAndDetail?boardNo=7608823&issueNo=7608811)

## 30 엄격한 조건 아래 중범죄 대응 활용

경기도의 도민인권배심회의는 중범죄 대응을 위한 실시간 얼굴인식을 다뤘습니다. 공식 발표는 엄격한 조건과 보호장치 아래 활용하는 경우에 대한 허용 의견을 전합니다. 동시에 오인 수사와 체포, 편향과 낙인의 위험도 논의됐습니다. 같은 기술에 관한 국내 논의에서도 허용할 목적과 먼저 갖출 조건이 판단을 구성합니다.

추가 질문: 국내 시민 숙의에서는 어떤 조건으로 활용 의견을 제시했는가?

다음 연결: 국내의 조건부 논의와 비교해 EU 법률은 금지와 예외 목적을 구체적으로 구분한다.

출처: [D02](https://gnews.gg.go.kr/briefing/brief_gongbo_view.do?BS_CODE=S017&number=67424)

## 31 EU의 원칙적 금지와 세 예외

EU는 법집행 목적의 공공장소 실시간 원격 생체식별을 원칙적으로 금지하고, 엄격히 필요한 경우에 한해 세 범주의 예외를 둡니다. 특정 피해자와 실종자 수색, 중대한 생명·안전 또는 테러 위협, 일정한 중대범죄의 용의자 식별입니다. 예외 목적을 충족하는지와 구체적 배치를 허가할지는 추가 요건을 통해 판단합니다.

추가 질문: EU는 어떤 목적에 예외 가능성을 두는가?

다음 연결: 법정 예외 목적에 해당하는 배치에도 허가·기간·장소·대상 제한이 붙는다.

출처: [F01](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5)

## 32 구체적 배치의 사전 허가

EU의 예외를 적용하려면 회원국의 법률이 사용 가능 범위와 세부 절차를 정하고, 사법기관이나 독립 행정기관이 구체적인 신청을 심사합니다. 긴급한 경우 사전 허가 없이 시작할 수 있지만 지체 없이, 늦어도 24시간 안에 허가를 신청해야 합니다. 거절되면 즉시 중단하고 관련 데이터와 결과를 삭제하도록 합니다.

추가 질문: 예외 목적에 해당하면 어떤 허가를 더 받아야 하는가?

다음 연결: 배치 통제의 구체성은 명단·장소의 재량을 심사한 영국 판결에서 드러난다.

출처: [F01](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5)

## 33 명단과 장소에 남겨진 재량

Bridges 판결은 명단에 누가 들어갈 수 있는지와 어떤 장소에 배치할 수 있는지를 구체적으로 물었습니다. 정보수집상 관심이 있다는 이유만으로 명단을 넓힐 여지가 있었고, 장소 선택의 한계도 충분히 정해져 있지 않았습니다. 항소법원은 이런 재량의 폭과 영향평가·평등의무 문제를 인정했습니다. 시스템의 정확성과 함께 누구에게 사용될지를 통제하는 기준이 필요합니다.

추가 질문: 경찰의 명단·장소 선택에는 어떤 구체성이 필요한가?

다음 연결: 2020년의 재량 통제 문제와 구분해 2026년 판결은 다른 경찰의 구체화된 정책을 심사했다.

출처: [F02](https://www.judiciary.uk/wp-content/uploads/2020/08/R-Bridges-v-CC-South-Wales-ors-Judgment.pdf)

## 34 구체화된 정책을 심사한 2026년 판결

2026년 판결이 심사한 것은 2024년 9월 채택된 런던경찰 정책의 명확성과 재량 통제였습니다. 법원은 명단과 장소, 비례성 검토를 연결한 지침을 전체적으로 읽고 자의적 운용을 통제할 구조가 있다고 보았습니다. 원고들이 제기한 법의 명확성 쟁점에서 청구가 기각됐습니다. 구체적인 배치의 필요성과 비례성은 그 배치의 사정을 바탕으로 판단하게 됩니다.

추가 질문: 2026년 법원은 어떤 정책의 어떤 쟁점을 판단했는가?

다음 연결: 사용 조건을 정하는 판단에는 신원을 식별하지 않는 안전 기능의 선택도 포함된다.

출처: [F03](https://www.judiciary.uk/wp-content/uploads/2026/04/AC-2024-LON-001764-R-Thompson-and-Carlo-version-for-hand-down-21-04-2026.pdf)

## 35 신원을 식별하지 않는 상황 탐지

파리 올림픽의 실험은 위험 상황을 먼저 찾는 기능에 초점을 맞췄습니다. 여덟 가지 사건 범주에는 버려진 물건, 쓰러진 사람, 높은 군중 밀도와 화재 등이 포함됩니다. 얼굴과 생체 신원식별은 제외했고 경보 뒤에는 사람이 영상을 확인했습니다. 안전 목표가 혼잡이나 사고 탐지라면 어떤 기술이 그 목표에 직접 답하는지를 구분할 수 있습니다.

추가 질문: 안전 목적을 위해 신원식별 외에 어떤 기능을 선택할 수 있는가?

다음 연결: 상황 탐지와 얼굴식별의 과업을 구분하면 목적별 대안의 조합을 비교할 수 있다.

출처: [F15](https://www.legifrance.gouv.fr/juri/id/CONSTEXT000047602516), [S17](https://www.cnil.fr/en/2024-olympics-cnils-qa-your-privacy-and-freedoms)

## 36 목적에 맞는 수단의 선택

정책 선택은 기술 이름보다 해결하려는 과업에서 시작할 수 있습니다. 특정 수배자의 소재를 찾는 일, 실종자의 이동 경로를 좁히는 일, 행사장 혼잡에 대응하는 일은 필요한 출력이 다릅니다. 기존 수사와 사후 검색, 상황 탐지, 현장 인력은 함께 사용할 수도 있습니다. 같은 목적에 대해 어느 조합이 더 빠르고 부담이 적은지 비교할 자료가 필요합니다.

추가 질문: 대안은 어떤 공통 과업을 기준으로 비교하는가?

다음 연결: 수단 선택이 운영 중에도 검토되려면 시작·확대·중단의 책임 주체가 필요하다.

출처: [S04](https://gonggam.korea.kr/newsContentView.es?mid=a12603000000&news_id=a19b4b5e-fad6-4a3a-9120-5e9488c3a8d9&section_id=), [S14](https://news.met.police.uk/news/child-sex-offender-identified-through-mets-live-facial-recognition-sentenced-505799), [F05](https://www.met.police.uk/SysSiteAssets/media/downloads/force-content/met/advice/lfr/other-lfr-documents/live-facial-recognition-annual-report-2025.pdf), [S17](https://www.cnil.fr/en/2024-olympics-cnils-qa-your-privacy-and-freedoms), [D39](https://record.council.jeju.kr/CLRecords/Files/FileAppendix/a12/A044556.pdf)

## 37 시작·확대·중단의 책임

허용 여부를 정하는 결정은 운영이 시작된 뒤에도 계속됩니다. 명단과 촬영 범위가 늘거나 용도가 바뀌면 영향을 받는 사람도 달라집니다. 그래서 운영기관이 남길 기록, 독립 평가자의 자료 접근권, 중단을 명할 주체를 구체화할 수 있습니다. 오류가 생긴 시민이 어디에 이의를 제기하고 어떤 자료를 통해 정정받을지도 설계에 포함됩니다.

추가 질문: 운영의 확대와 중단은 누가 어떤 자료로 결정하는가?

다음 연결: 통제 책임을 갖춘 설계는 도입 시점과 허용 범위의 정책 선택으로 구체화된다.

출처: [D37](https://www.humanrights.go.kr/webzine/webzineListAndDetail?boardNo=7608823&issueNo=7608811), [F01](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5), [F16](https://documents.un.org/doc/undoc/gen/g21/249/21/pdf/g2124921.pdf)

## 38 허용 범위를 정하는 세 선택

도입 유예, 제한적 허용, 한정 운영 뒤의 단계적 확대는 시점과 범위를 다르게 정합니다. 세 선택 모두 기존의 수사와 시민 보호 의무를 전제로 구체화해야 합니다. 제한적으로 허용한다고 하더라도 어떤 범죄와 어느 명단을 포함할지, 한 번의 허가가 어디까지 미칠지를 정해야 실제 정책이 됩니다.

추가 질문: 허용 여부를 구체적인 정책 선택으로 어떻게 표현하는가?

다음 연결: 정책 선택을 지지하려면 대응 필요성과 기존 수사 대비 추가 성과의 기준을 밝혀야 한다.

출처: [D01](https://www.humanrights.go.kr/base/board/read?boardManagementNo=24&boardNo=7609889&menuLevel=3&menuNo=91&page=1&searchCategory=&searchType=&searchWord=), [D02](https://gnews.gg.go.kr/briefing/brief_gongbo_view.do?BS_CODE=S017&number=67424), [D37](https://www.humanrights.go.kr/webzine/webzineListAndDetail?boardNo=7608823&issueNo=7608811), [F01](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5), [F16](https://documents.un.org/doc/undoc/gen/g21/249/21/pdf/g2124921.pdf)

## 39 필요성과 추가 성과의 판단

실제 수배자를 찾아낸 사례는 신속한 대응의 이익을 구체적으로 보여 줍니다. 그 이익에 큰 비중을 두는 입장은 중대한 위험을 놓칠 부담을 강조할 수 있습니다. 반면 통행인 전체를 대조하는 부담을 중시하면 기존 수사보다 더 얻는 성과의 입증을 요구할 수 있습니다. 어느 정도의 위험과 추가 이익이면 허용할지 판단 기준을 밝혀야 합니다.

추가 질문: 필요성과 성과에 대한 어떤 전제가 결론을 바꾸는가?

다음 연결: 성과의 이유와 함께 정보를 처리하고 사람에게 개입할 법적 문턱을 정해야 한다.

출처: [S14](https://news.met.police.uk/news/child-sex-offender-identified-through-mets-live-facial-recognition-sentenced-505799), [F05](https://www.met.police.uk/SysSiteAssets/media/downloads/force-content/met/advice/lfr/other-lfr-documents/live-facial-recognition-annual-report-2025.pdf), [D39](https://record.council.jeju.kr/CLRecords/Files/FileAppendix/a12/A044556.pdf)

## 40 법적 근거와 현장 판단의 문턱

도입의 근거를 어떻게 정할지와 개별 시민에게 무엇을 할 수 있을지는 연결되지만 서로 다른 판단입니다. 영국의 정책 심사는 운용 기준이 재량을 얼마나 통제하는지를 보여 줍니다. 한국에서는 관련 개인정보 처리 근거와 경찰작용·형사절차 요건을 적용해야 합니다. 법률과 지침, 사전 허가 중 어디에서 어느 내용을 구체화할지 자신의 이유를 제시할 수 있습니다.

추가 질문: 법률·지침·허가와 현장 확인은 각각 무엇을 맡는가?

다음 연결: 법적 문턱을 갖춘 운영에서도 남는 오류·접촉·정보 축적의 부담을 판단한다.

출처: [D01](https://www.humanrights.go.kr/base/board/read?boardManagementNo=24&boardNo=7609889&menuLevel=3&menuNo=91&page=1&searchCategory=&searchType=&searchWord=), [F01](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5), [F03](https://www.judiciary.uk/wp-content/uploads/2026/04/AC-2024-LON-001764-R-Thompson-and-Carlo-version-for-hand-down-21-04-2026.pdf), [X01](https://law.go.kr/LSW/lsSideInfoP.do?docCls=jo&joBrNo=00&joNo=0003&lsiSeq=282479&urlMode=lsScJoRltInfoR), [X02](https://www.law.go.kr/LSW/lsLinkCommonInfo.do?lsJoLnkSeq=1013583337), [S13](https://assets.aclu.org/live/uploads/2024/06/Final-Order-of-Dismissal-and-Settlement-Agreement.pdf)

## 41 오류 부담과 남길 기록

확인 절차가 잘못된 체포를 줄이는지 평가하는 일과 정지·질문 자체의 부담을 평가하는 일이 함께 필요합니다. 시스템이 정확히 찾은 경우에도 사용 목적이 지나치게 넓으면 표현과 이동의 자유가 제한될 수 있습니다. 어떤 정보는 빠르게 삭제하고 어떤 기록은 구제를 위해 남길지, 대상과 기간을 구분해 기준을 설명해야 합니다.

추가 질문: 어떤 오류와 권리 부담을 감수할 수 있으며 기록은 얼마나 남기는가?

다음 연결: 부담과 근거 공백을 다루는 방식은 시작 전 입증과 운영 후 평가의 선택으로 이어진다.

출처: [F05](https://www.met.police.uk/SysSiteAssets/media/downloads/force-content/met/advice/lfr/other-lfr-documents/live-facial-recognition-annual-report-2025.pdf), [F03](https://www.judiciary.uk/wp-content/uploads/2026/04/AC-2024-LON-001764-R-Thompson-and-Carlo-version-for-hand-down-21-04-2026.pdf), [F04](https://hudoc.echr.coe.int/app/conversion/pdf/?library=ECHR&id=001-225655&filename=CASE%20OF%20GLUKHIN%20v.%20RUSSIA.pdf), [F02](https://www.judiciary.uk/wp-content/uploads/2020/08/R-Bridges-v-CC-South-Wales-ors-Judgment.pdf), [D37](https://www.humanrights.go.kr/webzine/webzineListAndDetail?boardNo=7608823&issueNo=7608811)

## 42 운영하며 평가할 것인가, 먼저 입증할 것인가

현장 자료를 얻기 위해 한정 운영을 시작하자는 입장은 운영 자체가 정보의 공백을 줄인다고 봅니다. 먼저 입증하자는 입장은 그 정보를 얻는 동안 시민에게 발생하는 부담을 강조합니다. 어느 선택이든 평가 결과가 실제 중단과 재승인에 영향을 주어야 합니다. 운영기관과 독립 감독자의 권한·예산·자료 접근을 구체적으로 적으면 실행 가능성까지 검토할 수 있습니다.

추가 질문: 근거가 충분하지 않을 때 시작과 중단의 책임을 어떻게 배분하는가?

다음 연결: 앞의 판단 조건들을 필요·근거·성과·부담·조치·기록·감독의 일곱 질문으로 회수한다.

출처: [D37](https://www.humanrights.go.kr/webzine/webzineListAndDetail?boardNo=7608823&issueNo=7608811), [F16](https://documents.un.org/doc/undoc/gen/g21/249/21/pdf/g2124921.pdf), [F05](https://www.met.police.uk/SysSiteAssets/media/downloads/force-content/met/advice/lfr/other-lfr-documents/live-facial-recognition-annual-report-2025.pdf)

## 43 판단에 남는 일곱 질문

이 일곱 질문은 허용 여부를 구체적인 조건으로 바꿉니다. 필요성과 추가 성과는 무엇을 얻으려는지, 법적 근거와 현장 조치는 어떤 권한으로 행동하는지 묻습니다. 오류·노출과 기록·구제는 시민이 겪는 부담을 다루고, 감독·중단은 그 조건이 운영 중에도 지켜지게 할 주체를 묻습니다. 자신의 결론을 좌우하는 질문을 골라 자료와 이유를 연결할 수 있습니다.

추가 질문: 최종 결론을 바꾸는 핵심 질문은 무엇인가?

다음 연결: 일곱 질문 중 자기 결론을 좌우하는 조건을 골라 근거와 변경 조건을 적는다.

출처: [D01](https://www.humanrights.go.kr/base/board/read?boardManagementNo=24&boardNo=7609889&menuLevel=3&menuNo=91&page=1&searchCategory=&searchType=&searchWord=), [D02](https://gnews.gg.go.kr/briefing/brief_gongbo_view.do?BS_CODE=S017&number=67424), [D37](https://www.humanrights.go.kr/webzine/webzineListAndDetail?boardNo=7608823&issueNo=7608811), [F01](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5), [F02](https://www.judiciary.uk/wp-content/uploads/2020/08/R-Bridges-v-CC-South-Wales-ors-Judgment.pdf), [F03](https://www.judiciary.uk/wp-content/uploads/2026/04/AC-2024-LON-001764-R-Thompson-and-Carlo-version-for-hand-down-21-04-2026.pdf), [F04](https://hudoc.echr.coe.int/app/conversion/pdf/?library=ECHR&id=001-225655&filename=CASE%20OF%20GLUKHIN%20v.%20RUSSIA.pdf), [F05](https://www.met.police.uk/SysSiteAssets/media/downloads/force-content/met/advice/lfr/other-lfr-documents/live-facial-recognition-annual-report-2025.pdf), [X01](https://law.go.kr/LSW/lsSideInfoP.do?docCls=jo&joBrNo=00&joNo=0003&lsiSeq=282479&urlMode=lsScJoRltInfoR), [X02](https://www.law.go.kr/LSW/lsLinkCommonInfo.do?lsJoLnkSeq=1013583337)

## 44 나의 결론과 판단을 바꿀 조건

결론은 허용 또는 유예라는 말에 조건을 붙여 완성할 수 있습니다. 어느 범죄와 명단, 어느 장소와 기간을 말하는지 적어 보십시오. 핵심 자료 두 개를 고르고 그 자료에서 왜 자신의 결론이 나오는지 설명하면 전제가 드러납니다. 이어서 자신의 선택이 남기는 부담과 판단을 바꿀 새로운 사실을 적으면, 질의와 토론에서 검토할 부분이 분명해집니다.

추가 질문: 나의 정책 결론은 어떤 자료·전제·변경 조건에 기반하는가?

다음 연결: 본편 판단 활동이 끝난 뒤 보충 자료는 개별 질문이 있을 때 선택한다.

출처: [D01](https://www.humanrights.go.kr/base/board/read?boardManagementNo=24&boardNo=7609889&menuLevel=3&menuNo=91&page=1&searchCategory=&searchType=&searchWord=), [D02](https://gnews.gg.go.kr/briefing/brief_gongbo_view.do?BS_CODE=S017&number=67424), [F01](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5), [F05](https://www.met.police.uk/SysSiteAssets/media/downloads/force-content/met/advice/lfr/other-lfr-documents/live-facial-recognition-annual-report-2025.pdf)

## 45 보충 자료

개인 기기의 얼굴 확인, 광고 이미지의 오인, 민간 공연장의 출입 명단은 얼굴인식에 맡기는 과업과 목적이 어떻게 달라지는지 보여 줍니다. 국내의 데이터 처리 판단과 관제 운영 자료는 정보 처리와 권리구제를 더 구체적으로 검토할 수 있게 합니다.

추가 질문: 보충 자료는 어떤 질문을 더 설명하는가?

다음 연결: 익숙한 기기의 본인 확인은 거리의 명단 검색과 과업을 구분할 출발점이 된다.

출처: [S11](https://zjnews.zjol.com.cn/zjnews/nbnews/201811/t20181122_8807787.shtml), [S15](https://ag.ny.gov/press-release/2023/attorney-general-james-seeks-information-madison-square-garden-regarding-use), [S18](https://www.apple.com/kr/newsroom/2017/09/the-future-is-here-iphone-x/), [S20](https://obj.umiacs.umd.edu/papers_for_stories/chellappa_facial_recognition.pdf), [D18](https://www.korea.kr/briefing/policyBriefingView.do?newsId=156505203)

## 46 Face ID와 거리의 1:N 검색

휴대전화의 얼굴 잠금 해제는 익숙한 1:1 확인의 예입니다. 이용자가 등록한 얼굴과 지금 제시한 얼굴이 같은지 묻습니다. 거리의 1:N 검색은 명단 속 여러 사람 중 후보를 찾고, 명단 밖 통행인의 얼굴도 입력받습니다. 사용자의 행동과 대조 범위가 달라지므로 각 과업에 맞는 성능과 권리 기준이 필요합니다.

추가 질문: 본인 확인과 명단 검색은 무엇이 다른가?

다음 연결: 대조 과업을 구분한 뒤 얼굴 이미지와 실제 사람·행위를 연결하는 오류를 살핀다.

출처: [S18](https://www.apple.com/kr/newsroom/2017/09/the-future-is-here-iphone-x/), [S19](https://support.apple.com/en-us/102381), [F02](https://www.judiciary.uk/wp-content/uploads/2020/08/R-Bridges-v-CC-South-Wales-ors-Judgment.pdf)

## 47 버스 광고가 보행자로 잡힌 날

이 사건의 얼굴은 현장을 걷던 사람의 얼굴이 아니라 버스 광고에 인쇄된 얼굴이었습니다. 시스템의 표시에는 실제 사람과 이미지 속 인물, 보행 행위의 연결 문제가 들어 있습니다. 경찰은 오류를 인정하고 표시를 지웠습니다. 얼굴을 찾는 단계와 그 얼굴에 특정 행동을 귀속시키는 단계가 각각 검토 대상이라는 점을 보여 줍니다.

추가 질문: 시스템은 얼굴의 존재와 사람의 행동을 어떻게 연결했는가?

다음 연결: 맥락을 정확히 연결한 뒤에도 검색 명단에 포함할 목적과 이유가 남는다.

출처: [S11](https://zjnews.zjol.com.cn/zjnews/nbnews/201811/t20181122_8807787.shtml)

## 48 공연장 출입을 막은 검색 명단

공연장의 얼굴인식은 범죄 용의자 명단과 다른 목적의 명단을 사용했습니다. 회사와 소송 관계에 있는 로펌의 변호사라는 이유로 출입을 제한한 것입니다. 뉴욕주 법무장관은 관련 정보 제출을 요구했습니다. 식별이 정확한지에 더해, 명단에 포함될 이유와 그에 따른 불이익이 정당한지라는 질문이 남습니다.

추가 질문: 얼굴인식의 정확도 외에 어떤 명단 기준을 검토해야 하는가?

다음 연결: 명단 목적과 별도로 독립된 사람·알고리즘 판단의 결합을 실험할 수 있다.

출처: [S15](https://ag.ny.gov/press-release/2023/attorney-general-james-seeks-information-madison-square-garden-regarding-use), [S16](https://ag.ny.gov/sites/default/files/2023-01/nys_oag_letter_to_madison_square_garden_entertainment_corp.pdf)

## 49 독립 판단 점수를 결합한 사진 실험

이 연구는 사람과 알고리즘이 각각 사진쌍을 평가한 뒤 연구진이 점수를 결합한 실험입니다. 같은 사람인 사진 12쌍과 다른 사람인 사진 8쌍, 총 20쌍의 어려운 문제를 사용했습니다. 연구진은 점수 척도를 맞춰 평균했고, 전문가와 성능이 높은 알고리즘의 결합에서 좋은 정확도가 나타났습니다. 두 판단의 정보가 서로 얼마나 겹치고 보완되는지 검토하는 연구입니다.

추가 질문: 사람과 알고리즘의 결합은 이 연구에서 어떻게 이루어졌는가?

다음 연결: 연구의 학습·평가 데이터와 연결해 국내 AI 사업의 처리 목적·위탁 판단을 살핀다.

출처: [S20](https://obj.umiacs.umd.edu/papers_for_stories/chellappa_facial_recognition.pdf), [S21](https://www.nist.gov/news-events/news/2018/05/nist-study-shows-face-recognition-experts-perform-better-ai-partner)

## 50 출입국 AI 사업의 처리 목적과 위탁

개인정보위는 출입국 심사를 위한 법적 근거와 처리 목적, 위탁 관계를 나누어 판단했습니다. 심사 고도화를 위한 AI 학습과 감독하의 위탁은 인정하면서, 위탁 사실을 공개하지 않은 행위에는 과태료를 부과했습니다. 이상행동 추적용 CCTV 영상은 실제로 사용되지 않아 해당 부문 판단을 유보했습니다. 처리의 대상·목적·행위마다 법적 평가가 달라지는 국내 사례입니다.

추가 질문: 같은 AI 사업에서도 무엇을 기준으로 적법성과 의무 위반을 나누었는가?

다음 연결: 행정기관의 처리 판단과 별개로 헌법소원은 사후 심판의 소송요건을 검토했다.

출처: [D18](https://www.korea.kr/briefing/policyBriefingView.do?newsId=156505203)

## 51 사업 종료 뒤의 헌법소원 각하

이 헌법소원은 출입국 데이터의 AI 학습과 보관 등을 둘러싼 사건입니다. 헌재는 사업이 끝나고 데이터가 삭제된 사정, 법률조항이 직접 권리를 침해하는지 등의 소송요건을 심사했습니다. 결론은 전원일치 각하였습니다. 정보 처리의 기간과 기록 보존 방식은 당사자가 사후에 다툴 수 있는 조건과도 연결됩니다.

추가 질문: 이 헌재 결정은 어떤 요건을 심사해 청구를 끝냈는가?

다음 연결: 데이터를 둘러싼 국내 판단과 함께 검색 범위를 넓히는 실제 사업계획을 살핀다.

출처: [D09](https://www.ccourt.go.kr/site/kor/ex/bbs/View.do?bcIdx=4264348&cbIdx=1195)

## 52 자치구 경계를 넘는 영상 검색

실종자가 자치구 경계를 넘으면 한 구의 영상만으로 이동 경로를 찾기 어려울 수 있습니다. 서울시는 2026년 4월 발표에서 외형 특징 검색을 25개 자치구 전체로 확대하는 계획을 제시했습니다. 범위를 넓히는 운영에서는 누가 검색을 요청하고 어느 영상에 접근하며, 결과를 현장 수색에 어떻게 전달할지가 구체적인 과제가 됩니다.

추가 질문: 영상 검색 범위를 넓히면 어떤 협력과 통제가 필요한가?

다음 연결: 검색 범위 확대의 운영 과제에는 경보를 사용하는 요원의 경험도 포함된다.

출처: [S05](https://www.seoul.go.kr/news/news_report.do?nttNo=455379)

## 53 관제요원이 평가한 선별관제

이 조사는 관제요원이 지능형 선별관제를 사용하면서 느낀 정확도를 물었습니다. 전체 설문 35명 가운데 정확도 문항에는 34명이 답했고, 27명이 50퍼센트 미만 범주를 선택했습니다. 실제 영상에 정답을 붙여 측정한 성능과는 측정 방식이 다릅니다. 요원이 경보를 얼마나 신뢰하고 업무에 활용하는지를 파악하는 국내 운영 자료입니다.

추가 질문: 이 숫자는 누구의 무엇에 대한 평가인가?

다음 연결: 보충 자료는 본편의 성과·권리·운영 판단에 필요한 질문으로 회수한다.

출처: [D39](https://record.council.jeju.kr/CLRecords/Files/FileAppendix/a12/A044556.pdf)
