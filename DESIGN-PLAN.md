# ReStory（维修物语）攻略站 · 设计方案（G2 · v1）

> 主词：ReStory: Chill Electronics Repairs（中文：维修物语）｜ Steam appid 3812600 ｜ 2026-08-06 发售
> 验证：docs/20-候选词验证报告-第5站 §8（44/55 ✅ 主推，用户批准进 G2）｜知识库：docs/restory-research.md
> 状态：**G2 设计方案（等用户批准 ⛔）** → 批准后进 G3
> 域名：restorygameguides.com（L0 RDAP 可用；restoryguides.com 已被抢）

---

## 0. 一句话差异化（流量判断）

**主词「restory」处于 Steam 全球热销榜 #9 的上升窗口，但英文 SERP 全是浅层（成就列表/review/tips），中文「维修物语」深表全真空 → 我们做该游戏「最深 + 最全语言」的深表 hub：全设备修复步骤库 + 结局分支路线图 + 成就推荐顺序 + 中文维修物语全量 + 工单板交互。**

### 0.1 对标结论表（数据来源 work/bench-results-restory.json）
| 对手 | 做到 | 没做到 | 我们怎么做 |
|---|---|---|---|
| allthings.how（游戏专站） | 设备清单 / 50 成就全表 / 5 tips | 每台设备拆-查-清-换-装步骤库；结局；中文；交互 | 每台设备独立步骤页 + 工单板筛选 |
| intoindiegames（独立游戏媒体） | 新手机制长文（~2000 词） | 只有新手 1 篇 | 新手页做更结构化（五步循环 + 工具优先级表 + 常见错误 + FAQ） |
| gamerblurb（内容站） | clean / tips 单篇 | 单主题浅文 | 清洁/工具做系统页（优先级 + 进度表） |
| 2UpSkill（内容农场） | crash fix / Steam Deck / multiplayer 模板 | 无游戏特色、模板化 | 同题做但诚实（真实来源 + 澄清块 + 中文） |
| destructoid（大站媒体） | 成就全表 | 无步骤/无推荐顺序 | 成就 roadmap（推荐顺序 + 难度 + 时长 + 隐藏/易漏） |
| truesteamachievements（数据库站） | 50 成就 + 达成率追踪 | 无攻略步骤/无中文 | 可执行 roadmap + 步骤 + 中文，比纯数据库更「能照着做」 |
| pcgameres / TapTap（中文） | 维修物语 介绍页 / demo 评测 | 无任何中文深表 | **中文维修物语全量深表（真空补位）** |
| whisperofthehouse（IRON NEST 深表 hub，参照） | 08-06 上线 08-08 全关卡+4 结局深表 hub | 单语、无交互 | 同款深但更快 + 中文 + 工单板交互 |
| powerpyx（成就头部站，参照） | Roadmap 结构（难度/时长/missable/glitched） | 只做 3A/大作，indie 空白 | Roadmap 结构搬到 ReStory 50 成就 |

---

## 1. 站点主题概念

**「秋叶原 2005 维修工坊」（Akihabara 2005 Repair Workshop）**
- 推导链：游戏气质 = 治愈系经营模拟 + Y2K 复古电子修复 + 2005 东京秋叶原 + 官方授权 Atari → 站点 = 一家「开在网上的维修铺」：工单板、拆解台、零件盒、拍立得顾客档案、状态印章
- 与四站全部不同（禁模板套娃）：Meccha=街机选关路径 ｜ KTS=案件卷宗证据墙 ｜ Doloc=田垄季节切换 ｜ ApproximatelyUp=太空工程蓝图 ｜ **本站=维修工单板 + 拍立得档案 + 零件盒抽屉**
- 目标玩家情绪：治愈、怀旧、想「把东西修好」→ 站点的每一个组件都围绕「接单 → 修好 → 交付」展开

