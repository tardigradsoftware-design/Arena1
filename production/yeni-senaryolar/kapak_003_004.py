#!/usr/bin/env python3
"""Generate readable covers for scenarios 003 and 004 from their approved stills."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
root=Path(__file__).parent
font_path='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
for number,lines in [('003',('REGL SANCISI','BU NOKTA','NE İŞE YARAR?')),('004',('KURUYAN','PEYNİRE','BU KARIŞIM?!'))]:
    p=root/f'VID-{number}'
    im=ImageOps.fit(Image.open(p/'sahne-1.png').convert('RGB'),(1080,1920))
    d=ImageDraw.Draw(im,'RGBA')
    d.rounded_rectangle((30,550,1050,1160),radius=36,fill=(8,8,8,228),outline=(255,255,255,240),width=6)
    def line(y,text,fill,maximum,maxwidth=920):
        for size in range(maximum,40,-1):
            font=ImageFont.truetype(font_path,size)
            b=d.textbbox((0,0),text,font=font,stroke_width=3)
            if b[2]-b[0]<=maxwidth:break
        d.text(((1080-(b[2]-b[0]))//2,y),text,font=font,fill=fill,stroke_width=3,stroke_fill=(0,0,0,255))
    line(600,lines[0],(255,255,255,255),142)
    line(755,lines[1],(255,255,255,255),150)
    d.rounded_rectangle((75,945,1005,1115),radius=22,fill=(255,222,40,255),outline=(0,0,0,255),width=5)
    line(965,lines[2],(15,12,8,255),128,840)
    im.save(p/f'VID-{number}-img-1.jpg',quality=93)
    im.resize((180,320)).save(f'/tmp/kapak-{number}-kucuk.jpg',quality=90)
