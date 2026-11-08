#!/usr/bin/env python3
"""Build a standalone offline publishing workspace from the ranked ODS."""
from pathlib import Path
from odf.opendocument import load
from odf.table import Table,TableRow,TableCell
from odf import teletype
import json,re
root=Path(__file__).resolve().parents[1]; src=root/'google_drive/yeni_seneryolar_-_viral_siralamali.ods'
rows=load(str(src)).spreadsheet.getElementsByType(Table)[0].getElementsByType(TableRow)
items=[]
templates=["{topic} konusunda siz hangi yöntemi tercih ediyorsunuz? Farklı bir püf noktanız varsa paylaşın 👇", "Sizce {topic} için en pratik çözüm hangisi? Deneyimlerinizi merak ediyorum 👇", "Bir konu, farklı yöntemler: {topic} için sizin vazgeçilmeziniz ne?", "{topic} denince aklınıza ilk hangi ipucu geliyor? Yorumlarda buluşalım 💬", "Benzer konuda herkesin bir yöntemi var: {topic} için siz ne yapıyorsunuz?", "{topic} hakkında farklı görüşleri okuyalım: Sizce işe yarayan yaklaşım hangisi?", "Bu konuda karar sizin: {topic} için klasik yöntem mi, başka bir çözüm mü?", "Küçük bir tartışma açalım: {topic} için en iyi öneriniz nedir?", "{topic} konusunda hiç denemediğiniz ama merak ettiğiniz bir yöntem var mı?", "Sizin evde {topic} nasıl çözülüyor? Kendi yöntemlerinizi yazın 👇"]
custom={'VID-001':'Gider temizliğinde siz hangi yöntemi kullanıyorsunuz: hazır bir aparat mı, kendi yaptığınız bir çözüm mü? 👇','VID-002':'Halıdaki saç ve tüyler için siz süpürge dışında ne kullanıyorsunuz? Farklı yöntemleri merak ediyorum 👇','VID-003':'Yanık tencere temizliğinde sizin en çok işe yarayan yönteminiz ne? Malzemeye göre değişiyor mu? 💬','VID-004':'Beyaz ayakkabı tabanlarını temizlerken sizin vazgeçilmez yönteminiz nedir?','VID-005':'Kabloları korumak için siz hangi önlemi alıyorsunuz: kablo koruyucu mu, başka bir yöntem mi? 👇','VID-006':'Fırın camını temizlerken siz hangi yöntemi tercih ediyorsunuz? Deneyimlerinizi paylaşın 💬','VID-007':'Siyah kıyafetteki deodorant izleri için sizin pratik çözümünüz ne? 👇'}
for r in rows[1:]:
 cells=r.getElementsByType(TableCell)
 if not cells:continue
 text=teletype.extractText(cells[0]); head=text.split(';',3)
 if len(head)!=4 or not re.fullmatch(r'VID-\d{3}',head[0]):continue
 id,cat,subject,rest=head
 if ';Vertical' not in rest:raise ValueError(id)
 script,tail=rest.split(';Vertical',1); parts=tail.split(';')
 if len(parts)<10 or not (' | ' in parts[6]):raise ValueError('SFX '+id)
 title=parts[7].strip(); tags=parts[-2].strip(); hashtags=parts[-1].replace(' | ',' ').strip(); desc=';'.join(parts[8:-2]).strip()
 topic=tags.split(',')[0].strip().lower()
 comment=custom.get(id,templates[(int(id[-3:])-1)%len(templates)].format(topic=topic))
 items.append(dict(id=id,category=cat,subject=subject,title=title,description=desc,tags=tags,hashtags=hashtags,comment=comment))
assert len(items)==280 and len({x['id'] for x in items})==280
html=(root/'scripts/icerik-paneli-sablon.html').read_text().replace('/*__DATA__*/','const DATA = '+json.dumps(items,ensure_ascii=False).replace('</','<\\/')+';')
(root/'teslim/kadinca-yasam-icerik-paneli.html').write_text(html)
print('Oluşturuldu:',len(items),'video')
