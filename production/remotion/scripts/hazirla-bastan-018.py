from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import json, math, shutil, wave
root=Path(__file__).resolve().parents[3]; rem=root/'production/remotion'; d=root/'production/sifirdan-yeni/VID-018'
c=json.loads((rem/'bastan-017.json').read_text()); b=31.5
with wave.open(str(d/'anlatim.wav')) as w: dur=w.getnframes()/w.getframerate()
cta=round(b/1.55*30)
c.update(id='018',dir='bastan018',frames=math.ceil((b/1.55+(dur-b)/1.62+.3)*30),tempoBoundary=b,captionEnd=b/1.55,ctaStart=cta,caption='Aldığınız süzme balın gerçek arı balı mı yoksa glikoz şurubu mu olduğunu anlamak için balı yakmanıza gerek yok, soğuk su testiyle beş saniyede gerçeği görün! Düz beyaz bir tabağın ortasına bir tatlı kaşığı bal koyun, üzerine yarım çay bardağı soğuk çeşme suyu dökün ve tabağı elinizde dairesel olarak hafifçe sallayın. Gerçek bal soğuk suda hemen erimez ve genetik hafızası sayesinde saniyeler içinde altıgen arı peteği deseni oluşturur; sahte şekerli bal ise suya değdiği an dağılıp erir.',hook=['BAL VE SOĞUK SU','BU TEST NE GÖSTERİR?'],openIcon='bowl',ctaStackFrames=[round((b/1.55+(x-b)/1.62)*30) for x in [33.7,34.4,35.1,35.8]],shots=[{'from':f,'file':name} for f,name in [(0,'sahne-1.png'),(45,'sahne-2.png'),(115,'sahne-1.png'),(200,'sahne-2.png'),(270,'sahne-3.png'),(340,'sahne-4.png'),(445,'sahne-3.png')]],events=[{'from':210,'to':255,'a':'BİR KAŞIK','b':'BAL','icon':'spoon','side':'left','y':330},{'from':280,'to':325,'a':'SOĞUK','b':'SU','icon':'bowl','side':'right','y':330}])
dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for s in c['shots']: shutil.copyfile(d/s['file'],dest/s['file'])
(rem/'bastan-018.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
(rem/'bastan-018.jsx').write_text((rem/'bastan-017.jsx').read_text().replace('bastan-017.json','bastan-018.json'))
im=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((45,120,1035,470),radius=30,fill='#131e1c',outline='white',width=5)
for j,line in enumerate(['BAL VE SOĞUK SU','BU TEST NE GÖSTERİR?']):
 font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',60);g.text((540,225+j*135),line,font=font,fill='#ffe135' if j==0 else 'white',anchor='mm')
im.save(d/'VID-018-img-1.jpg',quality=92)
