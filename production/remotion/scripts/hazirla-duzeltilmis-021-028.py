#!/usr/bin/env python3
"""Generate edit timelines for the eight refreshed single-take episodes."""
from pathlib import Path
import json,math,shutil,wave
root=Path(__file__).resolve().parents[3]; r=root/'production/remotion';public=r/'public'
# Hand-estimated sentence pauses after 1.55x; verify against the narration before publication.
times={'021':(13.05,17.73),'022':(17.84,19.64),'023':(16.07,None),'024':(16.19,19.72),'025':(16.47,None),'026':(14.68,None),'027':(13.84,17.16),'028':(16.99,None)}
for id,(cta,final) in times.items():
 d=root/'production/yeni-senaryolar'/f'VID-{id}';c=json.loads((r/f'yeni-seri-{id}.json').read_text()); oldcta=c['ctaStart'];newcta=round(cta*30);factor=newcta/oldcta
 with wave.open(str(d/'duzeltilmis-anlatim.wav')) as w:c['frames']=math.ceil((w.getnframes()/w.getframerate()/1.55+.2)*30)
 orig=c['shots'];shots=[{'from':0,'file':orig[0]['file']},{'from':45,'file':orig[1]['file']},{'from':90,'file':orig[0]['file']}]
 for shot in orig[1:-1]:shots.append({'from':max(96,round(shot['from']*factor)),'file':shot['file']})
 shots.append({'from':newcta,'file':orig[-1]['file']});c['shots']=shots
 for e in c['events']:
  e['from']=round(e['from']*factor);e['to']=min(newcta,round(e['to']*factor))
 c['ctaStart']=newcta;c['captionEnd']=cta;c['ctaItems']=[['BEĞEN','like'],['ABONE OL','subscribe']]
 if final:
  c['cta2Start']=round(final*30);c['ctaHeading']='SEN NE DÜŞÜNÜYORSUN?';c['ctaFinalHeading']='BÖYLE İÇERİKLERİN DEVAMI İÇİN';c['ctaFirstItems']=[['YORUM YAP','talk'],['BEĞEN','like']]
 else:
  for key in ('cta2Start','ctaFinalHeading','ctaFirstItems'):c.pop(key,None)
  c['ctaHeading']='BÖYLE İÇERİKLERİN DEVAMI İÇİN'
 (r/f'duzeltilmis-seri-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
 (r/f'duzeltilmis-seri-{id}.jsx').write_text((r/f'yeni-seri-{id}.jsx').read_text().replace(f'yeni-seri-{id}.json',f'duzeltilmis-seri-{id}.json'))
 dest=public/c['dir'];dest.mkdir(exist_ok=True)
 for s in c['shots']:shutil.copy(d/s['file'],dest/s['file'])
 print(id, 'frames',c['frames'],'CTA',newcta,'shots',[(s['from'],s['file']) for s in shots])
