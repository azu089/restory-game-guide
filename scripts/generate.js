#!/usr/bin/env node
/**
 * ReStory Guides Static Site Generator — "Akihabara 2005 Repair Workshop" theme
 * 数据驱动 + 10 语言：data/site.json → node scripts/generate.js → public/
 * 语言：en（默认，根路径）/ zh-CN / zh-TW / ja / ko / fr / de / es / pt-BR / ru
 * 视觉：秋叶原 2005 维修工坊（暖纸+木+黄铜+印章三色、工单卡、拍立得、零件盒抽屉）
 * 交互：今日工单板筛选 / 修复循环勾选清单 / Zen 点数速算器（渐进增强，SEO 零风险）
 */
const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
const ROOT = path.join(__dirname, "..");
const DATA = JSON.parse(fs.readFileSync(path.join(ROOT, "data", "site.json"), "utf8"));
const OUT = path.join(ROOT, "public");
const KIT = require("./lib/site-kit");
const AFF = KIT.createAffiliate(DATA.site.affiliates);
const esc = KIT.esc;

// AdSense 自动广告脚本（与其余 5 站一致；未配 adsenseId 时零输出）
const AD_SNIPPET = DATA.site.adsenseId
  ? `<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${esc(DATA.site.adsenseId)}" crossorigin="anonymous"></script>`
  : "";
const clean = KIT.clean;
const LANGS = DATA.site.languages || ["en"];
const DEF = DATA.site.defaultLanguage || "en";
const CSS_V = crypto.createHash("md5").update(fs.readFileSync(path.join(ROOT,"templates","style.css"),"utf8")).digest("hex").slice(0,8);
const today = new Date().toISOString().slice(0,10);
const urlOf = KIT.createUrl({ domain: DATA.site.domain, defaultLang: DEF });
const LM = KIT.createLastmod({ manifestPath: path.join(ROOT,"data",".lastmod.json"), today });
const HERO_SET = "/images/hero-640.jpg 640w, /images/hero-1280.jpg 1280w, /images/hero.jpg 1600w";
const LANG_META = {
  "en":    { flag: "🇬🇧", name: "English",      html: "en" },
  "zh-CN": { flag: "🇨🇳", name: "简体中文",     html: "zh-CN" },
  "zh-TW": { flag: "🇹🇼", name: "繁體中文",     html: "zh-TW" },
  "ja":    { flag: "🇯🇵", name: "日本語",       html: "ja" },
  "ko":    { flag: "🇰🇷", name: "한국어",       html: "ko" },
  "fr":    { flag: "🇫🇷", name: "Français",     html: "fr" },
  "de":    { flag: "🇩🇪", name: "Deutsch",      html: "de" },
  "es":    { flag: "🇪🇸", name: "Español",      html: "es" },
  "pt-BR": { flag: "🇧🇷", name: "Português (BR)", html: "pt-BR" },
  "ru":    { flag: "🇷🇺", name: "Русский",      html: "ru" },
};
const FLAGS = {
  "en": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#012169"/><path d="M0 0 60 40M60 0 0 40" stroke="#fff" stroke-width="11"/><path d="M0 0 60 40M60 0 0 40" stroke="#C8102E" stroke-width="6"/><path d="M30 0v40M0 20h60" stroke="#fff" stroke-width="14"/><path d="M30 0v40M0 20h60" stroke="#C8102E" stroke-width="8"/></svg>',
  "zh-CN": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#EE1C25"/><g fill="#FFDE00"><path d="M12 8l1.7 3.4 3.8.5-2.8 2.7.7 3.8L12 16.7l-3.4 1.7.7-3.8-2.8-2.7 3.8-.5z"/><path d="M22 4l.8 1.6 1.8.3-1.3 1.3.3 1.8-1.6-.8-1.6.8.3-1.8-1.3-1.3 1.8-.3zM25 11l.8 1.6 1.8.3-1.3 1.3.3 1.8-1.6-.8-1.6.8.3-1.8-1.3-1.3 1.8-.3zM22 18l.8 1.6 1.8.3-1.3 1.3.3 1.8-1.6-.8-1.6.8.3-1.8-1.3-1.3 1.8-.3zM19 11l.8 1.6 1.8.3-1.3 1.3.3 1.8-1.6-.8-1.6.8.3-1.8-1.3-1.3 1.8-.3z"/></g></svg>',
  "zh-TW": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#FE0000"/><rect width="30" height="20" fill="#000095"/><g fill="#fff" stroke="#fff" stroke-width="1"><path d="M15 2l2.3 6.7 7 .1-5.6 4.2 2.1 6.7-5.8-4-5.8 4 2.1-6.7L5.7 8.8l7-.1z"/><g stroke-width=".6"><path d="M15 2v16M15 2 5.7 8.8 15 15.6M15 2l9.3 6.8L15 15.6M15 2v16M15 18.8 5.7 12 15 5.2M15 18.8l9.3-6.8L15 5.2"/></g></g></svg>',
  "ja": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#fff"/><circle cx="30" cy="20" r="11" fill="#BC002D"/></svg>',
  "ko": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#fff"/><g transform="translate(30 20)"><g transform="rotate(45)"><rect x="-10" y="-5" width="20" height="10" fill="#CD2E3A"/><rect x="-10" y="0" width="20" height="10" fill="#0047A0"/><circle r="6" fill="#fff"/></g><circle r="5" fill="#CD2E3A"/><path d="M0-5a5 5 0 0 1 0 10 2 2 0 0 1 0-10" fill="#0047A0"/></g><g fill="#000"><path d="M15 2h3v6h-3zM15 32h3v6h-3zM42 2h3v6h-3zM42 32h3v6h-3z"/></g></svg>',
  "fr": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#fff"/><rect width="20" height="40" fill="#0055A4"/><rect x="40" width="20" height="40" fill="#EF4135"/></svg>',
  "de": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#FFCE00"/><rect width="60" height="13.3" fill="#000"/><rect y="26.7" width="60" height="13.3" fill="#DD0000"/></svg>',
  "es": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#AA151B"/><rect y="10" width="60" height="20" fill="#F1BF00"/><g transform="translate(30 20)"><path d="M-10 0a10 10 0 0 1 10-10 10 10 0 0 1 0 20 10 10 0 0 1-10-10z" fill="#fff" opacity=".85"/></g></svg>',
  "pt-BR": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#009C3B"/><path d="M30 2l26 18-26 18L4 20z" fill="#FFDF00"/><circle cx="30" cy="20" r="6.5" fill="#002776"/><path d="M30 14.5a5.5 5.5 0 0 1 0 11z" fill="#fff"/></svg>',
  "ru": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#fff"/><rect width="60" height="13.3" fill="#0039A6"/><rect y="26.7" width="60" height="13.3" fill="#D52B1E"/></svg>',
};

