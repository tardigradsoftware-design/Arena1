#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import json,shutil
root=Path(__file__).resolve().parents[3]; r=root/'production/remotion'; p=root/'production/sifirdan-yeni'
shots={'013':[(0,'rev2-1.png'),(45,'sahne-1.png'),(125,'rev2-2.png'),(235,'rev2-1.png'),(315,'rev2-2.png'),(365,'rev2-3.png'),(575,'rev2-4.png')], '014':[(0,'rev2-1.png'),(45,'sahne-1.png'),(155,'sahne-2.png'),(245,'rev2-2.png'),(355,'rev2-3.png'),(520,'sahne-3.png'),(580,'rev2-4.png')]}
for id,entries in shots.items():
 d=p/f'VID-{id}'; c=json.loads((r/f'yeniden-{id}.json').read_text());c['dir']=f'rev2-{id}';c['shots']=[{'from':f,'file':name} for f,name in entries]
 if id=='013':c['highlight']={'file':'rev2-3.png','from':380,'to':440,'path':'M 229 550 C 250 520 310 509 382 510 C 456 510 520 524 540 555 C 554 584 548 642 532 665 C 508 694 447 705 380 704 C 312 705 251 691 230 662 C 213 641 211 582 229 550'}
 else:c['highlight'].update(file='sahne-1.png',**{'from':110,'to':150})
 dest=r/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
 for _,name in entries:shutil.copyfile(d/name,dest/name)
 (r/f'rev2-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
 (r/f'rev2-{id}.jsx').write_text((r/f'yeniden-{id}.jsx').read_text().replace(f'yeniden-{id}.json',f'rev2-{id}.json'))
 # Existing approved cover remains a separate deliverable; no generated diagram is used.
