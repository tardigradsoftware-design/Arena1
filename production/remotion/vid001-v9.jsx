import React from 'react';
import {AbsoluteFill, Audio, Composition, Img, Sequence, interpolate, registerRoot, spring, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
import captions from './vid001-captions.json';

const shots = [
 {from:0,file:'VID-001-a.png',focus:'50% 55%',scale:1.01},
 {from:98,file:'VID-001-a.png',focus:'50% 70%',scale:1.03},
 {from:188,file:'VID-001-b.png',focus:'50% 52%',scale:1.01},
 {from:275,file:'VID-001-b.png',focus:'50% 60%',scale:1.03},
 {from:338,file:'VID-001-c.png',focus:'50% 52%',scale:1.01},
 {from:460,file:'VID-001-d.png',focus:'50% 40%',scale:1.01},
 {from:550,file:'VID-001-d.png',focus:'50% 38%',scale:1.03},
];
const slideFrames=7;
const ease=(t)=>1-Math.pow(1-t,3);
const clamp={extrapolateLeft:'clamp',extrapolateRight:'clamp'};

function Background(){
 const f=useCurrentFrame();
 return <AbsoluteFill style={{backgroundColor:'#13110f',overflow:'hidden'}}>
  {shots.map((shot,i)=>{
    const next=shots[i+1]?.from??99999;
    if(f<shot.from || f>=next+slideFrames) return null;
    const p=interpolate(f-shot.from,[0,slideFrames],[0,1],clamp);
    const dir=i%2?1:-1;
    const x=i===0?0:dir*(1-ease(p))*720;
    const age=Math.max(f-shot.from,0); const zoom=shot.scale+0.045*ease(Math.min(age/100,1));
    return <AbsoluteFill key={i} style={{transform:`translateX(${x}px)`, overflow:'hidden'}}>
      <Img src={staticFile(shot.file)} style={{width:'100%',height:'100%',objectFit:'cover',objectPosition:shot.focus,transform:`scale(${zoom})`}}/>
      <AbsoluteFill style={{background:'linear-gradient(180deg,rgba(11,9,9,.22) 0%,rgba(11,9,9,0) 38%,rgba(11,9,9,.15) 100%)'}}/>
    </AbsoluteFill>;
  })}
 </AbsoluteFill>;
}
function Hook(){
 const f=useCurrentFrame();const {fps}=useVideoConfig();
 if(f>=60)return null;
 const entrance=spring({frame:f,fps,config:{damping:17,stiffness:230,mass:.7}});
 const opacity=interpolate(f,[0,2,48,59],[0.8,1,1,0],clamp);
 const scale=0.7+0.3*entrance;
 return <AbsoluteFill style={{opacity,pointerEvents:'none'}}>
    <div style={{position:'absolute',top:230,left:50,width:610,transform:`translateY(${(1-entrance)*-34}px) scale(${scale})`,transformOrigin:'center',fontFamily:'Arial, sans-serif',fontWeight:950,textAlign:'center',lineHeight:1.03,filter:'drop-shadow(0px 8px 6px rgba(0,0,0,.6))'}}>
     <div style={{display:'inline-block',fontSize:105,color:'#201510',background:'#ffe135',padding:'3px 32px 5px',transform:'rotate(-3deg)',borderRadius:8,letterSpacing:'-3px'}}>SAKIN!</div>
     <div style={{fontSize:42,color:'white',marginTop:14,textShadow:'0 3px 0 #000, 2px 2px 7px #000'}}>SARARAN KILIFLARI</div>
     <div style={{fontSize:46,color:'white',marginTop:3,textShadow:'0 3px 0 #000, 2px 2px 7px #000'}}>ÇÖPE ATMA<br/><span style={{color:'#ffe135'}}>YIPRATMA!</span></div>
    </div>
    <div style={{position:'absolute',left:75,top:240,width:31,height:10,background:'#fff',transform:`rotate(-25deg) scaleX(${entrance})`,borderRadius:8}}/>
    <div style={{position:'absolute',right:82,top:345,width:26,height:9,background:'#ffe135',transform:`rotate(30deg) scaleX(${entrance})`,borderRadius:8}}/>
 </AbsoluteFill>;
}
const C={ink:'#111111',paper:'#F8F9FA',dot:'#E2E5E9',red:'#E63946',green:'#10B981',yellow:'#F59E0B',blue:'#2563EB'};

// Word-linked timing is approximate (Vosk + interpolation), not verified alignment.
function Marker({type}) {
 if(type==='spoon') return <svg viewBox="0 0 100 100" width="72" height="72"><ellipse cx="36" cy="35" rx="19" ry="14" fill="#f3efe7" stroke="#25211b" strokeWidth="4"/><path d="M49 43 L81 78" stroke="#eee9df" strokeWidth="10" strokeLinecap="round"/><path d="M49 43 L81 78" stroke="#25211b" strokeWidth="3" strokeLinecap="round"/></svg>;
 if(type==='tablet') return <svg viewBox="0 0 100 100" width="72" height="72"><rect x="19" y="25" width="62" height="52" rx="13" fill="#eee8db" stroke="#25211b" strokeWidth="4"/><rect x="24" y="31" width="52" height="16" rx="5" fill="#5badb6"/><circle cx="50" cy="55" r="10" fill="#8bb9cb" stroke="#25211b" strokeWidth="3"/></svg>;
 if(type==='glass') return <svg viewBox="0 0 100 100" width="72" height="72"><path d="M28 20 Q49 26 72 20 L66 42 Q62 54 70 75 Q50 81 30 75 Q38 54 34 42 Z" fill="#d9eef1" fillOpacity=".9" stroke="#25211b" strokeWidth="4"/><path d="M35 53 Q50 57 65 53 L70 75 Q50 81 30 75Z" fill="#b7d7d4" fillOpacity=".65"/></svg>;
 return <svg viewBox="0 0 100 100" width="72" height="72"><path d="M26 14 H74 V86 L50 70 L26 86 Z" fill="#ffe135" stroke="#25211b" strokeWidth="5" strokeLinejoin="round"/></svg>;
}
// Timings derive from approximate word timestamps and still need listening review.
// Context-specific animated symbols, kept clear of the central captions.
function ContextArt({kind,age,side}){
 const {fps}=useVideoConfig();
 const p=spring({frame:Math.max(0,age-5),fps,config:{damping:16,stiffness:180,mass:.7}});
 const left=side==='left'?455:30;
 const alpha=interpolate(age,[0,5,12],[0,.55,1],clamp);
 return <div style={{position:'absolute',left,top:430,width:220,height:180,opacity:alpha,transform:`scale(${.75+.25*p})`,transformOrigin:'center',filter:'drop-shadow(3px 4px 0 rgba(0,0,0,.75))'}}>
 <svg viewBox="0 0 220 180" width="220" height="180">
  <rect x="16" y="17" width="187" height="145" rx="25" fill="#fffdf3" fillOpacity=".94" stroke="#211d19" strokeWidth="4"/>
  {kind==='fabric'&&<><path d="M45 62 Q108 42 174 62 L168 124 Q109 138 51 124 Z" fill="#fff9e6" stroke="#211d19" strokeWidth="4"/><path d="M59 72 Q110 61 160 72 M60 113 Q110 123 159 113" fill="none" stroke="#c9bda2" strokeWidth="3"/><path d="M150 34v22 M139 45h22 M42 127v17 M34 135h17" stroke="#f4bd00" strokeWidth="5" strokeLinecap="round"/></>}
  {kind==='spoon'&&<><ellipse cx="85" cy="77" rx="40" ry="23" fill="#f3f3f1" stroke="#211d19" strokeWidth="4"/><path d="M118 87 L166 125" stroke="#211d19" strokeWidth="13" strokeLinecap="round"/><path d="M118 87 L166 125" stroke="#e7e8e5" strokeWidth="7" strokeLinecap="round"/><circle cx="70" cy="70" r="3" fill="#c0b7a6"/><circle cx="87" cy="65" r="3" fill="#c0b7a6"/><circle cx="99" cy="77" r="3" fill="#c0b7a6"/></>}
  {kind==='tablet'&&<><rect x="68" y="40" width="90" height="100" rx="20" fill="#f4f2e9" stroke="#211d19" strokeWidth="4"/><path d="M70 68 H156" stroke="#4faeb9" strokeWidth="15"/><circle cx="113" cy="103" r="17" fill="#91c9d1" stroke="#211d19" strokeWidth="3"/></>}
  {kind==='glass'&&<><path d="M78 39 Q110 48 142 39 L133 79 Q129 93 140 135 Q110 144 80 135 Q91 93 87 79 Z" fill="#dff5f6" stroke="#211d19" strokeWidth="4"/><path d="M86 93 Q110 98 134 93 L140 135 Q110 144 80 135 Z" fill="#a4d6d8"/><path d="M160 66 Q174 82 160 88 Q147 82 160 66Z" fill="#80cbd2" stroke="#211d19" strokeWidth="3"/></>}
  {kind==='temp'&&<><circle cx="110" cy="90" r="51" fill="#e3f4f5" stroke="#211d19" strokeWidth="5"/><circle cx="110" cy="90" r="37" fill="none" stroke="#83cbd2" strokeWidth="6"/><path d="M80 93 Q100 67 130 89 T151 82" fill="none" stroke="#439aa6" strokeWidth="5" strokeLinecap="round"/><path d="M155 39 l12 -8 M162 51 l15 -1" stroke="#f4bd00" strokeWidth="5" strokeLinecap="round"/></>}
  {kind==='save'&&<><path d="M82 39 H141 V140 L111 120 L82 140 Z" fill="#ffe135" stroke="#211d19" strokeWidth="5" strokeLinejoin="round"/><path d="M154 54 l13 -9 M157 68 h15 M153 81 l13 9" stroke="#f4bd00" strokeWidth="5" strokeLinecap="round"/></>}
 </svg></div>;
}
function MotionGraphics(){
 const f=useCurrentFrame(),{fps}=useVideoConfig();
 const events=[
  {from:75,to:175,label:'SARARMIŞ', sub:'YASTIK KILIFLARI', kind:'fabric', side:'left'},
  {from:221,to:254,label:'1 YEMEK KAŞIĞI', sub:'KARBONAT',kind:'spoon',side:'left'},
  {from:255,to:286,label:'1 TABLET', sub:'BULAŞIK DETERJANI',kind:'tablet',side:'right'},
  {from:297,to:331,label:'YARIM ÇAY BARDAĞI', sub:'BEYAZ SİRKE',kind:'glass',side:'left'},
  {from:338,to:390,label:'60°',sub:'NORMAL PROGRAM',kind:'temp',side:'right'},
  {from:468,to:515,label:'BEYAZ',sub:'YASTIK KILIFLARI',kind:'fabric',side:'left'},
  {from:536,to:578,label:'KAYDET',sub:'LAZIM OLDUĞUNDA',kind:'save',side:'right'},
 ];
 const item=events.find(e=>f>=e.from&&f<e.to); if(!item)return null;
 const age=f-item.from;const p=spring({frame:age,fps,config:{damping:16,stiffness:230,mass:.65}});
 const fade=interpolate(f,[item.from,item.from+3,item.to-5,item.to],[0,1,1,0],clamp);
 const dir=item.side==='left'?-1:1; const rotation=dir*interpolate(p,[0,1],[7,2]);
 const line=interpolate(age,[3,14],[0,1],clamp); const scale=.75+.25*p;
 return <AbsoluteFill style={{opacity:fade,pointerEvents:'none'}}>
  <div style={{position:'absolute',left:item.side==='left'?46:undefined,right:item.side==='right'?46:undefined,top:225,display:'flex',gap:12,alignItems:'center',transform:`translateX(${dir*(1-p)*260}px) rotate(${rotation}deg) scale(${scale})`,transformOrigin:item.side==='left'?'left center':'right center',filter:'drop-shadow(0px 8px 9px rgba(0,0,0,.4))'}}>
   <div style={{width:94,height:94,flexShrink:0,display:'grid',placeItems:'center',background:'#fff9ea',border:'4px solid #211d19',borderRadius:22,boxShadow:'5px 5px 0 #211d19'}}>
    {item.kind==='temp'?<div style={{font:'900 39px Arial',color:'#211d19'}}>60°</div>:item.kind==='fabric'?<svg viewBox="0 0 100 100" width="68" height="68"><path d="M16 30 Q49 18 84 30 L80 72 Q50 79 20 72 Z" fill="#f9f5e9" stroke="#211d19" strokeWidth="5"/><path d="M25 38 Q50 32 75 38 M26 62 Q50 67 74 62" fill="none" stroke="#c8bdaa" strokeWidth="3"/></svg>:<Marker type={item.kind}/>}
   </div>
   <div style={{fontFamily:'Arial, sans-serif',fontWeight:900,color:'#211d19',lineHeight:1.05}}>
    <div style={{display:'table',background:'#ffe135',border:'3px solid #211d19',borderRadius:9,padding:'7px 12px',fontSize:item.kind==='temp'?36:25,boxShadow:'4px 4px 0 #211d19'}}>{item.label}</div>
    <div style={{display:'table',marginTop:7,background:'#fff9ea',border:'3px solid #211d19',borderRadius:9,padding:'7px 12px',fontSize:23,boxShadow:'4px 4px 0 #211d19'}}>{item.sub}</div>
   </div>
  </div>
  <ContextArt kind={item.kind} age={age} side={item.side}/>
  <svg viewBox="0 0 720 1280" style={{position:'absolute',inset:0,width:'100%',height:'100%',filter:'drop-shadow(0 2px 2px #111)'}}><path d={item.side==='left'?'M 110 370 C 115 403 145 418 185 430 M 185 430 L 169 412 M 185 430 L 163 434':'M 610 370 C 605 403 575 418 535 430 M 535 430 L 551 412 M 535 430 L 557 434'} fill="none" stroke="#ffe135" strokeWidth="6" strokeLinecap="round" strokeLinejoin="round" pathLength="1" strokeDasharray="1" strokeDashoffset={1-line}/></svg>
  {[0,1,2].map(i=><div key={i} style={{position:'absolute',top:380+i*20,left:item.side==='left'?55+i*13:undefined,right:item.side==='right'?55+i*13:undefined,width:8+i*2,height:8+i*2,borderRadius:'50%',background:i===1?'#fff':'#ffe135',transform:`scale(${Math.max(0,Math.min(1,(age-i*3)/8))})`}}/>)}
 </AbsoluteFill>;
}
function Caption(){const f=useCurrentFrame(),t=f/30;const cap=captions.find(c=>t>=c.start&&t<c.end);if(!cap||f<60)return null;const k=interpolate(f/30,[cap.start,cap.start+.08,cap.end],[.94,1.05,1],clamp);return <div style={{position:'absolute',top:795,left:42,right:42,display:'flex',justifyContent:'center',alignItems:'center',gap:9,font:'900 37px Arial',textAlign:'center'}}>{cap.words.map((w,i)=><span key={i} style={{background:i===cap.active?'#ffe135':'white',color:C.ink,border:'3px solid #111',boxShadow:'3px 3px 0 #111',borderRadius:8,padding:'7px 10px',transform:i===cap.active?`scale(${k}) rotate(-2deg)`:'none'}}>{w}</span>)}</div>}
function Video(){
 const f=useCurrentFrame();return <AbsoluteFill style={{backgroundColor:'#111',overflow:'hidden'}}>
  <Background/><Hook/><MotionGraphics/><Caption/>
  {((f>=65&&f<125)||(f>=300&&f<360)||(f>=540&&f<600))&&<div style={{position:'absolute',bottom:210,left:50,font:'bold 22px Arial',color:'white',textShadow:'0 2px 4px #000'}}>kadincayasam</div>}
  <Audio src={staticFile('VID-001-voice.wav')} volume={1}/><Audio src={staticFile('peaceful_days.mp3')} volume={.10}/>
  {/* Scene transitions: selected short whoosh; graphics: selected spring. */}
  {[98,188,275,338,460,550].map(n=><Sequence from={n} key={'transition'+n}><Audio src={staticFile('sfx-kisa-whoosh.wav')} volume={.38}/></Sequence>)}
  {[0,75,221,255,297,338,468,536].map(n=><Sequence from={n} key={'graphic'+n}><Audio src={staticFile('sfx-yay-ziplama.wav')} volume={.40}/></Sequence>)}
 </AbsoluteFill>;
}
function Root(){return <Composition id="VID001V9" component={Video} durationInFrames={620} fps={30} width={720} height={1280}/>}
registerRoot(Root);
