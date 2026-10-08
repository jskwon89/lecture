import fs from 'node:fs/promises';
import path from 'node:path';
import {createRequire} from 'node:module';
import {pathToFileURL} from 'node:url';
const require=createRequire(import.meta.url);
const {Presentation,PresentationFile}=await import(pathToFileURL(require.resolve('@oai/artifact-tool',{paths:[process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES||process.cwd()]})).href);
const skill=process.env.PRESENTATION_SKILL_ROOT||'/root/.codex/skills/builtins/presentations';
const {applyPresentationChartFont}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')).href);
const dest=process.env.W8_BUNDLE_DIR||path.resolve(path.dirname(new URL(import.meta.url).pathname),'..');
const here=process.env.W8_BUILD_DIR;
if(!here) throw new Error('Set W8_BUILD_DIR to an empty temporary build directory');
await fs.mkdir(here,{recursive:true});
const data=JSON.parse(await fs.readFile(path.join(dest,'w8_content.json'),'utf8'));
const layouts=JSON.parse(await fs.readFile(path.join(here,'layout.json'),'utf8'));
const sources=Object.fromEntries(JSON.parse(await fs.readFile(path.join(dest,'research/source_registry.json'),'utf8')).map(s=>[s.id,s]));
const p=Presentation.create({slideSize:{width:1279.68,height:720}});
const px=n=>n*96;
for(const [i,s] of data.slides.entries()){
 const slide=p.slides.add();slide.background.fill='#FFFFFF';
 for(const [j,o] of layouts[i].items.entries()){
  const position={left:px(o.x),top:px(o.y),width:px(o.w),height:px(o.h)};
  if(o.type==='text'){
   const sh=slide.shapes.add({geometry:'textbox',name:`s${i+1}_${o.tag}_${j}`,position,fill:'none',line:{fill:'none',width:0}});
   sh.text=o.text;
   sh.text.style={typeface:'Pretendard',fontSize:o.pt*96/72,bold:o.bold,color:o.color,autoFit:'none',wrap:'none',alignment:o.align,verticalAlignment:'top',insets:{top:0,bottom:0,left:0,right:0}};
  } else if(o.type==='line'){
   slide.shapes.add({geometry:'line',position,line:{fill:o.color,width:.8},fill:'none'});
  } else if(o.type==='rect'){
   slide.shapes.add({geometry:'rect',position,fill:o.fill,line:{fill:'none',width:0}});
  } else if(o.type==='table'){
   const t=slide.tables.add({rows:o.values.length,columns:o.values[0].length,left:position.left,top:position.top,width:position.width,height:position.height,values:o.values,columnWidths:o.widths.map(px)});
   t.styleOptions={headerRow:false,firstColumn:false,bandedRows:false,bandedColumns:false};
   t.borders.assign({style:'solid',fill:'#DCE0E8',width:.8});
   for(let r=0;r<o.values.length;r++){
    t.rows[r].height=px(o.rowhs[r]);
    for(let c=0;c<o.values[0].length;c++){
     const cell=t.getCell(r,c);cell.fill=r===0?'#F2F4F8':'#FFFFFF';
     cell.text.style={typeface:'Pretendard',fontSize:(r===0||c===0?13:12.5)*96/72,bold:r===0||c===0,color:r===0||c===0?'#1E2761':'#222633',alignment:c===0?'center':'left',verticalAlignment:'middle',autoFit:'none',wrap:'none'};
    }
   }
  } else if(o.type==='chart'){
   const chart=slide.charts.add('bar',{position,categories:o.categories,series:[{name:'사진 검색 미탐지율',values:o.values,fill:'#5A6699',points:[{idx:1,fill:'#C2A648'}],valuesFormatCode:'0.0"%"'}],barOptions:{direction:'column',grouping:'clustered',gapWidth:150},hasLegend:false,xAxis:{textStyle:{fontSize:17.33,typeface:'Pretendard',fill:'#222633'},line:{fill:'#DCE0E8',width:1}},yAxis:{min:0,max:5,majorUnit:1,numberFormatCode:'0"%"',textStyle:{fontSize:16,typeface:'Pretendard',fill:'#464D5C'},majorGridlines:{fill:'#DCE0E8',width:.5},line:{fill:'none',width:0}},dataLabels:{showValue:true,position:'outEnd',textStyle:{typeface:'Pretendard',fontSize:20,bold:true,fill:'#1E2761'}},chartFill:'#FFFFFF',chartLine:{fill:'none',width:0},plotAreaFill:'#FFFFFF',plotAreaLine:{fill:'none',width:0}});
   applyPresentationChartFont(chart,{fontFamily:'Pretendard'});
  }
 }
 const refs=s.sources.map(id=>{const r=sources[id];return `${id} | ${r.by} | ${r.date}\n${r.title}\n${r.rechecked_url||r.url}\n확인 범위: ${r.scope||r.locator||''}`;}).join('\n\n');
 const details=s.sources.map(id=>{const r=sources[id];return `${id}: ${r.finding}\n적용 범위·한계: ${r.limit||''}`;}).join('\n\n');
 const notes=`[낭독 대본]\n${s.script.join('\n\n')}\n\n[출처]\n${refs}\n\n[강사용 상세자료]\n학습목표: ${s.goal}\n확장 질문: ${s.question}\n${details}\n\n[내부 제작 메모]\n${s.id} / ${s.placement} / ${s.role}\n${s.memo}\n이전 연결: ${s.previous_connection}\n다음 연결: ${s.next_connection}\n운영시간 초안: ${s.minutes}분. 실제 리허설 측정값이 아님.`;
 slide.speakerNotes.textFrame.setText(notes);
}
await (await PresentationFile.exportPptx(p)).save(path.join(here,'candidate_raw.pptx'));
console.log(`Exported ${data.slides.length} editable slides`);
