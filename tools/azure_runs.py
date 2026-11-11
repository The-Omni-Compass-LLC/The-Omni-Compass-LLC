# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Every Azure run GitHub recorded, and where its receipt lives (results/live/AZURE_RUNS.md).

The founder's order of 8 November: "There's a whole bunch of Azure runs that you better have in there ... all the receipts
benchmarked and pushed in GitHub wherever they live, so that when somebody looks, they can find them." Every run of the two
Azure workflows (`aks-metered`, `aks-metered-full`) is one row: when it ran, the set, how it ended, the engine its commit
carries, its pairs, the bill, the machine-hours and the 95th percentile from its own receipt, where its files are, and what
counts it. The records (results/live/AZURE_RUN_RECORDS.json) are GitHub's own run records, read through GitHub's API, with
each run's engine (`tools/omni_version.py --commit`), whether the branch `raw` holds its folder, its receipt's means, and the
three-run table that names it.

  python3 tools/azure_runs.py                          write results/live/AZURE_RUNS.md from the records
  python3 tools/azure_runs.py --check                  exit 1 when the page differs from the records
  python3 tools/azure_runs.py --refresh RUNS.json --raw PATH
                                                       build the records again from a saved GitHub run list (the API's
                                                       workflow_runs, one list a workflow) and a clone holding the branch raw
