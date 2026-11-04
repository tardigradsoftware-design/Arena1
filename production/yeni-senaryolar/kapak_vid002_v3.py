#!/usr/bin/env python3
"""Generate a high-contrast, scenario-specific VID-002 mobile cover."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
p = Path(__file__).parent / 'VID-002'
im = ImageOps.fit(Image.open(p / 'sahne-1-yeni.png').convert('RGB'), (1080, 1920))
d = ImageDraw.Draw(im, 'RGBA')
d.rounded_rectangle((25, 560, 1055, 1170), radius=35, fill=(10, 9, 8, 232), outline=(255, 255, 255, 235), width=6)
font_path = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def drawline(y, text, fill, maximum):
    for size in range(maximum, 40, -1):
        font = ImageFont.truetype(font_path, size)
        box = d.textbbox((0, 0), text, font=font, stroke_width=3)
        if box[2] - box[0] <= 960:
            break
    x = (1080 - (box[2] - box[0])) // 2
    d.text((x, y), text, font=font, fill=fill, stroke_width=3, stroke_fill=(0, 0, 0, 255))
drawline(595, 'LAF SOKANA', (255,255,255,255), 148)
drawline(752, 'BEKLENMEDİK', (255,255,255,255), 134)
d.rounded_rectangle((72, 950, 1008, 1122), radius=22, fill=(255, 222, 40, 255), outline=(0,0,0,255), width=5)
drawline(970, 'TEK SORU!', (14, 12, 8, 255), 145)
im.save(p / 'VID-002-img-1-v3.jpg', quality=93)
im.resize((180, 320)).save('/tmp/vid002-kapak-v3-kucuk.jpg', quality=90)
