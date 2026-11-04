#!/usr/bin/env python3
from pathlib import Path
import json,shutil,wave,math
from PIL import Image,ImageDraw,ImageFont,ImageOps,ImageFilter
root=Path(__file__).resolve().parents[3];p=root/'production';r=p/'remotion';pub=r/'public'
settings={
'031':{'caption':'Otoparkta arabanıza bindiğinizde ön cam sileceğinizin altına sıkıştırılmış bir kağıt görürseniz sakın arabadan inip onu almaya çalışmayın! Bu, kötü niyetli kişilerin sizi çalışır vaziyetteki araçtan dışarı çekmek için kullandığı en tehlikeli tuzaktır. Arabaya biner binmez ilk saniyede merkezi kilidi kapatın ve kağıdı almadan doğrudan güvenli bir yere sürün.','hook':['SİLECEKTEKİ','KAĞIT NE?'],'cover':['SİLECEKTE','KAĞIT','GÖRÜRSEN?'],'openIcon':'question','cta':16.4,'final':19.6,'events':[(75,125,'SİLECEKTE','KAĞIT','question','right',350),(345,395,'ARAÇ','KİLİDİ','lock','right',300)],'shots':[(0,1),(45,2),(115,1),(220,4),(345,3),(445,4),(500,1)]},
'032':{'caption':'Birinin ricasını reddettiğinizde arkasından beş dakika boyunca mazeret uydurup kendinizi açıklamaya çalışıyorsanız, karşı tarafa sizi ikna etmesi için açık kapı bırakıyorsunuz demektir! Psikolojide fazla açıklama yapmak suçluluk belirtisidir. İstemediğiniz bir şeye sınır koyarken mazeret bildirmeyin; sadece gülümseyerek maalesef bu plan bana uymuyor ama sorman çok incelikliydi deyin.','hook':['HAYIR DERKEN','ZORLANIYOR MUSUN?'],'cover':['HAYIR','DEMEK','ZOR MU?'],'openIcon':'talk','cta':17.2,'final':20.1,'events':[(105,155,'AÇIKLAMA','YAPMAK','talk','right',340),(305,355,'SINIR','KOYMAK','hand','left',340)],'shots':[(0,1),(45,4),(105,3),(215,2),(305,1),(410,4),(520,3)]}}
# The stored 031 scene 2 is already cropped to remove the plate and logo.
for id,s in settings.items():
 d=p/'yeni-senaryolar'/f'VID-{id}'
 with wave.open(str(d/'seri-yeni-anlatim.wav')) as f:frames=math.ceil((f.getnframes()/f.getframerate()/1.55+.2)*30)
 c={key:s[key] for key in ('caption','hook','openIcon')};c.update(id=id,dir='yeniseri'+id,frames=frames,captionEnd=s['cta'],ctaStart=round(30*s['cta']),cta2Start=round(30*s['final']),ctaHeading='SEN NE DÜŞÜNÜYORSUN?',ctaFinalHeading='BÖYLE İÇERİKLERİN DEVAMI İÇİN',ctaItems=[['BEĞEN','like'],['ABONE OL','subscribe']],ctaFirstItems=[['YORUM YAP','talk'],['BEĞEN','like']],shots=[{'from':f,'file':f'sahne-{i}.png'} for f,i in s['shots']],events=[dict(zip(('from','to','a','b','icon','side','y'),x)) for x in s['events']])
 (r/f'yeni-seri-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(r/f'yeni-seri-{id}.jsx').write_text((r/'yeni-seri-030.jsx').read_text().replace('030',id));dest=pub/c['dir'];dest.mkdir(exist_ok=True)
 for i in range(1,5):shutil.copy(d/f'sahne-{i}.png',dest/f'sahne-{i}.png')
 im=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));draw=ImageDraw.Draw(im,'RGBA');draw.rounded_rectangle((30,95,1050,735),radius=36,fill=(8,8,8,232),outline='white',width=6)
 for i,text in enumerate(s['cover']):
  if i==2:draw.rounded_rectangle((75,500,1005,695),radius=20,fill=(255,222,40,255),outline='black',width=5)
  for sz in range(135,40,-1):
   font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',sz);box=draw.textbbox((0,0),text,font=font,stroke_width=2)
   if box[2]-box[0]<(820 if i==2 else 930):break
  draw.text(((1080-(box[2]-box[0]))/2,[155,310,500][i]),text,font=font,fill='black' if i==2 else 'white',stroke_width=2,stroke_fill='black')
 im.save(d/f'VID-{id}-img-1.jpg',quality=93);im.resize((180,320)).save(f'/tmp/kapak-{id}.jpg');print(id,frames)
