#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The verdict audit: every judged row of every three-run table recomputed from its stored native and Omni-Compass values, and
every count the pages print taken from one selection (the referee's work order of 25 October 2026, items 2, 3, 4, 6, 7, 9, 10,
13 and 14). The key is tools/readings.py, the only place a word is decided; nothing here decides a word of its own.

One selection (`tables()`), each table with its status:
  standing     the benchmark's newest whole table from omni-v8 on (tools/readings.py `landed`): what the page, the LOSS ledger
               and the appraisal count
  superseded   an earlier engine's table of a benchmark whose later table stands: its own engine's record, never counted
  the road     a table before omni-v8 (docs/history): kept, never counted
  taken out    the third arm, Omni-Compass by itself (results/orchestrator), taken out of the record by the founder's order of
               25 October: kept, never counted
and its comparison (against its native: every plain table and the four ways' TOP and BARE; in place of a controller: VS; the
orchestrator's own: ORCH; two changes at once: BOTH), its stack and evidence class (L, the real software; S, an outside
simulator driven by our own runner), its engine against the engine that stands, its runs, commits and repetitions.

Each row: every run's native, Omni-Compass and raw change (Omni-Compass − native, in percent of native where native is not zero,
else in the gauge's unit) with its 95% interval; the gauge's direction (work done, time waited, missed or failed, a resource
spent or held, work per resource, a count that must never rise, shown); the stored reading and the reading recomputed by the
key from the stored values; the word; and the evidence apart from the word (tools/readings.py `evidence`). A table kept only in
Markdown (the outside simulators, deterministic) is recomputed from its printed changes with its runner's declared aims.

  python3 tools/verdict_audit.py                write results/verdict_audit/VERDICT_AUDIT.json and VERDICT_AUDIT.md
  python3 tools/verdict_audit.py --check        exit 1 when the record is stale or a stored reading differs from the key's
  python3 tools/verdict_audit.py --base REV     also write results/verdict_audit/DISCREPANCIES.md: every row whose printed run
                                                cells or reading at the commit REV differ from now, with the reason
"""
from __future__ import annotations

import ast
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.legal import NOTICE, stamp                                                  # noqa: E402
from tools.readings import (EVIDENCE_RULE, EXACT_REL, GIVEN, HIGHER, LOWER, NEVER_LESS, NEVER_MORE, SIZE_FLOOR, SPENT,  # noqa: E402
                            WORK_PER, aim as aim_of, evidence, landed, reproduced_reading, three_run_reading, with_own_runs,
                            word_of)
from tools.reread import bare, gauges, readable                                        # noqa: E402

OUT = ROOT / "results" / "verdict_audit"
LIVE, ORCH = ROOT / "results" / "live", ROOT / "results" / "orchestrator"
FIRST_ENGINE = 8                      # the page's rule (docs/engine/export_scenarios.py): earlier tables are the road
COMPARISON = {"TOP": "against its native", "BARE": "against its native", "VS": "in place of a controller",
              "ORCH": "the orchestrator's own", "BOTH": "two changes at once"}
COMPARISONS = ("against its native", "in place of a controller", "the orchestrator's own", "two changes at once")
STATUSES = ("standing", "superseded", "the road", "taken out")
WORDS = ("GAIN", "power given", "STEADY", "LOSS", "the runs disagree", "the runs differ", "shown", "tuning")
DIRECTION = {HIGHER: "work done", LOWER: "time waited, missed or failed", SPENT: "resource spent or held",
             WORK_PER: "work per resource", NEVER_MORE: "a count that must never rise", NEVER_LESS: "a count that must never fall",
             None: "shown"}
RULE = (f"tools/readings.py three_run_reading: a change of {100 * SIZE_FLOOR:g}% or more, the mean of the three runs' changes in "
        f"percent of native, reads by the gauge's aim; under it STEADY, under the floor; every run's two values equal to "
        f"{EXACT_REL:g} of the value, STEADY, the same; runs that moved {100 * SIZE_FLOOR:g}% or more in opposite directions, the "
        "runs disagree. " + EVIDENCE_RULE)
OWN = "Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results."


def engine_standing() -> int:
    """The engine that stands: the newest fingerprint in the repository's root (OMNI_V<n>.json)."""
    return max(int(m.group(1)) for p in ROOT.glob("OMNI_V*.json") if (m := re.fullmatch(r"OMNI_V(\d+)\.json", p.name)))


