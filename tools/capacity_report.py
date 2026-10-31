#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The capacity test's table (docs/CAPACITY_PREREGISTRATION.md): native, and Omni-Compass on top of native, held to the
same resource cap, at every cap level. The work meter (deploy/kind/loadgen-meter.yaml) counts every request: answered
within the line, late, failed, or never sent. One row per cap level and one plain audit line under it, then what each arm
gets from each step up in the cap.

Two measures, both judged with the same latency and failure limits in both arms:
  completed work   the requests answered within the line over the whole window (the work that counts);
  capacity         the highest offered rate (requests per second) the arm served while keeping both limits, step by step
                   up the rising load: at least LATENCY_SHARE of a step's requests answered within the line, and no more
                   than FAIL_SHARE failed or never sent.

  python3 tools/capacity_report.py ROOT [ROOT ...] [--out CAPACITY.md]

ROOT holds cap-<millicores>-<rep>/bench-<arm>-<rep> folders (one artifact per job, both arms of a repetition on one
runner), each with work_meter.json, preflight.txt (cap_cpu_m=...) and latency.csv; a folder with INVALID is left out
and listed.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.legal import stamp  # noqa: E402
from tools.live_reps import T95  # noqa: E402
from tools.readings import GAIN, LOSS, EVEN_NOISE, receipt_key  # noqa: E402  (the words every table uses)

LATENCY_SHARE = 0.95      # a step keeps the latency limit when at least 95% of its requests are answered within the line
FAIL_SHARE = 0.01         # and the failure limit when no more than 1% failed or were never sent
SAT_SHARE = 0.99          # an arm that answered 99% of everything offered within the line never met the cap
OMNI_ARMS = ("compass", "omni")


def read_arm(d: Path):
    """One arm's record, or None when it holds no count."""
    meter = d / "work_meter.json"
    if not meter.exists():
        return None
    m = json.loads(meter.read_text().strip().splitlines()[-1])
    cap = None
    pre = d / "preflight.txt"
    if pre.exists():
        for line in pre.read_text().splitlines():
            if line.startswith("cap_cpu_m="):
                cap = int(line.split("=", 1)[1].split()[0])
    lat = []
    if (d / "latency.csv").exists():
        for r in csv.DictReader(open(d / "latency.csv")):
            if r.get("ok") == "1":
                lat.append(float(r["latency_ms"]))
    lat.sort()
    p95 = lat[min(len(lat) - 1, int(0.95 * len(lat)))] if lat else math.nan
    return {"cap": cap, "total": m["total"], "steps": m["steps"], "rates": m["rate_steps"], "slo_ms": m["slo_ms"],
            "p95_ms": p95}


def capacity(rec) -> float:
    """The highest rate of the rising steps the arm served within both limits, before its first step that broke one;
    0 when the first step already broke one."""
    best = 0.0
    for rate, s in zip(rec["rates"], rec["steps"]):
        sent = s["sent"] or 1
        if s["in_time"] / sent >= LATENCY_SHARE and (s["failed"] + s["not_sent"]) / sent <= FAIL_SHARE:
            best = rate
        else:
            break
    return best


def collect(*roots):
    """{cap: [(native record, omni record, rep, source)]} paired within one job's artifact, and the folders left out."""
    found, left_out = {}, []
    for root in roots:
        for d in sorted(Path(root).rglob("bench-*-*")):
            if not d.is_dir():
                continue
            _, arm, rep = d.name.split("-", 2)
            if (d / "INVALID").exists():
                left_out.append(f"{d.parent.name}/{d.name}: {(d / 'INVALID').read_text().strip()[:120]}")
                continue
            rec = read_arm(d)
            if rec is None:
                left_out.append(f"{d.parent.name}/{d.name}: no work meter count")
                continue
            found.setdefault((rec["cap"], str(d.parent), rep), {})[arm] = rec
    pairs = {}
    for (cap, src, rep), arms in sorted(found.items(), key=lambda x: (x[0][0] or 0, x[0][1], x[0][2])):
        omni = next((arms[a] for a in OMNI_ARMS if a in arms), None)
        if "native" in arms and omni is not None:
            pairs.setdefault(cap, []).append((arms["native"], omni, rep, src))
        else:
            left_out.append(f"{Path(src).name} repetition {rep}: one arm only ({', '.join(sorted(arms))})")
    return pairs, left_out


def paired(diffs):
    """(mean, low, high) of paired differences with the 95% t interval; a single pair has no interval."""
    n = len(diffs)
    m = sum(diffs) / n
    if n < 2:
        return m, math.nan, math.nan
    sd = math.sqrt(sum((x - m) ** 2 for x in diffs) / (n - 1))
    h = T95.get(n - 1, 1.96) * sd / math.sqrt(n)
    return m, m - h, m + h


