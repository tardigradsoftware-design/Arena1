"""Generate ten distinct, deterministic synthetic foam/pop audition clips."""
import math, random, struct, wave
from pathlib import Path

root = Path(__file__).resolve().parents[2] / 'audio' / 'foam-options'
root.mkdir(parents=True, exist_ok=True)
rate = 48000
# start time, frequency, amplitude, exponential decay, pitch-rise speed
presets = [
 [(0,420,.8,25,200)],
 [(0,680,.7,28,450),(.09,1100,.35,32,300)],
 [(0,950,.7,40,250)],
 [(0,300,.75,18,550),(.13,570,.3,25,300)],
 [(0,1100,.62,35,600),(.045,1500,.35,42,300),(.09,1900,.2,50,200)],
 [(0,520,.65,15,180),(.16,780,.3,24,150)],
 [(0,720,.65,42,-220),(.07,480,.45,32,-120)],
 [(0,380,.68,32,700),(.06,780,.38,36,600),(.12,1300,.25,42,500)],
 [(0,1500,.58,45,-300),(.06,1800,.36,48,-200),(.12,2200,.23,52,-200)],
 [(0,500,.62,22,450),(.10,650,.4,25,400),(.20,900,.28,30,350),(.29,1200,.18,35,300)],
]
for index, pops in enumerate(presets, 1):
    duration = max(p[0] for p in pops) + .24
    samples=[]
    for i in range(int(duration * rate)):
        t=i/rate; val=0
        for start, freq, amp, decay, rise in pops:
            u=t-start
            if u>=0:
                env=(1-math.exp(-u*500))*math.exp(-u*decay)
                phase=2*math.pi*(freq*u+rise*(u/35+math.exp(-35*u)/1225-1/1225))
                val+=amp*env*math.sin(phase)
        samples.append(max(-32767,min(32767,round(val*32767))))
    path=root/f'kopuk-sesi-{index:02d}.wav'
    with wave.open(str(path),'wb') as w:
        w.setparams((1,2,rate,0,'NONE','not compressed'))
        w.writeframes(b''.join(struct.pack('<h',s) for s in samples))
