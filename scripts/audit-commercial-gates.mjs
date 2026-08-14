#!/usr/bin/env node
import assert from "node:assert/strict";
import crypto from "node:crypto";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const generator = path.join(root, "scripts", "generate.js");
const baselineSha = "c239cad3bc9980ae66678e6ed843dfd72faf887f";
const publisher = "pub-4174270222899193";
const client = `ca-${publisher}`;
const temp = fs.mkdtempSync(path.join(os.tmpdir(), "restory-commercial-"));
const out = path.join(temp, "candidate-public");
const baselineRoot = path.join(temp, "baseline");

const count = (text, needle) => text.split(needle).length - 1;
const filesUnder = dir => fs.readdirSync(dir, { withFileTypes: true }).flatMap(entry => {
  const file = path.join(dir, entry.name);
  return entry.isDirectory() ? filesUnder(file) : [file];
}).sort();
const htmlRows = dir => filesUnder(dir).filter(file => file.endsWith(".html")).map(file => ({
  relative: path.relative(dir, file).split(path.sep).join("/"), html: fs.readFileSync(file, "utf8"),
}));
const treeHash = dir => {
  const hash = crypto.createHash("sha256");
  for (const file of filesUnder(dir)) {
    hash.update(path.relative(dir, file)); hash.update("\0"); hash.update(fs.readFileSync(file)); hash.update("\0");
  }
  return hash.digest("hex");
};
const run = (command, args, options = {}) => {
  const result = spawnSync(command, args, { encoding: "utf8", ...options });
  assert.equal(result.status, 0, result.stderr || result.stdout || `${command} failed`);
  return result.stdout.trim();
};
const buildCandidate = fixture => {
  const env = { ...process.env, TZ: "UTC", RESTORY_OUTPUT_DIR: out, RESTORY_LASTMOD_PATH: path.join(temp, "candidate-lastmod.json") };
  delete env.NODE_ENV; delete env.RESTORY_ADSENSE_FIXTURE;
  if (fixture) { env.NODE_ENV = "test"; env.RESTORY_ADSENSE_FIXTURE = "enabled"; }
  return run(process.execPath, [generator], { cwd: root, env });
};
const normalizeConfig = file => {
  const data = JSON.parse(fs.readFileSync(file, "utf8"));
  delete data.site.adsenseServing;
  return data;
};
const normalizeHtml = (relative, html) => {
  let value = html
    .replace(/<script async src="https:\/\/pagead2\.googlesyndication\.com\/pagead\/js\/adsbygoogle\.js\?client=[^"]+" crossorigin="anonymous"><\/script>/g, "")
    .replace(/<meta name="google-adsense-account" content="ca-pub-4174270222899193" \/>/g, "")
    .replace(/<div class="amazon-gear">[\s\S]*?<p class="aff-note">[\s\S]*?<\/p>\s*<\/div>/g, "");
  if (relative.endsWith("privacy.html")) {
    value = value.replace(/(<div class="page-hero reveal">[\s\S]*?<\/div>)[\s\S]*?(<\/article>)/, "$1[COMMERCIAL_PRIVACY_NOTICE]$2");
    value = value.replace(/<meta name="description" content="[^"]*">/, '<meta name="description" content="[COMMERCIAL_PRIVACY_META]">');
    value = value.replace(/<meta property="og:description" content="[^"]*">/, '<meta property="og:description" content="[COMMERCIAL_PRIVACY_META]">');
  }
  return value.replace(/\s+/g, " ").trim();
};

const gate = { enabled: false, providerReady: false, certifiedCmpReady: false };
for (const file of [path.join(root, "data/site.base.json"), path.join(root, "data/site.json")]) {
  const site = JSON.parse(fs.readFileSync(file, "utf8")).site;
  assert.equal(site.adsenseId, publisher, `${path.basename(file)} publisher must remain raw pub-`);
  assert.deepEqual(site.adsenseServing, gate, `${path.basename(file)} production gates must default false`);
}

