from pathlib import Path
import json, math, shutil, wave
from PIL import Image, ImageDraw, ImageFont, ImageOps
root=Path(__file__).resolve().parents[3]; rem=root/'production/remotion'
items={
'029':dict(boundary=34.5,caption='Beyaz masa örtünüze veya kıyafetinize nar, vişne ya da böğürtlen suyu damladığında üzerine hemen sabun sürerseniz leke morarıp kumaşa mühürlenir! Meyve asidi sabunla birleştiğinde kalıcı boyaya dönüşür. Lekeye hiç dokunmadan kumaşı lavabonun içindeki bir kasenin üzerine gergin şekilde tutun ve kaynayan su dolu çaydanlığı yarım metre yukarıdan lekenin tam üzerine dik olarak dökün. Sıcak suyun yukarıdan vuran basıncı meyve şekerini saniyede eritip kumaştan akıtacak ve tek bir iz bile kalmayacaktır.',hook=['MEYVE LEKESİ','NASIL ÇIKAR?'],icon='drop',shots=[(0,'1'),(45,'2'),(105,'1'),(290,'2'),(475,'3b'),(570,'4')],events=[(300,345,'KAYNAR','SU','drop','left'),(455,500,'LEKENİN','ÜZERİNE','drop','left')],cover=['MEYVE LEKESİ','NASIL ÇIKAR?']),
'030':dict(boundary=33.7,caption='Makarna haşlarken birbirine yapışmasın diye kaynayan suya sıvı yağ döküyorsanız, hem yağı çöpe atıyor hem de makarnanın sos tutmasını engelliyorsunuz! Suya dökülen yağ yüzeyde yüzer ve süzülürken makarnanın dışını kayganlaştırıp sosun üzerinden akıp gitmesine neden olur. Makarnanın asla yapışmaması için suya bol tuz atın ve makarnayı suya attığınız ilk iki dakika boyunca hiç bırakmadan karıştırın. Peki sen makarna suyuna yağ dökenlerden misin? Yorumlara yaz ve bu şef sırrını kaydet!',hook=['MAKARNA SUYUNA','YAĞ DÖKME!'],icon='pot',shots=[(0,'1'),(45,'3'),(105,'1'),(300,'2'),(405,'3'),(550,'4')],events=[(310,355,'BOL','TUZ','spoon','left'),(425,480,'İLK İKİ','DAKİKA','clock','right')],cover=['MAKARNA SUYU','YAĞSIZ MI?'])}
for id,x in items.items():
 d=root/f'production/sifirdan-yeni/VID-{id}';c=json.loads((rem/'bastan-024.json').read_text());b=x['boundary']
 with wave.open(str(d/'anlatim.wav')) as w:dur=w.getnframes()/w.getframerate()
 c.update(id=id,dir='yeniliste-bastan'+id,frames=math.ceil((b/1.55+(dur-b)/1.62+.4)*30),tempoBoundary=b,captionEnd=b/1.55,ctaStart=round(b/1.55*30),caption=x['caption'],hook=x['hook'],openIcon=x['icon'],ctaStackFrames=[round((b/1.55+(dur-b-off)/1.62)*30) for off in [2.65,1.95,1.25,.55]],shots=[{'from':f,'file':f'sahne-{n}.png'} for f,n in x['shots']],events=[{'from':a,'to':z,'a':t,'b':u,'icon':icon,'side':side,'y':330} for a,z,t,u,icon,side in x['events']])
 c.pop('highlight',None)
 if id=='029':c['highlight']={'file':'sahne-1.png','from':110,'to':165,'path':'M275 649 C279 597 340 574 400 580 C464 584 498 620 492 666 C486 711 430 735 372 735 C318 735 279 710 275 673'}
 dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
 for s in c['shots']:shutil.copyfile(d/s['file'],dest/s['file'])
 (rem/f'bastan-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(rem/f'bastan-{id}.jsx').write_text((rem/'bastan-024.jsx').read_text().replace('bastan-024.json',f'bastan-{id}.json'))
 im=ImageOps.fit(Image.open(d/('sahne-1.png' if id=='029' else 'sahne-4.png')).convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((45,120,1035,470),radius=30,fill='#131e1c',outline='white',width=5)
 for j,line in enumerate(x['cover']):g.text((540,225+j*135),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',62),fill='#ffe135' if j==0 else 'white',anchor='mm')
 im.save(d/f'VID-{id}-img-1.jpg',quality=92)
