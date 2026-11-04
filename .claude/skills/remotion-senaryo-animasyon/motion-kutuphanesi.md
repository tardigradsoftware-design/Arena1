# Remotion Motion Skill Library — v1.0 uyarlaması

Kullanıcının paylaştığı kütüphaneye dayanan genişletilebilir **tasarım ve planlama kataloğu**. Bir ID'nin burada bulunması, o bileşenin kodlandığı, otomatik seçim/senkron/takibin çalıştığı veya test edildiği anlamına gelmez. Her üretimde anlamı değerlendir, uygun olan az sayıdaki öğeyi seç; yeni öğeleri uygulayıp test ettikçe durumunu ayrıca belirt.

| ID | Animasyon ve kullanım fikri |
|---|---|
| MOT-001 | Zaman geçişi: gerçek süre/bekleme anlatıldığında analog saat, ibre ve uygun tik tak. |
| MOT-002 | Soru: anlamlı soru işareti, ölçek ve hafif sallanma; 3D yalnızca gerçekten uygulandıysa. |
| MOT-003 | Fikir/düşünme: ampulün yanması ve ölçülü ışık. |
| MOT-004 | Dikkat: ölçülü ünlem/kırmızı vurgu, bağlama uygun uyarı sesi; risk uydurma. |
| MOT-005 | Önce/sonra: gerçek ve uygun karşılaştırmayı sıralı veya bölünmüş geçişle göster; yapay görseli kanıt sayma. |
| MOT-006 | Dinamik altyazı: V14 aktif kelime vurgusu, hafif eğim ve oturma. |
| MOT-007 | Ses senkronizasyonu: animasyon giriş ve vurgularını anlatım/efekt/müzik ile eşleştir. |
| MOT-008 | Nesne dönüşümü: tanıtılan nesnenin perspektif/ölçek değişimi; gerçek 3D yalnızca mevcut ve uygunsa, aksi halde 2D. |
| MOT-009 | Sonuç/doğrulama: gösterilmiş ve doğrulanmış sonuçta tik, parıltı ve başarı sesi; doğrulanmamış iddiayı onaylama. |
| MOT-010 | Akışkan geçiş: konuya uygun maske, morph veya basit geçiş; anlamı ve okunabilirliği koru. |
| MOT-011 | Fiziksel hareket: ilgili olaya uygun düşme, yaylanma ve momentum; gerçek fizik simülasyonu yapıldıysa öyle adlandır. |
| MOT-012 | Nesne vurgusu/takibi: doğru hedefe ok, çember veya etiket; gerçek hareketli nesne takibi sadece uygun yöntemle yapılıp doğrulandığında. |
| MOT-013 | İnceleme/keşif: büyüteç veya tarama; teşhis ve tespit iddiası üretme. |
| MOT-014 | Güzellik/bakım: serum, damla, sınırlı parıltı veya açıkça temsili cilt katmanı. |
| MOT-015 | Mutfak: işlemle uyumlu buhar, saat, sıcaklık, karıştırma hareketi ve iş sesi. |
| MOT-016 | Zoom/kamera: sahneye ve önemli detaya uygun net zoom/pan; pikselli büyütme yok. |
| MOT-017 | Parıltı: gerektiğinde ölçülü ışık çizgisi/glow/parçacık; aşırı süsleme yok. |
| MOT-018 | Saç bakımı: saç teli veya parlaklık temsili; gerçek olmayan sonucu kanıt gibi gösterme. |
| MOT-019 | Ev temizliği: uygun işlemde silinme, köpük veya sprey; kesin hijyen/etki iddiası ekleme. |
| MOT-020 | Freeze frame: kritik anı kısa dondurup doğru hedefi işaretle. |
| MOT-021 | Sayısal sayaç: yüzde, miktar veya süre. **Kullanıcının mevcut V14 sayaç yasağı nedeniyle varsayılan kapalı; yalnızca özel izinle kullan.** Sayı doğrulanmış olmalı. |
| MOT-022 | Duygu: sahneyle uyumlu şaşkınlık, merak, korku veya rahatlama sembolleri; desteklenmeyen korku yaratma. |
| MOT-023 | Parallax: gerçek katmanlarla ön/orta/arka plan hareketi; basit zoomu gerçek 2.5D veya tracking diye sunma. |

## Seçim ve uygulama

