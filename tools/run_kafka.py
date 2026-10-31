#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Omni-Compass on top of a Kafka consumer group's operator-set size (docs/KAFKA_PREREGISTRATION.md).

Apache Kafka as shipped (one KRaft broker on the machine, its server.properties untouched but for the log directory) carries
a topic of 8 partitions. A producer offers messages at a stepped rate, the same in both arms; a consumer group reads them,
spends a declared service time of CPU on each (the work the messages are for), and records each message's end-to-end
latency, produce to consume. An operator sets the consumer count once; that fixed number is the native controller here.

  native  the consumer group at the operator's count (2 consumers) for the whole run
  omni    the same group, with the compass law (omnicompass/compass_law.py) on one knob, the consumer count, inside the
          cover [1, 8] (never under one consumer, never more consumers than partitions): the compass reads the group's own
          end-to-end latency on a band from 0 to the response line and holds it at 40% of the line; the service slow and
          messages waiting add consumers; calm gives back one idle consumer a second (above the operator's count, calm with
          nothing waiting gives one back with no idle test; idle is a full second with no message: store fix of 25 October);
          at 95% of the line every consumer the
          topic can use is started at once (fail up); the count is handed back to the operator's at the end and read back

Gauges from the consumers' own records (every message's latency), the group's lag (produced minus consumed) and the
host's /proc/stat (CPU seconds, the consumers' and the compass's own cost, counted against Omni). No energy is claimed
beyond the host's CPU seconds. Every row is reported, losses included.

  python3 tools/run_kafka.py --setup                      # start a broker and make the topics (the workflow does this)
  python3 tools/run_kafka.py --workloads tuning --reps 3 --out DIR
  python3 tools/run_kafka.py --report-only DIR            # re-read finished <workload>.json files and write KAFKA.md
