#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The live engine's guided tour, written once: one stop for every section of the page, in the page's own order, each in the
words the Live Engine Manual already prints for that section (the chapter that names the section's anchor), with the section's
own controls line from the page. Nothing in the tour is written for the tour alone but its opening and its close, which carry
the legal notice. The page builder (docs/engine/build_live_engine.py, the record `tour`) and the voice (tools/tour_voice.py,
the recorded clips) both read these steps, so the voice never says what the page and the manual do not.

    python3 tools/tour_script.py          prints every stop as it will be shown and spoken
    python3 tools/tour_script.py --check  exit 1 when a stop quotes words the page no longer carries
"""
from __future__ import annotations

import hashlib
import html
import json
import pathlib
import re
import sys
from decimal import ROUND_HALF_UP, Decimal

ROOT = pathlib.Path(__file__).resolve().parent.parent
MANUAL = ROOT / "docs" / "OMNI_COMPASS_LIVE_ENGINE_MANUAL.md"
PAGE = ROOT / "docs" / "engine" / "OMNI_COMPASS_LIVE_ENGINE.html"
sys.path.insert(0, str(ROOT / "tools"))
from legal import PLAIN  # noqa: E402  (the notice, written once)

# every part of the page a reader can stop at, in its order: the sections, the control cycle's trio, the title page and the
# disclosures (5 November, the editor seat: the tour said "That is the whole page" after leaving out 3e, A and G)
SECTION = r'<(?:section|header) class="(?:stack|trio|disclose|head)(?:\s[^"]*)?" id="([a-z0-9-]+)"'
CAP = 640           # the most characters a stop reads from its chapter, cut at a sentence: about 40 seconds of speech
CHAPTER = re.compile(r"^This chapter reads the page's (section [0-9]+[a-z]?|appendix [A-Z]|\*\*Contents\*\*)[, ]*(?:\*\*([^*]+)\*\*)? ?\(`#([a-z0-9-]+)`\)")
# the opening said in about 40 seconds, the notice after it (the live seat of 6 November: a 2 min 11 s opening, and a hand promised to point at what the
# words name, which it did not); what every button and key does is the card's own key, behind the blue question mark
OPEN = ("Welcome to the guided tour of the Omni-Compass Live Benchmark Engine. It starts with the figure of record, then walks the "
        "page section by section, in the words of the Live Benchmark Engine Manual. You do not have to take the tour: you can leave "
        "it at any moment and explore the page by hand, and the blue Guided tour tab brings it back. The section being read is outlined, and the lit "
        "sentence on this card is the one being spoken. The green circle, Skip, goes on; the red stop sign, Back, goes back; the "
        "blue question mark shows what every button and key does. Close, or the Escape key, ends the tour.")
CLOSE = ("That is the whole page. Its figure of record is the Omni index, read from the repository's three-run tables; every other "
         "aggregate on it is a second reading, and every LOSS row is shown in the LOSS Register. The three manuals, the Live "
         "Benchmark Engine Manual first, open from the control panel. Press Close to explore the page by hand; the blue Guided "
         "tour tab starts the tour again.")
BENEFIT = ROOT / "results" / "BENEFIT_SHEET.json"   # the Omni index row the result-first row (#heroRow) reads, as the record fleet carries it
NAV = ("This stop is done. Press the green circle, Skip, for the next stop; the yellow diamond, Replay, to hear this one again; "
       "the red stop sign, Back, for the stop before; or the blue question mark to see what every button does. While Step on by "
       "itself is on, the tour goes on by itself.")


def _strip_parens(s: str) -> str:
    """Parentheses that only point (a chapter, a section, an anchor, a file) are read by the eye, not the ear."""
    pointer = re.compile(r"\((?:[^()]*?(?:`|chapter|section|appendix|Appendix|monitor \d|monitors \d|#|\.py|\.json|\.md|\.yml)[^()]*?)\)")
    for _ in range(4):
        s2 = pointer.sub("", s)
        if s2 == s:
            break
        s = s2
    return s


def _code(m) -> str:
    """A name in code type, said as the ear can take it: a page by its own name, a program as the repository's code, a record
    as the record; a flag, a key or an expression is left to the eye."""
    c = m.group(1)
    if re.fullmatch(r"[A-Za-z][A-Za-z -]*", c):
        return c
    f = re.fullmatch(r"(?:[\w.-]+/)*([\w-]+)\.(md|pdf|html)", c)
    if f:
        return "the " + f.group(1).replace("_", " ").replace("-", " ").lower()
    if re.fullmatch(r"(?:[\w.-]+/)*[\w-]+\.(py|sh|cpp|js|yml)", c):
        return "the repository's code"
    if re.fullmatch(r"(?:[\w.-]+/)*[\w-]+\.(json|csv|txt)", c):
        return "the record"
    return ""


def _plain(md: str) -> str:
    s = " ".join(md.split())
    s = _strip_parens(s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"\1", s)
    s = re.sub(r"(?<![\w*])\*([^*]+)\*(?![\w*])", r"\1", s)
    s = re.sub(r",?\s*`#[^`]*`", "", s)                                   # an anchor is for the eye
    s = re.sub(r"\s+(?:of|in) the page's (?:section|appendix) \w+,(?=\s)", "", s)
    s = re.sub(r"`([^`]*)`", _code, s)
    s = re.sub(r"\b(own|its|their) the (record|repository's code)\b", r"\1 \2", s)   # "the run's own the record" (6 November)
    s = re.sub(r"\bthe record the record\b", "the record", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"\s+([,.;:])", r"\1", s)
    s = re.sub(r",\s*,", ",", s)
    return re.sub(r"\s{2,}", " ", s).strip()


def _cut(s: str, cap: int = CAP) -> str:
    if s.endswith(":"):
        s = re.sub(r"(?<=[.!?])\s+[^.!?]*:$", "", s)
    if len(s) <= cap:
        return s
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"'“(])", s)
    out = ""
    for p in parts:
        if out and len(out) + 1 + len(p) > cap:
            break
        out = (out + " " + p).strip()
    return out if out else s[:cap].rsplit(" ", 1)[0] + "."


def spoken(text: str) -> str:
    """The same words as the ear needs them: units, symbols and the engine's name said in full. Only the voice reads this;
    the card shows the text as written."""
    s = text
    s = re.sub(r"\bomni-v(\d+)\b", r"omni version \1", s)
    s = re.sub(r"(\d)\s?s\b", r"\1 seconds", s)
    s = re.sub(r"(\d)\s?ms\b", r"\1 milliseconds", s)
    s = s.replace("1 seconds", "1 second") if re.search(r"(?<!\d)1 seconds", s) else s
    for a, b in (("Δ", "delta "), ("−", " minus "), ("≤", " at most "), ("≥", " at least "), ("×", " times "), (" / ", " over "),
                 (" = ", " equals "), ("→", " to "), ("←", " from "), ("±", " plus or minus "), ("·", ","),
                 ("©", "Copyright"), ("www.omni-compass.com", "omni-compass dot com"), ("LLC", "L L C"), ("USA", "U S A"), (".md", ""),
                 ("e.g.", "for example"), ("i.e.", "that is"), ("&", " and ")):
        s = s.replace(a, b)
    s = re.sub(r"(?<=[A-Za-z])/(?=[A-Za-z])", ", ", s)
    return re.sub(r"\s{2,}", " ", s).strip()


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _chapters(manual: str) -> dict:
    lines, out = manual.splitlines(), {}
    starts = [(i, m) for i, l in enumerate(lines) if (m := CHAPTER.match(l))]
    for k, (i, m) in enumerate(starts):
        end = starts[k + 1][0] if k + 1 < len(starts) else len(lines)
        body = [lines[i][m.end():].lstrip(" .")] + lines[i + 1:end]
        cut = next((j for j, l in enumerate(body) if l.startswith("## ") or l.startswith("# ")), len(body))
        pars, cur = [], []
        for l in body[:cut] + [""]:
            if not l.strip():
                if cur:
                    pars.append(" ".join(cur))
                cur = []
                continue
            if l.startswith(("###", "|", "!", "```", "- ", "* ", "1. ", ">")) or l.startswith("<"):
                if cur:
                    pars.append(" ".join(cur))
                cur = []
                continue
            cur.append(l.strip())
        text = ""
        for p in pars:
            p = _plain(p)
            p = re.sub(r"(?:^|(?<=[.!?] ))This (?:book|manual) [^.]*\.\s*", "", p).strip()   # the tour shows the page, never "this book"
            if len(p) < 40:
                continue
            text = (text + " " + p).strip()
            if len(text) >= 300:
                break
        label = m.group(1).replace("**", "")
        out[m.group(3)] = {"label": label[0].upper() + label[1:], "title": (m.group(2) or label).strip(), "text": _cut(text)}
    return out


def _controls(page: str) -> dict:
    out = {}
    for m in re.finditer(SECTION, page):
        nxt = page.find("<section ", m.end()); scr = page.find("<script", m.end())   # the last section ends where the scripts begin
        nxt = min(x for x in (nxt, scr, len(page)) if x > 0)
        seg = page[m.end(): nxt]
        k = re.search(r'<div class="secknobs"[^>]*>(.*?)</div>', seg, re.S)
        text = ""
        if k:
            text = html.unescape(re.sub(r"<[^>]+>", "", k.group(1)))
            text = re.sub(r"^\s*Controls\.\s*", "", " ".join(text.split()))
            text = re.sub(r"\s*\([^()]*(?:\.json|\.py|\.md|POST|--)[^()]*\)", "", text)
        out[m.group(1)] = _cut(_plain(text), 320)
    return out


def steps(manual: str | None = None, page: str | None = None) -> list:
    """Every stop of the tour, in the page's order: the opening, each section the page carries, the close."""
    manual = MANUAL.read_text(encoding="utf-8") if manual is None else manual
    page = PAGE.read_text(encoding="utf-8") if page is None else page
    ch, ctl = _chapters(manual), _controls(page)
    out = [{"id": "intro", "label": "Guided tour", "title": "How the tour works", "text": OPEN, "controls": "", "notice": PLAIN}]
    hero = _hero(ch)
    if hero and 'id="heroRow"' in page:
        out.append(hero)
    for sid in ctl:
        c = ch.get(sid)
        if not c or not c["text"]:
            continue
        out.append({"id": sid, "label": c["label"], "title": c["title"], "text": c["text"], "controls": ctl[sid], "notice": ""})
    out.append({"id": "end", "label": "Guided tour", "title": "End of the tour", "text": CLOSE, "controls": "", "notice": PLAIN})
    for s in out:
        say = f"{s['label']}. {s['title']}. {s['text']}"
        if s["controls"]:
            say += f" Controls. {s['controls']}"   # the page's own label for the line (6 November: never "What you can do here:" before recorded data)
        if s["notice"]:
            say += " " + s["notice"]
        s["say"] = spoken(say)
        s["sha"] = sha(s["say"])
    return out


def _hero(ch: dict) -> dict | None:
    """The result first (the editor seat of 6 November: the tour skipped the row under the notice and never spoke the figure of
    record): the Omni index row of results/BENEFIT_SHEET.json, the row #heroRow and section 2a read from the record fleet, in the
    hero row's own words; its word by the row's own reading and its size rounded as the page rounds it, so the voice never says
    a number the record does not carry. A new index makes new words, and tools/tour_voice.py reads the stop again."""
    try:
        rows = json.loads(BENEFIT.read_text(encoding="utf-8")).get("rows", [])
    except (OSError, ValueError):
        return None
    ox = next((r for r in rows if "Omni index" in str(r.get("benchmark") or "")), None)
    if not ox or not isinstance(ox.get("pct"), (int, float)):
        return None
    w = str(ox.get("benefit") or "")
    word = ("GAIN" if w.startswith("GAIN") else "LOSS" if w.startswith("LOSS") else "the runs disagree" if "disagree" in w
            else "power given" if w.startswith("power given") else "STEADY")
    size = Decimal(abs(ox["pct"])).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)   # Math.abs(pct).toFixed(1), as the row prints it
    loss, eng = int(ox.get("loss") or 0), str(ox.get("engine") or "").split(" (")[0]
    reg = ch.get("s-loss") or {}
    where = f"{reg.get('label', 'Section 2d').lower()}, the {reg.get('title', 'LOSS Register')}"
    text = (f"Under the notice the page gives its result first: the figure of record, the Omni index, every real test together, "
            f"Omni-Compass on native against native alone, read from each real test's newest three-run table on {eng} (runs A, B "
            f"and C on GitHub's own machines, class L). It reads {word} {size}%. "
            + (f"Its tables hold {loss} LOSS row{'' if loss == 1 else 's'}, and every one is shown in {where}. " if loss else
               "Its tables hold no LOSS row. ")
            + "Every other aggregate on the page is a second reading.")
    return {"id": "heroRow", "label": "The result first", "title": "The Figure of Record", "text": text, "controls": "", "notice": ""}


