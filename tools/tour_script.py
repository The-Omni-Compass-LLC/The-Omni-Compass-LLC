#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The live engine's guided tour, written once: one stop for every section of the page, in the page's own order, each in the
words the Live Engine Manual already prints for that section (the chapter that names the section's anchor), with the section's
own controls line from the page. Nothing in the tour is written for the tour alone but its opening and its close, which carry
the legal notice. The page builder (docs/engine/build_live_engine.py, the record `tour`) and the voice (tools/tour_voice.py,
the recorded clips) both read these steps, so the voice never says what the page and the manual do not.

    python3 tools/tour_script.py          prints every stop as it will be shown and spoken
"""
from __future__ import annotations

import hashlib
import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MANUAL = ROOT / "docs" / "OMNI_COMPASS_LIVE_ENGINE_MANUAL.md"
PAGE = ROOT / "docs" / "engine" / "OMNI_COMPASS_LIVE_ENGINE.html"
sys.path.insert(0, str(ROOT / "tools"))
from legal import PLAIN  # noqa: E402  (the notice, written once)

CAP = 640           # the most characters a stop reads from its chapter, cut at a sentence: about 40 seconds of speech
CHAPTER = re.compile(r"^This chapter reads the page's (section [0-9]+[a-z]?|appendix [A-Z]|\*\*Contents\*\*)[, ]*(?:\*\*([^*]+)\*\*)? ?\(`#([a-z0-9-]+)`\)")
OPEN = ("Welcome to the guided tour of the Omni-Compass Live Engine. The tour walks the page from top to bottom, one section at "
        "a time, from the monitor wall to the glossary at the back. At each stop the section is outlined and scrolled into view, "
        "and this card says what the section shows in the words of the Live Engine Manual and names what you can do there; the "
        "buttons under Try these flash the real controls on the page. The line under the title always says what is happening and "
        "what to press. Play and Pause start and hold the voice; back ten seconds, forward ten seconds and From the start hear it "
        "again; Stop silences it and stays on this stop. Previous stop and Next stop move through the tour, and while Step on by "
        "itself is on, the next stop follows when this one ends. Press any sentence to hear it again from there. Where a browser "
        "plays sound only after a press, the Play button lights up: press it, and the voice starts where the card is reading. "
        "Where no voice can play, the card reads along by itself at the voice's pace. Close, or the Escape key, ends the tour; "
        "the Tour button starts it again where you are.")
CLOSE = ("That is the whole page. Every number on it is computed from the engine's own code or read from the repository's "
         "records, and every reading carries its word, GAIN, STEADY or LOSS, by what its gauge is for. The three manuals, the "
         "Live Engine Manual first, open from the control panel.")


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
    for m in re.finditer(r'<section class="stack[^"]*" id="([a-z0-9-]+)"', page):
        nxt = page.find("<section ", m.end())
        seg = page[m.end(): nxt if nxt > 0 else len(page)]
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
    for sid in ctl:
        c = ch.get(sid)
        if not c or not c["text"]:
            continue
        out.append({"id": sid, "label": c["label"], "title": c["title"], "text": c["text"], "controls": ctl[sid], "notice": ""})
    out.append({"id": "end", "label": "Guided tour", "title": "End of the tour", "text": CLOSE, "controls": "", "notice": PLAIN})
    for s in out:
        say = f"{s['label']}. {s['title']}. {s['text']}"
        if s["controls"]:
            say += f" What you can do here: {s['controls']}"
        if s["notice"]:
            say += " " + s["notice"]
        s["say"] = spoken(say)
        s["sha"] = sha(s["say"])
    return out


if __name__ == "__main__":
    for s in steps():
        print(f"[{s['id']}] {s['label']} — {s['title']} ({len(s['say'])} chars)\n  {s['say']}\n")
