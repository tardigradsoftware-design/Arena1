"""Create a short synthesized descending light-beam effect, no recorded source."""
import math, struct, wave
from pathlib import Path
rate=48000
duration=.24
phase=0
samples=[]
for i in range(int(rate*duration)):
    t=i/rate
    frequency=1650*math.exp(-t*6)+390
    phase+=2*math.pi*frequency/rate
    envelope=(1-math.exp(-t*130))*math.exp(-t*14)
    value=.62*envelope*(math.sin(phase)+.14*math.sin(phase*2.02))
    samples.append(round(max(-1,min(1,value))*32767))
p=Path(__file__).resolve().parent.parent/'public'/'sfx-isin.wav'
p.parent.mkdir(parents=True,exist_ok=True)
with wave.open(str(p),'wb') as w:
    w.setparams((1,2,rate,0,'NONE','not compressed'))
    w.writeframes(b''.join(struct.pack('<h',x) for x in samples))
