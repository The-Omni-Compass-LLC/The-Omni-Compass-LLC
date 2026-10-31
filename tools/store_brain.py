#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The max on a store's memory knob (omni-v22; docs/STORE_ROOT_CAUSES_2026-10-30.md): what the three cache wires share.

The store wires were written on 9 and 10 October 2026 with the brain's verdict judging every move under the resource objective,
before the founder's order of 12 October that the max is the default brain, and were never brought to it. Under the max a knob
runs at its own limit inside the operator's cover, never past it and never below native; the memory it takes is power given,
shown beside the misses it bought off; the tune-down (`dial save`) keeps omni-v21's loop, where giving memory back is the aim.
Where the memory can bring the knob no GAIN, the knob stays native (the engine's strictest form, the founder's words of 19
October): on a store that is not slow for want of memory, memory is not spent.

Four pieces, each read from the store's and the host's own meters, nothing written for a workload:

  the working set's floor   the most memory the store held in the last HOLD_WINDOW_S, with the fullness margin, rounded up to a
                            notch, never under native nor over the cover: a knob handed back below it evicts what the service
                            still asks for, and the next rise buys it back at the store's price (the sawtooth the Redis model
                            showed on a candidate without it)
  the cost of the misses    the store's own account: the share of the service's own time that its misses are, over
                            WORTH_WINDOW_S. MySQL: the performance schema's timer on the data files' reads against the
                            workload's statement timer; MongoDB: WiredTiger's time reading pages from disk for the application's
                            threads against the server's own read latency; Redis: the application's own split of each request
                            into hits and misses. A slope of latency on miss share was tried first and is not used: on the
                            archived runs it read 0.5 to 1.2 ms a unit of miss share inside the arms, while the controlled
                            comparison across pool sizes (a third of the misses gone, the latency unmoved) read none; the
                            seconds' noise is shared by both, and the slope reads it as a price
  the gate                  memory is spent only where that share is MISS_WORTH or more, the one key's own floor (a change of
                            0.5% or more is a change, the founder's order of 24 October): under it the misses are nothing the
                            key could read, so memory could buy nothing it could read, and the knob holds and says so; where the
                            store's account is not read this second, nothing is known and nothing is taken. The floor is not a
                            tuning: it is the smallest change the record reads at all
  the host's room           a notch is taken only while the host keeps HOST_CUSHION of its memory available after it (the
                            compass's cushion; the host is a muscle too, and never past its own limit); unread, nothing is taken
"""
from __future__ import annotations

import math
from collections import deque

HOLD_WINDOW_S = 60.0
WORTH_WINDOW_S = 10.0
MISS_WORTH = 0.005              # the one key's floor, tools/readings.py SIZE_FLOOR (a change under 0.5% reads EVEN, under the floor); written
                                # here as a number because this file is in the engine's fingerprint and readings.py is not
HOST_CUSHION = 0.05
MEMINFO = "/proc/meminfo"
KINDS = ("spend", "held_unread", "held_worth", "held_host", "handed_back", "handed_to_floor", "held_floor", "failups")


class WorkingSetFloor:
    def __init__(self, native, notch, cover, full=0.9, window_s=HOLD_WINDOW_S):
        self.native, self.notch, self.cover, self.full, self.window_s = native, notch, cover, full, window_s
        self.used = deque()

    def observe(self, t, used):
        if used is None:
            return
        self.used.append((t, float(used)))
        while self.used and t - self.used[0][0] > self.window_s:
            self.used.popleft()

    def value(self, t=None):
        peak = max((u for _, u in self.used), default=0.0) / self.full
        return min(self.cover[1], max(self.native, int(math.ceil(peak / self.notch)) * self.notch))


class MissCost:
    """The share of the service's own time that its misses are, from the store's own meter, over a window of seconds."""

    def __init__(self, window_s=WORTH_WINDOW_S):
        self.window_s = window_s
        self.rows = deque()

    def observe(self, t, miss_time_s, service_time_s):
        """One second: the time the store spent on its misses and the time the service spent on its requests, both in seconds.
        A second with no service time, or without the store's account, tells nothing and is not kept."""
        if miss_time_s is None or service_time_s is None or service_time_s <= 0:
            return False
        self.rows.append((t, max(0.0, float(miss_time_s)), float(service_time_s)))
        while self.rows and t - self.rows[0][0] > self.window_s:
            self.rows.popleft()
        return True

    def worth(self):
        """Σ miss time / Σ service time over the window, between 0 and 1; None until a second has been read."""
        service = sum(s for _, _, s in self.rows)
        if not self.rows or service <= 0:
            return None
        return max(0.0, min(1.0, sum(m for _, m, _ in self.rows) / service))


