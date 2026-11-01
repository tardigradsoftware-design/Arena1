# VID-035 Remotion kompozisyonu

Ses, görseller ve altyazı zamanları VID-035'e özeldir. Kaynak görseller ve sesler özel üretim dosyaları olduğundan Git'e eklenmemiştir. `public/` altında `VID-035-1.png` ... `VID-035-4.png`, `voice.wav` (1,45× hızlandırılmış tek parça ses), `peaceful_days.mp3`, `whoosh.wav`, `drip.wav` gerekir. Telifsiz seslerin kaynakları `../assets/CREDITS.md` içindedir.

```sh
cd production/remotion
npm ci
mkdir -p public
cp ../images/VID-035-[1234].png public/
cp ../audio/VID-035-fast.wav public/voice.wav
cp ../assets/{peaceful_days.mp3,whoosh.wav,drip.wav} public/
AWS_LAMBDA_JS_RUNTIME=nodejs22.x node -e "require('@sparticuz/chromium').default.executablePath().then(console.log)"
LD_LIBRARY_PATH=/tmp/al2023/lib npx remotion render index.jsx VID035 ../videos/VID-035-remotion.mp4 --browser-executable=/tmp/chromium --gl=angle --disable-web-security --concurrency=2 --codec=h264 --crf=24
```

Chromium'un paket içi Linux kütüphanelerine ihtiyacı bu ortamda test edilmiştir; işletim sistemine göre komut değişebilir. `npm audit` 4.0.539 Remotion araç zincirinin sabitlenmiş zod 4.5.4 bağımlılığında yüksek önem dereceli bellek tüketimi açığı bildirdi; bu araçları güvenilmeyen girdi veya internete açık servis ile kullanmayın, güncellemeler ve lisanslar doğrulanmalıdır. Remotion'un kendi kullanım lisansını ticari kullanımınıza göre ayrıca kontrol edin: https://www.remotion.dev/license .

Altyazı zamanları Vosk ile yaklaşık hizalanmıştır; kelime eşleşmeleri dinlenerek denetlenmelidir. Kalem işaretlerinin konumu yalnızca bu sürümdeki görseller içindir. Animasyonlar frame tabanlıdır; diğer videolara uyarlamadan önce kaynak senaryoyu, sahne zamanlarını ve görselleri gözden geçirin. Hook, senaryodan seçilmiş kelimeleri kullanır; anlatım metni değiştirilmemiştir.

Tasarım referansları: https://www.remotion.dev/docs/transitioning ve https://ads.tiktok.com/business/creativecenter/quicktok/online/tiktok_creative_accelerator/pc/en .
