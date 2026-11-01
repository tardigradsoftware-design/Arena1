import React from 'react';
import {Composition,registerRoot} from 'remotion';
import {BatchV14} from './BatchV14';
import captions from './vid104-captions.json';
import config from './vid104-config.json';
function Video(){return <BatchV14 config={config} captions={captions}/>}
function Root(){return <Composition id="VID104" component={Video} durationInFrames={config.frames} fps={30} width={720} height={1280}/>}
registerRoot(Root);