def read_meminfo(path=MEMINFO):
    """(available MB, total MB) from the host's own account, or (None, None) where it cannot be read."""
    try:
        avail = total = None
        with open(path) as fh:
            for line in fh:
                if line.startswith("MemAvailable:"):
                    avail = int(line.split()[1]) / 1024.0
                elif line.startswith("MemTotal:"):
                    total = int(line.split()[1]) / 1024.0
        return avail, total
    except (OSError, ValueError, IndexError):
        return None, None


def host_room(available_mb, total_mb, notch_mb, cushion=HOST_CUSHION):
    """Whether the host can give a notch and keep its cushion; None where the host's memory is unread (nothing known)."""
    if available_mb is None or total_mb is None or total_mb <= 0:
        return None
    return available_mb - notch_mb >= cushion * total_mb


def max_target(want, cur, native, floor, worth, room, why, worth_floor=MISS_WORTH):
    """The max's target from the wire's own rule (want): a spend goes through unclamped where the store's own account says the
    misses cost the service and the host has the notch to spare; it holds where the misses cost nothing, where the account is not
    read, or where the host has no room; a give-back never goes below the working set's floor nor below native.
    Returns (target, why, kind), kind one of KINDS or "hold"."""
    if want > cur:
        if worth is None:
            return cur, "the store's account of a miss's cost not read this second: nothing known, nothing taken", "held_unread"
        if worth < worth_floor:
            return cur, (f"misses are {100 * worth:.0f}% of the service's own time, under {100 * worth_floor:.0f}%: memory would buy "
                         "nothing; held"), "held_worth"
        if room is None:
            return cur, "the host's memory unread: nothing known, nothing taken", "held_host"
        if not room:
            return cur, f"the host has no notch to spare over its {100 * HOST_CUSHION:.0f}% cushion: held", "held_host"
        return want, why + f"; misses {100 * worth:.0f}% of the service's time: power given inside the cover", "spend"
    if want < cur:
        if want >= floor:
            return want, why + f"; the working set's last {HOLD_WINDOW_S:.0f} s fit under {floor}", "handed_back"
        if cur > floor:
            return max(want, floor), f"calm: handed back to the working set's floor, {floor}", "handed_to_floor"
        return cur, f"hold: {cur} is what the working set's last {HOLD_WINDOW_S:.0f} s occupied", "held_floor"
    return cur, why, "hold"


class MemoryMax:
    """The max on one store's memory knob: the four pieces above around the wire's own rule. Each wire's Brain keeps its own
    compass law and its own `decide`; this governs what that rule wants."""

    def __init__(self, native, notch, cover, full, meter):
        self.native, self.notch, self.cover, self.meter = native, notch, cover, meter
        self.floor = WorkingSetFloor(native, notch, cover, full=full)
        self.cost = MissCost()
        self.counts = {k: 0 for k in KINDS}
        self.counts["hold"] = 0

    def step(self, t, want, why, cur, used_mb, miss_time_s, service_time_s, host_avail_mb, host_total_mb, fail_up=False):
        self.floor.observe(t, used_mb)
        self.cost.observe(t, miss_time_s, service_time_s)
        worth = self.cost.worth()
        room = host_room(host_avail_mb, host_total_mb, self.notch)
        floor = self.floor.value(t)
        target, why, kind = max_target(want, cur, self.native, floor, worth, room, why)
        self.counts[kind] += 1
        if kind == "spend" and fail_up:
            self.counts["failups"] += 1
        info = {"verdict_phase": None, "verdict_direction": None, "allowed_low": None, "allowed_high": None, "dial": "max",
                "floor_mb": floor, "miss_worth": None if worth is None else round(worth, 3),
                "miss_time_ms": None if miss_time_s is None else round(1000.0 * miss_time_s, 3),
                "host_avail_mb": None if host_avail_mb is None else round(host_avail_mb),
                "host_room": room}
        return target, why, info

    @property
    def failups(self):
        return self.counts["failups"]

    def record(self, objective):
        """What the arm's record carries where omni-v21's loop carried the verdict's allowance."""
        return {"dial": "max", "objective": objective, "native": self.native, "notch": self.notch, "cover": list(self.cover),
                "state": f"the max: spends by {self.meter}, never below native; no allowance",
                "allowed_low": None, "allowed_high": None, "counts": dict(self.counts)}


def summarize_max(records):
    """One line for a table from the omni arms' records of one workload under the max."""
    parts = []
    for r in records:
        c = r.get("counts", {})
        parts.append(f"the max ({c.get('spend', 0)} spends, {c.get('held_worth', 0)} held: misses cheap, {c.get('held_unread', 0)} held: "
                     f"account unread, {c.get('held_host', 0)} held: the host, {c.get('handed_back', 0) + c.get('handed_to_floor', 0)} handed back)")
    return "; ".join(parts)
