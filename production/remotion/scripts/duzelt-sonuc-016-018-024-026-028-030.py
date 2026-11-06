#!/usr/bin/env python3
"""Revision preserves narration, original timeline and warning; replaces mismatched result shots."""
import json, shutil
from pathlib import Path
r=Path(__file__).resolve().parents[1]; p=r.parent; pub=r/'public'; pub.mkdir(exist_ok=True)
for id in ('016','018','024','026','028','030'):
 c=json.loads((r/f'yeni-liste-{id}.json').read_text()); c['dir']=f'yeniliste{id}duzelt'; c['representativeFiles']=[]
 if id=='016':
  c['shots']=[x for x in c['shots'] if x['from']<535]+[{'from':480,'file':'sahne-sonuc-duzeltilmis.png'}];c['representativeFiles']=['sahne-sonuc-duzeltilmis.png']
 if id=='018':
  for x in c['shots']:
   if x['from'] in (0,110):x['file']='sahne-once-duzeltilmis.png'
  c['representativeFiles']=['sahne-once-duzeltilmis.png','sahne-1.png']
 if id in ('024','026','028','030'):
  start={'024':520,'026':470,'028':500,'030':590}[id]
  c['shots']=[x for x in c['shots'] if x['from']<start]+[{'from':start,'file':'sahne-sonuc-duzeltilmis.png'}]
  if id=='028':
   next(x for x in c['shots'] if x['from']==45)['file']='sahne-2.png'
  c['representativeFiles']=['sahne-sonuc-duzeltilmis.png']
 dst=pub/c['dir'];dst.mkdir(exist_ok=True)
 for name in {s['file'] for s in c['shots']}:shutil.copy(p/'yeni-liste'/f'VID-{id}'/name,dst/name)
 (r/f'yeni-liste-{id}-sonuc-duzeltme.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
 (r/f'yeni-liste-{id}-sonuc-duzeltme.jsx').write_text((r/f'yeni-liste-{id}.jsx').read_text().replace(f'yeni-liste-{id}.json',f'yeni-liste-{id}-sonuc-duzeltme.json'))
