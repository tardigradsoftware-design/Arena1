from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import json, math, shutil, wave
root=Path(__file__).resolve().parents[3]; rem=root/'production/remotion'; d=root/'production/sifirdan-yeni/VID-016'
c=json.loads((rem/'bastan-012.json').read_text())
b=33.9
with wave.open(str(d/'anlatim.wav')) as w: dur=w.getnframes()/w.getframerate()
cta=round(b/1.55*30)
c.update(id='016',dir='bastan016',frames=math.ceil((b/1.55+(dur-b)/1.62+.3)*30),tempoBoundary=b,captionEnd=b/1.55,ctaStart=cta,caption='Mutfak dolaplarınızın tepesine ve aspiratörün üzerine yapışıp tozla birleşerek zamk gibi sertleşen o sarı yağ tabakasını çıkarmak için ağır kimyasallarla dolaplarınızı aşındırmayın! Kimyada altın kuraldır: Yağı en hızlı yine yağ çözer. İki yemek kaşığı karbonatın içine bir yemek kaşığı bildiğimiz ayçiçek yağı döküp macun yapın ve bu karışımı süngerle yapışkan dolap yüzeyine sürün. Asla çıkmayan o taşlaşmış yağların saniyeler içinde eriyip kendiliğinden kalktığını göreceksiniz, ardından sabunlu bezle silip geçin.',hook=['YAPIŞKAN YAĞ','NASIL TEMİZLENİR?'],openIcon='wipe',warning='',ctaStackFrames=[round((b/1.55+(x-b)/1.62)*30) for x in [36.3,37.0,37.7,38.4]],shots=[{'from':f,'file':name} for f,name in [(0,'sahne-1.png'),(45,'sahne-3.png'),(100,'sahne-1.png'),(245,'sahne-2.png'),(420,'sahne-3.png'),(575,'sahne-5.png')]],events=[{'from':250,'to':300,'a':'KARBONAT','b':'VE YAĞ','icon':'bowl','side':'left','y':330},{'from':425,'to':470,'a':'KARIŞIMI','b':'UYGULA','icon':'wipe','side':'right','y':330}])
c.pop('highlight',None)
dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for s in c['shots']: shutil.copyfile(d/s['file'],dest/s['file'])
(rem/'bastan-016.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
(rem/'bastan-016.jsx').write_text((rem/'bastan-012.jsx').read_text().replace('bastan-012.json','bastan-016.json'))
im=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((45,120,1035,470),radius=30,fill='#131e1c',outline='white',width=5)
for j,line in enumerate(['YAPIŞKAN YAĞ','NASIL ÇIKAR?']):g.text((540,225+j*135),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',75),fill='#ffe135' if j==0 else 'white',anchor='mm')
im.save(d/'VID-016-img-1.jpg',quality=92)
