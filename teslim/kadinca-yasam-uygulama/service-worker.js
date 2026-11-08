// Cache only this application's files. Do not delete any other app's caches.
const CACHE = 'kadinca-panel-aeff9c42bf46';
const ASSETS = ["./", "./index.html", "./manifest.webmanifest", "./icon-192.png", "./icon-512.png", "./icon-maskable-512.png"];
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
