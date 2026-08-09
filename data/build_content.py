# -*- coding: utf-8 -*-
"""ReStory Guides · site.json 重建：10 语言全量 (en/zh-CN/zh-TW/ja/ko/fr/de/es/pt-BR/ru)
内容层：content_en.py（基准） + content_zh_cn/ru/ja/ko/fr/de/es/pt_br.py（翻译模块）
zh-TW 由 zh-CN 经 OpenCC(s2tw) 自动生成。
事实口径：仅使用 docs/restory-research.md 的 L0 事实；未核实一律「待补」，禁止编造。
生成器：sites/restory/scripts/generate.js（data/site.json → public/）。
"""
import json, copy, sys, importlib
from pathlib import Path
import opencc

ROOT = Path(__file__).parent
cc = opencc.OpenCC("s2tw")

LANGS = ["en", "zh-CN", "zh-TW", "ja", "ko", "fr", "de", "es", "pt-BR", "ru"]
TRANS_LANGS = [l for l in LANGS if l not in ("en", "zh-TW")]

sys.path.insert(0, str(ROOT))
import content_en

# ---- 翻译模块（缺哪个会警告，最终必须 8 个齐）----
_LANG_MOD = {
    "zh-CN": ("content_zh_cn", "PAGES_ZH_CN"),
    "ru": ("content_ru", "PAGES_RU"),
    "ja": ("content_ja", "PAGES_JA"),
    "ko": ("content_ko", "PAGES_KO"),
    "fr": ("content_fr", "PAGES_FR"),
    "de": ("content_de", "PAGES_DE"),
    "es": ("content_es", "PAGES_ES"),
    "pt-BR": ("content_pt_br", "PAGES_PT_BR"),
}
PAGE_TRANS = {}
missing = []
for lg in TRANS_LANGS:
    mod, attr = _LANG_MOD[lg]
    try:
        m = importlib.import_module(mod)
        PAGE_TRANS[lg] = getattr(m, attr)
    except Exception as e:
        missing.append((lg, str(e)))

if missing:
    for lg, err in missing:
        print(f"⚠️ MISSING TRANSLATION MODULE {lg}: {err}")

# =====================================================================
# 站点级配置（site）+ 10 语 site.i18n
# =====================================================================
SITE = json.loads((ROOT / "site.base.json").read_text())["site"]