def reading(lo, hi, n) -> str:
    """Completed work and capacity are work done, so their aim is higher: a rise clear of the noise is GAIN, a fall LOSS
    (tools/readings.py)."""
    if n < 2 or math.isnan(lo):
        return "one pair (no reading)"
    if lo > 0:
        return GAIN
    if hi < 0:
        return LOSS
    return EVEN_NOISE


def row(cap, prs):
    """Every number of one cap level, and its audit line."""
    n = len(prs)
    slo = prs[0][0]["slo_ms"]
    wn = [p[0]["total"]["in_time"] for p in prs]
    wo = [p[1]["total"]["in_time"] for p in prs]
    offered = sum(p[0]["total"]["sent"] for p in prs) / n
    share = lambda xs, k: sum(x[k] for x in xs)
    sn = share([p[0]["total"] for p in prs], "in_time") / max(1, share([p[0]["total"] for p in prs], "sent"))
    so = share([p[1]["total"] for p in prs], "in_time") / max(1, share([p[1]["total"] for p in prs], "sent"))
    fail = lambda t: (t["failed"] + t["not_sent"]) / max(1, t["sent"])
    fn = sum(fail(p[0]["total"]) for p in prs) / n
    fo = sum(fail(p[1]["total"]) for p in prs) / n
    m, lo, hi = paired([o - nat for nat, o in zip(wn, wo)])
    base = sum(wn) / n
    pct = lambda x: 100.0 * x / base if base else math.nan
    cn = [capacity(p[0]) for p in prs]
    co = [capacity(p[1]) for p in prs]
    cm, clo, chi = paired([o - nat for nat, o in zip(cn, co)])
    p95n = sum(p[0]["p95_ms"] for p in prs) / n
    p95o = sum(p[1]["p95_ms"] for p in prs) / n
    r = {"cap_m": cap, "pairs": n, "slo_ms": slo, "offered": offered,
         "work_native": base, "work_omni": sum(wo) / n, "work_diff": m, "work_lo": lo, "work_hi": hi,
         "work_pct": pct(m), "work_pct_lo": pct(lo), "work_pct_hi": pct(hi), "work_reading": reading(lo, hi, n),
         "served_native": sn, "served_omni": so, "fail_native": fn, "fail_omni": fo,
         "capacity_native": sum(cn) / n, "capacity_omni": sum(co) / n, "capacity_diff": cm, "capacity_lo": clo,
         "capacity_hi": chi, "capacity_reading": reading(clo, chi, n), "p95_native": p95n, "p95_omni": p95o}
    r["audit"] = audit(r)
    return r


def audit(r) -> str:
    """One plain sentence: what the row shows, and what it does not."""
    cores = r["cap_m"] / 1000
    cap = f"{cores:g} core" + ("" if cores == 1 else "s")
    if r["served_native"] >= SAT_SHARE and r["served_omni"] >= SAT_SHARE:
        return (f"At {cap} the cap was never reached: both arms answered at least {SAT_SHARE:.0%} of the requests offered "
                f"within {r['slo_ms']:.0f} ms, so this row shows speed (95th-percentile response {r['p95_native']:.0f} → "
                f"{r['p95_omni']:.0f} ms), not more work; more work shows only where the cap holds native back.")
    iv = (f"; 95% interval {r['work_pct_lo']:+.1f}% to {r['work_pct_hi']:+.1f}%, {r['pairs']} pairs"
          if not math.isnan(r["work_lo"]) else f"; {r['pairs']} pair, no interval")
    cap_line = (f" The highest load served within both limits: {r['capacity_native']:.1f} → {r['capacity_omni']:.1f} "
                f"requests a second ({r['capacity_reading']}).")
    lim = f" Failed or never sent: {r['fail_native']:.1%} → {r['fail_omni']:.1%}."
    if r["work_reading"] == GAIN:
        return (f"At {cap}, Omni on top completed {r['work_diff']:,.0f} more requests within {r['slo_ms']:.0f} ms than "
                f"native alone ({r['work_pct']:+.1f}%{iv}): a GAIN, more work from the same cap.{cap_line}{lim}")
    if r["work_reading"] == LOSS:
        return (f"At {cap}, Omni on top completed {abs(r['work_diff']):,.0f} fewer requests within {r['slo_ms']:.0f} ms "
                f"than native alone ({r['work_pct']:+.1f}%{iv}): a LOSS, reported as it stands, its cause looked for in our "
                f"own wiring first.{cap_line}{lim}")
    return (f"At {cap}, the difference in completed work ({r['work_pct']:+.1f}%{iv}) is inside the noise: STEADY, no "
            f"difference beyond the noise at this cap.{cap_line}{lim}")


