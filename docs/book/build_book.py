#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Builds the printable book, docs/OMNI_COMPASS_MANUAL.pdf, and its one-file text, docs/book/OMNI_COMPASS_BOOK.md.

Three books (the founder's orders of 14 and 20 October): the Operator's Manual (the default), how to embed, wire, tune, run and
check Omni-Compass, with the muscle catalog and the license papers and nothing on how the engine is built; and, with
--owner, the Owner's Manual, the master, docs/OMNI_COMPASS_OWNERS_MANUAL.pdf and docs/book/OMNI_COMPASS_OWNERS_BOOK.md,
with everything: the theory and the declaration in docs/book/, the full manual, the repository's documents, the muscle
catalog and the engine's source; and, with --live, the Live Benchmark Engine Manual (docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.pdf and
docs/book/OMNI_COMPASS_LIVE_ENGINE_BOOK.md), how to read the live benchmark engine page, docs/engine/OMNI_COMPASS_LIVE_ENGINE.html: its
monitors, gauges and knobs, native beside Omni-Compass, and nothing on how the engine is built or wired. Each in the order set
in its outline below. US Letter, mirrored margins for binding,
running heads, roman numerals in the front matter, a contents with page
numbers and PDF bookmarks, and a List of Figures. The figures (the founder's order of 16 October, night: flow charts and
illustrations that interpret the language of the mathematics, then fifty more that interpret the code, the wiring and
the receipts, drawn with another tool) come from two kits, docs/book/figures.py (reportlab) and docs/book/schematics.py
(schemdraw and matplotlib: wiring schematics, block diagrams, flowcharts, timing diagrams, state machines, the receipts
charted from their tables, the grids), each drawn from the book's own code and the repository's own files, placed where a
manual carries a `![caption](book/figures/KEY.svg)` line, numbered and captioned; none of the founder's plates go in, and
no blank pages (the founder's order of 14 October): every chapter starts on the next page.
Type (the founder's prompt rules): body text, tables, lists, code and every label in a figure at 11 pt on a 1.5 line
height, headings scaled up from it; only the running heads and footers are smaller, at 8 pt.

    python3 docs/book/build_book.py            # the Operator's Manual
    python3 docs/book/build_book.py --owner    # the Owner's Manual, the master
    python3 docs/book/build_book.py --live     # the Live Benchmark Engine Manual: how to read the live benchmark engine page
"""
from __future__ import annotations

import json
import csv
import re
import sys
from pathlib import Path

from fontTools.ttLib import TTFont
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont as RLFont
from reportlab.platypus import (BaseDocTemplate, CondPageBreak, Flowable, Frame, KeepTogether, PageBreak, PageTemplate,
                                Paragraph, Spacer, Table, TableStyle, XPreformatted)
from reportlab.platypus.doctemplate import ActionFlowable
from reportlab.platypus.flowables import _listWrapOn
from reportlab.platypus.tableofcontents import SimpleIndex, TableOfContents

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from omni_version import VERSIONS  # noqa: E402  (the engines, newest first: the one list the books read the engine from)
NEWEST = next(iter(VERSIONS))                       # "v8", "v9", ...
ENGINE_JSON = f"OMNI_{NEWEST.upper()}.json"            # the engine that stands, as tools/omni_version.py names it
# the road to it: every engine page from v5 up to the one before the engine that stands, oldest first
ROAD = [f"docs/OMNI_V{n}.md" for n in range(5, int(NEWEST[1:])) if (ROOT / f"docs/OMNI_V{n}.md").exists()]
ROAD_TITLE = ", ".join(Path(p).stem[-2:].lower() for p in ROAD[:-1]) + " and " + Path(ROAD[-1]).stem[-2:].lower()
BOOK = ROOT / "docs" / "book"
# Two manuals (the founder's order of 14 October, night): the Operator's Manual, how to embed, wire, tune, run and check
# Omni-Compass and nothing on how it is built (the default); and the Owner's Manual, the master, with everything: the
# philosophy, the mathematics, the mechanism, the engine's source and every result (--owner). Both stay in the repository
# until the founder takes the Owner's Manual out.
OWNER = "--owner" in sys.argv
LIVE = "--live" in sys.argv          # the third book (the founder's order of 20 October): how to read the live benchmark engine page
MANUAL_REL = ("docs/OMNI_COMPASS_OWNERS_MANUAL.md" if OWNER else "docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md" if LIVE
              else "docs/OMNI_COMPASS_MANUAL.md")
OUT_PDF = ROOT / "docs" / ("OMNI_COMPASS_OWNERS_MANUAL.pdf" if OWNER else "OMNI_COMPASS_LIVE_ENGINE_MANUAL.pdf" if LIVE
                           else "OMNI_COMPASS_MANUAL.pdf")
OUT_MD = BOOK / ("OMNI_COMPASS_OWNERS_BOOK.md" if OWNER else "OMNI_COMPASS_LIVE_ENGINE_BOOK.md" if LIVE else "OMNI_COMPASS_BOOK.md")
EDITION_NAME = "Owner's Manual" if OWNER else "Live Benchmark Engine Manual" if LIVE else "Operator's Manual"
SUBTITLE = ("The Master Manual: Its Philosophy, Its Mathematics, Its Mechanism, Its Results, and How to Wire It onto Your Stack"
            if OWNER else "How to Read the Live Benchmark Engine: Its Monitors, Gauges and Knobs, Native beside Omni-Compass" if LIVE
            else "How to Embed, Wire, Tune and Run Omni-Compass on Your Stack")
SUBTITLE_HTML = ("The Master Manual:<br/>Its Philosophy, Its Mathematics, Its Mechanism, Its Results,<br/>and How to Wire It "
                 "onto Your Stack" if OWNER else "How to Read the Live Benchmark Engine:<br/>Its Monitors, Gauges and Knobs,<br/>Native beside "
                 "Omni-Compass" if LIVE else "How to Embed, Wire, Tune and Run<br/>Omni-Compass on Your Stack")
LICENSE_APPENDIX = "Appendix I" if OWNER else "Appendix F" if LIVE else "Appendix O"
INTRO = ("Introduction: The Idea and the Promise" if OWNER else
         "Introduction: The Page, Its Monitors and What This Manual Covers" if LIVE else
         "Introduction: The Idea and What This Manual Covers")
PROBLEM = "The Problem and the Answer"   # the front matter opens with it (the founder's order of 21 October)
PRELUDE = "Prelude: A Night at the Wall" if LIVE else "Prelude: A Night on the Cluster"
RESULTS_LINE = ("Every result in this book carries its evidence class." if OWNER else
                "This book is the reading manual of the live benchmark engine page and carries no benchmark results of its own; every "
                "published result carries its evidence class." if LIVE else
                "This book is the wiring and operating manual and carries no benchmark results; every published result "
                "carries its evidence class.")
EDITION = "October 2026"
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from tools.legal import TOP, _drop_end, normalize_markdown  # noqa: E402  (the one notice, written once)
from tools.repo import URL as REPO_URL  # noqa: E402  (the repository, written once in tools/repo.py)
BANNER_MD = f"> {TOP}"
FILED = ("All patents, copyrights and trademarks covering the Omni-Compass engine, its "
         "mathematics and its software have been filed in the United States by The Omni-Compass LLC.")

# ---------------------------------------------------------------- fonts
LIB = "/usr/share/fonts/truetype/liberation/"
DJV = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(RLFont("Serif", LIB + "LiberationSerif-Regular.ttf"))
pdfmetrics.registerFont(RLFont("Serif-Bold", LIB + "LiberationSerif-Bold.ttf"))
pdfmetrics.registerFont(RLFont("Serif-Italic", LIB + "LiberationSerif-Italic.ttf"))
pdfmetrics.registerFont(RLFont("Serif-BoldItalic", LIB + "LiberationSerif-BoldItalic.ttf"))
pdfmetrics.registerFont(RLFont("Sans", LIB + "LiberationSans-Regular.ttf"))
pdfmetrics.registerFont(RLFont("Sans-Bold", LIB + "LiberationSans-Bold.ttf"))
pdfmetrics.registerFont(RLFont("Mono", DJV + "DejaVuSansMono.ttf"))
pdfmetrics.registerFont(RLFont("Mono-Bold", DJV + "DejaVuSansMono-Bold.ttf"))
pdfmetrics.registerFont(RLFont("Sym", DJV + "DejaVuSans.ttf"))
pdfmetrics.registerFontFamily("Serif", normal="Serif", bold="Serif-Bold", italic="Serif-Italic", boldItalic="Serif-BoldItalic")
pdfmetrics.registerFontFamily("Sans", normal="Sans", bold="Sans-Bold", italic="Sans", boldItalic="Sans-Bold")
pdfmetrics.registerFontFamily("Mono", normal="Mono", bold="Mono-Bold", italic="Mono", boldItalic="Mono-Bold")
SERIF_CMAP = set(TTFont(LIB + "LiberationSerif-Regular.ttf").getBestCmap())
MONO_CMAP = set(TTFont(DJV + "DejaVuSansMono.ttf").getBestCmap())
SYM_CMAP = set(TTFont(DJV + "DejaVuSans.ttf").getBestCmap())
from docs.book import figures as FIG  # noqa: E402  (the figures, drawn from the code; after the fonts they are set in)
from docs.book import schematics as SCH  # noqa: E402  (the second kit: schematics, flowcharts, timing, receipts, grids)

FIGURES = {**FIG.FIGURES, **SCH.FIGURES}        # every figure of both kits, by key, with the title the list prints


def fig_drawing(key, width):
    """The drawing of a figure from whichever kit holds it."""
    return SCH.drawing(key, width) if key in SCH.FIGURES else FIG.drawing(key, width)

# ---------------------------------------------------------------- page and styles
PW, PH = letter
INNER, OUTER, TOP, BOTTOM = 1.0 * inch, 0.75 * inch, 0.95 * inch, 0.9 * inch
FW, FH = PW - INNER - OUTER, PH - TOP - BOTTOM
NAVY, GOLD, INK, GREY = colors.HexColor("#0b1f3a"), colors.HexColor("#a8801f"), colors.HexColor("#1a1a1a"), colors.HexColor("#666666")
RULE = colors.HexColor("#c9b27a")

PT, LEAD = 11, 16.5                 # the founder's prompt rules: 11 pt or larger for all text, a 1.5 line height
SMALL = 8                           # running heads and footers only
BODY = ParagraphStyle("body", fontName="Serif", fontSize=PT, leading=LEAD, alignment=TA_JUSTIFY, spaceAfter=7, textColor=INK,
                      bulletFontName="Serif", bulletFontSize=PT,        # list bullets and numbers at 11 pt too
                      allowWidows=0, allowOrphans=0)                    # no single line left alone on a page (no dead pages)
CELL = ParagraphStyle("cell", fontName="Serif", fontSize=PT, leading=LEAD, textColor=INK)
CELLH = ParagraphStyle("cellh", parent=CELL, fontName="Sans-Bold", fontSize=PT, textColor=colors.white)
CODE = ParagraphStyle("code", fontName="Mono", fontSize=PT, leading=LEAD, textColor=INK)
SRC = CODE
NOTE = ParagraphStyle("note", parent=BODY, leftIndent=10, rightIndent=10, borderColor=RULE, borderWidth=0.8, borderPadding=7,
                      backColor=colors.HexColor("#faf6ec"), spaceBefore=7, spaceAfter=11)
H1 = ParagraphStyle("h1", fontName="Serif-Bold", fontSize=26, leading=34, textColor=NAVY, spaceAfter=7)
H2 = ParagraphStyle("h2", fontName="Serif-Bold", fontSize=16, leading=22, textColor=NAVY, spaceBefore=13, spaceAfter=7, keepWithNext=1)
H3 = ParagraphStyle("h3", fontName="Serif-BoldItalic", fontSize=13, leading=19, textColor=NAVY, spaceBefore=9, spaceAfter=5, keepWithNext=1)
KICK = ParagraphStyle("kick", fontName="Sans-Bold", fontSize=PT, leading=LEAD, textColor=GOLD, spaceAfter=6)
CAP = ParagraphStyle("cap", fontName="Serif-Italic", fontSize=PT, leading=LEAD, alignment=TA_CENTER, textColor=GREY)
CENTER = ParagraphStyle("center", parent=BODY, alignment=TA_CENTER)
TOC1 = ParagraphStyle("toc1", fontName="Serif-Bold", fontSize=12, leading=18, leftIndent=0, spaceBefore=7, textColor=NAVY)
TOC2 = ParagraphStyle("toc2", fontName="Serif", fontSize=PT, leading=LEAD, leftIndent=18, firstLineIndent=0, rightIndent=40)
TOC3 = ParagraphStyle("toc3", fontName="Serif", fontSize=PT, leading=LEAD, leftIndent=36, textColor=GREY, rightIndent=40)
# the index at the back of the book (a monograph's): every entry at the body size, page numbers on the right
class Index(SimpleIndex):
    """The index with every page reference at the body size: an entry whose page list would run past its line keeps
    the pages that fit, where the term is defined and first used (reportlab would otherwise shrink the page list to fit
    the line, below 11 pt)."""
    MAX_WIDTH = 270.0                        # of the 486 pt line: the rest is the term and the dots
    book = None                              # set by the Book: the index prints the page label the reader sees

    def __call__(self, canv, kind, label):
        """Records an index anchor under the printed page label (roman in the front matter, arabic from the body's
        page 1), not the physical page count from the title page, so every reference lands where it says."""
        from reportlab.platypus.tableofcontents import commasplit, decode_label
        from reportlab.lib.utils import asNative
        label = asNative(label, "latin1")
        try:
            terms, _fmt, _off = decode_label(label)
        except Exception:
            terms = label
        terms = commasplit(terms)
        cPN = canv.getPageNumber()
        pns = self.book.label(cPN) if self.book is not None else str(cPN)
        key = "ix_%s_%s_p_%s" % (self.name, label, pns)
        info = canv._curr_tx_info
        canv.bookmarkHorizontal(key, info["cur_x"], info["cur_y"] + info["leading"])
        self.addEntry(terms, (cPN, pns), key)

    def _getlastEntries(self, dummy=None):
        entries = super()._getlastEntries() if dummy is None else super()._getlastEntries(dummy)
        out = []
        for texts, pages in entries:
            keep, width = [], 0.0
            for p in sorted(pages, key=lambda p: (p[0][0] if isinstance(p[0], tuple) else p[0], str(p))):
                shown = p[0][1] if isinstance(p[0], tuple) else p[0]
                width += pdfmetrics.stringWidth(f"{shown}, ", "Serif", PT)
                if keep and width > self.MAX_WIDTH:
                    break
                keep.append(p)
            out.append((texts, keep))
        return out


INDEX = Index(style=ParagraphStyle("ix", fontName="Serif", fontSize=PT, leading=LEAD), dot=" . ", headers=True)
# a figure's caption under its drawing ("Figure N." in bold), and the List of Figures after the Contents, both at the body size
FIGCAP = ParagraphStyle("figcap", parent=BODY, alignment=TA_LEFT, spaceBefore=5, spaceAfter=12)
FIGNOTE = ParagraphStyle("fignote", parent=BODY, spaceBefore=0)      # a long caption's rules, as text under the figure
LOF = ParagraphStyle("lof", fontName="Serif", fontSize=PT, leading=LEAD, leftIndent=0, rightIndent=40)   # room for the page number: never shrunk
CODE_WIDTH = 70                     # characters of 11 pt mono that fit the frame inside a code block's padding

# ---------------------------------------------------------------- text cleaning
AI_WORDS = re.compile(r"\b(grok|chatgpt|claude|gemini|anthropic|openai|xai|copilot|same assistant|other AI builds?)\b", re.I)
BANNER = re.compile(r"^>\s*(\*\*PROPRIETARY|©\s*2026 The Omni-Compass LLC|\*\*Evaluation and Simulation use only)")


def clean_lines(text: str) -> list[str]:
    """Strips the license banners, branch names and any line that speaks about the tools used to write the code."""
    text = re.sub(r"\bclaude/[\w.-]+", "main", text)
    out, lines, i = [], text.splitlines(), 0
    skip_level = None
    while i < len(lines):
        ln = lines[i]
        m = re.match(r"^(#{1,6}) ", ln)
        if m:
            lvl = len(m.group(1))
            if skip_level is not None and lvl <= skip_level:
                skip_level = None
            if skip_level is None and AI_WORDS.search(ln):
                skip_level = lvl
        if skip_level is not None:
            i += 1; continue
        if BANNER.match(ln):
            i += 1
            while i < len(lines) and lines[i].startswith(">"):
                i += 1
            continue
        if AI_WORDS.search(ln):
            ind = len(ln) - len(ln.lstrip())
            i += 1
            if re.match(r"^\s*(-|\d+\.) ", ln):            # a list item: its indented children go with it
                while i < len(lines) and lines[i].strip() and len(lines[i]) - len(lines[i].lstrip()) > ind:
                    i += 1
            continue
        out.append(ln); i += 1
    return _drop_end(out)[0]


def glyphs(t: str, cmap: set) -> str:
    return "".join(c if ord(c) < 128 or ord(c) in cmap or ord(c) not in SYM_CMAP else f'<font name="Sym">{c}</font>' for c in t)


TEX_SYM = {"sum": "\u2211", "int": "\u222b", "approx": "\u2248", "le": "\u2264", "leq": "\u2264", "ge": "\u2265",
           "geq": "\u2265", "times": "\u00d7", "cdot": "\u00b7", "Delta": "\u0394", "propto": "\u221d", "dots": "\u2026",
           "ldots": "\u2026", "infty": "\u221e", "lceil": "\u2308", "rceil": "\u2309", "max": "max", "min": "min",
           "qquad": "\u2003\u2003", "quad": "\u2003", ",": "\u2009", ";": " ", ":": " ", " ": " ", "!": "", "$": "$",
           "lambda": "\u03bb", "rho": "\u03c1", "sigma": "\u03c3", "mu": "\u03bc", "tau": "\u03c4", "alpha": "\u03b1"}
TEX_DROP = ("left", "right", "big", "Big", "bigg", "Bigg", "bigl", "bigr", "Bigl", "Bigr")


def tex(src: str) -> str:
    """A formula written in LaTeX in the markdown ($...$), set as text for the printed book: symbols as their glyphs,
    subscripts and superscripts as such, fractions as a/b. The markdown keeps the LaTeX."""
    s = src.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
    i, out = 0, []

    def group(j):                      # the {...} at j (or one character), and the index after it
        while j < len(s) and s[j] == " ":
            j += 1
        if j < len(s) and s[j] == "{":
            depth, k = 0, j
            while k < len(s):
                depth += {"{": 1, "}": -1}.get(s[k], 0)
                if depth == 0:
                    return s[j + 1:k], k + 1
                k += 1
            return s[j + 1:], len(s)
        if j < len(s) and s[j] == "\\" and re.match(r"\\([A-Za-z]+|.)", s[j:]):
            m = re.match(r"\\([A-Za-z]+|.)", s[j:])
            return s[j:j + len(m.group(0))], j + len(m.group(0))
        return s[j:j + 1], j + 1
    while i < len(s):
        c = s[i]
        if c == "\\":
            m = re.match(r"\\([A-Za-z]+|.)", s[i:])
            if m is None:
                i += 1; continue
            name = m.group(1); i += len(m.group(0))
            if name in TEX_DROP:
                continue
            if name in ("text", "mathrm", "mathbf", "mathit", "operatorname"):
                g, i = group(i); out.append(tex(g) if name != "text" else esc_txt(g)); continue
            if name == "frac":
                a, i = group(i); b, i = group(i)
                a, b = tex(a), tex(b)
                wrap = lambda x: f"({x})" if re.search(r"[ +\u2212=\u2009\u2003]", re.sub(r"<[^>]+>", "", x)) else x
                out.append(f"{wrap(a)}/{wrap(b)}"); continue
            if name == "sqrt":
                a, i = group(i); out.append("\u221a" + (tex(a) if len(a) == 1 else f"({tex(a)})")); continue
            out.append(TEX_SYM.get(name, name)); continue
        if c in "_^":
            g, i = group(i + 1)
            tag = "sub" if c == "_" else "super"           # at the body's own size: no text under 11 pt
            out.append(f'<{tag} size="{PT}" rise="{2 if c == "_" else 3}">{tex(g)}</{tag}>'); continue
        if c in "{}":
            i += 1; continue
        if c == "'":
            out.append("\u2032"); i += 1; continue
        if c == "-":
            out.append("\u2212"); i += 1; continue
        out.append(esc_txt(c)); i += 1
    return glyphs("".join(out), SERIF_CMAP)


def esc_txt(x: str) -> str:
    return x.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


MATH = re.compile(r"\$\$(.+?)\$\$|(?<![\\\w$])\$(?=\S)((?:\\\$|[^$\n])+?)(?<=\S)(?<!\\)\$(?![\w$])")


def inline(t: str) -> str:
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    codes = []

    def keep(m):
        codes.append(m.group(1)); return f"\x00{len(codes) - 1}\x00"
    t = re.sub(r"`([^`]+)`", keep, t)
    maths = []

    def keep_math(m):
        maths.append(tex(m.group(1) if m.group(1) is not None else m.group(2))); return f"\x01{len(maths) - 1}\x01"
    t = MATH.sub(keep_math, t)
    t = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", t)
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"<i>\1</i>", t)
    t = re.sub(r"(?<![\w_])_(?![\s_])([^_]+?)(?<![\s_])_(?![\w_])", r"<i>\1</i>", t)
    t = glyphs(t, SERIF_CMAP)
    t = re.sub(r"\x01(\d+)\x01", lambda m: maths[int(m.group(1))], t)
    return re.sub(r"\x00(\d+)\x00", lambda m: f'<font name="Mono" size="{PT}">' + glyphs(codes[int(m.group(1))], MONO_CMAP) + "</font>", t)


# ---------------------------------------------------------------- the index
# What is indexed: every glossary term where it is defined or discussed (in bold, or in a heading), every muscle family
# where it is named the same way, every repository file named in a code span, and every setting (--flag). A plain mention
# of a common word is not an entry: the index points to where a thing is explained, as a monograph's does.
_INDEX_TERM_RES = None
PATH_RE = re.compile(r"`((?:tools|scripts|docs|deploy|omnicompass|omni_controller|realms|tests|results|pilot|benchmarks|cpp|"
                     r"k8s_fleet|k8s_controlplane|fleet|hardware|tuning|\.github/workflows)/[\w./*-]+?)`")
FLAG_RE = re.compile(r"`(--[a-z][\w-]*)")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")


def index_term_res():
    """(term, its whole-word regex) for every glossary term and every muscle family, compiled once."""
    global _INDEX_TERM_RES
    if _INDEX_TERM_RES is None:
        terms = []
        for ln in MAN.get("Glossary", []):
            if ln.startswith("|") and not ln.startswith("| Term") and not re.match(r"^\|\s*-", ln):
                cell = re.sub(r"[`*]", "", ln.strip().strip("|").split("|")[0]).strip()
                if len(cell) >= 3:
                    terms.append(cell)
        with (ROOT / "realms" / "catalog_v5.csv").open() as f:
            terms += sorted({r["family"] for r in csv.DictReader(f)})
        seen, out = set(), []
        for t in terms:
            if t.lower() in seen:
                continue
            seen.add(t.lower())
            out.append((t, re.compile(r"(?<![\w-])" + re.escape(t) + r"(?![\w-])", re.I)))
        _INDEX_TERM_RES = out
    return _INDEX_TERM_RES


def index_items(text, kind="body"):
    """What a paragraph indexes, by what it names: files and settings always; glossary terms and families where the
    paragraph defines or discusses them (bold) or is a heading about them."""
    items = set()
    for m in PATH_RE.finditer(text):
        p = m.group(1).rstrip(".,;:")
        if "/" in p and not p.endswith("/"):
            items.add(p)
    for m in FLAG_RE.finditer(text):
        items.add(m.group(1))
    if kind in ("body", "heading", "note", "list"):
        hay = text if kind == "heading" else " ".join(BOLD_RE.findall(text))
        if hay:
            for term, rx in index_term_res():
                if rx.search(hay):
                    items.add(term)
    return sorted(items)


def index_tag(item):
    return '<index item="%s"/>' % item.replace(",", ";").replace("&", "&amp;").replace('"', "&quot;")


def index_tags(text, kind="body"):
    """The <index/> tags of a heading, at its start (a heading is never split over two pages)."""
    return "".join(index_tag(i) for i in index_items(text, kind))


def tagged(text, kind="body"):
    """A paragraph's markup with each <index/> tag placed at the term it names, so that a paragraph split over two
    pages indexes a term on the page where the term is printed, never where the paragraph began; a term the markup
    does not show (a family named by its muscles) is tagged at the start."""
    markup = inline(text)
    items = index_items(text, kind)
    if not items:
        return markup
    head, plan = [], []
    for item in items:
        rx = re.compile(r"(?<![\w-])" + re.escape(item) + r"(?![\w-])", re.I)
        pos = None
        for m in rx.finditer(markup):
            if markup.rfind("<", 0, m.start()) <= markup.rfind(">", 0, m.start()):   # outside any tag
                pos = m.end(); break
        (plan if pos is not None else head).append((pos, index_tag(item)))
    for pos, tag in sorted(plan, reverse=True):
        # right after the term, never before it: a zero-width mark before a term that is carried to the next line
        # stays on the line before (and on the page before at a page's foot); after the term it follows the term
        # wherever it lands, and it widens nothing (measured: the words sit where they sit without it)
        markup = markup[:pos] + tag + markup[pos:]
    return "".join(tag for _, tag in head) + markup


# ---------------------------------------------------------------- flowables
class Marker(Flowable):
    """Zero-size flowable that tells the document something when it is drawn (a chapter starts, the body starts)."""

    def __init__(self, kind, **kw):
        super().__init__(); self.kind, self.kw = kind, kw

    def wrap(self, *a):
        return 0, 0

    def draw(self):
        pass


class Heading(Paragraph):
    def __init__(self, text, style, level, toc_text=None, kind="section"):
        super().__init__(text, style)
        self.level, self.toc_text, self.kind = level, toc_text or re.sub(r"<[^>]+>", "", text), kind


FIG_NO = [0]
IMAGE_LINE = re.compile(r"^!\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\(([^()\s]+)\)\s*$")   # a caption may carry I[U] or K[P]
FIGURE_PATH = re.compile(r"^(?:docs/)?book/figures/([a-z0-9_]+)\.svg$")


class FloatFigure(KeepTogether):
    """A figure with its caption, kept together, that floats: where it does not fit under the text that names it, the
    text goes on down the page and the figure opens the next page (no dead space under a paragraph)."""


class KeepWithStart(KeepTogether):
    """A heading kept with what follows it. Where the whole of what follows (a table, a listing, a long paragraph) would
    not fit under the heading, the heading still stays on the page with the start of it, and the rest splits onto the
    next page; only when not even the heading and three lines fit does the whole move (no page ends on a heading, and no
    page is left half empty because a table was carried over whole)."""
    MIN = 3 * LEAD

    def split(self, aW, aH):
        if getattr(self, "_wrapInfo", None) != (aW, aH):
            self.wrap(aW, aH)
        content = self._content
        if self._H > aH and len(content) > 1:
            _, hH = _listWrapOn(content[:-1], aW, self.canv)
            room = aH - hH
            if room >= self.MIN:
                try:
                    pieces = content[-1].splitOn(self.canv, aW, room)
                except Exception:
                    pieces = []
                if pieces and not isinstance(pieces[0], ActionFlowable):
                    return content[:]                         # the heading, then the rest, which fits or splits on its own
        return super().split(aW, aH)


class ChapterBreak(Flowable):
    """The page break before a chapter. The chapter starts on the next page unless that would leave the page it ends
    less than FILL full; then it opens on the same page, under a rule (the founder's order of 16 October, night: no
    dead pages, every page at least four fifths used)."""
    def wrap(self, aw, ah):
        return 0, 0

    def draw(self):
        pass


class FlushFloats(Flowable):
    """Every figure still floating is placed here, before the matter that follows it."""
    def wrap(self, aw, ah):
        return 0, 0

    def draw(self):
        pass


class OpenerSpace(Flowable):
    """The air above a chapter's title: its full height at the top of a page, a line's worth when the chapter opens
    lower on a page that was not yet four fifths full."""
    def __init__(self, height, mid=6):
        super().__init__()
        self.height, self.mid = height, mid

    def wrap(self, aw, ah):
        return 0, 0

    def draw(self):
        pass


FILL = 0.8
FLOAT_SLACK = 24.0                        # a figure is placed only with this much room to spare under it (its caption never
                                          # parts from its drawing over a point of rounding)


def figure(key, caption):
    """A drawn figure with its numbered caption, kept on one page; a marker tells the document to list it."""
    FIG_NO[0] += 1
    n = FIG_NO[0]
    head, rest = split_caption(caption)
    cap = Paragraph(f"<b>Figure {n}.</b> " + inline(head), FIGCAP)
    pieces = [Spacer(1, 8), Marker("figure", number=n, title=FIGURES[key]), fig_drawing(key, FW), cap]
    for piece in pieces:
        piece._figpiece = True                # no other figure is ever slipped between a figure's drawing and its caption
    out = [FloatFigure(pieces)]
    if rest:                                  # the caption's rules, as text under the figure wherever it lands
        tail = Paragraph(inline(rest), FIGNOTE)
        tail._figpiece = tail._figtail = True
        out.append(tail)
    return out


def split_caption(caption, keep=320):
    """A caption longer than a few lines is cut at a sentence end: the first sentences stay under the drawing, the rest
    follows as text, so a drawing and its caption always fit one page together."""
    if len(caption) <= 2 * keep:
        return caption, ""
    k = caption.find(". ", keep)
    if k < 0 or k > len(caption) - 80:
        return caption, ""
    return caption[:k + 1], caption[k + 2:]


class GoldRule(Flowable):
    def __init__(self, width=FW, thick=1.2, space=10):
        super().__init__(); self.width, self.thick, self.space = width, thick, space

    def wrap(self, *a):
        return self.width, self.space

    def draw(self):
        self.canv.setStrokeColor(GOLD); self.canv.setLineWidth(self.thick)
        self.canv.line(0, self.space / 2, self.width, self.space / 2)


class BookTable(Table):
    """A table that ends a page at a row's end, unless a tall row would leave more than a few lines of the page empty: that
    row is then split inside it. Split at the row's end, the rest started lower on the same page under its header again
    (21 October: the header printed twice on one page, the problem and the solution's table, rows of eight lines)."""
    GAP = 4 * LEAD

    def split(self, availWidth, availHeight):
        parts = super().split(availWidth, availHeight)
        if len(parts) == 2 and self.splitInRow and availHeight - parts[0].wrap(availWidth, availHeight)[1] > self.GAP:
            inrow = self._splitRows(availHeight, doInRowSplit=True)
            if len(inrow) == 2:
                return inrow
        return parts


def table(rows_txt, small=False):
    n = max(len(r) for r in rows_txt)
    rows_txt = [r + [""] * (n - len(r)) for r in rows_txt]
    cs, hs = CELL, CELLH                     # 11 pt in every table, however many columns
    lens = [max(min(len(re.sub(r"[`*]", "", r[j])), 60) for r in rows_txt) for j in range(n)]
    weights = [max(4.0, x) ** 0.85 for x in lens]
    tot = sum(weights)
    widths = [FW * w / tot for w in weights]
    floor = min(30.0, FW / n)
    for _ in range(5):
        short = [k for k, w in enumerate(widths) if w < floor]
        if not short:
            break
        extra = sum(floor - widths[k] for k in short)
        big = sum(w for k, w in enumerate(widths) if k not in short)
        widths = [floor if k in short else w - extra * w / big for k, w in enumerate(widths)]
    data = [[Paragraph(tagged(c, "cell"), hs if k == 0 else cs) for c in r] for k, r in enumerate(rows_txt)]
    t = BookTable(data, colWidths=widths, repeatRows=1, hAlign="LEFT", splitInRow=1)   # a row taller than a page breaks across it
    t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#b8b8b8")),
                           ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                           ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f4f1ea")]),
                           ("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("TOPPADDING", (0, 0), (-1, -1), 2.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
                           ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4)]))
    return t


