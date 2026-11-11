#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""A referee's sweep of the engine that stands, for sign-off: every number on the page computed from the repository's own
records when the tool runs, never typed; the grades are the referee's judgement on those numbers, written beside them.

    python3 tools/referee_sweep.py            (writes docs/audits/REFEREE_GRADE_2026-11-11.md)
    python3 tools/referee_sweep.py --json     (the numbers alone)

What it reads: results/OMNI_INDEX.json (the index and its categories), the verdict audit's one selection of standing tables
(tools/verdict_audit.py, the same rows the LOSS ledger and the live engine's appraisal count), results/VERIFY_RECEIPT.txt (the
release check), docs/engine/monitors.json (the page's wiring registry) and docs/ENGINE_COVERAGE.md (the coverage record).
"""
from __future__ import annotations

import collections
import json
import math
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.legal import stamp as legal_stamp                                 # noqa: E402
from tools.company_attribution import normalize as canonical_name            # noqa: E402

OUT = ROOT / "docs" / "audits" / "REFEREE_GRADE_2026-11-11.md"


def gmean_pct(xs):
    return 100 * (math.exp(sum(math.log(1 + x / 100) for x in xs) / len(xs)) - 1)


def index_numbers():
    d = json.loads((ROOT / "results" / "OMNI_INDEX.json").read_text(encoding="utf-8"))
    cats, svc = d["categories"], d["service_categories"]
    loo = {k: gmean_pct([v for kk, v in cats.items() if kk != k]) for k in cats}
    svc_loo_kafka = gmean_pct([v for k, v in svc.items() if "Kafka" not in k])
    return {"engine": d.get("index_engine"), "headline": d["headline_pct"], "service": d["service_headline_pct"],
            "categories": cats, "leave_one_out": loo, "service_without_kafka": svc_loo_kafka}


def native_rows():
    from tools.verdict_audit import build
    rec = build()
    tab = {t["stem"]: t for t in rec["tables"]}
    strength = collections.Counter()
    words = collections.Counter()
    strong_loss_gauge, strong_loss_table, engines, tables = collections.Counter(), collections.Counter(), collections.Counter(), set()
    for r in rec["rows"]:
        t = tab[r["table"]]
        if t["status"] != "standing" or t["comparison"] != "against its native":
            continue
        tables.add(r["table"])
        engines[t["engine"]] += 0
        words[r["word"]] += 1
        if r["word"] not in ("GAIN", "LOSS"):
            continue
        s = str(r.get("stored") or "")
        if "all three" in s:
            k = "all three runs"
        else:
            m = re.search(r"beyond the noise in (\d) of 3", s)
            k = f"by the mean, {m.group(1) if m else '?'} of 3 runs beyond the noise"
        strength[(r["word"], k)] += 1
        if r["word"] == "LOSS" and k == "all three runs":
            g = re.sub(r"\(.*?\)", "", r["gauge"]).strip()
            g = re.sub(r", (mean|total|95th percentile|99th percentile).*", "", g)
            strong_loss_gauge[g] += 1
            strong_loss_table[t["stem"]] += 1
    for x in tables:
        engines[tab[x]["engine"]] += 1
    return {"tables": len(tables), "engines": dict(engines), "words": dict(words),
            "strength": {f"{w}, {k}": n for (w, k), n in sorted(strength.items())},
            "strong_loss_by_gauge": strong_loss_gauge.most_common(8), "strong_loss_by_table": strong_loss_table.most_common(10)}


def release_check():
    t = (ROOT / "results" / "VERIFY_RECEIPT.txt").read_text(encoding="utf-8")
    head = t.splitlines()[0] if t else ""
    return {"passed": t.count("\nPASS"), "failed": t.count("\nFAIL"), "verdict": "PASS" if "VERIFICATION: PASS" in t else "FAIL",
            "at": head}


def wiring():
    ms = json.loads((ROOT / "docs" / "engine" / "monitors.json").read_text(encoding="utf-8"))["monitors"]
    named = [p for m in ms for k in ("python", "cpp", "proof") for p in (m.get("wire", {}).get(k) or [])]
    missing = [p for p in named if not (ROOT / p.split("::")[0].split(" ")[0]).exists()]
    return {"monitors": len(ms), "files_named": len(named), "files_missing": len(missing),
            "cpp_twin": sum(1 for m in ms if m.get("wire", {}).get("cpp")),
            "proof_test": sum(1 for m in ms if m.get("wire", {}).get("proof")),
            "awaiting": [m["id"] for m in ms if m.get("awaiting")]}


def coverage():
    t = (ROOT / "docs" / "ENGINE_COVERAGE.md").read_text(encoding="utf-8")
    m = re.search(r"\*\*(\d+)% of the engine's ([\d,]+) statements run under the tests\*\*", t)
    e = re.search(r"measured on (omni-v\d+)", t) or re.search(r"engine it was measured on \((omni-v\d+)", t)
    return {"pct": int(m.group(1)) if m else None, "statements": m.group(2) if m else None, "engine": e.group(1) if e else None}


def v26_tables():
    return sorted({re.sub(r"\.(md|json)$", "", f) for f in os.listdir(ROOT / "results" / "live") if f.startswith("V26_")})


def build():
    return {"index": index_numbers(), "native": native_rows(), "release": release_check(), "wiring": wiring(),
            "coverage": coverage(), "v26_tables": v26_tables()}


def render(d):
    ix, nv, rc, w, cv = d["index"], d["native"], d["release"], d["wiring"], d["coverage"]
    st = nv["strength"]
    sg, sl = st.get("GAIN, all three runs", 0), st.get("LOSS, all three runs", 0)
    wg = sum(v for k, v in st.items() if k.startswith("GAIN, by the mean"))
    wl = sum(v for k, v in st.items() if k.startswith("LOSS, by the mean"))
    g0, l0 = st.get("GAIN, by the mean, 0 of 3 runs beyond the noise", 0), st.get("LOSS, by the mean, 0 of 3 runs beyond the noise", 0)
    kafka = next(k for k in ix["leave_one_out"] if "Kafka" in k)
    others = [v for k, v in ix["leave_one_out"].items() if "Kafka" not in k]
    L = [
        "# A referee's sweep of the engine that stands: where it grades, and what sign-off still needs",
        "",
        "Written by `tools/referee_sweep.py`; every number below is computed from the repository's records when the tool runs. The "
        "grades are a referee's judgement on those numbers. This is our own sweep, run on our own code and our own records: no "
        "outside party has reviewed or approved it, and it is not an underwriting opinion.",
        "",
        "## The grade at a glance",
        "",
        "| What is graded | Grade | Why, in one line |",
        "|---|---|---|",
        f"| The mechanism and its mathematics | A | Python and C++ equal to the last bit on every law, sealed, every parity check with a planted-fault control; the release check {rc['verdict']} ({rc['passed']} checks) |",
        f"| Reproducibility and provenance | A- | every run's raw files kept and hashed; but omni-v26's tables are not yet written ({len(d['v26_tables'])} of its tables on main) |",
        f"| The page's wiring | A | {w['monitors']} monitors, {w['files_named']} named files, {w['files_missing']} missing; {w['cpp_twin']} with a C++ twin, the rest with the reason written |",
        f"| Statistical design | B | paired, three runs, preregistered, Student's t; but no control for many comparisons, and {g0 + l0} rows earn a word by the mean when no run is beyond the noise |",
        f"| The headline's strength | C+ | the Omni index reads GAIN, up {ix['headline']:.2f}%, but without Kafka the other five read {('down' if ix['leave_one_out'][kafka] < 0 else 'up')} {abs(ix['leave_one_out'][kafka]):.2f}% |",
        f"| Do no harm against native | C+ | {sg} rows GAIN in all three runs, {sl} LOSS in all three runs, most in the batch-queue governor tests omni-v26 was built to fix and has not yet tabled |",
        "| The chip and the cloud | D | the one A10 card's three runs disagree, no other card result stands; the cloud's bill moved inside the noise and its work was not counted |",
        "| Independence | not yet graded | nobody outside the company has run, read or checked any of it; an underwriter signs on an outside party's replication, not on ours |",
        f"| Test coverage of the engine | B | {cv['pct']}% of {cv['statements']} statements run under the tests ({cv['engine']}); the database runners run whole only in their own benchmarks |",
        "",
        "**Overall:** as an engineering mechanism, A-. As evidence a buyer or an underwriter could sign on today, C+. The gap is not "
        "the code; it is the evidence around it.",
        "",
        "## 1. The headline leans on one product",
        "",
        f"The Omni index (omni-v25's tables, work, speed and machines) reads GAIN, up {ix['headline']:.2f}%. Recomputed with each "
        "product left out in turn:",
        "",
        "| Left out | The other five |",
        "|---|---|",
    ]
    for k, v in ix["leave_one_out"].items():
        L.append(f"| {k} | {'up' if v >= 0 else 'down'} {abs(v):.2f}% |")
    L += [
        "",
        f"Without Kafka the index falls below zero, because the four data stores are charged for the memory Omni-Compass gave them "
        f"(their work and speed read GAIN or STEADY). On work and speed alone, the five without Kafka read up "
        f"{ix['service_without_kafka']:.2f}%. A referee will ask for the headline to be stated with this leave-one-out beside it, or "
        "for a headline that does not rest on one product.",
        "",
        "## 2. Against native: how strong the rows are",
        "",
        f"Every standing table that sets Omni-Compass on native against native alone: {nv['tables']} tables "
        f"({', '.join(f'{k} {v}' for k, v in sorted(nv['engines'].items()))}). The rows that read GAIN or LOSS, by how many of the "
        "three runs moved beyond the noise:",
        "",
        "| Reading | Rows |",
        "|---|---|",
    ]
    for k, n in st.items():
        L.append(f"| {k} | {n} |")
    L += [
        "",
        f"The strong rows ({sg} GAIN, {sl} LOSS in all three runs) are the ones a referee counts. The {wg + wl} by the mean carry "
        "their word under the 0.5% rule even where no single run cleared the noise; they are shown, and they are weak.",
        "",
        "Where the LOSS rows in all three runs sit:",
        "",
        "| Gauge | Rows |",
        "|---|---|",
    ]
    L += [f"| {g} | {n} |" for g, n in nv["strong_loss_by_gauge"]]
    L += ["", "| Table | Rows |", "|---|---|"]
    L += [f"| {t} | {n} |" for t, n in nv["strong_loss_by_table"]]
    L += [
        "",
        "They are the batch queue sharing a cluster with a web service under the governors (pod start waits, the queue finishing "
        "later, job turnaround), on omni-v25. omni-v26 was landed to fix that fault (`docs/OMNI_V26.md`); its reruns of those "
        "governors finished on GitHub on 8 November, but no omni-v26 table has been written from them: the omni-v25 tables were "
        "written in one tabling pass over that campaign's archived runs (6 November), and that pass has not been run for "
        "omni-v26. Until those tables land, do no harm is not shown on these workloads.",
        "",
        "## 3. What sign-off needs, in order",
        "",
        "1. **Table omni-v26's governor and Kubernetes runs** (free, already run; the tabling pass over their archived files): the "
        "batch-queue LOSS rows either clear or are root-caused again.",
        "2. **Close the Kubernetes beat question** (free, running: `docs/PACE_PREREGISTRATION.md`, amendment 7), and land the "
        "beat that reads best as the next version through the model gate; then every Kubernetes test again on it.",
        "3. **State the headline with its leave-one-out**, or name a primary endpoint per product before the next campaign, so one "
        "product cannot carry the whole.",
        "4. **Control for many comparisons**: declare the primary gauge of each test before its runs, and read the rest as "
        "secondary; a word earned with no run beyond the noise is reported as such.",
        "5. **Measure the two places beyond the software end**: the cloud's work for each dollar over three runs on one engine, and "
        "the chip's own meter on the engine that stands (both paid: each needs the owner's approval first).",
        "6. **An outside replication**: a party with no stake runs the published recipe on its own machines and writes what it "
        "finds. Nothing else turns this record into something an underwriter can sign.",
        "7. **Keep main green**: GitHub's release check failed on every push to main from 9 to 11 November, and the job that "
        "refreshes the front page failed with it on a stale release manifest; both were repaired on 11 November.",
        "",
        "## Reproduce",
        "",
        "`python3 tools/referee_sweep.py --json` prints every number above from the records it names.",
        "",
    ]
    return canonical_name("\n".join(legal_stamp(L)) + "\n")


def main(argv):
    d = build()
    if "--json" in argv:
        print(json.dumps(d, indent=1, default=str))
        return 0
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(d), encoding="utf-8")
    print(f"{OUT.relative_to(ROOT)} written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
