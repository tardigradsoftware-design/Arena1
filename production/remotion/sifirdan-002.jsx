import React from 'react';
import {Composition,registerRoot} from 'remotion';
import {YeniSeriTekParca} from './YeniSeriTekParca';
import config from './sifirdan-002.json';
function Video(){return <YeniSeriTekParca config={config}/>};function Root(){return <Composition id="Seri" component={Video} durationInFrames={config.frames} fps={30} width={1080} height={1920}/>};registerRoot(Root);
