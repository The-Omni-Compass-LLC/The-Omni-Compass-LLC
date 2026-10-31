#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Every model-gate record read again by the one key that stands (the founder's order of 24 October 2026: a change of 0.5% or
more either way is a change, read by the gauge's aim; STEADY only under 0.5%).

Each record keeps its runs seed by seed (`per_seed`), so its readings are recomputed from those numbers with
`tools/model_gate.reading`, the record's JSON is written with them, and its page is rendered again from it: the model gate's own pages
by `tools/model_gate.render` (the engines the page named when it was first written kept, since the trees it ran in are gone), the
heartbeat ladder by `tools/beat_ladder.render`. A reading the record cannot recompute stays as it was recorded and the page says
which: a beat's own processor time against the 60 s beat of another report (a measured time is paired only inside its own
report), and the first readings a fix replaced, kept beside it. Nothing modelled is run again; class S, our own models.

  python3 tools/model_reread.py            read every record again and write it
  python3 tools/model_reread.py --check    exit 1 when any record's readings or page differ from what the rule gives
"""
from __future__ import annotations

import json
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from tools import model_gate as TG          # noqa: E402
from tools import beat_ladder as BL       # noqa: E402

DIR = ROOT / "results" / "model_gate"
SETS = (TG.GAUGES, TG.CONVEY_BATCH_GAUGES, TG.CONVEY_GAUGES, TG.CARD_GAUGES, TG.PACE_GAUGES)


def gauge_set(names):
    """The gauge set a model's rows were read by: the first that holds every one of its gauges."""
    for gs in SETS:
        if all(g in gs for g in names):
            return gs
    raise SystemExit(f"no gauge set holds {sorted(names)}")


def arms_reading(t, seeds):
    """A model of three arms (native, the standing engine, the candidate): every gauge's three pairings."""
    ps, rows = t["per_seed"], t["gauges"]
    gs = gauge_set(rows)
    for g, x in rows.items():
        nv = [ps["native"][s][g] for s in seeds]; bv = [ps["base"][s][g] for s in seeds]; cv = [ps["cand"][s][g] for s in seeds]
        x["cand_vs_base"] = TG.reading(g, [c - b for c, b in zip(cv, bv)], bv, gs)
        x["base_vs_native"] = TG.reading(g, [b - n for b, n in zip(bv, nv)], nv, gs)
        x["cand_vs_native"] = TG.reading(g, [c - n for c, n in zip(cv, nv)], nv, gs)


def pace_reading(t, seeds):
    """A pace model: every beat against the reference beat and against native, and the reference against native."""
    ps, ref = t["per_seed"], t["reference"]
    for g, x in t["reference_rows"].items():
        if g in TG.GAUGES:
            nv = [ps["native"][s].get(g, 0.0) for s in seeds]
            x["ref_vs_native"] = TG.reading(g, [ps[ref][s][g] - n for s, n in zip(seeds, nv)], nv, TG.PACE_GAUGES)
    for per, rows in t["against_reference"].items():
        for g, x in rows.items():
            rv = [ps[ref][s][g] for s in seeds]; pv = [ps[per][s][g] for s in seeds]; nv = [ps["native"][s].get(g, 0.0) for s in seeds]
            x["pace_vs_ref"] = TG.reading(g, [p - r for p, r in zip(pv, rv)], rv, TG.PACE_GAUGES)
            if g in TG.GAUGES:
                x["pace_vs_native"] = TG.reading(g, [p - n for p, n in zip(pv, nv)], nv, TG.PACE_GAUGES)


def engines_named(md: Path):
    """The standing engine and the candidate as the page named them when it was first written."""
    m = re.search(r"the standing engine (.+?), the candidate (.+?)\. Evidence class S", md.read_text(encoding="utf-8"))
    return (m.group(1), m.group(2)) if m else (None, None)


def reread_gate(js: Path, md: Path):
    r = json.loads(js.read_text(encoding="utf-8"))
    seeds = [str(s) for s in r["seeds"]]
    for model, t in r["models"].items():
        if "per_seed" not in t:
            continue
        if model.startswith("pace_"):
            pace_reading(t, seeds)
        elif "gauges" in t and {"native", "base", "cand"} <= set(t["per_seed"]):
            arms_reading(t, seeds)
    if not r.get("base_engine"):
        r["base_engine"], r["cand_engine"] = engines_named(md)
    keep_prose(r, md.read_text(encoding="utf-8"))
    return r, (lambda out: TG.render_report(r, out))


def keep_prose(r, old: str):
    """Words written into a page by hand after the gate rendered it stay with the record: the paragraph between the page's
    opening and its first model (the record's note) and a dated correction under its closing line (its afterword)."""
    body = old.split("\n---\n")[0]
    head, _, rest = body.partition("\n## ")
    paras = [p.strip() for p in head.split("\n\n") if p.strip()]
    top = [p for p in paras if not p.startswith(("# ", "> ", "Seeds "))]
    if top and not r.get("note"):
        r["note"] = "\n\n".join(top)
    tail = rest.split("Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.", 1)
    after = tail[1].strip() if len(tail) == 2 else ""
    if after and not r.get("afterword"):
        r["afterword"] = after


def reread_ladder(js: Path, md: Path):
    lad = json.loads(js.read_text(encoding="utf-8"))
    seeds = [str(s) for s in lad["seeds"]]
    for model, t in lad["models"].items():
        ps = t["per_seed"]
        for b, rows in t["rows"].items():
            for g, x in rows.items():
                pv = [ps[b][s][g] for s in seeds]; nv = [ps["native"][s].get(g, 0.0) for s in seeds]
                if g in TG.GAUGES:
                    x["vs_native"] = TG.reading(g, [p - n for p, n in zip(pv, nv)], nv, TG.PACE_GAUGES)
                if b != BL.MAIN and g not in BL.MEASURED:   # a measured time is paired only inside its own report: kept as recorded
                    rv = [ps[BL.MAIN][s][g] for s in seeds]
                    x["vs_main"] = TG.reading(g, [p - q for p, q in zip(pv, rv)], rv, TG.PACE_GAUGES)
    return lad, (lambda out: BL.render(lad, lad["sources"], out))


def records():
    for js in sorted(DIR.glob("*.json")):
        md = js.with_suffix(".md")
        if not md.exists() or js.name.startswith("HEARTBEAT_SWEEP"):
            continue                       # the heartbeat sweep is written from its own runs by tools/heartbeat_sweep.py
        d = json.loads(js.read_text(encoding="utf-8"))
        if "models" not in d:
            continue
        yield js, md, ("ladder" if "main_s" in d else "gate")


def main(argv) -> int:
    check, differ = "--check" in argv, []
    for js, md, kind in records():
        rec, write_md = (reread_ladder if kind == "ladder" else reread_gate)(js, md)
        new_js = json.dumps(rec, indent=1) + "\n"
        with tempfile.TemporaryDirectory() as t:
            out = Path(t) / md.name
            write_md(out)
            new_md = out.read_text(encoding="utf-8")
        if new_js != js.read_text(encoding="utf-8") or new_md != md.read_text(encoding="utf-8"):
            differ.append(md.name)
            if not check:
                js.write_text(new_js, encoding="utf-8"); md.write_text(new_md, encoding="utf-8")
    print(f"model reread: {len(differ)} record{'s' if len(differ) != 1 else ''} {'differ from' if check else 'read again by'} the rule that stands"
          + (f" ({', '.join(differ)})" if differ else ""))
    return 1 if check and differ else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
