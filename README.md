# ReStory Guides（维修物语攻略站）

第 5 热词站 · 主词：ReStory: Chill Electronics Repairs（维修物语）
域名：restorygameguides.com ｜ Steam appid 3812600 ｜ 2026-08-06 发售

## 关卡状态
- G0 热词获取 ✅（monitor + docs/20 §8）
- G1 验证 ✅（44/55 主推，docs/20）→ 用户批准
- G2 对标+设计方案 ✅（bench-results-restory.json + sites/restory/DESIGN-PLAN.md）→ 用户批准
- G3 建站 ✅（本目录）
- G4 双视角全维审计 ⏳
- G5 部署 ｜ G6 复盘

## 主题
「秋叶原 2005 维修工坊」——暖纸+木+黄铜+印章三色；工单卡/拍立得/零件盒抽屉/状态印章/五步器；
真交互：今日工单板筛选 / 修复循环勾选清单 / Zen 点数速算器。独立 UI 骨架，禁模板套娃。

## 构建
```bash
cd sites/restory
python3 data/build_content.py   # 内容层 → site.json（10 语 + zh-TW OpenCC + SEO 截断 + 结构校验）
node scripts/generate.js        # site.json → public/
python3 scripts/make_srcset.py  # 配图多档 srcset（首次出图后）
node ../../packages/site-kit/build-webp.js sites/restory
node ../../packages/site-kit/audit.js sites/restory
```

## 内容铁律
- 事实只来自 docs/restory-research.md（L0）；未核实一律标「待补」，禁止编造
- 每页 1-2 个 L0 来源，页面底部渲染来源
- 10 语全量（en/zh-CN/zh-TW/ja/ko/fr/de/es/pt-BR/ru），无混排
- 改内容只动 data/build_content.py 与 data/content_*.py，跑完两条命令，勿手改 site.json

## 里程碑/复盘
- D3/D7/D14：GSC 搜索词 + GA4 概览（领先指标：GA4 organic、Steam 需求信号、AI 引用份额）
