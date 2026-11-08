#!/usr/bin/env python3
from pathlib import Path
import math,wave,json,shutil
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).resolve().parents[3];p=root/'production';r=p/'remotion';pub=r/'public';ft='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
# A deliberately labelled diagram avoids presenting the inconsistent generated scissors as fact.
d=p/'sifirdan/VID-001';im=Image.new('RGB',(768,1376),'#efece4');g=ImageDraw.Draw(im);g.rounded_rectangle((35,130,733,1250),radius=30,fill='#fff',outline='#263a36',width=5);g.text((70,190),'TEMSİLİ ŞEMA',font=ImageFont.truetype(ft,40),fill='#263a36');g.rounded_rectangle((320,335,448,430),radius=8,fill='#e0e5e5',outline='#324d49',width=5);g.rectangle((350,355,420,395),outline='#324d49',width=5);g.polygon([(348,430),(420,430),(420,1030),(384,1115),(348,1030)],fill='#e4e9e8',outline='#324d49',width=5)
for y in range(520,960,95):
 g.polygon([(348,y),(365,y+12),(348,y+35)],fill='white');g.line([(348,y),(365,y+12),(348,y+35)],fill='#324d49',width=4)
 g.polygon([(420,y),(403,y+12),(420,y+35)],fill='white');g.line([(420,y),(403,y+12),(420,y+35)],fill='#324d49',width=4)
g.text((75,1150),'YAN KENAR ÇENTİKLERİ',font=ImageFont.truetype(ft,31),fill='#324d49');im.save(d/'sahne-sema.png')
common={
'001':{'caption':'Duş alırken su gitmiyor ve banyo gideriniz saç yüzünden tıkandıysa, pahalı kimyasallara veya tesisatçıya para harcamadan evde bulunan plastik bir cırt kelepçeyle gideri beş saniyede açın! Uzun bir plastik kablo bağının, cırt kelepçenin, iki yan kenarına makasla yukarı doğru bakan küçük çapraz çentikler keserek kancalı bir şerit oluşturun. Bu şeridi gider deliğinden içeri sokup iki kez çevirerek yukarı çektiğinizde, boruyu tıkayan tüm saç yumağını tek seferde çekip çıkardığını göreceksiniz.', 'captionEnd':20.6,'ctaStart':621,'hook':['TIKALI GİDER','NASIL AÇILIR?'],'openIcon':'drop','shots':[(0,'sahne-1.png'),(45,'sahne-sema.png'),(120,'sahne-1.png'),(205,'sahne-sema.png'),(420,'sahne-3.png'),(520,'sahne-4.png')],'events':[(105,150,'TIKALI','GİDER','drop','right',320),(230,275,'CIRT','KELEPÇE','wipe','left',320),(315,360,'KÜÇÜK','ÇENTİKLER','scissors','right',320),(455,500,'SAÇLARI','ÇIKAR','hand','left',320)],'cover':['TIKALI','GİDER','NASIL AÇILIR?']},
'003':{'caption':'Dibini tutturduğunuz çelik tencerenin veya fırın tepsisinin yanık karasını çıkarmak için tel süngerle kollarınızı koparana kadar ovalamayın! Yanık tencerenin içine sıcak su doldurup bir adet bulaşık makinesi tableti atın ve ocağın üzerinde on dakika kaynatın. Ardından suyu döküp alüminyum folyoyu top gibi buruşturun ve yumuşayan yanıkları folyoyla hafifçe silin. Tablet yağı çözerken folyo tencereyi hiç çizmeden tüm yanıkları saniyeler içinde söküp atacaktır.', 'captionEnd':21.0,'ctaStart':630,'hook':['YANMIŞ','TENCERE?'],'openIcon':'pot','shots':[(0,'sahne-1.png'),(45,'sahne-2.png'),(130,'sahne-1.png'),(220,'sahne-2.png'),(360,'sahne-3.png'),(570,'sahne-4.png')],'events':[(100,145,'YANMIŞ','TABAN','pot','right',320),(235,280,'BULAŞIK','TABLETİ','washer','left',320),(375,420,'ALÜMİNYUM','FOLYO','hand','right',320),(575,615,'TEMİZ','GÖRÜNÜM','pot','left',320)],'cover':['YANAN','TENCERE','NASIL ÇIKAR?']}}
for id,c0 in common.items():
 d=p/f'sifirdan/VID-{id}'
 with wave.open(str(d/'anlatim.wav')) as f:frames=math.ceil((f.getnframes()/f.getframerate()/1.55+.2)*30)
 print(id,frames)
 c=dict(id=id,dir='yenilisteSifirdan'+id,brand=True,frames=frames,caption=c0['caption'],captionEnd=c0['captionEnd'],ctaStart=min(c0['ctaStart'],frames-65),ctaTop=300,ctaHeading='FİKRİNİ PAYLAŞ',ctaItems=[['BEĞEN','like'],['PAYLAŞ','share']] if id=='001' else [['BEĞEN','like'],['YORUM YAP','talk']],hook=c0['hook'],openIcon=c0['openIcon'],shots=[{'from':x,'file':name} for x,name in c0['shots']],events=[dict(zip(('from','to','a','b','icon','side','y'),v)) for v in c0['events']],representativeFiles=sorted({name for x,name in c0['shots']}))
 dest=pub/c['dir'];dest.mkdir(parents=True,exist_ok=True)
 for f in {s['file'] for s in c['shots']}:shutil.copy(d/f,dest/f)
 (r/f'sifirdan-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(r/f'sifirdan-{id}.jsx').write_text((r/'sifirdan-002.jsx').read_text().replace('sifirdan-002.json',f'sifirdan-{id}.json'))
 im=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im,'RGBA');g.rounded_rectangle((30,95,1050,735),radius=36,fill=(8,8,8,232),outline='white',width=6)
 for i,text in enumerate(c0['cover']):
  if i==2:g.rounded_rectangle((55,500,1025,695),radius=20,fill=(255,222,40,255),outline='black',width=5)
  for sz in range(130,40,-1):
   font=ImageFont.truetype(ft,sz);box=g.textbbox((0,0),text,font=font,stroke_width=2)
   if box[2]-box[0]<(880 if i==2 else 930):break
  g.text(((1080-(box[2]-box[0]))/2,[155,310,520][i]),text,font=font,fill='black' if i==2 else 'white',stroke_width=2,stroke_fill='black')
 im.save(d/f'VID-{id}-img-1.jpg',quality=93);im.resize((180,320)).save(f'/tmp/sifirdan-{id}-cover.jpg')
