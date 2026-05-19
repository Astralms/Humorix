from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm, cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
import os

W, H = A4
LM = RM = 2.0 * cm
TM = 2.4 * cm
BM = 1.8 * cm
CW = W - LM - RM

# ── Palette ────────────────────────────────────────────────────────────────
INK        = colors.HexColor("#0D0D0D")
INK2       = colors.HexColor("#1E293B")
INK3       = colors.HexColor("#64748B")
RULE       = colors.HexColor("#E2E8F0")

NAVY       = colors.HexColor("#0F2044")
BLUE       = colors.HexColor("#1E40AF")
SKY        = colors.HexColor("#3B82F6")
PALE       = colors.HexColor("#F0F6FF")
TINT       = colors.HexColor("#DBEAFE")
GRID       = colors.HexColor("#BFDBFE")

TEAL       = colors.HexColor("#0D6E63")
TEAL_LT    = colors.HexColor("#CCFBF1")
GREEN      = colors.HexColor("#15803D")
GREEN_LT   = colors.HexColor("#DCFCE7")
AMBER      = colors.HexColor("#92400E")
AMBER_LT   = colors.HexColor("#FEF3C7")
RED        = colors.HexColor("#991B1B")
RED_LT     = colors.HexColor("#FEE2E2")
PURPLE     = colors.HexColor("#5B21B6")
PURPLE_LT  = colors.HexColor("#EDE9FE")
SLATE      = colors.HexColor("#334155")
SLATE_LT   = colors.HexColor("#F8FAFC")
WHITE      = colors.white

FOREST     = colors.HexColor("#14532D")
FOREST_LT  = colors.HexColor("#F0FDF4")
CRIMSON    = colors.HexColor("#7F1D1D")
CRIMSON_LT = colors.HexColor("#FFF1F2")


# ── Page Template ──────────────────────────────────────────────────────────
def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, H - TM + 2*mm, W, TM - 2*mm, fill=1, stroke=0)
    canvas.setFillColor(SKY)
    canvas.rect(0, H - TM + 1.5*mm, W, 0.8*mm, fill=1, stroke=0)
    canvas.setFont("Helvetica-Bold", 7.5)
    canvas.setFillColor(WHITE)
    canvas.drawString(LM, H - TM + 6.5*mm, "HUMORIX AI")
    canvas.setFont("Helvetica", 6.8)
    canvas.setFillColor(colors.HexColor("#93C5FD"))
    canvas.drawRightString(W - RM, H - TM + 6.5*mm,
        "HARDENED BLUEPRINT  v3.0  -  MEMORY  -  RESILIENCE  -  PRIVACY  -  VALIDATION")
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.4)
    canvas.line(LM, BM - 2*mm, W - RM, BM - 2*mm)
    canvas.setFont("Helvetica", 6.5)
    canvas.setFillColor(INK3)
    canvas.drawString(LM, BM - 4.5*mm,
        "Humorix AI  -  Supportive tool only  -  Not a substitute for licensed professional care")
    canvas.setFont("Helvetica-Bold", 8)
    canvas.setFillColor(BLUE)
    canvas.drawRightString(W - RM, BM - 4.5*mm, f"{doc.page}")
    canvas.restoreState()


# ── Styles ─────────────────────────────────────────────────────────────────
def mk(name, **kw):
    base = dict(fontName="Helvetica", fontSize=9, textColor=INK2,
                leading=14, spaceAfter=4, spaceBefore=0)
    base.update(kw)
    return ParagraphStyle(name, **base)

S = {
    "h2":    mk("h2",  fontName="Helvetica-Bold", fontSize=12.5, textColor=NAVY,
                leading=18, spaceBefore=16, spaceAfter=4),
    "h3":    mk("h3",  fontName="Helvetica-Bold", fontSize=9.5, textColor=BLUE,
                leading=14, spaceBefore=10, spaceAfter=3),
    "body":  mk("body", fontSize=9, textColor=INK2, leading=14.5,
                alignment=TA_JUSTIFY, spaceAfter=5),
    "small": mk("small", fontSize=7.5, textColor=INK3, leading=11, spaceAfter=2),
    "code":  mk("code", fontName="Courier", fontSize=7.2, textColor=NAVY, leading=11, spaceAfter=1),
    "th":    mk("th",  fontName="Helvetica-Bold", fontSize=7.5, textColor=WHITE,
                leading=11, alignment=TA_CENTER),
    "td":    mk("td",  fontSize=8, textColor=INK2, leading=12),
    "tdb":   mk("tdb", fontName="Helvetica-Bold", fontSize=8, textColor=NAVY, leading=12),
    "lbl":   mk("lbl", fontName="Helvetica-Bold", fontSize=8, textColor=SLATE, leading=12),
    "pill":  mk("pill", fontName="Helvetica-Bold", fontSize=7, textColor=WHITE,
                leading=10, alignment=TA_CENTER),
    "note":  mk("note", fontSize=8.5, textColor=INK2, leading=13, leftIndent=6),
    "toc_p": mk("toc_p", fontName="Helvetica-Bold", fontSize=9.5, textColor=NAVY, leading=16),
    "toc_i": mk("toc_i", fontSize=8.5, textColor=INK2, leading=14, leftIndent=14),
    "tag":   mk("tag",  fontName="Helvetica-Bold", fontSize=7, textColor=BLUE,
                leading=10, alignment=TA_CENTER),
    "new":   mk("new",  fontName="Helvetica-Bold", fontSize=7, textColor=GREEN,
                leading=10, alignment=TA_CENTER),
}


# ── UI Components ──────────────────────────────────────────────────────────
def sp(n=6): return Spacer(1, n)
def hr(c=RULE, t=0.4): return HRFlowable(width="100%", thickness=t, color=c, spaceAfter=4, spaceBefore=4)

def banner(sec, title, sub, color=NAVY, accent=SKY):
    html = (f'<font size="8" color="#60A5FA"><b>{sec}</b></font><br/>'
            f'<font size="16" color="white"><b>{title}</b></font><br/>'
            f'<font size="8" color="#BAE6FD">{sub}</font>')
    p = Paragraph(html, ParagraphStyle("bn", fontName="Helvetica",
                  fontSize=9, leading=22, alignment=TA_LEFT))
    t = Table([[p]], colWidths=[CW])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), color),
        ("TOPPADDING",    (0,0), (-1,-1), 14),
        ("BOTTOMPADDING", (0,0), (-1,-1), 14),
        ("LEFTPADDING",   (0,0), (-1,-1), 18),
        ("RIGHTPADDING",  (0,0), (-1,-1), 18),
        ("LINEBELOW",     (0,-1), (-1,-1), 3, accent),
    ]))
    return t

def section(title, sub=""):
    inner = [Paragraph(title, S["h2"])]
    if sub: inner.append(Paragraph(sub, S["small"]))
    t = Table([[x] for x in inner], colWidths=[CW - 12])
    t.setStyle(TableStyle([
        ("LINEBEFORE",    (0,0), (0,-1), 4, SKY),
        ("LEFTPADDING",   (0,0), (-1,-1), 10),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("BACKGROUND",    (0,0), (-1,-1), PALE),
    ]))
    return t

def new_section(title, sub=""):
    inner = [Paragraph(title, mk("h2g", fontName="Helvetica-Bold", fontSize=12.5,
                                  textColor=FOREST, leading=18, spaceBefore=16, spaceAfter=4))]
    if sub: inner.append(Paragraph(sub, S["small"]))
    t = Table([[x] for x in inner], colWidths=[CW - 12])
    t.setStyle(TableStyle([
        ("LINEBEFORE",    (0,0), (0,-1), 4, GREEN),
        ("LEFTPADDING",   (0,0), (-1,-1), 10),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("BACKGROUND",    (0,0), (-1,-1), FOREST_LT),
    ]))
    return t

