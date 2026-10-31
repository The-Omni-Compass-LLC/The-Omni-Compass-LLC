# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The page word for word: the last appendix of the Live Benchmark Engine Manual, written from the live benchmark engine page itself.

The founder's order of 20 October: three manuals in the end, the third reading the live benchmark engine top to bottom, so that the book
and the page read each other both ways. The book is docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md, built with the other two by
docs/book/build_book.py --live; its last appendix (Appendix L) is this file's output, docs/engine/PAGE_WORD_FOR_WORD.md: every
section of docs/engine/OMNI_COMPASS_LIVE_ENGINE.html in the page's own order with its number, title, summary and controls line,
every monitor under its own number with its evidence class, its state, the open-source feed that would carry it and its knobs
(docs/engine/monitors.json and the page's own order), every knob, and every LOSS row with its cause and the knob that answers
it, read from the page's embedded records. Nothing in it is typed twice. Rebuild it whenever the page changes, then the book:

  python3 docs/book/build_live_manual.py            docs/engine/PAGE_WORD_FOR_WORD.md
  python3 docs/book/build_live_manual.py --check    exit 1 if it differs from what the page gives
  python3 docs/book/build_book.py --live            the Live Benchmark Engine Manual, with the appendix bound in
"""
from __future__ import annotations

import html
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.legal import NOTICE, TOP, PLAIN, normalize_markdown  # noqa: E402

PAGE = ROOT / "docs" / "engine" / "OMNI_COMPASS_LIVE_ENGINE.html"
REG = ROOT / "docs" / "engine" / "monitors.json"
OUT_MD = ROOT / "docs" / "engine" / "PAGE_WORD_FOR_WORD.md"
BOOK = "The Live Benchmark Engine Manual"

CONTACT = ("The Omni-Compass LLC, main office infrastructure. Toll-free direct: 1-888-339-9551. System route asset: 1-888-DEX-YLL-1. "
           "Landline, registered in Florida: 321-746-4411. www.omni-compass.com")


def text(fragment: str) -> str:
    """Visible text of an HTML fragment, entities decoded, whitespace folded."""
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", fragment, flags=re.S)
    s = re.sub(r"<br\s*/?>", " ", s)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def embedded(page: str, key: str):
    m = re.search(r'<script type="application/json" id="%s">(.*?)</script>' % key, page, re.S)
    return json.loads(m.group(1)) if m else None


def model(page: str) -> dict:
    """The page as a book: the parts and sections in their order, each with its number, title, summary, controls, panels and
    monitors (every canvas, numbered in its order of appearance)."""
    body = re.sub(r'<script type="application/json" id="[^"]+">.*?</script>', "", page, flags=re.S)
    canv = re.findall(r'<canvas id="([A-Za-z0-9_-]+)"', body)
    canv = [c for c in canv if c != "wallCv"]
    number = {c: i + 1 for i, c in enumerate(canv)}
    items = []
    # the title page is a section of the page in its own place (appendix A on the page built in the page's order of
    # 31 October), numbered and titled by its own heading
    for m in re.finditer(r'<div class="partHead[^"]*" id="([^"]+)"><span class="pn">([^<]*)</span><span class="pt">([^<]*)</span></div>|<section class="[^"]*" id="([^"]+)"|<header class="head" id="title-page">(.*?)</header>', body, re.S):
        if m.group(1):
            items.append({"kind": "part", "id": m.group(1), "n": m.group(2), "title": html.unescape(m.group(3))})
            continue
        if m.group(5) is not None:
            tp = m.group(5)
            h2 = re.search(r'<h2[^>]*>(?:<span class="sn">([^<]*)</span>)?(.*?)</h2>', tp, re.S)
            words = [("p", text(x)) for x in re.findall(r'<p class="lede"[^>]*>(.*?)</p>|<div class="realDisclose"[^>]*>(.*?)</div>', tp, re.S) for x in x if x]
            items.append({"kind": "section", "id": "title-page", "n": (h2.group(1) or "") if h2 else "",
                          "title": text(h2.group(2)) if h2 else "Title page and build", "summary": "", "controls": "",
                          "words": [w for w in words if w[1]], "panels": [], "monitors": []})
            continue
        sid = m.group(4)
        i, depth, j = m.start(), 0, None
        for mm in re.finditer(r'<section\b|</section>', body[i:]):
            depth += -1 if mm.group(0) == "</section>" else 1
            if depth == 0:
                j = i + mm.end()
                break
        sec = body[i:j]
        h2 = re.search(r'<h2[^>]*>(?:<span class="sn">([^<]*)</span>)?(.*?)</h2>', sec, re.S)
        summ = re.search(r'<p class="plain"><b>Summary\.</b>(.*?)</p>', sec, re.S)
        ctl = re.search(r'<div class="secknobs"[^>]*><b>Controls\.</b>(.*?)</div>', sec, re.S)
        words = []
        for w in re.finditer(r'<h3[^>]*>(.*?)</h3>|<p class="(?:lede|note|plain|prose)[^"]*"[^>]*>(.*?)</p>|<div class="realDisclose"[^>]*>(.*?)</div>|<summary>(.*?)</summary>|<table class="[^"]*\bptab\b[^"]*">(.*?)</table>', sec, re.S):
            if w.group(5) is not None:              # a table of words the page writes itself, row by row
                words.append(("t", [[text(c) for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", tr, re.S)]
                                    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", w.group(5), re.S)]))
                continue
            if w.group(1) is not None:
                tx = text(w.group(1)); kind = "h"
            elif w.group(4) is not None:
                tx = text(w.group(4)); kind = "h"
            else:
                tx = text(w.group(2) if w.group(2) is not None else w.group(3)); kind = "p"
            if tx and tx not in ("—", "-") and not tx.startswith("Summary.") and len(tx) > 2:
                words.append((kind, tx))
        summ_t = text(summ.group(1)) if summ else ""
        if summ_t in ("", "—"):
            lede = re.search(r'<p class="lede"[^>]*>(.*?)</p>', sec, re.S)
            summ_t = text(lede.group(1)) if lede else ""
        items.append({"kind": "section", "id": sid, "n": (h2.group(1) or "") if h2 else "", "title": text(h2.group(2)) if h2 else sid,
                      "fixed": not re.search(r'\sid="', sec[sec.index(">") + 1:]),     # nothing in it is filled from a record
                      "summary": summ_t, "controls": text(ctl.group(1)) if ctl else "", "words": words,
                      "panels": [text(x) for x in re.findall(r"<h3[^>]*>(.*?)</h3>", sec, re.S)],
                      "monitors": [c for c in re.findall(r'<canvas id="([A-Za-z0-9_-]+)"', sec) if c != "wallCv"]})
    return {"items": items, "number": number, "canvases": canv}


READ = {   # how to read a monitor of each layer, and what the engineer in charge does with it
    "switch": ("The wiring from the top down: the master switch above the brain, the brain above the organism, the organism above every muscle, and native's own controllers under every muscle, never switched. The switch's state is the word on it: ON in green while Omni-Compass governs; engaged, the switch red and OFF in white.",
               "Press the kill switch only for security: it is instant, every setting goes back to native and is read back. Watch the governors' table beside it: every governor on the page says OFF and what it handed back."),
    "whole": ("Bars and tiles in the traffic light of the one key: GAIN green to one side, LOSS red to the other, STEADY yellow on zero, power given blue. A figure is a composition or a table's own word, never a single run's number.",
              "Read the word before the size, and the interval before the word: an interval across zero is STEADY whatever its centre. A LOSS on the board is answered on the status board, with its cause and its knob."),
    "service": ("The four golden signals of a service, one point a decision of the live benchmark engine: native in orange, Omni-Compass in blue, the same demand on both. A red band is a kill-switch window.",
                "Watch latency and errors first: a rise there is the only thing that can read LOSS. Saturation and throughput are the work and the capacity held: capacity is power given when it rises."),
    "cluster": ("A Kubernetes run played back from its own archived files, or the shipped controller replayed decision by decision from its own audit: the machines, the replicas, the response line, native beside Omni-Compass.",
                "Pick the run (A, B or C) and the gauge; read the paired difference in each repetition before the table's word. A run of the engine that stands carries {engine}; an older engine's run is its own record."),
    "cloud": ("The bill the cloud meters: machine-hours and the bill at list price, native's bar beside Omni-Compass's, each finished set with its word; the running set's repetitions measured so far; each provider's hourly gate with the reason its own job wrote.",
              "The bill aims lower: a fall is a GAIN, inside the noise STEADY, a rise power given. A provider whose gate holds runs nothing and bills nothing; its frame stays empty until its first set lands."),
    "orchestrators": ("Each scheduler, queue and multi-cluster governor four ways: the organism alone, the orchestrator as shipped, Omni-Compass on the organism alone, Omni-Compass on the orchestrator.",
                      "Only two of the four comparisons are Omni-Compass against its native (on top of the orchestrator; on the organism alone); the others are the orchestrator's own cost and are never counted as Omni-Compass's."),
    "chip": ("The card's own meter, second by second: its draw, the power limit Omni-Compass wrote (dashed), its clock, the 95th percentile against the response line, its temperature; every write of the governor a red tick.",
             "Power on a card is a resource: a fall is a cut, a rise power given; the response time is the judge. The one real run on the page is the replaced controller's record and is shown as such until its {engine} run lands."),
    "host": ("The processor's frequency ceiling (the knob), the clock the kernel's own governor ran at under it, the package power and the busy share, native beside Omni-Compass.",
             "Until a machine with its energy counter runs it, the monitor plays the harness's own modelled machine: read the mechanism, never the numbers."),
    "organism": ("The organism the brain governs, muscle by muscle: positions in the compass band, the brain's grants and pushes, the immune system's heat debt; native's own controllers under every muscle.",
                 "Turn the console's knobs (demand, noise, sensor delay, faults) and watch both arms take the same input; the difference between the lanes is what Omni-Compass did."),
    "organisms": ("Each organism or grid square read by the one key: green GAIN, yellow STEADY, red LOSS, grey a single run, dashed not yet run.",
                  "A dashed square is pending runner capacity, never rented. A LOSS square names its organism, its size and its runs."),
    "muscles": ("Every muscle of the catalog one cell, its word against native on its own load: green GAIN, yellow STEADY (pale: at its limit on native), red LOSS.",
                "Click a cell to read the muscle: its family, realm, template, knob and its word under each load."),
    "analytics": ("The organism's telemetry as a tensor (muscle by gauge by time), its difference between the arms, its principal modes, the service level against its objective and the error budget burned, native beside Omni-Compass.",
                  "The service level and the budget are what an on-call engineer is paged on: watch the burn rate on both arms under the same knobs."),
    "brain": ("The brain's six state variables integrated by the fourth-order Runge–Kutta step every decision, the compass band with its cushions and its two forces, the organs' grants, native's own controller beside each grant.",
              "The brain never forces: it reacts to what the body shows. A grant to expand is not a write; a write happens only where the muscle's own trial allows it."),
    "verdict": ("A give-back trial judged against native: its reference, its step, its interval, the word; then the keep ratio at every true cost.",
                "A step is kept only when its interval stays inside the allowance; a refused step leaves the muscle where native had it."),
    "console": ("The live benchmark engine's response to every knob, native beside Omni-Compass, and the page's own frame budget.",
                "Every knob acts on both arms alike; the difference between them is Omni-Compass's doing alone."),
    "proof": ("The Python's seeded runs beside this page's: one cell a run (green agrees to 1e-9, red differs, blue a new set), the two digests under them; and the Python's 500 scenarios a seed replayed with every trace hash.",
              "Press the button to run the Python's set here; run a new base to make a new set and run the printed command in the Python to compare digests. Print or download the receipts for the file."),
    "page": ("This page's own render loop governed by the compass law: the time between frames against its line, native (no governor) beside Omni-Compass.",
             "Load the page with the frame-load knob and watch the governor shed chart frames to keep every frame inside its line."),
    "ci": ("GitHub's runs in flight at the build by workflow, the Azure set's repetitions measured, each cloud's gate with its reason, the chips' runs.",
           "A gate that holds names its fix in its own words; nothing is billed while it holds."),
}


def md_lines() -> list[str]:
    page = PAGE.read_text(encoding="utf-8")
    reg = json.loads(REG.read_text(encoding="utf-8"))
    M = model(page)
    by = {m["id"]: m for m in reg["monitors"]}
    K = reg.get("knobs", {})
    build = embedded(page, "build") or {}
    scen = embedded(page, "scen") or {}
    eng = build.get("engine", "")
    from tools.omni_version import VERSIONS
    standing = f"omni-{next(iter(VERSIONS))}"    # the engine that stands: the version list's newest
    out = []
    # ---------------------------------------------------------------- Part II
    out += ["## Part II. The live benchmark engine, section by section", "",
            "Each part below is one section of the page, in the page's order and under its number: what the page says it is, its controls, its panels, and every monitor in it under its own number, with what it shows, its evidence and state, the feed that would carry it live, its knobs, how to read it and what to do with it.", ""]
    for it in M["items"]:
        if it["kind"] == "part":
            out += [f"### Part {it['n']} of the page: {it['title']}" if it["n"] else f"### The page's {it['title']}", ""]
            continue
        title = f"{it['n']} {it['title']}".strip()
        out += [f"### {title}", ""]
        if it["summary"]:
            out += [it["summary"], ""]
        if it["controls"]:
            out += [f"**Controls.** {it['controls']}", ""]
        if it.get("words"):
            out += ["**The page, in its own words.**", ""]
            for kind, tx in it["words"]:
                if kind == "t":
                    out += ["| " + " | ".join(tx[0]) + " |", "|" + "---|" * len(tx[0])]
                    out += ["| " + " | ".join(c.replace("|", "/") for c in row) + " |" for row in tx[1:]] + [""]
                    continue
                if tx == it["summary"]:
                    continue
                out += [f"**{tx}**" if kind == "h" else tx, ""]
        out += ["**Its monitors.**" if it["monitors"] else
                "**Its monitors.** This section draws no canvas: it is words and their sources, written in the page itself." if it.get("fixed") else
                "**Its monitors.** This section draws no canvas: its views are tables and text the page builds from its records.", ""]
        for cid in it["monitors"]:
            m = by.get(cid, {"name": cid, "what": "", "cls": "", "status": "", "feed": {"exporter": "", "metrics": [], "promql": []}, "knobs": [], "layer": "page"})
            n = m.get("n") or M["number"].get(cid, "?")       # the number its badge carries: its place on the wall (monitors.json)
            out += [f"#### Monitor {n}: {m['name']}", ""]
            if m.get("what"):
                out += [m["what"], ""]
            st = m.get("status", "")
            out += [f"- **Evidence and state.** Class {m.get('cls') or '—'}; {('awaiting its run: ' + m['awaiting']) if m.get('awaiting') else st}."]
            f = m.get("feed", {})
            feed = f.get("exporter") or "this page"
            if f.get("metrics"):
                feed += "; series " + ", ".join(f"`{x}`" for x in f["metrics"])
            if f.get("promql"):
                feed += "; on a running system: " + "; ".join(f"`{x}`" for x in f["promql"])
            out += [f"- **Feed.** {feed}."]
            wv = m.get("wire") or {}
            if wv:
                ticks = lambda xs: ", ".join(f"`{x}`" for x in xs)
                py, cpp = ticks(wv.get("python", [])) or wv.get("cpp_none", "none"), ticks(wv.get("cpp", [])) or wv.get("cpp_none", "none")
                held = f"; held equal by {ticks(wv['proof'])}" if wv.get("proof") else ""
                out += [f"- **Wired.** This page's `{wv['code']}` → the Python {py} → the C++ {cpp}{held}.", f"- **Moves.** {wv['moves'][:1].upper()}{wv['moves'][1:]}."]
            if m.get("knobs"):
                out += ["- **Knobs.** " + "; ".join(f"{K[k]['label']}: {K[k]['what']}" if k in K else k for k in m["knobs"]) + "."]
            # "the engine that stands" is the version list's newest (tools/omni_version.py, the one list the books read the
            # engine from); the page's own build record says which engine its records were built on, and lags a landing until
            # the page is rebuilt (21 October: omni-v15 landed while the page's records were still omni-v14's)
            rd, act = (x.replace("{engine}", standing) for x in READ.get(m.get("layer", ""), ("", "")))
            if rd:
                out += [f"- **How to read it.** {rd}", f"- **What to do with it.** {act}"]
            out += [""]
    # ---------------------------------------------------------------- back matter
    out += ["## Back matter", "", "### Appendix A. Every monitor", "", "| No. | Monitor | Section | Class | State |", "|---|---|---|---|---|"]
    sec_of = {}
    for it in M["items"]:
        if it["kind"] == "section":
            for c in it["monitors"]:
                sec_of[c] = f"{it['n']} {it['title'].split(':')[0]}"
    for c in sorted(M["canvases"], key=lambda c: (by.get(c, {}).get("n") or 10 ** 6, M["number"][c])):   # in the wall's order
        m = by.get(c, {"name": c, "cls": "", "status": ""})
        out.append(f"| {m.get('n') or M['number'][c]} | {m['name']} | {sec_of.get(c, '')} | {m.get('cls', '')} | {'awaiting its run' if m.get('awaiting') else m.get('status', '')} |")
    out += ["", "### Appendix B. Every knob", "", "| Knob | What it does | Where it is |", "|---|---|---|"]
    for k, v in K.items():
        out.append(f"| {v['label']} | {v['what']} | {v['where']} |")
    out += ["", "### Appendix C. Every LOSS row, whose it is, its cause and the knob that answers it", ""]
    rows = []
    for rc in scen.get("receipts", []):
        way = re.search(r"_4W_(TOP|ORCH|BARE|VS|BOTH)\.md$", rc.get("file", ""))
        omni = (not way) or way.group(1) in ("TOP", "BARE")
        for r in rc.get("rows", []):
            if r.get("w") != "LOSS":
                continue
            cause = next((c for c in rc.get("causes", []) if r["g"].lower().startswith(c["gauge"].lower())), None)
            rows.append((omni, rc, r, cause))
    rows.sort(key=lambda x: not x[0])
    out += [f"{sum(1 for x in rows if x[0])} LOSS rows are Omni-Compass against its native; {sum(1 for x in rows if not x[0])} are an orchestrator's own cost against the organism alone, with no Omni-Compass in either arm. Every one is shown as its table writes it.", ""]
    for omni, rc, r, cause in rows:
        g = r["g"].lower()
        if not omni:
            knob = "nothing of Omni-Compass to turn: the orchestrator's own cost"
        elif re.search(r"pod start wait|start wait", g):
            knob = "the test machine, not the governor: the image unpacked inside the window on the one runner every kind node shares (`docs/POD_START_WAIT.md`); the rig pre-pulls the image in both arms"
        elif re.search(r"response time|turnaround|time over the response line|wait", g):
            knob = "the compass band's upper cushion on this muscle or the give-back trial's tolerance; where no setting brings the row STEADY in the model gate, the muscle stays native on this stack"
        elif re.search(r"fail|lost|not served|unschedulable|no machine", g):
            knob = "the muscle's floor and the trial's tolerance; a muscle that fails a request native served stays native until the gate reads no LOSS"
        else:
            knob = "the muscle's own card (its band, cushions and glide); a setting that reads LOSS in the model gate is refused and the muscle stays native"
        cz = f" Cause: {cause['title']} (`{cause['file']}`)." if cause else ""
        out.append(f"- **{'Omni-Compass against native' if omni else 'the orchestrator’s own cost'}.** {rc.get('title', '').split(':')[0]} ({rc.get('engine', '')}, `{rc.get('file', '')}`): {r['g']}, A B C {' · '.join(r.get('abc') or [])}.{cz} The knob: {knob}.")
    out += ["", "### Appendix D. Glossary", "",
            "- **Native**: the system under its own controllers alone. **Omni-Compass** (the omni arm): the same system with Omni-Compass on top of those controllers.",
            "- **Muscle**: one knob of the system a native controller turns (replicas, machines, a power limit, a frequency ceiling, a cache size). **Organism**: a body of muscles governed as one.",
            "- **Compass law**: the band with 5% cushions and two antagonist forces, smooth (tanh), that moves a muscle's setting (`omnicompass/compass_law.py`).",
            "- **Brain**: the engine's six state variables, integrated by the fourth-order Runge–Kutta step every decision (`omnicompass/core.py`). **Verdict**: the give-back trial judged against native (`omnicompass/verdict.py`).",
            "- **Kill switch**: the master switch's instant hand-back of every setting to native, for security. **Lease**: the gradual walk back to native after a crash.",
            "- **The max / the tune-down**: the dial's two settings. **Power given**: a resource spent that rose, shown beside what it bought, never a LOSS.",
            "- **A, B and C**: a benchmark's three runs; a reading counts when it holds the same way in all three.",
            "- **Evidence classes**: P a physical meter, L live software, S our own models.",
            "", "### Contact", "", CONTACT, ""]
    return out


# ---------------------------------------------------------------- the PDF
def appendix_lines() -> list[str]:
    """The book's last appendix: the page's sections, monitors and knobs word for word (Part II of md_lines) and the tables of
    every monitor, every knob and every LOSS row (its back matter), one heading level up; the reading guide, the operating
    notes, the glossary and the contact are the book's own chapters and are not repeated here."""
    lines = md_lines()
    def block(start, stop):
        i = next(k for k, ln in enumerate(lines) if ln.startswith(start))
        j = next((k for k, ln in enumerate(lines) if k > i and stop and ln.startswith(stop)), len(lines))
        return lines[i + 1:j]
    up = lambda ls: [ln[1:] if ln.startswith("###") else ln for ln in ls]
    page = PAGE.read_text(encoding="utf-8")
    build = embedded(page, "build") or {}
    out = ["# The Live Benchmark Engine Page, Word for Word", "",
           "This appendix is the live benchmark engine page itself, written from `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html` at every build of "
           "this book (`docs/book/build_live_manual.py`): every section in the page's own order with its number, title, summary and "
           "controls line; every monitor under the number its badge carries, with its evidence class, its state, the open-source "
           "feed that would carry it on a running system and its knobs; every knob; and every LOSS row with whose it is, its cause "
           "and the knob that answers it. Nothing here is typed twice: what the page says, this appendix says, so the book and the "
           f"page read each other both ways. This edition was written from the page built {build.get('built_at', '')} on "
           f"{build.get('engine', '')} (digest {build.get('digest', '')[:16]}) from commit {build.get('commit', '')[:12]}.", ""]
    out += up(block("## Part II.", "## Back matter"))
    tail = block("## Back matter", None)
    keep, skip = [], False
    for ln in tail:
        if ln.startswith("### Appendix D.") or ln.startswith("### Contact"):
            skip = True
        elif ln.startswith("### "):
            skip = False
        if not skip:
            keep.append(ln)
    out += [re.sub(r"^## Appendix [A-C]\. ", "## ", ln) for ln in up(keep)]
    return out


MD_PATH = re.compile(r"(?<![\w/.`-])((?:[\w.-]+/)*[\w-]+\.md)(?![\w`])")


def code_paths(line: str) -> str:
    """A document's name set as code (`DISCLOSURES.md`), outside code already set, so the book reads "section 3" after it as
    that document's own numbering, never as one of its own sections."""
    if line.startswith("#"):
        return line
    parts = line.split("`")
    return "`".join(MD_PATH.sub(r"`\1`", seg) if i % 2 == 0 else seg for i, seg in enumerate(parts))


def main() -> int:
    text_md, _ = normalize_markdown("\n".join(code_paths(ln) for ln in appendix_lines()))
    if "--check" in sys.argv:
        same = OUT_MD.exists() and OUT_MD.read_text(encoding="utf-8") == text_md
        print("the page word for word matches the page" if same else "the page word for word differs from the page: python3 docs/book/build_live_manual.py")
        return 0 if same else 1
    OUT_MD.write_text(text_md, encoding="utf-8")
    print(f"{OUT_MD.relative_to(ROOT)} ({len(text_md.splitlines())} lines): the Live Benchmark Engine Manual's Appendix L; "
          "now python3 docs/book/build_book.py --live")
    return 0


if __name__ == "__main__":
    sys.exit(main())