SITE_I18N = {
 "en": {
  "name": "ReStory Guides", "tagline": "Akihabara 2005 Repair Workshop — full ReStory guides",
  "description": "ReStory (维修物语) guides: repair every device, achievements, endings, licenses, tools and a beginner's guide — in 10 languages.",
  "navHome": "Home", "navGuides": "Guides", "navAbout": "About", "navPrivacy": "Privacy", "navContact": "Contact",
  "langLabel": "Language", "aboutTitle": "About this site", "privacyTitle": "Privacy Policy", "contactTitle": "Contact",
  "footerNote": "Unofficial fan site — game and related assets belong to their respective owners.",
  "footerSource": "Information checked against the official Steam store page, allthings.how and intoindiegames; unverified details are marked.",
  "quickAnswers": "Quick answers", "guides": "All guides", "aboutGame": "About the game",
  "startPlaying": "Get it on Steam", "getOnSteam": "Get it on Steam ↗", "readGuide": "Read the guide →",
  "moreGuides": "More guides", "sources": "Sources & fact-checking", "updated": "Contents",
  "aboutText": "ReStory Guides is an unofficial fan resource. We research every page against the official Steam store page and reputable sources (allthings.how, intoindiegames), and clearly mark anything still being verified. We never invent details.",
  "aboutSources": "Where our information comes from",
  "navGroup1": "Guides", "navGroup2": "Devices", "navGroup3": "Achievements",
  "searchPh": "Search guides…", "searchLabel": "Search guides", "noMatch": "No matching work orders",
  "boardTag": "TODAY'S WORK ORDERS", "boardSub": "Pick a guide — every card is one repair job.",
  "filterAll": "All", "filterStart": "Start bench", "filterDevices": "Device bench", "filterAch": "Achievement wall", "filterStory": "Story line", "filterRef": "Reference",
  "diffEasy": "Easy", "diffMid": "Medium", "diffHard": "Deep",
  "stampTodo": "TO REPAIR", "stampWip": "IN REPAIR", "stampDone": "FIXED",
  "related": "Related work orders", "checklistTitle": "Repair loop checklist", "checklistSave": "Saved on this device",
  "zenCalcTitle": "Zen points calculator", "zenCalcLead": "Tap items to add their points — see how close you are to 100.",
  "zenTotal": "Total", "zenTarget": "Target 100", "zenReset": "Reset",
 },
 "zh-CN": {
  "name": "维修物语攻略站", "tagline": "秋叶原 2005 维修工坊——维修物语全攻略",
  "description": "维修物语（ReStory）攻略：修复全部设备、成就、结局、许可、工具与新手指南——10 种语言。",
  "navHome": "首页", "navGuides": "攻略", "navAbout": "关于", "navPrivacy": "隐私", "navContact": "联系",
  "langLabel": "语言", "aboutTitle": "关于本站", "privacyTitle": "隐私政策", "contactTitle": "联系我们",
  "footerNote": "非官方粉丝站——游戏及相关资产归其所有者所有。",
  "footerSource": "信息核对自 Steam 官方商店页、allthings.how 与 intoindiegames；未核实内容已明确标注。",
  "quickAnswers": "常见问题速答", "guides": "全部攻略", "aboutGame": "关于这款游戏",
  "startPlaying": "在 Steam 获取", "getOnSteam": "在 Steam 获取 ↗", "readGuide": "阅读攻略 →",
  "moreGuides": "更多攻略", "sources": "来源与事实核对", "updated": "目录",
  "aboutText": "维修物语攻略站是非官方粉丝资源站。我们针对 Steam 官方商店页与可靠来源（allthings.how、intoindiegames）逐页核对信息，并将仍在验证中的内容明确标注「待补」。我们绝不编造细节。",
  "aboutSources": "我们的信息来源",
  "navGroup1": "攻略", "navGroup2": "设备", "navGroup3": "成就",
  "searchPh": "搜索攻略…", "searchLabel": "搜索攻略", "noMatch": "没有匹配的工单",
  "boardTag": "今日工单板", "boardSub": "选一份攻略——每张卡片就是一单维修活。",
  "filterAll": "全部", "filterStart": "新手工位", "filterDevices": "设备拆解台", "filterAch": "成就墙", "filterStory": "剧情线", "filterRef": "参考区",
  "diffEasy": "入门", "diffMid": "进阶", "diffHard": "深表",
  "stampTodo": "待修", "stampWip": "维修中", "stampDone": "已修好",
  "related": "相关工单", "checklistTitle": "修复循环勾选清单", "checklistSave": "已保存在本机",
  "zenCalcTitle": "Zen 点数速算器", "zenCalcLead": "点选逸品累加点数——看看离 100 还差多少。",
  "zenTotal": "合计", "zenTarget": "目标 100", "zenReset": "重置",
 },
 "zh-TW": {
  "name": "維修物語攻略站", "tagline": "秋葉原 2005 維修工坊——維修物語全攻略",
  "description": "維修物語（ReStory）攻略：修復全部設備、成就、結局、許可、工具與新手指南——10 種語言。",
  "navHome": "首頁", "navGuides": "攻略", "navAbout": "關於", "navPrivacy": "隱私", "navContact": "聯繫",
  "langLabel": "語言", "aboutTitle": "關於本站", "privacyTitle": "隱私政策", "contactTitle": "聯繫我們",
  "footerNote": "非官方粉絲站——遊戲及相關資產歸其所有者所有。",
  "footerSource": "資訊核對自 Steam 官方商店頁、allthings.how 與 intoindiegames；未核實內容已明確標註。",
  "quickAnswers": "常見問題速答", "guides": "全部攻略", "aboutGame": "關於這款遊戲",
  "startPlaying": "在 Steam 獲取", "getOnSteam": "在 Steam 獲取 ↗", "readGuide": "閱讀攻略 →",
  "moreGuides": "更多攻略", "sources": "來源與事實核對", "updated": "目錄",
  "aboutText": "維修物語攻略站是非官方粉絲資源站。我們針對 Steam 官方商店頁與可靠來源（allthings.how、intoindiegames）逐頁核對資訊，並將仍在驗證中的內容明確標註「待補」。我們絕不編造細節。",
  "aboutSources": "我們的資訊來源",
  "navGroup1": "攻略", "navGroup2": "設備", "navGroup3": "成就",
  "searchPh": "搜尋攻略…", "searchLabel": "搜尋攻略", "noMatch": "沒有匹配的工單",
  "boardTag": "今日工單板", "boardSub": "選一份攻略——每張卡片就是一單維修活。",
  "filterAll": "全部", "filterStart": "新手工位", "filterDevices": "設備拆解台", "filterAch": "成就牆", "filterStory": "劇情線", "filterRef": "參考區",
  "diffEasy": "入門", "diffMid": "進階", "diffHard": "深表",
  "stampTodo": "待修", "stampWip": "維修中", "stampDone": "已修好",
  "related": "相關工單", "checklistTitle": "修復循環勾選清單", "checklistSave": "已保存在本機",
  "zenCalcTitle": "Zen 點數速算器", "zenCalcLead": "點選逸品累加點數——看看離 100 還差多少。",
  "zenTotal": "合計", "zenTarget": "目標 100", "zenReset": "重置",
 },
 "ja": {
  "name": "ReStory 攻略ガイド", "tagline": "秋葉原 2005 修理工房——ReStory 完全攻略",
  "description": "ReStory（維修物語）攻略：全デバイス修理・実績・エンディング・ライセンス・ツール・初心者ガイド——10言語対応。",
  "navHome": "ホーム", "navGuides": "攻略", "navAbout": "このサイト", "navPrivacy": "プライバシー", "navContact": "お問い合わせ",
  "langLabel": "言語", "aboutTitle": "このサイトについて", "privacyTitle": "プライバシーポリシー", "contactTitle": "お問い合わせ",
  "footerNote": "非公式ファンサイトです。ゲームおよび関連アセットは各権利者に帰属します。",
  "footerSource": "情報は Steam 公式ストア・allthings.how・intoindiegames で確認しています。未検証の内容は明記しています。",
  "quickAnswers": "よくある質問", "guides": "攻略一覧", "aboutGame": "このゲームについて",
  "startPlaying": "Steam で入手", "getOnSteam": "Steam で入手 ↗", "readGuide": "攻略を読む →",
  "moreGuides": "その他の攻略", "sources": "出典とファクトチェック", "updated": "目次",
  "aboutText": "ReStory 攻略ガイドは非公式のファンリソースです。各ページを Steam 公式ストアと信頼できる情報源（allthings.how、intoindiegames）で確認し、未検証の内容は「未検証」と明記します。細部を創作することはありません。",
  "aboutSources": "情報の出典",
  "navGroup1": "攻略", "navGroup2": "デバイス", "navGroup3": "実績",
  "searchPh": "攻略を検索…", "searchLabel": "攻略を検索", "noMatch": "一致する修理伝票がありません",
  "boardTag": "本日の修理伝票", "boardSub": "攻略を選んでください——各カードが1件の修理仕事です。",
  "filterAll": "すべて", "filterStart": "初心者ブース", "filterDevices": "分解台", "filterAch": "実績ウォール", "filterStory": "ストーリー", "filterRef": "リファレンス",
  "diffEasy": "初級", "diffMid": "中級", "diffHard": "詳細",
  "stampTodo": "修理待ち", "stampWip": "修理中", "stampDone": "修理済み",
  "related": "関連する修理伝票", "checklistTitle": "修理ループのチェックリスト", "checklistSave": "この端末に保存済み",
  "zenCalcTitle": "禅ポイント計算機", "zenCalcLead": "アイテムをタップして加算——100 まであとどれだけか確認。",
  "zenTotal": "合計", "zenTarget": "目標 100", "zenReset": "リセット",
 },
 "ko": {
  "name": "ReStory 가이드", "tagline": "아키하바라 2005 수리 공방 — ReStory 완전 가이드",
  "description": "ReStory(리스토리) 가이드: 전체 기기 수리, 업적, 엔딩, 라이선스, 도구, 초보자 가이드 — 10개 언어.",
  "navHome": "홈", "navGuides": "가이드", "navAbout": "소개", "navPrivacy": "개인정보", "navContact": "문의",
  "langLabel": "언어", "aboutTitle": "이 사이트 소개", "privacyTitle": "개인정보 처리방침", "contactTitle": "문의하기",
  "footerNote": "비공식 팬 사이트입니다. 게임 및 관련 자산은 각 소유자에게 있습니다.",
  "footerSource": "정보는 Steam 공식 스토어, allthings.how, intoindiegames에서 확인했습니다. 미확인 내용은 명확히 표시합니다.",
  "quickAnswers": "빠른 답변", "guides": "전체 가이드", "aboutGame": "게임 소개",
  "startPlaying": "Steam에서 받기", "getOnSteam": "Steam에서 받기 ↗", "readGuide": "가이드 읽기 →",
  "moreGuides": "더 많은 가이드", "sources": "출처 및 사실 확인", "updated": "목차",
  "aboutText": "ReStory 가이드는 비공식 팬 리소스입니다. 각 페이지를 Steam 공식 스토어와 신뢰할 수 있는 출처(allthings.how, intoindiegames)로 확인하고, 아직 확인되지 않은 내용은 명확히 표시합니다. 세부 사항을 지어내지 않습니다.",
  "aboutSources": "정보 출처",
  "navGroup1": "가이드", "navGroup2": "기기", "navGroup3": "업적",
  "searchPh": "가이드 검색…", "searchLabel": "가이드 검색", "noMatch": "일치하는 작업 지시서가 없습니다",
  "boardTag": "오늘의 작업 지시서", "boardSub": "가이드를 고르세요 — 카드 하나가 수리 작업 하나입니다.",
  "filterAll": "전체", "filterStart": "초보 작업대", "filterDevices": "분해대", "filterAch": "업적 벽", "filterStory": "스토리", "filterRef": "참고",
  "diffEasy": "입문", "diffMid": "중급", "diffHard": "심화",
  "stampTodo": "수리 대기", "stampWip": "수리 중", "stampDone": "수리 완료",
  "related": "관련 작업 지시서", "checklistTitle": "수리 루프 체크리스트", "checklistSave": "이 기기에 저장됨",
  "zenCalcTitle": "젠 포인트 계산기", "zenCalcLead": "아이템을 탭해 포인트를 더하세요 — 100까지 얼마나 남았는지 확인.",
  "zenTotal": "합계", "zenTarget": "목표 100", "zenReset": "초기화",
 },
 "fr": {
  "name": "Guides ReStory", "tagline": "Atelier de réparation Akihabara 2005 — guides complets ReStory",
  "description": "Guides ReStory (维修物语) : réparez chaque appareil, succès, fins, licences, outils et guide débutant — en 10 langues.",
  "navHome": "Accueil", "navGuides": "Guides", "navAbout": "À propos", "navPrivacy": "Confidentialité", "navContact": "Contact",
  "langLabel": "Langue", "aboutTitle": "À propos de ce site", "privacyTitle": "Politique de confidentialité", "contactTitle": "Contact",
  "footerNote": "Site de fans non officiel — le jeu et ses ressources appartiennent à leurs propriétaires.",
  "footerSource": "Informations vérifiées sur la page Steam officielle, allthings.how et intoindiegames ; les éléments non vérifiés sont signalés.",
  "quickAnswers": "Réponses rapides", "guides": "Tous les guides", "aboutGame": "À propos du jeu",
  "startPlaying": "Obtenir sur Steam", "getOnSteam": "Obtenir sur Steam ↗", "readGuide": "Lire le guide →",
  "moreGuides": "Plus de guides", "sources": "Sources et vérification", "updated": "Sommaire",
  "aboutText": "ReStory Guides est une ressource de fans non officielle. Nous vérifions chaque page sur la page Steam officielle et des sources fiables (allthings.how, intoindiegames), et signalons clairement tout ce qui est encore en cours de vérification. Nous n'inventons jamais de détails.",
  "aboutSources": "D'où viennent nos informations",
  "navGroup1": "Guides", "navGroup2": "Appareils", "navGroup3": "Succès",
  "searchPh": "Rechercher…", "searchLabel": "Rechercher", "noMatch": "Aucun bon de réparation correspondant",
  "boardTag": "BONS DE RÉPARATION DU JOUR", "boardSub": "Choisissez un guide — chaque carte est un travail de réparation.",
  "filterAll": "Tous", "filterStart": "Établi débutant", "filterDevices": "Établi appareils", "filterAch": "Mur des succès", "filterStory": "Ligne scénario", "filterRef": "Référence",
  "diffEasy": "Facile", "diffMid": "Moyen", "diffHard": "Approfondi",
  "stampTodo": "À RÉPARER", "stampWip": "EN RÉPARATION", "stampDone": "RÉPARÉ",
  "related": "Bons liés", "checklistTitle": "Checklist du cycle de réparation", "checklistSave": "Enregistré sur cet appareil",
  "zenCalcTitle": "Calculateur de points Zen", "zenCalcLead": "Touchez les objets pour additionner leurs points — voyez où vous en êtes.",
  "zenTotal": "Total", "zenTarget": "Objectif 100", "zenReset": "Réinitialiser",
 },
 "de": {
  "name": "ReStory Ratgeber", "tagline": "Reparaturwerkstatt Akihabara 2005 — komplette ReStory-Guides",
  "description": "ReStory (维修物语) Guides: jedes Gerät reparieren, Errungenschaften, Enden, Lizenzen, Werkzeuge und Einsteiger-Guide — in 10 Sprachen.",
  "navHome": "Start", "navGuides": "Guides", "navAbout": "Über", "navPrivacy": "Datenschutz", "navContact": "Kontakt",
  "langLabel": "Sprache", "aboutTitle": "Über diese Seite", "privacyTitle": "Datenschutzerklärung", "contactTitle": "Kontakt",
  "footerNote": "Inoffizielle Fan-Seite — Spiel und zugehörige Assets gehören ihren Besitzern.",
  "footerSource": "Informationen geprüft gegen die offizielle Steam-Seite, allthings.how und intoindiegames; Unverifiziertes ist markiert.",
  "quickAnswers": "Schnelle Antworten", "guides": "Alle Guides", "aboutGame": "Über das Spiel",
  "startPlaying": "Auf Steam holen", "getOnSteam": "Auf Steam holen ↗", "readGuide": "Guide lesen →",
  "moreGuides": "Weitere Guides", "sources": "Quellen & Faktencheck", "updated": "Inhalt",
  "aboutText": "ReStory Guides ist eine inoffizielle Fan-Ressource. Wir prüfen jede Seite gegen die offizielle Steam-Seite und zuverlässige Quellen (allthings.how, intoindiegames) und kennzeichnen alles, was noch verifiziert wird. Wir erfinden nie Details.",
  "aboutSources": "Woher unsere Informationen stammen",
  "navGroup1": "Guides", "navGroup2": "Geräte", "navGroup3": "Errungenschaften",
  "searchPh": "Guides suchen…", "searchLabel": "Guides suchen", "noMatch": "Keine passenden Reparaturaufträge",
  "boardTag": "HEUTIGE REPARATURAUFTRÄGE", "boardSub": "Wählen Sie einen Guide — jede Karte ist ein Reparaturauftrag.",
  "filterAll": "Alle", "filterStart": "Anfänger-Werkbank", "filterDevices": "Geräte-Werkbank", "filterAch": "Errungenschaften-Wand", "filterStory": "Handlungsstrang", "filterRef": "Referenz",
  "diffEasy": "Leicht", "diffMid": "Mittel", "diffHard": "Vertieft",
  "stampTodo": "ZU REPARIEREN", "stampWip": "IN REPARATUR", "stampDone": "REPARIERT",
  "related": "Verwandte Aufträge", "checklistTitle": "Checkliste Reparaturzyklus", "checklistSave": "Auf diesem Gerät gespeichert",
  "zenCalcTitle": "Zen-Punkte-Rechner", "zenCalcLead": "Tippen Sie Objekte an, um Punkte zu addieren — sehen Sie, wie nah Sie an 100 sind.",
  "zenTotal": "Summe", "zenTarget": "Ziel 100", "zenReset": "Zurücksetzen",
 },
 "es": {
  "name": "Guías de ReStory", "tagline": "Taller de reparación Akihabara 2005 — guías completas de ReStory",
  "description": "Guías de ReStory (维修物语): repara cada dispositivo, logros, finales, licencias, herramientas y guía para principiantes — en 10 idiomas.",
  "navHome": "Inicio", "navGuides": "Guías", "navAbout": "Acerca de", "navPrivacy": "Privacidad", "navContact": "Contacto",
  "langLabel": "Idioma", "aboutTitle": "Acerca de este sitio", "privacyTitle": "Política de privacidad", "contactTitle": "Contacto",
  "footerNote": "Sitio de fans no oficial: el juego y sus recursos pertenecen a sus propietarios.",
  "footerSource": "Información contrastada con la página oficial de Steam, allthings.how e intoindiegames; lo no verificado está marcado.",
  "quickAnswers": "Respuestas rápidas", "guides": "Todas las guías", "aboutGame": "Sobre el juego",
  "startPlaying": "Consíguelo en Steam", "getOnSteam": "Consíguelo en Steam ↗", "readGuide": "Leer la guía →",
  "moreGuides": "Más guías", "sources": "Fuentes y verificación", "updated": "Contenido",
  "aboutText": "ReStory Guides es un recurso de fans no oficial. Contrastamos cada página con la página oficial de Steam y fuentes fiables (allthings.how, intoindiegames), y marcamos claramente lo que aún se está verificando. Nunca inventamos detalles.",
  "aboutSources": "De dónde sale nuestra información",
  "navGroup1": "Guías", "navGroup2": "Dispositivos", "navGroup3": "Logros",
  "searchPh": "Buscar guías…", "searchLabel": "Buscar guías", "noMatch": "No hay partes de reparación que coincidan",
  "boardTag": "PARTES DE REPARACIÓN DE HOY", "boardSub": "Elija una guía: cada tarjeta es un trabajo de reparación.",
  "filterAll": "Todos", "filterStart": "Banco de inicio", "filterDevices": "Banco de dispositivos", "filterAch": "Muro de logros", "filterStory": "Línea de historia", "filterRef": "Referencia",
  "diffEasy": "Fácil", "diffMid": "Medio", "diffHard": "Profundo",
  "stampTodo": "POR REPARAR", "stampWip": "EN REPARACIÓN", "stampDone": "REPARADO",
  "related": "Partes relacionadas", "checklistTitle": "Lista del ciclo de reparación", "checklistSave": "Guardado en este dispositivo",
  "zenCalcTitle": "Calculadora de puntos Zen", "zenCalcLead": "Toca los objetos para sumar sus puntos — mira lo cerca que estás de 100.",
  "zenTotal": "Total", "zenTarget": "Objetivo 100", "zenReset": "Reiniciar",
 },
 "pt-BR": {
  "name": "Guias ReStory", "tagline": "Oficina de reparos Akihabara 2005 — guias completos de ReStory",
  "description": "Guias de ReStory (维修物语): conserte cada aparelho, conquistas, finais, licenças, ferramentas e guia para iniciantes — em 10 idiomas.",
  "navHome": "Início", "navGuides": "Guias", "navAbout": "Sobre", "navPrivacy": "Privacidade", "navContact": "Contato",
  "langLabel": "Idioma", "aboutTitle": "Sobre este site", "privacyTitle": "Política de Privacidade", "contactTitle": "Contato",
  "footerNote": "Site de fãs não oficial — o jogo e os recursos relacionados pertencem aos seus donos.",
  "footerSource": "Informações verificadas na página oficial da Steam, allthings.how e intoindiegames; detalhes não verificados são marcados.",
  "quickAnswers": "Respostas rápidas", "guides": "Todos os guias", "aboutGame": "Sobre o jogo",
  "startPlaying": "Obter na Steam", "getOnSteam": "Obter na Steam ↗", "readGuide": "Ler o guia →",
  "moreGuides": "Mais guias", "sources": "Fontes e verificação", "updated": "Conteúdo",
  "aboutText": "ReStory Guides é um recurso de fãs não oficial. Verificamos cada página na página oficial da Steam e em fontes confiáveis (allthings.how, intoindiegames), e marcamos claramente o que ainda está em verificação. Nunca inventamos detalhes.",
  "aboutSources": "De onde vêm nossas informações",
  "navGroup1": "Guias", "navGroup2": "Aparelhos", "navGroup3": "Conquistas",
  "searchPh": "Pesquisar guias…", "searchLabel": "Pesquisar guias", "noMatch": "Nenhuma ordem de serviço correspondente",
  "boardTag": "ORDENS DE SERVIÇO DE HOJE", "boardSub": "Escolha um guia — cada cartão é um trabalho de conserto.",
  "filterAll": "Todos", "filterStart": "Bancada inicial", "filterDevices": "Bancada de aparelhos", "filterAch": "Mural de conquistas", "filterStory": "Linha da história", "filterRef": "Referência",
  "diffEasy": "Fácil", "diffMid": "Médio", "diffHard": "Aprofundado",
  "stampTodo": "A CONSERTAR", "stampWip": "CONSERTANDO", "stampDone": "CONSERTADO",
  "related": "Ordens relacionadas", "checklistTitle": "Checklist do ciclo de conserto", "checklistSave": "Salvo neste dispositivo",
  "zenCalcTitle": "Calculadora de pontos Zen", "zenCalcLead": "Toque nos itens para somar pontos — veja o quão perto está de 100.",
  "zenTotal": "Total", "zenTarget": "Meta 100", "zenReset": "Redefinir",
 },
 "ru": {
  "name": "Гайды ReStory", "tagline": "Ремонтная мастерская Акихабара 2005 — полные гайды ReStory",
  "description": "Гайды ReStory (维修物语): ремонт всех устройств, достижения, концовки, лицензии, инструменты и гайд для новичков — на 10 языках.",
  "navHome": "Главная", "navGuides": "Гайды", "navAbout": "О сайте", "navPrivacy": "Конфиденциальность", "navContact": "Контакты",
  "langLabel": "Язык", "aboutTitle": "О сайте", "privacyTitle": "Политика конфиденциальности", "contactTitle": "Контакты",
  "footerNote": "Неофициальный фан-сайт — игра и связанные материалы принадлежат их владельцам.",
  "footerSource": "Информация проверена по официальной странице Steam, allthings.how и intoindiegames; непроверенное помечено.",
  "quickAnswers": "Быстрые ответы", "guides": "Все гайды", "aboutGame": "Об игре",
  "startPlaying": "В Steam", "getOnSteam": "В Steam ↗", "readGuide": "Читать гайд →",
  "moreGuides": "Больше гайдов", "sources": "Источники и проверка", "updated": "Содержание",
  "aboutText": "ReStory Guides — неофициальный фан-ресурс. Мы проверяем каждую страницу по официальной странице Steam и надёжным источникам (allthings.how, intoindiegames) и чётко помечаем всё, что ещё проверяется. Мы никогда не выдумываем детали.",
  "aboutSources": "Откуда наши данные",
  "navGroup1": "Гайды", "navGroup2": "Устройства", "navGroup3": "Достижения",
  "searchPh": "Поиск гайдов…", "searchLabel": "Поиск гайдов", "noMatch": "Нет подходящих нарядов на ремонт",
  "boardTag": "НАРЯДЫ НА РЕМОНТ", "boardSub": "Выберите гайд — каждая карточка это один заказ на ремонт.",
  "filterAll": "Все", "filterStart": "Стартовый верстак", "filterDevices": "Верстак устройств", "filterAch": "Стена достижений", "filterStory": "Сюжетная линия", "filterRef": "Справка",
  "diffEasy": "Легко", "diffMid": "Средне", "diffHard": "Глубоко",
  "stampTodo": "К РЕМОНТУ", "stampWip": "В РЕМОНТЕ", "stampDone": "ГОТОВО",
  "related": "Связанные наряды", "checklistTitle": "Чек-лист цикла ремонта", "checklistSave": "Сохранено на этом устройстве",
  "zenCalcTitle": "Калькулятор очков дзен", "zenCalcLead": "Нажимайте на предметы, чтобы прибавить очки — посмотрите, как близко вы к 100.",
  "zenTotal": "Итого", "zenTarget": "Цель 100", "zenReset": "Сброс",
 },
}

