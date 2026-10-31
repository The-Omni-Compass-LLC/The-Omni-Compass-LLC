#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The modelled machine's service for the CPU power harness (tools/run_cpu_power.py --plant sim), as the model's own queue.

The harness's modelled service was a sleep of the service time in worker processes, its latency measured by the wall clock,
so the machine's own load entered the model's physics: on a loaded runner late wake-ups read as slow requests, the verdict's
costs turned noisy and no notch was ever allowed, while a quiet runner passed (30 October 2026, tests/test_run_cpu_power.py).
Here the service is a queue of one server per worker advanced in modelled time: arrivals are the schedule's own times (each
step's count and the seeded spread, the same in both arms), a request is served when the model's clock reaches it, at the
service time the ceiling of that moment gives, and its latency is the model's, never a sleep. The real machine's path
(work_unit on real cores) is untouched. tools/run_cpu_power.py is inside the engine's fingerprint (omni-v15, every wire that
holds a governor's rules), so this model lives beside it and is driven through the seam the harness's test already uses
(ModelService in place of Service); it goes into the wire itself with the next engine version."""
from __future__ import annotations

import collections
import heapq
import random
import threading
import time

from tools import run_cpu_power as R

CURRENT = {"service": None, "clock": None}      # the modelled machine's parts the test installs: its service, its clock


def model_cpu_times():
    """The modelled machine's /proc/stat (in place of tools/run_cpu_power.py cpu_times): its workers' busy time is the service
    time they have served (ModelService.work_s), the rest idle, over the model's own clock. The harness's host busy share, read
    from the real /proc/stat, was the last way the machine under the test entered the model: the governor's cost sample under
    the resource objective carries it, so on a loaded runner the verdict judged the runner's load, not the model's."""
    clock, svc = CURRENT["clock"], CURRENT["service"]
    t = clock.monotonic() if clock else time.monotonic()
    n = svc.n_workers if svc else 4
    total = int(100 * n * t)
    busy = int(100 * (svc.work_s if svc else 0.0))
    return total, max(0, total - busy)


class ModelClock:
    """The modelled machine's clock (30 October 2026): every thread of the harness that keeps time (the service, the governor,
    the sampler, and the thread that runs the arms) sleeps and joins on this clock instead of the wall's, and the clock moves
    only when every one of them is waiting, to the earliest wake, one thread at a time. A decision then comes every DT of
    modelled time whatever the machine under the test is doing, and the run's reading is the same on a quiet runner and a
    loaded one: the test of 30 October passed alone and failed inside the whole suite because the governor's wall-clock
    decisions came late under load and its trial never reached its samples. The thread that runs the arms (the driver) is a
    keeper too: while it works the clock holds, and its join on a harness thread counts as waiting only while that thread
    sleeps on the clock, so the arm's end is read at the modelled time the service ended at, never a sampler's tick later
    (under load the native arm's energy read 778 to 793 J for one run before this rule). A thread that has ended keeps no
    place in the clock. Installed by the test in place of the `time` module of the harness and of this model, with the
    harness's threads on the clock (ModelService, ModelOmni, ModelSampler) in place of its own."""

    def __init__(self, start=1000.0):
        self.t, self.cv, self.waiting, self.joining, self.known = float(start), threading.Condition(), {}, {}, set()
        self.names = {}                                                # thread ident -> its name: threads created in a fixed order wake in it
        self.driver = threading.get_ident()                            # the thread that runs the arms: a keeper from the start

    def monotonic(self):
        return self.t

    perf_counter = monotonic

    def time(self):
        return 1.7e9 + self.t

    def _keepers(self):
        # the keepers of time: the harness's own threads (the service, the sampler, the governor) from the moment they are alive,
        # so a thread just started cannot be overtaken by the clock before its first sleep; any daemon thread that has slept on
        # the clock, while it lives; and the driver. A thread that has ended keeps no place
        live = list(threading.enumerate())
        alive = {t_.ident for t_ in live}
        return ({t_.ident for t_ in live if isinstance(t_, (R.Service, R.Sampler, R.Omni))}
                | {k for k in self.known if k in alive} | {self.driver})

    def _waits(self, k):
        """Thread k is waiting on the clock: asleep on it, or joining a thread that is itself asleep on it."""
        if k not in self.waiting:
            return False
        j = self.joining.get(k)
        return j is None or j.ident in self.waiting

    def _turn(self, me, done=None):
        """Under the lock: wait until the clock reaches my wake and it is my turn (one thread at a time, the earliest wake first,
        ties in the order the threads were made), or until done() says I may leave (the thread I join has ended)."""
        while True:
            if done is not None and done():
                return
            keepers = self._keepers() | {me}
            if all(self._waits(k) for k in keepers):                  # everyone who keeps time is waiting: the earliest wakes
                due = min((self.waiting[k], self.names[k], k) for k in keepers)
                self.t = max(self.t, due[0])
                if due[2] == me:
                    return
                self.cv.notify_all()
            self.cv.wait(0.0005)                                       # give the lock up: a woken thread leaves, a working one reaches its sleep

    def sleep(self, s):
        me, th = threading.get_ident(), threading.current_thread()
        with self.cv:
            if th.daemon:
                self.known.add(me)
            self.names[me] = th.name
            self.waiting[me] = self.t + max(1e-6, float(s))        # never shorter than a microsecond: a sleep that moved the clock by
            self.cv.notify_all()                                       # less than its own resolution would spin forever
            self._turn(me)
            del self.waiting[me]
            self.cv.notify_all()

    def join(self, thread, timeout=None):
        """A join on the clock: the caller waits while `thread` sleeps on the clock, the clock holds while it runs and while it
        ends, and the caller goes on the moment it has ended, at the modelled time it ended at. A timeout is modelled seconds."""
        me, th = threading.get_ident(), threading.current_thread()
        with self.cv:
            self.names[me] = th.name
            self.waiting[me] = self.t + float(timeout) if timeout is not None else float("inf")
            self.joining[me] = thread
            self.cv.notify_all()
            self._turn(me, lambda: not thread.is_alive())
            del self.waiting[me]; del self.joining[me]
            self.cv.notify_all()


class _OnTheClock:
    """A harness thread whose join goes through the model's clock while one is installed (the driver's wait is then modelled
    time, and the clock holds while the thread ends); the plain join otherwise."""

    def join(self, timeout=None):
        clock = CURRENT["clock"]
        if clock is None:
            return super().join(timeout)
        clock.join(self, timeout)


class ModelOmni(_OnTheClock, R.Omni):
    """The governor's thread, joined on the model's clock."""


class ModelSampler(_OnTheClock, R.Sampler):
    """The sampler's thread, joined on the model's clock."""


class ModelService(_OnTheClock, R.Service):
    """R.Service with the modelled machine's service as the model's own queue (sim_root set); the real plant as before."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sim = None
        if self.sim_root:
            self.sim = R.SimPlant.__new__(R.SimPlant); R.Plant.__init__(self.sim, self.sim_root)
            self.free = [0.0] * self.n_workers                                 # each modelled server: free from this modelled time (s)
            self.wrng = [random.Random((self.seed or 0) * 7919 + i) for i in range(self.n_workers)]   # each server's spread, seeded as the workers were
            self.arrived, self.pending = collections.deque(), []               # arrived and not yet served; served and not yet done
            self._factor = 1.0
            self.work_s = 0.0                                                  # the service time served so far: the modelled machine's busy time
            CURRENT["service"] = self

    def _advance(self, now_rel):
        """The model up to modelled time now_rel (s since t0): every arrived request whose service can start is served by the
        first free server at this moment's service time; every served request whose service has ended is recorded. Under the lock."""
        if self.sim is None:
            return
        try:
            self._factor = self.sim.service_factor()
        except (OSError, ValueError):                                          # the modelled file mid-replacement: the last factor stands
            pass
        while self.arrived:
            a = self.arrived[0]
            i = min(range(self.n_workers), key=self.free.__getitem__)
            start = max(a, self.free[i])
            if start > now_rel:
                break                                                          # it waits: its service has not begun, so its time is not yet known
            self.arrived.popleft()
            svc = self.service_ms / 1000.0 * self._factor * self.wrng[i].uniform(0.95, 1.05)
            self.free[i] = start + svc
            self.work_s += svc
            heapq.heappush(self.pending, (start + svc, a))
        while self.pending and self.pending[0][0] <= now_rel:
            done, a = heapq.heappop(self.pending)
            self.records.append((a, done - a)); self.done += 1; self.last_done_t = self.t0 + done

    def run(self):
        if self.sim is None:
            return super().run()
        self.t0 = time.monotonic()
        step_start = 0.0
        for step in self.steps:
            rate = step * self.unit; period = 1.0 / rate
            n_step = int(round(rate * self.step_s))                            # the step's requests, the same count in both arms
            next_rel = step_start
            for _ in range(n_step):
                while True:
                    now_rel = time.monotonic() - self.t0
                    if now_rel >= next_rel:
                        break
                    with self.lock:
                        self._advance(now_rel)
                    time.sleep(min(0.002, next_rel - now_rel))
                with self.lock:
                    self.arrived.append(next_rel); self.issued += 1
                    self._advance(now_rel)
                next_rel += period * self.rng.uniform(*self.JITTER)            # a Poisson-like spread around the rate, the same seed in both arms
            step_start += self.step_s
        deadline = time.monotonic() + 5.0                                     # the queue drains for at most five seconds
        while self.done < self.issued and time.monotonic() < deadline:
            with self.lock:
                self._advance(time.monotonic() - self.t0)
            time.sleep(0.05)
        self.stop_flag.set()

    def last_second(self, line_ms, since_s=1.0):
        if self.sim is None:
            return super().last_second(line_ms, since_s)
        if self.t0 is None:
            return 0, 0, None
        now_rel = time.monotonic() - self.t0
        with self.lock:
            self._advance(now_rel)
            lat = [l for t, l in self.records[-5000:] if t + l >= now_rel - since_s]
        if not lat:
            return 0, 0, None
        return len(lat), sum(1 for l in lat if l * 1000.0 <= line_ms), sum(lat) / len(lat)
