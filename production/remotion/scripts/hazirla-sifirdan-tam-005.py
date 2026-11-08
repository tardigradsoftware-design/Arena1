#!/usr/bin/env python3
from pathlib import Path
import math,wave,json,shutil
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).resolve().parents[3];p=root/'production';r=p/'remotion';d=p/'sifirdan-tam/VID-005';c=json.loads((r/'viral-sirali-005.json').read_text())
with wave.open(str(d/'anlatim.wav')) as f:c['frames']=math.ceil((f.getnframes()/f.getframerate()/1.55+.2)*30)
c.update(dir='yenilisteTam005',captionEnd=20.7,ctaStart=622,ctaHeading='BU FİKRİ PAYLAŞ',ctaItems=[['KAYDET','save'],['PAYLAŞ','share']],shots=[{'from':t,'file':name} for t,name in [(0,'sahne-1.png'),(45,'sahne-2.png'),(110,'sahne-1.png'),(190,'sahne-2.png'),(325,'sahne-3.png'),(470,'sahne-3.png')]],representativeFiles=['sahne-1.png','sahne-2.png','sahne-3.png'])
c['events']=[dict(zip(('from','to','a','b','icon','side','y'),v)) for v in [(105,145,'KABLO','UCU','cable','right',320),(220,265,'KALEMİN','YAYI','springwire','left',320),(355,400,'KABLOYA','SAR','hand','right',320),(480,525,'UÇ','BÖLGESİ','cable','left',320)]]
dest=r/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for f in {s['file'] for s in c['shots']}:shutil.copy(d/f,dest/f)
(r/'sifirdan-tam-005.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(r/'sifirdan-tam-005.jsx').write_text((r/'sifirdan-tam-004.jsx').read_text().replace('sifirdan-tam-004.json','sifirdan-tam-005.json'))
im=ImageOps.fit(Image.open(d/'sahne-3.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im,'RGBA');g.rounded_rectangle((30,95,1050,735),radius=36,fill=(8,8,8,232),outline='white',width=6)
for i,text in enumerate(['ŞARJ KABLOSU','KOPMASIN!','BU YAY NE İŞE YARAR?']):
 if i==2:g.rounded_rectangle((55,500,1025,695),radius=20,fill=(255,222,40,255),outline='black',width=5)
 for sz in range(130,40,-1):
  font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',sz);box=g.textbbox((0,0),text,font=font,stroke_width=2)
  if box[2]-box[0]<(880 if i==2 else 930):break
 g.text(((1080-(box[2]-box[0]))/2,[155,310,520][i]),text,font=font,fill='black' if i==2 else 'white',stroke_width=2,stroke_fill='black')
im.save(d/'VID-005-img-1.jpg',quality=93);im.resize((180,320)).save('/tmp/sifirdantam005-cover.jpg');print(c['frames'])
