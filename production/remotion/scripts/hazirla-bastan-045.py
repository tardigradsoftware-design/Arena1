from pathlib import Path
import json,math,shutil,wave
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).resolve().parents[3];rem=root/'production/remotion';d=root/'production/sifirdan-yeni/VID-045';b=36.9
caption='Mutfakta elinizden kayıp yere veya tezgaha düşen çiğ yumurtayı kağıt havluyla ya da bezle silmeye çalışırsanız, yumurtanın kaygan akı her yere yayılır ve sildiğiniz bez kokudan kullanılmaz hale gelir! Kırılan çiğ yumurtaya hiç bez değdirmeden üzerine hemen avuç dolusu sofra tuzu döküp yumurtanın tamamını tuzla kapatın ve sadece bir dakika bekleyin. Tuz çiğ yumurta proteinini saniyeler içinde pıhtılaştırıp katı bir hamura dönüştürecek; bir karton veya faraşla ittiğinizde yerde tek bir iz bile bırakmadan kalıp halinde kalkacaktır. Hemen kaydet ve paylaş!'
with wave.open(str(d/'anlatim.wav')) as w:dur=w.getnframes()/w.getframerate()
c=json.loads((rem/'bastan-024.json').read_text());c.update(id='045',dir='yeniliste-bastan045',frames=math.ceil((b/1.55+(dur-b)/1.62+.4)*30),tempoBoundary=b,captionEnd=b/1.55,ctaStart=round(b/1.55*30),caption=caption,safeCaptions=True,hook=['YERE KIRILAN','YUMURTA NASIL TOPLANIR?'],openIcon='drop',ctaStackFrames=[round((b/1.55+(dur-b-off)/1.62)*30) for off in [2.65,1.95,1.25,.55]],shots=[{'from':a,'file':f'sahne-{n}.png','captionTop':1510} for a,n in [(0,1),(48,1),(225,2),(340,2),(415,3),(525,3),(625,4)]],events=[{'from':a,'to':z,'a':t,'b':u,'icon':icon,'side':side,'y':330} for a,z,t,u,icon,side in [(240,290,'BOL','TUZ','drop','right'),(390,450,'1','DAKİKA','clock','left')]],highlight={'file':'sahne-1.png','from':55,'to':100,'path':'M160 560 C174 493 249 460 342 462 C460 457 558 494 578 560 C605 630 566 735 500 773 C407 817 272 791 201 750 C158 724 145 624 160 560'})
dest=rem/'public'/c['dir'];dest.mkdir(parents=True,exist_ok=True)
for shot in c['shots']:shutil.copyfile(d/shot['file'],dest/shot['file'])
(rem/'bastan-045.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(rem/'bastan-045.jsx').write_text((rem/'bastan-024.jsx').read_text().replace('bastan-024.json','bastan-045.json'))
im=ImageOps.fit(Image.open(d/'sahne-1.png').convert('RGB'),(1080,1920));g=ImageDraw.Draw(im);g.rounded_rectangle((45,120,1035,420),radius=30,fill='#131e1c',outline='white',width=5)
for j,line in enumerate(['YERE KIRILAN','YUMURTA NASIL TOPLANIR?']):g.text((540,205+j*125),line,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',50),fill='#ffe135' if j==0 else 'white',anchor='mm')
im.save(d/'VID-045-img-1.jpg',quality=92)
