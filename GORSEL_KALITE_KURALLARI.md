# Görsel kalite ve kontrol sistemi

Bu belge `VIDEO_URETIM_KURALLARI.md` ile birlikte kullanılır. Kaynak senaryo ve konuşmaya sadakat önceliklidir; gereksiz insan, el veya yüz üretme. Yüz gerekiyorsa yalnızca bir kısmı kadrajda olsun. Görseller gerçek çekim diye sunulmaz ve kusursuzluk garanti edilmez.

## Üretim öncesi

Her sahne için amaç, TTS zaman aralığı, gerekli nesneler/insan uzuvları, gerçekçi ölçek/temas, kadraj ve ışık tanımlanır. Karmaşık el/nesne ilişkileri yerine açıklayıcı basit kadraj tercih edilir. Prompt sırası: konu → eylem → ortam → nesneler/ölçek → açı → ışık → kompozisyon → fotogerçekçilik → anatomik/fiziksel kısıtlamalar → destekleniyorsa negative prompt. İnsanlara doğal anatomik uzuv sayısı, normal beş parmak ve nesneyle doğal temas; sıvı, ışık, gölge ve perspektife fiziksel tutarlılık şarttır. Plastik doku, bozuk araç gereç, havada duran nesne, kaynağa uymayan malzeme kabul edilmez.

Bu oturumda kullanılan görsel aracı referans/düzenleme için `images` kabul eder. Araç arayüzünde ayrı negative-prompt veya seed alanı **yoktur**; onları varmış gibi kullanma. İlgili olumsuz kısıtlamaları doğal dilde ana prompta ekle. Üretim sonrası bu oturumda görseller `read_file` ile görsel olarak incelenebilir; bu inceleme bir modelin yorumu olup kusursuz görsel garantisi değildir.

## Üretim sonrası / karar

Her görseli **tek tek**, mümkünse yüksek çözünürlükte incele: eller/parmaklar, uzuvlar, yüz, nesne/insan oranları, temas, fizik, sıvı, gölge, perspektif, görüntüdeki yapay ayrıntılar ve TTS/sahne eşleşmesi. Değerlendirici somut notla 0–100 verir: 90–100 kabul adayı; 75–89 düzelt veya tekrar denetle; 0–74 reddet. Kritik anatomi/fizik hatası puandan bağımsız kesin ret; belirsiz bir hata kanıtlanamıyorsa geçirmiş gibi değil, yeniden incele/reddet. Görüntüyü kullanımdan önce incelemek zorunludur; model yorumu hatasızlık garantisi değildir.

Ret halinde hata nedenini ve düzeltilen promptu kaydet, tekrar üret ve yeniden incele. İlk görüntüyü takiben en fazla 3 yeniden üretim; hâlâ uygunsuzsa kompozisyonu basitleştir. Her mesajda 8 görsel üretim sınırına uy. Kullanılan görsel aracı Python betiğiyle çağrılmadığından, `decision()` sadece tekrar üretim kararını verir; **bu sistem kendi başına otomatik görsel üretmez veya otomatik anatomik hata tespit etmez.** Araç üzerinden yeniden üretim ve görsel inceleme insan/ajan tarafından yapılır.

## Kodlu kapı

`production/image_quality.py` SHA-256 ile gözden geçirilmiş gerçek dosyayı bağlar; eksik inceleme, bozuk kayıt, değişen görsel, kritik hata veya 90 altı puanda kapıyı kapatır. Değerlendirici gerçek incelemesini JSON'a kaydeder; bu veri otomatik tespit sonucu değildir. Bir örnek, `review.json` dosyasının bulunduğu dizine göre göreli dosya yoluyla:

```json
{"images":[{"file":"../images/VID-001-1.png","sha256":"GERÇEK_DOSYANIN_SHA256_DEĞERİ","reviewed":true,"score":93,"critical_error":false,"notes":"Nesne, ölçek, fizik ve sahne eşleşmesi tek tek incelendi."}]}
```

Manifestte videoda kullanılan her görsel ayrıca bulunmalı. Boş, şablon veya başkasından devralınmış değerlendirme onay sayılmaz. `sha256sum production/images/VID-001-1.png` hash üretir. FFmpeg betiği `production/render.py` varsayılan olarak `production/quality/VID-NNN.json` manifestini okur ve dört kullanılan dosyayı kontrol etmeden başlamaz. Her yeni üretimin girdileri için yeni manifest oluşturulmalıdır. `production/render_reviewed.py` Remotion'da kullanılan **tüm** gerçek görüntüleri `--image` ile açıkça listeleyerek render komutunu kapıdan geçirir. Kompozisyonu değiştiren kişi bu listenin kompozisyonla tam eşleşmesini kontrol etmelidir; Remotion CLI'nin doğrudan çalıştırılması bu kapıyı atlar, bu yüzden yeni üretimde doğrudan çalıştırma. Bu kapı kontrol eksiklerini teknik olarak azaltır, görüntünün gerçekten doğru olduğunu veya listeye hiçbir şeyin unutulmadığını garanti etmez.

