from zipfile import ZipFile, ZIP_DEFLATED
from lxml import etree
from pathlib import Path
base=Path(__file__).parent
ns={'a':'http://schemas.openxmlformats.org/drawingml/2006/main','p':'http://schemas.openxmlformats.org/presentationml/2006/main'}
with ZipFile(base/'candidate_raw.pptx') as zin, ZipFile(base/'candidate.pptx','w',ZIP_DEFLATED) as zout:
    for item in zin.infolist():
        data=zin.read(item.filename)
        if item.filename.startswith(('ppt/slides/slide','ppt/notesSlides/notesSlide')) and item.filename.endswith('.xml'):
            r=etree.fromstring(data)
            for style in r.xpath('.//a:rPr | .//a:defRPr | .//a:endParaRPr',namespaces=ns):
                for tag in ['latin','ea','cs']:
                    f=style.find('a:'+tag,ns)
                    if f is None: f=etree.SubElement(style,'{'+ns['a']+'}'+tag)
                    f.set('typeface','Pretendard')
            for sp in r.findall('.//p:sp',ns):
                name=sp.find('p:nvSpPr/p:cNvPr',ns)
                if name is not None and name.get('name')=='chapter':
                    for rp in sp.findall('.//a:rPr',ns): rp.set('spc','200')
                body=sp.find('p:txBody',ns)
                if body is None: continue
                paras=body.findall('a:p',ns)
                multiple=sum(bool(pa.findall('.//a:t',ns)) for pa in paras)>1
                for pa in paras:
                    pp=pa.find('a:pPr',ns)
                    if pp is None: pp=etree.Element('{'+ns['a']+'}pPr');pa.insert(0,pp)
                    ln=pp.find('a:lnSpc',ns)
                    if ln is None: ln=etree.Element('{'+ns['a']+'}lnSpc');pp.insert(0,ln)
                    for ch in list(ln): ln.remove(ch)
                    etree.SubElement(ln,'{'+ns['a']+'}spcPct',val='125000' if multiple else '118000')
            data=etree.tostring(r,xml_declaration=True,encoding='UTF-8',standalone=True)
        zout.writestr(item,data)
print('Normalized fonts and paragraph spacing')
