from pathlib import Path
from PIL import Image,ImageDraw,ImageFont,ImageOps
import json,math,shutil,wave
root=Path(__file__).resolve().parents[3];rem=root/'production/remotion'
items={
'019':dict(boundary=33.54,caption='Misafirlikte veya bir kafede otururken açık renk gömleğinize ya da pantolonunuza çay veya kahve damladığında, peçeteyle silip lekeyi kumaşa yaymayın! Hemen çay tabağındaki kuru bir adet küp şekeri alın ve doğrudan ıslak çay veya kahve damlasının tam üzerine bastırıp beş saniye tutun. Küp şekerin sıkıştırılmış kristalleri müthiş bir kılcal emiş gücüyle kumaştaki renkli sıvıyı saniyeler içinde kendi içine vakumlayıp çekecek; şeker kahverengi olurken kıyafetinizde tek bir leke bile kalmayacaktır.',hook=['ÇAY LEKESİ','KÜP ŞEKER Mİ?'],openIcon='wipe',shots=[(0,1),(45,3),(100,1),(220,2),(315,3),(510,4)],events=[(240,285,'KÜP','ŞEKER','bowl','left'),(330,380,'BEŞ','SANİYE','clock','right')],cover=['ÇAY LEKESİ','KÜP ŞEKER Mİ?']),
'020':dict(boundary=33.1,caption='Duş başlığınızın delikleri kireçten tıkanıp suyu her yöne eğri büğrü fışkırtıyorsa, başlığı İngiliz anahtarıyla söküp contalarını bozmaya çalışmayın! Sağlam bir buzdolabı poşetinin içine bir su bardağı ısıtılmış beyaz sirke ve bir yemek kaşığı karbonat koyun; duş başlığını poşetin içindeki sirkeye tamamen gömülecek şekilde geçirip poşetin ağzını paket lastiğiyle boruya sıkıca bağlayın. On beş dakika bekleyip sıcak suyu açtığınızda tüm kireç taşlarının eridiğini ve suyun ilk günkü gibi gürül gürül aktığını göreceksiniz.',hook=['DUŞ BAŞLIĞI','KİREÇ NASIL ÇIKAR?'],openIcon='water',shots=[(0,1),(45,2),(100,1),(210,2),(325,3),(480,4)],events=[(215,260,'SİRKE','VE KARBONAT','bowl','left'),(410,460,'ON BEŞ','DAKİKA','clock','right')],cover=['DUŞ BAŞLIĞI','KİREÇ NASIL ÇIKAR?'])}
for id,x in items.items():
 d=root/f'production/sifirdan-yeni/VID-{id}';c=json.loads((rem/'bastan-018.json').read_text());b=x['boundary']
 with wave.open(str(d/'anlatim.wav')) as w:dur=w.getnframes()/w.getframerate()
 c.update(id=id,dir='bastan'+id,frames=math.ceil((b/1.55+(dur-b)/1.62+.3)*30),tempoBoundary=b,captionEnd=b/1.55,ctaStart=round(b/1.55*30),caption=x['caption'],hook=x['hook'],openIcon=x['openIcon'],ctaStackFrames=[round((b/1.55+(dur-b-off)/1.62)*30) for off in [2.65,1.95,1.25,.55]],shots=[{'from':f,'file':f'sahne-{i}.png'} for f,i in x['shots']],events=[{'from':a,'to':z,'a':t,'b':u,'icon':icon,'side':side,'y':330} for a,z,t,u,icon,side in x['events']])
 if id=='019':shutil.copyfile(root/'production/sifirdan-yeni/VID-014/sahne-3.png',d/'sahne-4.png')
 dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
 for shot in c['shots']:shutil.copyfile(d/shot['file'],dest/shot['file'])
 (rem/f'bastan-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(rem/f'bastan-{id}.jsx').write_text((rem/'bastan-018.jsx').read_text().replace('bastan-018.json',f'bastan-{id}.json'))
 im=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((45,120,1035,470),radius=30,fill='#131e1c',outline='white',width=5)
 for j,line in enumerate(x['cover']):g.text((540,225+j*135),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',60),fill='#ffe135' if j==0 else 'white',anchor='mm')
 im.save(d/f'VID-{id}-img-1.jpg',quality=92)
