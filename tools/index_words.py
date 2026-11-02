#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The Omni index in the Owner's Manual's own words, written from the index's record so it never stands stale.

The referee audit of 2 November 2026 found the Owner's Manual quoting the index of 24 October (+3.4%, the service reading
+9.4%, read from three engines' tables) while the index of record read GAIN 5.0% and GAIN 12.9% on omni-v21: the manual's
two passages were written by hand and fell out of line when the index moved. Both are written here now, from
`results/OMNI_INDEX.json` and the benefit sheet, between their markers, and `--check` (run by verify.py) fails a push where
either differs from what the record gives.

    python3 tools/index_words.py           write both passages into docs/OMNI_COMPASS_OWNERS_MANUAL.md
    python3 tools/index_words.py --check   exit 1 when either passage differs from the record
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import omni_index as OI  # noqa: E402

MANUAL = ROOT / "docs" / "OMNI_COMPASS_OWNERS_MANUAL.md"
INDEX = ROOT / "results" / "OMNI_INDEX.json"
SHEET = ROOT / "results" / "BENEFIT_SHEET.json"
FRONT = ("<!-- the index, front matter (tools/index_words.py) -->", "<!-- end of the index, front matter -->")
NUMBER = ("<!-- the index, the one number (tools/index_words.py) -->", "<!-- end of the index, the one number -->")
BOTTOM = ("<!-- the bottom line (tools/index_words.py) -->", "<!-- end of the bottom line -->")
ARMS = ROOT / "results" / "orchestrator" / "V21_THREE_ARMS_ABC.json"
WHOLE = ROOT / "results" / "WHOLE_SYSTEM.md"
ARM_NAMES = (("Omni on native against native", "Omni-Compass on native"),
             ("Omni direct against native", "Omni-Compass direct (Omni-Compass alone on the muscles, no Kubernetes)"))
GAUGE_NAMES = {"p95_ms": "the 95th percentile", "machines": "machines", "units": "serving units"}
ARMS_BLOCK = ("<!-- the three arms (tools/index_words.py) -->", "<!-- end of the three arms -->")
ROUTES = ("<!-- the routes (tools/index_words.py) -->", "<!-- end of the routes -->")
ARMS_MD = ROOT / "results" / "orchestrator" / "V21_THREE_ARMS_ABC.md"
OWN = ("Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.")
SHORT = OrderedDict([("Real Kubernetes (GitHub)", "real Kubernetes"),
                     ("Real database (PostgreSQL behind PgBouncer, GitHub)", "the database behind its pooler"),
                     ("Real messaging (Apache Kafka, GitHub)", "real messaging"),
                     ("Real cache (Redis, GitHub)", "the real cache"),
                     ("Real database cache (MongoDB under YCSB, GitHub)", "the database's storage-engine cache"),
                     ("Real database buffer pool (MySQL under sysbench, GitHub)", "the database's buffer pool")])


def reading(pct: float, service_pct: float | None = None) -> str:
    """A combined number with its word first, as the key prints it: 'GAIN 5.0%', 'power given 1.2%', 'STEADY 0.0%'."""
    x = 1.0 + pct / 100.0
    s = None if service_pct is None else 1.0 + service_pct / 100.0
    w = OI.index_word(round(x, 12), s)
    return f"{w} {OI.pw(x, w)}".strip()


def record() -> dict:
    d = json.loads(INDEX.read_text(encoding="utf-8"))
    row = next(r for r in json.loads(SHEET.read_text(encoding="utf-8"))["rows"]
               if r["benchmark"].startswith("Every real test together"))
    engines = OrderedDict()
    tests_per = OrderedDict()
    for t in d["tests"]:
        m = re.match(r"results/live/V(\d+)_", t["source"])
        engines.setdefault(int(m.group(1)) if m else 0, []).append(t["test"])
        tests_per[t["category"]] = tests_per.get(t["category"], 0) + 1
    return {"headline": float(d["headline_pct"]), "service": float(d["service_headline_pct"]),
            "cats": d["categories"], "scats": d["service_categories"], "tests": len(d["tests"]),
            "tests_per": tests_per, "engines": ", ".join(f"{len(v)} on omni-v{k}" for k, v in sorted(engines.items(), reverse=True)),
            "benefit": row["benefit"]}


def name(c: str) -> str:
    return SHORT.get(c, c)