def wrap_code(lines, width):
    out = []
    for ln in lines:
        ln = ln.replace("\t", "    ")
        while len(ln) > width:
            out.append(ln[:width]); ln = "    ↪ " + ln[width:]
        out.append(ln)
    return out


def code_block(lines, style=CODE, width=CODE_WIDTH):
    """A shaded code block, cut into page-sized pieces so that long listings flow across pages."""
    lines = wrap_code(lines, width)
    per = 6                             # small pieces, so that a listing fills each page to its foot (no dead space)
    parts = []
    for k in range(0, max(1, len(lines)), per):
        txt = "\n".join(lines[k:k + per])
        txt = glyphs(txt.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"), MONO_CMAP)
        t = Table([[XPreformatted(txt, style)]], colWidths=[FW])    # XPreformatted reads the entities and the font tags
        t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f3f3f1")),
                               ("LINEBEFORE", (0, 0), (0, -1), 2, RULE),
                               ("LEFTPADDING", (0, 0), (-1, -1), 8), ("TOPPADDING", (0, 0), (-1, -1), 4),
                               ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
        parts.append(t)
    return parts


# ---------------------------------------------------------------- markdown to flowables
def md_flow(lines, shift=0, story=None, strip=False):
    """A markdown subset to flowables. Heading level n becomes n - shift (level 1 is reserved for chapters)."""
    story = [] if story is None else story
    i = 0
    while i < len(lines):
        ln = lines[i]
        if re.fullmatch(r"\s*<!--.*-->\s*", ln):            # a page marker for the tools, never printed
            i += 1; continue
        if ln.startswith("```"):
            j = i + 1; buf = []
            while j < len(lines) and not lines[j].startswith("```"):
                buf.append(lines[j]); j += 1
            story += code_block(buf); story.append(Spacer(1, 6)); i = j + 1; continue
        if ln.startswith("    ") and ln.strip() and not re.match(r"^\s*(-|\d+\.) ", ln):
            buf = []
            while i < len(lines) and (lines[i].startswith("    ") or not lines[i].strip()):
                buf.append(lines[i][4:]); i += 1
            while buf and not buf[-1].strip():
                buf.pop()
            story += code_block(buf); story.append(Spacer(1, 6)); continue
        m = IMAGE_LINE.match(ln)
        if m:                                               # a figure drawn from the code is in the book; a plate is not
            fig = FIGURE_PATH.match(m.group(2))
            if fig and fig.group(1) in FIGURES:
                last = next((x for x in reversed(story) if not isinstance(x, Spacer)), None)
                if isinstance(last, Paragraph) and not isinstance(last, Heading) and not getattr(last, "_figpiece", False):
                    last._anchor = True       # the paragraph that names the figure: it never runs pages ahead of it
                story += figure(fig.group(1), m.group(1))
            i += 1; continue
        if ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in re.split(r"(?<!\\)\|", lines[i].strip().strip("|"))]
                if not all(re.fullmatch(r":?-+:?", c) for c in cells if c):
                    rows.append(cells)
                i += 1
            if rows:
                story += [table(rows), Spacer(1, 8)]
            continue
        m = re.match(r"^(#{1,6}) (.*)", ln)
        if m:
            lvl = max(2, min(3, len(m.group(1)) - shift + 1))
            txt = m.group(2).strip()
            if strip:                                   # the manual's own numbers give way to the book's
                txt = re.sub(r"^(\d+(\.\d+)*\.?|[A-Z]\.)\s+(?=[A-Z])", "", txt)
            story.append(Heading(index_tags(txt, "heading") + inline(txt), H2 if lvl == 2 else H3, lvl)); i += 1; continue
        if ln.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i].lstrip(">").strip()); i += 1
            story.append(Paragraph(tagged(" ".join(buf), "note"), NOTE)); continue
        if re.fullmatch(r"\s*(-{3,}|\*{3,}|_{3,})\s*", ln):
            story.append(Spacer(1, 6)); i += 1; continue
        mm = re.match(r"^(\s*)(-|\*|\d+\.) (.*)", ln)
        if mm:
            buf = [mm.group(3)]; i += 1
            while i < len(lines) and lines[i].strip() and not re.match(r"^\s*(-|\*|\d+\.) ", lines[i]) \
                    and not re.match(r"^(#|\||```|>)", lines[i]) and lines[i].startswith(" "):
                buf.append(lines[i].strip()); i += 1
            ind = 14 + 12 * (len(mm.group(1)) // 2)
            bullet = "•" if mm.group(2) in "-*" else mm.group(2)
            story.append(Paragraph(tagged(" ".join(buf), "list"), ParagraphStyle("li", parent=BODY, leftIndent=ind + 6, bulletIndent=ind - 8,
                                   spaceAfter=3, alignment=TA_LEFT), bulletText=bullet))
            continue
        if not ln.strip():
            i += 1; continue
        buf = [ln]; i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||```|>|!\[|<!--|\s*(-|\*|\d+\.) |-{3,})", lines[i]) \
                and not lines[i].startswith("    "):
            buf.append(lines[i]); i += 1
        text = " ".join(x.strip() for x in buf)
        story.append(Paragraph(tagged(text, "body"), BODY))
    return story


# ---------------------------------------------------------------- sources
def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def split_h1(text):
    """{title: lines} for a file with several level-1 chapters."""
    parts, cur = {}, None
    for ln in clean_lines(text):
        m = re.match(r"^# (.*)", ln)
        if m:
            cur = m.group(1).strip(); parts[cur] = []
        elif cur:
            parts[cur].append(ln)
    return parts


def manual_sections():
    """The manual, cut at its level-2 headings: {short title: lines}."""
    secs, cur, fence = {}, None, False
    for ln in clean_lines(read(MANUAL_REL)):
        if ln.lstrip().startswith("```"):
            fence = not fence                    # a line inside a code block is never a heading ("# a comment")
        m = None if fence or ln.lstrip().startswith("```") else re.match(r"^## (.*)", ln)
        if fence or ln.lstrip().startswith("```"):
            if cur:
                secs[cur].append(ln)
            continue
        if m:
            cur = re.sub(r"^\d+\.\s*", "", m.group(1).strip()); secs[cur] = []
        elif re.match(r"^# ", ln):
            cur = None
        elif cur:
            secs[cur].append(ln)
    return secs


def doc_body(rel):
    """A repository document: (its own title, its lines without the title)."""
    lines = clean_lines(read(rel))
    title = None
    for k, ln in enumerate(lines):
        if ln.startswith("# "):
            title = ln[2:].strip(); lines = lines[:k] + lines[k + 1:]; break
    return title, lines


MAN = manual_sections()
THEORY = split_h1((BOOK / "THEORY.md").read_text()) if OWNER else {}
DECL = split_h1((BOOK / "DECLARATION.md").read_text()) if OWNER else {}

# Each chapter: (title, source). Source: ("T", key) theory; ("D", key) declaration; ("M", key) manual section; ("F", path)
# a repository document; ("FS", [paths]) several documents in one chapter; ("X", name) generated here. The Operator's
# Manual binds nothing on how the engine is built and no benchmark results; the Owner's Manual binds everything.
OPERATOR_OUTLINE = [
    ("PART", "The Governor, from the Outside",
     "What Omni-Compass is as an installer meets it, how the muscles of a stack become one body, and how it is tuned."),
    ("What Omni-Compass Is", ("M", "What Omni-Compass Is")),
    ("Your Stack as One Body: Muscles and Organisms", ("M", "Your Stack as One Body: Muscles and Organisms")),
    ("The Spine: the Base Every Stack Runs On", ("F", "docs/THE_SPINE.md")),
    ("Tuning: The Factory Tune, the Dial and the Settings You Write",
     ("M", "Tuning: The Factory Tune, the Dial and the Settings You Write")),
    ("PART", "The Harness: Plugs, Wires and the Rules They Obey",
     "The universal plug, the adapters, the wire check that must pass before anything writes, and the rules every wire "
     "obeys."),
    ("The Plug, the Adapters and the Wire Check", ("M", "The Plug, the Adapters and the Wire Check")),
    ("The Rules the Wires Obey", ("M", "The Rules the Wires Obey")),
    ("PART", "Wiring It onto Your Stack, Step by Step",
     "The eight levels, from watching to governing the site, and the wiring of each kind of stack."),
    ("Before You Start, and the Eight Levels", ("M", "Before You Start, and the Eight Levels")),
    ("Stack by Stack", ("M", "Stack by Stack")),
    ("PART", "Operating It",
     "The OFF switch, the rules the governor obeys, the log it keeps, and the care of a running installation."),
    ("The OFF Switch, the Rules, and the Log", ("M", "The OFF Switch, the Rules, and the Log")),
    ("Maintenance, Upgrades and Security", ("M", "Maintenance, Upgrades and Security")),
    ("PART", "Checking It on Your Own System",
     "Paired runs and receipts on your own system, evidence classes, the engine version and the three-run rule."),
    ("Paired Runs and Receipts on Your Own System", ("M", "Paired Runs and Receipts on Your Own System")),
    ("Evidence Classes and How to Read a Receipt", ("M", "Evidence Classes and How to Read a Receipt")),
    ("The Engine Version and the Three-Run Rule", ("M", "The Engine Version and the Three-Run Rule")),
    ("PART", "The Implementer's Guide: Omni-Compass on a Cloud",
     "For the engineer who installs it on Azure, Google Cloud or Amazon Web Services and keeps it in service: the path and "
     "its gates, the permissions, each cloud step by step, the response-time feed, the cloud itself, day two, the graphics "
     "processor, observability, change and risk, planning a cloud run, own racks and private clouds, hardening, a fleet, "
     "the failure drills, a complete installation, and the questions implementers ask."),
    ("The Implementer's Path: From an Empty Account to a Governed Cluster",
     ("M", "The Implementer's Path: From an Empty Account to a Governed Cluster")),
    ("Identity, Permissions and Least Privilege on a Managed Cluster",
     ("M", "Identity, Permissions and Least Privilege on a Managed Cluster")),
    ("Azure Kubernetes Service, Step by Step", ("M", "Azure Kubernetes Service, Step by Step")),
    ("Google Kubernetes Engine, Step by Step", ("M", "Google Kubernetes Engine, Step by Step")),
    ("Amazon Elastic Kubernetes Service, Step by Step", ("M", "Amazon Elastic Kubernetes Service, Step by Step")),
    ("The Response-Time Feed and the Line", ("M", "The Response-Time Feed and the Line")),
    ("Running in the Cloud: the Whole Engine, the Bill and the Alarm Minutes",
     ("M", "Running in the Cloud: the Whole Engine, the Bill and the Alarm Minutes")),
    ("Day Two: Running Omni-Compass in Production", ("M", "Day Two: Running Omni-Compass in Production")),
    ("The Graphics Processor: Putting the Governor on a Card", ("M", "The Graphics Processor: Putting the Governor on a Card")),
    ("Observability: Feeding the Governor from Your Monitoring, and Watching It",
     ("M", "Observability: Feeding the Governor from Your Monitoring, and Watching It")),
    ("Change Management, Risk and Compliance", ("M", "Change Management, Risk and Compliance")),
    ("Planning a Cloud Run: Capacity, Cost and the Shape of Load",
     ("M", "Planning a Cloud Run: Capacity, Cost and the Shape of Load")),
    ("On Your Own Racks and in Private Clouds",
     ("M", "On Your Own Racks and in Private Clouds")),
    ("Hardening and the Supply Chain",
     ("M", "Hardening and the Supply Chain")),
    ("Rolling Out Across a Fleet: Many Clusters, Many Services, GitOps",
     ("M", "Rolling Out Across a Fleet: Many Clusters, Many Services, GitOps")),
    ("Failure Modes and the Drill Book",
     ("M", "Failure Modes and the Drill Book")),
    ("A Complete Installation, Start to Finish",
     ("M", "A Complete Installation, Start to Finish")),
    ("Questions an Implementer Asks", ("M", "Questions an Implementer Asks")),
    ("PART", "License and Your Copy",
     "The terms the software and this manual are licensed under, and how to verify a copy before it is installed."),
    ("License and Commercial Terms", ("M", "License and Commercial Terms")),
    ("Verifying Your Copy", ("M", "Verifying Your Copy")),
    ("BACK", None),
    ("Glossary", ("M", "Glossary")),
    ("Appendix A. Command Reference", ("M", "Appendix A - Command Reference")),
    ("Appendix B. The Files an Installation Touches", ("M", "Appendix B - The Files an Installation Touches")),
    ("Appendix C. The Gauges", ("M", "Appendix C - The Gauges")),
    ("Appendix D. Troubleshooting", ("M", "Appendix D - Troubleshooting")),
    ("Appendix E. The Muscles: What Each Is For, and How It Is Wired", ("F", "docs/MUSCLE_CATALOG.md")),
    ("Appendix F. The Azure Account, Click by Click", ("F", "docs/AZURE_SETUP.md")),
    ("Appendix G. The Google Cloud Account, Click by Click", ("F", "docs/GOOGLE_SETUP.md")),
    ("Appendix H. The Amazon Web Services Account, Click by Click", ("F", "docs/AMAZON_SETUP.md")),
    ("Appendix I. The Install Manifests", ("X", "manifests")),
    ("Appendix J. The Implementer's Checklists", ("M", "Appendix J - The Implementer's Checklists")),
    ("Appendix K. The Kubernetes Governor's Settings", ("M", "Appendix K - The Kubernetes Governor's Settings")),
    ("Appendix L. The Audit, Record by Record", ("M", "Appendix L - The Audit, Record by Record")),
    ("Appendix M. The Three Clouds Side by Side", ("M", "Appendix M - The Three Clouds Side by Side")),
    ("Appendix N. The Paired Run from GitHub: Every Input", ("M", "Appendix N - The Paired Run from GitHub: Every Input")),
    ("Appendix O. The License", ("X", "license")),
    ("Appendix P. Licensing: Questions and Answers", ("F", "LICENSING_FAQ.md")),
    ("Appendix Q. Third-Party Notices", ("F", "THIRD_PARTY_NOTICES.md")),
    ("Appendix R. The Enterprise License: Standard Terms", ("F", "ENTERPRISE_LICENSE.md")),
    ("Appendix S. Patents and Trademarks", ("FS", ["PATENTS.md", "TRADEMARKS.md"])),
    ("Appendix T. Security Policy", ("F", "SECURITY.md")),
    ("Index", ("X", "index")),
    ("Contact", ("X", "contact")),
]

OWNER_OUTLINE = [
    ("PART", "The Philosophy and the Theory",
     "Where Omni-Compass comes from: the closed circle, the four pieces, the compass, the basins and the reflex. The "
     "engineering in the rest of the book is this idea made exact."),
    ("What Omni-Compass Is", ("M", "What Omni-Compass Is")),
    ("The Referee's Summary: Each Claim, Its Evidence, and What Is Undetermined", ("F", "docs/REFEREE_SUMMARY.md")),
    ("The Referee's Grades, Category by Category, and the Plan to Raise Each", ("F", "docs/REFEREE_GRADES.md")),
    ("Related Work: Where the Idea Comes From, and What It Adds", ("F", "docs/RELATED_WORK.md")),
    ("The Seat: One Governor over the Muscles", ("F", "docs/THE_SEAT.md")),
    ("The Unified Circle Principle", ("T", "The Unified Circle Principle")),
    ("The Four-Piece Engine", ("T", "The Four-Piece Engine")),
    ("The Compass", ("T", "The Compass")),
    ("Basins, Polarity and the Dual-Basin Engine", ("T", "Basins, Polarity and the Dual-Basin Engine")),
    ("The Reflex Rule: One Body, One Brain", ("T", "The Reflex Rule: One Body, One Brain")),
    ("PART", "The Mathematics",
     "Eight equations, one control law, and the proofs, audits and declarations that hold them fixed."),
    ("The Canonical Declaration", ("D", "The Canonical Declaration")),
    ("The Engine: Eight Equations and One Control Law", ("M", "The Engine: Eight Equations and One Control Law")),
    ("The Canonical Engine", ("F", "docs/CANONICAL_ENGINE.md")),
    ("The Closed Circle: Why It Cannot Leave Its Compass", ("M", "The Closed Circle: Why It Cannot Leave Its Compass")),
    ("Closing the Circle in the Engine", ("T", "Closing the Circle in the Engine")),
    ("The Tracking Theorem", ("F", "docs/TRACKING_THEOREM.md")),
    ("The Engine's Machine-Checked Proofs", ("F", "docs/ENGINE_PROOFS.md")),
    ("The Conveyance Law", ("F", "docs/CONVEYANCE_LAW.md")),
    ("Formal Status of the Mathematics", ("F", "docs/FORMAL_STATUS.md")),
    ("The Max, Formally: Definitions, Guarantees and Measures", ("F", "docs/FORMAL_V5.md")),
    ("The Mechanism of Action", ("F", "docs/MECHANISM_OF_ACTION.md")),
    ("The Safety Case: Every Hazard, Its Guard, and the Evidence", ("F", "docs/SAFETY_CASE.md")),
    ("The Threat Model: Misuse, Its Guards, and What Is Open", ("F", "docs/THREAT_MODEL.md")),
    ("The Static Security Scan, Every Finding Reviewed", ("F", "docs/SECURITY_SCAN.md")),
    ("Every Dependency and Its License", ("F", "docs/DEPENDENCY_LICENSES.md")),
    (f"The Engine That Stands: Omni {NEWEST}", ("F", f"docs/OMNI_{NEWEST.upper()}.md")),
    ("The Engines and Their Audit", ("FS", ["docs/ENGINES.md", "docs/history/ENGINE_AUDIT.md"])),
    ("Change Control: How the Engine Changes", ("F", "docs/CHANGE_CONTROL.md")),
    ("How Much of the Engine the Tests Run", ("F", "docs/ENGINE_COVERAGE.md")),
    ("PART", "The Physics: the Compass and the Nervous System",
     "Push and pull, the band and its cushions, the physics of a processor, and the two-way wires that carry the "
     "force from the brain to every muscle and back."),
    ("The Compass: Push, Pull and the Two Forces", ("M", "The Compass: Push, Pull and the Two Forces")),
    ("The Physics of a Processor", ("T", "The Physics of a Processor")),
    ("The Two-Way Nervous System", ("M", "The Two-Way Nervous System")),
    ("The Nervous System in Detail", ("FS", ["docs/TWO_WAY_NERVOUS_SYSTEM.md", "docs/NERVOUS.md"])),
    ("PART", "The Body: Muscles, Realms and Organisms",
     "One thousand one hundred and seven muscles in four realms on one spine, built into seven organisms, and every gauge used to "
     "judge them."),
    ("The Muscles, the Realms and the Seven Organisms", ("M", "The Muscles, the Realms and the Seven Organisms")),
    ("The Spine: the Base Every Stack Runs On", ("F", "docs/THE_SPINE.md")),
    ("The Four Realms", ("F", "docs/REALMS.md")),
    ("The Realm Muscles", ("F", "docs/REALM_MUSCLES.md")),
    ("The Domain Map", ("F", "docs/DOMAIN_MAP.md")),
    ("The Problem Map", ("F", "docs/history/PROBLEM_MAP_2026-09.md")),
    ("The Seven Organisms and the Benchmark Grid", ("T", "The Seven Organisms and the Benchmark Grid")),
    ("The Metrics Catalog", ("F", "docs/METRICS_CATALOG.md")),
    ("PART", "The Harness and the Wiring",
     "The universal plug, the adapters, the wire check, and the step-by-step work of wiring Omni-Compass onto a "
     "running stack."),
    ("The Plug, the Adapters and the Wire Check", ("M", "The Plug, the Adapters and the Wire Check")),
    ("The Harness", ("F", "docs/HARNESS.md")),
    ("The Wiring Guide", ("F", "docs/WIRING_GUIDE.md")),
    ("Before You Start, and the Eight Levels", ("M", "Before You Start, and the Eight Levels")),
    ("Stack by Stack", ("M", "Stack by Stack")),
    ("The Integration Manual", ("F", "docs/INTEGRATION_MANUAL.md")),
    ("Running the GPU Benchmark", ("FS", ["docs/GPU_RUN_GUIDE.md", "docs/LAMBDA_SETUP.md"])),
    ("PART", "Operating It",
     "The OFF switch, the rules the governor obeys, the log it keeps, and the care of a running installation."),
    ("The OFF Switch, the Rules, and the Log", ("M", "The OFF Switch, the Rules, and the Log")),
    ("Maintenance, Upgrades and Security", ("M", "Maintenance, Upgrades and Security")),
    ("The Operator Manual", ("F", "docs/OPERATOR_MANUAL.md")),
    ("PART", "Proving It",
     "Paired runs, receipts, rules written before the runs, and every result to date with its evidence class."),
    ("The Receipts, in Their Totality", ("F", "docs/THE_RECEIPTS.md")),
    ("How to Read the Results", ("F", "docs/HOW_TO_READ_THE_RESULTS.md")),
    ("The Benefit Sheet: One Number per Benchmark", ("F", "docs/BENEFIT_SHEET.md")),
    ("Every Level on One Page", ("F", "docs/LEVELS.md")),
    ("The Dossier: Every Result in One Place", ("F", "docs/DOSSIER.md")),
    ("Paired Runs and Receipts on Your Own System", ("M", "Paired Runs and Receipts on Your Own System")),
    ("Evidence Classes and How to Read a Result", ("M", "Evidence Classes and How to Read a Result")),
    ("The Frozen Engines and the Three-Run Rule", ("M", "The Frozen Engines and the Three-Run Rule")),
    ("Results to Date", ("M", "Results to Date")),
    ("Wire In, or Watch: The Verdict per Knob", ("F", "docs/WIRING_VERDICTS.md")),
    ("The Pilot Protocol and Kit", ("FS", ["docs/PILOT_PROTOCOL.md", "docs/PILOT_KIT.md"])),
    ("The GPU Bench", ("F", "docs/GPU_BENCH.md")),
    ("The GPU Preregistration", ("F", "docs/GPU_PREREGISTRATION.md")),
    ("The Realms Preregistration", ("F", "docs/REALMS_PREREGISTRATION.md")),
    ("The Compass Law on Real Kubernetes: Preregistration", ("F", "docs/K8S_COMPASS_PREREGISTRATION.md")),
    ("The Pod Start Wait on One Shared Host", ("F", "docs/POD_START_WAIT.md")),
    ("The 95th and 99th Percentiles: Where a Tail Reads Higher, and Why", ("F", "docs/TAIL_LATENCY.md")),
    ("How Small an Effect Each Test Can See", ("F", "docs/POWER.md")),
    ("Every Change to Every Preregistration", ("F", "docs/DEVIATIONS.md")),
    ("Limitations and Threats to Validity", ("F", "docs/LIMITATIONS.md")),
    ("The Evidence Ledger", ("F", "docs/EVIDENCE_LEDGER.md")),
    ("The Claims Register", ("F", "docs/CLAIMS_REGISTER.md")),
    ("Comparison with Existing Controllers", ("F", "docs/COMPARISON.md")),
    ("The State of Play", ("F", "docs/STATE_OF_PLAY.md")),
    ("PART", "Value, License and History",
     "What a receipt is worth, how the license is priced against it, how the code is sealed, and how Omni-Compass came "
     "to be."),
    ("Where the Value Comes From", ("M", "Where the Value Comes From")),
    ("The Economics of a Receipt", ("T", "The Economics of a Receipt")),
    ("Due Diligence", ("F", "docs/DUE_DILIGENCE.md")),
    ("License and Commercial Terms", ("M", "License and Commercial Terms")),
    ("Licensing: Questions and Answers", ("F", "LICENSING_FAQ.md")),
    ("Third-Party Notices", ("F", "THIRD_PARTY_NOTICES.md")),
    ("The Enterprise License: Standard Terms", ("F", "ENTERPRISE_LICENSE.md")),
    ("Patents and Trademarks", ("FS", ["PATENTS.md", "TRADEMARKS.md"])),
    ("Security Policy", ("F", "SECURITY.md")),
    ("Repository Standards", ("F", "docs/REPOSITORY_STANDARDS.md")),
    ("Python, C++ and the Seal", ("M", "Python, C++ and the Seal")),
    ("The Founder's Working Notes", ("F", "docs/history/HANDOFF_CHAPTER.md")),
    (f"The Road to the Engine That Stands: Omni {ROAD_TITLE}", ("FS", ROAD)),
    ("History", ("F", "docs/HISTORY.md")),
    ("BACK", None),
    ("Glossary", ("M", "Glossary")),
    ("Appendix A. Command Reference", ("M", "Appendix A - Command Reference")),
    ("Appendix B. File Map", ("M", "Appendix B - File Map")),
    ("Appendix C. The Equations in Full", ("M", "Appendix C - The Equations in Full")),
    ("Appendix D. Metrics", ("M", "Appendix D - Metrics")),
    ("Appendix E. Troubleshooting", ("M", "Appendix E - Troubleshooting")),
    ("Appendix F. Evidence Map", ("M", "Appendix F - Evidence Map")),
    ("Appendix G. The Muscles: What Each Is For, and How It Is Wired", ("F", "docs/MUSCLE_CATALOG.md")),
    ("Appendix H. Source of the Engine", ("X", "source")),
    ("Appendix I. The License", ("X", "license")),
    ("Appendix J. Reproducing Everything, From a Clean Machine", ("M", "Appendix J - Reproducing Everything, From a Clean Machine")),
    ("Index", ("X", "index")),
    ("Contact", ("X", "contact")),
]

LIVE_OUTLINE = [
    # one chapter for each section of the live benchmark engine page, in the page's own order: the wall, the control panel,
    # the contents, Parts 2 to 5 section by section, the page's appendixes A to G; then the book's own reading and license parts
    ("PART", "Monitor Wall, Control Panel and Contents",
     "The monitor wall, the control panel directly under it, and the page's contents."),
    ("Monitor Wall", ("M", "Monitor Wall")),
    ("Control Panel", ("M", "Control Panel")),
    ("Contents: the Page's Order and Its Numbering", ("M", "Contents: the Page's Order and Its Numbering")),
    ("PART", "Results",
     "The page's Part 2: what Omni-Compass did against native, every LOSS row included."),
    ("Scorecard", ("M", "Scorecard")),
    ("Benefit Against Native", ("M", "Benefit Against Native")),
    ("Benefit Board", ("M", "Benefit Board")),
    ("LOSS Register", ("M", "LOSS Register")),
    ("Status Board", ("M", "Status Board")),
    ("PART", "Live Operation",
     "The page's Part 3: the engine at work, live, native beside Omni-Compass, from the organism to the dashboards."),
    ("Live Organism", ("M", "Live Organism")),
    ("Golden Signals and Event Log", ("M", "Golden Signals and Event Log")),
    ("Control Console", ("M", "Control Console")),
    ("Heartbeat Dial", ("M", "Heartbeat Dial")),
    ("Control Cycle", ("M", "Control Cycle")),
    ("Phase Plane and Scoreboard", ("M", "Phase Plane and Scoreboard")),
    ("Brain State", ("M", "Brain State")),
    ("Verdict", ("M", "Verdict")),
    ("Dashboards", ("M", "Dashboards")),
    ("PART", "Real Runs and Platforms",
     "The page's Part 4: the real runs played back, and the platforms they ran on."),
    ("Kubernetes Run Playback", ("M", "Kubernetes Run Playback")),
    ("Repetition Telemetry", ("M", "Repetition Telemetry")),
    ("Controller Decision Trace", ("M", "Controller Decision Trace")),
    ("Cloud Providers", ("M", "Cloud Providers")),
    ("Orchestrators and Governors", ("M", "Orchestrators and Governors")),
    ("GPU and CPU Hardware", ("M", "GPU and CPU Hardware")),
    ("CI Pipeline", ("M", "CI Pipeline")),
    ("PART", "Proof and Models",
     "The page's Part 5: the engine's own runs, its twin, its models and its specification."),
    ("Python Runs and Monte Carlo", ("M", "Python Runs and Monte Carlo")),
    ("C++ Twin", ("M", "C++ Twin")),
    ("Scenarios and Injection Grid", ("M", "Scenarios and Injection Grid")),
    ("Whole Organism", ("M", "Whole Organism")),
    ("Measured Effect", ("M", "Measured Effect")),
    ("Telemetry Analytics", ("M", "Telemetry Analytics")),
    ("Master Switch Wiring", ("M", "Master Switch Wiring")),
    ("Specification and Mathematics", ("M", "Specification and Mathematics")),
    ("Failure Modes and Controls", ("M", "Failure Modes and Controls")),
    ("Self-Governed Rendering", ("M", "Self-Governed Rendering")),
    ("PART", "The Page's Appendixes",
     "The page's appendixes A to G, where it keeps its build, its explanations, its key and its disclosures."),
    ("Title Page and Build", ("M", "Title Page and Build")),
    ("Reading Guide", ("M", "Reading Guide")),
    ("Problem and Answer", ("M", "Problem and Answer")),
    ("Executive Summary and Reading Key", ("M", "Executive Summary and Reading Key")),
    ("Monitor List", ("M", "Monitor List")),
    ("The Glossary and Index", ("M", "The Glossary and Index")),
    ("Disclosures, Law and Contact", ("M", "Disclosures, Law and Contact")),
    ("PART", "Reading a Result off the Page",
     "The mechanism of action side by side, the trace from a tile to its record, what to do when a tile reads LOSS, and what the page does not tell you."),
    ("The Mechanism of Action, Side by Side", ("M", "The Mechanism of Action, Side by Side")),
    ("From a Tile to Its Record", ("M", "From a Tile to Its Record")),
    ("When a Tile Reads LOSS", ("M", "When a Tile Reads LOSS")),
    ("What the Page Does Not Tell You", ("M", "What the Page Does Not Tell You")),
    ("PART", "License and Your Copy",
     "The terms the page and this manual are licensed under, and how to verify a copy of the page."),
    ("License and Commercial Terms", ("M", "License and Commercial Terms")),
    ("Verifying Your Copy of the Page", ("M", "Verifying Your Copy of the Page")),
    ("BACK", None),
    ("Glossary", ("M", "Glossary")),
    ("Appendix A. The Page, Section by Section", ("M", "Appendix A - The Page, Section by Section")),
    ("Appendix B. Every Control", ("M", "Appendix B - Every Control")),
    ("Appendix C. The Gauges on the Wall", ("M", "Appendix C - The Gauges on the Wall")),
    ("Appendix D. The Colours and the Marks", ("M", "Appendix D - The Colours and the Marks")),
    ("Appendix E. Troubleshooting the Page", ("M", "Appendix E - Troubleshooting the Page")),
    ("Appendix F. The License", ("X", "license")),
    ("Appendix G. Licensing: Questions and Answers", ("F", "LICENSING_FAQ.md")),
    ("Appendix H. Third-Party Notices", ("F", "THIRD_PARTY_NOTICES.md")),
    ("Appendix I. The Enterprise License: Standard Terms", ("F", "ENTERPRISE_LICENSE.md")),
    ("Appendix J. Patents and Trademarks", ("FS", ["PATENTS.md", "TRADEMARKS.md"])),
    ("Appendix K. Security Policy", ("F", "SECURITY.md")),
    # the page word for word, written from the page at every build (docs/book/build_live_manual.py), so the book and the
    # page read each other both ways
    ("Appendix L. The Page Word for Word: Every Section, Monitor and Knob", ("F", "docs/engine/PAGE_WORD_FOR_WORD.md")),
    ("Index", ("X", "index")),
    ("Contact", ("X", "contact")),
]

OUTLINE = OWNER_OUTLINE if OWNER else LIVE_OUTLINE if LIVE else OPERATOR_OUTLINE

# Manual section number -> book chapter number, so that "section 14" in the manual reads "Chapter 44" in the book.
MAN_NUM = {}
for m in re.finditer(r"^## (\d+)\. (.*)$", read(MANUAL_REL), re.M):
    MAN_NUM[int(m.group(1))] = m.group(2).strip()


def source_listing(rel, nb=None):
    lines = read(rel).splitlines()
    num = nb.heading(2, rel) if nb is not None else rel         # numbered like every other section of its appendix
    head = num[:len(num) - len(rel)] if nb is not None else ""
    return [Heading(inline(f"{head}`{rel}`"), H2, 2, toc_text=num), Paragraph(inline(f"{len(lines)} lines."), CAP), Spacer(1, 4),
            *code_block(lines, SRC), Spacer(1, 10)]


def special(name, nb=None):
    if name == "source":
        fp = json.loads(read(ENGINE_JSON))
        files = list(fp["files"])
        py = [rel for rel in files if rel.endswith(".py")]
        tables = [rel for rel in files if not rel.endswith(".py")]
        intro = (f"The engine that stands, {fp['version']}, is the {len(files)} files named in `{ENGINE_JSON}` (digest "
                 f"{fp['digest'][:16]}): {len(py)} Python files and {len(tables)} tables. The Python files are printed here in "
                 "full from the repository, in the fingerprint's order, so that the book and the code can be read side by side "
                 "and nothing in the mechanism is withheld from the owner: the Kubernetes governor, its muscles, the replica "
                 "room, the quota budget and the two card governors (`omni_controller/`); the engine core, the compass law, "
                 "the compass, the verdict, the conveyance law, the plug adapter, the nervous system, the master switch and "
                 "the rest of the library (`omnicompass/`); the modelled plants, the harness, the presets, the max's arm and "
                 "the card's model (`realms/`); and the three runners the fingerprint covers (`tools/`). The tables are the "
                 "muscle catalogs: `realms/catalog_v5.csv` (the 1,107 muscles, printed muscle by muscle in the Muscles "
                 "appendix with every card of `realms/muscle_cards_v5.csv`) and the earlier catalogs kept for their results "
                 "(" + ", ".join(f"`{rel}`" for rel in tables if "v5" not in rel) + "). `python3 tools/omni_version.py` hashes "
                 f"every one of the {len(files)} and prints {fp['version']} when none has changed; `verify.py` fails if a byte "
                 "of them differs from the fingerprint.")
        story = [Paragraph(inline(intro), BODY)]
        for rel in py:
            story += source_listing(rel, nb)
        return story
    if name == "index":
        return [Paragraph(inline("Every term of the glossary where this book defines or discusses it, every muscle family where it "
                                 "is named, every file of the repository and every command-line setting this book names, with the "
                                 "pages they stand on. A plain mention of a common word is not an entry: the index points to where "
                                 "a thing is explained. A term whose pages would run past its line keeps the pages that fit, where it "
                                 "is defined and first used; after those it is throughout the book."), BODY), Spacer(1, 10), INDEX]
    if name == "license":
        lines = [ln for ln in read("LICENSE").splitlines()]
        return [Paragraph(inline("The license under which this book and the software are made available, as it stands in "
                                 "the file `LICENSE` at the root of the repository."), BODY), *code_block(lines, CODE)]
    if name == "contact":
        return md_flow([
            "Licensing, pilots, evaluations and the Omni-Compass Enterprise License:", "",
            "**The Omni-Compass LLC**", "", "Owner and developer: AJ Dubra", "",
            "Main office infrastructure: toll-free direct 1-888-339-9551, system route asset 1-888-DEX-YLL-1", "",
            "Landline, registered in Florida: 321-746-4411", "",
            "www.omni-compass.com", "",
            f"Repository: {REPO_URL.removeprefix('https://')}", "",
            "Any use beyond evaluation and simulation requires a signed, paid Omni-Compass Enterprise License. "
            "Write to The Omni-Compass LLC before any production use."])
    raise KeyError(name)


# ---------------------------------------------------------------- the book's one numbering
# The founder's order of 17 October: once every figure is placed, renumber, then realign every reference. A chapter
# is numbered by the book (CHAPNUM, in the order of the outline); every section under it is numbered chapter.m in
# the order it appears, whatever label its source carried (the manual's own "16.1b", a bound page's "3." or "A."),
# and a subsection chapter.m.k; an appendix numbers its sections by its letter (K.1). Every reference in the text
# ("section 16.4b", "chapter 6", "Appendix E", "Part VI") is rewritten to the book's numbers from the map the
# headings make, and a reference that resolves to nothing is listed at the end of the build.
LABEL_RE = re.compile(r"^(?:(\d+(?:\.\d+)*[a-z]?)\.?|([A-Z])\.(\d+)?|([IVX]+)\.)\s+(?=\S)")
PART_WORDS = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
# the manual's own grouping of its chapters into parts (its preface) against the book's parts: the Operator's
# manual and its book share one grouping; the Owner's manual groups its 18 chapters in seven, the book in eight
PART_MAP = ({"II": "Two", "III": "Five", "IV": "Five", "V": "Six", "VI": "Seven", "VII": "Eight"} if OWNER
            else {"I": "One", "II": "Two", "III": "Three", "IV": "Four", "V": "Five", "VI": "Six", "VII": "Seven", "VIII": "Eight"})
SEC_REF = re.compile(r"\b([Ss]ections?)\s+(\d+(?:\.\d+)?[a-z]?(?:(?:,\s*|\s+and\s+|\s+or\s+|\s+to\s+)\d+(?:\.\d+)?[a-z]?)*)(?![\w.]\w)")
CHAP_REF = re.compile(r"\b([Cc]hapters?)\s+(\d+(?:(?:,\s*|\s+and\s+|\s+or\s+|\s+to\s+)\d+)*)\b")
APPX_REF = re.compile(r"\bAppendi(x|ces) ([A-Z])\b")
PART_REF = re.compile(r"\bPart ([IVX]+)\b")
# a reference that follows another document's name (`DISCLOSURES.md`, section 4; `LICENSE`, section 10; the Operator's
# Manual, Appendix L; the founder's manuscript) carries that document's numbering and is left as written; the book's own
# manual, named in full, is not another document
EXTERNAL = re.compile(r"(\.md`|\.md\)|LICENSE`|Manual,|Manual's|DISCLOSURES|of the manual|the page['’]s)\W*$")   # the page's section 4c: the live benchmark engine's own numbering
MANUSCRIPT = re.compile(r"[Mm]anuscript")
OWN_NAME = (re.compile(r"Owner's Manual|OWNERS_MANUAL\.md") if OWNER else re.compile(r"Live Benchmark Engine Manual|LIVE_ENGINE_MANUAL\.md") if LIVE
            else re.compile(r"Operator's Manual|OMNI_COMPASS_MANUAL\.md"))
# the repository's pages ("the manual, section 4.5") cite the Operator's Manual; bound into the Owner's book they are
# read through this map onto the Owner's own sections that carry the same text (identity in the Operator's book)
OPERATOR_TO_OWNER = ({"1.5": "1.6", **{f"4.{k}": f"8.{k}" for k in range(1, 8)}, **{f"6.{k}": f"9.{k}" for k in range(1, 5)},
                      "7.1": "10.1", "7.2": "10.2", "7.3": "10.3", "7.4": "10.5", "7.5": "10.6", "7.6": "10.7", "7.7": "10.8",
                      "7.8": "10.9", "7.9": "10.10", "7.10": "10.11"} if OWNER else {})
UNRESOLVED = []
MAN_LABELS = {}                           # the manual's "16.1b" -> the book's "48.2"
DOC_LABELS = {}                           # a bound page's own "3" or "A" -> the book's "28.3", keyed by the page
NUMBERERS = {}                            # the numberer of every outline item, keyed by its title


class Numberer:
    """The numbers of one chapter's headings, and the map from each heading's source label to its book number."""
    def __init__(self, chap):
        self.chap, self.m, self.k, self.labels = chap, 0, 0, {}

    def heading(self, lvl, txt):
        m = LABEL_RE.match(txt)
        label = None
        if m:
            if m.group(1):
                label = m.group(1)
            elif m.group(2):
                label = m.group(2) + ("." + m.group(3) if m.group(3) else "")
            else:
                label = m.group(4)
            txt = txt[m.end():]
        if self.chap is None:
            return txt
        if lvl <= 2:
            self.m += 1; self.k = 0; num = f"{self.chap}.{self.m}"
        else:
            self.k += 1; num = f"{self.chap}.{self.m}.{self.k}"
        if label:
            self.labels.setdefault(label, num)
        return f"{num} {txt}"


def number_headings(lines, shift, nb):
    """Every heading of a source renumbered by the book (a fenced code block's '# comment' is not a heading)."""
    out, fence = [], False
    for ln in lines:
        if ln.startswith("```"):
            fence = not fence; out.append(ln); continue
        m = None if fence else re.match(r"^(#{1,6}) (.*)", ln)
        if m:
            lvl = max(2, min(3, len(m.group(1)) - shift + 1))
            out.append(m.group(1) + " " + nb.heading(lvl, m.group(2).strip()))
        else:
            out.append(ln)
    return out


def rewrite_refs(text, kind, key, own, prev=""):
    """Every reference in one line rewritten to the book's numbers; one that resolves to nothing is kept as written
    and listed. A reference to another document's numbering (`DISCLOSURES.md`, section 4; the Operator's Manual,
    Appendix L; `LICENSE`, section 10; the manuscript) is left as it stands; prev, the line before, supplies the
    context of a reference that starts a line."""
    def flag(s):
        UNRESOLVED.append(f"{kind} {key}: {s}"); return s

    def external(start):
        ctx = (prev[-80:] + "\n" + text[:start]) if start < 60 else text[start - 60:start]
        if MANUSCRIPT.search(ctx[-200:]):
            return True
        return bool(EXTERNAL.search(ctx)) and not OWN_NAME.search(ctx[-70:])

    def man_chapter(t):
        if not t.isdigit():                        # a lettered section (the live benchmark engine page's 1j) is no chapter of a manual
            return None, None
        n = CHAPNUM.get(MAN_NUM.get(int(t), ""))
        return (str(n), "chapter") if n else (None, None)

    def sec_token(t, to_manual):
        if "." in t:
            if kind != "M" and t in own and not to_manual:
                return own[t], "section"
            t2 = OPERATOR_TO_OWNER.get(t, t) if kind in ("F", "FS") else t
            return (MAN_LABELS[t2], "section") if t2 in MAN_LABELS else (None, None)
        if kind == "M" or to_manual:
            return man_chapter(t)
        return (own[t], "section") if t in own else (None, None)

    def sec(mt):
        if external(mt.start()):
            return mt.group(0)
        word, lst = mt.group(1), mt.group(2)
        to_manual = kind != "M" and bool(re.search(r"manual(?:'s)?\W*$", text[max(0, mt.start() - 30):mt.start()]))
        res = [sec_token(t, to_manual) for t in re.findall(r"\d+(?:\.\d+)?[a-z]?", lst)]
        if any(r[0] is None for r in res) or len({r[1] for r in res}) != 1:
            return flag(mt.group(0))
        it = iter(res)
        new = re.sub(r"\d+(?:\.\d+)?[a-z]?", lambda m: next(it)[0], lst)
        if res[0][1] == "chapter":
            word = "Chapters" if word.endswith("s") else "Chapter"
        return f"{word} {new}"

    def chap(mt):
        if external(mt.start()):
            return mt.group(0)
        if kind != "M" and not re.search(r"manual(?:'s)?\W*$", text[max(0, mt.start() - 30):mt.start()]):
            return mt.group(0)                     # a bound page's own "chapter 3" is its own numbering, left as written
        nums = [CHAPNUM.get(MAN_NUM.get(int(t), "")) for t in re.findall(r"\d+", mt.group(2))]
        if any(n is None for n in nums):
            return flag(mt.group(0))
        it = iter(nums)
        return mt.group(1) + " " + re.sub(r"\d+", lambda m: str(next(it)), mt.group(2))

    def appx(mt):
        if mt.group(2) in BOOK_APPENDICES or external(mt.start()):
            return mt.group(0)
        return flag(mt.group(0))

    def part(mt):
        w = PART_MAP.get(mt.group(1))
        return f"Part {w}" if w else flag(mt.group(0))

    text = CHAP_REF.sub(chap, text)                    # first: a "Chapter N" made by the section rule below is final
    text = SEC_REF.sub(sec, text)
    text = APPX_REF.sub(appx, text)
    return PART_REF.sub(part, text)


def source_lines(src):
    """The lines of an outline item's source and the heading shift md_flow reads them with."""
    kind, key = src
    if kind == "T":
        return THEORY[key], 1
    if kind == "D":
        return DECL[key], 1
    if kind == "M":
        return MAN[key], 2
    if kind == "F":
        return doc_body(key)[1], 1
    if kind == "FS":
        lines = []
        for rel in key:
            t, body = doc_body(rel)
            lines += ["# " + (t or rel), ""] + body
        return lines, 0
    if kind == "X" and key == "manifests":
        return MAN["Appendix I - The Install Manifests"], 2
    return [], 0


def prepare(src, nb, own=None):
    """A source's lines numbered by the book and with every reference rewritten to the book's numbers."""
    kind, key = src
    lines, shift = source_lines(src)
    lines = number_headings(lines, shift, nb)
    own = nb.labels if own is None else own
    out, fence, prev = [], False, ""
    for ln in lines:
        if ln.startswith("```"):
            fence = not fence
        out.append(rewrite_refs(ln, kind, key, own, prev))
        if ln.strip():
            prev = ln
    return out


def chapter_flow(src, nb):
    kind, key = src
    nb.m = nb.k = 0      # the printing pass numbers the headings again from the first: the first pass only made the labels
    if kind == "X" and key != "manifests":
        return special(key, nb)
    lines, shift = source_lines(src)
    if not lines and kind != "X":
        raise KeyError(kind)
    flow = md_flow(prepare(src, nb), shift=shift)
    if kind == "X":                                           # the install manifests: the appendix text, then the files
        for rel in ["deploy/install/omni-compass.yaml", "deploy/install/rbac-cloud.yaml", "deploy/install/omni-compass-cloud.yaml",
                    "deploy/rbac-target.yaml", "deploy/Dockerfile", "deploy/Dockerfile.cloud"]:
            flow += source_listing(rel, nb)
    return flow


def appendix_letter(title):
    m = re.match(r"^Appendix ([A-Z])\.", title)
    return m.group(1) if m else None


CHAPNUM = {}
n = 0
for item in OUTLINE:
    if item[0] not in ("PART", "BACK") and not item[0].startswith(("Appendix", "Glossary", "Index", "Contact")):
        n += 1; CHAPNUM[item[0]] = n
        if item[1][0] == "M":
            CHAPNUM[item[1][1]] = n
BOOK_APPENDICES = {appendix_letter(item[0]) for item in OUTLINE if item[0].startswith("Appendix")}

# the first pass over the outline: every heading numbered, so that every reference can be rewritten in the second
for item in OUTLINE:
    if item[0] in ("PART", "BACK"):
        continue
    title, src = item
    chap = str(CHAPNUM[title]) if title in CHAPNUM else appendix_letter(title)
    nb = Numberer(chap)
    lines, shift = source_lines(src)
    number_headings(lines, shift, nb)
    NUMBERERS[title] = nb
    if src[0] == "M":
        MAN_LABELS.update(nb.labels)
    else:
        DOC_LABELS[title] = nb.labels

# ---------------------------------------------------------------- document


class Book(BaseDocTemplate):
    keepTogetherClass = KeepWithStart         # a heading with the start of what follows, never with the whole of it

    def __init__(self, path):
        super().__init__(str(path), pagesize=letter, leftMargin=INNER, rightMargin=OUTER, topMargin=TOP,
                         bottomMargin=BOTTOM, title="The Omni-Compass " + EDITION_NAME, author="The Omni-Compass LLC",
                         subject="How to embed, wire, tune and run Omni-Compass on your stack",
                         creator="The Omni-Compass LLC")
        self.keepTogetherClass = KeepWithStart    # the template's own default is the whole-or-nothing KeepTogether
        INDEX.book = self                         # the index records the page label the reader sees
        self.body_start = None
        self.chapter = ""
        self.part = ""
        self.no_head, self.bare = set(), set()
        self.frame = Frame(INNER, BOTTOM, FW, FH, id="f", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate("body", [self.frame], onPage=self.mirror, onPageEnd=self.decorate)])
        self.in_part = False
        self._hseq = 0
        self._floats = []
        self._page_figs = 0                       # figures placed on the page being filled: at most two

    def beforeDocument(self):
        self.body_start, self.chapter, self.no_head, self.bare, self.in_part, self._hseq = None, "", set(), set(), False, 0
        self._floats = []
        self._page_figs = 0

    def afterPage(self):
        self._page_figs = 0

    # no dead pages: a chapter break that would leave a page under FILL opens the chapter on the same page; a figure
    # that does not fit under its paragraph floats to the top of the next page while the text goes on
    def filterFlowables(self, flowables):
        f = flowables[0]
        frame = self.frame
        if frame is None:                                     # between two pages: only the page-begin action passes
            return
        avail = frame._y - frame._y1p
        if isinstance(f, FlushFloats):
            floats, self._floats = self._floats, []
            flowables[0:1] = floats or [None]
            return
        if self._floats and not getattr(f, "_figpiece", False) and (
                not isinstance(f, (PageBreak, CondPageBreak, Marker, ChapterBreak, OpenerSpace, FloatFigure))
                or frame._atTop and isinstance(f, (OpenerSpace, FloatFigure))):
            # a floating figure is placed at the first room that holds it: the top of the next page, or sooner, the
            # first gap under a paragraph that is tall enough; at most two figures stand on one page
            room, take = avail, []
            while self._floats and self._page_figs + len(take) < 2:
                g = self._floats[0]
                g.canv = self.canv
                try:
                    g.wrap(frame._aW, room)
                    h = g._H                                  # the content's own height (wrap() answers "split me")
                finally:
                    del g.canv
                if h + FLOAT_SLACK > room and (take or not frame._atTop):
                    break
                take.append(self._floats.pop(0)); room -= h
            if take and hasattr(f, "_postponed"):             # the floats take this page; f gets its next page again
                del f._postponed
                mbe = getattr(self, "_multiBuildEdits", None)
                if mbe:                                       # and the pass's own clean-up of that flag is withdrawn
                    edits = mbe.__self__
                    edits[:] = [e for e in edits if not (len(e) == 3 and e[1] is f and e[2] == "_postponed")]
            if take:
                placed = []
                for g in take:                                # a figure's own text (its tail) lands right under it
                    placed.append(g)
                    if getattr(g, "_tail", None) is not None:
                        placed.append(g._tail)
                flowables[0:0] = placed
                return
            anchor = getattr(f, "_anchor", False) or (isinstance(f, KeepTogether)
                                                      and any(getattr(x, "_anchor", False) for x in getattr(f, "_content", ())))
            share = avail / frame._aH
            if anchor and not frame._atTop and (share <= 1 - FILL or len(self._floats) >= 2 and share <= 0.45):
                # the paragraph that names the next figure (with the heading it opens under, if any) does not start
                # while an earlier figure still waits and the page is already four fifths used, nor while two or more
                # wait (a whole pair ahead of it) and the page is over half used: the waiting figures take the next page
                # tops and the paragraph follows them, so the figures never run pages behind the text that names them.
                # The second rule may leave one page before a run of full-page figures between half and four fifths
                # used; without it the text would run a whole paragraph ahead of its figures for the rest of the run
                flowables[0:0] = [PageBreak()]
                return
        if isinstance(f, ChapterBreak):                       # a figure still floating opens the next page, before the text
            if frame._atTop:
                flowables[0] = None
            elif avail / frame._aH > 1 - FILL:
                flowables[0] = Spacer(1, 16)
            else:
                flowables[0] = PageBreak()
            return
        if isinstance(f, OpenerSpace):
            flowables[0] = Spacer(1, f.height if frame._atTop else f.mid)
            return
        if isinstance(f, FloatFigure):
            if not frame._atTop and not getattr(f, "_floated", False):   # a figure floats once; placed, it stays
                f.canv = self.canv                            # a KeepTogether measures its content on the canvas
                try:
                    f.wrap(frame._aW, avail)
                    h = f._H                                  # the content's own height (wrap() answers "split me")
                finally:
                    del f.canv
                # it stays under its paragraph when it fits with a line to spare (so its caption never parts from its
                # drawing), the page holds fewer than two figures, and no earlier figure is still waiting (order kept)
                if h + FLOAT_SLACK > avail or self._page_figs >= 2 or self._floats:
                    f._floated = True
                    mbe = getattr(self, "_multiBuildEdits", None)
                    if mbe:                                   # every pass of the build starts with nothing floated
                        mbe((lambda x: x.__dict__.pop("_floated", None), f))
                    f._tail = flowables.pop(1) if len(flowables) > 1 and getattr(flowables[1], "_figtail", False) else None
                    self._floats.append(f); flowables[0] = None
            return

    # mirrored margins: odd pages are right-hand pages, the gutter is on the inside
    def mirror(self, c, d):
        x = INNER if d.page % 2 else OUTER
        for f in self.pageTemplate.frames:
            f._x1 = x; f._geom()

    def toc_label(self, page):
        b = getattr(self, "final_body_start", None)
        return roman(page) if b is None or page < b else str(page - b + 1)

    def label(self, page):
        if self.body_start is None or page < self.body_start:
            return roman(page)
        return str(page - self.body_start + 1)

    def decorate(self, c, d):
        p = d.page
        if p in self.bare:                  # the title page carries nothing but itself
            return
        c.saveState()
        right = p % 2 == 1
        x0, x1 = (INNER, PW - OUTER) if right else (OUTER, PW - INNER)
        # the head of every page but the title page (the founder's order of 17 October): the book on the left, the part
        # or chapter the page belongs to on the right, so a reader flipping through always knows where they are
        c.setFont("Sans", SMALL); c.setFillColor(GREY)
        c.drawString(x0, PH - 0.6 * inch, "THE OMNI-COMPASS " + EDITION_NAME.upper())
        if self.chapter:
            head = self.chapter.upper()
            while head and c.stringWidth(head, "Sans", SMALL) > (x1 - x0) * 0.6:
                head = head[:-2].rstrip() + "…"
            c.drawRightString(x1, PH - 0.6 * inch, head)
        c.setStrokeColor(RULE); c.setLineWidth(0.5); c.line(x0, PH - 0.66 * inch, x1, PH - 0.66 * inch)
        # the foot of every page: the notice in two centered lines, the website alone and centered on the bottom line,
        # the page number in both bottom corners (the founder's order of 17 October: the left and the right, everywhere)
        mid = (x0 + x1) / 2
        c.setFont("Serif-Italic", SMALL); c.setFillColor(GREY)
        c.drawCentredString(mid, 0.64 * inch, "© 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only.")   # one literal, so tools/legal.py reads it whole
        c.drawCentredString(mid, 0.51 * inch, "All patents, copyrights and trademarks filed in the USA.")
        c.setFont("Serif-Bold", 9); c.setFillColor(NAVY)
        c.drawCentredString(mid, 0.35 * inch, "www.omni-compass.com")
        c.setFont("Serif", 10); c.setFillColor(INK)
        lab = self.label(p)
        c.drawString(x0, 0.35 * inch, lab)
        c.drawRightString(x1, 0.35 * inch, lab)
        c.restoreState()

    def afterFlowable(self, f):
        if isinstance(f, Marker):
            if f.kind == "body":
                self.body_start = self.final_body_start = self.page
            elif f.kind == "nohead":
                self.no_head.add(self.page)
            elif f.kind == "bare":
                self.bare.add(self.page)
            elif f.kind == "chapter":
                self.chapter = f.kw["title"]
                if f.kw.get("opener"):
                    self.no_head.add(self.page)
            elif f.kind == "figure":
                self._page_figs += 1
                key = f"fig{f.kw['number']}"
                self.canv.bookmarkPage(key)
                self.notify("LOFEntry", (0, f"Figure {f.kw['number']}. {f.kw['title']}", self.page, key))
            return
        if isinstance(f, Heading):
            if f.level == 3:
                return
            self._hseq += 1
            key = f"h{self._hseq}"
            self.canv.bookmarkPage(key)
            if f.kind == "part":
                self.in_part = True
                lvl = 0
            elif f.kind == "chapter":
                lvl = 1 if self.in_part else 0
            else:
                lvl = 2 if self.in_part else 1
            self.canv.addOutlineEntry(re.sub(r"<[^>]+>", "", f.toc_text)[:120], key, level=lvl, closed=lvl >= 1)
            if f.kind in ("part", "chapter"):
                self.notify("TOCEntry", (0 if f.kind == "part" or not self.in_part else 1, f.toc_text, self.page, key))