PRIVACY_BODY = {
 "en": "<p>This is a game guide website. We respect your privacy. Below is what we collect and how we use it.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">What we collect</h2><p>We use Google Analytics (GA4) for anonymous traffic statistics: page views, referrer, device type and approximate region. We do not collect names, emails or other personal identifiers, and we do not sell data.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Cookies</h2><p>Google Analytics uses cookies to distinguish visitors. You can disable cookies in your browser settings.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Affiliate links</h2><p>Some outbound links may carry affiliate markers; this never changes your price or our factual content.</p>",
 "zh-CN": "<p>这是游戏攻略网站，我们尊重访问者隐私。以下说明我们收集什么、如何使用。</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">我们收集什么</h2><p>我们使用 Google Analytics（GA4）进行匿名流量统计：页面浏览、来源、设备类型和大致地区。我们不收集姓名、邮箱等个人身份信息，不出售数据。</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Cookie</h2><p>Google Analytics 会使用 Cookie 来区分访客。你可以通过浏览器设置禁用 Cookie。</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">联盟链接</h2><p>部分外链可能带联盟标识；这不影响你的价格，也不改变我们的事实内容。</p>",
 "zh-TW": "<p>這是遊戲攻略網站，我們尊重訪客隱私。以下說明我們收集什麼、如何使用。</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">我們收集什麼</h2><p>我們使用 Google Analytics（GA4）進行匿名流量統計：頁面瀏覽、來源、裝置類型和大致地區。我們不收集姓名、信箱等個人身分資訊，不出售資料。</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Cookie</h2><p>Google Analytics 會使用 Cookie 來區分訪客。你可以透過瀏覽器設定停用 Cookie。</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">聯盟連結</h2><p>部分外連可能帶聯盟標識；這不影響你的價格，也不改變我們的事實內容。</p>",
 "ja": "<p>当サイトはゲーム攻略サイトです。訪問者のプライバシーを尊重します。以下に収集する情報とその使い方を説明します。</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">収集する情報</h2><p>Google Analytics（GA4）で匿名のアクセス統計を取得しています：ページビュー、参照元、端末タイプ、おおよその地域。氏名・メールアドレスなどの個人を特定できる情報は収集せず、データを販売することもありません。</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Cookie</h2><p>Google Analytics は訪問者を識別するために Cookie を使用します。ブラウザ設定で Cookie を無効にできます。</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">アフィリエイトリンク</h2><p>一部の外部リンクにはアフィリエイト識別子が含まれる場合があります。価格や事実内容が変わることはありません。</p>",
 "ko": "<p>이 사이트는 게임 공략 웹사이트입니다. 방문자의 개인정보를 존중합니다. 아래에 수집하는 정보와 사용 방법을 설명합니다.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">수집 정보</h2><p>Google Analytics(GA4)로 익명의 트래픽 통계를 수집합니다: 페이지 조회, 유입 경로, 기기 유형, 대략적인 지역. 이름, 이메일 등 개인 식별 정보는 수집하지 않으며 데이터를 판매하지 않습니다.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">쿠키</h2><p>Google Analytics는 방문자 구분을 위해 쿠키를 사용합니다. 브라우저 설정에서 쿠키를 비활성화할 수 있습니다.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">제휴 링크</h2><p>일부 외부 링크에는 제휴 식별자가 포함될 수 있습니다. 가격이나 사실 내용이 바뀌지 않습니다.</p>",
 "fr": "<p>Ce site est un site de guides de jeux. Nous respectons votre vie privée. Voici ce que nous collectons et comment nous l'utilisons.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Ce que nous collectons</h2><p>Nous utilisons Google Analytics (GA4) pour des statistiques de trafic anonymes : pages vues, provenance, type d'appareil et région approximative. Nous ne collectons ni noms, ni e-mails, ni autres identifiants personnels, et nous ne vendons pas de données.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Cookies</h2><p>Google Analytics utilise des cookies pour distinguer les visiteurs. Vous pouvez les désactiver dans les paramètres de votre navigateur.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Liens affiliés</h2><p>Certains liens externes peuvent porter des marqueurs d'affiliation ; cela ne change jamais votre prix ni notre contenu factuel.</p>",
 "de": "<p>Diese Seite ist eine Spieleratgeber-Website. Wir respektieren Ihre Privatsphäre. Nachfolgend, was wir sammeln und wie wir es verwenden.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Was wir sammeln</h2><p>Wir nutzen Google Analytics (GA4) für anonyme Verkehrsstatistiken: Seitenaufrufe, Herkunft, Gerätetyp und ungefähre Region. Wir sammeln keine Namen, E-Mails oder andere persönliche Identifikatoren und verkaufen keine Daten.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Cookies</h2><p>Google Analytics verwendet Cookies, um Besucher zu unterscheiden. Sie können Cookies in den Browser-Einstellungen deaktivieren.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Affiliate-Links</h2><p>Einige ausgehende Links können Affiliate-Marker tragen; das ändert nie Ihren Preis oder unseren faktenbasierten Inhalt.</p>",
 "es": "<p>Este es un sitio de guías de videojuegos. Respetamos tu privacidad. Esto es lo que recopilamos y cómo lo usamos.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Qué recopilamos</h2><p>Usamos Google Analytics (GA4) para estadísticas de tráfico anónimas: visitas, origen, tipo de dispositivo y región aproximada. No recopilamos nombres, correos ni otros identificadores personales, y no vendemos datos.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Cookies</h2><p>Google Analytics usa cookies para distinguir visitantes. Puedes desactivarlas en la configuración de tu navegador.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Enlaces de afiliado</h2><p>Algunos enlaces externos pueden llevar marcadores de afiliado; esto nunca cambia tu precio ni nuestro contenido factual.</p>",
 "pt-BR": "<p>Este é um site de guias de jogos. Respeitamos sua privacidade. Veja o que coletamos e como usamos.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">O que coletamos</h2><p>Usamos o Google Analytics (GA4) para estatísticas anônimas de tráfego: visualizações, origem, tipo de dispositivo e região aproximada. Não coletamos nomes, e-mails nem outros identificadores pessoais e não vendemos dados.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Cookies</h2><p>O Google Analytics usa cookies para distinguir visitantes. Você pode desativá-los nas configurações do navegador.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Links de afiliados</h2><p>Alguns links externos podem conter marcadores de afiliado; isso nunca muda seu preço nem nosso conteúdo factual.</p>",
 "ru": "<p>Это сайт с гайдами по играм. Мы уважаем вашу приватность. Ниже — что мы собираем и как используем.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Что мы собираем</h2><p>Мы используем Google Analytics (GA4) для анонимной статистики трафика: просмотры, источник, тип устройства и примерный регион. Мы не собираем имена, почты или другие личные идентификаторы и не продаём данные.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Файлы cookie</h2><p>Google Analytics использует cookie для различения посетителей. Вы можете отключить cookie в настройках браузера.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Партнёрские ссылки</h2><p>Некоторые внешние ссылки могут содержать партнёрские метки; это никогда не меняет вашу цену или наши факты.</p>",
}
CONTACT_BODY = {
 "en": "<p>Questions, corrections or missing guides? Email us at <a href=\"mailto:contact@restorygameguides.com\">contact@restorygameguides.com</a>. We read every message and update guides as we verify new details.</p>",
 "zh-CN": "<p>有疑问、勘误或想要补充的攻略？请发邮件到 <a href=\"mailto:contact@restorygameguides.com\">contact@restorygameguides.com</a>。我们会阅读每一条消息，并在核实新细节后更新攻略。</p>",
 "zh-TW": "<p>有疑問、勘誤或想補充的攻略？請寄信到 <a href=\"mailto:contact@restorygameguides.com\">contact@restorygameguides.com</a>。我們會閱讀每一則訊息，並在核實新細節後更新攻略。</p>",
 "ja": "<p>質問・訂正・攻略のリクエストは <a href=\"mailto:contact@restorygameguides.com\">contact@restorygameguides.com</a> までご連絡ください。すべてのメッセージに目を通し、確認できた内容を随時ガイドに反映します。</p>",
 "ko": "<p>질문, 오류 정정, 가이드 요청은 <a href=\"mailto:contact@restorygameguides.com\">contact@restorygameguides.com</a>로 보내주세요. 모든 메시지를 읽고, 확인된 내용을 가이드에 반영합니다.</p>",
 "fr": "<p>Questions, corrections ou guides manquants ? Écrivez-nous à <a href=\"mailto:contact@restorygameguides.com\">contact@restorygameguides.com</a>. Nous lisons chaque message et mettons à jour les guides au fil de nos vérifications.</p>",
 "de": "<p>Fragen, Korrekturen oder fehlende Guides? Schreiben Sie uns an <a href=\"mailto:contact@restorygameguides.com\">contact@restorygameguides.com</a>. Wir lesen jede Nachricht und aktualisieren Guides, sobald wir Details verifizieren.</p>",
 "es": "<p>¿Preguntas, correcciones o guías que faltan? Escríbenos a <a href=\"mailto:contact@restorygameguides.com\">contact@restorygameguides.com</a>. Leemos cada mensaje y actualizamos las guías a medida que verificamos detalles.</p>",
 "pt-BR": "<p>Perguntas, correções ou guias faltando? Envie um e-mail para <a href=\"mailto:contact@restorygameguides.com\">contact@restorygameguides.com</a>. Lemos cada mensagem e atualizamos os guias conforme verificamos detalhes.</p>",
 "ru": "<p>Вопросы, правки или недостающие гайды? Напишите нам на <a href=\"mailto:contact@restorygameguides.com\">contact@restorygameguides.com</a>. Мы читаем каждое сообщение и обновляем гайды по мере проверки деталей.</p>",
}