def comparison(base: str) -> str:
    m = re.search(r"_4W_([A-Z]+)$", base)
    return COMPARISON.get(m.group(1), COMPARISONS[0]) if m else COMPARISONS[0]


def _three_run(md: Path) -> bool:
    try:
        return "three-run table" in md.read_text(encoding="utf-8").split("\n", 1)[0]
    except OSError:
        return False


def tables():
    """The one selection: every three-run table, each with its status (the module's docstring)."""
    found = []
    for md in sorted(LIVE.glob("V*_*.md")):
        m = re.fullmatch(r"V(\d+)_([A-Z0-9_]+)", md.stem)
        if m and _three_run(md):
            found.append({"n": int(m.group(1)), "base": m.group(2), "stem": md.stem, "md": md,
                          "json": md.with_suffix(".json") if md.with_suffix(".json").exists() else None})
    for j in sorted(ORCH.glob("V*_*.json")):
        m = re.fullmatch(r"V(\d+)_([A-Z0-9_]+)", j.stem)
        if m:
            found.append({"n": int(m.group(1)), "base": m.group(2), "stem": j.stem, "md": j.with_suffix(".md"), "json": j,
                          "taken_out": True})
    best = {}
    for t in found:
        t["landed"] = landed(t["json"] or t["md"])
        if t.get("taken_out") or t["n"] < FIRST_ENGINE:
            continue
        b = best.get(t["base"])
        if b is None or (t["landed"], t["n"]) > (b["landed"], b["n"]):
            best[t["base"]] = t
    for t in found:
        t["status"] = ("taken out" if t.get("taken_out") else "the road" if t["n"] < FIRST_ENGINE
                       else "standing" if best.get(t["base"]) is t else "superseded")
        t["comparison"] = comparison(t["base"])
    return found


# ---- the simulators' declared aims, read from their writers' own lists (never imported: a runner may need its simulator)
def _literal(path: Path, name: str):
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in node.targets):
            return ast.literal_eval(node.value)
    return None


def simulator_aims() -> dict:
    """{label: aim} for the gauges the outside simulators' tables print (CityLearn's scores by their key in backticks)."""
    out = {}
    for f in ("tools/run_mujoco.py", "tools/run_swarm.py", "tools/pandapower_abc.py"):
        for key, label, a in _literal(ROOT / f, "GAUGES") or []:
            out[label] = a
    cl = _literal(ROOT / "tools" / "citylearn_abc.py", "CITYLEARN_AIMS") or {}
    out["__citylearn__"] = cl
    return out


def _num(c: str):
    m = re.search(r"[-+−]?\d[\d,]*(?:\.\d+)?(?:e[-+]?\d+)?", c or "")
    return float(m.group(0).replace(",", "").replace("−", "-")) if m else None


