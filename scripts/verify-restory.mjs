// G4 视觉/交互审计：headless Chrome (CDP) + dev server 8899
// 覆盖 375 与 1440 两个视口；每个旅程先显式处理自动弹出的 consent 对话框
// （拒绝 = 零可选请求），避免模态遮挡后续真实交互。
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
  await dismissConsent(page);
}
const shot = async (page, name) => { const p = await page.screenshot(`${SHOT}/${name}.png`); console.log(`  📸 ${name}.png`); };
const ev = async (page, expr) => page.eval(expr);

/** 显式 consent-dialog 处理：对话框打开时点击拒绝（保存零请求偏好并关闭），
 *  保证后续点击不被 showModal 的模态遮挡。已持久化偏好时对话框不会自动打开。 */
async function dismissConsent(page) {
  await new Promise(r => setTimeout(r, 150));
  const open = await ev(page, `(() => { const d=document.querySelector("[data-consent-dialog]"); return !!(d && d.open); })()`);
  if (open) {
    await ev(page, `document.querySelector("[data-consent-reject]").click(); true`);
    await new Promise(r => setTimeout(r, 150));
  }
}
const escapeKey = async page => {
  await page.send("Input.dispatchKeyEvent", { type: "keyDown", key: "Escape", code: "Escape", windowsVirtualKeyCode: 27, nativeVirtualKeyCode: 27 });
  await page.send("Input.dispatchKeyEvent", { type: "keyUp", key: "Escape", code: "Escape", windowsVirtualKeyCode: 27, nativeVirtualKeyCode: 27 });
  await new Promise(r => setTimeout(r, 200));
};

const WIDTHS = [375, 1440];
const H = { 375: 812, 1440: 900 };

/* ========== consent 对话框旅程（两个视口） ========== */
for (const w of WIDTHS) {
  console.log(`== consent dialog @${w} ==`);
  const page = await newPage();
  await page.send("Emulation.setDeviceMetricsOverride", { width: w, height: H[w], deviceScaleFactor: 1, mobile: w < 500 });
  await page.goto(BASE + "/", 1200);
  // 清空偏好并重载 → 自动打开对话框，焦点落在标题
  await ev(page, `localStorage.removeItem("restory-consent-v1"); true`);
  await page.goto(BASE + "/", 1200);
  const autoOpen = await ev(page, `(() => { const d=document.querySelector("[data-consent-dialog]"); return !!(d && d.open); })()`);
  ok(autoOpen, `@${w} 无偏好时对话框自动打开`);
  const focusTitle = await ev(page, `document.activeElement && document.activeElement.id === "consent-title"`);
  ok(focusTitle, `@${w} 打开后焦点在标题`);
  await escapeKey(page);
  const closed = await ev(page, `(() => { const d=document.querySelector("[data-consent-dialog]"); return !d || !d.open; })()`);
  ok(closed, `@${w} Escape 关闭对话框`);
  const focusBack = await ev(page, `document.activeElement === document.querySelector("[data-consent-settings]")`);
  ok(focusBack, `@${w} Escape 后焦点归还设置按钮`);
  // 从设置按钮重新打开 → 拒绝保存并关闭（零请求偏好）
  await ev(page, `document.querySelector("[data-consent-settings]").click(); true`);
  await new Promise(r => setTimeout(r, 150));
  const reopen = await ev(page, `(() => { const d=document.querySelector("[data-consent-dialog]"); return !!(d && d.open); })()`);
  ok(reopen, `@${w} 设置按钮重新打开对话框`);
  await ev(page, `document.querySelector("[data-consent-reject]").click(); true`);
  await new Promise(r => setTimeout(r, 150));
  const afterReject = await ev(page, `(() => { const d=document.querySelector("[data-consent-dialog]"); return !d || !d.open; })()`);
  ok(afterReject, `@${w} 拒绝后对话框关闭`);
  page.close();
}