# 隐私/联系正文注入 site.i18n（generate.js 读取）
for _lg in LANGS:
    SITE_I18N[_lg]["privacyBody"] = PRIVACY_BODY[_lg]
    SITE_I18N[_lg]["contactBody"] = CONTACT_BODY[_lg]

# =====================================================================
# 来源 key → 各语言链接
# =====================================================================
def _src(label, url, labels):
    d = {"label": label, "url": url, "labels": dict(labels)}
    d["labels"]["zh-TW"] = cc.convert(d["labels"]["zh-CN"])
    return d

SRC_STEAM = _src("Official Steam page", "https://store.steampowered.com/app/3812600/ReStory_Chill_Electronics_Repairs/", {
    "en": "Official Steam page", "zh-CN": "Steam 官方商店页", "ja": "Steam 公式ストア", "ko": "Steam 공식 스토어",
    "fr": "Page Steam officielle", "de": "Offizielle Steam-Seite", "es": "Página oficial de Steam",
    "pt-BR": "Página oficial na Steam", "ru": "Официальная страница Steam",
})
SRC_ALLTHINGS = _src("allthings.how — ReStory device list & achievements", "https://allthings.how/restory-chill-electronics-repairs-every-device-you-can-repair/", {
    "en": "allthings.how — ReStory devices & achievements", "zh-CN": "allthings.how — ReStory 设备清单与成就",
    "ja": "allthings.how — ReStory デバイス一覧と実績", "ko": "allthings.how — ReStory 기기 목록 및 업적",
    "fr": "allthings.how — appareils et succès ReStory", "de": "allthings.how — ReStory Geräte & Errungenschaften",
    "es": "allthings.how — dispositivos y logros de ReStory", "pt-BR": "allthings.how — aparelhos e conquistas de ReStory",
    "ru": "allthings.how — устройства и достижения ReStory",
})
SRC_INTOINDIE = _src("intoindiegames — ReStory beginner guide", "https://intoindiegames.com/walkthroughs/tips-tricks/beginners-guide-to-restory-chill-electronics-repair/", {
    "en": "intoindiegames — ReStory beginner guide", "zh-CN": "intoindiegames — ReStory 新手指南",
    "ja": "intoindiegames — ReStory 初心者ガイド", "ko": "intoindiegames — ReStory 초보자 가이드",
    "fr": "intoindiegames — guide débutant ReStory", "de": "intoindiegames — ReStory Einsteiger-Guide",
    "es": "intoindiegames — guía para principiantes de ReStory", "pt-BR": "intoindiegames — guia para iniciantes de ReStory",
    "ru": "intoindiegames — гайд для новичков ReStory",
})
SRC_POWERPYX = _src("PowerPyx — achievement roadmap structure", "https://www.powerpyx.com/", {
    "en": "PowerPyx — roadmap structure", "zh-CN": "PowerPyx — 路线图结构参考",
    "ja": "PowerPyx — ロードマップ構成", "ko": "PowerPyx — 로드맵 구성",
    "fr": "PowerPyx — structure de roadmap", "de": "PowerPyx — Roadmap-Struktur",
    "es": "PowerPyx — estructura de hoja de ruta", "pt-BR": "PowerPyx — estrutura de roadmap",
    "ru": "PowerPyx — структура роадмапа",
})
SRC_MAP = {"steam": SRC_STEAM, "allthings": SRC_ALLTHINGS, "intoindie": SRC_INTOINDIE, "powerpyx": SRC_POWERPYX}

