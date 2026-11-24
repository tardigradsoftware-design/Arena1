from pathlib import Path
import json,math,shutil,wave
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).resolve().parents[3];rem=root/'production/remotion';d=root/'production/sifirdan-yeni/VID-051';b=35.3
caption='Duvarınızdaki bir tabloyu veya saati söktüğünüzde geriye kalan o çirkin siyah çivi ve dübel deliklerini kapatmak için nalburdan alçı alıp uğraşmanıza hiç gerek yok! Parmağınızın ucuna biraz düz beyaz diş macunu alın, eğer delik genişse içine bir adet ezilmiş beyaz aspirin tozu karıştırıp sertleştirin, ve doğrudan duvardaki deliğin içine bastırarak doldurun. Üzerini bir kredi kartı veya ıslak mendille duvara sıfır olacak şekilde sıyırdığınızda, kuruduktan sonra alçıdan farksız ve bembeyaz olduğunu göreceksiniz. Ev düzeni için hemen kaydet ve beğen!'
with wave.open(str(d/'anlatim.wav')) as w:dur=w.getnframes()/w.getframerate()
c=json.loads((rem/'bastan-024.json').read_text());c.update(id='051',dir='yeniliste-bastan051',frames=math.ceil((b/1.55+(dur-b)/1.62+.4)*30),tempoBoundary=b,captionEnd=b/1.55,ctaStart=round(b/1.55*30),caption=caption,safeCaptions=True,hook=['DUVARDAKİ DELİK','NASIL KAPANIR?'],openIcon='wipe',ctaStackFrames=[round((b/1.55+(dur-b-off)/1.62)*30) for off in [2.65,1.95,1.25,.55]],shots=[{'from':a,'file':f'sahne-{n}.png','captionTop':1510} for a,n in [(0,1),(48,2),(180,2),(285,2),(390,3),(480,4),(580,5)]],events=[{'from':a,'to':z,'a':t,'b':u,'icon':icon,'side':side,'y':330} for a,z,t,u,icon,side in [(170,220,'BEYAZ','MACUN','soap','right'),(490,535,'KARTLA','DÜZLE','wipe','left')]],highlight={'file':'sahne-1.png','from':8,'to':45,'path':'M310 600 C330 575 370 565 405 575 C445 585 465 615 465 650 C465 685 445 710 410 720 C370 730 330 720 310 695 C290 675 290 630 310 600'})
dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for shot in c['shots']:shutil.copyfile(d/shot['file'],dest/shot['file'])
(rem/'bastan-051.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(rem/'bastan-051.jsx').write_text((rem/'bastan-024.jsx').read_text().replace('bastan-024.json','bastan-051.json'))
im=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((45,120,1035,420),radius=30,fill='#131e1c',outline='white',width=5)
for j,line in enumerate(['DUVARDAKİ DELİK','NASIL KAPANIR?']):g.text((540,205+j*125),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',50),fill='#ffe135' if j==0 else 'white',anchor='mm')
im.save(d/'VID-051-img-1.jpg',quality=92)
