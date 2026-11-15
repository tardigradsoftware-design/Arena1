from pathlib import Path
import json,math,shutil,wave
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).resolve().parents[3]; rem=root/'production/remotion'
items={
'021':dict(boundary=29.9,caption='Pişirdiğiniz et suyunun, çorbanın veya sulu yemeğin yağı fazla kaçtıysa kaşıkla üstünden tek tek yağ toplamaya çalışarak vaktinizi harcamayın! Metal bir çorba kepçesinin içine dört beş adet buz küpü doldurun ve buzlu kepçenin dış alt tabanını sıcak yemeğin yüzeyinde yavaşça gezdirin. Dondurucu soğuk metalle temas eden tüm fazla yağ saniyeler içinde donarak kepçenin altına kalıp gibi yapışacak ve yemeğinizin fazla yağından beş saniyede kurtulacaksınız.',hook=['ÇORBANIN YAĞI','BUZLU KEPÇE'],icon='bowl',shots=[(0,'sahne-1.png'),(45,'yeni-2.png'),(90,'sahne-1.png'),(220,'yeni-2.png'),(355,'yeni-3b.png'),(475,'yeni-4.png')],events=[(185,230,'BUZLU','KEPÇE','bowl','left'),(355,410,'BEŞ','SANİYE','clock','right')],cover=['FAZLA YAĞA','BUZLU KEPÇE']),
'022':dict(boundary=26.5,caption='Aniden misafiriniz geldiğinde soğuk içeceğiniz yoksa şişeyi buzluğa atıp saatlerce soğumasını beklemeyin! Oda sıcaklığındaki içecek şişesinin etrafına bir kat kağıt havlu sarın, kağıt havluyu suyla tamamen ıslatıp üzerine bir yemek kaşığı tuz serpin ve buzlukta sadece beş dakika bekletin. Tuz suyun donma noktasını düşürürken ıslak peçete şişenin ısısını saniyeler içinde emerek içeceğinizi buz gibi yapar.',hook=['İÇECEK SICAK MI?','ISLAK PEÇETE'],icon='drop',shots=[(0,'yeni-1.png'),(45,'sahne-3.png'),(90,'yeni-1.png'),(195,'sahne-2.png'),(295,'sahne-3.png'),(390,'yeni-4b.png'),(490,'yeni-5.png')],events=[(190,235,'ISLAK','PEÇETE','wipe','left'),(310,355,'BEŞ','DAKİKA','clock','right')],cover=['İÇECEK SICAK MI?','ISLAK PEÇETE'])}
for id,x in items.items():
 d=root/f'production/sifirdan-yeni/VID-{id}'; c=json.loads((rem/'bastan-020.json').read_text()); b=x['boundary']
 with wave.open(str(d/'anlatim.wav')) as w: dur=w.getnframes()/w.getframerate()
 c.update(id=id,dir='bastan'+id,frames=math.ceil((b/1.55+(dur-b)/1.62+.3)*30),tempoBoundary=b,captionEnd=b/1.55,ctaStart=round(b/1.55*30),caption=x['caption'],hook=x['hook'],openIcon=x['icon'],ctaStackFrames=[round((b/1.55+(dur-b-off)/1.62)*30) for off in [2.65,1.95,1.25,.55]],shots=[{'from':f,'file':n} for f,n in x['shots']],events=[{'from':a,'to':z,'a':t,'b':u,'icon':icon,'side':side,'y':330} for a,z,t,u,icon,side in x['events']])
 dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
 for shot in c['shots']: shutil.copyfile(d/shot['file'],dest/shot['file'])
 (rem/f'bastan-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
 (rem/f'bastan-{id}.jsx').write_text((rem/'bastan-020.jsx').read_text().replace('bastan-020.json',f'bastan-{id}.json'))
 im=ImageOps.fit(Image.open(d/x['shots'][0][1]).convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((45,120,1035,470),radius=30,fill='#131e1c',outline='white',width=5)
 for j,line in enumerate(x['cover']):g.text((540,225+j*135),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',68),fill='#ffe135' if j==0 else 'white',anchor='mm')
 im.save(d/f'VID-{id}-img-1.jpg',quality=92)
