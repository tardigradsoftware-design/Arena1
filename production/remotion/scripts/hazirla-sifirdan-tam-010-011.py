#!/usr/bin/env python3
from pathlib import Path
import json, math, wave, shutil, zipfile, xml.etree.ElementTree as ET
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).resolve().parents[3]; prod=root/'production'; rem=prod/'remotion';ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with zipfile.ZipFile(root/'teslim/senaryolar-etkilesim-siralamasi-280.xlsx') as z:rows=ET.fromstring(z.read('xl/worksheets/sheet1.xml')).findall('.//s:row',ns)
data={}
for row in rows:
 c={''.join(ch for ch in x.get('r') if ch.isalpha()):''.join(x.itertext()) for x in row.findall('s:c',ns)}
 for id,term in [('010','Kavanozların Kapağını Güç Harcamadan'),('011','Bayat Ekmeği Fırından Yeni Çıkmış Gibi')]:
  if term in c.get('D',''):data[id]=c
font='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def diagram(id,kind,file):
 im=Image.new('RGB',(768,1376),'#f3f3ec');g=ImageDraw.Draw(im);big=ImageFont.truetype(font,46);small=ImageFont.truetype(font,28)
 if kind=='spoon':
  g.text((45,235),'KAŞIK SAPININ YERİ',font=big,fill='#213c32');g.text((45,305),'TEMSİLİ KESİT ŞEMASI',font=small,fill='#4e6e59')
  g.rounded_rectangle((190,580,555,1090),radius=40,outline='#8baeb4',width=13,fill='#e1eef0');g.rounded_rectangle((175,500,570,620),radius=20,fill='#a2a9a4',outline='#263a3d',width=8);g.rectangle((190,603,555,627),fill='#374d4b');g.polygon([(78,711),(84,682),(182,596),(202,601),(195,624)],fill='#7f9193',outline='#35474c',width=5);g.line((71,685,182,605),fill='#f3d251',width=7);g.arc((39,583,150,711),215,345,fill='#ce4538',width=8);g.polygon([(125,583),(157,587),(139,615)],fill='#ce4538')
 elif kind=='tape':
  g.text((45,235),'BANT KAPAĞIN ETRAFINDA',font=ImageFont.truetype(font,37),fill='#213c32');g.text((45,305),'TEMSİLİ ÜSTTEN GÖRÜNÜM',font=small,fill='#4e6e59');g.ellipse((170,475,590,895),fill='#9da6a2',outline='#253d38',width=10);g.ellipse((193,498,567,872),outline='#c38d45',width=35);g.polygon([(550,710),(680,760),(665,800),(525,754)],fill='#c38d45');g.line((610,750,690,780),fill='#c24237',width=10);g.polygon([(690,780),(665,750),(662,789)],fill='#c24237')
 else:
  g.text((67,220),'FIRINDA ISITMA',font=big,fill='#203a30');g.text((67,290),'TEMSİLİ SÜRE ŞEMASI',font=small,fill='#4e6e59');g.rounded_rectangle((88,470,680,910),radius=45,fill='#34443f');g.rounded_rectangle((135,520,633,860),radius=20,outline='#a3bab0',width=8,fill='#25332e');g.text((205,570),'200°C',font=ImageFont.truetype(font,95),fill='#ffe479');g.text((220,720),'5 DAKİKA',font=ImageFont.truetype(font,57),fill='white')
 im.save(file)
for id in ('010','011'):
 d=prod/f'sifirdan-tam/VID-{id}';c=data[id]
 if id=='010':
  diagram(id,'spoon',d/'sahne-sema-kasik.png');diagram(id,'tape',d/'sahne-sema-bant.png');end=27/1.55;shots=[(0,'sahne-1.png'),(45,'sahne-sema-kasik.png'),(105,'sahne-1.png'),(160,'sahne-sema-kasik.png'),(298,'sahne-3.png'),(386,'sahne-sema-bant.png'),(520,'sahne-3.png')];hook=['KAVANOZ KAPAĞI','NASIL AÇILIR?'];cover=['SIKIŞAN KAPAK','NASIL AÇILIR?','KAŞIKLA MI?'];events=[(165,210,'KAŞIK','SAPI','spoon','left'),(390,435,'BANT','YÖNTEMİ','hand','right')];warning='CAM HASARLIYSA KULLANMA';caption=c['M'].rsplit(' Kavanoz açarken',1)[0]
 else:
  diagram(id,'oven',d/'sahne-sema-firin.png');end=29.05/1.55;shots=[(0,'sahne-1.png'),(45,'sahne-2.png'),(100,'sahne-1.png'),(245,'sahne-2.png'),(340,'sahne-sema-firin.png'),(392,'sahne-3.png')];hook=['BAYAT EKMEK','NASIL YUMUŞAR?'];cover=['BAYAT EKMEK','NASIL YUMUŞAR?','SUYLA MI?'];events=[(140,185,'DIŞINI','ISLAT','drop','right'),(340,390,'FIRIN','5 DAKİKA','clock','left'),(435,480,'İÇİ','YUMUŞAK','hand','right')];warning='KÜFLÜ EKMEĞİ TÜKETME';caption=c['M'].rsplit(' Bu mutfak sırrını',1)[0]
 with wave.open(str(d/'anlatim.wav')) as f:frames=math.ceil((f.getnframes()/f.getframerate()/1.55+.2)*30)
 cfg={'id':id,'dir':'yenilisteTam'+id,'brand':True,'frames':frames,'caption':caption,'captionEnd':end,'ctaStart':round(end*30),'ctaTop':300,'ctaHeading':'BU FİKRİ PAYLAŞ','ctaItems':[['KAYDET','save'],['PAYLAŞ','share']] if id=='010' else [['KAYDET','save'],['BEĞEN','like']],'hook':hook,'openIcon':'jar' if id=='010' else 'oven','warning':warning,'shots':[{'from':t,'file':f} for t,f in shots],'events':[{'from':a,'to':b,'a':x,'b':y,'icon':i,'side':s,'y':330} for a,b,x,y,i,s in events],'representativeFiles':list(dict.fromkeys(f for _,f in shots))}
 dest=rem/'public'/cfg['dir'];dest.mkdir(parents=True,exist_ok=True)
 for f in cfg['representativeFiles']:shutil.copy(d/f,dest/f)
 (rem/f'sifirdan-tam-{id}.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2)+'\n');(rem/f'sifirdan-tam-{id}.jsx').write_text((rem/'sifirdan-tam-009.jsx').read_text().replace('sifirdan-tam-009.json',f'sifirdan-tam-{id}.json'))
 im=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im,'RGBA');g.rounded_rectangle((30,95,1050,735),radius=36,fill=(8,8,8,235),outline='white',width=6)
 for i,text in enumerate(cover):
  if i==2:g.rounded_rectangle((55,500,1025,695),radius=20,fill=(255,222,40,255),outline='black',width=5)
  for sz in range(120,40,-1):
   ft=ImageFont.truetype(font,sz);box=g.textbbox((0,0),text,font=ft,stroke_width=2)
   if box[2]-box[0]<(880 if i==2 else 930):break
  g.text(((1080-(box[2]-box[0]))/2,[155,310,520][i]),text,font=ft,fill='black' if i==2 else 'white',stroke_width=2,stroke_fill='black')
 im.save(d/f'VID-{id}-img-1.jpg',quality=93);print(id,frames,round(end*30),c['D'])
