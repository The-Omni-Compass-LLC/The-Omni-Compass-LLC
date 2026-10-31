#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The store gate: the data stores' wires (tools/run_pgbench.py, run_kafka.py, run_ycsb.py, run_redis.py, run_sysbench.py)
in our own model (evidence class S) before any real run, the model gate's rule for wires the model gate has no model of
(tools/model_gate.py models the Kubernetes governor, the card and the verdict, never these five).

The model is the stores' own archived seconds. Every omni arm of a real run wrote one audit record a second: the reading the
brain took (its force and the compass's position, the misses, the waiting, the lag, the idle consumers), the cost sample it
fed its verdict, and the knob it stood at. The gate replays those recorded inputs, decision by decision, through two wires:
the standing one (the runner as it stood at a base commit, read from git) and the candidate (the runner in this checkout),
each with its own verdict (tools/knob_verdict.py, fed the recorded cost samples) and its own knob, which moves only by its
own decisions. The replay is open-loop: the inputs are the ones the standing wire's knob produced, so a candidate that holds
the knob elsewhere is read on a world that did not answer it. It says what each wire decides on the same seconds, never what
a store would then have done.

Gauges, each arm one pair (the standing wire against the candidate on the same seconds), read by the gauge's aim
(tools/readings.py through tools/model_gate.reading: a change under 0.5% is STEADY; from 0.5% a resource spent that fell is a
cut, a GAIN, and one that rose is power given; time waited or missed that rose is a LOSS):
  setting, mean            the knob held (pool size, consumers, cache MB): a resource
  writes                   the knob's moves (a resize, a rebalance, a server closed and opened): wear, a resource
  below native             seconds at a setting below the operator's: shown (the resource given back)
  below native, short      seconds below the operator's setting while the store said the setting was short (clients waiting
                           for a server; the cache missing 1% or more of its requests; messages waiting): time waited, judged
  above native, idle       (Kafka) seconds above the operator's count with the service calm and nothing waiting: a resource
  first 15 s writes        (Kafka) consumer changes in an arm's first 15 seconds (each a rebalance of the whole group): wear
The standing wire's replay is checked against the knob the audit recorded (its share of seconds matching is printed); a
replay that does not reproduce its own record is not read.

