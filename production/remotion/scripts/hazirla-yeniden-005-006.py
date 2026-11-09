#!/usr/bin/env python3
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageOps
import json,math,shutil,wave
root=Path(__file__).resolve().parents[3];r=root/'production/remotion';p=root/'production/sifirdan-yeni';font='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
info={'005':{'boundary':35.05,'words':[37.29,37.98,38.70,39.51],'cover':['ŞARJ KABLOSU','NASIL KORUNUR?']},'006':{'boundary':30.25,'words':[32.37,33.12,33.81,34.59],'cover':['FIRIN CAMI','NASIL TEMİZLENİR?']}}
for id,v in info.items():
 d=p/f'VID-{id}';c=json.loads((r/f'sifirdan-tam-{id}.json').read_text());b=v['boundary']
 with wave.open(str(d/'anlatim.wav')) as f:duration=f.getnframes()/f.getframerate()
 c.update(dir='yeniden'+id,frames=math.ceil((b/1.55+(duration-b)/1.62+.3)*30),captionEnd=b/1.55,ctaStart=round(b/1.55*30),safeCaptions=True,hideRepresentativeLabel=True,representativeFiles=[],ctaStack=[['KAYDET','save'],['PAYLAŞ','share'],['YORUM YAP','talk'],['TAKİP ET','follow']],ctaStackFrames=[round((b/1.55+(x-b)/1.62)*30) for x in v['words']],tempoBoundary=b)
 im=Image.new('RGB',(768,1376),'#f1f0e9');g=ImageDraw.Draw(im)
 if id=='005':
  g.rounded_rectangle((180,560,340,700),radius=25,fill='#d6dedb',outline='#2d4942',width=6);g.rounded_rectangle((85,600,180,660),radius=10,fill='#a9bbb7',outline='#2d4942',width=5);g.line((340,630,760,630),fill='#c1cac5',width=48)
  for x in range(350,560,25):g.arc((x,588,x+48,672),20,270,fill='#445b54',width=6)
  c['highlight']={'file':'sahne-1.png','from':10,'to':43,'path':'M 365 650 C 385 620 440 615 482 625 C 520 630 553 650 551 680 C 550 720 511 742 470 746 C 430 751 382 738 367 715 C 355 698 354 671 365 650'}
 else:
  g.rounded_rectangle((105,410,665,985),radius=32,fill='#dce8e3',outline='#3d554d',width=10)
  for x,y in [(250,540),(460,660),(330,800),(520,835)]:g.ellipse((x,y,x+48,y+38),fill='#976947')
  g.rounded_rectangle((280,550,455,700),radius=28,fill='#f8f8f2',outline='#52645c',width=7);g.ellipse((330,585,405,660),fill='#79b9c3')
  c['highlight']={'file':'sahne-1.png','from':10,'to':43,'path':'M 245 540 C 285 495 355 480 415 495 C 490 510 545 555 550 620 C 552 690 500 740 430 747 C 345 755 265 720 245 670 C 230 640 230 575 245 540'}
 im.save(d/'sahne-4.png')
 c['shots']=[{'from':0,'file':'sahne-1.png'},{'from':45,'file':'sahne-2.png'},{'from':120,'file':'sahne-1.png'},{'from':190,'file':'sahne-2.png'},{'from':300,'file':'sahne-4.png'},{'from':480,'file':'sahne-4.png' if id=='005' else 'sahne-3.png'}]
 if id=='005': c['shots'].insert(4,{'from':250,'file':'sahne-3.png'})
 dest=r/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
 for f in {s['file'] for s in c['shots']}:shutil.copy(d/f,dest/f)
 (r/f'yeniden-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(r/f'yeniden-{id}.jsx').write_text((r/f'sifirdan-tam-{id}.jsx').read_text().replace(f'sifirdan-tam-{id}.json',f'yeniden-{id}.json'))
 bg=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(bg);g.rounded_rectangle((55,160,1025,515),radius=30,fill='#121d1b',outline='white',width=6)
 for j,line in enumerate(v['cover']):g.text((540,260+j*125),line,font=ImageFont.truetype(font,78 if j==0 else 62),fill='#ffe135' if j==0 else 'white',anchor='mm')
 bg.save(d/f'VID-{id}-img-1.jpg',quality=92);print(id,c['frames'],c['ctaStackFrames'])
