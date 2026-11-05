#!/usr/bin/env python3
from pathlib import Path
import json,shutil,wave,math
from PIL import Image,ImageDraw,ImageFont,ImageOps
root=Path(__file__).resolve().parents[3];p=root/'production';r=p/'remotion';pub=r/'public'
settings={'023':{'caption':'Evde patates kızarttığınızda dışının çıtır çıtır olmak yerine yağ çekip hamur gibi yumuşamasına son verin! Doğradığınız patatesleri yıkadıktan sonra soğuk su, bir yemek kaşığı elma sirkesi ve buz dolu kasede on beş dakika bekletin. Ardından patatesleri kağıt havluyla tek bir damla su kalmayana kadar kurutup üzerine sadece bir yemek kaşığı mısır nişastası serpiştirerek kızgın yağa atın. Patatesleriniz asla yağ çekmeden kütür kütür kızaracaktır.', 'hook':['PATATES','NASIL ÇITIR OLUR?'],'cover':['PATATES','NASIL','ÇITIR OLUR?'],'openIcon':'pot','cta':19.1,'events':[(110,155,'SOĞUK','SU VE BUZ','ice','right',330),(235,280,'15 DAKİKA','BEKLET','clock','left',330),(340,385,'KAĞIT','HAVLU','wipe','right',330),(440,485,'MISIR','NİŞASTASI','spoon','left',330)],'shots':[(0,3),(45,4),(115,1),(280,2),(380,2),(460,3),(575,3)],'highlight':None}}
common=(r/'scripts/hazirla-yeni-liste-013-014.py').read_text();loop=common[common.index('for id,s in settings.items():'):].replace("cover=4 if id=='013' else 1",'cover=3')
exec(compile(loop,__file__,'exec'))
f=r/'yeni-liste-023.json';c=json.loads(f.read_text());c['ctaItems']=[['ARKADAŞINA GÖNDER','share'],['ABONE OL','subscribe']];f.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
