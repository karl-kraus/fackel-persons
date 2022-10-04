import lxml.etree as ET

from acdh_tei_pyutils.tei import TeiReader

from config import LISTPERSON

transform = ET.XSLT(ET.parse('./xslt/tolistperson.xsl'))

doc = TeiReader(LISTPERSON)
result = transform(doc.tree)
with open(LISTPERSON, 'w') as f:
    content = str(result).replace(
        '<TEI>',
        '<TEI xmlns="http://www.tei-c.org/ns/1.0">'

    )
    f.write(content)