def roman(n):
    vals = [(1000, "m"), (900, "cm"), (500, "d"), (400, "cd"), (100, "c"), (90, "xc"), (50, "l"), (40, "xl"), (10, "x"),
            (9, "ix"), (5, "v"), (4, "iv"), (1, "i")]
    out = ""
    for v, s in vals:
        while n >= v:
            out += s; n -= v
    return out


def new_page():
    """The next page, unless this one is still empty: never a blank page."""
    return [CondPageBreak(FH - 2)]


def front_matter(doc):
    s = []
    # title page
    big = ParagraphStyle("tt", fontName="Serif-Bold", fontSize=34, leading=40, alignment=TA_CENTER, textColor=NAVY)
    sub = ParagraphStyle("st", fontName="Serif-Italic", fontSize=15, leading=20, alignment=TA_CENTER, textColor=INK)
    s += [Marker("bare"), Spacer(1, 1.6 * inch), Paragraph("THE OMNI-COMPASS", big), Paragraph(EDITION_NAME.upper(), big),
          Spacer(1, 14), GoldRule(FW, 1.5, 14),
          Paragraph(SUBTITLE_HTML, sub), Spacer(1, 1.2 * inch),
          Paragraph("AJ Dubra", ParagraphStyle("au", fontName="Serif-Bold", fontSize=14, alignment=TA_CENTER, leading=18)),
          Paragraph("Owner and Developer", CENTER), Spacer(1, 0.3 * inch),
          Paragraph("THE OMNI-COMPASS LLC", ParagraphStyle("pub", fontName="Sans-Bold", fontSize=11, alignment=TA_CENTER,
                                                           textColor=GOLD, leading=14)),
          Paragraph(EDITION, CENTER), PageBreak()]
    # copyright page
    cp = ParagraphStyle("cp", parent=BODY, alignment=TA_LEFT, spaceAfter=7)
    s += [Marker("nohead"), Marker("chapter", title="Copyright and License"), Spacer(1, 0.2 * inch)]
    for t in [
        f"<b>The Omni-Compass {EDITION_NAME}</b><br/>{SUBTITLE}<br/>" + EDITION,
        "Copyright © 2026 The Omni-Compass LLC. All rights reserved. No part of this book may be reproduced, stored "
        "or transmitted in any form or by any means, except as allowed by the Omni-Compass Evaluation License, without "
        "the written permission of The Omni-Compass LLC.",
        "The Omni-Compass LLC reserves the right to change this book, the software it describes and their terms at any "
        "time, without notice. Every copy, export and printout of any part of this book carries this page, the LICENSE, "
        "the NOTICE and the Disclosures unchanged.",
        FILED[:-1] + " (no filing number is stated, and no grant, registration or approval is claimed). www.omni-compass.com",
        "“Omni-Compass”, the Omni-Compass rose and the related names and marks are trademarks of The "
        "Omni-Compass LLC. Other names that appear in this book are the property of their owners and are used only to "
        "identify the systems Omni-Compass works with.",
        "<b>License.</b> This book and the software it describes are proprietary and are not open source "
        "(SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0). They may be used only to evaluate "
        "Omni-Compass and to reproduce its published results, in simulation and on systems the reader owns or controls. "
        "Any commercial use, commercialization, monetization, production use, redistribution, hosted or managed "
        "service, or incorporation into any product or service requires a written Omni-Compass Enterprise License, "
        "signed by The Omni-Compass LLC and paid for. The full terms are printed in " + LICENSE_APPENDIX + ".",
        "<b>Disclaimer.</b> The software is provided “as is”, without warranty of any kind. " + RESULTS_LINE + " A modelled result is a statement about a model; a software benchmark is a statement about the software "
        "it ran on; only a hardware meter speaks for hardware. Nothing in this book is a promise of a particular saving on "
        "a particular system: the only number that applies to a system is the one its own paired runs produce, on its own "
        "receipt.",
        "Set in Liberation Serif and DejaVu Sans Mono, the text at 11 pt on a 16.5 pt line. Built from the repository "
        "by <font name='Mono' size='11'>"
        "docs/book/build_book.py</font>; the book and the code change in the same commit.",
        "The Omni-Compass LLC · www.omni-compass.com"]:
        s.append(Paragraph(t, cp))
    s.append(PageBreak())
    return s


