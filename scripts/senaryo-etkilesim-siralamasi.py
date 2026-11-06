#!/usr/bin/env python3
"""Reorder the supplied ODS without altering scripts or losing source fields.
Scores are transparent text-based editorial heuristics, not performance data.
"""
from pathlib import Path
from odf.opendocument import load
from odf.table import Table,TableRow,TableCell
from odf import teletype
from openpyxl import Workbook,load_workbook
from openpyxl.styles import Font,PatternFill,Alignment
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table as XTable,TableStyleInfo
from difflib import SequenceMatcher
import re
src=Path('google_drive/yeni seneryolar - dzn'); dst=Path('teslim/senaryolar-etkilesim-siralamasi-280.xlsx')
rows=load(str(src)).spreadsheet.getElementsByType(Table)[0].getElementsByType(TableRow)
records=[]
for n,row in enumerate(rows,1):
 cells=row.getElementsByType(TableCell); raw=teletype.extractText(cells[0]) if cells else ''
 if not raw.startswith('VID-'):continue
 ident,category,title,body=raw.split(';',3); scenario,rest=body.split(';Vertical ',1);rest='Vertical '+rest
 fields=rest.split(';',4); prompt=fields[:4];suffix=fields[4].split(';',4);cam,transition,sfx,headline= suffix[:4];desc,tags,hashtags=suffix[4].rsplit(';',2)
 assert ';'.join([ident,category,title,scenario,*prompt,cam,transition,sfx,headline,desc,tags,hashtags])==raw
 records.append(dict(id=ident, category=category,title=title,scenario=scenario,prompt=prompt,cam=cam,transition=transition,sfx=sfx,headline=headline,desc=desc,tags=tags,hashtags=hashtags,raw=raw,source_row=n))
assert len(records)==280 and len({x['id'] for x in records})==280
# Signals applied to title + first sentence; each capped and interpretable. Rules are
# editorial approximations and cannot predict performance or validate claims.
def contains(text,terms):return any(t in text for t in terms)
def evaluate(r):
 title=r['title'].lower(); opening=r['scenario'].split('!')[0][:450].lower();t=title+' '+opening
 universal=('çamaşır','kıyafet','ayakkabı','mutfak','halı','buzdolab','tencere','tabak','ütü','yemek','leke','makine','yağ','soğan','yumurta','bulaşık','cam','limon','havlu','banyo','perde','kapak','ekmek','patates','domates','su','kurut','süpürge')
 strong=('leke','yanık','kireç','yağ','tüy','sararan','sararm','sıkış','tıkan','taşma','kırış','yapış','çür','koku','bayat','sertleş','kurum','karar','solma','küf','izleri','yırt','dökül','çatla','dibi','dökülen','paslan','çöpe')
 visual=('temiz','beyaz','çıkar','soy','kes','açan','toplayan','söken','parlat','kaldır','sil','buz','sıkan','yumuş','dökülen','köpük','kesim','dilim','kurut','piş','hamur','büyüt','dondur','çatla','kabuk','sıkış','renk','yıkama','yağ','ıslak','leke','delik','fermuar','rulo','kırılan')
 curiosity=('sır','hile','tekni','yöntem','kural','gizli','hiç','asla','saniye','dakika','buz','kimse','önleyen','yapmadan','kullanmadan','gerek kalmadan','kaşık','iğne','kalem','sürmeden','dokunmadan','1 ','2 ','3 ','5 ','10 ')
 saving=('kullan','sakla','kurtar','değiştir','harcamadan','tamir','bozulma','bayat','çöpe','su','para','artık','ısın','yıka','kıyafet','havlu','mutfak','koku','temiz')
 def hits(text,terms):return sum(term in text for term in terms)
 # Saturating counts allow multiple, different signals to contribute, instead of
 # assigning the maximum merely because a single common word appears.
 relevance=min(20,8+2*min(3,hits(title,universal))+2*min(3,hits(title,strong)))
 visual_score=min(20,7+2*min(4,hits(title,visual))+min(3,hits(title,strong)))
 intrigue=min(20,7+2*min(4,hits(title,curiosity))+min(4,hits(title,strong))+int('!' in opening))
 sharing=min(20,7+2*min(3,hits(title,saving))+2*min(2,hits(title,universal))+min(3,hits(title,strong)))
 engagement=min(20,7+2*min(3,hits(title,curiosity))+2*min(3,hits(title,strong))+int('?' in r['scenario'][:400]))

 reason=[]
 if contains(t,strong):reason.append('belirgin gündelik sorun')
 if contains(title,visual):reason.append('görselleştirilebilir işlem veya sonuç')
 if contains(title,curiosity):reason.append('merak uyandıran yöntem')
 if not reason:reason.append('pratik fayda odaklı konu')
 return (relevance,visual_score,intrigue,sharing,engagement,'; '.join(reason))
for r in records:
 r['criteria']=evaluate(r);r['score']=sum(r['criteria'][:5])
for r in records:
 scores=[]
 for o in records:
  if o['id']==r['id']:continue
  sim=SequenceMatcher(None,r['title'].lower(),o['title'].lower()).ratio()
  if sim>=.69:scores.append((sim,o['id']))
 r['similar']=', '.join(x[1] for x in sorted(scores,reverse=True)[:3])