/* ---------- SVG icons (repair workshop) ---------- */
const SVG = {
  "screwdriver": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20 14 10l-2-2L2 18l2 2zM14 10l4-4a2.1 2.1 0 0 1 3 0l1 1-2 2-2 2-1-1-3 3z"/><path d="M7 17l2 2"/></svg>',
  "wrench": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 6.5a4.5 4.5 0 0 0-6-6L11 3 9 5 7 3 3.5 6.5a4.5 4.5 0 0 0 6 6l8 8 3-3-8-8a4.5 4.5 0 0 0 2-3z"/></svg>',
  "gear": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M12 2v3m0 14v3M2 12h3m14 0h3M4.9 4.9l2.1 2.1m10 10 2.1 2.1m0-14.2-2.1 2.1m-10 10-2.1 2.1"/></svg>',
  "console": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="3"/><path d="M7 9h.01M10 9h.01M7 13h6M15 12v3m-3-1.5h6"/></svg>',
  "handheld": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="3" width="14" height="18" rx="3"/><path d="M9 6h.01M12 6h.01M15 6h.01M9 10h6M9 13h6M9 16h4"/></svg>',
  "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="7" y="2" width="10" height="20" rx="2.5"/><path d="M10.5 17.5h3"/></svg>',
  "camera": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="6" width="18" height="14" rx="3"/><path d="M8 6l1.5-3h5L16 6"/><circle cx="12" cy="13" r="4"/></svg>',
  "tape": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="7" cy="12" r="4"/><circle cx="17" cy="12" r="4"/><path d="M11 12h2"/><rect x="3" y="6" width="18" height="12" rx="2"/></svg>',
  "monitor": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="13" rx="2"/><path d="M9 21h6M12 17v4"/></svg>',
  "medal": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="15" r="5"/><path d="M9 10 7 3l5 2 5-2-2 7"/></svg>',
  "star": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"><path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/></svg>',
  "mystery": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 9v4m0 3h.01"/></svg>',
  "lamp": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9h12l-1.5 4h-9L6 9zM9.5 13l-1 8h7l-1-8"/><path d="M12 4V2m3 3 1.5-1.5M9 5 7.5 3.5"/></svg>',
  "branch": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 7h9a3 3 0 0 1 3 3v7"/><circle cx="4" cy="7" r="1.6"/><circle cx="16" cy="17" r="1.6"/><circle cx="9" cy="12" r="1.6"/><path d="M16 10l3 3-3 3"/></svg>',
  "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="3.2"/><path d="M3.5 20a5.5 5.5 0 0 1 11 0"/><circle cx="17" cy="9" r="2.5"/><path d="M16 15.5a4 4 0 0 1 4.5 4"/></svg>',
  "money": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="2.5" y="6" width="19" height="12" rx="2"/><circle cx="12" cy="12" r="3"/><path d="M6 9h.01M18 15h.01"/></svg>',
  "deck": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="5" width="16" height="12" rx="2.5"/><path d="M9 17v3m6-3v3M7 20h10"/><path d="M9 9h6"/></svg>',
  "cpu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="5" width="14" height="14" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3"/></svg>',
  "question": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 1 1 3.8 2.2c-.8.5-1.3 1-1.3 2.3v.5"/><path d="M12 17h.01"/></svg>',
  "update": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12a8 8 0 1 0 2.3-5.7"/><path d="M4 4v5h5"/><path d="M12 8v4l3 2"/></svg>',
  "book": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"/><path d="M4 19a2 2 0 0 1 2-2h13"/><path d="M8 7h7M8 10h5"/></svg>',
  "brush": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M20 3 9 14l-3-1-2 5 5-2-1-3L19 4z"/><path d="M14 7l3 3"/></svg>',
  "chip": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="6" width="12" height="12" rx="2"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/></svg>',
  "stamp": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="3" width="14" height="6" rx="1.5"/><path d="M7 9v4a5 5 0 0 0 10 0V9"/><path d="M5 17h14v2H5z"/></svg>',
  "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12.5 9.5 18 20 6.5"/></svg>',
  "search": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><circle cx="11" cy="11" r="6"/><path d="m16 16 4 4"/></svg>',
  "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>',
  "cart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 4h2l2.5 12h11L21 7H6"/><circle cx="9" cy="20" r="1.5"/><circle cx="17" cy="20" r="1.5"/></svg>',
  "bolt": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 4 14h6l-1 8 9-12h-6z"/></svg>',
  "part": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2l3 5 5 3-5 3-3 5-3-5-5-3 5-3z"/><circle cx="12" cy="10" r="1.5" fill="currentColor"/></svg>',
};
const PAGE_ICON = {
  "beginners-guide": "screwdriver", "repair-guide": "wrench", "all-devices": "console",
  "tools": "gear", "online-orders": "monitor", "licenses": "medal", "achievements": "star",
  "achievements-roadmap": "book", "hidden-achievements": "mystery", "zen-points": "lamp",
  "endings": "branch", "customers": "users", "economy": "money", "steam-deck": "deck",
  "system-requirements": "cpu", "faq": "question", "patch-notes": "update", "guides": "book",
};

/* ---------- helpers ---------- */
function siteI18n(lang){ return (DATA.site.i18n && DATA.site.i18n[lang]) || DATA.site.i18n[DEF] || {}; }
function pageOf(p, lang){ return Object.assign({}, p, p.i18n && p.i18n[lang] ? p.i18n[lang] : {}); }
function gnameOf(lang){ return (DATA.game.nameI18n && DATA.game.nameI18n[lang]) || DATA.game.name; }
function iconOf(slug){
  if (PAGE_ICON[slug]) return SVG[PAGE_ICON[slug]] || "⚙";
  const p = DATA.pages.find(x=>x.slug===slug);
  return (p && p.meta && SVG[p.meta.icon]) ? SVG[p.meta.icon] : (SVG.gear || "⚙");
}
function metaOf(slug){ return (DATA.pages.find(p=>p.slug===slug)||{}).meta || {}; }
function hreflang(slug){
  const alt = LANGS.map(l => `<link rel="alternate" hreflang="${LANG_META[l]?.html || l}" href="${urlOf(slug,l)}" />`).join("\n");
  return `${alt}\n<link rel="alternate" hreflang="x-default" href="${urlOf(slug,DEF)}" />`;
}

