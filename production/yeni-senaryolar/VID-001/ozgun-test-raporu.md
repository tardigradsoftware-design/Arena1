# Yeni liste VID-001 — özgün senaryo test raporu

## Senaryo ve önemli bilgi

Yeni listedeki VID-001 seslendirme metni aynen okunmak üzere üretildi; kurgu testi ayrı sürümdür ve mevcut stok değiştirilmez. İlk hamle ses ve görüntü tasarımına yöneliktir. **Önemli doğruluk sınırı:** Senaryonun aynada tırnak ve yansıma arasında boşluk olmamasının iki yönlü ayna olduğunu kesin gösterdiği iddiası güvenilir değildir. Boşluk olması da mahremiyetin kanıtı değildir; ayna yapıları farklı olabilir. Yapay fotoğraf gerçek ayna testi veya izlenme kanıtı değildir. Bu sebeple test, doğruluğu onaylanmış veya güvenle yayıma hazır içerik olarak değerlendirilmemelidir. Kaynak: https://leadstories.com/hoax-alert/2022/09/fact-check-this-test-of-hotel-mirror-does-not-conclusively-demonstrate-if-it-is-2-way-mirror.html

## Sahne ve varlık çizelgesi (yaklaşık)

- 0–4,3 sn: `test-1.png`, kabin içinde kadın yüzü; hızlı giriş, yakınlaşma, 0,5 saniyede bas vuruşu ve hook metni.
- 4,3–8,1 sn: `test-parmak.png`, aynaya dokunan tırnak ve temsili yansıma. Görsel bir durumun gerçek testi veya güvenliğinin kanıtı değildir.
- 8,1–12,4 sn: `test-2.png`, boş aynanın genel görüntüsü; ses devam eder.
- 12,4–19,9 sn: `test-3.png`, kabin yakınındaki kadın; ardından konu ve soru metni.
- 19,9–23,77 sn: `test-4.png`, iki arkadaşın yüzleri ve soru/yorum kapanışı.

Dört ayrı fotoğraf ve parmak görseli yapay üretimdir. Kadınlar sahneler boyunca aynı kişi değildir; arka plan ve kişi sürekliliği sağlanmadı. Tek tek görsellerle saniyelik örnek kareler gözle incelendi; ilk denemede yansıması tutarsız `test-yuz-1.png` reddedildi ve videoya alınmadı. Fotoğraflar 1080p'ye büyütüldü; gerçek detay üretilmedi. Gerçek hareketli çekim, gerçek 2.5D veya hareket takibi yoktur.

Ses: tek parça `ozgun-anlatim.wav` kadın İstanbul Türkçesi sesi; sesin başlangıcı 1,22×, devamı 1,12×. Kelimeyi kesmemek için geçiş kaynağın 4,54. saniyesindeki saptanmış sessizlikte yapıldı; bu nedenle çıkışta tam 3. saniye değildir. −38 dB/0,15 sn `silenceremove` uygulandı, 0,08 sn bırakıldı; gerçek kelime sınırları ve telaffuz dinlenmedi. Müzik Peaceful Days, Juhani Junkala, CC0 1.0: https://github.com/S3M1TR4SH/asset-library/blob/main/audio/music/juhani-junkala/INFO.txt ; 0,5. saniye bas vuruşu FFmpeg miks betiği tarafından sentezlenir. Kullanılan kazanımlar müzik −22 dB ve bas −8 dB; bunlar nihai ölçülen seviyeler değildir. Limiter uygulanır.

FFmpeg (`production/yeni-senaryolar/ozgun-test-render.py`): ilk fotoğrafta zoom punch, kesme/kadrajlar, kayan büyük yazılar, miks ve H.264/AAC. Metinler yalnız kısa sahne özeti, tam kelime altyazısı değildir; zamanları tahminidir. Gerçek eylem videosu yok, hareket fotoğraf animasyonudur.

## Teknik QC

1080×1920, 9:16, 30 fps, H.264/AAC stereo 48 kHz; 23,77 sn, yaklaşık 2,7 MB. FFmpeg ile final tam decode yapıldı; blackdetect (0,2 sn) ve silencedetect (−55 dB, 0,5 sn) olay bildirmedi. Volumedetect ortalama −20,2 dB, örnek maksimum −6,9 dB ölçtü; true-peak ölçülmedi. Sesin tamamı dinlenmedi; tüm video gerçek zamanlı izlenmedi, yazı/ses senkronu ve sessizlik kesimlerinin kelimeleri kesmediği doğrulanmadı. Kullanıcı cihazında mobil okunurluk kontrolü yapılmadı.

## Başlık / açıklama / hashtag önerisi

Başlık: Soyunma Kabinindeki Ayna Hakkında Bilmen Gerekenler

Açıklama: Bu test, kaynak senaryonun kurgusunu değerlendirmek içindir. Videodaki tırnak ve yansıma boşluğuna dayalı çift taraflı ayna iddiası güvenilir değildir; görseller temsili yapay üretimdir. Kendinizi güvende hissetmediğiniz bir ortamdan çıkın ve gerektiğinde yetkililere başvurun. Siz kabine girdiğinizde neyi kontrol edersiniz?

#KadınGüvenliği #Mahremiyet #Farkındalık #KadıncaYaşam
