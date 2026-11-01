"""Deterministic synthetic hook sweep and save confirmation effects."""
import math
import random
import struct
import wave
from pathlib import Path
rate=48000
out=Path(__file__).resolve().parent.parent/'public'
out.mkdir(parents=True,exist_ok=True)

def write(name, samples):
    with wave.open(str(out/name),'wb') as w:
        w.setparams((1,2,rate,0,'NONE','not compressed'))
        w.writeframes(b''.join(struct.pack('<h',round(max(-.95,min(.95,v))*32767)) for v in samples))

# A short rising shimmer with a low impact and bright accent: not an actual recording.
rng=random.Random(31); phase=0; low=0; hook=[]
for i in range(int(.85*rate)):
    t=i/rate
    phase+=2*math.pi*(340+1050*(t/.85)**1.6)/rate
    n=rng.uniform(-1,1);low=.94*low+.06*n
    swell=math.sin(math.pi*min(t/.85,1))**2
    impact=math.exp(-t*19)*math.sin(2*math.pi*(125*t-180*t*t))
    high=0 if t<.57 else math.exp(-(t-.57)*9)*math.sin(2*math.pi*1880*(t-.57))
    hook.append(.28*swell*math.sin(phase)+.24*swell*low+.40*impact+.16*high)
write('sfx-hook-merak.wav',hook)

# An intentional soft click followed by a short double confirmation note.
rng=random.Random(98); save=[]
for i in range(int(.48*rate)):
    t=i/rate
    click=.24*rng.uniform(-1,1)*math.exp(-t*120)
    notes=0
    for start,freq,amp in [(0.018,880,.32),(.10,1320,.25)]:
        u=t-start
        if u>=0: notes+=amp*(1-math.exp(-u*300))*math.exp(-u*15)*math.sin(2*math.pi*freq*u)
    save.append(click+notes)
write('sfx-kaydet.wav',save)