/* ---------- head / header / footer ---------- */
function siteLd(lang){
  return {"@context":"https://schema.org","@type":"WebSite","name":siteI18n(lang).name,
    "url":`https://${DATA.site.domain}/`, "inLanguage":LANG_META[lang]?.html||lang,
    "publisher":{"@type":"Organization","name":siteI18n(lang).name}};
}
function gameLd(){
  const g = DATA.game;
  return {"@context":"https://schema.org","@type":"VideoGame","name":g.name,
    "applicationCategory":"Game","operatingSystem":"Windows, macOS",
    "genre":g.genre,"datePublished":g.releaseDate,
    "offers":{"@type":"Offer","price":g.price.match(/\d+\.\d+/)?.[0] || "17.99","priceCurrency":"USD"}};
}
function head(title, desc, extraLd, slug, lang, ogImage){
  const ld = JSON.stringify([siteLd(lang)].concat(extraLd || []));
    const gsc = DATA.site.gscVerification ? `<meta name="google-site-verification" content="${esc(DATA.site.gscVerification)}" />` : "";
    const adsenseMeta = DATA.site.adsenseId ? `<meta name="google-adsense-account" content="ca-${esc(DATA.site.adsenseId)}" />` : "";
  const gaTag = DATA.site.gaId ? `<script async src="https://www.googletagmanager.com/gtag/js?id=${esc(DATA.site.gaId)}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','${esc(DATA.site.gaId)}');</script>` : "";
  const og = ogImage || DATA.site.ogImage;
  return `<!doctype html>
<html lang="${LANG_META[lang].html}"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(title)}</title>
<meta name="description" content="${esc(desc)}">
<link rel="canonical" href="${urlOf(slug,lang)}">
${hreflang(slug)}
<meta property="og:type" content="website"><meta property="og:site_name" content="${esc(siteI18n(lang).name)}">
<meta property="og:title" content="${esc(title)}"><meta property="og:description" content="${esc(desc)}">
<meta property="og:url" content="${urlOf(slug,lang)}"><meta property="og:image" content="https://${DATA.site.domain}${og}">
<meta name="twitter:card" content="summary_large_image">
${gsc}
${adsenseMeta}
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Audiowide&family=Nunito+Sans:wght@400;600;700;800&family=Space+Mono&family=M+PLUS+Rounded+1c:wght@400;500;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css?v=${CSS_V}">
${slug === "index" ? KIT.heroPreload({ srcset: HERO_SET, sizes: "100vw" }) : ""}
<script type="application/ld+json">${ld}</script>
${gaTag}
</head>`;
}

function renderAmazonAffiliate(lang) {
  const AMZ = {
    "en":    { title: "Game Gear", note: "As an Amazon Associate we earn from qualifying purchases. Prices and availability may change.", items: [["Gaming Keyboard","gaming keyboard"],["Gaming Mouse","gaming mouse"],["Headset","gaming headset"],["Controller","game controller"],["Monitor","gaming monitor"]] },
    "zh-CN": { title: "游戏装备", note: "作为亚马逊联盟伙伴，我们会从符合条件的购买中获得佣金。价格与库存可能随时变化。", items: [["游戏键盘","gaming keyboard"],["游戏鼠标","gaming mouse"],["耳机","gaming headset"],["手柄","game controller"],["显示器","gaming monitor"]] },
    "zh-TW": { title: "遊戲裝備", note: "作為亞馬遜聯盟夥伴，我們會從符合條件的購買中獲得佣金。價格與庫存可能隨時變化。", items: [["遊戲鍵盤","gaming keyboard"],["遊戲滑鼠","gaming mouse"],["耳機","gaming headset"],["手把","game controller"],["顯示器","gaming monitor"]] },
    "ja":    { title: "ゲームギア", note: "Amazonアソシエイトとして、適格購入から手数料を得ることがあります。価格と在庫は変動します。", items: [["ゲーミングキーボード","gaming keyboard"],["ゲーミングマウス","gaming mouse"],["ヘッドセット","gaming headset"],["コントローラー","game controller"],["モニター","gaming monitor"]] },
    "ko":    { title: "게임 장비", note: "Amazon 어소시에이트로서 적격 구매로부터 수수료를 받습니다. 가격과 재고는 변동될 수 있습니다.", items: [["게이밍 키보드","gaming keyboard"],["게이밍 마우스","gaming mouse"],["헤드셋","gaming headset"],["컨트롤러","game controller"],["모니터","gaming monitor"]] },
    "es":    { title: "Equipo de juego", note: "Como afiliado de Amazon, ganamos con las compras que califican. El precio y la disponibilidad pueden cambiar.", items: [["Teclado gamer","gaming keyboard"],["Ratón gamer","gaming mouse"],["Auriculares","gaming headset"],["Mando","game controller"],["Monitor","gaming monitor"]] },
    "fr":    { title: "Équipement de jeu", note: "En tant que partenaire Amazon, nous touchons une commission sur les achats éligibles. Prix et disponibilité peuvent changer.", items: [["Clavier gamer","gaming keyboard"],["Souris gamer","gaming mouse"],["Casque","gaming headset"],["Manette","game controller"],["Écran","gaming monitor"]] },
    "de":    { title: "Gaming-Ausrüstung", note: "Als Amazon-Partner verdienen wir an qualifizierten Käufen. Preise und Verfügbarkeit können sich ändern.", items: [["Gaming-Tastatur","gaming keyboard"],["Gaming-Maus","gaming mouse"],["Headset","gaming headset"],["Controller","game controller"],["Monitor","gaming monitor"]] },
    "it":    { title: "Accessori gaming", note: "In qualità di affiliato Amazon, guadagniamo dagli acquisti idonei. Prezzi e disponibilità possono cambiare.", items: [["Tastiera gaming","gaming keyboard"],["Mouse gaming","gaming mouse"],["Cuffie","gaming headset"],["Controller","game controller"],["Monitor","gaming monitor"]] },
    "pl":    { title: "Sprzęt gamingowy", note: "Jako partner Amazon zarabiamy na kwalifikowanych zakupach. Ceny i dostępność mogą się zmieniać.", items: [["Klawiatura gamingowa","gaming keyboard"],["Mysz gamingowa","gaming mouse"],["Słuchawki","gaming headset"],["Pad","game controller"],["Monitor","gaming monitor"]] },
    "pt-BR": { title: "Equipamentos de jogo", note: "Como associado da Amazon, ganhamos com compras qualificadas. Preços e disponibilidade podem mudar.", items: [["Teclado gamer","gaming keyboard"],["Mouse gamer","gaming mouse"],["Headset","gaming headset"],["Controle","game controller"],["Monitor","gaming monitor"]] },
    "ru":    { title: "Игровое оборудование", note: "Как партнёр Amazon мы получаем комиссию с соответствующих покупок. Цены и наличие могут меняться.", items: [["Игровая клавиатура","gaming keyboard"],["Игровая мышь","gaming mouse"],["Гарнитура","gaming headset"],["Геймпад","game controller"],["Монитор","gaming monitor"]] },
    "uk":    { title: "Ігрове обладнання", note: "Як партнер Amazon ми отримуємо комісію з відповідних покупок. Ціни та наявність можуть змінюватися.", items: [["Ігрова клавіатура","gaming keyboard"],["Ігрова миша","gaming mouse"],["Гарнітура","gaming headset"],["Геймпад","game controller"],["Монітор","gaming monitor"]] },
    "vi":    { title: "Thiết bị chơi game", note: "Là cộng tác viên Amazon, chúng tôi nhận hoa hồng từ các giao dịch mua đủ điều kiện. Giá và tình trạng hàng có thể thay đổi.", items: [["Bàn phím gaming","gaming keyboard"],["Chuột gaming","gaming mouse"],["Tai nghe","gaming headset"],["Tay cầm","game controller"],["Màn hình","gaming monitor"]] },
  };
  const t = AMZ[lang] || AMZ.en;
  const tag = "cozysimhub20-20";
  const links = t.items.map(it => `<a href="https://www.amazon.com/s?k=${encodeURIComponent(it[1])}&tag=${tag}" target="_blank" rel="sponsored noopener nofollow">${esc(it[0])}</a>`).join("");
  return `<div class="amazon-gear">
    <h3>${esc(t.title)}</h3>
    <div class="amazon-gear-links">${links}</div>
    <p class="aff-note">${esc(t.note)}</p>
  </div>`;
}


