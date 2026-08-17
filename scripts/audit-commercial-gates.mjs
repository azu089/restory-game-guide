#!/usr/bin/env node
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const pub=path.join(root,"public");
const walk=d=>fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(d,e.name)):[path.join(d,e.name)]);
const rows=walk(pub).filter(f=>f.endsWith(".html")).map(f=>({file:path.relative(pub,f),html:fs.readFileSync(f,"utf8")}));
assert.equal(rows.length,441);
for(const {file,html} of rows){
  assert(!/<script[^>]+src="https:\/\/www\.googletagmanager\.com\/gtag\/js/i.test(html),`eager GA4 ${file}`);
  assert(!/<script[^>]+src="https:\/\/pl30767301\.effectivecpmnetwork\.com/i.test(html),`eager Adsterra ${file}`);
  assert(!html.includes("pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"),`AdSense serving ${file}`);
  assert(!html.includes("affiliate_click"),`affiliate event emitted ${file}`);
  assert(!/href="[^"]*store\.steampowered\.com[^"]*"[^>]*rel="[^"]*sponsored/i.test(html),`sponsored Steam ${file}`);
  assert(html.includes("data-consent-settings"),`settings missing ${file}`);
}
for(const file of ["privacy.html","zh-CN/privacy.html","zh-TW/privacy.html","ja/privacy.html","ko/privacy.html","fr/privacy.html","de/privacy.html","es/privacy.html","pt-BR/privacy.html","ru/privacy.html"]){
  const html=rows.find(r=>r.file===file)?.html||"";
  for(const marker of ["Google Analytics 4","Adsterra","effectivecpmnetwork.com","AdSense"])assert(html.includes(marker),`${marker} missing ${file}`);
}
const faultChecks=[
  ["sponsored pollution",rows[0].html+'<a href="https://store.steampowered.com" rel="sponsored">fault</a>',h=>!/rel="[^"]*sponsored/.test(h)],
  ["affiliate classifier",rows[0].html.replace("outbound_click","affiliate_click"),h=>!h.includes("affiliate_click")],
];
for(const [name,fault,check] of faultChecks){let failed=false;try{assert(check(fault));}catch{failed=true;}assert(failed,`${name} fault escaped`);}
console.log(JSON.stringify({status:"pass",htmlPages:rows.length,eagerGa4:0,eagerAdsterra:0,adsenseServing:0,sponsoredSteam:0,affiliateEvents:0,privacyLocales:10,negativeFaults:faultChecks.length},null,2));
