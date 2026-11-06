# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The robustness test's readings (tools/live_reps.py, docs/ROBUSTNESS_PREREGISTRATION.md) without a cluster: the kill and
hand-back marks are read from robust.log, the 300 s after the kill (120 s up to omni-v14) are compared in both arms from the probe's own records,
the governor's memory ratio comes from the process-table samples, a hand-back past the allowance or a memory growth past
the limit is marked, and the three-run rows read the same in all three of our runs only when every run's every repetition was handed back."""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import live_reps as R
from tools import confirm_abc as C


def arm(root, name, rep, t0, kill_at, handed_back, mode="kill", rss=(50000, 52000), second=True, native=False, window=900,
        gaps=None, failed=0, end_ok=True):
    d = root / f"bench-{name}-{rep}"; d.mkdir()
    (d / "window_start.txt").write_text(f"{t0}\n")
    lines = [f"{t0} robust {mode}: window {window} s, start {t0}"]
    if mode == "long":
        # the long run: decisions at the governor's own cadence (the configured 60 s interval plus its decision time), the reset check at the end
        g1, g2 = gaps or (62.0, 62.0)
        t, recs = t0, []
        while t < t0 + window - 1:
            recs.append(json.dumps({"time": t, "mode": "nodepool", "decision": {"n": len(recs)}}) + "\n")
            t += g1 if t < t0 + window / 2 else g2
        recs += [json.dumps({"time": t0 + 100, "decision_failed": "API 500 for apis/autoscaling/v2/horizontalpodautoscalers"}) + "\n"] * failed
        (d / "audit.jsonl").write_text("".join(recs))
        (d / "kill_switch.txt").write_text(f"restored target: 50\nworkers in service: {'6 of 6' if end_ok else '5 of 6'}\nOmni records left after kill: none\n")
    if mode == "kill":
        if native:
            lines.append(f"{t0 + kill_at} kill mark (native: nothing to kill)")
        else:
            lines.append(f"{t0 + kill_at} kill: SIGKILL to governor pid 1234 (settings before: target=40)")
            lines.append(f"{t0 + kill_at + handed_back} handed back: every setting at the operator's after {handed_back} s (target=50)" if handed_back is not None
                         else f"{t0 + kill_at + 300} NOT handed back after 300 s: target=40")
            if second:
                lines.append(f"{t0 + 450} second governor started: pid 2345, 7 decisions to the end of the window")
    (d / "robust.log").write_text("\n".join(lines) + "\n")
    # the probe: a sample every 5 s; slow and failed samples only in the window after the kill of the native arm (the rise
    # of the omni-v11 kill test, 140 to 190 s after the kill, lies inside the 300 s window omni-v15 reads)
    rows = ["elapsed_seconds,latency_ms,ok"]
    for e in range(0, 900, 5):
        slow = native and kill_at <= e <= kill_at + R.ROBUST_AFTER_KILL_S and e % 10 == 0
        rows.append(f"{e},{900.0 if slow else 100.0},{0 if (native and e == kill_at + 20) else 1}")
    (d / "latency.csv").write_text("\n".join(rows) + "\n")
    if not native:
        # two hours of samples every 15 s: the first ten minutes at rss[0], the last ten at rss[1], the middle between them
        last_t = 15 * 479
        samples = ["epoch_s,rss_kb,processes"] + [f"{t0 + 15 * i},{rss[0] if 15 * i <= 600 else rss[1] if 15 * i >= last_t - 600 else (rss[0] + rss[1]) // 2},1" for i in range(480)]
        (d / "rss.csv").write_text("\n".join(samples) + "\n")
        if mode != "long":
            (d / "audit.jsonl").write_text("".join(json.dumps({"decision": {"n": i}}) + "\n" for i in range(13)))
        (d / "watchdog.log").write_text(json.dumps({"watchdog": "handed back", "ok": True}) + "\n")
    return d