function header(lang, activeSlug){
  const s = siteI18n(lang);
  const prefix = lang === DEF ? "" : `/${lang}`;
  const navLink = (slug) => {
    const p = DATA.pages.find(x=>x.slug===slug); if(!p) return "";
    const t = pageOf(p, lang);
    return `<a class="dd-link" href="${prefix}/${slug}"><span class="dd-ic">${iconOf(slug)}</span><span>${esc(t.title.replace(/[—–].*$|:.*$/,"").trim())}</span></a>`;
  };
  const group1 = ["beginners-guide","repair-guide","all-devices","tools","online-orders","licenses","economy"];
  const group2 = ["achievements","achievements-roadmap","hidden-achievements","zen-points"];
  const group3 = ["endings","customers","steam-deck","system-requirements","faq","patch-notes"];
  const dd = (label, key, slugs) => `<details class="dd" ${activeSlug && slugs.includes(activeSlug) ? "open" : ""}><summary>${esc(label)}</summary><div class="dd-menu">${slugs.map(navLink).join("")}</div></details>`;
  const langItems = LANGS.map(l=>{
    const cur = l===lang;
    return `<a class="lang-item${cur?" on":""}" href="${urlOf(activeSlug && activeSlug!=="index" ? activeSlug : "index", l)}"><span class="lang-flag">${FLAGS[l]||""}</span><span>${LANG_META[l].name}</span>${cur?'<span class="lang-cur">✓</span>':""}</a>`;
  }).join("");
  return `<header class="site-head">
  <div class="head-inner">
    <a class="brand" href="${prefix}/"><span class="brand-mark">${SVG.screwdriver}</span><span class="brand-name">${esc(s.name)}</span></a>
    <nav class="main-nav" aria-label="${esc(s.navGuides)}">
      ${dd(s.navGroup1,"g1",group1)}
      ${dd(s.navGroup2,"g2",group2)}
      ${dd(s.navGroup3,"g3",group3)}
    </nav>
    <details class="dd lang-dd"><summary><span class="lang-flag">${FLAGS[lang]||""}</span><span class="lang-cur-name">${LANG_META[lang].name}</span></summary><div class="dd-menu lang-menu">${langItems}</div></details>
  </div>
</header>`;
}
function footer(lang){
  const s = siteI18n(lang);
  const prefix = lang === DEF ? "" : `/${lang}`;
  return `<footer class="site-foot">
  <div class="foot-inner">
    <div class="foot-note">${esc(s.footerNote)}</div>
    <div class="foot-src">${esc(s.footerSource)}</div>
    <nav class="foot-nav"><a href="${prefix}/about">${esc(s.aboutTitle)}</a> · <a href="${prefix}/privacy">${esc(s.privacyTitle)}</a> · <a href="${prefix}/contact">${esc(s.contactTitle)}</a></nav>
  </div>
${renderAmazonAffiliate(lang)}
</footer>
<script>
(function(){
  // 下拉菜单：点击外部收起 + Esc
  document.addEventListener("click",function(e){document.querySelectorAll("details.dd[open]").forEach(function(d){ if(!d.contains(e.target)) d.removeAttribute("open"); });});
  document.addEventListener("keydown",function(e){ if(e.key==="Escape"){document.querySelectorAll("details.dd[open]").forEach(function(d){d.removeAttribute("open");});} });
})();
</script>
${DATA.site.adsterra ? DATA.site.adsterra : ""}
</body></html>`;
}

/* ---------- section renderer (Repair-Workshop components) ---------- */
let SEC_IDX = 0;
function secId(){ SEC_IDX += 1; return "sec-" + SEC_IDX; }
const STEP_ICONS = ["console","handheld","monitor","chip","cart","bolt","part","stamp","brush","tape"];
function renderSection(s, lang){
  const id = secId();
  const st = siteI18n(lang);
  const tag = esc(s.tag || st.boardTag || "WORK ORDER");
  switch(s.type){
    case "steps": {
      const items = (s.items||[]).map((it,i)=>{
        return `<li class="ws-item">
          <span class="ws-no" aria-hidden="true">${String(i+1).padStart(2,"0")}</span>
          <span class="ws-ic" aria-hidden="true">${SVG[STEP_ICONS[i%STEP_ICONS.length]]||SVG.wrench}</span>
          <div class="ws-body"><b>${esc(it[0])}</b>${it[1]?`<p>${esc(it[1])}</p>`:""}</div>
        </li>`;
      }).join("");
      return `<section class="panel-block reveal" id="${id}"><div class="panel-head"><span class="panel-tag">${tag}</span><h2>${esc(s.heading)}</h2></div>${s.body?`<p class="panel-lead">${esc(s.body)}</p>`:""}<ol class="ws-list">${items}</ol></section>`;
    }
    case "list": {
      const items = (s.items||[]).map(it=>`<li class="part-item"><span class="part-mark" aria-hidden="true">${SVG.part||"▣"}</span><p>${esc(it)}</p></li>`).join("");
      return `<section class="panel-block reveal" id="${id}"><div class="panel-head"><span class="panel-tag">${tag}</span><h2>${esc(s.heading)}</h2></div>${s.body?`<p class="panel-lead">${esc(s.body)}</p>`:""}<ul class="part-list">${items}</ul></section>`;
    }
    case "table": {
      const headRow = (s.columns||[]).map(c=>`<th>${esc(c)}</th>`).join("");
      const attrsOf = i => { const a=(s.rowAttrs||[])[i]; if(!a) return ""; return " "+Object.entries(a).map(([k,v])=>`data-${k}="${esc(v)}"`).join(" "); };
      const rows = (s.rows||[]).map((r,i)=>`<tr${attrsOf(i)}>${r.map(c=>`<td>${esc(c)}</td>`).join("")}</tr>`).join("");
      const cls = s.rowAttrs ? "data-table filterable" : "data-table";
      const noMatch = s.noMatch || st.noMatch || "No matching entries";
      return `<section class="panel-block reveal" id="${id}"><div class="panel-head"><span class="panel-tag">${tag}</span><h2>${esc(s.heading)}</h2></div>${s.body?`<p class="panel-lead">${esc(s.body)}</p>`:""}<div class="${cls}"><table><thead><tr>${headRow}</tr></thead><tbody>${rows}</tbody></table><p class="table-empty" hidden>${esc(noMatch)}</p></div></section>`;
    }
    case "faq": {
      const items = (s.items||[]).map(([q,a])=>`<details class="panel-faq"><summary><span class="panel-q" aria-hidden="true">${SVG.question||"?"}</span><span>${esc(q)}</span><span class="pm">+</span></summary><div class="panel-a">${esc(a)}</div></details>`).join("");
      return `<section class="panel-block reveal" id="${id}"><div class="panel-head"><span class="panel-tag">${tag}</span><h2>${esc(s.heading)}</h2></div>${items}</section>`;
    }
    case "evidence": {
      const items = (s.items||[]).map(([label,txt])=>`<figure class="polaroid"><span class="pol-label">${esc(label)}</span><figcaption><p>${esc(txt)}</p></figcaption></figure>`).join("");
      return `<section class="panel-block reveal" id="${id}"><div class="panel-head"><span class="panel-tag">${tag}</span><h2>${esc(s.heading)}</h2></div>${s.body?`<p class="panel-lead">${esc(s.body)}</p>`:""}<div class="polaroids">${items}</div></section>`;
    }
    case "timeline": {
      const items = (s.items||[]).map(([t,txt])=>`<li class="job-tl"><span class="job-tl-date">${esc(t)}</span><p>${esc(txt)}</p></li>`).join("");
      return `<section class="panel-block reveal" id="${id}"><div class="panel-head"><span class="panel-tag">${tag}</span><h2>${esc(s.heading)}</h2></div>${s.body?`<p class="panel-lead">${esc(s.body)}</p>`:""}<ul class="job-timeline">${items}</ul></section>`;
    }
    case "note": {
      return `<section class="panel-block reveal sticky-note" id="${id}"><div class="sticky-pin" aria-hidden="true"></div><div class="panel-head"><span class="panel-tag">${tag}</span><h2>${esc(s.heading)}</h2></div>${s.body?`<p class="panel-lead">${esc(s.body)}</p>`:""}</section>`;
    }
    default:
      return `<section class="panel-block reveal" id="${id}"><div class="panel-head"><span class="panel-tag">${tag}</span><h2>${esc(s.heading)}</h2></div>${s.body?`<p class="panel-lead">${esc(s.body)}</p>`:""}</section>`;
  }
}

