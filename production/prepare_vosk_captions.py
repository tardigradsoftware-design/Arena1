"""Build approximate Vosk-anchored captions and editable VID-002 scene plan."""
import difflib, json, re, sys, xml.etree.ElementTree as ET, zipfile
from pathlib import Path
import numpy as np
root=Path(__file__).resolve().parent.parent
num=int(sys.argv[1]); vid=f'VID-{num:03d}'
r=ET.fromstring(zipfile.ZipFile(root/'google_drive/Senryolar.ods').read('content.xml'))
ns={'x':'urn:oasis:names:tc:opendocument:xmlns:text:1.0'}
raw=next(''.join(p.itertext()) for p in r.findall('.//x:p',ns) if ''.join(p.itertext()).startswith(vid+';'))
text=raw.split(';',3)[3].split(';Vertical',1)[0]
words=re.findall(r'[\wÇĞİÖŞÜçğıöşü]+(?:[’\'][\w]+)?[.,!?]?',text)
result=json.loads((root/f'production/audio/{vid}-audit.json').read_text())
found=result['vosk_words']; duration=result['seconds_analyzed']
def norm(x): return re.sub(r'[^\w]','',x.lower().replace('ı','i'))
a=[norm(x) for x in words];b=[norm(x['word']) for x in found]
match=difflib.SequenceMatcher(None,a,b,autojunk=False)
anchors={}
for block in match.get_matching_blocks():
 for k in range(block.size): anchors[block.a+k]=(found[block.b+k]['start'],found[block.b+k]['end'])
points=[(-1,0.)]+[(i,(v[0]+v[1])/2) for i,v in sorted(anchors.items())]+[(len(words),duration)]
centers=np.interp(range(len(words)),[x[0] for x in points],[x[1] for x in points]);bounds=[0]+[(centers[i-1]+centers[i])/2 for i in range(1,len(words))]+[duration]
caps=[]
for i in range(len(words)):
 j=i//2*2
 caps.append({'start':round(float(bounds[i]),3),'end':round(float(bounds[i+1]),3),'words':words[j:j+2], 'active':i-j})
(root/f'production/remotion/vid{num:03d}-captions.json').write_text(json.dumps(caps,ensure_ascii=False,indent=2))
for i,w in enumerate(words): print(i,w,round(float(bounds[i]),2),round(float(bounds[i+1]),2),'matched' if i in anchors else 'estimate')
print('Vosk exact anchors',len(anchors),'/',len(words),'duration',duration)
