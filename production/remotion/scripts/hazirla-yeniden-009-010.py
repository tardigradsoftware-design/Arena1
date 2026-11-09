#!/usr/bin/env python3
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageOps
import json,math,shutil,wave
root=Path(__file__).resolve().parents[3];r=root/'production/remotion';p=root/'production/sifirdan-yeni';font='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
info={'009':{'boundary':32.65,'words':[34.65,35.31,35.97,36.78],'cover':['PENCERE PİMİ','NASIL AYARLANIR?']},'010':{'boundary':27.95,'words':[30.09,30.78,31.50,32.28],'cover':['KAVANOZ KAPAĞI','NASIL AÇILIR?']}}
for id,v in info.items():
 d=p/f'VID-{id}';c=json.loads((r/f'sifirdan-tam-{id}.json').read_text());b=v['boundary']
 with wave.open(str(d/'anlatim.wav')) as f:duration=f.getnframes()/f.getframerate()
 c.update(dir='yeniden'+id,frames=math.ceil((b/1.55+(duration-b)/1.62+.3)*30),captionEnd=b/1.55,ctaStart=round(b/1.55*30),safeCaptions=True,hideRepresentativeLabel=True,representativeFiles=[],warning='',ctaStack=[['KAYDET','save'],['PAYLAŞ','share'],['YORUM YAP','talk'],['TAKİP ET','follow']],ctaStackFrames=[round((b/1.55+(x-b)/1.62)*30) for x in v['words']],tempoBoundary=b)
 c['events']=[dict(e,b='PİM') if e['b']=='ŞEMASI' else e for e in c['events']]
 im=Image.new('RGB',(768,1376),'#f1f0e9');g=ImageDraw.Draw(im)
 if id=='009':
  g.rectangle((130,350,480,1010),fill='#d5ddd9',outline='#344f46',width=8);g.rectangle((475,350,530,1010),fill='#41564f');g.ellipse((245,570,420,745),fill='#98aaa3',outline='#344f46',width=8);g.line((333,657,410,657),fill='#263e37',width=14)
  c['shots']=[{'from':0,'file':'sahne-1.png'},{'from':45,'file':'sahne-2.png'},{'from':115,'file':'sahne-1.png'},{'from':210,'file':'sahne-2.png'},{'from':315,'file':'sahne-4.png'},{'from':550,'file':'sahne-3.png'}]
  c['highlight']={'file':'sahne-4.png','from':325,'to':370,'path':'M 240 595 C 255 570 290 553 325 555 C 365 557 404 578 414 611 C 424 647 405 678 374 688 C 339 700 290 689 265 675 C 240 661 230 620 240 595'}
 else:
  # Side cross-section: spoon end rests under lid's lower skirt.
  g.rounded_rectangle((180,530,590,950),radius=35,fill='#d5e3dc',outline='#364e47',width=7);g.rounded_rectangle((160,465,610,555),radius=18,fill='#aab7b2',outline='#364e47',width=8)
  g.polygon([(565,558),(600,540),(710,630),(705,647),(595,570)],fill='#778c86',outline='#364e47')
  tape=Image.new('RGB',(768,1376),'#f1f0e9');t=ImageDraw.Draw(tape);t.ellipse((165,430,603,868),fill='#aab7b2',outline='#364e47',width=9);t.ellipse((195,460,573,838),outline='#c28f4d',width=35);t.polygon([(550,675),(691,720),(675,765),(535,720)],fill='#c28f4d')
  tape.save(d/'sahne-5.png')
  c['shots']=[{'from':0,'file':'sahne-1.png'},{'from':45,'file':'sahne-2.png'},{'from':105,'file':'sahne-1.png'},{'from':160,'file':'sahne-4.png'},{'from':298,'file':'sahne-3.png'},{'from':386,'file':'sahne-5.png'},{'from':500,'file':'sahne-3.png'}]
  c['highlight']={'file':'sahne-4.png','from':165,'to':210,'path':'M 540 520 C 557 510 584 512 604 525 C 624 537 627 557 611 570 C 595 584 565 581 547 570 C 530 559 526 533 540 520'}
 im.save(d/'sahne-4.png');dest=r/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
 for f in {s['file'] for s in c['shots']}:shutil.copy(d/f,dest/f)
 (r/f'yeniden-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(r/f'yeniden-{id}.jsx').write_text((r/f'sifirdan-tam-{id}.jsx').read_text().replace(f'sifirdan-tam-{id}.json',f'yeniden-{id}.json'))
 bg=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(bg);g.rounded_rectangle((55,160,1025,515),radius=30,fill='#121d1b',outline='white',width=6)
 for j,line in enumerate(v['cover']):g.text((540,260+j*125),line,font=ImageFont.truetype(font,72 if j==0 else 62),fill='#ffe135' if j==0 else 'white',anchor='mm')
 bg.save(d/f'VID-{id}-img-1.jpg',quality=92);print(id,c['frames'],c['ctaStackFrames'])
