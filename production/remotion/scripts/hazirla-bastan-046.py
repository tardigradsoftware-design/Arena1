from pathlib import Path
import json,math,shutil,wave
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).resolve().parents[3];rem=root/'production/remotion';d=root/'production/sifirdan-yeni/VID-046';b=36.7
caption='Tenekeyle veya şişeyle aldığınız sızma zeytinyağının saf zeytinyağı mı yoksa içine ucuz tohum yağı karıştırılmış sahte yağ mı olduğunu evde iki basit testle anlayın! İlk olarak yarım çay bardağı zeytinyağını dondurucuya koyup yarım saat bekletin; hakiki zeytinyağı soğukta donup tereyağı gibi kristalleşir, sıvı kalan kısımlar ise karışımdır. İkinci olarak bir bardak ılık suya bir kaşık yağ döküp çalkalayın; gerçek zeytinyağı halkalar halinde hemen suyun en üstüne çıkar ve dağılmaz. Evdeki yağı test etmek için hemen kaydet, dene ve sonucu yorumlara yaz!'
with wave.open(str(d/'anlatim.wav')) as w:dur=w.getnframes()/w.getframerate()
c=json.loads((rem/'bastan-024.json').read_text());c.update(id='046',dir='yeniliste-bastan046',frames=math.ceil((b/1.55+(dur-b)/1.62+.4)*30),tempoBoundary=b,captionEnd=b/1.55,ctaStart=round(b/1.55*30),caption=caption,safeCaptions=True,hook=['ZEYTİNYAĞINI','NASIL TEST EDERSİN?'],openIcon='drop',ctaStackFrames=[round((b/1.55+(dur-b-off)/1.62)*30) for off in [2.65,1.95,1.25,.55]],shots=[{'from':a,'file':f'sahne-{n}.png','captionTop':1510} for a,n in [(0,1),(48,1),(205,2),(300,3),(400,3),(485,4),(605,5)]],events=[{'from':a,'to':z,'a':t,'b':u,'icon':icon,'side':side,'y':330} for a,z,t,u,icon,side in [(205,260,'30','DAKİKA','clock','left'),(500,550,'SUYA','DÖK','drop','right')]],highlight={'file':'sahne-1.png','from':55,'to':100,'path':'M255 850 C267 806 310 790 382 791 C452 792 493 817 501 860 C515 906 495 942 440 951 C364 964 300 946 273 915 C261 899 254 874 255 850'})
dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for shot in c['shots']:shutil.copyfile(d/shot['file'],dest/shot['file'])
(rem/'bastan-046.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(rem/'bastan-046.jsx').write_text((rem/'bastan-024.jsx').read_text().replace('bastan-024.json','bastan-046.json'))
im=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((45,120,1035,420),radius=30,fill='#131e1c',outline='white',width=5)
for j,line in enumerate(['ZEYTİNYAĞINI','NASIL TEST EDERSİN?']):g.text((540,205+j*125),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',50),fill='#ffe135' if j==0 else 'white',anchor='mm')
im.save(d/'VID-046-img-1.jpg',quality=92)
