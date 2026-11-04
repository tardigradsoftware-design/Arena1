#!/usr/bin/env python3
"""Generate original synthesized mono 48 kHz interface SFX used by the series mixer."""
import math, random, struct, wave
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'public';p.mkdir(exist_ok=True);rate=48000
for name,duration in [('sfx-isin.wav',.32),('sfx-fast-tick.wav',.045),('sfx-kaydet.wav',.18)]:
 rng=random.Random(name);values=[];prev=0.0
 for i in range(int(duration*rate)):
  t=i/rate
  if name=='sfx-isin.wav':
   prev=.84*prev+.16*rng.uniform(-1,1); env=math.sin(math.pi*t/duration)**2; x=env*(.45*prev+.22*math.sin(2*math.pi*(520*t-480*t*t)))
  elif name=='sfx-fast-tick.wav':
   env=math.exp(-80*t);x=env*(.45*rng.uniform(-1,1)+.24*math.sin(2*math.pi*2700*t))
  else:
   env=math.exp(-20*t);x=env*(.45*math.sin(2*math.pi*760*t)+.22*math.sin(2*math.pi*1140*t))
  values.append(struct.pack('<h',int(32767*max(-1,min(1,x)))))
 with wave.open(str(p/name),'wb') as w:w.setparams((1,2,rate,len(values),'NONE','not compressed'));w.writeframes(b''.join(values))
