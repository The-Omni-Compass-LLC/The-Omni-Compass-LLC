#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""How steadily the governor steered: its decisions, the settings commands it wrote, how often each recommendation moved
and turned back, and the time each decision took, read from the omni arm's audit in every run of the engine's real
Kubernetes tables (results/live/RECIPES.json). Shown, not judged: native has no governor to compare with, so no row here
reads GAIN, STEADY or LOSS; a page a referee or an operator reads to see whether the governor hammers.

  python3 tools/steering.py [--raw results/live/raw] [--out results/STEERING.md]

The raw folders are the archive's (scripts/raw_archive.sh open, or `tools/reproduce.py --patterns` for the list). Each
gauge is the omni arm's own, per hour of its audit, averaged over the run's repetitions; the three runs are shown side by
side (A, B, C), never pooled. The gauges are the same ones tools/omni_exporter.py serves to Prometheus.
"""
from __future__ import annotations

import argparse, json, statistics, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from tools.omni_exporter import Gauges            # noqa: E402
from tools.legal import stamp as legal_stamp      # noqa: E402

RECIPES = ROOT / "results" / "live" / "RECIPES.json"
TESTS = [("V11_GOLDILOCKS", "On top of Goldilocks and the VPA's recommender"),
         ("V11_KEDA_REQUESTS", "On top of KEDA's HTTP add-on"),
         ("V11_KEDA_CPU_REQUESTS", "On top of KEDA on CPU and requests"),
         ("V11_CAPACITY", "Fixed capacity, four caps"),
         ("V11_ROBUST_KILL", "The governor killed outright mid-run"),
         ("V11_ROBUST_LONG", "The long run, two hours an arm")]
SETTINGS = ("hpa_target", "nodes", "power_cap")


def arm(audit: Path) -> dict | None:
    """One omni arm's steering gauges from its audit, per hour of the audit."""
    g, times, ms = Gauges(), [], []
    with audit.open(encoding="utf-8", errors="replace") as f:
        for ln in f:
            g.feed(ln)
            try:
                r = json.loads(ln)
            except ValueError:
                continue
            if isinstance(r, dict) and isinstance(r.get("time"), (int, float)):
                times.append(r["time"])
                if isinstance(r.get("decision_ms"), (int, float)):
                    ms.append(r["decision_ms"] / 1000.0)
    if len(times) < 2 or not g.decisions:
        return None
    hours = (max(times) - min(times)) / 3600.0
    if hours <= 0:
        return None
    out = {"hours": hours, "decisions_h": g.decisions / hours, "writes_h": sum(g.writes.values()) / hours,
           "writes_by_why": {k: v / hours for k, v in g.writes.items()},
           "decision_s_mean": statistics.mean(ms) if ms else None, "decision_s_max": max(ms) if ms else None,
           "own_cpu": g.own_cpu, "errors_h": sum(g.errors.values()) / hours}
    zoned = sum(g.zones.values())
    for z in ("slack", "band", "wall"):
        out[f"share_{z}"] = 100.0 * g.zones[z] / zoned if zoned else None
    out["recovery_s_mean"] = g.recovery_sum / g.recovery_count if g.recovery_count else None
    out["recovery_s_max"] = g.recovery_max
    for s in SETTINGS:
        out[f"moves_h_{s}"] = g.moves.get(s, 0) / hours
        out[f"reversals_h_{s}"] = g.reversals.get(s, 0) / hours
        out[f"travel_h_{s}"] = g.travel.get(s, 0.0) / hours
    return out


def run(folder: Path) -> dict | None:
    arms = [a for a in (arm(p) for p in sorted(folder.rglob("bench-compass-*/audit.jsonl"))) if a]
    if not arms:
        return None
    keys = [k for k in arms[0] if k != "writes_by_why"]
    m = {k: statistics.mean(a[k] for a in arms if a.get(k) is not None) if any(a.get(k) is not None for a in arms) else None
         for k in keys}
    why: dict[str, float] = {}
    for a in arms:
        for k, v in a["writes_by_why"].items():
            why[k] = why.get(k, 0.0) + v / len(arms)
    m["writes_by_why"] = dict(sorted(why.items(), key=lambda kv: -kv[1]))
    m["repetitions"] = len(arms)
    return m


