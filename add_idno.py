import pandas as pd
from acdh_tei_pyutils.tei import TeiReader
from config import LISTPERSON, DEDUPE_DATA

doc = TeiReader(LISTPERSON)

df = pd.read_csv(DEDUPE_DATA)
df = df[df['id'].notna()]
df = df[df['id.1'].notna()]

data = {}
for i, row in df.iterrows():
    data[row['id']] = f"https://pmb.acdh.oeaw.ac.at/entity/{row['id.1'].replace('person__', '')}/"

