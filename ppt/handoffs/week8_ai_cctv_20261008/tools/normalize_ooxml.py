"""Normalize exported typography; no slide/content authoring occurs here."""
from pathlib import Path
import os
from zipfile import ZipFile,ZIP_DEFLATED
from lxml import etree as E
import json
P=Path(os.environ['W8_BUILD_DIR'])
NS={'a':'http://schemas.openxmlformats.org/drawingml/2006/main','p':'http://schemas.openxmlformats.org/presentationml/2006/main'}
A='{'+NS['a']+'}'
with ZipFile(P/'candidate_raw.pptx') as z: parts={n:z.read(n) for n in z.namelist()}
for name,raw in list(parts.items()):
 if not name.endswith('.xml') or not name.startswith('ppt/'):continue
 root=E.fromstring(raw)
 for el in root.xpath('//*[@typeface]'):el.set('typeface','Pretendard')
 for body in root.xpath('//a:txBody|//p:txBody',namespaces=NS):
  paras=body.findall(A+'p');multi=len(paras)>1 or bool(body.findall('.//'+A+'br'))
  for pr in body.findall(A+'bodyPr'):
   pr.set('wrap','none')
   for x in ['lIns','rIns','tIns','bIns']:pr.set(x,'0')
   for tag in ['normAutofit','spAutoFit']:
    for e in pr.findall(A+tag):pr.remove(e)
   if pr.find(A+'noAutofit') is None:E.SubElement(pr,A+'noAutofit')
  for p in paras:
   pp=p.find(A+'pPr')
   if pp is None:pp=E.Element(A+'pPr');p.insert(0,pp)
   for tag in ['lnSpc','spcBef','spcAft']:
    for e in pp.findall(A+tag):pp.remove(e)
   ls=E.Element(A+'lnSpc');E.SubElement(ls,A+'spcPct',val='125000' if multi else '118000');pp.insert(0,ls)
   for tag in ['spcBef','spcAft']:
    b=E.SubElement(pp,A+tag);E.SubElement(b,A+'spcPts',val='0')
   for r in p.findall(A+'r'):
    rp=r.find(A+'rPr')
    if rp is None:rp=E.Element(A+'rPr');r.insert(0,rp)
    for tag in ['latin','ea','cs']:
     e=rp.find(A+tag)
     if e is None:e=E.SubElement(rp,A+tag)
     e.set('typeface','Pretendard')
 for tc in root.findall('.//'+A+'tc'):
  pr=tc.find(A+'tcPr')
  if pr is None:pr=E.SubElement(tc,A+'tcPr')
  for k,v in {'marL':146304,'marR':146304,'marT':91440,'marB':91440}.items():pr.set(k,str(v))
  pr.set('anchor','ctr')
  for tag in ['lnL','lnR','lnT','lnB']:
   for old in pr.findall(A+tag):pr.remove(old)
   ln=E.SubElement(pr,A+tag,w='7620');sf=E.SubElement(ln,A+'solidFill');E.SubElement(sf,A+'srgbClr',val='DCE0E8')
   E.SubElement(ln,A+'prstDash',val='solid')
 for shape in root.findall('.//p:sp',NS):
  nv=shape.find('p:nvSpPr/p:cNvPr',NS)
  if nv is not None and '_kicker_' in nv.get('name',''):
   for rp in shape.findall('.//'+A+'rPr'):rp.set('spc','200')
 parts[name]=E.tostring(root,xml_declaration=True,encoding='UTF-8',standalone=True)
with ZipFile(P/'candidate.pptx','w',ZIP_DEFLATED) as z:
 for n in ['[Content_Types].xml']+sorted(n for n in parts if n!='[Content_Types].xml'):z.writestr(n,parts[n])
print('Normalized typography and native table margins')
