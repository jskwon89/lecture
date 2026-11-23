_pre=open('e121.py').read().split('# ================= 35')[0].replace("Presentation('v120.pptx')","Presentation('v215.pptx')")
exec(_pre)
from pptx.util import Inches,Pt
from pptx.dml.color import RGBColor
def paras(sh,items):
    ps=sh.text_frame.paragraphs; assert len(ps)==len(items),(len(ps),items)
    for q,t in zip(ps,items):
        for r in q.runs[1:]: r._r.getparent().remove(r._r)
        q.runs[0].text=t
src=p.slides[26]; assert one(src,'title').text_frame.text.startswith('범죄자 집계')
ns=p.slides.add_slide(src.slide_layout)
for sh in list(ns.shapes): sh._element.getparent().remove(sh._element)
for sh in src.shapes: ns.shapes._spTree.append(copy.deepcopy(sh._element))
N=len(p.slides)
ids=p.slides._sldIdLst; L=list(ids); mv=L[-1]; ids.remove(mv); L[40].addnext(mv)   # 41쪽 뒤 → 42쪽
sl=p.slides[41]
settext(one(sl,'chapter'),p.slides[40].shapes[0].text_frame.text if False else one(p.slides[40],'chapter').text_frame.text)
settext(one(sl,'title'),'유럽 40개국에서 판사는 비자의입원에 얼마나 관여하는가')
settext(one(sl,'message'),'유럽정신의학회의 40개국 조사(Wasserman 등 2020)에서 33개국은 판사가 비자의입원의 최종 결정에 관여했고, 32개국은 일정 기간 뒤 판사가 다시 심사했다.')
settext(one(sl,'next'),'다음 → 입원부터 법원 심사까지 걸리는 기간')
# 범례 3개
keys=[s for s in sl.shapes if s.name=='legend-key']; labs=[s for s in sl.shapes if s.name=='legend-label']
k3=copy.deepcopy(keys[1]._element); l3=copy.deepcopy(labs[1]._element); sl.shapes._spTree.append(k3); sl.shapes._spTree.append(l3)
keys=[s for s in sl.shapes if s.name=='legend-key']; labs=[s for s in sl.shapes if s.name=='legend-label']
COL=['C2A648','5A6699','B9C0D4']; LT=['판사가 관여한다','관여하지 않는다','지역마다 다르다(영국)']; LX=[4.30,6.60,8.90]
for k,l,c,t,x in zip(keys,labs,COL,LT,LX):
    fill(k,c); k.left=Inches(x); l.left=Inches(x+0.24); l.width=Inches(2.0); settext(l,t)
hl=[s for s in sl.shapes if s.name=='h-label']; hv=[s for s in sl.shapes if s.name=='h-value']
paras(hl[0],['최종 결정','입원을 결정할 때']); 
q=hl[1].text_frame.paragraphs
if len(q)==3: q[2]._p.getparent().remove(q[2]._p)
paras(hl[1],['일정 기간 뒤 심사','입원한 뒤 다시 심사할 때'])
paras(hv[0],['33개국','40개국 가운데 83%']); paras(hv[1],['32개국','40개국 가운데 80%'])
segs=[s for s in sl.shapes if s.name=='seg']
X0,WT=4.30,8.23
def bar(pair,vals):
    y=pair[0].top; h=pair[0].height
    e3=copy.deepcopy(pair[1]._element); sl.shapes._spTree.append(e3)
    third=[s for s in sl.shapes if s._element is e3][0]
    x=X0
    for s,v,c in zip([pair[0],pair[1],third],vals,COL):
        w=WT*v/40; s.left=Inches(x); s.width=Inches(w-0.03); s.top=y; s.height=h; fill(s,c); x+=w
        tf=s.text_frame; tf.text=str(v); r=tf.paragraphs[0].runs[0]; r.font.size=Pt(14); r.font.bold=True; r.font.name='Pretendard'
        r.font.color.rgb=RGBColor.from_string('1E2761' if c!='5A6699' else 'FFFFFF')
        tf.margin_left=tf.margin_right=0
        from pptx.enum.text import PP_ALIGN
        tf.paragraphs[0].alignment=PP_ALIGN.CENTER
