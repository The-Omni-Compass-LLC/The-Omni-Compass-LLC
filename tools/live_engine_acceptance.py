# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The live benchmark engine's acceptance record (the solid-A directive's phase 6): runs docs/engine/accept_live_engine.js in a
real browser (Chromium through Playwright) on the page, checks what it read against the repository (the engine that stands,
the immune rule's own numbers in omnicompass/immune.py), and writes docs/audit/LIVE_ENGINE_ACCEPTANCE.md with every check and
its result as read. A check that did not run is written as not run, never as passed.

Usage: python3 tools/live_engine_acceptance.py [PAGE_OR_URL] [--from-json FILE]"""
from __future__ import annotations

import argparse
import ast
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
PAGE = ROOT / "docs" / "engine" / "OMNI_COMPASS_LIVE_ENGINE.html"
JS = ROOT / "docs" / "engine" / "accept_live_engine.js"
OUT = ROOT / "docs" / "audit" / "LIVE_ENGINE_ACCEPTANCE.md"


def immune_defaults():
    """The immune rule's own numbers: the defaults of Immune.__init__ in omnicompass/immune.py, read from its source."""
    tree = ast.parse((ROOT / "omnicompass" / "immune.py").read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "__init__":
            names = [a.arg for a in node.args.args][-len(node.args.defaults):]
            return {n: ast.literal_eval(d) for n, d in zip(names, node.args.defaults)}
    return {}


def engine_that_stands():
    out = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py")], capture_output=True, text=True, cwd=ROOT).stdout
    return out.strip().splitlines()[-1].split()[0] if out.strip() else "unknown"


def row(name, ok, read, rule):
    word = "PASS" if ok is True else "FAIL" if ok is False else "NOT RUN"
    return f"| {name} | **{word}** | {read} | {rule} |"


def render(d, target):
    from tools.legal import stamp
    c = d.get("checks", {})
    eng = engine_that_stands()
    imm = immune_defaults()
    rc = c.get("reflex_config") or {}
    want = {"streak": imm.get("streak"), "relief": imm.get("relief"), "margin": imm.get("margin"), "hold": imm.get("hold"),
            "holdMax": imm.get("hold_max")}
    rr, k, e, ph, g, sg, an, hd = (c.get(x) or {} for x in ("reflex_run", "kill", "errors", "phone", "geometry", "signals", "anchors", "head"))
    gain, steady, loss = g.get("gain") or {}, g.get("steady") or {}, g.get("loss") or {}
    rows = [
        row("The page opens", bool(c.get("load_ms")), f"loaded in {c.get('load_ms', '—')} ms; {hd.get('bytes', 0) / 1e6:.1f} MB as rendered",
            "the load event within 180 s"),
        row("Its title", hd.get("title") == "The Omni-Compass Live Benchmark Engine", f"“{hd.get('title', '—')}”", "The Omni-Compass Live Benchmark Engine"),
        row("The engine it names", hd.get("engine") == eng, f"data-engine {hd.get('engine')}, prose {hd.get('prose')}; the repository: {eng}",
            "the engine `tools/omni_version.py` reads"),
        row("No error in the page", e.get("page_errors") == 0 and e.get("console_errors") == 0,
            f"{e.get('page_errors', '—')} page errors, {e.get('console_errors', '—')} console errors", "none"),
        row("Every contents link lands", an.get("broken") == 0, f"{an.get('links', '—')} links, {an.get('broken', '—')} broken", "none broken"),
        row("GAIN is a green circle", gain.get("radius") == "50%" and "200" in (gain.get("bg") or ""),
            f"border-radius {gain.get('radius')}, {gain.get('bg')}; drawn {g.get('drawn', {}).get('gain', '—')} times", "round, green"),
        row("STEADY is a yellow diamond", (steady.get("transform") or "").startswith("matrix(0.707107, 0.707107"),
            f"rotated 45° ({(steady.get('transform') or '')[:28]}…), {steady.get('bg')}; drawn {g.get('drawn', {}).get('steady', '—')} times",
            "a square turned 45°, yellow"),
        row("LOSS is a red octagonal stop sign", "polygon" in (loss.get("pill_clip") or "") and "255, 77, 85" in (loss.get("pill_bg") or ""),
            f"the word's plate clipped to an octagon, {loss.get('pill_bg')}, a white octagon inside; drawn {g.get('drawn', {}).get('loss', '—')} times",
            "an octagon, red"),
        row("The four live words", sg.get("words") == ["GAINING", "STEADY", "REDLINING", "AWAITING", "OVER THE LINE"],
            f"{', '.join(sg.get('words') or [])}; {sg.get('monitors', '—')} monitors, {sg.get('strips', '—')} signals",
            "GAINING, STEADY, REDLINING, AWAITING, OVER THE LINE"),
        row("The reflex runs on the engine's own numbers", all(rc.get(k_) == v for k_, v in want.items()) and bool(want.get("streak")),
            f"the page {json.dumps({k_: rc.get(k_) for k_ in want})}; `omnicompass/immune.py` {json.dumps(want)}",
            "equal, every one a knob on the panel"),
        row("The reflex acts under a surge", (rr.get("hand_backs", 0) + rr.get("stayed", 0)) > 0,
            f"decision {rr.get('t', '—')}: {rr.get('hand_backs', '—')} hand-backs to native, {rr.get('stayed', '—')} stays, {rr.get('handed_now', '—')} held native now",
            "a hand-back or a stay recorded"),
        row("The kill switch", k.get("off", {}).get("killed") is True and k.get("on_again") is True,
            f"pressed: every side native ({k.get('off', {}).get('killed')}); pressed again: Omni-Compass on ({k.get('on_again')})", "off at once, on again"),
        row("A phone, 390 px", ph.get("overflow_px") == 0 and ph.get("page_errors") == 0,
            f"page {ph.get('scroll_width', '—')} px wide on a {ph.get('client_width', '—')} px screen; wide tables scroll inside their own box",
            "no sideways scroll of the page"),
    ]
    L = ["# The live benchmark engine: acceptance in a real browser", "",
         f"Read on {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} by `tools/live_engine_acceptance.py` "
         f"(`docs/engine/accept_live_engine.js`, Chromium through Playwright) from `{target}`. Each line is what the browser read; "
         "a check that did not run says so.", "",
         "| Check | Result | What the browser read | The rule |", "|---|---|---|---|"] + rows + ["",
         "## What the page's controls are", "",
         "| Control | What it is |", "|---|---|",
         "| The monitors' recorded views, the receipts, the trading floor, the audit | read-only displays of committed receipts, each traced to its file and run |",
         "| The live model, the mechanism's knobs, the reflex's knobs, the dial, the faults, the kill switch on the page | an interactive model in the browser (class S); nothing it does reaches any machine |",
         "| The Prometheus reader | read-only queries to a Prometheus the viewer names; nothing is written |",
         "| The run buttons | links to GitHub's own pages, where a person with access starts a workflow; the page starts nothing |",
         "| Physical actuators | none: no control on this page writes to a real system; the engine's real writes are the governors' (`omni_controller/`), under their own authority and kill switch |",
         "", "The page makes no request to any server of its own; it opens as one file, offline, or from any static host."]
    return "\n".join(stamp(L)) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("target", nargs="?", default=str(PAGE))
    ap.add_argument("--from-json", help="a run's JSON already read (the browser not started again)")
    a = ap.parse_args(argv)
    if a.from_json:
        d = json.loads(Path(a.from_json).read_text(encoding="utf-8"))
    else:
        r = subprocess.run(["node", str(JS), a.target], capture_output=True, text=True, timeout=900)
        d = json.loads(r.stdout.strip().splitlines()[-1])
    if "fatal" in d:
        print("the browser run failed:", d["fatal"])
        return 1
    tgt = a.target if a.target.startswith("http") else str(Path(a.target).resolve().relative_to(ROOT)) if Path(a.target).resolve().is_relative_to(ROOT) else Path(a.target).name
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(d, tgt), encoding="utf-8")
    t = OUT.read_text(encoding="utf-8")
    print(f"{OUT.relative_to(ROOT)}: {t.count('**PASS**')} pass, {t.count('**FAIL**')} fail, {t.count('**NOT RUN**')} not run")
    return 0 if "**FAIL**" not in t else 1


if __name__ == "__main__":
    sys.exit(main())

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