### 1.1 独特组件（≥3，全部 CSS/SVG 原生，无第三方库）
1. **工单卡（Work-order ticket）**——攻略区卡片 = 维修工单横向条卡：工单编号（WO-001）+ 设备图标 + 标题 + 状态印章（待修/维修中/已修好）+ 难度/时长角标。替代方块网格。
2. **拍立得档案（Palaloid card）**——顾客/结局卡 = 拍立得相框（白边 + 手写体标注 + 微旋转 ±1.5°），呼应游戏内 Palaloid 拍立得设备。
3. **零件盒抽屉（Parts-cabinet drawer）**——分类导航/章节折叠 = 木箱抽屉（拉手 + 分隔标签 + 展开动画），呼应拆解台零件盒。
4. **状态印章（Status stamp）**——待修（红）/维修中（黄）/已修好（绿）橡皮章徽章，旋转 2-4° 双色描边，全站状态语义统一。
5. **修复五步进度器（5-step repair stepper）**——拆→查→清→换→装 步骤条，攻略页通用页头组件（当前步骤高亮 + 印章勾选）。

### 1.2 真交互（首页攻略区必须「点了会变」，不是装饰 tab）
1. **今日工单板筛选器**（首页攻略区真交互）：工单卡按设备类型（主机/掌机/手机/相机/其他）+ 难度筛选——点筛选 → JS 过滤工单卡 + 印章弹入动画 + 面板计数更新。i18n 全语言。
2. **设备修复清单勾选器**（checklist，渐进增强）：每台设备页五步循环勾选进度（本地存储）。
3. **Zen 点数速算器**：逸品表点选加总，实时显示距 100 分还差多少。

---

## 2. 视觉语言

> UI 基准：ui-ux-pro-max 检索结论（Retro-Futurism = Y2K 复古科技锚点；Organic Biophilic 的圆润治愈感）→ **覆盖其默认霓虹紫为「暖工坊」调**（游戏是 chill 治愈不是 cyberpunk）；动效原则按 emil-design-eng。

### 2.1 配色（暖工坊 + Y2K 复古，区别于四站全部冷/艳调）
| Token | Light | Dark | 用途 |
|---|---|---|---|
| 纸 Cream `#F3EDDF` | 主背景 | — | 灯下纸张感 |
| 深夜工坊 `#201B14` | — | 主背景 | 深夜营业感 |
| 墨 Ink `#2A241C` | 正文 | 正文 | 暖黑 |
| 木 Wood `#6B4423` / 深木 `#4A2E1B` | 导航/标题底 | 组件底 | 工作台木色 |
| 黄铜 Brass `#C29A3B` | 强调/链接 | 强调 | 工具金属 |
| 修好绿 `#3F7D4F` | 已修好/成功 | 同 | 印章绿 |
| 待修红 `#BF3B2C` | 待修/警示 | 同 | 印章红 |
| 线上青 `#2F6F8F` | 线上单/信息 | 同 | 在线业务 |
| 贴纸黄 `#E0A458` | 贴纸/彩蛋 | 同 | Y2K 点缀 |

### 2.2 字体
- 展示/标题：**Nunito ExtraBold**（EN）+ **M PLUS Rounded 1c 800**（CJK）——圆润治愈 + 日系 Y2K 感
- 正文：Nunito Sans / M PLUS Rounded 1c 400
- 数据/工单编号/标签：**Space Mono**（标签机/工单编号等宽感）
- Google Fonts 加载，CJK 走系统字体回退；对比度 ≥4.5:1

### 2.3 图标语言
- 全部 SVG（Lucide/Heroicons 风格手绘感），设备图标自定义（游戏机/掌机/翻盖手机/拍立得/随身听/电子宠物）
- 状态用印章而非圆点；工具图标（螺丝刀/刷子/气罐/烙铁/碎纸机）为章节图标

### 2.4 动效原则（emil-design-eng）
- 过渡只写具体属性，**禁止 `transition: all`**；150-300ms；进场用 ease-out，反馈用快速 ease-out
- 工单卡 hover：`translateY(-2px)` + 阴影加深（拿起工单感）；`:active` 按压缩放 0.98
- 印章切换：`scale(1.08)→1` 200ms 弹入（盖印章感），transform-origin 从印章中心
- 抽屉展开：height/opacity 过渡 220ms，禁止 width/height 抖动
- 工具图标 hover：轻微旋转 8°（拿起工具感）
- `prefers-reduced-motion` 全部降级为瞬变；键盘 focus-visible 用黄铜色 2px ring

