from pathlib import Path
import json, math, shutil, wave
from PIL import Image, ImageDraw, ImageFont, ImageOps
root=Path(__file__).resolve().parents[3]; rem=root/'production/remotion'; d=root/'production/sifirdan-yeni/VID-057'; b=32.3
caption='Yemek yaparken sarımsakları tek tek bıçakla soymakla uğraşıp parmaklarınıza günlerce çıkmayan sarımsak kokusu sinmesine son verin! Bütün sarımsağı elinizle dişlerine ayırıp derin bir cam kavanoza atın, üzerine biraz ılık su ekleyip kapağını kapatın ve on saniye boyunca kuvvetlice çalkalayın. Suyun içine döktüğünüzde tüm kabukların kendiliğinden soyulup yüzeye çıktığını, sarımsakların ise tertemiz dibe çöktüğünü göreceksiniz. Mutfakta hız kazandıran bu sırrı hemen kaydet!'
with wave.open(str(d/'anlatim.wav')) as w: dur=w.getnframes()/w.getframerate()
c=json.loads((rem/'bastan-024.json').read_text()); c.update(id='057',dir='yeniliste-bastan057',frames=math.ceil((b/1.55+(dur-b)/1.62+.4)*30),tempoBoundary=b,captionEnd=b/1.55,ctaStart=round(b/1.55*30),caption=caption,safeCaptions=True,hook=['SARIMSAK NASIL','KOLAY SOYULUR?'],openIcon='drop',ctaStackFrames=[round((b/1.55+(dur-b-off)/1.62)*30) for off in [2.65,1.95,1.25,.55]],shots=[{'from':a,'file':f'sahne-{n}.png','captionTop':1510} for a,n in [(0,1),(48,2),(195,2),(265,3),(330,4),(405,5),(500,6)]],events=[{'from':a,'to':z,'a':t,'b':u,'icon':icon,'side':side,'y':330} for a,z,t,u,icon,side in [(270,310,'BİRAZ','ILIK SU','drop','left'),(345,390,'10 SANİYE','ÇALKALA','clock','left')]],highlight={'file':'sahne-1.png','from':8,'to':44,'path':'M125 760 C125 695 170 665 225 665 C290 665 320 710 320 780 C320 845 280 890 220 890 C160 890 125 850 125 800 Z'})
dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for shot in c['shots']: shutil.copyfile(d/shot['file'],dest/shot['file'])
(rem/'bastan-057.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n'); (rem/'bastan-057.jsx').write_text((rem/'bastan-024.jsx').read_text().replace('bastan-024.json','bastan-057.json'))
im=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((45,120,1035,420),radius=30,fill='#131e1c',outline='white',width=5)
for j,line in enumerate(['SARIMSAK NASIL','KOLAY SOYULUR?']):g.text((540,205+j*125),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',54),fill='#ffe135' if j==0 else 'white',anchor='mm')
im.save(d/'VID-057-img-1.jpg',quality=92)