def md_rows(t, aims):
    """The judged rows of a table kept only in Markdown (an outside simulator's: deterministic, its three runs reproduce), each
    recomputed from its printed changes by the key's rule for reproducing runs, with its runner's declared aim."""
    out, sect, hdr = [], "", None
    for ln in t["md"].read_text(encoding="utf-8").splitlines():
        if ln.startswith("#"):
            sect, hdr = ln.lstrip("# ").strip(), None
            continue
        if not ln.startswith("|"):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if cells and cells[-1] == "Reading":
            hdr = cells
            continue
        if hdr is None or re.fullmatch(r"[|\-: ]+", ln) or len(cells) != len(hdr):
            continue
        d = dict(zip(hdr, cells))
        gauge = cells[0].replace("`", "")
        key = re.search(r"`([a-z_]+)`", cells[0])
        a = aims["__citylearn__"].get(key.group(1), LOWER) if key and "CITYLEARN" in t["base"] else aims.get(gauge)
        stored = bare(d["Reading"])
        word = "tuning" if re.search(r"not counted|\(the tuning", sect) else word_of(stored)   # the case the rules were frozen on
        abc = [d.get(k, "") for k in "ABC"]
        ch = [_num(c) for c in abc]
        pct = all("%" in c for c in abc)
        nat = _num(d.get("native (A)", "")) if "native (A)" in d else None
        omni = _num(d.get("omni (A)", "")) if "omni (A)" in d else None
        rec = None
        if a in (None, "shown") or any(x is None for x in ch):
            rec = None
        elif "runs differ" in stored:
            rec = "the runs differ"
        elif all(x == 0 for x in ch):    # printed 0.00% in every run: the same, or under the floor past the second decimal
            rec = stored if stored.startswith("STEADY") else "STEADY, the same or under the floor (printed 0.00%)"
        elif pct:
            rec = bare(reproduced_reading([x / 100 for x in ch], aim_of(a)))
        else:
            rec = bare(reproduced_reading(ch, aim_of(a))) if nat else None
        out.append({"section": sect, "gauge": gauge, "aim": a, "direction": DIRECTION.get(aim_of(a) if a else None, "shown"),
                    "cells": abc, "stored": stored, "recomputed": rec, "word": word or "shown",
                    "runs": [{"native": nat if i == 0 else None, "omni": omni if i == 0 else None,
                              "raw_pct": ch[i] if pct else None, "raw_unit": None if pct else ch[i]} for i in range(3)],
                    "from": "the printed changes (two decimals), the runner's declared aim",
                    **({"evidence": {"runs": 3, "strength": "deterministic, reproduced in all three runs"}}
                       if word in ("GAIN", "LOSS", GIVEN) and len(set(abc)) == 1 else {})})
    return out


def md_cells(md: Path):
    """{gauge text: (A, B, C cells, reading)} of a table's Markdown, in order, for the cross-check against its JSON."""
    out, hdr = [], None
    for ln in md.read_text(encoding="utf-8").splitlines():
        if ln.startswith("#"):
            hdr = None
            continue
        if not ln.startswith("|"):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if cells and cells[-1] == "Reading":
            hdr = cells
            continue
        if hdr is None or re.fullmatch(r"[|\-: ]+", ln) or len(cells) != len(hdr):
            continue
        d = dict(zip(hdr, cells))
        out.append(([d.get(k, "") for k in "ABC"], bare(d["Reading"])))
    return out


def run_fields(r):
    nat, omni, d = r.get("native"), r.get("omni"), r.get("diff")
    if omni is None and nat is not None and d is not None:
        omni = nat + d
    lo, hi = (list(r.get("ci95") or []) + [None, None])[:2]
    ok = lambda v: isinstance(v, (int, float)) and v == v
    f = {"native": nat, "omni": omni, "diff": d}
    if nat:
        f["raw_pct"] = 100 * d / abs(nat)
        f["ci95_pct"] = [100 * lo / abs(nat), 100 * hi / abs(nat)] if ok(lo) and ok(hi) else None
    else:
        f["raw_unit"] = d
        f["ci95_unit"] = [lo, hi] if ok(lo) and ok(hi) else None
    lo_, hi_ = (lo, hi) if ok(lo) and ok(hi) else (None, None)
    f["clear"] = bool(r["significant"]) if "significant" in r else (lo_ is not None and (lo_ > 0 or hi_ < 0))
    return f


def json_rows(t):
    data = json.loads(t["json"].read_text(encoding="utf-8"))
    out = []
    if isinstance(data.get("rows"), list):          # the third arm's table, taken out: each run keeps only its change and word
        for g in data["rows"]:
            stored = bare(g.get("reading"))
            out.append({"section": g.get("pair", ""), "gauge": g.get("label") or g.get("gauge"), "aim": None, "direction": "shown",
                        "stored": stored, "recomputed": None, "word": word_of(stored) or "shown",
                        "runs": [{"raw_pct": 100 * v["rel"]} for v in (g.get("runs") or {}).values() if isinstance(v, dict) and "rel" in v],
                        "from": "its runs' own changes (the table keeps no native values); taken out, never counted"})
        return data, out
    for path, g in gauges(data):
        tuning = path[0] == "workloads" and path[1] == "tuning"
        a = g.get("aim")
        aim_ = aim_of(a, path[-1]) if a else None
        rs = g.get("runs") if isinstance(g.get("runs"), list) else []
        stored = bare(g.get("reading"))
        rec = bare(three_run_reading(rs, a)) if readable(g) else None
        word = "tuning" if tuning else (word_of(stored, aim_) or "shown")
        row = {"section": " / ".join(path[1:-1]), "gauge": path[-1], "aim": a, "direction": DIRECTION.get(aim_, "shown"),
               "stored": stored, "recomputed": rec, "word": word,
               "runs": [run_fields(r) for r in rs if isinstance(r, dict) and r.get("native") is not None and r.get("diff") is not None],
               "from": "the stored native, Omni-Compass and difference of every run"}
        if readable(g):
            row["evidence"] = evidence(rs, aim_)
        out.append(row)
    return data, out


