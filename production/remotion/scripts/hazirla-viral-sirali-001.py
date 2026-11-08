#!/usr/bin/env python3
from pathlib import Path
import math,wave,json,shutil
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).resolve().parents[3]; p=root/'production';r=p/'remotion';d=p/'viral-sirali/VID-001';pub=r/'public';pub.mkdir(exist_ok=True)
# A labelled, illustrative diagram, not a photo of the modified tool.
im=Image.new('RGB',(768,1376),'#e8e3d9');g=ImageDraw.Draw(im);font='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
g.rounded_rectangle((38,145,730,1250),radius=38,fill='#ffffff',outline='#1d3438',width=6)
g.text((70,190),'TEMSİLİ ŞEMA',font=ImageFont.truetype(font,43),fill='#1d3438')
g.rounded_rectangle((320,340,448,450),radius=12,fill='#ebeff0',outline='#42565a',width=6);g.rectangle((350,365,418,405),outline='#42565a',width=5)
left=[(345,450)];right=[(423,450)]
for y in range(500,1000,90):
 left += [(345,y),(324,y),(345,y+30)];right += [(423,y),(444,y),(423,y+30)]
poly=left+[(345,1030),(384,1120),(423,1030)]+list(reversed(right));g.polygon(poly,fill='#e3eaeb',outline='#42565a',width=5)
g.line((545,960,545,645),fill='#d84d41',width=12);g.polygon([(545,610),(520,660),(570,660)],fill='#d84d41')
g.text((490,1000),'YUKARI',font=ImageFont.truetype(font,30),fill='#bd332b');im.save(d/'sahne-sema.png')
with wave.open(str(d/'anlatim.wav')) as f: frames=math.ceil((f.getnframes()/f.getframerate()/1.55+.2)*30)
c={'id':'001','dir':'yenilisteViral001','brand':True,'frames':frames,'caption':'Duş alırken su gitmiyor ve banyo gideriniz saç yüzünden tıkandıysa, pahalı kimyasallara veya tesisatçıya para harcamadan evde bulunan plastik bir cırt kelepçeyle gideri beş saniyede açın! Uzun bir plastik kablo bağının, cırt kelepçenin, iki yan kenarına makasla yukarı doğru bakan küçük çapraz çentikler keserek kancalı bir şerit oluşturun. Bu şeridi gider deliğinden içeri sokup iki kez çevirerek yukarı çektiğinizde, boruyu tıkayan tüm saç yumağını tek seferde çekip çıkardığını göreceksiniz.', 'captionEnd':21.13,'ctaStart':634,'ctaTop':300,'ctaHeading':'BÖYLE İÇERİKLERİN DEVAMI İÇİN','ctaItems':[['BEĞEN','like'],['ABONE OL','subscribe']],'hook':['TIKALI GİDER','NASIL AÇILIR?'],'openIcon':'drop','shots':[{'from':x,'file':name} for x,name in [(0,'sahne-1.png'),(45,'sahne-2.png'),(125,'sahne-1.png'),(205,'sahne-2.png'),(290,'sahne-sema.png'),(450,'sahne-3.png'),(525,'sahne-3.png'),(605,'sahne-5.png')]],'events':[dict(zip(('from','to','a','b','icon','side','y'),v)) for v in [(105,150,'TIKALI','GİDER','drop','right',320),(230,275,'CIRT','KELEPÇE','wipe','left',320),(315,360,'KÜÇÜK','ÇENTİKLER','wipe','right',320),(440,485,'SAÇLARI','ÇIKAR','hand','left',320)]], 'representativeFiles':['sahne-sema.png','sahne-3.png','sahne-5.png'], 'highlight':{'file':'sahne-1.png','from':135,'to':190,'path':'M160 649 C165 598 206 563 262 562 C322 559 365 587 388 631 C407 670 398 716 371 741 C339 770 277 777 227 763 C184 750 156 716 158 681 C157 669 157 659 160 649'}}
dest=pub/c['dir'];dest.mkdir(exist_ok=True)
for f in {s['file'] for s in c['shots']}:shutil.copy(d/f,dest/f)
(r/'viral-sirali-001.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n'); (r/'viral-sirali-001.jsx').write_text((r/'yeni-liste-038.jsx').read_text().replace('yeni-liste-038.json','viral-sirali-001.json'))
im=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im,'RGBA');g.rounded_rectangle((30,95,1050,735),radius=36,fill=(8,8,8,232),outline='white',width=6)
for i,text in enumerate(['TIKALI','GİDER','NASIL AÇILIR?']):
 if i==2:g.rounded_rectangle((75,500,1005,695),radius=20,fill=(255,222,40,255),outline='black',width=5)
 for sz in range(135,40,-1):
  font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',sz);box=g.textbbox((0,0),text,font=font,stroke_width=2)
  if box[2]-box[0]<(820 if i==2 else 930):break
 g.text(((1080-(box[2]-box[0]))/2,[155,310,500][i]),text,font=font,fill='black' if i==2 else 'white',stroke_width=2,stroke_fill='black')
im.save(d/'VID-001-img-1.jpg',quality=93);im.resize((180,320)).save('/tmp/viral-001-cover.jpg');print(frames)
