#!/usr/bin/env python3
"""Create a readable VID-001 cover using the existing face-free mirror image."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
p = Path(__file__).parent / 'VID-001'
im = ImageOps.fit(Image.open(p / 'test-parmak.png').convert('RGB'), (1080, 1920))
d = ImageDraw.Draw(im, 'RGBA')
d.rounded_rectangle((45, 470, 1035, 990), radius=32, fill=(10, 9, 8, 225), outline=(255, 255, 255, 240), width=6)
font_path = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def line(y, text, color, maximum):
    for size in range(maximum, 40, -1):
        font = ImageFont.truetype(font_path, size)
        bbox = d.textbbox((0, 0), text, font=font, stroke_width=3)
        if bbox[2] - bbox[0] <= 920:
            break
    d.text(((1080 - (bbox[2] - bbox[0])) // 2, y), text, font=font, fill=color, stroke_width=3, stroke_fill=(0, 0, 0, 255))
line(490, 'AYNADA', (255, 255, 255, 255), 150)
line(645, 'BU DETAYA', (255, 255, 255, 255), 145)
d.rounded_rectangle((95, 805, 985, 950), radius=22, fill=(255, 222, 40, 255), outline=(0, 0, 0, 255), width=5)
line(820, 'DİKKAT!', (14, 12, 8, 255), 125)
im.save(p / 'VID-001-img-1.jpg', quality=93)
im.resize((180, 320)).save('/tmp/vid001-kapak-kucuk.jpg', quality=90)
