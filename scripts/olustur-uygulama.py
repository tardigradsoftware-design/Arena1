#!/usr/bin/env python3
"""Package the existing single-file panel as a relative-path, offline-capable PWA."""
from pathlib import Path
import hashlib, json, shutil
from PIL import Image, ImageDraw, ImageFont
root=Path(__file__).resolve().parents[1]
out=root/'teslim/kadinca-yasam-uygulama';out.mkdir(parents=True,exist_ok=True)
html=(root/'teslim/kadinca-yasam-icerik-paneli.html').read_text(encoding='utf-8')
html=html.replace('</title>', '''</title><meta name="theme-color" content="#436f60"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-title" content="Kadınca Yaşam"><link rel="manifest" href="./manifest.webmanifest"><link rel="apple-touch-icon" href="./icon-192.png">''',1)
html=html.replace('<nav class="nav" aria-label="Sayfalar">','<button id="install-app" class="btn small hidden" type="button">Uygulamayı yükle</button><nav class="nav" aria-label="Sayfalar">',1)
html=html.replace('</body></html>', '''<script>
// Local files and insecure origins cannot register service workers.
if ('serviceWorker' in navigator && window.isSecureContext) {
  window.addEventListener('load', () => navigator.serviceWorker.register('./service-worker.js').catch(() => {}));
}
let installPrompt;
window.addEventListener('beforeinstallprompt', e => { e.preventDefault(); installPrompt=e; document.querySelector('#install-app').classList.remove('hidden'); });
document.querySelector('#install-app').addEventListener('click', async () => {
  if (!installPrompt) return;
  const prompt=installPrompt; installPrompt=null; document.querySelector('#install-app').classList.add('hidden');
  await prompt.prompt();
});
window.addEventListener('appinstalled', () => { installPrompt=null; document.querySelector('#install-app').classList.add('hidden'); });
</script></body></html>''',1)
(out/'index.html').write_text(html,encoding='utf-8')
manifest={'id':'./','name':'Kadınca Yaşam İçerik Paneli','short_name':'Kadınca Yaşam','description':'280 içerik için çevrimdışı çalışabilen kişisel içerik paneli.','lang':'tr','start_url':'./','scope':'./','display':'standalone','background_color':'#f7f9f6','theme_color':'#436f60','icons':[{'src':'./icon-192.png','sizes':'192x192','type':'image/png','purpose':'any'},{'src':'./icon-512.png','sizes':'512x512','type':'image/png','purpose':'any'},{'src':'./icon-maskable-512.png','sizes':'512x512','type':'image/png','purpose':'maskable'}]}
(out/'manifest.webmanifest').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Simple placeholder monogram, not a final brand logo.
for size,maskable in [(192,False),(512,False),(512,True)]:
 im=Image.new('RGB',(size,size),'#436f60');draw=ImageDraw.Draw(im); inset=size*.13 if maskable else size*.075
 draw.rounded_rectangle((inset,inset,size-inset,size-inset),radius=size*.20,fill='#e5f0e8')
 font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf',int(size*(.44 if maskable else .50)))
 draw.text((size/2,size/2-0.01*size),'K',font=font,fill='#315848',anchor='mm')
 im.save(out/(f'icon-maskable-{size}.png' if maskable else f'icon-{size}.png'))
assets=['./','./index.html','./manifest.webmanifest','./icon-192.png','./icon-512.png','./icon-maskable-512.png']
digest=hashlib.sha256((html+json.dumps(manifest)).encode()).hexdigest()[:12]
sw='''// Cache only this application's files. Do not delete any other app's caches.
const CACHE = 'kadinca-panel-__VERSION__';
const ASSETS = __ASSETS__;
self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE).then(cache => cache.addAll(ASSETS)));
});
self.addEventListener('activate', event => {
  event.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k.startsWith('kadinca-panel-') && k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', event => {
  const req = event.request, url = new URL(req.url);
  if (req.method !== 'GET' || url.origin !== self.location.origin || !url.href.startsWith(self.registration.scope)) return;
  if (req.mode === 'navigate') {
    event.respondWith(fetch(req).then(response => { if (response.ok) {const copy=response.clone(); caches.open(CACHE).then(c=>c.put('./index.html',copy));} return response; }).catch(() => caches.match('./index.html')));
  } else {
    event.respondWith(caches.match(req).then(hit => hit || fetch(req)));
  }
});
'''.replace('__VERSION__',digest).replace('__ASSETS__',json.dumps(assets))
(out/'service-worker.js').write_text(sw,encoding='utf-8')
(out/'KURULUM.txt').write_text('''KADINCA YAŞAM İÇERİK PANELİ — KURULUM

1. Dosyaları aynı klasörde tutun. Önce eski panelde Ayarlar > Yedeği indir ile JSON yedeği alın.
2. Bilgisayar: Bu klasörde terminal açın ve python3 -m http.server 8000 komutunu çalıştırın (Windows: py -m http.server 8000). Chrome veya Edge ile http://localhost:8000/ adresini açın. Adres çubuğundaki uygulama yükleme simgesini veya uygulamada beliren “Uygulamayı yükle” düğmesini kullanın. Terminali kapatırsanız ilk açılış için sunucuyu tekrar çalıştırmanız gerekebilir; ilk başarılı kurulum ve önbelleğe almanın ardından çevrimdışı açılabilir.
3. Telefon: Bu klasörü HTTPS sunan bir statik siteye yayınlayın ve HTTPS adresini telefonda açın. Android Chrome: menü > Uygulamayı yükle / Ana ekrana ekle. iPhone Safari: Paylaş > Ana Ekrana Ekle. Seçenek ve davranışlar tarayıcıya ve sisteme göre değişebilir. Google Drive dosya önizlemesi bir HTTPS uygulama sunucusu değildir; bu paket Drive üzerinden doğrudan kurulmaz.
4. Yeni uygulamada Ayarlar > Yedeği yükle ile eski JSON yedeğinizi içeri alın. file://, localhost ve farklı HTTPS adresleri farklı depolama alanları kullanır; kayıtlar otomatik taşınmayabilir.

Kurulumdan sonra en az bir kez çevrimiçi açılışı tamamlayın. Kayıtlar cihaz ve tarayıcıya özeldir; silinen site verileri, özel tarama ve cihaz değişikliği kayıtları etkileyebilir. Düzenli olarak Ayarlar > Yedeği indir yapın. Görünen K uygulama simgesi geçici bir monogramdır.
''',encoding='utf-8')
print(f'PWA hazır: {out} ({digest})')
