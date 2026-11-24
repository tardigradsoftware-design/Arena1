from pathlib import Path
import json, math, shutil, wave
from PIL import Image, ImageDraw, ImageFont, ImageOps
root=Path(__file__).resolve().parents[3]; rem=root/'production/remotion'; d=root/'production/sifirdan-yeni/VID-054'; b=35.1
caption='Açık renk halınızın üzerine çay veya kahve döküldüğünde bezle bastırarak ovalarsanız lekeyi halının en alt ipliklerine kadar hapsedersiniz! Döküldüğü ilk saniyede kuru bir kağıt havluyla hiç ovalamadan sadece tampon yaparak sıvıyı çektirin; ardından lekenin üzerine yarım şişe sade maden suyu döküp bir yemek kaşığı karbonat serpin. Maden suyunun kabarcıkları ve karbonat lekeyi halının dibinden köpürterek yüzeye çıkaracak, temiz bezle sildiğinizde iz bile kalmayacaktır. Acil durumlar için hemen kaydet, beğen ve arkadaşına gönder!'
with wave.open(str(d/'anlatim.wav')) as w: dur=w.getnframes()/w.getframerate()
c=json.loads((rem/'bastan-024.json').read_text()); c.update(id='054',dir='yeniliste-bastan054',frames=math.ceil((b/1.55+(dur-b)/1.62+.4)*30),tempoBoundary=b,captionEnd=b/1.55,ctaStart=round(b/1.55*30),caption=caption,safeCaptions=True,hook=['HALIDAKİ KAHVE LEKESİ','NASIL ÇIKAR?'],openIcon='drop',ctaStackFrames=[round((b/1.55+(dur-b-off)/1.62)*30) for off in [2.65,1.95,1.25,.55]],shots=[{'from':a,'file':f'sahne-{n}.png','captionTop':1510} for a,n in [(0,0),(48,1),(190,2),(310,3),(405,4),(565,5)]],events=[{'from':a,'to':z,'a':t,'b':u,'icon':icon,'side':side,'y':330} for a,z,t,u,icon,side in [(192,235,'OVALAMADAN','TAMPON YAP','wipe','left'),(319,360,'SADE','MADEN SUYU','drop','right'),(410,453,'BİR YEMEK KAŞIĞI','KARBONAT','spoon','left')]],highlight={'file':'sahne-0.png','from':8,'to':44,'path':'M115 765 C150 705 270 675 400 675 C530 665 670 710 680 775 C685 850 610 930 490 960 C360 990 210 950 140 900 C100 870 85 815 115 765'})
dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for shot in c['shots']: shutil.copyfile(d/shot['file'],dest/shot['file'])
(rem/'bastan-054.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n'); (rem/'bastan-054.jsx').write_text((rem/'bastan-024.jsx').read_text().replace('bastan-024.json','bastan-054.json'))
im=ImageOps.fit(Image.open(d/'sahne-0.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((45,120,1035,420),radius=30,fill='#131e1c',outline='white',width=5)
for j,line in enumerate(['HALIDAKİ KAHVE LEKESİ','NASIL ÇIKAR?']):g.text((540,205+j*125),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',49),fill='#ffe135' if j==0 else 'white',anchor='mm')
im.save(d/'VID-054-img-1.jpg',quality=92)
