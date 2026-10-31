# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The Redis runner (tools/run_redis.py) without a Redis: the decision rule (misses grow the ceiling by notches, calm with
nothing evicted gives back one notch after the dwell, the wall puts the whole cover on at once, the cover holds), the
application's own reading, the Zipf working set, the plug's one-writer rule against a standin console, and the paired
reading over repetitions."""
import random
import tempfile
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import run_redis as R


class StandinRedis:
    """A console that remembers maxmemory and can be moved by 'someone else'."""

    def __init__(self, mb):
        self.mm = mb * R.MB; self.evicted = 0

    def config_get(self, k):
        return {"maxmemory": str(self.mm)}

    def config_set(self, k, v):
        self.mm = int(v)

    def info(self, section):
        return {"evicted_keys": self.evicted}


def main():
    lo, hi = R.COVER_MB
    # the decision rule
    assert R.decide(0.5, 0.35, evicted_last_s=10, cur_mb=64, last_change_age=10, full=True)[0] == 64 + R.STEP_MB * 4, "misses with the cache full grow by ceil(force / 0.1) notches"
    assert R.decide(0.5, 0.35, evicted_last_s=0, cur_mb=64, last_change_age=10, full=False)[0] == 64, "misses with room to spare are cold misses: nothing to do"
    assert R.decide(0.5, 1.0, evicted_last_s=10, cur_mb=504, last_change_age=10, full=True)[0] == hi, "the cover holds on the way up"
    assert R.decide(0.96, 0.0, evicted_last_s=0, cur_mb=64, last_change_age=10, full=True)[0] == 64 + R.FAILUP_MB and "fail up" in R.decide(0.96, 0.0, 0, 64, 10, True)[1]
    assert R.decide(0.96, 0.0, evicted_last_s=0, cur_mb=500, last_change_age=10, full=True)[0] == hi, "the cover holds on a fail-up too"
    assert R.decide(0.96, 0.0, evicted_last_s=0, cur_mb=64, last_change_age=10, full=False)[0] == 64, "no fail-up for a cache with room: the ceiling cannot mend it"
    assert R.decide(0.1, -0.5, evicted_last_s=0, cur_mb=64, last_change_age=10, full=False)[0] == 64 - R.STEP_MB, "calm with nothing evicted gives a notch back"
    assert R.decide(0.1, -0.5, evicted_last_s=3, cur_mb=64, last_change_age=10, full=True)[0] == 64, "not while keys are being evicted"
    assert R.decide(0.1, -0.5, evicted_last_s=0, cur_mb=64, last_change_age=2, full=False)[0] == 64, "not within the dwell"
    assert R.decide(0.1, -0.5, evicted_last_s=0, cur_mb=lo, last_change_age=10, full=False)[0] == lo, "never under the cover"
    assert R.decide(0.3, 0.02, evicted_last_s=0, cur_mb=64, last_change_age=10, full=True)[0] == 64, "inside the cushion nothing moves"
    # the plug: snapshot once, write and read back, another writer stops it, restore
    fr = StandinRedis(64); plug = R.Ceiling(fr)
    assert plug.attach() == 64 * R.MB and plug.write(96) == 96 and plug.lever() == 96 * R.MB
    fr.mm = 200 * R.MB                                            # someone else moved the knob
    try:
        plug.lever(); raise AssertionError("a foreign writer must stop Omni")
    except RuntimeError as e:
        assert "another writer" in str(e)
    assert plug.restore() and fr.mm == 64 * R.MB, "restored to the snapshot and read back"
    # the working set: Zipf, hot keys first, the same draws for the same seed
    d1 = R.zipf_sampler(random.Random(7), 1000); d2 = R.zipf_sampler(random.Random(7), 1000)
    a = [d1() for _ in range(5000)]; b = [d2() for _ in range(5000)]
    assert a == b, "the same seed draws the same keys"
    assert all(0 <= k < 1000 for k in a) and a.count(0) > a.count(500) and sum(1 for k in a if k < 100) > 1200, "hot keys first (about a third of the draws on the top tenth at Zipf 0.5)"
    # the application's own reading: the last second's mean latency in seconds; nothing asked reads calm
    app = R.App.__new__(R.App); app.lock = __import__("threading").Lock(); now = time.time()
    app.recent = [(now - 5, 9.0), (now - 0.3, 0.2), (now - 0.1, 5.4)]
    assert abs(app.reading(1.0) - 0.0028) < 1e-9
    app.recent = []; assert app.reading(1.0) == 0.0
    # the brain's sample: the last second's requests, how many were inside the line, and their mean latency in seconds
    with tempfile.TemporaryDirectory() as t:
        app = R.App(None, 16, 10, "1", 1.0, 0, Path(t) / "requests.log"); now = time.time()
        app.recent = [(now, 0.5), (now, 5.0), (now - 5.0, 1.0)]
        n, inside, mean_s = app.last_second(2.0)
        assert (n, inside) == (2, 1) and abs(mean_s - 0.00275) < 1e-12, "two requests this second, one inside the 2 ms line, mean 2.75 ms"
        assert app.last_second(2.0) == (0, 0, None) or app.last_second(2.0)[0] == 2, "nothing new reads none"
    # the paired reading, the same rule as the database benchmark
    reps = [{"native": {"hit_rate": 0.70, "maxmemory_mb_mean": 64.0, "failed": 0}, "omni": {"hit_rate": 0.95, "maxmemory_mb_mean": 150.0, "failed": 0}},
            {"native": {"hit_rate": 0.71, "maxmemory_mb_mean": 64.0, "failed": 0}, "omni": {"hit_rate": 0.94, "maxmemory_mb_mean": 140.0, "failed": 0}},
            {"native": {"hit_rate": 0.69, "maxmemory_mb_mean": 64.0, "failed": 0}, "omni": {"hit_rate": 0.96, "maxmemory_mb_mean": 160.0, "failed": 0}}]
    assert R.paired(reps, "hit_rate", "higher")["reading"] == "GAIN"
    assert R.paired(reps, "maxmemory_mb_mean", "spent")["reading"] == "power given", "more memory held is power given"
    assert R.paired(reps, "failed", "never more")["reading"] == "STEADY, the same"
    reps[2]["omni"]["failed"] = 2
    assert R.paired(reps, "failed", "never more")["reading"] == "**LOSS in a repetition**"
    assert R.COVER_MB == (16, 512) and R.NATIVE_MB == 64 and R.LINE_MS == 2.0 and R.MISS_PENALTY_MS > R.LINE_MS, "a miss lies outside the line by construction"
    # native as shipped (17 October): no ceiling (maxmemory 0); any ceiling Omni wrote would sit below native, so it writes
    # nothing, says why in its audit, and hands back the untouched setting
    fr = StandinRedis(0); plug = R.Ceiling(fr)
    with tempfile.TemporaryDirectory() as t:
        om = R.Omni(plug, None, Path(t) / "audit.jsonl")
        om.stop_flag.set(); om.run()
        assert fr.mm == 0 and om.writes == 0 and om.handed_back, "no ceiling is written over a native with none"
        assert "at its limit on native" in (Path(t) / "audit.jsonl").read_text()
    assert R.POLICY == {"operator": "allkeys-lru", "shipped": "noeviction"}, "Redis ships with noeviction"
    print("PASS  Redis runner: misses grow the ceiling by notches, calm with nothing evicted gives one back after the dwell, the wall puts the whole cover on, "
          "the cover holds; the plug snapshots, reads back, stops for another writer and restores; a seeded Zipf working set; the application's own reading; the paired reading")


if __name__ == "__main__":
    main()