def keep_with_next(flowables):
    """The opener's pieces stay with the first lines of the chapter: a title never ends a page."""
    for f in flowables:
        f.keepWithNext = 1
    return flowables


def chapter_opener(num, title, kicker=None, top=0.9 * inch):
    k = kicker or f"CHAPTER {num}"
    return [Marker("chapter", title=title, opener=True), OpenerSpace(top)] + keep_with_next(
        [Paragraph(k, KICK), Heading(inline(title), H1, 1, toc_text=(f"{num}. {title}" if num else title), kind="chapter"),
         GoldRule(FW, 1.2, 16), Spacer(1, 6)])


def front_lines(lines, kind="M", key="front"):
    """A front-matter section's lines: its headings carry no number, its references the book's numbers."""
    nb = Numberer(None)
    return [rewrite_refs(ln, kind, key, {}) for ln in number_headings(lines, 2, nb)]


def front_chapter(doc, title, lines, kind="M"):
    return [ChapterBreak(), Marker("chapter", title=title, opener=True), OpenerSpace(0.9 * inch)] + keep_with_next(
        [Heading(inline(title), H1, 1, kind="chapter"), GoldRule(FW, 1.2, 16)]) + md_flow(front_lines(lines, kind, title), shift=2)


OPERATOR_PREFACE = """I wrote this book for the engineers who put Omni-Compass into a running system: how to embed it, how to wire
it to every muscle of a stacked, clustered system or to any one muscle, how to tune it, how to run it, how to switch it
off, and how to check on their own system, with their own paired runs, what it does there. It is the manual for the glove
box, not a description of how the engine is built.

The book is in six parts, after the front matter.

| You are | Read |
|---|---|
| CTO, architect, head of platform | the front matter, Part One, the eight levels in Part Three, then Part Five |
| The engineer wiring it | everything, in order. Do not skip the wire check or the watch level |
| Platform engineer for one stack | Part Two, the chapter of Part Three for your stack, and Part Four |
| Data-center, facility or energy operator | the Quick Reference card, Part One, Part Three (levels five to seven, the processor and the data center under the servers), Part Four |
| Site reliability engineer, on call | the Quick Reference card, Part Four (the switches and the log), the troubleshooting appendix |
| Security and compliance | Part Four, the Disclosures, the license in the back matter |
| Procurement and counsel | the Disclosures, Part Six, the license and its questions and answers in the back matter |

**Part One, the governor from the outside,** says what Omni-Compass is as an installer meets it, how the muscles of a
stack become one body, and how it is tuned: the factory tune, the dial, each muscle's own card and the settings an
operator writes. **Part Two, the harness,** is the universal plug, the adapters, the wire check and the rules every wire
obeys. **Part Three** wires it onto a stack one level at a time and then stack by stack. **Part Four** is operating it:
the OFF switch, the rules, the log, maintenance and security. **Part Five** is checking it on your own system: paired
runs and receipts, evidence classes, the engine version and the three-run rule. **Part Six** is the license and how to
verify a copy. The back matter holds the glossary, every command, the files an installation touches, the gauges,
troubleshooting, and every muscle with its wiring and its own card.

**Conventions.** `Code` is a command, file or switch exactly as typed. "Native" means a system as it runs today,
without Omni-Compass. "Muscle" means any machine, service or controller Omni-Compass can read and set. "Knob" or
"lever" is one setting on a muscle. "The band" is a service reading's safe range. A step that writes to a system is
marked **WRITES**. Every number in a receipt carries its evidence class: S for a model (modelled), L for live software,
P for a physical meter."""


