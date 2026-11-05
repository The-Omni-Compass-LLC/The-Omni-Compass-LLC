#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The film, YIELD LIMIT LINE: one screenplay and one production file, compiled into everything a studio reader, a
production office and a text-to-video or image-to-video tool takes (the founder's words of 4 November 2026: scripts that
"any production company ... would have read ... and could see and understand the whole movie", fed "into ... Sora ... any
AI video and all the apps that exist").

Sources (written by hand):
  docs/film/YIELD_LIMIT_LINE.fountain   the screenplay, in Fountain (fountain.io), the open plain-text screenplay format
  docs/film/production.json             characters, props, places, look, every shot, every number the film speaks
  docs/film/STORY_BIBLE.md              the book of the film: logline, world, people, structure, the whole movie

Outputs (written by this file):
  docs/film/YIELD_LIMIT_LINE.pdf        the screenplay on the industry's page: 12-point monospace (Liberation Mono, the
                                        Courier metric), 1.5-inch left margin, one page about one minute, scene numbers
  docs/film/YIELD_LIMIT_LINE_BOOK.pdf   the book: the story bible, then the screenplay
  docs/film/YIELD_LIMIT_LINE.fdx        the same screenplay for Final Draft
  docs/film/SHOT_LIST.csv               every shot: scene, length, framing, lens, action, words, sound, each tool's clip length
  docs/film/PROMPTS.json, PROMPTS.md    every shot's self-contained prompt (motion) and start-frame prompt (still)
  docs/film/REFERENCE_SHEETS.md         image prompts for every character, prop and place, made first, for continuity
  docs/film/cards/*.svg                 title, receipt, fiction and notice cards (the receipt card read from
                                        results/SITE_NUMBERS.json)
  docs/film/overlays/*.svg              every word the audience reads on a screen, phone, slide or sign, composited in the
                                        edit, because video models cannot write legible text

The check (python3 tools/film.py --check, run by verify.py) fails when an output is not what the sources give; a
production scene is not a scene of the screenplay; a shot's words are not the screenplay's words, or a line of the
screenplay has no shot; a shot names a character, prop, place or light that is not declared; or a number the audience
reads or hears is not declared: as the story's own (a time, a road, a setting), as a claim the story refuses (the fictional
vendor's slide, a modelled figure), or as a receipt, whose value is read again from its record here (the pages a person
would be sent, results/OVERSIGHT_PAGES.json by tools/pages.py; the end card by results/SITE_NUMBERS.json).
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import re
import sys
import textwrap
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
FILM = ROOT / "docs" / "film"
SRC, PROD, BIBLE = FILM / "YIELD_LIMIT_LINE.fountain", FILM / "production.json", FILM / "STORY_BIBLE.md"
PDF, BOOK, FDX = FILM / "YIELD_LIMIT_LINE.pdf", FILM / "YIELD_LIMIT_LINE_BOOK.pdf", FILM / "YIELD_LIMIT_LINE.fdx"
CSV, PJSON, PMD, REFS = FILM / "SHOT_LIST.csv", FILM / "PROMPTS.json", FILM / "PROMPTS.md", FILM / "REFERENCE_SHEETS.md"
SCENES_MD = FILM / "SCENES.md"
CARDS, OVERLAYS = FILM / "cards", FILM / "overlays"
SITE = ROOT / "results" / "SITE_NUMBERS.json"
PAGES_REC = ROOT / "results" / "OVERSIGHT_PAGES.json"

NOTICE = ("© 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only. Any commercial use, "
          "commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass "
          "requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and "
          "printout carries this notice with LICENSE, NOTICE and DISCLOSURES.md. All patents, copyrights and trademarks filed "
          "in the USA. www.omni-compass.com")
SHORT = ("© 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or "
         "monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed "
         "in the USA. www.omni-compass.com")
SIZES = {"EWS": "extreme wide shot", "WS": "wide shot", "MS": "medium shot", "MCU": "medium close-up", "CU": "close-up",
         "ECU": "extreme close-up", "INSERT": "insert close-up", "OTS": "over-the-shoulder shot", "TWO": "two-shot"}
LENGTHS = (4, 5, 6, 8, 9, 10, 12)


# ---------------------------------------------------------------- Fountain

SCENE_RE = re.compile(r"^(INT|EXT|EST|INT\./EXT|INT/EXT|I/E)[ .]", re.I)


def plain(s: str) -> str:
    """The text without Fountain's emphasis marks."""
    return re.sub(r"(\*\*|\*|_)(.+?)\1", r"\2", s)


def _cue(s: str) -> bool:
    if s.startswith("@"):
        return True
    base = re.sub(r"\(.*?\)", "", s).strip().rstrip("^").strip()
    return bool(re.search(r"[A-Z]", base)) and base == base.upper() and not base.endswith(":") and not s.startswith(">")


def _classify(p: list[str]) -> list[tuple]:
    first = p[0].strip()
    if first == "===":
        return [("page_break", "")]
    if first.startswith(".") and not first.startswith(".."):
        return [("scene", first[1:].strip())] + ([("action", "\n".join(p[1:]))] if p[1:] else [])
    if SCENE_RE.match(first):
        return [("scene", first)] + ([("action", "\n".join(p[1:]))] if p[1:] else [])
    if all(x.strip().startswith(">") and x.strip().endswith("<") for x in p):
        return [("centered", x.strip()[1:-1].strip()) for x in p]
    if len(p) == 1 and first.startswith(">"):
        return [("transition", first[1:].strip())]
    if len(p) == 1 and first == first.upper() and first.endswith("TO:"):
        return [("transition", first)]
    if len(p) >= 2 and _cue(first):
        out, dl = [("character", first.lstrip("@").strip())], []
        for x in p[1:]:
            s = x.strip()
            if s.startswith("(") and s.endswith(")"):
                if dl:
                    out.append(("dialogue", " ".join(dl)))
                    dl = []
                out.append(("parenthetical", s))
            else:
                dl.append(s)
        if dl:
            out.append(("dialogue", " ".join(dl)))
        return out
    return [("action", "\n".join(x.lstrip("!") for x in p))]


def parse(text: str) -> tuple[dict, list[tuple]]:
    """The title page (lower-case keys, lists of lines) and the body's elements (kind, text), in order."""
    body = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    body = re.sub(r"\[\[.*?\]\]", "", body, flags=re.S)
    lines, title, i = body.split("\n"), {}, 0
    if lines and re.match(r"^[A-Za-z][A-Za-z ]*:", lines[0]):
        key = None
        while i < len(lines) and lines[i].strip():
            ln = lines[i]
            m = re.match(r"^([A-Za-z][A-Za-z ]*):\s*(.*)$", ln)
            if m and not ln[:1].isspace():
                key = m.group(1).strip().lower()
                title[key] = [m.group(2).strip()] if m.group(2).strip() else []
            elif key:
                title[key].append(ln.strip())
            i += 1
    els, para = [], []
    for ln in lines[i:]:
        if ln.strip():
            para.append(ln.rstrip())
        elif para:
            els += _classify(para)
            para = []
    if para:
        els += _classify(para)
    return title, els


def blocks(els: list[tuple]) -> list[tuple[str, str]]:
    """Every dialogue block, (character's name without its extension, the words), in order."""
    out, who = [], None
    for k, t in els:
        if k == "character":
            who = re.sub(r"\(.*?\)", "", t).strip().rstrip("^").strip()
        elif k == "dialogue" and who:
            out.append((who, t))
        elif k not in ("parenthetical",):
            who = None
    return out


def norm(s: str) -> str:
    s = plain(s).replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()


# ---------------------------------------------------------------- the records the film's numbers are read from

NUMWORDS = ("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen "
            "eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety").split()
NW = "|".join(sorted(NUMWORDS, key=len, reverse=True))
SCAN = [re.compile(r"\d"), re.compile(rf"\b(?:{NW})(?:-(?:{NW}))?\s+point\s+\w+", re.I),
        re.compile(rf"\b(?:{NW})(?:-(?:{NW}))?\s+percent\b", re.I), re.compile(r"\ba quarter\b|\bhalf (?:the|of|as)\b|\bby half\b", re.I),
        re.compile(rf"\b(?:{NW})\s+(?:Kubernetes\s+)?(?:runs?|tests?|times)\b", re.I)]


def words_number(s: str) -> float | None:
    """'thirteen point eight' gives 13.8, 'thirteen Kubernetes tests' 13, 'run three times' 3."""
    val = {w: i for i, w in enumerate(NUMWORDS[:20])} | {w: 10 * (i + 2) for i, w in enumerate(NUMWORDS[20:])}
    toks = re.findall(r"[a-z]+", s.lower().replace("-", " "))
    nums = [t for t in toks if t in val or t == "point"]
    if not nums:
        return None
    if "point" in nums:
        k = nums.index("point")
        whole = sum(val[t] for t in nums[:k])
        frac = "".join(str(val[t]) for t in nums[k + 1:])
        return float(f"{whole}.{frac}") if frac else float(whole)
    return float(sum(val[t] for t in nums))


def receipts() -> dict:
    """The pages a person would be sent, read again from their record by the pages tool's own reading."""
    sys.path.insert(0, str(ROOT / "tools"))
    import pages as P  # noqa: E402
    rec = json.loads(PAGES_REC.read_text(encoding="utf-8"))
    r = P.reading(rec, P.PRIMARY)
    pooled = r["pooled"]
    nat = sum(p["native"] for p in pooled) / len(pooled)
    omn = sum(p["omni"] for p in pooled) / len(pooled)
    return {"pages_native": nat, "pages_omni": omn, "pages_change": 100 * (omn / nat - 1), "pages_tests": len(rec["tests"]),
            "pages_runs": min(len(t["runs"]) for t in rec["tests"]), "pages_engine": rec["engine"],
            "reading": norm(r["reading"].replace("**", ""))}


def check_receipt(n: dict, R: dict) -> str | None:
    """None when the declared text says what its record says; else why not."""
    c, t = n.get("check"), n["text"]
    all3 = "in all three of our runs" in R["reading"]
    if c == "pages_native":
        v = words_number(t)
        return None if v is not None and abs(v - round(R["pages_native"], 1)) < 1e-9 else f"{t!r} against {R['pages_native']:.2f}"
    if c == "pages_omni":
        v = words_number(t)
        return None if v is not None and abs(v - round(R["pages_omni"], 1)) < 1e-9 else f"{t!r} against {R['pages_omni']:.2f}"
    if c == "pages_change":
        return None if t == f"{abs(R['pages_change']):.1f}%" and R["pages_change"] < 0 else f"{t!r} against {R['pages_change']:.1f}%"
    if c == "pages_quarter":
        x = -R["pages_change"]
        return None if 22.5 <= x <= 27.5 and all3 else f"{t!r} against down {x:.1f}% ({R['reading']})"
    if c == "pages_tests":
        return None if words_number(t) == R["pages_tests"] else f"{t!r} against {R['pages_tests']} tests"
    if c == "pages_runs":
        return None if words_number(t) == R["pages_runs"] == 3 and all3 else f"{t!r} against {R['pages_runs']} runs ({R['reading']})"
    if c == "pages_engine":
        return None if t == f"omni-v{R['pages_engine']}" else f"{t!r} against omni-v{R['pages_engine']}"
    return f"{t!r}: no such check {c!r}"


def site_pages() -> dict:
    d = json.loads(SITE.read_text(encoding="utf-8"))
    return next(n for n in d["show"] if n["id"] == "pages")


# ---------------------------------------------------------------- what the audience reads and hears, and the checks

def seen_texts(els: list[tuple], P: dict) -> list[tuple[str, str]]:
    out = [(f"screenplay {k}", plain(t)) for k, t in els if k in ("scene", "action", "dialogue", "centered", "transition",
                                                                   "parenthetical")]
    out += [(f"overlay {s['id']}", s["txt"]["text"]) for s in P["shots"] if s.get("txt")]
    for c in P["cards"]:
        out += [(f"card {c['id']}", x) for x in card_lines(c)]
    return out


def number_problems(els: list[tuple], P: dict) -> list[str]:
    bad, used = [], set()
    decl = sorted(P["numbers"], key=lambda n: -len(n["text"]))
    R = receipts()
    for n in decl:
        if n["kind"] not in ("story", "claim_refused", "receipt"):
            bad.append(f"number {n['text']!r}: kind {n['kind']!r} is not story, claim_refused or receipt")
        if n["kind"] == "receipt":
            why = check_receipt(n, R)
            if why:
                bad.append(f"the receipt {n['text']!r} does not say what its record says: {why}")
    for where, text in seen_texts(els, P):
        masked = re.sub(r"\(\d{1,3}\)", " ", text)                      # a character's age where the character enters
        for n in decl:
            pat = re.compile(re.escape(n["text"]), re.I)
            if pat.search(masked):
                used.add(n["text"].lower())
                masked = pat.sub(" ", masked)
        for rx in SCAN:
            for m in rx.finditer(masked):
                ctx = masked[max(0, m.start() - 20): m.end() + 20].strip()
                bad.append(f"{where}: a number with no declaration ({m.group(0)!r} in ...{ctx}...)")
    for n in decl:
        if n["text"].lower() not in used:
            bad.append(f"number {n['text']!r} is declared but the film never says or shows it")
    return sorted(set(bad))


def problems(P: dict, title: dict, els: list[tuple]) -> list[str]:
    bad = []
    heads = [plain(t) for k, t in els if k == "scene"]
    for sc in P["scenes"]:
        if sc["heading"] not in heads:
            bad.append(f"scene {sc['n']}: {sc['heading']!r} is not a scene heading of the screenplay")
    scn = {s["n"] for s in P["scenes"]}
    chars, locs, props, pal = P["characters"], P["locations"], P["props"], P["style"]["palettes"]
    ids = set()
    for s in P["shots"]:
        sid = s["id"]
        if sid in ids:
            bad.append(f"shot {sid} appears twice")
        ids.add(sid)
        if not re.fullmatch(rf"{s['sc']:02d}-\d\d", sid):
            bad.append(f"shot {sid}: its number does not name its scene {s['sc']}")
        if s["sc"] not in scn:
            bad.append(f"shot {sid}: scene {s['sc']} is not declared")
        if s["s"] not in LENGTHS:
            bad.append(f"shot {sid}: {s['s']} s is not a clip length any tool makes ({LENGTHS})")
        if s["size"] not in SIZES:
            bad.append(f"shot {sid}: framing {s['size']!r} unknown")
        for w in s.get("who", []):
            if w not in chars:
                bad.append(f"shot {sid}: character {w!r} undeclared")
        for p in s.get("props", []):
            if p not in props:
                bad.append(f"shot {sid}: prop {p!r} undeclared")
        if s["at"] not in locs:
            bad.append(f"shot {sid}: place {s['at']!r} undeclared")
        if s["lt"] not in pal:
            bad.append(f"shot {sid}: light {s['lt']!r} undeclared")
    bl = blocks(els)
    said = {}
    for s in P["shots"]:
        for ln in s.get("say", []):
            if ln["who"] not in chars:
                bad.append(f"shot {s['id']}: speaker {ln['who']!r} undeclared")
                continue
            name = chars[ln["who"]]["name"]
            said.setdefault(name, []).append(norm(ln["line"]))
            if not any(norm(ln["line"]) in norm(t) for w, t in bl if w == name):
                bad.append(f"shot {s['id']}: {name} says {ln['line']!r}, which is not the screenplay's line")
    for w, t in bl:
        if norm(t) not in " ".join(said.get(w, [])):
            bad.append(f"the screenplay's line {w}: {t[:60]!r} has no shot that speaks it")
    for c in P["cards"]:
        if c.get("after") and c["after"] not in ids and c["after"] not in {x["id"] for x in P["cards"]}:
            bad.append(f"card {c['id']}: placed after {c['after']!r}, which is no shot or card")
    sp = site_pages()
    want = re.sub(r" \(omni-v\d+\)\.$", ".", sp["sentence"])
    cent = [plain(t) for k, t in els if k == "centered"]
    if want not in cent:
        bad.append(f"the end card must read the website's own sentence, {want!r} (results/SITE_NUMBERS.json)")
    decl = {n["text"].lower() for n in P["numbers"]}
    for m in re.finditer(r"\d+(?:\.\d+)?%", BIBLE.read_text(encoding="utf-8") if BIBLE.exists() else ""):
        if m.group(0).lower() not in decl:
            bad.append(f"docs/film/STORY_BIBLE.md: {m.group(0)} is not a number the production file declares")
    if "copyright" not in title or "www.omni-compass.com" not in " ".join(title.get("copyright", [])):
        bad.append("the title page carries no notice")
    return bad + number_problems(els, P)


# ---------------------------------------------------------------- prompts

def tool_lengths(s: int, P: dict) -> dict:
    out = {}
    for k, t in P["tools"].items():
        if k.startswith("_"):
            continue
        ok = [x for x in t["seconds"] if x >= s]
        out[k] = str(min(ok)) if ok else f"{max(t['seconds'])}+{s - max(t['seconds'])} (extend)"
    return out


def _cap(s: str) -> str:
    return s[:1].upper() + s[1:]


OFF = ("off-screen", "voice-over", "through the phone")


def offscreen(s: dict, w: str) -> bool:
    """A character heard and not seen in this shot: every line of theirs in it is off-screen, a voice-over or a phone."""
    lines = [x for x in s.get("say", []) if x["who"] == w]
    return bool(lines) and all(any(o in x["how"] for o in OFF) for x in lines)


def cast_lines(s: dict, P: dict) -> list[str]:
    out = []
    for w in s.get("who", []):
        c = P["characters"][w]
        if c["look"] == "unseen" or offscreen(s, w):
            continue
        out.append(f"{c['full'].split(chr(34))[1] if chr(34) in c['full'] else c['full'].split()[0]}: {c['look']}; wearing {c['wear']}.")
    return out


def prompt(s: dict, P: dict) -> str:
    st = P["style"]
    parts = [st["base"] + ".", _cap(st["palettes"][s["lt"]]) + ".",
             f"{_cap(SIZES[s['size']])}, {s['ang']} angle, {s['mv']}, {s['lens']} lens.",
             "Setting: " + P["locations"][s["at"]]["look"] + "."]
    parts += cast_lines(s, P)
    parts += ["Prop: " + P["props"][p] + "." for p in s.get("props", [])]
    parts.append(s["do"])
    if set(s.get("props", [])) & {"wall", "board"} or "light" in s["do"].lower() and s["at"] in ("data_hall", "wall"):
        parts.append(_cap(st["signs"]) + ".")
    for ln in s.get("say", []):
        c = P["characters"][ln["who"]]
        who = "A radio voice" if ln["who"] == "radio" else (c["full"].split(chr(34))[1] if chr(34) in c["full"] else c["full"].split()[0])
        parts.append(f'Off-screen, the voice of {who} ({ln["how"]}): "{ln["line"]}"' if offscreen(s, ln["who"])
                     else f'{who} ({ln["how"]}): "{ln["line"]}"')
    parts.append("Sound: " + s["snd"] + ".")
    parts.append("Screens, phones, signs and paper show no legible text; every word on screen is added in the edit.")
    return " ".join(parts)


def still(s: dict, P: dict) -> str:
    st = P["style"]
    parts = [st["base"] + ".", _cap(st["palettes"][s["lt"]]) + ".", f"Still frame, {SIZES[s['size']]}, {s['ang']} angle, "
             f"{s['lens']} lens.", "Setting: " + P["locations"][s["at"]]["look"] + "."]
    parts += cast_lines(s, P)
    parts += ["Prop: " + P["props"][p] + "." for p in s.get("props", [])]
    parts += [s["do"], "No legible text anywhere in the frame."]
    return " ".join(parts)


def heading_of(n: int, P: dict) -> str:
    return next(x["heading"] for x in P["scenes"] if x["n"] == n)


def prompt_pack(P: dict) -> dict:
    neg = ", ".join(P["style"]["negative"])
    shots = []
    for s in P["shots"]:
        refs = [f"characters/{w}" for w in s.get("who", []) if P["characters"][w]["look"] != "unseen" and not offscreen(s, w)]
        refs += [f"props/{p}" for p in s.get("props", [])] + [f"places/{s['at']}"]
        shots.append({"id": s["id"], "scene": s["sc"], "heading": heading_of(s["sc"], P), "seconds": s["s"],
                      "generate_seconds": tool_lengths(s["s"], P), "prompt": prompt(s, P), "start_frame": still(s, P),
                      "negative": neg, "dialogue": [{"speaker": P["characters"][x["who"]]["name"], "line": x["line"],
                                                     "delivery": x["how"]} for x in s.get("say", [])],
                      "sound": s["snd"], "overlay": f"overlays/{s['id']}.svg" if s.get("txt") else None,
                      "reference_images": refs})
    return {"notice": NOTICE, "title": P["title"], "source": "tools/film.py (docs/film/production.json, "
            "docs/film/YIELD_LIMIT_LINE.fountain)", "format": P["format"], "tools": P["tools"],
            "how_to_use": ["Make the reference images first (REFERENCE_SHEETS.md) and keep them: every character, prop and "
                           "place, one image each, used as the start frame or reference in every shot that names it.",
                           "For a tool that takes a start image, make the shot's start_frame still from its references, "
                           "then the motion from prompt; for a tool that takes text only, use prompt.",
                           "Generate at the tool's own clip length (generate_seconds) and trim to seconds in the edit.",
                           "Tools that make sound take the dialogue inside the prompt; for tools that do not, record the "
                           "dialogue (speaker, line, delivery) and lay it in the edit.",
                           "Every word the audience reads is an overlay (overlays/), every card is in cards/: no video model "
                           "is asked to write text.",
                           "Every number spoken or shown is declared in production.json and checked by tools/film.py: the "
                           "story's own, a claim the story refuses, or a receipt read again from its record."],
            "runtime_seconds": sum(s["s"] for s in P["shots"]) + sum(c["s"] for c in P["cards"]),
            "shots": shots, "notice_end": NOTICE}


def prompts_md(pack: dict, P: dict) -> str:
    L = [f"# {P['title']}: The Prompt Pack", "",
         "Written by `tools/film.py` from `docs/film/production.json` and the screenplay; `PROMPTS.json` is the same for "
         "a program. Every shot carries a self-contained prompt for a text-to-video tool and a start-frame prompt for an "
         "image tool, so a shot can be made alone, in any order, by any tool.", "", "## How to use it", ""]
    L += [f"{i}. {x}" for i, x in enumerate(pack["how_to_use"], 1)]
    L += ["", "## Each tool's clip lengths", "", "| Tool | Clip lengths (s) | Sound | Start image |", "|---|---|---|---|"]
    for k, t in P["tools"].items():
        if not k.startswith("_"):
            L.append(f"| {t['name']} | {', '.join(map(str, t['seconds']))} | {'yes' if t['audio'] else 'no'} | "
                     f"{'yes' if t['image_to_video'] else 'no'} |")
    L += ["", P["tools"]["_note"], "", f"Runtime: {pack['runtime_seconds'] // 60} min {pack['runtime_seconds'] % 60} s in "
          f"{len(pack['shots'])} shots and {len(P['cards'])} cards.", "", "Avoid, in every shot: " + pack["shots"][0]["negative"] + "."]
    cur = None
    for s in pack["shots"]:
        if s["scene"] != cur:
            cur = s["scene"]
            L += ["", f"## Scene {cur}: {s['heading']}"]
        gen = ", ".join(f"{P['tools'][k]['name']} {v}" for k, v in s["generate_seconds"].items())
        L += ["", f"### Shot {s['id']} · {s['seconds']} s", "", f"Generate: {gen}." +
              (f" Overlay: `{s['overlay']}`." if s["overlay"] else ""), "", "Prompt:", "", "```text", s["prompt"], "```", "",
              "Start frame:", "", "```text", s["start_frame"], "```"]
    return "\n".join(L) + "\n"


def refs_md(P: dict) -> str:
    st = P["style"]
    L = [f"# {P['title']}: Reference Sheets", "",
         "Make these images first, with any image tool, and keep them. Every shot that names a character, a prop or a place "
         "uses its image as the start frame or the reference, so a face, a coupon or a room looks the same in shot 158 as in "
         "shot 1. Written by `tools/film.py` from `docs/film/production.json`.", "", "## The characters", ""]
    for k, c in P["characters"].items():
        if c["look"] == "unseen":
            continue
        L += [f"### {c['full']} (`characters/{k}`)", "", "```text",
              f"Character reference sheet, photoreal: {c['look']}, wearing {c['wear']}. Full-body front view, three-quarter "
              "view and profile, and one close-up portrait, on a neutral grey studio background, soft even light, natural skin "
              "texture. No text, no logos.", "```", "", f"Voice: {c['voice']}.", ""]
    L += ["## The props", ""]
    for k, p in P["props"].items():
        L += [f"### `props/{k}`", "", "```text", f"Prop reference, photoreal: {p}. Three angles on a neutral grey background, "
              "soft even light. No text, no logos.", "```", ""]
    L += ["## The places", ""]
    for k, x in P["locations"].items():
        L += [f"### `places/{k}`", "", "```text", f"Establishing still, photoreal, 16:9: {x['look']}. {st['base']}. No people, "
              "no text, no logos.", "```", ""]
    L += ["## The look", "", f"Base: {st['base']}.", "", "Light, by name:", ""]
    L += [f"- `{k}`: {v}." for k, v in st["palettes"].items()]
    L += ["", f"Signs: {st['signs']}.", ""]
    return "\n".join(L) + "\n"


def shot_csv(P: dict) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    tools = [k for k in P["tools"] if not k.startswith("_")]
    w.writerow([NOTICE])
    w.writerow(["shot", "scene", "heading", "seconds", "framing", "angle", "movement", "lens", "characters", "place", "light",
                "action", "dialogue", "sound", "overlay"] + [P["tools"][k]["name"] for k in tools])
    for s in P["shots"]:
        say = " / ".join(f"{P['characters'][x['who']]['name']}: {x['line']}" for x in s.get("say", []))
        gl = tool_lengths(s["s"], P)
        w.writerow([s["id"], s["sc"], heading_of(s["sc"], P), s["s"], SIZES[s["size"]], s["ang"], s["mv"], s["lens"],
                    ", ".join(P["characters"][x]["name"] for x in s.get("who", [])), s["at"], s["lt"], s["do"], say, s["snd"],
                    (s.get("txt") or {}).get("text", "").replace("\n", " | ")] + [gl[k] for k in tools])
    w.writerow([NOTICE])
    return buf.getvalue()


def running_order(P: dict) -> list[tuple[str, dict]]:
    """Every shot and card in the order the film runs: a card follows the shot or card it names."""
    out = [("shot", s) for s in P["shots"]]
    for c in P["cards"]:
        k = next((i for i, (_, x) in enumerate(out) if x["id"] == c["after"]), len(out) - 1)
        out.insert(k + 1, ("card", c))
    return out


def _mmss(t: int) -> str:
    return f"{t // 60}:{t % 60:02d}"


def scenes_md(P: dict) -> str:
    rows, t, cur = [], 0, None
    for kind, x in running_order(P):
        if kind == "card":
            rows.append([f"card: {x['id']}", "", "", x["s"], _mmss(t)])
            t += x["s"]
            continue
        if x["sc"] != cur:
            cur = x["sc"]
            rows.append([str(cur), heading_of(cur, P), 0, 0, _mmss(t)])
        rows[-1][2] += 1
        rows[-1][3] += x["s"]
        t += x["s"]
    L = [f"# {P['title']}: The Scenes", "", "Written by `tools/film.py` from the shot list in `docs/film/production.json`: every "
         "scene in the order the film runs, with its shots, its length and the moment it starts; the cards are placed where "
         "they play.", "", "| Scene | Heading | Shots | Seconds | Starts at |", "|---|---|---|---|---|"]
    L += [f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} |" for r in rows]
    L += ["", f"Running time: {_mmss(t)} ({len(P['shots'])} shots and {len(P['cards'])} cards).", ""]
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------- cards and overlays (SVG)

def card_lines(c: dict) -> list[str]:
    if c["kind"] == "receipt":
        sp = site_pages()
        return [sp["sentence"], "Where: " + sp["place"] + ".", "Receipt: " + sp["receipt"],
                "Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results."]
    if c["kind"] == "notice":
        return [NOTICE]
    return list(c.get("lines", []))


def _svg(body: str, bg: str | None = "#000") -> str:
    head = (f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!-- {escape(NOTICE)} -->\n"
            "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"1920\" height=\"1080\" viewBox=\"0 0 1920 1080\">\n")
    return head + (f"<rect width=\"1920\" height=\"1080\" fill=\"{bg}\"/>\n" if bg else "") + body + f"</svg>\n<!-- {escape(NOTICE)} -->\n"


def _text(lines: list[str], x: int, y: int, size: int, fill: str, family: str, weight: str = "normal", anchor: str = "middle",
          gap: float = 1.45) -> str:
    out = []
    for i, ln in enumerate(lines):
        out.append(f"<text x=\"{x}\" y=\"{int(y + i * size * gap)}\" font-family=\"{family}\" font-size=\"{size}\" "
                   f"font-weight=\"{weight}\" fill=\"{fill}\" text-anchor=\"{anchor}\">{escape(ln)}</text>")
    return "\n".join(out) + "\n"


def card_svg(c: dict) -> str:
    sans = "Liberation Sans, Arial, sans-serif"
    if c["kind"] == "title":
        return _svg(_text(c["lines"], 960, 560, 120, "#f4f1ea", sans, "bold") +
                    "<line x1=\"560\" y1=\"610\" x2=\"1360\" y2=\"610\" stroke=\"#f4f1ea\" stroke-width=\"3\"/>\n")
    lines = card_lines(c)
    size = 30 if c["kind"] == "notice" else 40
    wrapped = []
    for ln in lines:
        wrapped += textwrap.wrap(ln, 64 if size == 40 else 92) + [""]
    wrapped = wrapped[:-1]
    y = int(540 - (len(wrapped) - 1) * size * 1.45 / 2)
    return _svg(_text(wrapped, 960, y, size, "#f4f1ea", sans))


SHAPE = {"green": "<circle cx=\"{x}\" cy=\"{y}\" r=\"18\" fill=\"#2e9b4f\"/>",
         "yellow": "<polygon points=\"{x},{t} {r},{y} {x},{b} {l},{y}\" fill=\"#e2b007\"/>",
         "red": "<polygon points=\"{a}\" fill=\"#c8102e\"/>"}


def _shape(kind: str, x: int, y: int) -> str:
    if kind == "red":
        import math
        pts = " ".join(f"{x + 20 * math.cos(math.pi / 8 + k * math.pi / 4):.1f},{y + 20 * math.sin(math.pi / 8 + k * math.pi / 4):.1f}"
                       for k in range(8))
        return SHAPE["red"].format(a=pts)
    return SHAPE[kind].format(x=x, y=y, t=y - 22, b=y + 22, l=x - 22, r=x + 22)


def overlay_svg(s: dict) -> str:
    t = s["txt"]
    kind, lines = t["kind"], t["text"].split("\n")
    mono, sans = "Liberation Mono, Courier New, monospace", "Liberation Sans, Arial, sans-serif"
    if kind == "slide":
        body = _text(lines, 960, int(540 - (len(lines) - 1) * 90 * 1.3 / 2), 90, "#111", sans, "bold", gap=1.3)
        return _svg(body, "#fafafa")
    if kind == "phone":
        h = 120 + 64 * len(lines)
        body = (f"<rect x=\"560\" y=\"{540 - h // 2}\" width=\"800\" height=\"{h}\" rx=\"36\" fill=\"#1c1c1e\" fill-opacity=\"0.94\"/>\n"
                + _text(lines, 620, 540 - h // 2 + 100, 44, "#f2f2f7", sans, anchor="start", gap=1.45))
        return _svg(body, None)
    if kind == "clock":
        return _svg(_text(lines, 960, 600, 260, "#e8e8e8", mono, "bold"), None)
    if kind == "board":
        rows = ""
        for i, sh in enumerate(["green", "green", "yellow", "green", "green"]):
            y = 380 + i * 90
            rows += (f"<rect x=\"520\" y=\"{y - 34}\" width=\"880\" height=\"68\" fill=\"#0f1a24\"/>\n" + _shape(sh, 580, y) + "\n"
                     f"<rect x=\"640\" y=\"{y - 10}\" width=\"{560 - 60 * (i % 3)}\" height=\"20\" rx=\"10\" fill=\"#33485c\"/>\n")
        return _svg(rows, None)
    size = 56 if kind in ("wall", "screen") else 48
    w = max(len(x) for x in lines) * size * 0.62 + 120
    h = len(lines) * size * 1.45 + 80
    body = (f"<rect x=\"{960 - w / 2:.0f}\" y=\"{540 - h / 2:.0f}\" width=\"{w:.0f}\" height=\"{h:.0f}\" rx=\"18\" fill=\"#05080c\" "
            f"fill-opacity=\"0.9\" stroke=\"#3b4a5a\" stroke-width=\"2\"/>\n" +
            _text(lines, 960, int(540 - h / 2 + 40 + size), size, "#e6f0f8", mono, "bold"))
    return _svg(body, None)


# ---------------------------------------------------------------- Final Draft

def fdx(title: dict, els: list[tuple]) -> str:
    def para(kind: str, text: str, align: str | None = None) -> str:
        a = f" Alignment=\"{align}\"" if align else ""
        return f"    <Paragraph{a} Type=\"{kind}\">\n      <Text>{escape(plain(text))}</Text>\n    </Paragraph>\n"
    kinds = {"scene": "Scene Heading", "action": "Action", "character": "Character", "dialogue": "Dialogue",
             "parenthetical": "Parenthetical", "transition": "Transition"}
    out = ["<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\" ?>\n", f"<!-- {escape(NOTICE)} -->\n",
           "<FinalDraft DocumentType=\"Script\" Template=\"No\" Version=\"5\">\n  <Content>\n"]
    for k, t in els:
        if k == "centered":
            out.append(para("Action", t, "Center"))
        elif k in kinds:
            out.append(para(kinds[k], t.replace("\n", " ") if k != "action" else t))
    out.append(para("General", NOTICE))
    out.append("  </Content>\n  <TitlePage>\n    <Content>\n")
    for key in ("title", "credit", "author", "source", "draft date", "contact", "copyright", "notes"):
        for ln in title.get(key, []):
            out.append(para("Text", ln, "Center" if key in ("title", "credit", "author", "source") else "Left").replace("    ", "      ", 1))
    out.append("    </Content>\n  </TitlePage>\n</FinalDraft>\n")
    out.append(f"<!-- {escape(NOTICE)} -->\n")
    return "".join(out)


# ---------------------------------------------------------------- the PDFs (reportlab, the faces the books embed)

def _pdf_tools():
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.units import inch
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    lib = "/usr/share/fonts/truetype/liberation/"
    for name, f in (("FilmMono", "LiberationMono-Regular.ttf"), ("FilmMono-Bold", "LiberationMono-Bold.ttf"),
                    ("FilmSerif", "LiberationSerif-Regular.ttf"), ("FilmSerif-Bold", "LiberationSerif-Bold.ttf"),
                    ("FilmSerif-Italic", "LiberationSerif-Italic.ttf"), ("FilmSans", "LiberationSans-Regular.ttf"),
                    ("FilmSans-Bold", "LiberationSans-Bold.ttf")):
        if name not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont(name, lib + f))
    # every face is a Liberation face, as in the books (the audit of 2 November): the page's opening font, a table cell's
    # and a bullet's take Liberation Sans, never the PDF's base-14 Helvetica
    from reportlab import rl_config
    import reportlab.platypus.tables as tables
    from reportlab.lib.styles import ParagraphStyle
    rl_config.canvas_basefontname = "FilmSans"
    tables.CellStyle.fontname = "FilmSans"
    ParagraphStyle.defaults["fontName"] = ParagraphStyle.defaults["bulletFontName"] = "FilmSans"
    from reportlab.lib.fonts import addMapping
    addMapping("FilmSerif", 0, 0, "FilmSerif")
    addMapping("FilmSerif", 1, 0, "FilmSerif-Bold")
    addMapping("FilmSerif", 0, 1, "FilmSerif-Italic")
    addMapping("FilmSerif", 1, 1, "FilmSerif-Bold")
    return letter, inch


def script_flowables(title: dict, els: list[tuple], P: dict):
    from reportlab.platypus import Flowable, KeepTogether
    from reportlab.lib.units import inch
    num = {x["heading"]: x["n"] for x in P["scenes"]}

    class Mono(Flowable):
        def __init__(self, text, left=0.0, width=60, align="left", bold=False, before=1, number=None, keep=False):
            super().__init__()
            self.lines = []
            for para in text.split("\n"):
                self.lines += textwrap.wrap(para, width) or [""]
            self.left, self.width_chars, self.align, self.bold = left, width, align, bold
            self.before, self.number, self.keepWithNext = before, number, keep

        def wrap(self, aw, ah):
            self._aw = aw
            return aw, 12 * (len(self.lines) + self.before)

        def split(self, aw, ah):
            n = int(ah // 12) - self.before
            if self.number is not None or n < 2 or n >= len(self.lines) or self.align != "left" or self.left:
                return []
            a = Mono("\n".join(self.lines[:n]), self.left, self.width_chars, before=self.before)
            b = Mono("\n".join(self.lines[n:]), self.left, self.width_chars, before=0)
            return [a, b]

        def draw(self):
            c = self.canv
            c.setFont("FilmMono-Bold" if self.bold else "FilmMono", 12)
            h = 12 * len(self.lines)
            for i, ln in enumerate(self.lines):
                y = h - 12 * (i + 1) + 3
                if self.align == "center":
                    c.drawCentredString(3 * inch, y, ln)
                elif self.align == "right":
                    c.drawRightString(6 * inch, y, ln)
                else:
                    c.drawString(self.left * inch, y, ln)
            if self.number is not None:
                c.setFont("FilmMono", 12)
                c.drawRightString(-0.35 * inch, h - 12 + 3, f"{self.number}")
                c.drawString(6.35 * inch, h - 12 + 3, f"{self.number}")

    out, i = [], 0
    while i < len(els):
        k, t = els[i]
        if k == "scene":
            out.append(Mono(plain(t).upper(), bold=True, before=2 if out else 0, number=num.get(plain(t)), keep=True))
        elif k == "action":
            out.append(Mono(plain(t)))
        elif k == "centered":
            out.append(Mono(plain(t), align="center", bold=t.startswith("**")))
        elif k == "transition":
            out.append(Mono(plain(t).upper(), align="right"))
        elif k == "character":
            grp = [Mono(plain(t), left=2.2, width=38)]
            j = i + 1
            while j < len(els) and els[j][0] in ("dialogue", "parenthetical"):
                kk, tt = els[j]
                grp.append(Mono(plain(tt), left=1.6, width=25, before=0) if kk == "parenthetical"
                           else Mono(plain(tt), left=1.0, width=35, before=0))
                j += 1
            out.append(KeepTogether(grp))
            i = j
            continue
        elif k == "page_break":
            from reportlab.platypus import PageBreak
            out.append(PageBreak())
        i += 1
    return out


def _title_page(canv, doc, title: dict):
    from reportlab.lib.units import inch
    canv.saveState()
    w, h = doc.pagesize
    canv.setFont("FilmMono-Bold", 14)
    canv.drawCentredString(w / 2, h - 3.6 * inch, plain(" ".join(title.get("title", []))).upper())
    canv.setFont("FilmMono", 12)
    canv.drawCentredString(w / 2, h - 4.1 * inch, " ".join(title.get("credit", [])))
    canv.drawCentredString(w / 2, h - 4.35 * inch, " ".join(title.get("author", [])))
    y = h - 4.9 * inch
    canv.setFont("FilmSerif-Italic", 11)
    for ln in textwrap.wrap(" ".join(title.get("source", [])), 78):
        canv.drawCentredString(w / 2, y, ln)
        y -= 16.5
    canv.setFont("FilmMono", 11)
    y = h - 6.55 * inch
    for ln in title.get("contact", []):
        canv.drawString(1.0 * inch, y, ln)
        y -= 14
    canv.drawRightString(w - 1.0 * inch, h - 6.55 * inch, " ".join(title.get("draft date", [])))
    canv.setFont("FilmSerif", 11)
    y = 3.0 * inch
    for ln in textwrap.wrap(" ".join(title.get("notes", [])), 96):
        canv.drawString(1.0 * inch, y, ln)
        y -= 16.5
    y -= 6
    for ln in textwrap.wrap(" ".join(title.get("copyright", [])), 96):
        canv.drawString(1.0 * inch, y, ln)
        y -= 16.5
    canv.restoreState()


def _foot(canv, doc):
    from reportlab.lib.units import inch
    canv.saveState()
    canv.setFont("FilmSans", 8)
    w = doc.pagesize[0]
    for i, ln in enumerate(textwrap.wrap(SHORT, 140)):
        canv.drawCentredString(w / 2, 0.45 * inch - i * 10, ln)
    canv.restoreState()


def md_flowables(md: str):
    """The bible's Markdown: headings, paragraphs, lists, tables, quotes and rules, in the house type (11 point on 16.5)."""
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, HRFlowable
    from reportlab.lib import colors
    body = ParagraphStyle("b", fontName="FilmSerif", fontSize=11, leading=16.5, spaceAfter=7)
    quote = ParagraphStyle("q", parent=body, fontName="FilmSerif-Italic", leftIndent=14)
    h1 = ParagraphStyle("h1", parent=body, fontName="FilmSerif-Bold", fontSize=22, leading=28, spaceAfter=12)
    h2 = ParagraphStyle("h2", parent=body, fontName="FilmSerif-Bold", fontSize=15, leading=21, spaceBefore=12, spaceAfter=6)
    h3 = ParagraphStyle("h3", parent=body, fontName="FilmSerif-Bold", fontSize=12.5, leading=18, spaceBefore=8, spaceAfter=4)
    li = ParagraphStyle("li", parent=body, leftIndent=18, bulletIndent=4, spaceAfter=3, bulletFontName="FilmSerif")
    cell = ParagraphStyle("c", parent=body, fontSize=11, leading=15, spaceAfter=0)

    def inl(t):
        t = escape(t)
        t = re.sub(r"`([^`]+)`", r'<font name="FilmMono">\1</font>', t)
        t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
        t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
        t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", t)
        return t

    out, para, table = [], [], []
    lines = md.split("\n")

    def flush_para():
        if para:
            out.append(Paragraph(inl(" ".join(para)), body))
            para.clear()

    def flush_table():
        if table:
            rows = [[Paragraph(inl(c.strip()), cell) for c in r.strip().strip("|").split("|")] for r in table
                    if not re.fullmatch(r"\|?\s*:?-{3,}.*", r.strip())]
            n = max(len(r) for r in rows)
            rows = [r + [Paragraph("", cell)] * (n - len(r)) for r in rows]
            tb = Table(rows, colWidths=[6.5 * 72 / n] * n, repeatRows=1)
            tb.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#999999")),
                                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eeeeee")),
                                    ("VALIGN", (0, 0), (-1, -1), "TOP")]))
            out.append(tb)
            out.append(Spacer(1, 8))
            table.clear()

    for ln in lines:
        s = ln.rstrip()
        if s.startswith("|"):
            flush_para()
            table.append(s)
            continue
        flush_table()
        if not s.strip():
            flush_para()
            continue
        if s.startswith("#"):
            flush_para()
            lvl = len(s) - len(s.lstrip("#"))
            out.append(Paragraph(inl(s.lstrip("#").strip()), {1: h1, 2: h2}.get(lvl, h3)))
        elif re.match(r"^\s*[-*] ", s):
            flush_para()
            out.append(Paragraph(inl(re.sub(r"^\s*[-*] ", "", s)), li, bulletText="•"))
        elif re.match(r"^\s*\d+\. ", s):
            flush_para()
            m = re.match(r"^\s*(\d+)\. (.*)$", s)
            out.append(Paragraph(inl(m.group(2)), li, bulletText=m.group(1) + "."))
        elif s.startswith(">"):
            flush_para()
            out.append(Paragraph(inl(s.lstrip("> ").strip()), quote))
        elif s.strip() == "---":
            flush_para()
            out.append(HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#888888"), spaceBefore=6, spaceAfter=6))
        else:
            para.append(s.strip())
    flush_para()
    flush_table()
    return out


def render_pdf(title: dict, els: list[tuple], P: dict, book: bool) -> bytes:
    letter, inch = _pdf_tools()
    from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, NextPageTemplate, PageBreak, Spacer, Paragraph
    from reportlab.platypus.flowables import Flowable
    from reportlab.lib.styles import ParagraphStyle
    buf = io.BytesIO()
    state = {"script_first": None}

    class Mark(Flowable):
        def wrap(self, aw, ah):
            return 0, 0

        def draw(self):
            if state["script_first"] is None:
                state["script_first"] = self.canv.getPageNumber()

    def on_title(c, d):
        _title_page(c, d, title)                         # the whole notice is on the page itself

    def on_script(c, d):
        n = c.getPageNumber()
        first = state["script_first"] or n
        if n > first:
            c.saveState()
            c.setFont("FilmMono", 12)
            c.drawRightString(d.pagesize[0] - 1.0 * inch, d.pagesize[1] - 0.5 * inch, f"{n - first + 1}.")
            c.restoreState()
        _foot(c, d)

    def on_bible(c, d):
        c.saveState()
        c.setFont("FilmSans", 8)
        c.drawString(1.0 * inch, d.pagesize[1] - 0.55 * inch, P["title"] + ": the book of the film")
        c.drawRightString(d.pagesize[0] - 1.0 * inch, d.pagesize[1] - 0.55 * inch, f"{c.getPageNumber()}")
        c.restoreState()
        _foot(c, d)

    doc = BaseDocTemplate(buf, pagesize=letter, title=P["title"], author="The Omni-Compass LLC",
                          subject="Screenplay" + (" and story bible" if book else ""), creator="tools/film.py", invariant=1,
                          initialFontName="FilmSans")
    W, H = letter
    script_frame = Frame(1.5 * inch, 1.0 * inch, 6.0 * inch, H - 2.0 * inch, leftPadding=0, rightPadding=0, topPadding=0,
                         bottomPadding=0, id="s")
    bible_frame = Frame(1.0 * inch, 1.0 * inch, W - 2.0 * inch, H - 2.0 * inch, id="b")
    doc.addPageTemplates([PageTemplate("title", [Frame(0, 0, W, H, id="t")], onPage=on_title),
                          PageTemplate("bible", [bible_frame], onPage=on_bible),
                          PageTemplate("script", [script_frame], onPage=on_script)])
    story = [Spacer(1, 1)]
    if book:
        story += [NextPageTemplate("bible"), PageBreak()] + md_flowables(BIBLE.read_text(encoding="utf-8"))
        story += [PageBreak()] + md_flowables(scenes_md(P))
        story += [NextPageTemplate("title"), PageBreak(), Spacer(1, 1)]
    story += [NextPageTemplate("script"), PageBreak(), Mark()] + script_flowables(title, els, P)
    end = ParagraphStyle("end", fontName="FilmSerif", fontSize=11, leading=16.5)
    story += [Spacer(1, 36), Paragraph(escape(NOTICE), end)]
    doc.build(story)
    return buf.getvalue()


def pdf_pages(data: bytes) -> int:
    return len(re.findall(rb"/Type\s*/Page[^s]", data))


