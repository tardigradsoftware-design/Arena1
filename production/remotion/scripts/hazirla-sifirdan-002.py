#!/usr/bin/env python3
from pathlib import Path
import math,wave,json,shutil
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).resolve().parents[3];p=root/'production';r=p/'remotion';d=p/'sifirdan/VID-002';pub=r/'public'
with wave.open(str(d/'anlatim.wav')) as f:frames=math.ceil((f.getnframes()/f.getframerate()/1.55+.2)*30)
c={'id':'002','dir':'yenilisteSifirdan002','brand':True,'frames':frames,'caption':'Halınızı en güçlü elektrik süpürgesiyle süpürdüğünüz halde halının ilmeklerine dolanan uzun saçları ve evcil hayvan tüylerini süpürgenin çekemediğini biliyor muydunuz? Halınızı süpürdükten sonra elinize cam silmek için kullandığınız kuru bir kauçuk çekpası alın ve halının üzerinde kendinize doğru bastırarak tarar gibi çekin. Kauçuk lastiğin sürtünme gücüyle temiz sandığınız halının içinden avuç dolusu saç ve tüy yumağı çıktığını gördüğünüzde gözlerinize inanamayacaksınız!', 'captionEnd':19.2,'ctaStart':578,'ctaTop':300,'ctaHeading':'FİKRİNİ PAYLAŞ','ctaItems':[['BEĞEN','like'],['YORUM YAP','talk']],'hook':['TEMİZ HALIDA','GİZLİ TÜYLER?'],'openIcon':'vacuum','shots':[{'from':x,'file':name} for x,name in [(0,'sahne-1.png'),(45,'sahne-2.png'),(95,'sahne-1.png'),(205,'sahne-2.png'),(325,'sahne-2.png'),(425,'sahne-3.png'),(520,'sahne-3.png')]],'events':[dict(zip(('from','to','a','b','icon','side','y'),v)) for v in [(100,145,'SAÇ VE','TÜYLER','vacuum','right',320),(230,275,'KURU','ÇEKPAS','squeegee','left',320),(350,395,'HALIDA','GERİ ÇEK','squeegee','right',320),(470,515,'TOPLANAN','TÜYLER','hand','left',320)]], 'representativeFiles':['sahne-1.png','sahne-2.png','sahne-3.png']}
dest=pub/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for f in {s['file'] for s in c['shots']}:shutil.copy(d/f,dest/f)
(r/'sifirdan-002.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(r/'sifirdan-002.jsx').write_text((r/'viral-sirali-001.jsx').read_text().replace('viral-sirali-001.json','sifirdan-002.json'))
im=ImageOps.fit(Image.open(d/'sahne-3.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im,'RGBA');g.rounded_rectangle((30,95,1050,735),radius=36,fill=(8,8,8,232),outline='white',width=6)
for i,text in enumerate(['TEMİZ HALI','GERÇEKTEN','TEMİZ Mİ?']):
 if i==2:g.rounded_rectangle((55,500,1025,695),radius=20,fill=(255,222,40,255),outline='black',width=5)
 for sz in range(130,40,-1):
  font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',sz);box=g.textbbox((0,0),text,font=font,stroke_width=2)
  if box[2]-box[0]<(880 if i==2 else 930):break
 g.text(((1080-(box[2]-box[0]))/2,[155,310,520][i]),text,font=font,fill='black' if i==2 else 'white',stroke_width=2,stroke_fill='black')
im.save(d/'VID-002-img-1.jpg',quality=93);im.resize((180,320)).save('/tmp/sifirdan-002-cover.jpg');print(frames)
