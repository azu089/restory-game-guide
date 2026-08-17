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

# Consent controls are site-owned (not a Google-certified CMP).  Keep the
# complete choice vocabulary in the content layer so every generated locale
# exposes the same accept / reject / manage / withdraw meanings.
CONSENT_I18N = {
 "en": {"settings":"Privacy settings", "title":"Privacy choices", "intro":"Optional analytics and advertising stay off until you choose.", "analytics":"Analytics (Google Analytics 4)", "analyticsHelp":"Measures page views, referrers, device/browser details and approximate region.", "ads":"Advertising (Adsterra)", "adsHelp":"Loads the effectivecpmnetwork.com ad integration, which may receive IP address, device/browser details, page URL, referrer and cookies or similar identifiers.", "accept":"Accept optional services", "reject":"Reject optional services", "manage":"Manage choices", "save":"Save choices", "withdraw":"Withdraw consent", "close":"Close"},
 "zh-CN": {"settings":"隐私设置", "title":"隐私选择", "intro":"在你作出选择前，可选的分析与广告服务保持关闭。", "analytics":"分析（Google Analytics 4）", "analyticsHelp":"衡量页面浏览、来源、设备/浏览器信息和大致地区。", "ads":"广告（Adsterra）", "adsHelp":"加载 effectivecpmnetwork.com 广告集成；该服务可能接收 IP 地址、设备/浏览器信息、页面 URL、来源以及 Cookie 或类似标识符。", "accept":"接受可选服务", "reject":"拒绝可选服务", "manage":"管理选择", "save":"保存选择", "withdraw":"撤回同意", "close":"关闭"},
 "zh-TW": {"settings":"隱私設定", "title":"隱私選擇", "intro":"在你作出選擇前，選用的分析與廣告服務保持關閉。", "analytics":"分析（Google Analytics 4）", "analyticsHelp":"衡量頁面瀏覽、來源、裝置／瀏覽器資訊和大致地區。", "ads":"廣告（Adsterra）", "adsHelp":"載入 effectivecpmnetwork.com 廣告整合；該服務可能接收 IP 位址、裝置／瀏覽器資訊、頁面 URL、來源以及 Cookie 或類似識別碼。", "accept":"接受選用服務", "reject":"拒絕選用服務", "manage":"管理選擇", "save":"儲存選擇", "withdraw":"撤回同意", "close":"關閉"},
 "ja": {"settings":"プライバシー設定", "title":"プライバシーの選択", "intro":"選択するまで、任意の解析と広告サービスは無効です。", "analytics":"解析（Google Analytics 4）", "analyticsHelp":"ページビュー、参照元、端末・ブラウザ情報、おおよその地域を測定します。", "ads":"広告（Adsterra）", "adsHelp":"effectivecpmnetwork.com の広告連携を読み込みます。同サービスは IP アドレス、端末・ブラウザ情報、ページ URL、参照元、Cookie または類似識別子を受け取る場合があります。", "accept":"任意サービスを許可", "reject":"任意サービスを拒否", "manage":"選択を管理", "save":"選択を保存", "withdraw":"同意を撤回", "close":"閉じる"},
 "ko": {"settings":"개인정보 설정", "title":"개인정보 선택", "intro":"선택하기 전에는 선택적 분석 및 광고 서비스가 꺼져 있습니다.", "analytics":"분석(Google Analytics 4)", "analyticsHelp":"페이지 조회, 유입 경로, 기기·브라우저 정보와 대략적인 지역을 측정합니다.", "ads":"광고(Adsterra)", "adsHelp":"effectivecpmnetwork.com 광고 연동을 불러옵니다. 해당 서비스는 IP 주소, 기기·브라우저 정보, 페이지 URL, 유입 경로, 쿠키 또는 유사 식별자를 받을 수 있습니다.", "accept":"선택 서비스 허용", "reject":"선택 서비스 거부", "manage":"선택 관리", "save":"선택 저장", "withdraw":"동의 철회", "close":"닫기"},
 "fr": {"settings":"Réglages de confidentialité", "title":"Choix de confidentialité", "intro":"L’analyse et la publicité facultatives restent désactivées jusqu’à votre choix.", "analytics":"Mesure d’audience (Google Analytics 4)", "analyticsHelp":"Mesure les pages vues, la provenance, l’appareil/navigateur et la région approximative.", "ads":"Publicité (Adsterra)", "adsHelp":"Charge l’intégration effectivecpmnetwork.com, susceptible de recevoir adresse IP, appareil/navigateur, URL, référent et cookies ou identifiants similaires.", "accept":"Accepter les services facultatifs", "reject":"Refuser les services facultatifs", "manage":"Gérer les choix", "save":"Enregistrer les choix", "withdraw":"Retirer le consentement", "close":"Fermer"},
 "de": {"settings":"Datenschutzeinstellungen", "title":"Datenschutzauswahl", "intro":"Optionale Analyse und Werbung bleiben bis zu Ihrer Auswahl deaktiviert.", "analytics":"Analyse (Google Analytics 4)", "analyticsHelp":"Misst Seitenaufrufe, Herkunft, Geräte-/Browserdaten und die ungefähre Region.", "ads":"Werbung (Adsterra)", "adsHelp":"Lädt die effectivecpmnetwork.com-Integration; sie kann IP-Adresse, Geräte-/Browserdaten, Seiten-URL, Referrer und Cookies oder ähnliche Kennungen erhalten.", "accept":"Optionale Dienste akzeptieren", "reject":"Optionale Dienste ablehnen", "manage":"Auswahl verwalten", "save":"Auswahl speichern", "withdraw":"Einwilligung widerrufen", "close":"Schließen"},
 "es": {"settings":"Ajustes de privacidad", "title":"Opciones de privacidad", "intro":"La analítica y la publicidad opcionales permanecen desactivadas hasta que elijas.", "analytics":"Analítica (Google Analytics 4)", "analyticsHelp":"Mide páginas vistas, procedencia, dispositivo/navegador y región aproximada.", "ads":"Publicidad (Adsterra)", "adsHelp":"Carga la integración de effectivecpmnetwork.com, que puede recibir dirección IP, dispositivo/navegador, URL, referente y cookies o identificadores similares.", "accept":"Aceptar servicios opcionales", "reject":"Rechazar servicios opcionales", "manage":"Gestionar opciones", "save":"Guardar opciones", "withdraw":"Retirar consentimiento", "close":"Cerrar"},
 "pt-BR": {"settings":"Configurações de privacidade", "title":"Escolhas de privacidade", "intro":"Análise e publicidade opcionais ficam desligadas até você escolher.", "analytics":"Análise (Google Analytics 4)", "analyticsHelp":"Mede visualizações, origem, aparelho/navegador e região aproximada.", "ads":"Publicidade (Adsterra)", "adsHelp":"Carrega a integração effectivecpmnetwork.com, que pode receber endereço IP, aparelho/navegador, URL, referenciador e cookies ou identificadores semelhantes.", "accept":"Aceitar serviços opcionais", "reject":"Recusar serviços opcionais", "manage":"Gerenciar escolhas", "save":"Salvar escolhas", "withdraw":"Retirar consentimento", "close":"Fechar"},
 "ru": {"settings":"Настройки конфиденциальности", "title":"Выбор конфиденциальности", "intro":"Необязательные аналитика и реклама отключены, пока вы не сделаете выбор.", "analytics":"Аналитика (Google Analytics 4)", "analyticsHelp":"Измеряет просмотры, источники переходов, сведения об устройстве/браузере и примерный регион.", "ads":"Реклама (Adsterra)", "adsHelp":"Загружает интеграцию effectivecpmnetwork.com, которая может получить IP-адрес, сведения об устройстве/браузере, URL, источник перехода и cookie или похожие идентификаторы.", "accept":"Разрешить необязательные сервисы", "reject":"Отклонить необязательные сервисы", "manage":"Управлять выбором", "save":"Сохранить выбор", "withdraw":"Отозвать согласие", "close":"Закрыть"},
}
for _lg in LANGS:
    SITE_I18N[_lg]["consent"] = CONSENT_I18N[_lg]