1. Metni cümle/sahnelere ayır; tek kelime eşleşmesi yerine niyeti, gerçek işlemi, gösterilebilir nesneyi ve bağlamı değerlendir. Anlatımın anlamı veya kanıtı desteklemiyorsa animasyon seçme.
2. Seçilen ID'ler için başlangıç/bitiş, hedef nesne, varlık, renk/yoğunluk, katman, ses ve kaynak planla; gerektiğinde aynı sahnede birden fazla animasyonu okunabilirlik kaybolmadan birleştir. Her cümleye zorunlu animasyon ekleme.
3. Remotion `useCurrentFrame`, `useVideoConfig`, `interpolate`, `spring`, `Sequence`, `AbsoluteFill`, `Audio`, `staticFile` kullanarak kare bazlı deterministik bileşenler üret; parametreleri ihtiyaç oldukça başlangıç, süre, yoğunluk ve renk olarak aç. Varlık yoksa bağlama uygun sade alternatif veya kullanıcı onayı kullan.
4. Öneri olarak 30 fps'de kısa 12–24, orta 24–45, uzun 45–90 kare, geçiş 12–24 kare; bağlam, hız ve kullanıcının en fazla iki saniyelik bitiş şartı daha önceliklidir. 1080×1920, 9:16 varsayılan.
5. Gerektiğinde gerçek 3D veya gerçek nesne takip yöntemlerini araştır ve uygula; uygulanmadıysa uygulandı deme. Kaynak-katman dönüşümünü paylaşmak tek başına nesne tracking değildir. `SKILL.md` doğru işaretleme kapısını uygula. Hafif 2D alternatifleri tercih et; ayrı düşük/yüksek performans sürümleri ancak gerçekte geliştirilip test edildiğinde mevcut sayılır.
6. Render öncesi/sonrası sahne-anlam eşleşmesi, doğru hedef, hareket ve geçiş, ses/altyazı senkronu, karmaşa, okunabilirlik, dikey güvenli alan ve mümkünse cihaz kontrolü yap. Otomatik ölçümü dinleme/izleme yerine geçirme; yapılmayan kontrolü belirt.

Örnek: '10 dakika içinde farkı göreceksiniz' için süre gerçekse MOT-001 ve işlemi temsil eden hareket düşünülebilir; önce/sonra veya başarı efekti yalnızca karşılaştırma gerçekten güvenilir biçimde gösterilebiliyorsa eklenir. Senaryodaki süre ve sonuç iddiaları ayrıca doğrulanmadan kesinlik kazandırılmaz.

Yeni animasyon fikirleri eklenebilir; yeni bileşenler gerçek render ve uygun sahne testlerinden sonra uygulanmış olarak işaretlenmelidir. Skill ve katalog kullanıcının en güncel talimatlarını geçersiz kılmaz.

## Programatik uygulama notları (araştırma, 2026-11)
- Remotion kare tabanlı `spring` ve `interpolate` ile giriş/çıkışları deterministik kur; `Sequence` ile sahne içi yerel zamanı ayır. Aynı kaynaktan gelen 2B görüntü ve kırmızı vurguyu birlikte dönüştür (MOT-020/023). Nesne takibi yapılmadıysa tracking iddia etme.
- Gerçek işlem varsa adımları kademeli göster (MOT-005); gerçek süre varsa dönen ibre ve eşzamanlı tik tak (MOT-001). Animasyonları gerekçesiz sayaca, maskota veya dekoratif parıltıya dönüştürme. Görselde doğrulanamayan sonuç için başarılı sonuç rozeti veya yanıltıcı karşılaştırma yapma.
- `@remotion/transitions` içindeki `TransitionSeries` ve `linearTiming`/`springTiming` yumuşak fade, slide veya wipe için seçeneklerdir; sahne süresi örtüşmesini ve ses zamanını hesapla, bütün sahnelere aynı geçişi zorla uygulama. Bu paketin varlığı geçişlerin her videoda kullanıldığı anlamına gelmez.
- SVG çizgilerini kareye bağlı `strokeDashoffset` ile aç; giriş yönlerini ve yoğunluğu sahne, görsel güvenli alan ve anlatıya göre ayarla. Tarayıcı saatine bağlı CSS/SMIL animasyonları yerine video karelerinden hesaplanan değerleri tercih et.
- Gerçek katmanlar olmadan parallax/3D/tracking yapılmış gibi sunma. Taslak video karelerini giriş, hedef, grafik, CTA ve kapanış boyunca al; V14 kelime zamanları interpolasyonsa yalnızca tahmin say. Ses seviyesini analiz etmek tam dinlemenin yerine geçmez.
- Kaynaklar: https://www.remotion.dev/docs/dataset-render ; https://www.remotion.dev/docs/transitioning ; https://www.remotion.dev/docs/animations ; https://github.com/reactvideoeditor/remotion-templates (fikir taraması: depo API'sinde lisans belirtilmemişti; kod veya varlıkları izin/lisans doğrulanmadan kopyalama).
