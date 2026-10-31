# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The store fixes of 25 October, each checked without a server: every check here fails on the runners as they stood at
0364382a54 and passes on the fixed ones.

  sysbench  the brain reads the workload's statements (sysbench's own account, its prepared statements counted), never the
            harness's own monitoring queries (the omni-v16 runs read 4.1 statements a second while sysbench sent 994 to 4,839)
  Kafka     above the operator's count, calm with nothing waiting gives a consumer back with no idle test; idle is a full
            second with no message and a consumer starts busy (no 2 -> 1 -> 2 double rebalance at the start of an arm)
  YCSB      below the operator's size, misses of 1% or more add a notch back each second up to it, with no slow or full
            condition; full at WiredTiger's own 80% or evicting; serverStatus asked only for the sections read; the CPU apart
  Redis     redis-server's, the application's and the brain's CPU apart, steal excluded, beside the host figure
  pgbench   the tables re-initialised and a CHECKPOINT before every arm, every second aggregated, a thirty-second dwell
  readers   the index prefers the stack's own CPU-seconds where a table holds them
"""
import importlib.util
import inspect
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import run_sysbench as S  # noqa: E402
from tools import run_kafka as K  # noqa: E402
from tools import run_ycsb as Y  # noqa: E402
from tools import run_redis as R  # noqa: E402
from tools import run_pgbench as P  # noqa: E402
from tools import omni_index as OI  # noqa: E402


def _test_module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "tests" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_sysbench_reads_the_workload_not_the_harness():
    standin = _test_module("test_run_sysbench")
    srv = standin.StandinServer(512)
    two_ms, a_tenth = 2_000_000_000, 120_000_000                         # picoseconds a statement
    srv.events = [(S.USER, "statement/sql/select", 4, 4 * a_tenth),       # the harness's own monitoring SELECTs, every second
                  (S.LOAD_USER, "statement/com/Execute", 3600, 3600 * two_ms),   # sysbench's prepared statements (binary protocol)
                  (S.LOAD_USER, "statement/sql/execute_sql", 10, 10 * two_ms),   # an SQL-level EXECUTE
                  (S.USER, "statement/com/Execute", 7, 7 * a_tenth)]      # another account's prepared statements: not the workload's
    assert S.LOAD_USER != S.USER, "sysbench runs as its own account, apart from the harness's"
    timer, count = S.stmt_latency(S.status(srv))
    assert count == 3610 and timer == 3610 * two_ms, (timer, count)
    # sysbench connects as that account
    seen = []
    real = S.subprocess.run
    S.subprocess.run = lambda args, **kw: (seen.append(args), type("R", (), {"stdout": "", "stderr": ""})())[1]
    try:
        S.sysbench("oltp_read_write", "run", 1, 200, 1, None)
    finally:
        S.subprocess.run = real
    assert f"--mysql-user={S.LOAD_USER}" in seen[0], seen[0]
    assert "events_statements_summary_by_user_by_event_name" in S.workload_statements_sql() and "statement/com/Execute" in S.workload_statements_sql()


def test_kafka_gives_back_above_the_operators_count():
    snap, dw = K.NATIVE_CONSUMERS, K.HANDBACK_DWELL_S
    # above native: calm with no more waiting than one poll round gives one back after the hand-back dwell, no idle consumer
    # needed (every consumer of a round-robin topic has work, and the messages in flight keep the lag above zero in 388 of 389
    # calm seconds, so the omni-v16 rule held a third consumer to the end of the arm)
    assert K.decide(0.1, -0.5, lag=0, idle=0, cur=snap + 1, last_change_age=dw, snapshot=snap, consumed=980)[0] == snap
    assert K.decide(0.1, -0.5, lag=8, idle=0, cur=snap + 1, last_change_age=dw, snapshot=snap, consumed=980)[0] == snap, "messages in flight are not waiting"
    assert K.decide(0.1, -0.5, lag=(snap + 1) * K.POLL_RECORDS + 1, idle=0, cur=snap + 1, last_change_age=dw, snapshot=snap, consumed=980)[0] == snap + 1, "not while more than a poll round waits"
    assert K.decide(0.1, -0.5, lag=0, idle=0, cur=snap + 1, last_change_age=dw - 1, snapshot=snap, consumed=980)[0] == snap + 1, "not within the hand-back dwell"
    assert K.decide(0.1, -0.5, lag=0, idle=0, cur=snap + 1, last_change_age=dw, snapshot=snap, consumed=0)[0] == snap + 1, "a second that consumed nothing says nothing"
    assert K.decide(0.5, 0.35, lag=40, idle=0, cur=snap + 1, last_change_age=dw, snapshot=snap, consumed=980)[0] > snap + 1, "slow with messages waiting still adds"
    assert K.decide(0.96, 0.0, lag=0, idle=0, cur=snap + 1, last_change_age=dw, snapshot=snap, consumed=980)[0] == K.COVER[1], "the fail-up still comes first"
    # at or below native the idle test and an empty backlog stay, and a second that consumed nothing gives nothing back (the
    # omni-v16 arms began their give-back trial on the idle flags of the seconds before the producer started)
    assert K.decide(0.1, -0.5, lag=0, idle=0, cur=snap, last_change_age=30, snapshot=snap, consumed=290)[0] == snap, "at native a busy consumer is never taken"
    assert K.decide(0.1, -0.5, lag=0, idle=1, cur=snap, last_change_age=30, snapshot=snap, consumed=290)[0] == snap - 1, "an idle one may be, inside the verdict"
    assert K.decide(0.1, -0.5, lag=0, idle=2, cur=snap, last_change_age=30, snapshot=snap, consumed=0)[0] == snap, "nothing consumed yet: nothing taken"
    assert K.decide(0.1, -0.5, lag=3, idle=1, cur=snap, last_change_age=30, snapshot=snap, consumed=290)[0] == snap, "below native only with nothing waiting at all"
    # idle is sustained, and a consumer starts busy
    assert not K.is_idle(100.0, 100.5) and K.is_idle(100.0, 100.0 + K.IDLE_S) and K.IDLE_S >= 1.0

    class Proc:
        def __init__(self, target=None, args=(), daemon=None):
            pass

        def start(self):
            pass

    real = K.mp.Process
    K.mp.Process = Proc
    try:
        with tempfile.TemporaryDirectory() as t:
            g = K.Group("topic", "group", 1.0, Path(t))
            g.start_one(); g.start_one()
            assert g.idle() == 0, "a consumer starts busy: no give-back trial before it has had a second to consume"
    finally:
        K.mp.Process = real
    src = inspect.getsource(K.Brain.step)      # omni-v22: the decision is the Brain's, the code the real run and the model drive
    assert "snapshot=self.snapshot" in src and "consumed=n_msg" in src, "the brain hands decide() the operator's count and the second's consumption"
    assert "give_ok=False" in src and "max(lo, v_target)" in src, "never below the operator's count at the max"


def test_ycsb_hands_the_cache_back_below_native():
    n = Y.NATIVE_MB
    # below native, misses of 1% or more: a notch back each second, up to native, with no slow or full condition
    assert Y.decide(0.1, -0.35, miss_share_last_s=0.095, cur_mb=n - 64, last_change_age=30, full=False, native_mb=n)[0] == n
    assert Y.decide(0.1, -0.35, miss_share_last_s=0.095, cur_mb=n - 128, last_change_age=30, full=False, native_mb=n)[0] == n - 64, "one notch a second"
    assert Y.decide(0.1, -0.35, miss_share_last_s=0.095, cur_mb=n, last_change_age=30, full=False, native_mb=n)[0] == n, "never past native by this rule"
    assert Y.decide(0.1, -0.35, miss_share_last_s=0.095, cur_mb=n - 64, last_change_age=30, full=False, native_mb=n, reads=False)[0] == n - 64, "a second with no page requested says nothing"
    assert Y.decide(0.1, -0.35, miss_share_last_s=0.004, cur_mb=n - 64, last_change_age=30, full=False, native_mb=n)[0] == n - 128, "holding the working set: the give-back stands"
    assert Y.decide(0.5, 0.35, miss_share_last_s=0.3, cur_mb=n - 64, last_change_age=30, full=True, native_mb=n)[0] == n - 64 + Y.STEP_MB * 4, "slow, full and missing: the larger step"
    # full at WiredTiger's own eviction target, or evicting
    assert Y.FULL == 0.8 and Y.cache_full(410, 512) and not Y.cache_full(336, 448) and Y.cache_full(336, 448, evicted_last_s=5)
    # serverStatus asked only for the sections read
    standin = _test_module("test_run_ycsb")
    fc = standin.StandinClient(512)
    real_command = fc.admin.command

    def command(cmd):
        doc = real_command(cmd)
        return {**doc, "metrics": {"x": 1}, "tcmalloc": {"y": 2}, "locks": {}, "host": "h", "ok": 1.0}
    fc.admin.command = command
    plug = Y.CacheSize(fc)
    plug.attach(); plug.lever()
    last = fc.admin.calls[-1]
    assert isinstance(last, dict) and last.get("serverStatus") == 1 and last.get("metrics") == 0 and last.get("tcmalloc") == 0 and last.get("locks") == 0, last
    assert "wiredTiger" not in last and "opLatencies" not in last and "host" not in last, last
    sampler = Y.Sampler(fc); sampler.status(); sampler.status()
    assert isinstance(fc.admin.calls[-1], dict) and fc.admin.calls[-1].get("metrics") == 0, "the sampler reads the lean document too"
    # the CPU apart
    assert Y.host_cpu_split("cpu  100 5 50 1000 20 3 2 40 7 0") == (160, 40), "busy without steal or guest; the steal apart"
    assert Y.proc_cpu_jiffies(None, stat_text="4242 (mongo d) S 1 1 1 0 -1 0 0 0 0 0 250 50 0 0 20 0 30 0") == 300
    keys = [k for k, _, _ in Y.GAUGES]
    assert all(k in keys for k in ("process_cpu_seconds", "server_cpu_seconds", "harness_cpu_seconds", "host_cpu_seconds_no_steal", "steal_seconds", "cpu_seconds"))
    out = Y.CpuApart("no-such-server-process").start().stop()
    assert out["server_cpu_seconds"] is None and out["process_cpu_seconds"] is None and out["harness_cpu_seconds"] >= 0 and out["steal_seconds"] >= 0


def test_redis_cpu_apart():
    a = R.cpu_apart(server_s=10.0, process_s=20.0, brain_s=2.0, sampler_s=1.0, busy_s=50.0, steal_s=3.0)
    assert a == {"server_cpu_seconds": 10.0, "app_cpu_seconds": 17.0, "brain_cpu_seconds": 2.0, "sampler_cpu_seconds": 1.0,
                 "process_cpu_seconds": 30.0, "host_cpu_seconds_no_steal": 50.0, "steal_seconds": 3.0}, a
    assert R.cpu_apart(None, 20.0, 0.0, 1.0, 50.0, 0.0)["process_cpu_seconds"] is None, "no server read: no stack figure claimed"
    keys = [k for k, _, _ in R.GAUGES]
    assert all(k in keys for k in R.OPTIONAL_GAUGES) and "cpu_seconds" in keys, "the host figure kept beside"
    th = R.Sampler(None)
    assert th.cpu_s == 0.0
    assert "thread_time" in inspect.getsource(R.Omni.run) and "thread_time" in inspect.getsource(R.Sampler.run)
    # no change to the knob's rule
    assert R.decide(0.1, -0.5, 0, 64, 10, True)[0] == 64 - R.STEP_MB and R.decide(0.5, 0.35, 3, 64, 10, True)[0] == 64 + R.STEP_MB * 4


def test_pgbench_same_state_every_arm_and_every_second_kept():
    snap = P.NATIVE_POOL
    assert P.DWELL_S >= 30.0
    assert P.decide(0.1, -0.3, 0.0, 3, snap, snap, 1, 10.0)[:2] == (snap, 0), "ten seconds after an add-back: still no give-back"
    rows = [(100.2, 1000, 10), (100.7, 3000, 30), (101.1, 2000, 0)]
    assert P.aggregate_per_second(rows) == ["100 2 4000 10000000 1000 3000 40 1000 10 30", "101 1 2000 4000000 2000 2000 0 0 0 0"]
    with tempfile.TemporaryDirectory() as t:
        f = Path(t) / "step-00.123"
        f.write_text("0 1 1500 0 1700000100 200000 120\n3 9 52000 0 1700000100 900000 50000\nbad\n")
        assert P.parse_log_rows([f]) == [(1700000100.2, 1500, 120), (1700000100.9, 52000, 50000)]
        seen = []
        done = P.reset_tables("host=127.0.0.1 port=5432", "bench", "bench", "pw", 2, t,
                              run=lambda args, **kw: (seen.append(args), type("R", (), {"returncode": 0, "stdout": "", "stderr": ""})())[1])
        assert seen[0][0] == "pgbench" and "-i" in seen[0] and seen[0][seen[0].index("-s") + 1] == "2", seen
        assert seen[1][-1] == "CHECKPOINT" and "psql" in seen[1], seen
        assert done["reinit_exit"] == 0 and done["checkpoint_exit"] == 0 and (Path(t) / "prepare.txt").exists()
    assert "prepare" in inspect.signature(P.run_arm).parameters
    wf = (ROOT / ".github" / "workflows" / "pgbench.yml").read_text()
    assert all(w in wf for w in ("vmstat", "iostat", "log_checkpoints", "log_lock_waits", "out/host"))


def test_index_prefers_the_stacks_own_cpu():
    host = {"reading": "x", "runs": [{"native": 1, "omni": 1}] * 3}
    own = {"reading": "y", "runs": [{"native": 2, "omni": 2}] * 3}
    assert OI.workload_gauge({"cpu_seconds": host, "process_cpu_seconds": own}, ("process_cpu_seconds", "cpu_seconds")) is own
    assert OI.workload_gauge({"cpu_seconds": host, "process_cpu_seconds": {"runs": [None, None, None]}}, ("process_cpu_seconds", "cpu_seconds")) is host
    assert OI.workload_gauge({"cpu_seconds": host}, ("process_cpu_seconds", "cpu_seconds")) is host, "an older table reads as before"
    assert OI.workload_gauge({"cpu_seconds": host}, "cpu_seconds") is host


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
    print("PASS  store fixes of 25 October: sysbench reads its own workload, Kafka hands a consumer back above native, YCSB hands the "
          "cache back below native on misses, the CPU apart (YCSB, Redis), pgbench's per-arm reset and per-second record, the index "
          "prefers the stack's own CPU")
