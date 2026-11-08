#!/usr/bin/env python3
from pathlib import Path
import json,math,wave,shutil
root=Path(__file__).resolve().parents[3];p=root/'production';r=p/'remotion'
for id in ('001','002'):
 c=json.loads((r/f'sifirdan-{id}.json').read_text());d=p/f'sifirdan-tam/VID-{id}'
 with wave.open(str(d/'anlatim.wav')) as f: c['frames']=math.ceil((f.getnframes()/f.getframerate()/1.55+.2)*30)
 c['ctaHeading']='BU FİKRİ PAYLAŞ' if id=='001' else 'SONUCUNU PAYLAŞ'
 c['ctaItems']=[['KAYDET','save'],['PAYLAŞ','share']] if id=='001' else [['KAYDET','save'],['YORUM YAP','talk']]
 c['ctaStart']=618 if id=='001' else 578;c['captionEnd']=c['ctaStart']/30
 (r/f'sifirdan-tam-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(r/f'sifirdan-tam-{id}.jsx').write_text((r/f'sifirdan-{id}.jsx').read_text().replace(f'sifirdan-{id}.json',f'sifirdan-tam-{id}.json'))
 # Reuse only the freshly produced assets from this new run, not the older series.
 dest=r/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
 for f in {s['file'] for s in c['shots']}:shutil.copy(p/f'sifirdan/VID-{id}'/f,dest/f)
 print(id,c['frames'])
