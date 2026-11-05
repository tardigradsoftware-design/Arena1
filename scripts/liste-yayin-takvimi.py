#!/usr/bin/env python3
"""Generate the 132-item video metadata and 4-per-day schedule from the numbered ODS."""
from datetime import datetime, timedelta, time
from pathlib import Path
import re, zipfile, xml.etree.ElementTree as ET
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

root=Path(__file__).resolve().parents[1]
source=root/'google_drive/yeni seneryolar numaralandirilmis.ods'
output=root/'teslim/yeni-liste-132-yayin-takvimi.xlsx'
ns={'t':'urn:oasis:names:tc:opendocument:xmlns:table:1.0','x':'urn:oasis:names:tc:opendocument:xmlns:text:1.0'}
with zipfile.ZipFile(source) as z:doc=ET.fromstring(z.read('content.xml'))
rows=[]
for row in doc.findall('.//t:table-row',ns):
 ps=row.findall('.//x:p',ns); text=''.join(ps[0].itertext()) if ps else ''
 if not re.match(r'^VID-\d{3};',text):continue
 head,sep,rest=text.partition(';Vertical 9:16,')
 if not sep:raise ValueError('Missing first prompt: '+text[:7])
 vid,category,topic,narration=head.split(';',3)
 bits=('Vertical 9:16,'+rest).split(';')
 if len(bits)<11:raise ValueError('Incomplete row '+vid)
 scenes=bits[:4];camera,transitions,sfx,title=bits[4:8];desc=';'.join(bits[8:-2]);tags,hashtags=bits[-2:]
 if not all(p.startswith('Vertical 9:16,') for p in scenes):raise ValueError('Unexpected scene delimiters '+vid)
 rows.append([vid,category,topic,narration,*scenes,camera,transitions,sfx,title,desc,tags,hashtags])
assert len(rows)==132
assert [r[0] for r in rows]==[f'VID-{n:03}' for n in range(1,133)]
wb=Workbook();ws=wb.active;ws.title='Yayın Takvimi'
headers=['VIDEO ID','KATEGORİ','KONU','TAM TTS METNİ','SAHNE 1 PROMPT','SAHNE 2 PROMPT','SAHNE 3 PROMPT','SAHNE 4 PROMPT','KAMERA EFEKTLERİ','GEÇİŞ EFEKTLERİ','SFX LİSTESİ','VİDEO BAŞLIĞI','VİDEO AÇIKLAMASI','ETİKETLER','HASHTAGLER','TOPLU AÇIKLAMA','PAYLAŞIM TARİHİ','PAYLAŞIM SAATİ']
ws.append(headers); slots=[time(8,0),time(11,0),time(15,0),time(19,0)]
for i,row in enumerate(rows):
 title,desc,tags,hashtags=row[11:15]
 # Copy-ready text: one item per line group, with blank lines between sections.
 combined='\n\n'.join([title.strip(),desc.strip(),tags.strip(),hashtags.replace(' | ',' ').strip()])
 date=datetime(2026,11,5)+timedelta(days=i//4)
 ws.append(row+[combined,date,slots[i%4]])
for cell in ws[1]:cell.font=Font(bold=True,color='FFFFFF');cell.fill=PatternFill('solid',fgColor='5B3754');cell.alignment=Alignment(horizontal='center',vertical='center',wrap_text=True)
ws.row_dimensions[1].height=34
widths=[14,24,55,70,48,48,48,48,36,30,38,55,60,45,45,70,19,18]
for i,width in enumerate(widths,1):ws.column_dimensions[get_column_letter(i)].width=width
for row in ws.iter_rows(min_row=2):
 ws.row_dimensions[row[0].row].height=90
 for c in row:
  c.alignment=Alignment(vertical='top',wrap_text=True)
  if c.row%2==0:c.fill=PatternFill('solid',fgColor='F8F2F6')
 row[16].number_format='dd.mm.yyyy';row[17].number_format='hh:mm'
ws.freeze_panes='D2';ws.auto_filter.ref=ws.dimensions
ws.sheet_view.zoomScale=80
output.parent.mkdir(parents=True,exist_ok=True);wb.save(output)
check=load_workbook(output,data_only=True).active
assert check.max_row==133 and check.max_column==18
assert check['A2'].value=='VID-001' and check['A133'].value=='VID-132'
assert check['Q2'].value==datetime(2026,11,5) and check['R2'].value==time(8)
assert check['Q133'].value==datetime(2026,12,7) and check['R133'].value==time(19)
print(output, len(rows), check['Q2'].value, check['Q133'].value, check['R133'].value)