/* ========== 每个交互旅程跑两个视口 ========== */
for (const w of WIDTHS) {
  console.log(`== EN home @${w} ==`);
  {
    const page = await newPage();
    await setup(page, w, H[w], BASE + "/");
    await shot(page, `en-home-${w}`);
    const tickets = await ev(page, `document.querySelectorAll(".ticket").length`);
    const chips = await ev(page, `document.querySelectorAll(".jb-chip").length`);
    const visible = await ev(page, `[...document.querySelectorAll(".ticket")].filter(t=>!t.hidden).length`);
    ok(tickets === 18, `@${w} 工单卡 18 张 (got ${tickets})`);
    ok(chips === 5, `@${w} 筛选 chip 5 个 (got ${chips})`);
    ok(visible === 4, `@${w} 默认 START 组 4 张可见 (got ${visible})`);
    await ev(page, `document.querySelector('.jb-chip[data-cat="DEVICE"]').click()`);
    await new Promise(r => setTimeout(r, 300));
    const v2 = await ev(page, `[...document.querySelectorAll(".ticket")].filter(t=>!t.hidden).length`);
    ok(v2 === 3, `@${w} 点 DEVICE 后 3 张可见 (got ${v2})`);
    const overflow = await ev(page, `document.documentElement.scrollWidth > document.documentElement.clientWidth`);
    ok(!overflow, `@${w} 无横向溢出`);
    page.close();
  }
  console.log(`== EN achievements @${w} ==`);
  {
    const page = await newPage();
    await setup(page, w, H[w], BASE + "/achievements");
    await shot(page, `en-achievements-${w}`);
    const rows = await ev(page, `document.querySelectorAll(".data-table tbody tr").length`);
    ok(rows >= 40, `@${w} 成就表行数 >= 40 (got ${rows})`);
    const faq = await ev(page, `document.querySelectorAll(".panel-faq").length`);
    ok(faq >= 1, `@${w} FAQ 手风琴存在 (got ${faq})`);
    const toc = await ev(page, `document.querySelectorAll(".cab-drawers a").length`);
    ok(toc === 3, `@${w} 目录抽屉恰 3 个 (got ${toc})`);
    const overflow = await ev(page, `document.documentElement.scrollWidth > document.documentElement.clientWidth`);
    ok(!overflow, `@${w} 无横向溢出`);
    page.close();
  }
  console.log(`== EN repair-guide checklist @${w} ==`);
  {
    const page = await newPage();
    await setup(page, w, H[w], BASE + "/repair-guide");
    await shot(page, `en-repair-${w}`);
    const rc = await ev(page, `document.querySelectorAll("#rc .rc-item").length`);
    ok(rc === 5, `@${w} 修复循环清单 5 步 (got ${rc})`);
    await ev(page, `document.querySelector('#rc .rc-item[data-rc="clean"] input').click()`);
    await new Promise(r => setTimeout(r, 200));
    const on = await ev(page, `document.querySelector('#rc .rc-item[data-rc="clean"]').classList.contains("on")`);
    ok(on, `@${w} 勾选后 class=on（真交互）`);
    page.close();
  }
  console.log(`== EN zen-points calculator (input flow) @${w} ==`);
  {
    const page = await newPage();
    await setup(page, w, H[w], BASE + "/zen-points");
    await shot(page, `en-zen-${w}`);
    // 当前生成器为输入式：输入框 #zen-current → input 事件 → #zen-total 显示
    await ev(page, `(() => { const i=document.getElementById("zen-current"); i.value="17"; i.dispatchEvent(new Event("input",{bubbles:true})); return true; })()`);
    await new Promise(r => setTimeout(r, 200));
    const total = await ev(page, `document.getElementById("zen-total").textContent`);
    ok(total === "17", `@${w} Zen 输入 17 → 显示 17 (got ${total})`);
    page.close();
  }
  console.log(`== zh-CN achievements (brand + localized title) @${w} ==`);
  {
    const page = await newPage();
    await setup(page, w, H[w], BASE + "/zh-CN/achievements");
    const h1 = await ev(page, `document.querySelector("h1") ? document.querySelector("h1").textContent : ""`);
    ok(/官方 50 项成就追踪器/.test(h1), `@${w} h1 为本地化副题 (${h1.trim().slice(0,24)})`);
    const title = await ev(page, `document.title`);
    ok(/ReStory\s*—\s*官方/.test(title), `@${w} title 为品牌 + 中文副题 (${title})`);
    page.close();
  }
}

/* ========== 语言纯净 / 固定视口旅程 ========== */
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
