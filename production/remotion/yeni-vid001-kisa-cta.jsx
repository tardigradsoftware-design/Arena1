import React from 'react';
import {AbsoluteFill, Composition, Img, interpolate, registerRoot, spring, staticFile, useCurrentFrame, useVideoConfig} from 'remotion';
const clamp={extrapolateLeft:'clamp',extrapolateRight:'clamp'};
const clips=[
 {from:0,file:'test-parmak.png',position:'50% 52%'},
 {from:21,file:'yeni-mirror-close.png',position:'50% 51%'},
 {from:58,file:'test-parmak.png',position:'50% 52%'},
 {from:106,file:'yuzsuz-1.png',position:'50% 50%'},
 {from:170,file:'yeni-mirror-close.png',position:'50% 53%'},
 {from:224,file:'test-parmak.png',position:'50% 54%'},
 {from:282,file:'yuzsuz-1.png',position:'50% 54%'},
 {from:349,file:'yuzsuz-2.png',position:'50% 49%'},
 {from:415,file:'yeni-support.png',position:'50% 55%'},
 {from:505,file:'yuzsuz-2.png',position:'50% 50%'}
];
const text='Girdiğiniz soyunma kabinindeki aynaya tırnağınızı dayadığınızda parmağınızla yansımanız arasında boşluk yoksa hemen oradan çıkın! Gerçek aynalarda cam kalınlığından dolayı milimetrik bir boşluk kalır; boşluk olmaması arkadan izlenen çift taraflı bir cam olduğunu gösterir. Peki sen kabine girdiğinde ilk neyi kontrol edersin? Yorumlara yaz ki herkes öğrensin ve bu videoyu arkadaşına göndermeyi unutma.';
const captionText=text.split(' Yorumlara yaz')[0];
const words=captionText.split(/\s+/); const weights=words.map(w=>Math.max(2,w.replace(/[^\p{L}]/gu,'').length)); const total=weights.reduce((a,b)=>a+b,0);
let offset=0;const wordTime=words.map((w,i)=>{const start=offset/total*14.5;offset+=weights[i];return {word:w,start,end:offset/total*14.5};});
function Background(){const f=useCurrentFrame();const i=clips.reduce((n,c,j)=>f>=c.from?j:n,0);const c=clips[i], age=f-c.from;const p=interpolate(age,[0,20],[0,1],clamp);const zoom=(i%2===0?1.03+0.06*p:1.11-0.05*p);return <AbsoluteFill style={{overflow:'hidden',background:'#13100c'}}><Img src={staticFile('yenitest/'+c.file)} style={{width:'100%',height:'100%',objectFit:'cover',objectPosition:c.position,transform:`scale(${zoom}) translateX(${(i%2?1:-1)*5*p}px)`}}/><AbsoluteFill style={{background:'linear-gradient(180deg,rgba(0,0,0,.32),transparent 48%,rgba(0,0,0,.22))'}}/></AbsoluteFill>}
function Hook(){const f=useCurrentFrame(),{fps}=useVideoConfig();if(f>=67)return null;const p=spring({frame:f,fps,config:{damping:17,stiffness:220}});const opacity=interpolate(f,[0,3,55,67],[1,1,1,0],clamp);return <AbsoluteFill style={{opacity,pointerEvents:'none'}}><div style={{position:'absolute',left:85,right:85,top:255,textAlign:'center',fontFamily:'Arial, sans-serif',fontWeight:950,transform:`scale(${.82+.18*p})`,filter:'drop-shadow(0 8px 9px #000)'}}><div style={{color:'white',fontSize:62,textShadow:'0 3px 3px #000'}}>SOYUNMA KABİNİNDE</div><div style={{display:'inline-block',marginTop:12,background:'#ffe135',border:'5px solid #18140e',boxShadow:'8px 8px 0 #18140e',borderRadius:12,padding:'8px 24px',fontSize:86,color:'#18140e',transform:'rotate(-2deg)'}}>AYNAYI KONTROL ET!</div></div></AbsoluteFill>}
function Captions(){const f=useCurrentFrame(),t=f/30;if(f<67||t>=14.5)return null;const i=wordTime.findIndex(w=>t>=w.start&&t<w.end);if(i<0)return null;const pair=i-i%2;return <div style={{transform:`rotate(${i%2 ? 1 : -1}deg) scale(${0.96+0.04*spring({frame:Math.max(0,f-Math.round(wordTime[i].start*30)),fps:30,config:{damping:18,stiffness:200}})})`,position:'absolute',top:1190,left:45,right:45,display:'flex',justifyContent:'center',gap:10,font:'900 55px Arial, sans-serif',textAlign:'center',flexWrap:'wrap'}}>{wordTime.slice(pair,pair+2).map((w,k)=><span key={w.start} style={{background:pair+k===i?'#ffe135':'white',border:'4px solid #16120e',borderRadius:9,padding:'7px 12px',color:'#16120e',boxShadow:'4px 5px 0 #16120e'}}>{w.word}</span>)}</div>}
// Purpose-built scene overlays, not actual tracking or evidence of mirror type.
function MotionAnnotations(){
 const f=useCurrentFrame(),{fps}=useVideoConfig();
 const scenes=[
  {from:112,to:169,type:'mirror'},
  {from:288,to:348,type:'glass'},
  {from:359,to:410,type:'exit'}, {from:425,to:465,type:'message'}
 ];
 const e=scenes.find(x=>f>=x.from&&f<x.to);if(!e)return null;
 const age=f-e.from, length=e.to-e.from;
 const pop=spring({frame:age,fps,config:{damping:16,stiffness:190,mass:.75}});
 const fade=interpolate(age,[0,4,length-7,length],[0,1,1,0],clamp);
 const draw=interpolate(age,[2,16],[0,1],clamp);
 const pulse=1+0.018*Math.sin(age/7);
 const style={filter:'drop-shadow(0px 4px 4px rgba(0,0,0,.8))'};
 return <AbsoluteFill style={{opacity:fade,pointerEvents:'none'}}>
  {e.type==='finger'&&<svg viewBox="0 0 1080 1920" width="1080" height="1920" style={style}>
    <g transform={`translate(510 1010) scale(${(.75+.25*pop)*pulse})`}>
     <circle r="115" fill="none" stroke="#ffe135" strokeWidth="9" strokeDasharray="20 12"/>
     <circle r="95" fill="none" stroke="#ffffff" strokeWidth="3" opacity=".8"/>
    </g>
    <path d="M 770 800 C 730 850 685 875 630 905 M 630 905 L 660 903 M 630 905 L 645 880" fill="none" stroke="#ffe135" strokeWidth="9" strokeLinecap="round" strokeLinejoin="round" pathLength="1" strokeDasharray="1" strokeDashoffset={1-draw}/>
    <rect x="720" y="720" width="255" height="76" rx="16" fill="#ffe135" stroke="#14110e" strokeWidth="4"/>
    <text x="847" y="769" fill="#14110e" textAnchor="middle" fontFamily="Arial" fontWeight="900" fontSize="30">TEMAS NOKTASI</text>
   </svg>}
  {e.type==='mirror'&&<div style={{position:'absolute',top:380,left:65,display:'flex',gap:18,alignItems:'center',transform:`translateX(${(1-pop)*-180}px) rotate(-2deg)`,...style}}><div style={{background:'#fffdf4',border:'6px solid #17130f',borderRadius:22,padding:15,boxShadow:'7px 8px 0 #17130f'}}><svg width="100" height="100" viewBox="0 0 100 100"><rect x="24" y="8" width="52" height="80" rx="10" fill="#bce1e4" stroke="#17130f" strokeWidth="5"/><path d="M34 35l20-20M36 57l28-28" stroke="white" strokeWidth="5"/></svg></div><div style={{display:'flex',flexDirection:'column',gap:10,font:'900 39px Arial',color:'#17130f'}}><div style={{background:'#ffe135',border:'5px solid #17130f',borderRadius:10,padding:'8px 16px',boxShadow:'5px 6px 0 #17130f'}}>SOYUNMA KABİNİ</div><div style={{background:'#fffdf4',border:'5px solid #17130f',borderRadius:10,padding:'8px 16px',boxShadow:'5px 6px 0 #17130f',alignSelf:'flex-start'}}>AYNA</div></div></div>}
  {e.type==='glass'&&<div style={{position:'absolute',top:400,right:70,width:365,transform:`translateX(${(1-pop)*180}px)`,...style}}>
   <svg viewBox="0 0 360 220" width="360" height="220"><rect x="18" y="18" width="324" height="184" rx="20" fill="#fff9ee" stroke="#15120e" strokeWidth="7"/><rect x="108" y="43" width="30" height="134" rx="7" fill="#83cad7" stroke="#15120e" strokeWidth="4"/><path d="M48 75 H93 M48 145 H93 M263 75 H315 M263 145 H315" stroke="#15120e" strokeWidth="6" strokeLinecap="round"/><path d="M162 72 H235 M162 145 H235" stroke="#e8a800" strokeWidth="7" strokeLinecap="round"/><path d="M222 60 L237 72 L222 84 M222 133 L237 145 L222 157" fill="none" stroke="#e8a800" strokeWidth="6"/></svg>
   <div style={{font:'900 30px Arial',color:'#15120e',background:'#ffe135',border:'4px solid #15120e',borderRadius:10,textAlign:'center',padding:9}}>CAM YÜZEYİ · TEMSİLİ</div>
  </div>}
  {e.type==='exit'&&<div style={{position:'absolute',top:420,left:85,display:'flex',gap:15,alignItems:'center',transform:`translateX(${(1-pop)*-180}px)`,...style}}>
   <svg width="130" height="130" viewBox="0 0 100 100"><rect x="20" y="10" width="50" height="78" rx="7" fill="#fff7e4" stroke="#14110e" strokeWidth="5"/><circle cx="58" cy="50" r="4" fill="#14110e"/><path d="M35 50 H88 M73 35 L88 50 L73 65" fill="none" stroke="#e6aa00" strokeWidth="8" strokeLinecap="round" strokeLinejoin="round"/></svg>
   <div style={{font:'900 38px Arial',color:'#15120e',background:'#ffe135',border:'4px solid #15120e',borderRadius:12,padding:'12px 18px'}}>KABİNDEN ÇIK</div>
  </div>}
  {e.type==='message'&&<div style={{position:'absolute',top:420,right:80,transform:`scale(${.7+.3*pop})`,...style}}>
   <svg width="150" height="150" viewBox="0 0 100 100"><path d="M12 15 H88 Q95 15 95 23 V67 Q95 75 87 75 H50 L30 90 V75 H13 Q5 75 5 67 V23 Q5 15 12 15Z" fill="#ffe135" stroke="#15120e" strokeWidth="5" strokeLinejoin="round"/><circle cx="30" cy="46" r="5" fill="#15120e"/><circle cx="50" cy="46" r="5" fill="#15120e"/><circle cx="70" cy="46" r="5" fill="#15120e"/></svg>
  </div>}
 </AbsoluteFill>
}
function CTA(){const f=useCurrentFrame(),{fps}=useVideoConfig();if(f<490||f>=548)return null;const age=f-490;const fade=interpolate(f,[490,495,539,548],[0,1,1,0],clamp);const items=[['BEĞEN','M12 21h-4V10h4m0 11h7a2 2 0 0 0 2-1.6l1-7A2 2 0 0 0 20 10h-5l.6-3.1C16 4.8 14.8 3 13 3l-1 5-3 3v10'],['YORUM','M4 4h16a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-8l-5 4v-4H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z'],['PAYLAŞ','M4 19c1-7 5-10 12-10V5l6 7-6 7v-4C10 15 7 16 4 19z'],['KAYDET','M6 3h12v18l-6-4-6 4z']];return <AbsoluteFill style={{opacity:fade,background:'linear-gradient(180deg,rgba(12,11,10,.35),rgba(12,11,10,.7))',pointerEvents:'none'}}><div style={{position:'absolute',top:300,left:55,right:55,textAlign:'center',color:'white',font:'900 46px Arial',textShadow:'0 5px 8px #000'}}>YORUMLARA YAZ!<br/>ARKADAŞINA GÖNDERMEYİ UNUTMA!</div><div style={{position:'absolute',top:510,left:65,right:65,display:'flex',justifyContent:'space-around'}}>{items.map(([label,path],i)=>{let t=age, click=7+i*5;let p=spring({frame:t,fps,config:{damping:17,stiffness:200}});let tap=interpolate(t,[click-2,click,click+3],[1,.80,1],clamp);let burst=interpolate(t,[click,click+2,click+9],[0,1,0],clamp);return <div key={label} style={{textAlign:'center',transform:`scale(${p*tap})`,color:'white',font:'900 32px Arial',textShadow:'0 3px 5px #000'}}><svg viewBox="0 0 100 100" width="155" height="155" style={{position:'absolute',top:-22,left:'50%',transform:'translateX(-50%)',overflow:'visible',opacity:burst,pointerEvents:'none'}}>{Array.from({length:8},(_,j)=>{let angle=j*Math.PI/4;let radius=35+Math.max(0,t-click)*2;return <circle key={j} cx={50+Math.cos(angle)*radius} cy={50+Math.sin(angle)*radius} r={j%2?3:5} fill={j%2?'#fff':'#ffe135'}/>})}</svg><svg viewBox="0 0 24 24" width="112" height="112" style={{display:'block',margin:'0 auto 12px',filter:'drop-shadow(0 5px 5px #000)'}}><path d={path} fill="#fa2028" stroke="white" strokeWidth="1.2" strokeLinejoin="round" strokeLinecap="round"/></svg>{label}</div>})}</div>{(()=>{let t=age,p=spring({frame:t,fps,config:{damping:17,stiffness:200}}),tap=interpolate(t,[25,27,30],[1,.85,1],clamp),burst=interpolate(t,[27,29,36],[0,1,0],clamp);return <div style={{position:'absolute',top:780,left:140,right:140,borderRadius:100,background:'#ef1b24',padding:'25px',textAlign:'center',font:'900 55px Arial',color:'white',boxShadow:'0 7px 0 #8e1118,0 12px 15px #0008',transform:`scale(${p*tap})`}}><svg viewBox="0 0 700 100" width="100%" height="120" style={{position:"absolute",left:0,top:-10,opacity:burst,overflow:"visible"}}>{Array.from({length:10},(_,i)=>{let a=i*Math.PI/5,r=40+Math.max(0,t-27)*5;return <circle key={i} cx={350+Math.cos(a)*r} cy={50+Math.sin(a)*r} r={i%2?5:8} fill={i%2?"#fff":"#ffe135"}/>})}</svg><svg viewBox="0 0 24 24" width="58" height="58" style={{verticalAlign:'middle',marginRight:20}}><path fill="white" d="M12 2a2 2 0 0 1 2 2 7 7 0 0 1 5 7v4l2 3v1H3v-1l2-3v-4a7 7 0 0 1 5-7 2 2 0 0 1 2-2zm-2 19h4a2 2 0 0 1-4 0z"/></svg>ABONE OL</div>})()}</AbsoluteFill>}
function Video(){return <AbsoluteFill><Background/><Hook/><MotionAnnotations/><Captions/><CTA/></AbsoluteFill>}
function Root(){return <Composition id="Yeni001Grafik" component={Video} durationInFrames={607} fps={30} width={1080} height={1920}/>};registerRoot(Root);
