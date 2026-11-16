from pathlib import Path
import json, math, shutil, wave
from PIL import Image, ImageDraw, ImageFont, ImageOps
root=Path(__file__).resolve().parents[3]; rem=root/'production/remotion'
items={
'025':dict(boundary=29.0,caption='Elektronik eşyaların, pillerin veya oyuncakların o taş gibi sert, preslenmiş şeffaf plastik ambalajlarını açmaya çalışırken bıçak veya makas kayıp elinizi yaralamayın! Mutfak çekmecenizdeki sıradan bir dönerli konserve açacağını alın ve konserve kapağı açar gibi plastik ambalajın sert kenar çerçevesine takıp kolunu çevirin. Konserve açacağı o sert plastiği kağıt keser gibi pürüzsüz ve güvenli bir şekilde beş saniyede boydan boya açacaktır.',hook=['SERT AMBALAJ','KONSERVE AÇACAĞI'],icon='scissors',shots=[(0,1),(45,2),(105,1),(210,2),(330,3),(480,4)],events=[(220,265,'DÖNERLİ','AÇACAK','hand','left'),(390,435,'KENAR','ÇERÇEVE','scissors','right')],cover=['SERT AMBALAJ','NASIL AÇILIR?']),
'026':dict(boundary=33.6,caption='Ahşap yemek masanızda, sehpanızda veya parkelerinizde oluşan o beyazlamış çizikleri kapatmak için pahalı mobilya kalemleri almanıza hiç gerek yok! Mutfağınızdaki kabuğu kırılmış çiğ bir ceviz içini alın ve çizik olan ahşap yüzeyin üzerine bastırarak ileri geri on saniye boyunca sürtün, ardından parmağınızla çizgiyi ovup kuru bezle parlatın. Cevizin içindeki yoğun doğal yağ ve renk pigmentleri çizilen ahşap liflerini anında doyurup şişirecek ve çiziğin saniyeler içinde görünmez olduğunu fark edeceksiniz.',hook=['AHŞAP ÇİZİĞİ','CEVİZ İÇİ Mİ?'],icon='wipe',shots=[(0,1),(45,2),(110,1),(220,2),(375,3),(500,4)],events=[(220,265,'ÇİĞ','CEVİZ','leaf','left'),(310,355,'ON','SANİYE','clock','right')],cover=['AHŞAP ÇİZİĞİ','CEVİZ İÇİ Mİ?'])}
for id,x in items.items():
 d=root/f'production/sifirdan-yeni/VID-{id}';c=json.loads((rem/'bastan-024.json').read_text());b=x['boundary']
 with wave.open(str(d/'anlatim.wav')) as w:dur=w.getnframes()/w.getframerate()
 c.update(id=id,dir='yeniliste-bastan'+id,frames=math.ceil((b/1.55+(dur-b)/1.62+.3)*30),tempoBoundary=b,captionEnd=b/1.55,ctaStart=round(b/1.55*30),caption=x['caption'],hook=x['hook'],openIcon=x['icon'],ctaStackFrames=[round((b/1.55+(dur-b-off)/1.62)*30) for off in [2.65,1.95,1.25,.55]],shots=[{'from':f,'file':f'sahne-{n}.png'} for f,n in x['shots']],events=[{'from':a,'to':z,'a':t,'b':u,'icon':icon,'side':side,'y':330} for a,z,t,u,icon,side in x['events']])
 c.pop('highlight',None)
 if id=='026':c['highlight']={'file':'sahne-2.png','from':245,'to':300,'path':'M225 830 C252 800 310 765 352 744 C376 730 394 733 399 744 C404 757 387 773 368 782 L255 856 C235 868 219 856 225 830'}
 dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
 for s in c['shots']:shutil.copyfile(d/s['file'],dest/s['file'])
 (rem/f'bastan-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(rem/f'bastan-{id}.jsx').write_text((rem/'bastan-024.jsx').read_text().replace('bastan-024.json',f'bastan-{id}.json'))
 im=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((45,120,1035,470),radius=30,fill='#131e1c',outline='white',width=5)
 for j,line in enumerate(x['cover']):g.text((540,225+j*135),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',62),fill='#ffe135' if j==0 else 'white',anchor='mm')
 im.save(d/f'VID-{id}-img-1.jpg',quality=92)
