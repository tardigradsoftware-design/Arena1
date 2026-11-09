from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageOps
import json,math,shutil,wave
root=Path(__file__).resolve().parents[3];rem=root/'production/remotion';base=root/'production/sifirdan-yeni'
config={'005':{'b':32.13,'words':[34.17,34.86,35.58,36.42],'shots':[(0,1),(45,5),(130,1),(195,5),(300,3),(470,4)],'cover':['ŞARJ KABLOSU','NASIL KORUNUR?'],'path':'M 205 650 C 230 600 285 580 340 590 C 395 600 450 625 465 660 C 475 700 455 735 415 750 C 370 765 305 755 265 735 C 230 720 205 690 205 650'},'006':{'b':28.3,'words':[30.09,30.72,31.32,31.95],'shots':[(0,1),(45,2),(120,1),(195,2),(290,3),(465,4)],'cover':['FIRIN CAMI','NASIL TEMİZLENİR?'],'path':'M 285 505 C 330 480 400 480 465 495 C 520 510 555 550 560 605 C 560 670 540 740 510 790 C 475 840 420 850 360 840 C 305 830 270 800 260 750 C 250 670 260 560 285 505'}}
for id,v in config.items():
 d=base/f'VID-{id}';c=json.loads((rem/f'yeniden-{id}.json').read_text());b=v['b']
 with wave.open(str(d/'rev2-anlatim.wav')) as w:dur=w.getnframes()/w.getframerate()
 old=c['ctaStart'];cta=round(b/1.55*30);ratio=cta/old
 for e in c['events']:
  e['from']=round(e['from']*ratio);e['to']=min(cta,round(e['to']*ratio))
 c.update(dir='bastan'+id,frames=math.ceil((b/1.55+(dur-b)/1.62+.3)*30),captionEnd=b/1.55,ctaStart=cta,tempoBoundary=b,ctaStackFrames=[round((b/1.55+(x-b)/1.62)*30) for x in v['words']],shots=[{'from':round(a*ratio),'file':f'rev2-{n}.png'} for a,n in v['shots']],highlight={'file':'rev2-1.png','from':10,'to':42,'path':v['path']})
 dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
 for shot in c['shots']:shutil.copyfile(d/shot['file'],dest/shot['file'])
 (rem/f'bastan-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(rem/f'bastan-{id}.jsx').write_text((rem/f'yeniden-{id}.jsx').read_text().replace(f'yeniden-{id}.json',f'bastan-{id}.json'))
 im=ImageOps.fit(Image.open(d/'rev2-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((55,160,1025,500),radius=30,fill='#121d1b',outline='white',width=6)
 for j,line in enumerate(v['cover']):g.text((540,250+j*125),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',70 if len(line)<17 else 58),fill='#ffe135' if j==0 else 'white',anchor='mm')
 im.save(d/f'VID-{id}-bastan-img-1.jpg',quality=92);print(id,c['frames'],c['ctaStackFrames'],c['shots'])