def pdf_fonts(data: bytes) -> set:
    return {m.decode() for m in re.findall(rb"/BaseFont\s*/([A-Za-z0-9+_-]+)", data)}


# ---------------------------------------------------------------- build and check

def build() -> dict:
    P = json.loads(PROD.read_text(encoding="utf-8"))
    title, els = parse(SRC.read_text(encoding="utf-8"))
    pack = prompt_pack(P)
    out = {FDX: fdx(title, els), CSV: shot_csv(P), PJSON: json.dumps(pack, indent=1, ensure_ascii=False) + "\n",
           PMD: prompts_md(pack, P), REFS: refs_md(P), SCENES_MD: scenes_md(P)}
    for c in P["cards"]:
        out[CARDS / f"{c['id']}.svg"] = card_svg(c)
    for s in P["shots"]:
        if s.get("txt"):
            out[OVERLAYS / f"{s['id']}.svg"] = overlay_svg(s)
    return {"P": P, "title": title, "els": els, "text": out}


def _stamp_md(path: Path, text: str) -> str:
    sys.path.insert(0, str(ROOT / "tools"))
    import legal  # noqa: E402
    return legal.normalize_markdown(text)[0] if path.suffix == ".md" else text


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    B = build()
    bad = problems(B["P"], B["title"], B["els"])
    files = {p: _stamp_md(p, t) for p, t in B["text"].items()}
    if a.check:
        for p, t in files.items():
            if not p.exists() or p.read_text(encoding="utf-8") != t:
                bad.append(f"{p.relative_to(ROOT)} is not what the sources give (python3 tools/film.py)")
        known = {p.name for p in files if p.parent in (CARDS, OVERLAYS)}
        for d in (CARDS, OVERLAYS):
            for f in sorted(d.glob("*.svg")) if d.exists() else []:
                if f.name not in known:
                    bad.append(f"{f.relative_to(ROOT)} belongs to no card or shot")
        faces_here = Path("/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf").exists()
        for p, book in ((PDF, False), (BOOK, True)):
            if not faces_here:
                print(f"  note: {p.relative_to(ROOT)} not rendered again here (no Liberation faces on this machine)")
                continue
            if not p.exists():
                bad.append(f"{p.relative_to(ROOT)} is missing (python3 tools/film.py)")
                continue
            got = p.read_bytes()
            want = render_pdf(B["title"], B["els"], B["P"], book)
            if pdf_pages(got) != pdf_pages(want):
                bad.append(f"{p.relative_to(ROOT)} has {pdf_pages(got)} pages where the sources give {pdf_pages(want)}")
            faces = {f.split("+")[-1] for f in pdf_fonts(got)}
            if not faces or any(not f.startswith("Liberation") for f in faces):
                bad.append(f"{p.relative_to(ROOT)} embeds faces other than Liberation: {sorted(faces)}")
        print("the film: " + ("in line with its screenplay, its production file and its records" if not bad else
                              f"{len(bad)} problem(s)"))
        for b in bad[:60]:
            print("  " + b)
        return 1 if bad else 0
    if bad:
        for b in bad[:60]:
            print("  " + b)
        print(f"the film: {len(bad)} problem(s); nothing written")
        return 1
    for p, t in files.items():
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(t, encoding="utf-8")
    PDF.write_bytes(render_pdf(B["title"], B["els"], B["P"], False))
    BOOK.write_bytes(render_pdf(B["title"], B["els"], B["P"], True))
    P = B["P"]
    rt = sum(s["s"] for s in P["shots"]) + sum(c["s"] for c in P["cards"])
    print(f"the film: {len(P['shots'])} shots and {len(P['cards'])} cards, {rt // 60} min {rt % 60} s; screenplay "
          f"{pdf_pages(PDF.read_bytes()) - 1} pages; the book {pdf_pages(BOOK.read_bytes())} pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
