# Özgün örnek — Buzdolabın kaç derece?

## Teslim ve amaç

Özgün fikir: sıcaklık bilgisini ilk karede ver, sonra termometre ve çiğ et saklama için ilgili görselleri göster, doğal soruyla bitir. ODS senaryolarından bağımsız bir testtir. Kaynak görüntüler fotoğraf gerçekçiliğinde **yapay olarak üretilmiştir**; gerçek çekim veya ölçüm değildir.

## Sahne ve ses çizelgesi (yaklaşık)

| Süre | Görsel ve metin | Kurgu |
|---|---|---|
| 0–3,5 sn | Buzdolabı; “4°C VE ALTI” | Kanca, yumuşak yakınlaşma ve kadraj kesmesi |
| 3,5–8,6 sn | Raf ve termometre; “ORTA RAFA KOY” | Farklı fotoğraflar, kadraj hareketi ve kayan başlık |
| 8,6–13,4 sn | Ayrı, kapalı çiğ et kutusu | Yakınlaşma/uzaklaşma ve kısa bilgi metni |
| 13,4–16,5 sn | Termometre bulunan buzdolabı; “SENİN DOLABIN KAÇ DERECE?” | Soru ve bitiş |

Seslendirme: `anlatim.mp3`, seçilen Türkçe kadın sesi; FFmpeg `atempo=1.08`. Müzik: bu örnekte `render.py` ile sıfırdan sentezlenen basit özgün melodi ve ritim. Harici müzik veya SFX kaydı kullanılmadı. Sahne görselleri `gorsel-1.png`, `gorsel-3.png`, `gorsel-4.png` yapay üretimdir. Yakın termometre ölçeği tutarsız `gorsel-2.png` reddedildi ve videoya alınmadı. Ufak kadranlar gerçek bir ölçüm olarak sunulmaz.

Animasyon ve kodlama FFmpeg ile yapıldı (`render.py`): zoompan, kadraj değişikliği, kayan metin, kontrast kutular, müzik ve ses miksajı. Derinlik çözümlemesi, gerçek 2.5D, motion tracking veya gerçek video kullanılmadı. Görseller 1080p'ye büyütüldü; eksik detay oluşmaz. Kullanılan font: DejaVu Sans Bold, Bitstream Vera/DejaVu lisansı (`/usr/share/doc/fonts-dejavu-core/copyright`, sistem fontu).

## Teknik kalite kontrol

1080×1920, dikey, 30 fps, H.264/AAC, 48 kHz stereo; 16,5 saniye, yaklaşık 2,6 MB. FFmpeg ile tam decode, blackdetect (0,2 sn) ve silencedetect (−55 dB, 0,5 sn): olay raporlanmadı. Ölçülen ortalama −21,3 dB ve örnek maksimum −7,3 dB; true-peak ölçümü değildir. Saniyelik örnek kareler incelendi; ses baştan sona dinlenmedi, yazı zamanları tahmini, tüm sahnelerde dudak/kelime hizalaması veya fiziksel mobil cihazda kontrol yapılmadı. Kullanılan görseller gerçek cihaz ölçümü ya da güvenlik kanıtı değildir. Yükleme öncesi ses ve altyazı zamanlaması dinlenerek doğrulanmalıdır.

## Başlık ve açıklama

**Başlık:** Buzdolabın Gerçekten Kaç Derece? 🧊

**Açıklama:** Buzdolabı sıcaklığını termometreyle kontrol etmek ve çiğ eti diğer yiyeceklerden ayrı, sızdırmaz kapta tutmak gıda güvenliği için önemlidir. Buzdolabının 4°C veya altında olması önerilir. Soğutma tüm tehlikeleri ortadan kaldırmaz; ürünlerin saklama sürelerine ve cihaz talimatlarına da uyun. Sizin dolabınız kaç derece?

**Hashtag:** #Buzdolabı #GıdaGüvenliği #Mutfakİpuçları #KadıncaYaşam

Kaynaklar: FDA, buzdolabının 4°C veya altında tutulması ve termometre kullanımı https://www.fda.gov/food/buy-store-serve-safe-food/what-you-need-know-about-preventing-listeria-infections ; çiğ etin sızdırmaz kapta diğer yiyeceklerden ayrılması https://www.fda.gov/food/people-risk-foodborne-illness/meat-poultry-seafood-food-safety-moms-be .
