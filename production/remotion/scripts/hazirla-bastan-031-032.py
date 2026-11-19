from pathlib import Path
import json, math, shutil, wave
from PIL import Image, ImageDraw, ImageFont, ImageOps
root=Path(__file__).resolve().parents[3]; rem=root/'production/remotion'
items={
'031':dict(boundary=32.0,caption='Çamaşır makinenizin deterjan çekmecesini çıkardığınızda iç kısımlarında siyah küf ve taşlaşmış deterjan kalıntıları görüyorsanız, temiz kıyafetlerinize her yıkamada bakteri bulaşıyor demektir! Çekmecenin ortasındaki mavi mandala basarak kutuyu yerinden çıkarın, sıcak su dolu bir leğenin içine iki yemek kaşığı limon tuzu ve bir kaşık bulaşık parlatıcısı döküp çekmeceyi on dakika bekletin. Küfler hiç fırçalamadan kendiliğinden akıp gidecek ve parlatıcı sayesinde bir daha deterjan yapışmayacaktır.',hook=['DETERJAN GÖZÜ','KÜF NASIL ÇIKAR?'],icon='washer',shots=[(0,'1'),(45,'2'),(105,'1'),(235,'2'),(335,'3b'),(485,'4'),(565,'5')],events=[(240,285,'MAVİ','MANDAL','hand','right'),(390,445,'ON','DAKİKA','clock','left')],cover=['DETERJAN GÖZÜ','NASIL TEMİZLENİR?']),
'032':dict(boundary=35.3,caption='Karpuz seçerken üzerine vurup ses dinlemekle uğraşmayın, karpuzun bal gibi tatlı ve kıpkırmızı olduğunu dışındaki şu iki işaretten beş saniyede anlayın! İlk olarak karpuzun tarlada toprağa değdiği alt kısmındaki lekeye bakın: Eğer bu leke beyaz veya açık yeşilse karpuz erken koparılmış ve kelektir; leke koyu tereyağı sarısı veya turuncuya yakınsa güneşte tam olgunlaşmıştır. İkinci olarak kabuğun üzerindeki kahverengi örümcek ağı çizgileri ne kadar çoksa arılar çiçeğe o kadar çok dokunmuş ve karpuz o kadar şekerli demektir.',hook=['KARPUZ SEÇERKEN','BU İKİ İŞARET'],icon='question',shots=[(0,'2b'),(45,'3'),(105,'2'),(245,'1c'),(360,'2b'),(480,'3'),(610,'4')],events=[(360,410,'SARI','LEKE','question','right'),(480,530,'KAHVERENGİ','ÇİZGİLER','question','left')],cover=['KARPUZ SEÇERKEN','NEYE BAKILIR?'])}
for id,x in items.items():
 d=root/f'production/sifirdan-yeni/VID-{id}';c=json.loads((rem/'bastan-024.json').read_text());b=x['boundary']
 with wave.open(str(d/'anlatim.wav')) as w:dur=w.getnframes()/w.getframerate()
 c.update(id=id,dir='yeniliste-bastan'+id,frames=math.ceil((b/1.55+(dur-b)/1.62+.4)*30),tempoBoundary=b,captionEnd=b/1.55,ctaStart=round(b/1.55*30),caption=x['caption'],hook=x['hook'],openIcon=x['icon'],ctaStackFrames=[round((b/1.55+(dur-b-off)/1.62)*30) for off in [2.65,1.95,1.25,.55]],shots=[{'from':f,'file':f'sahne-{n}.png'} for f,n in x['shots']],events=[{'from':a,'to':z,'a':t,'b':u,'icon':icon,'side':side,'y':330} for a,z,t,u,icon,side in x['events']])
 c.pop('highlight',None)
 if id=='032':
  for shot in c['shots']:
   if shot['file']=='sahne-2b.png': shot['captionTop']=1500
 if id=='031':c['highlight']={'file':'sahne-2.png','from':245,'to':300,'path':'M324 695 C332 660 380 639 422 642 C460 645 481 665 481 690 C482 716 447 734 407 737 C371 739 339 729 324 711'}
 if id=='032':c['highlight']={'file':'sahne-2b.png','from':375,'to':425,'path':'M251 892 C265 846 310 813 374 806 C437 801 497 825 521 863 C534 889 512 916 475 929 C417 945 333 943 281 925'}
 dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
 for s in c['shots']:shutil.copyfile(d/s['file'],dest/s['file'])
 (rem/f'bastan-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(rem/f'bastan-{id}.jsx').write_text((rem/'bastan-024.jsx').read_text().replace('bastan-024.json',f'bastan-{id}.json'))
 im=ImageOps.fit(Image.open(d/('sahne-1.png' if id=='031' else 'sahne-2b.png')).convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((45,120,1035,470),radius=30,fill='#131e1c',outline='white',width=5)
 for j,line in enumerate(x['cover']):g.text((540,225+j*135),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',62),fill='#ffe135' if j==0 else 'white',anchor='mm')
 im.save(d/f'VID-{id}-img-1.jpg',quality=92)