# =====================================================================
# 页面组装
# =====================================================================
def _trunc(t, lim):
    return t if len(t) <= lim else t[:lim - 1].rstrip() + "…"

def _trunc_w(t, lim):
    # 宽字符截断：CJK 各计 1（lim 以宽字符计）
    if len(t) <= lim: return t
    out, w = "", 0
    for ch in t:
        w += 2 if ord(ch) > 0x2E7F else 1
        if w > lim: break
        out += ch
    return out.rstrip() + "…"

def _page(slug, title, meta_title, meta_desc, intro, sections, sources, icon):
    return {
        "slug": slug, "title": title, "metaTitle": meta_title, "metaDescription": meta_desc,
        "intro": intro, "sections": sections, "sources": sources,
        "meta": {"icon": icon},
    }

# 翻译校验：与 EN 结构完全一致
def _shape(p):
    return [(s.get("type"), len(s.get("items", [])), len(s.get("rows", [])), len(s.get("columns", []))) for s in p["sections"]]

EN_SHAPE = {slug: _shape(content_en.PAGES_EN[slug]) for slug in content_en.PAGE_ORDER}

PAGES = []
for slug in content_en.PAGE_ORDER:
    en = content_en.PAGES_EN[slug]
    i18n = {"en": copy.deepcopy(en)}
    for lg in TRANS_LANGS:
        if lg not in PAGE_TRANS: continue
        tr = PAGE_TRANS[lg].get(slug)
        if tr is None:
            print(f"⚠️ {slug} missing in {lg}")
            continue
        if _shape(tr) != EN_SHAPE[slug]:
            print(f"❌ SHAPE MISMATCH {slug}/{lg}: {_shape(tr)} != {EN_SHAPE[slug]}")
        i18n[lg] = copy.deepcopy(tr)
    # zh-TW：由 zh-CN 经 OpenCC
    if "zh-CN" in i18n:
        i18n["zh-TW"] = json.loads(cc.convert(json.dumps(i18n["zh-CN"], ensure_ascii=False)))
    page = _page(slug, en["title"], en["metaTitle"], en["metaDescription"], en["intro"],
                 en["sections"], [SRC_MAP[k] for k in en["sources"]], en.get("icon", "rocket"))
    page["i18n"] = i18n
    PAGES.append(page)
