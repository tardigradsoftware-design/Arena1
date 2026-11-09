#!/usr/bin/env python3
from pathlib import Path
import json, math, shutil, wave
root=Path(__file__).resolve().parents[3];rem=root/'production/remotion';d=root/'production/denemeler/CTA-015';c=json.loads((rem/'sifirdan-tam-015.json').read_text());audio=d/'anlatim.wav'
# Approximate narration/CTA boundary, chosen from a pause in the single take.
boundary=29.9
with wave.open(str(audio)) as f:duration=f.getnframes()/f.getframerate()
c.update(dir='ctaOrnek015',captionEnd=boundary/1.55,ctaStart=round(boundary/1.55*30),frames=math.ceil((boundary/1.55+(duration-boundary)/1.62+.3)*30),ctaStack=[['KAYDET','save'],['PAYLAŞ','share'],['YORUM YAP','talk'],['TAKİP ET','follow']])
dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for f in c['representativeFiles']:shutil.copy(root/'production/sifirdan-tam/VID-015'/f,dest/f)
(rem/'cta-ornek-015.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(rem/'cta-ornek-015.jsx').write_text((rem/'sifirdan-tam-015.jsx').read_text().replace('sifirdan-tam-015.json','cta-ornek-015.json'))
print('boundary input seconds',boundary,'cta frame',c['ctaStart'],'duration frames',c['frames'],'source duration',duration)