def subsec(t): return Paragraph(t, S["h3"])
def body(t): return Paragraph(t, S["body"])

def note_box(txt, kind="info"):
    cfg = {
        "info":   (PALE,       GRID,    BLUE,   "i"),
        "ok":     (GREEN_LT,   GREEN,   GREEN,  "OK"),
        "warn":   (AMBER_LT,   AMBER,   AMBER,  "!"),
        "crit":   (RED_LT,     RED,     RED,    "!!"),
        "new":    (FOREST_LT,  GREEN,   FOREST, "NEW"),
        "purple": (PURPLE_LT,  PURPLE,  PURPLE, "*"),
        "dark":   (colors.HexColor("#1E293B"), NAVY, WHITE, "->"),
    }
    bg, border, ic_c, icon = cfg[kind]
    text_color = WHITE if kind == "dark" else INK2
    sty = mk("nb", fontSize=8.5, textColor=text_color, leading=13, leftIndent=6)
    t = Table([[Paragraph(f"<b>{icon}</b>  {txt}", sty)]], colWidths=[CW])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), bg),
        ("BOX",           (0,0), (-1,-1), 0.6, border),
        ("LINEBEFORE",    (0,0), (0,-1), 3.5, border),
        ("TOPPADDING",    (0,0), (-1,-1), 7),
        ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ("LEFTPADDING",   (0,0), (-1,-1), 10),
        ("RIGHTPADDING",  (0,0), (-1,-1), 10),
    ]))
    return t

def kv(rows, c1=0.28, highlight=None):
    w1, w2 = CW * c1, CW * (1 - c1)
    data = []
    for i, r in enumerate(rows):
        data.append([Paragraph(r[0], S["lbl"]), Paragraph(r[1], S["td"])])
    t = Table(data, colWidths=[w1, w2])
    ts = [
        ("ROWBACKGROUNDS", (0,0), (-1,-1), [WHITE, PALE]),
        ("BOX",            (0,0), (-1,-1), 0.5, GRID),
        ("INNERGRID",      (0,0), (-1,-1), 0.3, GRID),
        ("TOPPADDING",     (0,0), (-1,-1), 5),
        ("BOTTOMPADDING",  (0,0), (-1,-1), 5),
        ("LEFTPADDING",    (0,0), (-1,-1), 8),
        ("RIGHTPADDING",   (0,0), (-1,-1), 8),
        ("VALIGN",         (0,0), (-1,-1), "TOP"),
    ]
    if highlight:
        for idx in highlight:
            ts.append(("BACKGROUND", (0, idx), (-1, idx), GREEN_LT))
    t.setStyle(TableStyle(ts))
    return t

def grid(headers, rows, widths=None, accent=NAVY):
    n = len(headers)
    widths = widths or [CW / n] * n
    head = [Paragraph(h, S["th"]) for h in headers]
    body_r = [[Paragraph(str(c), S["td"]) for c in r] for r in rows]
    t = Table([head] + body_r, colWidths=widths)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,0), accent),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [WHITE, PALE]),
        ("BOX",           (0,0), (-1,-1), 0.5, GRID),
        ("INNERGRID",     (0,0), (-1,-1), 0.3, GRID),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 7),
        ("RIGHTPADDING",  (0,0), (-1,-1), 7),
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
    ]))
    return t

def new_grid(headers, rows, widths=None):
    return grid(headers, rows, widths, accent=FOREST)

def pills(labels, palette=None):
    palette = palette or [NAVY, BLUE, TEAL, PURPLE, AMBER, GREEN, RED, FOREST]
    cw = [CW / len(labels)] * len(labels)
    cells = [Paragraph(lb, S["pill"]) for lb in labels]
    t = Table([cells], colWidths=cw)
    ts = [("TOPPADDING",(0,0),(-1,-1),5),("BOTTOMPADDING",(0,0),(-1,-1),5),
          ("LEFTPADDING",(0,0),(-1,-1),2),("RIGHTPADDING",(0,0),(-1,-1),2)]
    for i, c in enumerate(palette[:len(labels)]):
        ts.append(("BACKGROUND",(i,0),(i,0),c))
    t.setStyle(TableStyle(ts))
    return t

def code_block(lines, accent=SKY):
    rows = [[Paragraph(ln, S["code"])] for ln in lines]
    t = Table(rows, colWidths=[CW])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), colors.HexColor("#F0F7FF")),
        ("BOX",           (0,0), (-1,-1), 0.5, GRID),
        ("LINEBEFORE",    (0,0), (0,-1), 3, accent),
        ("TOPPADDING",    (0,0), (-1,-1), 2),
        ("BOTTOMPADDING", (0,0), (-1,-1), 2),
        ("LEFTPADDING",   (0,0), (-1,-1), 14),
        ("RIGHTPADDING",  (0,0), (-1,-1), 8),
    ]))
    return t

def new_code(lines):
    rows = [[Paragraph(ln, S["code"])] for ln in lines]
    t = Table(rows, colWidths=[CW])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), FOREST_LT),
        ("BOX",           (0,0), (-1,-1), 0.5, GREEN),
        ("LINEBEFORE",    (0,0), (0,-1), 3, GREEN),
        ("TOPPADDING",    (0,0), (-1,-1), 2),
        ("BOTTOMPADDING", (0,0), (-1,-1), 2),
        ("LEFTPADDING",   (0,0), (-1,-1), 14),
        ("RIGHTPADDING",  (0,0), (-1,-1), 8),
    ]))
    return t

def two_col(left, right, gap=10):
    half = (CW - gap) / 2
    rows = []
    for i in range(max(len(left), len(right))):
        l = left[i]  if i < len(left)  else sp(1)
        r = right[i] if i < len(right) else sp(1)
        rows.append([l, r])
    t = Table(rows, colWidths=[half, half])
    t.setStyle(TableStyle([
        ("VALIGN",       (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING",  (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING",   (0,0), (-1,-1), 0),
        ("BOTTOMPADDING",(0,0), (-1,-1), 2),
        ("LINEAFTER",    (0,0), (0,-1), 0.4, RULE),
        ("LEFTPADDING",  (1,0), (1,-1), 10),
    ]))
    return t

def change_tag(label, kind="new"):
    color = GREEN if kind == "new" else AMBER if kind == "upgrade" else RED
    bg    = GREEN_LT if kind == "new" else AMBER_LT if kind == "upgrade" else RED_LT
    p = Paragraph(f"<b>{label}</b>",
                  mk("ct", fontName="Helvetica-Bold", fontSize=6.5, textColor=color,
                     leading=10, alignment=TA_CENTER))
    t = Table([[p]], colWidths=[18*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), bg),
        ("BOX",           (0,0), (-1,-1), 0.5, color),
        ("TOPPADDING",    (0,0), (-1,-1), 2),
        ("BOTTOMPADDING", (0,0), (-1,-1), 2),
        ("LEFTPADDING",   (0,0), (-1,-1), 4),
        ("RIGHTPADDING",  (0,0), (-1,-1), 4),
    ]))
    return t

