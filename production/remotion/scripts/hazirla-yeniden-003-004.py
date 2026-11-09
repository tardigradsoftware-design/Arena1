#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import json,math,shutil,wave
root=Path(__file__).resolve().parents[3];rem=root/'production/remotion';prod=root/'production/sifirdan-yeni';font='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
info={'003':{'boundary':30.5,'words':[32.49,33.15,33.84,34.59], 'cover':['YANIK TENCERE','NASIL TEMİZLENİR?']},'004':{'boundary':24.55,'words':[26.64,27.33,28.02,28.80], 'cover':['SARARAN TABAN','NASIL BEYAZLAR?']}}
for id,v in info.items():
 d=prod/f'VID-{id}';c=json.loads((rem/f'sifirdan-tam-{id}.json').read_text());b=v['boundary']
 with wave.open(str(d/'anlatim.wav')) as f: dur=f.getnframes()/f.getframerate()
 c.update(dir='yeniden'+id,frames=math.ceil((b/1.55+(dur-b)/1.62+.3)*30),captionEnd=b/1.55,ctaStart=round(b/1.55*30),safeCaptions=True,hideRepresentativeLabel=True,ctaStack=[['KAYDET','save'],['PAYLAŞ','share'],['YORUM YAP','talk'],['TAKİP ET','follow']],ctaStackFrames=[round((b/1.55+(t-b)/1.62)*30) for t in v['words']],tempoBoundary=b,representativeFiles=[])
 # Plain, original graphics, without production-facing labels.
 im=Image.new('RGB',(768,1376),'#f0eee7');g=ImageDraw.Draw(im)
 if id=='003':
  g.ellipse((135,460,635,960),fill='#b7c4c0',outline='#3f514b',width=10);g.ellipse((185,510,585,910),fill='#e4e7e4',outline='#728681',width=6)
  for x,y in [(245,580),(395,555),(290,700),(440,725),(345,800)]:g.line((x,y,x+90,y+70,x+40,y+95),fill='#798987',width=5)
  g.rounded_rectangle((510,250,690,410),radius=35,fill='#fff',outline='#354c45',width=7);g.ellipse((560,290,640,370),fill='#54a8bc')
 else:
  g.rounded_rectangle((100,600,660,850),radius=80,fill='#e9e9df',outline='#424c46',width=8);g.line((130,760,640,760),fill='#ac9372',width=18)
  g.rounded_rectangle((190,440,570,480),radius=16,fill='#437b79');g.line((195,480,570,480),fill='#849693',width=18)
  for x in range(220,550,22):g.line((x,480,x,540),fill='#637d79',width=5)
 im.save(d/'sahne-4.png')
 if id=='003':
  foil=Image.new('RGB',(768,1376),'#f0eee7');fd=ImageDraw.Draw(foil);fd.ellipse((170,425,598,855),fill='#b5c0bd',outline='#41544e',width=8)
  for x,y in [(250,500),(330,485),(410,500),(240,590),(350,600),(440,590),(290,690),(410,700)]:fd.line((x,y,x+65,y+50,x+10,y+75),fill='#71817d',width=6)
  foil.save(d/'sahne-5.png')
 if id=='003':
  # Discard generated alternate pot with exterior stains: it mismatches the interior burn.
  c['shots']=[{'from':0,'file':'sahne-1.png'},{'from':45,'file':'sahne-4.png'},{'from':130,'file':'sahne-1.png'},{'from':220,'file':'sahne-4.png'},{'from':360,'file':'sahne-5.png'},{'from':520,'file':'sahne-3.png'}]
  c['highlight']={'file':'sahne-1.png','from':10,'to':43,'path':'M 180 520 C 230 450 310 430 390 440 C 480 450 560 500 580 575 C 600 660 550 750 475 775 C 375 810 255 790 205 730 C 165 680 155 570 180 520'}
 else:
  c['shots']=[{'from':0,'file':'sahne-1.png'},{'from':45,'file':'sahne-2.png'},{'from':110,'file':'sahne-1.png'},{'from':190,'file':'sahne-2.png'},{'from':290,'file':'sahne-4.png'},{'from':440,'file':'sahne-3.png'}]
  c['highlight']={'file':'sahne-1.png','from':10,'to':43,'path':'M 74 770 C 150 800 245 810 340 820 C 440 825 550 800 680 750 C 715 740 730 770 700 800 C 570 855 430 880 300 870 C 200 860 110 835 75 810 C 60 800 60 780 74 770'}
 dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
 for shot in c['shots']: shutil.copy(d/shot['file'],dest/shot['file'])
 (rem/f'yeniden-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
 (rem/f'yeniden-{id}.jsx').write_text((rem/f'sifirdan-tam-{id}.jsx').read_text().replace(f'sifirdan-tam-{id}.json',f'yeniden-{id}.json'))
 bg=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(bg);g.rounded_rectangle((55,160,1025,515),radius=30,fill='#121d1b',outline='white',width=6)
 for j,line in enumerate(v['cover']):
  sz=78 if j==0 else 62;g.text((540,260+j*125),line,font=ImageFont.truetype(font,sz),fill='#ffe135' if j==0 else 'white',anchor='mm')
 bg.save(d/f'VID-{id}-img-1.jpg',quality=92)
 print(id,c['frames'],c['ctaStackFrames'])
