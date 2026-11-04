---
name: remotion-senaryo-animasyon
description: Kadınca Yaşam kısa videolarında senaryoya uygun Remotion animasyonları, doğru nesne vurgusu, eşzamanlı ses efektleri ve hızlı etkileşim kapanışı tasarlar. Senaryo videosu, hareketli grafik, işaretleme, hook veya etkileşim animasyonu üretirken kullan.
---

# Senaryoya uygun Remotion animasyonu

Önce `production/yeni-senaryolar/TERCIHLER.md`, bu skill yanındaki `motion-kutuphanesi.md` kataloğunu ve ilgili senaryoyu oku. Kullanıcının en güncel talimatı önce gelir; özgün metni izinsiz değiştirme. Yanlış veya tehlikeli iddiayı ayrı bildir, animasyonla doğrulanmış gibi gösterme. İnsan yüzü kullanma. Video başına en az dört sahneye uygun görsel, 1080×1920, gerçek Remotion, onaylı V14 altyazı; ses hızı varsayılan 1,55×. Kullanıcı prompt vermese de sahne planını kendin üret.

## Öncelikli güncel kurallar
- Tüm anlatımı, onaylanmış iki eylemli kapanış dâhil, seçilen sesle tek seferde bir bütün olarak üret. Ayrı sesli çağrı üretip sonradan ekleme veya anlatım parçalarını birleştirme. Kullanıcının özgün metin ve onay sınırlarına uy; gerekirse önce izin al. Müzik/SFX ayrıca mikslenebilir.
- Vurgulanacak doğru noktalar görselde gerçekten doğrulandığında kırmızı, hafif düzensiz görünmez kalemle göster ve kamera hareketiyle aynı dönüşümü uygula. Doğrulanamayan noktaları çizme; eksikliği bildir.
- Uygun sahnelerde daha fazla anlamlı Remotion SVG animasyonu kullan; ana eylem ve altyazıyı kapatma. Her video için konuya uygun farklı, özgün bir giriş sesi sentezle; ses anlatımı bastırmasın. Sahne, anlatım, ses ve çizgiler tutarlı olsun.
- Sesli kapanış çağrısı sırasında altyazı gösterme; uygun çağrı düğmeleri/grafikleri kalabilir. Kapanış tarzı son testten sonra henüz onaylanmadı. Bu kurallar aşağıdaki eski örneklerin üzerinde önceliklidir.

## Akış
1. Metni anlamlı cümlelere böl. Her cümle için görsel, önemli nesne, yaklaşık ses zamanı, animasyon ve efekt planla. Bütün animasyonları her videoya yığma: sadece anlatılan olaya, nesneye ve kelimeye uygun olanları seç. İşlem, sonuç, süre veya tehlike uydurma.
2. Görselleri üret ve tek tek incele; sahne ile anlatım, fizik, anatomi ve nesnelerin konumu tutarlı mı kontrol et. Önemli noktaları ana nesneyi/altyazıyı kapatmadan göster. Hızlı, enerjik ama anlaşılır hareket; pikselli zoom ve titreme yok.
3. Her sahnede önce aşağıdaki doğru işaretleme kapısını uygula. Ardından grafik hareketlerini Remotion ile kareye bağlı, deterministik olarak yaz; sahne ve ses zamanına yerleştir. Hook'a özgü vurgu ve seçilen animasyona uygun, lisanslı veya sentezlenmiş efekt ekle; anlatımı bastırma.
4. Altyazı V14: kısa alt-orta kelime grupları, aktif sarı/siyah, diğerleri beyaz/siyah, okunabilir ufak eğim ve hafif oturma hareketi. Hook ile aynı yazıyı eşzamanlı tekrarlama. Zamanlar yaklaşık ise kesinmiş gibi sunma.
5. Kapanışa senaryoya doğal uygun sesli yorum/kaydetme/abonelik teşviki koy; özgün metnin değiştirilmesi gerekiyorsa önceden izin al. Kullanıcının seçtiği ses kimliği kullanılamıyorsa yeni ses uydurma, uygun seçeneği kullanıcıyla çöz. Türkçe özgün SVG etkileşim düğmeleri birlikte belirir, hızla basılır, kısa parçacık ve click sesiyle en fazla iki saniyede tamamlanır; hemen ardından video biter. Kapanışta 'kız arkadaşına' yerine kullanıcının izin verdiği 'arkadaşına göndermeyi unutma' kullanılabilir.
6. Videoyu mümkünse baştan sona izle ve dinle. Örnek kareler, tam decode, siyah/sessiz bölüm, ses seviyesi, metin, anlatım/efekt/altyazı eşleşmesi ve mobil okunabilirliği kontrol et; yapılmayan kontrolü dürüstçe belirt. Her test için ayrı MD raporu ya da Drive raporu oluşturma; önemli sınırlamaları kısa mesajda bildir.