def fmt(v, nd=1):
    return "—" if v is None else f"{v:.{nd}f}"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--raw", dest="archive", type=Path, default=ROOT / "results" / "live" / "raw")
    ap.add_argument("--out", type=Path, default=ROOT / "results" / "STEERING.md")
    a = ap.parse_args(argv)
    rec = json.loads(RECIPES.read_text(encoding="utf-8"))
    data, L = {}, ["# How steadily the governor steered: its own moves on every omni-v11 Kubernetes table", "",
                   "Evidence class L, the omni arm only (native has no governor): shown, not judged. Each cell is the omni arm's own "
                   "gauge per hour of its audit, averaged over the run's repetitions, for runs A / B / C of the table named; the "
                   "runs are never pooled. A recommendation is what a decision asks for; a write is a command that changed a "
                   "setting. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these "
                   "results. Made by `tools/steering.py` from the archived audits; the same gauges are served live by "
                   "`tools/omni_exporter.py`.", ""]
    rows = [("decisions an hour", "decisions_h", 1), ("settings commands written an hour", "writes_h", 1),
            ("HPA target recommendation: moves an hour", "moves_h_hpa_target", 1),
            ("HPA target recommendation: reversals an hour", "reversals_h_hpa_target", 1),
            ("machines recommendation: moves an hour", "moves_h_nodes", 1),
            ("machines recommendation: reversals an hour", "reversals_h_nodes", 1),
            ("power cap recommendation: moves an hour (not written on Kubernetes)", "moves_h_power_cap", 1),
            ("power cap recommendation: reversals an hour (not written on Kubernetes)", "reversals_h_power_cap", 1),
            ("HPA target recommendation: distance travelled an hour", "travel_h_hpa_target", 3),
            ("machines recommendation: distance travelled an hour", "travel_h_nodes", 2),
            ("decisions with the compass in its band (%)", "share_band", 1),
            ("decisions with the compass under its lower cushion, the service far from its line (%)", "share_slack", 1),
            ("decisions with the compass at or past the line (%)", "share_wall", 1),
            ("time from the line back into the band, mean (s)", "recovery_s_mean", 0),
            ("time from the line back into the band, longest (s)", "recovery_s_max", 0),
            ("errors recorded an hour", "errors_h", 1),
            ("decision time, mean (s)", "decision_s_mean", 2), ("decision time, longest (s)", "decision_s_max", 2),
            ("the governor's own processor (cores)", "own_cpu", 4)]
    for key, title in TESTS:
        r = rec.get(key)
        if not r:
            continue
        runs = [run(a.archive / x) for x in r["runs"]]
        if not all(runs):
            missing = [x for x, m in zip(r["runs"], runs) if not m]
            L += [f"## {title} (`results/live/{key}.md`)", "", f"Not read: no omni-arm audit under {', '.join(missing)} "
                  f"(open them with `scripts/raw_archive.sh open`).", ""]
            continue
        data[key] = {"title": title, "runs": r["runs"], "gauges": runs}
        L += [f"## {title} (`results/live/{key}.md`)", "",
              f"Runs {', '.join(x.split('/')[0].rsplit('-', 1)[-1] for x in r['runs'])}; {runs[0]['repetitions']}, "
              f"{runs[1]['repetitions']} and {runs[2]['repetitions']} omni repetitions.", "",
              "| Gauge | A | B | C |", "|---|---:|---:|---:|"]
        for label, k, nd in rows:
            L.append(f"| {label} | {fmt(runs[0][k], nd)} | {fmt(runs[1][k], nd)} | {fmt(runs[2][k], nd)} |")
        top = list(runs[0]["writes_by_why"].items())[:4]
        L += ["", "Writes an hour by the head of their reason, run A: " + "; ".join(f"{k} {v:.1f}" for k, v in top) + ".", ""]
    a.out.write_text("\n".join(legal_stamp(L)) + "\n", encoding="utf-8")
    a.out.with_suffix(".json").write_text(json.dumps(data, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"steering: {len(data)} tables read -> {a.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
