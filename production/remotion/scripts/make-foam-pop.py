"""Generate a two-bubble synthetic foam pop in public/, without external assets."""
import math, struct, wave
from pathlib import Path
rate = 48000
samples=[]
for i in range(int(rate*.22)):
    t=i/rate
    total=0
    for start, freq, amp in [(0,690,0.68),(.064,1120,.38),(.102,1450,.18)]:
        u=t-start
        if u>=0:
            envelope=(1-math.exp(-u*700))*math.exp(-u*32)
            phase=2*math.pi*(freq*u + 1000*(u/35 + math.exp(-35*u)/1225-1/1225))
            total+=amp*envelope*math.sin(phase)
    samples.append(max(-32767,min(32767,round(total*32767))))
path=Path(__file__).resolve().parent.parent/'public'/'VID-001-foam-pop.wav'
path.parent.mkdir(parents=True,exist_ok=True)
with wave.open(str(path),'wb') as w:
    w.setparams((1,2,rate,0,'NONE','not compressed'))
    w.writeframes(b''.join(struct.pack('<h',s) for s in samples))
