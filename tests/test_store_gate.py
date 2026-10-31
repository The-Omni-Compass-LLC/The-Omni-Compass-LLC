# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The store gate (tools/store_gate.py) without archived runs: its gauges from a replayed knob, its paired reading by the gauge's
aim, the candidate cache wire handing back below native where the recorded seconds miss, the Kafka wire giving no consumer
back on a second that consumed nothing, and the Redis rule read identically by both wires."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import store_gate as G  # noqa: E402


def ycsb_rows(n=60, miss_from=30):
    return [{"t": float(t), "force": -0.35, "p": 0.05, "miss_share": 0.0005 if t < miss_from else 0.095, "pages_requested_last_s": 1000,
             "used_mb": 336.0, "evicted_last_s": 0 if t < miss_from else 900, "cost": 1e-6, "cache_mb": 512} for t in range(n)]


def test_gauges_and_reading():
    traj = [{"t": 0.0, "cur": 20, "short": False, "idle_calm": False, "wrote": True},
            {"t": 1.0, "cur": 19, "short": True, "idle_calm": False, "wrote": False},
            {"t": 20.0, "cur": 21, "short": False, "idle_calm": True, "wrote": True}]
    g = G.gauges_of(traj, 20)
    assert g == {"setting_mean": 20.0, "writes": 2, "below_native_s": 1, "below_native_short_s": 1, "above_native_idle_s": 1, "first_writes": 1}, g
    pairs = [({"setting_mean": 10.0, "writes": 4, "below_native_s": 3, "below_native_short_s": 3, "above_native_idle_s": 0, "first_writes": 2},
              {"setting_mean": 10.0, "writes": 2, "below_native_s": 1, "below_native_short_s": 1, "above_native_idle_s": 0, "first_writes": 0})] * 3
    r = G.read_pairs("x", pairs)
    assert r["writes"]["word"] == "GAIN" and r["below_native_short_s"]["word"] == "GAIN" and r["below_native_s"]["word"] == "shown"
    assert r["setting_mean"]["word"].startswith("STEADY")
    worse = [(c, b) for b, c in pairs]
    assert G.read_pairs("x", worse)["below_native_short_s"]["word"] == "LOSS" and G.read_pairs("x", worse)["writes"]["word"] == "power given"


def test_candidate_cache_hands_back_where_the_standing_held():
    cand = G.load_wire("run_ycsb")
    rows = ycsb_rows()
    traj = G.replay_ycsb(cand, rows, 512)
    below_short = [x for x in traj if x["cur"] < 512 and x["short"]]
    deficit = (512 - min(x["cur"] for x in traj if x["t"] >= 30)) // cand.STEP_MB
    assert 0 < len(below_short) <= deficit, "missing below native: a notch handed back each second"
    assert all(x["cur"] == 512 for x in traj if x["t"] >= 30 + deficit), "and back at native's size once the notches are in"


def test_kafka_nothing_consumed_nothing_taken():
    cand = G.load_wire("run_kafka")
    rows = [{"t": float(t), "force": -0.38, "p": 0.0, "lag": 0, "idle": 2, "consumed_last_s": 0 if t == 0 else 290, "cost": 1e-6} for t in range(20)]
    traj = G.replay_kafka(cand, rows, 2)
    assert not any(x["wrote"] for x in traj), "no give-back trial from the idle flags of a second that consumed nothing"


def test_redis_rule_identical():
    a = G.load_wire("run_redis")
    rows = [{"p": 0.1, "force": f, "evicted_last_s": e, "maxmemory_mb": 64, "full": True} for f in (-0.5, 0.0, 0.3, 1.0) for e in (0, 5)]
    assert G.replay_redis(a, rows, 64) == G.replay_redis(G.load_wire("run_redis"), rows, 64)


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
    print("PASS  store gate: gauges from a replayed knob, the paired reading by aim, the cache handed back below native on misses, "
          "no Kafka give-back on an empty second, the Redis rule identical")