/* ---------- interactive tools ---------- */
function zenCalc(lang){
  const st = siteI18n(lang);
  const items = [["VHS",2],["Daruma",2],["Maneki-neko",3],["Seashell",3],["Shoji lamp",4],["Troll",4],["Billy Bass",4],["Gloves",5],["Bonsai",7],["Stormtrooper",7],["Kaiju",8],["Prism",8],["Ghostbusters",9]];
  const chips = items.map(([n,p])=>`<button type="button" class="zen-chip" data-zen="${p}">${esc(n)} <b>+${p}</b></button>`).join("");
  return `<section class="zen-calc reveal" id="zen-calc">
    <div class="panel-head"><span class="panel-tag">${esc(st.zenCalcTitle||"ZEN CALC")}</span><h2>${esc(st.zenCalcTitle||"Zen points calculator")}</h2></div>
    <p class="panel-lead">${esc(st.zenCalcLead||"")}</p>
    <div class="zen-chips">${chips}</div>
    <div class="zen-readout"><span>${esc(st.zenTotal||"Total")}</span><b id="zen-total">0</b><span class="zen-bar"><i id="zen-fill" style="width:0%"></i></span><em>${esc(st.zenTarget||"Target 100")}: 100</em><button type="button" class="zen-reset" id="zen-reset">${esc(st.zenReset||"Reset")}</button></div>
  </section>`;
}
function repairChecklist(lang){
  const st = siteI18n(lang);
  const steps = [["1","accept"],["2","disassemble"],["3","inspect"],["4","clean"],["5","reassemble"]].map(([n,k])=>{
    return `<label class="rc-item" data-rc="${k}"><input type="checkbox"><span class="rc-box"></span><span class="rc-no">${n}</span><span class="rc-tx"></span></label>`;
  }).join("");
  return `<section class="rc-wrap reveal" id="rc">
    <div class="panel-head"><span class="panel-tag">${esc(st.checklistTitle||"CHECKLIST")}</span><h2>${esc(st.checklistTitle||"Repair loop checklist")}</h2></div>
    <div class="rc-list">${steps}</div>
    <p class="rc-save">${esc(st.checklistSave||"Saved on this device")}</p>
  </section>`;
}

