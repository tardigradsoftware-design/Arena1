#!/usr/bin/env python3
from pathlib import Path
import json,shutil,wave,math
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).resolve().parents[3];p=root/'production';r=p/'remotion';pub=r/'public'
settings={
'021':{'caption':'Yarısını kahvaltıda yediğiniz avokadoyu veya elmayı buzdolabına koyduğunuzda bir saat içinde simsiyah olmasına son verin! Avokadonun çekirdeğini çıkarmayın, kesik olan yeşil yüzeyine parmağınızla çok ince bir kat zeytinyağı sürün ya da saklama kabının tabanına iki halka kuru soğan koyup avokadoyu üzerine yerleştirin. Zeytinyağı oksijenle teması keserek avokadonuzu günlerce yemyeşil tutacaktır.', 'hook':['YARIM AVOKADO','NASIL SAKLANIR?'],'cover':['AVOKADO','NASIL','SAKLANIR?'], 'openIcon':'avocado','cta':17.36,'events':[(95,140,'AVOKADO','VE ELMA','food','right',330),(215,260,'ZEYTİNYAĞI','İNCE KAT','drop','left',330),(315,360,'SOĞAN','HALKALARI','avocado','right',330),(390,430,'BUZDOLABI','SAKLAMA','ice','left',330)],'shots':[(0,1),(45,2),(130,1),(200,2),(300,3),(400,4),(520,1)]},
'022':{'caption':'Yeni aldığınız konserve veya turşu kavanozunun kapağı vakumdan dolayı sıkıştığında bileğinizi zorlayıp elinizi acıtmayın! Kavanoz kapağının yan kenarındaki metal boşluğa bir tatlı kaşığının sapını sokup hafifçe dışa doğru kanırtın; pıs diye vakum sesini duyduğunuz an kapak tek parmakla dönecektir. Eğer kaşık yoksa kapağın etrafına bir parça koli bandı yapıştırıp bandın ucundan çekin, saniyesinde açılır.', 'hook':['KAVANOZ KAPAĞI','NASIL AÇILIR?'],'cover':['KAVANOZ','NASIL','AÇILIR?'], 'openIcon':'jar','cta':16.9,'events':[(95,140,'SIKI','KAPAK','jar','right',330),(200,245,'KAŞIK','SAPI','spoon','left',330),(330,375,'KAVANOZ','KAPAĞI','jar','right',330),(430,475,'KOLİ','BANDI','wipe','left',330)],'shots':[(0,1),(45,2),(130,1),(200,2),(300,4),(405,3),(500,4)]}}
# No target-specific highlight: the images depict tools and ingredients, not the action itself.
for s in settings.values():s['highlight']=None
common=(r/'scripts/hazirla-yeni-liste-013-014.py').read_text();loop=common[common.index('for id,s in settings.items():'):].replace("cover=4 if id=='013' else 1",'cover=1')
exec(compile(loop,__file__,'exec'))

# The second recording asks the viewer to share and subscribe.
f=r/'yeni-liste-022.json'; c=json.loads(f.read_text()); c['ctaItems']=[['ARKADAŞINA GÖNDER','share'],['ABONE OL','subscribe']]; f.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
