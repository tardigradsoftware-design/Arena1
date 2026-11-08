#!/usr/bin/env python3
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageOps
import json,math,wave,shutil,zipfile,xml.etree.ElementTree as ET
root=Path(__file__).resolve().parents[3];prod=root/'production';rem=prod/'remotion';ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with zipfile.ZipFile(root/'teslim/senaryolar-etkilesim-siralamasi-280.xlsx') as z: rows=ET.fromstring(z.read('xl/worksheets/sheet1.xml')).findall('.//s:row',ns)
data={}
for row in rows:
 c={''.join(ch for ch in x.get('r') if ch.isalpha()):''.join(x.itertext()) for x in row.findall('s:c',ns)}
 for id,term in [('008','Süpürge Başlığına Dolanmış Saçları'),('009','Pencerelerden Gelen Soğuk Havayı')]:
  if term in c.get('D',''):data[id]=c
font='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
for id in ('008','009'):
 d=prod/f'sifirdan-tam/VID-{id}';c=data[id]; im=Image.new('RGB',(768,1376),'#e7e7df');g=ImageDraw.Draw(im)
 if id=='008':
  g.rounded_rectangle((80,540,690,810),radius=80,fill='#344558',outline='#0b1520',width=9);g.rounded_rectangle((120,656,655,698),radius=20,fill='#101820');
  for x in range(140,660,65):g.arc((x-45,475,x+45,885),75,290,fill='#996847',width=9)
  g.polygon([(275,620),(360,630),(570,670),(363,681),(275,671)],fill='#d7e2e8',outline='#1b2930',width=5)
  lines=['KESİM OLUĞU','TEMSİLİ ŞEMA'];hook=['SÜPÜRGE FIRÇASI','SAÇLAR NASIL ÇIKAR?'];cover=['FIRÇADAKİ SAÇ','NASIL ÇIKAR?','GİZLİ OLUK MU?']; end=32.4/1.55; st=round(end*30)
  shots=[(0,'sahne-1.png'),(45,'sahne-2.png'),(115,'sahne-1.png'),(240,'sahne-4.png'),(480,'sahne-3.png')]
  events=[(110,165,'DOLANAN','SAÇ','vacuum','right'),(260,310,'KANAL','ŞEMASI','scissors','left'),(495,535,'TEMİZ','FIRÇA','brush','right')];warning='OLUK VE YÖNTEM MODELE GÖRE DEĞİŞİR'
 else:
  g.rounded_rectangle((190,370,575,975),radius=18,fill='#f9f9f5',outline='#8c979c',width=9);g.rounded_rectangle((555,370,610,975),radius=10,fill='#26333a');g.ellipse((260,550,500,790),fill='#a9b4bc',outline='#3d4a4e',width=10);g.regular_polygon((380,670,46),6,rotation=30,fill='#303c42');g.arc((235,520,525,820),195,330,fill='#f2b900',width=12);g.polygon([(487,575),(526,563),(514,610)],fill='#f2b900');
  lines=['KİLİT PİMİ','TEMSİLİ ŞEMA'];hook=['PENCERE PİMİ','AYARLANABİLİR Mİ?'];cover=['PENCERE PİMİ','KIŞ AYARI MI?','ÖNCE KONTROL!'];end=34.05/1.55;st=round(end*30)
  shots=[(0,'sahne-1.png'),(45,'sahne-2.png'),(115,'sahne-1.png'),(210,'sahne-2.png'),(315,'sahne-4.png'),(550,'sahne-3.png')]
  events=[(130,180,'PENCERE','KENARI','door','right'),(245,295,'METAL','PİM','lock','left'),(440,485,'AYAR','ŞEMASI','lock','right')];warning='AYAR ŞEKLİ PENCERE MODELİNE BAĞLIDIR'
 g.text((85,200),lines[0],font=ImageFont.truetype(font,58),fill='#17232a');g.text((85,275),lines[1],font=ImageFont.truetype(font,34),fill='#334950');im.save(d/'sahne-4.png')
 with wave.open(str(d/'anlatim.wav')) as f:frames=math.ceil((f.getnframes()/f.getframerate()/1.55+.2)*30)
 caption=c['M'].rsplit(' Süpürge temizliği',1)[0] if id=='008' else c['M'].rsplit(' Şimdi pencerenizi',1)[0]
 cfg={'id':id,'dir':'yenilisteTam'+id,'brand':True,'frames':frames,'caption':caption,'captionEnd':end,'ctaStart':st,'ctaTop':300,'ctaHeading':'BU FİKRİ PAYLAŞ','ctaItems':[['BEĞEN','like'],['PAYLAŞ','share']],'hook':hook,'openIcon':'vacuum' if id=='008' else 'door','warning':warning,'shots':[{'from':t,'file':f} for t,f in shots], 'events':[dict(from_=a,to=b,a=x,b=y,icon=i,side=s,y=320) for a,b,x,y,i,s in events],'representativeFiles':[f'sahne-{i}.png' for i in range(1,5)]}
 for e in cfg['events']:e['from']=e.pop('from_')
 dest=rem/'public'/cfg['dir'];dest.mkdir(parents=True,exist_ok=True)
 for i in range(1,5):shutil.copy(d/f'sahne-{i}.png',dest/f'sahne-{i}.png')
 (rem/f'sifirdan-tam-{id}.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2)+'\n');(rem/f'sifirdan-tam-{id}.jsx').write_text((rem/'sifirdan-tam-007.jsx').read_text().replace('sifirdan-tam-007.json',f'sifirdan-tam-{id}.json'))
 im=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im,'RGBA');g.rounded_rectangle((30,95,1050,735),radius=36,fill=(8,8,8,235),outline='white',width=6)
 for i,text in enumerate(cover):
  if i==2:g.rounded_rectangle((55,500,1025,695),radius=20,fill=(255,222,40,255),outline='black',width=5)
  for sz in range(120,40,-1):
   ft=ImageFont.truetype(font,sz);box=g.textbbox((0,0),text,font=ft,stroke_width=2)
   if box[2]-box[0]<(880 if i==2 else 930):break
  g.text(((1080-(box[2]-box[0]))/2,[155,310,520][i]),text,font=ft,fill='black' if i==2 else 'white',stroke_width=2,stroke_fill='black')
 im.save(d/f'VID-{id}-img-1.jpg',quality=93);print(id,frames,st,c['D'])
