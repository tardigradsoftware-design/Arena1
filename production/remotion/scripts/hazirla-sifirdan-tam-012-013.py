#!/usr/bin/env python3
from pathlib import Path
import json,math,wave,shutil,zipfile,xml.etree.ElementTree as ET
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).resolve().parents[3];prod=root/'production';rem=prod/'remotion';ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with zipfile.ZipFile(root/'teslim/senaryolar-etkilesim-siralamasi-280.xlsx') as z:rows=ET.fromstring(z.read('xl/worksheets/sheet1.xml')).findall('.//s:row',ns)
data={}
for row in rows:
 c={''.join(ch for ch in x.get('r') if ch.isalpha()):''.join(x.itertext()) for x in row.findall('s:c',ns)}
 for id,term in [('012','Evdeki Körelmiş Bıçakları ve Makasları 10 Saniyede'),('013','Birbirinin İçine Sıkışan Cam Bardakları')]:
  if term in c.get('D',''):data[id]=c
font='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def diagram(kind,file):
 im=Image.new('RGB',(768,1376),'#f1f3ec');g=ImageDraw.Draw(im);big=ImageFont.truetype(font,43);small=ImageFont.truetype(font,28)
 if kind=='mug':
  g.text((50,220),'SIRSIZ TABAN HALKASI',font=ImageFont.truetype(font,39),fill='#203a30');g.text((50,290),'TEMSİLİ ŞEMA',font=small,fill='#4d6b5d');g.rounded_rectangle((210,640,565,990),radius=35,fill='#fff',outline='#698079',width=8);g.ellipse((215,585,560,705),fill='#fff',outline='#698079',width=8);g.ellipse((270,615,505,680),outline='#bd9f76',width=15);g.polygon([(70,548),(78,530),(420,625),(428,640)],fill='#889995',outline='#40514d');g.arc((320,550,420,660),30,100,fill='#e6aa13',width=6);g.text((395,535),'20°',font=small,fill='#946000')
 else:
  g.text((50,210),'İÇ İÇE İKİ BARDAK' if kind=='nested' else 'SICAKLIK FARKI',font=big,fill='#203a30');g.text((50,280),'TEMSİLİ ŞEMA',font=small,fill='#4d6b5d');g.polygon([(188,520),(580,520),(545,980),(224,980)],fill='#e0eef0',outline='#4e7881',width=10);g.polygon([(245,430),(524,430),(500,805),(268,805)],fill='#c7e9f2',outline='#31717f',width=9)
  if kind=='heat':
   g.text((278,555),'İÇ',font=big,fill='#1a6778');g.text((285,885),'DIŞ',font=big,fill='#365c57');g.line((215,720,144,720),fill='#bb483a',width=9);g.line((550,720,620,720),fill='#bb483a',width=9);g.text((100,1080),'ANİ ISI FARKI RİSKLİDİR',font=ImageFont.truetype(font,29),fill='#9c342d')
  else:g.text((210,1065),'SIKIŞMA TEMSİLİ',font=small,fill='#365c57')
 im.save(file)
for id in ('012','013'):
 d=prod/f'sifirdan-tam/VID-{id}';c=data[id]
 if id=='012':
  diagram('mug',d/'sahne-sema-kupa.png');end=32.7/1.55;shots=[(0,'sahne-1.png'),(45,'sahne-3.png'),(100,'sahne-1.png'),(280,'sahne-sema-kupa.png'),(470,'sahne-2.png'),(565,'sahne-3.png')];hook=['KÖRELEN BIÇAK','KUPA İŞE YARAR MI?'];cover=['KÖRELEN BIÇAK','KUPAYLA MI?','HALKA NEREDE?'];events=[(190,245,'SIRSIZ','HALKA','mug','left'),(310,355,'AÇI','ŞEMASI','knife','right'),(475,515,'ALÜMİNYUM','FOLYO','scissors','left')];warning='FOLYONUN BİLEME ETKİSİ BELİRSİZ';caption=c['M'].rsplit(' Deneyip sonucunu',1)[0]
 else:
  diagram('nested',d/'sahne-sema-bardak.png');diagram('heat',d/'sahne-sema-isi.png');end=34.65/1.55;shots=[(0,'sahne-1.png'),(45,'sahne-sema-bardak.png'),(105,'sahne-1.png'),(250,'sahne-sema-bardak.png'),(345,'sahne-sema-isi.png'),(575,'sahne-3.png')];hook=['SIKIŞAN BARDAKLAR','NASIL AYRILIR?'];cover=['SIKIŞAN BARDAK','NASIL AYRILIR?','ISI FARKI MI?'];events=[(125,170,'İÇ İÇE','BARDAK','glass','left'),(370,420,'ISI','FARKI','drop','right'),(590,630,'AYRI','BARDAKLAR','glass','left')];warning='ANİ ISI FARKI CAMI ÇATLATabilir'.upper();caption=c['M'].rsplit(' Mutfak kazalarını',1)[0]
 with wave.open(str(d/'anlatim.wav')) as f:frames=math.ceil((f.getnframes()/f.getframerate()/1.55+.2)*30)
 cfg={'id':id,'dir':'yenilisteTam'+id,'brand':True,'frames':frames,'caption':caption,'captionEnd':end,'ctaStart':round(end*30),'ctaTop':300,'ctaHeading':'BU FİKRİ PAYLAŞ','ctaItems':[['YORUM YAP','talk'],['BEĞEN','like']] if id=='012' else [['KAYDET','save'],['PAYLAŞ','share']],'hook':hook,'openIcon':'mug' if id=='012' else 'glass','warning':warning,'shots':[{'from':t,'file':f} for t,f in shots],'events':[{'from':a,'to':b,'a':x,'b':y,'icon':i,'side':s,'y':330} for a,b,x,y,i,s in events],'representativeFiles':list(dict.fromkeys(f for _,f in shots))}
 dest=rem/'public'/cfg['dir'];dest.mkdir(parents=True,exist_ok=True)
 for f in cfg['representativeFiles']:shutil.copy(d/f,dest/f)
 (rem/f'sifirdan-tam-{id}.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2)+'\n');(rem/f'sifirdan-tam-{id}.jsx').write_text((rem/'sifirdan-tam-011.jsx').read_text().replace('sifirdan-tam-011.json',f'sifirdan-tam-{id}.json'))
 im=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im,'RGBA');g.rounded_rectangle((30,95,1050,735),radius=36,fill=(8,8,8,235),outline='white',width=6)
 for i,text in enumerate(cover):
  if i==2:g.rounded_rectangle((55,500,1025,695),radius=20,fill=(255,222,40,255),outline='black',width=5)
  for sz in range(120,40,-1):
   ft=ImageFont.truetype(font,sz);box=g.textbbox((0,0),text,font=ft,stroke_width=2)
   if box[2]-box[0]<(880 if i==2 else 930):break
  g.text(((1080-(box[2]-box[0]))/2,[155,310,520][i]),text,font=ft,fill='black' if i==2 else 'white',stroke_width=2,stroke_fill='black')
 im.save(d/f'VID-{id}-img-1.jpg',quality=93);print(id,frames,round(end*30),c['D'])
