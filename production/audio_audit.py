"""Inspect audio levels/silence and optionally transcribe Turkish with Vosk.

These are machine estimates, not a replacement for human listening.
"""
import argparse
import json
import math
import subprocess
from pathlib import Path

import imageio_ffmpeg
import numpy as np

RATE = 16000
MAX_SECONDS = 600


def analyze(samples, rate=RATE):
    samples = np.asarray(samples, dtype=np.float32)
    if not len(samples):
        raise ValueError('Audio stream is empty')
    peak = float(np.max(np.abs(samples)))
    rms = float(np.sqrt(np.mean(np.square(samples, dtype=np.float64))))
    frame_size = max(1, rate // 20)
    windows = [samples[i:i + frame_size] for i in range(0, len(samples), frame_size)]
    quiet = [float(np.sqrt(np.mean(np.square(w, dtype=np.float64)))) < 10**(-45/20) for w in windows]
    spans = []
    start = None
    for i, silent in enumerate(quiet + [False]):
        if silent and start is None:
            start = i
        elif not silent and start is not None:
            end = min(len(samples) / rate, i * frame_size / rate)
            begin = start * frame_size / rate
            if end - begin >= 0.3:
                spans.append({'start': round(begin, 2), 'end': round(end, 2)})
            start = None
    return {
        'seconds_analyzed': round(len(samples)/rate, 3),
        'peak_dbfs': round(20 * math.log10(max(peak, 1e-12)), 2),
        'rms_dbfs': round(20 * math.log10(max(rms, 1e-12)), 2),
        'near_full_scale_percent': round(float(np.mean(np.abs(samples) >= 0.999)) * 100, 4),
        'quiet_intervals_below_minus_45dbfs': spans,
        'possible_truncation_at_600s': len(samples) >= MAX_SECONDS * rate,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('audio', type=Path)
    ap.add_argument('--model', type=Path, help='Optional Vosk Turkish model directory')
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    cmd = [imageio_ffmpeg.get_ffmpeg_exe(), '-v', 'error', '-i', str(args.audio), '-t', str(MAX_SECONDS), '-vn', '-ac', '1', '-ar', str(RATE), '-f', 's16le', '-']
    decoded = subprocess.run(cmd, check=True, stdout=subprocess.PIPE).stdout
    pcm = np.frombuffer(decoded, dtype='<i2')
    result = analyze(pcm.astype(np.float32) / 32768.0)
    result['limitations'] = 'Teknik analizdir; sesin öznel kalitesi veya kelime zamanlarının doğruluğu dinlenerek doğrulanmamıştır.'
    if args.model:
        from vosk import Model, KaldiRecognizer, SetLogLevel
        SetLogLevel(-1)
        recognizer = KaldiRecognizer(Model(str(args.model)), RATE)
        recognizer.SetWords(True)
        words = []
        for offset in range(0, len(decoded), 8000):
            if recognizer.AcceptWaveform(decoded[offset:offset + 8000]):
                words.extend(json.loads(recognizer.Result()).get('result', []))
        words.extend(json.loads(recognizer.FinalResult()).get('result', []))
        result['vosk_words'] = words
        result['asr_note'] = 'ASR tahminidir, zorlanmış hizalama değildir; kaynak metin ile ve dinleyerek karşılaştırılmalıdır.'
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Analiz: {args.output}; süre {result["seconds_analyzed"]} sn, tepe {result["peak_dbfs"]} dBFS')


if __name__ == '__main__':
    main()