def steps_up(rows):
    """What each arm gets from each step up in the cap: completed work and capacity per added core."""
    out = []
    for a, b in zip(rows, rows[1:]):
        dc = (b["cap_m"] - a["cap_m"]) / 1000.0
        if dc <= 0:
            continue
        out.append({"from_m": a["cap_m"], "to_m": b["cap_m"],
                    "work_per_core_native": (b["work_native"] - a["work_native"]) / dc,
                    "work_per_core_omni": (b["work_omni"] - a["work_omni"]) / dc,
                    "capacity_per_core_native": (b["capacity_native"] - a["capacity_native"]) / dc,
                    "capacity_per_core_omni": (b["capacity_omni"] - a["capacity_omni"]) / dc})
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--out", default="")
    a = ap.parse_args(argv)
    pairs, left_out = collect(*a.roots)
    rows = [row(cap, prs) for cap, prs in sorted(pairs.items(), key=lambda x: x[0] or 0)]
    ups = steps_up(rows)
    L = ["# The capacity test: native and Omni-Compass on top at the same resource cap", "", *receipt_key(), "",
         "Evidence class **L** (the real thing: a real Kubernetes cluster, real requests, every answer counted). The cap is "
         "a quota on the served app's CPU (the same in both arms, enforced by the cluster, not by either controller); the "
         "load rises step by step past what the cap can serve, the same requests in both arms. **Completed work**: requests "
         "answered within the response-time line over the whole window. **Capacity**: the highest offered rate served while "
         f"at least {LATENCY_SHARE:.0%} of a step's requests are answered within the line and no more than "
         f"{FAIL_SHARE:.0%} fail or are never sent. Paired within one job (both arms on one runner, order rotated).", ""]
    if not rows:
        L += ["No paired repetition yet.", ""]
    else:
        L += ["| Cap (cores) | Pairs | Offered (requests) | Completed, native | Completed, Omni on top | Difference | Reading | "
              "Capacity, native → Omni (req/s) | Capacity reading | p95, native → Omni (ms) | Failed or not sent, native → Omni |",
              "|---:|---:|---:|---:|---:|---:|---|---|---|---|---|"]
        for r in rows:
            iv = "" if math.isnan(r["work_lo"]) else f" ({r['work_pct_lo']:+.1f}% to {r['work_pct_hi']:+.1f}%)"
            L.append(f"| {r['cap_m'] / 1000:g} | {r['pairs']} | {r['offered']:,.0f} | {r['work_native']:,.0f} | "
                     f"{r['work_omni']:,.0f} | {r['work_pct']:+.1f}%{iv} | **{r['work_reading']}** | "
                     f"{r['capacity_native']:.1f} → {r['capacity_omni']:.1f} | {r['capacity_reading']} | "
                     f"{r['p95_native']:.0f} → {r['p95_omni']:.0f} | {r['fail_native']:.1%} → {r['fail_omni']:.1%} |")
        L += ["", "**The audit lines** (one per row, in plain words):", ""]
        L += [f"- {r['audit']}" for r in rows]
        if ups:
            L += ["", "## Each step up in the cap: what one more core gives each arm", "",
                  "| Cap step (cores) | Completed work per added core, native → Omni | Capacity per added core, native → Omni (req/s) |",
                  "|---|---|---|"]
            for u in ups:
                L.append(f"| {u['from_m'] / 1000:g} → {u['to_m'] / 1000:g} | {u['work_per_core_native']:,.0f} → "
                         f"{u['work_per_core_omni']:,.0f} | {u['capacity_per_core_native']:.1f} → {u['capacity_per_core_omni']:.1f} |")
            L += ["", "Where Omni's figure is the higher, Omni turns each added core into more completed work than native "
                  "does; where both are the same, the added core is used alike."]
    L += ["", "## How to read a row", "",
          "- **Both arms served everything offered** (the cap never reached): the row shows speed, not more work. A run "
          "with a fixed offered load, served in full by both arms, can only show faster service for that load (the KEDA "
          "add-on run of 12 October: CPU used +32%, 95th-percentile response -55%, the same six workers; faster service "
          "for the same work, not yet more completed work).",
          "- **The cap holds native back** (native leaves offered requests unanswered within the line): a higher count "
          "for Omni on top at the same cap is more work from the same capacity, a GAIN.",
          "- **Each step up in the cap**: if both arms do more as the cap rises, the step table shows which turns each "
          "added core into more completed work.",
          "- Completed work and capacity are work done, so a rise is GAIN and a fall is LOSS; inside the noise is STEADY (the "
          "key: `docs/HOW_TO_READ_THE_RESULTS.md`). A LOSS is reported as it stands; its cause is looked for in our own "
          "wiring, setup and scoring first."]
    if left_out:
        L += ["", "Left out (listed, never dropped silently):", ""] + [f"- {x}" for x in left_out]
    L += ["", "Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results."]
    text = "\n".join(stamp(L)) + "\n"
    out = Path(a.out) if a.out else Path(a.roots[0]) / "CAPACITY.md"
    out.write_text(text)
    out.with_suffix(".json").write_text(json.dumps({"rows": rows, "steps_up": ups, "left_out": left_out,
                                                    "latency_share": LATENCY_SHARE, "fail_share": FAIL_SHARE},
                                                   indent=1, default=str) + "\n")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
