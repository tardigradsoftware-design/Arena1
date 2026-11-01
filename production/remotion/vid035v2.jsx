import React from 'react';
import {AbsoluteFill,Audio,Composition,Img,Sequence,interpolate,registerRoot,spring,staticFile,useCurrentFrame,useVideoConfig} from 'remotion';
import captions from './captions.json';
const c={extrapolateLeft:'clamp',extrapolateRight:'clamp'};
const shots=[
 {s:0,e:2.30,img:'VID-035-1.png',pan:'top'},
 {s:2.30,e:3.60,img:'VID-035-v2-2.png',pan:'bottom'},
 {s:3.60,e:5.16,img:'VID-035-1.png',pan:'top'},
 {s:5.16,e:7.84,img:'VID-035-v2-4.png',pan:'bottom'},
 {s:7.84,e:9.41,img:'VID-035-2.png',pan:'middle'},
 {s:9.41,e:11.09,img:'VID-035-4.png',pan:'middle'},
 {s:11.09,e:12.73,img:'VID-035-3.png',pan:'middle'},
 {s:12.73,e:14.14,img:'VID-035-v2-8.png',pan:'middle'},
 {s:14.14,e:15.33,img:'VID-035-v2-9.png',pan:'bottom'},
 {s:15.33,e:17.50,img:'VID-035-v2-10.png',pan:'middle'},
 {s:17.50,e:19.29,img:'VID-035-v2-11.png',pan:'bottom'},
 {s:19.29,e:20.97,img:'VID-035-4.png',pan:'bottom'},
];
function Background(){let f=useCurrentFrame();let t=f/30; return <AbsoluteFill style={{background:'#201c18',overflow:'hidden'}}>{shots.map((s,i)=>{
 if(t<s.s||t>=s.e+.16)return null;
 let local=f-Math.round(s.s*30); let slide=[4,6,9].includes(i); let p=interpolate(local,[0,5],[0,1],c); let x=slide?(1-p)*(i===6?-720:720):0;
 let alpha= i===0||slide?1:interpolate(local,[0,4],[0,1],c);
 let z=interpolate(local,[0,Math.max(1,(s.e-s.s)*30)],[1.015,i%2?1.035:1.022],c);
 return <AbsoluteFill key={i} style={{opacity:alpha,transform:`translateX(${x}px)`,overflow:'hidden'}}><Img src={staticFile(s.img)} style={{width:'100%',height:'100%',objectFit:'cover',objectPosition:s.pan==='top'?'50% 36%':s.pan==='bottom'?'50% 70%':'50% 50%',transform:`scale(${z})`}}/><AbsoluteFill style={{background:'linear-gradient(180deg,rgba(18,12,9,.17),transparent 45%,rgba(18,12,9,.12))'}}/></AbsoluteFill>;
 })}</AbsoluteFill>}
function Hook(){let f=useCurrentFrame();let {fps}=useVideoConfig();if(f>=69)return null;let p=spring({frame:f,fps,config:{damping:18,stiffness:230,mass:.7}});let opacity=interpolate(f,[0,3,59,68],[1,1,1,0],c);return <AbsoluteFill style={{opacity,pointerEvents:'none'}}><div style={{position:'absolute',top:225,left:45,width:620,transform:`scale(${.76+.24*p})`,textAlign:'center',fontFamily:'Arial,sans-serif',fontWeight:950,lineHeight:1,filter:'drop-shadow(0 7px 6px rgba(0,0,0,.65))'}}><div style={{display:'inline-block',fontSize:105,letterSpacing:'-3px',background:'#ffe135',color:'#1b160d',padding:'4px 32px',borderRadius:8,transform:'rotate(-3deg)'}}>SAKIN!</div><div style={{fontSize:44,color:'white',marginTop:14}}>SOĞAN DOĞRARKEN</div><div style={{fontSize:48,color:'white',marginTop:4}}>GÖZYAŞLARINA<br/><span style={{color:'#ffe135'}}>BOĞULUP...</span></div></div></AbsoluteFill>}
function Captions(){let f=useCurrentFrame(),t=f/30;let cap=captions.find(x=>t>=x.start&&t<x.end);if(!cap||f<69)return null;return <div style={{position:'absolute',top:640,left:35,width:650,transform:'translateY(-50%)',textAlign:'center',fontFamily:'Arial,sans-serif',fontSize:46,fontWeight:900,color:'white',lineHeight:1.18,textShadow:'0 3px 1px #000, 0 0 8px #000, 2px 2px 4px #000',WebkitTextStroke:'1px #141414'}}>{cap.words.map((w,i)=><React.Fragment key={i}><span style={{color:i===cap.active?'#ffe230':'#fff'}}>{w}</span>{i<cap.words.length-1?' ':''}</React.Fragment>)}</div>}
function Details(){let f=useCurrentFrame();let {fps}=useVideoConfig();let tags=[{a:284,b:326,text:'SU DOLU BİR BARDAK',icon:'drop',y:890},{a:387,b:421,text:'SOĞUK SU',icon:'drop',y:925},{a:557,b:580,text:'HEMEN KAYDET',icon:'save',y:850}];let z=tags.find(v=>f>=v.a&&f<v.b);if(!z)return null;let n=f-z.a,p=spring({frame:n,fps,config:{damping:19,stiffness:220,mass:.7}}),fade=interpolate(z.b-f,[0,5],[0,1],c);return <AbsoluteFill style={{opacity:fade,pointerEvents:'none'}}><div style={{position:'absolute',left:60,top:z.y,transform:`translateY(${(1-p)*18}px) scale(${.9+.1*p})`,transformOrigin:'left center',background:'#fff5ca',border:'2px solid #221e17',borderRadius:14,padding:'11px 18px',boxShadow:'0 5px 0 #222,0 8px 16px #0005',font:'900 29px Arial,sans-serif',color:'#211b12'}}><span style={{color:z.icon==='drop'?'#159bd2':'#d3a600',marginRight:10}}>{z.icon==='drop'?'●':'◆'}</span>{z.text}</div></AbsoluteFill>}
function Film(){let f=useCurrentFrame();return <AbsoluteFill><Background/><Hook/><Details/><Captions/>{((f>=75&&f<120)||(f>=320&&f<365)||(f>=510&&f<560))&&<div style={{position:'absolute',bottom:205,width:'100%',textAlign:'center',font:'500 23px Arial',color:'#ffffffb3',textShadow:'0 2px 4px #000'}}>kadincayasam</div>}<Audio src={staticFile('voice.wav')} volume={1}/><Audio src={staticFile('peaceful_days.mp3')} volume={.09}/>{[0,235,333,460].map((n,i)=><Sequence from={n} key={n}><Audio src={staticFile('whoosh.wav')} volume={i===0?.16:.12}/></Sequence>)}<Sequence from={386}><Audio src={staticFile('drip.wav')} volume={.10}/></Sequence></AbsoluteFill>}
function Root(){return <Composition id="VID035V2" component={Film} durationInFrames={629} fps={30} width={720} height={1280}/>}; registerRoot(Root);
