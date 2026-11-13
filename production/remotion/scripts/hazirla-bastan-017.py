from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import json, math, shutil, wave
root=Path(__file__).resolve().parents[3]; rem=root/'production/remotion'; d=root/'production/sifirdan-yeni/VID-017'
c=json.loads((rem/'bastan-016.json').read_text()); b=33.74
with wave.open(str(d/'anlatim.wav')) as w: dur=w.getnframes()/w.getframerate()
cta=round(b/1.55*30)
c.update(id='017',dir='bastan017',frames=math.ceil((b/1.55+(dur-b)/1.62+.3)*30),tempoBoundary=b,captionEnd=b/1.55,ctaStart=cta,caption='Haşladığınız yumurtaları soyarken kabuğun yumurtaya yapışıp beyazının yarısını koparmasına ve şeklinin bozulmasına artık son verin! Yumurtalar haşlanır haşlanmaz sıcak sudan çıkarıp buz gibi soğuk suya atarak iki dakika şoklayın. Ardından yumurtayı bir su bardağının içine koyup yarısına kadar soğuk su ekleyin, elinizle bardağın ağzını kapatıp üç saniye kuvvetlice çalkalayın. Su kabuğun altındaki zara sızacağı için yumurtayı çıkardığınızda kabuğun tek parça halinde elinizde kaldığını göreceksiniz.',hook=['YUMURTA KABUĞU','NASIL SOYULUR?'],openIcon='bowl',ctaStackFrames=[round((b/1.55+(x-b)/1.62)*30) for x in [36.25,37.0,37.7,38.5]],shots=[{'from':f,'file':name} for f,name in [(0,'sahne-1.png'),(45,'sahne-2.png'),(100,'sahne-1.png'),(180,'sahne-2.png'),(310,'sahne-3.png'),(390,'sahne-5.png'),(550,'sahne-4.png')]],events=[{'from':215,'to':265,'a':'BUZLU SU','b':'İKİ DAKİKA','icon':'clock','side':'left','y':330},{'from':410,'to':460,'a':'SU BARDAĞI','b':'ÜÇ SANİYE','icon':'clock','side':'right','y':330}])
dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for s in c['shots']: shutil.copyfile(d/s['file'],dest/s['file'])
(rem/'bastan-017.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
(rem/'bastan-017.jsx').write_text((rem/'bastan-016.jsx').read_text().replace('bastan-016.json','bastan-017.json'))
im=ImageOps.fit(Image.open(d/'sahne-5.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((45,120,1035,470),radius=30,fill='#131e1c',outline='white',width=5)
for j,line in enumerate(['YUMURTA','BARDAKLA SOYULUR MU?']):
 font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',67 if j==0 else 55);g.text((540,225+j*135),line,font=font,fill='#ffe135' if j==0 else 'white',anchor='mm')
im.save(d/'VID-017-img-1.jpg',quality=92)