---

## 3. 信息架构 + 页面矩阵（每页 = 1 个搜索意图，核心需求起量优先，不堆长尾）

### 3.1 首页结构（承接主词 restory chill electronics repairs / 维修物语）
hero（游戏名 + 一句话 + 核心数据卡：评价 1828+/50 成就/9 语/官方授权 Atari）→ **今日工单板（攻略区真交互）** → 设备速览（拍立得墙）→ 结局/成就入口 → 全站导航 → FAQ

### 3.2 页面矩阵（P0 首发约 18 页 × 10 语 ≈ 180 URL）
| 优先级 | slug | 承接搜索词 | 类型 |
|---|---|---|---|
| P0 | `/` | restory guide / 维修物语 攻略 | 首页枢纽 |
| P0 | `/beginners-guide` | restory how to play / getting started / 维修物语 新手 | 主攻略（≥1000 词） |
| P0 | `/repair-guide` | restory repair / how to repair devices | 机制深页（五步循环+笔记本） |
| P0 | `/all-devices` | restory every device you can repair | 设备索引（核心差异化入口） |
| P0 | `/tools` | restory tools / screwdriver upgrade | 机制页（工具表+优先级） |
| P0 | `/online-orders` | restory online orders / how to fulfill | 机制页（期限/声誉） |
| P0 | `/licenses` | restory licenses / official partner | 机制页（许可解锁链） |
| P0 | `/achievements` | restory achievements / 维修物语 成就 | 答案页（50 成就全表） |
| P0 | `/achievements-roadmap` | restory achievement guide / 100% | **差异化**：推荐顺序+难度+时长+易漏 |
| P0 | `/hidden-achievements` | restory hidden achievements | 答案页（5 隐藏） |
| P0 | `/zen-points` | restory zen / a place of zen | **差异化**：逸品表+速算器 |
| P0 | `/endings` | restory endings / multiple endings | **差异化**：结局分支路线图 |
| P0 | `/customers` | restory customers / character stories | **差异化**：顾客支线档案（拍立得） |
| P0 | `/economy` | restory how to make money / millionaire | 机制页（翻新转卖/被动收入） |
| P0 | `/steam-deck` | restory steam deck | 答案页 |
| P0 | `/system-requirements` | restory system requirements | 答案页（数据表+FAQ） |
| P0 | `/faq` | restory multiplayer / controller / save | 答案页（FAQ schema） |
| P0 | `/patch-notes` | restory update / patch notes | 追踪页（回访驱动） |

**P1（首发后第一批，核心差异化的第二层）**：设备独立步骤页 `/devices/<slug>`（约 14-15 台：atari-2600 / eggotchi / pokia-3310 / nony-playmachine / autorolla-razor / palaloid / nony-goman / patento-bs / pokia-njoy / nony-pmp / atari-lynx / walkie-talkie / unicorp-99l / robodog / atari-cx40）——每页 = 拆-查-清-换-装 步骤库 + 常见错误 + 清单勾选器。
**P2（数据验证后）**：每顾客支线独立页 / 每结局独立页 / 中文专项页（维修物语 设备/结局/成就）。

### 3.3 页面类型统计
| 类型 | 数量 |
|---|---|
| 首页 | 1 |
| 主攻略/机制深页 | 7 |
| 答案页 | 6 |
| 差异化深表（roadmap/结局/zen/顾客） | 4 |
| **P0 合计** | **18**（×10 语 ≈ 180 URL） |

---

## 4. 语言集

- **Steam 官方 9 语全量**：en / fr / de / es-ES / ja / ko / pt-BR / ru / zh-CN
- + zh-TW（OpenCC 简体→繁体）
- **合计 10 语**（对手全站 0 hreflang → 10 语是我们最大杠杆）
- 优先级：en（核心）+ zh-CN/zh-TW（中文真空）+ ja/ko（东方 Y2K 共鸣）+ es/fr/de/pt-BR/ru（欧洲/拉美量）
- ⚠️ 铁律：全站无混排；改语言后 grep 校验 `lang==="zh"` 硬编码 + curl 验语言纯净（references/pitfalls.md P0 坑）