/* ---------- home ---------- */
function renderHome(lang){
  const s = siteI18n(lang);
  const prefix = lang === DEF ? "" : `/${lang}`;
  const gname = gnameOf(lang);
  const gintro = s.homeIntro || DATA.game.intro;
  const stats = (DATA.game.stats||[]).map((x,i)=>`<div class="gauge"><b>${esc(x.value)}</b><span>${esc((s.homeStats||[])[i] || x.label)}</span></div>`).join("");
  const keyFacts = (s.homeFacts || DATA.game.keyFacts || []).map(f=>`<li>${esc(f)}</li>`).join("");
  // 今日工单板（真交互：按工位分类 + 难度筛选）
  const BOARDS = [
    {code:"START", key:"filterStart", diff:"easy", slugs:["beginners-guide","repair-guide","tools","faq"]},
    {code:"DEVICE", key:"filterDevices", diff:"mid", slugs:["all-devices","licenses","online-orders"]},
    {code:"ACH", key:"filterAch", diff:"mid", slugs:["achievements","achievements-roadmap","hidden-achievements","zen-points"]},
    {code:"STORY", key:"filterStory", diff:"hard", slugs:["endings","customers","economy"]},
    {code:"REF", key:"filterRef", diff:"easy", slugs:["steam-deck","system-requirements","patch-notes","guides"]},
  ];
  const chips = BOARDS.map((b,i)=>`<button type="button" class="jb-chip${i===0?" on":""}" data-cat="${b.code}">${esc(s[b.key]||b.key)}</button>`).join("");
  const cards = BOARDS.flatMap(b=>b.slugs.map(slug=>{
    const p=DATA.pages.find(x=>x.slug===slug); if(!p) return "";
    const t=pageOf(p,lang);
    const diff = b.diff;
    const diffLabel = s["diff"+ (diff==="easy"?"Easy":diff==="mid"?"Mid":"Hard")] || diff;
    return `<a class="ticket" href="${prefix}/${slug}" data-cat="${b.code}" data-diff="${diff}">
      <span class="ticket-no">WO-${String(DATA.pages.indexOf(p)+1).padStart(3,"0")}</span>
      <span class="ticket-ic">${iconOf(slug)}</span>
      <span class="ticket-body"><b>${esc(t.title)}</b><span class="ticket-meta">${esc(diffLabel)} · ${esc(t.intro.split(/[.。!?！？]/)[0])}</span></span>
      <span class="ticket-stamp stamp-${diff}">${esc(diffLabel)}</span>
      <span class="ticket-go">${SVG.arrow}</span>
    </a>`;
  }).join(""));
  const heroImg = DATA.site.ogImage || "/images/hero.jpg";
  return `<!doctype html>
<html lang="${LANG_META[lang].html}"><head>${head(s.name, s.description, [gameLd()], "index", lang)}</head>
<body class="home">
${AD_SNIPPET}
${header(lang, "")}
<main class="shop">
  <section class="hero reveal">
    <div class="hero-paper">
      <div class="hero-bg">${KIT.picture({ src: heroImg, srcset: "/images/hero-640.jpg 640w, /images/hero-1280.jpg 1280w, /images/hero.jpg 1600w", sizes: "100vw", attrs: `class="hero-img" alt="${esc(gname)}" loading="eager" width="1600" height="900"` })}</div>
      <div class="hero-copy">
        <span class="hero-kicker">${esc(s.boardTag)}</span>
        <h1>${esc(gname)}</h1>
        <p class="hero-lead">${esc(gintro)}</p>
        <div class="hero-cta">
          <a class="btn btn-primary" href="${esc(DATA.game.steamUrl)}" rel="noopener sponsored">${esc(s.getOnSteam)}</a>
          <a class="btn btn-ghost" href="${prefix}/beginners-guide">${esc(s.readGuide)}</a>
        </div>
      </div>
      <div class="gauges">${stats}</div>
    </div>
  </section>
  <section class="jb reveal" id="jobboard">
    <div class="panel-head"><span class="panel-tag">${esc(s.boardTag)}</span><h2>${esc(s.guides)}</h2></div>
    <p class="panel-lead">${esc(s.boardSub)}</p>
    <div class="jb-chips">${chips}</div>
    <div class="jb-board">${cards}</div>
    <p class="jb-empty" hidden>${esc(s.noMatch)}</p>
  </section>
  <section class="about-line reveal">
    <div class="panel-head"><span class="panel-tag">${esc(s.aboutGame)}</span><h2>${esc(gname)}</h2></div>
    <ul class="log-list">${keyFacts}</ul>
  </section>
</main>
${footer(lang)}
<script>
(function(){
  var board=document.getElementById("jobboard"); if(!board) return;
  var chips=board.querySelectorAll(".jb-chip"), cards=board.querySelectorAll(".ticket"), empty=board.querySelector(".jb-empty");
  function apply(){
    var cat=board.getAttribute("data-cat")||"START", diff=board.getAttribute("data-diff")||"all", shown=0;
    cards.forEach(function(c){
      var ok=(cat==="ALL"||c.getAttribute("data-cat")===cat)&&(diff==="all"||c.getAttribute("data-diff")===diff);
      c.hidden=!ok; if(ok) shown++;
    });
    if(empty) empty.hidden=shown>0;
  }
  chips.forEach(function(ch){ ch.addEventListener("click",function(){
    chips.forEach(function(x){x.classList.remove("on");});
    ch.classList.add("on"); board.setAttribute("data-cat",ch.getAttribute("data-cat")); apply();
  });});
  board.setAttribute("data-cat","START"); apply();
})();
</script>
</body></html>`;
}