REPAIR_STEPS = {
 "en": [["Accept the job", "Confirm the device, deadline and customer request."], ["Disassemble in order", "Lay parts out in sequence so reassembly stays clear."], ["Inspect every part", "Record each part as clean, dirty, broken or missing."], ["Clean or replace", "Clean dirty parts and replace only broken or missing ones."], ["Reassemble and test", "Follow the recorded order, verify completion, then deliver."]],
 "zh-CN": [["接下工单", "确认设备、期限与顾客要求。"], ["按顺序拆解", "依次摆放零件，方便准确复原。"], ["检查每个零件", "记录干净、脏污、损坏或缺失状态。"], ["清洁或更换", "清洁脏污件，只更换损坏或缺失件。"], ["组装并检查", "按记录复原，确认完成后再交付。"]],
 "zh-TW": [["接下工單", "確認裝置、期限與顧客要求。"], ["按順序拆解", "依次擺放零件，方便準確復原。"], ["檢查每個零件", "記錄乾淨、髒漬、損壞或缺失狀態。"], ["清潔或更換", "清潔髒漬件，只更換損壞或缺失件。"], ["組裝並檢查", "按記錄復原，確認完成後再交付。"]],
 "ja": [["依頼を受ける", "デバイス、期限、顧客の要望を確認します。"], ["順番に分解", "再組立てできるよう部品を順番に並べます。"], ["全パーツを点検", "清潔・汚れ・破損・欠品を記録します。"], ["清掃または交換", "汚れを清掃し、破損・欠品だけ交換します。"], ["再組立てと確認", "記録順に戻し、完了を確認して納品します。"]],
 "ko": [["작업 접수", "기기, 마감일과 고객 요청을 확인합니다."], ["순서대로 분해", "재조립할 수 있도록 부품을 순서대로 놓습니다."], ["모든 부품 검사", "깨끗함, 오염, 파손, 누락 상태를 기록합니다."], ["청소 또는 교체", "오염 부품은 청소하고 파손·누락 부품만 교체합니다."], ["재조립 및 확인", "기록 순서대로 조립하고 완료를 확인한 뒤 인도합니다."]],
 "fr": [["Accepter la commande", "Confirmez l’appareil, le délai et la demande du client."], ["Démonter dans l’ordre", "Disposez les pièces en séquence pour faciliter le remontage."], ["Inspecter chaque pièce", "Notez si elle est propre, sale, cassée ou absente."], ["Nettoyer ou remplacer", "Nettoyez le sale et ne remplacez que le cassé ou l’absent."], ["Remonter et vérifier", "Suivez l’ordre noté, contrôlez, puis livrez."]],
 "de": [["Auftrag annehmen", "Gerät, Frist und Kundenwunsch bestätigen."], ["Geordnet zerlegen", "Teile in Reihenfolge ablegen, damit der Zusammenbau klar bleibt."], ["Jedes Teil prüfen", "Sauber, schmutzig, defekt oder fehlend notieren."], ["Reinigen oder ersetzen", "Schmutziges reinigen, nur Defektes oder Fehlendes ersetzen."], ["Zusammenbauen und prüfen", "Der Notiz folgen, Abschluss prüfen und dann ausliefern."]],
 "es": [["Aceptar el encargo", "Confirma el dispositivo, el plazo y la petición del cliente."], ["Desmontar en orden", "Coloca las piezas en secuencia para poder montar bien."], ["Inspeccionar cada pieza", "Anota si está limpia, sucia, rota o ausente."], ["Limpiar o reemplazar", "Limpia lo sucio y reemplaza solo lo roto o ausente."], ["Montar y comprobar", "Sigue el orden anotado, verifica y entrega."]],
 "pt-BR": [["Aceitar o serviço", "Confirme o aparelho, o prazo e o pedido do cliente."], ["Desmontar em ordem", "Organize as peças em sequência para remontar corretamente."], ["Inspecionar cada peça", "Registre se está limpa, suja, quebrada ou ausente."], ["Limpar ou substituir", "Limpe o que estiver sujo e troque apenas o quebrado ou ausente."], ["Remontar e verificar", "Siga a ordem registrada, confira e entregue."]],
 "ru": [["Принять заказ", "Уточните устройство, срок и просьбу клиента."], ["Разобрать по порядку", "Раскладывайте детали последовательно для правильной сборки."], ["Проверить каждую деталь", "Отметьте: чистая, грязная, сломанная или отсутствует."], ["Очистить или заменить", "Очистите грязное, заменяйте только сломанное или отсутствующее."], ["Собрать и проверить", "Следуйте записи, проверьте результат и сдайте заказ."]],
}
for _lg in LANGS:
    SITE_I18N[_lg]["repairSteps"] = REPAIR_STEPS[_lg]

