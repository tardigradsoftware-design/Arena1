# VID-001 — hızlı ritimli HD test

Video: https://drive.google.com/file/d/1K-hq3N1x8MOkBUVA5lQZYFddpkSf7YKb/view

## Kurgu ve sahne çizelgesi

- 0–2,2 sn: sararmış yastık kılıfı ve ilk kareden hook.
- 2,2–6,27 sn: aynı kılıfın farklı kadrajları ve anlatım altyazısı.
- 6,27–11,27 sn: makine/tablet görüntüsünde malzeme metin ve ikonları.
- 11,27–15,33 sn: makine görseli, 60 derece/program kartı.
- 15,33–20,67 sn: katlanmış kılıfların temsili yapay görseli ve kaydet vurgusu.
- 20,67–23,67 sn: beğen, takip, paylaş ve yorum çağrısı; seslendirilmemiştir.

Önceki versiyona göre yaklaşık her saniye daha hızlı kadraj kesmeleri, fotoğraf kaydırma ve zoomları, ana sahnelerde sarı çapraz wipe, kısa vurgu çizgileri ve aktif altyazı kelimesinde hızlı ölçek animasyonu eklendi. Kesme anlarına alçak seviyeli sentez perküsyon eklendi. Yeni çekim veya hareketli video üretilmedi: dört eski fotoğraf yeniden kadrajlandı, dolayısıyla sahneler gerçek hareketli çekim değil. Gerçek 2.5D ve motion tracking yoktur.

## Görsel, ses ve lisans

Görseller `VID-001-a.png`–`VID-001-d.png` aynı önceden üretilmiş yapay görsellerdir; `production/vid001-v6-review.json` SHA/inceleme manifesti kullanıldı. Kaynak fotoğrafların 1080p'ye yükseltilmesi yeni ayrıntı yaratmaz. Önceki 1,45× özgün tek parça kadın anlatımı (`VID-001-fast.wav`), Peaceful Days / Juhani Junkala müziği (CC0), Wyzowl SFX Kit whoosh (CC0) ve proje için sentezlenmiş hook, beam, result ve save efektleri kullanıldı. Ek vurgu perküsyonu `mix-vid001-dinamik.py` tarafından sentezlenir; harici örnek içermez. Kaynak ve bağlantı ayrıntıları `sinematik-teslim-raporu.md` ve `production/assets/CREDITS.md` içinde.

## Teknik QC ve sınırlamalar

1080×1920, 30 fps, H.264/AAC stereo, 48 kHz, 23,67 sn, 7.010.263 bayt. SHA kontrolü ve FFmpeg tam decode tamamlandı; blackdetect 0,2 sn ve silencedetect −55 dB/0,5 sn eşikleriyle olay raporlanmadı. `volumedetect` ortalama −21,3 dB, örnek maksimum −5,9 dB; gerçek dinleme veya true-peak denetimi değildir. Çıkarılan saniyelik 24 kare görsel olarak incelendi, ancak tam video izlenmedi ve ses baştan sona dinlenmedi. Bazı altyazı zamanları tahmini; ses/yazı tam senkronu ve fiziksel mobil cihazda okunurluk doğrulanmadı. Yüksek kare hızı veya viral performans garantisi yoktur.

## Başlık, açıklama, etiketler

**Başlık:** Sararmış Yastık Kılıfları Hakkında Bir Fikir | Kadınca Yaşam

**Açıklama:** Sararmış yastık kılıfları konusunda bir yöntem anlatılıyor. Videodaki karışımın cihaz ve ürün uyumluluğu ile ileri sürülen sonuç doğrulanmamıştır. Çamaşır makinesi, deterjan ve kumaşın üretici talimatlarını izleyin; klor içeren ürünleri sirkeyle karıştırmayın. Sizin çamaşır bakımı için tercih ettiğiniz yöntem nedir?

**Hashtag:** #ÇamaşırBakımı #YastıkKılıfı #EvDüzeni #PratikHayat #KadıncaYaşam

**Önemli:** Özgün anlatım kullanıcı isteğiyle değiştirilmemiştir. Tablet + karbonat + sirke önerisinin ürün/makineye uygunluğu ve tek yıkamada sonuç iddiası doğrulanmadı. Klor içeren ürünlerin sirkeyle karıştırılması zararlı gaz çıkarabilir. Temsili yapay sonuç görüntüsü gerçek sonuç kanıtı değildir; uyarı eklenmesi videodaki tehlikeli öneriyi düzeltmez. Güvenli yayın için içerik düzeltilmelidir.