---

## 5. 内容策略

- 事实只来自 `docs/restory-research.md`（L0：Steam 官方 appdetails + allthings.how + intoindiegames；L2 只用于判断不写入正文）
- 未核实一律标「待补」（每台设备步骤细节/结局触发/隐藏成就/供应商价格），禁止编造（knowledge base §9 清单逐条销项）
- 每页 sources 1-2 个 L0 来源；答案优先 + FAQ schema（答案页必带）
- 标题 ≤60；CJK meta 按宽字符截断（references/pitfalls.md）
- 深度标准（standards.md）：主攻略 ≥1000 词 ≥8 章 + ≥2 富组件；答案页 ≥400 词 + FAQ + 澄清块（如「bug 成就当前 100% 不可达」）；机制页 ≥600 词 + 步骤拆解 + 常见错误
- 周更保鲜：patch-notes + update-log 每周至少 1 次真实更新
- 站内搜索：header 轻量 Google `site:` 搜索框（零后端，对齐头部站逻辑）

---

## 6. 配图清单（Seedream）

- **统一风格 prompt 模板**：`温暖灯光下的复古维修工作台，秋叶原 2005 氛围，Y2K 电子设备，cozy 治愈，柔和暖调，胶片颗粒，16:9`
- hero：维修工坊工作台 + 秋叶原街景 1 张
- 设备页：每台设备「拍立得特写」风格 1 张（P1 14-15 台）
- 页面插图：成就/结局/经济/新手各 1 张主题图
- 比例 16:9 三档 srcset（WebP/AVIF）；懒加载 + 预留尺寸防 CLS

---

## 7. 执行顺序

1. G3 建站：theme 重写 style.css（暖工坊调）+ generate.js 适配（工单卡/拍立得/抽屉/印章/五步器）→ 首页工单板筛选真交互 + 3 个交互工具
2. P0 18 页内容从知识库产出（L0 来源逐页标注）→ 10 语全量
3. G4 双视角全维审计（工单板交互 headless 实测 + 语言纯净 + SEO schema）→ 达标
4. G5 部署：GitHub → Cloudflare Pages → restorygameguides.com → GSC + GA4（独立媒体资源）
5. G6 复盘：D3/D7/D14 三查；Steam 需求信号持续采集（关注者曲线浏览器补）

---

## 8. 流量判断（为什么这个设计能起量）

1. **踩在趋势上**：Steam 全球热销榜实时 #9（L0）+ 评价 609/天（L0）+ 发售 D+3 上升窗口 → 搜索需求正在形成，不是赌冷门
2. **需求强度**：Simulation + 叙事多结局 + 50 成就 = 强「查表/教程」需求（玩家要查怎么修、怎么解锁、怎么拿成就）；750K 愿望单 + 15K 同时在线 [L2 多源] = 玩家底座大
3. **可切入**：英文 SERP 全浅层（无人做步骤库/结局/roadmap）+ **中文维修物语全真空** → 我们做最深 + 唯一中文深表，窗口干净
4. **多语言杠杆**：10 语 vs 对手 0 hreflang → 西/德/法/葡/俄/日/韩全吃
5. **交互留存**：工单板筛选 + 清单勾选 + Zen 速算器 → 停留/回访/分享，不只是静态页
6. **形态已验证**：whisperofthehouse（IRON NEST）08-06→08-08 证明「新游深表 hub」能 2 天起量（L0），我们做同款但更快 + 中文 + 交互

---

## 9. 变现（对齐产线体系）

- 联盟：Steam 无官方联盟 → Fanatical / GamersGate 查货（首发期大概率有），有货再埋
- 广告：Adsterra 待接（有流量后），AdSense 押后；ads.txt + 隐私/免责合规页随站内置
- 不做任何站内虚假下载/破解诱导（红线，见 monetization.md）

---

## 10. 批准点

**请用户确认 ⛔**：批准本设计方案（主题「秋叶原 2005 维修工坊」+ 18 页 P0 矩阵 + 10 语 + 工单板交互）→ 批准后进 G3 建站。