def dvite():
    steps = [("01","DETECT","Fusion outputs emotion\n+ severity score"),
             ("02","VALIDATE","Clinically-worded\nempathy response"),
             ("03","INTERVENE","CBT/DBT technique\nmatched to severity"),
             ("04","TRACK","User rates 1-10\nTrend computed"),
             ("05","ESCALATE","Threshold breach\n-&gt; helplines")]
    shades = [colors.HexColor("#0F2744"), colors.HexColor("#12305A"),
              colors.HexColor("#163970"), colors.HexColor("#1A4280"),
              colors.HexColor("#1D4B90")]
    cells = []
    for num, label, desc in steps:
        html = (f'<font size="7" color="#93C5FD"><b>{num}</b></font>  '
                f'<font size="8.5" color="white"><b>{label}</b></font><br/>'
                f'<font size="7" color="#BFDBFE">{desc}</font>')
        cells.append(Paragraph(html, ParagraphStyle("dv", fontName="Helvetica",
                     fontSize=8, leading=13, alignment=TA_CENTER)))
    cw = [CW / 5] * 5
    t = Table([cells], colWidths=cw)
    ts = [("TOPPADDING",(0,0),(-1,-1),10),("BOTTOMPADDING",(0,0),(-1,-1),10),
          ("LEFTPADDING",(0,0),(-1,-1),3),("RIGHTPADDING",(0,0),(-1,-1),3),
          ("INNERGRID",(0,0),(-1,-1),0.5,colors.HexColor("#3B6BAF")),
          ("BOX",(0,0),(-1,-1),0.5,SKY)]
    for i, sh in enumerate(shades):
        ts.append(("BACKGROUND",(i,0),(i,0),sh))
    t.setStyle(TableStyle(ts))
    return t

def version_compare(rows):
    w = CW / 2
    data = [[Paragraph("v2.0 BLUEPRINT", S["th"]),
             Paragraph("v3.0 HARDENED", S["th"])]]
    for r in rows:
        data.append([Paragraph(str(r[0]), S["td"]),
                     Paragraph(f"<b>{str(r[1])}</b>",
                               mk("vc", fontSize=8, textColor=FOREST, leading=12))])
    t = Table(data, colWidths=[w, w])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,0), NAVY),
        ("BACKGROUND",    (1,0), (1,0), FOREST),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [WHITE, PALE]),
        ("BOX",           (0,0), (-1,-1), 0.5, GRID),
        ("INNERGRID",     (0,0), (-1,-1), 0.3, GRID),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 8),
        ("RIGHTPADDING",  (0,0), (-1,-1), 8),
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
        ("LINEAFTER",     (0,0), (0,-1), 1.5, GREEN),
    ]))
    return t

def closing():
    html = ('<font size="11" color="white"><b>'
            'DETECT  -&gt;  VALIDATE  -&gt;  INTERVENE  -&gt;  TRACK  -&gt;  ESCALATE'
            '</b></font><br/>'
            '<font size="7.5" color="#BAE6FD">'
            'Humorix AI v3.0  -  Hardened  -  Adaptive  -  Clinically-viable'
            '</font>')
    p = Paragraph(html, ParagraphStyle("cl", fontName="Helvetica",
                  fontSize=9, leading=20, alignment=TA_CENTER))
    t = Table([[p]], colWidths=[CW])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), NAVY),
        ("TOPPADDING",    (0,0), (-1,-1), 16),
        ("BOTTOMPADDING", (0,0), (-1,-1), 16),
        ("LINEABOVE",     (0,0), (-1,0), 3, SKY),
    ]))
    return t


