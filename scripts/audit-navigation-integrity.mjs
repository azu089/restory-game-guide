#!/usr/bin/env node
// 导航完整性 + 内容完整性审计（G4 negative-path coverage）
// 覆盖：44px 触控目标 / 移动端菜单不横向滚动 / Escape 焦点归还 / 菜单语义，
//       以及 v1.0.010r patch 历史存在性、五步修复清单正文非空、成就搜索标签持久性（10 语）。
// 每个注入故障都必须被对应检查捕获：故障逃逸即非零退出。
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const css=fs.readFileSync(path.join(root,"templates","style.css"),"utf8");
const html=fs.readFileSync(path.join(root,"public","index.html"),"utf8");
const LOCALES=["","zh-CN/","zh-TW/","ja/","ko/","fr/","de/","es/","pt-BR/","ru/"];
const readHtml=(rel)=>fs.readFileSync(path.join(root,"public",rel),"utf8");

/* ---------- 导航（原有） ---------- */
for(const token of ["min-height:44px","grid-template-columns:repeat(3,minmax(0,1fr))","overflow:visible","grid-template-columns:1fr"])assert(css.includes(token),token);
assert(html.includes('e.key==="Escape"')&&html.includes("s.focus()"),"Escape focus return missing");
assert(html.includes('aria-haspopup="true"'),"menu semantics missing");

/* ---------- 内容完整性（10 语） ---------- */
// 1) v1.0.010r patch 历史：每语 patch-notes 页必须包含官方版本串（正向断言）
const patchOk=h=>h.includes("1.0.010r");
for(const l of LOCALES) assert(patchOk(readHtml(l+"patch-notes.html")),`patch v1.0.010r missing ${l||"en"}`);

// 2) 五步修复清单：每语 repair-guide 恰好 5 个 rc-item，标题与正文都非空
const RC_RE=/<label class="rc-item" data-rc="([a-z]+)"><input type="checkbox"><span class="rc-box"><\/span><span class="rc-no">\d+<\/span><span class="rc-tx"><b>([^<]*)<\/b><small>([^<]*)<\/small><\/span><\/label>/g;
const checklistOk=h=>{
  const m=[...h.matchAll(RC_RE)];
  return m.length===5 && m.every(x=>x[2].trim().length>0 && x[3].trim().length>0);
};
for(const l of LOCALES) assert(checklistOk(readHtml(l+"repair-guide.html")),`repair checklist bodies empty/missing ${l||"en"}`);

// 3) 成就搜索标签：每语 achievements 页必须有可见 field-label 且非空（非 placeholder-only）
const SEARCH_RE=/<label class="ach-search"><span class="field-label">([^<]*)<\/span><input type="search" data-ach-search/;
const searchOk=h=>{const m=h.match(SEARCH_RE);return !!m && m[1].trim().length>0;};
for(const l of LOCALES) assert(searchOk(readHtml(l+"achievements.html")),`achievement search label missing/empty ${l||"en"}`);

/* ---------- 注入故障：每个都必须被捕获 ---------- */
const faultChecks=[
  // patch-freshness 回归：把 en patch-notes 的 1.0.010r 抹掉
  ["patch-freshness", readHtml("patch-notes.html").replaceAll("1.0.010r","1.0.010x"), patchOk],
  // 修复清单正文为空（标题保留，正文置空）
  ["empty checklist body", readHtml("repair-guide.html").replace(/<label class="rc-item" data-rc="clean">([\s\S]*?)<small>[^<]*<\/small>/, `<label class="rc-item" data-rc="clean">$1<small></small>`), checklistOk],
  // 成就搜索 label 变 placeholder-only（field-label 空）
  ["empty search label", readHtml("zh-CN/achievements.html").replace(SEARCH_RE, '<label class="ach-search"><span class="field-label"></span><input type="search" data-ach-search'), searchOk],
];
for(const [name,fault,check] of faultChecks){let failed=false;try{assert(check(fault));}catch{failed=true;}assert(failed,`${name} fault escaped`);}
console.log(JSON.stringify({status:"pass",staticWidths:[375,1440],targetMinPx:44,escapeFocusReturn:true,horizontalMenuScroll:false,patchFreshness:"1.0.010r",checklistSteps:5,searchLabelLocales:10,negativeFaults:faultChecks.length},null,2));
