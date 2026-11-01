# Video üretimi

## Kurulum

Python 3.10+ ve Git gerekir. Bu ortam CPU-only, yaklaşık 3,8 GiB RAM; büyük yerel görsel modelleri için yeterli değildir. Ortam sıfırlanırsa:

```sh
python -m venv production/.venv
production/.venv/bin/pip install -r production/requirements.txt
git clone --depth 1 https://github.com/serkanalgur/vosk-model-small-tr-0.3-fixed production/vosk-tr
```

Model depoya dahil değildir. Kullanıcının ODS dosyasını `google_drive/Senryolar.ods` konumuna yerleştirin. Tek parça sesleri `production/audio/VID-NNN.wav`, dört sahne görselini `production/images/VID-NNN-1.png` ... `-4.png` konumuna koyun. Görseller kaynak senaryo ve anlatıma uyacak şekilde oluşturulur; senaryo değiştirilmez. Ses üretimini bu betik yapmaz. `--foley` yalnızca sahneye uygun bir ses mevcutsa kullanın:

```sh
production/.venv/bin/python production/quality_check.py 35
production/.venv/bin/python production/render.py 35 --foley production/assets/drip.wav --foley-at 11.5
```

Kurgu kaynağındaki otomatik kelime eşleşmeleri eksik olabilir; eşleşmeyen zamanlar tahmin edilir. 035 hariç sahne kesimleri şimdilik eşit sürelidir, konuşma ile eşleşmeyebilir. Yayından önce sahne/kelime zamanlarını ve sesi baştan sona denetleyin, gerekli süreleri senaryoya göre düzeltin. Betik: 1,45× ses, 720×1280 H.264 30 fps, sabit iki kelime altyazı, etkin kelime sarı, aralıklı filigran, CC0 fon müziği, hızlı kaydırmalı sahne geçişleri ve onlarla eşzamanlı geçiş sesleri üretir. Görsellerde çok hafif, ortalanmış yakınlaşma vardır. Çıktı boyutu süre ve sahne karmaşıklığına bağlıdır; 6 MB garanti değildir. Program sesi dinleyerek ve görüntüyü izleyerek kalite kontrolü yerine geçmez.

## Görsel kalite kontrolü

Her görseli tek başına ve `quality_check.py` temas sayfasıyla incele. Konu, nesneler, sahne eylemi, fiziksel bağlantılar, el/parmaklar, göz, perspektif, bıçak/su gibi ayrıntılar ve birbirine benzer ortam/ışığı kontrol et. Yüz gerekiyorsa yalnızca bir kısmı kadrajda olmalı. Hatalıyı yeniden üretip tekrar incele. İlgi çekici ama senaryoya uymayan veya mantıksız bir görseli kullanma. Otomatik foto-gerçekçilik garantisi yoktur. Varsa referans görseli sonraki sahnelerde kullan; görselde yalan vaat veya belirsiz nesne üretme.

## Açık kaynak araştırması ve kısıtlar

- [FLUX.1](https://github.com/black-forest-labs/flux) resmî kodu, [schnell model kartı](https://github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-schnell.md): açık ağırlıklı seçenek; lisansı ve donanımı ayrıca kontrol edin. Bu sandbox'ta GPU yok, 3,8 GiB RAM var ve ağırlık sunucularına erişim sınırlı; model kurulmadı/denenmedi. Görselleri otomatik iyileştirdiği iddia edilemez.
- [Stable Audio 3](https://github.com/Stability-AI/stable-audio-3): müzik/efekt için açık ağırlıklı seçenek; kullanım ve model lisansı ayrı kontrol edilmeli. Ağırlıkları bu ortamda indirilmedi, sentez modeli denenmedi.
- Dahil edilmiş CC0 parçaların kaynağı ve lisansı `assets/CREDITS.md` dosyasındadır. SFX kitindeki efektler kayıt olmak zorunda değildir; gerçek dünyadan alınmış kayıt olarak sunulmaz.
