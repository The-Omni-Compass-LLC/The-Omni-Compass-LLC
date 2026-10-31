# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The database runner's rule (tools/run_pgbench.py, docs/POSTGRES_PREREGISTRATION.md), without a database: the decision
each second (where the time goes decides the direction; calm gives back one idle server and never a server in use; the
cushion, the dwell, the cover and the fail-up to the pooler's own setting), pgbench's per-transaction log read into the
gauges, and the paired reading over repetitions (GAIN, LOSS or power given by what the gauge is for, STEADY, never more)."""
import math
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import run_pgbench as R


def main():
    snap = R.NATIVE_POOL
    # the service slow and clients waiting: grow, by the force
    t, d, why = R.decide(0.5, 0.25, 0.8, 0, 10, snap, 0, 99)
    assert (t, d) == (13, 1) and "more" in why, (t, d, why)
    t, d, _ = R.decide(0.6, 1.0, 0.9, 0, 10, snap, 0, 99)
    assert t == 20 and d == 1, "full force adds ten slots"
    # the service slow inside the server: one fewer
    t, d, why = R.decide(0.5, 0.25, 0.2, 3, 10, snap, 0, 99)
    assert (t, d) == (9, -1) and "inside the server" in why
    # calm: one idle server given back, never a server in use
    assert R.decide(0.1, -0.3, 0.0, 2, 10, snap, 0, 99)[:2] == (9, -1)
    assert R.decide(0.1, -0.3, 0.0, 0, 10, snap, 0, 99)[:2] == (10, 0), "no idle server: nothing taken"
    # amendment 2, the queue line: a server is taken back only while clients waited for one under 1% of the pooler's time in the
    # last second and a transaction was served; at 1% or more one is added back a second, up to the pooler's own setting; above
    # that setting only slowness adds; adding is never held
    assert R.decide(0.1, -0.3, 0.0, 2, 10, snap, 0, 99, queue_share=0.012)[:2] == (12, 1), "clients waited 1.2% of the time under the pooler's setting: two added back (one per percent, rounded up)"
    assert R.decide(0.1, -0.3, 0.0, 2, 10, snap, -1, 1.0, queue_share=0.01)[:2] == (11, 1), "a take-back that put clients in the queue (1%) is undone the next second"
    assert R.decide(0.1, -0.3, 0.0, 2, 10, snap, 0, 99, queue_share=0.06)[:2] == (16, 1), "6% waiting: six added back"
    assert R.decide(0.1, -0.3, 0.0, 2, 10, snap, 0, 99, queue_share=0.30)[:2] == (snap, 1), "30% waiting: back to the pooler's own setting, never past it by the queue line"
    assert R.decide(0.1, -0.3, 0.0, 2, snap, snap, 0, 99, queue_share=0.02)[:2] == (snap, 0), "at the pooler's own setting with clients waiting: nothing taken, nothing added by the queue line"
    assert R.decide(0.1, -0.3, 0.0, 2, 25, snap, 0, 99, queue_share=0.02)[:2] == (25, 0), "above the pooler's own setting with clients waiting: nothing taken; only slowness adds"
    assert R.decide(0.4, 0.0, 0.0, 2, 10, snap, 0, 99, queue_share=0.02)[:2] == (12, 1), "inside the cushion the queue line still adds back"
    assert R.decide(0.1, -0.3, 0.0, 2, 10, snap, 0, 99, queue_share=0.005)[:2] == (9, -1), "under 1%: an idle server given back"
    assert R.decide(0.1, -0.3, 0.0, 2, 10, snap, 0, 99, served=False)[:2] == (10, 0), "nothing served in the last second: nothing known, nothing moved"
    assert R.decide(0.5, 0.25, 0.2, 3, 10, snap, 0, 99, queue_share=0.02)[:2] == (12, 1), "slow inside the server, but clients waited: added back, not taken"
    assert R.decide(0.5, 0.25, 0.2, 3, 10, snap, 0, 99, queue_share=0.005)[:2] == (9, -1), "slow inside the server, nobody waiting: one fewer"
    assert R.decide(0.5, 0.25, 0.2, 3, 10, snap, 0, 99, served=False)[:2] == (10, 0), "slow inside the server, nothing served: nothing moved"
    assert R.decide(0.5, 0.25, 0.8, 0, 10, snap, 0, 99, queue_share=0.5)[:2] == (13, 1), "slow and waiting: the force adds, as before"
    assert R.decide(0.5, 0.25, 0.8, 0, 25, snap, 0, 99, queue_share=0.5, served=False)[:2] == (28, 1), "the force's add is never held, served or not"
    assert R.decide(0.1, -0.3, 0.0, 2, 10, snap, 1, 2.0, queue_share=0.005)[:2] == (10, 0), "the brake still dwells five seconds after an add"
    assert R.GIVEBACK_WAIT_SHARE == 0.01

    # the console client's protocol parsing (amendment 2: one held connection for the arm, no process launched for a reading)
    import struct
    def field(name):
        return name.encode() + b"\0" + b"\0" * R.Console.ROW_DESCRIPTION_TAIL
    def row(*vals):
        out = struct.pack("!H", len(vals))
        for v in vals:
            out += struct.pack("!i", -1) if v is None else struct.pack("!i", len(v)) + v.encode()
        return out
    T = struct.pack("!H", 2) + field("key") + field("value")
    rows = R.Console.parse_messages([(b"T", T), (b"D", row("default_pool_size", "20")), (b"D", row("other", None)), (b"C", b"SHOW\0"), (b"Z", b"I")])
    assert rows == [{"key": "default_pool_size", "value": "20"}, {"key": "other", "value": None}], rows
    assert R.Console.parse_messages([(b"C", b"SET\0"), (b"Z", b"I")]) == [], "a command with no rows gives none"
    try:
        R.Console.parse_messages([(b"E", b"SERROR\0Mno such command\0\0"), (b"Z", b"I")]); raise AssertionError("the console's refusal must be raised once the result ends")
    except RuntimeError as e:
        assert "no such command" in str(e)
    try:
        R.Console.parse_messages([(b"T", T)]); raise AssertionError("a connection closed before the result ends must be said")
    except ConnectionError:
        pass
    try:
        R.Console.parse_messages([(b"T", b"\x00\x02garbage"), (b"Z", b"I")]); raise AssertionError("a garbled message must not parse")
    except (ValueError, ConnectionError):
        pass
    # the cushion
    assert R.decide(0.4, 0.03, 0.9, 5, 10, snap, 0, 99)[:2] == (10, 0)
    assert R.decide(0.4, -0.03, 0.9, 5, 10, snap, 0, 99)[:2] == (10, 0)
    # the dwell (amendment 1): adding is never held, even two seconds after taking back; taking back waits DWELL_S after adding
    # (thirty seconds since the store fix of 25 October, five before), then goes
    assert R.decide(0.5, 0.3, 0.9, 0, 10, snap, -1, 2.0)[:2] == (13, 1), "gas is never held"
    assert R.decide(0.5, 0.3, 0.9, 0, 10, snap, 1, 2.0)[:2] == (13, 1), "the same direction is never held"
    assert R.decide(0.1, -0.3, 0.0, 3, 10, snap, 1, 2.0)[:2] == (10, 0), "the brake dwells after the gas"
    assert R.decide(0.1, -0.3, 0.0, 3, 10, snap, 1, R.DWELL_S - 1.0)[:2] == (10, 0), "still inside the dwell"
    assert R.decide(0.1, -0.3, 0.0, 3, 10, snap, 1, R.DWELL_S + 1.0)[:2] == (9, -1)
    # the cover
    assert R.decide(0.1, -0.3, 0.0, 1, R.FLOOR, snap, 0, 99)[:2] == (R.FLOOR, 0)
    assert R.decide(0.6, 1.0, 0.9, 0, R.CEILING - 3, snap, 0, 99)[:2] == (R.CEILING, 1)
    # fail up: the pooler's own setting at once, whatever the direction rule would say
    t, d, why = R.decide(0.97, 1.0, 0.1, 0, 7, snap, -1, 1.0)
    assert t == snap and d == 0 and "fail up" in why

    # amendment 1: the reading is the pooler's service time or the share of its clients queued for a server, whichever is larger
    assert R.service_reading(0.0001, 0.0, 0.05) == 0.0001, "no client waiting: the service time alone"
    assert abs(R.service_reading(0.0001, 0.9, 0.05) - 0.045) < 1e-12, "nine in ten clients waiting reads as nine tenths of the line"
    assert R.service_reading(0.06, 0.2, 0.05) == 0.06, "a long transaction still reads as itself"
    p_full = R.Band(0.0, 0.05).position(R.service_reading(0.0001, 1.0, 0.05))
    assert p_full >= 0.95, "every client waiting is past the wall: fail up"

    # pgbench's log into the gauges: 10 transactions, 8 inside a 50 ms line, over 2 s of load
    with tempfile.TemporaryDirectory() as tmp:
        f = Path(tmp) / "step-00.123"
        us = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 60000, 90000]
        f.write_text("".join(f"{i % 4} {i} {u} 0 1791260718 {i * 1000} 50\n" for i, u in enumerate(us)))
        lat = R.parse_latencies([f])
        assert lat == us
        g = R.latency_gauges(lat, 2.0)
        assert g["transactions"] == 10 and g["tps"] == 5.0 and g["work_inside_line_tps"] == 4.0 and g["inside_line_share"] == 0.8
        assert g["p95_ms"] == 90.0 and g["p50_ms"] == 5.0 and abs(g["mean_ms"] - 18.6) < 1e-9
        g0 = R.latency_gauges([], 2.0)
        assert g0["transactions"] == 0 and math.isnan(g0["p95_ms"])
    s = R.parse_summary("number of failed transactions: 3 (0.030%)\nlatency average = 2.2 ms\ntps = 398.697039 (without initial connection time)\n")
    assert s == {"tps": 398.697039, "failed": 3}

    # the paired reading over repetitions
    def reps(nat, om, key):
        return [{"native": {key: n}, "omni": {key: o}} for n, o in zip(nat, om)]
    r = R.paired(reps([100, 102, 98], [120, 121, 119], "work_inside_line_tps"), "work_inside_line_tps", "higher")
    assert r["reading"] == "GAIN" and r["significant"] and r["ci95"][0] > 0, r
    r = R.paired(reps([100, 102, 98], [120, 121, 119], "p95_ms"), "p95_ms", "lower")
    assert r["reading"] == "LOSS", "a higher p95, clear of the noise, is a LOSS"
    r = R.paired(reps([100, 102, 98], [120, 121, 119], "servers_alive_mean"), "servers_alive_mean", "spent")
    assert r["reading"] == "power given", "more server connections held is power given, never a LOSS"
    r = R.paired(reps([100, 102, 98], [110, 90, 101], "p95_ms"), "p95_ms", "lower")
    assert r["reading"] == "STEADY, no difference beyond the noise" and not r["significant"]
    r = R.paired(reps([100.0, 100.0, 100.0], [100.0, 100.0, 100.0 + 1e-9], "tps"), "tps", "higher")
    assert r["reading"] == "STEADY, the same"
    r = R.paired(reps([0, 0, 0], [1, 2, 1], "failed"), "failed", "never more")
    assert r["reading"] == "**LOSS in a repetition**", "more failed transactions is marked whatever the size"
    r = R.paired(reps([20, 20, 20], [11, 12, 10], "pool_mean"), "pool_mean", "shown")
    assert r["reading"] == "shown, not judged"
    assert R.paired(reps([1, 2], [float("nan"), 3], "x"), "x", "lower")["n"] == 1
    print("PASS  database runner: the direction follows where the time goes, calm gives back one idle server and never one in use nor one in demand, "
          "cushion, dwell, cover and fail-up to the pooler's own setting hold; pgbench's log reads into the gauges; the paired "
          "reading says GAIN, LOSS or power given by what the gauge is for, STEADY, and never-more")


if __name__ == "__main__":
    main()