sysbench: the candidate changes the reading itself (sysbench's own statements, its prepared ones counted, never the
harness's), and the archived seconds hold only the standing reading's counter. The gate reads both counters where the raw
files hold them: the statements the standing reading counted each second (the audit), against the statements sysbench sent
(its own per-notch summary, reads and writes), which is what the candidate's reading counts. The candidate's decisions on its
own reading are not in any archived file; a short real run's files are the model's input for them.
Redis: the knob's rule is unchanged; the gate checks the two wires decide identically on every archived second. The CPU
apart is a new gauge, read only by runs that record it.

  python3 tools/store_gate.py [--base 0364382a54] [--raw results/live/raw] [--engine V16]
    -> results/model_gate/STORE_GATE.md, results/model_gate/STORE_GATE.json
"""
from __future__ import annotations

import argparse
import importlib.util
import inspect
import gzip
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from omnicompass.compass_law import Band  # noqa: E402
from tools.knob_verdict import KnobVerdict  # noqa: E402
from tools.model_gate import reading  # noqa: E402  (the model gate's paired reading: the mean change, its 95% interval, the word)
from tools.readings import by_word  # noqa: E402  (the number beside a word wears the word's sign)

try:
    from tools.legal import stamp as _legal_stamp
except ImportError:                                            # pragma: no cover
    _legal_stamp = None

BASE = "0364382a54"
LIVE = ROOT / "results" / "live"
OUT = ROOT / "results" / "model_gate"
WINDOW_S = 15.0                                                # Kafka's first-seconds window
POLL_RECORDS = 50                                              # Kafka's poll round a consumer (max_poll_records), for the idle-calm gauge alike in both wires
MATCH_MIN = 0.95                                               # a standing replay that reproduces less of its own record is not read

# gauge -> (aim, a resource spent?); aim None: shown, not judged
GAUGES = {"setting_mean": ("lower", True), "writes": ("lower", True), "below_native_s": (None, False),
          "below_native_short_s": ("lower", False), "above_native_idle_s": ("lower", True), "first_writes": ("lower", True)}
LABELS = {"setting_mean": "setting, mean (the knob held)", "writes": "writes (the knob's moves)", "below_native_s": "seconds below native",
          "below_native_short_s": "seconds below native while short (waiting, missing, lagging)",
          "above_native_idle_s": "seconds above native, calm with nothing waiting", "first_writes": "writes in the first 15 s (rebalances)"}


# --------------------------------------------------------------------------------------------------- the two wires
def load_wire(name, rev=None):
    """tools/<name>.py as a module: from this checkout, or as it stood at git revision rev."""
    if rev is None:
        path = ROOT / "tools" / f"{name}.py"
    else:
        src = subprocess.run(["git", "show", f"{rev}:tools/{name}.py"], cwd=ROOT, capture_output=True, text=True, check=True).stdout
        tmp = Path(tempfile.mkdtemp(prefix="store_gate_")) / f"{name}_at_{rev}.py"
        tmp.write_text(src)
        path = tmp
    spec = importlib.util.spec_from_file_location(f"store_gate_{name}_{rev or 'here'}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def takes(fn, arg):
    return arg in inspect.signature(fn).parameters


def wall_of(mod, line_ms):
    return Band(0.0, line_ms / 1000.0, center=mod.CENTER).wall_high


# --------------------------------------------------------------------------------------------------- the replays
def replay_ycsb(mod, rows, native):
    """The cache wire as its Omni.run calls it, on the recorded seconds; the candidate's own hand-back below native, its full
    and its trial abandoned while missing below native where the module has them."""
    v = KnobVerdict(native, mod.STEP_MB, mod.COVER_MB, objective="resource", settle_s=mod.TAU)
    wall = wall_of(mod, mod.LINE_MS)
    new = takes(mod.decide, "native_mb")
    cur, last_change, out = native, -1e9, []
    for r in rows:
        t, f, p, share, rq = r["t"], r["force"], r["p"], r["miss_share"], r["pages_requested_last_s"]
        used, ev = r["used_mb"], r.get("evicted_last_s", 0)
        v.observe(r.get("cost"), t)
        full = mod.cache_full(used, cur, ev) if hasattr(mod, "cache_full") else used >= mod.FULL * cur
        kw = {"native_mb": native} if new else {}
        target, why = mod.decide(p, f, share, cur, t - last_change, full, wall=wall, reads=rq > 0, **kw)
        missing_below = cur < native and rq > 0 and share >= mod.GROW_MISS_SHARE
        stress = (f > 0.05 or missing_below) if new else f > 0.05
        target, why, _ = v.decide(target, spend_ok=(f > 0.05 and full and share >= mod.GROW_MISS_SHARE),
                                  give_ok=(f < -0.05 and rq > 0 and share < mod.GIVEBACK_MISS_SHARE),
                                  t=t, why=why, stress=stress, calm=f < -0.05, fail_up=why.startswith("fail up"))
        out.append({"t": t, "cur": cur, "short": rq > 0 and share >= mod.GROW_MISS_SHARE, "idle_calm": False, "wrote": target != cur})
        if target != cur:
            if target > cur:
                last_change = t
            cur = target
    return out


def replay_kafka(mod, rows, native):
    """The consumer wire as its Omni.run calls it. The candidate's idle is a full second with no message: from the audit, a
    second whose group consumed nothing (consumed_last_s 0) keeps the recorded idle count, any other reads none idle (with
    keys round-robin over eight partitions every consumer has work while the group consumes); the standing wire reads the
    recorded count (an empty 200 ms poll)."""
    v = KnobVerdict(native, 1, mod.COVER, objective="resource", settle_s=2 * mod.TAU)
    wall = wall_of(mod, mod.LINE_MS)
    new = takes(mod.decide, "snapshot")
    sustained = hasattr(mod, "is_idle")
    cur, last_change, out = native, -1e9, []
    for r in rows:
        t, f, p, lag = r["t"], r["force"], r["p"], r["lag"]
        idle = (r["idle"] if r.get("consumed_last_s", 0) == 0 else 0) if sustained else r["idle"]
        v.observe(r.get("cost"), t)
        consumed = r.get("consumed_last_s", 0)
        kw = {"snapshot": native} if new else {}
        if takes(mod.decide, "consumed"):
            kw["consumed"] = consumed
        target, d, why = mod.decide(p, f, lag, idle, cur, t - last_change, wall=wall, **kw)
        give_ok = f < -0.05 and idle > 0 and lag == 0 and ((cur <= native and consumed > 0) if new else True)
        target, why, _ = v.decide(target, spend_ok=(f > 0.05 and lag > 0), give_ok=give_ok, t=t, why=why, stress=f > 0.05,
                                  calm=f < -0.05, fail_up=why.startswith("fail up"))
        out.append({"t": t, "cur": cur, "short": lag > 0 and f > 0.05, "idle_calm": f < -0.05 and lag <= cur * POLL_RECORDS, "wrote": target != cur})
        if target != cur:
            last_change = t
            cur = target
    return out


def replay_pgbench(mod, rows, native):
    """The pool wire as its Omni.run calls it (the dwell is the module's own DWELL_S)."""
    v = KnobVerdict(native, 1, (mod.FLOOR, mod.CEILING), objective="resource", settle_s=mod.TAU)
    wall = wall_of(mod, mod.LINE_MS)
    cur, last_dir, last_change, out = native, 0, -1e9, []
    for r in rows:
        t, f, p, ws, qs, served, idle = r["t"], r["force"], r["p"], r["wait_share"], r["queue_share"], r["served"], r["idle"]
        v.observe(r.get("cost"), t)
        target, d, why = mod.decide(p, f, ws, idle, cur, native, last_dir, t - last_change, wall=wall, queue_share=qs, served=served)
        fail_up = why.startswith("fail up")
        target, why, _ = v.decide(target, spend_ok=(f > mod.DEAD and ws >= mod.WAIT_SHARE),
                                  give_ok=(f < -mod.DEAD and served and qs < mod.GIVEBACK_WAIT_SHARE and idle >= 1),
                                  t=t, why=why, stress=f > mod.DEAD, calm=f < -mod.DEAD, fail_up=fail_up)
        out.append({"t": t, "cur": cur, "short": qs >= mod.GIVEBACK_WAIT_SHARE, "idle_calm": False, "wrote": target != cur})
        if target != cur:
            dd = (target > cur) - (target < cur)
            last_dir, last_change = (0, t) if fail_up else (dd, t)
            cur = target
    return out


def replay_redis(mod, rows, native):
    """The ceiling wire's own rule on the recorded seconds (decide alone: the rule the store fix leaves unchanged)."""
    wall = wall_of(mod, mod.LINE_MS)
    return [mod.decide(r["p"], r["force"], r["evicted_last_s"], r["maxmemory_mb"], 99.0, r["full"], wall=wall) for r in rows]


def replay_sysbench(mod, rows, native):
    """The buffer-pool wire as omni-v21's Omni.run calls it, on the recorded seconds (the standing wire)."""
    v = KnobVerdict(native, mod.STEP_MB, mod.COVER_MB, objective="resource", settle_s=mod.TAU, max_trial=120)
    wall = wall_of(mod, mod.LINE_STMT_MS)
    cur, last_change, out = native, -1e9, []
    for r in rows:
        t, f, p, share, rq = r["t"], r["force"], r["p"], r["miss_share"], r["read_requests_last_s"]
        resizing = mod.resizing(r.get("resize") or "") if hasattr(mod, "resizing") else False
        full = r["full"] if cur == r["pool_mb"] else r["used_mb"] >= mod.FULL * cur
        v.observe(r.get("cost"), t, settled=not resizing)
        target, why = mod.decide(p, f, share, cur, t - last_change, full, wall=wall, reads=rq > 0)
        target, why, _ = v.decide(target, spend_ok=(f > 0.05 and full and share >= mod.GROW_MISS_SHARE),
                                  give_ok=(f < -0.05 and rq > 0 and share < mod.GIVEBACK_MISS_SHARE),
                                  t=t, why=why, stress=f > 0.05, calm=f < -0.05, fail_up=why.startswith("fail up"))
        wrote = target != cur and not resizing
        out.append({"t": t, "cur": cur, "short": rq > 0 and share >= mod.GROW_MISS_SHARE, "idle_calm": False, "wrote": wrote})
        if wrote:
            last_change = t; cur = target
    return out


def replay_redis_traj(mod, rows, native):
    """The ceiling wire as omni-v21's Omni.run calls it, on the recorded seconds (the standing wire)."""
    v = KnobVerdict(native, mod.STEP_MB, mod.COVER_MB, objective="resource", settle_s=mod.TAU)
    wall = wall_of(mod, mod.LINE_MS)
    cur, last_change, out = native, -1e9, []
    for r in rows:
        t, f, p, ev = r["t"], r["force"], r["p"], r["evicted_last_s"]
        full = r["full"] if cur == r["maxmemory_mb"] else r["used_mb"] >= mod.FULL * cur
        v.observe(r.get("cost"), t)
        target, why = mod.decide(p, f, ev, cur, t - last_change, full, wall=wall)
        target, why, _ = v.decide(target, spend_ok=(f > 0.05 and full), give_ok=(f < -0.05 and ev == 0), t=t, why=why,
                                  stress=f > 0.05, calm=f < -0.05, fail_up=why.startswith("fail up"))
        out.append({"t": t, "cur": cur, "short": ev > 0 and f > 0.05, "idle_calm": False, "wrote": target != cur})
        if target != cur:
            if target > cur:
                last_change = t
            cur = target
    return out


def replay_brain(mod, rows, native, wire):
    """A candidate wire's Brain (omni-v22: the max) on the recorded seconds: its knob moves by its own decisions, the world's
    readings are the recorded ones (open-loop, as the gate's header says). The observation each wire's Brain reads is built from
    the standing audit's fields; a field the old audits lack (Kafka's arrivals, Redis's hit and miss latencies) is None, and the
    Brain decides as it does without it."""
    brain = mod.Brain(native, "resource")
    cur, out = native, []
    for r in rows:
        t = r["t"]; reading = r["reading_ms"] / 1000.0
        if wire == "sysbench":
            full = r["full"] if cur == r["pool_mb"] else r["used_mb"] >= mod.FULL * cur
            obs = {"reading_s": reading, "statements": r.get("statements", 0), "miss_share": r["miss_share"], "pool_mb": cur, "used_mb": r["used_mb"],
                   "full": full, "reads": r["read_requests_last_s"] > 0, "resizing": mod.resizing(r.get("resize") or "") if hasattr(mod, "resizing") else False,
                   "cpu_share": r.get("cpu_share")}
            short = obs["reads"] and r["miss_share"] >= mod.GROW_MISS_SHARE
        elif wire == "ycsb":
            ev = r.get("evicted_last_s", 0)
            full = r["full"] if cur == r["cache_mb"] else (mod.cache_full(r["used_mb"], cur, ev) if hasattr(mod, "cache_full") else r["used_mb"] >= mod.FULL * cur)
            obs = {"reading_s": reading, "reads": r.get("reads", 0), "miss_share": r["miss_share"], "cache_mb": cur, "used_mb": r["used_mb"], "full": full,
                   "requested": r["pages_requested_last_s"] > 0, "cpu_share": r.get("cpu_share")}
            short = obs["requested"] and r["miss_share"] >= mod.GROW_MISS_SHARE
        elif wire == "redis":
            obs = {"reading_s": reading, "n": r.get("requests_last_s", 0), "inside": r.get("inside_last_s", 0), "evicted_last_s": r["evicted_last_s"],
                   "ceiling_mb": cur, "used_mb": r["used_mb"], "cpu_share": r.get("cpu_share")}
            short = r["evicted_last_s"] > 0 and r["force"] > 0.05
        elif wire == "kafka":
            obs = {"reading": reading if r.get("consumed_last_s", 0) else None, "n_msg": r.get("consumed_last_s", 0), "inside": r.get("inside_last_s", 0),
                   "lag": r["lag"], "idle": r["idle"], "consumers": cur, "cpu_share": r.get("cpu_share"), "arrivals": None}
            short = r["lag"] > 0 and r["force"] > 0.05
        elif wire == "pgbench":
            obs = {"reading_s": reading, "wait_share": r["wait_share"], "idle": r["idle"], "pool": cur, "queue_share": r["queue_share"],
                   "served": r["served"]}
            short = r["queue_share"] >= mod.GIVEBACK_WAIT_SHARE
        else:
            raise ValueError(wire)
        target, why, info = brain.step(t, obs)
        wrote = target != cur and not (wire == "sysbench" and obs["resizing"])
        idle_calm = wire == "kafka" and r["force"] < -0.05 and r["lag"] <= cur * POLL_RECORDS
        out.append({"t": t, "cur": cur, "short": short, "idle_calm": idle_calm, "wrote": wrote})
        if wrote:
            cur = target
    return out


def gauges_of(traj, native, recorded_key=None, rows=None):
    n = len(traj) or 1
    g = {"setting_mean": sum(x["cur"] for x in traj) / n, "writes": sum(x["wrote"] for x in traj),
         "below_native_s": sum(1 for x in traj if x["cur"] < native),
         "below_native_short_s": sum(1 for x in traj if x["cur"] < native and x["short"]),
         "above_native_idle_s": sum(1 for x in traj if x["cur"] > native and x["idle_calm"]),
         "first_writes": sum(1 for x in traj if x["wrote"] and x["t"] < WINDOW_S)}
    if recorded_key and rows:
        g["matches_record"] = sum(1 for x, r in zip(traj, rows) if x["cur"] == r[recorded_key]) / n
    return g


# --------------------------------------------------------------------------------------------------- the archive
WIRES = {
    # wire: (table, raw folder prefix, workloads, recorded knob key, native, replay)
    "pgbench": ("PGBENCH", "pgbench", ("select", "simple_update", "tpcb_hot"), "pool", 20, replay_pgbench),
    "kafka": ("KAFKA", "kafka", ("burst", "heavy", "light"), "consumers", 2, replay_kafka),
    "ycsb": ("YCSB", "ycsb", ("b", "burst", "c", "f"), "cache_mb", 512, replay_ycsb),
    "sysbench": ("SYSBENCH", "sysbench", ("burst", "read_only", "read_write", "update_index"), "pool_mb", 512, replay_sysbench),
    "redis": ("REDIS", "redis", ("burst", "large", "small"), "maxmemory_mb", 64, replay_redis_traj),
}


NOTES = {   # what each candidate changes, in the gate's words (the store fix of 25 October)
    "pgbench": "omni-v22, the max: a server added while clients wait is never clamped by an allowance, and the pool is never taken below the "
               "pooler's own setting (the standing wire's calm give-back took it below, inside the allowance, and the queue line added the "
               "servers back when the load rose): the seconds below native fall to none, the servers held rise, power given.",
    "kafka": "omni-v22, the max: the group's twin (each partition's arrivals placed on the members by the range assignor) and the reflex, "
             "never clamped by an allowance, with a hold that hands a consumer back only to a count that carries the last minute's peak. "
             "omni-v21's audits carry no arrivals, so in this replay the twin reads none and the reflex adds consumers from the compass's "
             "own wanting; the closed-loop model, which carries them, shows the twin at work (tools/kafka_model.py).",
    "ycsb": "The candidate holds more cache. Below native it hands a notch back each second while the cache misses 1% or more (the seconds "
            "below native while short fall), and its full (WiredTiger's own 80%, or evicting) opens the grow path on seconds that were slow, "
            "missing and evicting, which the standing wire read as 'slow with room to spare' at 90%: spend trials above native, power given, "
            "allowed by the verdict on the recorded cost samples, which in an open-loop replay never show what the larger cache would have "
            "bought. The writes rise with the hand-backs and the spends: wear, power given.",
    "sysbench": "omni-v22, the max: the pool never below the operator's (the seconds below native fall to none), and memory spent only where "
                "the server's own account (the performance schema's timer on the data files' reads) says the misses cost the statements and "
                "the host has a chunk to spare. omni-v21's audits carry neither account, so in this replay the candidate holds at native and "
                "writes nothing: the first run on omni-v22 reads them; the memory the tune-down gave back is the tune-down's (dial save).",
    "ycsb": "omni-v22, the max: the cache never below the operator's (the seconds below native fall to none), and memory spent only where "
            "WiredTiger's own account (its time reading pages from disk for the application's threads) says the misses cost the reads and "
            "the host has a notch to spare. omni-v21's audits carry neither account, so in this replay the candidate holds at native and "
            "writes nothing: the first run on omni-v22 reads them.",
    "redis": "omni-v22, the max: misses with the cache full go through unclamped (the standing wire's allowance refused them in 4,426 of "
             "the 4,581 seconds over the line) where the application's own split says they cost the service and the host has a notch to "
             "spare, and the ceiling is never handed back below the working set's floor nor below the operator's. omni-v21's audits carry "
             "neither the split nor the host's memory, so in this replay the candidate holds at native; the closed-loop model, which carries "
             "both, shows what the larger cache buys (tools/redis_model.py).",
}


def run_ids(engine, table):
    return [f"{r['tag']} {r['run']}" for r in json.loads((LIVE / f"{engine}_{table}.json").read_text())["runs"]]


def audits(raw, engine, table, prefix, wl):
    """[(run tag, rep, rows)] of every omni arm's audit of one workload, from the runs the engine's three-run table names."""
    t = json.loads((LIVE / f"{engine}_{table}.json").read_text())
    out = []
    for run in t["runs"]:
        for rep_dir in sorted((Path(raw) / f"run-{run['run']}" / f"{prefix}-{wl}" / f"{prefix}-{wl}").glob("rep-*")):
            f = rep_dir / "omni" / "audit.jsonl"
            if f.exists():
                rows = [json.loads(x) for x in f.read_text().splitlines() if x.strip()]
                rows = [r for r in rows if "force" in r and "error" not in r]
                out.append((run["tag"], rep_dir.name, rows))
    return out


def read_pairs(name, pairs, gauges=GAUGES):
    res = {}
    for g, (aim, spent) in gauges.items():
        base = [b[g] for b, _ in pairs]; cand = [c[g] for _, c in pairs]
        if aim is None:
            res[g] = {"standing": sum(base) / len(base), "candidate": sum(cand) / len(cand), "word": "shown"}
            continue
        r = reading(g, [c[g] - b[g] for b, c in pairs], base, gauges={g: (aim, spent)})
        res[g] = {"standing": sum(base) / len(base), "candidate": sum(cand) / len(cand), **r}
    return res


def sysbench_counters(raw, engine):
    """Per arm: the statements a second the standing reading counted (the audit) against the statements sysbench sent (its
    per-notch summaries: reads and writes, what the candidate's reading counts)."""
    t = json.loads((LIVE / f"{engine}_SYSBENCH.json").read_text())
    out = {}
    for wl in ("read_only", "read_write", "update_index", "burst"):
        arms = []
        for run in t["runs"]:
            for rep_dir in sorted((Path(raw) / f"run-{run['run']}" / f"sysbench-{wl}" / f"sysbench-{wl}").glob("rep-*")):
                f = rep_dir / "omni" / "audit.jsonl"
                # the archive gzips a large log (archive-run.yml): read it in either form
                logs = sorted((rep_dir / "omni").glob("notch-*.log")) + sorted((rep_dir / "omni").glob("notch-*.log.gz"))
                if not f.exists() or not logs:
                    continue
                rows = [json.loads(x) for x in f.read_text().splitlines() if x.strip()]
                seen = [r.get("statements", 0) for r in rows if "statements" in r]
                rw, secs = 0, 0.0
                for lg in logs:
                    txt = gzip.decompress(lg.read_bytes()).decode() if lg.suffix == ".gz" else lg.read_text()
                    m_r = re.search(r"read:\s+(\d+)", txt); m_w = re.search(r"write:\s+(\d+)", txt); m_t = re.search(r"total time:\s+([0-9.]+)s", txt)
                    if m_r and m_w and m_t:
                        rw += int(m_r.group(1)) + int(m_w.group(1)); secs += float(m_t.group(1))
                if seen and secs:
                    arms.append({"run": run["tag"], "rep": rep_dir.name, "standing_reading_per_s": sum(seen) / len(seen),
                                 "workload_statements_per_s": rw / secs})
        if arms:
            out[wl] = {"arms": arms, "standing_reading_per_s": sum(a["standing_reading_per_s"] for a in arms) / len(arms),
                       "workload_statements_per_s": sum(a["workload_statements_per_s"] for a in arms) / len(arms)}
    return out


def redis_identity(raw, engine, base_mod, cand_mod):
    t = json.loads((LIVE / f"{engine}_REDIS.json").read_text())
    seconds = differ = 0
    for wl in ("burst", "large", "small"):
        for run in t["runs"]:
            for f in sorted((Path(raw) / f"run-{run['run']}" / f"redis-{wl}" / f"redis-{wl}").glob("rep-*/omni/audit.jsonl")):
                rows = [json.loads(x) for x in f.read_text().splitlines() if x.strip()]
                rows = [r for r in rows if "force" in r and "maxmemory_mb" in r]
                a, b = replay_redis(base_mod, rows, 64), replay_redis(cand_mod, rows, 64)
                seconds += len(rows); differ += sum(1 for x, y in zip(a, b) if x != y)
    return {"seconds": seconds, "decisions_different": differ}


# --------------------------------------------------------------------------------------------------- the report
def fmt_word(r):
    if r.get("word") in (None, "shown"):
        return "shown"
    rel, w = r.get("relative"), r["word"]
    noise = "" if r.get("beyond_noise") or w.startswith("STEADY") else ", inside the arms' noise"
    if rel is not None and rel == rel:
        return f"{by_word(100 * rel, w)} {w}{noise}"
    return f"{by_word(r['mean_change'], w, unit=' a arm', digits=2)} {w}{noise} (the standing wire's mean is 0)"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", default=BASE, help="the standing runners' git revision")
    ap.add_argument("--raw", default=str(LIVE / "raw"), help="the archived runs' folder (scripts/raw_archive.sh open places them here)")
    ap.add_argument("--engine", default="V16", help="the three-run tables whose runs are replayed")
    ap.add_argument("--out", default=str(OUT))
    a = ap.parse_args(argv)
    report = {"base": a.base, "engine_tables": a.engine, "class": "S (our own model: the archived seconds replayed open-loop)", "wires": {}}
    for wire, (table, prefix, wls, key, native, replay) in WIRES.items():
        base_mod, cand_mod = load_wire(f"run_{wire}", a.base), load_wire(f"run_{wire}")
        all_pairs, per_wl, matches, unread = [], {}, [], []
        for wl in wls:
            pairs = []
            for tag, rep, rows in audits(a.raw, a.engine, table, prefix, wl):
                b = gauges_of(replay(base_mod, rows, native), native, key, rows)
                # a candidate with a Brain (omni-v22, the max) is replayed through it; one without, as the standing wire is
                c = gauges_of(replay_brain(cand_mod, rows, native, wire) if hasattr(cand_mod, "Brain") else replay(cand_mod, rows, native), native)
                matches.append(b["matches_record"])
                if b["matches_record"] < MATCH_MIN:
                    unread.append({"workload": wl, "run": tag, "rep": rep, "matches_record": round(b["matches_record"], 3)})
                    continue
                pairs.append((b, c))
            if pairs:
                per_wl[wl] = {"arms": len(pairs), "reading": read_pairs(wire, pairs)}
                all_pairs += pairs
        if all_pairs:
            report["wires"][wire] = {"arms": len(all_pairs), "runs": run_ids(a.engine, table), "unread": unread, "standing_replay_matches_record": sum(matches) / len(matches),
                                     "standing_replay_matches_record_min": min(matches), "reading": read_pairs(wire, all_pairs), "workloads": per_wl}
    report["sysbench"] = sysbench_counters(a.raw, a.engine)
    report["redis"] = redis_identity(a.raw, a.engine, load_wire("run_redis", a.base), load_wire("run_redis"))
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    (out / "STORE_GATE.json").write_text(json.dumps(report, indent=1) + "\n")
    (out / "STORE_GATE.md").write_text("\n".join(render(report)) + "\n")
    print((out / "STORE_GATE.md").read_text())
    losses = [(w, wl, g) for w, d in report["wires"].items() for wl, x in [("all", d), *d["workloads"].items()]
              for g, r in x["reading"].items() if r.get("word") == "LOSS"]
    return 1 if losses else 0


def render(r):
    L = ["# The store gate: the data stores' wires, standing against candidate, on their own archived seconds", "",
         f"Evidence class S, our own model: every omni arm's archived audit seconds (the {r['engine_tables']} three-run tables' runs), "
         f"replayed decision by decision through the standing wires (the runners at `{r['base']}`) and the candidates (this checkout), "
         "each with its own verdict fed the recorded cost samples and its own knob. Open-loop: the inputs are those the standing wire's "
         "knob produced, so the gate says what each wire decides on the same seconds, never what a store would then have done. "
         "Each arm is one pair; the reading is the mean change over the arms, its 95% interval and the word by the gauge's aim "
         "(`tools/model_gate.py` `reading`, `tools/readings.py`). A reading here shows whether a change shows promise before a real run; "
         "it is never a benchmark result.", ""]
    for wire, d in r["wires"].items():
        L += [f"## {wire}: {d['arms']} omni arms", "",
              f"Runs (branch `raw`, `run-<id>/`): {', '.join(d.get('runs', []))}; each workload's three repetitions a run.", "",
              NOTES.get(wire, ""), "",
              f"The standing wire's replay reproduces its own recorded knob in {100 * d['standing_replay_matches_record']:.1f}% of the seconds "
              f"(the lowest arm {100 * d['standing_replay_matches_record_min']:.1f}%)."
              + ("" if not d.get("unread") else " Not read, the standing replay reproducing under 95% of its own record: "
                 + "; ".join(f"{u['workload']} run {u['run']} {u['rep']} ({100 * u['matches_record']:.1f}%)" for u in d["unread"])
                 + " (at the second it leaves its record, a verdict step reads the other way on the recorded seconds, which the audit rounds: t to 0.01 s, the cost to 1e-9)."), "",
              "| Gauge | Standing (mean a arm) | Candidate (mean a arm) | Candidate against standing |", "|---|---:|---:|---|"]
        for g, x in d["reading"].items():
            if g in ("above_native_idle_s", "first_writes") and wire != "kafka":
                continue
            L.append(f"| {LABELS[g]} | {x['standing']:.2f} | {x['candidate']:.2f} | {fmt_word(x)} |")
        L += ["", "By workload:", "", "| Workload | Arms | " + " | ".join(LABELS[g] for g in GAUGES if not (g in ('above_native_idle_s', 'first_writes') and wire != 'kafka')) + " |",
              "|---|---:|" + "---|" * len([g for g in GAUGES if not (g in ('above_native_idle_s', 'first_writes') and wire != 'kafka')])]
        for wl, x in d["workloads"].items():
            cells = [f"{x['reading'][g]['standing']:.1f} → {x['reading'][g]['candidate']:.1f}: {fmt_word(x['reading'][g])}"
                     for g in GAUGES if not (g in ("above_native_idle_s", "first_writes") and wire != "kafka")]
            L.append(f"| {wl} | {x['arms']} | " + " | ".join(cells) + " |")
        L.append("")
    s = r.get("sysbench") or {}
    L += ["## sysbench: the reading itself", "",
          "The candidate reads sysbench's own statements (its account, its prepared statements counted); the standing reading counted "
          "the four plain statement names for every account. The archived seconds hold only the standing reading's counter, so the "
          "candidate's decisions on its own reading cannot be replayed from these files: a short real run's files are the model's "
          "input for them. Both counters where the raw files hold them (the statements the standing reading counted were the harness's "
          "own monitoring SELECTs, so of the workload it saw none):", "",
          "| Workload | Arms | Statements a second the standing reading counted (the harness's own SELECTs) | Statements a second sysbench sent (reads and writes: what the candidate counts) | The standing count as a share of the workload's |",
          "|---|---:|---:|---:|---:|"]
    for wl, x in s.items():
        share = x["standing_reading_per_s"] / x["workload_statements_per_s"] if x["workload_statements_per_s"] else float("nan")
        L.append(f"| {wl} | {len(x['arms'])} | {x['standing_reading_per_s']:.1f} | {x['workload_statements_per_s']:,.0f} | {100 * share:.2f}% |")
    rd = r.get("redis") or {}
    L += ["", "## Redis: the rule unchanged", "",
          f"The ceiling's rule is the same in both wires: on {rd.get('seconds', 0):,} archived seconds the two decide differently in "
          f"{rd.get('decisions_different', 0)}. The CPU apart (redis-server, the application, the brain, the sampler) is a new gauge, "
          "read only by runs that record it.", ""]
    losses = [(w, wl, g) for w, d in r["wires"].items() for wl, x in [("all", d), *d["workloads"].items()]
              for g, x2 in x["reading"].items() if x2.get("word") == "LOSS"]
    L += ["## The gate's verdict", "",
          ("No LOSS: no judged gauge (time below native while short) rose on any wire or workload." if not losses
           else "LOSS: " + "; ".join(f"{w} {wl} {g}" for w, wl, g in losses) + ". Root-caused and fixed in the code before the version lands."), ""]
    return _legal_stamp(L) if _legal_stamp else L


if __name__ == "__main__":
    sys.exit(main())
