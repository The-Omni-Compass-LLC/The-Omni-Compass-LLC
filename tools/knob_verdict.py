# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The brain's own verdict on one live knob, in real time (the founder's order of 9 October 2026).

Every knob starts in watch: one wire out, nothing written. It is written only between native and the deepest step a paired
trial on the stack itself has allowed under the declared objective, and a step that fails its trial is not taken. The
trial, the judgement, the allowance and the recheck are the frozen engine's (omnicompass/verdict.py, Omni v3, byte for
byte); this module gives that Verdict the knob's notch, the cost it judges and the condition under which a trial of this
knob is fair. Nothing in the engine changes.

  two directions   spend (more of the resource: a bigger ceiling, more consumers, more connections) and give back (less:
                   fewer connections, a smaller pool or cache), each its own Verdict with its own steps outward from native.
                   Restoring native is never a step: the knob may always be moved back toward the operator's setting.
  the condition    a give-back step is tried while the service is calm and the stack's own give-back condition holds (the
                   engine's rule: a trial is never run under stress); a spend step is tried while the compass asks to spend
                   and the stack's own spend condition holds (a cache full and missing, messages waiting, clients queued),
                   because that is the only time a spend can show what it buys. A give-back trial once started runs on
                   until its samples are in unless the service leaves calm, when it is abandoned (the engine's rule). A
                   spend trial runs to its samples whatever the compass's force: the spend's own effect calms the service
                   within seconds, and a trial ended on that calm could never be judged (the first counted set of 10
                   October 2026 abandoned every Kafka spend trial that way; amendment 3 in the five preregistrations). Only
                   the wall (a fail-up) or the engine's own time limit ends a spend trial early.
  the cost         one sample a second from the stack's own readings. Under the resource objective, the preregistered
                   reading of the Omni index, cost = resource held x host CPU busy share x latency / work: a step passes only
                   if the service gained outweighs the resource and CPU spent, by the index's own arithmetic (a geometric mean
                   of the four ratios no lower than one is the same statement). Under the service objective cost = latency /
                   work: the resources are shown and not judged. The aim is the lower cost; "no higher within the tolerance" passes,
                   which is the engine's judge, so a step that buys nothing and costs nothing is allowed and a step that costs
                   more than it buys is refused.
  the hold         during a trial the knob stands at the phase's value whatever the compass asks: the reference at the
                   deepest step already allowed (native at first), then the trial step one notch further. Between trials the
                   compass moves the knob by its own law, clamped to the allowance. A fail-up never spends beyond the
                   allowance; toward native it is always free.
  the record       every trial, allowance, refusal and abandonment is kept for the audit, with the counts and the state:
                   "left native" (no step allowed in either direction) or "acting" with the allowance.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from omnicompass.verdict import Verdict  # noqa: E402  (the frozen engine's verdict, unchanged)

RESOURCE, SERVICE, PER_WORK = "resource", "service", "per-work"
OBJECTIVES = (RESOURCE, SERVICE, PER_WORK)
SPEND, GIVE = "spend", "give back"


def sample_cost(objective, work, latency, resource, cpu_share):
    """One second's cost under the objective (its aim: lower); None when nothing worked (nothing was measured).

    resource   the index's reading: resource x host CPU busy share x latency / work (declared 9 October)
    service    latency / work: the resources shown, not judged (declared 9 October)
    per-work   resource / work: the resource spent per unit of work inside the line, the speed left to the compass's own line
               as the guardrail (the card's reading, work per energy; added 10 October for the machine's own power, where the
               resource is the energy the processor's meter reads)"""
    if work is None or latency is None or work <= 0 or latency < 0:
        return None
    if objective == SERVICE:
        return latency / work
    if objective == PER_WORK:
        return max(float(resource), 1e-9) / work
    cpu = 1.0 if cpu_share is None else max(float(cpu_share), 1e-3)
    return max(float(resource), 1e-9) * cpu * latency / work


