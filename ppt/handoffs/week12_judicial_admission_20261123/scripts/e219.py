_pre=open('e121.py').read().split('# ================= 35')[0].replace("Presentation('v120.pptx')","Presentation('v218.pptx')")
exec(_pre)
sl=p.slides[56]; assert one(sl,'title').text_frame.text.startswith('쟁점 ④')
R={'장애와 위험 예측에 근거한 입원은 법원이 승인해도 정당하지 않다.':'정신질환과 위험 예측에 근거한 입원은 법원이 승인해도 정당하지 않다.',
'· 이 입원은 이미 저지른 범죄가 아니라 앞으로 위험할 것이라는 예측을 근거로 하므로, 예측이 틀리면 가둘 필요가 없는 사람을 가두게 된다.':'· 이 입원은 범죄의 결과가 아니라, 정신질환이 있다는 사실과 앞으로 위험할 것이라는 예측을 근거로 한다. 예측이 틀리면 가둘 필요가 없는 사람을 가두게 된다.'}
tb=[x for x in sl.shapes if getattr(x,'has_table',False) and x.has_table][0].table
k=0
qs=[q for r in tb.rows for c in r.cells for q in c.text_frame.paragraphs]+list(sl.notes_slide.notes_text_frame.paragraphs)
for q in qs:
    if q.text in R:
        t=R[q.text]
        for x in q.runs[1:]: x._r.getparent().remove(x._r)
        q.runs[0].text=t; k+=1
print(k); p.save('v219.pptx')