OWNER_PREFACE = """This is the Owner's Manual, the master: everything about Omni-Compass in one book, for whoever owns or licenses
it and so must know the whole mechanism. I wrote it so that the owner understands what they hold: not only which wire
goes where, but why the governor behaves the way it does, where its law comes from, how it is built, and how to prove on
their own system what it does for them. The Operator's Manual is the shorter book for the people who run it.

The book is in eight parts, and it can be read in two ways.

| You are | Read |
|---|---|
| CEO, board member, investor | the Problem and the Answer, the Foreword, the Prelude, the Introduction, the Executive Summary, Part One, the Results to Date, and Part Eight |
| CTO, architect, head of platform | Parts One to Four, then the eight wiring levels in Part Five, then Part Seven |
| The engineer wiring it | everything, in order. Do not skip the wire check or the watch level |
| Data-center, facility or energy operator | the Quick Reference card, Part One's chapter on the reflex, Part Five (levels five to seven, the processor and the data center under the servers), Part Six |
| Site reliability engineer, on call | the Quick Reference card, Part Six (the switches and the log), the troubleshooting appendix |
| Auditor, diligence team | Part Two (the mathematics), Part Seven (the proof), Appendices C, F and H |
| Procurement and counsel | the Disclosures, the license in the back matter, Part Eight |

**Part One, the philosophy and the theory,** sets out the closed circle: a system that is closed, bounded and pulled
toward a center cannot run away, and everything it does is a return. **Part Two, the mathematics,** gives the eight
equations and the control law that make the circle exact, with the theorem, the declaration and the audits that hold
them fixed. **Part Three, the physics,** brings the law into the machine: the compass, push and pull, the band and its
cushions, the physics of a processor, and the two-way nervous system. **Part Four, the body,** lays out the
muscles, the spine, the four realms and the seven organisms. **Part Five, the harness and the wiring,** is the universal plug and
the step-by-step work of wiring Omni-Compass onto a stack. **Part Six, operating it,** is the OFF switch, the rules
and the log. **Part Seven, proving it,** is every rule written before a run and every result after it. **Part Eight**
is value, the license, the seal and the history.

**Conventions.** `Code` is a command, file or switch exactly as typed. "Native" means a system as it runs today,
without Omni-Compass. "Muscle" means any machine, service or controller Omni-Compass can read and set. "Knob" or
"lever" is one setting on a muscle. "The band" is a knob's or a service reading's safe range. A step that writes to a
system is marked **WRITES**. Every result carries its evidence class: T for a theorem, V for verification of the code,
S for our own models (modelled), L for live software, P for a physical meter.

Some chapters gather documents that were written as the work went on, each at the moment its result came in. They
are kept as they were written, because the record of how a result was reached is part of the proof. Where two
chapters give different figures for the same thing, the later run and the State of Play govern."""


