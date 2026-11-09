#!/usr/bin/env python3
from pathlib import Path
import json, math, shutil, wave
from PIL import Image, ImageDraw
root=Path(__file__).resolve().parents[3];rem=root/'production/remotion';d=root/'production/denemeler/CTA-015';c=json.loads((rem/'sifirdan-tam-015.json').read_text());audio=d/'anlatim.wav'
# Approximate narration/CTA boundary, chosen from a pause in the single take.
boundary=29.9
with wave.open(str(audio)) as f:duration=f.getnframes()/f.getframerate()
c.update(dir='ctaOrnek015',captionEnd=boundary/1.55,ctaStart=round(boundary/1.55*30),frames=math.ceil((boundary/1.55+(duration-boundary)/1.62+.3)*30),ctaStack=[['KAYDET','save'],['PAYLAŞ','share'],['YORUM YAP','talk'],['TAKİP ET','follow']])
# Vosk word starts from the single original take; tempo mapping is approximate.
word_starts=[31.80,32.46,33.06,33.69]
c['ctaStackFrames']=[round((boundary/1.55+(t-boundary)/1.62)*30) for t in word_starts]
c['hideRepresentativeLabel']=True
c['warning']=''
c['events']=[event for event in c['events'] if event['a']!='OCAĞI']
dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for f in c['representativeFiles']:shutil.copy(root/'production/sifirdan-tam/VID-015'/f,dest/f)
# Remove production-facing labels baked into the diagram, retaining the diagram.
p=dest/'sahne-sema-tencere.png'
im=Image.open(p).convert('RGB'); draw=ImageDraw.Draw(im); bg=im.getpixel((5,5))
draw.rectangle((40,265,600,330),fill=bg); draw.rectangle((160,1025,520,1100),fill=bg); im.save(p)
(rem/'cta-ornek-015.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(rem/'cta-ornek-015.jsx').write_text((rem/'sifirdan-tam-015.jsx').read_text().replace('sifirdan-tam-015.json','cta-ornek-015.json'))
print('boundary input seconds',boundary,'cta frame',c['ctaStart'],'duration frames',c['frames'],'source duration',duration)