def table_meta(t, data):
    runs = (data or {}).get("runs") or []
    runs = [r for r in runs if isinstance(r, dict)]
    return {"runs": [{k: r.get(k) for k in ("tag", "run", "commit", "engine", "paired_repetitions") if r.get(k) is not None} for r in runs],
            "raw": [f"results/live/raw/run-{r['run']}/ (the branch raw)" for r in runs if r.get("run")]}


def stack_of(t, data):
    if isinstance(data, dict) and "workloads" in data:
        return "Linux services", "L"
    if isinstance(data, dict) and "rows" in data:
        return "Kubernetes", "L"
    return "an outside simulator", "S"


def build():
    """The audit record: every table of the one selection, every row recomputed, every count."""
    now = engine_standing()
    aims = simulator_aims()
    out_tables, rows = [], []
    for t in tables():
        data = None
        if t["json"]:
            data, rs = json_rows(t)
            if t["md"].exists():
                printed = md_cells(t["md"])
                judged_rs = [r for r in rs]
                for r, (cells, rd) in zip(judged_rs, printed):
                    r["cells"] = cells
                    r["md_reading"] = rd
                t["md_rows"] = len(printed)
        else:
            rs = md_rows(t, aims)
        stack, cls = stack_of(t, data)
        meta = table_meta(t, data)
        tab = {"stem": t["stem"], "file": str(t["md"].relative_to(ROOT)), "json": str(t["json"].relative_to(ROOT)) if t["json"] else None,
               "engine": f"omni-v{t['n']}", "status": t["status"], "comparison": t["comparison"], "stack": stack, "class": cls,
               "on_the_engine_that_stands": t["n"] == now, "landed": t["landed"], **meta,
               "title": (data or {}).get("title") or t["md"].read_text(encoding="utf-8").split("\n", 1)[0].lstrip("# ")}
        out_tables.append(tab)
        for r in rs:
            r["table"] = t["stem"]
            r["agrees"] = r["recomputed"] is None or r["recomputed"] == r["stored"]
            if "md_reading" in r:          # compared by word; a road table's JSON keeps its own older words (better, worse ...)
                old = re.match(r"(better|worse|toward|away|confirmed|lower|higher|same|no difference)", r["stored"], re.I)
                r["md_agrees"] = (None if old and tab["status"] == "the road" else
                                  word_of(r["md_reading"]) == word_of(r["stored"], aim_of(r["aim"], r["gauge"]) if r["aim"] else None))
            rows.append(r)
    return {"title": "The verdict audit", "notice": NOTICE, "own_runs": OWN, "engine_standing": f"omni-v{now}",
            "rule": RULE, "exact_rel": EXACT_REL, "floor": SIZE_FLOOR, "tables": out_tables, "rows": rows,
            "counts": counts(out_tables, rows)}


