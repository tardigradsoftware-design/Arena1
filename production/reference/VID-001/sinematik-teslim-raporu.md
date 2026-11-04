# VID-001 — Sinematik HD test ve kalite raporu

## Teslim

- Test videosu: https://drive.google.com/file/d/1u3PSuQJ3d8qsb-jyOEmW9b5lMRixacue/view
- Sadece test amaçlı; eski video ve önceki test korunmuştur. Kaynak anlatım kullanıcının isteğiyle aynen yeniden kullanıldı, kapanışa yeni sessiz CTA eklendi.
- Orijinal anlatımdaki bulaşık makinesi tableti, karbonat, sirke ve 60 derece önerisinin ürün/makine uygunluğu ve tek seferde tüm lekelerin çıkacağı iddiası doğrulanmadı. Klor içeren ürünleri sirkeyle karıştırmak zararlı gaz çıkarabilir. Uyarı açıklaması veya test kurgusu videodaki riski düzeltmez; güvenli yayın için içerik düzeltilmelidir.

## Video başlığı

Sararmış Yastık Kılıfları Hakkında Bir Fikir | Kadınca Yaşam

## Açıklama

Sararmış yastık kılıfları konusunda bir yöntem anlatılıyor. Videodaki karışımın cihaz ve ürün uyumluluğu ile ileri sürülen sonuç doğrulanmamıştır. Çamaşır makinesi, deterjan ve kumaşın üretici talimatlarını izleyin; klor içeren ürünleri sirkeyle karıştırmayın. Sizin çamaşır bakımı için tercih ettiğiniz yöntem nedir?

Bu uyarı videodaki öneriyi düzeltmez; video güvenli hâle getirilmeden yayıma uygun kabul edilmemelidir.

## Hashtag önerileri

#ÇamaşırBakımı #YastıkKılıfı #EvDüzeni #PratikHayat #KadıncaYaşam

## Sahne zaman çizelgesi ve görsel/efektler

| Süre (yaklaşık) | Görsel/kurgu | Ses |
|---|---|---|
| 0–2,2 sn | `VID-001-a.png` sararmış kılıf; ilk kareden güçlü sarı hook, çizilen ok ve ışık şeridi | Özgün anlatım, sentezlenmiş hook sesi |
| 2,2–6,3 sn | Kılıfa yumuşak yakınlaşma, konu kartı, kısa sarı aktif kelime altyazısı | Özgün anlatım ve alçak seviyeli müzik |
| 6,3–11,3 sn | `VID-001-b.png` makine/tablet; her malzemeye küçük SVG/ok; yanal geçiş | Alçak seviyeli whoosh ve bilgi grafiklerine sentezlenmiş ışın sesleri |
| 11,3–15,3 sn | `VID-001-c.png` makine ve 60 derece kartı, çizilen daire | Anlatım, müzik, bilgi grafik sesi |
| 15,3–20,67 sn | `VID-001-d.png` katlanmış beyaz kılıfların yapay temsili; çizgi ve kaydet vurgusu. Temsili görüntü sonucu kanıtlamaz | Yumuşak whoosh, sentezlenmiş sonuç ve kaydet sesleri |
| 20,67–23,67 sn | Kapanış: beğen, takip et, paylaş ve yorum; kullanıcı adı | Müzik yumuşak azalır; CTA seslendirilmemiştir |

Hareket: fotoğraflarda ölçülü yakınlaşma ve kadraj kaydırmaları, kaydırmalı geçişler, vektör çizimleri, kanca ışık şeridi ve söz kartları. Gerçek derinlik haritası, nesne ayrıştırmalı 2.5D parallax, gerçek motion tracking, profesyonel motion blur ve kusursuz döngü uygulanmadı. Daha doğal derinlik ve daha anlamlı CTA sorusu sonraki testte geliştirilebilir; mevcut yaklaşım hâlâ durağan fotoğraflara dayanmaktadır.

## Kullanılan kaynaklar

- Görseller: `production/reference/VID-001/VID-001-{a,b,c,d}.png`; daha önce üretilmiş ve incelenmiş yapay görseller. SHA manifesti `production/vid001-v6-review.json`; görseller gerçek çekim veya sonuç kanıtı değildir.
- Anlatım: `production/reference/VID-001/VID-001-fast.wav`, önceki 1,45× tek parça özgün seslendirme. Yeni ses üretilmedi.
- Müzik: Juhani Junkala, Peaceful Days, CC0 1.0; https://github.com/S3M1TR4SH/asset-library/blob/main/audio/music/juhani-junkala/INFO.txt .
- Geçiş sesi: Wyzowl SFX Kit `whoosh.wav`, CC0 1.0; https://github.com/wyzowl/sfx-kit .
- Hook, ışın, sonuç ve kaydet: bu proje için sentezlenen sesler; betikleri `production/remotion/scripts/make-hook-save-sfx.py`, `make-beam-sfx.py`, `make-result-chime.py`. Yeni bir harici lisans gerektiren kayıt kullanılmadı.
- Kod: `production/remotion/vid001-sinematik-hd.jsx`, `production/remotion/scripts/mix-vid001-sinematik.py`. Remotion 4.0.539 ve imageio-ffmpeg ile sağlanan FFmpeg kullanıldı. Sessiz görsel render Remotion, ses miksajı/son MP4 eşlemesi FFmpeg; video son aşamada yeniden kodlanmadı.

## Teknik kalite kontrolü

- 1080×1920, dikey 9:16, H.264, 30 fps; AAC 48 kHz stereo yaklaşık 128 kbit/s. 23,67 sn; 5.877.440 bayt. Kaynak fotoğraflar yükseltildi; 1080p'ye büyütmek kaynakta olmayan ayrıntı yaratmaz.
- Görseller önceki SHA manifestiyle eşleşti. Önceki renderdan saniyede bir örnek kare ve son renderın CTA karesi görsel olarak incelendi; CTA okunurluğu büyütülerek revize edildi. Bu, videonun bütün karelerinin insan gözüyle izlendiği anlamına gelmez.
- Finalde tam teknik decode ve `blackdetect` (0,2 sn eşik) ile siyah bölüm saptanmadı; `silencedetect` (−55 dB, 0,5 sn) sessiz bölüm bildirmedi. FFmpeg `volumedetect`: ortalama −21,3 dB, maksimum −5,9 dB; bunlar gerçek dinleme ya da true-peak ölçümü değildir.
- Ses baştan sona dinlenmedi. Altyazıların bir kısmı Vosk eşleşmesi ve interpolasyondur; zorlanmış hizalama ve bütün kelimelerin işitsel senkronu doğrulanmadı. Mobil ekran testi fiziksel cihazda yapılmadı, yalnız çıkarılan karede görsel boyut gözlendi. Yanıltıcı iddiaların doğruluğu veya algoritmik/viral performans test edilmedi.