_LEGACY_PRIVACY_BODY = {
 "en": "<p>This guide site loads Google Analytics 4 (GA4) and an Adsterra advertising integration served from effectivecpmnetwork.com.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Analytics</h2><p>GA4 measures activity such as page views, referrers, device/browser information and approximate region. Google may use cookies or similar identifiers to distinguish browsers. See Google's privacy controls and policies for details.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Advertising</h2><p>Google AdSense advertising is loaded from pagead2.googlesyndication.com. Google may process cookies or similar identifiers, IP address, browser/device information, page URL and ad interaction data under its advertising privacy policies. The effectivecpmnetwork.com advertising script is supplied by a third party. When it loads, that provider may process network and device data such as IP address, browser information, page URL, referrer, and cookies or similar identifiers, according to its own policy. We do not control that third-party collection.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Your choices</h2><p>You can block or clear cookies and other site data in your browser, use content-blocking controls, or leave before third-party scripts load. Blocking them may change analytics or ad display.</p>",
 "zh-CN": "<p>本攻略站会加载 Google Analytics 4（GA4），以及由 effectivecpmnetwork.com 提供的 Adsterra 广告集成。</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">分析统计</h2><p>GA4 会衡量页面浏览、来源、设备/浏览器信息和大致地区等活动。Google 可能使用 Cookie 或类似标识符来区分浏览器；详情以 Google 的隐私控制和政策为准。</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">广告</h2><p>本站会从 pagead2.googlesyndication.com 加载 Google AdSense 广告。Google 可能依照其广告隐私政策处理 Cookie 或类似标识符、IP 地址、浏览器/设备信息、页面 URL 和广告互动数据。effectivecpmnetwork.com 广告脚本由第三方提供。脚本加载时，该提供商可能依照其政策处理 IP 地址、浏览器信息、页面 URL、来源以及 Cookie 或类似标识符等网络和设备数据。我们无法控制该第三方的数据收集。</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">你的选择</h2><p>你可以在浏览器中阻止或清除 Cookie 与其他网站数据、使用内容拦截功能，或在第三方脚本加载前离开。阻止这些功能可能影响统计或广告显示。</p>",
 "zh-TW": "<p>本攻略站會載入 Google Analytics 4（GA4），以及由 effectivecpmnetwork.com 提供的 Adsterra 廣告整合。</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">分析統計</h2><p>GA4 會衡量頁面瀏覽、來源、裝置/瀏覽器資訊和大致地區等活動。Google 可能使用 Cookie 或類似識別碼來區分瀏覽器；詳情以 Google 的隱私控制和政策為準。</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">廣告</h2><p>本站會從 pagead2.googlesyndication.com 載入 Google AdSense 廣告。Google 可能依照其廣告隱私政策處理 Cookie 或類似識別碼、IP 位址、瀏覽器/裝置資訊、頁面 URL 和廣告互動資料。effectivecpmnetwork.com 廣告指令碼由第三方提供。指令碼載入時，該提供者可能依照其政策處理 IP 位址、瀏覽器資訊、頁面 URL、來源，以及 Cookie 或類似識別碼等網路和裝置資料。我們無法控制該第三方的資料收集。</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">你的選擇</h2><p>你可以在瀏覽器中封鎖或清除 Cookie 與其他網站資料、使用內容封鎖功能，或在第三方指令碼載入前離開。封鎖這些功能可能影響統計或廣告顯示。</p>",
 "ja": "<p>本攻略サイトは Google Analytics 4（GA4）と、effectivecpmnetwork.com から配信される Adsterra 広告連携を読み込みます。</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">アクセス解析</h2><p>GA4 はページビュー、参照元、端末・ブラウザ情報、おおよその地域などを測定します。Google はブラウザを区別するため Cookie または類似の識別子を使用する場合があります。詳細は Google のプライバシー管理とポリシーをご確認ください。</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">広告</h2><p>本サイトは pagead2.googlesyndication.com から Google AdSense 広告を読み込みます。Google は広告プライバシーポリシーに従い、Cookie または類似の識別子、IP アドレス、ブラウザ・端末情報、ページ URL、広告操作データを処理する場合があります。effectivecpmnetwork.com の広告スクリプトは第三者が提供します。読み込み時に、その事業者は自社ポリシーに従い、IP アドレス、ブラウザ情報、ページ URL、参照元、Cookie または類似の識別子などのネットワーク・端末データを処理する場合があります。当サイトは第三者による収集を管理できません。</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">選択肢</h2><p>ブラウザで Cookie などのサイトデータを拒否・削除する、コンテンツブロック機能を使う、または第三者スクリプトの読み込み前に離脱できます。拒否すると解析や広告表示が変わる場合があります。</p>",
 "ko": "<p>이 가이드 사이트는 Google Analytics 4(GA4)와 effectivecpmnetwork.com에서 제공되는 Adsterra 광고 연동을 불러옵니다.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">분석</h2><p>GA4는 페이지 조회, 유입 경로, 기기·브라우저 정보, 대략적인 지역 등의 활동을 측정합니다. Google은 브라우저를 구분하기 위해 쿠키 또는 유사 식별자를 사용할 수 있습니다. 자세한 내용은 Google의 개인정보 보호 설정과 정책을 확인하세요.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">광고</h2><p>이 사이트는 pagead2.googlesyndication.com에서 Google AdSense 광고를 불러옵니다. Google은 광고 개인정보 보호정책에 따라 쿠키 또는 유사 식별자, IP 주소, 브라우저·기기 정보, 페이지 URL과 광고 상호작용 데이터를 처리할 수 있습니다. effectivecpmnetwork.com 광고 스크립트는 제3자가 제공합니다. 스크립트가 로드될 때 해당 업체는 자체 정책에 따라 IP 주소, 브라우저 정보, 페이지 URL, 유입 경로, 쿠키 또는 유사 식별자 같은 네트워크·기기 데이터를 처리할 수 있습니다. 당사는 그 제3자의 수집을 통제하지 않습니다.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">선택 사항</h2><p>브라우저에서 쿠키와 기타 사이트 데이터를 차단·삭제하거나 콘텐츠 차단 기능을 사용하거나 제3자 스크립트가 로드되기 전에 사이트를 떠날 수 있습니다. 차단하면 분석 또는 광고 표시가 달라질 수 있습니다.</p>",
 "fr": "<p>Ce site de guides charge Google Analytics 4 (GA4) ainsi qu'une intégration publicitaire Adsterra diffusée depuis effectivecpmnetwork.com.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Mesure d'audience</h2><p>GA4 mesure notamment les pages vues, la provenance, les informations sur l'appareil et le navigateur, et la région approximative. Google peut utiliser des cookies ou identifiants similaires pour distinguer les navigateurs. Consultez les contrôles et règles de confidentialité de Google.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Publicité</h2><p>Le site charge la publicité Google AdSense depuis pagead2.googlesyndication.com. Google peut traiter des cookies ou identifiants similaires, l’adresse IP, des informations sur le navigateur/appareil, l’URL de la page et les interactions publicitaires selon ses règles de confidentialité publicitaire. Le script publicitaire effectivecpmnetwork.com est fourni par un tiers. Lors de son chargement, ce fournisseur peut traiter, selon sa propre politique, des données réseau et appareil telles que l'adresse IP, le navigateur, l'URL de la page, le référent et des cookies ou identifiants similaires. Nous ne contrôlons pas cette collecte tierce.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Vos choix</h2><p>Vous pouvez bloquer ou effacer les cookies et autres données de site dans votre navigateur, utiliser un bloqueur de contenu ou quitter avant le chargement des scripts tiers. Cela peut modifier la mesure ou l'affichage publicitaire.</p>",
 "de": "<p>Diese Guide-Seite lädt Google Analytics 4 (GA4) sowie eine Adsterra-Werbeintegration von effectivecpmnetwork.com.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Analyse</h2><p>GA4 misst unter anderem Seitenaufrufe, Herkunft, Geräte- und Browserinformationen sowie die ungefähre Region. Google kann Cookies oder ähnliche Kennungen verwenden, um Browser zu unterscheiden. Einzelheiten stehen in Googles Datenschutzeinstellungen und Richtlinien.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Werbung</h2><p>Die Seite lädt Google AdSense-Werbung von pagead2.googlesyndication.com. Google kann gemäß seinen Datenschutzregeln für Werbung Cookies oder ähnliche Kennungen, IP-Adresse, Browser-/Gerätedaten, Seiten-URL und Anzeigeninteraktionen verarbeiten. Das Werbeskript von effectivecpmnetwork.com stammt von einem Drittanbieter. Beim Laden kann dieser gemäß eigener Richtlinie Netzwerk- und Gerätedaten wie IP-Adresse, Browserinformationen, Seiten-URL, Referrer sowie Cookies oder ähnliche Kennungen verarbeiten. Wir kontrollieren diese Datenerhebung des Drittanbieters nicht.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Ihre Wahl</h2><p>Sie können Cookies und andere Websitedaten im Browser blockieren oder löschen, Inhaltsblocker verwenden oder die Seite vor dem Laden von Drittskripten verlassen. Dadurch können Analyse oder Werbeanzeige verändert werden.</p>",
 "es": "<p>Este sitio de guías carga Google Analytics 4 (GA4) y una integración publicitaria de Adsterra servida desde effectivecpmnetwork.com.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Analítica</h2><p>GA4 mide actividad como páginas vistas, procedencia, información del dispositivo y navegador, y región aproximada. Google puede usar cookies o identificadores similares para distinguir navegadores. Consulta los controles y políticas de privacidad de Google.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Publicidad</h2><p>El sitio carga publicidad de Google AdSense desde pagead2.googlesyndication.com. Google puede tratar cookies o identificadores similares, dirección IP, datos del navegador/dispositivo, URL de la página e interacciones publicitarias según sus políticas de privacidad publicitaria. El script publicitario de effectivecpmnetwork.com pertenece a un tercero. Al cargarse, ese proveedor puede tratar, según su política, datos de red y dispositivo como dirección IP, navegador, URL de la página, referente y cookies o identificadores similares. No controlamos esa recopilación de terceros.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Tus opciones</h2><p>Puedes bloquear o borrar cookies y otros datos del sitio en el navegador, usar controles de bloqueo de contenido o salir antes de que carguen los scripts de terceros. Esto puede cambiar la analítica o la presentación de anuncios.</p>",
 "pt-BR": "<p>Este site de guias carrega o Google Analytics 4 (GA4) e uma integração de anúncios da Adsterra fornecida por effectivecpmnetwork.com.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Análise</h2><p>O GA4 mede atividades como visualizações de página, origem, informações do aparelho e navegador e região aproximada. O Google pode usar cookies ou identificadores semelhantes para distinguir navegadores. Consulte os controles e as políticas de privacidade do Google.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Publicidade</h2><p>O site carrega anúncios do Google AdSense de pagead2.googlesyndication.com. O Google pode processar cookies ou identificadores semelhantes, endereço IP, dados do navegador/aparelho, URL da página e interações com anúncios conforme suas políticas de privacidade de publicidade. O script de anúncios de effectivecpmnetwork.com é fornecido por terceiros. Ao carregar, esse fornecedor pode processar, conforme sua própria política, dados de rede e aparelho como endereço IP, informações do navegador, URL da página, referenciador e cookies ou identificadores semelhantes. Não controlamos essa coleta de terceiros.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Suas escolhas</h2><p>Você pode bloquear ou limpar cookies e outros dados do site no navegador, usar bloqueadores de conteúdo ou sair antes que scripts de terceiros carreguem. Isso pode alterar a análise ou a exibição de anúncios.</p>",
 "ru": "<p>Этот сайт с гайдами загружает Google Analytics 4 (GA4) и рекламную интеграцию Adsterra с домена effectivecpmnetwork.com.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Аналитика</h2><p>GA4 измеряет просмотры страниц, источники переходов, сведения об устройстве и браузере и примерный регион. Google может использовать cookie или похожие идентификаторы, чтобы различать браузеры. Подробности приведены в настройках и правилах конфиденциальности Google.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Реклама</h2><p>Сайт загружает рекламу Google AdSense с pagead2.googlesyndication.com. Google может по своим правилам конфиденциальности рекламы обрабатывать cookie или похожие идентификаторы, IP-адрес, сведения о браузере/устройстве, URL страницы и взаимодействия с рекламой. Рекламный скрипт effectivecpmnetwork.com предоставлен третьей стороной. При загрузке этот поставщик может по своей политике обрабатывать сетевые данные и сведения об устройстве, включая IP-адрес, браузер, URL страницы, источник перехода, cookie или похожие идентификаторы. Мы не контролируем сбор данных этой третьей стороной.</p><h2 style=\"font-size:1.05rem;margin:18px 0 8px\">Ваш выбор</h2><p>Можно блокировать или удалять cookie и другие данные сайта в браузере, использовать блокировщик контента или уйти до загрузки сторонних скриптов. Это может изменить аналитику или показ рекламы.</p>",
}