LIVE_PREFACE = """This is the Live Benchmark Engine Manual, the third book: how to read the live benchmark engine page, the monitor of the engine and of
the benchmark runs GitHub ran. It is for the operator at the dashboard: which tile means what, which knob does what, where every
number comes from, and how the mechanism of action of Omni-Compass against native shows on the monitors. It explains neither how
the engine is built (the Owner's Manual) nor how it is wired onto a stack (the Operator's Manual).

The book is in eight parts, in the page's own order (the Contents follow), and it can be read in two ways.

| You are | Read |
|---|---|
| The operator at the wall | the Quick Reference card; Parts One and Two; when a tile reads LOSS (Part Seven) |
| CTO, architect, head of platform | the scorecard (chapter 4); the fuse box and its tabs (chapter 2); Part Five |
| CEO, CFO, CIO, board member | the Problem and the Answer; the Disclosures; chapters 4, 5, 6 and 21 |
| Site reliability engineer | Part Two; the golden signals and metrics (chapter 10); the wall stack, `deploy/wall` (chapter 2) |
| Control or plant engineer | the contract and the mechanism knobs (chapter 2); chapters 13 to 16 |
| Auditor, diligence team | Part Six; Part Seven; the pipeline (chapter 24); the page word for word (Appendix L) |
| Procurement and counsel | the Disclosures and the papers bound into the back matter |

**Conventions.** `Code` is a command, file, anchor or switch exactly as typed. "Native" is the system by itself, orange;
"Omni-Compass" is Omni-Compass on top of native, blue. Those are the two sides, and the only two: Omni-Compass is never by
itself. Violet marks only a knob or profile turned from the factory tune. Red is never a side: it is
the stop sign of a line crossed. "A section" is a numbered part of the page, named by its number, its title and its anchor;
"a chapter" is a chapter of this book. A knob marked **LIVE** acts on the live benchmark engine; one marked **RECORDED** chooses a record and modifies
nothing. Every number carries its evidence class: P a physical meter, L live software, S our own
models (modelled); a model is never proof."""