const privacyMarkers = {
  "privacy.html": "does not mean AdSense ads are currently serving",
  "zh-CN/privacy.html": "不代表 AdSense 广告目前正在投放",
  "zh-TW/privacy.html": "不代表 AdSense 廣告目前正在投放",
  "ja/privacy.html": "現在 AdSense 広告が配信中であることを意味しません",
  "ko/privacy.html": "현재 AdSense 광고가 게재 중이라는 뜻은 아닙니다",
  "fr/privacy.html": "ne signifie pas que des annonces AdSense sont actuellement diffusées",
  "de/privacy.html": "bedeutet nicht, dass derzeit AdSense-Anzeigen ausgeliefert werden",
  "es/privacy.html": "no significa que los anuncios de AdSense se estén publicando ahora",
  "pt-BR/privacy.html": "não significa que anúncios do AdSense estejam sendo veiculados agora",
  "ru/privacy.html": "не означает, что реклама AdSense сейчас показывается",
};
const assertCandidate = fixture => {
  const rows = htmlRows(out);
  assert.equal(rows.length, 371, "HTML route count changed");
  assert.equal(count(fs.readFileSync(path.join(out, "sitemap.xml"), "utf8"), "<loc>"), 220, "sitemap route count changed");
  let adsterra = 0;
  for (const { relative, html } of rows) {
    assert.equal(count(html, `<meta name="google-adsense-account" content="${client}" />`), 1, `account meta count changed in ${relative}`);
    assert.equal(count(html, "pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"), fixture ? 1 : 0, `serving count changed in ${relative}`);
    assert.equal(html.includes("client=pub-"), false, `raw pub leaked as client in ${relative}`);
    assert.equal(html.includes("client=ca-ca-pub-"), false, `double ca prefix in ${relative}`);
    if (fixture) assert.equal(count(html, `client=${client}`), 1, `fixture client mismatch in ${relative}`);
    assert.equal(html.includes('class="amazon-gear"'), false, `Amazon module remains in ${relative}`);
    assert.equal(html.includes("cozysimhub20-20"), false, `Amazon tag remains in ${relative}`);
    assert.equal(/https:\/\/(?:www\.)?amazon\.[^\s"'<]+/i.test(html), false, `Amazon URL remains in ${relative}`);
    adsterra += count(html, "pl30767301.effectivecpmnetwork.com");
  }
  assert.equal(adsterra, 371, "Adsterra coverage changed");
  for (const [relative, marker] of Object.entries(privacyMarkers)) {
    const html = rows.find(row => row.relative === relative)?.html || "";
    assert(html.includes(marker), `gated AdSense status missing in ${relative}`);
    assert(html.includes("effectivecpmnetwork.com"), `Adsterra disclosure missing in ${relative}`);
  }
  assert.equal(fs.readFileSync(path.join(out, "ads.txt"), "utf8"),
    `google.com, ${publisher}, DIRECT, f08c47fec0942fa0\n`, "ads.txt raw publisher record changed");
  return rows;
};

try {
  fs.mkdirSync(baselineRoot, { recursive: true });
  const archive = path.join(temp, "baseline.tar");
  run("git", ["archive", "--format=tar", `--output=${archive}`, baselineSha], { cwd: root });
  run("tar", ["-xf", archive, "-C", baselineRoot]);
  run("python3", ["data/build_content.py"], { cwd: baselineRoot, env: { ...process.env, TZ: "UTC" } });
  run(process.execPath, ["scripts/generate.js"], { cwd: baselineRoot, env: { ...process.env, TZ: "UTC" } });

  const build1 = buildCandidate(false); const defaultRows = assertCandidate(false); const defaultHash = treeHash(out);
  const build2 = buildCandidate(false); assertCandidate(false); assert.equal(treeHash(out), defaultHash, "default builds differ");
  const fixture1 = buildCandidate(true); assertCandidate(true); const fixtureHash = treeHash(out);
  const fixture2 = buildCandidate(true); assertCandidate(true); assert.equal(treeHash(out), fixtureHash, "fixture builds differ");
  buildCandidate(false); assertCandidate(false); assert.equal(treeHash(out), defaultHash, "fixture round-trip changed default output");

  assert.deepEqual(normalizeConfig(path.join(root, "data/site.json")), normalizeConfig(path.join(baselineRoot, "data/site.json")),
    "editorial/factual site data changed outside the AdSense gate");
  const baselineRows = new Map(htmlRows(path.join(baselineRoot, "public")).map(row => [row.relative, row.html]));
  for (const row of defaultRows) {
    assert.equal(normalizeHtml(row.relative, row.html), normalizeHtml(row.relative, baselineRows.get(row.relative) || ""),
      `non-commercial generated output changed in ${row.relative}`);
  }
  for (const file of ["sitemap.xml", "robots.txt", "llms.txt"]) {
    assert.equal(fs.readFileSync(path.join(out, file), "utf8"), fs.readFileSync(path.join(baselineRoot, "public", file), "utf8"), `${file} changed`);
  }
  console.log(JSON.stringify({ status: "pass", locales: 10, htmlPages: 371, indexablePages: 220,
    defaultServingScripts: 0, fixtureScriptsPerPage: 1, amazonModules: 0, amazonTagUrls: 0,
    adsterraProviderPages: 371, commercialOnlyGeneratedDiff: true,
    defaultTreeSha256: defaultHash, fixtureTreeSha256: fixtureHash,
    builds: [build1, build2, fixture1, fixture2] }, null, 2));
} finally {
  fs.rmSync(temp, { recursive: true, force: true });
}