class KnobVerdict:
    def __init__(self, native, notch, cover, objective=RESOURCE, tolerance=0.02, min_samples=8, probe_every=20, recheck=60,
                 max_trial=40, settle_s=2.0):
        if objective not in OBJECTIVES:
            raise ValueError(f"objective must be one of {OBJECTIVES}, not {objective!r}")
        lo, hi = cover
        self.native, self.notch, self.lo, self.hi = native, notch, lo, hi
        self.objective = objective
        self.settle_s = settle_s
        self.verdicts = {
            SPEND: Verdict(tolerance, min_samples, probe_every, recheck, max_steps=max(0, int((hi - native) // notch)),
                           max_trial=max_trial, incremental=True),
            GIVE: Verdict(tolerance, min_samples, probe_every, recheck, max_steps=max(0, int((native - lo) // notch)),
                          max_trial=max_trial, incremental=True),
        }
        self.phase_dir = None                     # the direction whose trial phase holds the knob, or None
        self.events = []
        self.counts = {"trials": 0, "allowed": 0, "refused": 0, "abandoned": 0, "clamped": 0, "held": 0, "samples": 0}
        self.last_value, self.changed_at, self.t = native, None, 0.0

    # ---------------------------------------------------------------------------------------------- the steps
    def value_of(self, direction, step):
        v = self.native + step * self.notch if direction == SPEND else self.native - step * self.notch
        return max(self.lo, min(self.hi, v))

    @property
    def allowed_low(self):
        return self.value_of(GIVE, self.verdicts[GIVE].allowed)

    @property
    def allowed_high(self):
        return self.value_of(SPEND, self.verdicts[SPEND].allowed)

    @property
    def state(self):
        if self.verdicts[SPEND].allowed == 0 and self.verdicts[GIVE].allowed == 0:
            return "left native"
        return f"acting: {self.allowed_low} to {self.allowed_high}"

    # ---------------------------------------------------------------------------------------------- the samples
    def observe(self, cost, t, settled=True):
        """This second's cost sample, measured under the value the knob stood at. Fed to the direction in a trial phase,
        once the knob has settled after its last change; nothing else is kept."""
        if cost is None or not settled or self.phase_dir is None:
            return False
        if self.changed_at is not None and t - self.changed_at < self.settle_s:
            return False
        self.verdicts[self.phase_dir].observe([cost])
        self.counts["samples"] += 1
        return True

    # ---------------------------------------------------------------------------------------------- the decision
    def decide(self, wanted, spend_ok, give_ok, t, why="", stress=None, calm=None, fail_up=False):
        """The compass's wanted value becomes the knob's target: the phase's value while a trial holds the knob, the wanted
        value clamped to the allowance otherwise. spend_ok / give_ok: the stack's own conditions for a step in each direction
        this second (the compass asking to spend with the stack full and missing; calm with the stack holding its demand).
        stress / calm: the service past the cushion toward the line / inside the calm cushion (the compass's force): a
        give-back trial is abandoned when the service leaves calm (the engine's rule); a spend trial runs to its samples
        whatever the force (amendment 3, 10 October 2026). fail_up: the service at the wall: every trial is abandoned and
        the knob goes where the fail-up says, native always free, never beyond the allowance.
        Returns (target, why, info)."""
        self.t = t
        order = [SPEND, GIVE] if self.phase_dir != GIVE else [GIVE, SPEND]
        ok = {SPEND: bool(spend_ok), GIVE: bool(give_ok)}
        stress = bool(spend_ok) if stress is None else bool(stress)
        calm = bool(give_ok) if calm is None else bool(calm)
        holding = self.phase_dir
        results = {}
        for name in order:
            v = self.verdicts[name]
            if fail_up:
                go_on = False
            elif v.phase is not None:
                # a give-back trial is abandoned when the service leaves calm (the engine's rule: never a trial under stress);
                # a spend trial runs to its samples whatever the compass's force, because the spend's own effect calms the
                # service within seconds and ending the trial on that calm would mean no spend could ever be judged (seen on
                # every Kafka trial of the first counted set, 10 October 2026: amendment 3); only the wall ends it early
                go_on = (not stress) if name == GIVE else True
            else:
                go_on = ok[name] and holding in (None, name)             # a new trial only in a free second, in the direction asked for
            step, is_trial, ev = v.tick(go_on)
            if ev:
                self.events.append({"t": round(t, 1), "direction": name, **ev})
                self._count(ev)
            results[name] = (step, is_trial)
            if v.phase is not None:
                holding = name
            elif holding == name:
                holding = None
        self.phase_dir = holding
        info = {"verdict_phase": None, "verdict_direction": self.phase_dir, "allowed_low": self.allowed_low, "allowed_high": self.allowed_high}
        if self.phase_dir is not None:
            v = self.verdicts[self.phase_dir]
            step, _ = results[self.phase_dir]
            target = self.value_of(self.phase_dir, step)
            info["verdict_phase"] = v.phase
            if target != wanted:
                self.counts["held"] += 1
            why = f"{why}; held by the verdict: {self.phase_dir} {'reference' if v.phase == 'ref' else 'trial'} at {target}"
        else:
            target = min(max(wanted, self.allowed_low), self.allowed_high)
            if target != wanted:
                self.counts["clamped"] += 1
                why = f"{why}; the verdict allows {self.allowed_low} to {self.allowed_high}: held at {target}"
        if target != self.last_value:
            self.changed_at, self.last_value = t, target
        return target, why, info

    def _count(self, ev):
        s = ev.get("verdict", "")
        if s == "trial":
            self.counts["trials"] += 1
        elif s == "step allowed":
            self.counts["allowed"] += 1
        elif s.startswith("step refused"):
            self.counts["refused"] += 1
        elif s.startswith("trial abandoned"):
            self.counts["abandoned"] += 1

    # ---------------------------------------------------------------------------------------------- the record
    def record(self, keep_events=400):
        return {"objective": self.objective, "state": self.state, "native": self.native, "notch": self.notch,
                "spend_allowed_steps": self.verdicts[SPEND].allowed, "give_back_allowed_steps": self.verdicts[GIVE].allowed,
                "allowed_low": self.allowed_low, "allowed_high": self.allowed_high, "counts": dict(self.counts),
                "events": self.events[:keep_events], "events_total": len(self.events)}


def summarize(records):
    """One line for a table from the omni arms' records of one workload: under the tune-down the verdict's state and allowance in
    each arm; under the max (omni-v22, records with dial "max") the max's own counts (tools/store_brain.py)."""
    if not records:
        return "no verdict record"
    parts = []
    for r in records:
        if r.get("dial") == "max":
            from tools.store_brain import summarize_max
            parts.append(summarize_max([r]))
            continue
        c = r.get("counts", {})
        parts.append(f"{r.get('state', '?')} ({c.get('trials', 0)} trials, {c.get('allowed', 0)} allowed, {c.get('refused', 0)} refused)")
    return "; ".join(parts)
