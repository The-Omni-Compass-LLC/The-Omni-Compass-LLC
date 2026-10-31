# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The benchmark scoring contract, exported metric by metric and audited by a second, independent classifier (the founder's
solid-A directive of 26 October 2026, phase 4).

Every judged row of every three-run table in the verdict audit (results/verdict_audit/VERDICT_AUDIT.json, written by
tools/verdict_audit.py from the tables' own stored native, Omni-Compass and difference) is written to
docs/audit/BENCHMARK_DISCREPANCIES.csv with: the benchmark, its engine, native and Omni-Compass in each run, the raw change
100 × (omni − native) / native with its true sign (an absolute difference where native stands at zero, never a percentage
made up), the gauge's declared aim, the effect on that aim, the key's word, the class of the reading, the statistical
confidence, the practical significance, the run-to-run stability, the evidence class and the source files and runs.

The class of every reading is computed twice: once as the key reads it (the row's own word, from tools/readings.py), and once
by independent() below, written from the rule's statement and sharing no code with tools/readings.py: it recomputes each run's
difference from the stored native and Omni-Compass values themselves. A row where the two differ is a discrepancy and is listed
in docs/audit/STATISTICAL_VALIDATION.md with both readings. No measurement is changed by this tool; it reads and writes reports.

Usage: python3 tools/audit_export.py [--check]"""
from __future__ import annotations

import argparse
import csv
import io
import json
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

AUDIT = ROOT / "results" / "verdict_audit" / "VERDICT_AUDIT.json"
CSV_OUT = ROOT / "docs" / "audit" / "BENCHMARK_DISCREPANCIES.csv"
MD_OUT = ROOT / "docs" / "audit" / "STATISTICAL_VALIDATION.md"

# The rule as stated (tools/readings.py's docstrings and docs/HOW_TO_READ_THE_RESULTS.md), written again here on purpose:
FLOOR = 0.005          # a mean change under half of one percent of native is under the practical threshold
EXACT = 1e-9           # "exactly the same": every run's two values equal to nine decimal places of the value
WORK_PER = "work per resource"   # work bought with each unit of a resource: a rise is a GAIN, a fall power given

GAIN, LOSS, GIVEN, STEADY = "GAIN", "LOSS", "power given", "STEADY"
C_GAIN, C_LOSS, C_GIVEN = "GAIN", "LOSS", "POWER GIVEN"
C_EXACT, C_FLOOR, C_DISAGREE = "STEADY (EXACT)", "BELOW PRACTICAL THRESHOLD", "RUNS DISAGREE"
C_INVALID, C_SHOWN, C_TUNING, C_DIFFER = "INVALID OR MISSING", "SHOWN, NEVER JUDGED", "TUNING, NEVER COUNTED", "RUNS DIFFER IN RIG"
C_NOISE = "STATISTICALLY INCONCLUSIVE"   # an older key's STEADY, no difference beyond the noise (a table read before 24 October)

COLUMNS = ["table", "status", "comparison", "benchmark", "engine", "gauge", "metric_direction", "native_runs", "omni_runs",
           "raw_delta_runs", "raw_delta_mean", "raw_delta_mean_ci95", "performance_effect", "verdict", "classification",
           "confidence", "practical_significance", "run_stability", "evidence_class", "source", "independent_classification",
           "independent_agrees"]


def fnum(x, digits=6):
    if x is None or (isinstance(x, float) and not math.isfinite(x)):
        return ""
    return f"{x:.{digits}g}"


def signed_pct(x):
    if x is None:
        return ""
    return f"{'+' if x > 0 else '−' if x < 0 else '±'}{abs(x):.3f}%"


def run_values(row):
    """Each run's (native, omni, relative change or None, interval clear of zero or None), recomputed from the stored values."""
    out = []
    for r in row.get("runs") or []:
        nat, om = r.get("native"), r.get("omni")
        ci = r.get("ci95_pct") or r.get("ci95_unit")
        clear = None
        if ci and len(ci) == 2 and all(isinstance(v, (int, float)) and math.isfinite(v) for v in ci):
            clear = ci[0] > 0 or ci[1] < 0
        elif "clear" in r:
            clear = bool(r["clear"])
        if isinstance(nat, (int, float)) and isinstance(om, (int, float)):
            d = om - nat
            rel = d / abs(nat) if nat else None
            out.append({"native": nat, "omni": om, "diff": d, "rel": rel, "clear": clear})
        elif r.get("raw_pct") is not None:        # a table that printed only its changes (two decimals) and no values
            out.append({"native": None, "omni": None, "diff": r["raw_pct"], "rel": r["raw_pct"] / 100, "clear": clear,
                        "printed": True})
        elif r.get("raw_unit") is not None:       # ... or only its difference in the gauge's own unit
            out.append({"native": None, "omni": None, "diff": r["raw_unit"], "rel": None, "clear": clear, "printed": True})
        else:
            out.append(None)
    return out


def toward(fell, aim):
    """Whether a change that fell (or rose) went toward the gauge's declared aim."""
    if aim in ("higher", "never less"):
        return not fell
    if aim == WORK_PER:
        return not fell
    return fell                                   # lower, never more, spent


def independent(row):
    """The reading's class by the rule, from the stored values alone: (class, word)."""
    if row.get("section") == "tuning" or row.get("word") == "tuning":
        return C_TUNING, "tuning"
    aim = row.get("aim")
    if aim in (None, "shown"):
        return C_SHOWN, "shown"
    vals = run_values(row)
    if not vals or any(v is None for v in vals):
        return C_INVALID, "no value"
    if aim == "never more":
        if any(v["diff"] > 0 for v in vals):
            return C_LOSS, LOSS
        if all(abs(v["diff"]) <= 1e-12 for v in vals):
            return C_EXACT, STEADY
        return C_GAIN, GAIN
    if all(v["native"] is not None for v in vals) and all(abs(v["diff"]) <= EXACT * max(abs(v["native"]), 1e-12) for v in vals):
        return C_EXACT, STEADY
    sgn = [(v["diff"] > 0) - (v["diff"] < 0) for v in vals]
    if all(v["rel"] is not None for v in vals):
        mean = sum(v["rel"] for v in vals) / len(vals)
        big = {s for s, v in zip(sgn, vals) if s and abs(v["rel"]) >= FLOOR}
        if len(big) > 1:
            return C_DISAGREE, "the runs disagree"
        if abs(mean) < FLOOR:
            return C_FLOOR, STEADY
        fell = mean < 0
    else:                                          # a native at zero: read by the signs, no percentage
        if len({s for s in sgn if s}) > 1:
            return C_DISAGREE, "the runs disagree"
        fell = sum(v["diff"] for v in vals) < 0
    good = toward(fell, aim)
    if aim == "spent":
        return (C_GAIN, GAIN) if good else (C_GIVEN, GIVEN)
    if aim == WORK_PER:
        return (C_GAIN, GAIN) if good else (C_GIVEN, GIVEN)
    return (C_GAIN, GAIN) if good else (C_LOSS, LOSS)


NO_AIM = "not recomputable: the record declares no aim for this gauge (a table of an earlier engine, its words kept as printed)"
PRINTED = ("not recomputable at nine decimals: the committed table printed its changes to two decimals; the runner's raw "
           "files hold the values")
ROUNDED = "not recomputable: the printed changes round across the 0.5% floor"


def recomputable(row, key_cls, ind_cls):
    """Why a row's reading cannot be recomputed from the committed record, or None where it can."""
    if ind_cls == C_SHOWN and key_cls not in (C_SHOWN, C_TUNING):
        return NO_AIM
    vals = run_values(row)
    printed = bool(vals) and all(v and v.get("printed") for v in vals if v) or any(v and v.get("printed") for v in vals)
    if printed:
        if key_cls == C_EXACT or ind_cls == C_INVALID:
            return PRINTED
        rels = [v["rel"] for v in vals if v and v["rel"] is not None]
        if len(rels) == len(vals) and abs(abs(sum(rels) / len(rels)) - FLOOR) < 5e-5:
            return ROUNDED
    return None


def key_class(row):
    """The reading's class as the key wrote it (the row's stored word and its evidence)."""
    w, ev = row.get("word"), row.get("evidence") or {}
    rec = (row.get("recomputed") or row.get("stored") or "").replace("**", "")
    if w == "tuning":
        return C_TUNING
    if w == "shown":
        return C_SHOWN
    if w == "the runs differ":
        return C_DIFFER
    if w == "the runs disagree":
        return C_DISAGREE
    if w == STEADY:
        if "the same" in rec or ev.get("steady") == "exactly the same":
            return C_EXACT
        if "under the floor" in rec or ev.get("steady") == "under the floor":
            return C_FLOOR
        if "beyond the noise" in rec:
            return C_NOISE
        return C_FLOOR
    if rec.startswith("no value"):
        return C_INVALID
    return {GAIN: C_GAIN, LOSS: C_LOSS, GIVEN: C_GIVEN}.get(w, C_INVALID)


def effect(row, vals):
    aim = row.get("aim")
    if aim in (None, "shown") or not vals or any(v is None for v in vals):
        return ""
    rels = [v["rel"] for v in vals]
    if all(r is not None for r in rels):
        m = sum(rels) / len(rels)
        if abs(m) < 1e-15:
            return "no change"
        fell = m < 0
    else:
        t = sum(v["diff"] for v in vals)
        if t == 0:
            return "no change"
        fell = t < 0
    if aim == "spent":
        return "resource cut" if fell else "resource spent (what it bought is in the table's other rows)"
    if aim == WORK_PER:
        return "more work per unit" if not fell else "less work per unit (power given)"
    return "toward its aim" if toward(fell, aim) else "away from its aim"


def stability(vals):
    rels = [v["rel"] for v in vals if v and v["rel"] is not None]
    if len(rels) < 2:
        return ""
    spread = 100 * (max(rels) - min(rels))
    dirs = {(r > 0) - (r < 0) for r in rels if abs(r) >= FLOOR}
    return f"spread {spread:.3f} pp; {'one direction' if len(dirs) <= 1 else 'opposite directions'}"


def confidence(row, vals):
    ev = row.get("evidence") or {}
    if ev.get("strength"):
        k = ev.get("clear_with_mean")
        s = ev["strength"]
        s = C_NOISE.lower() if s == "inconclusive" else s
        return f"{s}; {k} of {ev.get('runs', len(vals))} runs beyond their noise the mean's way" if k is not None else s
    if ev.get("steady"):
        return ev["steady"]
    clear = [v["clear"] for v in vals if v]
    if clear and all(c is not None for c in clear):
        return f"{sum(clear)} of {len(clear)} runs beyond their noise"
    return ""


def build():
    a = json.loads(AUDIT.read_text(encoding="utf-8"))
    tables = {t["stem"]: t for t in a["tables"]}
    out = []
    for row in a["rows"]:
        t = tables[row["table"]]
        vals = run_values(row)
        rels = [v["rel"] for v in vals if v]
        mean = (100 * sum(rels) / len(rels)) if rels and all(r is not None for r in rels) else None
        ev = row.get("evidence") or {}
        ci = ev.get("mean_ci95_pct")
        if mean is None and vals and all(v for v in vals):
            raw_mean = f"absolute {fnum(sum(v['diff'] for v in vals) / len(vals))} (native at zero: no percentage)"
        else:
            raw_mean = signed_pct(mean)
        ic, iw = independent(row)
        kc = key_class(row)
        same = (ic == kc) or (kc == C_DIFFER) or (kc == C_NOISE and ic in (C_GAIN, C_LOSS, C_GIVEN, C_FLOOR))
        why = None if same else recomputable(row, kc, ic)
        runs = t.get("runs") or []
        out.append({
            "table": t["file"], "status": t["status"], "comparison": t["comparison"],
            "benchmark": f"{t.get('stack', '')}{' / ' + row['section'] if row.get('section') else ''}",
            "engine": t["engine"], "gauge": row["gauge"],
            "metric_direction": f"{row.get('aim') or 'shown'}: {row.get('direction') or ''}".strip(),
            "native_runs": "; ".join(fnum(v["native"]) if v and v["native"] is not None else "" for v in vals),
            "omni_runs": "; ".join(fnum(v["omni"]) if v and v["omni"] is not None else "" for v in vals),
            "raw_delta_runs": "; ".join(signed_pct(100 * v["rel"]) if v and v["rel"] is not None
                                        else (f"absolute {fnum(v['diff'])}" if v else "") for v in vals),
            "raw_delta_mean": raw_mean,
            "raw_delta_mean_ci95": f"{signed_pct(ci[0])} to {signed_pct(ci[1])}" if ci else "",
            "performance_effect": effect(row, vals),
            "verdict": row.get("word") or "", "classification": kc,
            "confidence": confidence(row, vals),
            "practical_significance": "" if mean is None or kc in (C_SHOWN, C_TUNING) else
                                      ("at or above the 0.5% floor" if abs(mean) >= 100 * FLOOR else "under the 0.5% floor"),
            "run_stability": stability(vals),
            "evidence_class": t.get("class", ""),
            "source": f"{t['file']}; {t.get('json') or ''}; runs " + " ".join(f"{r.get('tag', '')}:{r.get('run', '')}" for r in runs),
            "independent_classification": ic, "independent_agrees": "yes" if same else (why or "NO"),
        })
    return a, out


def render_csv(rows):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=COLUMNS, lineterminator="\n")
    w.writeheader()
    for r in rows:
        w.writerow(r)
    return buf.getvalue()


def render_md(a, rows):
    from tools.legal import stamp   # the notice under the title and at the end, written once in tools/legal.py
    st = [r for r in rows if r["status"] == "standing"]
    nat = [r for r in st if r["comparison"] == "against its native"]
    by_eng = defaultdict(Counter)
    for r in nat:
        by_eng[r["engine"]][r["classification"]] += 1
    classes = [C_GAIN, C_LOSS, C_GIVEN, C_EXACT, C_FLOOR, C_NOISE, C_DISAGREE, C_DIFFER, C_INVALID, C_SHOWN, C_TUNING]
    conf = Counter(r["confidence"].split(";")[0] for r in nat if r["classification"] in (C_GAIN, C_LOSS, C_GIVEN))
    stab = Counter(("opposite" if "opposite" in r["run_stability"] else "one") for r in nat
                   if r["classification"] in (C_GAIN, C_LOSS, C_GIVEN, C_DISAGREE) and r["run_stability"])
    bad = [r for r in rows if r["independent_agrees"] == "NO"]
    nrc = Counter((r["independent_agrees"], r["status"]) for r in rows if r["independent_agrees"] not in ("yes", "NO"))
    n_ok = sum(1 for r in rows if r["independent_agrees"] == "yes")
    eng_order = sorted(by_eng, key=lambda e: -int(e.split("-v")[1]))
    L = ["# Statistical validation: every reading reconstructed from its raw values", "",
         "Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.", "",
         f"Written by `tools/audit_export.py` from `results/verdict_audit/VERDICT_AUDIT.json` (its digest `{a['digest']}`), "
         f"which `tools/verdict_audit.py` writes from every three-run table's stored native, Omni-Compass and difference. The "
         f"engine that stands: {a['engine_standing']}. Every row is in `docs/audit/BENCHMARK_DISCREPANCIES.csv`, one line per "
         "gauge, with each run's native and Omni-Compass values, the raw change with its true sign, the key's word, its class, "
         "the confidence, the practical significance and the run-to-run stability, apart from one another.", "",
         "## The rule", "",
         "- The raw change of a run is 100 × (Omni-Compass − native) / native, with its true sign. Where native stands at zero, "
         "the absolute difference is printed and the reading goes by the signs; no percentage is made.",
         "- The gauge's declared aim decides the word, never the sign: time waited, missed or failed that fell is a GAIN; work "
         "that rose is a GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is power given, never a LOSS.",
         "- A mean change under 0.5% of native reads STEADY, under the floor (BELOW PRACTICAL THRESHOLD). STEADY, exactly the "
         "same means every run's two values equal to nine decimal places of the value (STEADY (EXACT)); a smaller change "
         "measured past that is under the floor, never \"the same\".",
         "- Runs that moved 0.5% or more in opposite directions read the runs disagree (RUNS DISAGREE), an unresolved reading.",
         "- The confidence stands beside the word and never changes it: strong, every run the mean's way and beyond its noise "
         "(its 95% interval clear of zero); moderate, all but one; weak, one; statistically inconclusive, none. A table read "
         "by the key before 24 October that printed STEADY, no difference beyond the noise is classed STATISTICALLY "
         "INCONCLUSIVE.",
         "- The three runs are three separate GitHub runs on the same engine, each holding its paired repetitions; within a "
         "run the 95% interval is the runner's own (Student t on the paired differences); across runs the interval of the "
         "mean change is Student t with 2 degrees of freedom on the three runs' changes (`omnicompass/student_t.py`).", "",
         "## The independent check", "",
         f"Every one of the {len(rows):,} rows was classed twice: as the key wrote it, and by `independent()` in "
         "`tools/audit_export.py`, written from the rule above with no code shared with `tools/readings.py` and each run's "
         "difference recomputed as Omni-Compass minus native from the stored values. "
         f"**{n_ok:,} agree; {len(bad)} differ**" + ("" if not bad else ", each listed below with both readings") + "; "
         f"{sum(nrc.values()):,} cannot be recomputed from the committed record, for the reasons counted here (none of them "
         "is changed by this report: a table's words stay as its runner printed them).",
         "", "| Why a row cannot be recomputed | the road | superseded | standing | taken out |", "|---|---:|---:|---:|---:|"]
    for why in sorted({w for w, _ in nrc}):
        L.append(f"| {why} | " + " | ".join(str(nrc.get((why, st), 0)) for st in ("the road", "superseded", "standing", "taken out")) + " |")
    L += [
         "",
         "A standing table that cannot be recomputed at nine decimals from the committed table is a traceability gap: its "
         "runner's raw files (on the branch `raw`, `scripts/raw_archive.sh open`) hold the values, and the next export reads "
         "them there.",
         "", "## Standing tables, Omni-Compass against its native, by engine", "",
         "Each benchmark's newest table on its own engine. A table on an older engine stands only until its three runs on the "
         "engine that stands land; nothing is read across engines.", "",
         "| Engine | " + " | ".join(classes) + " |", "|---|" + "---:|" * len(classes)]
    for e in eng_order:
        L.append(f"| {e} | " + " | ".join(str(by_eng[e].get(c, 0)) for c in classes) + " |")
    tot = Counter()
    for e in by_eng:
        tot.update(by_eng[e])
    L.append("| **all** | " + " | ".join(f"**{tot.get(c, 0)}**" for c in classes) + " |")
    L += ["", "## Confidence of the GAIN, LOSS and power given rows (standing, against native)", "",
          "| Confidence | Rows |", "|---|---:|"] + [f"| {k or 'not recorded (a table that printed its changes only)'} | {v} |"
                                                  for k, v in conf.most_common()]
    L += ["", "## Run-to-run stability (standing, against native, rows that moved)", "",
          "| The runs | Rows |", "|---|---:|",
          f"| moved one direction (0.5% or more) | {stab.get('one', 0)} |",
          f"| moved in opposite directions (0.5% or more) | {stab.get('opposite', 0)} |", "",
          "The rows that disagree are not resolved by this report: each is a test unstable at that gauge, to be looked into "
          "(workload instability, the shared runner, baseline drift or too few repetitions) and run again; a disagreement is "
          "never counted as a GAIN or a LOSS.", ""]
    if bad:
        L += ["## Rows the independent check reads otherwise", "", "| Table | Gauge | The key | Independent |", "|---|---|---|---|"]
        L += [f"| `{r['table']}` | {r['gauge']} | {r['classification']} | {r['independent_classification']} |" for r in bad]
        L.append("")
    L += ["## What this does not show", "",
          "- Only 12 of the 85 standing tables ran on the engine that stands; the rest stand on the engine their table names "
          "until their three runs on it land. No older table's LOSS is presumed repaired.",
          "- The classes describe the recorded runs (evidence class L: live software on GitHub's shared runners; S: our own "
          "models). They are not a claim about any other machine, workload or configuration.",
          "- A resource spent that rose is power given: what it bought is in the same table's other rows; nothing here says it "
          "was worth it."]
    return "\n".join(stamp(L)) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="fail if the written files differ from what the record gives now")
    a_ = ap.parse_args(argv)
    a, rows = build()
    c, m = render_csv(rows), render_md(a, rows)
    if a_.check:
        ok = CSV_OUT.exists() and CSV_OUT.read_text(encoding="utf-8") == c and MD_OUT.exists() and MD_OUT.read_text(encoding="utf-8") == m
        print("audit export current" if ok else "audit export stale: python3 tools/audit_export.py")
        return 0 if ok else 1
    CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
    CSV_OUT.write_text(c, encoding="utf-8")
    MD_OUT.write_text(m, encoding="utf-8")
    ok = sum(1 for r in rows if r["independent_agrees"] == "yes")
    bad = sum(1 for r in rows if r["independent_agrees"] == "NO")
    print(f"{CSV_OUT.relative_to(ROOT)}: {len(rows)} rows; {MD_OUT.relative_to(ROOT)}; independent check: {ok} agree, {bad} differ, "
          f"{len(rows) - ok - bad} not recomputable from the committed record")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
