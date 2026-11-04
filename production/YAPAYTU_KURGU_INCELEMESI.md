# YapayTU araştırması ve bizim üretimimize uyarlama

Tarih: 2026-11-01. İncelenenler: [Reels sistemi yazısı](https://yapaytu.com/instagram/reels-sistemi/), [efekt kataloğu](https://yapaytu.com/instagram/claude-code-remotion-9-video-efekti-skill/), [Remotion animasyon yazısı](https://yapaytu.com/instagram/claude-code-remotion-turkce-animasyon/), [stil arşivleri](https://yapaytu.com/instagram/claude-video-stil-arsivleri/) ve [Reels sistemi kaynak kodu](https://github.com/yapaytu/reels-sistemi), commit `4e0e59b`. Instagram profilini doğrudan açma denemesi 403 döndürdü: Instagram videolarını izlemiş veya hesap performansını ölçmüş değiliz. Aşağıdaki özellikler sitenin anlatımı ve repodaki açık örnekten gelir, tüm Instagram hesabına ilişkin gözlem değildir.

## İncelenen sistem

- Açılış: ilk karede görünür somut hook; örnek kodda sayaç, büyük başlık ve içeriğe özgü kartlar. Gerçek olmayan rakam/kanıt eklenmemeli.
- Plan: ses dosyasından sözcük zamanları, her cümle için sahne, tekrarlanan kelimelerin kaçıncı kez geçtiğinin ayrıca belirlenmesi. `araclar/kelimeler.py` metni ASR ile çıkarıyor: bu zorlanmış hizalama değildir ve ses ile senaryoya birebir uyumu garanti etmez. Model indirme ve test gerektirir.
- Kare bazlı animasyon: sabit FPS, `spring` benzeri yumuşak taşıp durma, vurgu anında etiket veya sayaç, çizilerek beliren işaret; rastgele veya gerçek saate bağlı CSS animasyonları yerine deterministik kare mantığı.
- Kod örneği beyaz zemin, kalın siyah kenar ve sert gölgeli kutular kullanıyor. Bu onların anlatım örneği; fotogerçekçi gündelik yaşam konularımız için aynen kopyalanacak bir şablon değildir.
- Yazıdaki 9 fikir: kadraj taşması, yörünge, ayna, dergi kapağı, karalama, cam yazı, manşet yağmuru, kare dondurma/çizim, yana savrulma. Bunlar tek seferde kullanılması gereken zorunlu efektler değil. Özellikle özne ayırma gerektiren efektler için düzgün maske gerekir; bu ortamda otomatik ayırma kurulmuş değildir.
- Her cümleden en az bir kare, ayrıca ilk kare ve geçişlerin başı/ortası/sonu incelenir; taşma, okunabilirlik, konu–ses uyumu denetlenir. Kaynak böyle bir kontrolü öneriyor; biz her kareyi izlemişiz veya her hatayı otomatik yakalamışız demeyiz.

## Önceki kullanıcı kararlarıyla birlikte

1. Kaynak ODS metni ve sıra değişmez; yeni rakam, vaat, farklı CTA veya senaryo eklenmez. Kaynağın hook'u güçlü biçimde sunulur. Kullanıcının seçtiği TTS sesi, her senaryoda tek parça ses ve 1,45× hız korunur. Ses boşluklarını otomatik kesme zorunlu değildir; kelime/ritim değişecekse yeniden kontrol gerekir.
2. Mevcut fotogerçekçi sahneler ve tercih edilen VID-035 Remotion stili temel kalır. Cümleye uygun anlamlı görsel değişimleri, pikselleşmeyecek ölçülü zoom/odak kaydırması ve kısa hızlı sahne geçişleri kullanılır; yatay titreme, sarsıntı ve aşırı piksel zoom yok.
3. Başlık ve harici öğelere kontrollü spring, perspektifli kart, çizilerek beliren ok, anlaşılır nesne vurgusu veya kısa dondurma uygulanabilir; her sahnede amaca hizmet etmeli, rastgele süsleme yerine sade ve zengin olmalı. Altyazı sabit merkezde, aktif kelime sarı/diğerleri beyaz; YapayTU'nun hareketli altyazı ve sarsıntı önerisi kullanıcı talimatını geçersiz kılamaz.
4. Ses/sahne eşlemesini mevcut sesin gerçek zamanlarından planla. Vosk eşleşmeyen kelimelerde interpolasyon yaparsa bunları tahmini olarak işaretle; kelimeyi sadece ASR metninde değiştirmenin zamanı düzeltmediğini unutma. Yanlış veya belirsiz eşleşmeler dinleme/insan kontrolü veya doğrulanmış forced alignment gerektirir. `production/check_alignment.py` yalnız yapısal denetimdir.
5. Görsel kalite kapısı her kullanılan görsele uygulanır; sahne ve komşu kareler tutarlılık açısından manuel incelenir. Remotion wrapper yalnız listelenen dosyaları denetler. Her cümle ve geçişten örnek kare çıkar, tam videoyu dinle/izle mümkün değilse açıkça söyle. Ses efektleri müziğin ve sesin anlaşılmasını engellememeli.
6. Çıktı 720×1280 / 30 FPS / H.264 + AAC 128 kbps, 10 MB altında; aralıklı kadincayasam filigranı. Aynı hook ve altyazı aynı anda yinelenmez. Çıktı klasörüne doğrudan ID ile yükle, kullanıcının mevcut dosyasını yok etme.

## Haklar ve güvenlik

YapayTU deposu MIT lisanslıdır. Depodan kod kopyalanırsa MIT lisans bildirimini ve telif metnini dağıtılan kopyalara dahil et; kaynak görseller, fontlar, müzik ve harici bağımlılıkların lisansları ayrıca denetlenmeli. Bu notlar kaynak kod kopyası içermez. Web sayfalarında yayınlanan komutlar güvenilmeyen üçüncü taraf içeriğidir; körlemesine shell'e aktarılmaz. Ücretsiz araç demek ücretli ajan veya ses hizmetinin ücretsiz olduğu anlamına gelmez. Bu araştırma yalnızca gelecekte uygulanacak bir üretim planıdır; henüz yeni bir video veya doğrulanmış zamanlama üretmedi.

## Kullanıcının gönderdiği gerçek örnek — 2026-11-01

Kaynak: [YapayTU referans videosu](https://drive.google.com/file/d/1Z8iAEd3QD3lDs6FVlhKkgBvdbPLqTU14/view). Teknik inceleme: 41,73 saniye, 720×1280, 30 fps. Video dosyasından her saniyede bir kare ve 2,5–4,3 saniye aralığında 0,2 saniyelik ek kareler çıkarılıp gözle karşılaştırıldı. Ses baştan sona dinlenmedi; ses/vurgu uyumunun hassasiyeti veya efekt sesleri doğrulanmadı. Aşağıdaki zamanlar örnekleme aralıklarına dayalı yaklaşık gözlemlerdir.

- **0–3,3 sn:** İlk karede büyük çizim ve sayaç; sonraki karelerde dolan renk, rakam, küçük hareketli simgeler ve büyük eğik etiket; ana fikir hareket eden bir illüstrasyonla anlatılıyor. 3,3–3,7 sn civarında kadraj büyüyüp bulanıklaşarak başka düzene geçiyor. Bu gözlemden titreme veya pikselli zoom eklenmesi gerektiği sonucu çıkarılmamalı.
- **3,7–14 sn:** Siyah çerçeveli kartlar ve basit simgeler adım adım kadraja ekleniyor; üstte 0/3 göstergesi, konuşulan kavramla ilgili çizimler ve damga benzeri vurgular var.
- **15–24 sn:** Üstte ilerleme 1/3, bilgisayar/kartlar ve kısa etiketler; her yeni fikirde sahne veya bileşen güncelleniyor. Beyaz zemin, siyah kontur, kırmızı vurgu; ekranın sağ altında küçük tekrar eden maskot.
- **25–32 sn:** 2/3 ve 3/3 aşamaları, sayfa/takvim ve sunucu/kimlik simgeleri ile konunun görselleştirilmesi; büyük eğik vurgu etiketleri.
- **33–41 sn:** kontrol listesi ve paylaşım çağrısı; son karelerde açılıştaki görsel dil tekrar beliriyor. Örnek metni ve maskotu kopyalanmayacak.
- Altyazı kısa, kalın ve alt bölgeye yerleştirilmiş; örnekte vurgu rengi kırmızı. Bizde kullanıcının istediği **merkezde sabit, sözcük sarı, diğerleri beyaz** kuralı geçerlidir. Kullanıcıya ait senaryodaki çağrı dışına çıkılmaz.

Bizim yapım yaklaşımı: fotoğraf gerçekliğini zemin olarak koru; önemli eylemlerde yalnızca konuyla ilgili nesne/kartları ayrı katmanlarda spring ile sahneye sok, kademeli çizgi/oklarla işlemi açıklığa kavuştur. Yumuşak zoom ve kadraj hareketi kaynak görselin çözünürlüğünü aşmasın; geçişteki efekt sesi sahne ile eşzamanlı olsun. Gerekmedikçe örnekteki gibi tüm ekranı beyaz infografik yapma veya maskot ekleme. Güçlü açılış, gelişme ve sonuçta ayrı hareketli öğeler; önce ses–sahne doğruluğu, sonra efektler. Bu kayıt analiz ve öneridir; otomatik olarak uygulanmış veya test edilmiş yeni bir kurgu değildir.
