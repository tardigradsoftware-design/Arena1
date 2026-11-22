from pathlib import Path
import json,math,shutil,wave
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).resolve().parents[3];rem=root/'production/remotion';d=root/'production/sifirdan-yeni/VID-044';b=35.7
caption='Mutfak ve banyo musluklarının tezgahla birleştiği o dar dip kısımlarında biriken taşlaşmış beyaz yeşil kireç halkalarını bıçakla kazıyıp kromu çizmeyin! İki yaprak kağıt havluyu katlayıp doğrudan beyaz sirkenin içine batırın ve bu sirkeli ıslak peçeteyi musluğun dip kısmına atkı sarar gibi sıkıca dolayıp yirmi dakika bekletin. Sıvı sirke akıp gider ama peçeteye hapsolan sirke kirecin üzerinde kaldığı için yirmi dakika sonunda peçeteyi çektiğinizde o taşlaşmış kirecin hamur gibi eriyip tek silişte çıktığını göreceksiniz. Temizlik için hemen kaydet ve beğen!'
with wave.open(str(d/'anlatim.wav')) as w:dur=w.getnframes()/w.getframerate()
c=json.loads((rem/'bastan-024.json').read_text());c.update(id='044',dir='yeniliste-bastan044',frames=math.ceil((b/1.55+(dur-b)/1.62+.4)*30),tempoBoundary=b,captionEnd=b/1.55,ctaStart=round(b/1.55*30),caption=caption,safeCaptions=True,hook=['MUSLUK DİBİNDEKİ','KİRECE NE YAPILIR?'],openIcon='shine',ctaStackFrames=[round((b/1.55+(dur-b-off)/1.62)*30) for off in [2.65,1.95,1.25,.55]],shots=[{'from':a,'file':f'sahne-{n}.png','captionTop':1510} for a,n in [(0,1),(48,1),(210,5),(300,2),(390,3),(520,3),(610,4)]],events=[{'from':a,'to':z,'a':t,'b':u,'icon':icon,'side':side,'y':330} for a,z,t,u,icon,side in [(220,270,'BEYAZ','SİRKE','drop','right'),(400,455,'20','DAKİKA','clock','left')]],highlight={'file':'sahne-1.png','from':55,'to':100,'path':'M194 771 C199 720 248 695 318 691 C395 683 474 707 497 758 C518 807 500 913 465 951 C421 984 300 979 240 953 C199 935 184 852 194 771'})
dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for shot in c['shots']:shutil.copyfile(d/shot['file'],dest/shot['file'])
(rem/'bastan-044.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(rem/'bastan-044.jsx').write_text((rem/'bastan-024.jsx').read_text().replace('bastan-024.json','bastan-044.json'))
im=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((45,120,1035,420),radius=30,fill='#131e1c',outline='white',width=5)
for j,line in enumerate(['MUSLUK DİBİNDEKİ','KİRECE NE YAPILIR?']):g.text((540,205+j*125),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',50),fill='#ffe135' if j==0 else 'white',anchor='mm')
im.save(d/'VID-044-img-1.jpg',quality=92)
