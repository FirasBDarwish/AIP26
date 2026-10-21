#!/usr/bin/env python3
"""Independent privacy risk AUDIT for workshop data, not an anonymiser.

Uses original *synthetic* data as an audit reference. Must NOT be imported,
read as a strategy, or used to reverse engineer transformations by starter.py.
Reports possible leaks and descriptive risk indicators, never certifies anonymity.
"""
import csv
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'data' / 'hospital_discharge_raw.csv'
OUTPUT = ROOT / 'encounters_private.csv'
DIRECT = {'encounter_id','patient_id','patient_name','date_of_birth','phone','email','street_address'}
POSSIBLE_QI = ('age','age_band','gender','region','city','neighborhood','postal_code','diagnosis','occupation','household_children','housing_status','preferred_language')
SENSITIVE = ('diagnosis','housing_status','household_children','caregiver_relation','preferred_language')
PATTERNS = {
    'email address': r'\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b',
    'synthetic phone': r'\b202[- ]?555[- ]?\d{4}\b',
    'synthetic MRN': r'\bFAKE-\d{6}-\d{3}\b',
    'patient/encounter token': r'\b(?:P-\d{4}|ENC-\d{4})\b',
    'ISO date': r'\b(?:19|20)\d{2}-\d{2}-\d{2}\b',
    'day/month/year date': r'\b\d{2}/\d{2}/(?:19|20)\d{2}\b',
    'day month year date': r'\b\d{1,2} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (?:19|20)\d{2}\b',
    'street or flat': r'\b\d{1,3} (?:Copper|Cedar|Linden|Lantern|Maple|Willow|Quarry|Harbor) (?:Lane|Road|Court|Street|Crescent|Walk|Rise|Drive)\b',
    'very specific place': r'\b(?:lighthouse|water tower|pedestrian bridge|observatory|lantern parade|clock keeper|ferry captain|bridge inspector|opera singer|museum curator)\b',
    'household/housing description': r'\b(?:\d+ children|foster carer|single parent|shelter|supported flat|temporary shelter|caregiver|dependent parent)\b',
}

def load(path):
    with path.open(newline='',encoding='utf-8') as f:
        return list(csv.DictReader(f))

def main():
    path=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else OUTPUT
    if not path.exists():
        sys.exit(f'No output CSV at {path}. First run python starter.py')
    raw, transformed=load(RAW),load(path)
    if not transformed: sys.exit('Output dataset is empty')
    columns=set(transformed[0]); out=[str(v) for row in transformed for v in row.values() if v]
    alltext='\n'.join(out)
    raw_names={row['patient_name'] for row in raw}
    raw_contacts={row['phone'] for row in raw}|{row['email'] for row in raw}|{row['street_address'] for row in raw}
    raw_unique_jobs={row['occupation'] for row in raw if row['occupation'].startswith(('only ','town ','regional ','sole ','island ','orchid '))}
    name_hits=sorted(x for x in raw_names if re.search(r'(?<!\w)'+re.escape(x)+r'(?!\w)',alltext,re.I))
    contact_hits=sorted(x for x in raw_contacts if x in alltext)
    rare_hits=sorted(x for x in raw_unique_jobs if re.search(re.escape(x),alltext,re.I))
    print('\nPRIVACY RISK AUDIT (educational heuristic; NOT certification)')
    print('='*65)
    print(f'Rows: {len(transformed)} (input 250); columns: {len(columns)}')
    print(f'Label retained: {"follow_up_7d" in columns}; note retained: {"discharge_note" in columns}')
    print('Direct-ID columns present:',sorted(columns & DIRECT) or 'none')
    print('Raw patient names seen anywhere:',len(name_hits),'example(s):',name_hits[:2])
    print('Exact original contacts/addresses seen anywhere:',len(contact_hits))
    print('Original rare occupations seen anywhere:',len(rare_hits))
    print('\nPattern matches across output (includes structured columns):')
    for label,pattern in PATTERNS.items():
        print(f'  {label}: {len(re.findall(pattern,alltext,flags=re.I))}')
    qis=[c for c in POSSIBLE_QI if c in columns]
    print('\nRemaining plausible quasi-identifiers:',', '.join(qis) or 'none of preset fields')
    for sample in [('age_band','gender','region'),('age','gender','city'),('region','diagnosis','household_children'),('region','housing_status','preferred_language')]:
        keys=[x for x in sample if x in columns]
        if len(keys)<2: continue
        groups=Counter(tuple(row.get(k,'') for k in keys) for row in transformed)
        singleton_rows=sum(count for count in groups.values() if count==1)
        few_rows=sum(count for count in groups.values() if count<5)
        print(f'  QI {keys}: min group={min(groups.values())}; singleton records={singleton_rows}/{len(transformed)}; records in groups <5={few_rows}/{len(transformed)}')
    if 'discharge_note' in columns:
        notes=[row.get('discharge_note','') for row in transformed]
        notempty=sum(bool(x.strip()) for x in notes)
        print(f'\nNonempty narrative reports: {notempty}/{len(notes)}. Manually inspect redactions, indirect clues and clinical usefulness.')
    print('\nMANUAL REVIEW REQUIRED: rare combinations, cross-record linkage,')
    print('attributes inferable from context, outside knowledge, linkage attacks,')
    print('and whether required clinical information was lost. No universal score')
    print('or k value proves anonymisation; this audit is deliberately incomplete.')
    print('For meaningful k-anonymity, YOU must define threat model and QI set.')
    if columns & DIRECT or name_hits or contact_hits:
        print('\nSTATUS: OBVIOUS IDENTIFIER RISK DETECTED (not an exhaustive result).')
    else:
        print('\nSTATUS: No preset direct ID hit; RESIDUAL RISK STILL EXISTS.')

if __name__=='__main__': main()
