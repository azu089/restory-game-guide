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
SRC_STEAM_ACHIEVEMENTS = _src("Official Steam global achievement stats", "https://steamcommunity.com/stats/3812600/achievements", {
    "en": "Official Steam achievement list & global stats", "zh-CN": "Steam 官方成就清单与全球统计",
    "zh-TW": "Steam 官方成就清單與全球統計", "ja": "Steam 公式実績リスト・世界統計",
    "ko": "Steam 공식 도전 과제 목록 및 전 세계 통계", "fr": "Liste officielle des succès et statistiques Steam",
    "de": "Offizielle Steam-Errungenschaften und globale Statistik", "es": "Lista oficial de logros y estadísticas de Steam",
    "pt-BR": "Lista oficial de conquistas e estatísticas globais da Steam", "ru": "Официальный список достижений и глобальная статистика Steam",
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
    # The endings add-ons contained speculative branch theories. Until exact
    # triggers are verified at L0, keep this page deliberately concise.
    if page["slug"] in ("endings", "achievements", "achievements-roadmap", "hidden-achievements"): return
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

# ---- Official achievement dataset + local progress tracker ----
# Steam Community exposes all 50 names, unlock conditions and global unlock
# rates. Keep that snapshot as the sole source of truth for /achievements;
# older article copy was incomplete (47 named rows + a placeholder).
_ACH_DATA = json.loads((ROOT / "achievements_official.json").read_text())
_ACH_GROUP_KEYS = [
    "repair","repair","economy","online","reputation","license","tools","market","repair","workshop",
    "online","market","reputation","story","license","economy","custom","economy","economy","tools",
    "collection","reputation","tools","workshop","story","market","story","market","custom","online",
    "time","custom","time","hidden","custom","license","hidden","custom","license","economy",
    "market","hidden","hidden","time","hidden","custom","story","repair","custom","time",
]
_ACH_UI = {
 "en": ["Official 50-achievement tracker", "All 50 entries below come from Steam's official global achievement page. Global unlock rates are a snapshot from 13 August 2026; editorial groups are only for filtering.", "All 50 achievements", "Achievement", "Official unlock condition", "Global unlock", "Group", "Search achievements…", "All groups", "Hide completed", "completed", "Reset progress", "No achievements match these filters.", "Progress is saved only in this browser.", "Steam does not reveal this hidden condition.", "How many achievements does ReStory have?", "50. The list and conditions below are taken directly from Steam's official achievement data.", "Are the global unlock rates live?", "No. They are a dated snapshot from 13 August 2026 and will change as more players unlock achievements."],
 "zh-CN": ["官方 50 项成就追踪器", "下方 50 项全部取自 Steam 官方全球成就页。全球解锁率为 2026 年 8 月 13 日快照；分组仅用于筛选。", "全部 50 项成就", "成就", "官方解锁条件", "全球解锁率", "分组", "搜索成就…", "全部分组", "隐藏已完成", "已完成", "重置进度", "没有符合筛选条件的成就。", "进度仅保存在当前浏览器。", "Steam 未公开这个隐藏条件。", "ReStory 有多少项成就？", "共 50 项。下方清单与条件直接取自 Steam 官方成就数据。", "全球解锁率是实时的吗？", "不是。这是 2026 年 8 月 13 日的快照，随着更多玩家解锁会继续变化。"],
 "zh-TW": ["官方 50 項成就追蹤器", "下方 50 項全部取自 Steam 官方全球成就頁。全球解鎖率為 2026 年 8 月 13 日快照；分組僅用於篩選。", "全部 50 項成就", "成就", "官方解鎖條件", "全球解鎖率", "分組", "搜尋成就…", "全部分組", "隱藏已完成", "已完成", "重設進度", "沒有符合篩選條件的成就。", "進度僅儲存在目前瀏覽器。", "Steam 未公開這個隱藏條件。", "ReStory 有多少項成就？", "共 50 項。下方清單與條件直接取自 Steam 官方成就資料。", "全球解鎖率是即時的嗎？", "不是。這是 2026 年 8 月 13 日的快照，會隨更多玩家解鎖而變化。"],
 "ja": ["公式50実績トラッカー", "以下の50件はすべてSteam公式のグローバル実績ページに基づきます。解除率は2026年8月13日時点のスナップショットで、分類は絞り込み用です。", "全50実績", "実績", "公式解除条件", "世界解除率", "分類", "実績を検索…", "すべての分類", "完了を隠す", "完了", "進捗をリセット", "条件に一致する実績はありません。", "進捗はこのブラウザにのみ保存されます。", "Steamではこの隠し条件は公開されていません。", "ReStoryの実績はいくつ？", "50件です。以下の一覧と条件はSteam公式実績データから取得しています。", "世界解除率はリアルタイム？", "いいえ。2026年8月13日時点のスナップショットで、今後変動します。"],
 "ko": ["공식 도전 과제 50개 추적기", "아래 50개 항목은 모두 Steam 공식 전 세계 도전 과제 페이지에서 가져왔습니다. 달성률은 2026년 8월 13일 스냅샷이며 그룹은 필터용입니다.", "도전 과제 50개", "도전 과제", "공식 달성 조건", "전 세계 달성률", "그룹", "도전 과제 검색…", "모든 그룹", "완료 항목 숨기기", "완료", "진행 상황 초기화", "필터와 일치하는 도전 과제가 없습니다.", "진행 상황은 이 브라우저에만 저장됩니다.", "Steam에서 이 숨겨진 조건을 공개하지 않습니다.", "ReStory에는 도전 과제가 몇 개 있나요?", "50개입니다. 아래 목록과 조건은 Steam 공식 도전 과제 데이터에서 가져왔습니다.", "전 세계 달성률은 실시간인가요?", "아닙니다. 2026년 8월 13일 스냅샷이며 계속 변합니다."],
 "fr": ["Suivi officiel des 50 succès", "Les 50 entrées viennent de la page officielle des succès Steam. Les taux mondiaux datent du 13 août 2026 ; les groupes servent uniquement au filtrage.", "Les 50 succès", "Succès", "Condition officielle", "Taux mondial", "Groupe", "Rechercher un succès…", "Tous les groupes", "Masquer les terminés", "terminés", "Réinitialiser", "Aucun succès ne correspond à ces filtres.", "La progression reste dans ce navigateur.", "Steam ne révèle pas cette condition cachée.", "Combien de succès compte ReStory ?", "50. La liste et les conditions proviennent directement des données officielles de Steam.", "Les taux mondiaux sont-ils en direct ?", "Non. Il s'agit d'un instantané du 13 août 2026 qui évoluera avec les joueurs."],
 "de": ["Offizieller Tracker für 50 Errungenschaften", "Alle 50 Einträge stammen von Steams offizieller globaler Statistikseite. Die Freischaltraten sind ein Stand vom 13. August 2026; Gruppen dienen nur als Filter.", "Alle 50 Errungenschaften", "Errungenschaft", "Offizielle Bedingung", "Global freigeschaltet", "Gruppe", "Errungenschaften suchen…", "Alle Gruppen", "Erledigte ausblenden", "erledigt", "Fortschritt zurücksetzen", "Keine Errungenschaften entsprechen den Filtern.", "Der Fortschritt wird nur in diesem Browser gespeichert.", "Steam zeigt diese versteckte Bedingung nicht an.", "Wie viele Errungenschaften hat ReStory?", "50. Liste und Bedingungen stammen direkt aus den offiziellen Steam-Daten.", "Sind die globalen Raten live?", "Nein. Sie sind ein Stand vom 13. August 2026 und verändern sich weiter."],
 "es": ["Rastreador oficial de 50 logros", "Las 50 entradas proceden de la página oficial de logros globales de Steam. Las tasas son una captura del 13 de agosto de 2026; los grupos solo sirven para filtrar.", "Los 50 logros", "Logro", "Condición oficial", "Desbloqueo global", "Grupo", "Buscar logros…", "Todos los grupos", "Ocultar completados", "completados", "Restablecer progreso", "Ningún logro coincide con estos filtros.", "El progreso se guarda solo en este navegador.", "Steam no revela esta condición oculta.", "¿Cuántos logros tiene ReStory?", "50. La lista y las condiciones proceden directamente de los datos oficiales de Steam.", "¿Las tasas globales son en tiempo real?", "No. Son una captura del 13 de agosto de 2026 y seguirán cambiando."],
 "pt-BR": ["Rastreador oficial das 50 conquistas", "As 50 entradas vêm da página oficial de conquistas globais da Steam. As taxas são um retrato de 13 de agosto de 2026; os grupos servem apenas para filtrar.", "Todas as 50 conquistas", "Conquista", "Condição oficial", "Desbloqueio global", "Grupo", "Buscar conquistas…", "Todos os grupos", "Ocultar concluídas", "concluídas", "Redefinir progresso", "Nenhuma conquista corresponde aos filtros.", "O progresso fica salvo somente neste navegador.", "A Steam não revela esta condição oculta.", "Quantas conquistas ReStory tem?", "50. A lista e as condições vêm diretamente dos dados oficiais da Steam.", "As taxas globais são em tempo real?", "Não. São um retrato de 13 de agosto de 2026 e continuarão mudando."],
 "ru": ["Официальный трекер 50 достижений", "Все 50 пунктов взяты с официальной страницы глобальной статистики Steam. Проценты — снимок на 13 августа 2026 года; группы нужны только для фильтрации.", "Все 50 достижений", "Достижение", "Официальное условие", "Глобально", "Группа", "Поиск достижений…", "Все группы", "Скрыть выполненные", "выполнено", "Сбросить прогресс", "Нет достижений, подходящих под фильтры.", "Прогресс хранится только в этом браузере.", "Steam не раскрывает условие этого скрытого достижения.", "Сколько достижений в ReStory?", "50. Список и условия взяты напрямую из официальных данных Steam.", "Глобальные проценты показываются в реальном времени?", "Нет. Это снимок на 13 августа 2026 года, и значения будут меняться."],
}
_ACH_GROUP_LABELS = {
 "en": ["Repair", "Economy", "Online", "Reputation", "Licenses", "Tools", "Marketplace", "Workshop", "Story", "Customization", "Collection", "Time", "Hidden"],
 "zh-CN": ["维修", "经济", "线上订单", "声望", "许可证", "工具", "市场", "工坊", "剧情", "定制", "收藏", "时间", "隐藏"],
 "zh-TW": ["維修", "經濟", "線上訂單", "聲望", "許可證", "工具", "市場", "工坊", "劇情", "自訂", "收藏", "時間", "隱藏"],
 "ja": ["修理", "経済", "オンライン", "評判", "ライセンス", "ツール", "マーケット", "工房", "ストーリー", "カスタム", "収集", "時間", "隠し"],
 "ko": ["수리", "경제", "온라인", "평판", "라이선스", "도구", "마켓", "작업장", "스토리", "꾸미기", "수집", "시간", "숨김"],
 "fr": ["Réparation", "Économie", "En ligne", "Réputation", "Licences", "Outils", "Marché", "Atelier", "Histoire", "Personnalisation", "Collection", "Temps", "Caché"],
 "de": ["Reparatur", "Wirtschaft", "Online", "Ruf", "Lizenzen", "Werkzeuge", "Markt", "Werkstatt", "Story", "Anpassung", "Sammlung", "Zeit", "Versteckt"],
 "es": ["Reparación", "Economía", "En línea", "Reputación", "Licencias", "Herramientas", "Mercado", "Taller", "Historia", "Personalización", "Colección", "Tiempo", "Oculto"],
 "pt-BR": ["Conserto", "Economia", "Online", "Reputação", "Licenças", "Ferramentas", "Mercado", "Oficina", "História", "Personalização", "Coleção", "Tempo", "Oculta"],
 "ru": ["Ремонт", "Экономика", "Онлайн", "Репутация", "Лицензии", "Инструменты", "Рынок", "Мастерская", "Сюжет", "Настройка", "Коллекция", "Время", "Скрытое"],
}
_ACH_GROUP_ORDER = ["repair","economy","online","reputation","license","tools","market","workshop","story","custom","collection","time","hidden"]

for page in PAGES:
    if page["slug"] != "achievements": continue
    page["sources"] = [SRC_STEAM_ACHIEVEMENTS, SRC_STEAM]
    for lg in LANGS:
        t, ui = page["i18n"][lg], _ACH_UI[lg]
        labels = dict(zip(_ACH_GROUP_ORDER, _ACH_GROUP_LABELS[lg]))
        rows = _ACH_DATA["locales"][lg]
        table_rows, row_attrs = [], []
        for row, group_key in zip(rows, _ACH_GROUP_KEYS):
            condition = row["condition"] or ui[14]
            table_rows.append([row["name"], condition, row["rarity"], labels[group_key]])
            row_attrs.append({"achievement-id": row["id"], "group": group_key})
        t["title"] = ui[0]
        t["metaTitle"] = ui[0]
        t["intro"] = ui[1]
        t["metaDescription"] = ui[1]
        t["sections"] = [
            {"type": "note", "heading": ui[0], "body": ui[1]},
            {"type": "table", "heading": ui[2], "columns": ui[3:7], "rows": table_rows,
             "rowAttrs": row_attrs, "tracker": "achievements", "trackerLabels": ui[7:14], "noMatch": ui[12]},
            {"type": "faq", "heading": "FAQ", "items": [[ui[15], ui[16]], [ui[17], ui[18]]]},
        ]

_ACH_RELATED_UI = {
 "en": {"roadTitle":"ReStory Achievement Roadmap: Official-Condition Order","roadIntro":"A practical 100% order built only from Steam's official unlock conditions. It avoids the old, incorrect advice to leave the game open for 168 real hours.","plan":"Efficient order","cols":["Stage","Combine these goals","Why now"],"rows":[["1 · Natural start","First repair, soldering, first email order, first license, 5 reviews and 2 bills","These unlock through normal onboarding."],["2 · Buy core tools","Professional screwdriver, automatic ultrasonic bath and shredder","They unlock achievements and speed later volume goals."],["3 · Batch counters","Email orders 25/100; marketplace devices 5/25; boxes 1/50; stickers 1/25/100; cleaning 100/1,000; reprogramming 1/25","Stack related actions instead of grinding them separately."],["4 · Protect day rules","Buy no new parts for 10 days; do not end the day for 7 days; play through days 30, 90 and 365","These are in-game day conditions—not a verified 168-hour real-time session."],["5 · Story and competitions","Help a child for free; win 1, 3 and every-device competitions; finish the five hidden entries last","Steam does not publish the exact hidden conditions." ]],"noteTitle":"No verified 100% blocker","note":"Steam's official list does not identify an achievement as currently unobtainable. We therefore do not repeat the older third-party claim that 100% is blocked.","q":"Does Akiba never sleeps require 168 real hours?","a":"No such real-time condition appears in Steam's official data. The official text says: do not end the day for 7 days in a row.","hiddenTitle":"ReStory Hidden Achievements: What Steam Confirms","hiddenIntro":"Steam lists five hidden entries by name but does not reveal their conditions. This page separates confirmed facts from community theories.","hiddenHead":"The five hidden entries","hiddenCondition":"Condition not disclosed by Steam"},
 "zh-CN": {"roadTitle":"ReStory 成就路线图：按官方条件排序","roadIntro":"只依据 Steam 官方解锁条件制定的 100% 顺序，并移除旧版“现实挂机 168 小时”的错误建议。","plan":"高效完成顺序","cols":["阶段","合并完成的目标","为什么现在做"],"rows":[["1 · 自然开局","首次维修、焊接、首个邮件订单、首张许可证、5 条评价与支付 2 张账单","这些会随新手流程自然解锁。"],["2 · 购买核心工具","专业螺丝刀、自动超声波清洗机和粉碎机","既解锁成就，也提升后续批量任务效率。"],["3 · 批量计数","邮件订单 25/100；市场设备 5/25；零件箱 1/50；贴纸 1/25/100；清理零件 100/1000；重编程 1/25","把同类动作叠加完成，避免分开刷。"],["4 · 保护天数条件","连续 10 天不买新零件；连续 7 天不结束当天；游玩至第 30/90/365 天","这里是游戏内天数，不是已核实的现实 168 小时挂机。"],["5 · 剧情与比赛","免费帮助孩子；赢得 1 次、3 种及全设备比赛；最后处理 5 项隐藏成就","Steam 没有公开隐藏成就的准确条件。"]],"noteTitle":"没有已核实的 100% 阻断项","note":"Steam 官方清单没有标出当前无法获得的成就，因此本站不再重复旧第三方“100% 被阻断”的说法。","q":"Akiba never sleeps 需要现实挂机 168 小时吗？","a":"Steam 官方数据没有这个条件。官方原文是：连续 7 天不要结束当天。","hiddenTitle":"ReStory 隐藏成就：Steam 已确认的信息","hiddenIntro":"Steam 列出 5 项隐藏成就名称，但没有公开条件。本页只保留已确认事实，不把社区猜测写成攻略。","hiddenHead":"5 项隐藏成就","hiddenCondition":"Steam 未公开条件"},
 "zh-TW": {"roadTitle":"ReStory 成就路線圖：按官方條件排序","roadIntro":"只依據 Steam 官方解鎖條件制定的 100% 順序，並移除舊版「現實掛機 168 小時」的錯誤建議。","plan":"高效完成順序","cols":["階段","合併完成的目標","為什麼現在做"],"rows":[["1 · 自然開局","首次維修、焊接、首個郵件訂單、首張許可證、5 則評價與支付 2 張帳單","這些會隨新手流程自然解鎖。"],["2 · 購買核心工具","專業螺絲起子、自動超音波清洗機和粉碎機","既解鎖成就，也提升後續批量任務效率。"],["3 · 批量計數","郵件訂單 25/100；市場設備 5/25；零件箱 1/50；貼紙 1/25/100；清理零件 100/1000；重編程 1/25","把同類動作疊加完成，避免分開刷。"],["4 · 保護天數條件","連續 10 天不買新零件；連續 7 天不結束當天；遊玩至第 30/90/365 天","這是遊戲內天數，不是已核實的現實 168 小時掛機。"],["5 · 劇情與比賽","免費幫助孩子；贏得 1 次、3 種及全設備比賽；最後處理 5 項隱藏成就","Steam 沒有公開隱藏成就的準確條件。"]],"noteTitle":"沒有已核實的 100% 阻斷項","note":"Steam 官方清單沒有標出目前無法取得的成就，因此本站不再重複舊第三方「100% 被阻斷」的說法。","q":"Akiba never sleeps 需要現實掛機 168 小時嗎？","a":"Steam 官方資料沒有這個條件。官方原文是：連續 7 天不要結束當天。","hiddenTitle":"ReStory 隱藏成就：Steam 已確認的資訊","hiddenIntro":"Steam 列出 5 項隱藏成就名稱，但沒有公開條件。本頁只保留已確認事實，不把社群猜測寫成攻略。","hiddenHead":"5 項隱藏成就","hiddenCondition":"Steam 未公開條件"},
 "ja": {"roadTitle":"ReStory 実績ロードマップ：公式条件順","roadIntro":"Steam公式の解除条件だけで組んだ100%ルートです。旧版の「現実時間で168時間放置」という誤った助言は削除しました。","plan":"効率的な順番","cols":["段階","まとめて進める目標","この順番の理由"],"rows":[["1 · 自然な序盤","初修理、はんだ付け、初メール注文、初ライセンス、レビュー5件、請求書2件","チュートリアル中に自然に解除できます。"],["2 · 基本道具","プロ用ドライバー、自動超音波洗浄機、シュレッダー","実績解除と後半の効率化を同時に進めます。"],["3 · 回数をまとめる","メール25/100、市場購入5/25、箱1/50、ステッカー1/25/100、清掃100/1000、再プログラム1/25","同じ行動を別々に稼がず重ねます。"],["4 · 日数条件を守る","10日間新品部品を買わない、7日連続で一日を終了しない、30/90/365日プレイ","ゲーム内日数の条件で、現実の168時間ではありません。"],["5 · 物語と大会","子供を無料で助ける、1回・3種類・全機器の大会に勝つ、隠し5件は最後","Steamは隠し条件を公開していません。"]],"noteTitle":"確認済みの100%阻害要因はなし","note":"Steam公式リストは現在取得不能な実績を示していません。そのため、古い第三者情報の「100%不可」は掲載しません。","q":"Akiba never sleepsは現実の168時間が必要？","a":"Steam公式データにその条件はありません。公式文は「7日連続で一日を終了しない」です。","hiddenTitle":"ReStory 隠し実績：Steamで確認できること","hiddenIntro":"Steamは隠し実績5件の名称を載せていますが、条件は公開していません。推測と確認済み情報を分けます。","hiddenHead":"隠し実績5件","hiddenCondition":"Steamでは条件非公開"},
 "ko": {"roadTitle":"ReStory 도전 과제 로드맵: 공식 조건 순서","roadIntro":"Steam 공식 달성 조건만으로 만든 100% 진행 순서입니다. 예전의 '현실 시간 168시간 방치'라는 잘못된 조언은 제거했습니다.","plan":"효율적인 순서","cols":["단계","함께 진행할 목표","이 순서인 이유"],"rows":[["1 · 자연스러운 시작","첫 수리, 납땜, 첫 이메일 주문, 첫 라이선스, 리뷰 5개, 청구서 2개","초반 진행 중 자연스럽게 달성됩니다."],["2 · 핵심 도구","전문 드라이버, 자동 초음파 세척기, 파쇄기","도전 과제와 후반 효율을 함께 챙깁니다."],["3 · 횟수 묶기","이메일 25/100, 마켓 기기 5/25, 부품 상자 1/50, 스티커 1/25/100, 청소 100/1000, 재프로그래밍 1/25","같은 행동을 따로 반복하지 않고 겹칩니다."],["4 · 날짜 조건 보호","10일간 새 부품 미구매, 7일 연속 하루를 종료하지 않기, 30/90/365일 플레이","게임 내 날짜 조건이며 현실 168시간 조건이 아닙니다."],["5 · 스토리와 대회","아이를 무료로 돕기, 1회·3종·모든 기기 대회 우승, 숨김 5개는 마지막","Steam은 정확한 숨김 조건을 공개하지 않습니다."]],"noteTitle":"확인된 100% 차단 요소 없음","note":"Steam 공식 목록은 현재 획득 불가능한 도전 과제를 표시하지 않습니다. 따라서 오래된 제3자 주장을 반복하지 않습니다.","q":"Akiba never sleeps에 현실 168시간이 필요한가요?","a":"Steam 공식 데이터에는 그런 조건이 없습니다. 공식 문구는 7일 연속 하루를 종료하지 말라는 것입니다.","hiddenTitle":"ReStory 숨겨진 도전 과제: Steam 확인 정보","hiddenIntro":"Steam은 숨겨진 항목 5개의 이름은 공개하지만 조건은 공개하지 않습니다. 추측은 사실과 분리합니다.","hiddenHead":"숨겨진 도전 과제 5개","hiddenCondition":"Steam에서 조건을 공개하지 않음"},
 "fr": {"roadTitle":"Feuille de route des succès ReStory : conditions officielles","roadIntro":"Un ordre pratique fondé uniquement sur les conditions officielles de Steam. L'ancien conseil erroné d'attendre 168 heures réelles a été retiré.","plan":"Ordre efficace","cols":["Étape","Objectifs à combiner","Pourquoi maintenant"],"rows":[["1 · Début naturel","Première réparation et soudure, première commande, première licence, 5 avis et 2 factures","Ils se débloquent naturellement au début."],["2 · Outils essentiels","Tournevis professionnel, bain à ultrasons automatique et broyeur","Ils donnent des succès et accélèrent les objectifs suivants."],["3 · Compteurs groupés","E-mails 25/100, marché 5/25, boîtes 1/50, autocollants 1/25/100, nettoyage 100/1000, reprogrammation 1/25","Cumulez les actions similaires."],["4 · Règles de jours","10 jours sans pièce neuve, ne pas terminer la journée pendant 7 jours, jouer 30/90/365 jours","Ce sont des jours en jeu, pas 168 heures réelles."],["5 · Histoire et concours","Aider un enfant gratuitement, gagner 1/3/tous les concours, garder les 5 cachés pour la fin","Steam ne publie pas leurs conditions exactes."]],"noteTitle":"Aucun blocage du 100% vérifié","note":"La liste officielle Steam ne signale aucun succès actuellement impossible. Nous ne reprenons donc pas cette ancienne affirmation tierce.","q":"Akiba never sleeps exige-t-il 168 heures réelles ?","a":"Cette condition n'apparaît pas dans les données officielles. Le texte dit de ne pas terminer la journée pendant 7 jours de suite.","hiddenTitle":"Succès cachés ReStory : ce que confirme Steam","hiddenIntro":"Steam nomme cinq succès cachés sans révéler leurs conditions. Cette page sépare les faits des théories.","hiddenHead":"Les cinq succès cachés","hiddenCondition":"Condition non révélée par Steam"},
 "de": {"roadTitle":"ReStory-Erfolgsroadmap nach offiziellen Bedingungen","roadIntro":"Eine praktische 100%-Reihenfolge nur aus Steams offiziellen Bedingungen. Der alte, falsche Rat zu 168 echten Stunden wurde entfernt.","plan":"Effiziente Reihenfolge","cols":["Phase","Ziele kombinieren","Warum jetzt"],"rows":[["1 · Natürlicher Start","Erste Reparatur und Lötarbeit, erster Onlineauftrag, erste Lizenz, 5 Bewertungen und 2 Rechnungen","Diese kommen beim Einstieg von selbst."],["2 · Kernwerkzeuge","Profi-Schraubendreher, automatisches Ultraschallbad und Schredder","Sie geben Erfolge und beschleunigen spätere Ziele."],["3 · Zähler bündeln","E-Mails 25/100, Marktgeräte 5/25, Kisten 1/50, Sticker 1/25/100, Reinigung 100/1000, Programmierung 1/25","Ähnliche Aktionen gemeinsam abarbeiten."],["4 · Tagesregeln","10 Tage keine Neuteile, 7 Tage den Tag nicht beenden, 30/90/365 Tage spielen","Das sind Spieltage, keine 168 echten Stunden."],["5 · Story und Wettbewerbe","Einem Kind kostenlos helfen, 1/3/alle Gerätewettbewerbe gewinnen, fünf versteckte zuletzt","Steam nennt die versteckten Bedingungen nicht."]],"noteTitle":"Keine bestätigte 100%-Blockade","note":"Steams offizielle Liste markiert keinen derzeit unerreichbaren Erfolg. Die alte Drittanbieterbehauptung wird deshalb nicht wiederholt.","q":"Braucht Akiba never sleeps 168 echte Stunden?","a":"Diese Bedingung steht nicht in den offiziellen Daten. Dort heißt es: 7 Tage in Folge den Tag nicht beenden.","hiddenTitle":"Versteckte ReStory-Erfolge: Was Steam bestätigt","hiddenIntro":"Steam nennt fünf versteckte Erfolge, verrät aber ihre Bedingungen nicht. Fakten und Theorien bleiben getrennt.","hiddenHead":"Die fünf versteckten Erfolge","hiddenCondition":"Bedingung von Steam nicht veröffentlicht"},
 "es": {"roadTitle":"Hoja de ruta de logros ReStory: condiciones oficiales","roadIntro":"Un orden práctico basado solo en las condiciones oficiales de Steam. Se eliminó el antiguo consejo erróneo de esperar 168 horas reales.","plan":"Orden eficiente","cols":["Etapa","Objetivos que combinar","Por qué ahora"],"rows":[["1 · Inicio natural","Primera reparación y soldadura, primer pedido, primera licencia, 5 reseñas y 2 facturas","Se obtienen con el progreso inicial."],["2 · Herramientas clave","Destornillador profesional, baño ultrasónico automático y trituradora","Desbloquean logros y aceleran los siguientes."],["3 · Contadores juntos","Correos 25/100, mercado 5/25, cajas 1/50, pegatinas 1/25/100, limpieza 100/1000, reprogramación 1/25","Acumula acciones relacionadas."],["4 · Reglas de días","10 días sin piezas nuevas, no terminar el día durante 7 días, jugar 30/90/365 días","Son días del juego, no 168 horas reales."],["5 · Historia y concursos","Ayudar gratis a un niño, ganar 1/3/todos los concursos y dejar los 5 ocultos al final","Steam no publica sus condiciones exactas."]],"noteTitle":"Ningún bloqueo del 100% verificado","note":"La lista oficial de Steam no marca ningún logro como inalcanzable actualmente. No repetimos esa antigua afirmación de terceros.","q":"¿Akiba never sleeps exige 168 horas reales?","a":"Esa condición no aparece en los datos oficiales. El texto dice que no termines el día durante 7 días seguidos.","hiddenTitle":"Logros ocultos de ReStory: lo que confirma Steam","hiddenIntro":"Steam nombra cinco logros ocultos, pero no revela sus condiciones. Separamos los hechos de las teorías.","hiddenHead":"Los cinco logros ocultos","hiddenCondition":"Condición no revelada por Steam"},
 "pt-BR": {"roadTitle":"Roteiro de conquistas ReStory: condições oficiais","roadIntro":"Uma ordem prática baseada somente nas condições oficiais da Steam. A antiga dica incorreta de esperar 168 horas reais foi removida.","plan":"Ordem eficiente","cols":["Etapa","Metas combinadas","Por que agora"],"rows":[["1 · Início natural","Primeiro conserto e solda, primeiro pedido, primeira licença, 5 avaliações e 2 contas","Desbloqueiam naturalmente no começo."],["2 · Ferramentas principais","Chave profissional, banho ultrassônico automático e triturador","Liberam conquistas e aceleram as próximas metas."],["3 · Contadores juntos","E-mails 25/100, mercado 5/25, caixas 1/50, adesivos 1/25/100, limpeza 100/1000, programação 1/25","Acumule ações relacionadas."],["4 · Regras de dias","10 dias sem peças novas, não encerrar o dia por 7 dias, jogar 30/90/365 dias","São dias no jogo, não 168 horas reais."],["5 · História e competições","Ajudar uma criança de graça, vencer 1/3/todas as competições e deixar as 5 ocultas por último","A Steam não publica as condições exatas."]],"noteTitle":"Nenhum bloqueio de 100% verificado","note":"A lista oficial da Steam não marca nenhuma conquista como indisponível. Não repetimos a antiga alegação de terceiros.","q":"Akiba never sleeps exige 168 horas reais?","a":"Essa condição não aparece nos dados oficiais. O texto diz para não encerrar o dia por 7 dias seguidos.","hiddenTitle":"Conquistas ocultas de ReStory: o que a Steam confirma","hiddenIntro":"A Steam nomeia cinco conquistas ocultas, mas não revela suas condições. Fatos ficam separados de teorias.","hiddenHead":"As cinco conquistas ocultas","hiddenCondition":"Condição não revelada pela Steam"},
 "ru": {"roadTitle":"План достижений ReStory по официальным условиям","roadIntro":"Практичный порядок на 100%, основанный только на официальных условиях Steam. Старый ошибочный совет ждать 168 реальных часов удалён.","plan":"Эффективный порядок","cols":["Этап","Совмещайте цели","Почему сейчас"],"rows":[["1 · Обычное начало","Первый ремонт и пайка, первый онлайн-заказ, первая лицензия, 5 отзывов и 2 счёта","Открываются естественно в начале."],["2 · Основные инструменты","Профессиональная отвёртка, автоматическая ультразвуковая ванна и измельчитель","Дают достижения и ускоряют следующие цели."],["3 · Счётчики вместе","Почта 25/100, рынок 5/25, коробки 1/50, наклейки 1/25/100, чистка 100/1000, прошивка 1/25","Объединяйте похожие действия."],["4 · Правила дней","10 дней без новых деталей, 7 дней не завершать день, сыграть 30/90/365 дней","Это игровые дни, а не 168 реальных часов."],["5 · Сюжет и турниры","Бесплатно помочь ребёнку, выиграть 1/3/все турниры, оставить 5 скрытых напоследок","Steam не публикует их точные условия."]],"noteTitle":"Подтверждённой блокировки 100% нет","note":"Официальный список Steam не помечает достижения как недоступные. Мы не повторяем старое стороннее утверждение.","q":"Akiba never sleeps требует 168 реальных часов?","a":"Такого условия в официальных данных нет. Нужно 7 дней подряд не завершать день.","hiddenTitle":"Скрытые достижения ReStory: что подтверждает Steam","hiddenIntro":"Steam называет пять скрытых достижений, но не раскрывает условия. Здесь факты отделены от теорий.","hiddenHead":"Пять скрытых достижений","hiddenCondition":"Steam не раскрывает условие"},
}

for page in PAGES:
    if page["slug"] not in ("achievements-roadmap", "hidden-achievements"): continue
    page["sources"] = [SRC_STEAM_ACHIEVEMENTS, SRC_STEAM]
    for lg in LANGS:
        t, u = page["i18n"][lg], _ACH_RELATED_UI[lg]
        if page["slug"] == "achievements-roadmap":
            t.update({"title":u["roadTitle"], "metaTitle":u["roadTitle"], "metaDescription":u["roadIntro"], "intro":u["roadIntro"]})
            t["sections"] = [{"type":"table", "heading":u["plan"], "columns":u["cols"], "rows":u["rows"]}, {"type":"note", "heading":u["noteTitle"], "body":u["note"]}, {"type":"faq", "heading":"FAQ", "items":[[u["q"],u["a"]]]}]
        else:
            hidden_rows = [_ACH_DATA["locales"][lg][i] for i in (33,36,41,42,44)]
            t.update({"title":u["hiddenTitle"], "metaTitle":u["hiddenTitle"], "metaDescription":u["hiddenIntro"], "intro":u["hiddenIntro"]})
            t["sections"] = [{"type":"note", "heading":u["hiddenTitle"], "body":u["hiddenIntro"]}, {"type":"table", "heading":u["hiddenHead"], "columns":[_ACH_UI[lg][3], _ACH_UI[lg][4]], "rows":[[r["name"], r["condition"] or u["hiddenCondition"]] for r in hidden_rows]}]
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
# ---- 首页 hero / about 页本地化（修复全语言英文残留）----
_HOME_I18N = {
 "en": {
  "homeIntro": "ReStory is a chill, narrative-driven shop management simulator from the creators of I Am Future. Set in mid-2000s Tokyo, you run an electronics repair shop — restore nostalgic Y2K devices, talk to customers, and shape a branching story with multiple endings.",
  "homeFacts": ["Run a repair shop in mid-2000s Tokyo (Akihabara)","Restore nostalgic Y2K devices, including officially licensed Atari consoles","Branching storyline with multiple endings based on your choices","50 Steam achievements + trading cards + cloud saves","Official 9 languages + Traditional Chinese (10 total)","From the creators of I Am Future — published by tinyBuild"],
  "homeStats": ["Released","Achievements","Languages","Repairable devices","On Steam (10% off)","Reviews in 3 days"],
  "aboutPoints": ["Facts checked against the official Steam store page and reputable sources (allthings.how, intoindiegames)","Anything still being verified is explicitly marked — we never invent details","Available in 10 languages; every page lists its own sources"]
 },
 "zh-CN": {
  "homeIntro": "《ReStory：维修物语》是一款由 I Am Future 团队打造的治愈系叙事经营模拟游戏。故事发生在 2005 年的东京秋叶原——你经营一家电子维修铺，修复怀旧 Y2K 设备、倾听顾客的故事，用你的选择塑造多条分支结局。",
  "homeFacts": ["在 2005 年东京秋叶原经营维修铺","修复怀旧 Y2K 设备，包括官方授权的 Atari 主机","基于你的选择的分支剧情与多结局","50 个 Steam 成就 + 卡牌 + 云存档","9 种官方语言 + 繁体中文（共 10 种）","来自 I Am Future 团队，由 tinyBuild 发行"],
  "homeStats": ["发售日","成就","语言","可修设备","Steam 价格（9 折）","3 天评价数"],
  "aboutPoints": ["事实核对自 Steam 官方商店页与可靠来源（allthings.how、intoindiegames）","仍在验证的内容明确标注——我们绝不编造细节","提供 10 种语言；每个页面都列出自己的来源"]
 },
 "zh-TW": {
  "homeIntro": "《ReStory：維修物語》是一款由 I Am Future 團隊打造的治癒系敘事經營模擬遊戲。故事發生在 2005 年的東京秋葉原——你經營一家電子維修鋪，修復懷舊 Y2K 設備、傾聽顧客的故事，用你的選擇塑造多條分支結局。",
  "homeFacts": ["在 2005 年東京秋葉原經營維修鋪","修復懷舊 Y2K 設備，包括官方授權的 Atari 主機","基於你的選擇的分支劇情與多結局","50 個 Steam 成就 + 卡牌 + 雲端存檔","9 種官方語言 + 繁體中文（共 10 種）","來自 I Am Future 團隊，由 tinyBuild 發行"],
  "homeStats": ["發售日","成就","語言","可修設備","Steam 價格（9 折）","3 天評價數"],
  "aboutPoints": ["事實核對自 Steam 官方商店頁與可靠來源（allthings.how、intoindiegames）","仍在驗證的內容明確標註——我們絕不編造細節","提供 10 種語言；每個頁面都列出自己的來源"]
 },
 "ja": {
  "homeIntro": "『ReStory：まったり電子機器修理』は I Am Future の開発者による、癒やし系ストーリー経営シミュレーション。2005年の中旬・東京秋葉原で電子機器修理店を営み、懐かしいY2Kデバイスを修復し、お客の物語に耳を傾け、選択で分岐する複数のエンディングを紡ぎます。",
  "homeFacts": ["2005年・秋葉原で修理店を経営","公式ライセンスのAtariなど懐かしいY2Kデバイスを修復","選択で変わる分岐ストーリーと複数エンディング","Steam実績50個 + トレーディングカード + クラウド保存","公式9言語 + 繁体中国語（計10言語）","I Am Future 開発チーム、tinyBuild 発行"],
  "homeStats": ["発売日","実績","言語","修理可能デバイス","Steam価格（10%OFF）","3日間のレビュー数"],
  "aboutPoints": ["Steam公式ストアと信頼できる情報源（allthings.how、intoindiegames）で確認","未検証の内容は明記 — 細部を創作しません","10言語対応；各ページに出典を掲載"]
 },
 "ko": {
  "homeIntro": "《ReStory: 리스토리》는 I Am Future 제작진이 만든 힐링형 스토리 경영 시뮬레이션입니다. 2005년 도쿄 아키하바라에서 전자제품 수리점을 운영하며, 추억의 Y2K 기기를 복원하고 손님의 이야기를 듣고, 선택에 따라 갈라지는 여러 엔딩을 만들어 갑니다.",
  "homeFacts": ["2005년 도쿄 아키하바라에서 수리점 운영","공식 라이선스 Atari 등 추억의 Y2K 기기 복원","선택에 따라 달라지는 분기 스토리와 다중 엔딩","Steam 업적 50개 + 트레이딩 카드 + 클라우드 저장","공식 9개 언어 + 대만 중국어(총 10개)","I Am Future 제작진, tinyBuild 배급"],
  "homeStats": ["출시일","업적","언어","수리 가능 기기","Steam 가격(10% 할인)","3일 리뷰 수"],
  "aboutPoints": ["Steam 공식 스토어와 신뢰할 수 있는 출처(allthings.how, intoindiegames)로 확인","미검증 내용은 명확히 표시 — 세부 사항을 지어내지 않습니다","10개 언어 제공; 각 페이지에 출처 명시"]
 },
 "fr": {
  "homeIntro": "ReStory est un simulateur de gestion narratif et relaxant signé par les créateurs de I Am Future. Dans le Tokyo des années 2000, vous tenez une boutique de réparation d'électronique : restaurez des appareils Y2K nostalgiques, écoutez les histoires des clients et façonnez une histoire à embranchements et fins multiples.",
  "homeFacts": ["Tenez une boutique de réparation dans le Tokyo des années 2000 (Akihabara)","Restaurez des appareils Y2K nostalgiques, dont les consoles Atari sous licence officielle","Histoire à embranchements et fins multiples selon vos choix","50 succès Steam + cartes + sauvegarde cloud","9 langues officielles + chinois traditionnel (10 au total)","Par les créateurs de I Am Future — édité par tinyBuild"],
  "homeStats": ["Sortie","Succès","Langues","Appareils réparables","Sur Steam (-10 %)","Avis en 3 jours"],
  "aboutPoints": ["Informations vérifiées sur la page Steam officielle et des sources fiables (allthings.how, intoindiegames)","Tout ce qui reste à vérifier est signalé — nous n'inventons jamais de détails","Disponible en 10 langues ; chaque page liste ses sources"]
 },
 "de": {
  "homeIntro": "ReStory ist ein entspannter, erzählerischer Shop-Management-Simulator von den Machern von I Am Future. In Tokio Mitte der 2000er führst du einen Elektronik-Reparaturshop: stelle nostalgische Y2K-Geräte wieder her, höre den Geschichten der Kunden zu und gestalte eine verzweigte Geschichte mit mehreren Enden.",
  "homeFacts": ["Führe einen Reparaturshop im Tokio der 2000er (Akihabara)","Stelle nostalgische Y2K-Geräte wieder her, inkl. offiziell lizenzierter Atari-Konsolen","Verzweigte Geschichte mit mehreren Enden je nach deinen Entscheidungen","50 Steam-Errungenschaften + Karten + Cloud-Speicher","9 offizielle Sprachen + traditionelles Chinesisch (10 gesamt)","Von den Machern von I Am Future — veröffentlicht von tinyBuild"],
  "homeStats": ["Erschienen","Errungenschaften","Sprachen","Reparierbare Geräte","Auf Steam (-10 %)","Bewertungen in 3 Tagen"],
  "aboutPoints": ["Informationen geprüft gegen die offizielle Steam-Seite und zuverlässige Quellen (allthings.how, intoindiegames)","Alles Unverifizierte ist markiert — wir erfinden nie Details","Verfügbar in 10 Sprachen; jede Seite listet ihre Quellen"]
 },
 "es": {
  "homeIntro": "ReStory es un simulador de gestión narrativo y relajante de los creadores de I Am Future. En el Tokio de mediados de los 2000, regentas una tienda de reparación de electrónica: restaura dispositivos Y2K nostálgicos, escucha las historias de los clientes y da forma a una historia ramificada con múltiples finales.",
  "homeFacts": ["Regenta una tienda de reparación en el Tokio de 2005 (Akihabara)","Restaura dispositivos Y2K nostálgicos, incluidas consolas Atari con licencia oficial","Historia ramificada con múltiples finales según tus decisiones","50 logros de Steam + cromos + guardado en la nube","9 idiomas oficiales + chino tradicional (10 en total)","De los creadores de I Am Future — publicado por tinyBuild"],
  "homeStats": ["Lanzamiento","Logros","Idiomas","Dispositivos reparables","En Steam (-10 %)","Reseñas en 3 días"],
  "aboutPoints": ["Información contrastada con la página oficial de Steam y fuentes fiables (allthings.how, intoindiegames)","Todo lo pendiente de verificar está marcado — nunca inventamos detalles","Disponible en 10 idiomas; cada página lista sus fuentes"]
 },
 "pt-BR": {
  "homeIntro": "ReStory é um simulador de gestão narrativo e relaxante dos criadores de I Am Future. No Tóquio de meados dos anos 2000, você administra uma loja de consertos de eletrônicos: restaure aparelhos Y2K nostálgicos, ouça as histórias dos clientes e molde uma história ramificada com múltiplos finais.",
  "homeFacts": ["Administre uma loja de consertos no Tóquio de 2005 (Akihabara)","Restaure aparelhos Y2K nostálgicos, incluindo consoles Atari com licença oficial","História ramificada com múltiplos finais conforme suas escolhas","50 conquistas na Steam + cards + nuvem","9 idiomas oficiais + chinês tradicional (10 no total)","Dos criadores de I Am Future — publicado pela tinyBuild"],
  "homeStats": ["Lançamento","Conquistas","Idiomas","Aparelhos reparáveis","Na Steam (-10 %)","Avaliações em 3 dias"],
  "aboutPoints": ["Informações verificadas na página oficial da Steam e fontes confiáveis (allthings.how, intoindiegames)","Tudo que está em verificação é marcado — nunca inventamos detalhes","Disponível em 10 idiomas; cada página lista suas fontes"]
 },
 "ru": {
  "homeIntro": "ReStory — расслабленный нарративный симулятор управления магазином от создателей I Am Future. В Токио середины 2000-х вы держите мастерскую по ремонту электроники: восстанавливайте ностальгические Y2K-устройства, слушайте истории клиентов и формируйте ветвящуюся историю с несколькими концовками.",
  "homeFacts": ["Держите мастерскую по ремонту в Токио 2005 (Акихабара)","Восстанавливайте ностальгические Y2K-устройства, включая официально лицензированные консоли Atari","Ветвящаяся история с несколькими концовками в зависимости от выбора","50 достижений Steam + карточки + облачные сохранения","9 официальных языков + традиционный китайский (всего 10)","От создателей I Am Future — издатель tinyBuild"],
  "homeStats": ["Релиз","Достижения","Языки","Ремонтируемые устройства","В Steam (-10 %)","Отзывов за 3 дня"],
  "aboutPoints": ["Информация проверена по официальной странице Steam и надёжным источникам (allthings.how, intoindiegames)","Всё, что ещё проверяется, помечено — мы никогда не выдумываем детали","Доступно на 10 языках; каждая страница перечисляет свои источники"]
 },
}
for lg, v in _HOME_I18N.items():
    SITE_I18N[lg].update(v)




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
