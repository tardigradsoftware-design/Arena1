#!/usr/bin/env python3
from pathlib import Path
import math,wave,json,shutil
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).resolve().parents[3];p=root/'production';r=p/'remotion';d=p/'viral-sirali/VID-005';pub=r/'public'
with wave.open(str(d/'anlatim.wav')) as f:frames=math.ceil((f.getnframes()/f.getframerate()/1.55+.2)*30)
c={'id':'005','dir':'yenilisteViral005','brand':True,'frames':frames,'caption':'Orijinal telefon şarj kablolarınızın her seferinde tam uç birleşim yerinden bükülüp dış plastiğinin soyulmasından ve kablonun çöp olmasından bıktıysanız, bitmiş bir tükenmez kalemi atmayın! Basmalı bir tükenmez kalemin içindeki o küçük esnek metal yayı çıkarın, yayın ucunu tırnağınızla hafifçe aralayıp şarj kablonuzun en çok bükülen uç kısmına döndürerek sarın. Çelik yay kablonun doksan derece kırılmasını fiziksel olarak engelleyecek ve şarj kablonuzu yıllarca kopmadan ilk günkü gibi koruyacaktır.', 'captionEnd':22.2,'ctaStart':670,'ctaTop':300,'ctaHeading':'BU FİKRİ PAYLAŞ','ctaItems':[['BEĞEN','like'],['PAYLAŞ','share']],'hook':['KOPAN ŞARJ','KABLOLARI?'],'openIcon':'cable','shots':[{'from':x,'file':name} for x,name in [(0,'sahne-4.png'),(45,'sahne-2.png'),(120,'sahne-4.png'),(210,'sahne-2.png'),(345,'sahne-3.png'),(440,'sahne-3.png'),(550,'sahne-5.png')]],'events':[dict(zip(('from','to','a','b','icon','side','y'),v)) for v in [(95,140,'KABLO','UCU','cable','right',320),(245,290,'KALEMİN','YAYI','springwire','left',320),(405,450,'KABLOYA','SAR','hand','right',320),(560,605,'UÇ','BÖLGESİ','cable','left',320)]], 'representativeFiles':['sahne-3.png','sahne-5.png']}
dest=pub/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for f in {s['file'] for s in c['shots']}:shutil.copy(d/f,dest/f)
(r/'viral-sirali-005.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(r/'viral-sirali-005.jsx').write_text((r/'viral-sirali-001.jsx').read_text().replace('viral-sirali-001.json','viral-sirali-005.json'))
im=ImageOps.fit(Image.open(d/'sahne-3.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im,'RGBA');g.rounded_rectangle((30,95,1050,735),radius=36,fill=(8,8,8,232),outline='white',width=6)
for i,text in enumerate(['ŞARJ KABLOSU','KOPMASIN!','BU YAY NE İŞE YARAR?']):
 if i==2:g.rounded_rectangle((55,500,1025,695),radius=20,fill=(255,222,40,255),outline='black',width=5)
 for sz in range(130,40,-1):
  font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',sz);box=g.textbbox((0,0),text,font=font,stroke_width=2)
  if box[2]-box[0]<(880 if i==2 else 930):break
 g.text(((1080-(box[2]-box[0]))/2,[155,310,520][i]),text,font=font,fill='black' if i==2 else 'white',stroke_width=2,stroke_fill='black')
im.save(d/'VID-005-img-1.jpg',quality=93);im.resize((180,320)).save('/tmp/viral-005-cover.jpg');print(frames)
