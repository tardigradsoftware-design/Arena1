#!/usr/bin/env python3
"""Timeline and sources for VID-029/030. CTA timing is estimated from pauses."""
from pathlib import Path
import json,shutil,wave,math
from PIL import Image
root=Path(__file__).resolve().parents[3];p=root/'production';r=p/'remotion';pub=r/'public'
d29=p/'yeni-senaryolar/VID-029';d30=p/'yeni-senaryolar/VID-030'
# The four 029 visuals include a dedicated sealed-bag freezer shot.
shutil.copy(p/'reference/VID-017/VID-017-2.png',d30/'sahne-4.png')
settings={
'029':{'caption':'Akşam yemeğine yarım saat kala buzluktan çıkardığınız taş gibi kıymayı çözdürmek için üzerine sıcak su döküp bakteri üretmeyin! Kilitli poşetteki donmuş kıymayı derin bir kase soğuk çeşme suyunun içine batırın, suya iki yemek kaşığı kaya tuzu atıp üzerine ağır bir tabak koyun. Tuzlu soğuk su ısıyı yirmi kat hızlı ileterek kıymayı on dakikada lokum gibi çözer.','hook':['DONMUŞ KIYMA','NASIL ÇÖZÜLÜR?'],'openIcon':'ice','cta':16.45,'events':[(75,125,'DONDURUCU','KIYMA','ice','right',320),(175,225,'KİLİTLİ','POŞET','bag','left',320),(280,330,'SOĞUK','SU','drop','right',320),(375,420,'KAYA TUZU','VE SU','bowl','left',320)],'shots':[(0,1),(45,4),(90,1),(165,2),(310,3),(494,2)]},
'030':{'caption':'Beyaz spor ayakkabılarınızın lastik taban kenarları ne kadar silerseniz silin sararıyor ve siyah çizgiler çıkmıyorsa çamaşır suyu sürüp lastiği eritmeyin! Bir tatlı kaşığı beyazlatıcı diş macunu, bir tatlı kaşığı karbonat ve birkaç damla bulaşık deterjanını karıştırıp eski bir diş fırçasıyla tabanları fırçalayın. Sildiğiniz an ayakkabılarınız kutusundan yeni çıkmış gibi kar beyazı olacaktır.','hook':['SARARAN TABAN','NASIL TEMİZLENİR?'],'openIcon':'shoe','cta':16.33,'final':17.72,'events':[(80,130,'SPOR','AYAKKABI','shoe','right',320),(210,260,'DİŞ MACUNU','KARBONAT','bowl','left',320),(310,365,'FIRÇAYLA','TEMİZLE','brush','right',320)],'shots':[(0,1),(45,4),(90,1),(195,3),(300,2),(490,1)]}}
for id,s in settings.items():
 d=p/'yeni-senaryolar'/f'VID-{id}'
 with wave.open(str(d/'seri-yeni-anlatim.wav')) as w:frames=math.ceil((w.getnframes()/w.getframerate()/1.55+.2)*30)
 c={key:s[key] for key in ('caption','hook','openIcon')};c.update(id=id,dir='yeniseri'+id,frames=frames,captionEnd=s['cta'],ctaStart=round(30*s['cta']),ctaHeading='BÖYLE İÇERİKLERİN DEVAMI İÇİN',ctaItems=[['BEĞEN','like'],['ABONE OL','subscribe']],shots=[{'from':f,'file':f'sahne-{i}.png'} for f,i in s['shots']],events=[dict(zip(('from','to','a','b','icon','side','y'),x)) for x in s['events']])
 if s.get('final'):c.update(cta2Start=round(s['final']*30),ctaHeading='SONUCU PAYLAŞ',ctaFinalHeading='BÖYLE İÇERİKLERİN DEVAMI İÇİN',ctaFirstItems=[['YORUM YAP','talk'],['BEĞEN','like']])
 (r/f'yeni-seri-{id}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');(r/f'yeni-seri-{id}.jsx').write_text((r/'yeni-seri-028.jsx').read_text().replace('028',id)); dest=pub/c['dir'];dest.mkdir(exist_ok=True)
 for i in range(1,5):shutil.copy(d/f'sahne-{i}.png',dest/f'sahne-{i}.png')
 print(id,frames,c['ctaStart'])
