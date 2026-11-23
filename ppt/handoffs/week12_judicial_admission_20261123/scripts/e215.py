_pre=open('e121.py').read().split('# ================= 35')[0].replace("Presentation('v120.pptx')","Presentation('v214.pptx')")
exec(_pre)
from pptx.util import Inches,Pt
from pptx.dml.color import RGBColor
def pos(s,x,y,w,h): s.left=Inches(x); s.top=Inches(y); s.width=Inches(w); s.height=Inches(h)
def T(n,start):
    sl=p.slides[n-1]; assert one(sl,'title').text_frame.text.startswith(start); return sl
def find(sl,name,sub): return [s for s in sl.shapes if s.name==name and s.has_text_frame and sub in s.text_frame.text][0]
def paras(sh,items):
    ps=sh.text_frame.paragraphs; assert len(ps)==len(items)
    for q,t in zip(ps,items):
        for r in q.runs[1:]: r._r.getparent().remove(r._r)
        q.runs[0].text=t
# 21
sl=T(21,'임세원')
settext(one(sl,'message'),'이 사건으로 퇴원한 뒤 외래치료 기간에도 환자를 관리해야 한다는 지적이 제기됐고, 그 결과 퇴원 통보와 외래치료지원을 고치는 법 개정이 이루어졌다.')
script(21)
# 23 금색 통일: ② 줄은 문장 전체를 금색
sl=T(23,'세 사건의 공통점')
for sh in sl.shapes:
    if sh.name=='step-text':
        for q in sh.text_frame.paragraphs:
            if q.text.startswith('②'):
                for r in q.runs: r.font.color.rgb=RGBColor.from_string('A8871C')
# 31
sl=T(31,'2024년 정부')
for s in list(sl.shapes):
    if s.name in('step-panel','step-bar','step-text') and s.left/I>9.5: rm(s)
    elif s.name=='flow-arrow' and s.left/I>9.4: rm(s)
X=[0.80,4.81,8.82]; W=3.71
for s in sl.shapes:
    if s.name in('step-panel','step-bar','step-text'):
        x=s.left/I; i=0 if x<3 else 1 if x<6 else 2
        if s.name=='step-text': s.left=Inches(X[i]+0.18); s.width=Inches(W-0.36)
        else: s.left=Inches(X[i]); s.width=Inches(W)
    elif s.name=='flow-arrow':
        i=0 if s.left/I<5 else 1; s.left=Inches(X[i]+W+0.04)
paras(find(sl,'step-text','위원회가 서류로'),['위원회가 서류로 심사','입원적합성심사위원회가 1개월 안에 결과를 통지한다. 법원의 심사는 없고, 병원장·지자체장이 최초 3개월까지 입원시킨다.'])
paras(find(sl,'step-text','①'),['①','입원 신청권자 확대','정신건강복지센터장·의사 등도 신청할 수 있게 넓힌다.'])
paras(find(sl,'step-text','②'),['②','초기 입원 기간 연장: 최대 4주','전문의 1명의 진단으로 2주, 다른 전문의 1명의 진단으로 2주 더 입원한다.'])
paras(find(sl,'step-text','③'),['③','법원의 재판으로 계속 입원 결정','입원적합성심사위원회가 조사한 뒤 법원에 재판을 청구한다. 대면 재판이 원칙이고, 절차조력인이 환자의 입장을 대변한다.'])
script(31)
# 32 외래치료명령 행 삭제, 행 확대
sl=T(32,'국내 안에서')
for s in list(sl.shapes):
    if s.name in('rowhead-bg','rowhead','cell-bg','cell') and abs(s.top/I-5.38)<0.02: rm(s)
NEW={3.01:3.04,3.80:4.06,4.59:5.08}
for s in sl.shapes:
    if s.name in('rowhead-bg','rowhead','cell-bg','cell'):
        for o,n in NEW.items():
            if abs(s.top/I-o)<0.02: s.top=Inches(n); s.height=Inches(0.94); break
        if s.name in('rowhead','cell'):
            for q in s.text_frame.paragraphs:
                for r in q.runs:
                    if r.font.size: r.font.size=Pt(r.font.size.pt+1.5)
settext(one(sl,'message'),'지금 두 위원회가 맡는 심사 가운데 무엇을 법원으로 옮기는지가 안마다 다르다. 금색 칸이 법원이 맡는 심사다.')
paras(find(sl,'cell','병원장·지자체장이 결정'),['병원장·지자체장','응급입원: 경찰·의사'])
script(32)
# 33 색 맞바꿈
sl=T(33,'법원 심사에 대한')
for s in sl.shapes:
    left=s.left/I<6
    if s.name=='step-panel': fill(s,'F2F4F8' if left else 'FBF3DC')
    elif s.name=='step-bar': fill(s,'1E2761' if left else 'C2A648')
    elif s.name=='c-title':
        s.text_frame.paragraphs[0].runs[0].font.color.rgb=RGBColor.from_string('1E2761' if left else 'A8871C')
    elif s.name=='step-text' and left:
        r=s.text_frame.paragraphs[0].runs[0]; r.font.color.rgb=RGBColor.from_string('5A6699')
p.save('v215.pptx')