# ══════════════════════════════════════════════════════════════════════════
def build():
    story = []

    # ── COVER ───────────────────────────────────────────────────────────────
    story.append(sp(45))
    cover_html = (
        '<font size="10" color="#60A5FA">HUMORIX AI</font><br/>'
        '<font size="36" color="white"><b>Blueprint v3.0</b></font><br/>'
        '<font size="10" color="#4ADE80"><b>Hardened Edition</b></font><br/>'
        '<font size="8" color="#60A5FA">--------------------------------------</font><br/>'
        '<font size="9" color="#BAE6FD">'
        'Memory Layer  -  Dynamic Fusion  -  Uncertainty Scoring  -  Edge Privacy  -  '
        'Intervention Validation  -  Personalization  -  Resilience Protocol'
        '</font>'
    )
    cp = Paragraph(cover_html, ParagraphStyle("cv", fontName="Helvetica",
                   fontSize=9, leading=28, alignment=TA_CENTER))
    ct = Table([[cp]], colWidths=[CW])
    ct.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), NAVY),
        ("TOPPADDING",    (0,0), (-1,-1), 30),
        ("BOTTOMPADDING", (0,0), (-1,-1), 30),
        ("LINEBELOW",     (0,-1), (-1,-1), 4, GREEN),
    ]))
    story.append(ct)
    story.append(sp(14))

    story.append(kv([
        ["Version",    "3.0 - Hardened Edition  (builds on v2.0 Developer Blueprint)"],
        ["What's New", "Dynamic fusion weights · Uncertainty scoring · Semantic crisis detection · "
                       "Affective memory (vector store) · On-device ONNX inference · "
                       "Intervention efficacy loop · Personalization layer · Control-mode toggle · "
                       "Visible privacy UX · Evaluation metrics framework"],
        ["Disclaimer", "Supportive tool only. Not a substitute for licensed professional mental health care."],
    ]))
    story.append(sp(8))
    story.append(note_box(
        "v3.0 is a direct response to critical review of v2.0. Every change is tagged  "
        "[ UPGRADE ]  or  [ NEW ]  throughout this document so you can track exactly "
        "what changed and why.", "new"))
    story.append(PageBreak())


    # ── WHAT CHANGED ────────────────────────────────────────────────────────
    story.append(section("What Changed from v2.0 to v3.0",
                          "9 critical improvements — tagged throughout the document"))
    story.append(sp(6))
    story.append(version_compare([
        ["Static fusion weights (0.45 / 0.30 / 0.25)",
         "Dynamic weights — degrade gracefully when modality unreliable"],
        ["No uncertainty output",
         "overall_uncertainty score added — softer responses when AI is unsure"],
        ["Keyword-only crisis detection",
         "Semantic intent classifier + multi-message pattern detection"],
        ["Single-moment conflict handling",
         "Session-level denial pattern tracking across multiple messages"],
        ["Generic DVITE for all users",
         "Personalization layer: response style, length, tone memory"],
        ["Satvic always-on",
         "User preference gate — Satvic suppressed if not opted-in"],
        ["UI with no explicit control mode",
         "Control Mode Toggle: Minimal / Voice-only / Full Multimodal"],
        ["Privacy as policy only",
         "Visible real-time processing indicators + deletion confirmation UX"],
        ["No success measurement",
         "Full evaluation metrics: efficacy loop, KPIs, clinical dashboard"],
    ]))
    story.append(PageBreak())


    # ── TOC ─────────────────────────────────────────────────────────────────
    story.append(section("Table of Contents"))
    story.append(sp(6))
    toc = [
        ("A", "System Architecture (Unchanged Foundation)",   ["A1 Five-Layer Pipeline", "A2 File Structure v3", "A3 WebSocket Flow"]),
        ("B", "Safety Middleware — Hardened",                  ["B1 Semantic Crisis Detection (UPGRADE)", "B2 Multi-Message Pattern Tracking (NEW)", "B3 Existing Keyword Layer retained"]),
        ("C", "Dynamic Fusion Engine v3",                     ["C1 Dynamic Weight Calculation (UPGRADE)", "C2 Uncertainty Score (NEW)", "C3 Degradation Protocol (NEW)"]),
        ("D", "Affective Memory Layer",                       ["D1 Vector Store Architecture (NEW)", "D2 Privacy: Local Encrypted Store", "D3 Longitudinal Context Usage"]),
        ("E", "DVITE + Personalization",                      ["E1 Protocol Overview", "E2 Personalization Layer (NEW)", "E3 Disorder Module Library", "E4 Intervention Efficacy Loop (NEW)"]),
        ("F", "Conflict Handling — Upgraded",                 ["F1 Session-Level Denial Tracking (UPGRADE)", "F2 Empathetic Inquiry Protocol retained"]),
        ("G", "Satvic Wellness — Repositioned",               ["G1 User Preference Gate (UPGRADE)", "G2 Wellness Nudge retained", "G3 Meal Plans & Food Laws"]),
        ("H", "UI System — Hardened",                         ["H1 Control Mode Toggle (NEW)", "H2 Visible Privacy UX (NEW)", "H3 Adaptive States retained"]),
        ("I", "Edge Privacy & Deployment",                    ["I1 ONNX On-Device Inference (UPGRADE)", "I2 Ephemeral Processing retained", "I3 Deployment Modes"]),
        ("J", "Evaluation Metrics & KPIs",                   ["J1 Intervention Efficacy Loop (NEW)", "J2 System KPIs (NEW)", "J3 Clinical Dashboard"]),
        ("K", "Ethics, Limitations & Roadmap",               ["K1 Non-Negotiables", "K2 Known Gaps", "K3 v4.0 Roadmap"]),
    ]
    left_b, right_b = [], []
    for i, (let, title, subs) in enumerate(toc):
        block = [Paragraph(f"<b>{let} — {title}</b>", S["toc_p"])]
        for s in subs: block.append(Paragraph(s, S["toc_i"]))
        block.append(sp(4))
        (left_b if i % 2 == 0 else right_b).extend(block)
    story.append(two_col(left_b, right_b))
    story.append(PageBreak())


    # ══ A — ARCHITECTURE ════════════════════════════════════════════════════
    story.append(banner("A", "System Architecture", "Foundation unchanged · New modules added at Decision and Data layers"))
    story.append(sp(10))
    story.append(section("A1  Five-Layer Pipeline — v3 Updates"))
    story.append(grid(
        ["#", "Layer", "v2 Components", "v3 Additions"],
        [["1","INPUT",      "Webcam · Mic · Text",
          "Control Mode toggle gates which inputs are active"],
         ["2","PROCESSING", "OpenCV · Librosa · Tokenizers",
          "Confidence scoring per frame now feeds dynamic weight calculator"],
         ["3","EMOTION",    "FER · Voice ML · Sentiment",
          "Uncertainty score computed alongside each modality output"],
         ["4","DECISION",   "Fusion · DVITE · Satvic KB",
          "+ Affective Memory (ChromaDB) · Personalization Layer · Efficacy Loop"],
         ["5","OUTPUT",     "FastAPI · Streamlit · Crisis",
          "+ Real-time processing indicator · Deletion confirmation UX"]],
        widths=[CW*0.04, CW*0.12, CW*0.34, CW*0.50]
    ))
    story.append(sp(8))
    story.append(section("A2  File Structure — v3"))
    story.append(code_block([
        "humorix/",
        "    app/",
        "        main.py",
        "        core/",
        "            safety.py          # Gatekeeper — keyword + semantic (UPGRADE)",
        "            fusion.py          # Dynamic weights + uncertainty score (UPGRADE)",
        "            triage.py          # DVITE + personalization layer (UPGRADE)",
        "            memory.py          # Affective vector store (NEW)",
        "            efficacy.py        # Intervention success measurement (NEW)",
        "            wellness.py        # Satvic — preference-gated (UPGRADE)",
        "    models/",
        "        vision/                # MediaPipe + DeepFace (unchanged)",
        "        audio/                 # Librosa + speech model (unchanged)",
        "        nlp/                   # Transformer sentiment (unchanged)",
        "        intent/                # Semantic crisis intent classifier (NEW)",
        "    data/",
        "        schemas.py",
        "        protocols.py",
        "        resources.py",
        "        user_profile.py        # Preference + style memory (NEW)",
        "    vector_store/              # Local encrypted ChromaDB (NEW)",
        "        affective_context.db",
    ]))
    story.append(PageBreak())


    # ══ B — SAFETY HARDENED ═════════════════════════════════════════════════
    story.append(banner("B", "Safety Middleware — Hardened",
                        "Keyword layer retained · Semantic detection added · Multi-message patterns",
                        color=colors.HexColor("#3B0000")))
    story.append(sp(10))
    story.append(note_box(
        "The v2 keyword list was a necessary start — but people in crisis rarely use textbook language. "
        "'I'm tired of everything' carries the same risk as 'I want to die.' v3 adds two layers above keywords.", "crit"))
    story.append(sp(8))

    story.append(new_section("B1  Semantic Crisis Detection  [ UPGRADE ]",
                              "Intent classifier runs in parallel with keyword check"))
    story.append(body(
        "A fine-tuned transformer intent classifier runs on every input alongside the keyword check. "
        "It detects semantic hopelessness and veiled crisis intent even when no trigger word is present."))
    story.append(sp(5))
    story.append(new_code([
        "# app/core/safety.py  (v3)",
        "",
        "CRISIS_KEYWORDS = {'kill', 'die', 'suicide', 'end it', 'hurt myself', 'cant go on'}",
        "",
        "SEMANTIC_RISK_PHRASES = [",
        "    'tired of everything', 'nothing matters anymore', 'wish I could disappear',",
        "    'everyone would be better off', 'no point anymore', 'cant do this anymore'",
        "]",
        "",
        "def run_safety_check(text: str, intent_model) -> dict:",
        "    # Layer 1: Fast keyword scan (< 2ms)",
        "    if any(kw in text.lower() for kw in CRISIS_KEYWORDS):",
        "        return _crisis_response('keyword')",
        "",
        "    # Layer 2: Semantic phrase patterns (< 5ms)",
        "    if any(phrase in text.lower() for phrase in SEMANTIC_RISK_PHRASES):",
        "        return _crisis_response('semantic_phrase')",
        "",
        "    # Layer 3: Intent classifier (< 20ms, runs async)",
        "    intent_score = intent_model.predict(text)  # Fine-tuned on crisis datasets",
        "    if intent_score['crisis_probability'] > 0.75:",
        "        return _crisis_response('intent_classifier')",
        "",
        "    return {'status': 'SAFE', 'action': 'PROCEED'}",
    ]))
    story.append(sp(8))

    story.append(new_section("B2  Multi-Message Pattern Tracking  [ NEW ]",
                              "Emotions are patterns, not snapshots"))
    story.append(body(
        "A session-level buffer stores the last N messages. If hopelessness indicators appear "
        "across multiple messages — even if none individually cross the threshold — the system "
        "escalates its sensitivity and prompts an empathetic check-in."))
    story.append(sp(5))
    story.append(new_code([
        "# app/core/safety.py  — pattern tracker",
        "",
        "class SessionSafetyTracker:",
        "    def __init__(self, window=5):",
        "        self.buffer = []          # Last N message risk scores",
        "        self.window = window",
        "",
        "    def update(self, risk_score: float):",
        "        self.buffer.append(risk_score)",
        "        if len(self.buffer) > self.window:",
        "            self.buffer.pop(0)",
        "",
        "    def sustained_risk(self, threshold=0.4) -> bool:",
        "        # True if average risk across window exceeds threshold",
        "        if len(self.buffer) < 3:",
        "            return False",
        "        return sum(self.buffer) / len(self.buffer) > threshold",
    ]))
    story.append(PageBreak())


    # ══ C — DYNAMIC FUSION ══════════════════════════════════════════════════
    story.append(banner("C", "Dynamic Fusion Engine v3",
                        "Adaptive weights · Uncertainty score · Degradation protocol",
                        color=colors.HexColor("#0C1F3C")))
    story.append(sp(10))
    story.append(note_box(
        "v2 used fixed weights (0.45 / 0.30 / 0.25). The core problem: bad lighting or background noise "
        "made those weights actively misleading. v3 asks 'who is trustworthy right now?' and leads with that.", "warn"))
    story.append(sp(8))

    story.append(new_section("C1  Dynamic Weight Calculation  [ UPGRADE ]"))
    story.append(new_code([
        "# app/core/fusion.py  (v3)",
        "",
        "BASE = {'face': 0.45, 'voice': 0.30, 'text': 0.25}",
        "",
        "def dynamic_weights(face_conf: float, voice_conf: float,",
        "                    env_noise_high: bool = False) -> dict:",
        "    w = BASE.copy()",
        "",
        "    # Degrade face weight in unreliable conditions",
        "    if face_conf < 0.5:",
        "        deficit = w['face'] * (1 - face_conf / 0.5)",
        "        w['face'] -= deficit",
        "        w['voice'] += deficit * 0.6   # Voice picks up most of face's slack",
        "        w['text']  += deficit * 0.4",
        "",
        "    # Degrade voice weight in noisy environments",
        "    if env_noise_high and voice_conf < 0.5:",
        "        deficit = w['voice'] * 0.5",
        "        w['voice'] -= deficit",
        "        w['text']  += deficit",
        "",
        "    # Normalise to sum = 1.0",
        "    total = sum(w.values())",
        "    return {k: v / total for k, v in w.items()}",
        "",
        "def calculate_fusion(face: float, voice: float, text: float,",
        "                     face_conf: float, voice_conf: float,",
        "                     env_noise: bool = False) -> dict:",
        "    w = dynamic_weights(face_conf, voice_conf, env_noise)",
        "    fused = face*w['face'] + voice*w['voice'] + text*w['text']",
        "    if max(face, voice, text) > 0.9:",
        "        fused = max(face, voice, text)  # Trust a high-confidence signal",
        "    return {'fused_score': fused, 'weights_used': w}",
    ]))
    story.append(sp(8))

    story.append(new_section("C2  Uncertainty Score  [ NEW ]",
                              "How sure is the AI? Softer responses when it isn't."))
    story.append(body(
        "The uncertainty score is the system's humility metric. When overall_confidence is low, "
        "the AI adapts its language — hedging rather than asserting, asking rather than prescribing. "
        "This prevents the system from sounding like a fake therapist that claims certainty it doesn't have."))
    story.append(sp(5))
    story.append(new_code([
        "# Computed after every fusion call",
        "",
        "def compute_uncertainty(overall_confidence: float,",
        "                        weight_variance: float) -> dict:",
        "    uncertainty = 1.0 - overall_confidence",
        "    return {",
        "        'overall_uncertainty': round(uncertainty, 3),",
        "        'response_mode': 'tentative' if uncertainty > 0.4 else 'direct'",
        "    }",
        "",
        "# Response tone examples based on uncertainty:",
        "# uncertainty > 0.4 -> 'I'm noticing something that might be anxiety — does that feel right?'",
        "# uncertainty < 0.2 -> 'I can see you're experiencing significant anxiety right now.'",
    ]))
    story.append(sp(8))

    story.append(new_section("C3  Degradation Protocol  [ NEW ]",
                              "Formal fallback logic — never fail silently"))
    story.append(new_grid(
        ["Condition", "Trigger", "System Response", "UI Message"],
        [["Face unavailable",  "face_conf < 0.3",
          "Face weight set to 0. Voice + text carry 100%.",
          "'Video analysis unavailable — switching to voice support'"],
         ["Voice noisy",       "env_noise_high AND voice_conf < 0.4",
          "Voice weight halved. Text compensates.",
          "'Background noise detected — relying on text signals'"],
         ["All low-confidence","All modalities < 0.35",
          "Soft mode: no intervention pushed. Ask user directly.",
          "'I want to make sure I understand — how are you feeling right now?'"],
         ["Text only mode",    "User selects text-only in Control Mode",
          "Face weight = 0, voice weight = 0, text weight = 1.0",
          "No camera/mic indicator shown"]],
        widths=[CW*0.16, CW*0.20, CW*0.34, CW*0.30]
    ))
    story.append(PageBreak())


    # ══ D — MEMORY LAYER ════════════════════════════════════════════════════
    story.append(banner("D", "Affective Memory Layer",
                        "Vector store · Local encrypted · Longitudinal context · Privacy-first",
                        color=colors.HexColor("#1A0D33")))
    story.append(sp(10))
    story.append(note_box(
        "If a user mentions a conflict at work on Tuesday, the AI shouldn't have forgotten it by Friday. "
        "The Memory Layer stores contextual emotional embeddings — not raw biometrics — locally on the device.", "new"))
    story.append(sp(8))

    story.append(new_section("D1  Vector Store Architecture  [ NEW ]"))
    story.append(kv([
        ["Database",       "ChromaDB (local) — lightweight, Python-native, no server required"],
        ["What is stored", "Semantic embeddings of: session emotional themes · trigger contexts · "
                           "successful intervention types · disorder risk history"],
        ["What is NOT stored","Raw video frames · audio recordings · biometric readings — never persisted"],
        ["Embedding model", "sentence-transformers (e.g. all-MiniLM-L6-v2) — runs entirely on-device"],
        ["Encryption",     "AES-256 encryption on the ChromaDB file. Key stored in device keychain."],
        ["Retention",      "Default: 90 days. User-configurable. Full deletion on request (immediate)."],
    ]))
    story.append(sp(6))
    story.append(new_code([
        "# app/core/memory.py",
        "",
        "import chromadb",
        "from sentence_transformers import SentenceTransformer",
        "",
        "class AffectiveMemory:",
        "    def __init__(self):",
        "        self.client = chromadb.PersistentClient(path='./vector_store')  # Local only",
        "        self.col    = self.client.get_or_create_collection('affective_context')",
        "        self.model  = SentenceTransformer('all-MiniLM-L6-v2')",
        "",
        "    def store_session(self, session_summary: str, metadata: dict):",
        "        embedding = self.model.encode(session_summary).tolist()",
        "        self.col.add(embeddings=[embedding],",
        "                     documents=[session_summary],",
        "                     metadatas=[metadata],",
        "                     ids=[metadata['session_id']])",
        "",
        "    def retrieve_context(self, current_input: str, n=3) -> list:",
        "        query_emb = self.model.encode(current_input).tolist()",
        "        results   = self.col.query(query_embeddings=[query_emb], n_results=n)",
        "        return results['documents'][0]   # Top-N relevant past contexts",
    ]))
    story.append(sp(8))

    story.append(new_section("D2  Longitudinal Context Usage"))
    story.append(new_grid(
        ["Use Case", "How Memory Is Used", "Clinical Value"],
        [["Repeated triggers",    "Detect that 'work stress' appears in 3 of last 5 sessions",
          "Flag as persistent stressor — suggest dedicated GAD module"],
         ["Intervention history", "Track which techniques worked vs. which were skipped",
          "Stop suggesting interventions the user consistently dismisses"],
         ["Denial pattern",       "Log 'user said OK / biometrics said distress' mismatches",
          "After 5+ mismatches, gently probe for disclosure readiness"],
         ["Progress tracking",    "Compare severity scores across sessions",
          "Visualise trend in session history sidebar"],
         ["Satvic alignment",     "Track which wellness suggestions led to positive follow-up mood",
          "Personalise wellness recommendations over time"]],
        widths=[CW*0.22, CW*0.40, CW*0.38]
    ))
    story.append(PageBreak())


    # ══ E — DVITE + PERSONALIZATION ═════════════════════════════════════════
    story.append(banner("E", "DVITE + Personalization Layer",
                        "Protocol unchanged · Personalization added · Efficacy loop new",
                        color=colors.HexColor("#0F2044")))
    story.append(sp(10))
    story.append(section("E1  DVITE Protocol — Unchanged Core"))
    story.append(dvite())
    story.append(sp(8))

    story.append(new_section("E2  Personalization Layer  [ NEW ]",
                              "Same protocol — different voice, pace, and depth per user"))
    story.append(body(
        "DVITE was clean but generic — same tone for every user, every session. "
        "The personalization layer wraps the protocol: before generating any response, "
        "it reads the user's style profile and adjusts accordingly. No structural change to DVITE itself."))
    story.append(sp(6))
    story.append(new_grid(
        ["Dimension", "Options", "How Detected / Set"],
        [["Response length",    "Short / Medium / Long",
          "User preference at onboarding + adaptive from engagement patterns"],
         ["Tone",              "Warm-emotional / Analytical-logical / Balanced",
          "Detected from user's own language patterns across first 3 sessions"],
         ["Intervention style","Sensory-first (grounding) / Cognitive-first (CBT) / Mixed",
          "Tracked from which interventions the user completes vs. skips"],
         ["Fatigue detection", "Flag if user has received same technique 3x in session",
          "Auto-rotate to next technique in same tier"],
         ["Disclosure speed",  "Fast discloser / slow discloser",
          "Inferred from how many sessions before significant personal sharing"]],
        widths=[CW*0.20, CW*0.26, CW*0.54]
    ))
    story.append(sp(6))
    story.append(new_code([
        "# data/user_profile.py",
        "",
        "class UserProfile:",
        "    response_length:    str   = 'medium'    # short | medium | long",
        "    tone:               str   = 'balanced'  # warm | analytical | balanced",
        "    preferred_modality: str   = 'mixed'     # sensory | cognitive | mixed",
        "    fatigue_log:        list  = []           # last N interventions used",
        "    denial_count:       int   = 0            # 'OK' + high-bio mismatches",
        "    disclosure_speed:   str   = 'unknown'   # fast | slow | unknown",
    ]))
    story.append(sp(8))

    story.append(new_section("E3  Intervention Efficacy Loop  [ NEW ]",
                              "Measures whether the intervention actually worked"))
    story.append(body(
        "The current system selects an intervention and moves on. The efficacy loop adds a "
        "measurement step: after each intervention, the system re-scans biometrics for 60 seconds "
        "and checks whether distress indicators have reduced. This turns a static tool into an "
        "adaptive clinical assistant."))
    story.append(sp(6))
    story.append(new_code([
        "# app/core/efficacy.py",
        "",
        "def measure_efficacy(pre_score: float, post_score: float,",
        "                     intervention_type: str, user_id: str) -> dict:",
        "    change = pre_score - post_score    # Positive = improvement",
        "    pct    = (change / pre_score) * 100 if pre_score > 0 else 0",
        "",
        "    if pct >= 20:",
        "        result = 'effective'",
        "    elif pct >= 5:",
        "        result = 'partial'",
        "    else:",
        "        result = 'ineffective'",
        "",
        "    # Log to user profile for personalization",
        "    log_intervention_result(user_id, intervention_type, result)",
        "",
        "    # If ineffective: try next intervention in same tier",
        "    # If still ineffective after 2 attempts: escalate severity level",
        "    return {'result': result, 'pct_change': round(pct, 1)}",
    ]))
    story.append(sp(6))
    story.append(new_grid(
        ["Result", "Criterion", "System Action"],
        [["Effective",    "> 20% bio score reduction",  "Affirm, log success, continue"],
         ["Partial",      "5-20% reduction",            "Continue, offer one additional technique"],
         ["Ineffective",  "< 5% reduction",             "Try next technique in tier; after 2 fails — escalate severity"]],
        widths=[CW*0.18, CW*0.32, CW*0.50]
    ))
    story.append(sp(8))

    story.append(section("E4  Disorder Module Library — 8 Conditions (unchanged)"))
    story.append(grid(
        ["Code", "Condition", "Escalate", "Techniques (by severity)"],
        [["GAD",   "Generalised Anxiety",       "7/10+",
          "Mild: 5-4-3-2-1 · Extended exhale  |  Mod: 4-7-8 · PMR · Thought challenge  |  Severe: CBT referral"],
         ["PANIC", "Panic Disorder",            "8/10+",
          "Mild: Box breathing · Floor grounding  |  Mod: DARE  |  Severe: Crisis stabilisation"],
         ["MDD",   "Major Depressive Disorder", "7/10+",
          "Mild: Activation · Gratitude  |  Mod: Pleasure prediction · Thought record  |  Severe: Safety inquiry"],
         ["PTSD",  "Post-Traumatic Stress",     "7/10+",
          "Mild: Grounding anchor · Safe place  |  Mod: Window of tolerance  |  Severe: EMDR referral"],
         ["MANIA", "Bipolar — Manic Episode",   "7/10+",
          "Mild: Sleep regulation  |  Mod: 48-hr decision rule  |  Severe: Psychiatrist contact"],
         ["OCD",   "Obsessive-Compulsive",      "8/10+",
          "Mild: Thought defusion · Delay  |  Mod: ERP ladder  |  Severe: Specialist referral"],
         ["ED",    "Eating Disorders",          "6/10+",
          "Mild: Body neutrality  |  Mod: Voice challenging  |  Severe: NAED helpline"],
         ["ADHD",  "Attention Deficit",         "8/10+",
          "Mild: 2-min rule · Pomodoro  |  Mod: Task hacks  |  Severe: Psychiatry eval"]],
        widths=[CW*0.07, CW*0.18, CW*0.10, CW*0.65]
    ))
    story.append(PageBreak())


    # ══ F — CONFLICT HANDLING ═══════════════════════════════════════════════
    story.append(banner("F", "Conflict Handling — Upgraded",
                        "Session-level denial tracking added to v2 single-moment logic",
                        color=colors.HexColor("#1F1200")))
    story.append(sp(10))
    story.append(new_section("F1  Session-Level Denial Pattern Tracking  [ UPGRADE ]"))
    story.append(body(
        "v2 handled the conflict in a single moment. But if a user says 'I'm fine' while "
        "biometrics consistently show distress — across 5, 7, 10 messages — the system needs "
        "to recognise the pattern and gradually adapt its tone rather than repeating the same "
        "empathetic inquiry each time."))
    story.append(sp(6))
    story.append(new_code([
        "# Integrated into UserProfile",
        "",
        "def handle_conflict(user_text: str, bio_score: float,",
        "                    profile: UserProfile) -> dict:",
        "    sentiment = analyze_sentiment(user_text)",
        "    conflict  = bio_score > 0.7 and sentiment < 0.5",
        "",
        "    if conflict:",
        "        profile.denial_count += 1",
        "",
        "        if profile.denial_count <= 3:",
        "            # Early stage: gentle empathetic inquiry",
        "            tone = 'empathetic_inquiry'",
        "            msg  = 'I hear you are okay — I am noticing some tension. I am here.'",
        "",
        "        elif profile.denial_count <= 7:",
        "            # Mid stage: acknowledge the pattern, give more space",
        "            tone = 'spacious_presence'",
        "            msg  = 'No pressure at all — I am just here whenever you are ready.'",
        "",
        "        else:",
        "            # Late stage: direct but gentle — name the mismatch",
        "            tone = 'named_mismatch'",
        "            msg  = 'I have noticed a pattern and want to check in directly —'",
        "                   ' how are things actually going?'",
        "",
        "        return {'tone': tone, 'response': msg, 'denial_count': profile.denial_count}",
        "",
        "    profile.denial_count = 0   # Reset on genuine self-disclosure",
        "    return {'tone': 'standard', 'response': 'Great to hear.'}",
    ]))
    story.append(PageBreak())


    # ══ G — SATVIC REPOSITIONED ═════════════════════════════════════════════
    story.append(banner("G", "Satvic Wellness — Repositioned",
                        "Optional lifestyle layer · User preference gate · Nudge method retained",
                        color=colors.HexColor("#073020")))
    story.append(sp(10))
    story.append(note_box(
        "The v2 risk: users came for mental health support and received diet advice. "
        "v3 makes Satvic explicitly opt-in and positions it as a lifestyle companion, "
        "never a therapeutic solution.", "warn"))
    story.append(sp(8))

    story.append(new_section("G1  User Preference Gate  [ UPGRADE ]"))
    story.append(kv([
        ["Onboarding Question","'Would you like lifestyle and wellness suggestions (Satvic philosophy)?  Yes / No / Ask me later'"],
        ["Default",           "OFF — user must opt in. Not assumed."],
        ["Suppression Rule",  "Even if opted-in: suppressed when severity_score > 0.6 (unchanged from v2)"],
        ["Preference Code",   "if user_profile.satvic_enabled == False: skip wellness module entirely"],
        ["Positioning",       "Framed as: 'Optional lifestyle layer, not a therapeutic solution'"],
    ]))
    story.append(sp(8))

    story.append(section("G2  Wellness Nudge — Retained from v2"))
    story.append(note_box("The Wellness Nudge delivery method is unchanged. "
                           "Contextual, soft, woven into conversation — not prescribed.", "ok"))
    story.append(sp(8))

    story.append(section("G3  Satvic Reference — 9 Laws & Meal Plans"))
    story.append(grid(
        ["#", "Food Law", "Avoid", "Eat"],
        [["1","No Dead Foods","Packaged / tinned","Fresh fruits, veg, grains — farm to kitchen"],
         ["2","No Refined","White sugar, flour, refined oil","Dates, jaggery, millets, cold-pressed oils"],
         ["3","No Animal","Meat, dairy, eggs","Coconut milk, almond milk, cashew (homemade)"],
         ["4","Less Grain, More Veg","Grain-dominant plates","2x more vegetables than grain always"],
         ["5","Seasonal & Local","Imported exotics","Regional seasonal produce"],
         ["6","Soak Nuts","Unsoaked nuts","Soak 6-8h, discard water"],
         ["7","Mild Spices","Packaged masalas","Fresh green chili, black pepper, herbs"],
         ["8","Minimal Cooking","High-heat frying","Lowest temp, shortest time — raw if possible"],
         ["9","No Stimulants","Tea, coffee, onions, garlic","Herbal teas, coconut water"]],
        widths=[CW*0.04, CW*0.18, CW*0.34, CW*0.44]
    ))
    story.append(PageBreak())


    # ══ H — UI HARDENED ═════════════════════════════════════════════════════
    story.append(banner("H", "UI System — Hardened",
                        "Control Mode Toggle new · Visible privacy UX new · Adaptive states retained"))
    story.append(sp(10))

    story.append(new_section("H1  Control Mode Toggle  [ NEW ]",
                              "Users control exactly what the AI can see"))
    story.append(body(
        "Not every user wants the AI watching their face and analysing their voice at all times. "
        "The Control Mode toggle gives users explicit agency over which modalities are active — "
        "without reducing the quality of support in any mode."))
    story.append(sp(6))
    story.append(new_grid(
        ["Mode", "Active Inputs", "Fusion Weights", "Use Case"],
        [["Minimal (Text Only)", "Text input only",
          "Text 1.0 / Face 0.0 / Voice 0.0",
          "Maximum privacy · public spaces · low-bandwidth"],
         ["Voice + Text",        "Mic + Text",
          "Voice 0.55 / Text 0.45 / Face 0.0",
          "Private voice support without camera"],
         ["Full Multimodal",     "Webcam + Mic + Text",
          "Dynamic (face 0.45 base)",
          "Maximum accuracy — full support capability"]],
        widths=[CW*0.20, CW*0.22, CW*0.26, CW*0.32]
    ))
    story.append(sp(8))

    story.append(new_section("H2  Visible Privacy UX  [ NEW ]",
                              "Trust is not just policy — it is UX"))
    story.append(body(
        "Users don't trust what they can't see. v3 adds real-time visible indicators that "
        "show exactly what is being processed and confirm when data is deleted — not buried in a settings menu."))
    story.append(sp(6))
    story.append(new_grid(
        ["Element", "Behaviour", "Location"],
        [["Camera indicator",      "'Camera ON · Analysing'  /  'Camera OFF'  — colour-coded dot",
          "Header bar — always visible"],
         ["Mic indicator",         "'Voice ON · Processing'  /  'Voice OFF'",
          "Header bar — always visible"],
         ["Processing badge",      "Subtle pulsing indicator while biometrics are being analysed",
          "Bottom of Adaptive Canvas"],
         ["Deletion confirmation", "Animation: shield icon + 'Session data deleted' on confirm",
          "Full-screen overlay for 2 seconds"],
         ["Data age label",        "'Memory: 3 sessions stored · Last: 2 days ago'",
          "Settings / privacy panel"]],
        widths=[CW*0.22, CW*0.50, CW*0.28]
    ))
    story.append(sp(8))

    story.append(section("H3  Adaptive Screen States — Retained from v2"))
    story.append(grid(
        ["State", "Trigger", "UI Behaviour"],
        [["Check-in",  "Baseline / neutral",         "Standard gradient · normal pace · full interface"],
         ["Grounding", "Anxiety / panic detected",   "Muted blue-grey · slow text · breathing animation"],
         ["Wellness",  "Low severity + Satvic opt-in","Nature palette · recipe cards · mindful prompts"],
         ["Crisis",    "Crisis protocol triggered",   "Minimal UI · large text · helplines immediately visible"]],
        widths=[CW*0.15, CW*0.28, CW*0.57]
    ))
    story.append(PageBreak())


    # ══ I — EDGE PRIVACY ════════════════════════════════════════════════════
    story.append(banner("I", "Edge Privacy & Deployment",
                        "On-device ONNX inference · Ephemeral processing · Deployment modes"))
    story.append(sp(10))

    story.append(new_section("I1  ONNX On-Device Inference  [ UPGRADE ]",
                              "Data that never leaves the device cannot be breached"))
    story.append(body(
        "Converting PyTorch models to ONNX format enables the Humorix inference pipeline to run "
        "entirely on the user's device — no facial features, audio patterns, or text ever transmitted "
        "to a cloud server. This is the strongest possible privacy guarantee, and a prerequisite "
        "for NIMHANS clinical validation."))
    story.append(sp(6))
    story.append(new_code([
        "# Convert trained PyTorch model to ONNX (run once after training)",
        "import torch, onnx",
        "",
        "model = load_trained_emotion_model()     # Your PyTorch model",
        "dummy = torch.randn(1, 3, 224, 224)      # Example input shape",
        "",
        "torch.onnx.export(",
        "    model, dummy,",
        "    'models/emotion_model.onnx',",
        "    input_names=['face_frame'],",
        "    output_names=['emotion_probs'],",
        "    dynamic_axes={'face_frame': {0: 'batch'}}",
        ")",
        "",
        "# Runtime inference on device — no network call",
        "import onnxruntime as ort",
        "session = ort.InferenceSession('models/emotion_model.onnx',",
        "          providers=['CPUExecutionProvider'])",
        "result  = session.run(None, {'face_frame': frame_array})",
    ]))
    story.append(sp(8))

    story.append(section("I2  Deployment Modes"))
    story.append(grid(
        ["Mode", "Stack", "Privacy Level", "When to Use"],
        [["Local Dev",    "Python + Streamlit · CPU/GPU",   "High",     "Dev + personal use"],
         ["ONNX Edge",    "ONNX Runtime · on-device",       "Maximum",  "Privacy-first production start"],
         ["GPU Cloud",    "Docker + Triton · AWS/GCP",      "Medium",   "Scale — add consent + encryption"],
         ["Mobile ONNX",  "ONNX + React Native / Flutter",  "Maximum",  "Consumer app — offline capable"],
         ["Clinical API", "FastAPI REST · JWT · TLS",       "High",     "EHR/telehealth integration"]],
        widths=[CW*0.14, CW*0.28, CW*0.16, CW*0.42]
    ))
    story.append(PageBreak())


    # ══ J — EVALUATION METRICS ══════════════════════════════════════════════
    story.append(banner("J", "Evaluation Metrics & KPIs",
                        "Intervention efficacy · System KPIs · Clinical dashboard",
                        color=colors.HexColor("#0A1A2E")))
    story.append(sp(10))
    story.append(note_box(
        "v2 had no success measurement. If you can't measure it, you can't improve it — "
        "and you certainly can't take it to NIMHANS for clinical validation.", "new"))
    story.append(sp(8))

    story.append(new_section("J1  System-Level KPIs  [ NEW ]"))
    story.append(new_grid(
        ["Metric", "Definition", "Target", "Measurement Method"],
        [["Intervention success rate","% of interventions where bio score drops > 20% post-exercise",
          "> 60%", "Efficacy loop (app/core/efficacy.py)"],
         ["Crisis detection accuracy","% of genuine crises correctly identified",
          "> 95%", "Annotated test set + live flag review"],
         ["False positive rate",      "% of non-crisis inputs flagged as crisis",
          "< 3%",  "Annotated test set"],
         ["Session completion rate",  "% of users who complete full DVITE loop",
          "> 70%", "Session tracking"],
         ["Dropout rate",            "% who disengage after < 2 DVITE steps",
          "< 20%", "Funnel analytics"],
         ["Modality reliability",    "% of sessions where face confidence > 0.5",
          "Track only", "Per-session logging"],
         ["Uncertainty mean",        "Average overall_uncertainty score across sessions",
          "< 0.35", "Fusion engine logs"]],
        widths=[CW*0.24, CW*0.30, CW*0.12, CW*0.34]
    ))
    story.append(sp(8))

    story.append(new_section("J2  Clinical Dashboard  [ NEW ]",
                              "For professional review — not user-facing"))
    story.append(new_grid(
        ["Panel", "Data Shown", "Purpose"],
        [["Trend Overview",       "Severity score across sessions (line chart)",
          "Identify improving / stable / deteriorating users"],
         ["Intervention Log",     "Which techniques used · efficacy result per attempt",
          "Which techniques work for this user vs. population"],
         ["Conflict Flags",       "Sessions with high denial_count",
          "Flag users who may need professional outreach"],
         ["Crisis Events",        "All crisis triggers with timestamp and resource shown",
          "Audit trail for clinical compliance"],
         ["Uncertainty Heatmap",  "Which sessions had high overall_uncertainty",
          "Identify hardware or context reliability issues"]],
        widths=[CW*0.20, CW*0.44, CW*0.36]
    ))
    story.append(PageBreak())


    # ══ K — ETHICS & ROADMAP ════════════════════════════════════════════════
    story.append(banner("K", "Ethics, Limitations & v4 Roadmap",
                        "Non-negotiables unchanged · Gaps addressed · Next horizon"))
    story.append(sp(10))

    story.append(section("K1  Ethical Non-Negotiables — Unchanged"))
    story.append(grid(
        ["Principle", "Status"],
        [["No diagnosis — ever",              "Non-negotiable. Cannot be overridden."],
         ["Disclaimer every session",         "Non-negotiable. Cannot be disabled."],
         ["Crisis resources unconditional",   "Non-negotiable. Helplines foregrounded immediately."],
         ["Biometric consent before capture", "Non-negotiable. Modal required."],
         ["Transparency of detection",        "Non-negotiable. System explains what it detected."],
         ["No third-party data sale",         "Non-negotiable."],
         ["Bias audit per release",           "Required. Covers skin tone, age, gender, culture."]],
        widths=[CW*0.44, CW*0.56]
    ))
    story.append(sp(8))

    story.append(section("K2  v3 Gaps — Honest Assessment"))
    story.append(grid(
        ["Gap", "Why It Remains", "v4 Plan"],
        [["Demographic FER accuracy",  "Training data still skewed — takes time",
          "South Asian + East African datasets in collection"],
         ["No published clinical RCT", "Requires partner institution and ethics approval",
          "NIMHANS MOU in progress"],
         ["Intent classifier training","Requires crisis-labelled dataset (sensitive)",
          "Partner with crisis org for annotated data"],
         ["ONNX mobile latency",       "Some models too heavy for older devices",
          "Knowledge distillation to create lightweight variants"],
         ["Indian language NLP",       "Transformer fine-tuning requires data + time",
          "Hindi + Tamil models target for v4"]],
        widths=[CW*0.26, CW*0.38, CW*0.36]
    ))
    story.append(sp(8))

    story.append(new_section("K3  v4.0 Roadmap"))
    story.append(pills(["WEARABLES", "FEDERATED LEARNING", "MULTILINGUAL NLP",
                         "CLINICAL RCT", "LIGHTWEIGHT ONNX", "VOICE CLONING DETECT"]))
    story.append(sp(8))
    story.append(new_grid(
        ["Initiative", "Description", "Priority"],
        [["Wearable Integration",      "HRV, GSR, sleep data as 4th modality",                        "High"],
         ["Federated Learning",        "Per-user model fine-tuning without central data transmission", "High"],
         ["Indian Language NLP",       "Hindi, Tamil, Telugu, Bengali, Marathi",                      "High"],
         ["Clinical RCT",             "NIMHANS-partnered controlled trial",                           "High"],
         ["Lightweight ONNX Models",  "Knowledge distillation for mobile-first deployment",           "Medium"],
         ["Voice Spoofing Detection", "Detect synthetic voice input to prevent system gaming",        "Medium"],
         ["Therapist Handoff API",    "Structured session summary export to licensed practitioner",   "Medium"]],
        widths=[CW*0.26, CW*0.58, CW*0.16]
    ))
    story.append(sp(14))

    story.append(section("Blueprint Version Summary"))
    story.append(sp(6))
    story.append(grid(
        ["Area", "v1 (Research)", "v2 (Developer Blueprint)", "v3 (Hardened)"],
        [["Fusion",    "Fixed concept",       "Static 0.45/0.30/0.25",         "Dynamic + uncertainty score"],
         ["Safety",    "Keyword list",        "Keyword list",                   "Keyword + semantic + pattern"],
         ["Memory",    "None",                "None",                           "Local vector store (ChromaDB)"],
         ["Privacy",   "Policy only",         "Ephemeral processing",           "ONNX on-device + visible UX"],
         ["UI",        "Concept",             "Adaptive states",                "Control mode + privacy indicators"],
         ["Wellness",  "Always-on",           "Severity-gated",                 "Opt-in preference + severity-gated"],
         ["Metrics",   "None",                "None",                           "Full KPI framework + efficacy loop"],
         ["Clinical",  "Disorder modules",    "DVITE + 8 modules",              "DVITE + personalization + efficacy"]],
        widths=[CW*0.14, CW*0.20, CW*0.28, CW*0.38]
    ))
    story.append(sp(12))
    story.append(closing())
    return story


# ── BUILD ──────────────────────────────────────────────────────────────────
# ✅ OUTPUT PATH FIXED — saves to your local Desktop project folder
out = r"C:\Users\Suchitha Kumari\OneDrive\Desktop\AI\Humorix OS\Humorix_AI_Blueprint_v3_Hardened.pdf"

# Make sure the output directory exists (creates it if missing)
os.makedirs(os.path.dirname(out), exist_ok=True)

doc = SimpleDocTemplate(
    out, pagesize=A4,
    topMargin=TM, bottomMargin=BM,
    leftMargin=LM, rightMargin=RM,
    title="Humorix AI — Hardened Blueprint v3.0",
    author="Humorix AI",
    subject="Memory · Resilience · Privacy · Validation · Personalization"
)
doc.build(build(), onFirstPage=on_page, onLaterPages=on_page)
print("Done:", out)