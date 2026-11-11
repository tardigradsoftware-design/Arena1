"""Yasal seri: 1080x1920 dikey kısa video üretici (PIL + FFmpeg).

Kullanım: production/.venv/bin/python production/yasal/render_yasal.py <ID> [<ID> ...]
Girdi : production/yasal/rows.json, audio/<ID>_raw.wav, img/<ID>_{a,b,c}.png
Çıktı : production/videos/<ID>_<CTA>.mp4  (+ work/<ID>_words.json)

Akış: sessizlik kısaltma + 1.15x hız -> Vosk ile yaklaşık kelime zamanı ->
hook (ilk 3 sn) + karaoke altyazı + 3-4 sn'de bir sahne/zoom + CTA (son 3 sn).
Kelime zamanları Vosk çapaları + interpolasyondur; zorlanmış hizalama değildir.
"""
import difflib, json, math, re, subprocess, sys, wave
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import imageio_ffmpeg

HERE = Path(__file__).resolve().parent
PROD = HERE.parent
FF = imageio_ffmpeg.get_ffmpeg_exe()
W, H, FPS = 1080, 1920, 30
SPEED = 1.15
HOOK, CTA = 3.0, 3.0
TAIL = 0.9
YELLOW, WHITE, BLACK, RED = (255, 212, 0), (255, 255, 255), (12, 12, 14), (230, 57, 70)
F_BLACK = str(HERE / 'fonts/Montserrat-Black.ttf')
F_XBOLD = str(HERE / 'fonts/Montserrat-ExtraBold.ttf')
WORK = HERE / 'work'; WORK.mkdir(exist_ok=True)
OUT = PROD / 'videos'; OUT.mkdir(exist_ok=True)


def font(path, size): return ImageFont.truetype(path, size)
def tr_upper(s): return s.replace('i', 'İ').replace('ı', 'I').upper()
def tr_lower(s): return s.replace('I', 'ı').replace('İ', 'i').lower()
def c01(x): return max(0.0, min(1.0, x))
def ease(x): x = c01(x); return 1 - (1 - x) ** 3
def back(x):
    x = c01(x); c = 1.9
    return 1 + (c + 1) * (x - 1) ** 3 + c * (x - 1) ** 2
def run(cmd): subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


# ---------- ses ----------
def prepare_audio(rid):
    raw = HERE / f'audio/{rid}_raw.wav'
    tight = WORK / f'{rid}_tight.wav'   # sessizlik kısaltılmış, hız 1.0 (hizalama için)
    fast = WORK / f'{rid}_voice.wav'    # 1.15x
    sr = ('silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.03,'
          'silenceremove=stop_periods=-1:stop_duration=0.30:stop_threshold=-40dB:stop_silence=0.15')
    run([FF, '-y', '-i', str(raw), '-af', sr, '-ar', '16000', '-ac', '1', str(tight)])
    run([FF, '-y', '-i', str(raw), '-af', sr + f',atempo={SPEED},loudnorm=I=-15:TP=-1.5:LRA=7',
         '-ar', '48000', '-ac', '1', str(fast)])
    with wave.open(str(fast)) as w: dur = w.getnframes() / w.getframerate()
    return tight, fast, dur


def norm(w): return re.sub(r'[^a-z0-9çğıöşü]', '', tr_lower(w))


