from pathlib import Path
import json, math, shutil, wave
from PIL import Image, ImageDraw, ImageFont, ImageOps
root=Path(__file__).resolve().parents[3]; rem=root/'production/remotion'
items={
'023': dict(boundary=30.8, caption='Mutfakta bir bardak veya tabak kırıldığında büyük parçaları süpürseniz bile yerde kalan o gözle görülmeyen mikroskobik cam kıymıkları günler sonra ayağınıza batar! Süpürge bu toz camları çekemez. Kırıkların olduğu bölgenin üzerinde bir dilim taze tost ekmeğinin veya bayat ekmeğin yumuşak iç kısmını hafifçe nemlendirip yere bastırarak tampon hareketlerle gezdirin. Ekmeğin süngerimsi gözenekleri yerdeki en ufak görünmez cam tozlarını bile mıknatıs gibi içine hapsedecektir.', hook=['KIRILAN CAM','EKMEK İÇİ Mİ?'], icon='glass', shots=[(0,'sahne-1.png'),(45,'sahne-2.png'),(100,'sahne-1.png'),(230,'sahne-2.png'),(320,'sahne-3.png'),(480,'sahne-4.png')], events=[(235,280,'NEMLİ','EKMEK','drop','left'),(365,410,'TAMPON','HAREKET','hand','right')], cover=['KIRILAN CAM','EKMEK İÇİ Mİ?']),
'024': dict(boundary=32.4, caption='Koltuklarınızın veya siyah kabanınızın üzeri evcil hayvan tüyü, saç ve tozla kaplandığında yapışkanlı rulo bantlarınız bittiyse, mutfaktaki sarı plastik bulaşık eldivenini elinize geçirin! Kuru bulaşık eldivenini muslukta çok hafif nemlendirip suyunu silkeleyin ve elinizi koltuğun veya kabanın üzerinde yukarıdan aşağıya doğru tek yönde süpürür gibi gezdirin. Kauçuk eldivenin oluşturduğu sürtünme ve statik elektrik, kumaşın en derinine saplanmış tüyleri bile beş saniyede tek bir yumak halinde toplayacaktır.', hook=['KOLTUKTA TÜY','ELDİVENLE TOPLA'], icon='hand', shots=[(0,'sahne-1.png'),(45,'sahne-3b.png'),(105,'sahne-1.png'),(205,'sahne-2.png'),(320,'sahne-3b.png'),(500,'sahne-4b.png')], events=[(210,255,'HAFİF','NEMLİ','drop','right'),(340,390,'TEK','YÖNDE','hand','left')], cover=['KOLTUKTA TÜY','ELDİVENLE TOPLA'])}
for id,x in items.items():
 d=root/f'production/sifirdan-yeni/VID-{id}'; c=json.loads((rem/'bastan-022.json').read_text()); b=x['boundary']
 with wave.open(str(d/'anlatim.wav')) as w: dur=w.getnframes()/w.getframerate()
 c.update(id=id,dir='bastan'+id,frames=math.ceil((b/1.55+(dur-b)/1.62+.3)*30),tempoBoundary=b,captionEnd=b/1.55,ctaStart=round(b/1.55*30),caption=x['caption'],hook=x['hook'],openIcon=x['icon'],ctaStackFrames=[round((b/1.55+(dur-b-off)/1.62)*30) for off in [2.65,1.95,1.25,.55]],shots=[{'from':f,'file':name} for f,name in x['shots']],events=[{'from':a,'to':z,'a':t,'b':u,'icon':icon,'side':side,'y':330} for a,z,t,u,icon,side in x['events']])
 if id=='024': c['highlight']={'file':'sahne-3b.png','from':410,'to':470,'path':'M210 808 C238 785 285 780 338 791 C389 799 427 819 431 842 C434 864 402 882 359 889 C309 899 254 889 228 868 C210 854 201 831 210 808'}
 else: c.pop('highlight',None)
 dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
 for shot in c['shots']: shutil.copyfile(d/shot['file'],dest/shot['file'])
 (rem/f'bastan-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
 (rem/f'bastan-{id}.jsx').write_text((rem/'bastan-022.jsx').read_text().replace('bastan-022.json',f'bastan-{id}.json'))
 im=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((45,120,1035,470),radius=30,fill='#131e1c',outline='white',width=5)
 for j,line in enumerate(x['cover']):g.text((540,225+j*135),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',68),fill='#ffe135' if j==0 else 'white',anchor='mm')
 im.save(d/f'VID-{id}-img-1.jpg',quality=92)
