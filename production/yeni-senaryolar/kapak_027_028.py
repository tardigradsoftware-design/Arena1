from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).parent;font='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
for id,lines in [('027',('SÜREKLİ ÖZÜR','YERİNE','NE DENEBİLİR?')),('028',('UYUMADAN ÖNCE','LAVANTA','NE YAPAR?'))]:
 p=root/f'VID-{id}';im=ImageOps.fit(Image.open(p/'sahne-1.png').convert('RGB'),(1080,1920));d=ImageDraw.Draw(im,'RGBA');d.rounded_rectangle((30,95,1050,735),radius=36,fill=(8,8,8,232),outline='white',width=6)
 for i,text in enumerate(lines):
  if i==2:d.rounded_rectangle((75,500,1005,695),radius=20,fill=(255,222,40,255),outline='black',width=5)
  for sz in range(135,40,-1):
   f=ImageFont.truetype(font,sz);box=d.textbbox((0,0),text,font=f,stroke_width=2)
   if box[2]-box[0]<(820 if i==2 else 930):break
  d.text(((1080-(box[2]-box[0]))/2,[155,310,500][i]),text,font=f,fill='black' if i==2 else 'white',stroke_width=2,stroke_fill='black')
 im.save(p/f'VID-{id}-img-1.jpg',quality=93);im.resize((180,320)).save(f'/tmp/kapak-{id}-kucuk.jpg')
