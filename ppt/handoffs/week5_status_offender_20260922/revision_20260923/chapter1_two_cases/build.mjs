import fs from 'node:fs/promises';
import { Presentation, PresentationFile } from '@oai/artifact-tool';
const base='/workspace/scratch/f938a546368b';
const p=Presentation.create({slideSize:{width:1280,height:720}});
function addManualCase(){
const s=p.slides.add(); s.background.fill='#FFFFFF';
const C={navy:'#1E2761',blue:'#5A6699',gold:'#C2A648',body:'#222633',gray:'#464D5C',muted:'#6E7686',line:'#DCE0E8'};
function rect(name,x,y,w,h,color){return s.shapes.add({name,geometry:'rect',position:{left:x,top:y,width:w,height:h},fill:color,line:{fill:'none',width:0}})}
function txt(name,value,x,y,w,h,pt=14,color=C.body,bold=false,align='left'){
 const a=s.shapes.add({name,geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
 a.text=value;a.text.style={typeface:'Pretendard',fontSize:pt*4/3,color,bold,alignment:align,verticalAlignment:'top',insets:{left:0,right:0,top:0,bottom:0},autoFit:'none',wrap:'none',lineSpacing:1.25};return a;
}
txt('chapter','1. 논제의 대상과 현행 우범소년 제도',76.8,38.4,550,30,12.5,C.gray,true);
txt('next','다음 → 성범죄 연루 우려가 제시된 송치 사례',650,40.3,552.6,27,10.5,C.muted,false,'right');
txt('title','가정폭력·장기가출 뒤 시설 위탁으로 이어진 사례',76.8,80,1126.1,57,27.5,C.navy,true);
rect('header_rule',76.8,145.6,1126.1,1.6,C.navy);
txt('summary','법원 실무자료는 조건만남으로 가출 생활을 유지할 가능성을 소년보호시설 위탁의 이유로 제시한다.',76.8,166,1126.1,45,13,C.navy,true);
const x1=76.8,x2=659.52,w=543.36;
rect('left_section_rule',x1,229,w,4,C.blue);
rect('right_section_rule',x2,229,w,4,C.blue);
txt('left_header','가출 경위와 기존 지원',x1,248,w,30,14,C.navy,true);
txt('right_header','법원 개입과 처분 이유',x2,248,w,30,14,C.navy,true);
txt('left_key_1','쉼터 입소 후에도 가출이 장기화됐다',x1,290,w,27,14,C.body,true);
txt('left_detail_1','음주 신고 뒤 귀가를 거부해 쉼터에 입소했다.\n임시퇴소 후 학교의 연락을 받지 않았고,\n아버지와의 갈등 속에서 가출이 장기화됐다.',x1,320,w,70,12.5,C.gray);
txt('right_key_1','연락 불응 뒤 동행영장이 발부됐다',x2,290,w,27,14,C.body,true);
txt('right_detail_1','아버지와 연락이 끊겼고, 조사관의 전화·문자에도\n응답하지 않았다. 동행영장이 발부되었으며\n소년분류심사원에 임시위탁되었다.',x2,320,w,70,12.5,C.gray);
txt('left_key_2','아버지의 폭력으로 사례관리가 진행 중이었다',x1,402,w,27,14,C.body,true);
txt('left_detail_2','아동보호전문기관의 사례관리와 함께\n청소년의 조건만남 정황도 자료에 기록됐다.',x1,432,w,49,12.5,C.gray);
txt('right_key_2','조건만남을 통한 생활 지속 가능성을 들었다',x2,402,w,27,14,C.body,true);
txt('right_detail_2','실무자료는 이 가능성이 높아\n소년보호시설 위탁 처분이 이루어졌다고 설명한다.',x2,432,w,49,12.5,C.gray);
const px=[76.8,461.76,846.72],pw=356.16;
for(let i=0;i<3;i++)rect('procedure_rule_'+i,px[i],515,pw,1.7,C.line);
txt('procedure_1','학교장 통고',px[0],529,pw,55,14,C.body,true);
txt('procedure_2','소년사건 조사·동행영장\n소년분류심사원 임시위탁',px[1],529,pw,55,14,C.body,true);
txt('procedure_3','소년보호시설 감호위탁(6호)\n장기보호관찰(5호)',px[2],529,pw,55,14,C.body,true);
txt('arrow_1','→',437.2,539,23,32,16,C.gold,true,'center');
txt('arrow_2','→',822.16,539,23,32,16,C.gold,true,'center');
rect('question_band',118.08,603.84,1040.64,48,C.navy);
txt('question','성착취 위험과 불안정한 생활에, 시설 위탁과 피해지원·주거지원은 각각 무엇을 제공할 수 있는가?',138,615.5,1001,28,12.5,'#FFFFFF',true,'center');
s.speakerNotes.textFrame.setText(`출처: 법원행정처, 『소년 통고 실무(2024년 개정판)』, 인쇄면 33쪽(PDF 42번째 면), 학교현장 통고 사례 7 「반복된 거짓말, 장기무단가출」. 공식 게시일 2024.12.20. 사건 발생·결정 연도와 동일시하지 않는다. 공식 원문 게시 페이지: https://www.scourt.go.kr/portal/news/NewsViewAction.work?gubun=713&seqnum=43\n확인 위치: '비행사실'에 음주 신고·귀가 거부·쉼터 입소·임시퇴소 후 학교 연락 불응·부와의 갈등 및 장기가출이 기재되어 있다. '특이사항'에는 부의 폭력에 따른 아동보호전문기관 사례관리, 소년의 조건만남 정황, 보호자 및 소년사건조사관과 연락 불응, 동행영장 발부와 소년분류심사원 임시위탁(구금)이 기재되어 있다. '처분내용'은 조건만남 등을 통해 가출 생활을 유지할 가능성이 높아 시설 위탁 처분이 이루어졌다고 설명하며, 소년보호시설 감호위탁과 장기보호관찰을 열거한다.\n처분 번호는 현행 소년법 제32조 제1항 제5호·제6호의 명칭과 대조하여 붙였다. https://law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1014134273\n설명: 이미 쉼터와 아동보호전문기관이 등장한 사건이다. 가정 내 폭력과 가출 중 생계·성착취 위험이 겹쳤고, 소년사법 경로에서는 신병 확보와 시설 위탁, 보호관찰로 대응한 사례로 설명한다. 해당 기관들이 제공한 구체적 지원의 내용·기간이나 부족했던 이유는 이 요약에 없으므로 '복지지원 실패가 확인됐다'고 단정하지 않는다.\n소년의 거짓말을 부의 폭력의 정당화 사유로 말하지 않는다. 원자료의 '조건만남 정황'과 '가출 생활을 유지할 가능성'을 성매매 피해 확정이나 청소년의 성범죄 가해 사실로 바꾸지 않는다. 실무자료의 사건 요약이며 사건번호·결정문·상세 요건 판단은 제시되지 않았다. '정당한 이유 없음'을 법원이 어떤 이유로 인정했는지까지 확정하는 판례로 사용하지 않는다.\n하단 질문은 강의상 비교 질문이다. 시설 위탁의 실제 효과 또는 피해지원·주거지원과의 비교 결과가 이 자료에 제시되어 있다는 뜻은 아니다. 다음 B 사건에서는 별도의 사정에 따라 7호 처분이 선택되었다는 점을 이어 설명한다.`);

}
function addBCase(){
const s=p.slides.add(); s.background.fill='#FFFFFF';
const C={navy:'#1E2761',blue:'#5A6699',gold:'#C2A648',body:'#222633',gray:'#464D5C',muted:'#6E7686',line:'#DCE0E8'};
function rect(name,x,y,w,h,color){return s.shapes.add({name,geometry:'rect',position:{left:x,top:y,width:w,height:h},fill:color,line:{fill:'none',width:0}})}
function txt(name,value,x,y,w,h,pt=14,color=C.body,bold=false,align='left'){
 const a=s.shapes.add({name,geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
 a.text=value;a.text.style={typeface:'Pretendard',fontSize:pt*4/3,color,bold,alignment:align,verticalAlignment:'top',insets:{left:0,right:0,top:0,bottom:0},autoFit:'none',wrap:'none',lineSpacing:1.25};return a;
}
txt('chapter','1. 논제의 대상과 현행 우범소년 제도',76.8,38.4,550,30,12.5,C.gray,true);
txt('next','다음 → 성착취 피해 위험과 장래 범법 우려',650,40.3,552.6,27,10.5,C.muted,false,'right');
txt('title','성범죄 연루 우려가 제시된 송치 사례',76.8,80,1126.1,57,27.5,C.navy,true);
rect('header_rule',76.8,145.6,1126.1,1.6,C.navy);
txt('summary','담당 변호사의 보고에는 가정폭력 환경에서 가출한 청소년의 송치 경위와 7호 처분에 고려된 사정이 제시되어 있다.',76.8,166,1126.1,47,13,C.navy,true);
const xs=[76.8,461.76,846.72],w=356.16;
const heads=['① 가출의 배경','② 송치에 이른 과정','③ 처리 결과'];
const bodies=[
 'B는 부모의 다툼을 피해\n초등학교 때 처음 가출했다.\n가정폭력 위험으로\n아동보호전문기관과 구청의\n사례관리를 받고 있었다.',
 '아버지의 신고 후 경찰서장이\n소년부로 송치했다.\n가출, 부모 동의 없는 소액결제,\n성인 남성과의 접촉 등이 제시됐고\n‘성범죄 연루 우려’가 거론됐다.',
 '부모가 B를 보호하기 어렵다는 점,\n부모의 시설처분 요청,\nB의 치료 필요성 등이 고려되었다.\n분류심사원 위탁을 거쳐\n7호 보호처분을 받았다고 보고됐다.'
];
for(let i=0;i<3;i++){
 rect('column_rule_'+i,xs[i],281.5,w,4,C.blue);
 txt('column_header_'+i,heads[i],xs[i],300,w,28,14,C.navy,true);
 const body=txt('column_body_'+i,bodies[i],xs[i],344,w,160,14,C.body);
 const strong=i===0?['부모의 다툼을 피해','가정폭력 위험']:i===1?['부모 동의 없는 소액결제','성인 남성과의 접촉']:['부모가 B를 보호하기 어렵다는 점','부모의 시설처분 요청','B의 치료 필요성'];
 for(const q of strong) body.text.get(q).bold=true;
}
txt('arrow_1','→',437.2,404,23,32,16,C.gold,true,'center');
txt('arrow_2','→',822.16,404,23,32,16,C.gold,true,'center');
rect('definition_rule',76.8,533,1126.1,1,C.line);
txt('definition_label','현행 7호 처분',76.8,548,133,30,12.5,C.gray,true);
txt('definition','병원·요양소 또는 의료재활소년원에 위탁(소년법 제32조 제1항 제7호)',221,548,982,30,12.5,C.gray);
rect('question_band',118.08,603.84,1040.64,48,C.navy);
const q=txt('question','이 사례에서 소년부 송치와 치료를 위한 위탁은 각각 어떤 사정을 근거로 이루어졌는가?',138,615.5,1001,28,12.5,'#FFFFFF',true,'center');
s.speakerNotes.textFrame.setText(`강정은, 「아동의 권리에 비추어 본 우범소년 개정방향」, 『우범소년 규정 폐지 필요성 토론회』(2021.3.9), 인쇄면 18쪽. 두루 자료 게시 페이지: https://duroo.org/data/?bmode=view&idx=128595217\n발제자가 직접 수행한 B 사건의 보고이다. 법원 결정문이나 사건번호가 공개된 판례로 소개하지 않는다.\n보고에 따르면 부모가 B를 보호하기 어렵고 시설처분을 원하고 있으며 B에게 치료가 필요하다는 이유 등이 고려되어 7호 처분을 받았다. 이 설명은 해당 보고가 제시한 처분 사정이다. B의 진단명, 의료진 의견, 특정 시설 및 다른 대안 대신 7호를 선택한 법원의 상세 판단은 자료에서 확인되지 않는다. 원문 괄호의 '치료감호'를 현행 7호 처분의 정식 명칭으로 사용하지 않는다.\n현행 소년법 제32조 제1항 제7호: 병원, 요양소 또는 「보호소년 등의 처우에 관한 법률」에 따른 의료재활소년원에 위탁하는 처분.\n제32조 공식 확인 링크: https://law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1014134273\n설명: 송치 경위와 보호처분 선택의 사정을 순서대로 설명한다. 부모의 시설 요청 자체가 송치 법정요건을 대신하는 것으로 설명하지 않는다. 다음 장에서 성착취 피해 위험과 소년 자신의 장래 범법 우려를 구별한다.`);

}
addManualCase();
addBCase();
await (await PresentationFile.exportPptx(p)).save(base+'/ch1_cases_build/candidate_raw.pptx');
console.log('Created two case slides');