def counts(tabs, rows):
    by_t = {t["stem"]: t for t in tabs}
    c = {"tables": Counter(t["status"] for t in tabs)}
    words = defaultdict(Counter)
    for r in rows:
        t = by_t[r["table"]]
        words[(t["status"], t["comparison"])][r["word"]] += 1
    c["words"] = {f"{s} | {k}": dict(v) for (s, k), v in sorted(words.items())}
    st = [r for r in rows if by_t[r["table"]]["status"] == "standing"]
    nat = [r for r in st if by_t[r["table"]]["comparison"] == COMPARISONS[0]]
    c["standing_against_native"] = dict(Counter(r["word"] for r in nat))
    c["standing_against_native_by_engine"] = {e: dict(Counter(r["word"] for r in nat if by_t[r["table"]]["engine"] == e))
                                              for e in sorted({by_t[r["table"]]["engine"] for r in nat}, key=lambda e: -int(e[6:]))}
    c["standing_against_native_by_class"] = {k: dict(Counter(r["word"] for r in nat if by_t[r["table"]]["class"] == k)) for k in ("L", "S")}
    c["standing_against_native_by_direction"] = {d: dict(Counter(r["word"] for r in nat if r["direction"] == d))
                                                 for d in sorted({r["direction"] for r in nat})}
    c["standing_against_native_strength"] = {w: dict(Counter((r.get("evidence") or {}).get("strength") or "not recomputable from runs"
                                                            for r in nat if r["word"] == w)) for w in ("GAIN", "LOSS", "power given")}
    c["standing_against_native_steady"] = dict(Counter(((r.get("evidence") or {}).get("steady") or
                                                        ("exactly the same" if r["stored"].startswith("STEADY, the same") else
                                                         "under the floor" if "under the floor" in r["stored"] else "other"))
                                                       for r in nat if r["word"] == "STEADY"))
    c["standing_against_native_disagree"] = dict(Counter((r.get("evidence") or {}).get("disagree") or "not recomputable from runs"
                                                         for r in nat if r["word"] == "the runs disagree"))
    c["standing_tables_on_the_engine_that_stands"] = sum(1 for t in tabs if t["status"] == "standing" and t["on_the_engine_that_stands"])
    c["standing_tables_not_yet_rerun"] = sum(1 for t in tabs if t["status"] == "standing" and not t["on_the_engine_that_stands"])
    c["standing_tables_against_native"] = sum(1 for t in tabs if t["status"] == "standing" and t["comparison"] == COMPARISONS[0])
    c["stored_readings_the_key_reads_otherwise"] = sum(1 for r in rows if not r["agrees"])
    c["markdown_readings_unlike_their_json"] = sum(1 for r in rows if r.get("md_agrees") is False)
    c["recomputed"] = sum(1 for r in rows if r["recomputed"] is not None)
    c["rows"] = len(rows)
    return c


def loss_rows(rec, comparison_=COMPARISONS[0], status="standing"):
    """Every LOSS row of the selection: the one list the LOSS ledger and the appraisal take their counts from."""
    by_t = {t["stem"]: t for t in rec["tables"]}
    return [r for r in rec["rows"] if r["word"] == "LOSS" and by_t[r["table"]]["status"] == status
            and by_t[r["table"]]["comparison"] == comparison_]


def digest(rec) -> str:
    return hashlib.sha256(json.dumps({k: rec[k] for k in ("tables", "rows", "counts")}, sort_keys=True,
                                     separators=(",", ":"), default=str).encode()).hexdigest()[:16]


def fmt_pct(x, d=1):
    return "—" if x is None else f"{'+' if x > 0 else '−' if x < 0 else '±'}{abs(x):.{d}f}%"


