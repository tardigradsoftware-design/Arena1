"""Generate 20 distinct, synthetic, royalty-free SFX audition WAV files."""
import math, random, struct, wave
from pathlib import Path
rate=48000
out=Path(__file__).resolve().parents[2]/'audio'/'sfx-selection'
out.mkdir(parents=True,exist_ok=True)
items=[('01-pop','pop',.32),('02-cift-pop','double',.4),('03-kopuk','bubble',.45),('04-kisa-whoosh','whoosh',.4),('05-uzun-whoosh','swoosh',.8),('06-tik','click',.24),('07-dijital-bip','beep',.35),('08-pozitif-bildirim','up',.6),('09-cam-ting','glass',.7),('10-parilti','sparkle',.9),('11-ahsap-tik','wood',.35),('12-yumusak-vurus','thump',.48),('13-derin-vurus','boom',.7),('14-kaydirma','slide',.55),('15-yay-ziplama','spring',.6),('16-su-damlasi','drop',.5),('17-kagit-hisirtisi','paper',.6),('18-ters-gecis','reverse',.7),('19-dijital-onay','confirm',.6),('20-kisa-davul','drum',.45)]
for num,(name,kind,dur) in enumerate(items):
 rng=random.Random(922+num); data=[]; prev=0; phase=0
 for i in range(round(rate*dur)):
  t=i/rate; noise=rng.uniform(-1,1); prev=.86*prev+.14*noise
  def tone(freq,decay,start=0,amp=1):
   u=t-start
   return 0 if u<0 else amp*math.exp(-u*decay)*math.sin(2*math.pi*freq*u)
  if kind in ('pop','double','bubble','drop'):
   specs={'pop':[(0,550,.65)],'double':[(0,620,.6),(.12,850,.45)],'bubble':[(0,370,.65),(.11,760,.35),(.21,1200,.2)],'drop':[(0,1150,.6)]}[kind]; val=0
   for start,f,a in specs:
    u=t-start
    if u>=0:
     env=(1-math.exp(-u*700))*math.exp(-u*(20 if kind=='drop' else 30));val+=a*env*math.sin(2*math.pi*(f*u+140*(1-math.exp(-u*30))/30))
  elif kind in ('whoosh','swoosh','slide','reverse','paper'):
   x=t/dur; env=math.sin(math.pi*x)**(1.5 if kind!='reverse' else .4)
   if kind=='reverse': env=x*x
   if kind=='paper': env*=.55+.45*math.sin(80*t)**2
   if kind=='slide': val=.55*env*(noise-prev)+.12*env*math.sin(2*math.pi*(300*t+400*t*t))
   else: val=env*(.65*(noise-prev) if kind in ('whoosh','paper') else 1.4*prev)
  elif kind=='click': val=.7*math.exp(-t*100)*noise+.3*tone(1400,90)
  elif kind=='wood': val=tone(520,35,amp=.48)+tone(780,45,amp=.2)+.2*noise*math.exp(-t*75)
  elif kind in ('beep','up','confirm'):
   pitches={'beep':[(0,850)],'up':[(0,660),(.13,990)],'confirm':[(0,720),(.11,920),(.22,1200)]}[kind]
   val=sum(tone(f,12,start,.38)*(1-math.exp(-max(0,t-start)*200)) for start,f in pitches)
  elif kind in ('glass','sparkle'):
   freqs=([1250,2100,3250] if kind=='glass' else [1500,2200,2800,3600]);val=sum(tone(f,5+j*2,j*.055,.32/(j+1)) for j,f in enumerate(freqs))
  elif kind in ('thump','boom','drum'):
   phase+=2*math.pi*((70 if kind=='boom' else 115)+(190*math.exp(-t*26)))/rate
   val=.72*math.sin(phase)*math.exp(-t*(8 if kind=='boom' else 16))+.22*noise*math.exp(-t*(45 if kind=='drum' else 65))
  else: # elastic pitch sweep
   phase+=2*math.pi*(180+900*math.exp(-t*9)+100*math.sin(t*35)*math.exp(-t*8))/rate
   val=.62*math.sin(phase)*math.exp(-t*8)
  val*=min(1,t*400) * min(1,(dur-t)*120)
  data.append(round(max(-.92,min(.92,val))*32767))
 with wave.open(str(out/f'{name}.wav'),'wb') as w:
  w.setparams((1,2,rate,0,'NONE','not compressed'));w.writeframes(b''.join(struct.pack('<h',x) for x in data))
