// Real headless Chromium smoke test, with no account or saved session.
const {chromium} = require('playwright-core');
const chromiumBin = require('@sparticuz/chromium').default;
(async () => {
  const executablePath = await chromiumBin.executablePath();
  const browser = await chromium.launch({executablePath, args: chromiumBin.args, headless: true});
  try {
    const page = await browser.newPage({viewport: {width: 720, height: 1280}});
    await page.setContent('<!doctype html><html><head><title>Browser smoke test</title></head><body><button id="ok">Test</button><p id="result">before</p><script>document.querySelector("#ok").onclick=()=>document.querySelector("#result").textContent="clicked"</script></body></html>');
    await page.click('#ok');
    if (await page.locator('#result').innerText() !== 'clicked') throw new Error('click failed');
    console.log('Chromium local interaction: OK; browser version:', browser.version());
    if (process.argv.includes('--network')) try {
      const resp = await page.goto('https://github.com/', {waitUntil: 'domcontentloaded', timeout: 20000});
      console.log('GitHub:', resp.status(), 'title:', await page.title());
    } catch (e) {
      console.error('GitHub network test failed:', e.message);
      process.exitCode = 1;
    }
  } finally { await browser.close(); }
})().catch(e => { console.error(e); process.exitCode = 1; });
