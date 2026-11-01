"""Synthesize a short bubble-like pop (no external recordings)."""
import math
import struct
import wave
from pathlib import Path

rate = 48000
duration = .16
phase = 0.0
out = bytearray()
for i in range(int(rate * duration)):
    t = i / rate
    frequency = 480 + 550 * (1 - math.exp(-t * 26))
    phase += 2 * math.pi * frequency / rate
    envelope = (1 - math.exp(-t * 350)) * math.exp(-t * 27)
    sample = .55 * envelope * (math.sin(phase) + .15 * math.sin(2 * phase))
    out.extend(struct.pack('<h', int(max(-1, min(1, sample)) * 32767)))
path = Path(__file__).resolve().parent.parent / 'public' / 'VID-001-bubble.wav'
path.parent.mkdir(parents=True, exist_ok=True)
with wave.open(str(path), 'wb') as w:
    w.setparams ( (1, 2, rate, 0, 'NONE', 'not compressed') )
    w.writeframes(out)