"""
from __future__ import annotations

import argparse
import json
import math
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
RECORDS, OUT = ROOT / "results" / "live" / "AZURE_RUN_RECORDS.json", ROOT / "results" / "live" / "AZURE_RUNS.md"
WORKFLOWS = ("aks-metered.yml", "aks-metered-full.yml")
GAUGES = [("compute bill at list price ($)", "the bill ($)"), ("machines billed, machine-hours", "machine-hours"),
          ("response time (ms), 95th percentile", "95th percentile (ms)")]
TABLE_DIRS = ("results/live", "results/orchestrator", "results/gpu")
# what the record says of a run no table names (docs/RUN_LEDGER.md, docs/REPAIR_20261106.md)
NOTES = {40940616527: "read in no table: 26 of its 27 refused repetitions were the pod watch's expired history, repaired "
                      "6 November (`docs/REPAIR_20261106.md`)"}


def _git(repo, *a):
    return subprocess.run(["git", "-C", repo, *a], capture_output=True, text=True).stdout


def refresh(runs_file: str, raw: str) -> dict:
    data = json.loads(Path(runs_file).read_text(encoding="utf-8"))
    names = _git(raw, "ls-tree", "--name-only", "origin/raw").split()
    folder = {m.group(1): n for n in names for m in [re.fullmatch(r"(?:.*-)?run-(\d+)", n)] if m}
    named = {}
    for d in TABLE_DIRS:
        # a table names its runs in its record or, for the older Azure tables, only on its page; this page and its records
        # are left out, so no run is said to be counted by the list of runs itself
        for p in sorted((ROOT / d).glob("*.json")) + sorted((ROOT / d).glob("*.md")):
            if p.name.startswith("AZURE_RUN"):
                continue
            text = p.read_text(encoding="utf-8", errors="replace")
            for rid in set(re.findall(r"\b(\d{11})\b", text)):
                named.setdefault(rid, []).append(str(p.relative_to(ROOT).with_suffix(".md")))
    engines, out = {}, []
    for wf in WORKFLOWS:
        for r in data[wf]["runs"]:
            sha = r.get("head_sha") or ""
            if sha and sha not in engines:
                v = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py"), "--commit", sha], cwd=ROOT,
                                   capture_output=True, text=True).stdout
                m = re.search(r"^(omni-v\d+) \(digest", v, re.M)
                engines[sha] = m.group(1) if m else "no declared version"
            rid = str(r["id"])
            rec = {"id": r["id"], "workflow": wf, "title": r.get("display_title"), "conclusion": r.get("conclusion") or r.get("status"),
                   "created": r.get("created_at"), "updated": r.get("updated_at"), "sha": sha, "engine": engines.get(sha, "unread"),
                   "folder": folder.get(rid), "tables": sorted(set(named.get(rid, []))), "receipt": None}
            if rec["folder"]:
                listing = _git(raw, "ls-tree", "-r", "origin/raw", rec["folder"] + "/")
                f = next((ln for ln in listing.splitlines() if ln.endswith("/LIVE_REPS.json") and "_omni_legal" not in ln), None)
                if f:
                    oid = f.split()[2]
                    _git(raw, "-c", "fetch.negotiationAlgorithm=noop", "fetch", "-q", "--no-write-fetch-head", "--no-tags", "origin", oid)
                    j = json.loads(_git(raw, "cat-file", "-p", oid).replace("NaN", "null") or "{}")
                    means = {}
                    for g, _ in GAUGES:
                        n = (j.get("means", {}).get("native") or {}).get(g)
                        o = (j.get("means", {}).get("compass") or {}).get(g)
                        if isinstance(n, (int, float)) and isinstance(o, (int, float)) and not (math.isnan(n) or math.isnan(o)):
                            means[g] = {"native": n, "omni": o}
                    reps = j.get("repetitions") or {}
                    rec["receipt"] = {"path": f.split("\t", 1)[1], "pairs": len(set(reps.get("native", [])) & set(reps.get("compass", []))),
                                      "means": means}
            out.append(rec)
    out.sort(key=lambda x: x["created"] or "", reverse=True)
    return {"read": "GitHub's own run records of aks-metered and aks-metered-full (read through GitHub's API on 8 and 11 November "
                    "2026) and the branch raw's tree", "runs": out}


def standing(r: dict) -> str:
    if r["tables"]:
        return "named in: " + ", ".join(f"`{t}`" for t in r["tables"])
    if r["id"] in NOTES:
        return NOTES[r["id"]]
    rc = r.get("receipt") or {}
    if "work meter" in (r.get("title") or "") and rc.get("pairs") == 1:
        return "a tuning case of the work-meter set: it set the counted rates and is never counted (`docs/K8S_COMPASS_PREREGISTRATION.md`)"
    if r["conclusion"] == "cancelled" and not r.get("folder"):
        return "cancelled; no files handed in (most such runs waited behind a running set and never started)"
    if not r.get("folder"):
        return "no folder on the branch `raw`" + (" (requested for the archive)" if r["conclusion"] in ("success", "failure") else "")
    if rc.get("pairs"):
        return f"archived with its receipt, {rc['pairs']} pairs; read in no three-run table (an engine since replaced it)"
    return "archived; no receipt in its folder"


def change(m: dict) -> str:
    n, o = m["native"], m["omni"]
    if not n:
        return f"{n:g} → {o:g}"
    pct = (o / n - 1.0) * 100.0
    fmt = (lambda x: f"{x:,.0f}") if max(abs(n), abs(o)) >= 1000 else (lambda x: f"{x:.4g}")
    return f"{fmt(n)} → {fmt(o)}, raw {'up' if pct > 0 else 'down'} {abs(pct):.1f}%"


def render(rec: dict) -> str:
    from tools.legal import stamp
    runs = rec["runs"]
    by = {}
    for r in runs:
        by[r["conclusion"]] = by.get(r["conclusion"], 0) + 1
    url = "https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC/actions/runs/"
    lines = ["# Every Azure run, and where its receipt lives", "",
             f"Every run of the two Azure workflows that GitHub recorded, {len(runs)} in all ("
             + ", ".join(f"{v} {k}" for k, v in sorted(by.items())) + "), newest first, read from "
             "`results/live/AZURE_RUN_RECORDS.json`: " + rec["read"] + ". Each number is one run's means, native against "
             "Omni-Compass on native, with its raw change: it is not a three-run reading, and only a three-run table reads GAIN, "
             "STEADY or LOSS (the tables this page names). A run's folder opens with `scripts/raw_archive.sh open /<folder>/`. "
             "Written by `python3 tools/azure_runs.py`; `verify.py` fails a push where it differs from the records. Run and "
             "scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these "
             "results.", "",
             "| Run | Started (UTC) | Workflow and set | Outcome | Engine | Pairs | " + " | ".join(g[1] for g in GAUGES)
             + " | Its files | Standing |",
             "|---|---|---|---|---|---:|" + "---|" * len(GAUGES) + "---|---|"]
    for r in runs:
        rc = r.get("receipt") or {}
        means = rc.get("means") or {}
        cells = [change(means[g]) if g in means else "—" for g, _ in GAUGES]
        lines.append(f"| [{r['id']}]({url}{r['id']}) | {(r['created'] or '')[:16].replace('T', ' ')} | {r['title']} | "
                     f"{r['conclusion']} | {r['engine']} | {rc.get('pairs') or '—'} | " + " | ".join(cells)
                     + f" | {'`' + r['folder'] + '/`' if r.get('folder') else 'none'} | {standing(r)} |")
    lines.append("")
    return "\n".join(stamp(lines)) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--refresh", default="")
    ap.add_argument("--raw", default="")
    a = ap.parse_args(argv)
    if a.refresh:
        RECORDS.write_text(json.dumps(refresh(a.refresh, a.raw or str(ROOT)), indent=1) + "\n", encoding="utf-8")
    md = render(json.loads(RECORDS.read_text(encoding="utf-8")))
    if a.check:
        ok = OUT.exists() and OUT.read_text(encoding="utf-8") == md
        print("azure runs: results/live/AZURE_RUNS.md is what its records give" if ok else
              "azure runs: results/live/AZURE_RUNS.md differs from its records: python3 tools/azure_runs.py")
        return 0 if ok else 1
    OUT.write_text(md, encoding="utf-8")
    print(f"results/live/AZURE_RUNS.md: {md.count(chr(10) + '| [')} runs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