def align(rid, text, tight, dur):
    words = text.split()
    from vosk import Model, KaldiRecognizer, SetLogLevel
    SetLogLevel(-1)
    rec = KaldiRecognizer(Model(str(PROD / 'vosk-tr')), 16000); rec.SetWords(True)
    found = []
    with wave.open(str(tight)) as w:
        tdur = w.getnframes() / 16000
        while True:
            d = w.readframes(4000)
            if not d: break
            if rec.AcceptWaveform(d): found += json.loads(rec.Result()).get('result', [])
        found += json.loads(rec.FinalResult()).get('result', [])
    a = [norm(x) for x in words]; b = [norm(x['word']) for x in found]
    anchors = {}
    for blk in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks():
        for k in range(blk.size):
            f = found[blk.b + k]; anchors[blk.a + k] = (f['start'], f['end'])
    # çapa yoksa karakter sayısına orantılı interpolasyon
    weight = np.cumsum([0] + [len(x) + 2 + (4 if x[-1] in '.!?' else 0) for x in words]).astype(float)
    mid = (weight[:-1] + weight[1:]) / 2
    px = [0.0] + [mid[i] for i in sorted(anchors)] + [weight[-1]]
    py = [0.0] + [(anchors[i][0] + anchors[i][1]) / 2 for i in sorted(anchors)] + [tdur]
    centers = np.interp(mid, px, py)
    bounds = [0.0] + [(centers[i - 1] + centers[i]) / 2 for i in range(1, len(words))] + [tdur]
    res = []
    for i, w_ in enumerate(words):
        s, e = (anchors[i] if i in anchors else (bounds[i], bounds[i + 1]))
        s = max(s, res[-1]['start'] + 0.04) if res else s
        res.append({'word': w_, 'start': round(s / SPEED, 3), 'end': round(max(e, s + 0.08) / SPEED, 3),
                    'matched': i in anchors})
    (WORK / f'{rid}_words.json').write_text(json.dumps(res, ensure_ascii=False, indent=1))
    print(f'  hizalama: {len(anchors)}/{len(words)} kelime Vosk çapası, kalanı tahmin')
    return res


def chunks(words):
    out, cur = [], []
    for w_ in words:
        cur.append(w_)
        ln = sum(len(x['word']) for x in cur) + len(cur) - 1
        if w_['word'][-1] in '.!?,' or len(cur) == 3 or ln >= 17:
            out.append(cur); cur = []
    if cur: out.append(cur)
    return out


# ---------- çizim ----------
def text_sprite(txt, fnt, fill, stroke=0, stroke_fill=BLACK, box=None, pad=(34, 16), radius=26, shadow=True):
    l, t, r, b = fnt.getbbox(txt, stroke_width=stroke)
    asc, desc = fnt.getmetrics()
    tw, th = r - l, asc + desc
    px, py = pad if box else (stroke + 6, stroke + 6)
    off = 10 if shadow and box else 0
    im = Image.new('RGBA', (tw + 2 * px + off, th + 2 * py + off), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if box:
        if off: d.rounded_rectangle((off, off, tw + 2 * px + off - 1, th + 2 * py + off - 1), radius, fill=(0, 0, 0, 255))
        d.rounded_rectangle((0, 0, tw + 2 * px - 1, th + 2 * py - 1), radius, fill=box + (255,))
    d.text((px - l, py), txt, font=fnt, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)
    return im


def paste_scaled(frame, spr, cx, cy, scale=1.0, alpha=1.0, rot=0.0):
    if scale <= 0.02 or alpha <= 0.02: return
    s = spr
    if abs(scale - 1) > 0.004:
        s = s.resize((max(1, int(s.width * scale)), max(1, int(s.height * scale))), Image.BICUBIC)
    if rot: s = s.rotate(rot, expand=True, resample=Image.BICUBIC)
    if alpha < 0.99:
        a = s.getchannel('A').point(lambda v: int(v * alpha)); s = s.copy(); s.putalpha(a)
    frame.paste(s, (int(cx - s.width / 2), int(cy - s.height / 2)), s)


def wrap_title(title, max_w, max_lines=3):
    words = tr_upper(title).split()
    for size in range(150, 70, -4):
        f = font(F_BLACK, size); lines, cur = [], ''
        for w_ in words:
            t = (cur + ' ' + w_).strip()
            if f.getlength(t) <= max_w or not cur: cur = t
            else: lines.append(cur); cur = w_
        lines.append(cur)
        if len(lines) <= max_lines and all(f.getlength(x) <= max_w for x in lines): return f, lines
    return f, lines


def load_bg(path):
    im = Image.open(path).convert('RGB')
    k = max(W / im.width, H / im.height) * 1.22
    im = im.resize((int(im.width * k) + 1, int(im.height * k) + 1), Image.LANCZOS)
    return im.filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=2))


MOVES = [  # (zoom0, zoom1, fx0, fy0, fx1, fy1)  odak 0..1
    (1.00, 1.14, .50, .50, .50, .46),
    (1.16, 1.04, .50, .40, .50, .52),
    (1.04, 1.18, .46, .56, .54, .48),
    (1.20, 1.08, .56, .46, .46, .52),
    (1.02, 1.16, .50, .44, .50, .56),
    (1.18, 1.05, .44, .54, .52, .46),
]


