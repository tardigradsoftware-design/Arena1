import React from 'react';
import {interpolate, useCurrentFrame} from 'remotion';

/**
 * A manually verified annotation in SOURCE IMAGE coordinates (normalized 0..1).
 * Render inside the same source-sized layer as the image, then apply crop,
 * camera pan/zoom and rotation to their common parent. This is NOT tracking.
 * Pass verified=true only after inspecting the actual output frames. If the
 * image or transform changes, verify again. Never point at an inferred target.
 */
export function VerifiedHighlight({verified = false, target, origin, width, height, from = 0, to, color = '#ffe135'}) {
  const frame = useCurrentFrame();
  const validPoint = (p) => p && Number.isFinite(p.x) && Number.isFinite(p.y) && p.x >= 0 && p.x <= 1 && p.y >= 0 && p.y <= 1;
  if (!verified || !validPoint(target) || !validPoint(origin) || !Number.isFinite(width) || !Number.isFinite(height) || width <= 0 || height <= 0 || !Number.isFinite(from) || !Number.isFinite(to) || to <= from || frame < from || frame >= to) return null;
  const x = target.x * width, y = target.y * height;
  const ox = origin.x * width, oy = origin.y * height;
  const angle = Math.atan2(y - oy, x - ox);
  const size = Math.max(14, Math.min(width, height) * 0.035);
  const left = [x - size * Math.cos(angle - 0.55), y - size * Math.sin(angle - 0.55)];
  const right = [x - size * Math.cos(angle + 0.55), y - size * Math.sin(angle + 0.55)];
  const progress = interpolate(frame - from, [0, 10], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return <svg width={width} height={height} viewBox={`0 0 ${width} ${height}`} style={{position: 'absolute', inset: 0, pointerEvents: 'none', overflow: 'hidden', filter: 'drop-shadow(0 2px 3px #000)'}} aria-hidden="true">
    <path d={`M ${ox} ${oy} L ${x} ${y}`} fill="none" stroke={color} strokeWidth={Math.max(3, size * 0.16)} strokeLinecap="round" pathLength="1" strokeDasharray="1" strokeDashoffset={1 - progress}/>
    {progress >= 1 && <path d={`M ${left[0]} ${left[1]} L ${x} ${y} L ${right[0]} ${right[1]}`} fill="none" stroke={color} strokeWidth={Math.max(3, size * 0.16)} strokeLinecap="round" strokeLinejoin="round"/>}
  </svg>;
}
