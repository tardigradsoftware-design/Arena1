#!/usr/bin/env python3
from pathlib import Path
import json, shutil, wave, math
from PIL import Image, ImageDraw, ImageFont, ImageOps
root=Path(__file__).resolve().parents[3]; p=root/'production'; r=p/'remotion'; pub=r/'public'
settings={
'013': {'caption':'Kapağını açtığınız salça kavanozunun üstüne zeytinyağı dökseniz bile kaşık değdiği için kenarlarından beyaz küf bağlamasına son verin! Salçadan her zaman temiz ve kuru bir kaşıkla aldıktan sonra, kavanozun iç kenarlarını peçeteyle silin, üzerine ince bir kat zeytinyağı gezdirip kapağını sıkıca kapatın ve buzdolabına ters çevirerek koyun. Kavanoza hava sızamayacağı için salçanız son kaşığına kadar küflenmez.', 'hook':['SALÇAYI','NASIL SAKLAMALI?'], 'cover':['SALÇA','NASIL','SAKLANIR?'], 'openIcon':'jar', 'cta':17.4, 'final':19.92, 'events':[(100,145,'TEMİZ','KAŞIK','spoon','right',330),(220,265,'ZEYTİNYAĞI','KAVANOZ','jar','left',330),(350,390,'BUZDOLABI','SAKLAMA','ice','right',330)], 'shots':[(0,4),(45,1),(125,2),(240,4),(335,3),(445,2),(520,4)], 'highlight':{'file':'sahne-1.png','from':70,'to':112,'path':'M195 657 C214 603 276 574 352 582 C432 583 496 610 520 659 C545 708 500 744 434 750 C337 764 234 745 207 705 C195 691 191 674 195 657'}},
'014': {'caption':'Aniden misafiriniz geldiğinde soğuk içeceğiniz yoksa şişeyi buzluğa atıp saatlerce soğumasını beklemeyin! Oda sıcaklığındaki içecek şişesinin etrafına bir kat kağıt havlu sarın, kağıt havluyu suyla tamamen ıslatıp üzerine bir yemek kaşığı tuz serpin ve buzlukta sadece beş dakika bekletin. Tuz suyun donma noktasını düşürürken ıslak peçete şişenin ısısını saniyeler içinde emerek içeceğinizi buz gibi yapar.', 'hook':['İÇECEKLER','NASIL SOĞUR?'], 'cover':['İÇECEKLER','NASIL','SOĞUTULUR?'], 'openIcon':'bottle', 'cta':17.33, 'events':[(100,145,'KAĞIT','HAVLU','wipe','right',320),(230,275,'SU VE','TUZ','drop','left',320),(325,370,'BUZLUKTA','BEKLET','ice','right',320)], 'shots':[(0,1),(45,4),(110,2),(220,4),(300,3),(390,2),(510,1)], 'highlight':{'file':'sahne-2.png','from':140,'to':200,'path':'M235 510 C238 495 292 489 374 490 C463 491 515 493 522 515 L528 1145 C520 1185 480 1202 394 1205 C310 1208 259 1190 253 1159 Z'}}}
for id,s in settings.items():
 d=p/'yeni-liste'/f'VID-{id}'
 with wave.open(str(d/'anlatim.wav')) as f: frames=math.ceil((f.getnframes()/f.getframerate()/1.55+.2)*30)
 c={key:s[key] for key in ('caption','hook','openIcon','highlight')}
 c.update(id=id,dir='yeniliste'+id,frames=frames,captionEnd=s['cta'],ctaStart=round(30*s['cta']),ctaTop=300,ctaHeading='BÖYLE İÇERİKLERİN DEVAMI İÇİN',ctaItems=[['BEĞEN','like'],['ABONE OL','subscribe']],shots=[{'from':f,'file':f'sahne-{i}.png'} for f,i in s['shots']],events=[dict(zip(('from','to','a','b','icon','side','y'),x)) for x in s['events']])
 if 'final' in s: c.update(cta2Start=round(30*s['final']),ctaHeading='SEN NE DÜŞÜNÜYORSUN?',ctaFinalHeading='BÖYLE İÇERİKLERİN DEVAMI İÇİN',ctaFirstItems=[['YORUM YAP','talk'],['BEĞEN','like']])
 (r/f'yeni-liste-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
 (r/f'yeni-liste-{id}.jsx').write_text((r/'yeni-seri-030.jsx').read_text().replace('yeni-seri-030.json',f'yeni-liste-{id}.json'))
 dest=pub/c['dir'];dest.mkdir(exist_ok=True)
 for i in sorted({i for _,i in s['shots']}):shutil.copy(d/f'sahne-{i}.png',dest/f'sahne-{i}.png')
 cover=4 if id=='013' else 1
 im=ImageOps.fit(Image.open(d/f'sahne-{cover}.png').convert('RGB'),(1080,1920));draw=ImageDraw.Draw(im,'RGBA')
 draw.rounded_rectangle((30,95,1050,735),radius=36,fill=(8,8,8,232),outline='white',width=6)
 for i,text in enumerate(s['cover']):
  if i==2:draw.rounded_rectangle((75,500,1005,695),radius=20,fill=(255,222,40,255),outline='black',width=5)
  for sz in range(135,40,-1):
   font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',sz);box=draw.textbbox((0,0),text,font=font,stroke_width=2)
   if box[2]-box[0]<(820 if i==2 else 930):break
  draw.text(((1080-(box[2]-box[0]))/2,[155,310,500][i]),text,font=font,fill='black' if i==2 else 'white',stroke_width=2,stroke_fill='black')
 im.save(d/f'VID-{id}-img-1.jpg',quality=93);im.resize((180,320)).save(f'/tmp/liste-kapak-{id}.jpg');print(id,frames,c['ctaStart'])
