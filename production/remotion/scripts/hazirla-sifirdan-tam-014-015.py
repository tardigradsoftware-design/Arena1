#!/usr/bin/env python3
from pathlib import Path
import json,math,wave,shutil,zipfile,xml.etree.ElementTree as ET
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).resolve().parents[3];prod=root/'production';rem=prod/'remotion';ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with zipfile.ZipFile(root/'teslim/senaryolar-etkilesim-siralamasi-280.xlsx') as z:rows=ET.fromstring(z.read('xl/worksheets/sheet1.xml')).findall('.//s:row',ns)
data={}
for row in rows:
 c={''.join(ch for ch in x.get('r') if ch.isalpha()):''.join(x.itertext()) for x in row.findall('s:c',ns)}
 for id,term in [('014','Beyaz Gömlek ve Tişörtlerdeki Sarı Ter Lekelerini Söken'),('015','Kaynayan Sütün ve Çorbanın Taşmasını')]:
  if term in c.get('D',''):data[id]=c
font='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def diagram(kind,file):
 im=Image.new('RGB',(768,1376),'#f2f5ef');g=ImageDraw.Draw(im);big=ImageFont.truetype(font,42);small=ImageFont.truetype(font,28)
 if kind=='brush':
  g.text((50,210),'LEKEYE UYGULAMA',font=big,fill='#203a30');g.text((50,280),'TEMSİLİ ŞEMA',font=small,fill='#4d6b5d');g.polygon([(220,500),(297,455),(470,455),(548,500),(650,635),(552,695),(525,640),(525,1000),(242,1000),(242,640),(215,695),(118,635)],fill='white',outline='#879e93',width=7);g.ellipse((462,590,552,700),fill='#e4c980');g.rounded_rectangle((402,560,590,588),radius=12,fill='#5b9a9c');g.rectangle((475,588,570,605),fill='#548e90')
 else:
  g.text((50,210),'TENCERE ÜST KENARI',font=big,fill='#203a30');g.text((50,280),'TEMSİLİ ÜSTTEN GÖRÜNÜM',font=small,fill='#4d6b5d');g.ellipse((100,435,668,1003),fill='#a5b5ac',outline='#3d5d50',width=10);g.ellipse((135,470,633,968),fill='#f4f5f1',outline='#d8bd70',width=20);g.rounded_rectangle((76,692,704,718),radius=13,fill='#a9763d');g.text((193,1050),'OCAĞI TAKİP ET',font=small,fill='#943b31')
 im.save(file)
for id in ('014','015'):
 d=prod/f'sifirdan-tam/VID-{id}';c=data[id]
 if id=='014':
  diagram('brush',d/'sahne-sema-firca.png');end=33.2/1.55;shots=[(0,'sahne-1.png'),(45,'sahne-2.png'),(105,'sahne-1.png'),(205,'sahne-2.png'),(350,'sahne-sema-firca.png'),(515,'sahne-3.png')];hook=['SARI TER LEKESİ','NASIL ÇIKAR?'];cover=['SARI LEKELER','NASIL ÇIKAR?','ASPİRİN Mİ?'];events=[(120,160,'SARI','LEKE','wipe','right'),(235,280,'KARIŞIM','TEMSİLİ','bowl','left'),(390,435,'FIRÇA','ŞEMASI','brush','right')];warning='SONUÇ KUMAŞA GÖRE DEĞİŞİR';caption=c['M'].rsplit(' Hemen kaydet',1)[0]
 else:
  diagram('pot',d/'sahne-sema-tencere.png');end=31.5/1.55;shots=[(0,'sahne-1.png'),(45,'sahne-3.png'),(105,'sahne-1.png'),(200,'sahne-2.png'),(340,'sahne-sema-tencere.png'),(420,'sahne-3.png')];hook=['SÜT TAŞMASI','NASIL ÖNLENİR?'];cover=['SÜT TAŞMASIN','DİYE NE YAPILIR?','TEREYAĞI MI?'];events=[(215,260,'İNCE','YAĞ ŞERİDİ','pot','left'),(345,390,'TAHTA','KAŞIK','spoon','right'),(470,510,'OCAĞI','TAKİP ET','oven','left')];warning='TAŞMA YİNE OLABİLİR · OCAĞI TAKİP ET';caption=c['M'].rsplit(' Ocağı temizlemekten',1)[0]
 with wave.open(str(d/'anlatim.wav')) as f:frames=math.ceil((f.getnframes()/f.getframerate()/1.55+.2)*30)
 cfg={'id':id,'dir':'yenilisteTam'+id,'brand':True,'frames':frames,'caption':caption,'captionEnd':end,'ctaStart':round(end*30),'ctaTop':300,'ctaHeading':'BU FİKRİ PAYLAŞ','ctaItems':[['KAYDET','save'],['PAYLAŞ','share']],'hook':hook,'openIcon':'wipe' if id=='014' else 'pot','warning':warning,'shots':[{'from':t,'file':f} for t,f in shots],'events':[{'from':a,'to':b,'a':x,'b':y,'icon':i,'side':s,'y':330} for a,b,x,y,i,s in events],'representativeFiles':list(dict.fromkeys(f for _,f in shots))}
 cfg['highlight']=({'file':'sahne-1.png','from':110,'to':170,'path':'M118 600 C126 568 158 544 190 550 C217 553 237 575 236 606 C236 636 211 666 178 670 C145 671 121 652 118 627 C116 618 116 608 118 600'} if id=='014' else {'file':'sahne-2.png','from':215,'to':260,'path':'M122 710 C145 684 188 657 231 640 C258 628 291 621 313 630 C328 641 326 661 305 676 C276 690 250 693 219 704 C186 717 153 737 133 739 C121 739 115 726 122 710'})
 dest=rem/'public'/cfg['dir'];dest.mkdir(parents=True,exist_ok=True)
 for f in cfg['representativeFiles']:shutil.copy(d/f,dest/f)
 (rem/f'sifirdan-tam-{id}.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2)+'\n');(rem/f'sifirdan-tam-{id}.jsx').write_text((rem/'sifirdan-tam-013.jsx').read_text().replace('sifirdan-tam-013.json',f'sifirdan-tam-{id}.json'))
 im=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im,'RGBA');g.rounded_rectangle((30,95,1050,735),radius=36,fill=(8,8,8,235),outline='white',width=6)
 for i,text in enumerate(cover):
  if i==2:g.rounded_rectangle((55,500,1025,695),radius=20,fill=(255,222,40,255),outline='black',width=5)
  for sz in range(120,40,-1):
   ft=ImageFont.truetype(font,sz);box=g.textbbox((0,0),text,font=ft,stroke_width=2)
   if box[2]-box[0]<(880 if i==2 else 930):break
  g.text(((1080-(box[2]-box[0]))/2,[155,310,520][i]),text,font=ft,fill='black' if i==2 else 'white',stroke_width=2,stroke_fill='black')
 im.save(d/f'VID-{id}-img-1.jpg',quality=93);print(id,frames,round(end*30),c['D'])
