# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The sysbench-on-MySQL runner (tools/run_sysbench.py) without a server or sysbench: the decision rule (slow statements grow the
pool by chunks only while it is full, calm with no page read from disk gives back one chunk after the dwell, the wall adds four
chunks, the cover holds), the plug's one-writer rule and its wait for the server's online resize against a standin console, the
server's own reading from the performance schema, sysbench's histogram and summary parsed, quantiles from the histogram, and the
paired reading over repetitions."""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import run_sysbench as S


class StandinCursor:
    def __init__(self, server):
        self.s, self.rows = server, []

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def execute(self, sql):
        s = self.s; q = sql.strip()
        if s.stall_until is not None:                            # a shrink under load stays "withdrawing blocks" until the load eases
            if time.monotonic() < s.stall_until:
                s.resize_status = "buffer pool 0 : withdrawing blocks. (8173/8191)"
            else:
                s.stall_until = None; s.resize_status = "Completed resizing buffer pool at 260101 12:00:00."
                if s.pending is not None:
                    s.mb = s.pending; s.pending = None
        if q.startswith("SHOW GLOBAL STATUS"):
            total = s.mb * S.MB // S.PAGE
            self.rows = [("Innodb_buffer_pool_pages_total", str(total)), ("Innodb_buffer_pool_pages_data", str(int(total * s.fill))),
                         ("Innodb_buffer_pool_pages_free", str(total - int(total * s.fill))), ("Innodb_buffer_pool_reads", str(s.disk_reads)),
                         ("Innodb_buffer_pool_read_requests", "1000"), ("Innodb_buffer_pool_resize_status", s.resize_status)]
        elif q.startswith("SELECT @@innodb_buffer_pool_size"):
            self.rows = [(s.mb * S.MB,)]
        elif "events_statements_summary_global_by_event_name" in q:   # every account's statements (the old reading)
            ev = [e for e in s.events if f"'{e[1]}'" in q]
            self.rows = [(s.timer_ps + sum(e[3] for e in ev), s.count + sum(e[2] for e in ev))]
        elif "events_statements_summary_by_user_by_event_name" in q:  # one account's statements (the store fix of 25 October)
            ev = [e for e in s.events if f"USER = '{e[0]}'" in q and f"'{e[1]}'" in q]
            self.rows = [(s.timer_ps + sum(e[3] for e in ev), s.count + sum(e[2] for e in ev))]
        elif "file_summary_by_event_name" in q:                       # the data files' reads and their time (omni-v22's account of a miss)
            self.rows = [(s.file_reads, s.file_ps)]
        elif q.startswith("SET GLOBAL innodb_buffer_pool_size"):
            want = int(q.split("=")[1]) // S.MB
            if s.ignore_set_while_resizing and S.resizing(s.resize_status):
                return                                       # MySQL ignores a new size while a resize is in progress
            s.pending = want; s.resize_status = "Resizing buffer pool from %d to %d (unit=134217728)." % (s.mb * S.MB, want * S.MB); s.ticks = 2
        else:
            raise AssertionError(sql)

    def fetchall(self):
        # the server's asynchronous resize completes after two reads (a stalled shrink is handled in execute)
        s = self.s
        if s.stall_until is not None:
            return self.rows
        if s.pending is not None:
            s.ticks -= 1
            if s.ticks <= 0:
                s.mb = s.pending; s.pending = None; s.resize_status = "Completed resizing buffer pool at 260101 12:00:00."
        return self.rows


class StandinServer:
    def __init__(self, mb, fill=0.5, ignore_set_while_resizing=False):
        self.mb, self.fill, self.disk_reads, self.timer_ps, self.count = mb, fill, 0, 0, 0
        self.file_reads, self.file_ps = 0, 0                        # the data files' reads and their time (picoseconds), omni-v22's account
        self.events = []                                            # (user, event name, count, timer ps) rows of the performance schema
        self.resize_status, self.pending, self.ticks = "", None, 0
        self.ignore_set_while_resizing, self.stall_until = ignore_set_while_resizing, None

    def cursor(self):
        return StandinCursor(self)


def main():
    lo, hi = S.COVER_MB
    # the decision rule
    assert S.decide(0.5, 0.35, misses_last_s=0.3, cur_mb=512, last_change_age=20, full=True)[0] == 512 + S.STEP_MB * 4, "slow with the pool full grows by ceil(force / 0.1) chunks"
    assert S.decide(0.5, 0.35, misses_last_s=0.004, cur_mb=512, last_change_age=20, full=True)[0] == 512, "slow with the pool full but holding its working set (misses under 1%): not the pool's to mend (amendment 2)"
    assert S.decide(0.1, -0.5, misses_last_s=0.0, cur_mb=512, last_change_age=20, full=True, reads=False)[0] == 512, "a second with no read request says nothing: nothing taken (amendment 2)"
    assert S.GROW_MISS_SHARE == S.GIVEBACK_MISS_SHARE == 0.01, "one line, used both ways; no new number"
    assert S.decide(0.5, 0.35, misses_last_s=0.0, cur_mb=512, last_change_age=20, full=False)[0] == 512, "slow with room to spare: not the pool's to mend"
    assert S.decide(0.5, 1.0, misses_last_s=0.3, cur_mb=2000, last_change_age=20, full=True)[0] == hi, "the cover holds on the way up"
    assert S.decide(0.96, 0.0, misses_last_s=0.0, cur_mb=512, last_change_age=20, full=True)[0] == 512 + S.FAILUP_MB and "fail up" in S.decide(0.96, 0.0, 0.0, 512, 20, True)[1]
    assert S.decide(0.96, 0.0, misses_last_s=0.0, cur_mb=1900, last_change_age=20, full=True)[0] == hi, "the cover holds on a fail-up too"
    assert S.decide(0.96, 0.0, misses_last_s=0.0, cur_mb=512, last_change_age=20, full=False)[0] == 512, "no fail-up for a pool with room"
    assert S.decide(0.1, -0.5, misses_last_s=0.004, cur_mb=512, last_change_age=20, full=True)[0] == 512 - S.STEP_MB, "calm with misses under 1% of reads gives a chunk back, full or not (stale pages stay resident)"
    assert S.decide(0.1, -0.5, misses_last_s=0.05, cur_mb=512, last_change_age=20, full=True)[0] == 512, "not while the pool misses more than 1% of its reads: it does not hold the working set"
    assert S.decide(0.1, -0.5, misses_last_s=0.0, cur_mb=512, last_change_age=5, full=False)[0] == 512, "not within the dwell"
    assert S.decide(0.1, -0.5, misses_last_s=0.0, cur_mb=lo, last_change_age=20, full=False)[0] == lo, "never under the cover"
    assert S.decide(0.3, 0.02, misses_last_s=0.0, cur_mb=512, last_change_age=20, full=True)[0] == 512, "inside the cushion nothing moves"
    assert S.miss_share(5, 1000) == 0.005 and S.miss_share(0, 0) == 0.0 and S.miss_share(300, 1000) == 0.3
    # the plug: snapshot once, write in whole chunks and wait for the server's resize, read back, another writer stops it, restore
    srv = StandinServer(512); plug = S.BufferPool(srv)
    assert plug.attach() == 512
    assert plug.write(700) == 640, "a write is rounded to whole chunks (700 MB asks for 5 chunks, 640 MB) and read back once the resize completes"
    assert plug.lever() == 640 and srv.pending is None
    srv.mb = 1024                                               # someone else moved the knob
    try:
        plug.lever(); raise AssertionError("a foreign writer must stop Omni")
    except RuntimeError as e:
        assert "another writer" in str(e)
    srv.mb = 640; srv.resize_status = "Resizing buffer pool from 671088640 to 1073741824 (unit=134217728)."
    assert plug.lever() == 640, "mid-resize the server is still carrying out our write: not a foreign writer"
    srv.resize_status = ""
    assert plug.restore() and srv.mb == 512, "restored to the snapshot and read back"
    assert S.resizing("Resizing buffer pool from 1 to 2.") and S.resizing("Withdrawing blocks to be shrunken.") and not S.resizing("Completed resizing buffer pool at 260101 12:00:00.") and not S.resizing("")
    # the restore waits for a resize the server is still carrying out (a shrink under load withdraws its last blocks only when the
    # load eases, and the server ignores a new size meanwhile), and writes once more if the server ignored the first write
    _sleep, _wait = S.time.sleep, S.RESIZE_WAIT_S
    S.time.sleep = lambda s: None; S.RESIZE_WAIT_S = 0.6
    try:
        srv2 = StandinServer(512, ignore_set_while_resizing=True); plug2 = S.BufferPool(srv2); plug2.attach()
        assert plug2.write(128) == 128
        srv2.stall_until = time.monotonic() + 0.2                    # still withdrawing blocks when the arm ends; eases inside the wait
        assert plug2.restore() and srv2.mb == 512 and plug2.restore_info["writes"] == 1 and "withdrawing" in plug2.restore_info["resize_in_flight_at_end"], plug2.restore_info
        srv2 = StandinServer(512, ignore_set_while_resizing=True); plug2 = S.BufferPool(srv2); plug2.attach(); plug2.write(128)
        srv2.stall_until = time.monotonic() + 0.9                    # eases after the first wait: the first write is ignored, the second taken
        assert plug2.restore() and srv2.mb == 512 and plug2.restore_info["writes"] == 2, plug2.restore_info
        srv2 = StandinServer(512, ignore_set_while_resizing=True); plug2 = S.BufferPool(srv2); plug2.attach(); plug2.write(128)
        srv2.stall_until = time.monotonic() + 60                     # never eases inside the budget: not handed back, and the receipt says so
        assert not plug2.restore() and plug2.restore_info["final_mb"] == 128 and plug2.restore_info["writes"] == 2 and not plug2.restore_info["ok"], plug2.restore_info
    finally:
        S.time.sleep, S.RESIZE_WAIT_S = _sleep, _wait
    # the server's own reading and pool figures
    srv.timer_ps, srv.count = 2_000_000_000_000, 1000              # 2 s over 1,000 statements: 2 ms each
    st = S.status(srv)
    assert S.stmt_latency(st) == (2_000_000_000_000, 1000) and S.read_requests(st) == 1000
    mb, used, reads, rs = S.pool_stats(st)
    assert mb == 512 and abs(used - 256) < 1.0 and reads == 0 and not S.resizing(rs), (mb, used, reads, rs)
    assert not S.pool_full(st); srv.fill = 0.95; assert S.pool_full(S.status(srv))
    # sysbench's histogram, summary and quantiles
    txt = ("SQL statistics:\n    queries performed:\n        read:                            59230\n    transactions:                        59230  (2961.50 per sec.)\n"
           "    queries:                             59230  (2961.50 per sec.)\n    ignored errors:                      2      (0.10 per sec.)\n"
           "    reconnects:                          0      (0.00 per sec.)\n\nGeneral statistics:\n    total time:                          20.0005s\n"
           "Latency (ms):\n         min:                                    0.08\n         avg:                                    0.21\n         max:                                   12.10\n"
           "         95th percentile:                        0.42\n         sum:                                12452.50\n\n"
           "Latency histogram (values are in milliseconds)\n       value  ------------- distribution ------------- count\n"
           "       0.100 |****************************************  5000\n       0.200 |**********************                  3000\n"
           "       0.500 |****                                      1500\n       2.000 |*                                        500\n\n"
           "Threads fairness:\n    events (avg/stddev):           1850.9375/12.21\n")
    h = S.parse_histogram(txt)
    assert h == [(0.1, 5000), (0.2, 3000), (0.5, 1500), (2.0, 500)], h
    s = S.parse_summary(txt)
    assert s["transactions"] == 59230 and s["errors"] == 2 and abs(s["seconds"] - 20.0005) < 1e-9 and abs(s["avg_ms"] - 0.21) < 1e-9 and abs(s["p95_ms_sysbench"] - 0.42) < 1e-9, s
    assert S.quantile(h, 0.5) == 0.1 and S.quantile(h, 0.95) == 0.5 and S.quantile(h, 0.99) == 2.0 and S.quantile([], 0.5) != S.quantile([], 0.5)
    assert sum(c for v, c in h if v <= 1.0) == 9500, "transactions inside a 1 ms line, from the histogram"
    # the paired reading, the same rule as the other stores
    reps = [{"native": {"tps": 2900.0, "pool_mb_mean": 512.0, "failed": 0}, "omni": {"tps": 2950.0, "pool_mb_mean": 900.0, "failed": 0}},
            {"native": {"tps": 2910.0, "pool_mb_mean": 512.0, "failed": 0}, "omni": {"tps": 2955.0, "pool_mb_mean": 880.0, "failed": 0}},
            {"native": {"tps": 2890.0, "pool_mb_mean": 512.0, "failed": 0}, "omni": {"tps": 2945.0, "pool_mb_mean": 920.0, "failed": 0}}]
    assert S.paired(reps, "tps", "higher")["reading"] == "GAIN"
    assert S.paired(reps, "pool_mb_mean", "spent")["reading"] == "power given", "more pool held is power given"
    assert S.paired(reps, "failed", "never more")["reading"] == "STEADY, the same"
    assert S.COVER_MB == (128, 2048) and S.NATIVE_MB == 512 and lo <= S.NATIVE_MB <= hi and S.STEP_MB == S.CHUNK_MB == 128 and S.NATIVE_MB % S.CHUNK_MB == 0
    assert all(s_ >= 1 and r_ > 0 for _, s_, r_, _, _ in S.WORKLOADS.values()) and sum(1 for w in S.WORKLOADS.values() if w[4]) == 1, "one tuning workload"
    print("PASS  sysbench runner: slow statements with the pool full and missing grow the pool by chunks, calm with misses under 1% of reads gives one back after the dwell, "
          "the wall adds four chunks, the cover holds; the plug snapshots, writes whole chunks, waits for the server's resize, reads back, stops for another "
          "writer and restores; the server's own reading; sysbench's histogram and summary parsed; the paired reading")


if __name__ == "__main__":
    main()