## Animasyon ve ses sözlüğü
- Süre geçmesi: analog saat/kum saati, tik tak. Yalnızca senaryoda gerçekten süre varsa.
- Soru: kısa soru işareti/konuşma balonu, merak sesi. Düşünce/fikir: ampul ve hafif parlama.
- Önemli uyarı: ölçülü dikkat ikonu ve uyarı sesi; tehlikeyi uydurma veya abartma.
- Malzeme/nesne: doğru nesneye uygun küçük SVG ve sarı/beyaz etiket; sesli belirme. Adımlar: nesneleri anlatım sırasıyla göster, ölçülü tık sesi.
- Sıcak/soğuk: doğru bağlamda termometre, alev veya kar tanesi. Karıştırma/çalkalama: dönen kaşık veya kap ve uygun iş sesi.
- Temizlik: ölçülü köpük/parıltı; gerçek kanıt olmadan başarı veya kesin sonuç iddia etme. Karşılaştırma: doğru iki seçeneği sırayla göster; kanıtlanmamış artı/eksi hükmü koyma.
- Gerçekten gösterilen sonuç: parıltı ve başarı sesi. Önemli detay: aşağıdaki kontrollerden geçerse doğru nesneye ok/çember. Yorum: konuya uygun soru balonu. Kaydet/paylaş: basılma ve click.
- Hareket: içerikle uyumlu kadraj değişimi, zoom/pan, katman, reveal ve kinetik tipografi. Sayaç, maskot, ilerleme çubuğu veya sürekli süs ekleme. Saat, iş/ışın, başarı, hook ve click seslerini sahneye uygun kullan. V14 sentez efektleri `production/remotion/scripts/make-hook-save-sfx.py`, `make-beam-sfx.py`, `make-result-chime.py` ile yeniden üretilir.

## Zorunlu doğru işaretleme kapısı
1. Her ok/çember için *hedef nesnenin ve hedef noktanın* adını, kaynak görsel dosyasını, sahne başlangıç/bitişini ve normalleştirilmiş koordinatını kaydet. Görseli gerçekten incele; işaretin ucunun doğru nesnenin doğru bölümünde olduğundan emin ol. İsimlendirme, tahmini koordinat veya otomatik tespit tek başına doğrulama değildir.
2. Hedefi sahne görüntüsüyle **aynı koordinat sisteminde** tut. Cover kırpması, object-position, zoom, pan ve varsa rotasyon işaretin konumunu değiştirir. En güvenli yaklaşım görseli ve işaretlemeyi aynı kaynak-boyutlu katmana yerleştirip, cover/crop ve kamera dönüşümünü üst kapsayıcıya birlikte uygulamaktır. `production/remotion/components/VerifiedHighlight.jsx` bu katmana konulabilir; varsayılanı kapalıdır. Bileşen nesneyi tanımaz veya takip etmez.
3. Sahne başlangıcı, ortası ve sonundan, ayrıca geçiş ve hareketin uç noktalarından kareler al; çıktı kadrajında ok ucunun hedefte kaldığını ve altyazı/nesneyi örtmediğini görsel olarak doğrula. Birden fazla görselde veya kesitte koordinatı yeniden değerlendir. Hareketli video, deformasyon veya nesne hareketi varsa gerçek izleme ve doğrulama yap; sadece ortak kamera dönüşümü nesne takibi değildir.
4. Herhangi bir karede güven belirsizse, hedef kadraj dışında/kapanmışsa veya işaret yanlış nesneye kayıyorsa **işareti gösterme**. Gerekirse hedefi işaretlemeyen simge/etiket veya temsili şema kullan. Görsel doğrulama yapılmadıysa `verified` değerini true yapma ve bunu kullanıcıya bildir.
5. Tırnak/ayna örneğinde yapay görsel ve ok ölçüm/kanıt değildir; boşluk çift yönlü aynayı kesin göstermez.
