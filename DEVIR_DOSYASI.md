# DEVİR — Kadıncayaşam video üretimi

Güncelleme: 2026-11-01. Bu dosya yeni oturumda önce okunacak başlangıçtır. Ardından `VIDEO_URETIM_KURALLARI.md` (özellikle bölüm 10) ve `GORSEL_KALITE_KURALLARI.md` okunur. Kullanıcı yeni talimat verdiğinde ilgili dosyalar güncellenir. Dosyayı okuyan ajan önce gerçek çalışma alanını ve Drive durumunu kontrol eder; dosya kayıtları erişimi, ses kimliğinin oturumlar arasında çalışmasını veya önceki işlerin güncelliğini garanti etmez.

## Kullanıcıyla çalışma

- Kısa ve açık Türkçe yanıt ver. Yalnız kullanıcı komut verdikçe, verdiği senaryoyu değiştirmeden ilgili video ID'sini üret; senaryo veya uydurma iddia ekleme. Kullanıcı hangi ID'yi istediğini söylememişse sor. Kalıcı stil onayı V14'edir; diğer ID'lere V14'ün metinlerini ve sabit zamanlarını kopyalama.
- Kullanıcı her görev sonunda `devam` yazmayı kabul etti; aynı görevi kullanıcının ayrıca onayı gerekmedikçe tamamla. Her mesajda en fazla 8 ses ve 8 görsel, sırayla önce ses, ardından görsel, ardından kurgu. Tek parça kadın İstanbul Türkçesi ses, 1,45×. Kullanıcının bu oturumda seçtiği `voice-01`; ses kimliği yeni oturumda erişilemiyorsa yeniden seçim dayatma, durumu bildirip alternatif için onay iste.
- Kullanıcı bu dosyayı kendisi yeni bilgi verdikçe güncellememizi istiyor. Üretim betiklerini oturumun izin verilen çalışma dalında commit/push et; dal kurallarına uy, başka dal açma.

## Onaylı stil ve referans

