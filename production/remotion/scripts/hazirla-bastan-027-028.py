from pathlib import Path
import json, math, shutil, wave
from PIL import Image, ImageDraw, ImageFont, ImageOps
root=Path(__file__).resolve().parents[3]; rem=root/'production/remotion'
items={
'027':dict(boundary=36.6,caption='Çantanızda düşüp tuzla buz olan en sevdiğiniz pudranızı, allığınızı veya göz farınızı dağıldı diye sakın çöpe atmayın, otuz saniyede fabrikadan yeni çıkmış gibi presleyin! Kırılan far veya pudrayı kendi kutusunun içinde kürdanın ucuyla tamamen un haline gelene kadar ezin; üzerine sadece üç dört damla eczane alkolü veya seksen derece kolonya damlatıp bıçak sırtıyla düzleştirin. Üzerine bir parça kağıt havlu koyup madeni bir parayla on saniye sertçe bastırın ve açık bırakıp kurutun; alkol uçacak ve pudranız taş gibi tek parça olacaktır.',hook=['KIRILAN PUDRA','ÇÖPE GİTMESİN'],icon='brush',shots=[(0,1),(45,2),(105,1),(230,2),(360,4),(485,3),(595,5)],events=[(345,390,'BİRKAÇ','DAMLA','drop','right'),(505,550,'ON','SANİYE','clock','left')],cover=['KIRILAN PUDRA','NASIL KURTULUR?']),
'028':dict(boundary=34.75,caption='Evde yoğurduğunuz köfteler pişerken küçülüyor, içi kuru ve lastik gibi sert oluyorsa kıyma harcına yumurta kırmayı hemen bırakın! Yumurta köfteyi sıkılaştırıp sertleştirir. Yarım kilo köfte harcını yoğururken içine yumurta yerine yarım çay bardağı sade maden suyu ve yarım çay kaşığı karbonat ekleyip on dakika yoğurun, ardından buzdolabında yarım saat dinlendirin. Maden suyu ve karbonat etin liflerini pamuk gibi kabartacak, köfteleriniz dışı karamelize içi ise sulu lokanta köftesi gibi pişecektir.',hook=['KÖFTENİN SIRRI','MADEN SUYU MU?'],icon='pan',shots=[(0,3),(45,1),(120,3),(245,1),(355,2),(475,3),(555,4)],events=[(250,300,'MADEN','SUYU','glass','right'),(380,425,'ON','DAKİKA','clock','left')],cover=['KÖFTENİN SIRRI','MADEN SUYU MU?'])}
for id,x in items.items():
 d=root/f'production/sifirdan-yeni/VID-{id}';c=json.loads((rem/'bastan-024.json').read_text());b=x['boundary']
 with wave.open(str(d/'anlatim.wav')) as w:dur=w.getnframes()/w.getframerate()
 c.update(id=id,dir='yeniliste-bastan'+id,frames=math.ceil((b/1.55+(dur-b)/1.62+.4)*30),tempoBoundary=b,captionEnd=b/1.55,ctaStart=round(b/1.55*30),caption=x['caption'],hook=x['hook'],openIcon=x['icon'],ctaStackFrames=[round((b/1.55+(dur-b-off)/1.62)*30) for off in [2.65,1.95,1.25,.55]],shots=[{'from':f,'file':f'sahne-{n}.png'} for f,n in x['shots']],events=[{'from':a,'to':z,'a':t,'b':u,'icon':icon,'side':side,'y':330} for a,z,t,u,icon,side in x['events']])
 c.pop('highlight',None)
 dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
 for s in c['shots']:shutil.copyfile(d/s['file'],dest/s['file'])
 (rem/f'bastan-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(rem/f'bastan-{id}.jsx').write_text((rem/'bastan-024.jsx').read_text().replace('bastan-024.json',f'bastan-{id}.json'))
 im=ImageOps.fit(Image.open(d/('sahne-1.png' if id=='027' else 'sahne-4.png')).convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((45,120,1035,470),radius=30,fill='#131e1c',outline='white',width=5)
 for j,line in enumerate(x['cover']):g.text((540,225+j*135),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',62),fill='#ffe135' if j==0 else 'white',anchor='mm')
 im.save(d/f'VID-{id}-img-1.jpg',quality=92)
