# VID-001 — Hareketli dış grafik testi

## Farklar ve sahne çizelgesi

Bu ayrı testte özgün anlatım ve önceki yüzsüz 5 yapay görsel korunur; Remotion ile sonradan eklenen vektör grafikler güçlendirilmiştir:

- 0–2,23 sn: “SOYUNMA KABİNİNDE / AYNAYA DİKKAT!” açılışı, hızlı sahne değişimi, çizilen ok ve bas vuruşu.
- 2,33–3,5 sn: parmak üzerinde çizgiyle beliren daire, okun ilerlemesi ve “TEMAS NOKTASI” kartı.
- 3,73–5,63 sn: hareketli ayna simgesi ve etiket; sahneye uygun ses vurgusu.
- 7,63–9,37 sn: parmak temasına ikinci animasyonlu daire ve ok.
- 9,6–11,6 sn: cam yüzeyini anlatan, üzerinde “TEMSİLİ” yazan şematik vektör; gerçek ölçüm veya tanı değildir.
- 11,97–13,67 sn: kapı simgesi ve hareketli “KABİNDEN ÇIK” kartı.
- 14,17–16,7 sn: yorum balonu simgesi.
- 17,83–20,23 sn: animasyonlu yorum ve paylaşım çağrısı, sesli kısa vurgular.

Kartlar, oklar ve şekiller `production/remotion/yeni-vid001-grafik-test.jsx` içinde kodlanmıştır: yay animasyonu, SVG çizgi reveal, konum/ölçek, yumuşak görünme ve kaybolma. Fiziksel nesne motion tracking veya gerçek 2.5D değildir. İlk 6 sn yaklaşık 1,65×, sonra 1,5×; tek parça özgün ses kullanıldı. Grafik ve altyazı zamanları yaklaşık, sesle tam senkronu dinlenerek doğrulanmadı.

## Görsel/ses ve lisans

Görseller: `test-parmak.png`, `yuzsuz-1.png`, `yeni-mirror-close.png`, `yuzsuz-2.png`, `yeni-support.png` — önceki sürümün 5 yapay görseli, hepsi yüzsüz ve temsili. Yapay parmak/yansıma bir cihaz testi ya da kanıt değildir. Kurgudaki açıklayıcı grafikler de temsili çizimdir.

Özgün `ozgun-anlatim.wav`; Juhani Junkala Peaceful Days CC0 (https://github.com/S3M1TR4SH/asset-library/blob/main/audio/music/juhani-junkala/INFO.txt); iki alçak seviyeli Wyzowl SFX Kit whoosh CC0 (https://github.com/wyzowl/sfx-kit); bas vuruşu ve grafik/etkileşim tonları `production/remotion/scripts/mix-yeni001-grafik.py` ile sentezlendi. Sesler insan tarafından dinlenmedi; otomatik ölçüm dinlemenin yerini tutmaz.

## Teknik QC

Remotion render ve FFmpeg miks; 1080×1920, 30 fps, H.264/AAC stereo 48 kHz, 20,23 sn, 4.193.980 bayt. Tam FFmpeg decode; blackdetect 0,2 sn ve silencedetect −55 dB/0,5 sn olay raporlamadı. Volumedetect ortalama −20,8 dB ve örnek maksimum −7,3 dB; true-peak değildir. Finalden saniyelik örnek kareler incelendi; tam video gerçek zamanlı izlenmedi, ses ve efektlerin tümü dinlenmedi, altyazı sesle zorlanmış hizalanmadı. Mobil cihazda test yapılmadı. Animasyonlar gözle seçilen sahne zamanlarına bağlıdır, güvenilir nesne takibi değildir.

## Başlık / açıklama / hashtag

**Başlık:** Soyunma Kabininde Ayna Hakkında Dikkat

**Açıklama:** Bu kurgu testi kaynak senaryoyu aynen kullanır. Videodaki tırnak ve yansıma arasındaki boşluğun iki yönlü aynayı kesin olarak belirlediği iddiası güvenilir değildir; görseller ve grafikler temsili yapay üretimdir. Kendinizi güvende hissetmediğiniz bir ortamdan çıkıp gerektiğinde yetkililere başvurun. Siz kabine girince neyi kontrol edersiniz?

#KadınGüvenliği #Mahremiyet #Farkındalık #KadıncaYaşam

**Doğruluk uyarısı:** Boşluk varlığı veya yokluğu aynanın iki yönlü olup olmadığını ya da izlenip izlenmediğinizi kesin göstermez. Kaynak: https://leadstories.com/hoax-alert/2022/09/fact-check-this-test-of-hotel-mirror-does-not-conclusively-demonstrate-if-it-is-2-way-mirror.html . Özgün senaryonun kullanılması güvenlik veya doğruluk onayı değildir.
