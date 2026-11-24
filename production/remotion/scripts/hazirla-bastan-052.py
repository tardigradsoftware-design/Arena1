from pathlib import Path
import json,math,shutil,wave
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).resolve().parents[3];rem=root/'production/remotion';d=root/'production/sifirdan-yeni/VID-052';b=37.8
caption='Buzdolabının, çamaşır makinesinin veya alçak bazaların altındaki o iki parmaklık dar boşluğa süpürge başlığı girmediği için biriken yıllanmış toz yumaklarını eşyayı çekmeden beş saniyede alın! Uzun bir oklavanın, süpürge sapının veya cetvelin ucuna kullanmadığınız ince bir naylon külotlu çorabı geçirip paket lastiğiyle sabitleyin ve o dar boşluğa sokup ileri geri gezdirin. Naylon çorabın oluşturduğu güçlü statik elektrik, en arkadaki tozları ve tüyleri bile mıknatıs gibi kendine çekip tek seferde dışarı çıkaracaktır. Temizlik için hemen kaydet ve beğen!'
with wave.open(str(d/'anlatim.wav')) as w:dur=w.getnframes()/w.getframerate()
c=json.loads((rem/'bastan-024.json').read_text());c.update(id='052',dir='yeniliste-bastan052',frames=math.ceil((b/1.55+(dur-b)/1.62+.4)*30),tempoBoundary=b,captionEnd=b/1.55,ctaStart=round(b/1.55*30),caption=caption,safeCaptions=True,hook=['DOLAP ALTINDAKİ TOZ','NASIL ÇIKAR?'],openIcon='wipe',ctaStackFrames=[round((b/1.55+(dur-b-off)/1.62)*30) for off in [2.65,1.95,1.25,.55]],shots=[{'from':a,'file':'sahne-3b.png' if n==3 else f'sahne-{n}.png','captionTop':1510} for a,n in [(0,1),(48,2),(190,2),(300,2),(405,3),(510,3),(600,4)]],events=[{'from':a,'to':z,'a':t,'b':u,'icon':icon,'side':side,'y':330} for a,z,t,u,icon,side in [(210,255,'NAYLON','ÇORAP','foot','right'),(440,485,'DAR','BOŞLUK','wipe','left')]],highlight={'file':'sahne-1.png','from':8,'to':45,'path':'M170 680 C190 650 260 640 340 650 C410 655 460 680 475 720 C485 760 440 785 370 790 C290 795 210 780 180 755 C155 735 155 705 170 680'})
dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for shot in c['shots']:shutil.copyfile(d/shot['file'],dest/shot['file'])
(rem/'bastan-052.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(rem/'bastan-052.jsx').write_text((rem/'bastan-024.jsx').read_text().replace('bastan-024.json','bastan-052.json'))
im=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((45,120,1035,420),radius=30,fill='#131e1c',outline='white',width=5)
for j,line in enumerate(['DOLAP ALTINDAKİ TOZ','NASIL ÇIKAR?']):g.text((540,205+j*125),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',50),fill='#ffe135' if j==0 else 'white',anchor='mm')
im.save(d/'VID-052-img-1.jpg',quality=92)
