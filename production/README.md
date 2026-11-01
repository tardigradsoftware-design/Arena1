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

## Altyazı zaman damgası kontrolü

`check_alignment.py` kaynak metin ile kelime-zaman JSON'undaki kelime sırasını, eksikleri, çakışmayı ve ses süresi sınırını kontrol eder; hizalama üretmez, sesi dinlemez ve kelimelerin doğru zamanda söylendiğini kanıtlamaz. JSON şeması `{"duration": 1.0, "words": [{"word": "örnek", "start": 0.1, "end": 0.8}]}`; UTF-8 kaynak metni ile `production/.venv/bin/python production/check_alignment.py metin.txt kelimeler.json` şeklinde çalıştırılır. Kontrol aracı bağımsızdır; henüz render kapısına bağlanmadı. Hataları düzeltmek ve ses üzerinden gözden geçirmek gerekir.

Türkçe forced alignment için [WhisperX](https://github.com/m-bain/whisperX) ve `mpoyraz/wav2vec2-xls-r-300m-cv7-turkish` adayı araştırıldı. Model bu ortamda indirilip test edilmedi; mevcut Vosk ASR, forced alignment değildir. Araçları kurulmuş/başarılı gibi varsayma ve 035'teki interpolasyonları kesin zamanlama diye sunma. Yayın öncesi ses–altyazı–sahne kontrolü gereklidir.

## Ses analizi (gerçek dinleme yerine geçmez)

`audio_audit.py` FFmpeg ile sesi mono/16 kHz çözer, ilk en fazla 600 saniyenin RMS/tepe düzeyi, tam ölçeğe yaklaşan örnek oranı ve düşük seviyeli aralıklarını ölçer; isteğe bağlı Vosk Türkçe tanıma çıktısı verir. Eşikler otomatik tahmindir: müzikli miks konuşma boşluğunu maskeleyebilir, tam ölçek yakınlığı kesin clipping teşhisi değildir. Sesin vurgu, doğallık, efekt dengesi veya senkron kalitesini dinlemeden doğrulamaz. ASR hataları doğrudan seslendirme hatası olarak yorumlanamaz.

```sh
production/.venv/bin/python production/audio_audit.py production/reference/VID-001/VID-001-fast.wav --model production/vosk-tr --output production/audio/VID-001-audit.json
production/.venv/bin/python -m unittest discover -s production/tests -v
```

2026-11-01 denemesinde VID-001 sesinin analiz edilen süresi 20,65 sn, tepe değeri −4,45 dBFS, 45 dBFS altı 0,35 sn aralık tespit edildi. Türkçe Vosk bazı kelimeleri hatalı tanıdı; insan dinlemesi yerine geçmez. Asistanın bu ortamda sese doğrudan dinleme aracı yoktur; dinlemiş gibi raporlanmaz. WAV/MP4 kullanıcı tarafından oynatılıp geri bildirim verilebilir. Model ve venv geçicidir, yukarıdaki kurulumla geri yüklenebilir.
