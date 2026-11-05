#!/usr/bin/env python3
from pathlib import Path
import json,shutil,wave,math
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).resolve().parents[3];p=root/'production';r=p/'remotion';pub=r/'public'
settings={'024':{'caption':'Dibini tutturduğunuz çelik tencerenin veya fırın tepsisinin yanık karasını çıkarmak için tel süngerle kollarınızı koparana kadar ovalamayın! Yanık tencerenin içine sıcak su doldurup bir adet bulaşık makinesi tableti atın ve ocağın üzerinde on dakika kaynatın. Ardından suyu döküp alüminyum folyoyu top gibi buruşturun ve yumuşayan yanıkları folyoyla hafifçe silin. Tablet yağı çözerken folyo tencereyi hiç çizmeden tüm yanıkları saniyeler içinde söküp atacaktır.', 'hook':['YANIK TENCERE','NASIL TEMİZLENİR?'],'cover':['YANIK TENCERE','NASIL','TEMİZLENİR?'],'openIcon':'pot','cta':20.42,'events':[(95,140,'YANIK','TENCERE','pot','right',330),(205,250,'BULAŞIK','TABLETİ','soap','left',330),(285,330,'10 DAKİKA','BEKLET','clock','right',330),(400,445,'ALÜMİNYUM','FOLYO','wipe','left',330)],'shots':[(0,1),(45,5),(130,1),(200,2),(320,5),(400,3),(520,6),(610,1)],'highlight':None}}
common=(r/'scripts/hazirla-yeni-liste-013-014.py').read_text();loop=common[common.index('for id,s in settings.items():'):].replace("cover=4 if id=='013' else 1",'cover=1')
exec(compile(loop,__file__,'exec'))
f=r/'yeni-liste-024.json';c=json.loads(f.read_text());c['warning']='TASLAK · BU YÖNTEMİ UYGULAMAYIN';f.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
