# -*- coding: utf-8 -*-
"""ReStory 配图生成：Seedream 文生图，秋叶原 2005 暖工坊统一风格，16:9 高清."""
import os, re, json, time, urllib.request, base64, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets" / "images"
ASSETS.mkdir(parents=True, exist_ok=True)

env = open("/Users/azu/Documents/跨境电商AI系统/.env", encoding="utf-8").read()
m = re.search(r"^ARK_API_KEY=(.+)$", env, re.M)
if not m:
    sys.exit("ARK_API_KEY not found")
API_KEY = m.group(1).strip().strip('"').strip("'").strip()

ENDPOINT = "https://ark.cn-beijing.volces.com/api/v3/images/generations"
MODEL_PRO = "doubao-seedream-5-0-pro-260628"
MODEL_LITE = "doubao-seedream-5-0-lite-260128"

# 暖工坊统一风格：Y2K 秋叶原 2005 电子维修铺，温暖治愈
STYLE = ("warm cozy electronics repair shop scene in Akihabara Tokyo 2005, Y2K retro devices on a wooden "
         "workbench, warm lamp light, nostalgic mid-2000s Japanese urban vibe, soft film grain, "
         "cinematic composition, high detail, no text, no watermark, no logos, 16:9 widescreen")

PROMPTS = {
  "hero": "A cozy electronics repair shop counter in Akihabara 2005 at dusk, shelves of retro Y2K devices, warm tungsten lamps, a customer handing a handheld console to the shop owner, nostalgic anime-free realistic illustration, " + STYLE,
  "beginners-guide": "A first-day repair: a young shop owner opening a retro handheld console with a screwdriver on a wooden workbench, parts neatly laid out, warm lamp light, " + STYLE,
  "repair-guide": "Close-up of a repair in progress: a disassembled retro console, screwdriver, brush and spare parts on a wooden workbench, notebook beside it, warm light, " + STYLE,
  "all-devices": "A shelf full of nostalgic Y2K devices: retro game consoles, flip phones, a Tamagotchi-like pet, a instant camera, a handheld player, warm shop lighting, " + STYLE,
  "tools": "A row of repair tools on a wooden pegboard: screwdriver, brush, compressed air can, small shredder, tip jar, sonic cleaning bath, warm workshop light, " + STYLE,
  "online-orders": "A retro CRT computer on a wooden desk showing a mail-order repair form, boxes of shipped devices stacked nearby, Akihabara 2005 shop, warm light, " + STYLE,
  "licenses": "A framed official repair license certificate hanging on a shop wall beside retro device posters, warm lamp glow, " + STYLE,
  "achievements": "A wall of framed achievement badges and stickers in a cozy repair shop, a shop owner looking proudly, warm light, " + STYLE,
  "achievements-roadmap": "A planning board in a repair shop with sticky notes and a checklist pinned to cork, retro tools around, warm lamp, " + STYLE,
  "hidden-achievements": "A mysterious locked drawer in a repair shop, soft warm light spilling from it, retro devices around, slightly mysterious mood, " + STYLE,
  "zen-points": "A shelf of small zen knick-knacks: daruma, maneki-neko, bonsai, a small Buddha lamp, cozy corner of a repair shop, warm light, " + STYLE,
  "endings": "A branching hallway in the back of an Akihabara 2005 repair shop with two doors glowing warmly, nostalgic atmosphere, " + STYLE,
  "customers": "A shop owner talking with a customer over a repaired retro camera at the counter, warm friendly light, nostalgic 2005 Tokyo, " + STYLE,
  "economy": "A cash drawer full of yen notes at a retro repair shop counter, a tip jar and a small shredder beside it, warm light, " + STYLE,
  "steam-deck": "A retro handheld console lying on a repair bench next to a modern portable PC-like device, warm workshop light, " + STYLE,
  "system-requirements": "A retro computer with a spec sheet on screen at a repair shop desk, wooden desk, warm lamp light, " + STYLE,
  "faq": "A cozy repair shop counter with a question sign, retro devices around, warm welcoming light, " + STYLE,
  "patch-notes": "A clipboard with update notes pinned on a corkboard in a repair shop, retro tools and warm light, " + STYLE,
  "guides": "An open repair manual on a wooden workbench with diagrams, screwdriver and parts, warm lamp light, " + STYLE,
}

def call(prompt, model=MODEL_PRO, retries=3):
    body = json.dumps({"model": model, "prompt": prompt, "size": "1600x900",
                       "response_format": "url", "watermark": False}).encode()
    for i in range(retries):
        try:
            req = urllib.request.Request(ENDPOINT, data=body, method="POST", headers={
                "Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=180) as r:
                data = json.loads(r.read().decode())
            items = data.get("data") or []
            if items:
                return items[0].get("url") or (items[0].get("b64_json") and "data:"+items[0]["b64_json"])
        except Exception as e:
            print(f"  attempt {i+1} failed: {e}")
            time.sleep(8 * (i + 1))
    return None

def download(url, dest):
    if url.startswith("data:"):
        b64 = url.split(",", 1)[1]
        Path(dest).write_bytes(base64.b64decode(b64))
        return True
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=180) as r:
        Path(dest).write_bytes(r.read())
    return True

def main():
    todo = dict(PROMPTS)
    done = []
    for name, prompt in todo.items():
        dest = ASSETS / f"{name}.jpg"
        if dest.exists() and dest.stat().st_size > 20000:
            print(f"skip {name} (exists)")
            done.append(name)
            continue
        print(f"generating {name} ...", flush=True)
        url = call(prompt)
        if not url:
            print(f"  FAILED {name}, trying lite model")
            url = call(prompt, model=MODEL_LITE)
        if url:
            download(url, dest)
            print(f"  OK {name} -> {dest.stat().st_size} bytes", flush=True)
            done.append(name)
        else:
            print(f"  FAILED {name}")
        time.sleep(2)
    print(f"\nDone: {len(done)}/{len(todo)} images")

if __name__ == "__main__":
    main()