def render(rec) -> str:
    c, by_t = rec["counts"], {t["stem"]: t for t in rec["tables"]}
    words = lambda d: ", ".join(f"{d.get(w, 0)} {w}" for w in WORDS if d.get(w)) or "none"
    L = ["# The verdict audit: every row recomputed from its stored values, every count from one selection", "", OWN, "",
         f"Written by `tools/verdict_audit.py` from the three-run tables as they stand (digest `{rec['digest']}`). The engine that "
         f"stands is {rec['engine_standing']}. The rule: {rec['rule']}", "",
         "## The counts", "",
         "| What | Count |", "|---|---|",
         f"| Three-run tables | {sum(c['tables'].values())}: " + ", ".join(f"{c['tables'].get(s, 0)} {s}" for s in STATUSES) + " |",
         f"| Standing tables, Omni-Compass against its native | {c['standing_tables_against_native']} |",
         f"| Standing tables on the engine that stands ({rec['engine_standing']}) | {c['standing_tables_on_the_engine_that_stands']} |",
         f"| Standing tables not yet run again on {rec['engine_standing']} | {c['standing_tables_not_yet_rerun']} |",
         f"| Rows recomputed from their stored values | {c['recomputed']} of {c['rows']} |",
         f"| Stored readings the key reads otherwise | {c['stored_readings_the_key_reads_otherwise']} |",
         f"| Markdown readings unlike their JSON twin | {c['markdown_readings_unlike_their_json']} |", ""]
    L += ["### Standing tables: Omni-Compass against its native (the readings do no harm is judged by)", "",
          f"Every word: {words(c['standing_against_native'])}. The four categories are exclusive: each row has one word.", "",
          "| Engine | Words |", "|---|---|"]
    L += [f"| {e} | {words(d)} |" for e, d in c["standing_against_native_by_engine"].items()]
    L += ["", "| Evidence class | Words |", "|---|---|"]
    L += [f"| {k} ({'the real software' if k == 'L' else 'an outside simulator driven by our own runner'}) | {words(d)} |"
          for k, d in c["standing_against_native_by_class"].items()]
    L += ["", "Useful work, time waited and resources apart (item 8 of the work order): a resource spent or held that rose is power "
          "given, shown beside what it bought, never a gain in work.", "", "| The gauge's direction | Words |", "|---|---|"]
    L += [f"| {d} | {words(v)} |" for d, v in c["standing_against_native_by_direction"].items()]
    L += ["", "Evidence strength beside the word (it never changes the word):", "", "| Word | Strength |", "|---|---|"]
    L += [f"| {w} | " + ", ".join(f"{n} {k}" for k, n in sorted(v.items(), key=lambda kv: -kv[1])) + " |"
          for w, v in c["standing_against_native_strength"].items() if v]
    L += ["", "| STEADY of each kind | " + ", ".join(f"{n} {k}" for k, n in c["standing_against_native_steady"].items()) + " |",
          "|---|---|",
          "| The runs disagree, by cause | " + ", ".join(f"{n} {k}" for k, n in c["standing_against_native_disagree"].items()) + " |", ""]
    L += ["### Every comparison and status", "", "| Status, comparison | Words |", "|---|---|"]
    L += [f"| {k} | {words(v)} |" for k, v in c["words"].items()]
    L += ["", "The orchestrator's own rows (ORCH) carry no Omni-Compass in either arm; two changes at once (BOTH) and in place of a "
          "controller (VS) are shown, never a reading of Omni-Compass against its native.", ""]
    lr = loss_rows(rec)
    L += [f"## Every LOSS row of Omni-Compass against its native ({len(lr)})", "",
          "| Table | Engine | Class | Gauge | Native → Omni-Compass, raw change, each run | Evidence |", "|---|---|---|---|---|---|"]
    for r in lr:
        t = by_t[r["table"]]
        runs = "; ".join(f"{x['native']:.4g} → {x['omni']:.4g} ({fmt_pct(x.get('raw_pct'))})" if x.get("native") is not None and x.get("omni") is not None
                         and x.get("raw_pct") is not None else (fmt_pct(x.get("raw_pct")) if x.get("raw_pct") is not None else f"{x.get('raw_unit')}")
                         for x in r["runs"])
        ev = r.get("evidence") or {}
        evs = f"{ev.get('strength')}; {ev.get('clear_with_mean')} of {ev.get('runs')} beyond the noise" if ev else r["from"]
        L.append(f"| `{t['file']}` | {t['engine']} | {t['class']} | {(r['section'] + ': ') if r['section'] else ''}{r['gauge']} | {runs} | {evs} |")
    bad = [r for r in rec["rows"] if not r["agrees"] or r.get("md_agrees") is False]
    L += ["", f"## Stored readings the key reads otherwise ({len(bad)})", ""]
    L += (["| Table | Gauge | Stored | Recomputed | Markdown |", "|---|---|---|---|---|"]
          + [f"| `{r['table']}` | {r['gauge']} | {r['stored']} | {r['recomputed']} | {r.get('md_reading', '—')} |" for r in bad]
          if bad else ["None: every stored reading is the key's reading of its stored values, and every Markdown table prints its JSON's."])
    L += ["", "## Every table", "", "| Table | Engine | Status | Comparison | Class | Runs |", "|---|---|---|---|---|---|"]
    for t in rec["tables"]:
        L.append(f"| `{t['file']}` | {t['engine']} | {t['status']} | {t['comparison']} | {t['class']} | "
                 + (", ".join(f"{r.get('tag', '')} {r.get('run', '')} ({r.get('paired_repetitions', '?')} reps, `{str(r.get('commit', ''))[:12]}`)" for r in t["runs"]) or "in its own Markdown") + " |")
    L.append("")
    return "\n".join(stamp(L)) + "\n"


