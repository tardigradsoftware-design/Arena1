"""Synthesize a short two-note result chime; no external audio sources."""
import math, struct, wave
from pathlib import Path
rate=48000
duration=.82
samples=[]
for i in range(int(rate*duration)):
    t=i/rate
    value=0.0
    for start,f,amp in [(0,1046.5,.42),(.115,1568,.30)]:
        u=t-start
        if u>=0:
            env=(1-math.exp(-u*400))*math.exp(-u*6.8)
            value+=amp*env*(math.sin(2*math.pi*f*u)+.18*math.sin(2*math.pi*f*2.01*u))
    value*=min(1,(duration-t)*30)
    samples.append(round(max(-1,min(1,value))*32767))
p=Path(__file__).resolve().parent.parent/'public'/'sfx-result-chime.wav'
p.parent.mkdir(parents=True,exist_ok=True)
with wave.open(str(p),'wb') as w:
    w.setparams((1,2,rate,0,'NONE','not compressed'))
    w.writeframes(b''.join(struct.pack('<h',x) for x in samples))
