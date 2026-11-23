from pathlib import Path
import json,math,shutil,wave
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).resolve().parents[3];rem=root/'production/remotion';d=root/'production/sifirdan-yeni/VID-049';b=34.5
caption='Montunuzun, çizmenizin veya en sevdiğiniz çantanızın fermuarı sıkışıp yarıda kaldığında zorlayarak çekip fermuar başlığını elinizde bırakmayın! Evdeki bildiğimiz siyah uçlu bir kurşun kalemi alın ve kalemin ucunu fermuarın takıldığı yerdeki dişlerin üzerine ileri geri sürterek boyayın. Kurşun kalemin içindeki saf grafit maddesi dünyadaki en güçlü kuru yağlayıcıdır ve kumaşta asla yağ lekesi bırakmaz. Fermuarı çektiğiniz an yağ gibi kayıp açıldığını göreceksiniz. Bu kurtarıcı bilgiyi hemen kaydet, beğen ve arkadaşına gönder!'
with wave.open(str(d/'anlatim.wav')) as w:dur=w.getnframes()/w.getframerate()
c=json.loads((rem/'bastan-024.json').read_text());c.update(id='049',dir='yeniliste-bastan049',frames=math.ceil((b/1.55+(dur-b)/1.62+.4)*30),tempoBoundary=b,captionEnd=b/1.55,ctaStart=round(b/1.55*30),caption=caption,safeCaptions=True,hook=['SIKIŞAN FERMUAR','NASIL AÇILIR?'],openIcon='drop',ctaStackFrames=[round((b/1.55+(dur-b-off)/1.62)*30) for off in [2.65,1.95,1.25,.55]],shots=[{'from':a,'file':'sahne-3b.png' if n==3 else f'sahne-{n}.png','captionTop':1510} for a,n in [(0,1),(48,1),(175,2),(270,2),(370,2),(490,3),(580,4)]],events=[{'from':a,'to':z,'a':t,'b':u,'icon':icon,'side':side,'y':330} for a,z,t,u,icon,side in [(195,240,'KURŞUN','KALEM','shine','right'),(380,425,'GRAFİT','UÇ','shine','left')]],highlight={'file':'sahne-1.png','from':55,'to':100,'path':'M260 450 C280 410 360 390 430 410 C490 430 500 490 490 550 C480 610 410 630 350 620 C300 610 260 580 250 530 C245 500 245 470 260 450'})
dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for shot in c['shots']:shutil.copyfile(d/shot['file'],dest/shot['file'])
(rem/'bastan-049.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(rem/'bastan-049.jsx').write_text((rem/'bastan-024.jsx').read_text().replace('bastan-024.json','bastan-049.json'))
im=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((45,120,1035,420),radius=30,fill='#131e1c',outline='white',width=5)
for j,line in enumerate(['SIKIŞAN FERMUAR','NASIL AÇILIR?']):g.text((540,205+j*125),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',50),fill='#ffe135' if j==0 else 'white',anchor='mm')
im.save(d/'VID-049-img-1.jpg',quality=92)