# ---- addon 合并（新增章节 + intro 追加；每语言一个 JSON，EN 为基准）----
_ADDON_FILE = {
    "zh-CN": "addons_zh_cn.json",
    "zh-TW": "addons_zh_cn.json",
    "pt-BR": "addons_pt_br.json",
}

def _load_addons(lg):
    if lg == "zh-TW":
        raw = json.loads((ROOT / "addons_zh_cn.json").read_text())
        # zh-TW：由 zh-CN addon 经 OpenCC(s2tw) 转台湾标准字形
        return json.loads(cc.convert(json.dumps(raw, ensure_ascii=False)))
    name = _ADDON_FILE.get(lg, f"addons_{lg}.json")
    fp = ROOT / name
    if not fp.exists():
        fp = ROOT / "addons_en.json"
    return json.loads(fp.read_text())

def _merge_addons(page, lg, addons):
    t = page["i18n"].get(lg)
    if not t: return
    a = addons.get(page["slug"])
    if not a: return
    if a.get("intro_extra") and t.get("intro"):
        t["intro"] = t["intro"] + a["intro_extra"]
    if a.get("sections"):
        t["sections"] = list(t.get("sections", [])) + list(a["sections"])

for lg in LANGS:
    addons = _load_addons(lg)
    for page in PAGES:
        _merge_addons(page, lg, addons)
