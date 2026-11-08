#!/usr/bin/env python3
from pathlib import Path
import math,wave,json,shutil
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).resolve().parents[3];p=root/'production';r=p/'remotion';d=p/'viral-sirali/VID-006';pub=r/'public'
with wave.open(str(d/'anlatim.wav')) as f:frames=math.ceil((f.getnframes()/f.getframerate()/1.55+.2)*30)
c={'id':'006','dir':'yenilisteViral006','brand':True,'frames':frames,'caption':'Fırınınızın iç camına yapışıp taşlaşmış o kahverengi yanık yağ lekelerini çıkarmak için tel süngerle camı çizmeyin! Elinize bir eldiven giyin, sert bir bulaşık makinesi tabletinin ucunu ılık suya sadece bir saniye batırıp çıkarın ve tableti doğrudan silgi gibi ıslak fırın camının üzerindeki yanık lekelerine sürtün. Tabletin yoğunlaştırılmış enzimleri camı zerre kadar çizmeden en eski yanık yağları bile saniyeler içinde eritip akıtacaktır.', 'captionEnd':19.45,'ctaStart':588,'ctaTop':300,'ctaHeading':'BÖYLE İÇERİKLERİN DEVAMI İÇİN','ctaItems':[['BEĞEN','like'],['ABONE OL','subscribe']],'hook':['FIRIN CAMI','NASIL TEMİZLENİR?'],'openIcon':'oven','shots':[{'from':x,'file':name} for x,name in [(0,'sahne-1.png'),(45,'sahne-2.png'),(120,'sahne-1.png'),(180,'sahne-2.png'),(290,'sahne-3.png'),(390,'sahne-3.png'),(510,'sahne-4.png')]],'events':[dict(zip(('from','to','a','b','icon','side','y'),v)) for v in [(100,145,'YANMIŞ','YAĞ','oven','right',320),(205,250,'BULAŞIK','TABLETİ','washer','left',320),(330,375,'ISLAK','CAM','wipe','right',320),(520,565,'TEMİZ','GÖRÜNÜM','oven','left',320)]], 'representativeFiles':['sahne-1.png','sahne-2.png','sahne-3.png','sahne-4.png'], 'highlight':{'file':'sahne-1.png','from':125,'to':170,'path':'M220 465 C268 421 373 414 457 435 C526 452 561 518 557 606 C553 698 533 795 472 859 C414 914 326 913 259 887 C204 864 185 797 182 707 C181 603 184 511 220 465'}}
dest=pub/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for f in {s['file'] for s in c['shots']}:shutil.copy(d/f,dest/f)
(r/'viral-sirali-006.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(r/'viral-sirali-006.jsx').write_text((r/'viral-sirali-001.jsx').read_text().replace('viral-sirali-001.json','viral-sirali-006.json'))
im=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im,'RGBA');g.rounded_rectangle((30,95,1050,735),radius=36,fill=(8,8,8,232),outline='white',width=6)
for i,text in enumerate(['FIRIN CAMI','NASIL TEMİZLENİR?','TABLETLE Mİ?']):
 if i==2:g.rounded_rectangle((55,500,1025,695),radius=20,fill=(255,222,40,255),outline='black',width=5)
 for sz in range(130,40,-1):
  font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',sz);box=g.textbbox((0,0),text,font=font,stroke_width=2)
  if box[2]-box[0]<(880 if i==2 else 930):break
 g.text(((1080-(box[2]-box[0]))/2,[155,310,520][i]),text,font=font,fill='black' if i==2 else 'white',stroke_width=2,stroke_fill='black')
im.save(d/'VID-006-img-1.jpg',quality=93);im.resize((180,320)).save('/tmp/viral-006-cover.jpg');print(frames)
