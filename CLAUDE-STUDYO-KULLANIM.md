# Claude Stüdyo — kurulum ve kullanım notu

Kaynak: https://github.com/yapaytu/claude-studyo, incelenen commit `ed69cc99cb7e1c6c08f5b639a0fccba44effdf8e`; MIT lisansı `CLAUDE-STUDYO-LICENSE`. Projenin 7 skill tanımı `.claude/skills/`, örnekleri `ornekler/`, araçları `araclar/`, orijinal sözleşmesi `STUDYO.md`, upstream README `CLAUDE-STUDYO-README.md`. Bu dosyalar talimat ve örnektir; Arena'da Claude Code'un otomatik skill çağırdığı iddia edilmez. Burada ajan onları okuyup teknikleri elle uyguladı. Claude Code kullanan bir kullanıcı proje kökünde becerileri Türkçe isteyebilir; Claude Code/abonelik ayrıca gerekir.

| Skill | Ne zaman | Uyarı |
|---|---|---|
| `kil-animasyon` | Hamur/stop-motion ürünü | Titreme/plastik görünüm kullanıcı tercihine aykırıysa kullanma. |
| `3d-animasyon` | Three.js ile 3D nesne | Oyuncak estetiği fotogerçekçi değildir; referans görsellerin yerini kendiliğinden almaz. |
| `reklam-filmi` | Sinematik ürün tanıtımı | Letterbox/kamera etiketleri dikey ve kullanıcı isteğine göre seçilmeli. |
| `belgesel` | Yavaş bilgi/belgesel anlatısı | Bölüm başlığı/sayılar kullanıcının isteğine ters veya senaryoda yoksa eklenmez. |
| `motion-grafik` | Kinetik yazı, çizilen işaretler | VID-001 Stüdyo karşılaştırmasında uyarlanmıştır, kullanıcı V14 stilini tercih etti. |
| `cizgi-film` | Çizgi karakterli sahneler | Çocuk estetiği ve maskot varsayılan değil. |
| `konusan-maskot` | Ses genliğine bağlı ağız | RMS ağız hareketi fonem/dudak senkronu değildir; maskot kullanıcının mevcut genel tercihinde yok. |

## Nasıl işler ve kurulum

Tek HTML `window.FPS`, `window.SURE` ve sadece kare numarasına bağlı `window.ciz(f)` sağlar. `STUDYO.md` ayrıntıları, 7 örnek ise temel kodları içerir. Aracın `kayit=1` modunda Playwright her kareyi çizer, sahne görüntüsünü FFmpeg'e aktarır; `--ses dosya.wav` eklersen AAC ses de ekler. `node araclar/kaydet.mjs ornekler/motion.html` bir örnek render komutudur.

Node 18+, FFmpeg ve Playwright Chromium gereklidir: `npm ci`, sonra sistemine uygun `npx playwright install chromium`. Güvenlik nedeniyle upstream 1.48.2 yerine Playwright 1.64.1 kilitlendi (eski sürümde GHSA-7mvr-c777-76hp); 3D için `three@0.160.0` npm üzerinden kuruldu ve 3D örneği bu yerel kopyayı kullanır. Örnekler Google Fonts'a başvurur: bu ortamda erişilemediğinde sistem fontları kullanılır; Google fontlarını kuruluymuş gibi varsayma. Aracımız yerel test için Chromium ve FFmpeg yollarını ortam değişkeniyle seçebilir; `--allow-file-access-from-files` sadece güvendiğiniz yerel HTML için kullanılmalı. Upstream 3D skill metnindeki CDN URL'si yerine yerel `three` kullanılması bu ortamda gerekir.

Bu ortamda yedi örneğin her biri Chromium ile açıldı, `ciz(42)` çağrıldı ve JS sayfa hatası görülmedi; bu 7 tam MP4 renderı, ses kalitesi veya tüm karelerin kontrolü değildir. `motion-grafik` uygulaması olarak VID-001'in tamamı ayrıca gerçek Stüdyo kayıt aracından MP4 alındı ve decode edildi.

## VID-001 karşılaştırması

`ciktilar/VID-001-studyo.html` özgün uyarlama, V14 senaryosu/sesi ve önceki dört incelenmiş görseli kullanır; tam ekran fotoğraf ve kullanıcı tercihleri korunarak skill'in kare tabanlı, kademeli kinetik tipografi ve çizgi tekniği uygulanmıştır. `production/vid001-studyo-review.json` dört referans fotoğraf için önceki manuel SHA inceleme kaydıdır. V14 MP4'ünün sesi WAV'a açılıp Stüdyo kaydıyla tekrar AAC kodlanmıştır; yeni seslendirme yoktur. Kelime süreleri kısmen tahmini, video baştan sona dinlenmemiştir. Kullanıcı V14 stilini seçti; Stüdyo karşılaştırma videosu Drive çöpüne taşındı, araçlar ve kaynak kodu korundu.

Kayıt örneği (bu sandbox'ta FFmpeg ve Chromium yollarını kontrol et; önce V14 ses miks WAV'ını hazırla):

```sh
npm ci
# FFMPEG_PATH, STUDYO_CHROMIUM ve LD_LIBRARY_PATH ortamınıza uygun olmalı.
"$FFMPEG_PATH" -i production/videos/VID-001-v14.mp4 -vn -c:a pcm_s16le production/audio/VID-001-v14-mix.wav
STUDYO_WIDTH=720 STUDYO_HEIGHT=1280 STUDYO_CRF=23 node araclar/kaydet.mjs ciktilar/VID-001-studyo.html production/videos/VID-001-studyo.mp4 --ses production/audio/VID-001-v14-mix.wav
```

Yeni bir konuya doğrudan VID-001 zamanlarını/metnini kopyalama; önce senaryo, ses, özel sahne planı ve SHA'lı görsel incelemesi yap. İlgili kullanıcı kuralları `VIDEO_URETIM_KURALLARI.md` ve `DEVIR_DOSYASI.md` önceliklidir.