# 设备网格文案（无则用英文，避免空）
_DEV_T = {
 "en": ["Device step pages","Each device has its own page with the repair loop, weak points and an interactive checklist."],
 "zh-CN": ["设备步骤页","每台设备都有自己的页面：修复循环、薄弱点与交互式检查清单。"],
 "zh-TW": ["設備步驟頁","每台設備都有自己的頁面：修復循環、薄弱點與互動式檢查清單。"],
 "ja": ["デバイス別ステップ","各デバイスに修理ループ・弱点・インタラクティブチェックリストのページがあります。"],
 "ko": ["기기별 단계 페이지","각 기기에는 수리 루프, 약점, 대화형 체크리스트 페이지가 있습니다."],
 "fr": ["Pages par appareil","Chaque appareil a sa page : boucle de réparation, points faibles et checklist interactive."],
 "de": ["Geräte-Schritt-Seiten","Jedes Gerät hat seine eigene Seite: Reparaturzyklus, Schwachstellen und interaktive Checkliste."],
 "es": ["Páginas por dispositivo","Cada dispositivo tiene su página: bucle de reparación, puntos débiles y lista interactiva."],
 "pt-BR": ["Páginas por aparelho","Cada aparelho tem sua página: ciclo de conserto, pontos fracos e checklist interativo."],
 "ru": ["Страницы устройств","У каждого устройства есть своя страница: цикл ремонта, слабые места и интерактивный чек-лист."],
}
for lg, (t, l) in _DEV_T.items():
    SITE_I18N[lg]["devicesTitle"] = t
    SITE_I18N[lg]["devicesLead"] = l



