# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The YCSB-on-MongoDB runner (tools/run_ycsb.py) without a server or YCSB: the decision rule (slow reads grow the cache by
notches only while it is full and missing, calm with the cache's misses under 1% of its requests gives back one notch after the
dwell and never in a second with no request, the wall adds a quarter of the cover, the cover holds), the plug's one-writer rule
against a standin server console, the server's own reading from serverStatus,
YCSB's raw records and failed-operation summary parsed, and the paired reading over repetitions."""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import run_ycsb as Y


class StandinAdmin:
    def __init__(self, mb):
        self.mb = mb; self.reads = (0, 0); self.calls = []

    def command(self, cmd):
        if cmd == "serverStatus" or (isinstance(cmd, dict) and "serverStatus" in cmd):   # in full, or with sections asked away (25 October)
            self.calls.append(cmd)
            return {"wiredTiger": {"cache": {"maximum bytes configured": self.mb * Y.MB, "bytes currently in the cache": self.mb * Y.MB // 2,
                                             "pages read into cache": 100, "unmodified pages evicted": 5, "modified pages evicted": 1,
                                             "pages evicted by application threads": 0, "pages requested from the cache": 10000}},
                    "opLatencies": {"reads": {"latency": self.reads[0], "ops": self.reads[1]}}}
        if "setParameter" in cmd:
            cfg = cmd["wiredTigerEngineRuntimeConfig"]; self.mb = int(cfg.split("=")[1].rstrip("M")); return {"ok": 1}
        raise AssertionError(cmd)


class StandinClient:
    def __init__(self, mb):
        self.admin = StandinAdmin(mb)


