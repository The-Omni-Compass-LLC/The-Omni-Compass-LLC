#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Every Azure run that handed in a receipt, in one record, each under the engine it ran on (the founder's words of 8 November:
"Where's the cloud? The Azures ... make sure all the most benchmark shit is sitting in there. I don't care what version").

Each run of the workflow `aks-metered` whose files are on the branch `raw` handed in its own receipt
(`run-<id>/live-reps-aks/LIVE_REPS.json`, written by `tools/live_reps.py` in the run's own aggregate job). This tool reads every
one of them as it stands, names the engine of the run's commit (`tools/omni_version.py --commit`), and writes one row a run and
one table a run, every number the receipt's own and every word by the one key (`tools/readings.py`: a change of 0.5% or more
of native's value is a change, read by what the gauge is for; a resource spent that rose is power given, never a loss). A run
is never read across engines and no two runs are pooled: each run's word stands by itself (the founder's order of 31 October).

What a run is, from its title and the record: a counted set (steady, a burst, the real day; at the tune-down on the machines
alone until 31 October, the founder's order of 14 October), a set under the stopping rule (up to 100 paired repetitions), or a
tuning case (the work meter at the max, one repetition, run once before the counted A, B and C to freeze their rates; never
counted, `docs/K8S_COMPASS_PREREGISTRATION.md`, the amendment of 31 October, night).

The runs' own records (title, commit, start and end, conclusion) are GitHub's: read with `gh` where a token is present and kept
in `results/live/AZURE_RUNS.json`, which also keeps each commit's engine (an engine never changes for a commit).

    python3 tools/azure_record.py           writes results/live/AZURE_RECORD.md and results/live/AZURE_RECORD.json
    python3 tools/azure_record.py --check   exits 1 where either differs from the receipts
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "docs" / "engine"))
from legal import stamp  # noqa: E402
import readings as K  # noqa: E402

RUNS = ROOT / "results" / "live" / "AZURE_RUNS.json"
OUT_JSON, OUT_MD = ROOT / "results" / "live" / "AZURE_RECORD.json", ROOT / "results" / "live" / "AZURE_RECORD.md"
RECEIPT = "live-reps-aks/LIVE_REPS.json"

WORK = "work inside the response line (requests a second; the capacity test's own gauge)"
WORK_DOLLAR = "work per dollar of the bill (answers inside the line for each $; the cloud's judged number)"
ALERT = "alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line)"
# the gauges a row shows, each with its short name and its aim (what it is for); every gauge of the receipt is in its own table
GAUGES = (
    (WORK, "work inside the line", K.HIGHER),
    (WORK_DOLLAR, "work per dollar", K.WORK_PER),
    ("compute bill at list price ($)", "the bill", K.SPENT),
    ("machines billed, machine-hours", "machine-hours", K.SPENT),
    ("response time (ms), 95th percentile", "95th percentile", K.LOWER),
    ("response time (ms), 99th percentile", "99th percentile", K.LOWER),
    ("time over the response line (% of samples)", "time over the line", K.LOWER),
    ("failed requests (%)", "failed requests", K.NEVER_MORE),
    (ALERT, "alert minutes", K.LOWER),
    ("time pods had no machine to take them, pod-minutes", "pods with no machine", K.LOWER),
)
ROW = ("work inside the line", "the bill", "95th percentile", "99th percentile", "failed requests", "time over the line")
SHOWN = {"CPU used (cores), mean", "utilisation (used / allocatable)", "Omni's own CPU (cores), mean", "CPU used with Omni's own (cores), mean",
         "energy per core-hour (Wh)", "pending pods, pod-minutes", "settings commands the governor wrote on its own (no person touched either arm)",
         "HPA replicas, mean", "pods started"}
WHY = {
    K.HIGHER: "work done: more work is more output from the same organism",
    K.WORK_PER: "work bought with each dollar of the bill: more is more work for the bill",
    K.SPENT: "a resource the bill pays for: a fall is a cut, a rise is power given beside what it bought, never a loss",
    K.LOWER: "time waited, missed or failed: less helps the system, more hurts it",
    K.NEVER_MORE: "a count that must never rise: any rise hurts the system and reads LOSS, with no floor",
}
# what the record says of a run beyond its receipt (from docs/RUN_LEDGER.md and docs/REPAIR_20261106.md, each with its page)
NOTES = {
    40069633316: "97 of its 100 paired repetitions passed (repetitions 82, 90 and 93 failed); its table is `results/live/AKS_STEADY_100_OMNI_V18.md`",
    40940616527: ("it ended in failure on 3 November with 27 of its 100 repetitions refused, 26 of them by one fault of the rig's evidence tool "
                  "(the pod watch's expired history, native and Omni-Compass arms alike; repaired 6 November, `docs/REPAIR_20261106.md`); the "
                  "refused repetitions stay refused and the set is read in no three-run table"),
    38455383137: "cancelled on 14 October before the set's end; its receipt reads the repetitions it finished",
}