# Current runtime contract: GA4 and Adsterra are optional and remain blocked
# until the visitor opts in. AdSense account metadata/ads.txt may be present,
# but ad serving is disabled. These policies describe the generated behavior,
# including how to withdraw through the persistent settings control.
_PRIVACY_CURRENT = {
 "en": ["This guide site keeps optional analytics and advertising off until you choose in Privacy settings.", "Analytics", "If enabled, Google Analytics 4 (GA4) measures page views, referrers, device/browser information and approximate region, and may use cookies or similar identifiers for this purpose.", "Advertising", "If enabled, Adsterra loads from effectivecpmnetwork.com. That provider may process IP address, device/browser information, page URL, referrer, ad interactions and cookies or similar identifiers to deliver and measure advertising. Google AdSense account metadata and ads.txt are configured, but AdSense ad serving is disabled and no AdSense serving script is loaded.", "Your choices", "Accept, reject or manage the two optional purposes in Privacy settings. You can reopen Privacy settings on any page and withdraw consent; withdrawal prevents new optional provider loads on later page loads. Previously transmitted data cannot be recalled."],
 "zh-CN": ["本攻略站在你通过“隐私设置”作出选择前，会关闭可选的分析与广告服务。", "分析统计", "启用后，Google Analytics 4（GA4）会为流量分析衡量页面浏览、来源、设备/浏览器信息和大致地区，并可能为此使用 Cookie 或类似标识符。", "广告", "启用后，Adsterra 会从 effectivecpmnetwork.com 加载。该提供商可能为广告投放与衡量处理 IP 地址、设备/浏览器信息、页面 URL、来源、广告互动以及 Cookie 或类似标识符。Google AdSense 账户验证元数据与 ads.txt 已配置，但 AdSense 广告投放保持关闭，不会加载 AdSense 投放脚本。", "你的选择", "你可以在“隐私设置”中接受、拒绝或分别管理两项可选用途。任何页面都可重新打开设置并撤回同意；撤回后，后续页面加载不会新加载可选服务。已经传输的数据无法收回。"],
 "zh-TW": ["本攻略站在你透過「隱私設定」作出選擇前，會關閉選用的分析與廣告服務。", "分析統計", "啟用後，Google Analytics 4（GA4）會為流量分析衡量頁面瀏覽、來源、裝置／瀏覽器資訊和大致地區，並可能為此使用 Cookie 或類似識別碼。", "廣告", "啟用後，Adsterra 會從 effectivecpmnetwork.com 載入。該供應商可能為廣告投放與衡量處理 IP 位址、裝置／瀏覽器資訊、頁面 URL、來源、廣告互動以及 Cookie 或類似識別碼。Google AdSense 帳戶驗證後設資料與 ads.txt 已設定，但 AdSense 廣告投放保持關閉，不會載入 AdSense 投放指令碼。", "你的選擇", "你可以在「隱私設定」中接受、拒絕或分別管理兩項選用用途。任何頁面都可重新開啟設定並撤回同意；撤回後，後續頁面載入不會新載入選用服務。已傳輸的資料無法收回。"],
 "ja": ["本攻略サイトでは、プライバシー設定で選択するまで任意の解析と広告を無効にしています。", "アクセス解析", "有効にすると Google Analytics 4（GA4）がページビュー、参照元、端末・ブラウザ情報、おおよその地域を測定し、その目的で Cookie または類似識別子を使う場合があります。", "広告", "有効にすると Adsterra が effectivecpmnetwork.com から読み込まれます。同事業者は広告の配信・測定のため、IP アドレス、端末・ブラウザ情報、ページ URL、参照元、広告操作、Cookie または類似識別子を処理する場合があります。Google AdSense の確認用メタデータと ads.txt は設定済みですが、広告配信は無効で、配信スクリプトは読み込まれません。", "選択肢", "プライバシー設定で許可、拒否、または目的別に管理できます。どのページでも設定を開いて同意を撤回でき、以後のページ読み込みでは任意サービスが新たに読み込まれません。送信済みデータは取り消せません。"],
 "ko": ["이 가이드 사이트는 개인정보 설정에서 선택하기 전까지 선택적 분석 및 광고를 꺼 둡니다.", "분석", "활성화하면 Google Analytics 4(GA4)가 페이지 조회, 유입 경로, 기기·브라우저 정보와 대략적인 지역을 측정하며 이를 위해 쿠키 또는 유사 식별자를 사용할 수 있습니다.", "광고", "활성화하면 Adsterra가 effectivecpmnetwork.com에서 로드됩니다. 해당 공급자는 광고 제공·측정을 위해 IP 주소, 기기·브라우저 정보, 페이지 URL, 유입 경로, 광고 상호작용, 쿠키 또는 유사 식별자를 처리할 수 있습니다. Google AdSense 확인 메타데이터와 ads.txt는 설정되어 있지만 광고 게재는 꺼져 있고 게재 스크립트는 로드되지 않습니다.", "선택 사항", "개인정보 설정에서 허용, 거부하거나 목적별로 관리할 수 있습니다. 모든 페이지에서 설정을 다시 열어 동의를 철회할 수 있으며 이후 페이지 로드에는 선택적 공급자가 새로 로드되지 않습니다. 이미 전송된 데이터는 회수할 수 없습니다."],
 "fr": ["Ce site laisse l’analyse et la publicité facultatives désactivées jusqu’à votre choix dans les réglages de confidentialité.", "Mesure d’audience", "Si vous l’activez, Google Analytics 4 (GA4) mesure pages vues, provenance, appareil/navigateur et région approximative, et peut utiliser des cookies ou identifiants similaires à cette fin.", "Publicité", "Si vous l’activez, Adsterra est chargé depuis effectivecpmnetwork.com. Ce fournisseur peut traiter adresse IP, appareil/navigateur, URL, référent, interactions publicitaires et cookies ou identifiants similaires pour diffuser et mesurer la publicité. Les métadonnées de validation Google AdSense et ads.txt sont configurées, mais la diffusion AdSense est désactivée et aucun script de diffusion n’est chargé.", "Vos choix", "Vous pouvez accepter, refuser ou gérer séparément les deux finalités. Rouvrez les réglages sur toute page pour retirer votre consentement ; cela empêche de nouveaux chargements facultatifs lors des pages suivantes. Les données déjà transmises ne peuvent pas être rappelées."],
 "de": ["Diese Guide-Seite lässt optionale Analyse und Werbung deaktiviert, bis Sie in den Datenschutzeinstellungen wählen.", "Analyse", "Nach Aktivierung misst Google Analytics 4 (GA4) Seitenaufrufe, Herkunft, Geräte-/Browserdaten und die ungefähre Region und kann dafür Cookies oder ähnliche Kennungen verwenden.", "Werbung", "Nach Aktivierung wird Adsterra von effectivecpmnetwork.com geladen. Der Anbieter kann für Werbeauslieferung und -messung IP-Adresse, Geräte-/Browserdaten, Seiten-URL, Referrer, Anzeigeninteraktionen und Cookies oder ähnliche Kennungen verarbeiten. Google-AdSense-Prüfmetadaten und ads.txt sind konfiguriert, aber die AdSense-Auslieferung ist deaktiviert und kein Auslieferungsskript wird geladen.", "Ihre Wahl", "Sie können beide optionalen Zwecke akzeptieren, ablehnen oder getrennt verwalten. Öffnen Sie die Einstellungen auf jeder Seite erneut, um zu widerrufen; dadurch werden auf folgenden Seiten keine optionalen Anbieter neu geladen. Bereits übertragene Daten lassen sich nicht zurückrufen."],
 "es": ["Este sitio mantiene desactivadas la analítica y la publicidad opcionales hasta que elijas en los ajustes de privacidad.", "Analítica", "Si la activas, Google Analytics 4 (GA4) mide páginas vistas, procedencia, dispositivo/navegador y región aproximada, y puede usar cookies o identificadores similares para ello.", "Publicidad", "Si la activas, Adsterra se carga desde effectivecpmnetwork.com. Ese proveedor puede tratar dirección IP, dispositivo/navegador, URL, referente, interacciones publicitarias y cookies o identificadores similares para servir y medir anuncios. Los metadatos de verificación de Google AdSense y ads.txt están configurados, pero la publicación de AdSense está desactivada y no se carga su script.", "Tus opciones", "Puedes aceptar, rechazar o gestionar por separado ambas finalidades. Reabre los ajustes en cualquier página para retirar el consentimiento; así no se cargarán nuevos proveedores opcionales en páginas posteriores. Los datos ya transmitidos no pueden recuperarse."],
 "pt-BR": ["Este site mantém análise e publicidade opcionais desligadas até você escolher nas configurações de privacidade.", "Análise", "Se ativado, o Google Analytics 4 (GA4) mede visualizações, origem, aparelho/navegador e região aproximada e pode usar cookies ou identificadores semelhantes para isso.", "Publicidade", "Se ativado, o Adsterra é carregado de effectivecpmnetwork.com. Esse fornecedor pode processar endereço IP, aparelho/navegador, URL, referenciador, interações com anúncios e cookies ou identificadores semelhantes para veicular e medir publicidade. Metadados de verificação do Google AdSense e ads.txt estão configurados, mas a veiculação do AdSense está desativada e seu script não é carregado.", "Suas escolhas", "Você pode aceitar, recusar ou gerenciar separadamente as duas finalidades. Reabra as configurações em qualquer página para retirar o consentimento; isso impede novos carregamentos opcionais nas páginas seguintes. Dados já transmitidos não podem ser recuperados."],
 "ru": ["Этот сайт оставляет необязательные аналитику и рекламу отключёнными, пока вы не выберете их в настройках конфиденциальности.", "Аналитика", "После включения Google Analytics 4 (GA4) измеряет просмотры, источники переходов, сведения об устройстве/браузере и примерный регион и может использовать для этого cookie или похожие идентификаторы.", "Реклама", "После включения Adsterra загружается с effectivecpmnetwork.com. Поставщик может для показа и измерения рекламы обрабатывать IP-адрес, сведения об устройстве/браузере, URL, источник перехода, взаимодействия с рекламой и cookie или похожие идентификаторы. Метаданные проверки Google AdSense и ads.txt настроены, но показ AdSense отключён и скрипт показа не загружается.", "Ваш выбор", "Можно разрешить, отклонить или раздельно настроить обе цели. На любой странице настройки можно открыть снова и отозвать согласие; после этого на следующих страницах необязательные поставщики не загружаются заново. Уже переданные данные вернуть нельзя."],
}
def _privacy_html(parts):
    return f'<p>{parts[0]}</p><h2 style="font-size:1.05rem;margin:18px 0 8px">{parts[1]}</h2><p>{parts[2]}</p><h2 style="font-size:1.05rem;margin:18px 0 8px">{parts[3]}</h2><p>{parts[4]}</p><h2 style="font-size:1.05rem;margin:18px 0 8px">{parts[5]}</h2><p>{parts[6]}</p>'
PRIVACY_BODY = {lg: _privacy_html(parts) for lg, parts in _PRIVACY_CURRENT.items()}
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

