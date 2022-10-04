import lxml.etree as ET

from acdh_tei_pyutils.tei import TeiReader

LISTPERSON = './listperson_fackel.xml'
transform = ET.XSLT(ET.parse('./xslt/tolistperson.xsl'))

doc = TeiReader(LISTPERSON)
result = transform(doc.tree)
with open(LISTPERSON, 'w') as f:
    f.write(str(result))
