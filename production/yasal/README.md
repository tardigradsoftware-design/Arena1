# Yasal seri (yasal.csv.ods) — video + Notion rehber hattı

Kaynak tablo: Drive `yasal.csv.ods` (ID `1zv6_IBQZRpc9TvrPjw8m6zAg2th1cf4Z`, klasör `1oI9Ek0aUxHfdIlxqPCD9wwCovYwiF9xC`). Her satır tek hücrede CSV metnidir; `rows.json` ayrıştırılmış kopyadır ve durum/linkler burada tutulur. Bağlayıcı ODS'i yerinde düzenleyemediği için güncel tablo aynı klasöre `yasal_takip` adlı Google E-Tablosu olarak yüklenir (`yasal_takip.csv`'den).

Kurallar (kullanıcı görevi): 1080×1920, ses `voice-00` (bu oturumda seçildi) 1,15× + sessizlik kısaltma, ilk 3 sn `Ekran_Yazisi` hook + whoosh/pop, 3–4 sn'de bir sahne/zoom, sarı/beyaz Montserrat karaoke altyazı, son 3 sn "Yoruma [CTA] yaz, rehberi gönderelim!". ManyChat/DM otomasyonu YAPILMAZ.

Üretim: `audio/<ID>_raw.wav` (TTS) ve `img/<ID>_{a,b,c}.png` (yapay görseller, yüz tam gösterilmez, okunur yazı yok) hazırlanır, sonra:

    production/.venv/bin/python production/yasal/render_yasal.py 4 5 6

Kurulum: `python3 -m venv production/.venv && production/.venv/bin/pip install imageio-ffmpeg numpy Pillow vosk`; Vosk modeli `production/README.md`'deki depodan `production/vosk-tr`'ye. Font: Montserrat (OFL, `fonts/OFL.txt`).

Sınırlar: kelime zamanları Vosk çapası + interpolasyon (zorlanmış hizalama değil); ses dinlenerek doğrulanmadı. Notion sayfaları `Adım Adım Uygulama Rehberleri` üst sayfasının altındadır; API ile "Web'de yayınla" yapılamaz, kullanıcı üst sayfayı bir kez yayımlamalıdır. Rehber içerikleri genel bilgilendirmedir.

Durum: 1–3 Hazır (2026-11-11). Sırada 4.