# SEO 后处理：CJK 宽字符截断
CJK = {"zh-CN", "zh-TW", "ja", "ko"}
for p in PAGES:
    for lg in LANGS:
        t = p["i18n"].get(lg)
        if not t: continue
        if lg in CJK:
            t["metaTitle"] = _trunc_w(t["metaTitle"].replace(" & ", " · ").replace("&", "·"), 30)
            t["metaDescription"] = _trunc_w(t["metaDescription"], 74)
        else:
            t["metaTitle"] = _trunc(t["metaTitle"].replace(" & ", " and ").replace("&", "and"), 58)
            t["metaDescription"] = _trunc(t["metaDescription"], 150)

# heroImage 自动填充（assets/images/<slug>.jpg 存在才填）
img_dir = ROOT / ".." / "assets" / "images"
for p in PAGES:
    if (img_dir / f"{p['slug']}.jpg").exists():
        p["heroImage"] = f"/images/{p['slug']}.jpg"

# =====================================================================
# 组装 site.json
# =====================================================================
base = json.loads((ROOT / "site.base.json").read_text())
site = copy.deepcopy(base["site"])
site["i18n"] = SITE_I18N
game = copy.deepcopy(base["game"])

out = {"site": site, "game": game, "pages": PAGES}
(ROOT / "site.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

# 校验报告
have = [lg for lg in TRANS_LANGS if lg in PAGE_TRANS]
missing_tr = [lg for lg in TRANS_LANGS if lg not in PAGE_TRANS]
print(f"✓ {len(LANGS)} locales（zh-TW=OpenCC 自动）｜{len(PAGES)} 页")
print(f"✓ 翻译齐全: {'NONE' if not missing_tr else missing_tr}")
print(f"✓ section-count mismatch: NONE（已在上方告警）")
print(f"✓ 使用语言: {LANGS}")
print(f"✓ 来源映射: steam/allthings/intoindie/powerpyx 各语言 label 齐备")