def front(r: dict) -> str:
    loss = [c for c, v in r["cats"].items() if reading(v, r["scats"].get(c)).startswith("LOSS")]
    whole = ("no whole category among them" if not loss else
             f"{'one whole category' if len(loss) == 1 else f'{len(loss)} whole categories'} among them "
             f"({', '.join(name(c) for c in loss)}; section 16.6)")
    return (f"On real machines (class L, live software), the combined Omni index, work, speed and machines read together, "
            f"stands at **{reading(r['headline'])}**, and the service reading alone, work and speed, at "
            f"**{reading(r['service'])}**, judged across our three runs by the rule of 24 October (`results/OMNI_INDEX.md`; "
            f"{r['tests']} tests, each read from its own engine's newest three-run table, {r['engines']}; none pooled across "
            f"engines). The rows that read LOSS stand in their tables, {whole}, as does the pod start wait on the kind rig "
            f"(`docs/POD_START_WAIT.md`).")


def number(r: dict) -> str:
    cats = "; ".join(
        f"{name(c)} **{reading(v, r['scats'].get(c))}**"
        + (f" over its {r['tests_per'][c]} tests" if r["tests_per"].get(c, 0) > 1 and c == "Real Kubernetes (GitHub)" else "")
        for c, v in r["cats"].items())
    scats = "; ".join(f"{name(c)} {reading(v, v)}" for c, v in r["scats"].items())
    return (f"**The one number.** The Omni index over the real categories, judged across our three runs by the rule of 24 "
            f"October, each test read from its own newest table with a reading ({r['engines']}; no table is pooled across "
            f"engines): **{reading(r['headline'])}** ({cats}; each category weighed the same; Azure and the card join as "
            f"their three-run tables land). The second reading, service alone (work and speed scored, machines and energy "
            f"shown), stands at **{reading(r['service'])}** ({scats}). The benefit sheet reads the index's row "
            f"{r['benefit']}. A category enters at whatever its tables show in all three of our runs, nothing included, which "
            f"is the reader's guarantee that the number is not built from the categories that happened to work. The numbers "
            f"of earlier engines are the road, in `docs/history`, and are never read beside these.")


def cell(r: dict) -> str:
    """A three-run reading in the bottom line's words: the word, the mean size, how it held, each run's raw change."""
    rels = [100.0 * r["runs"][k]["rel"] for k in ("A", "B", "C")]
    word = r["reading"].replace("**", "").split(" in all three")[0].split(" by the mean")[0]
    how = "in all three of our runs" if "in all three" in r["reading"] else r["reading"].replace("**", "")[len(word) + 1:]
    raw = ", ".join(f"{k} {'+' if v > 0 else '−' if v < 0 else '±'}{abs(v):.1f}%" for k, v in zip("ABC", rels))
    return f"**{word} {abs(sum(rels) / 3):.1f}%** {how} (raw {raw})"


def bottom(r: dict) -> str:
    d = json.loads(ARMS.read_text(encoding="utf-8"))
    rows = {(x["pair"], x["gauge"]): x for x in d["rows"]}
    L = [f"The number is how much more work was done for the same demand, the mean of our three runs (one real test on "
         f"GitHub's own machines, class {d['class']}; `results/orchestrator/V21_THREE_ARMS_ABC.md`, engine "
         f"{d['engine'].split(' (')[0]}, commit `{d['commit'][:12]}`; section 16.1c):", "",
         "| Way to run it | Light | Work against native | Everything else the record reads |", "|---|---|---|---|",
         "| Native alone (Kubernetes' published autoscaling rule on the muscles, written by us as the yardstick) | yellow, "
         "STEADY | 0%: the baseline | — |"]
    for pair, label in ARM_NAMES:
        work = rows[(pair, "requests")]
        others = [rows[(pair, g)] for g in ("p95_ms", "machines", "units") if (pair, g) in rows]
        service_loss = any(o["reading"].replace("**", "").startswith("LOSS") for o in others if o["gauge"] == "p95_ms")
        w = work["reading"].replace("**", "")
        light = ("red, REDLINING" if service_loss or w.startswith("LOSS") else
                 "green, GAINING" if w.startswith("GAIN") else "yellow, STEADY")
        L.append(f"| {label} | {light} | {cell(work)} | " + "; ".join(f"{GAUGE_NAMES[o['gauge']]} {cell(o)}" for o in others) + " |")
    m = re.search(r"\| without the card \(the cluster, the services and the cloud\) \| every interval carried \| \*\*the index over "
                  r"work, speed and machines\*\* \| \*\*×([0-9.]+)\*\* \| \*\*([+−-][0-9.]+%)\*\* \(gauges independent ([^;]+); gauges "
                  r"correlated ([^)]+)\)", WHOLE.read_text(encoding="utf-8"))
    whole = (f"**GAIN {abs(100 * (float(m.group(1)) - 1)):.1f}%** over work, speed and machines, the cloud's layer entering as "
             f"exactly 1 (it holds), every interval carried ({m.group(4)} with the gauges correlated; `results/WHOLE_SYSTEM.md`)"
             if m else "read in `results/WHOLE_SYSTEM.md`")
    lo = min(r["cats"].items(), key=lambda kv: kv[1])
    hi = max(r["cats"].items(), key=lambda kv: kv[1])
    L += ["", f"The whole workload, composed layer by layer (a model of measurements, class S of class L and P; section 16.3b): "
              f"{whole}. It is the composition's index, not a price: a bill is the sum of the costs inside a declared boundary, "
              f"and neither route's bill is resolved yet (section 3.8). Every real test together, the Omni index of Omni-Compass "
              f"on native reads **{reading(r['headline'])}**, work, speed and machines read together, its categories from "
              f"{name(hi[0])} **{reading(hi[1], r['scats'].get(hi[0]))}** to {name(lo[0])} "
              f"**{reading(lo[1], r['scats'].get(lo[0]))}** (section 16.6)."]
    return "\n".join(L)