Örnek (kompozisyonun kullandığı her dosya eksiksiz eklenmeli):

```sh
production/.venv/bin/python production/render_reviewed.py \
  --review production/quality/VID-001.json \
  --image production/remotion/public/VID-001-1.png \
  --image production/remotion/public/VID-001-2.png \
  --cwd production/remotion -- npx remotion render entry.jsx COMP out.mp4
```

Burada yalnızca iki örnek dosya gösterilmiştir; gerçek kompozisyon daha çok görsel kullanıyorsa hepsi eklenmelidir. Dosyaların SHA'ları Remotion'ın **gerçek kullandığı kopyalarla** eşleşmelidir. `production/.venv/bin/python -m unittest discover -s production/tests -v` kapı mantığını test eder; test görsellerindeki otomatik anatomi tespiti değildir.

## Gerçek deneme — 2026-11-01

Üretilen 6 test görseli tek tek değerlendirildi: tabak/çatal/bıçak (93, kabul adayı), telefonun yanında el (92, kabul adayı); ilk bardak/elde temas ve yansıma belirsiz (72, ret), ilk telefon kavraması belirsiz (84, ret), yüzsüz okuma sahnesinde eylem ve yazı sorunu (78, ret), bardak tekrarında başparmak görünmüyor (83, yeniden incele/ret). Puanlar sübjektif ajansal görsel değerlendirmelerdir; tüm anatomik doğruluğu garanti etmez. Reddedilen bardak ve telefon sahneleri araçla birer kez yeniden üretildi; bardak tekrarında hâlâ belirsizlik var. Kalite kapısının bu kayıtlar için ret/kabul kararı ve 3 yeniden üretim sonrası basitleştirme yönlendirmesi test edildi; otomatik hata keşfi veya otomatik model çağrısı uygulanmadı. Test görüntüleri video üretiminde kullanılmadı ve Drive'a yüklenmedi.

## Referans temelli sahne tutarlılığı — 2026-11-01 araştırma ve denemesi

Bağımsız promptlarla farklı çamaşır makineleri, renkli çamaşır ve mekân değişiklikleri oluştu. Yeni yöntem: Önce tek bir referans kare seç, onun kamera ve ışık özelliklerini belirle; komşu sahneleri mümkünse aynı referansı `images` girdisiyle düzenleyerek üret. Referansı zorunlu bir garanti değil, görsel ipucu say. Her kareyi tam boy ve sonra komşularıyla yan yana incele; makine tipi, kapak, tezgâh, pencere, ölçek, malzeme ve eylemi karşılaştır. Kontrol paneli, kamera ve nesnelerin temasında değişim varsa düzelt veya reddet. Birbiriyle tutarsız referanslı görselleri sırf referans kullanıldı diye kabul etme. Sonuçlar doğrulanmadıysa video üretme.

Karşılaştırma sayfası yalnızca inceleme yardımcısıdır, kendi başına onay değildir:

```sh
production/.venv/bin/python production/contact_sheet.py \
  production/images/VID-001-1.png production/images/VID-001-consistent-2b.png \
  production/images/VID-001-consistent-3.png production/images/VID-001-consistent-4b.png \
  --output production/images/VID-001-consistency-review.jpg
```

Dört yeni referans düzenleme denemesinde aynı ışık ve çevre daha iyi korundu. İlk açık makine denemesinde ikinci makine belirdi; açık kapak düzeltmesinde tablet/kaşık kapak dudağı üzerinde ve sirke eksik. Son karede kumaş/tezgâh teması belirsiz; bütün kareler arasında makine aynılığı da tam doğrulanmadı. Bunlar **üretime onaylı değildir**. İstenen sahne ile referans koruması bazen çatışabilir; küçük bölgesel düzeltme veya sahneyi sadeleştirme denenmeli.

Araştırılan alternatifler: [FLUX.2](https://github.com/black-forest-labs/flux2) klein 4B Apache-2.0, çoklu referanslı düzenlemeyi destekliyor ve üretici yaklaşık 8 GB VRAM belirtiyor; 9B ve dev için ticari olmayan lisans kısıtı var. [ComfyUI](https://github.com/Comfy-Org/ComfyUI) ve ControlNet gibi akışlar poz/derinlik kompozisyonu yönlendirebilir; model/eklenti lisansları ayrıca incelenmeli ve ellerin doğru olacağı varsayılmamalı. [InstantID](https://github.com/instantX-research/InstantID) kodu Apache olsa da ilgili yüz modelleri ve kendi ağırlıkları yalnız araştırma amaçlıdır; ticari kullanım varsayılmamalı. Bu ortamda GPU görünmüyor ve toplam RAM yaklaşık 3,8 GiB; bu alternatifler indirilip çalıştırılmadı veya karşılaştırılmadı. Harici GPU ortamı olmadan bunları kullanılmış gibi bildirme. Bu oturumun mevcut görsel aracında ayrı seed veya negative prompt alanı yoktur.
