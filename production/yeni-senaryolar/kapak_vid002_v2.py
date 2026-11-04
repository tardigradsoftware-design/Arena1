#!/usr/bin/env python3
"""Create a high-contrast VID-002 cover from its face-free scenario image."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

p = Path(__file__).parent / 'VID-002'
im = ImageOps.fit(Image.open(p / 'sahne-1-yeni.png').convert('RGB'), (1080, 1920))
d = ImageDraw.Draw(im, 'RGBA')
d.rounded_rectangle((35, 570, 1045, 1120), radius=38, fill=(8, 8, 8, 220), outline=(255, 255, 255, 235), width=6)
font_path = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

def centered(y, text, fill, max_size):
    for size in range(max_size, 40, -1):
        font = ImageFont.truetype(font_path, size)
        box = d.textbbox((0, 0), text, font=font, stroke_width=4)
        if box[2] <= 940:
            break
    width = box[2] - box[0]
    d.text(((1080 - width) // 2, y), text, font=font, fill=fill, stroke_width=3, stroke_fill=(0, 0, 0, 255))

centered(610, 'LAF MI', (255, 255, 255, 255), 165)
centered(765, 'SOKTU?', (255, 255, 255, 255), 165)
d.rounded_rectangle((90, 950, 990, 1090), radius=24, fill=(255, 222, 40, 255), outline=(0, 0, 0, 255), width=5)
centered(960, 'BUNU SOR!', (15, 12, 8, 255), 130)
im.save(p / 'VID-002-img-1-v2.jpg', quality=93)