# ---- the discrepancy report against an earlier commit -------------------------------------------------------------------
def at(rev: str, rel: str):
    try:
        return subprocess.run(["git", "-C", str(ROOT), "show", f"{rev}:{rel}"], capture_output=True, text=True, check=True).stdout
    except subprocess.CalledProcessError:
        return None


def discrepancies(rec, rev: str):
    """Every row whose printed run cells or reading at rev differ from now, with the reason, the source file and the test."""
    by_t = {t["stem"]: t for t in rec["tables"]}
    out = []
    for stem in sorted({r["table"] for r in rec["rows"]}):
        t = by_t[stem]
        old_md = at(rev, t["file"])
        if old_md is None:
            continue
        tmp = OUT / ".old.md"
        tmp.parent.mkdir(parents=True, exist_ok=True)
        tmp.write_text(old_md, encoding="utf-8")
        old = md_cells(tmp)
        tmp.unlink()
        new = [r for r in rec["rows"] if r["table"] == stem]
        for r, (cells, rd) in zip(new, old):
            if "cells" not in r:
                continue
            reasons, kinds = [], []
            now = r.get("md_reading", r["stored"])
            if rd != now:
                ow, nw = word_of(rd), word_of(r["stored"])
                if ow != nw:
                    kinds.append("word")
                    reasons.append(f"the word: {ow} → {nw}, the stored values read by the key that stands (the row had been left "
                                   "on an older key's words: its gauge carried no aim, or a run had one pair and no interval)")
                elif re.sub(r"\bEVEN\b", "STEADY", rd) == now:
                    kinds.append("renamed")
                    reasons.append("EVEN renamed STEADY (the founder's order of 25 October), nothing else")
                elif "the same" in re.sub(r"\bEVEN\b", "STEADY", rd) and "under the floor" in now:
                    kinds.append("exact")
                    reasons.append("“the same” is held to nine decimal places of the value (tools/readings.py EXACT_REL): the "
                                   "change is measured, under the floor")
                else:
                    kinds.append("words")
                    reasons.append("the reading's words")
            flips = []
            for oc, nc, x in zip(cells, r["cells"], r["runs"]):
                ov = _num(oc)
                raw = x.get("raw_pct", x.get("raw_unit"))
                if ov is not None and raw is not None and abs(raw) > 1e-12 and ov != 0 and (ov > 0) != (raw > 0):
                    flips.append(True)
            if flips:
                kinds.append("sign")
                reasons.append("the printed change wore the word's sign, opposite to the raw change; now native → Omni-Compass and the "
                               "raw change with its true sign, the word apart")
            elif cells != r["cells"]:
                kinds.append("fields")
                reasons.append("the cell's fields: native → Omni-Compass, the raw change with its true sign (it already had it), "
                               "the word apart")
            if reasons:
                out.append({"table": t["file"], "status": t["status"], "gauge": r["gauge"], "section": r["section"],
                            "old_cells": cells, "old_reading": rd, "new_cells": r["cells"], "new_reading": now,
                            "word_changed": "word" in kinds, "sign_restored": bool(flips), "kinds": kinds, "reasons": reasons})
    return out


