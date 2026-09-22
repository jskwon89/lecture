import fs from 'node:fs/promises';
import { Presentation, PresentationFile } from '@oai/artifact-tool';
const base='/workspace/scratch/f938a546368b';
const p=Presentation.create({slideSize:{width:1280,height:720}});
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
await (await PresentationFile.exportPptx(p)).save(base+'/ch1_case_build/candidate_raw.pptx');
console.log('Created one editable slide');