# Resolve ties transparently by stronger first hook then original source order.
ranked=sorted(records,key=lambda r:(-r['score'],-r['criteria'][2],-r['criteria'][1],r['source_row']))
w=Workbook();ws=w.active;ws.title='Potansiyel sıralaması'
headers=['SIRA','ORİJİNAL VIDEO_ID','KATEGORİ','KONU / TAM BAŞLIK','TAHMİNİ POTANSİYEL / 100','GÜNLÜK İLGİ / 20','GÖRSEL ANLATIM / 20','MERAK / 20','PAYLAŞILABİLİRLİK / 20','ETKİLEŞİM / 20','SIRALAMA SİNYALLERİ','BENZER BAŞLIK ID (OLASI)','TAM TTS METNİ','SAHNE 1 PROMPT','SAHNE 2 PROMPT','SAHNE 3 PROMPT','SAHNE 4 PROMPT','KAMERA EFEKTLERİ','GEÇİŞ EFEKTLERİ','SFX LİSTESİ','VİDEO BAŞLIĞI','AÇIKLAMA','ETİKETLER','HASHTAGLER','KAYNAK SATIR','KAYNAK SATIRIN TAMAMI']
ws.append(headers)
for i,r in enumerate(ranked,1):
 v=r['criteria'];ws.append([i,r['id'],r['category'],r['title'],r['score'],*v[:5],v[5],r['similar'],r['scenario'],*r['prompt'],r['cam'],r['transition'],r['sfx'],r['headline'],r['desc'],r['tags'],r['hashtags'],r['source_row'],r['raw']])
ws.freeze_panes='E2';ws.auto_filter.ref=f'A1:Z{len(ranked)+1}';ws.sheet_view.showGridLines=False
for cell in ws[1]:cell.fill=PatternFill('solid',fgColor='1E3944');cell.font=Font(bold=True,color='FFFFFF');cell.alignment=Alignment(wrap_text=True,vertical='center')
ws.row_dimensions[1].height=32
widths=[8,19,25,65,20,15,16,14,20,16,45,24,90,70,70,70,70,35,35,35,65,80,55,50,16,100]
for i,width in enumerate(widths,1):ws.column_dimensions[get_column_letter(i)].width=width
for row in ws.iter_rows(min_row=2):
 for cell in row:cell.alignment=Alignment(vertical='top',wrap_text=cell.column in [4,11,12,13,14,15,16,17,21,22,23,24,26]);
 if row[0].row%2==0:
  for cell in row:cell.fill=PatternFill('solid',fgColor='F0F6F5')
 row[4].font=Font(bold=True,color='126B57');ws.row_dimensions[row[0].row].height=48
ws.column_dimensions['Z'].hidden=True
info=w.create_sheet('Okuma rehberi');notes=[['ÖLÇÜT','AÇIKLAMA'],['Kaynak','Kullanıcının paylaştığı yeni seneryolar - dzn dosyası; 280 benzersiz video. Aradaki yinelenmiş başlık satırı veri değildir.'],['Sıralama','Başlık ve senaryonun ilk cümlesindeki sözcüklere dayanan otomatik, şeffaf editoryal önceliklendirme. Performans verisi veya platform tahmini değildir.'],['Puan','5 ölçütün her biri 20 puan üzerinden: gündelik ilgi, görsel anlatım, merak, paylaşılabilirlik ve etkileşim. 100 puan viral olma olasılığı veya başarı garantisi değildir.'],['Eşitlik','Eşit puanda önce merak, sonra görsellik; hâlâ eşitse kaynak sırası.'],['Benzer başlık','Metin benzerliği ile otomatik eşleşme; aynı video veya aynı senaryo olduğu doğrulanmış değildir. Hiçbir satır silinmedi.'],['Senaryolar','VIDEO_ID, senaryo ve bütün kaynak alanları korunmuştur; orijinal dosya değiştirilmemiştir. Gizli Z sütununda kaynak satırın tamamı bulunur.'],['Not','Ölçütler anlatımın doğru veya güvenli olduğunu doğrulamaz. Başarı; kurgu, izleyici tepkisi, platform ve yayın zamanına bağlıdır.']]
for row in notes:info.append(row)
info.column_dimensions['A'].width=25;info.column_dimensions['B'].width=110
for cell in info[1]:cell.fill=PatternFill('solid',fgColor='1E3944');cell.font=Font(bold=True,color='FFFFFF')
for row in info.iter_rows():
 for cell in row:cell.alignment=Alignment(vertical='top',wrap_text=True)
for i in range(2,9):info.row_dimensions[i].height=44
w.save(dst)
q=load_workbook(dst,read_only=True); data=list(q.worksheets[0].values); assert len(data)==281 and {r[1] for r in data[1:]}=={r['id'] for r in records};assert all(data[i][4]>=data[i+1][4] for i in range(1,280));assert {r[-1] for r in data[1:]}=={r['raw'] for r in records}
print('RECORDS',len(records),'FILE',dst)
for i,r in enumerate(ranked[:15],1):print(i,r['id'],r['score'],r['title'])