def arms_block() -> str:
    """Section 16.1c from the three-arm record that stands: its runs, its table as the record prints it, its totals."""
    d = json.loads(ARMS.read_text(encoding="utf-8"))
    table = [ln for ln in ARMS_MD.read_text(encoding="utf-8").splitlines() if ln.startswith("| ")]
    answered = [v[arm]["answered"] for v in d["totals"].values() for arm in ("yardstick", "omni_native", "omni")]
    bad = sum(v[arm]["failed"] + v[arm]["wrong"] for v in d["totals"].values() for arm in ("yardstick", "omni_native", "omni"))
    rows = {(x["pair"], x["gauge"]): x for x in d["rows"]}
    def mean(pair, gauge):
        x = rows.get((pair, gauge))
        return None if x is None else sum(100.0 * x["runs"][k]["rel"] for k in ("A", "B", "C")) / 3
    def said(pair):
        w, f, m, u = (mean(pair, g) for g in ("requests", "p95_ms", "machines", "units"))
        return (f"work {'+' if w >= 0 else '−'}{abs(w):.1f}%, the 95th percentile {abs(f):.1f}% {'faster' if f < 0 else 'slower'}, "
                f"machines {abs(m):.1f}% {'fewer' if m < 0 else 'more'}, serving units {abs(u):.1f}% {'more' if u > 0 else 'fewer'}")
    loss = [x for x in d["rows"] if x["reading"].replace("**", "").startswith("LOSS")]
    return "\n".join([
        "The founder's order of 23 October: native, Omni-Compass on native and Omni-Compass direct, always shown together. The test "
        "is Omni-Compass's own orchestrator (`omni_orchestrator/`, `docs/OMNI_ORCHESTRATOR.md`): native is Kubernetes' published "
        "autoscaling rule on the muscles, written by us as the yardstick (brain `yardstick`); Omni-Compass on native is Omni-Compass "
        "on top of that rule (brain `omni_native`); Omni-Compass direct is Omni-Compass alone on the muscles, no Kubernetes (brain "
        f"`omni`). Three runs on GitHub's own machines, A, B and C from one commit (`{d['commit'][:12]}`, engine "
        f"{d['engine'].split(' (')[0]}, runs {', '.join(d['runs'][k] for k in ('A', 'B', 'C'))}), the full form: 18 steps of 25 s, "
        "the clients stepping 1 2 3 2 3 4 …, the busy room rule; each pair read by the one key, paired by step "
        f"(`results/orchestrator/V21_THREE_ARMS_ABC.md`, class {d['class']}):", "", *table, "",
        f"{'No request failed and none was answered wrong' if not bad else f'{bad} requests failed or were answered wrong'} in any "
        f"arm of any run ({min(answered):,} to {max(answered):,} requests answered an arm). The means of the three runs, which the "
        f"bottom line carries: Omni-Compass on native against native, {said('Omni on native against native')}; Omni-Compass direct "
        f"against native, {said('Omni direct against native')}; Omni-Compass direct against Omni-Compass on native, "
        f"{said('Omni direct against Omni on native')}. "
        + ("No pair reads LOSS on any gauge. " if not loss else
           f"{len(loss)} rows read LOSS, each shown in the table: " + "; ".join(f"{x['pair']}, {x['label']}" for x in loss) + ". ")
        + "The test runs again on the engine that stands. " + OWN])