def main():
    with tempfile.TemporaryDirectory() as t:
        root = Path(t); t0 = 1_800_000_000.0
        n = arm(root, "native", 1, t0, 360, None, native=True)
        o = arm(root, "compass", 1, t0, 360, 12)
        m = R.robust_marks(o)
        assert m["kill_epoch"] == t0 + 360 and m["handed_back_s"] == 12 and m["second_governor"] and m["mode"] == "kill", m
        assert R.robust_marks(n)["kill_epoch"] == t0 + 360 and "handed_back_s" not in R.robust_marks(n), "native carries the mark only"
        wn, wo = R.robust_window(n, 500.0), R.robust_window(o, 500.0)
        assert R.ROBUST_AFTER_KILL_S == 300, "omni-v15 reads the 300 s after the kill (docs/ROBUSTNESS_PREREGISTRATION.md)"
        over, failed = ("robust: time over the line in the 300 s after the kill (% of samples)", "robust: failed requests in the 300 s after the kill (%)")
        assert wn[over] > wo[over] == 0.0 and wn[failed] > wo[failed] == 0.0, (wn, wo)
        assert abs(R.robust_memory(o)["ratio"] - 52000 / 50000) < 1e-9
        L, s = R.robust_table(root, ["native", "compass"])
        assert s["compass"]["handed_back_within_allowance_all"] and s["compass"]["handed_back_s_max"] == 12 and s["compass"]["second_governor_all"]
        assert any("| omni | 1 | kill | 12 | yes | yes | 1 | 1.040 | 13 |" in x for x in L), L
        # a slow hand-back, a leak and a missing second governor are marked
        arm(root, "compass", 2, t0, 360, 90, rss=(50000, 70000), second=False)
        L, s = R.robust_table(root, ["native", "compass"])
        assert not s["compass"]["handed_back_within_allowance_all"] and s["compass"]["second_governor_all"] is False and s["compass"]["memory_ratio_max"] > R.ROBUST_MEMORY_LIMIT
        assert any("**no**" in x and "**(a leak)**" in x for x in L)
        # never handed back
        arm(root, "compass", 3, t0, 360, None)
        _, s = R.robust_table(root, ["native", "compass"])
        assert s["compass"]["never_handed_back"] == 1 and s["compass"]["handed_back_s_max"] == float("inf")
        # the three-run rows: the same in all three of our runs only when every run was handed back within the allowance everywhere
        good = {"compass": {"repetitions": 10, "kill_repetitions": 10, "handed_back_within_allowance_all": True, "handed_back_s_mean": 11.0, "handed_back_s_max": 18.0,
                            "never_handed_back": 0, "second_governor_all": True, "memory_ratio_max": 1.03, "allowance_s": 60.0, "memory_limit": 1.25}}
        bad = {"compass": dict(good["compass"], handed_back_within_allowance_all=False, handed_back_s_max=95.0, memory_ratio_max=1.40)}
        runs = [("1", {}, 10, good), ("2", {}, 10, good), ("3", {}, 10, good)]
        lines, rows = C.robust_rows(runs)
        assert len(lines) == 3 and "handed back within the allowance in every repetition, in all three of our runs" in lines[0] and "no leak" in lines[2]
        lines, rows = C.robust_rows([("1", {}, 10, good), ("2", {}, 10, bad), ("3", {}, 10, good)])
        assert "not handed back within the allowance in a repetition" in lines[0] and "a leak" in lines[2]
        assert C.robust_rows([("1", {}, 10, good), ("2", {}, 10, None), ("3", {}, 10, good)]) == ([], {}), "a run without the block makes no robustness rows"
        assert set(R.ROBUST) <= set(R.KEYS) and all(C.aim_of_row(k) == "lower" for k in R.ROBUST), "the 300 s after the kill is time over the line and failed requests: a rise is a LOSS"
    with tempfile.TemporaryDirectory() as t:
        # the long run: 7,200 s, decisions every 62 s (60 s interval + 2 s of the governor's own), the reset check at the end
        root = Path(t); t0 = 1_800_000_000.0
        o = arm(root, "compass", 1, t0, None, None, mode="long", window=7200)
        m = R.robust_marks(o)
        assert m["mode"] == "long" and m["window_s"] == 7200.0, m
        dec = R.robust_decisions(o, 7200.0)
        assert dec["expected"] == 120.0 and 0.95 <= dec["share"] <= 1.0 and dec["failed"] == 0 and dec["handed_back_end"] is True, dec
        assert abs(dec["decision_time_first_s"] - 2.0) < 1e-6 and abs(dec["decision_time_ratio"] - 1.0) < 1e-6, dec
        L, s = R.robust_table(root, ["native", "compass"])
        c = s["compass"]
        assert c["long_repetitions"] == 1 and c["decisions_share_min"] >= 0.95 and c["failed_decisions_total"] == 0 and c["handed_back_end_all"] is True
        assert abs(c["decision_time_ratio_max"] - 1.0) < 1e-6 and any("| 1.00 | yes |" in x for x in L), L
        # a slower governor in the last hour (4 s a decision against 2 s), a failed decision, a worker not back: each is marked, or INVALID
        arm(root, "compass", 2, t0, None, None, mode="long", window=7200, gaps=(62.0, 64.0), failed=1, end_ok=False)
        L, s = R.robust_table(root, ["native", "compass"])
        c = s["compass"]
        assert 1.9 < c["decision_time_ratio_max"] <= 2.0 and c["failed_decisions_total"] == 1 and c["handed_back_end_all"] is False, c
        assert c["failed_reasons"] == ["API 500 for apis/autoscaling/v2/horizontalpodautoscalers"], c
        assert any("**(grew past the limit)**" in x and "**no**" in x and "1 (shown: API 500" in x for x in L), L
        # too few decisions reads INVALID
        arm(root, "compass", 3, t0, None, None, mode="long", window=7200, gaps=(90.0, 90.0))
        _, s = R.robust_table(root, ["native", "compass"])
        assert s["compass"]["decisions_share_min"] < 0.95
        # the three-run rows
        good = {"compass": {"repetitions": 3, "kill_repetitions": 0, "handed_back_within_allowance_all": None, "handed_back_s_mean": None, "handed_back_s_max": None,
                            "never_handed_back": 0, "second_governor_all": None, "memory_ratio_max": 1.05, "allowance_s": 60.0, "memory_limit": 1.25,
                            "long_repetitions": 3, "decisions_expected": 120.0, "decisions_share_min": 0.975, "failed_decisions_total": 0,
                            "decision_time_ratio_max": 1.1, "handed_back_end_all": True, "decision_share_limit": 0.95, "cycle_growth_limit": 1.5}}
        bad = {"compass": dict(good["compass"], decisions_share_min=0.90, failed_decisions_total=2, failed_reasons=["API 500 for apis/autoscaling/v2/horizontalpodautoscalers"],
                               decision_time_ratio_max=1.8, handed_back_end_all=False)}
        lines, rows = C.robust_rows([("1", {}, 3, good), ("2", {}, 3, good), ("3", {}, 3, good)])
        assert len(lines) == 5 and "no leak" in lines[0] and "valid (every repetition" in lines[1] and "none in any repetition" in lines[2] \
            and "no growth" in lines[3] and "every setting handed back at the end of every repetition, in all three of our runs" in lines[4], lines
        lines, rows = C.robust_rows([("1", {}, 3, good), ("2", {}, 3, bad), ("3", {}, 3, good)])
        assert "INVALID" in lines[1] and "shown, not judged: API 500" in lines[2] and "grew" not in lines[2] and "grew by more than half" in lines[3] \
            and "not handed back at the end" in lines[4], lines
    print("PASS  robustness readings: the kill and hand-back marks, the 300 s after the kill in both arms, the memory ratio; a late hand-back, a leak or a missing "
          "second governor is marked; the long run's decisions of expected, failed decisions, decision-time growth and hand-back at the end; "
          "the three-run rows read the same in all three of our runs only when every run's every repetition was handed back within the allowance")


if __name__ == "__main__":
    main()
