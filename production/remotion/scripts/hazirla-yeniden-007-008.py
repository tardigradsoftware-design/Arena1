#!/usr/bin/env python3
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageOps
import json,math,shutil,wave
root=Path(__file__).resolve().parents[3];r=root/'production/remotion';p=root/'production/sifirdan-yeni';font='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
info={'007':{'boundary':36.15,'words':[37.98,38.64,39.36,40.32],'cover':['DEODORANT İZİ','NASIL ÇIKAR?']},'008':{'boundary':31.60,'words':[33.66,34.35,35.07,35.88],'cover':['FIRÇAYA DOLANAN','SAÇ NASIL ÇIKAR?']}}
for id,v in info.items():
 d=p/f'VID-{id}';c=json.loads((r/f'sifirdan-tam-{id}.json').read_text());b=v['boundary']
 with wave.open(str(d/'anlatim.wav')) as f:duration=f.getnframes()/f.getframerate()
 c.update(dir='yeniden'+id,frames=math.ceil((b/1.55+(duration-b)/1.62+.3)*30),captionEnd=b/1.55,ctaStart=round(b/1.55*30),safeCaptions=True,hideRepresentativeLabel=True,representativeFiles=[],warning='',ctaStack=[['KAYDET','save'],['PAYLAŞ','share'],['YORUM YAP','talk'],['TAKİP ET','follow']],ctaStackFrames=[round((b/1.55+(x-b)/1.62)*30) for x in v['words']],tempoBoundary=b)
 im=Image.new('RGB',(768,1376),'#f1f0e9');g=ImageDraw.Draw(im)
 if id=='007':
  g.rounded_rectangle((135,375,635,1040),radius=48,fill='#27322e',outline='#101b18',width=6);g.line((255,590,310,710,275,800),fill='#e8e7dc',width=24);g.ellipse((345,635,570,850),fill='#fdfdf8',outline='#a6b0ab',width=7)
  c['highlight']={'file':'sahne-1.png','from':10,'to':43,'path':'M 280 535 C 300 510 340 505 370 515 C 405 525 413 550 410 590 L 382 920 C 376 950 345 975 315 968 C 285 965 275 940 278 900 L 285 600 C 286 575 278 550 280 535'}
  c['shots']=[{'from':0,'file':'sahne-1.png'},{'from':45,'file':'sahne-2.png'},{'from':100,'file':'sahne-1.png'},{'from':220,'file':'sahne-2.png'},{'from':310,'file':'sahne-4.png'},{'from':585,'file':'sahne-3.png'}]
 else:
  g.rounded_rectangle((105,520,665,855),radius=80,fill='#b6c3bd',outline='#324d44',width=9)
  g.rounded_rectangle((155,660,615,710),radius=16,fill='#394f48')
  for x in range(145,650,34):g.line((x,520,x-8,450),fill='#263c35',width=8);g.line((x,855,x-8,925),fill='#263c35',width=8)
  g.line((190,625,585,625),fill='#c18f5f',width=8)
  c['events']=[dict(e, b='OLUK') if e['b']=='ŞEMASI' else e for e in c['events']]
  c['highlight']={'file':'sahne-1.png','from':10,'to':43,'path':'M 180 630 C 230 580 320 560 410 570 C 520 575 600 600 640 650 C 665 680 640 730 595 750 C 500 790 300 790 215 750 C 175 730 150 675 180 630'}
  c['shots']=[{'from':0,'file':'sahne-1.png'},{'from':45,'file':'sahne-2.png'},{'from':115,'file':'sahne-1.png'},{'from':240,'file':'sahne-4.png'},{'from':480,'file':'sahne-3.png'}]
 im.save(d/'sahne-4.png');dest=r/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
 for f in {s['file'] for s in c['shots']}:shutil.copy(d/f,dest/f)
 (r/f'yeniden-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(r/f'yeniden-{id}.jsx').write_text((r/f'sifirdan-tam-{id}.jsx').read_text().replace(f'sifirdan-tam-{id}.json',f'yeniden-{id}.json'))
 bg=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(bg);g.rounded_rectangle((55,160,1025,515),radius=30,fill='#121d1b',outline='white',width=6)
 for j,line in enumerate(v['cover']):g.text((540,260+j*125),line,font=ImageFont.truetype(font,70 if j==0 else 62),fill='#ffe135' if j==0 else 'white',anchor='mm')
 bg.save(d/f'VID-{id}-img-1.jpg',quality=92);print(id,c['frames'],c['ctaStackFrames'])
