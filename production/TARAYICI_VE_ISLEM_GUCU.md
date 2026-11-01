# Tarayıcı ve işlem gücü araştırması — 2026-11-01

## Gerçek tarayıcı

`production/remotion` içine açık kaynak Playwright Core eklendi; mevcut `@sparticuz/chromium` gerçek Chromium başsız çalıştırıldı. Yerel JavaScript sayfasında butona tıklama ve metin değişimi başarıyla test edildi. Bu bir tarayıcı otomasyonudur; kullanıcı oturumlarına erişim, her web sitesine erişim veya grafik masaüstü değildir. Sistem dış ağını yalnızca izinli alan adlarına sınırlar; tarayıcı bunu aşamaz. Şifre ve çerez saklama.

Kurulum (`node_modules` ve `/tmp` kalıcı sayılmaz):

```sh
cd production/remotion
npm ci
AWS_LAMBDA_JS_RUNTIME=nodejs22.x node -e "require('@sparticuz/chromium').default.executablePath().then(console.log)"
LD_LIBRARY_PATH=/tmp/al2023/lib node scripts/browser-smoke.cjs
```

Ağ deneyi için `--network` kullanılır. Bu ortamda GitHub sayfası varsayılan sertifika doğrulaması ile `ERR_CERT_AUTHORITY_INVALID` verdi. Yalnız teşhis amaçlı, geçici bir izole tarayıcı bağlamında TLS doğrulaması kapatıldığında GitHub 200 döndü. Güvenli genel çözüm değildir; şifre/hesap/özel veriyle bu şekilde kullanılmamalı. Güvenilir CA yapılandırılana dek güvenli uzak tarayıcı erişimi doğrulanmış sayılmaz. Mevcut npm bağımlılık zincirinde 10 yüksek güvenlik uyarısı vardır; tarayıcı altyapısını açık internete sunma.

## CPU ve GPU

Bu ortamda CPU zaten mevcut; yazılım eklemek fiziksel CPU veya GPU sağlamaz. RAM toplamı 3,8 GiB, GPU görünmüyor. [FastSD CPU](https://github.com/rupeshs/fastsdcpu) açık kaynak bir CPU görsel çalıştırıcısıdır; LCM için en az 2 GB, FLUX.2 OpenVINO için 8 GB RAM listeliyor. [stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp) CPU çalıştırmayı ve çeşitli modelleri destekler; ağırlık ve RAM ihtiyaçları modele göre değişir. Hiçbirinin kaliteli model ağırlıkları bu ortamda indirilmedi veya çalıştırılmadı; model barındırma adresleri mevcut dış ağ izinleri dışında olabilir. Kurulmuş ya da görsel üretmiş gibi sunma. CPU üzerinde daha eski küçük modellerin profesyonel görsel kalitesini sağlayacağı garanti değildir.

[Google Colab](https://research.google.com/colaboratory/faq.html) ücretsiz katmanda kimi zaman GPU sağlayabilir; kota, kullanılabilirlik ve oturum süresi değişir, GPU garantisi yoktur. Bu servis açık kaynak bir GPU değildir; uzaktaki bir hizmettir. Buradan Colab'a bağlantı/açık kullanıcı oturumu yok, donanım edinilmedi. Kullanıcının kendi hesabıyla hizmette GPU açması ve ilgili hizmet/model lisanslarını kabul etmesi gerekir; kimlik bilgisi isteme, ağ kısıtlarını aşmaya çalışma. Ayrı bir GPU ortamında test etmeden performans, maliyet veya kalite vaat etme.

## GitHub Actions CPU denemesi

Açık kaynak projede `cpu-image-test.yml` yalnızca bu oturum dalında workflow dosyası değiştiğinde veya elle çalışır. GitHub'ın standart açık depo Linux runner'ı dokümana göre 4 vCPU ve 16 GB RAM sunar, GPU sunmaz: https://docs.github.com/en/actions/reference/runners/github-hosted-runners . Ücretsiz standart runner bilgisi ve kotalar GitHub tarafından değiştirilebilir; yalnızca makul, projeyle ilgili işler çalıştır. İş, stable-diffusion.cpp CPU sürümünü derlemeyi, SD 1.5 modelini indirmeyi ve tek bir 512×512 deneme görseli üretmeyi dener; çıktı yalnızca kısa süreli GitHub Actions artifact'ıdır, video değildir. Model CreativeML Open RAIL-M lisansına tabidir; kullanım şartlarını kontrol et. Model veya kalite testinin başarıya ulaşması garanti değildir. Bu workflow kodu doğrudan video üretmez ve sonucu görsel incelemeden onaylama. `workflow_dispatch` için GitHub'ın workflow dosyasının varsayılan dalda bulunması şartı geçerlidir; bu dalda dosya değişikliğiyle tetikleme kullanılır.
