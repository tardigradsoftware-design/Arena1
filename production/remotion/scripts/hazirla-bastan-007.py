from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageOps
import json,math,shutil,wave
root=Path(__file__).resolve().parents[3];rem=root/'production/remotion';d=root/'production/sifirdan-yeni/VID-007';c=json.loads((rem/'yeniden-007.json').read_text());b=33.98
with wave.open(str(d/'rev2-anlatim.wav')) as w:dur=w.getnframes()/w.getframerate()
cta=round(b/1.55*30);ratio=cta/c['ctaStart']
for e in c['events']:e['from']=round(e['from']*ratio);e['to']=min(cta,round(e['to']*ratio))
ImageOps.mirror(Image.open(d/'rev2-2.png')).save(d/'rev2-2-ayna.png')
c.update(dir='bastan007',frames=math.ceil((b/1.55+(dur-b)/1.62+.3)*30),captionEnd=b/1.55,ctaStart=cta,tempoBoundary=b,ctaStackFrames=[round((b/1.55+(x-b)/1.62)*30) for x in [35.94,36.63,37.29,38.07]],shots=[{'from':round(a*ratio),'file':n} for a,n in [(0,'rev2-1.png'),(45,'rev2-2-ayna.png'),(100,'rev2-1.png'),(220,'rev2-2-ayna.png'),(310,'rev2-3.png'),(585,'rev2-4.png')]],highlight={'file':'rev2-1.png','from':10,'to':42,'path':'M 105 560 C 125 540 160 535 188 550 C 212 560 222 580 213 605 C 205 632 175 645 145 640 C 115 635 95 620 95 600 C 94 585 98 570 105 560'})
dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for s in c['shots']:shutil.copyfile(d/s['file'],dest/s['file'])
(rem/'bastan-007.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(rem/'bastan-007.jsx').write_text((rem/'yeniden-007.jsx').read_text().replace('yeniden-007.json','bastan-007.json'))
im=ImageOps.fit(Image.open(d/'rev2-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((55,160,1025,500),radius=30,fill='#121d1b',outline='white',width=6)
for j,line in enumerate(['DEODORANT İZİ','NASIL ÇIKAR?']):g.text((540,250+j*125),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',70),fill='#ffe135' if j==0 else 'white',anchor='mm')
im.save(d/'VID-007-bastan-img-1.jpg',quality=92);print(c['frames'],c['ctaStackFrames'])
