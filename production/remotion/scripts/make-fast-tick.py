"""Short synthetic tick; repeat at chosen frame spacing to evoke a fast clock."""
import math,random,struct,wave
from pathlib import Path
rate=48000;rng=random.Random(544);samples=[]
for i in range(int(.045*rate)):
 t=i/rate;env=(1-math.exp(-t*900))*math.exp(-t*125);x=env*(.45*math.sin(2*math.pi*2300*t)+.18*rng.uniform(-1,1));samples.append(round(max(-1,min(1,x))*32767))
p=Path(__file__).resolve().parent.parent/'public'/'sfx-fast-tick.wav';p.parent.mkdir(parents=True,exist_ok=True)
with wave.open(str(p),'wb') as w:
 w.setparams((1,2,rate,0,'NONE','not compressed'));w.writeframes(b''.join(struct.pack('<h',v) for v in samples))