def bg_frame(bg, mv, p):
    z0, z1, x0, y0, x1, y1 = mv
    e = p * p * (3 - 2 * p) * 0.35 + p * 0.65
    z = z0 + (z1 - z0) * e
    cw, ch = W * 1.0 / z * (bg.width / (W * 1.22)), H * 1.0 / z * (bg.height / (H * 1.22))
    cw, ch = min(cw, bg.width), min(ch, bg.height)
    fx, fy = x0 + (x1 - x0) * e, y0 + (y1 - y0) * e
    l = (bg.width - cw) * fx; t = (bg.height - ch) * fy
    return bg.resize((W, H), Image.BILINEAR, box=(l, t, l + cw, t + ch))


def gradient():
    g = np.zeros((H, W), np.float32)
    y = np.arange(H, dtype=np.float32)[:, None]
    g += np.clip((520 - y) / 520, 0, 1) * 0.55
    g += np.clip((y - 820) / 700, 0, 1) * 0.72
    return Image.fromarray((np.clip(g, 0, 1) * 255).astype(np.uint8), 'L')


def bubble_icon(size=120):
    im = Image.new('RGBA', (size, size), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((4, 8, size - 4, size - 28), 30, fill=BLACK + (255,))
    d.polygon([(26, size - 32), (22, size - 2), (60, size - 32)], fill=BLACK + (255,))
    for i in range(3):
        cx = size / 2 + (i - 1) * 26
        d.ellipse((cx - 8, size / 2 - 18, cx + 8, size / 2 - 2), fill=YELLOW + (255,))
    return im


def cta_card(kw):
    cw = 940
    f1 = font(F_BLACK, 74); f2 = font(F_XBOLD, 58)
    for size in range(74, 40, -3):
        f1 = font(F_BLACK, size); kwf = font(F_BLACK, int(size * 1.2))
        a = text_sprite('Yoruma', f1, BLACK, shadow=False)
        pill = text_sprite(kw, kwf, WHITE, box=RED, pad=(26, 6), radius=28)
        b = text_sprite('yaz,', f1, BLACK, shadow=False)
        if a.width + pill.width + b.width + 28 <= cw - 190 - 36: break
    c = text_sprite('rehberi gönderelim!', f2, BLACK, shadow=False)
    ch = 300
    card = Image.new('RGBA', (cw + 14, ch + 14), (0, 0, 0, 0)); d = ImageDraw.Draw(card)
    d.rounded_rectangle((14, 14, cw + 13, ch + 13), 48, fill=(0, 0, 0, 255))
    d.rounded_rectangle((0, 0, cw - 1, ch - 1), 48, fill=YELLOW + (255,), outline=BLACK + (255,), width=8)
    ic = bubble_icon(130); card.paste(ic, (36, 84), ic)
    x0 = 190; row_w = a.width + pill.width + b.width + 28
    x = x0 + max(0, (cw - x0 - 30 - row_w) // 2); y = 92
    card.paste(a, (x, y - a.height // 2), a); x += a.width + 14
    pill_pos = (x + pill.width // 2, y)
    x += pill.width + 14; card.paste(b, (x, y - b.height // 2), b)
    card.paste(c, (x0 + max(0, (cw - x0 - 30 - c.width) // 2), 196 - c.height // 2), c)
    return card, pill, pill_pos


# ---------- efekt sesleri (sentez) ----------
def synth_pop(path, f0=520, f1=980, dur=0.16, vol=0.55):
    sr = 48000; t = np.arange(int(sr * dur)) / sr
    f = f0 + (f1 - f0) * (t / dur) ** 0.5
    x = np.sin(2 * np.pi * np.cumsum(f) / sr) * np.exp(-t * 26) * vol
    x[:48] *= np.linspace(0, 1, 48)
    with wave.open(str(path), 'w') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((x * 32767).astype('<i2').tobytes())


def synth_ding(path, vol=0.42):
    sr = 48000; t = np.arange(int(sr * 0.9)) / sr; x = np.zeros_like(t)
    for k, (f, d0) in enumerate([(1046.5, 0.0), (1568.0, 0.11)]):
        tt = np.clip(t - d0, 0, None); on = t >= d0
        x += on * (np.sin(2 * np.pi * f * tt) + 0.35 * np.sin(2 * np.pi * 2 * f * tt)) * np.exp(-tt * 6.5)
    x = x / np.max(np.abs(x)) * vol; x[:96] *= np.linspace(0, 1, 96)
    with wave.open(str(path), 'w') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((x * 32767).astype('<i2').tobytes())


# ---------- ana ----------
def render(row):
    rid = f"{int(row['ID']):02d}"; kw = row['CTA_Kelimesi']
    print(f'[{rid}] {row["Ekran_Yazisi"]}')
    tight, voice, vdur = prepare_audio(rid)
    words = align(rid, row['TTS_Metni'], tight, vdur)
    total = vdur + TAIL; n = int(math.ceil(total * FPS))
    cks = chunks(words)
    spans = []
    for i, c in enumerate(cks):
        s = c[0]['start']; e = c[-1]['end']
        if i + 1 < len(cks): e = max(e, min(cks[i + 1][0]['start'], e + 0.45))
        spans.append((s, e))
    # sahneler: ~3.2 sn, altyazı bloğu başlangıcına yapıştır
    imgs = [load_bg(p) for p in sorted((HERE / 'img').glob(f'{rid}_*.png'))]
    ns = max(len(imgs), int(round(total / 3.2)))
    cuts = [0.0]
    for k in range(1, ns):
        tgt = total * k / ns
        best = min((s for s, _ in spans), key=lambda s: abs(s - tgt))
        if abs(best - tgt) < 0.9 and best - cuts[-1] > 2.0: tgt = best
        cuts.append(tgt)
    cuts.append(total)
    print('  sahne kesimleri:', [round(c, 2) for c in cuts], 'süre', round(total, 2))
    grad = gradient(); black = Image.new('RGB', (W, H), (0, 0, 0))
    # hook
    tf, tlines = wrap_title(row['Ekran_Yazisi'], 860)
    tspr = [text_sprite(l, tf, BLACK, box=YELLOW if i % 2 == 0 else WHITE, pad=(38, 6), radius=30) for i, l in enumerate(tlines)]
    chip = text_sprite(tr_upper(row['Kategori']), font(F_XBOLD, 46), WHITE, box=RED, pad=(30, 10), radius=24)
    lh = tspr[0].height + 14; ty0 = 620 - lh * (len(tspr) - 1) / 2
    # altyazı
    cf = font(F_BLACK, 84); cap_cache = {}
    def cap_sprite(txt, active):
        k = (txt, active)
        if k not in cap_cache:
            cap_cache[k] = text_sprite(txt, cf, YELLOW if active else WHITE, stroke=9)
        return cap_cache[k]
    space = cf.getlength(' ')
    card, pill, pill_pos = cta_card(kw)
    cta_t = total - CTA

    out = OUT / f"{int(row['ID'])}_{kw}.mp4"
    silent = WORK / f'{rid}_silent.mp4'
    enc = subprocess.Popen([FF, '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                            '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p', str(silent)],
                           stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)
    for fi in range(n):
        t = fi / FPS
        si = max(i for i in range(len(cuts) - 1) if cuts[i] <= t)
        p = (t - cuts[si]) / (cuts[si + 1] - cuts[si])
        fr = bg_frame(imgs[si % len(imgs)], MOVES[si % len(MOVES)], p)
        dt = t - cuts[si]
        if si > 0 and dt < 0.2:  # hızlı dikey itme geçişi
            q = ease(dt / 0.2); pj = si - 1
            prev = bg_frame(imgs[pj % len(imgs)], MOVES[pj % len(MOVES)], 1.0)
            comp = Image.new('RGB', (W, H)); off = int(H * q)
            comp.paste(prev, (0, -off)); comp.paste(fr, (0, H - off)); fr = comp
        fr = Image.composite(black, fr, grad)
        # hook başlığı
        if t < HOOK + 0.25:
            outp = ease((t - HOOK) / 0.22) if t > HOOK else 0
            a = 1 - outp
            paste_scaled(fr, chip, W / 2, ty0 - lh / 2 - 62 - 60 * outp, max(0.9, back(t / 0.28)) if t < .28 else 1, a)
            for i, s in enumerate(tspr):
                st = 0.05 + i * 0.11
                sc = back((t - st) / 0.30) if t < st + 0.30 else 1 + 0.018 * math.sin((t - st) * 5)
                if t < st and fi > 0: continue
                if fi == 0: sc = max(sc, 0.9)
                paste_scaled(fr, s, W / 2, ty0 + i * lh - 80 * outp, sc * (1 - 0.25 * outp), a, rot=-3 if i % 2 == 0 else -1.5)
        # altyazı (karaoke)
        for (s, e), c in zip(spans, cks):
            if s <= t < e:
                sprs = []
                for w_ in c:
                    act = w_['start'] <= t and (t < w_['end'] or w_ is c[-1] or t < c[c.index(w_) + 1]['start'])
                    said = t >= w_['start']
                    sprs.append((cap_sprite(w_['word'], act), act, said, w_))
                # satırlara böl
                lines, cur, cw_ = [], [], 0
                for it in sprs:
                    wpx = it[0].width - 30
                    if cur and cw_ + wpx + space > 900: lines.append(cur); cur, cw_ = [], 0
                    cur.append(it); cw_ += wpx + space
                lines.append(cur)
                ent = back((t - s) / 0.14) if t - s < 0.14 else 1
                y = (1090 if t >= cta_t - 0.1 else 1150) - (len(lines) - 1) * 52
                for ln in lines:
                    tw = sum(it[0].width - 30 for it in ln) + space * (len(ln) - 1)
                    x = W / 2 - tw / 2
                    for spr, act, said, w_ in ln:
                        wpx = spr.width - 30
                        sc = (1 + 0.10 * (1 - ease((t - w_['start']) / 0.16))) if act else 1
                        paste_scaled(fr, spr, x + wpx / 2, y, sc * (0.9 + 0.1 * ent), 1.0 if said else 0.92)
                        x += wpx + space
                    y += 104
                break
        # CTA
        if t >= cta_t:
            q = back((t - cta_t) / 0.4) if t - cta_t < 0.4 else 1
            cy = 1410 + (1 - q) * 520
            fr.paste(card, (int(W / 2 - card.width / 2), int(cy - card.height / 2)), card)
            if q == 1:
                pulse = 1 + 0.07 * (0.5 + 0.5 * math.sin((t - cta_t - 0.4) * 9))
                paste_scaled(fr, pill, W / 2 - card.width / 2 + pill_pos[0], cy - card.height / 2 + pill_pos[1], pulse)
            else:
                paste_scaled(fr, pill, W / 2 - card.width / 2 + pill_pos[0], cy - card.height / 2 + pill_pos[1], 1)
        enc.stdin.write(fr.tobytes())
    enc.stdin.close(); enc.wait()
    pop, ding = WORK / 'pop.wav', WORK / 'ding.wav'
    synth_pop(pop); synth_ding(ding)
    whoosh = PROD / 'assets/whoosh.wav'
    fc = (f"[1:a]apad=whole_dur={total:.3f}[v];[2:a]volume=0.55[w];[3:a]adelay=120|120,volume=0.9[p];"
          f"[4:a]adelay={int(cta_t*1000)}|{int(cta_t*1000)}[d];[2:a]adelay={int(cta_t*1000-150)}|{int(cta_t*1000-150)},volume=0.35[w2];"
          f"[v][w][p][d][w2]amix=inputs=5:duration=first:normalize=0,alimiter=limit=0.95[a]")
    run([FF, '-y', '-i', str(silent), '-i', str(voice), '-i', str(whoosh), '-i', str(pop), '-i', str(ding),
         '-filter_complex', fc, '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k', '-ar', '48000',
         '-t', f'{total:.3f}', '-movflags', '+faststart', str(out)])
    print('  ->', out, round(out.stat().st_size / 1e6, 2), 'MB')
    return out


if __name__ == '__main__':
    rows = {int(r['ID']): r for r in json.loads((HERE / 'rows.json').read_text())}
    for a in sys.argv[1:]: render(rows[int(a)])