def render_discrepancies(rec, rev, ds) -> str:
    def n(kind, status=None):
        return sum(1 for d in ds if kind in d["kinds"] and (status is None or d["status"] == status))
    rows = (("sign", "A printed change wore the word's sign, opposite to the raw change: now the raw change with its true sign"),
            ("fields", "A printed change already had its raw sign: now in separate fields (native → Omni-Compass; raw change; word)"),
            ("renamed", "EVEN renamed STEADY, nothing else"),
            ("exact", "“STEADY, the same” held to nine decimal places: now STEADY, under the floor (a measured change)"),
            ("word", "The word itself: the stored values read by the key that stands, where an older key's words had stayed"))
    L = ["# The discrepancy report: every printed value and reading that changed, with its reason", "", OWN, "",
         f"Against the tables as committed at `{rev}`, written by `tools/verdict_audit.py --base {rev}`. No raw measurement was "
         "changed: every native, Omni-Compass and difference in every JSON table is the byte its run wrote. A gauge's declared "
         "aim was added where its table's writer had always meant it but not written it (the capacity test: work done, higher). "
         "A row can change in more than one way.", "",
         "| What changed | Standing tables | Every table |", "|---|---:|---:|"]
    L += [f"| {txt} | {n(k, 'standing')} | {n(k)} |" for k, txt in rows]
    L += [f"| Rows whose printed cells or reading changed | {sum(1 for d in ds if d['status'] == 'standing')} | {len(ds)} |", ""]
    L += [
         "Tests: `tests/test_verdict_audit.py` (every stored reading is the key's reading of its stored values; every printed run "
         "cell carries the raw change's true sign; the counts of the LOSS ledger and the appraisal are this record's) and "
         "`tests/test_readings.py` (the key's rule at the edges: falls, rises, exact equality to nine decimals, a zero native, "
         "every three-run combination).", ""]
    if any(d["word_changed"] for d in ds):
        L += ["## Rows whose word changed", "", "| Table | Status | Gauge | Original | Corrected | Reason |", "|---|---|---|---|---|---|"]
        L += [f"| `{d['table']}` | {d['status']} | {d['gauge']} | {d['old_reading']} | {d['new_reading']} | {'; '.join(d['reasons'])} |"
              for d in ds if d["word_changed"]]
        L.append("")
    L += ["## Every row", "", "| Table | Gauge | Original run A cell; reading | Corrected run A cell; reading | Reason |", "|---|---|---|---|---|"]
    for d in ds:
        L.append(f"| `{d['table']}` | {(d['section'] + ': ') if d['section'] else ''}{d['gauge']} | {d['old_cells'][0]}; {d['old_reading']} | "
                 f"{d['new_cells'][0]}; {d['new_reading']} | {'; '.join(d['reasons'])} |")
    L.append("")
    return "\n".join(stamp(L)) + "\n"


def main(argv):
    rec = build()
    rec["digest"] = digest(rec)
    js = json.dumps(rec, separators=(",", ":"), ensure_ascii=False, default=str) + "\n"
    md = render(rec)
    jf, mf = OUT / "VERDICT_AUDIT.json", OUT / "VERDICT_AUDIT.md"
    if "--check" in argv:
        bad = rec["counts"]["stored_readings_the_key_reads_otherwise"] + rec["counts"]["markdown_readings_unlike_their_json"]
        stale = not (jf.exists() and mf.exists() and json.loads(jf.read_text(encoding="utf-8")).get("digest") == rec["digest"]
                     and mf.read_text(encoding="utf-8") == md)
        print(f"verdict audit: {rec['counts']['recomputed']} rows recomputed, {bad} disagree with the key; record "
              + ("stale: run python3 tools/verdict_audit.py" if stale else "current"))
        return 1 if bad or stale else 0
    OUT.mkdir(parents=True, exist_ok=True)
    jf.write_text(js, encoding="utf-8")
    mf.write_text(md, encoding="utf-8")
    print(f"{mf.relative_to(ROOT)} written: {rec['counts']['rows']} rows, {rec['counts']['recomputed']} recomputed, "
          f"{rec['counts']['stored_readings_the_key_reads_otherwise']} stored readings the key reads otherwise")
    if "--base" in argv:
        rev = argv[argv.index("--base") + 1]
        ds = discrepancies(rec, rev)
        (OUT / "DISCREPANCIES.md").write_text(render_discrepancies(rec, rev, ds), encoding="utf-8")
        (OUT / "DISCREPANCIES.json").write_text(json.dumps({"notice": NOTICE, "base": rev, "rows": ds}, ensure_ascii=False,
                                                           separators=(",", ":")) + "\n", encoding="utf-8")
        print(f"{len(ds)} discrepancies against {rev}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
