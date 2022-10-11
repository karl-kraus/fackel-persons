import pandas as pd
import lxml.etree as ET
import shutil
import os
from tqdm import tqdm
from acdh_tei_pyutils.tei import TeiReader

from config import FINAL, MIT_GND, KONKORDANZ

print(f"read openrefine output {MIT_GND} into DataFrame" )
df = pd.read_excel(MIT_GND)
df = df[df['GND-Kennung'].notna()]
df = df[df['personId'].notna()]
df["personId"] = pd.to_numeric(df["personId"], downcast='integer')

print(f"read mapping of person IDs and Fackel-IDs from {KONKORDANZ} into DataFrame")
konkordanz_df = pd.read_csv(KONKORDANZ)

print(f"merge {KONKORDANZ} into {MIT_GND}")
merged = df.merge(konkordanz_df, 'left', left_on='personId', right_on='id')

merged.to_csv('merged.csv', index=False)

print(f"write GND and WikiData Ids into {FINAL}")
doc = TeiReader(FINAL)
persons = doc.any_xpath('.//tei:person')

for x in tqdm(persons, total=len(persons)):
    f_id = x.attrib["{http://www.w3.org/XML/1998/namespace}id"][4:]
    row = merged.loc[merged[' "fackel_id"'] == f_id ]
    try:
        gnd = row["GND-Kennung"].values[0]
    except IndexError:
        gnd = None
    try:
        wikidata = row["NEW URL"].values[0]
    except IndexError:
        wikidata = None
    if gnd is not None:
        idno_pmb = ET.Element('{http://www.tei-c.org/ns/1.0}idno')
        idno_pmb.attrib['type'] = 'url'
        idno_pmb.attrib['subtype'] = 'gnd'
        idno_pmb.text = f"https://d-nb.info/gnd/{gnd}"
        x.append(idno_pmb)
    if wikidata is not None:
        idno_pmb = ET.Element('{http://www.tei-c.org/ns/1.0}idno')
        idno_pmb.attrib['type'] = 'url'
        idno_pmb.attrib['subtype'] = 'wikidata'
        idno_pmb.text = wikidata
        x.append(idno_pmb)
doc.tree_to_file(FINAL)