"""
from __future__ import annotations

import argparse
import json
import math
import multiprocessing as mp
import os
import statistics
import subprocess
import sys
import threading
import time
from collections import deque
from pathlib import Path

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import pathlib as _p; sys.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from omnicompass.compass_law import Band, CompassLaw  # noqa: E402
from omnicompass.immune import Immune  # noqa: E402  (omni-v22: the immune system's self-knowledge on the group's knob)
from tools.knob_verdict import KnobVerdict, sample_cost, OBJECTIVES, RESOURCE as DEFAULT_OBJECTIVE  # noqa: E402  (amendment 2: the brain's own verdict)
from tools.readings import word as gel_word, aim as gel_aim, EVEN_SAME, EVEN_NOISE, SHOWN  # noqa: E402  (the words every table uses)

BOOTSTRAP = os.environ.get("KAFKA_BOOTSTRAP", "localhost:9092")
PARTITIONS = 8
LINE_MS = 500.0           # the response line: a message handled within 500 ms of being produced
CENTER = 0.4              # the compass holds the service at 40% of the line
DT = 1.0                  # one decision a second
TAU = 3.0                 # a consumer added or removed shows in the latency within a few seconds (the group rebalances)
SMOOTH = 0.5
NATIVE_CONSUMERS = 2      # the operator's count
COVER = (1, PARTITIONS)   # never under one consumer, never more than partitions
DWELL_S = 5.0             # no taking back within five seconds of a change
DIAL = os.environ.get("OMNI_DIAL", "max")   # omni-v22: max, the factory tune; save, the tune-down
POLL_RECORDS = 50         # the most messages a consumer takes in one poll (KafkaConsumer max_poll_records)
HEARTBEAT_MS = 3000       # the consumers' heartbeat (KafkaConsumer heartbeat_interval_ms, the client's own default): a member learns of a
                          # rebalance at its next heartbeat, so a change reaches every member within one interval
SESSION_MS = 10000        # the consumers' session timeout (KafkaConsumer session_timeout_ms, the client's own default)
HANDBACK_DWELL_S = 30.0   # store fix of 25 October: a consumer above the operator's count is handed back only 30 s after the last change (each
                          # change rebalances the whole group, and a hand-back that is undone at once is two pauses for nothing)
IDLE_S = 1.0              # store fix of 25 October: a consumer is idle only after a full second with no message (a sustained state, never one
                          # empty 200 ms poll), and a consumer starts busy: the omni-v16 runs read a momentary empty poll as idle, which made a
                          # 2 -> 1 -> 2 give-back trial and its fail-up (two rebalances) in the first 11 seconds of every omni arm, and with 8
                          # partitions keyed round-robin no consumer above the operator's count was ever idle, so none was ever given back
STEPS = "1 2 3 2 3 4 5 6 5 4 3 2 1 2 1"
BURST = "1 6 1 8 1 6"
PEAK_SHARE = 0.9          # the peak notch offers nine tenths of native's measured capacity
from omnicompass.student_t import T95  # noqa: E402  (the two-sided 95% point of Student's t, any degrees of freedom)
SAME_REL = 1e-6

WORKLOADS = {
    # name: (service ms of CPU per message, payload bytes, steps, tuning?)
    "tuning": (2.0, 256, STEPS, True),
    "light": (1.0, 128, STEPS, False),
    "heavy": (5.0, 1024, STEPS, False),
    "burst": (2.0, 256, BURST, False),
}

GAUGES = [  # key, label, direction
    ("work_inside_line_mps", "work inside the response line (messages a second handled within the line)", "higher"),
    ("mps", "throughput (messages a second consumed)", "higher"),
    ("p95_ms", "end-to-end latency, 95th percentile (ms)", "lower"),
    ("p99_ms", "end-to-end latency, 99th percentile (ms)", "lower"),
    ("p50_ms", "end-to-end latency, median (ms)", "lower"),
    ("mean_ms", "end-to-end latency, mean (ms)", "lower"),
    ("lag_max", "consumer lag, most messages waiting at once", "lower"),
    ("lag_mean", "consumer lag, mean messages waiting", "lower"),
    ("lost", "messages produced and never consumed", "never more"),
    ("consumers_mean", "consumers running, mean (the resources held)", "spent"),
    ("consumers_max", "consumers running, most at once", "spent"),
    ("cpu_busy_share", "host CPU busy (share of the run)", "spent"),
    ("cpu_seconds", "host CPU-seconds", "spent"),
    ("cpu_s_per_1k_inside", "host CPU-seconds per 1,000 messages inside the line", "spent"),
    ("rebalances", "consumer changes written (the knob's moves)", "shown"),
]


# ------------------------------------------------------------------ the producer and the consumers
def busy_ms(ms):
    """Spend `ms` of CPU on a message (the work the message is for)."""
    end = time.perf_counter() + ms / 1000.0
    x = 0.0
    while time.perf_counter() < end:
        x = math.sqrt(x + 1.0)
    return x


def producer_proc(topic, rate_steps, step_s, payload_bytes, produced, stop, log_path):
    """Offer messages at the stepped rate; every message carries its produce time (ns, the machine's monotonic clock)."""
    from kafka import KafkaProducer
    p = KafkaProducer(bootstrap_servers=BOOTSTRAP, linger_ms=5, acks=1)
    pad = b"x" * max(0, payload_bytes - 40)
    seq = 0
    with open(log_path, "w") as log:
        for rate in rate_steps:
            t_end = time.perf_counter() + step_s
            interval = 1.0 / max(rate, 1e-9)
            nxt = time.perf_counter()
            log.write(f"{time.time():.3f} rate {rate:.1f}\n"); log.flush()
            while time.perf_counter() < t_end and not stop.is_set():
                now = time.perf_counter()
                if now >= nxt:
                    p.send(topic, key=str(seq % PARTITIONS).encode(), value=f"{seq}:{time.perf_counter_ns()}:".encode() + pad)
                    seq += 1; nxt += interval
                    with produced.get_lock():
                        produced.value = seq
                else:
                    time.sleep(min(0.001, nxt - now))
            if stop.is_set():
                break
        p.flush(); p.close()


def consumer_proc(topic, group, service_ms, consumed, stop_evt, rec_path, idle_flag):
    """One consumer of the group: poll, spend the service time per message, record (consume time, latency ms)."""
    from kafka import KafkaConsumer
    c = KafkaConsumer(topic, bootstrap_servers=BOOTSTRAP, group_id=group, auto_offset_reset="earliest",
                      enable_auto_commit=True, max_poll_records=POLL_RECORDS, session_timeout_ms=SESSION_MS, heartbeat_interval_ms=HEARTBEAT_MS)
    n = 0
    last_msg = time.monotonic()                                 # a consumer starts busy: idle only after IDLE_S with no message
    with open(rec_path, "a") as rec:
        while not stop_evt.is_set():
            batch = c.poll(timeout_ms=200)
            got = 0
            for msgs in batch.values():
                for m in msgs:
                    seq, t_ns, _ = m.value.split(b":", 2)
                    busy_ms(service_ms)
                    lat_ms = (time.perf_counter_ns() - int(t_ns)) / 1e6
                    rec.write(f"{time.time():.3f} {seq.decode()} {lat_ms:.3f}\n")
                    got += 1
            if got:
                n += got; rec.flush()
                with consumed.get_lock():
                    consumed.value += got
            if got:
                last_msg = time.monotonic()
            idle_flag.value = 1 if is_idle(last_msg, time.monotonic()) else 0
    c.close()


def is_idle(last_msg_t, now, idle_s=IDLE_S):
    """A consumer is idle when no message has reached it for idle_s seconds or more (a sustained state, store fix of 25 October)."""
    return now - last_msg_t >= idle_s


class Group:
    """The consumer group as a fleet of processes: start one, stop one, how many run, which are idle."""

    def __init__(self, topic, group, service_ms, out: Path):
        self.topic, self.group, self.service_ms, self.out = topic, group, service_ms, out
        self.consumed = mp.Value("l", 0); self.procs = []; self.k = 0; self.changes = 0

    def start_one(self):
        stop = mp.Event(); idle = mp.Value("i", 0)                 # a consumer starts busy (store fix of 25 October)
        self.k += 1
        p = mp.Process(target=consumer_proc, args=(self.topic, self.group, self.service_ms, self.consumed, stop, str(self.out / f"consumer-{self.k}.log"), idle), daemon=True)
        p.start(); self.procs.append((p, stop, idle)); self.changes += 1

    def stop_one(self, prefer_idle=True):
        if not self.procs:
            return False
        order = sorted(range(len(self.procs)), key=lambda i: -self.procs[i][2].value) if prefer_idle else range(len(self.procs))
        i = list(order)[0]
        p, stop, _ = self.procs.pop(i); stop.set(); p.join(timeout=15); self.changes += 1
        return True

    def count(self):
        return len(self.procs)

    def idle(self):
        return sum(1 for _, _, f in self.procs if f.value)

    def stop_all(self):
        for p, stop, _ in self.procs:
            stop.set()
        for p, _, _ in self.procs:
            p.join(timeout=15)
        self.procs = []


# ------------------------------------------------------------------ the compass on the consumer count
def service_sample(rec_files, since_s, line_ms=LINE_MS):
    """The brain's sample from the consumers' own records: (the mean end-to-end latency in s of the messages consumed in the
    last second, or None when none was; how many were consumed; how many of them inside the line)."""
    now = time.time(); lat = []
    for f in rec_files:
        try:
            with open(f) as fh:
                fh.seek(0, 2); size = fh.tell(); fh.seek(max(0, size - 65536))
                for ln in fh.read().splitlines()[-400:]:
                    t, _, l = ln.split(" ")
                    if float(t) >= now - since_s:
                        lat.append(float(l) / 1000.0)
        except (OSError, ValueError):
            pass
    if not lat:
        return None, 0, 0
    return sum(lat) / len(lat), len(lat), sum(1 for l in lat if l * 1000.0 <= line_ms)


def service_reading(rec_files, since_s):
    """The group's own reading: the mean end-to-end latency (s) of the messages consumed in the last second; nothing
    consumed reads as the lag's age (messages waiting with no one taking them), capped at the line."""
    return service_sample(rec_files, since_s)[0]


def decide(p, force, lag, idle, cur, last_change_age, wall=0.95, snapshot=None, consumed=None):
    """The knob's move this second: (target, direction, why). The service slow with messages waiting adds consumers,
    ceil(force / 0.1) at a time; calm gives back one idle consumer a second, after the dwell; past the wall, every
    consumer the topic can use at once.
    Store fix of 25 October: above the operator's own count (snapshot), calm with no more waiting than the group takes in one
    poll round (POLL_RECORDS a consumer: the messages in flight between the producer and the consumers, which keep the lag
    above zero in 388 of 389 calm seconds of an omni-v16 arm) gives one consumer back, HANDBACK_DWELL_S after the last change,
    with no idle test (every consumer of a topic keyed round-robin has work, so the idle test held a consumer added above
    native to the end of the arm). Below the operator's count the idle test and an empty backlog stay. A second in which the
    group consumed nothing (consumed 0: before the producer starts, or a rebalance) says nothing about the demand: nothing
    is given back in it."""
    lo, hi = COVER
    if p is not None and p >= wall:
        return hi, 0, "fail up: the line is at hand, every consumer at once"
    if force > 0.05 and lag > 0:
        want = min(hi, cur + max(1, math.ceil(force / 0.1)))
        return want, (1 if want != cur else 0), f"slow with {lag} waiting: add {want - cur}"
    if consumed is not None and consumed <= 0:
        return cur, 0, "nothing consumed in the last second: nothing known, nothing taken"
    if (snapshot is not None and cur > snapshot and force < -0.05 and lag <= cur * POLL_RECORDS
            and last_change_age >= HANDBACK_DWELL_S):
        return cur - 1, -1, "calm, nothing waiting beyond one poll round, above the operator's count: one consumer given back"
    if force < -0.05 and idle > 0 and cur > lo and last_change_age >= DWELL_S and lag == 0 and (snapshot is None or cur <= snapshot):
        return cur - 1, -1, "calm, an idle consumer given back"
    return cur, 0, "hold"


# omni-v22: the group's twin and the immune reflex (docs/KAFKA_PREREGISTRATION.md, amendment 4; docs/STORE_ROOT_CAUSES_2026-10-30.md).
# On omni-v21 the verdict's allowance clamped every move, the wall's fail-up included, and the wall abandoned every spend trial, so in
# 1,413 of the 1,428 seconds the service stood over its line the brain asked for consumers and was refused; and the hand-back gave
# a consumer back that the load still needed, each give-back and re-add a rebalance of the whole group (a median 2.58 s and 1.24 s
# of every message waiting). The twin knows which count carries the load; the reflex goes there and holds it.
RHO_SPEND = 0.9           # the twin spends to the smallest count whose busiest member runs at or under nine tenths of its rate
RHO_HAND = 0.7            # it hands back only to a count whose busiest member stays at or under seven tenths at the window's peak
HANDBACK_WINDOW_S = 60.0  # the window the hand-back reads the arrivals' peak over
DRAIN_S = 2 * TAU         # a backlog the twin finds, and the one a change's own rebalance makes, is drained within this
MU_KEEP = 15              # the member's rate: the median of the twin's last 15 estimates
STALL_KEEP = 9            # a change's own stall: the median of the last 9 the group showed


class RateTwin:
    """The consumer group's twin: each partition's arrivals (the topic's log-end offsets, once a second) placed on the members by
    Kafka's range assignor, and one member's rate learned from the group's own seconds. In a second in which the queue grew
    and no change was settling, the group consumed sum(min(load_i, mu)) over its members (the members over their rate serve
    mu, the others their load), solved for mu. The stall a change costs is learned the same way: the seconds after a change in
    which the group consumed under half its rate before it. Nothing in it is a number written for a workload."""

    def __init__(self, partitions=PARTITIONS):
        self.partitions = partitions
        self.mu_est = deque(maxlen=MU_KEEP)
        self.stalls = deque(maxlen=STALL_KEEP)
        self.watch = None                       # (time of the change, the rate consumed before it, seconds stalled so far)

    @property
    def mu(self):
        return statistics.median(self.mu_est) if self.mu_est else None

    @property
    def stall_s(self):
        """A change's own stall: the median the group showed, or, before it has shown one, the protocol's bound (a rebalance
        reaches every member within one heartbeat interval, the consumers' own setting)."""
        return statistics.median(self.stalls) if self.stalls else HEARTBEAT_MS / 1000.0

    def ranges(self, c):
        c = max(1, min(c, self.partitions))
        n, extra = divmod(self.partitions, c)
        out, start = [], 0
        for i in range(c):
            size = n + (1 if i < extra else 0)
            out.append(range(start, start + size)); start += size
        return out

    def loads(self, c, arrivals, backlog=None):
        """Each member's load (messages a second) at count c: its partitions' arrivals, and a backlog to drain within DRAIN_S."""
        total = sum(arrivals) or 1.0
        out = []
        for r in self.ranges(c):
            a = sum(arrivals[p] for p in r)
            if backlog:
                a += backlog * (a / total) / DRAIN_S       # the backlog sits where the messages arrive
            out.append(a)
        return out

    def learn(self, c, arrivals, consumed):
        loads = self.loads(c, arrivals)
        total = sum(loads)
        if consumed <= 0 or consumed >= 0.98 * total:
            return None
        lo, hi = 0.0, max(loads)
        for _ in range(48):
            mid = (lo + hi) / 2
            if sum(min(x, mid) for x in loads) < consumed:
                lo = mid
            else:
                hi = mid
        mu = (lo + hi) / 2
        if mu > 0:
            self.mu_est.append(mu)
        return mu

    def changed(self, t, consumed_before):
        self.watch = [t, consumed_before, 0]

    def after_change(self, t, consumed):
        """Counts the seconds after a change the group consumed under half its rate before it: the change's own stall."""
        if self.watch is None:
            return
        t0, before, stalled = self.watch
        if before > 0 and consumed < 0.5 * before and t - t0 <= 10:
            self.watch[2] = stalled + 1
            return
        if t - t0 >= 1:
            self.stalls.append(float(stalled)); self.watch = None

    def busiest(self, c, arrivals, backlog=0.0):
        mu = self.mu
        return None if mu is None else max(self.loads(c, arrivals, backlog)) / mu

    def needed(self, arrivals, lo, hi, rho, backlog=0.0):
        """The smallest count in [lo, hi] whose busiest member runs at or under rho; where none does, the smallest count with the
        least busy busiest member (a count that adds no relief is never chosen over a smaller one)."""
        best = None
        for c in range(lo, hi + 1):
            b = self.busiest(c, arrivals, backlog)
            if b is None:
                return None
            if b <= rho:
                return c
            if best is None or b < best[0] - 1e-9:
                best = (b, c)
        return best[1]


class Brain:
    """The knob's decision, one a second (omni-v22): the same code the real run (Omni) and the closed-loop model
    (tools/kafka_model.py) drive. obs: reading (s, or None), n_msg, inside, lag, idle, consumers, cpu_share and arrivals (each
    partition's messages a second, or None while unread).

      the reflex   with the twin's rate known: the count cannot carry the arrivals and the backlog (its own and the one a change's
                   stall would add) at nine tenths of its rate, so the knob goes at once to the smallest count that can, up to the
                   partitions; the immune system's reflex, never clamped by the verdict's allowance (the allowance judges the
                   compass's own moves). At the wall with no rate known, the compass's fail-up goes one consumer up, and the
                   twin learns the rate from the second it sees the queue grow
      the hold     above the operator's count the knob stays where the reflex put it; it is handed back, in one move (one
                   rebalance), only to the smallest count at or above the operator's whose busiest member stays at or under seven
                   tenths of its rate at the arrivals' peak of the last 60 s, 30 s after the last change, calm, nothing waiting
                   beyond one poll round a consumer
      the floor    never below the operator's count (the max, the factory tune)
      the immune   Omni-Compass's count redlining past the line, stuck, and native's twin (the operator's count on the same
                   arrivals) reading lower: the knob goes back to native for the immune hold (omnicompass/immune.py)
      the rest     the compass law and the verdict as on omni-v21, inside the allowance, never under the reflex's count"""

    def __init__(self, snapshot, objective=DEFAULT_OBJECTIVE, line_ms=LINE_MS):
        self.snapshot = snapshot; self.objective = objective; self.line_s = line_ms / 1000.0
        self.law = CompassLaw(Band(0.0, self.line_s, center=CENTER), dt=DT, tau=TAU, smooth=SMOOTH)
        self.verdict = KnobVerdict(snapshot, 1, COVER, objective=objective, settle_s=2 * TAU)   # a consumer that joins rebalances the group first
        self.twin = RateTwin()
        self.immune = Immune()
        self.window = deque()                    # (t, arrivals) over HANDBACK_WINDOW_S
        self.last_change = -1e9; self.prev_lag = None; self.prev_consumed = 0; self.failups = 0

    def step(self, t, obs):
        lo, hi = max(COVER[0], self.snapshot), COVER[1]
        reading = obs["reading"]; lag, n_msg, cur, idle = obs["lag"], obs["n_msg"], obs["consumers"], obs["idle"]
        if reading is None:
            reading = min(self.line_s, 0.0 if lag == 0 else self.line_s)        # waiting with no one consuming: the line
        f = self.law.force(reading)
        cost = sample_cost(self.objective, obs["inside"], reading if n_msg else None, cur, obs["cpu_share"])
        self.verdict.observe(cost, t)
        arrivals = obs.get("arrivals")
        settling = t - self.last_change < 2 * TAU
        self.twin.after_change(t, n_msg)
        if arrivals is not None:
            self.window.append((t, list(arrivals)))
            while self.window and t - self.window[0][0] > HANDBACK_WINDOW_S:
                self.window.popleft()
            grew = self.prev_lag is not None and lag > self.prev_lag
            if grew and not settling:
                self.twin.learn(cur, arrivals, n_msg)
        self.prev_lag = lag
        info = {"mu": None if self.twin.mu is None else round(self.twin.mu, 1), "stall_s": round(self.twin.stall_s, 2)}
        target, why = None, None
        if arrivals is not None and self.twin.mu is not None:
            rate = sum(arrivals)
            backlog = lag + self.twin.stall_s * rate             # what waits now, and what one change's stall would add
            busy_now = self.twin.busiest(cur, arrivals, lag)
            info["busiest"] = round(busy_now, 3)
            if busy_now > RHO_SPEND and not settling:
                want = self.twin.needed(arrivals, max(lo, cur), hi, RHO_SPEND, backlog)
                if want is not None and want > cur:
                    target, why = want, f"the twin: the busiest member at {busy_now:.2f} of its rate; {want} consumers carry it"
            elif cur > lo and not settling and t - self.last_change >= HANDBACK_DWELL_S and f < -0.05 and lag <= cur * POLL_RECORDS:
                peak = [max(a[p] for _, a in self.window) for p in range(PARTITIONS)]
                want = self.twin.needed(peak, lo, cur, RHO_HAND, 0.0)
                if want is not None and want < cur:
                    target, why = want, f"calm, and {want} consumers carry the last {HANDBACK_WINDOW_S:.0f} s's peak at {RHO_HAND} of their rate: handed back in one move"
        if target is None:
            d_target, _, d_why = decide(self.law.p, f, lag, idle, cur, t - self.last_change, wall=self.law.band.wall_high,
                                        snapshot=self.snapshot, consumed=n_msg)
            fail_up = d_why.startswith("fail up")
            if fail_up and self.twin.mu is None:
                target, why = min(hi, cur + 1), "fail up, the twin's rate not yet known: one consumer up"
                self.failups += 1
            else:
                v_target, why, vinfo = self.verdict.decide(d_target, spend_ok=(f > 0.05 and lag > 0), give_ok=False, t=t, why=d_why,
                                                           stress=f > 0.05, calm=f < -0.05, fail_up=fail_up)
                info.update(vinfo)
                target = max(lo, v_target)
                if cur > lo and target < cur:
                    target, why = cur, f"{why}; held at the reflex's count until the hand-back's terms are met"
                if target > cur and (settling or (arrivals is not None and self.twin.mu is not None)):
                    # a change's own stall is not demand, and where the twin knows the group only the twin adds: the compass's
                    # add, read on the seconds a hand-back's rebalance stalled the group, re-added the consumer just handed back
                    # (the model, heavy, seeds 105 and 108: 2 -> 3 -> 2 every 30 s)
                    target, why = cur, f"{why}; the twin carries the spend: held"
        # the immune system's self-knowledge: Omni-Compass's count redlining and stuck, native's twin reading lower
        p_omni = reading / self.line_s
        p_native = p_omni
        if arrivals is not None and self.twin.mu is not None:
            b_nat = self.twin.busiest(self.snapshot, arrivals, lag)
            b_cur = self.twin.busiest(cur, arrivals, lag)
            p_native = p_omni * (b_nat / b_cur) if b_cur else p_omni
        mode, ev = self.immune.tick(p_omni, p_native, moved=target != cur, at_limit=cur >= hi)
        if mode == "native":
            target, why = self.snapshot, "the immune system: Omni-Compass's count redlined, stuck, and native's twin reads lower: native holds the knob"
            if ev:
                info["immune"] = ev
        if target != cur:
            self.twin.changed(t, n_msg)
            self.last_change = t
        info.update({"p": round(self.law.p, 4), "force": round(f, 4)})
        return target, why, info


class Offsets:
    """The topic's log-end offset of each partition, read from the broker once a second (one wire in): each partition's arrivals,
    as any deployment reads them (the consumer group tool's LOG-END-OFFSET)."""

    def __init__(self, topic):
        from kafka import KafkaConsumer, TopicPartition
        self.c = KafkaConsumer(bootstrap_servers=BOOTSTRAP, group_id=None, enable_auto_commit=False)
        self.tps = [TopicPartition(topic, p) for p in range(PARTITIONS)]
        self.last, self.last_t = None, None

    def rates(self, now):
        try:
            end = self.c.end_offsets(self.tps)
        except Exception:
            return None
        cur = [end.get(tp, 0) for tp in self.tps]
        out = None
        if self.last is not None and now > self.last_t:
            out = [max(0.0, (a - b) / (now - self.last_t)) for a, b in zip(cur, self.last)]
        self.last, self.last_t = cur, now
        return out

    def close(self):
        try:
            self.c.close()
        except Exception:
            pass


class Omni(threading.Thread):
    """The brain, one decision a second, writing the audit; the knob is handed back at the end and read back. Amendment 2 (the
    brain's own verdict, 2026-10-09): the compass's own moves are written only inside the allowance a paired trial on the group
    itself has earned under the declared objective (tools/knob_verdict.py around the engine's own Verdict). From omni-v22 the
    decision is the Brain's (above): the twin's reflex and hold, the floor at the operator's count, the immune system."""

    def __init__(self, grp: Group, produced, audit_path: Path, line_ms=LINE_MS, objective=DEFAULT_OBJECTIVE, topic=None, dial=DIAL):
        super().__init__(daemon=True)
        self.grp, self.produced, self.audit, self.line_ms, self.objective, self.topic, self.dial = grp, produced, audit_path, line_ms, objective, topic, dial
        self.law = CompassLaw(Band(0.0, line_ms / 1000.0, center=CENTER), dt=DT, tau=TAU, smooth=SMOOTH)   # the tune-down's own law
        self.stop_flag = threading.Event(); self.failups = 0; self.handed_back = False; self.verdict = None; self.brain = None; self.last_change = -1e9

    def govern_record(self):
        """The record of what governed the knob: the max's twin and verdict (omni-v22) or the verdict alone (the tune-down)."""
        return self.verdict.record() if self.verdict else None

    def run(self):
        snapshot = self.grp.count()                        # read once, before the first write: the operator's count
        t0 = time.monotonic(); cpu_prev = cpu_times()
        self.verdict = KnobVerdict(snapshot, 1, COVER, objective=self.objective, settle_s=2 * TAU)   # a consumer that joins rebalances the group first
        if self.dial == "max":
            self.brain = Brain(snapshot, self.objective, self.line_ms); self.verdict = self.brain.verdict
        offsets = None
        if self.topic:
            try:
                offsets = Offsets(self.topic)
            except Exception:
                offsets = None                             # unread arrivals: the twin waits, the compass decides as on omni-v21
        with open(self.audit, "w") as fh:
            while not self.stop_flag.is_set():
                tick = time.monotonic()
                recs = [self.grp.out / f"consumer-{k}.log" for k in range(1, self.grp.k + 1)]
                lag = max(0, self.produced.value - self.grp.consumed.value)
                reading, n_msg, inside = service_sample(recs, 1.0, self.line_ms)
                cur = self.grp.count(); idle = self.grp.idle()
                cpu_now = cpu_times(); d_total = cpu_now[0] - cpu_prev[0]; d_idle = cpu_now[1] - cpu_prev[1]; cpu_prev = cpu_now
                cpu_share = (1.0 - d_idle / d_total) if d_total > 0 else None
                arrivals = offsets.rates(tick) if offsets else None
                shown = reading if reading is not None else min(LINE_MS / 1000.0, 0.0 if lag == 0 else LINE_MS / 1000.0)
                if self.brain is not None:                                               # the max (omni-v22): the twin, the reflex, the hold
                    obs = {"reading": reading, "n_msg": n_msg, "inside": inside, "lag": lag, "idle": idle, "consumers": cur,
                           "cpu_share": cpu_share, "arrivals": arrivals}
                    target, why, info = self.brain.step(tick - t0, obs)
                    fail_up = False
                else:                                                                    # the tune-down: omni-v21's loop
                    f = self.law.force(shown)
                    cost = sample_cost(self.objective, inside, shown if n_msg else None, cur, cpu_share)
                    self.verdict.observe(cost, tick - t0)                                 # measured under the count of the last second
                    target, d, why = decide(self.law.p, f, lag, idle, cur, tick - self.last_change, wall=self.law.band.wall_high, snapshot=snapshot,
                                            consumed=n_msg)
                    fail_up = why.startswith("fail up")
                    # a give-back above the operator's count is the hand-back of a spend, inside the allowance: no give-back trial (whose
                    # steps run below native) is started for it
                    target, why, info = self.verdict.decide(target, spend_ok=(f > 0.05 and lag > 0), give_ok=(f < -0.05 and idle > 0 and lag == 0 and cur <= snapshot and n_msg > 0),
                                                            t=tick - t0, why=why, stress=f > 0.05, calm=f < -0.05, fail_up=fail_up)
                    info.update({"p": round(self.law.p, 4), "force": round(f, 4), "cost": None if cost is None else round(cost, 9), "dial": "save"})
                if target > cur:
                    for _ in range(target - cur):
                        self.grp.start_one()
                    self.last_change = tick
                    if fail_up:
                        self.failups += 1
                elif target < cur:
                    for _ in range(cur - target):
                        self.grp.stop_one()
                    self.last_change = tick
                fh.write(json.dumps({"t": round(tick - t0, 2), "reading_ms": round(shown * 1000, 2), "lag": lag, "idle": idle,
                                     "consumers": cur, "target": target, "consumed_last_s": n_msg, "inside_last_s": inside,
                                     "cpu_share": None if cpu_share is None else round(cpu_share, 4),
                                     "arrivals": None if arrivals is None else [round(x, 1) for x in arrivals],
                                     "allowed_low": self.verdict.allowed_low, "allowed_high": self.verdict.allowed_high,
                                     **info, "why": why}) + "\n")
                time.sleep(max(0.0, DT - (time.monotonic() - tick)))
        if self.brain is not None:
            self.failups = self.brain.failups
        if offsets:
            offsets.close()
        # the hand-back: the operator's count, read back
        while self.grp.count() > snapshot:
            self.grp.stop_one(prefer_idle=False)
        while self.grp.count() < snapshot:
            self.grp.start_one()
        self.handed_back = self.grp.count() == snapshot


class Sampler(threading.Thread):
    """Consumers running and lag, once a second, in both arms."""

    def __init__(self, grp: Group, produced):
        super().__init__(daemon=True)
        self.grp, self.produced, self.stop_flag, self.rows = grp, produced, threading.Event(), []

    def run(self):
        while not self.stop_flag.is_set():
            self.rows.append((self.grp.count(), max(0, self.produced.value - self.grp.consumed.value)))
            time.sleep(DT)


def cpu_times():
    with open("/proc/stat") as fh:
        f = fh.readline().split()
    vals = list(map(int, f[1:]))
    idle = vals[3] + vals[4]
    return sum(vals), idle


def kafka_bin(name):
    home = os.environ.get("KAFKA_HOME", "")
    return str(Path(home) / "bin" / name) if home else name


def make_topic(topic):
    subprocess.run([kafka_bin("kafka-topics.sh"), "--bootstrap-server", BOOTSTRAP, "--create", "--if-not-exists", "--topic", topic,
                    "--partitions", str(PARTITIONS), "--replication-factor", "1"], check=True, capture_output=True, text=True)


def delete_topic(topic):
    subprocess.run([kafka_bin("kafka-topics.sh"), "--bootstrap-server", BOOTSTRAP, "--delete", "--topic", topic], capture_output=True, text=True)


# ------------------------------------------------------------------ one arm, one repetition
def run_arm(arm, wl_dir: Path, rep, service_ms, payload, steps, step_s, base, line_ms, objective=DEFAULT_OBJECTIVE):
    d = wl_dir / f"rep-{rep}" / arm; d.mkdir(parents=True, exist_ok=True)
    topic = f"omni-{wl_dir.name}-{rep}-{arm}-{int(time.time())}"; group = topic + "-g"
    make_topic(topic)
    rates = [base * int(s) for s in steps.split()]
    produced = mp.Value("l", 0); stop_prod = mp.Event()
    grp = Group(topic, group, service_ms, d)
    for _ in range(NATIVE_CONSUMERS):
        grp.start_one()
    time.sleep(8)                                              # the group forms and settles (both arms)
    sampler = Sampler(grp, produced); sampler.start()
    omni = None
    if arm == "omni":
        omni = Omni(grp, produced, d / "audit.jsonl", line_ms, objective, topic=topic); omni.start()
    cpu0 = cpu_times(); t0 = time.time()
    prod = mp.Process(target=producer_proc, args=(topic, rates, step_s, payload, produced, stop_prod, str(d / "producer.log")))
    prod.start(); prod.join()
    # drain: up to 30 s for the group to catch up, then stop
    t_drain = time.time()
    while grp.consumed.value < produced.value and time.time() - t_drain < 30:
        time.sleep(0.5)
    t1 = time.time(); cpu1 = cpu_times()
    if omni:
        omni.stop_flag.set(); omni.join(timeout=60)
    sampler.stop_flag.set(); sampler.join(timeout=5)
    changes = grp.changes
    grp.stop_all()
    # the gauges, from every consumer's record
    lats = []
    for f in sorted(d.glob("consumer-*.log")):
        for ln in f.read_text().splitlines():
            try:
                t, seq, lat = ln.split(" "); lats.append((float(t), float(lat)))
            except ValueError:
                pass
    seconds = t1 - t0
    lat_sorted = sorted(l for _, l in lats)
    n = len(lat_sorted)
    def q(p):
        return lat_sorted[min(n - 1, int(p * n))] if n else float("nan")
    inside = sum(1 for l in lat_sorted if l <= line_ms)
    cons = [c for c, _ in sampler.rows] or [NATIVE_CONSUMERS]; lags = [l for _, l in sampler.rows] or [0]
    total = (cpu1[0] - cpu0[0]); idle = (cpu1[1] - cpu0[1]); tick_hz = os.sysconf("SC_CLK_TCK")
    cpu_s = (total - idle) / tick_hz
    g = {"arm": arm, "rep": rep, "seconds": round(seconds, 1), "produced": produced.value, "consumed": n,
         "work_inside_line_mps": inside / seconds, "mps": n / seconds, "p95_ms": q(0.95), "p99_ms": q(0.99), "p50_ms": q(0.5),
         "mean_ms": (sum(lat_sorted) / n) if n else float("nan"), "lag_max": max(lags), "lag_mean": sum(lags) / len(lags),
         "lost": max(0, produced.value - n), "consumers_mean": sum(cons) / len(cons), "consumers_max": max(cons),
         "cpu_busy_share": (total - idle) / max(1, total), "cpu_seconds": cpu_s, "cpu_s_per_1k_inside": 1000.0 * cpu_s / max(1, inside),
         "rebalances": changes, "handed_back": (omni.handed_back if omni else True), "failups": (omni.failups if omni else 0),
         "verdict": (omni.verdict.record() if omni and omni.verdict else None)}
    (d / "arm.json").write_text(json.dumps(g, indent=1))
    delete_topic(topic)
    print(f"   {arm} rep {rep}: {n} of {produced.value} consumed, inside the line {inside / seconds:.1f}/s, p95 {g['p95_ms']:.0f} ms, "
          f"lag max {g['lag_max']}, consumers {g['consumers_mean']:.2f}, CPU {cpu_s:.1f} s, handed back {g['handed_back']}"
          + (f", verdict {g['verdict']['state']}" if g.get("verdict") else ""), flush=True)
    return g


def capacity(wl_dir: Path, service_ms, payload, calib_s):
    """Native's unlimited capacity: the operator's consumers fed faster than they can take for calib_s seconds."""
    d = wl_dir / "capacity"; d.mkdir(parents=True, exist_ok=True)
    topic = f"omni-{wl_dir.name}-cap-{int(time.time())}"; make_topic(topic)
    produced = mp.Value("l", 0); stop_prod = mp.Event()
    grp = Group(topic, topic + "-g", service_ms, d)
    for _ in range(NATIVE_CONSUMERS):
        grp.start_one()
    time.sleep(8)
    c0 = grp.consumed.value
    prod = mp.Process(target=producer_proc, args=(topic, [5000.0], calib_s, payload, produced, stop_prod, str(d / "producer.log")))
    prod.start(); t0 = time.time(); prod.join(); t1 = time.time()
    rate = (grp.consumed.value - c0) / (t1 - t0)
    grp.stop_all(); delete_topic(topic)
    return rate


def paired(reps, key, direction):
    """omni against native on one gauge over the repetitions: means, the mean paired difference, its 95% interval."""
    d = [r["omni"][key] - r["native"][key] for r in reps if _num(r["omni"].get(key)) and _num(r["native"].get(key))]
    if not d:
        return None
    n = len(d)
    nat = sum(r["native"][key] for r in reps) / n
    om = sum(r["omni"][key] for r in reps) / n
    mean = sum(d) / n
    if n > 1:
        sd = math.sqrt(sum((x - mean) ** 2 for x in d) / (n - 1))
        half = T95.get(n - 1, 1.96) * sd / math.sqrt(n)
    else:
        half = float("nan")
    lo, hi = mean - half, mean + half
    same = abs(mean) <= SAME_REL * max(abs(nat), 1e-12)
    clear = n > 1 and (lo > 0 or hi < 0) and not same
    if direction == "shown":
        reading = SHOWN
    elif direction == "never more" and any(x > 0 for x in d):
        reading = "**LOSS in a repetition**"
    elif same:
        reading = EVEN_SAME
    elif not clear:
        reading = EVEN_NOISE
    else:
        reading = gel_word(mean < 0, gel_aim(direction, key))      # the word by what the gauge is for, never by its sign
    return {"native": nat, "omni": om, "diff": mean, "ci95": [lo, hi], "n": n, "significant": clear, "reading": reading}


def _num(x):
    return isinstance(x, (int, float)) and not (isinstance(x, float) and math.isnan(x))


def engine():
    try:
        out = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py")], cwd=ROOT, capture_output=True, text=True, timeout=120).stdout.strip()
        sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
        return {"version": out.splitlines()[0] if out else "unknown", "commit": sha[:12]}
    except (OSError, subprocess.SubprocessError):
        return {"version": "unknown", "commit": "?"}


def run_workload(name, out: Path, reps, step_s, calib_s, line_ms, objective=DEFAULT_OBJECTIVE):
    service_ms, payload, steps, tuning = WORKLOADS[name]
    wl_dir = out / f"kafka-{name}"; wl_dir.mkdir(parents=True, exist_ok=True)
    print(f"== {name}: {service_ms} ms of work a message, {payload} B, steps {steps}, {step_s} s a notch, the verdict's objective {objective}", flush=True)
    cap = capacity(wl_dir, service_ms, payload, calib_s)
    peak = max(int(s) for s in steps.split())
    base = PEAK_SHARE * cap / peak
    print(f"   native capacity with {NATIVE_CONSUMERS} consumers: {cap:.0f} messages a second; base rate {base:.1f}/s (peak notch {peak} offers {PEAK_SHARE:.0%} of it)", flush=True)
    rec = {"workload": name, "tuning": tuning, "service_ms": service_ms, "payload_bytes": payload, "steps": steps, "step_s": step_s,
           "line_ms": line_ms, "native_consumers": NATIVE_CONSUMERS, "cover": list(COVER), "capacity_mps": cap, "base_rate_mps": base,
           "objective": objective, "dial": DIAL, "engine": engine(), "reps": []}
    for rep in range(1, reps + 1):
        order = ("native", "omni") if rep % 2 else ("omni", "native")
        r = {}
        for arm in order:
            r[arm] = run_arm(arm, wl_dir, rep, service_ms, payload, steps, step_s, base, line_ms, objective)
        rec["reps"].append(r)
        (wl_dir / f"{name}.json").write_text(json.dumps(rec, indent=1))
    rec["paired"] = {k: paired(rec["reps"], k, dr) for k, _, dr in GAUGES}
    (wl_dir / f"{name}.json").write_text(json.dumps(rec, indent=1))
    return rec


def fmt(v):
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return "n/a"
    return f"{v:,.0f}" if abs(v) >= 100 else f"{v:,.3g}"


def report(recs, out: Path):
    L = ["# Kafka: Omni-Compass on top of a consumer group's operator-set size", "",
         f"Apache Kafka as shipped (one broker, a topic of {PARTITIONS} partitions); native: the consumer group at the operator's count "
         f"({NATIVE_CONSUMERS}); omni: the compass law on the consumer count inside [{COVER[0]}, {COVER[1]}], holding the group's own "
         f"end-to-end latency at {CENTER:.0%} of the {LINE_MS:.0f} ms line. The same offered load in both arms. Energy is the host's CPU "
         "seconds, the compass's own cost included. Every row is reported, losses included.", ""]
    for rec in recs:
        L += [f"## {rec['workload']}: {rec['service_ms']} ms of work a message, {rec['payload_bytes']} B, steps {rec['steps']} × {rec['step_s']} s"
              + (" (the tuning workload)" if rec.get("tuning") else ""), "",
              f"Native capacity {rec['capacity_mps']:.0f} messages a second; base rate {rec['base_rate_mps']:.1f}/s; {len(rec['reps'])} paired repetitions; "
              f"engine {rec['engine']['version']} at `{rec['engine']['commit']}`.", "",
              "| Gauge | native | omni | change | 95% interval of the difference | reading |", "|---|---:|---:|---:|---:|---|"]
        for k, label, direction in GAUGES:
            p = rec.get("paired", {}).get(k)
            if not p:
                continue
            ch = "" if p["native"] == 0 else f"{100 * p['diff'] / abs(p['native']):+.1f}%"
            L.append(f"| {label} | {fmt(p['native'])} | {fmt(p['omni'])} | {ch} | {fmt(p['ci95'][0])} to {fmt(p['ci95'][1])} | {p['reading']} |")
        hb = all(r["omni"]["handed_back"] for r in rec["reps"])
        L += ["", f"Every omni arm handed back to the operator's count: {'yes' if hb else 'NO'}; fail-ups: "
              f"{sum(r['omni']['failups'] for r in rec['reps'])}.", ""]
    (out / "KAFKA.md").write_text("\n".join(_legal_stamp(L)) + "\n")
    return out / "KAFKA.md"


def setup():
    """The workflow's broker: Kafka as shipped from KAFKA_HOME, one KRaft node, the log directory the only change."""
    home = Path(os.environ["KAFKA_HOME"]); props = Path("/tmp/omni-kafka-server.properties"); logs = Path("/tmp/omni-kraft-logs")
    txt = (home / "config" / "kraft" / "server.properties").read_text().replace("log.dirs=/tmp/kraft-combined-logs", f"log.dirs={logs}")
    props.write_text(txt)
    uuid = subprocess.run([str(home / "bin" / "kafka-storage.sh"), "random-uuid"], capture_output=True, text=True, check=True).stdout.strip().splitlines()[-1]
    subprocess.run([str(home / "bin" / "kafka-storage.sh"), "format", "-t", uuid, "-c", str(props)], check=True, capture_output=True, text=True)
    subprocess.Popen([str(home / "bin" / "kafka-server-start.sh"), str(props)], stdout=open("/tmp/omni-kafka-server.log", "w"), stderr=subprocess.STDOUT)
    for _ in range(60):
        if "Kafka Server started" in Path("/tmp/omni-kafka-server.log").read_text():
            print("broker up"); return 0
        time.sleep(2)
    print("broker did not start", file=sys.stderr); return 1


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--setup", action="store_true")
    ap.add_argument("--workloads", default="tuning")
    ap.add_argument("--reps", type=int, default=3)
    ap.add_argument("--step-s", type=float, default=20.0)
    ap.add_argument("--calib-s", type=float, default=20.0)
    ap.add_argument("--line-ms", type=float, default=LINE_MS)
    ap.add_argument("--out", default="kafka-out")
    ap.add_argument("--objective", default=DEFAULT_OBJECTIVE, choices=OBJECTIVES,
                    help="what the brain's verdict judges a step by: resource (the index's reading: work, speed, consumers and CPU together) or service (work and speed alone)")
    ap.add_argument("--report-only", default="")
    a = ap.parse_args(argv)
    if a.setup:
        return setup()
    out = Path(a.out)
    if a.report_only:
        recs = [json.loads(f.read_text()) for f in sorted(Path(a.report_only).rglob("kafka-*/*.json"))]
        print(report(recs, Path(a.report_only))); return 0
    names = list(WORKLOADS) if a.workloads == "all" else a.workloads.split(",")
    recs = [run_workload(n, out, a.reps, a.step_s, a.calib_s, a.line_ms, a.objective) for n in names]
    print(report(recs, out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