PREFACE = OWNER_PREFACE if OWNER else LIVE_PREFACE if LIVE else OPERATOR_PREFACE


def preface_lines():
    """The book's preface: how the book reads, then the standards every page keeps (from the manual's preface)."""
    man = MAN["Preface: How to Use This Manual"]
    a = next(k for k, ln in enumerate(man) if ln.startswith("**The standards every page"))
    b = next(k for k, ln in enumerate(man) if ln.startswith("**How this manual is organised."))
    return PREFACE.splitlines() + [""] + man[a:b]


def build():
    FIG.write_svgs()                      # the same drawings, as files, for the pages on GitHub
    SCH.write_svgs()
    FIG_NO[0] = 0
    doc = Book(OUT_PDF)
    story = front_matter(doc)
    # contents, then the list of figures
    toc = TableOfContents(levelStyles=[TOC1, TOC2, TOC3], dotsMinLevel=1, formatter=doc.toc_label)
    story += new_page() + [Marker("nohead"), Marker("chapter", title="Contents"), Spacer(1, 0.5 * inch),
                           Paragraph("Contents", H1), GoldRule(FW, 1.2, 16), toc]
    lof = TableOfContents(levelStyles=[LOF], dotsMinLevel=0, formatter=doc.toc_label, notifyKind="LOFEntry")
    story += [ChapterBreak(), Marker("nohead"), Marker("chapter", title="List of Figures"), OpenerSpace(0.5 * inch, mid=24)] + keep_with_next(
        [Paragraph("List of Figures", H1), GoldRule(FW, 1.2, 16)]) + [
                           Paragraph(inline("Every figure is drawn from the code it pictures, by one of two kits "
                                            "(`docs/book/figures.py`; `docs/book/schematics.py` for the wiring "
                                            "schematics, block diagrams, flowcharts, timing diagrams, state machines, "
                                            "the receipts charted from their own tables and the grids), and printed "
                                            "where the text first needs it; the same drawings stand beside the text on "
                                            "GitHub, in `docs/book/figures/`. A chart of a receipt is read by the "
                                            "reading key: it pictures the table and adds nothing to it."), BODY),
                           Spacer(1, 6), lof]
    # the front matter, in full chapters, before a word about wiring (the founder's order of 14 October): the problem the
    # whole industry faces and Omni-Compass's solution first (21 October), then the foreword, the preface, the prelude and
    # the introduction, then the key, what a hooked-up system looks like and the card
    story += front_chapter(doc, PROBLEM, MAN[PROBLEM])
    story += front_chapter(doc, "Foreword", MAN["Foreword"])
    story += front_chapter(doc, "Preface", preface_lines())
    story += front_chapter(doc, PRELUDE, MAN[PRELUDE])
    story += front_chapter(doc, INTRO, MAN[INTRO])
    story += front_chapter(doc, "The key: GAIN, STEADY and LOSS", MAN["The key: GAIN, STEADY and LOSS"])
    story += front_chapter(doc, "What You Are Looking At", MAN["What You Are Looking At: Omni-Compass, Hooked Up, and How to Read Its Report"])
    story += front_chapter(doc, "Quick Reference: The Card for the Glove Box", MAN["Quick Reference: The Card for the Glove Box"])
    if OWNER:
        story += front_chapter(doc, "Executive Summary", MAN["Executive Summary"])
    story += front_chapter(doc, "Disclosures, Declarations and Disclaimers", doc_body("DISCLOSURES.md")[1], kind="F")
    md_parts = [f"# THE OMNI-COMPASS {EDITION_NAME.upper()}", "", BANNER_MD, "", EDITION, "", FILED, "",
                "The printable book of this text, with its contents and appendices: "
                f"`docs/{OUT_PDF.name}`. Built by `docs/book/build_book.py`" + (" --owner" if OWNER else " --live" if LIVE else "") + ".", ""]
    md_parts += [f"## {PROBLEM}", ""] + front_lines(MAN[PROBLEM]) + [""]
    md_parts += ["## Foreword", ""] + front_lines(MAN["Foreword"]) + ["## Preface", ""] + front_lines(preface_lines()) + [""]
    for sec in (PRELUDE, INTRO,
                "The key: GAIN, STEADY and LOSS", "What You Are Looking At: Omni-Compass, Hooked Up, and How to Read Its Report",
                "Quick Reference: The Card for the Glove Box") + (("Executive Summary",) if OWNER else ()):
        md_parts += [f"## {sec}", ""] + front_lines(MAN[sec]) + [""]

    part_no = 0
    words = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    first, after_part = True, False
    for item in OUTLINE:
        if item[0] == "PART":
            title, blurb = item[1], item[2]
            if first:                                       # the body opens on a fresh page: its page 1
                story += new_page() + [Marker("body")]; first = False
            else:                                           # a later part opens where the chapter before it ends
                story += [ChapterBreak()]                   # unless that page is already four fifths used
            story += [Marker("nohead"), Marker("chapter", title=title, opener=True), OpenerSpace(0.3 * inch, mid=14)] + keep_with_next(
                     [Paragraph(f"PART {words[part_no].upper()}", ParagraphStyle("pk", fontName="Sans-Bold", fontSize=13,
                                alignment=TA_CENTER, textColor=GOLD, leading=16)), Spacer(1, 6),
                      Heading(inline(title), ParagraphStyle("pt", fontName="Serif-Bold", fontSize=26, leading=32,
                              alignment=TA_CENTER, textColor=NAVY), 1, toc_text=f"Part {words[part_no]}. {title}", kind="part"),
                      Spacer(1, 8), GoldRule(FW, 1.5, 14), Spacer(1, 6),
                      Paragraph(inline(blurb), ParagraphStyle("pb", parent=BODY, fontName="Serif-Italic", fontSize=12,
                                leading=18, alignment=TA_CENTER, leftIndent=40, rightIndent=40))])
            md_parts += ["", f"# Part {words[part_no]}. {title}", "", f"*{blurb}*", ""]
            part_no += 1
            after_part = True
            continue
        if item[0] == "BACK":
            story += [ChapterBreak(), Marker("nohead"), Marker("chapter", title="Back Matter", opener=True),
                      OpenerSpace(0.3 * inch, mid=14)] + keep_with_next(
                     [Heading("Back Matter", ParagraphStyle("bm", fontName="Serif-Bold", fontSize=26, leading=32,
                              alignment=TA_CENTER, textColor=NAVY), 1, toc_text="Back Matter", kind="part"),
                      GoldRule(FW, 1.5, 14)])
            md_parts += ["", "# Back Matter", ""]
            after_part = True
            continue
        title, src = item
        num = CHAPNUM.get(title)
        flow = chapter_flow(src, NUMBERERS[title])
        opener = [Marker("chapter", title=title)] + chapter_opener(
            num, title, None if num else ("APPENDIX" if title.startswith("Appendix") else "BACK MATTER"),
            top=0.25 * inch if after_part or title == "Contact" else 0.9 * inch)   # the last chapter keeps the end notice on its page
        if after_part and LIVE:          # the live book: a part's heading stays on its page with its first chapter's opening
            keep_with_next(opener)
        story += ([] if after_part else [ChapterBreak()]) + opener
        story += flow
        after_part = False
        md_parts += ["", f"## {str(num) + '. ' if num else ''}{title}", ""]
        md_parts += md_text(src, NUMBERERS[title])
    # the notice at the end of the book, as at its start
    # whole, never split across a page: a page never opens on the last lines of a paragraph
    story += [FlushFloats(), Spacer(1, 8), KeepTogether([GoldRule(FW, 1.2, 10),
              Paragraph(inline(BANNER_MD[2:]), ParagraphStyle("end", parent=BODY, alignment=TA_LEFT))])]
    doc.multiBuild(story, canvasmaker=INDEX.getCanvasMaker())
    OUT_MD.write_text(normalize_markdown("\n".join(md_parts) + "\n")[0], encoding="utf-8")   # the notice on top and at the end
    seen = sorted(set(UNRESOLVED))
    print(f"references not resolved to the book's numbering: {len(seen)}" + "".join("\n  " + s for s in seen))
    print(OUT_PDF, doc.page, "pages")
    report_fill(OUT_PDF)


