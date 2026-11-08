#!/usr/bin/env python3
from pathlib import Path
import math,wave,json,shutil
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).resolve().parents[3];p=root/'production';r=p/'remotion';d=p/'viral-sirali/VID-007';pub=r/'public'
with wave.open(str(d/'anlatim.wav')) as f:frames=math.ceil((f.getnframes()/f.getframerate()/1.55+.2)*30)
c={'id':'007','dir':'yenilisteViral007','brand':True,'frames':frames,'caption':'Tam evden çıkacakken giydiğiniz siyah tişörtün veya elbisenin üzerine bulaşan o beyaz deodorant izini ıslak mendille silerseniz lekeyi çamur gibi yayıp daha da büyütürsünüz! Deodorant lekesine asla su sürmeyin. Çekmecenizdeki temiz ve kuru bir ince külotlu çorabı veya giydiğiniz pamuklu çorabın tersini top haline getirip beyaz lekenin üzerine kuru kuru üç saniye sürtün. Naylon dokunun yarattığı statik elektrik tüm beyaz pudra taneciklerini kumaştan mıknatıs gibi çekecek ve siyah kıyafetiniz anında tertemiz olacaktır.', 'captionEnd':22.3,'ctaStart':675,'ctaTop':300,'ctaHeading':'BU FİKRİ PAYLAŞ','ctaItems':[['BEĞEN','like'],['PAYLAŞ','share']],'hook':['DEODORANT','İZİ NASIL ÇIKAR?'],'openIcon':'wipe','shots':[{'from':x,'file':name} for x,name in [(0,'sahne-1.png'),(45,'sahne-2.png'),(95,'sahne-1.png'),(225,'sahne-2.png'),(335,'sahne-2.png'),(470,'sahne-3.png'),(565,'sahne-3.png')]],'events':[dict(zip(('from','to','a','b','icon','side','y'),v)) for v in [(105,150,'BEYAZ','İZ','wipe','right',320),(280,330,'KURU','ÇORAP','hand','left',320),(410,455,'HAFİFÇE','SÜRT','hand','right',320),(570,610,'TEMİZ','GÖRÜNÜM','wipe','left',320)]], 'representativeFiles':['sahne-1.png','sahne-2.png','sahne-3.png'],'highlight':{'file':'sahne-1.png','from':100,'to':170,'path':'M550 570 C567 528 617 505 661 509 C711 511 733 540 731 583 C728 624 699 653 655 660 C610 668 564 651 550 618 C544 604 545 585 550 570'}}
dest=pub/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for f in {s['file'] for s in c['shots']}:shutil.copy(d/f,dest/f)
(r/'viral-sirali-007.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(r/'viral-sirali-007.jsx').write_text((r/'viral-sirali-001.jsx').read_text().replace('viral-sirali-001.json','viral-sirali-007.json'))
im=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im,'RGBA');g.rounded_rectangle((30,95,1050,735),radius=36,fill=(8,8,8,232),outline='white',width=6)
for i,text in enumerate(['BEYAZ İZ','NASIL SİLİNİR?','ÇORAPLA MI?']):
 if i==2:g.rounded_rectangle((55,500,1025,695),radius=20,fill=(255,222,40,255),outline='black',width=5)
 for sz in range(130,40,-1):
  font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',sz);box=g.textbbox((0,0),text,font=font,stroke_width=2)
  if box[2]-box[0]<(880 if i==2 else 930):break
 g.text(((1080-(box[2]-box[0]))/2,[155,310,520][i]),text,font=font,fill='black' if i==2 else 'white',stroke_width=2,stroke_fill='black')
im.save(d/'VID-007-img-1.jpg',quality=93);im.resize((180,320)).save('/tmp/viral-007-cover.jpg');print(frames)
