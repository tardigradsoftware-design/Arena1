# VID-001 — yüzsüz V14 tarzı hız testi

## Kurgu ve teknik detay

Kullanıcı isteği doğrultusunda insan yüzü yok; özgün senaryo seslendirmesi yeniden kullanıldı. Hız talepleri (ilk 6 saniye ve 5. saniyeden sonra) çakıştığı için ilk **6 çıkış saniyesinde 1,65×**, devamında 1,5× seçildi. Ham sesteki başlangıç sessizliğinden 0,31 sn kırpıldı; ham ses 0,31–10,21 sn 1,65×, devamı 1,5× işlendi. Bu düzenleme tam 6 sn hedefler; geçiş dinlenerek doğrulanmadı. Uzun sessizlikleri sonradan otomatik kesmek, 6 saniyelik sınırı kaydıracağından bu sürümde ayrıca uygulanmadı.

Önceki V14'ten esinlenilmiş tam ekran fotoğraflar, sarı aktif kelime ve beyaz diğer kelime, güçlü ilk kare “AYNAYA DİKKAT!”, kısa yakınlaşma, geçişler, marka ve anlatım. Anlatımla aynı hook cümlesi eşzamanlı tekrarlanmaz. Sayaç, maskot ve ilerleme çubuğu yok. Fotoğraflardan hareket elde edildi; gerçek eylem videosu veya gerçek 2.5D/tracking yoktur.

**Sahneler:** Yaklaşık 0–6,3 sn: `test-parmak.png` yakın plan, sarı kanca, parmak/yansıma; yaklaşık 6,3–12,6 sn: `yuzsuz-1.png` boş kabin aynası; yaklaşık 12,6–18,53 sn: `yuzsuz-2.png` mağaza çıkışı ve soru. Her biri yapay üretim; aynanın görünümü veya parmak görseli gerçek test veya gözlem kanıtı değildir. Tek tek üç görsel ve nihai videodan saniyelik kareler incelendi. Görseller birbirinden bağımsız sahneler; aynı mekân oldukları doğrulanmadı.

**Ses:** `ozgun-anlatim.wav` özgün senaryodan oluşturulmuş seçili Türkçe kadın sesi; Juhani Junkala Peaceful Days, CC0 1.0 https://github.com/S3M1TR4SH/asset-library/blob/main/audio/music/juhani-junkala/INFO.txt ; 0,5 sn bas vuruşu kurguda sentezlendi. Müzik −22 dB, vuruş −8 dB filtre kazancı, limiter. Bunlar toplam çıkış veya sesle ölçülmüş gerçek dB farkı değildir.

**Altyazı:** Karakter uzunluğuna dayanan tahmini zamanlamadır; zorlanmış ses hizalaması yapılmadı. İlk 2,1 sn hook ve altyazı tekrarı olmasın diye ilk kelimelerin altyazısı gösterilmedi. Kelime senkronu ve hızlı anlatımın anlaşılabilirliği baştan sona dinlenerek doğrulanmadı. Bu nedenle seri üretim için kalite onayı değildir.

## QC

1080×1920, 30 fps, H.264/AAC stereo 48 kHz, 18,53 sn, 1.997.499 bayt. FFmpeg tam decode, blackdetect 0,2 sn ve silencedetect −55 dB/0,5 sn olay bildirmedi. Volumedetect ortalama −20,4 dB, örnek maksimum −7,3 dB; true peak veya gerçek dinleme testi değildir. Tam video izlenmedi, tüm ses dinlenmedi, fiziksel mobil cihazda okunurluk kontrol edilmedi.

## Başlık ve açıklama önerisi

**Başlık:** Soyunma Kabininde Ayna Testi

**Açıklama:** Bu örnek, orijinal senaryonun kurgu ve hız testidir. Video içindeki tırnak ve yansıma arasındaki boşluğun iki yönlü aynayı kesin olarak belirlediği iddiası güvenilir değildir. Görseller temsili yapay üretimdir. Mahremiyetinizden şüphe duyarsanız ortamdan çıkıp sorumlu yetkiliye veya gerektiğinde polise başvurun. Siz kabine girince neyi kontrol edersiniz?

**Hashtag:** #KadınGüvenliği #Mahremiyet #Farkındalık #KadıncaYaşam

**Kritik doğruluk notu:** Senaryoda iddia edildiği gibi tırnakla yansıma arasındaki boşluk veya boşluk yokluğu, aynanın iki yönlü olduğunu ya da izlenip izlenmediğinizi kesin olarak göstermez. Özgün metin kullanıcının isteğiyle korunmuştur; bu durum uyarıyı ortadan kaldırmaz. Kaynak: https://leadstories.com/hoax-alert/2022/09/fact-check-this-test-of-hotel-mirror-does-not-conclusively-demonstrate-if-it-is-2-way-mirror.html