def report_fill(pdf):
    """No dead pages (the founder's order of 16 October, night): how far down the frame the content of every page
    reaches, and every page under four fifths, printed with the build so a shortfall is seen before a push."""
    try:
        import pymupdf
    except ImportError:
        print("page fill: not measured (pymupdf is not installed)")
        return
    book = pymupdf.open(str(pdf))
    page_h = book[0].rect.height
    short = []
    for n, page in enumerate(book, 1):
        low = TOP
        for b in page.get_text("dict")["blocks"]:
            if b["bbox"][3] < page_h - BOTTOM - 2:
                low = max(low, b["bbox"][3])
        for d in page.get_drawings():
            if d["rect"].height >= 2 and d["rect"].y1 < page_h - BOTTOM - 2:
                low = max(low, d["rect"].y1)
        reach = (low - TOP) / FH
        if reach < FILL:
            short.append(f"p{n} {reach:.0%}")
    print(f"page fill: {len(book) - len(short)} of {len(book)} pages at least {FILL:.0%} used; under it: "
          + (", ".join(short) if short else "none"))


def md_text(src, nb):
    """The book's one-file text for a chapter: a figure line points to its drawing beside the text (docs/book/figures/),
    and any other image (a plate) is left out (14 October)."""
    out = []
    for ln in _md_text(src, nb):
        m = IMAGE_LINE.match(ln)
        if m:
            fig = FIGURE_PATH.match(m.group(2))
            if fig and fig.group(1) in FIGURES:
                out.append(f"![{m.group(1)}](figures/{fig.group(1)}.svg)")
            continue
        out.append(ln)
    return out


def _md_text(src, nb):
    """The chapter's lines as the book numbers them: a chapter is '##', its sections '###', their subsections '####'."""
    kind, key = src
    if kind in ("T", "D", "F"):                                # their '##' is a section: one level down under the chapter
        return ["#" + ln if ln.startswith("#") else ln for ln in prepare(src, Numberer(nb.chap))]
    if kind == "M":                                            # the manual's '###' is already a section
        return prepare(src, Numberer(nb.chap))
    if kind == "FS":                                           # a bound page's title is a section, its '##' a subsection
        return ["##" + ln if ln.startswith("#") else ln for ln in prepare(src, Numberer(nb.chap))]
    if kind == "X" and key == "manifests":
        return prepare(src, Numberer(nb.chap))
    if kind == "X":
        if key == "source":
            fp = json.loads(read(ENGINE_JSON))
            py = [rel for rel in fp["files"] if rel.endswith(".py")]
            return [f"The full source of every Python file of the engine that stands, {fp['version']} (`{ENGINE_JSON}`, digest "
                    f"{fp['digest'][:16]}), {len(py)} files, as the printed book carries it: " + ", ".join(f"`{rel}`" for rel in py) + "."]
        if key == "license":
            return ["The license is the file `LICENSE`."]
        if key == "index":
            return ["Every glossary term where the book defines or discusses it, every muscle family, every file of the repository "
                    "and every setting the book names, with the pages they stand on in the printed book (this one-file text has no pages)."]
        if key == "contact":
            return ["The Omni-Compass LLC. Owner and developer: AJ Dubra. Main office infrastructure: toll-free direct "
                    "1-888-339-9551, system route asset 1-888-DEX-YLL-1; landline, registered in Florida, 321-746-4411. "
                    "www.omni-compass.com"]
    return []


if __name__ == "__main__":
    build()
