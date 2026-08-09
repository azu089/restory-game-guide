// G4 视觉/交互审计：headless Chrome (CDP 9223) + dev server 8899
import { newPage } from "../../../packages/site-kit/cdp.mjs";
import fs from "fs";
const BASE = "http://127.0.0.1:8899";
const SHOT = "/tmp/restory-shots";
fs.mkdirSync(SHOT, { recursive: true });
let pass = 0, fail = 0;
const ok = (cond, msg) => { if (cond) { pass++; console.log("  ✅", msg); } else { fail++; console.log("  ❌", msg); } };

async function setup(page, w, h, url) {
  await page.send("Emulation.setDeviceMetricsOverride", { width: w, height: h, deviceScaleFactor: 1, mobile: w < 500 });
  await page.goto(url, 1200);
}
const shot = async (page, name) => { const p = await page.screenshot(`${SHOT}/${name}.png`); console.log(`  📸 ${name}.png`); };
const ev = async (page, expr) => page.eval(expr);

console.log("== EN home (desktop) ==");
{
  const page = await newPage();
  await setup(page, 1440, 900, BASE + "/");
  await shot(page, "en-home");
  const tickets = await ev(page, `document.querySelectorAll(".ticket").length`);
  const chips = await ev(page, `document.querySelectorAll(".jb-chip").length`);
  const visible = await ev(page, `[...document.querySelectorAll(".ticket")].filter(t=>!t.hidden).length`);
  ok(tickets === 18, `home 工单卡 18 张 (got ${tickets})`);
  ok(chips === 5, `筛选 chip 5 个 (got ${chips})`);
  ok(visible === 4, `默认 START 组 4 张可见 (got ${visible})`);
  await ev(page, `document.querySelector('.jb-chip[data-cat="DEVICE"]').click()`);
  await new Promise(r => setTimeout(r, 300));
  const v2 = await ev(page, `[...document.querySelectorAll(".ticket")].filter(t=>!t.hidden).length`);
  ok(v2 === 3, `点 DEVICE 后 3 张可见 (got ${v2})`);
  const overflow = await ev(page, `document.documentElement.scrollWidth > document.documentElement.clientWidth`);
  ok(!overflow, "desktop 无横向溢出");
  page.close();
}
console.log("== EN achievements (desktop) ==");
{
  const page = await newPage();
  await setup(page, 1440, 900, BASE + "/achievements");
  await shot(page, "en-achievements");
  const rows = await ev(page, `document.querySelectorAll(".data-table tbody tr").length`);
  ok(rows >= 40, `成就表行数 >= 40 (got ${rows})`);
  const faq = await ev(page, `document.querySelectorAll(".panel-faq").length`);
  ok(faq >= 1, `FAQ 手风琴存在 (got ${faq})`);
  const toc = await ev(page, `document.querySelectorAll(".cab-drawers a").length`);
  ok(toc >= 4, `目录抽屉 >= 4 (got ${toc})`);
  const overflow = await ev(page, `document.documentElement.scrollWidth > document.documentElement.clientWidth`);
  ok(!overflow, "desktop 无横向溢出");
  page.close();
}
console.log("== EN repair-guide checklist ==");
{
  const page = await newPage();
  await setup(page, 1440, 900, BASE + "/repair-guide");
  await shot(page, "en-repair");
  const rc = await ev(page, `document.querySelectorAll("#rc .rc-item").length`);
  ok(rc === 5, `修复循环清单 5 步 (got ${rc})`);
  await ev(page, `document.querySelector('#rc .rc-item[data-rc="clean"] input').click()`);
  await new Promise(r => setTimeout(r, 200));
  const on = await ev(page, `document.querySelector('#rc .rc-item[data-rc="clean"]').classList.contains("on")`);
  ok(on, "勾选后 class=on（真交互）");
  page.close();
}
console.log("== EN zen-points calculator ==");
{
  const page = await newPage();
  await setup(page, 1440, 900, BASE + "/zen-points");
  await shot(page, "en-zen");
  await ev(page, `document.querySelector('.zen-chip[data-zen="9"]').click()`);
  await ev(page, `document.querySelector('.zen-chip[data-zen="8"]').click()`);
  await new Promise(r => setTimeout(r, 200));
  const total = await ev(page, `document.getElementById("zen-total").textContent`);
  ok(total === "17", `Zen 速算 9+8=17 (got ${total})`);
  page.close();
}
console.log("== zh-CN home (mobile 375) ==");
{
  const page = await newPage();
  await setup(page, 375, 812, BASE + "/zh-CN/");
  await shot(page, "zh-home-mobile");
  const overflow = await ev(page, `document.documentElement.scrollWidth > document.documentElement.clientWidth`);
  ok(!overflow, "移动端无横向溢出");
  const nav = await ev(page, `document.querySelectorAll(".dd").length`);
  ok(nav >= 4, `移动端导航下拉存在 (got ${nav})`);
  page.close();
}
console.log("== zh-CN achievements (language purity) ==");
{
  const page = await newPage();
  await setup(page, 1440, 900, BASE + "/zh-CN/achievements");
  const h1 = await ev(page, `document.querySelector("h1") ? document.querySelector("h1").textContent : ""`);
  ok(/维修物语/.test(h1), `h1 为中文 (${h1.trim().slice(0,20)})`);
  const title = await ev(page, `document.title`);
  ok(/维修物语/.test(title), `title 为中文 (${title})`);
  page.close();
}
console.log("== ja privacy (language purity) ==");
{
  const page = await newPage();
  await setup(page, 1440, 900, BASE + "/ja/privacy");
  const bodyText = await ev(page, `document.body.innerText`);
  ok(/プライバシー|Cookie|収集/.test(bodyText), "ja privacy 正文为日文");
  page.close();
}
console.log("== zh-TW home (OpenCC) ==");
{
  const page = await newPage();
  await setup(page, 1440, 900, BASE + "/zh-TW/");
  const title = await ev(page, `document.title`);
  ok(/維修物語/.test(title), `zh-TW title 繁体 (${title})`);
  page.close();
}
console.log(`\nRESULT: ${pass} pass / ${fail} fail`);
process.exit(fail ? 1 : 0);
