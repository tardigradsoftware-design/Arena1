#!/usr/bin/env python3
from pathlib import Path
import json,math,wave,shutil
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).resolve().parents[3];p=root/'production';r=p/'remotion'; covers={'006':['FIRIN CAMI','YANMIŞ YAĞ','NASIL ÇIKAR?'],'007':['BEYAZ İZ','NASIL SİLİNİR?','ÇORAPLA MI?']}
for id in ('006','007'):
 d=p/f'sifirdan-tam/VID-{id}';c=json.loads((r/f'viral-sirali-{id}.json').read_text())
 with wave.open(str(d/'anlatim.wav')) as f:c['frames']=math.ceil((f.getnframes()/f.getframerate()/1.55+.2)*30)
 c.update(dir='yenilisteTam'+id,brand=True,ctaHeading='BU FİKRİ PAYLAŞ',ctaItems=[['KAYDET','save'],['YORUM YAP','talk']] if id=='006' else [['BEĞEN','like'],['PAYLAŞ','share']],representativeFiles=[f'sahne-{i}.png' for i in range(1,5)])
 if id=='006':
  c.update(captionEnd=18.9,ctaStart=571,shots=[{'from':t,'file':name} for t,name in [(0,'sahne-1.png'),(45,'sahne-2.png'),(120,'sahne-1.png'),(180,'sahne-2.png'),(290,'sahne-3.png'),(390,'sahne-3.png'),(500,'sahne-4.png')]],highlight={'file':'sahne-1.png','from':125,'to':170,'path':'M245 618 C266 595 316 594 339 618 C351 637 340 674 316 684 C280 694 252 676 246 652 C243 640 241 629 245 618'})
 else:
  c.update(captionEnd=22.9,ctaStart=688,shots=[{'from':t,'file':name} for t,name in [(0,'sahne-1.png'),(45,'sahne-3.png'),(100,'sahne-1.png'),(220,'sahne-3.png'),(310,'sahne-2.png'),(460,'sahne-2.png'),(585,'sahne-4.png')]],highlight={'file':'sahne-1.png','from':105,'to':170,'path':'M520 540 C535 508 575 487 612 495 C653 501 676 534 668 567 C663 603 628 625 591 623 C551 622 518 599 515 572 C513 559 515 549 520 540'})
 dest=r/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
 for f in {x['file'] for x in c['shots']}:shutil.copy(d/f,dest/f)
 (r/f'sifirdan-tam-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(r/f'sifirdan-tam-{id}.jsx').write_text((r/'sifirdan-tam-005.jsx').read_text().replace('sifirdan-tam-005.json',f'sifirdan-tam-{id}.json'))
 im=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im,'RGBA');g.rounded_rectangle((30,95,1050,735),radius=36,fill=(8,8,8,232),outline='white',width=6)
 for i,text in enumerate(covers[id]):
  if i==2:g.rounded_rectangle((55,500,1025,695),radius=20,fill=(255,222,40,255),outline='black',width=5)
  for sz in range(130,40,-1):
   font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',sz);box=g.textbbox((0,0),text,font=font,stroke_width=2)
   if box[2]-box[0]<(880 if i==2 else 930):break
  g.text(((1080-(box[2]-box[0]))/2,[155,310,520][i]),text,font=font,fill='black' if i==2 else 'white',stroke_width=2,stroke_fill='black')
 im.save(d/f'VID-{id}-img-1.jpg',quality=93);im.resize((180,320)).save(f'/tmp/tam-{id}-cover.jpg');print(id,c['frames'])