/* ---------- article pages ---------- */
function renderFull(lang, title, desc, extraLd, slug, body, ogImage){
  const s = siteI18n(lang);
  return head(title, desc, extraLd, slug, lang, ogImage) + "<body>" + AD_SNIPPET + header(lang, slug === "index" ? "" : slug) + body + footer(lang);
}
function renderPage(lang, page){
  const t = Object.assign(pageOf(page, lang), {slug: page.slug});
  const prefix = lang === DEF ? "" : `/${lang}`;
  SEC_IDX = 0;
  const toc = (t.sections||[]).filter(x=>x.heading).map(x=>{
    SEC_IDX += 1;
    const n = String(SEC_IDX).padStart(2,"0");
    return `<a href="#sec-${SEC_IDX}"><span class="cab-no">${n}</span><span class="cab-tx">${esc(x.heading)}</span></a>`;
  }).join("");
  SEC_IDX = 0;
  let sections2 = (t.sections||[]).map(x => renderSection(x, lang)).join("");
  // 真交互挂载
  if (page.slug === "zen-points") sections2 += zenCalc(lang);
  if (page.slug === "all-devices") {
    const devPages = DATA.pages.filter(x=>x.slug.startsWith("devices/"));
    const grid = devPages.map(dp=>{
      const t = pageOf(dp, lang);
      return `<a class="dev-link" href="${prefix}/${dp.slug}"><span class="dev-ic">${iconOf(dp.slug)}</span><span class="dev-tx">${esc(t.title)}</span><span class="dev-go">${SVG.arrow}</span></a>`;
    }).join("");
    sections2 += `<section class="panel-block reveal" id="dev-grid"><div class="panel-head"><span class="panel-tag">${esc(siteI18n(lang).boardTag)}</span><h2>${esc(siteI18n(lang).devicesTitle || "Device step pages")}</h2></div><p class="panel-lead">${esc(siteI18n(lang).devicesLead || "Each device has its own page with the repair loop, weak points and an interactive checklist.")}</p><div class="dev-grid">${grid}</div></section>`;
  }
  if (page.slug === "repair-guide" || page.slug.startsWith("devices/")) sections2 += repairChecklist(lang);
  const srcList = page.sources || [];
  const sources = srcList.map(x=>`<li>${AFF.anchor({ url: x.url, text: (x.labels && x.labels[lang]) || x.label, suffix: " ↗" })}</li>`).join("");
  const affNote = AFF.needsDisclosure(srcList.map(x=>x.url)) ? `<p class="aff-note">${esc(KIT.affiliateDisclosure(lang))}</p>` : "";
  const s = siteI18n(lang);
  const heroImg = t.heroImage;
  const srcsetOf = img => { if(!img) return null; const base=img.replace(/\.(jpg|jpeg|png|webp)$/i,""); return {srcset:`${base}-640.jpg 640w, ${base}-1280.jpg 1280w, ${img} 1600w`, sizes:"(max-width: 640px) 94vw, (max-width: 960px) 92vw, 820px"}; };
  const pageHero = heroImg ? `<div class="bench-img">${KIT.picture({...srcsetOf(heroImg), src:heroImg, attrs:`alt="${esc(t.title)}" loading="lazy" width="1600" height="900"`})}</div>` : "";
  const related = DATA.pages.filter(p=>p.slug!==page.slug).slice(0,5).map((p,i)=>{
    return `<a href="${prefix}/${p.slug}" class="rel-link"><span class="rel-no">${String(i+1).padStart(2,"0")}</span><span class="nav-ic">${iconOf(p.slug)}</span><span>${esc(pageOf(p,lang).title)}</span></a>`;
  }).join("");
  const body = `
  <main class="bench-page">
  <div class="bench-wrap">
    <div class="bench-bar">
      <span class="bench-code">${esc(s.boardTag)} / ${esc(page.slug.toUpperCase())}</span>
      <span class="bench-meta">${esc(t.title.split(":")[0].split("—")[0].trim())} · ${today}</span>
      <a class="bench-home" href="${prefix}/">${esc(s.navHome)}</a>
    </div>
    <header class="bench-head reveal">
      <span class="bench-ic" aria-hidden="true">${iconOf(page.slug)}</span>
      <h1>${esc(t.title)}</h1>
      <p class="bench-lead">${esc(t.intro)}</p>
      ${pageHero}
    </header>
    <div class="bench-body">
      <nav class="cabinet-nav reveal">
        <b class="cab-title">${esc(s.updated||"Contents")}</b>
        ${toc ? `<div class="cab-drawers">${toc}</div>` : ""}
      </nav>
      <div class="bench-main">
        ${sections2}
        ${renderAmazonAffiliate(lang)}
        ${sources ? `<footer class="bench-src reveal"><b>${esc(s.sources||"Sources")}</b><ul>${sources}</ul>${affNote}
</footer>` : ""}
      </div>
      <aside class="bench-side reveal">
        <div class="side-block"><span class="hab-code">${esc(s.related||"RELATED")}</span>${related}</div>
        <div class="side-block"><span class="hab-code">STEAM</span><p>${esc(gnameOf(lang))}</p><a class="btn btn-primary" href="${esc(DATA.game.steamUrl)}" target="_blank" rel="noopener sponsored">${esc(s.getOnSteam)}</a></div>
      </aside>
    </div>
  </div>
  </main>
  <script>
  (function(){
    // 修复循环勾选清单（localStorage）
    var rc=document.getElementById("rc"); if(rc){
      var key="restory-rc-"+document.documentElement.lang;
      var items=rc.querySelectorAll(".rc-item"); var saved={}; try{saved=JSON.parse(localStorage.getItem(key)||"{}");}catch(e){}
      items.forEach(function(it){ var k=it.getAttribute("data-rc"); var tx=it.querySelector(".rc-tx");
        var label=document.querySelectorAll("#rc .panel-lead, #rc .rc-save"); void label;
        void it;
        if(saved[k]) it.classList.add("on");
        it.addEventListener("click",function(ev){
          // 阻止浏览器 label→input 原生激活，避免与手动 toggle 双重翻转
          ev.preventDefault();
          if(ev.target.tagName==="INPUT") return;
          var c=it.querySelector("input");
          c.checked=!c.checked;
          it.classList.toggle("on",c.checked);
          save();
        });
        var inp=it.querySelector("input"); inp.addEventListener("change",function(){ it.classList.toggle("on",inp.checked); save(); });
      });
      function save(){ var o={}; items.forEach(function(it){ o[it.getAttribute("data-rc")]=it.classList.contains("on"); }); localStorage.setItem(key,JSON.stringify(o)); }
    }
    // Zen 点数速算器
    var zc=document.getElementById("zen-calc"); if(zc){
      var chips=zc.querySelectorAll(".zen-chip"), total=zc.querySelector("#zen-total"), fill=zc.querySelector("#zen-fill"), reset=zc.querySelector("#zen-reset");
      var sum=0;
      chips.forEach(function(ch){ ch.addEventListener("click",function(){ sum+=parseInt(ch.getAttribute("data-zen"),10); draw(); }); });
      if(reset) reset.addEventListener("click",function(){ sum=0; draw(); });
      function draw(){ total.textContent=sum; fill.style.width=Math.min(100,sum)+"%"; total.classList.toggle("done",sum>=100); }
      draw();
    }
  })();
  </script>`;
  const extraLd = [articleLd(page, lang), breadcrumbLd(page, lang)];
  const fq = faqLd(t.sections);
  if (fq) extraLd.push(fq);
  return renderFull(lang, t.metaTitle || t.title, t.metaDescription, extraLd, page.slug, body, heroImg || DATA.site.ogImage);
}

/* ---------- static pages ---------- */
function renderStatic(lang, slug, title, body){
  const prefix = lang === DEF ? "" : `/${lang}`;
  const s = siteI18n(lang);
  const descRaw = KIT.staticDesc(slug, lang, s.name, title);
  const isCjk = ["zh-CN","zh-TW","ja","ko"].includes(lang);
  const desc = descRaw.length > (isCjk ? 74 : 148) ? descRaw.slice(0,(isCjk?73:147)).replace(/\s+[^\s]*$/,"") + "…" : descRaw;
  const pageTitle = `${title} — ${s.name}`;
  return renderFull(lang, pageTitle, desc, [breadcrumbLd({slug,title}, lang)], slug, `<main class="container"><div class="article-wrap single"><article><div class="page-hero reveal"><span class="evidence-tag">${esc(s.boardTag)} // ${esc(slug.toUpperCase())}</span><h1>${esc(title)}</h1></div>${body}</article></div></main>`);
}
function genStatic(lang){
  const s = siteI18n(lang);
  const dir = path.join(OUT, lang === DEF ? "" : lang);
  const aboutPoints = (s.aboutPoints && s.aboutPoints.length) ? s.aboutPoints : (DATA.game.aboutPoints || []);
  const aboutBody = `<p>${esc(s.aboutText)}</p><h2 style="font-size:1.05rem;margin:18px 0 8px">${esc(s.aboutSources)}</h2><ul class="checks">${aboutPoints.map(x=>`<li>${esc(x)}</li>`).join("")}</ul>`;
  writePage(path.join(dir,"about.html"), "about", lang, renderStatic(lang,"about", s.aboutTitle,
    aboutBody + `<section class="card">` + KIT.editorialPolicy(lang, { siteName: s.name, contactEmail: `contact@${DATA.site.domain}` }) + `</section>`));
  const privacyBody = s.privacyBody || `<p>This is a game guide website. We respect your privacy.</p>`;
  writePage(path.join(dir,"privacy.html"), "privacy", lang, renderStatic(lang,"privacy", s.privacyTitle, privacyBody));
  const contactBody = s.contactBody || `<p>contact@${DATA.site.domain}</p>`;
  writePage(path.join(dir,"contact.html"), "contact", lang, renderStatic(lang,"contact", s.contactTitle, contactBody));
}

