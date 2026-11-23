from pathlib import Path
import json,math,shutil,wave
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).resolve().parents[3];rem=root/'production/remotion';d=root/'production/sifirdan-yeni/VID-047';b=30.5
caption='Sıcak duştan çıktığınızda banyo aynasının tamamen buğulanıp hiçbir şey göstermemesine ve elinizle sildiğinizde iz kalmasına son verin! Kuru banyo aynasının yüzeyine bir kalıp kuru beyaz sabunu hafifçe sürün, ardından su değdirmeden sadece kuru bir mikrofiber bezle aynayı parlatana kadar silin. Camda oluşan görünmez gliserin tabakası su buharının tutunmasını bir ay boyunca engelleyecek ve aynanız en sıcak duşta bile net kalacaktır. Banyoda denemek için hemen kaydet ve arkadaşına gönder!'
with wave.open(str(d/'anlatim.wav')) as w:dur=w.getnframes()/w.getframerate()
c=json.loads((rem/'bastan-024.json').read_text());c.update(id='047',dir='yeniliste-bastan047',frames=math.ceil((b/1.55+(dur-b)/1.62+.4)*30),tempoBoundary=b,captionEnd=b/1.55,ctaStart=round(b/1.55*30),caption=caption,safeCaptions=True,hook=['BUĞULANAN AYNA','NASIL NET KALIR?'],openIcon='drop',ctaStackFrames=[round((b/1.55+(dur-b-off)/1.62)*30) for off in [2.65,1.95,1.25,.55]],shots=[{'from':a,'file':f'sahne-{n}.png','captionTop':1510} for a,n in [(0,1),(48,1),(180,2),(260,2),(330,3),(430,3),(510,4)]],events=[{'from':a,'to':z,'a':t,'b':u,'icon':icon,'side':side,'y':330} for a,z,t,u,icon,side in [(190,240,'KURU','SABUN','drop','left'),(360,410,'KURU','BEZ','shine','right')]],highlight={'file':'sahne-1.png','from':55,'to':100,'path':'M220 320 C255 260 340 240 444 250 C530 260 580 310 590 390 C600 460 565 535 510 560 C445 590 300 580 250 540 C205 500 195 390 220 320'})
dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for shot in c['shots']:shutil.copyfile(d/shot['file'],dest/shot['file'])
(rem/'bastan-047.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(rem/'bastan-047.jsx').write_text((rem/'bastan-024.jsx').read_text().replace('bastan-024.json','bastan-047.json'))
im=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((45,120,1035,420),radius=30,fill='#131e1c',outline='white',width=5)
for j,line in enumerate(['BUĞULANAN AYNA','NASIL NET KALIR?']):g.text((540,205+j*125),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',50),fill='#ffe135' if j==0 else 'white',anchor='mm')
im.save(d/'VID-047-img-1.jpg',quality=92)