def git(*a) -> str:
    r = subprocess.run(["git", "-C", str(ROOT), *a], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def raw_ref():
    import export_runs as XR
    return XR.raw_ref()


def read_runs(check: bool) -> dict:
    """GitHub's records of every aks-metered run: fresh from gh where a token is present (never under --check), else as kept."""
    kept = json.loads(RUNS.read_text(encoding="utf-8")) if RUNS.exists() else {"runs": [], "engines": {}}
    if check or not shutil.which("gh") or not (os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")):
        return kept
    from repo import NAME as REPO  # noqa: E402
    r = subprocess.run(["gh", "run", "list", "-R", REPO, "--workflow", "aks-metered.yml", "--limit", "200", "--json",
                        "databaseId,displayTitle,status,conclusion,createdAt,updatedAt,headSha,headBranch"], capture_output=True, text=True, cwd=ROOT)
    try:
        got = json.loads(r.stdout or "[]") if r.returncode == 0 else None
    except json.JSONDecodeError:
        got = None
    if not got:
        return kept
    by = {x["id"]: x for x in kept["runs"]}
    for x in got:
        by[x["databaseId"]] = {"id": x["databaseId"], "title": x["displayTitle"], "status": x["status"], "conclusion": x["conclusion"] or None,
                               "created": x["createdAt"], "updated": x["updatedAt"], "sha": x["headSha"], "branch": x["headBranch"]}
    import datetime
    kept["runs"] = sorted(by.values(), key=lambda x: x["id"])
    kept["read_at"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    kept["source"] = "GitHub's own run records of the workflow aks-metered (gh run list)"
    return kept


def engine_of(sha: str, engines: dict, check: bool):
    if sha in engines:
        return engines[sha]
    if check:
        return None
    if subprocess.run(["git", "-C", str(ROOT), "cat-file", "-e", sha + "^{commit}"], capture_output=True).returncode:
        shallow = git("rev-parse", "--is-shallow-repository").strip() == "true"
        subprocess.run(["git", "-C", str(ROOT), "fetch", "-q", *(["--depth", "1"] if shallow else []), "origin", sha], capture_output=True)
    out = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py"), "--commit", sha], capture_output=True, text=True, cwd=ROOT).stdout
    m = re.search(r"(omni-v\d+) \(digest", out)
    engines[sha] = m.group(1) if m else None
    return engines[sha]


def kind(title: str) -> tuple[str, str]:
    """What the set is, from its title: (the set, how it counts)."""
    t = title.replace("aks-metered", "").strip()
    if "work meter" in t:
        rates = re.search(r"work meter ([\d ]+?) dial", t)
        return f"the work meter at rates {rates.group(1).strip() if rates else '?'} a second", "tuning case: sets the counted rates, never counted"
    m = re.search(r"burst ([\d ]+?) replica", t) or re.search(r"burst ([\d ]+?) dial", t)
    if m:
        steps = m.group(1).strip()
        name = "the real day on 1 to 9 (Google 2011)" if len(steps.split()) > 12 else f"the burst {steps}"
        return name, "counted set"
    if "steady" in t or not t:
        return ("the steady set" + (" under the stopping rule" if "stopping rule" in t else "")), "counted set"
    return t, "counted set"


def pct(g):
    n, d = g.get("native"), g.get("diff")
    return None if n in (None, 0) or d is None else 100.0 * d / abs(n)


def reading(g, aim_, reps: int) -> dict:
    """One run's own word on one gauge: the change of 0.5% or more of native's value read by the gauge's aim, STEADY under it,
    with whether the run's paired 95% interval stands clear of zero (one repetition has no interval)."""
    p = pct(g)
    if aim_ == K.NEVER_MORE and g.get("diff") is not None:   # tools/readings.py: any rise is LOSS, no floor; no rise and fewer, GAIN or STEADY
        d0 = g["diff"]
        w = K.LOSS if d0 > 0 else K.STEADY if abs(d0) <= 1e-12 else f"{K.GAIN} or {K.STEADY}"
    else:
        w = K.run_word(g, aim_) if p is not None else None
    if w is None:
        return {"word": None, "change_pct": p}
    noise = "one repetition, no interval" if reps < 2 else ("beyond the noise" if K.significant(g) else "inside the noise")
    d = "unchanged" if not p else ("up" if p > 0 else "down")
    if p is None:
        text = f"{w}, {'up' if g['diff'] > 0 else 'down' if g['diff'] < 0 else 'unchanged'} from zero to {g.get('omni'):.3g}" if g.get("diff") else w
    else:
        text = w if w == K.STEADY and abs(p) < 100 * K.SIZE_FLOOR else f"{w}, {d} {abs(p):.1f}%"
    return {"word": w, "change_pct": None if p is None else round(p, 3), "text": f"{text} ({noise})", "noise": noise, "native": g.get("native"),
            "omni": g.get("omni"), "ci95": g.get("ci95"), "why": WHY.get(aim_, "")}


def build(check: bool = False) -> dict:
    meta = read_runs(check)
    engines = dict(meta.get("engines") or {})
    ref, pre = raw_ref()
    out = []
    for r in sorted(meta["runs"], key=lambda x: x["id"]):
        txt = git("show", f"{ref}:{pre}run-{r['id']}/{RECEIPT}")
        if not txt:
            continue
        try:
            lr = json.loads(txt)
        except json.JSONDecodeError:
            continue
        key = next(iter(lr.get("paired") or {}), None)
        if not key:
            continue
        arm = lr["paired"][key]
        reps_by = lr.get("repetitions") or {}
        base = key.split("|")[-1] if "|" in key else "native"
        paired = len(set(reps_by.get(key.split("|")[0]) or []) & set(reps_by.get(base) or []))
        eng = engine_of(r["sha"], engines, check)
        the_set, counts = kind(r["title"])
        gauges = {}
        for g, short, aim_ in GAUGES:
            if g in arm:
                gauges[short] = reading(arm[g], aim_, paired)
        every = []
        for g, v in arm.items():
            a = next((x[2] for x in GAUGES if x[0] == g), None)
            if a is None and g not in SHOWN:
                a = K.aim(K.LOWER, "energy" if "energy" in g else ("machines" if "node" in g or "worker" in g else g))
            every.append({"gauge": g, "native": v.get("native"), "omni": v.get("omni"), "change_pct": None if pct(v) is None else round(pct(v), 3),
                          "ci95": v.get("ci95"), "significant": v.get("significant"),
                          "word": None if g in SHOWN else (reading(v, a, paired).get("text") if a else None)})
        dial = "max" if "dial max" in r["title"] else ("save (the tune-down, the machines alone)" if "dial save" in r["title"] else "the engine's default of the day")
        out.append({"id": r["id"], "title": r["title"], "engine": eng, "commit": r["sha"], "branch": r.get("branch"), "started": r.get("created"),
                    "ended": r.get("updated"), "conclusion": r.get("conclusion"), "set": the_set, "counts": counts, "dial": dial,
                    "paired_repetitions": paired, "arm": key, "receipt": f"raw:run-{r['id']}/{RECEIPT}", "note": NOTES.get(r["id"]),
                    "gauges": gauges, "every_gauge": every})
    with_receipt = {x["id"] for x in out}
    pending = [{"id": r["id"], "title": r["title"], "engine": engine_of(r["sha"], engines, check), "conclusion": r.get("conclusion"),
                "started": r.get("created")} for r in meta["runs"] if r["id"] not in with_receipt and r.get("conclusion") == "success"]
    return {"read_at": meta.get("read_at"), "source": meta.get("source"), "raw": f"{ref}" + (f":{pre}" if pre else ""),
            "runs": out, "finished_without_a_receipt_on_raw": pending, "engines": engines, "meta": meta}


def cell(x):
    if not x or not x.get("word"):
        return "—"
    return x["text"].replace(" (", "<br>(", 1)


def markdown(d: dict) -> str:
    runs = d["runs"]
    by_engine = {}
    for x in runs:
        by_engine.setdefault(x["engine"] or "no declared engine", []).append(x)
    counted = [x for x in runs if x["counts"] == "counted set"]
    L = ["# Azure: every run that handed in a receipt, each under its own engine", "",
         f"Written by `tools/azure_record.py` from each run's own receipt on the branch `raw` (`run-<id>/{RECEIPT}`, written by "
         "`tools/live_reps.py` in the run's own aggregate job); `results/live/AZURE_RECORD.json` is the same in a form a page reads. "
         f"The runs' own records (title, commit, start, end, conclusion) are GitHub's, read {d.get('read_at') or 'as kept'}; each "
         "run's engine is the one its commit stands on (`tools/omni_version.py --commit`). Evidence class **L** (live software on "
         "Azure Kubernetes Service, the bill metered: Azure's own count of the machines it billed every 15 s, priced at list).", "",
         f"**{len(runs)} Azure runs handed in a receipt**: {len(counted)} counted sets and {len(runs) - len(counted)} tuning cases, on "
         f"{len(by_engine)} engines ({', '.join(sorted(by_engine, key=lambda e: int(re.sub(r'[^0-9]', '', e) or 0)))}). Each run's "
         "word stands by itself, on its own number, by the one key; no two runs are pooled and no run is read across engines. A set "
         "of five repetitions has wide intervals: its words say what it measured, and how many of them stand beyond the noise. The "
         "sets before 31 October ran at the tune-down on the machines alone (the founder's order of 14 October, struck on 31 "
         "October): there Omni-Compass only parked a machine the cloud already made, so the work could not grow and the service "
         "rows read the noise of the same pods. The sets at the max on the work meter start after their tuning cases.", "",
         "How to read a cell: the word first (GAIN, STEADY, LOSS, power given), then the direction and size of the change against "
         "native in words, then whether the run's paired 95% interval stands clear of zero. Why a word reads so: " +
         "; ".join(f"{WHY[a]}" for a in (K.HIGHER, K.WORK_PER, K.SPENT, K.LOWER, K.NEVER_MORE)) + ".", "",
         "## Every run, newest first", "",
         "| Run | Engine | Set | Counts | Paired repetitions | Work inside the line | The bill | 95th percentile | 99th percentile | Failed requests | Time over the line |",
         "|---|---|---|---|---:|---|---|---|---|---|---|"]
    for x in sorted(runs, key=lambda x: -x["id"]):
        g = x["gauges"]
        L.append(f"| [{x['id']}](#run-{x['id']}) | {x['engine'] or 'no declared engine'} | {x['set']} | {x['counts']} | {x['paired_repetitions']} | "
                 + " | ".join(cell(g.get(k)) for k in ROW) + " |")
    if d["finished_without_a_receipt_on_raw"]:
        L += ["", "Finished on GitHub, its files not yet on `raw` (the hourly archive takes them; `archive-run.yml`): " +
              "; ".join(f"run {p['id']} ({p['engine'] or 'no declared engine'}, {kind(p['title'])[0]}, started {str(p['started'])[:10]})"
                        for p in d["finished_without_a_receipt_on_raw"]) + "."]
    L += ["", "## Each run, every gauge of its receipt", ""]
    for x in sorted(runs, key=lambda x: -x["id"]):
        L += [f"### Run {x['id']}", "", f'<a id="run-{x["id"]}"></a>', "",
              f"`aks-metered`, {x['title'].replace('aks-metered', '').strip() or 'the steady set'}; engine **{x['engine'] or 'no declared engine (its commit matches no declared fingerprint)'}** "
              f"(commit `{x['commit'][:10]}`, branch `{x['branch']}`); started {str(x['started'])[:16].replace('T', ' ')} UTC, ended "
              f"{str(x['ended'])[:16].replace('T', ' ')} UTC; GitHub's conclusion **{x['conclusion']}**; {x['paired_repetitions']} paired "
              f"repetition{'s' if x['paired_repetitions'] != 1 else ''}; the dial {x['dial']}; {x['counts']}. Receipt `{x['receipt']}`."
              + (f" The record: {x['note']}." if x.get("note") else ""), "",
              "| Gauge | native | Omni-Compass on native | Change against native | 95% interval of the difference | Reading |", "|---|---:|---:|---:|---:|---|"]
        for e in x["every_gauge"]:
            n, o, c, ci = e["native"], e["omni"], e["change_pct"], e["ci95"]
            f = lambda v: "—" if v is None or v != v else f"{v:.4g}"  # noqa: E731
            cc = "—" if c is None else f"{'up' if c > 0 else 'down' if c < 0 else 'unchanged'} {abs(c):.1f}%"
            iv = "—" if not ci or None in ci else f"{f(ci[0])} to {f(ci[1])}"
            L.append(f"| {e['gauge']} | {f(n)} | {f(o)} | {cc} | {iv} | {e['word'] or 'shown, not judged'} |")
        L.append("")
    L += ["Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.", ""]
    return "\n".join(stamp(L)) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    d = build(check=a.check)
    js, md = json.dumps({k: v for k, v in d.items() if k not in ("engines", "meta")}, indent=1, ensure_ascii=False) + "\n", markdown(d)
    if a.check:
        if not d["runs"]:   # the branch raw is not fetched on this machine: nothing to read the receipts from, so nothing is compared
            print("the Azure record: not checked here (the branch raw is not fetched; scripts/raw_archive.sh fetch)")
            return 0
        bad = [p.relative_to(ROOT).as_posix() for p, s in ((OUT_JSON, js), (OUT_MD, md)) if not p.exists() or p.read_text(encoding="utf-8") != s]
        print("the Azure record: " + ("in line with every run's own receipt" if not bad else "out of date: " + ", ".join(bad) + " (python3 tools/azure_record.py)"))
        return 1 if bad else 0
    meta = dict(d["meta"], engines=d["engines"])
    RUNS.write_text(json.dumps(meta, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_JSON.write_text(js, encoding="utf-8")
    OUT_MD.write_text(md, encoding="utf-8")
    print(f"{OUT_MD.relative_to(ROOT)}: {len(d['runs'])} Azure runs with their own receipts, "
          f"{len(d['finished_without_a_receipt_on_raw'])} finished with their files not yet on raw")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
