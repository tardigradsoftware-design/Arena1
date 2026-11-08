#!/usr/bin/env python3
from pathlib import Path
import json,math,wave,shutil
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).resolve().parents[3];p=root/'production';r=p/'remotion'
c=json.loads((r/'sifirdan-003.json').read_text());c['captionEnd']=19.7;c['ctaStart']=594;c['ctaHeading']='SONUCUNU PAYLAŞ';c['ctaItems']=[['KAYDET','save'],['YORUM YAP','talk']];c['events'][-1]['from']=565;c['events'][-1]['to']=590;c['shots'][-1]['from']=550
cfg={'003':c,'004':{'id':'004','dir':'yenilisteTam004','brand':True,'caption':'Beyaz spor ayakkabılarınızın lastik taban kenarları ne kadar silerseniz silin sararıyor ve siyah çizgiler çıkmıyorsa çamaşır suyu sürüp lastiği eritmeyin! Bir tatlı kaşığı beyazlatıcı diş macunu, bir tatlı kaşığı karbonat ve birkaç damla bulaşık deterjanını karıştırıp eski bir diş fırçasıyla tabanları fırçalayın. Sildiğiniz an ayakkabılarınız kutusundan yeni çıkmış gibi kar beyazı olacaktır.', 'captionEnd':16.95,'ctaStart':510,'ctaTop':300,'ctaHeading':'SONUCUNU PAYLAŞ','ctaItems':[['KAYDET','save'],['YORUM YAP','talk']],'hook':['SARARAN TABAN','NASIL BEYAZLAR?'],'openIcon':'shoe','shots':[{'from':x,'file':name} for x,name in [(0,'sahne-1.png'),(45,'sahne-2.png'),(110,'sahne-1.png'),(190,'sahne-2.png'),(290,'sahne-3.png'),(440,'sahne-4.png')]],'events':[dict(zip(('from','to','a','b','icon','side','y'),v)) for v in [(105,145,'SARARAN','TABAN','shoe','right',320),(205,245,'DİŞ MACUNU','KARBONAT','brush','left',320),(320,365,'FIRÇAYLA','TEMİZLE','brush','right',320),(450,490,'BEYAZ','TABAN','shoe','left',320)]], 'representativeFiles':['sahne-1.png','sahne-2.png','sahne-3.png','sahne-4.png']}}
for id,c in cfg.items():
 d=p/f'sifirdan-tam/VID-{id}'
 with wave.open(str(d/'anlatim.wav')) as f:c['frames']=math.ceil((f.getnframes()/f.getframerate()/1.55+.2)*30)
 dest=r/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True);source=(p/f'sifirdan/VID-{id}') if id=='003' else d
 for f in {s['file'] for s in c['shots']}:shutil.copy(source/f,dest/f)
 (r/f'sifirdan-tam-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(r/f'sifirdan-tam-{id}.jsx').write_text((r/'sifirdan-tam-001.jsx').read_text().replace('sifirdan-tam-001.json',f'sifirdan-tam-{id}.json'));print(id,c['frames'])
 if id=='004':
  im=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im,'RGBA');g.rounded_rectangle((30,95,1050,735),radius=36,fill=(8,8,8,232),outline='white',width=6)
  for i,text in enumerate(['SARARAN','TABANLAR','NASIL BEYAZLAR?']):
   if i==2:g.rounded_rectangle((55,500,1025,695),radius=20,fill=(255,222,40,255),outline='black',width=5)
   for sz in range(130,40,-1):
    font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',sz);box=g.textbbox((0,0),text,font=font,stroke_width=2)
    if box[2]-box[0]<(880 if i==2 else 930):break
   g.text(((1080-(box[2]-box[0]))/2,[155,310,520][i]),text,font=font,fill='black' if i==2 else 'white',stroke_width=2,stroke_fill='black')
  im.save(d/'VID-004-img-1.jpg',quality=93);im.resize((180,320)).save('/tmp/sifirdantam004-cover.jpg')
