from pathlib import Path
import json, math, shutil, wave
from PIL import Image, ImageDraw, ImageFont, ImageOps
root=Path(__file__).resolve().parents[3]; rem=root/'production/remotion'; d=root/'production/sifirdan-yeni/VID-053'; b=26.7
caption='Duşakabin camlarında biriken o mat beyaz kireç ve sabun kalıntılarını çıkarmak için her hafta fırçayla kollarınızı yormayın! Süngerin üzerine bir tatlı kaşığı bulaşık makinesi parlatıcısı ve birkaç damla bulaşık deterjanı döküp camı silin, ardından suyla durulayın. Parlatıcı camda su kaydırıcı bir kalkan oluşturur. Temizlik gününde denemek için kaydet; senin duşakabin için kullandığın özel bir yöntem varsa yorumlara yaz!'
with wave.open(str(d/'anlatim.wav')) as w: dur=w.getnframes()/w.getframerate()
c=json.loads((rem/'bastan-024.json').read_text()); c.update(id='053',dir='yeniliste-bastan053',frames=math.ceil((b/1.55+(dur-b)/1.62+.4)*30),tempoBoundary=b,captionEnd=b/1.55,ctaStart=round(b/1.55*30),caption=caption,safeCaptions=True,hook=['DUŞ CAMINDAKİ LEKELER','NASIL TEMİZLENİR?'],openIcon='drop',ctaStackFrames=[round((b/1.55+(dur-b-off)/1.62)*30) for off in [2.65,1.95,1.25,.55]],shots=[{'from':a,'file':f'sahne-{n}.png','captionTop':1510} for a,n in [(0,1),(48,2),(160,2),(255,3),(335,4),(405,5)]],events=[{'from':a,'to':z,'a':t,'b':u,'icon':icon,'side':side,'y':330} for a,z,t,u,icon,side in [(165,210,'BİR TATLI KAŞIĞI','PARLATICI','drop','right'),(338,380,'SUYLA','DURULAYIN','drop','left')]],highlight={'file':'sahne-1.png','from':8,'to':44,'path':'M205 340 C210 270 290 230 350 260 C410 290 420 390 390 470 C360 540 270 550 225 500 C195 460 190 395 205 340'})
dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for shot in c['shots']: shutil.copyfile(d/shot['file'],dest/shot['file'])
(rem/'bastan-053.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n'); (rem/'bastan-053.jsx').write_text((rem/'bastan-024.jsx').read_text().replace('bastan-024.json','bastan-053.json'))
im=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920)); g=ImageDraw.Draw(im);g.rounded_rectangle((45,120,1035,420),radius=30,fill='#131e1c',outline='white',width=5)
for j,line in enumerate(['DUŞ CAMINDAKİ LEKELER','NASIL TEMİZLENİR?']):g.text((540,205+j*125),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',49),fill='#ffe135' if j==0 else 'white',anchor='mm')
im.save(d/'VID-053-img-1.jpg',quality=92)