- [VID-001 V14](https://drive.google.com/file/d/1S6QNtWWDd9YPKrqWO0S7sNLkaMc4-JP6/view), Drive ID `1S6QNtWWDd9YPKrqWO0S7sNLkaMc4-JP6`; `production/remotion/vid001-v14.jsx`, kompozisyon `VID001V14`. Kullanıcı 1 Kasım 2026'da tüm videoların bu şekilde yapılmasını istedi.
- Devamlı tam ekran, gerçekçi, senaryoya uygun görseller; ölçülü zoom ve kaydırmalı geçişler, pikselleşme/yatay titreme yok. Tekrar eden büyük ikon yok. Bilgiye bağlı çerçeveli etiketler, kodlu animasyon, çizilen ok/işaret; anlamlı, ekranı doldurmayan ve okunabilir. Sayaç, maskot, ilerleme çubuğu, giriş/gelişme/sonuç başlığı yok.
- Altyazı V14 gibi alt-orta kısa bloklar: aktif kelime siyah yazı/sarı zemin, diğerleri siyah yazı/beyaz zemin; siyah kenar ve gölge. Hook ile aynı anda aynı altyazı tekrar edilmez. V14'te vurgu hafif ölçek/dönüş içerir; büyük zıplama veya titreme yok. Anlatım metninde olmayan kelime/iddia ekleme. `kadincayasam` filigranı aralıklarla.
- Ses tasarımı: ilk karede hook için dikkat çekici ayrı efekt; bilgilendirici grafik ve işaretlerde ışın; sonuçta parıltı/başarı sesi; senaryoda varsa kaydet çağrısında özel kaydet sesi. **Sahne geçişlerine ses efekti yok.** Efektler sentezdir, gerçek kayıt veya işitsel kalite onayı olarak sunulmaz. Senaryoda kaydet yoksa yeni çağrı uydurma. Lisansları uygun müzik ve anlatım dengeli olsun.
- Başarı/parıltı dekoratif bir vurgu; doğrulanmamış sonuç iddiasını kanıtlanmış gibi sunma. Önceki beğenilen V3 ve önceki karşılaştırmalar V14 yerine varsayılan değil.

## Ses ve senkron kısıtları

- VID-001 orijinal TTS ve 1,45× WAV `production/reference/VID-001/`; 4 fotoğraf aynı dizinde. `production/remotion/vid001-captions.json`: Vosk 44/64 eşleşti, diğer zamanlar interpolasyon. Gerçek zorlanmış hizalama değil; ses baştan sona dinlenmedi. Önceki çıktıların çoğunda manuel işitsel doğrulama yapılmadı. Teknik ölçüm, render/ffmpeg decode veya temas sayfası dinleme yerine geçmez.
- Her yeni videoda mümkünse Türkçe forced alignment ve bütün video için gerçek işitsel/görsel kontrol yap; yapılamıyorsa açıkça söyle. V14'ün makine tableti, sirke ve kesin leke giderme iddiası doğrulanmamıştır; üretici talimatları ve güvenlik önemlidir. Kullanıcı senaryoyu değiştirmemeyi istedi; riski açıkça bildir, güvenlik kurallarına uy.

## Drive, kaynak ve teslim

- Senaryolar Drive `Senryolar.ods` ID `1AWIxtyFS6AL6Mt50eCdGfQQoraXtLNUP`; yerel kopya `google_drive/Senryolar.ods` Git dışı olabilir. ODS satırı ayrıştırırken `split(';',3)[3].split(';Vertical',1)[0]`; kaynak dosyayı doğrula.
- Yeni videolar [Yeni Videolar](https://drive.google.com/drive/folders/1SmBq0LXdGV_SnK1ge83SGWEf5rfmMEmF) ana klasörüne doğrudan `VID-xxx.mp4`; karşılaştırma gerekiyorsa farklı `VID-xxx-vN.mp4`. Eski Drive klasör `18rnZhzVI7oMD6d22S8ZYN1N949jzl57N`. Ses seçenekleri için kullanıcı özel klasör istedi: `1Iw8idglFwqKhNNSj292bWZ8AuwqklU4_`. Dosyaları silmeden önce kapsam ve bağımlılıkları doğrula; mümkünse kalıcı silme yerine çöp.
- 001–034 ve 036 eski klasöre yüklendi; 035'in önceki tercih edilmiş referansı `1wnYeQx8Hzm7fXdlPC0vtOSen8OYZJpuc`. 037–038 eski üretimler tamamlanmadı. Önce Drive'ı sorgula, eksikleri varsayma. Bu kayıt, tamamlanmış eski videoların V14 standardını karşıladığı anlamına gelmez.
- 720×1280, 30 FPS, H.264/AAC, en fazla 10 MB, mümkünse yaklaşık 6 MB. V14 20,67 sn ve 3.612.937 bayt; video teknik decode edildi, tepe −6,9 dBFS. Sesi dinlenmedi; altyazı zamanları kısmen tahmini. Kullanıcıya dosya bağlantısı ve ilgili sınırlamaları söyle.

## Yeniden üretim ve kaynaklar

- `production/remotion/scripts/make-hook-save-sfx.py` → `public/sfx-hook-merak.wav`, `public/sfx-kaydet.wav`; `make-beam-sfx.py` → `public/sfx-isin.wav`; `make-result-chime.py` → `public/sfx-result-chime.wav`. `public/` çalışma dosyaları ve üretilmiş WAV'lar Git dışı olabilir. Betikleri çalıştır, V14 fotoğraflarını/`VID-001-voice.wav` dosyasını `production/reference/VID-001/` altından public'e kopyala; `production/assets/` müzik dosyasını oraya koy. Müzik kaynakları `production/assets/CREDITS.md`.
- Görseller için SHA-bağlı manuel inceleme manifesti `production/vid001-v6-review.json`; `production/render_reviewed.py` tüm kullanılan fotoğrafların gerçek yollarını doğrular. Bu bir otomatik anatomi veya senkron tespiti değildir. Yeni video için yeni gözle inceleme, yeni manifest ve sahne planı gerekir.
- `production/remotion/package-lock.json` ile `npm ci`; sandbox Chromium için `AWS_LAMBDA_JS_RUNTIME=nodejs22.x node -e "require('@sparticuz/chromium').default.executablePath().then(console.log)"`, Remotion `--browser-executable=/tmp/chromium --gl=angle --disable-web-security`, gerekirse `LD_LIBRARY_PATH=/tmp/al2023/lib`. Python/FFmpeg sanal ortamı, node_modules, Chromium ve büyük modeller geçici; sistemde ffmpeg olmayabilir. Bunları ortamı kontrol ederek yeniden kur. Ağ, GPU ve lisans yeteneklerini test etmeden var sayma.
- Görsel kalite, senaryo tutarlılığı, doğru nesne ve fizik denetimi `GORSEL_KALITE_KURALLARI.md` içinde. Hatalı görseli kullanma; gerektiğinde yeniden üret. Kullanıcı test ve kullanılan betiklerin push edilmesini istedi.

## Şu an

V14 kullanıcı tarafından genel stil olarak kabul edildi. Yeni videolar klasöründe V14 dışındaki 14 adet VID-001 deneme videosu geri alınabilir şekilde çöp kutusuna taşındı; V14 ve diğer videolar korundu. Kullanıcı kurulan skill/araçların gerektiğinde kullanılmak üzere korunmasını istedi. Henüz yeni video ID'si verilmedi.

## Claude Stüdyo — V14 seçildi, araçlar korunuyor

YapayTU'nun 7 MIT skill'i `.claude/skills/`, örnekler `ornekler/`, araçlar `araclar/`; kurulum/kullanım ve gerçek test kapsamı `CLAUDE-STUDYO-KULLANIM.md`, lisans `CLAUDE-STUDYO-LICENSE`. Skill tanımları Claude Code biçimindedir; Arena'da otomatik skill yürütme varsayılmadı, içerikleri okunup uyarlama elle yapıldı. `ciktilar/VID-001-studyo.html` gerçek Stüdyo/Playwright kare-kare kayıt aracı ile oluşturulan VID-001 motion-grafik karşılaştırmasıdır; 4 incelenmiş fotoğraf ve V14 miks sesini kullanır. Kullanıcı V14 stilini seçti; Stüdyo karşılaştırma videosu Drive çöpüne taşındı. Kurulu araçlar ve kaynak kodu gerektiğinde kullanmak üzere korunuyor. Ses baştan sona dinlenmedi, kelime zamanları kısmen tahmini.

## VID-002–010 seri üretim, 2026-11-01

Kullanıcı VID-002–010 istedi. VID-002 V14 stilinde üretildi ve Drive'a yüklendi: https://drive.google.com/file/d/1iGBWsAqR0HmwmR1oCYqPhDhTByIJLF3D/view . `production/remotion/vid002-v14.jsx`, `vid002-captions.json`, `VID-002-plan.md`, `production/prepare_vid002.py` ve `production/reference/VID-002/` kaydedildi. 23,62 sn, 4.716.643 bayt; Vosk 37/72 kelimede tam eşleşme, kalanı interpolasyon; ses bütünüyle dinlenmedi, 3 hafta taze kalma iddiası doğrulanmadı. 15 örnek kare, tam decode ve blackdetect yapıldı. `production/reference/VID-003/README.md` sonraki adımı ve reddedilen yüzü açıklar; 003 ham/hızlı ses ve 3 aday görsel var, render/teslim yok. Kullanıcının bir turda en fazla 8 görsel tercihi nedeniyle yeni tur gerekir. VID-004 sıcak ütüye ağrı kesici sürme önerisi yanık ve zararlı duman riski taşır; güvenli alternatif için kullanıcı onayı al, kaynak senaryoyu sessizce değiştirme. 005–010 henüz üretilmedi. Başka videoları teslim edilmiş gibi yazma.

### Seri üretim güncellemesi

VID-003 https://drive.google.com/file/d/1qDz-u-ZwtVXnuYa9oOTSO152WPx4J27P/view (23,21 sn, 3.910.391 bayt; Vosk 39/63) ve VID-005 https://drive.google.com/file/d/1ZElThoRR2r7cVR_YnfTFM00l4_OB4GQy/view (22,74 sn, 5.686.225 bayt; Vosk 47/66) tamamlandı. `production/reference/VID-003/`, `VID-005/`, `production/remotion/BatchV14.jsx`, her iki `vidNNN-config.json`, `vidNNN-captions.json`, `vidNNN-v14.jsx` ve `production/prepare_vosk_captions.py` kaynaklar. İki video da tam decode, blackdetect ve 15 örnek kare kontrolünden geçti; sesi baştan sona dinlenmedi, diğer kelime süreleri interpolasyondur. VID-003 doğrudan buz uygulaması ciltte tahriş/soğuk yanığı riski taşır; iddia edilen sonuç doğrulanmadı. VID-004 sıcak ütüye ilaç sürme nedeniyle beklemede; 006–010 henüz üretilmedi. Önceki paragraftaki VID-003'ün tamamlanmadığı ifadesi tarihsel kaldı; bu güncelleme geçerlidir.

### Güncelleme — VID-004 onaylı güvenli uyarlama

Kullanıcı tehlikeli orijinal yerine güvenli yöntemle yapılmasını onayladı. VID-004 yeni metinle tamamlandı: https://drive.google.com/file/d/1UUD1Ad2WQXsqqjYCwzhBU_9kspcmkdra/view ; 22,87 sn, 4.155.541 bayt. `production/reference/VID-004/script.txt`, kaynak ses/görseller ve SHA inceleme, `production/remotion/vid004-config.json`/`vid004-v14.jsx` kaydedildi. 40/67 Vosk eşleşmesi; kalanı interpolasyon, ses dinlenmedi. Bilgi kartı ikonları ve bekleme anında dönen analog saat + hızlı tik tak var. `VIDEO_URETIM_KURALLARI.md` bölüm 11 kullanıcı tercihini kaydeder. Önceki VID-004 bekliyor notu artık geçersizdir. Sıradaki 006: 3. görsel desteklenmeyen havada damlalık nedeniyle reddedildi; `production/reference/VID-006/README.md` sonraki adımı anlatır. Görsel limiti nedeniyle sonraki turda düzelt. VID-007–010 henüz üretilmedi.

### VID-006 tamamlandı

https://drive.google.com/file/d/19979tufTu4uBvXFVSvV1rBlY9yyL9mK6/view — 21,37 sn, 3.539.216 bayt. Önceki havada duran damlalık sahnesi reddedildi; tezgağa dayalı damlalık içeren yeni 3. sahne oluşturuldu, dört kaynak tek tek incelendi ve SHA kalite kapısıyla render edildi. `production/reference/VID-006/README.md` ve `production/remotion/vid006-{config.json,captions.json,v14.jsx}` kaynaklardır. 24 saat için animasyonlu saat ve tik tak, küçük kahve/damla ikonları eklendi. Tam teknik decode, blackdetect, ses düzeyi, 24 saat örnek karesi kontrol edildi; ses dinlenmedi, altyazının 26 kelimesi interpolasyondur. ODS'deki 24 saatte tüm kokuları giderme iddiası doğrulanmadı. Sırada VID-007; 007–010 tamamlanmadı.

### Kullanıcı doğrulama önceliği

Kullanıcı sıradan doğrulanmamış iddiaların ayrıntılarına takılmadan senaryoların uygulanmasını, özellikle hukuki risklere dikkat edilmesini istedi. `VIDEO_URETIM_KURALLARI.md` bölüm 12; önemli güvenlik/yasal riskte dikkat ve açık iletişim, sessiz senaryo değişikliği yok. Sırada VID-007.

### VID-007 ve VID-008

Kullanıcının isteğiyle ikişer üretim: VID-007 https://drive.google.com/file/d/14ap96lTFDE_Q_23wNhKw4KysCsUrjW0v/view (20,73 sn; 2.868.755 bayt), VID-008 https://drive.google.com/file/d/1lWCmFfIrS8vc_IHWpxLsvbHIWYHkiwHk/view (23,50 sn; 5.186.451 bayt). Tek parça voice-01, 1,45×, V14, ilgili küçük SVG ve saat/tik tak; kaynakları `production/reference/VID-007/`, `VID-008/`, kurgu `production/remotion/vid007-*`, `vid008-*`. 007'nin ilk 4. görseli doğal olmayan kesik boyun nedeniyle reddedildi, görsel kotası aşılamadığından son sahnede 1. görsel tekrarlandı. Görseller elle kontrol ve SHA, tam decode/blackdetect/ses seviyesi ve 3 saniyede bir örnek kare kontrol edildi. Vosk sırasıyla 41/66 ve 46/67 eşleşme; diğerleri interpolasyon, sesler baştan sona dinlenmedi. Sonraki sıra VID-009 ve VID-010.
