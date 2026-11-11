# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Why the Kubernetes index read +28.0351% on omni-v21 and +20.4633% on omni-v25: the numbers of
docs/audits/K8S_V21_V25_DECLINE_2026-11-11.md, read again from the repository's own files.

It reads, and changes nothing:
  the two index files    results/OMNI_INDEX.json as committed on 31 October (3ad522226bf3, omni-v21's nine Kubernetes tables)
                         and on 5 November (79344173670c, omni-v25's nine), each workload's score and measures, and each
                         workload's share of the fall (its change in ln(1 + score) over nine)
  the two engines        which fingerprinted files moved between omni-v21 and omni-v25, and which of them the Kubernetes
                         governor runs (tools/carry.py's import closure)
  the 54 runs            for every Omni arm of every repetition of the 18 three-run tables (nine workloads, two engines; the
                         branch raw): the beat it ran at (omni_interval.txt), its decisions and writes (audit.jsonl), and its
                         processor-limit writes (the conveyance) split into raises and hand-backs, the cycles of a raise
                         handed back, the median seconds a raise was held, and the reasons the governor wrote

  python3 tools/k8s_decline.py [--repo PATH] [--ref origin/raw] [--main origin/main] [--json OUT.json]

PATH is a checkout whose git holds main's history and the branch raw (a partial clone serves: the blobs the runs need are
fetched in one batch before they are read).
"""
from __future__ import annotations

import argparse
import json
import math
import re
import statistics as st
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_AT = {"omni-v21": "3ad522226bf3", "omni-v25": "79344173670c"}       # the two committed index files the readings name
K8S = "Real Kubernetes (GitHub)"
SETUP = {"KEDA_REQUESTS": "http", "KEDA_CPU_REQUESTS": "both"}            # an add-on run holds one folder per native setup


def git(repo, *a):
    return subprocess.run(["git", "-C", repo, *a], capture_output=True, text=True).stdout


def index_tests(repo, commit):
    d = json.loads(git(repo, "show", f"{commit}:results/OMNI_INDEX.json"))
    tests = {t["source"].split("_", 1)[1].rsplit(".", 1)[0]: t for t in d["tests"] if t["category"] == K8S}
    return d["categories"][K8S], tests


def decomposition(repo):
    (a_pct, a), (b_pct, b) = index_tests(repo, INDEX_AT["omni-v21"]), index_tests(repo, INDEX_AT["omni-v25"])
    fall = math.log1p(a_pct / 100) - math.log1p(b_pct / 100)
    rows = []
    for w in sorted(a):
        x, y = a[w], b[w]
        share = (math.log1p(x["index_pct"] / 100) - math.log1p(y["index_pct"] / 100)) / len(a)
        sx, sy = x["measures"]["speed"], y["measures"]["speed"]
        rows.append({"workload": w, "tables": [x["source"], y["source"]], "score": [x["index_pct"], y["index_pct"]],
                     "share_of_fall": share / fall, "p95_native_ms": [sx["native"], sy["native"]], "p95_omni_ms": [sx["omni"], sy["omni"]],
                     "speed_ratio": [sx["ratio"], sy["ratio"]], "speed_reading": [sx["reading"], sy["reading"]],
                     "other_measures_same": all(x["measures"][m]["ratio"] == y["measures"][m]["ratio"] or abs(x["measures"][m]["ratio"] - y["measures"][m]["ratio"]) < 0.05
                                                for m in ("machines", "energy") if m in x["measures"] and m in y["measures"])})
    geo = {e: (math.prod(1 + t["index_pct"] / 100 for t in tt.values()) ** (1 / len(tt)) - 1) * 100 for e, tt in (("omni-v21", a), ("omni-v25", b))}
    return {"index": {"omni-v21": a_pct, "omni-v25": b_pct}, "recomputed_from_scores": geo, "fall_points": a_pct - b_pct, "rows": rows}


def engines(repo, main):
    fp = {v: json.loads(git(repo, "show", f"{main}:OMNI_V{v}.json"))["files"] for v in range(21, 27)}
    steps = {f"omni-v{a}→omni-v{a + 1}": [f for f in sorted(set(fp[a]) | set(fp[a + 1])) if fp[a].get(f) != fp[a + 1].get(f)] for a in range(21, 26)}
    sys.path.insert(0, str(ROOT))
    from tools.carry import imports
    closure = sorted(imports("omni_controller/controller.py", set(fp[21]) | set(fp[25])))
    return {"steps": steps, "governor_closure": closure, "closure_moved_v21_to_v25": [f for f in closure if fp[21].get(f) != fp[25].get(f)]}


def runs_of(repo, main):
    out = {}
    for w in sorted(SETUP) + ["ALL_FOUR", "BATCH", "FAIRNESS", "FAULTS", "STEADY", "TRACE_GOOGLE2011", "WANDERING"]:
        for e in ("21", "25"):
            d = json.loads(git(repo, "show", f"{main}:results/live/V{e}_{w}.json"))
            out[f"{w}:omni-v{e}"] = [(r["tag"], r["run"]) for r in d["runs"]]
    return dict(sorted(out.items()))


def mechanism(repo, ref, runs):
    names = git(repo, "ls-tree", "--name-only", ref).split()
    folder = {m.group(1): n for n in names for m in [re.fullmatch(r"(?:.*-)?run-(\d+)", n)] if m}
    want = re.compile(r"/bench-compass-(\d+)/(omni_interval\.txt|audit\.jsonl)$")
    items = []
    for key, rr in runs.items():
        w = key.split(":")[0]
        for tag, run in rr:
            base = f"{folder[run]}/{SETUP[w]}" if w in SETUP else folder[run]
            for line in git(repo, "ls-tree", "-r", ref, base + "/").splitlines():
                meta, path = line.split("\t", 1)
                if want.search(path):
                    items.append((key, tag, run, path, meta.split()[2]))
    oids = sorted({i[4] for i in items})
    for k in range(0, len(oids), 300):          # a partial clone: every blob the runs need, fetched in one round trip a batch
        subprocess.run(["git", "-C", repo, "-c", "fetch.negotiationAlgorithm=noop", "fetch", "-q", "--no-write-fetch-head",
                        "--no-tags", "origin", *oids[k:k + 300]], capture_output=True)
    acc = defaultdict(lambda: {"beats": Counter(), "decisions": [], "writes": [], "raises": [], "hand_backs": [], "cycles": [],
                               "held": [], "why": Counter(), "arms": 0})
    for key, tag, run, path, oid in items:
        a = acc[key]
        text = git(repo, "cat-file", "-p", oid)
        if path.endswith("omni_interval.txt"):
            a["beats"][text.strip()] += 1
            continue
        dec = wr = 0
        ev = []
        for line in text.splitlines():
            try:
                d = json.loads(line)
            except ValueError:
                continue
            dec += "decision" in d
            w = d.get("write")
            if not w or d.get("dry_run"):
                continue
            wr += 1
            s = w if isinstance(w, list) else str(w).split()
            if "pod" in s and "patch" in s and "-p" in s:
                try:
                    ev.append((d["time"], s[s.index("pod") + 1], json.loads(s[s.index("-p") + 1])[0]["value"], (d.get("why") or "")[:110]))
                except (ValueError, IndexError, KeyError, TypeError):
                    pass
        r = b = cyc = 0
        bypod = defaultdict(list)
        for t, pod, val, why in ev:
            bypod[pod].append((t, val, why))
        for seq in bypod.values():
            up = None
            for t, v, why in sorted(seq):
                # the governor's own reason says which way a write went: back to the operator's limit (the guard at the
                # shared host's top, or the reset), or a share of a machine's idle processor given to its serving pods
                back = "operator's limit" in why or why.startswith(("reset", "restore"))
                label = re.sub(r"worker\d*", "worker", re.sub(r"busy \d\.\d+", "busy …", why))
                if back:
                    b += 1
                    a["why"]["hand-back: " + label] += 1
                    if up is not None:
                        a["held"].append(t - up)
                        cyc += 1
                        up = None
                else:
                    r += 1
                    a["why"]["raise: " + label] += 1
                    up = t if up is None else up
        a["decisions"].append(dec); a["writes"].append(wr); a["raises"].append(r); a["hand_backs"].append(b); a["cycles"].append(cyc)
        a["arms"] += 1
    out = {}
    for key, a in sorted(acc.items()):
        out[key] = {"omni_arms": a["arms"], "beats_s": dict(a["beats"]), "decisions_per_arm": st.mean(a["decisions"]),
                    "writes_per_arm": st.mean(a["writes"]), "limit_raises_per_arm": st.mean(a["raises"]),
                    "limit_hand_backs_per_arm": st.mean(a["hand_backs"]), "raise_then_hand_back_cycles_per_arm": st.mean(a["cycles"]),
                    "median_s_a_raise_was_held": st.median(a["held"]) if a["held"] else None,
                    "reasons": a["why"].most_common(6)}
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo", default=str(ROOT))
    ap.add_argument("--ref", default="origin/raw")
    ap.add_argument("--main", default="origin/main", help="the ref whose fingerprints and tables are read")
    ap.add_argument("--json", default="")
    a = ap.parse_args(argv)
    runs = runs_of(a.repo, a.main)
    rec = {"read_from": {"index_files": INDEX_AT, "tables": "results/live/V21_*.json and V25_*.json", "raw": a.ref},
           "decomposition": decomposition(a.repo), "engines": engines(a.repo, a.main), "runs": runs,
           "mechanism": mechanism(a.repo, a.ref, runs)}
    print(json.dumps(rec, indent=1))
    if a.json:
        Path(a.json).write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
