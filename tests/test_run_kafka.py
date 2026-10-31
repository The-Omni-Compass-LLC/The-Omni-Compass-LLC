# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The Kafka runner (tools/run_kafka.py) without a broker: the decision rule (slow with messages waiting adds consumers,
calm gives back one idle consumer after the dwell and only with nothing waiting, the wall starts every consumer at once,
the cover holds), the group's reading from the consumers' own records, the paired reading over repetitions, and the
declared service time spent as CPU."""
import math
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import run_kafka as K


def main():
    lo, hi = K.COVER
    # the decision rule
    assert K.decide(0.5, 0.35, lag=40, idle=0, cur=2, last_change_age=10)[0] == 2 + 4, "full-ish force adds ceil(force / 0.1)"
    assert K.decide(0.5, 0.35, lag=0, idle=0, cur=2, last_change_age=10)[0] == 2, "slow but nothing waiting: hold"
    assert K.decide(0.5, 2.0, lag=1, idle=0, cur=2, last_change_age=10)[0] == hi, "the cover holds on the way up"
    assert K.decide(0.96, 0.0, lag=0, idle=2, cur=2, last_change_age=10) == (hi, 0, "fail up: the line is at hand, every consumer at once")
    assert K.decide(0.1, -0.5, lag=0, idle=1, cur=3, last_change_age=10)[0] == 2, "calm with an idle consumer gives one back"
    assert K.decide(0.1, -0.5, lag=0, idle=1, cur=3, last_change_age=2)[0] == 3, "not within the dwell"
    assert K.decide(0.1, -0.5, lag=3, idle=1, cur=3, last_change_age=10)[0] == 3, "not while messages wait"
    assert K.decide(0.1, -0.5, lag=0, idle=0, cur=3, last_change_age=10)[0] == 3, "a busy consumer is never taken"
    assert K.decide(0.1, -0.5, lag=0, idle=1, cur=lo, last_change_age=10)[0] == lo, "never under the cover"
    assert K.decide(0.3, 0.02, lag=5, idle=0, cur=2, last_change_age=10)[0] == 2, "inside the cushion nothing moves"
    # the reading from the consumers' records: the mean latency of the last second's messages, in seconds
    with tempfile.TemporaryDirectory() as t:
        f = Path(t) / "consumer-1.log"; now = time.time()
        f.write_text(f"{now - 5:.3f} 1 900.0\n{now - 0.2:.3f} 2 100.0\n{now - 0.1:.3f} 3 300.0\n")
        r = K.service_reading([f], 1.0)
        assert abs(r - 0.2) < 1e-9, "the last second's messages, mean, in seconds"
        assert K.service_reading([Path(t) / "none.log"], 1.0) is None, "no record reads None (the caller decides: the line if waiting, calm if not)"
        mean_s, n, inside = K.service_sample([f], 1.0, line_ms=200.0)
        assert abs(mean_s - 0.2) < 1e-9 and n == 2 and inside == 1, "the brain's sample: the mean, the count, and how many were inside the line"
        assert K.service_sample([Path(t) / "none.log"], 1.0) == (None, 0, 0)
    # the paired reading over repetitions, the same rule as the database benchmark
    reps = [{"native": {"p95_ms": 400.0, "lost": 0, "consumers_mean": 2.0}, "omni": {"p95_ms": 20.0, "lost": 0, "consumers_mean": 5.0}},
            {"native": {"p95_ms": 420.0, "lost": 0, "consumers_mean": 2.0}, "omni": {"p95_ms": 25.0, "lost": 0, "consumers_mean": 5.5}},
            {"native": {"p95_ms": 390.0, "lost": 0, "consumers_mean": 2.0}, "omni": {"p95_ms": 15.0, "lost": 0, "consumers_mean": 4.5}}]
    p = K.paired(reps, "p95_ms", "lower"); assert p["reading"] == "GAIN" and p["significant"], "a shorter wait is a GAIN"
    c = K.paired(reps, "consumers_mean", "spent"); assert c["reading"] == "power given", "more consumers held is power given"
    assert K.paired(reps, "lost", "never more")["reading"] == "STEADY, the same"
    reps[1]["omni"]["lost"] = 1
    assert K.paired(reps, "lost", "never more")["reading"] == "**LOSS in a repetition**", "a message never consumed in any repetition is marked"
    noisy = [{"native": {"x": 1.0}, "omni": {"x": 1.1}}, {"native": {"x": 1.0}, "omni": {"x": 0.9}}, {"native": {"x": 1.0}, "omni": {"x": 1.05}}]
    assert K.paired(noisy, "x", "lower")["reading"] == "STEADY, no difference beyond the noise"
    # the service time is spent as CPU
    t0 = time.perf_counter(); K.busy_ms(20); dt = time.perf_counter() - t0
    assert 0.018 <= dt <= 0.2, f"20 ms of work took {dt:.3f} s"
    assert K.COVER == (1, K.PARTITIONS) and K.NATIVE_CONSUMERS == 2 and math.isclose(K.LINE_MS, 500.0)
    print("PASS  Kafka runner: slow with messages waiting adds consumers, calm gives back one idle consumer after the dwell and only with nothing "
          "waiting, the wall starts every consumer at once, the cover holds; the group's reading from its own records; the paired reading; the service time spent as CPU")


if __name__ == "__main__":
    main()