def check(page: str | None = None) -> list:
    """Every stop that quotes the page quotes words the page still carries (the editor seat of 6 November: the 2a stop quoted a
    dock line the page had dropped): each quotation of twelve characters or more in a stop's words, against the page's text."""
    page = PAGE.read_text(encoding="utf-8") if page is None else page
    norm = lambda t: re.sub(r"\s+([,.;:)])", r"\1", " ".join(t.split())).lower()
    shown = re.sub(r'<script type="application/json" id="tour">.*?</script>', " ", page, flags=re.S)   # never the tour's own record
    flat = norm(html.unescape(re.sub(r"<[^>]+>", " ", shown)))
    bad = []
    for s in steps(page=page):
        for q in re.findall('[\u201c"]([^\u201d"]{12,})[\u201d"]', s["text"]):
            if norm(q) not in flat:
                bad.append((s["id"], q))
    return bad


def nav() -> dict:
    """The line the card reads between two stops (5 November: the founder's words, "when Section 1 is done you need to ... tell
    them ... hit the button for a question ... hit the other button to continue"), one recorded clip shared by every stop."""
    say = spoken(NAV)
    return {"id": "nav", "label": "Guided tour", "title": "Between the stops", "text": NAV, "controls": "", "notice": "",
            "say": say, "sha": sha(say)}


if __name__ == "__main__":
    if "--check" in sys.argv:
        bad = check()
        for sid, q in bad:
            print(f"[{sid}] quotes words the page no longer carries: \u201c{q}\u201d")
        print("every quotation in the tour is on the page" if not bad else f"{len(bad)} quotation(s) the page no longer carries")
        sys.exit(1 if bad else 0)
    for s in steps():
        print(f"[{s['id']}] {s['label']} — {s['title']} ({len(s['say'])} chars)\n  {s['say']}\n")