/* ---------- JSON-LD helpers ---------- */
function articleLd(page, lang){
  const t = pageOf(page, lang);
  return {"@context":"https://schema.org","@type":"Article","headline":t.title,"description":t.metaDescription,
    "url":urlOf(page.slug,lang),datePublished:today,dateModified:KIT.LASTMOD_TOKEN,
    inLanguage:LANG_META[lang]?.html||lang,publisher:{"@type":"Organization",name:siteI18n(lang).name}};
}
function faqLd(sections){
  const items=(sections||[]).filter(s=>s.type==="faq").flatMap(s=>s.items||[]);
  if(!items.length) return null;
  return {"@context":"https://schema.org","@type":"FAQPage",mainEntity:items.map(([q,a])=>({"@type":"Question",name:q,acceptedAnswer:{"@type":"Answer",text:a}}))};
}
function breadcrumbLd(page, lang){
  return {"@context":"https://schema.org","@type":"BreadcrumbList",itemListElement:[
    {"@type":"ListItem",position:1,name:siteI18n(lang).navHome,item:`https://${DATA.site.domain}/${lang===DEF?"":lang+"/"}`},
    {"@type":"ListItem",position:2,name:pageOf(page, lang).title,item:urlOf(page.slug,lang)}]};
}

/* ---------- build ---------- */
const writePage = (filePath, slug, lang, html) => {
  fs.mkdirSync(path.dirname(filePath), {recursive:true});
  fs.writeFileSync(filePath, LM.stamp(urlOf(slug, lang), html));
};
fs.rmSync(OUT, {recursive:true, force:true});
fs.mkdirSync(OUT, {recursive:true});

// favicon：螺丝刀 + 维修铺
const faviconSvg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect x="2" y="2" width="60" height="60" rx="14" fill="#2A241C"/><rect x="2" y="2" width="60" height="60" rx="14" fill="none" stroke="#C29A3B" stroke-width="2"/><path d="M20 46 40 26l-3-3L17 43l3 3zM40 26l7-7a3 3 0 0 1 5 1l1 1-3 3-3 3-2-2-5 5z" fill="none" stroke="#F3EDDF" stroke-width="2.6" stroke-linejoin="round"/><circle cx="34" cy="32" r="2.4" fill="#C29A3B"/></svg>`;
fs.writeFileSync(path.join(OUT, "favicon.svg"), faviconSvg);
for (const f of ["favicon-16x16.png","favicon-32x32.png","apple-touch-icon.png"]) {
  const srcFav = path.join(ROOT,"templates","favicon",f);
  if (fs.existsSync(srcFav)) fs.copyFileSync(srcFav, path.join(OUT,f));
}
for (const f of ["favicon.svg","favicon-16x16.png","favicon-32x32.png","apple-touch-icon.png"]) {
  const src = path.join(ROOT,"assets","favicon",f);
  if (fs.existsSync(src)) fs.copyFileSync(src, path.join(OUT,f));
}
const imgDir = path.join(ROOT,"assets","images");
if (fs.existsSync(imgDir)) {
  fs.mkdirSync(path.join(OUT,"images"),{recursive:true});
  for (const f of fs.readdirSync(imgDir)) {
    if (/\.(jpg|jpeg|webp)$/i.test(f)) fs.copyFileSync(path.join(imgDir,f), path.join(OUT,"images",f));
  }
}
fs.mkdirSync(path.join(OUT,"css"),{recursive:true});
fs.writeFileSync(path.join(OUT,"css","style.css"), fs.readFileSync(path.join(ROOT,"templates","style.css"),"utf8"));

for (const lang of LANGS) {
  const dir = path.join(OUT, lang === DEF ? "" : lang);
  fs.mkdirSync(dir, {recursive:true});
  writePage(path.join(dir,"index.html"), "index", lang, renderHome(lang));
  for (const page of DATA.pages) {
    SEC_IDX = 0;
    const html = renderPage(lang, page);
    writePage(path.join(dir, page.slug + ".html"), page.slug, lang, html);
  }
  genStatic(lang);
}
gen404();

const urls = [];
for (const lang of LANGS) {
  urls.push({ loc: urlOf("index",lang), priority: "1.0" });
  for (const p of DATA.pages) urls.push({ loc: urlOf(p.slug,lang), priority: "0.8" });
  for (const sp of ["about","privacy","contact"]) urls.push({ loc: urlOf(sp,lang), priority: "0.3" });
}
const smN = KIT.writeSitemap(OUT, urls, LM);
KIT.writeRobots(OUT, DATA.site.domain);
KIT.writeAds(OUT, DATA.site.adsenseId);
KIT.writeHeaders(OUT);
KIT.writeIndexNowKey(OUT, DATA.site.indexNowKey);
KIT.writeLlmsTxt(OUT, {
  siteName: DATA.site.name,
  domain: DATA.site.domain,
  summary: `Unofficial ${DATA.game.name} guide site. Each page answers one question players actually search for, and lists the sources it was checked against. Available in ${LANGS.length} languages: ${LANGS.join(", ")}.`,
  pages: DATA.pages.map(p => { const t = pageOf(p, DEF); return { slug: p.slug, title: t.title, desc: t.metaDescription }; }),
  notes: [
    "Facts are checked against the official Steam store page, allthings.how and intoindiegames; every page lists its own sources at the bottom.",
    "Anything we could not verify is explicitly marked as unverified — gaps are left open rather than filled with generated text.",
    "Localised versions live under /<lang>/ (e.g. /ja/beginners-guide) and are declared via hreflang on every page.",
    "This is an unofficial fan site, not affiliated with the game's developer or publisher."
  ]
});
const lm = LM.save();
console.log(`✓ ${LANGS.length} locales × ${1+DATA.pages.length+3} pages｜sitemap ${smN} URL｜内容有变更 ${lm.changed}/${lm.total} 页`);

function gen404(){
  const s = siteI18n(DEF);
  const hot = ["beginners-guide","all-devices","achievements","endings","tools","zen-points"].map(slug=>{
    const p=DATA.pages.find(x=>x.slug===slug); if(!p) return "";
    const t=pageOf(p,DEF);
    return `<a class="rel-link" href="/${slug}"><span class="nav-ic">${iconOf(slug)}</span><span>${esc(t.title)}</span></a>`;
  }).join("");
  const html = `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex"><title>404 — ${esc(s.name)}</title><link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Audiowide&family=Nunito+Sans:wght@400;600;700;800&family=Space+Mono&family=M+PLUS+Rounded+1c:wght@400;500;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css?v=${CSS_V}"></head><body class="home">${AD_SNIPPET}<main class="shop"><section class="hero reveal"><div class="hero-paper"><div class="hero-copy"><span class="hero-kicker">404</span><h1>${esc(s.noMatch||"Not found")}</h1><p class="hero-lead">This page is missing — the part was probably lost in the drawer.</p><a class="btn btn-primary" href="/">${esc(s.navHome)}</a><a class="btn btn-ghost" href="/beginners-guide">${esc(s.readGuide)}</a></div></div></section><section class="jb"><div class="panel-head"><span class="panel-tag">FIX IT</span><h2>Popular guides</h2></div><div class="jb-board">${hot}</div></section></main>${footer(DEF)}</body></html>`;
  fs.writeFileSync(path.join(OUT,"404.html"), html);
}
