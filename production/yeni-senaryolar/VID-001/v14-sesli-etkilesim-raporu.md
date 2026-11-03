# VID-001 — V14 sesli etkileşim testi

Önceki testteki beş yüzsüz yapay görsel, 1,55× eski seçili ses kaydı ve kaynaklar `155-test-raporu.md` ve `hareketli-grafik-teslim.md` içindedir. Eski ses kaydında 'kız arkadaşlarına' bulunduğu için ses 22,78. kaynak saniyede kesilir; kapanıştaki 'arkadaşına göndermeyi unutma' sadece ekrandadır. Ses kesimi ve altyazı zamanlaması dinlenerek doğrulanmadı.

V14 kaynak kompozisyonundaki gerçek sentez efektleri kullanıldı: `sfx-hook-merak.wav` girişte, `sfx-isin.wav` bilgilendirme grafiklerinde, `sfx-result-chime.wav` etkileşim ekranı girişinde, `sfx-kaydet.wav` beş düğmenin basılma anlarında. Dosyalar `production/remotion/scripts/make-hook-save-sfx.py`, `make-beam-sfx.py`, `make-result-chime.py` ile yeniden üretilir. Müzik Peaceful Days CC0 ve iki düşük seviyeli CC0 whoosh; detay önceki raporda. Kapanış düğmeleri birlikte yaylanarak gelir, ardından sırayla küçülüp üstlerinde kısa sarı/beyaz parçacık patlamaları ve tıklama duyulur. Nesneyi yanlış işaretleme riskine karşı önceki parmak okları kullanılmaz.

Remotion kaynağı `production/remotion/yeni-vid001-v14-etkilesim.jsx`; miks `production/remotion/scripts/mix-yeni001-v14-etkilesim.py`. 1080×1920, 30 fps, H.264/AAC, 20,23 sn. Final tam FFmpeg decode edildi; önceki aynı ses miksinde blackdetect olay bildirmedi, ortalama −21,4 dB ve örnek maksimum −7,0 dB; true-peak değil. Önceki renderın bir kapanış karesi incelenip çakışan mesaj simgesi son renderda kaldırıldı. Final video baştan sona izlenmedi, ses ve senkron kulakla doğrulanmadı, mobil cihazda test edilmedi.

Başlık: Soyunma Kabininde Ayna Hakkında Dikkat. Açıklama: Mahremiyet konusunda şüphe duyduğunuz ortamdan çıkıp gerektiğinde yetkililere başvurun. Siz kabine girdiğinizde neyi kontrol edersiniz? #KadınGüvenliği #Mahremiyet #Farkındalık #KadıncaYaşam

**Güvenlik:** Tırnakla boşluk kontrolü iki yönlü aynayı kesin belirlemez; özgün senaryodaki iddia güvenilir değildir. https://leadstories.com/hoax-alert/2022/09/fact-check-this-test-of-hotel-mirror-does-not-conclusively-demonstrate-if-it-is-2-way-mirror.html
