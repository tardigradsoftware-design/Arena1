"""ASS overlays for the reviewed VID-035 shots. Coordinates use 720x1280 pixels."""
import math


def _time(t):
    t = max(0, t)
    return '%d:%02d:%05.2f' % (int(t // 3600), int(t // 60) % 60, t % 60)


def _polygon(a, b, width=5):
    dx, dy = b[0]-a[0], b[1]-a[1]
    length = math.hypot(dx, dy) or 1
    nx, ny = -dy/length*width/2, dx/length*width/2
    pts = [(a[0]+nx,a[1]+ny), (b[0]+nx,b[1]+ny), (b[0]-nx,b[1]-ny), (a[0]-nx,a[1]-ny)]
    return 'm %d %d l %d %d %d %d %d %d' % tuple(round(v) for pt in pts for v in pt)


def _arrow(f, start, end, points):
    # Successively reveal connected strokes; no hand or moving pen is shown.
    count = len(points)-1
    for i in range(1, count+1):
        t0 = start + (i-1)*0.06
        t1 = start + i*0.06 if i < count else end
        path = ' '.join(_polygon(points[j], points[j+1]) for j in range(i))
        f.write('Dialogue: 2,%s,%s,Default,,0,0,0,,{\\an7\\pos(0,0)\\p1\\bord1\\3c&H303030&\\1c&HFFFFFF&}%s{\\p0}\n' % (_time(t0), _time(t1), path))


def overlays(f, num, cuts):
    if num != 35:
        return
    # Quoted words from the scenario, separate from the fixed central captions.
    f.write('Dialogue: 2,0:00:00.10,0:00:02.70,Default,,0,0,0,,{\\an8\\pos(360,150)\\fs39\\bord4\\fad(120,250)\\1c&H00FFFF&}SOĞAN DOĞRARKEN\\NGÖZYAŞLARINA BOĞULUP\n')
    _arrow(f, cuts[0]+0.55, cuts[1]-0.20, [(372,625),(390,632),(409,642),(428,654),(447,671),(465,690),(481,712),(490,728),(471,718),(490,728),(492,707)])
    _arrow(f, cuts[1]+0.45, cuts[2]-0.20, [(560,650),(550,665),(539,681),(525,697),(508,714),(489,733),(470,752),(451,771),(457,747),(451,771),(475,765)])