def routes_block() -> str:
    """Section 16.3b's places and routes from the whole-system regrouping (docs/engine/export_whole.py), every interval
    carried and by the index's rule, without the card's old run; no expectation is printed beside them."""
    import importlib.util
    import tempfile
    spec = importlib.util.spec_from_file_location("export_whole", ROOT / "docs" / "engine" / "export_whole.py")
    ew = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ew)
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "whole.json"
        import contextlib
        import io
        with contextlib.redirect_stdout(io.StringIO()):
            ew.main(str(out))
        d = json.loads(out.read_text(encoding="utf-8"))
    res = d["results"]["without"]
    def g(v):
        if v is None:
            return "not read"
        return f"{v['word']} {abs(v['pct']):.1f}%" if v["word"] != "STEADY" else f"STEADY {abs(v['pct']):.1f}%"
    def gauges(sc):
        gs = res["carried"]["scenarios"][sc]["gauges"]
        return "; ".join(f"{k} **{g(gs[k])}**" for k in ("work", "speed", "machines", "energy", "bill") if k in gs and gs[k])
    def idx(reading, sc):
        x = res[reading]["scenarios"][sc]["index"]
        lo, hi = x["correlated"]
        return f"**{x['word']} {abs(x['pct']):.1f}%** ({'+' if lo >= 0 else '−'}{abs(lo):.1f}% to {'+' if hi >= 0 else '−'}{abs(hi):.1f}%)"
    sw = res["carried"]["groups"]["software"]["gauges"]
    L = ["| Place | Measured so far (every interval carried, without the card's old run) |", "|---|---|",
         "| The software end: the cluster and the services on it (class L) | " + "; ".join(
             f"{k} **{g(sw[k])}**" for k in ("work", "speed", "machines", "energy") if k in sw and sw[k]) + " |",
         "| The bare metal: the card and the machine | not in the headline scope: the machine's own layer is not yet run, and the "
         "card's own three runs are read on their own bill (`results/TWO_BILLS.md`) |",
         "| The cloud's wire | it holds: the layer enters as exactly 1 on every gauge, its bill kept as native's |", "",
         "| Route | Light | The whole workload against native (its index; the gauges correlated) | Gauge by gauge |",
         "|---|---|---|---|"]
    for sc, label in (("onsite", "On site: the software end × the bare metal"),
                      ("cloud", "Through the cloud: the software end × the cloud's wire × the bare metal at the back end")):
        word = res["carried"]["scenarios"][sc]["index"]["word"]
        light = "green, GAINING" if word == "GAIN" else "red, REDLINING" if word == "LOSS" else "yellow, STEADY"
        L.append(f"| {label} | {light} | {idx('carried', sc)} | {gauges(sc)} |")
    L += ["", f"By the index's rule (only what held the same way in all three of our runs enters) the same routes read "
              f"{idx('index', 'onsite')} on site and {idx('index', 'cloud')} through the cloud. The bare metal enters both routes "
              "as no change until it is measured, so both routes today are the software end's and, through the cloud, the wire "
              "holding. Neither is a bill in money (section 3.8): a bill is the sum of the costs inside a declared boundary, and "
              "no figure is written for a place before its runs read it. " + OWN]
    return "\n".join(L)


def put(text: str, marks: tuple, body: str) -> str:
    a, b = marks
    i, j = text.index(a), text.index(b)
    return text[:i + len(a)] + "\n" + body + "\n" + text[j:]


def build(text: str) -> str:
    r = record()
    text = put(put(put(text, FRONT, front(r)), NUMBER, number(r)), BOTTOM, bottom(r))
    return put(put(text, ARMS_BLOCK, arms_block()), ROUTES, routes_block())


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    text = MANUAL.read_text(encoding="utf-8")
    new = build(text)
    if a.check:
        ok = new == text
        print("the index in the Owner's Manual: " + ("in line with the record" if ok else "out of date (python3 tools/index_words.py)"))
        return 0 if ok else 1
    MANUAL.write_text(new, encoding="utf-8")
    print(f"{MANUAL.relative_to(ROOT)}: the index's two passages written from the record")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
