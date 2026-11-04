"""Synthesize a short, elastic spring-like sound for graphic entrances."""
import math
import struct
import wave
from pathlib import Path
rate = 48000
duration = .32
phase = 0.0
samples = []
for i in range(int(rate * duration)):
    t = i / rate
    frequency = 490 + 350 * math.exp(-8*t) * math.sin(2*math.pi*8*t + 1.2)
    phase += 2*math.pi*frequency/rate
    envelope = (1-math.exp(-t*250))*math.exp(-t*13) * min(1, (duration-t)*55)
    v = .62*envelope*(math.sin(phase) + .16*math.sin(2*phase+.3))
    samples.append(round(max(-1,min(1,v))*32767))
p=Path(__file__).resolve().parent.parent/'public'/'sfx-yay-yeni.wav'
p.parent.mkdir(parents=True,exist_ok=True)
with wave.open(str(p),'wb') as w:
    w.setparams((1,2,rate,0,'NONE','not compressed'))
    w.writeframes(b''.join(struct.pack('<h',x) for x in samples))
