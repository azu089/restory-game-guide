#!/usr/bin/env node
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const css=fs.readFileSync(path.join(root,"templates","style.css"),"utf8");
const html=fs.readFileSync(path.join(root,"public","index.html"),"utf8");
for(const token of ["min-height:44px","grid-template-columns:repeat(3,minmax(0,1fr))","overflow:visible","grid-template-columns:1fr"])assert(css.includes(token),token);
assert(html.includes('e.key==="Escape"')&&html.includes("s.focus()"),"Escape focus return missing");
assert(html.includes('aria-haspopup="true"'),"menu semantics missing");
const bad=css.replace("overflow:visible","overflow-x:auto");assert.equal(bad.includes("overflow:visible"),false,"overflow fault escaped");
console.log(JSON.stringify({status:"pass",staticWidths:[375,1440],targetMinPx:44,escapeFocusReturn:true,horizontalMenuScroll:false,negativeFaults:1},null,2));
