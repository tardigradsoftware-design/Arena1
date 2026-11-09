#!/usr/bin/env python3
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageOps
import json,math,shutil,wave
root=Path(__file__).resolve().parents[3];r=root/'production/remotion';p=root/'production/sifirdan-yeni';font='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
info={'013':{'boundary':32.55,'words':[34.41,35.07,35.73,36.48],'cover':['SIKIŞAN BARDAK','NASIL AYRILIR?']},'014':{'boundary':33.55,'words':[35.46,36.18,36.87,37.68],'cover':['SARI TER LEKESİ','NASIL ÇIKAR?']}}
for id,v in info.items():
 d=p/f'VID-{id}';c=json.loads((r/f'sifirdan-tam-{id}.json').read_text());b=v['boundary']
 with wave.open(str(d/'anlatim.wav')) as f:duration=f.getnframes()/f.getframerate()
 c.update(dir='yeniden'+id,frames=math.ceil((b/1.55+(duration-b)/1.62+.3)*30),captionEnd=b/1.55,ctaStart=round(b/1.55*30),safeCaptions=True,hideRepresentativeLabel=True,representativeFiles=[],warning='',ctaStack=[['KAYDET','save'],['PAYLAŞ','share'],['YORUM YAP','talk'],['TAKİP ET','follow']],ctaStackFrames=[round((b/1.55+(x-b)/1.62)*30) for x in v['words']],tempoBoundary=b)
 im=Image.new('RGB',(768,1376),'#f1f0e9');g=ImageDraw.Draw(im)
 if id=='013':
  # Side section: bowl water surrounds the LOWER glass; upper glass contains ice water.
  g.polygon([(95,750),(673,750),(625,1010),(145,1010)],fill='#d1e1de',outline='#3d574e');g.rectangle((120,800,648,975),fill='#e6b790');g.polygon([(235,530),(535,530),(495,960),(275,960)],fill='#e0efeb',outline='#3d574e');g.polygon([(275,380),(495,380),(475,830),(295,830)],fill='#d3edf3',outline='#3d574e');g.rectangle((295,450,475,650),fill='#a9dbe6')
  for x,y in [(320,475),(385,500),(345,555)]:g.rectangle((x,y,x+45,y+45),outline='#fff',width=5)
  c['shots']=[{'from':0,'file':'sahne-1.png'},{'from':45,'file':'sahne-2.png'},{'from':105,'file':'sahne-1.png'},{'from':250,'file':'sahne-2.png'},{'from':345,'file':'sahne-4.png'},{'from':575,'file':'sahne-3.png'}]
  c['highlight']={'file':'sahne-4.png','from':355,'to':400,'path':'M 245 530 C 270 510 320 510 370 510 C 425 510 480 510 510 530 C 530 550 520 580 500 590 C 450 610 300 610 260 590 C 240 580 235 550 245 530'}
 else:
  g.polygon([(165,470),(325,400),(450,400),(600,470),(555,950),(210,950)],fill='#fff',outline='#40564d');g.ellipse((250,600,370,710),fill='#d5bf79');g.rounded_rectangle((350,460,590,510),radius=18,fill='#6f9b99');g.rectangle((340,500,430,560),fill='#b5c9c1');
  for x in range(350,430,12):g.line((x,560,x,592),fill='#667b73',width=4)
  c['events']=[dict(e,b='MALZEMELER') if e['b']=='TEMSİLİ' else (dict(e,b='UYGULA') if e['b']=='ŞEMASI' else e) for e in c['events']]
  c['shots']=[{'from':0,'file':'sahne-1.png'},{'from':45,'file':'sahne-2.png'},{'from':105,'file':'sahne-1.png'},{'from':205,'file':'sahne-2.png'},{'from':350,'file':'sahne-4.png'},{'from':515,'file':'sahne-3.png'}]
  c['highlight']={'file':'sahne-1.png','from':110,'to':170,'path':'M 190 555 C 215 530 250 525 280 540 C 315 554 330 580 328 610 C 325 650 300 680 270 690 C 238 700 205 685 192 660 C 177 635 177 585 190 555'}
 im.save(d/'sahne-4.png');dest=r/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
 for f in {s['file'] for s in c['shots']}:shutil.copy(d/f,dest/f)
 (r/f'yeniden-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(r/f'yeniden-{id}.jsx').write_text((r/f'sifirdan-tam-{id}.jsx').read_text().replace(f'sifirdan-tam-{id}.json',f'yeniden-{id}.json'))
 bg=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(bg);g.rounded_rectangle((55,160,1025,515),radius=30,fill='#121d1b',outline='white',width=6)
 for j,line in enumerate(v['cover']):g.text((540,260+j*125),line,font=ImageFont.truetype(font,70 if j==0 else 62),fill='#ffe135' if j==0 else 'white',anchor='mm')
 bg.save(d/f'VID-{id}-img-1.jpg',quality=92);print(id,c['frames'],c['ctaStackFrames'])
