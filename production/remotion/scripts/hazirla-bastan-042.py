from pathlib import Path
import json,math,shutil,wave
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).resolve().parents[3]; rem=root/'production/remotion'; id='042';d=root/'production/sifirdan-yeni/VID-042';b=38.8
caption='En sevdiğiniz kot pantolonunuzun fermuarı yürüdükçe veya oturdukça kendiliğinden aşağı kayıyorsa ve sürekli kontrol etmek zorunda kalıyorsanız pantolonu terziye götürmenize gerek yok! Evdeki eski bir anahtarlığın ucundaki o küçük yuvarlak metal halkayı çıkarın ve pantolon fermuarınızın tutma deliğine geçirin. Fermuarı yukarı çektikten sonra metal halkayı pantolonun bel düğmesine ilikler gibi takıp düğmeyi öyle kapatın. Halka düğmenin altında tamamen gizlenecek ve fermuarınızın bir milim bile aşağı kayması imkansız olacaktır. Bu hayat kurtaran hileyi hemen kaydet ve paylaş!'
with wave.open(str(d/'anlatim.wav')) as w:dur=w.getnframes()/w.getframerate()
c=json.loads((rem/'bastan-024.json').read_text()); c.update(id=id,dir='yeniliste-bastan042',frames=math.ceil((b/1.55+(dur-b)/1.62+.4)*30),tempoBoundary=b,captionEnd=b/1.55,ctaStart=round(b/1.55*30),caption=caption,hook=['KAYAN FERMUAR','NASIL SABİTLENİR?'],openIcon='lock',ctaStackFrames=[round((b/1.55+(dur-b-off)/1.62)*30) for off in [2.65,1.95,1.25,.55]],shots=[{'from':a,'file':f'sahne-{n}.png'} for a,n in [(0,'1'),(45,'2b'),(100,'1'),(240,'2b'),(360,'3c'),(495,'3c'),(610,'4')]],events=[{'from':a,'to':z,'a':t,'b':u,'icon':icon,'side':side,'y':330} for a,z,t,u,icon,side in [(250,300,'METAL','HALKA','ring','right'),(390,440,'DÜĞMEYE','GEÇİR','lock','left')]],highlight={'file':'sahne-3c.png','from':405,'to':455,'path':'M290 435 C303 414 331 407 359 409 C401 410 445 430 456 467 C469 501 454 546 425 565 C393 583 343 574 315 552 C292 534 280 476 290 435'})
dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for s in c['shots']:shutil.copyfile(d/s['file'],dest/s['file'])
(rem/'bastan-042.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(rem/'bastan-042.jsx').write_text((rem/'bastan-024.jsx').read_text().replace('bastan-024.json','bastan-042.json'))
im=ImageOps.fit(Image.open(d/'sahne-3c.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((45,120,1035,470),radius=30,fill='#131e1c',outline='white',width=5)
for j,line in enumerate(['KAYAN FERMUARI','NASIL SABİTLERSİN?']):g.text((540,225+j*135),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',54),fill='#ffe135' if j==0 else 'white',anchor='mm')
im.save(d/'VID-042-img-1.jpg',quality=92)
