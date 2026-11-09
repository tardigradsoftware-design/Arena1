#!/usr/bin/env python3
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageOps
import json,math,shutil,wave
root=Path(__file__).resolve().parents[3];r=root/'production/remotion';p=root/'production/sifirdan-yeni';font='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
info={'011':{'boundary':27.85,'words':[29.82,30.54,31.26,32.13],'cover':['BAYAT EKMEK','NASIL YUMUŞAR?']},'012':{'boundary':33.55,'words':[35.82,36.60,37.41,38.37],'cover':['KÖRELEN BIÇAK','NASIL KESKİNLEŞİR?']}}
for id,v in info.items():
 d=p/f'VID-{id}';c=json.loads((r/f'sifirdan-tam-{id}.json').read_text());b=v['boundary']
 with wave.open(str(d/'anlatim.wav')) as f:duration=f.getnframes()/f.getframerate()
 c.update(dir='yeniden'+id,frames=math.ceil((b/1.55+(duration-b)/1.62+.3)*30),captionEnd=b/1.55,ctaStart=round(b/1.55*30),safeCaptions=True,hideRepresentativeLabel=True,representativeFiles=[],warning='',ctaStack=[['KAYDET','save'],['PAYLAŞ','share'],['YORUM YAP','talk'],['TAKİP ET','follow']],ctaStackFrames=[round((b/1.55+(x-b)/1.62)*30) for x in v['words']],tempoBoundary=b)
 im=Image.new('RGB',(768,1376),'#f1f0e9');g=ImageDraw.Draw(im)
 if id=='011':
  g.rounded_rectangle((110,390,660,970),radius=30,fill='#dce4df',outline='#344e44',width=9);g.rectangle((155,455,615,895),fill='#81948b',outline='#344e44',width=8);g.line((175,750,595,750),fill='#344e44',width=12);g.ellipse((225,610,545,750),fill='#b78046',outline='#624b31',width=6)
  for x in (290,350,410,470):g.line((x,640,x+24,670),fill='#eed4a9',width=7)
  c['shots']=[{'from':0,'file':'sahne-1.png'},{'from':45,'file':'sahne-2.png'},{'from':100,'file':'sahne-1.png'},{'from':220,'file':'sahne-2.png'},{'from':340,'file':'sahne-4.png'},{'from':392,'file':'sahne-3.png'}]
  c['highlight']={'file':'sahne-4.png','from':345,'to':385,'path':'M 230 620 C 250 594 300 582 360 586 C 425 588 500 600 524 625 C 545 649 532 686 506 696 C 462 710 330 710 265 696 C 232 689 215 651 230 620'}
 else:
  g.ellipse((140,400,630,890),fill='#fffdfa',outline='#384f47',width=10);g.ellipse((220,480,550,810),outline='#a78866',width=32)
  # Cross-section-like blade at about 20 degrees to horizontal.
  g.polygon([(235,706),(555,590),(565,617),(245,732)],fill='#9aaba5',outline='#384f47')
  g.line((235,735,570,735),fill='#384f47',width=5)
  c['events']=[dict(e,a='20',b='DERECE') if e['b']=='ŞEMASI' else e for e in c['events']]
  c['shots']=[{'from':0,'file':'sahne-2.png'},{'from':45,'file':'sahne-1.png'},{'from':100,'file':'sahne-2.png'},{'from':190,'file':'sahne-1.png'},{'from':280,'file':'sahne-4.png'},{'from':470,'file':'sahne-3.png'}]
  c['highlight']={'file':'sahne-1.png','from':190,'to':235,'path':'M 195 640 C 210 565 280 525 365 526 C 450 525 525 570 546 640 C 565 720 520 805 455 832 C 390 860 290 844 236 794 C 195 756 182 689 195 640'}
 im.save(d/'sahne-4.png');dest=r/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
 for f in {s['file'] for s in c['shots']}:shutil.copy(d/f,dest/f)
 (r/f'yeniden-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(r/f'yeniden-{id}.jsx').write_text((r/f'sifirdan-tam-{id}.jsx').read_text().replace(f'sifirdan-tam-{id}.json',f'yeniden-{id}.json'))
 bg=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(bg);g.rounded_rectangle((55,160,1025,515),radius=30,fill='#121d1b',outline='white',width=6)
 for j,line in enumerate(v['cover']):g.text((540,260+j*125),line,font=ImageFont.truetype(font,72 if j==0 else 62),fill='#ffe135' if j==0 else 'white',anchor='mm')
 bg.save(d/f'VID-{id}-img-1.jpg',quality=92);print(id,c['frames'],c['ctaStackFrames'])
