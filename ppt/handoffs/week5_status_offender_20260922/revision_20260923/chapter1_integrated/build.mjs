import fs from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
import { Presentation, PresentationFile } from '@oai/artifact-tool';
const base=path.dirname(fileURLToPath(import.meta.url));
const D=JSON.parse(await fs.readFile(base+'/content.json','utf8'));
const p=Presentation.create({slideSize:{width:1280,height:720}});
const C={navy:'#1E2761',blue:'#5A6699',gold:'#C2A648',tg:'#A8871C',ink:'#222633',gray:'#464D5C',muted:'#6E7686',line:'#DCE0E8',light:'#F2F4F8',neutral:'#C9CEDA'};
let s;
function rect(name,x,y,w,h,color){return s.shapes.add({name,geometry:'rect',position:{left:x,top:y,width:w,height:h},fill:color,line:{fill:'none',width:0}})}
function txt(name,value,x,y,w,h,pt=14,color=C.ink,bold=false,align='left'){
 const a=s.shapes.add({name,geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
 a.text=value;a.text.style={typeface:'Pretendard',fontSize:pt*4/3,color,bold,alignment:align,verticalAlignment:'top',insets:{left:0,right:0,top:0,bottom:0},autoFit:'none',wrap:'none',lineSpacing:1.25};return a;
}
function baseSlide(n,next,summary,question=false){
 s=p.slides.add();s.background.fill='#FFFFFF';
 txt('chapter','1. 논제의 대상과 현행 우범소년 제도',76.8,38.4,550,30,12.5,C.gray,true);
 txt('next','다음 → '+next,650,40.3,552.6,27,10.5,C.muted,false,'right');
 txt('title',D.slides[n-1].title,76.8,80,1126.1,57,27.5,C.navy,true);
 if(question){rect('header_rule',76.8,145.6,1126.1,1.6,C.navy);txt('summary',summary,76.8,166,1126.1,49,13,C.navy,true);}
 else{rect('summary_bg',76.8,148.8,1126.1,57.6,C.light);rect('summary_marker',76.8,148.8,5,57.6,C.navy);txt('summary',summary,105.6,168,1080,28,13,C.navy,true);}
 return s;
}
function finish(n){const d=D.slides[n-1];s.speakerNotes.textFrame.setText([
  `제1장 ${n}/11 · ${d.title}\n목적: ${d.purpose}\n설명 시간: ${d.time} (수업 운영용 추정)`,
  '강의 대본\n'+d.script.join('\n\n'),'다음 연결\n'+d.transition,
  '자료 확인\n'+d.evidence,'설명 범위\n'+d.guard,
  d.optional?'선택 설명\n'+d.optional:'',
  '출처\n'+d.sources.map(id=>{let a=D.sources.find(q=>q.id===id);return `[${id}] ${a.name}\n${a.where}\n${a.url}\n${a.use}`}).join('\n\n')
 ].filter(Boolean).join('\n\n'));}
function conclusion(value){rect('conclusion_top',76.8,580.8,1126.1,1,C.line);txt('conclusion',value,76.8,603,1126.1,33,13,C.navy,true);rect('conclusion_bottom',76.8,645.1,1126.1,1.7,C.navy);}
function question(value){rect('question_band',118.08,603.84,1040.64,48,C.navy);txt('question',value,138,615.5,1001,28,12.5,'#FFFFFF',true,'center');}
function section(name,x,y,w,head,small=''){rect(name+'_rule',x,y,w,4,C.blue);txt(name+'_head',head,x,y+18,w,32,14,C.navy,true);if(small)txt(name+'_small',small,x,y+51,w,26,10.5,C.muted);}
const X=[76.8,461.76,846.72], W=356.16;

baseSlide(1,'우범소년의 세 요건','범죄소년·촉법소년은 이미 한 행위, 우범소년은 법정 사유와 장래 범법 우려를 기준으로 본다');
const h1=['죄를 범한 소년','촉법소년','우범소년'];
const b1=['14세 이상 19세 미만\n이미 범한 죄를 기준으로 본다.','10세 이상 14세 미만\n형벌 법령에 저촉되는 행위를 했지만\n형사책임 연령에 이르지 않았다.','10세 이상 19세 미만\n법정 우범사유와\n장래 범법 우려를 함께 본다.'];
for(let i=0;i<3;i++){rect('start_rule_'+i,X[i],266,W,4,i===2?C.blue:C.neutral);txt('article_'+i,'제4조 제1항 제'+(i+1)+'호',X[i],286,W,27,10.5,i===2?C.tg:C.gray,true);txt('start_'+i,h1[i],X[i],322,W,30,14,C.ink,true);txt('description_'+i,b1[i],X[i],365,W,83,12.5,C.gray);}
rect('definition_rule',76.8,466,1126.1,1,C.line);
txt('definition_label','우범·우범사유',76.8,491,200,56,13,C.navy,true);
txt('definition','우범(虞犯)은 ‘앞으로 범죄를 저지를 우려가 있다’는 뜻이다.\n우범사유는 그런 우려를 갖게 하는 행동이나 상황이다. 법 적용에서는 법정 사유를 확인한다.',286,490,917,64,12.5,C.ink);
conclusion('세 범주는 모두 소년법상 보호사건의 대상이지만, 보호사건이 성립하는 요건은 서로 다르다.');finish(1);

baseSlide(2,'가출과 법정 우범사유','소년법 제4조 제1항 제3호는 연령·법정 우범사유·장래 범법 우려를 함께 요구한다');
const heads2=['연령','법정 우범사유','장래의 우려'];
const bodies2=['10세 이상 19세 미만\n소년법 제2조·제4조 제1항 제3호','가목·나목·다목 중\n해당하는 사유가 있을 것','그의 성격이나 환경에 비추어\n앞으로 형벌 법령에 저촉되는\n행위를 할 우려가 있을 것'];
for(let i=0;i<3;i++){rect('requirement_rule_'+i,X[i],272,W,4,C.blue);txt('number_'+i,'요건 '+['①','②','③'][i],X[i],290,W,28,10.5,C.gray);txt('requirement_'+i,heads2[i],X[i],332,W,42,22.5,C.navy,true);txt('requirement_detail_'+i,bodies2[i],X[i],394,W,84,12.5,C.gray);}
txt('plus1','+',437.2,343,24,35,18,C.gold,true,'center');txt('plus2','+',822.16,343,24,35,18,C.gold,true,'center');
rect('judge_rule',76.8,509,1126.1,1,C.line);txt('judge_label','판단의 단계',76.8,533,180,31,13,C.navy,true);txt('judge_detail','경찰서장이 송치 전 요건을 판단하고, 소년부 판사가 조사·심리를 통해 요건과 처분 필요성을 판단한다.',262,533,941,32,12.5,C.ink);
conclusion('가출 사실만으로는 충분하지 않다. 법정 사유에 해당하는지와 장래 범법 우려를 함께 확인해야 한다.');finish(2);

baseSlide(3,'성착취 피해 위험과 장래 범법 우려','가출에 관한 나목은 “정당한 이유 없이 가출하는 것”을 법정 우범사유로 정한다');
rect('legal_table_start',76.8,234,1126.1,1.7,C.blue);
const rowY=[250,347,444];
rect('runaway_highlight',76.8,336,1126.1,92,C.light);
const legal=['집단적으로 몰려다니며 주위 사람들에게 불안감을 조성하는 성벽(性癖)이 있는 것','정당한 이유 없이 가출하는 것','술을 마시고 소란을 피우거나 유해환경에 접하는 성벽이 있는 것'];
for(let i=0;i<3;i++){txt('legal_label_'+i,['가목','나목','다목'][i],102,rowY[i]+7,135,35,13,i===1?C.tg:C.navy,true,'center');txt('legal_text_'+i,legal[i],255,rowY[i]+7,925,41,14,i===1?C.tg:C.ink,i===1);if(i<2)rect('row_rule_'+i,76.8,rowY[i]+79,1126.1,1,C.line);}
txt('habit_label','성벽(性癖)',76.8,525,180,29,12.5,C.navy,true);txt('habit','여기서는 행동상의 버릇·성향을 뜻한다. 성적인 습성을 뜻하는 말로 읽지 않는다.',255,525,948,31,12.5,C.gray);
conclusion('가출을 이유로 판단하려면, 집을 나온 경위와 돌아갈 가정의 상황도 확인해야 한다.');finish(3);

baseSlide(4,'우범소년 사건의 송치·통고 경로','성착취를 당할 위험과 청소년이 앞으로 범죄에 해당하는 행동을 할 우려는 서로 다른 질문이다');
const cx=[76.8,659.52], cw=543.36;
for(let i=0;i<2;i++){
 rect('comparison_header_'+i,cx[i],250,cw,43,C.blue);txt('comparison_name_'+i,i===0?'성착취 피해 위험':'소년법상 장래 범법 우려',cx[i]+12,260,cw-24,28,13,'#FFFFFF',true,'center');
 txt('risk_question_'+i,i===0?'“이 청소년이 피해를 당할 위험이 있는가?”':'“이 청소년이 범죄에 해당하는 행동을 할까?”',cx[i],321,cw,62,14,C.ink,true);
 txt('risk_description_'+i,i===0?'성매매·성착취의 피해자가 되거나\n다시 피해를 입을 가능성':'그 청소년의 성격이나 환경에 비추어\n앞으로 형벌 법령에 저촉되는 행위를 할 우려',cx[i],391,cw,60,12.5,C.gray);
 rect('risk_detail_rule_'+i,cx[i],472,cw,1,C.line);txt('risk_view_'+i,i===0?'판단할 것  ·  안전한 거처, 생계, 상담·치료 등':'판단할 것  ·  우려되는 행위와 이를 뒷받침할 사정',cx[i],492,cw,35,12.5,C.navy,true);
 txt('risk_goal_'+i,i===0?'피해 예방과 회복을 위한 지원 필요':'우범소년 요건에 해당하는지에 관한 판단',cx[i],530,cw,30,12.5,C.gray);
}
conclusion('피해를 입을 위험이 크다는 설명만으로, 청소년의 장래 범법 우려까지 인정할 수는 없다.');finish(4);

baseSlide(5,'반복 피해와 지원 연결의 어려움','경찰서장의 송치와 보호자·기관장의 통고는 소년부로 이어지지만, 주체와 법적 성격이 다르다');
section('police',76.8,259,485,'경찰서장  ·  직접 송치');
txt('police_detail','촉법소년·우범소년에 해당하면\n직접 관할 소년부에 송치하여야 한다.',76.8,311,485,60,14,C.ink);
txt('police_law','소년법 제4조 제2항',76.8,382,485,25,10.5,C.muted);
section('notifier',76.8,435,485,'보호자·학교·사회복리시설·보호관찰소의 장');
txt('notifier_detail','제4조 제1항의 소년을 발견하면\n관할 소년부에 통고할 수 있다.',76.8,487,485,60,14,C.ink);
txt('notifier_law','소년법 제4조 제3항',76.8,554,485,23,10.5,C.muted);
rect('merge_vertical',613,341,1.4,180,C.neutral);rect('merge_upper',587,341,27,1.4,C.neutral);rect('merge_lower',587,520,27,1.4,C.neutral);txt('merge_arrow','→',618,416,34,37,18,C.gold,true,'center');
section('court',678,324,525,'소년부 판사의 판단');
txt('court_process','사실·환경 조사 → 심리·처분 필요성 판단',678,383,525,33,14,C.ink,true);
txt('court_detail','심리불개시·불처분 결정도 가능하다.\n보호처분이 필요하면 종류와 내용을 정한다.',678,435,525,61,12.5,C.gray);
txt('court_law','소년법 제3조·제19조·제29조·제32조',678,522,525,26,10.5,C.muted);
conclusion('송치·통고는 사건을 소년부로 보내는 절차이며, 시설 위탁 등 특정 보호처분이 곧바로 정해지는 것은 아니다.');finish(5);

baseSlide(6,'가정폭력·장기가출 뒤 시설 위탁 사례','2025년 경찰관 10명·피해지원 종사자 10명 면접에는 반복 피해와 지원 지속의 어려움이 함께 나타난다.',true);
const h6=['반복해서 나타나는 피해','늦어지는 지원 연결','지속하기 어려운 지원'];
const k6=['“어제 왔던 애가 오늘 또 오고”','통보가 늦으면 개입 시점도 늦어진다','상담·교육을 이어 가기 어렵다'];
const b6=['경찰 면접에는 반복 피해를 막으려\n가출 등 다른 사유로 개입하는\n상황과 고민이 제시된다.','수사 뒤 피해 사실을 늦게 통보받아\n지원이 지연되거나 관계 형성이\n어려워지는 사정이 제시된다.','청소년이나 보호자가 지원을\n받아들이지 않거나 협조하지 않아\n지속적 관계 형성에 어려움을 겪는다.'];
for(let i=0;i<3;i++){section('barrier_'+i,X[i],267,W,h6[i]);txt('barrier_key_'+i,k6[i],X[i],336,W,61,14,C.ink,true);txt('barrier_body_'+i,b6[i],X[i],417,W,95,12.5,C.gray);}
rect('context_rule',76.8,537,1126.1,1,C.line);txt('context','이 자료는 현장의 경험을 보여 준다. 전국 발생률이나 송치의 피해 예방 효과를 측정한 결과는 아니다.',76.8,554,1126.1,30,12.5,C.gray);
question('반복 피해를 막으려면, 즉시 위험에서 분리하는 조치와 지속적인 생활 지원을 어떻게 연결해야 하는가?');finish(6);

// Retained native case layouts, based on the reviewed two-slide v3.
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
txt('next','다음 → 기관 협의로 달라진 송치 계획',650,40.3,552.6,27,10.5,C.muted,false,'right');
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
addManualCase();s=p.slides.items[6];finish(7);
addBCase();s=p.slides.items[7];finish(8);

baseSlide(9,'보호를 위한 개입과 소년사법의 부담','지원기관의 사례 보고에는 치료를 이유로 계획된 우범소년 송치가 경찰과의 협의 뒤 중단된 경위가 나온다.',true);
const h9=['① 송치 계획','② 지원기관과 협의','③ 달라진 대응'];
const b9=['지적장애가 있는\n성착취 피해청소년에 대해\n경찰이 치료를 이유로\n우범소년 송치를 계획했다.','지원기관은 피해자로서의 지위와\n개정법의 취지를 설명했다.\n경찰과 여러 차례\n향후 보호 방안을 협의했다.','우범소년 송치 계획이\n중단되었다고 보고됐다.\n지원기관은\n가해자 수사를 요청했다.'];
for(let i=0;i<3;i++){section('response_'+i,X[i],274,W,h9[i]);txt('response_body_'+i,b9[i],X[i],349,W,138,14,C.ink);}
txt('response_arrow_1','→',437.2,398,23,32,16,C.gold,true,'center');txt('response_arrow_2','→',822.16,398,23,32,16,C.gold,true,'center');
rect('response_limit_rule',76.8,524,1126.1,1,C.line);txt('response_limit','평화의샘의 2021년 활동 보고  ·  이후 치료·안전 확보의 성과까지 제시된 자료는 아니다.',76.8,546,1126.1,32,12.5,C.gray);
question('송치 대신 피해지원 경로로 연결할 때, 필요한 치료와 안전을 누가 어떻게 책임질 것인가?');finish(9);

baseSlide(10,'현행법 적용과 정책·제도 판단','2021년 토론회에서는 반복 피해를 막을 개입 수단과, 피해청소년에게 지워지는 부담이 함께 논의됐다.',true);
section('claim1',cx[0],257,cw,'지속적인 보호 수단이 필요하다는 주장');
section('claim2',cx[1],257,cw,'청소년에게 문제를 떠넘길 수 있다는 비판');
txt('speaker1','고평기 · 당시 경찰청 아동청소년과장',cx[0],309,cw,28,10.5,C.muted);
txt('speaker2','이승현 · 당시 한국형사정책연구원 선임연구위원',cx[1],309,cw,28,10.5,C.muted);
txt('claim1_key','반복 피해를 막기 위해 송치한 사례를 제시했다.',cx[0],356,cw,53,14,C.ink,true);
txt('claim2_key','가정·지원체계의 문제를 소년사법으로 넘길 수 있다.',cx[1],356,cw,53,14,C.ink,true);
txt('claim1_body','위험한 환경에서 분리하고\n보호를 이어 갈 수단이 필요하다는 논거다.',cx[0],418,cw,64,12.5,C.gray);
txt('claim2_body','가정의 학대·방임을 해결하지 못한 채\n청소년의 자유 제한과 낙인이 생길 수 있다는 논거다.',cx[1],418,cw,64,12.5,C.gray);
for(let i=0;i<2;i++)rect('claim_question_rule_'+i,cx[i],510,cw,1,C.line);
txt('claim1_check','확인할 것  ·  송치가 실제 피해를 줄이는가?',cx[0],532,cw,33,12.5,C.navy,true);
txt('claim2_check','확인할 것  ·  지원으로 같은 보호 기능을 제공할 수 있는가?',cx[1],532,cw,33,12.5,C.navy,true);
question('송치로 얻는 보호의 이익, 청소년이 부담하는 제약, 다른 지원 경로의 가능성을 무엇으로 비교할 것인가?');finish(10);

baseSlide(11,'제2장 · 성매매 피해청소년의 법적 지위 변화','현행법 적용은 요건 충족을, 정책 판단은 이 경로를 유지·축소·대체·보완할 이유를 묻는다.',true);
txt('law_label','현행법 적용',76.8,242,1126.1,31,13,C.navy,true);
const h11=['사실관계 확인','우범소년 요건 판단','요건이 성립하면 직접 송치'];
const b11=['가출 경위와 환경, 우려되는 행위','법정 우범사유 + 장래 범법 우려','경찰서장의 송치 의무 · 제4조 제2항'];
for(let i=0;i<3;i++){rect('law_step_rule_'+i,X[i],285,W,2,C.blue);txt('law_step_'+i,h11[i],X[i],304,W,32,14,C.ink,true);txt('law_detail_'+i,b11[i],X[i],346,W,31,12.5,C.gray);}
txt('law_arrow1','→',437.2,308,23,32,16,C.gold,true,'center');txt('law_arrow2','→',822.16,308,23,32,16,C.gold,true,'center');
rect('policy_separator',76.8,404,1126.1,1,C.line);txt('policy_label','정책·제도 판단',76.8,426,220,31,13,C.navy,true);
txt('policy_text','이 경로를 유지·축소·대체·보완할 것인가?\n필요한 보호는 누가 제공하고, 자유 제한의 부담은 어떻게 줄일 것인가?',314,426,889,66,14,C.ink,true);
rect('recent_rule',76.8,516,1126.1,1,C.line);txt('recent_label','2026.9.17. 간담회',76.8,540,224,32,12.5,C.gray,true);
txt('recent_detail','지원기관은 피해청소년 송치 문제를 제기했고, 경찰 측은 현장 실태와 대안 검토를 언급했다.',314,540,889,35,12.5,C.gray);
question('우범소년 송치의 법정요건이 충족되는가, 그리고 그 경로를 유지할 이유는 무엇인가?');finish(11);

await (await PresentationFile.exportPptx(p)).save(base+'/candidate_raw.pptx');
console.log('Created',p.slides.items.length,'editable slides with complete speaker notes');
