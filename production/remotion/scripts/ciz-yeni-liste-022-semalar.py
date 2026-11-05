#!/usr/bin/env python3
"""Produce labelled, simplified schematics rather than misleading AI jar mechanics."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
out=Path(__file__).resolve().parents[2]/'yeni-liste'/'VID-022'
out.mkdir(parents=True,exist_ok=True)
W,H=768,1376
bold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
reg='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def font(n):return ImageFont.truetype(bold,n)
def base(title):
 im=Image.new('RGB',(W,H),'#f2f0e9');d=ImageDraw.Draw(im)
 d.rounded_rectangle((45,70,723,157),20,fill='#1b2932')
 d.text((69,91),'TEMSİLİ ŞEMA • '+title,font=font(27),fill='white')
 return im,d
def label(d,text,xy):
 d.rounded_rectangle((xy[0]-12,xy[1]-9,xy[0]+d.textlength(text,font=font(25))+15,xy[1]+37),10,fill='white')
 d.text(xy,text,font=font(25),fill='#24323a')
# Side cutaway, intentionally schematic and not a depiction of a verified execution.
im,d=base('YANDAN GÖRÜNÜM')
d.rounded_rectangle((90,360,678,1110),35,fill='#e2e9e8')
# Outer lip and neck, cross-section on one side of a jar.
d.polygon([(250,508),(475,508),(475,690),(455,715),(473,740),(473,1050),(370,1050),(370,760),(350,740),(370,710),(370,625),(250,625)],fill='#b9d9de',outline='#32606c',width=5)
d.line([(370,760),(440,760),(470,740)],fill='#32606c',width=7)
d.polygon([(130,450),(506,450),(506,655),(475,655),(475,508),(130,508)],fill='#c5a35c',outline='#604a27',width=5)
d.line([(140,466),(488,466)],fill='#ead9aa',width=5)
# Tip touches the outside edge of metal skirt; handle remains outside.
d.polygon([(469,652),(482,640),(659,724),(653,738)],fill='#8d9ba4',outline='#293f49',width=4)
d.ellipse((459,640,487,668),outline='#d52f39',width=5)
label(d,'METAL KAPAK',(153,392));label(d,'CAM',(277,1010));label(d,'KAŞIK SAPI',(473,790))
d.line((526,792,558,742),fill='#24323a',width=4)
im.save(out/'sema-kasik.png')
# Top view: a strip hugging the outer circumference of lid and a tangential tail.
im,d=base('ÜSTTEN GÖRÜNÜM')
d.rounded_rectangle((90,360,678,1110),35,fill='#e2e9e8')
d.ellipse((193,501,575,883),fill='#c4a463',outline='#5e4b29',width=7)
d.ellipse((221,529,547,855),outline='#f0e5cb',width=5)
d.arc((179,487,589,897),32,300,fill='#9c7552',width=23)
d.arc((179,487,589,897),32,300,fill='#dfba7d',width=13)
# Tail extends tangentially from the tape around the lid.
d.polygon([(548,792),(561,778),(666,882),(650,897)],fill='#d8b37a',outline='#9c7552',width=3)
label(d,'KAPAK',(325,667));label(d,'BANT',(239,939))
d.line((326,940,278,885),fill='#24323a',width=4)
im.save(out/'sema-bant.png')
