import pandas as pd
import lxml.etree as ET
import shutil
import os
from tqdm import tqdm
from acdh_tei_pyutils.tei import TeiReader

from config import LISTPERSON, DEDUPE_DATA, FINAL

doc = TeiReader(LISTPERSON)
nsmap = doc.nsmap
df = pd.read_csv(DEDUPE_DATA)
df = df[df['id'].notna()]
df = df[df['id.1'].notna()]

data = {}
for i, row in df.iterrows():
    data[row['id']] = f"https://pmb.acdh.oeaw.ac.at/entity/{row['id.1'].replace('person__', '')}/"
persons = doc.any_xpath('.//tei:person[@xml:id]')
for x in tqdm(persons, total=len(persons)):
    xml_id = x.attrib['{http://www.w3.org/XML/1998/namespace}id']
    match = data.get(xml_id, None)
    fk_url = f"https://fackel.oeaw.ac.at/?p=fackelp{xml_id.split('_')[-1]}"
    idno_fk = ET.Element('{http://www.tei-c.org/ns/1.0}idno')
    idno_fk.attrib['type'] = 'url'
    idno_fk.attrib['subtype'] = 'fackel'
    idno_fk.text = fk_url
    x.append(idno_fk)
    if match:
        idno_pmb = ET.Element('{http://www.tei-c.org/ns/1.0}idno')
        idno_pmb.attrib['type'] = 'url'
        idno_pmb.attrib['subtype'] = 'pmb'
        idno_pmb.text = match
        x.append(idno_pmb)

shutil.rmtree('./data', ignore_errors=True)
os.makedirs('./data/')
doc.tree_to_file(FINAL)