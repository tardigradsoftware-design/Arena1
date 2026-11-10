from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageOps
import json,math,shutil,wave
root=Path(__file__).resolve().parents[3];rem=root/'production/remotion';d=root/'production/sifirdan-yeni/VID-009';c=json.loads((rem/'yeniden-009.json').read_text())
# Approximation based on the previous take; final spoken alignment needs listening.
b=31.17
with wave.open(str(d/'rev2-anlatim.wav')) as w:dur=w.getnframes()/w.getframerate()
cta=round(b/1.55*30);ratio=cta/c['ctaStart']
for e in c['events']:e['from']=round(e['from']*ratio);e['to']=min(cta,round(e['to']*ratio))
c.update(dir='bastan009',frames=math.ceil((b/1.55+(dur-b)/1.62+.3)*30),captionEnd=b/1.55,ctaStart=cta,tempoBoundary=b,ctaStackFrames=[round((b/1.55+(x-b)/1.62)*30) for x in [33.17,33.83,34.49,35.30]],shots=[{'from':round(a*ratio),'file':n} for a,n in [(0,'rev2-1.png'),(45,'rev2-5.png'),(115,'rev2-1.png'),(210,'rev2-7.png'),(315,'rev2-6.png'),(550,'rev2-5.png')]])
c.pop('highlight',None)
dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for s in c['shots']:shutil.copyfile(d/s['file'],dest/s['file'])
(rem/'bastan-009.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(rem/'bastan-009.jsx').write_text((rem/'yeniden-009.jsx').read_text().replace('yeniden-009.json','bastan-009.json'))
im=ImageOps.fit(Image.open(d/'rev2-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((55,160,1025,500),radius=30,fill='#121d1b',outline='white',width=6)
for j,line in enumerate(['PENCERE PİMİ','NASIL AYARLANIR?']):g.text((540,250+j*125),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',68),fill='#ffe135' if j==0 else 'white',anchor='mm')
im.save(d/'VID-009-bastan-img-1.jpg',quality=92);print(c['frames'],c['ctaStackFrames'])
