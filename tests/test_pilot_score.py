# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""pilot/score.py on generated captures: a real efficiency gain is detected, identical clusters show no significant
difference, a service regression is detected, measured power is used when present."""
import csv, sys, tempfile
from pathlib import Path
import numpy as np
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from pilot.score import main as score
F = ["timestamp", "elapsed_seconds", "nodes_ready", "nodes_total", "alloc_cpu_m", "req_cpu_m", "used_cpu_m", "pods_pending",
     "hpa_count", "hpa_current_replicas", "hpa_desired_replicas", "power_w"]


def capture(path, nodes, seed, pending_rate=0.0, power=False):
    rng = np.random.default_rng(seed)
    with open(path, "w", newline="") as f:
        w = csv.writer(f); w.writerow(F)
        for i in range(24 * 240):
            t = 15 * i; used = 40000 * (1 + 0.4 * np.sin(2 * np.pi * t / 86400)) * (1 + 0.05 * rng.standard_normal())
            pend = int(rng.random() < pending_rate) * 3
            pw = nodes * (200 + 350 * min(1.0, used / (nodes * 32000))) if power else ""
            w.writerow(["", t, nodes, nodes, nodes * 32000, 60000, int(used), pend, 5, 20, 20 + pend, pw])


def main():
    t = Path(tempfile.mkdtemp())
    capture(t / "base.csv", 20, 1); capture(t / "omni.csv", 12, 2); capture(t / "same.csv", 20, 3)
    capture(t / "bad.csv", 12, 4, pending_rate=0.3)
    capture(t / "base_p.csv", 20, 5, power=True); capture(t / "omni_p.csv", 12, 6, power=True)
    r = score(["--baseline", str(t / "base.csv"), "--omni", str(t / "omni.csv"), "--idle-w", "200", "--dyn-w", "350"])["metrics"]
    assert r["node_hours_per_core_hour"]["verdict"] == "GAIN" and r["kwh_per_core_hour"]["verdict"] == "GAIN"
    assert r["utilisation"]["verdict"] == "GAIN" and r["pending_pod_minutes_per_hour"]["verdict"] == "STEADY, no significant difference"
    s = score(["--baseline", str(t / "base.csv"), "--omni", str(t / "same.csv"), "--idle-w", "200", "--dyn-w", "350"])["metrics"]
    assert all(v["verdict"] == "STEADY, no significant difference" for k, v in s.items() if k != "pending_pod_minutes_per_hour"), s
    b = score(["--baseline", str(t / "base.csv"), "--omni", str(t / "bad.csv")])["metrics"]
    assert b["pending_pod_minutes_per_hour"]["verdict"] == "LOSS" and b["hpa_shortfall_minutes_per_hour"]["verdict"] == "LOSS"
    # the reverse pair: omni holds more machine for the same work, so node-hours rise and utilisation falls; both are
    # power given, never a LOSS (one fact read from its two sides)
    g = score(["--baseline", str(t / "omni.csv"), "--omni", str(t / "base.csv"), "--idle-w", "200", "--dyn-w", "350"])["metrics"]
    assert g["node_hours_per_core_hour"]["verdict"] == "power given" and g["utilisation"]["verdict"] == "power given", g
    p = score(["--baseline", str(t / "base_p.csv"), "--omni", str(t / "omni_p.csv")])["metrics"]
    assert p["kwh_per_core_hour"]["verdict"] == "GAIN"
    print("pilot score: GAIN detected; identical clusters read STEADY, no significant difference; a service LOSS detected; measured power used")
    print("PASS test_pilot_score")


if __name__ == "__main__":
    main()
