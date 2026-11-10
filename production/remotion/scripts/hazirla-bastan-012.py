from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageOps
import json,math,shutil,wave
root=Path(__file__).resolve().parents[3];rem=root/'production/remotion';d=root/'production/sifirdan-yeni/VID-012';c=json.loads((rem/'yeniden-012.json').read_text())
# Approximate timings from previous narration take, not forced alignment.
b=30.83
with wave.open(str(d/'rev2-anlatim.wav')) as w:dur=w.getnframes()/w.getframerate()
cta=round(b/1.55*30);ratio=cta/c['ctaStart']
for e in c['events']:e['from']=round(e['from']*ratio);e['to']=min(cta,round(e['to']*ratio))
c.update(dir='bastan012',frames=math.ceil((b/1.55+(dur-b)/1.62+.3)*30),captionEnd=b/1.55,ctaStart=cta,tempoBoundary=b,ctaStackFrames=[round((b/1.55+(x-b)/1.62)*30) for x in [33.10,33.88,34.69,35.65]],shots=[{'from':round(a*ratio),'file':f'rev2-{n}.png'} for a,n in [(0,5),(45,2),(100,5),(190,2),(280,3),(470,4),(550,5)]],highlight={'file':'rev2-2.png','from':round(195*ratio),'to':round(245*ratio),'path':'M 205 735 C 208 657 256 592 331 579 C 409 564 483 602 518 668 C 552 736 537 820 484 866 C 438 905 365 912 304 887 C 239 860 204 807 205 735'})
dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for s in c['shots']:shutil.copyfile(d/s['file'],dest/s['file'])
(rem/'bastan-012.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(rem/'bastan-012.jsx').write_text((rem/'yeniden-012.jsx').read_text().replace('yeniden-012.json','bastan-012.json'))
im=ImageOps.fit(Image.open(d/'rev2-5.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((55,160,1025,500),radius=30,fill='#121d1b',outline='white',width=6)
for j,line in enumerate(['KÖRELEN BIÇAK','NASIL KESKİNLEŞİR?']):g.text((540,250+j*125),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',64),fill='#ffe135' if j==0 else 'white',anchor='mm')
im.save(d/'VID-012-bastan-img-1.jpg',quality=92);print(c['frames'],c['ctaStackFrames'])
