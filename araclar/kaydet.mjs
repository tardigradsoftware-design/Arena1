// Bir sahne HTML'ini kare kare MP4'e çevirir.
// Kullanım: node araclar/kaydet.mjs ornekler/kil.html [cikti.mp4] [--ses ses.mp3]
// Sahne sözleşmesi STUDYO.md'de: sayfa window.ciz(kare), window.SURE (sn) ve window.FPS tanımlar, #sahne 1080x1920'dir.
import { chromium } from "playwright";
import { spawn } from "node:child_process";
import path from "node:path";
import fs from "node:fs";

const arg = process.argv.slice(2);
const sesI = arg.indexOf("--ses");
const ses = sesI >= 0 ? arg.splice(sesI, 2)[1] : null;
const [girdi, ciktiArg] = arg;
if (!girdi || !fs.existsSync(girdi)) {
  console.error("Kullanım: node araclar/kaydet.mjs <sahne.html> [cikti.mp4] [--ses ses.mp3]");
  process.exit(1);
}
const cikti = ciktiArg || girdi.replace(/\.html?$/, "") + ".mp4";

const tarayici = await chromium.launch({ ...(process.env.STUDYO_CHROMIUM ? {executablePath: process.env.STUDYO_CHROMIUM} : {}), args: ["--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--allow-file-access-from-files"] });
const sayfa = await tarayici.newPage({ viewport: { width: Number(process.env.STUDYO_WIDTH || 1080), height: Number(process.env.STUDYO_HEIGHT || 1920) }, deviceScaleFactor: 1 });
await sayfa.goto("file://" + path.resolve(girdi) + "?kayit=1");
await sayfa.waitForFunction(() => typeof window.ciz === "function" && window.SURE > 0, null, { timeout: 30000 });
await sayfa.evaluate(() => document.fonts.ready);
if (await sayfa.evaluate(() => typeof window.hazir === "function")) await sayfa.evaluate(() => window.hazir());
const { SURE, FPS } = await sayfa.evaluate(() => ({ SURE: window.SURE, FPS: window.FPS || 30 }));
const toplam = Math.round(SURE * FPS);

const ff = spawn(process.env.FFMPEG_PATH || "ffmpeg", [
  "-y", "-loglevel", "error",
  "-f", "image2pipe", "-framerate", String(FPS), "-i", "-",
  ...(ses ? ["-i", ses, "-shortest", "-c:a", "aac", "-b:a", "192k"] : []),
  "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", process.env.STUDYO_CRF || "17", "-preset", "medium", "-movflags", "+faststart",
  cikti,
], { stdio: ["pipe", "inherit", "inherit"] });

const sahne = await sayfa.$("#sahne");
for (let f = 0; f < toplam; f++) {
  await sayfa.evaluate((k) => window.ciz(k), f);
  const kare = await sahne.screenshot({ type: "jpeg", quality: 92 });
  if (!ff.stdin.write(kare)) await new Promise((r) => ff.stdin.once("drain", r));
  if (f % FPS === 0) process.stdout.write(`\r${f}/${toplam} kare`);
}
ff.stdin.end();
const code = await new Promise((resolve, reject) => { ff.on("error", reject); ff.on("close", resolve); });
await tarayici.close();
if (code !== 0) throw new Error(`ffmpeg exited with code ${code}`);
console.log(`\r${toplam}/${toplam} kare → ${cikti}`);
