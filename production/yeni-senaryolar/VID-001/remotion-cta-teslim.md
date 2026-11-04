# Yeni VID-001 — Remotion hook ve etkileşim test raporu

## Kapsam ve önemli doğruluk uyarısı

Bu ayrı test sürümünde kullanıcının istediği özgün senaryo ve daha önce oluşturulan tek parça ses yeniden kullanıldı. Senaryodaki tırnak ve yansıma arasındaki boşluğun iki yönlü aynayı kesin olarak belirlediği iddiası güvenilir değildir. Boşluk olması da mahremiyet garantisi değildir. Kaynak: https://leadstories.com/hoax-alert/2022/09/fact-check-this-test-of-hotel-mirror-does-not-conclusively-demonstrate-if-it-is-2-way-mirror.html . Yapay görseller gerçek test veya güvenlik kanıtı değildir. Bu nedenle kurgu testi, güvenle yayınlanabilecek doğrulanmış bir içerik değildir.

## Sahne çizelgesi

- 0–2,23 sn: parmak ve ayna görseli; 0,7 sn civarında kabin aynasına hızlı kesme; “SOYUNMA KABİNİNDE / AYNAYA DİKKAT!” hook, animasyonlu ok ve 0,5 sn bas vuruşu.
- 2,23–11,63 sn: parmak, ayna ve kabin detayları; hareketli kadraj ve ilgili kısmi yazılar. Bazı karelerde sarı çizgi/ok vurgusu.
- 11,63–17,83 sn: kabinden çıkış ve telefon görseli; soru, yorum ve paylaşım anlatımı.
- 17,83–20,23 sn: Remotion ile hareketlenen “Sen neyi kontrol edersin?”, yorum butonu ve arkadaşla paylaş çağrısı; iki sentezlenmiş kısa chime efekti. CTA özgün sesin bitişine yaklaşık 0,19 sn kala açılır; yeni bir seslendirme eklenmemiştir.

## Görsel ve ses listesi

- `test-parmak.png`, `yuzsuz-1.png`, `yuzsuz-2.png` önceki testten; `yeni-mirror-close.png` ve `yeni-support.png` bu test için üretildi. Toplam 5 yüzsüz yapay görüntü; her biri ve tamamından 1 saniye arayla örnek kareler incelendi. Mekânlar farklı yapay görsellerdir; devamlılık garantisi yok. Kaynak görsellerin 1080p'ye yükseltilmesi yeni detay eklemez.
- `ozgun-anlatim.wav`: özgün metnin önceki tek parça kadın sesi. Ham kaynakta 0,31–10,21 sn 1,65×, devamı 1,5×; yaklaşık ilk 6 çıkış saniyesi hızlı bölüm. Kullanıcı talimatındaki 5/6 sn çakışmasında 6 sn seçildi. Kesme sınırı ve konuşmanın anlaşılabilirliği dinlenerek doğrulanmadı.
- Müzik: Juhani Junkala, Peaceful Days, CC0 1.0; https://github.com/S3M1TR4SH/asset-library/blob/main/audio/music/juhani-junkala/INFO.txt . İki hafif whoosh: Wyzowl SFX Kit, CC0, https://github.com/wyzowl/sfx-kit . Bas vuruşu ve kapanıştaki iki UI tonu bu proje betiğinde sentezlendi. Müzik −22 dB ve sentez −8 dB filtre kazançları ölçülmüş nihai düzeyler değildir; limiter kullanıldı.

## Animasyon ve kalite kontrol

`production/remotion/yeni-vid001-cta-test.jsx` ve `production/remotion/scripts/mix-yeni001-cta.py`: Remotion 4 ile sahneye göre zoom/pan ve kesme, hook girişi, SVG çizimi, kısa iki kelimeli aktif sarı altyazı, son CTA spring animasyonu. FFmpeg ile özgün sesin hızlandırılması, CC0 müzik, SFX miks ve AAC eşleme; video son aşamada yeniden kodlanmadı. Gerçek video, hareket takibi veya 2.5D yoktur.

1080×1920, 9:16, H.264/AAC stereo 48 kHz, 30 fps, 20,23 sn, 4.034.315 bayt. FFmpeg tam decode; blackdetect 0,2 sn ve silencedetect −55 dB/0,5 sn olay bildirmedi. Volumedetect ortalama −20,8 dB, örnek maksimum −7,3 dB; true-peak değildir. Başlangıç/bitiş efektleri, müzik dengesi ve sesin tamamı insan tarafından dinlenmedi; video tamamen gerçek zamanlı izlenmedi. Altyazı zamanları karakter uzunluğu ile tahminidir; sesle kelime senkronu ve hız anlaşılabilirliği doğrulanmadı. Fiziksel telefonda güvenli alan kontrolü yapılmadı. Viral sonuç garantisi yok.

## Başlık, açıklama, hashtag

**Başlık:** Soyunma Kabininde Ayna Hakkında Dikkat

**Açıklama:** Bu kurgu testi, kaynak senaryoyu aynen kullanıyor. Videodaki tırnak ve yansıma boşluğunun çift taraflı aynayı kesin belirlediği iddiası güvenilir değildir. Görseller temsili yapay üretimdir. Kendinizi güvende hissetmediğiniz ortamdan çıkın ve gerektiğinde yetkililere başvurun. Siz kabine girince neyi kontrol edersiniz?

#KadınGüvenliği #Mahremiyet #Farkındalık #KadıncaYaşam
