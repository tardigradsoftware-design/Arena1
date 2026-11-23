from pathlib import Path
import json,math,shutil,wave
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).resolve().parents[3];rem=root/'production/remotion';d=root/'production/sifirdan-yeni/VID-050';b=37.8
caption='Fırında bütün tavuk veya baget pişirdiğinizde derisi çıtır çıtır olmak yerine soluk ve lastik gibi yumuşak kalıyorsa, üzerine salçalı sulu sos sürme hatasını bırakın! Tavuğu fırına vermeden önce kağıt havluyla dış derisini kupkuru olacak şekilde kurulayın; ardından bir çay kaşığı kabartma tozu, tuz ve yarım çay kaşığı balı çok az zeytinyağıyla karıştırıp derisine sürün. Kabartma tozu derideki nemi çekip mikro kabarcıklar oluşturarak tavuğun tıpkı çevirme tavuk gibi nar gibi kızarmasını ve cips gibi çıtır olmasını sağlar. Tariflerin için hemen kaydet ve beğen!'
with wave.open(str(d/'anlatim.wav')) as w:dur=w.getnframes()/w.getframerate()
c=json.loads((rem/'bastan-024.json').read_text());c.update(id='050',dir='yeniliste-bastan050',frames=math.ceil((b/1.55+(dur-b)/1.62+.4)*30),tempoBoundary=b,captionEnd=b/1.55,ctaStart=round(b/1.55*30),caption=caption,safeCaptions=True,hook=['TAVUĞUN DERİSİ','NASIL ÇITIR OLUR?'],openIcon='drop',ctaStackFrames=[round((b/1.55+(dur-b-off)/1.62)*30) for off in [2.65,1.95,1.25,.55]],shots=[{'from':a,'file':f'sahne-{n}.png','captionTop':1510} for a,n in [(0,4),(48,1),(210,1),(300,2),(435,2),(550,3),(650,4)]],events=[{'from':a,'to':z,'a':t,'b':u,'icon':icon,'side':side,'y':330} for a,z,t,u,icon,side in [(235,280,'KURU','DERİ','shine','left'),(365,410,'KABARTMA','TOZU','shine','right')]],highlight={'file':'sahne-1.png','from':65,'to':110,'path':'M160 510 C200 455 300 430 400 465 C480 490 530 555 520 630 C510 700 460 745 370 750 C280 755 195 720 165 660 C145 610 145 550 160 510'})
dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for shot in c['shots']:shutil.copyfile(d/shot['file'],dest/shot['file'])
(rem/'bastan-050.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(rem/'bastan-050.jsx').write_text((rem/'bastan-024.jsx').read_text().replace('bastan-024.json','bastan-050.json'))
im=ImageOps.fit(Image.open(d/'sahne-4.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((45,120,1035,420),radius=30,fill='#131e1c',outline='white',width=5)
for j,line in enumerate(['TAVUĞUN DERİSİ','NASIL ÇITIR OLUR?']):g.text((540,205+j*125),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',50),fill='#ffe135' if j==0 else 'white',anchor='mm')
im.save(d/'VID-050-img-1.jpg',quality=92)
