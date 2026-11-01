# VID-001 kaynakları

`VID-001-a.png` ... `d.png` Remotion kompozisyonunun incelenen kaynakları; `VID-001-raw.wav` özgün tek parça TTS, `VID-001-fast.wav` 1,45×. Bu görüntüler AI üretimidir. `review-original-paths.json` üretim zamanı SHA-256 ve öznel görsel kontrol notlarını saklar, yollar mevcut üretim ağacına göredir. Yeniden üretimde bunları `production/remotion/public/` altına aynı adlarla kopyalayıp inceleme yollarını yeniden doğrula. `production/remotion/vid001-captions.json` Vosk eşleşmesi/interpolasyonu ile yaklaşık sürelerdir (44/64 kelime eşleşti); kesin hizalama değildir. Videonun tamamı sesli incelenmedi. Senaryodaki bulaşık tableti, sirke karışımı ve kesin temizlik vaadi üreticinin çamaşır makinesi ve ürün talimatlarına uygunluğu doğrulanmamış bir öneridir.

Hareketli karşılaştırma sürümü: `production/remotion/vid001-motion.jsx` / `VID001Motion`. İlk sürüm korunmuştur. Kullanılan kelime zamanları yine kısmen tahmini; örnek kareler incelendi, ses baştan sona dinlenemedi. Derlemek için mevcut dosyaları public klasörüne kopyalayın ve görsel manifestiyle `render_reviewed.py` kullanın.

`production/remotion/vid001-v3.jsx` / `VID001V3`: çubuk ve bölüm başlıkları olmadan yeni grafikler içeren karşılaştırma sürümü. Kelime zamanları tahmini; referans görseller ve ses aynı, örnek kareler incelendi, video baştan sona dinlenmedi.

`production/remotion/vid001-hybrid.jsx` / `VID001Hybrid`: V4 örnek, fotoğraflar ile kodlanmış etiket/çizim ve sahne hareketlerini birleştirir; gerçek kesilmiş fotoğraf katmanları veya doğrulanmış 2.5D kullanmaz. Render sonrası 13 örnek kare ve tam teknik decode kontrol edildi; ses baştan sona dinlenmedi ve altyazı zamanları kısmen tahmini.