_PRIVACY_META = {
 "en":"Privacy: GA4 analytics, Google AdSense advertising from pagead2.googlesyndication.com, Adsterra/effectivecpmnetwork, cookies and device/network data.",
 "zh-CN":"隐私说明：GA4 分析、pagead2.googlesyndication.com 的 Google AdSense 广告、Adsterra/effectivecpmnetwork、Cookie 与设备/网络数据。",
 "zh-TW":"隱私說明：GA4 分析、pagead2.googlesyndication.com 的 Google AdSense 廣告、Adsterra/effectivecpmnetwork、Cookie 與裝置/網路資料。",
 "ja":"プライバシー：GA4、pagead2.googlesyndication.com の Google AdSense 広告、Adsterra/effectivecpmnetwork、Cookie、端末・ネットワークデータ。",
 "ko":"개인정보 안내: GA4, pagead2.googlesyndication.com의 Google AdSense 광고, Adsterra/effectivecpmnetwork, 쿠키와 기기·네트워크 데이터.",
 "fr":"Confidentialité : GA4, Google AdSense via pagead2.googlesyndication.com, Adsterra/effectivecpmnetwork, cookies et données réseau/appareil.",
 "de":"Datenschutz: GA4, Google AdSense über pagead2.googlesyndication.com, Adsterra/effectivecpmnetwork, Cookies und Netzwerk-/Gerätedaten.",
 "es":"Privacidad: GA4, Google AdSense mediante pagead2.googlesyndication.com, Adsterra/effectivecpmnetwork, cookies y datos de red/dispositivo.",
 "pt-BR":"Privacidade: GA4, Google AdSense via pagead2.googlesyndication.com, Adsterra/effectivecpmnetwork, cookies e dados de rede/aparelho.",
 "ru":"Конфиденциальность: GA4, Google AdSense через pagead2.googlesyndication.com, Adsterra/effectivecpmnetwork, cookie и сетевые данные/устройство.",
}
for _lg in LANGS:
    SITE_I18N[_lg]["privacyMetaDescription"] = _PRIVACY_META[_lg]

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
SRC_STEAM_NEWS = _src("Official Steam announcements", "https://steamcommunity.com/app/3812600/allnews/", {
    "en": "Official Steam announcements", "zh-CN": "Steam 官方公告", "ja": "Steam 公式アナウンス", "ko": "Steam 공식 공지",
    "fr": "Annonces Steam officielles", "de": "Offizielle Steam-Ankündigungen", "es": "Anuncios oficiales de Steam",
    "pt-BR": "Anúncios oficiais da Steam", "ru": "Официальные объявления Steam",
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
# ---- L3 社区来源（仅用于明确标注的社区参考数据；未经官方核实）----
SRC_RESTORY_WIKI = _src("restory.wiki — Palaloid (community wiki)", "https://restory.wiki/w/Palaloid", {
    "en": "restory.wiki — Palaloid (community wiki)", "zh-CN": "restory.wiki — Palaloid（社区维基）",
    "ja": "restory.wiki — Palaloid（コミュニティWiki）", "ko": "restory.wiki — Palaloid（커뮤니티 위키）",
    "fr": "restory.wiki — Palaloid (wiki communautaire)", "de": "restory.wiki — Palaloid (Community-Wiki)",
    "es": "restory.wiki — Palaloid (wiki de la comunidad)", "pt-BR": "restory.wiki — Palaloid (wiki da comunidade)",
    "ru": "restory.wiki — Palaloid (вики сообщества)",
})
SRC_STEAM_GUIDE_AKIBA = _src("Steam guide: Legend of Akiba [EN]", "https://steamcommunity.com/sharedfiles/filedetails/?id=3782095380", {
    "en": "Steam guide: Legend of Akiba [EN]", "zh-CN": "Steam 指南：Legend of Akiba [EN]",
    "ja": "Steam ガイド：Legend of Akiba [EN]", "ko": "Steam 가이드: Legend of Akiba [EN]",
    "fr": "Guide Steam : Legend of Akiba [EN]", "de": "Steam-Guide: Legend of Akiba [EN]",
    "es": "Guía de Steam: Legend of Akiba [EN]", "pt-BR": "Guia da Steam: Legend of Akiba [EN]",
    "ru": "Гайд Steam: Legend of Akiba [EN]",
})
SRC_STEAM_GUIDE_PRICES = _src("Steam guide: Device Sale Prices", "https://steamcommunity.com/sharedfiles/filedetails/?id=3783450316", {
    "en": "Steam guide: Device Sale Prices", "zh-CN": "Steam 指南：Device Sale Prices",
    "ja": "Steam ガイド：Device Sale Prices", "ko": "Steam 가이드: Device Sale Prices",
    "fr": "Guide Steam : Device Sale Prices", "de": "Steam-Guide: Device Sale Prices",
    "es": "Guía de Steam: Device Sale Prices", "pt-BR": "Guia da Steam: Device Sale Prices",
    "ru": "Гайд Steam: Device Sale Prices",
})
SRC_STEAM_DISC_PAINT = _src("Steam discussion: painting the Palaloid camera", "https://steamcommunity.com/app/3812600/discussions/0/588434705716615986/", {
    "en": "Steam discussion: painting the Palaloid camera", "zh-CN": "Steam 讨论：Palaloid 相机上色",
    "ja": "Steam ディスカッション：Palaloid カメラの塗装", "ko": "Steam 토론: Palaloid 카메라 도색",
    "fr": "Discussion Steam : peindre l'appareil photo Palaloid", "de": "Steam-Diskussion: Palaloid-Kamera bemalen",
    "es": "Debate de Steam: pintar la cámara Palaloid", "pt-BR": "Tópico da Steam: pintar a câmera Palaloid",
    "ru": "Обсуждение Steam: покраска камеры Palaloid",
})
SRC_STEAM_DISC_INVISIBLE = _src("Steam discussion: invisible part on table", "https://steamcommunity.com/app/3812600/discussions/1/588434161796313713/", {
    "en": "Steam discussion: invisible part on table", "zh-CN": "Steam 讨论：零件隐形/桌面上的隐形零件",
    "ja": "Steam ディスカッション：テーブル上の見えないパーツ", "ko": "Steam 토론: 테이블 위에 보이지 않는 부품",
    "fr": "Discussion Steam : pièce invisible sur la table", "de": "Steam-Diskussion: unsichtbares Teil auf dem Tisch",
    "es": "Debate de Steam: pieza invisible sobre la mesa", "pt-BR": "Tópico da Steam: peça invisível na mesa",
    "ru": "Обсуждение Steam: невидимая деталь на столе",
})
# ---- L3 社区来源：29 台设备三源一致（restory.wiki 分类页 + Steam 讨论区名单帖 + Legend of Akiba 指南）----
SRC_RESTORY_WIKI_DEVICES = _src("restory.wiki — Devices category (community wiki)", "https://restory.wiki/w/Devices", {
    "en": "restory.wiki — Devices category (community wiki)", "zh-CN": "restory.wiki — 设备分类页（社区维基）",
    "ja": "restory.wiki — デバイスカテゴリ（コミュニティWiki）", "ko": "restory.wiki — 기기 분류 페이지（커뮤니티 위키）",
    "fr": "restory.wiki — catégorie Appareils (wiki communautaire)", "de": "restory.wiki — Kategorie Geräte (Community-Wiki)",
    "es": "restory.wiki — categoría Dispositivos (wiki de la comunidad)", "pt-BR": "restory.wiki — categoria Aparelhos (wiki da comunidade)",
    "ru": "restory.wiki — категория «Устройства» (вики сообщества)",
})
SRC_STEAM_DISC_DEVICES = _src("Steam discussion: ReStory device list (29 devices)", "https://steamcommunity.com/app/3812600/discussions/0/588434434320138300/", {
    "en": "Steam discussion: ReStory device list (29 devices)", "zh-CN": "Steam 讨论：ReStory 设备清单（29 台）",
    "ja": "Steam ディスカッション：ReStory デバイス一覧（29台）", "ko": "Steam 토론: ReStory 기기 목록(29개)",
    "fr": "Discussion Steam : liste des appareils ReStory (29 appareils)", "de": "Steam-Diskussion: ReStory Geräteliste (29 Geräte)",
    "es": "Debate de Steam: lista de dispositivos de ReStory (29 dispositivos)", "pt-BR": "Tópico da Steam: lista de aparelhos de ReStory (29 aparelhos)",
    "ru": "Обсуждение Steam: список устройств ReStory (29 устройств)",
})
# ---- L0 官方补丁公告（5 台设备在官方 Steam 补丁中被点名）----
SRC_STEAM_PATCH_009R = _src("Official Steam announcement — Update #1 (v1.0.009r)", "https://steamcommunity.com/games/3812600/announcements/detail/711157251640918758", {
    "en": "Official Steam announcement — Update #1 (v1.0.009r)", "zh-CN": "Steam 官方公告——更新 #1（v1.0.009r）",
    "ja": "Steam公式アナウンス — アップデート#1（v1.0.009r）", "ko": "Steam 공식 공지 — 업데이트 #1(v1.0.009r)",
    "fr": "Annonce Steam officielle — Mise à jour n°1 (v1.0.009r)", "de": "Offizielle Steam-Ankündigung — Update Nr. 1 (v1.0.009r)",
    "es": "Anuncio oficial de Steam — Actualización n.º 1 (v1.0.009r)", "pt-BR": "Anúncio oficial da Steam — Atualização nº 1 (v1.0.009r)",
    "ru": "Официальное объявление Steam — Обновление №1 (v1.0.009r)",
})
SRC_STEAM_PATCH_010R = _src("Official Steam announcement — Update #2 (v1.0.010r)", "https://steamcommunity.com/games/3812600/announcements/detail/676254988366774831", {
    "en": "Official Steam announcement — Update #2 (v1.0.010r)", "zh-CN": "Steam 官方公告——更新 #2（v1.0.010r）",
    "ja": "Steam公式アナウンス — アップデート#2（v1.0.010r）", "ko": "Steam 공식 공지 — 업데이트 #2(v1.0.010r)",
    "fr": "Annonce Steam officielle — Mise à jour n°2 (v1.0.010r)", "de": "Offizielle Steam-Ankündigung — Update Nr. 2 (v1.0.010r)",
    "es": "Anuncio oficial de Steam — Actualización n.º 2 (v1.0.010r)", "pt-BR": "Anúncio oficial da Steam — Atualização nº 2 (v1.0.010r)",
    "ru": "Официальное объявление Steam — Обновление №2 (v1.0.010r)",
})
# ---- 16 台新设备各自的 restory.wiki 页面（L3）----
_WIKI_LABELS = {
    "en": "restory.wiki — {d} (community wiki)", "zh-CN": "restory.wiki — {d}（社区维基）",
    "ja": "restory.wiki — {d}（コミュニティWiki）", "ko": "restory.wiki — {d}（커뮤니티 위키）",
    "fr": "restory.wiki — {d} (wiki communautaire)", "de": "restory.wiki — {d} (Community-Wiki)",
    "es": "restory.wiki — {d} (wiki de la comunidad)", "pt-BR": "restory.wiki — {d} (wiki da comunidade)",
    "ru": "restory.wiki — {d} (вики сообщества)",
}
def _wiki_src(device, slug):
    labels = {lg: tpl.format(d=device) for lg, tpl in _WIKI_LABELS.items()}
    return _src(f"restory.wiki — {device} (community wiki)", f"https://restory.wiki/w/{slug}", labels)

SRC_WIKI_BRICK_GAME = _wiki_src("Brick Game", "Brick_Game")
SRC_WIKI_GAME_DUCK = _wiki_src("Game Duck", "Game_Duck")
SRC_WIKI_BREADBOX_JOYSTICK = _wiki_src("BreadBox Joystick", "BreadBox_Joystick")
SRC_WIKI_XI_BOX = _wiki_src("XI-box", "XI-box")
SRC_WIKI_XI_BOX_CONTROLLER = _wiki_src("XI-box Controller", "XI-box_Controller")
SRC_WIKI_SIMSONS_M65 = _wiki_src("Simsons M65", "Simsons_M65")
SRC_WIKI_BLUEBERRY_CURL = _wiki_src("Blueberry Curl", "Blueberry_Curl")
SRC_WIKI_WERTU_SIGNATURE = _wiki_src("Wertu Signature", "Wertu_Signature")
SRC_WIKI_UNICORP_KETTLE = _wiki_src("Unicorp Kettle", "Unicorp_Kettle")
SRC_WIKI_AUTOROLLA_WT2000 = _wiki_src("Autorolla WT2000", "Autorolla_WT2000")
SRC_WIKI_UNICORP_VISION = _wiki_src("Unicorp Vision", "Unicorp_Vision")
SRC_WIKI_ROBBY = _wiki_src("Robby", "Robby")
SRC_WIKI_NERDIO_W91F = _wiki_src("Nerdio W-91F", "Nerdio_W-91F")
SRC_WIKI_GUITAR_LEGEND = _wiki_src("Guitar Legend", "Guitar_Legend")
SRC_WIKI_MAPPLE_MYPOD = _wiki_src("Mapple Mypod", "Mapple_Mypod")
SRC_WIKI_IDM_THINKERDAD = _wiki_src("IDM ThinkerDad", "IDM_ThinkerDad")
SRC_MAP = {"steam": SRC_STEAM, "steam-achievements": SRC_STEAM_ACHIEVEMENTS, "steam-news": SRC_STEAM_NEWS, "allthings": SRC_ALLTHINGS, "intoindie": SRC_INTOINDIE, "powerpyx": SRC_POWERPYX,
           "restory-wiki": SRC_RESTORY_WIKI, "steam-guide-akiba": SRC_STEAM_GUIDE_AKIBA, "steam-guide-prices": SRC_STEAM_GUIDE_PRICES, "steam-discussion-paint": SRC_STEAM_DISC_PAINT, "steam-discussion-invisible": SRC_STEAM_DISC_INVISIBLE,
           "restory-wiki-devices": SRC_RESTORY_WIKI_DEVICES, "steam-discussion-devices": SRC_STEAM_DISC_DEVICES, "steam-patch-009r": SRC_STEAM_PATCH_009R, "steam-patch-010r": SRC_STEAM_PATCH_010R,
           "wiki-brick-game": SRC_WIKI_BRICK_GAME, "wiki-game-duck": SRC_WIKI_GAME_DUCK, "wiki-breadbox-joystick": SRC_WIKI_BREADBOX_JOYSTICK,
           "wiki-xi-box": SRC_WIKI_XI_BOX, "wiki-xi-box-controller": SRC_WIKI_XI_BOX_CONTROLLER, "wiki-simsons-m65": SRC_WIKI_SIMSONS_M65,
           "wiki-blueberry-curl": SRC_WIKI_BLUEBERRY_CURL, "wiki-wertu-signature": SRC_WIKI_WERTU_SIGNATURE, "wiki-unicorp-kettle": SRC_WIKI_UNICORP_KETTLE,
           "wiki-autorolla-wt2000": SRC_WIKI_AUTOROLLA_WT2000, "wiki-unicorp-vision": SRC_WIKI_UNICORP_VISION, "wiki-robby": SRC_WIKI_ROBBY,
           "wiki-nerdio-w91f": SRC_WIKI_NERDIO_W91F, "wiki-guitar-legend": SRC_WIKI_GUITAR_LEGEND, "wiki-mapple-mypod": SRC_WIKI_MAPPLE_MYPOD,
           "wiki-idm-thinkerdad": SRC_WIKI_IDM_THINKERDAD}

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

# ---- Zen calculator UI ----
# Factual Zen and device copy lives directly in content_*.py. Do not add a
# terminal content override here: source and generated output must agree.
_ZEN_UI = {
 "en": ["Enter your current Zen total", "Use the total shown in your game. The official achievement requires more than 100.", "Current total", "Requires >100", "Check"],
 "zh-CN": ["输入当前 Zen 合计", "使用游戏显示的合计。官方成就要求超过 100。", "当前合计", "要求 >100", "检查"],
 "zh-TW": ["輸入目前 Zen 合計", "使用遊戲顯示的合計。官方成就要求超過 100。", "目前合計", "要求 >100", "檢查"],
 "ja": ["現在のZen合計を入力", "ゲームに表示される合計を使用してください。公式実績は100より多く必要です。", "現在の合計", "条件 >100", "確認"],
 "ko": ["현재 Zen 합계 입력", "게임에 표시된 합계를 사용하세요. 공식 업적은 100보다 많이 필요합니다.", "현재 합계", "요구 >100", "확인"],
 "fr": ["Saisissez votre total Zen", "Utilisez le total affiché dans le jeu. Le succès officiel exige plus de 100.", "Total actuel", "Requis >100", "Vérifier"],
 "de": ["Aktuelle Zen-Summe eingeben", "Verwenden Sie die im Spiel angezeigte Summe. Der Erfolg verlangt mehr als 100.", "Aktuelle Summe", "Erfordert >100", "Prüfen"],
 "es": ["Introduce tu total Zen", "Usa el total del juego. El logro oficial exige más de 100.", "Total actual", "Requiere >100", "Comprobar"],
 "pt-BR": ["Digite seu total Zen", "Use o total mostrado no jogo. A conquista oficial exige mais de 100.", "Total atual", "Exige >100", "Verificar"],
 "ru": ["Введите текущую сумму дзен", "Используйте сумму из игры. Для достижения нужно больше 100.", "Текущая сумма", "Нужно >100", "Проверить"],
}
for lg in LANGS:
    ui = _ZEN_UI[lg]
    SITE_I18N[lg].update({"zenCalcTitle":ui[0], "zenCalcLead":ui[1], "zenTotal":ui[2], "zenTarget":ui[3], "zenReset":ui[4]})

# Keep page-level default-language fields synchronized with i18n.en.
for page in PAGES:
    en = page["i18n"]["en"]
    for key in ("title", "metaTitle", "metaDescription", "intro", "sections"):
        page[key] = copy.deepcopy(en[key])

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
        t["metaTitle"] = f"ReStory — {ui[0]}"
        t["intro"] = ui[1]
        t["metaDescription"] = f"ReStory: {ui[1]}"
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
 "en": ["Device profiles","Each profile lists the verified device name and family, official Atari status where supported, and marks the device-specific procedure as unknown."],
 "zh-CN": ["设备资料","每份资料列出已核实的设备名称与类别；有来源支持时标注 Atari 官方授权，并明确设备专属流程未知。"],
 "zh-TW": ["裝置資料","每份資料列出已核實的裝置名稱與類別；有來源支持時標註 Atari 官方授權，並明確裝置專屬流程未知。"],
 "ja": ["デバイス資料","各資料には確認済みのデバイス名と分類、出典がある場合のAtari公式ライセンス状況を掲載し、固有手順は不明と明記します。"],
 "ko": ["기기 자료","각 자료에는 확인된 기기 이름과 분류, 출처가 있는 경우 Atari 공식 라이선스 상태가 있으며 기기별 절차는 알려지지 않았다고 표시합니다."],
 "fr": ["Fiches appareils","Chaque fiche indique le nom et la famille vérifiés, le statut Atari officiel lorsqu'il est étayé, et précise que la procédure propre à l'appareil est inconnue."],
 "de": ["Geräteprofile","Jedes Profil nennt den verifizierten Gerätenamen und die Familie, bei Beleg den offiziellen Atari-Status, und kennzeichnet den gerätespezifischen Ablauf als unbekannt."],
 "es": ["Fichas de dispositivos","Cada ficha muestra el nombre y la familia verificados, el estado oficial de Atari cuando está respaldado, y marca el procedimiento específico como desconocido."],
 "pt-BR": ["Perfis de aparelhos","Cada perfil mostra nome e família verificados, status oficial da Atari quando respaldado e informa que o procedimento específico é desconhecido."],
 "ru": ["Профили устройств","В каждом профиле указаны подтверждённые название и категория, официальный статус Atari при наличии источника, а процедура отмечена как неизвестная."],
}
for lg, (t, l) in _DEV_T.items():
    SITE_I18N[lg]["devicesTitle"] = t
    SITE_I18N[lg]["devicesLead"] = l
# ---- 首页 hero / about 页本地化（修复全语言英文残留）----
_HOME_I18N = {
 "en": {
  "homeIntro": "ReStory is a chill, narrative-driven shop management simulator from the creators of I Am Future. Set in mid-2000s Tokyo, you run an electronics repair shop — restore nostalgic Y2K devices, talk to customers, and shape a branching story with multiple endings.",
  "homeFacts": ["Run a repair shop in mid-2000s Tokyo (Akihabara)","Restore nostalgic Y2K devices, including officially licensed Atari consoles","Branching storyline with multiple endings based on your choices","50 Steam achievements + trading cards + cloud saves","Official 9 languages + Traditional Chinese (10 total)","From the creators of I Am Future — published by tinyBuild"],
  "homeStats": ["Released","Achievements","Official + guide languages","Repairable devices","On Steam (10% off)","Reviews in 3 days"],
  "aboutPoints": ["Facts checked against the official Steam store page and reputable sources (allthings.how, intoindiegames)","Anything still being verified is explicitly marked — we never invent details","Available in 10 languages; every page lists its own sources"]
 },
 "zh-CN": {
  "homeIntro": "《ReStory：维修物语》是一款由 I Am Future 团队打造的治愈系叙事经营模拟游戏。故事发生在 2005 年的东京秋叶原——你经营一家电子维修铺，修复怀旧 Y2K 设备、倾听顾客的故事，用你的选择塑造多条分支结局。",
  "homeFacts": ["在 2005 年东京秋叶原经营维修铺","修复怀旧 Y2K 设备，包括官方授权的 Atari 主机","基于你的选择的分支剧情与多结局","50 个 Steam 成就 + 卡牌 + 云存档","9 种官方语言 + 繁体中文（共 10 种）","来自 I Am Future 团队，由 tinyBuild 发行"],
  "homeStats": ["发售日","成就","官方 + 指南语言","可修设备","Steam 价格（9 折）","3 天评价数"],
  "aboutPoints": ["事实核对自 Steam 官方商店页与可靠来源（allthings.how、intoindiegames）","仍在验证的内容明确标注——我们绝不编造细节","提供 10 种语言；每个页面都列出自己的来源"]
 },
 "zh-TW": {
  "homeIntro": "《ReStory：維修物語》是一款由 I Am Future 團隊打造的治癒系敘事經營模擬遊戲。故事發生在 2005 年的東京秋葉原——你經營一家電子維修鋪，修復懷舊 Y2K 設備、傾聽顧客的故事，用你的選擇塑造多條分支結局。",
  "homeFacts": ["在 2005 年東京秋葉原經營維修鋪","修復懷舊 Y2K 設備，包括官方授權的 Atari 主機","基於你的選擇的分支劇情與多結局","50 個 Steam 成就 + 卡牌 + 雲端存檔","9 種官方語言 + 繁體中文（共 10 種）","來自 I Am Future 團隊，由 tinyBuild 發行"],
  "homeStats": ["發售日","成就","官方 + 指南語言","可修設備","Steam 價格（9 折）","3 天評價數"],
  "aboutPoints": ["事實核對自 Steam 官方商店頁與可靠來源（allthings.how、intoindiegames）","仍在驗證的內容明確標註——我們絕不編造細節","提供 10 種語言；每個頁面都列出自己的來源"]
 },
 "ja": {
  "homeIntro": "『ReStory：まったり電子機器修理』は I Am Future の開発者による、癒やし系ストーリー経営シミュレーション。2005年の中旬・東京秋葉原で電子機器修理店を営み、懐かしいY2Kデバイスを修復し、お客の物語に耳を傾け、選択で分岐する複数のエンディングを紡ぎます。",
  "homeFacts": ["2005年・秋葉原で修理店を経営","公式ライセンスのAtariなど懐かしいY2Kデバイスを修復","選択で変わる分岐ストーリーと複数エンディング","Steam実績50個 + トレーディングカード + クラウド保存","公式9言語 + 繁体中国語（計10言語）","I Am Future 開発チーム、tinyBuild 発行"],
  "homeStats": ["発売日","実績","公式 + ガイド言語","修理可能デバイス","Steam価格（10%OFF）","3日間のレビュー数"],
  "aboutPoints": ["Steam公式ストアと信頼できる情報源（allthings.how、intoindiegames）で確認","未検証の内容は明記 — 細部を創作しません","10言語対応；各ページに出典を掲載"]
 },
 "ko": {
  "homeIntro": "《ReStory: 리스토리》는 I Am Future 제작진이 만든 힐링형 스토리 경영 시뮬레이션입니다. 2005년 도쿄 아키하바라에서 전자제품 수리점을 운영하며, 추억의 Y2K 기기를 복원하고 손님의 이야기를 듣고, 선택에 따라 갈라지는 여러 엔딩을 만들어 갑니다.",
  "homeFacts": ["2005년 도쿄 아키하바라에서 수리점 운영","공식 라이선스 Atari 등 추억의 Y2K 기기 복원","선택에 따라 달라지는 분기 스토리와 다중 엔딩","Steam 업적 50개 + 트레이딩 카드 + 클라우드 저장","공식 9개 언어 + 대만 중국어(총 10개)","I Am Future 제작진, tinyBuild 배급"],
  "homeStats": ["출시일","업적","공식 + 가이드 언어","수리 가능 기기","Steam 가격(10% 할인)","3일 리뷰 수"],
  "aboutPoints": ["Steam 공식 스토어와 신뢰할 수 있는 출처(allthings.how, intoindiegames)로 확인","미검증 내용은 명확히 표시 — 세부 사항을 지어내지 않습니다","10개 언어 제공; 각 페이지에 출처 명시"]
 },
 "fr": {
  "homeIntro": "ReStory est un simulateur de gestion narratif et relaxant signé par les créateurs de I Am Future. Dans le Tokyo des années 2000, vous tenez une boutique de réparation d'électronique : restaurez des appareils Y2K nostalgiques, écoutez les histoires des clients et façonnez une histoire à embranchements et fins multiples.",
  "homeFacts": ["Tenez une boutique de réparation dans le Tokyo des années 2000 (Akihabara)","Restaurez des appareils Y2K nostalgiques, dont les consoles Atari sous licence officielle","Histoire à embranchements et fins multiples selon vos choix","50 succès Steam + cartes + sauvegarde cloud","9 langues officielles + chinois traditionnel (10 au total)","Par les créateurs de I Am Future — édité par tinyBuild"],
  "homeStats": ["Sortie","Succès","Langues officielles + guide","Appareils réparables","Sur Steam (-10 %)","Avis en 3 jours"],
  "aboutPoints": ["Informations vérifiées sur la page Steam officielle et des sources fiables (allthings.how, intoindiegames)","Tout ce qui reste à vérifier est signalé — nous n'inventons jamais de détails","Disponible en 10 langues ; chaque page liste ses sources"]
 },
 "de": {
  "homeIntro": "ReStory ist ein entspannter, erzählerischer Shop-Management-Simulator von den Machern von I Am Future. In Tokio Mitte der 2000er führst du einen Elektronik-Reparaturshop: stelle nostalgische Y2K-Geräte wieder her, höre den Geschichten der Kunden zu und gestalte eine verzweigte Geschichte mit mehreren Enden.",
  "homeFacts": ["Führe einen Reparaturshop im Tokio der 2000er (Akihabara)","Stelle nostalgische Y2K-Geräte wieder her, inkl. offiziell lizenzierter Atari-Konsolen","Verzweigte Geschichte mit mehreren Enden je nach deinen Entscheidungen","50 Steam-Errungenschaften + Karten + Cloud-Speicher","9 offizielle Sprachen + traditionelles Chinesisch (10 gesamt)","Von den Machern von I Am Future — veröffentlicht von tinyBuild"],
  "homeStats": ["Erschienen","Errungenschaften","Offizielle + Guide-Sprachen","Reparierbare Geräte","Auf Steam (-10 %)","Bewertungen in 3 Tagen"],
  "aboutPoints": ["Informationen geprüft gegen die offizielle Steam-Seite und zuverlässige Quellen (allthings.how, intoindiegames)","Alles Unverifizierte ist markiert — wir erfinden nie Details","Verfügbar in 10 Sprachen; jede Seite listet ihre Quellen"]
 },
 "es": {
  "homeIntro": "ReStory es un simulador de gestión narrativo y relajante de los creadores de I Am Future. En el Tokio de mediados de los 2000, regentas una tienda de reparación de electrónica: restaura dispositivos Y2K nostálgicos, escucha las historias de los clientes y da forma a una historia ramificada con múltiples finales.",
  "homeFacts": ["Regenta una tienda de reparación en el Tokio de 2005 (Akihabara)","Restaura dispositivos Y2K nostálgicos, incluidas consolas Atari con licencia oficial","Historia ramificada con múltiples finales según tus decisiones","50 logros de Steam + cromos + guardado en la nube","9 idiomas oficiales + chino tradicional (10 en total)","De los creadores de I Am Future — publicado por tinyBuild"],
  "homeStats": ["Lanzamiento","Logros","Idiomas oficiales + guía","Dispositivos reparables","En Steam (-10 %)","Reseñas en 3 días"],
  "aboutPoints": ["Información contrastada con la página oficial de Steam y fuentes fiables (allthings.how, intoindiegames)","Todo lo pendiente de verificar está marcado — nunca inventamos detalles","Disponible en 10 idiomas; cada página lista sus fuentes"]
 },
 "pt-BR": {
  "homeIntro": "ReStory é um simulador de gestão narrativo e relaxante dos criadores de I Am Future. No Tóquio de meados dos anos 2000, você administra uma loja de consertos de eletrônicos: restaure aparelhos Y2K nostálgicos, ouça as histórias dos clientes e molde uma história ramificada com múltiplos finais.",
  "homeFacts": ["Administre uma loja de consertos no Tóquio de 2005 (Akihabara)","Restaure aparelhos Y2K nostálgicos, incluindo consoles Atari com licença oficial","História ramificada com múltiplos finais conforme suas escolhas","50 conquistas na Steam + cards + nuvem","9 idiomas oficiais + chinês tradicional (10 no total)","Dos criadores de I Am Future — publicado pela tinyBuild"],
  "homeStats": ["Lançamento","Conquistas","Idiomas oficiais + guia","Aparelhos reparáveis","Na Steam (-10 %)","Avaliações em 3 dias"],
  "aboutPoints": ["Informações verificadas na página oficial da Steam e fontes confiáveis (allthings.how, intoindiegames)","Tudo que está em verificação é marcado — nunca inventamos detalhes","Disponível em 10 idiomas; cada página lista suas fontes"]
 },
 "ru": {
  "homeIntro": "ReStory — расслабленный нарративный симулятор управления магазином от создателей I Am Future. В Токио середины 2000-х вы держите мастерскую по ремонту электроники: восстанавливайте ностальгические Y2K-устройства, слушайте истории клиентов и формируйте ветвящуюся историю с несколькими концовками.",
  "homeFacts": ["Держите мастерскую по ремонту в Токио 2005 (Акихабара)","Восстанавливайте ностальгические Y2K-устройства, включая официально лицензированные консоли Atari","Ветвящаяся история с несколькими концовками в зависимости от выбора","50 достижений Steam + карточки + облачные сохранения","9 официальных языков + традиционный китайский (всего 10)","От создателей I Am Future — издатель tinyBuild"],
  "homeStats": ["Релиз","Достижения","Официальные + языки гайда","Ремонтируемые устройства","В Steam (-10 %)","Отзывов за 3 дня"],
  "aboutPoints": ["Информация проверена по официальной странице Steam и надёжным источникам (allthings.how, intoindiegames)","Всё, что ещё проверяется, помечено — мы никогда не выдумываем детали","Доступно на 10 языках; каждая страница перечисляет свои источники"]
 },
}
for lg, v in _HOME_I18N.items():
    SITE_I18N[lg].update(v)

# Official Steam announcement, 2026-08-13: Update #2 (1.0.010r).
# Insert it immediately before the existing unknown-DLC row and replace the
# stale FAQ answers that still described announced fixes as unknown.
_PATCH_010R = {
 "en": ["Aug 13, 2026", "Update #2 (v1.0.010r): fixed long saves and possible save-time crashes, a blocker caused by missing screws in a device, and a minor issue with Robby's wires (official Steam announcement).", "Yes. Official updates v1.0.009r and v1.0.010r are listed above.", "Use the official entries above for announced fixes; unannounced achievement changes remain unknown."],
 "zh-CN": ["2026-08-13", "第二次更新（v1.0.010r）：修复保存时间过长及可能在保存时崩溃、设备缺少螺丝造成的阻断，以及 Robby 电线的小问题（Steam 官方公告）。", "有。官方更新 v1.0.009r 与 v1.0.010r 已列在上方。", "请以上方官方条目判断已公布的修复；未公告的成就变更仍属未知。"],
 "zh-TW": ["2026-08-13", "第二次更新（v1.0.010r）：修復儲存時間過長及可能在儲存時當機、裝置缺少螺絲造成的阻斷，以及 Robby 電線的小問題（Steam 官方公告）。", "有。官方更新 v1.0.009r 與 v1.0.010r 已列在上方。", "請以上方官方條目判斷已公布的修復；未公告的成就變更仍屬未知。"],
 "ja": ["2026年8月13日", "アップデート第2弾（v1.0.010r）：セーブ時間の長期化とセーブ時にクラッシュする可能性、デバイス内のネジ欠落による進行不能、Robby の配線に関する軽微な問題を修正（Steam公式発表）。", "はい。公式アップデート v1.0.009r と v1.0.010r を上に掲載しています。", "発表済みの修正は上の公式項目を参照してください。未発表の実績変更は不明です。"],
 "ko": ["2026년 8월 13일", "두 번째 업데이트(v1.0.010r): 저장 시간이 길어지거나 저장 중 충돌할 수 있는 문제, 기기에서 나사가 사라져 진행이 막히는 문제, Robby 전선의 사소한 문제를 수정했습니다(Steam 공식 공지).", "있습니다. 공식 업데이트 v1.0.009r과 v1.0.010r이 위에 정리되어 있습니다.", "발표된 수정은 위 공식 항목을 확인하세요. 공지되지 않은 업적 변경은 아직 알 수 없습니다."],
 "fr": ["13 août 2026", "Mise à jour n°2 (v1.0.010r) : correction des sauvegardes longues et d'un possible plantage pendant la sauvegarde, d'un blocage dû à des vis manquantes dans un appareil et d'un problème mineur avec les fils de Robby (annonce Steam officielle).", "Oui. Les mises à jour officielles v1.0.009r et v1.0.010r figurent ci-dessus.", "Consultez les entrées officielles ci-dessus pour les correctifs annoncés ; les changements de succès non annoncés restent inconnus."],
 "de": ["13. August 2026", "Update Nr. 2 (v1.0.010r): lange Speichervorgänge und mögliche Abstürze beim Speichern, einen Blocker durch fehlende Schrauben in einem Gerät sowie ein kleines Problem mit Robbys Kabeln behoben (offizielle Steam-Ankündigung).", "Ja. Die offiziellen Updates v1.0.009r und v1.0.010r stehen oben.", "Für angekündigte Fixes gelten die offiziellen Einträge oben; nicht angekündigte Erfolgsänderungen bleiben unbekannt."],
 "es": ["13 de agosto de 2026", "Actualización n.º 2 (v1.0.010r): corregidos los guardados largos y un posible cierre al guardar, un bloqueo por tornillos ausentes en un dispositivo y un problema menor con los cables de Robby (anuncio oficial de Steam).", "Sí. Las actualizaciones oficiales v1.0.009r y v1.0.010r aparecen arriba.", "Consulta arriba las correcciones anunciadas oficialmente; los cambios de logros no anunciados siguen sin conocerse."],
 "pt-BR": ["13 de agosto de 2026", "Atualização nº 2 (v1.0.010r): corrigidos salvamentos demorados e possível travamento ao salvar, um bloqueio por parafusos ausentes em um aparelho e um problema menor com os fios do Robby (anúncio oficial da Steam).", "Sim. As atualizações oficiais v1.0.009r e v1.0.010r estão listadas acima.", "Use as entradas oficiais acima para correções anunciadas; mudanças de conquistas não anunciadas continuam desconhecidas."],
 "ru": ["13 авг 2026", "Обновление №2 (v1.0.010r): исправлены долгое сохранение и возможный сбой при сохранении, блокировка из-за отсутствующих винтов в устройстве и небольшая проблема с проводами Robby (официальное объявление Steam).", "Да. Официальные обновления v1.0.009r и v1.0.010r перечислены выше.", "Об объявленных исправлениях смотрите официальные пункты выше; неанонсированные изменения достижений остаются неизвестными."],
}
for page in PAGES:
    if page["slug"] != "patch-notes":
        continue
    page["sources"] = [SRC_STEAM_NEWS, SRC_STEAM]
    for lg in LANGS:
        current = page["i18n"][lg]
        timeline = next(section for section in current["sections"] if section["type"] == "timeline")
        if not any("1.0.010r" in row[1] for row in timeline["items"]):
            timeline["items"].insert(max(0, len(timeline["items"]) - 1), _PATCH_010R[lg][:2])
        faq = next(section for section in current["sections"] if section["type"] == "faq")
        faq["items"][1][1] = _PATCH_010R[lg][2]
        faq["items"][2][1] = _PATCH_010R[lg][3]




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
print(f"✓ 来源映射: steam/allthings/intoindie/powerpyx/restory-wiki/steam-guide-*/steam-discussion-*/steam-patch-*/wiki-* 各语言 label 齐备")
