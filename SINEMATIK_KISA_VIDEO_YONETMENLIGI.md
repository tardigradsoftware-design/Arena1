# Sinematik kısa video yönetmenliği — güncel talimat

Bu belge 3 Kasım 2026 kullanıcı talimatıdır. Önceki teknik/stil belgeleriyle çelişen noktalarda bu belge önceliklidir. Mevcut videolar değiştirilmez. Ayrı test klasörü: https://drive.google.com/drive/folders/1XQCWe2fIbBB6TyOiOCs3ck3ECRnOQXtZ .

## Amaç ve içerik

- Fotoğraf, görsel, metin, animasyon ve sesi Remotion/FFmpeg ile sahneye özgü yaşayan sinematik anlatıya dönüştür. İlk 1–2 saniyede konuya bağlı çarpıcı, dürüst kanca ve erken bilgi ödülü; gereksiz gecikme ve tekrar yok. Mobil izlenebilirlik, yorum ve paylaşım potansiyelini hedefle; viral performans garantisi verme.
- Her senaryo için özgün sahne sırası, süre, kamera, palet, müzik, efekt ve animasyon planı yap. Her karede gereksiz hareket veya aynı hareketi tekrarlama. Anlatım–görüntü uyumu, görsel gerçekçilik ve mevcut video üretim kurallarındaki kullanıcı tercihleri korunur.
- Clickbait, yanıltıcı bilgi, sahte iddia ve doğrulanmamış sonuçları olgu gibi kullanma. Kaynak senaryoda bunlar varsa sessizce değiştirme, kısa ve net bildir; gerekli hallerde düzeltilmiş metin üzerinde anlaşmadan yayıma hazır bir son ürün gibi sunma. Önceden verilen VID-004 ve VID-013 değişiklik izinleri diğer senaryoları kapsamaz.
- Kapanışta kullanıcı isteği kapsamında uygun beğeni, takip, paylaşım ve doğal yorum daveti eklenebilir; senaryoya ait ana bilgi ile yeni CTA'yı ayrı tut. İzleyiciye uygulanması riskli tavsiyeyi sadece açıklamada uyararak güvenli hale getirmiş sayma.

## Sahne ve grafik dili

- Tam ekran gerçekçi görsel, anlamlı Ken Burns hareketleri, sahneye özel kaydırma/zoom, odak, ışık ve renk. Pikselli büyütme ve rahatsız edici yatay titreme yok; gerekiyorsa uygun sahnede kontrollü kamera sarsıntısı. Gözün takip edebileceği bir tempo ve güvenli yazı alanları kullan.
- Mask/reveal, kinetik tipografi, sarı aktif kelimeli kısa altyazılar, küçük konuya uygun SVG'ler, işaretler ve katmanlı hareketlerle önemli bilgileri destekle. Aynı metni aynı anda hook ve altyazı olarak yineleme. Sayaç, maskot, bölüm başlığı ve ilerleme çubuğu varsayılan değil.
- 2.5D parallax veya gerçek motion tracking yalnızca sahne katmanları/izleme gerçekten hazırlanıp incelendiğinde uygulanır. Düz fotoğraf ve grafik katmanlarını gerçek derinlik çözümlemesi veya izleme diye sunma. Motion blur ve 3D hissi gibi özellikler uygulanıp test edilmeden raporda var sayılmaz.
- Uygunsa ilk ve son sahne bağlanabilir; takip/yorum CTA veya kaynak metni buna uymuyorsa sahte bir kusursuz döngü iddiasında bulunma.

## Ses ve teknik

- İstanbul Türkçesi kadın ses tercihi, tek parça ana anlatım, 1,45×, mevcut tercihli ses yeniden kullanılabiliyorsa yeniden seçtirmeme; ayrı ses veya CTA kullanılırsa açıkça belirt. Kullanıcının görsel veya ses araçlarında mesaj başına 8 sınırına uy.
- Anlatım ön planda, müzik ve efektler altında; ani ses sıçramalarını önle, başlangıç/sonu düzenle. İzinli/lisansı doğrulanmış kaynakları listele. Önceki geçiş sesi yasağının yerine yeni açık talimat geçer: gerektiğinde geçişlerde uygun ve ölçülü whoosh/impact/riser/click/pop/ambient kullanılabilir. Her geçişe otomatik ses koyma; anlatımı örtme. Saat anlamlıysa animasyonlu analog saat ve tik tak tercihi devam eder.
- Varsayılan 1080×1920, 9:16, 30 fps; içeriğe uygun olduğunda 60 fps. H.264 MP4/AAC; kaliteli bitrate. Önceki en fazla 10 MB tercihini mümkün olduğunda koru; süre/kalite ile bağdaşmıyorsa sonucu ve boyutu bildir, kaliteyi gizlice bozma. Orijinal görseller 1080 genişlikten küçükse yukarı örneklemenin gerçek yeni ayrıntı yaratmadığını belirt.
- Remotion sahne ve motion graphics içindir; FFmpeg renk/ses işleme, uygun final kodlama ve ölçüm için kullanılır. Aynı işi gereksiz yere tekrarlama. Ortamdaki gerçek paket ve yetenekleri kontrol et.

## Kalite ve teslim

- Çıktıyı baştan sona görüntü ve ses olarak kontrol etmeyi hedefle; yapılamıyorsa bunu açıkça bildir. Teknik tam decode, blackdetect, ses tepe/sessizlik analizi, kare/temas sayfası, yazı/güvenli alan, altyazı ve sahne senkronu ayrı konulardır; otomatik kontroller manuel görme/dinleme veya kalite onayı değildir. Sorun bulunan sahneleri düzelt ve tekrar kontrol et.
- Her üretim tesliminde final MP4, görsel/ses/lisans listesi, sahne zaman çizelgesi, animasyon/efektler, dürüst teknik kalite kontrolü, video başlığı, açıklama ve hashtag önerileri sağla. Bilinmeyen lisansı uygun kabul etme. Doküman ve çalışma betiklerini izinli oturum dalına kaydet/push et; büyük geçici renderları gereksiz yere Git'e alma.
- VID-001 özgün anlatımındaki bulaşık tableti + sirke/karbonat kombinasyonunun cihaz uygunluğu ve kesin temizlik sonucu doğrulanmamıştır. Tek parça özgün anlatımı aynen kullanmak, yeni yanıltıcı içerik yasağıyla çatışabilir; önce bu uyuşmazlığı açıkça belirt. Önceki CTA'lı test güvenliğe ilişkin düzeltme değildir.
