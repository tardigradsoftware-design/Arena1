# VID-035 alternatif versiyon

Kompozisyon `../remotion/vid035v2.jsx`, plan `STORYBOARD.md`, son kodlama `finalize.py`. Kaynak senaryo ve TTS değiştirilmedi. V1 korunmuştur. Remotion kurulumu ve ortak lisanslı ses kaynakları `../remotion/README.md` ve `../assets/CREDITS.md` içinde.

Bu deneme için ses ve görseller, boyut/özel içerik nedeniyle Git'e konmaz: `../images/VID-035-[1234].png`, `../images/VID-035-v2-{2,4,8,9,10,11}.png`, `../audio/VID-035-fast.wav` ve `../assets/` dosyalarını Remotion `public/` içine kopyalayın. `captions.json` Vosk ve interpolasyon kullanılarak oluşturulmuştur; gerçek forced alignment değildir. Yerel Chromium kütüphaneleri için `../remotion/README.md`'ye bakın.

```sh
cp ../images/VID-035-[1234].png ../remotion/public/
cp ../images/VID-035-v2-{2,4,8,9,10,11}.png ../remotion/public/
cp ../audio/VID-035-fast.wav ../remotion/public/voice.wav
cp ../assets/{peaceful_days.mp3,whoosh.wav,drip.wav} ../remotion/public/
cd ../remotion
LD_LIBRARY_PATH=/tmp/al2023/lib npx remotion render vid035v2.jsx VID035V2 ../videos/VID-035-v2-raw.mp4 --browser-executable=/tmp/chromium --gl=angle --disable-web-security --concurrency=2 --codec=h264 --crf=18
cd ../..
production/.venv/bin/python production/remotion-v2/finalize.py production/videos/VID-035-v2-raw.mp4 production/videos/VID-035-v2.mp4 --seconds 20.967 --max-mb 10
```

Bu sandbox'ta WhisperX ve Türkçe zorlanmış hizalama modeli indirilemedi. Sahne/altyazı zamanlamalarının elle dinlenmesi ve doğrulanması gerekir. Çıktıdaki sağlık/bilim iddiaları kaynak senaryoya aittir ve doğrulanmış bilimsel bilgi olarak sunulmamalıdır.
