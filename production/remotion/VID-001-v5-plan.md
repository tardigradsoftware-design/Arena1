# VID-001 V5 — Neo-Brutalist hibrit plan

## 1. Seslendirme ve vurgu haritası

Önceden seçilen `voice-01` ile oluşturulmuş, senaryo değiştirilmeden tek parça üretilmiş VID-001 sesinin 1,45× sürümü kullanıldı. Dosya `production/reference/VID-001/VID-001-fast.wav`; konuşma için yaklaşık 20,65 saniye. Konuşmanın metni `vid001-captions.json` içindeki her girdinin `words[active]` kelimelerinin sırasıyla birleştirilmesidir. Öne çıkan kelimeler: **sakın**, **karbonat**, **bulaşık deterjanı**, **beyaz sirke**, **altmış derecede**, **kaydet**. 44/64 kelime Vosk ile eşleşti; diğer zamanlar interpolasyondur ve kelimeler/yazı zamanları dinleyerek doğrulanmamıştır.

## 2. Sahne matrisi

Zamanlar yaklaşık; SFX'ler kullanılan zaman çizelgesindedir. Görsel üretim aracı Midjourney parametrelerini ayrı alan olarak desteklemez; bunlar kullanılmış gibi gösterilmez. Yeni görsel üretilmedi, daha önce görsel denetiminden geçen arşiv dosyaları kullanıldı; aşağıdaki İngilizce açıklamalar kullanılan kaynakların tarifidir, orijinal üretim parametrelerinin tam dökümü değildir.

| Zaman | Sayaç | Tür | Tasarım / hareket | Görsel veya prompt tarifi | SFX |
|---|---|---|---|---|---|
| 0–6,1 sn | 0/3 | Fotoğraf | Yaylanan siyah konturlu 4:3 pencere, içte yavaş zoom ve SAKIN damgası | `VID-001-a.png`: photorealistic yellowed white pillowcase draped over a laundry basket in a softly lit laundry room | 0 sn whoosh |
| 6,1–11,23 sn | 0/3 → 3/3 | UI | Üç malzeme kartı sözle yaklaşık eşzamanlı kayarak renklenir | Yeni fotoğraf yok | 6,1 / 7,33 / 8,50 / 9,87 sn whoosh |
| 11,23–15,67 sn | 3/3 | Fotoğraf | Makine fotoğrafı 4:3 kartta yakınlaşır; 60° damgası | `VID-001-c.png`: front-loading white washer with closed door and white cotton pillowcases, natural daylight | 11,23 sn whoosh |
| 15,67–20,67 sn | 3/3 | UI | Yaylanarak gelen kaydet kartı, görsel tik | Yeni fotoğraf yok | 15,67 / 18,13 sn whoosh |

Kartlardaki üç sayısı yalnız senaryoda sıralanan malzemeleri sayar. CTA senaryodaki **kaydet** çağrısıdır; uydurma yorum/DM vaadi yok. Küçük çamaşır makinesi maskotu özgün SVG'dir. Noktalı arka plan, çerçeve ve gölgeler kodla çizilir.

## 3. Stil ve kod parametreleri

720×1280, 30 FPS, Remotion, ses 1,45×; #F8F9FA arka plan, #E2E5E9 nokta, #111111 çerçeve/gölge, #E63946 kırmızı vurgu, #10B981 yeşil, #F59E0B sarı, #2563EB mavi. React `spring` ile giriş; fotoğraf içinde yaklaşık 1,01–1,11× zoom; konuşulan kelime kırmızı hap içinde, diğerleri beyaz. Kullanıcı karşılaştırması bekleniyor; seçilmiş kalıcı stil varsayılmamalı.

## Kontrol ve sınırlamalar

İki kullanılan fotoğraf SHA-256 ile önceki manuel inceleme kaydına karşı denetlendi. MP4'ün tamamı teknik olarak decode edildi, 13 örnek kare incelendi; `blackdetect` seçilen eşiklerde siyah aralık bulmadı. Sesin tamamı dinlenemedi; profesyonel kalite veya tam senkron garanti değil. VID-001'deki bulaşık makinesi tableti ve sirke karışımının çamaşır makinesi için uygunluğu doğrulanmamıştır; ürün/makine üreticisi talimatları izlenmelidir.
