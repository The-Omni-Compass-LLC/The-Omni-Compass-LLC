# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The Redis A/B/C rule (tools/redis_abc.py): GAIN or LOSS in all three of our runs (by what the gauge is for) only with the same sign and every interval clear of zero in all three
runs; a change of 0.5% or more reads by its aim, in all three of our runs or by their mean with the count of runs beyond the noise; STEADY only under 0.5%; clear runs pointing different ways read
the runs disagree; any failed request is marked; the knob's moves are shown; the tuning workload is shown and not counted."""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import redis_abc as M


def pr(diff, lo, hi, native=100.0):
    return {"native": native, "omni": native + diff, "diff": diff, "ci95": [lo, hi], "n": 3, "significant": lo > 0 or hi < 0, "reading": "x"}


def arm(**kw):
    base = {"work_inside_line_rps": 1000.0, "rps": 1450.0, "hit_rate": 0.70, "p95_ms": 5.6, "p99_ms": 5.9, "mean_ms": 1.8, "failed": 0,
            "maxmemory_mb_mean": 64.0, "used_mb_mean": 63.0, "evictions": 50000, "cpu_busy_share": 0.4, "cpu_seconds": 100.0, "cpu_s_per_1k_inside": 0.3,
            "writes": 0, "handed_back": True, "foreign_writer": False, "failups": 0}
    base.update(kw); return base


def rec(name, tuning=False, **omni):
    reps = [{"native": arm(), "omni": arm(**omni)} for _ in range(3)]
    for i, r in enumerate(reps):
        r["omni"]["p95_ms"] += i * 0.02; r["native"]["p95_ms"] += i * 0.01
    return {"workload": name, "tuning": tuning, "value_bytes": 1024, "base_keys": 20000, "steps": "1 2 3", "step_s": 20.0, "line_ms": 2.0,
            "rate_rps": 1500.0, "miss_penalty_ms": 5.0, "native_mb": 64, "cover_mb": [16, 512], "redis_version": "7.0.15",
            "engine": {"version": "omni-v3", "commit": "abc123def456"}, "reps": reps}


def main():
    assert M.verdict([pr(-20, -30, -10)] * 3, "lower") == "**GAIN in all three of our runs**", "a shorter wait is a GAIN"
    assert M.verdict([pr(+3, +1, +5)] * 3, "spent") == "**power given in all three of our runs**", "more memory held is power given, never a LOSS"
    assert M.verdict([pr(+3, +1, +5)] * 3, "lower") == "**LOSS in all three of our runs**", "a longer wait is a LOSS"
    assert M.verdict([pr(+3, +1, +5)] * 3, "higher") == "**GAIN in all three of our runs**", "more work is a GAIN"
    assert M.verdict([pr(-20, -30, -10), pr(-20, -30, -10), pr(-2, -10, +6)], "lower") == "**GAIN by the mean of our three runs, beyond the noise in 2 of 3**"
    assert M.verdict([pr(-20, -30, -10), pr(+20, +10, +30), pr(-20, -30, -10)], "lower") == "**the runs disagree**"
    assert M.verdict([pr(0, -1, 1, native=0)] * 3, "never more") == "STEADY, the same"
    assert M.verdict([pr(0, -1, 1, native=0), pr(1, 0, 2, native=0), pr(0, -1, 1, native=0)], "never more") == "**LOSS in at least one of our runs**", "a failed request in any run is marked"
    assert M.verdict([pr(1, 0, 2)] * 3, "shown") == "shown, not judged"
    with tempfile.TemporaryDirectory() as t:
        dirs = []
        for i in (1, 2, 3):
            d = Path(t) / f"run-{i}"
            for name, r in (("small", rec("small", p95_ms=0.4, hit_rate=0.96, maxmemory_mb_mean=150.0)), ("tuning", rec("tuning", tuning=True, p95_ms=0.5))):
                (d / f"redis-{name}").mkdir(parents=True); (d / f"redis-{name}" / f"{name}.json").write_text(json.dumps(r))
            dirs.append(str(d))
        out = Path(t) / "V3.md"
        assert M.main(dirs + ["--out", str(out)]) == 0
        txt = out.read_text()
        assert "## small" in txt and "## tuning" in txt and "shown and not counted" in txt
        assert "Across 1 untouched workloads" in txt, "the tuning workload is not counted"
        assert "| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 150.0 |" in txt and "power given in all three of our runs" in txt
        assert json.loads(out.with_suffix(".json").read_text())["workloads"]["small"]["p95_ms"]["reading"] == "GAIN in all three of our runs"
    print("PASS  Redis A/B/C rule: GAIN or LOSS in all three of our runs (by what the gauge is for) only with the same sign and every interval clear of zero in all three runs; a change of 0.5% or more "
          "reads by its aim, in all three of our runs or by their mean; STEADY only under 0.5%; any failed request is marked; more memory held reads power given; the tuning workload is not counted")


if __name__ == "__main__":
    main()