def main():
    lo, hi = Y.COVER_MB
    # the decision rule
    assert Y.decide(0.5, 0.35, miss_share_last_s=0.3, cur_mb=512, last_change_age=10, full=True)[0] == 512 + Y.STEP_MB * 4, "slow with the cache full and missing grows by ceil(force / 0.1) notches"
    assert Y.decide(0.5, 0.35, miss_share_last_s=0.3, cur_mb=512, last_change_age=10, full=False)[0] == 512, "slow with room to spare: not the cache's to mend"
    assert Y.decide(0.5, 0.35, miss_share_last_s=0.004, cur_mb=512, last_change_age=10, full=True)[0] == 512, "slow with the cache full but holding its working set (misses under 1%): not the cache's to mend (amendment 1)"
    assert Y.decide(0.5, 1.0, miss_share_last_s=0.3, cur_mb=2000, last_change_age=10, full=True)[0] == hi, "the cover holds on the way up"
    assert Y.decide(0.96, 0.0, miss_share_last_s=0.0, cur_mb=512, last_change_age=10, full=True)[0] == 512 + Y.FAILUP_MB and "fail up" in Y.decide(0.96, 0.0, 0.0, 512, 10, True)[1]
    assert Y.decide(0.96, 0.0, miss_share_last_s=0.0, cur_mb=1900, last_change_age=10, full=True)[0] == hi, "the cover holds on a fail-up too"
    assert Y.decide(0.96, 0.0, miss_share_last_s=0.0, cur_mb=512, last_change_age=10, full=False)[0] == 512, "no fail-up for a cache with room"
    assert Y.decide(0.1, -0.5, miss_share_last_s=0.004, cur_mb=512, last_change_age=10, full=False)[0] == 512 - Y.STEP_MB, "calm with misses under 1% of requests gives a notch back"
    assert Y.decide(0.1, -0.5, miss_share_last_s=0.004, cur_mb=512, last_change_age=10, full=True)[0] == 512 - Y.STEP_MB, "full or not: a cache holding its working set gives a notch back (WiredTiger keeps a cache full)"
    assert Y.decide(0.1, -0.5, miss_share_last_s=0.05, cur_mb=512, last_change_age=10, full=True)[0] == 512, "not while the cache misses 1% or more of its requests: it does not hold the working set"
    assert Y.decide(0.1, -0.5, miss_share_last_s=0.0, cur_mb=512, last_change_age=10, full=False, reads=False)[0] == 512, "a second with no page requested says nothing: nothing taken (a cold cache is not a small working set)"
    assert Y.decide(0.1, -0.5, miss_share_last_s=0.0, cur_mb=512, last_change_age=2, full=False)[0] == 512, "not within the dwell"
    assert Y.decide(0.1, -0.5, miss_share_last_s=0.0, cur_mb=lo, last_change_age=10, full=False)[0] == lo, "never under the cover"
    assert Y.decide(0.3, 0.02, miss_share_last_s=0.0, cur_mb=512, last_change_age=10, full=True)[0] == 512, "inside the cushion nothing moves"
    assert Y.miss_share(5, 1000) == 0.005 and Y.miss_share(0, 0) == 0.0 and Y.GIVEBACK_MISS_SHARE == Y.GROW_MISS_SHARE == 0.01
    # the plug: snapshot once, write and read back, another writer stops it, restore
    fc = StandinClient(512); plug = Y.CacheSize(fc)
    assert plug.attach() == 512 and plug.write(768) == 768 and plug.lever() == 768
    fc.admin.mb = 1024                                           # someone else moved the knob
    try:
        plug.lever(); raise AssertionError("a foreign writer must stop Omni")
    except RuntimeError as e:
        assert "another writer" in str(e)
    assert plug.restore() and fc.admin.mb == 512, "restored to the snapshot and read back"
    # the server's own reading and cache figures from serverStatus
    st = fc.admin.command("serverStatus")
    assert Y.read_latency(st) == (0, 0)
    mb, used, pages, ev, requested = Y.cache_stats(st)
    assert mb == 512 and abs(used - 256) < 1e-9 and pages == 100 and ev == 6 and requested == 10000
    # YCSB's raw records and its failed-operation summary
    with tempfile.TemporaryDirectory() as t:
        raw = Path(t) / "n.raw"
        raw.write_text("op, timestamp(ms), latency(us)\nREAD,1700000000123,345\nUPDATE,1700000000130,2500\nbad line\nREAD,1700000000140,-1\n")
        recs = Y.parse_raw(raw)
        assert len(recs) == 3 and abs(recs[0][1] - 0.345) < 1e-9 and abs(recs[1][1] - 2.5) < 1e-9, recs
        assert Y.parse_raw(Path(t) / "missing.raw") == []
    assert Y.parse_failed("[OVERALL], RunTime(ms), 20000\n[READ-FAILED], Operations, 3\n[UPDATE-FAILED], Operations, 2\n[READ], Operations, 100\n") == 5
    assert Y.parse_failed("[READ], Operations, 100\n") == 0
    # the paired reading, the same rule as the database and cache benchmarks
    reps = [{"native": {"ops": 2900.0, "cache_mb_mean": 512.0, "failed": 0}, "omni": {"ops": 2950.0, "cache_mb_mean": 900.0, "failed": 0}},
            {"native": {"ops": 2910.0, "cache_mb_mean": 512.0, "failed": 0}, "omni": {"ops": 2955.0, "cache_mb_mean": 880.0, "failed": 0}},
            {"native": {"ops": 2890.0, "cache_mb_mean": 512.0, "failed": 0}, "omni": {"ops": 2945.0, "cache_mb_mean": 920.0, "failed": 0}}]
    assert Y.paired(reps, "ops", "higher")["reading"] == "GAIN"
    assert Y.paired(reps, "cache_mb_mean", "spent")["reading"] == "power given", "more cache held is power given"
    assert Y.paired(reps, "failed", "never more")["reading"] == "STEADY, the same"
    reps[1]["omni"]["failed"] = 1
    assert Y.paired(reps, "failed", "never more")["reading"] == "**LOSS in a repetition**"
    assert Y.COVER_MB == (256, 2048) and Y.NATIVE_MB == 512 and lo <= Y.NATIVE_MB <= hi and len(Y.YCSB_SHA256) == 64
    # native as shipped (17 October): MongoDB's own default cache (half of RAM less 1 GB: 7,680 MB on a 16 GB machine) is
    # above the cover; any size Omni wrote would sit below native, so it writes nothing and hands back the untouched setting
    fc = StandinClient(7680); plug = Y.CacheSize(fc)
    with tempfile.TemporaryDirectory() as t:
        om = Y.Omni(plug, Path(t) / "audit.jsonl")
        om.stop_flag.set(); om.run()
        assert fc.admin.mb == 7680 and om.writes == 0 and om.handed_back, "no size is written under a native above the cover"
        assert "at its" in (Path(t) / "audit.jsonl").read_text()
    print("PASS  YCSB runner: slow reads with the cache full and missing grow the cache by notches, calm with misses under 1% of requests gives one back after the dwell, the wall adds a quarter "
          "of the cover, the cover holds; the plug snapshots, reads back, stops for another writer and restores; the server's own reading; YCSB's records parsed; the paired reading")


if __name__ == "__main__":
    main()
