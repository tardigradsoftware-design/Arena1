import os,sys,re,json,wave,subprocess,difflib,zipfile,xml.etree.ElementTree as ET
import argparse
import numpy as np
import imageio_ffmpeg
from vosk import Model,KaldiRecognizer,SetLogLevel
root=os.path.dirname(os.path.abspath(__file__)); ff=imageio_ffmpeg.get_ffmpeg_exe(); SetLogLevel(-1); model=Model(root+'/vosk-tr')
r=ET.fromstring(zipfile.ZipFile('google_drive/Senryolar.ods').read('content.xml')); ns={'x':'urn:oasis:names:tc:opendocument:xmlns:text:1.0'}
def norm(s): return re.sub(r'[^\w]','',s.lower().replace('ı','i'))
def stamp(t):
 t=max(0,t); return '%d:%02d:%05.2f'%(int(t//3600),int(t//60)%60,t%60)
parser = argparse.ArgumentParser(description='Render a script-faithful 9:16 video; inspect visuals and timing before publishing.')
parser.add_argument('videos', nargs='+', type=int)
parser.add_argument('--music', default=root+'/assets/peaceful_days.mp3', help='Licensed music bed')
parser.add_argument('--foley', help='Optional scene-appropriate licensed sound file')
parser.add_argument('--foley-at', type=float, default=0, help='Foley start time in seconds')
args = parser.parse_args()
if not os.path.isfile(args.music): parser.error('Music file not found')
if args.foley and not os.path.isfile(args.foley): parser.error('Foley file not found')
if args.foley_at < 0: parser.error('Foley start must be non-negative')
for num in args.videos:
 id=f'VID-{num:03d}'; raw=next(''.join(p.itertext()) for p in r.findall('.//x:p',ns) if ''.join(p.itertext()).startswith(id+';')); text=raw.split(';',3)[3].split(';Vertical',1)[0]; words=re.findall(r'[\wÇĞİÖŞÜçğıöşü]+(?:[’\'][\w]+)?[.,!?]?',text)
 wav=f'{root}/audio/{id}-fast.wav'; subprocess.run([ff,'-y','-loglevel','error','-i',f'{root}/audio/{id}.wav','-filter:a','atempo=1.45','-ar','16000','-ac','1',wav],check=True)
 w=wave.open(wav); dur=w.getnframes()/w.getframerate(); rec=KaldiRecognizer(model,16000);rec.SetWords(True); found=[]
 while True:
  b=w.readframes(4000)
  if not b: break
  if rec.AcceptWaveform(b): found += json.loads(rec.Result()).get('result',[])
 found+=json.loads(rec.FinalResult()).get('result',[]); w.close()
 a=[norm(x) for x in words];b=[norm(x['word']) for x in found];sm=difflib.SequenceMatcher(None,a,b,autojunk=False); anchors={}
 for block in sm.get_matching_blocks():
  for k in range(block.size): anchors[block.a+k]=(found[block.b+k]['start'],found[block.b+k]['end'])
 points=[(-1,0.0)]+[(i,(v[0]+v[1])/2) for i,v in sorted(anchors.items())]+[(len(words),dur)]; centers=np.interp(range(len(words)),[x[0] for x in points],[x[1] for x in points]); bounds=[0]+[(centers[i-1]+centers[i])/2 for i in range(1,len(words))]+[dur]
 ass=f'{root}/audio/{id}.ass'; header='''[Script Info]\nScriptType: v4.00+\nPlayResX: 720\nPlayResY: 1280\n[V4+ Styles]\nFormat: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding\nStyle: Default,DejaVu Sans,46,&H00FFFFFF,&H0000FFFF,&H00101010,&H88000000,-1,0,0,0,100,100,0,0,1,3,1,5,40,40,10,1\nStyle: Water,DejaVu Sans,25,&H55FFFFFF,&H00FFFFFF,&H77000000,&H88000000,0,0,0,0,100,100,0,0,1,1,0,2,40,40,200,1\n[Events]\nFormat: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text\n'''
 with open(ass,'w') as f:
  f.write(header)
  for i,word in enumerate(words):
   j=i//2*2; chunk=[]
   for n in range(j,min(j+2,len(words))): chunk.append((' {\\c&H00FFFF&}' if n==i else ' {\\c&HFFFFFF&}')+words[n])
   f.write('Dialogue: 0,%s,%s,Default,,0,0,0,,%s\n'%(stamp(bounds[i]),stamp(bounds[i+1]),''.join(chunk).strip()))
  for t in (2,10,18):
   if t<dur: f.write('Dialogue: 0,%s,%s,Water,,0,0,0,,{\\fad(400,400)}kadincayasam\n'%(stamp(t),stamp(min(t+2.5,dur))))
 cuts = [7.79, 10.84, 13.70] if num == 35 else [dur*.25, dur*.5, dur*.75]
 cmd=[ff,'-y','-loglevel','error'];
 lengths = [cuts[0], cuts[1]-cuts[0], cuts[2]-cuts[1], dur-cuts[2]]
 for i in range(1,5):cmd+=['-loop','1','-framerate','30','-t',str(lengths[i-1]+.1),'-i',f'{root}/images/{id}-{i}.png']
 cmd+=['-i',wav,'-stream_loop','-1','-i',args.music,'-i',root+'/assets/whoosh.wav'];
 if args.foley: cmd += ['-i', args.foley]
 filters=[]
 for i in range(4): filters.append(f'[{i}:v]scale=756:1344:force_original_aspect_ratio=increase,crop=756:1344,zoompan=z=\'min(1.035,1+on*0.00016)\':x=\'iw/2-iw/zoom/2\':y=\'ih/2-ih/zoom/2\':d=1:s=720x1280:fps=30,setsar=1,trim=duration={lengths[i]},setpts=PTS-STARTPTS[v{i}]')
 filters+=['[v0][v1][v2][v3]concat=n=4:v=1:a=0,ass='+ass+'[v]', f'[5:a]volume=0.10,atrim=duration={dur},afade=t=out:st={max(0,dur-1)}:d=1[music]', '[6:a]asplit=3[w0][w1][w2]']
 tracks=['[4:a]','[music]']
 for i,t in enumerate(cuts):
  delay=int(max(0,t-.15)*1000); filters.append(f'[w{i}]volume=0.13,adelay={delay}:all=1[fx{i}]'); tracks.append(f'[fx{i}]')
 if args.foley:
  filters.append(f'[7:a]volume=0.13,adelay={int(args.foley_at*1000)}:all=1[foley]'); tracks.append('[foley]')
 filters.append(''.join(tracks)+f'amix=inputs={len(tracks)}:duration=first:normalize=0,alimiter=limit=0.95[a]')
 out=f'{root}/videos/{id}.mp4';os.makedirs(os.path.dirname(out),exist_ok=True)
 cmd+=['-filter_complex',';'.join(filters),'-map','[v]','-map','[a]','-r','30','-c:v','libx264','-preset','veryfast','-crf','24','-pix_fmt','yuv420p','-c:a','aac','-b:a','96k','-movflags','+faststart','-t',str(dur),out];subprocess.run(cmd,check=True);print(id,'duration',round(dur,2),'ASR matches',len(anchors),'/',len(words),'MB',round(os.path.getsize(out)/1e6,2),flush=True)
