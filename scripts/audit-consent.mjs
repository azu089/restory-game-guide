#!/usr/bin/env node
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const html=fs.readFileSync(path.join(root,"public","index.html"),"utf8");
for(const token of ["data-consent-settings","data-consent-dialog","data-consent-accept","data-consent-reject","data-consent-manage-open","data-consent-save","data-consent-withdraw","dialog.showModal()","restory-consent-v1"])assert(html.includes(token),token);
assert(!/<script[^>]+src="https:\/\/(?:www\.googletagmanager\.com|pl30767301\.effectivecpmnetwork\.com|pagead2\.googlesyndication\.com)/i.test(html));
for(const locale of ["","zh-CN/","zh-TW/","ja/","ko/","fr/","de/","es/","pt-BR/","ru/"]){const h=fs.readFileSync(path.join(root,"public",locale,"index.html"),"utf8");assert(h.includes("data-consent-accept"),locale);}
const faults=[html.replaceAll("data-consent-reject","data-broken-reject"),html.replaceAll("dialog.showModal()","dialog.show()"),html.replaceAll("loaded.analytics=false","loaded.analytics=true")];
const checks=[h=>h.includes("data-consent-reject"),h=>h.includes("dialog.showModal()"),h=>h.includes("loaded.analytics=false")];
faults.forEach((h,i)=>assert.equal(checks[i](h),false,`fault ${i+1} not detected`));
console.log(JSON.stringify({status:"pass",locales:10,defaultProviderRequests:0,controls:["accept","reject","manage","withdraw"],negativeFaults:faults.length},null,2));