bar(segs[0:2],[33,6,1]); bar(segs[2:4],[32,7,1])
settext(one(sl,'row-label'),'수치의 뜻')
paras(one(sl,'row-text'),['두 단계 모두 판사가 관여하는 나라가 29개국이고, 두 단계 모두 관여하지 않는 나라는 덴마크·아일랜드·몰타 3개국이다.',
 '‘최종 결정에 관여’에는 판사가 입원 전에 결정하는 나라와 입원한 뒤에 결정하는 나라가 함께 들어 있다. 핀란드·노르웨이·스웨덴은 의사가 결정하고 판사는 일정 기간 뒤 심사에만 관여한다.'])
# 노트
nt=sl.notes_slide.notes_text_frame
nt.text=('[출처와 확인 위치]\nWasserman D 등(2020), Compulsory admissions of patients with mental disorders: State of the art on ethical and legislative aspects in 40 European countries, European Psychiatry 63(1), e82, 표 4·5(5쪽). 유럽정신의학회 2018~2020년 조사, 40개국.\n'
 '표 4 질문: Is a judge involved in making the final decision about compulsory admission? 예 33, 아니오 6, 영국 내 상이 1.\n표 5: 일정 기간 뒤 심사할 때 판사 관여. 예 32, 아니오 7, 영국 내 상이 1.\n두 표 모두 예 29개국, 예·아니오 4개국(아르메니아·라트비아·폴란드·튀르키예), 아니오·예 3개국(핀란드·노르웨이·스웨덴), 모두 아니오 3개국(덴마크·아일랜드·몰타)은 두 표의 국가명을 대조해 센 값이다.\n'
 '주의: 설문은 최종 결정에 관여하는지를 물었고 입원과 결정의 선후는 묻지 않았다. 33개국을 입원 전에 판사의 허가를 받는 나라로 설명하지 않는다. 한국은 조사 대상이 아니다.\n\n[낭독 대본]\n'
 '유럽정신의학회가 2018년부터 2020년까지 유럽 40개국을 조사했습니다. 33개국은 판사가 비자의입원의 최종 결정에 관여했고, 32개국은 일정 기간 뒤 판사가 다시 심사했습니다.\n'
 '두 단계 모두 판사가 관여하는 나라가 29개국이고, 두 단계 모두 관여하지 않는 나라는 덴마크, 아일랜드, 몰타 3개국입니다.\n'
 '최종 결정에 관여한다는 응답에는 판사가 입원 전에 결정하는 나라와 입원한 뒤에 결정하는 나라가 함께 들어 있습니다. 핀란드, 노르웨이, 스웨덴은 의사가 결정하고 판사는 일정 기간 뒤 심사에만 관여합니다.')
# 앞뒤 연결과 쪽 번호
nxt(41,'유럽 40개국에서 판사는 비자의입원에 얼마나 관여하는가')
c=[s for s in p.slides[35].shapes if s.name=='toc-item' and '세 제도 비교' in s.text_frame.text][0]; settext(c,'세 유형, 유럽 40개국의 판사 관여, 심사까지 걸리는 기간')
tb=[s for s in p.slides[1].shapes if getattr(s,'has_table',False) and s.has_table][0].table
for r,pg in zip(list(tb.rows)[5:],['44쪽','48쪽','52쪽']):
    q=r.cells[2].text_frame.paragraphs[0]; q.runs[0].text=pg
for s in p.slides:
    for sh in s.shapes:
        if sh.name=='chip-text' and '쪽' in sh.text_frame.text:
            settext(sh,sh.text_frame.text.replace('53·56쪽','54·57쪽').replace('· 56쪽','· 57쪽'))
p.save('v216.pptx')
print([(i+1,one(s,'title').text_frame.text) for i,s in enumerate(p.slides) if i in (40,41,42,43,47,51)])
print([c.text for r in tb.rows for c in r.cells if '쪽' in c.text])
