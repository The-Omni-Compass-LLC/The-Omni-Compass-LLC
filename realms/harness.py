# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Realm harness: every muscle native, watched and governed; every realm, and the whole tower, as one organism.

Arms, all on the same seed (the same demand, weather, disturbances):
  native  the plant and its native controller alone
  watch   the frozen governor reads the plant every period and writes nothing; must equal native exactly
  omni    the frozen governor holds the muscle's one knob; at 90% of the run it is killed, the knob returns to the
          native controller, and the harness checks that it did

The governor is omnicompass.adapter.Governor, unchanged (the engine with u = 0, the stack law, the reset).

Single muscle: one plant, one governor reading that plant.
Organism: all the plants of a realm (or the whole tower) on one 15 s clock, coupled: the electrical power of compute, motion
and process plants is heat in the realm's thermal zones; the organism's load swing is load on its storage sites; the
zones' temperature is the ambient every other plant reports. One governor reads the organism's aggregate and its one
directive sets every muscle's knob.

Primary outcome per seed: work per energy, omni against native: (work_omni / work_native) / (energy_omni /
energy_native) - 1. For an organism, work is the mean over its plants of work_omni / work_native (their work units
differ) and energy is total joules. Guardrails: work not lower by more than 1%; the share of periods in violation not
higher by more than 1 percentage point. Labels by rule (label()).
"""
from __future__ import annotations

import csv
import math
from pathlib import Path
from typing import Dict, List

from omnicompass.adapter import Governor, OBSERVE
from omnicompass.nervous_system import from_governor
from .plants import TEMPLATES, ThermalZone, EnergyStorage, pack
from .compass_arm import compass_apply
from .compass_arm_v5 import apply_v5, apply_v5_save, max_apply, max_body_step, Bone, V5CFG, CARDS   # the v5 law: the max
                                                     # (arm v5, the default) and the tune-down (arm v5save)
from .presets import STEPS_SINGLE, ORGANISM_STEPS, CAL_SEED, params_for

ROOT = Path(__file__).resolve().parents[1]
LAWS = {"compass": compass_apply, "v5": lambda p, k: max_apply(p, k, V5CFG), "v5save": apply_v5_save}
ARMS = ("native", "watch", "compass")   # native; Omni watching (writes nothing); the compass law on top (amendment, 2026-10-05)
SOLO = "solo"     # Omni-Compass by itself (omni-v19, docs/SOLO_PREREGISTRATION.md): the max, with every pool whose own count is
                  # the muscle's knob run with its autoscaler switched off (and its twin, the brain's sense of native, too)


def native_off_pool(template: str, knob: str) -> bool:
    """Whether by itself switches off this muscle's own native controller: a pool whose knob is its count (capacity, or the
    autoscaler's target), where native is the autoscaler. A power cap, an admission limit and every other plant's knob are
    a setting native already holds still, or run through native's own loop as their actuator: by itself is the same arm."""
    return template == "compute_pool" and knob not in ("power", "admission")
# for a setpoint muscle, a fourth arm: the native controller with the setpoint simply fixed at the band's calm end.
# It shows how much of any Omni result on that muscle the band alone would give, with no governor.
FIXED = "fixed_calm"
KILL_AT = 0.8
WALK = 24         # decisions over which the lease walks every setting back to native after the brain goes silent (the
                  # plug's own reflex: a room warmed or a loop eased is brought back slowly enough that the body repays it
                  # without a jump its lines must absorb at once); the security kill switch stays instant. The run keeps
                  # going native after the walk, so every setting is proven back at the operator's before it ends
CLIMB = (1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 4, 3, 2, 1, 2, 1)
# the climb: the load steps by one, up and down (1 2 3 2 3 4 ...), level 4 is the organism's own normal load and level
# 8 twice it; every muscle's work demand follows it (requests, the rooms' IT heat, the axes' tasks, the loops' demand),
# so the organism is pushed past what native can carry and the most each arm can do shows. A site's own base load stays
# its own: the climb reaches it through the body's power swing on its line


LINE = 0.25       # the line: work already waiting when the run starts, a quarter of the work the run itself brings (the
                  # founder's order of 12 October: work waiting in line, so the most each arm can clear shows). A pool's
                  # line is jobs submitted before the start (its machines take them from what the requests leave them),
                  # an axis's is tasks queued, a site's is flexible load held over; a room's heat and a loop's demand
                  # cannot wait, so they have none. Both arms of a seed start with the same line. Fixed before any
                  # preregistered run (docs/OMNI_V5.md, the max)


def climb_level(k: int, steps: int) -> float:
    """The climb's load multiplier at decision k of steps (level / 4)."""
    return CLIMB[min(len(CLIMB) - 1, k * len(CLIMB) // steps)] / 4.0


def put_line(p):
    """Put the line on one plant (in place): a quarter of its own run's work, waiting when the run starts."""
    P = p.P
    if p.template == "compute_pool":
        p.B = p.line0 = LINE * sum(p.lam) * P["dt"]
    elif p.template == "motion_axis":
        n = int(round(LINE * sum(p.arrivals)))
        p.backlog += n
        p.waits = [0.0] * n + p.waits
        p.line_n = n
    elif p.template == "energy_storage":
        p.line_e = LINE * P["flex"] * sum(p.load) * P["dt"]
        p.deferred_j += p.line_e
    return p


def scale_load_plant(p, profile="climb"):
    """Put a load on one plant's work demand (in place): the climb, the line, or a constant multiple."""
    if profile == "line":
        return put_line(p)
    steps = p.steps
    m = [climb_level(k, steps) for k in range(steps)] if profile == "climb" else [float(profile)] * steps
    if p.template == "compute_pool":
        p.lam = [x * m[k] for k, x in enumerate(p.lam)]
    elif p.template == "thermal_zone":
        p.qit = [x * m[k] for k, x in enumerate(p.qit)]
    elif p.template == "motion_axis":
        p.arrivals = [int(round(x * m[k])) for k, x in enumerate(p.arrivals)]
    elif p.template == "process_loop":
        p.d = [x * m[k] for k, x in enumerate(p.d)]
    return p


def scale_load(body, profile="climb"):
    """Put a load on a body's work demand (in place; every arm of a seed gets the same load)."""
    body.load = profile
    for p in body.plants:
        scale_load_plant(p, profile)
    return body
from omnicompass.student_t import T95  # noqa: E402  (the two-sided 95% point of Student's t, any degrees of freedom)


def catalog(path=None) -> List[dict]:
    return list(csv.DictReader((Path(path) if path else ROOT / "realms" / "catalog.csv").open()))


# the six organisms: the four realms, the whole tower (every muscle once) and the stack (the four realms on one clock,
# every duplicate kept). Nothing is named by a count: the v1 names carried one and are read as aliases.
TOWER, STACK = "tower", "stack"
ORGANISM_ALIAS = {"organism_656": TOWER, "tower_656": TOWER, "stack_1226": STACK}


def organism_name(name: str) -> str:
    return ORGANISM_ALIAS.get(name, name)


def organism_sizes(rows=None) -> dict:
    """{organism: muscles} for the six, from the catalog."""
    rows = rows or catalog()
    realms = ("compute_ai_cloud", "physics_robotics_autonomous", "energy_facility_industrial", "distribution_specialized")
    sizes = {r: sum(1 for x in rows if r in x["realms"].split(";")) for r in realms}
    sizes[STACK] = sum(sizes.values())
    sizes[TOWER] = len(rows)
    return sizes


def seed_for(muscle_id: str, seed: int) -> int:
    h = 0
    for ch in f"{muscle_id}:{seed}":
        h = (h * 1000003 + ord(ch)) % 2_147_483_647
    return h


def make_plant(row, seed, organism=False):
    steps = ORGANISM_STEPS if organism else STEPS_SINGLE[row["template"]]
    p = TEMPLATES[row["template"]](params_for(row, organism), seed_for(row["muscle_id"], seed), steps)
    if row["template"] == "compute_pool" and not organism:
        p.budget_w = 1.25 * native_mean_power(row)
    p._card = CARDS.get(row["muscle_id"])        # the muscle's own settings for the max (none: the global setting)
    return p


_CAL = {}


def native_mean_power(row):
    """A compute pool's declared power budget basis: its mean native draw on the calibration seed."""
    key = row["muscle_id"]
    if key not in _CAL:
        c = TEMPLATES[row["template"]](params_for(row), seed_for(key, CAL_SEED), STEPS_SINGLE[row["template"]])
        tot = 0.0
        for _ in range(c.steps):
            c.step()
            tot += c.power_w
        _CAL[key] = tot / c.steps
    return _CAL[key]


def calibrate_organism(rows):
    """Each plant's mean native power in the organism on the calibration seed: the organism's declared budget and
    coupling basis (the same for every arm and every result seed)."""
    key = tuple(r["muscle_id"] for r in rows)
    if key not in _CAL:
        nat = run_organism_arm(rows, CAL_SEED, "native", nominal=None)
        _CAL[key] = nat["mean_power"]
    return _CAL[key]


def authority(g, obs, d, clean):
    """The nervous system's authority after the governor's step, as the live controller computes it."""
    return from_governor(g, dict(obs, slo_clean=clean), d, mode="autopilot")


def _apply(plant, knob, g, d, auth):
    """Set the plant's override from the directive and authority; return it ({} when the knob is native)."""
    if g is None or not g.has_authority:
        plant.override = {}
        return {}
    plant.override = plant.omni_override(knob, d, g, auth)
    return plant.override


def _restored(plant, knob):
    return plant.override == {}


def _native_of(plant, key):
    """The operator's own value of an override key (what the snapshot holds); None: the key has no setting of its own
    (a floor, a release, a paced job, a battery's clip ceiling) and is simply let go."""
    P, t = plant.P, plant.template
    if key == "target":
        return P["target"]
    if key == "setpoint":
        return P["t_set"] if t == "thermal_zone" else P["reserve"] if t == "energy_storage" else P["sp"]
    if key in ("power",) or (key == "capacity" and t in ("motion_axis", "process_loop")):
        return 1.0
    if key == "floor":
        return float(P["n_min"])          # a floor walks down to the pool's least machines (the autoscaler governs)
    return None


def walk_back(plant, left):
    """One decision of the lease's walk back to native: every setting moves 1/left of the way to the operator's own;
    a key with no setting of its own is let go. left = 1 is the last step: everything native."""
    out = {}
    for key, x in plant.override.items():
        nat = _native_of(plant, key)
        if nat is None or left <= 1:
            continue
        if key == "floor" and getattr(plant, "_mx_guard", False):
            continue        # a floor that only held the pool at native's own count (it added nothing) is let go at once:
                            # the autoscaler has the pool, and a walking floor would hold machines native has released
        y = x + (nat - x) / left
        if abs(y - nat) > 1e-9:
            out[key] = y
    plant.override = out
    return out


PACE_HIGH, PACE_LOW, PACE_HEAT = 0.95, 0.8, 0.96             # the live batch_pace defaults (omni_controller/muscles.py)


def pace(paced_plants, obs, auth):
    """The live batch_pace rule over the admission muscles: while hot, suspend the next running one; while calm, resume
    the first suspended one; one per decision either way. Band first: a job whose service is out of its line, or would
    leave it if held one more period, is never suspended, and if suspended it is resumed at once (fail up)."""
    if not paced_plants:
        return
    for p in paced_plants:
        if p.paced and not (p.slo_clean and p.can_hold()):
            p.paced = False
    hot = (obs["power_stress"] >= PACE_HIGH or obs["thermal"] >= PACE_HEAT
           or bool(auth and auth["organs"]["batch"].get("pause")))
    calm = obs["power_stress"] <= PACE_LOW and obs["thermal"] < PACE_HEAT - 0.06
    if hot:
        for p in paced_plants:
            if not p.paced and p.slo_clean and p.can_hold():
                p.paced = True
                return
    elif calm:
        for p in paced_plants:
            if p.paced:
                p.paced = False
                return


def line_left(plant):
    """The share of a plant's line still waiting at the end (0: cleared; None: the plant had no line)."""
    if getattr(plant, "line_n", 0):
        return max(0, plant.line_n - plant.line_done) / plant.line_n
    if getattr(plant, "line_e", 0.0):
        return max(0.0, plant.deferred_j) / plant.line_e
    if plant.template == "compute_pool" and getattr(plant, "line0", 0.0):
        return plant.B / plant.line0
    return None


def run_muscle_arm(row, seed, arm, load=None):
    plant = make_plant(row, seed)
    if load is not None:
        scale_load_plant(plant, load)
    knob = row["knob"]
    if arm == FIXED:
        for k in range(plant.steps):
            plant.override = plant.fixed_calm()
            plant.step()
        plant.finalize()
        return dict(plant.m, writes=0, after_kill_writes=0, restore_ok=True)
    g = None if arm in ("native", FIXED, "compass", "v5", "v5save", SOLO) else Governor()
    if arm == "watch":
        g.set_mode(OBSERVE)
    kill_at = int(KILL_AT * plant.steps)
    writes = after_kill_writes = 0
    last = None
    restore_ok = True
    twin = make_plant(row, seed) if arm in ("v5", SOLO) else None    # the brain's model of native (the max's floor)
    if twin is not None and load is not None:
        scale_load_plant(twin, load)
    if arm == SOLO and native_off_pool(row["template"], knob):
        plant.native_off = twin.native_off = True                    # by itself: the pool's own autoscaler off, in both
    for k in range(plant.steps):
        if arm in ("compass", "v5", "v5save", SOLO):
            apply = LAWS["v5" if arm == SOLO else arm]
            if k < kill_at:
                if twin is not None:
                    twin.step()
                    v = max_apply(plant, knob, V5CFG, twin)
                else:
                    v = apply(plant, knob)
                if v and v != last:
                    writes += 1
            else:
                v = walk_back(plant, kill_at + WALK - k)
                if k >= kill_at + WALK - 1:
                    restore_ok = restore_ok and _restored(plant, knob)
            last = v
        elif g is not None:
            obs = plant.observe()
            if arm == "omni" and k == kill_at:
                g.kill()
            g.current_cap = 1.0                                    # as the live controller sets it
            d = g.step(obs, 0)
            auth = authority(g, obs, d, plant.slo_clean) if g.has_authority else None
            if knob == "admission" and g.has_authority and (row["template"] != "compute_pool" or plant.P.get("pausable")):
                pace([plant], obs, auth)
            v = _apply(plant, knob, g, d, auth)
            if v:
                if v != last:
                    writes += 1
                last = v
            if arm == "omni" and k >= kill_at:
                after_kill_writes += int(bool(v))
                restore_ok = restore_ok and _restored(plant, knob)
        plant.step()
    plant.finalize()
    m = dict(plant.m)
    m.update(writes=writes, after_kill_writes=after_kill_writes, restore_ok=restore_ok and after_kill_writes == 0)
    left = line_left(plant)
    if left is not None:                     # the line: the decision it was cleared at (the run's length if it was not)
        m.update(line_left=left, line_k=plant.line_k if plant.line_k is not None else plant.steps)
    return m


def run_muscle(row, seed) -> Dict:
    out = {arm: run_muscle_arm(row, seed, arm) for arm in ARMS}
    if row["knob"] == "setpoint":
        out[FIXED] = run_muscle_arm(row, seed, FIXED)
    core = ("work", "energy_j", "viol", "steps")
    out["watch_equal"] = all(out["watch"][f] == out["native"][f] for f in core) and out["watch"]["writes"] == 0
    return out


# ---------------------------------------------------------------------------------------------------------------
class Body:
    """One organism's plants and its internal coupling: the electrical power of compute, motion and process plants is
    heat in its thermal zones, its load swing is load on its storage sites, and its zones' temperature is the ambient
    every other plant reports."""

    def __init__(self, rows, seed, nominal="calibrated"):
        self.rows, self.seed, self.nominal = rows, seed, nominal
        self.load = None                     # the load profile put on the body's work demand (None: its own)
        # the calibration run first, then this body: one organism in memory at a time (1,000 copies of the four stacked
        # is 1.2 million plants). Each plant is packed as it is made (plants.pack): the same numbers, a quarter of the room
        cal = calibrate_organism(rows) if nominal == "calibrated" else None
        self.plants = [pack(make_plant(r, seed, organism=True)) for r in rows]
        if cal is not None:
            for p, w in zip(self.plants, cal):
                p.nominal_w = max(w, 1.0)
        self.knobs = [r["knob"] for r in rows]
        self.paced = [p for p, r in zip(self.plants, rows) if r["knob"] == "admission"
                      and (r["template"] != "compute_pool" or p.P.get("pausable"))]
        self.zones = [p for p in self.plants if isinstance(p, ThermalZone)]
        self.stores = [p for p in self.plants if isinstance(p, EnergyStorage)]
        self.sources = [p for p in self.plants if not isinstance(p, (ThermalZone, EnergyStorage))]
        self.nom_src = sum(p.nominal_w for p in self.sources) or 1.0
        self.nom_sz = self.nom_src + sum(z.nominal_w for z in self.zones)
        self.nom_all = self.nom_sz + sum(s.nominal_w for s in self.stores)
        self.k_heat = [0.3 * z.P["q_it_w"] / (self.nom_src / len(self.zones)) for z in self.zones] if self.zones else []
        self.k_load = [0.3 * s.P["load_w"] / (self.nom_sz / len(self.stores)) for s in self.stores] if self.stores else []
        self.budget = 1.25 * self.nom_all
        self.src_w, self.sz_w, self.all_w = self.nom_src, self.nom_sz, self.nom_all
        self.psum = [0.0] * len(self.plants)

    def couple(self):
        zones = self.zones
        th = sum(z.zone_thermal() for z in zones) / len(zones) if zones else None
        for z, kh in zip(zones, self.k_heat):
            z.ext = {"heat_w": kh * self.src_w / len(zones)}
        for s, kl in zip(self.stores, self.k_load):
            s.ext = {"load_w": kl * (self.sz_w - self.nom_sz) / len(self.stores)}
        if th is not None:
            for p in self.plants:
                if not isinstance(p, ThermalZone):
                    p.ext["thermal"] = th

    def step(self):
        for i, p in enumerate(self.plants):
            p.step()
            self.psum[i] += p.power_w
        self.src_w = sum(p.power_w for p in self.sources)
        self.sz_w = self.src_w + sum(p.power_w for p in self.zones)
        self.all_w = self.sz_w + sum(p.power_w for p in self.stores)


def aggregate(bodies):
    """One governor's reading of the bodies it serves: the mean of every plant's observation, and power stress as the
    bodies' total draw against their total budget."""
    obs = [p.observe() for b in bodies for p in b.plants]
    n = len(obs)
    agg = {key: sum(o[key] for o in obs) / n for key in ("queue_ratio", "load_ratio", "network_stress", "drift_ratio",
                                                          "thermal")}
    agg.update(power_stress=sum(b.all_w for b in bodies) / sum(b.budget for b in bodies), stale=0.0,
               security_block=0.0)
    return agg


def omni_bones(bodies):
    """The max's skeleton for each body (realms/compass_arm_v5.py, Bone), with its pools' twins."""
    return [Bone(b, V5CFG) for b in bodies]


def omni_step(bodies, bones, k, kill_at):
    """One decision of the engine's default brain over bodies: the max with each body's bone before the kill, the lease's
    walk back to native after it. Returns the plants whose setting changed (for the write count)."""
    changed = 0
    for bi, b in enumerate(bodies):
        if k >= kill_at:
            for p in b.plants:
                walk_back(p, kill_at + WALK - k)
            continue
        before = [dict(p.override) for p in b.plants]
        bones[bi].advance_twin()
        max_body_step(b, V5CFG, bones[bi])
        changed += sum(1 for p, o in zip(b.plants, before) if p.override and p.override != o)
    return changed


def run_bodies(bodies, arm, groups):
    """Run bodies on one 15 s clock. groups: lists of body indices, one governor per group (one group of all bodies is
    one governor over the whole stack; one group per body is a separate governor per body). arm native: no governor."""
    govs = []
    if arm not in ("native", "compass", "v5", "v5save", SOLO):
        for grp in groups:
            g = Governor()
            if arm == "watch":
                g.set_mode(OBSERVE)
            govs.append((g, [bodies[i] for i in grp]))
    kill_at = int(KILL_AT * ORGANISM_STEPS)
    writes = after_kill_writes = 0
    restore_ok = True
    last = {}
    bones, twins = [], []
    if arm in ("v5", SOLO):
        bones = [Bone(b, V5CFG) for b in bodies]                       # each body's skeleton, with its pools' twins
    if arm == SOLO:                                                    # by itself: every pool whose count is its knob runs with
        for b, bone in zip(bodies, bones):                             # its autoscaler off, and so does its twin
            for i, (p, r) in enumerate(zip(b.plants, b.rows)):
                if native_off_pool(p.template, r["knob"]):
                    p.native_off = True
                    if i in bone.twins:
                        bone.twins[i].native_off = True
    for k in range(ORGANISM_STEPS):
        for b in bodies:
            b.couple()
        if arm in ("compass", "v5", "v5save", SOLO):
            apply = LAWS["v5" if arm == SOLO else arm]
            for bi, b in enumerate(bodies):
                if k >= kill_at:
                    for p in b.plants:
                        walk_back(p, kill_at + WALK - k)
                        if k >= kill_at + WALK - 1:
                            restore_ok = restore_ok and _restored(p, None)
                    continue
                if arm in ("v5", SOLO):
                    bones[bi].advance_twin()
                    max_body_step(b, V5CFG, bones[bi])                 # the max: one body, its bone, its spare shared
                    for p in b.plants:
                        v = p.override
                        if v and v != last.get(id(p)):
                            writes += 1
                        last[id(p)] = dict(v)
                    continue
                for p, knob in zip(b.plants, b.knobs):
                    v = apply(p, knob)
                    if v and v != last.get(id(p)):
                        writes += 1
                    last[id(p)] = v
        for g, bs in govs:
            agg = aggregate(bs)
            if arm == "omni" and k == kill_at:
                g.kill()
            g.current_cap = 1.0
            d = g.step(agg, 0)
            auth = {c: authority(g, agg, d, c) for c in (True, False)} if g.has_authority else {True: None, False: None}
            if g.has_authority:
                pace([p for b in bs for p in b.paced], agg, auth[True])
            for b in bs:
                for p, knob in zip(b.plants, b.knobs):
                    v = _apply(p, knob, g, d, auth[p.slo_clean])
                    if v:
                        if v != last.get(id(p)):
                            writes += 1
                        last[id(p)] = v
                    if arm == "omni" and k >= kill_at:
                        after_kill_writes += int(bool(v))
                        restore_ok = restore_ok and _restored(p, knob)
        for b in bodies:
            b.step()
        for tw in twins:
            tw.couple()
            tw.step()
    for b in bodies:
        for p in b.plants:
            p.finalize()
    return {"plants": [dict(p.m) for b in bodies for p in b.plants], "writes": writes,
            "after_kill_writes": after_kill_writes, "restore_ok": restore_ok and after_kill_writes == 0,
            "mean_power": [x / ORGANISM_STEPS for b in bodies for x in b.psum]}


def run_organism_arm(rows, seed, arm, nominal="calibrated", load=None):
    b = Body(rows, seed, nominal)
    if load is not None:
        scale_load(b, load)
    return run_bodies([b], arm, [[0]])


def run_organism(rows, seed) -> Dict:
    out = {arm: run_organism_arm(rows, seed, arm) for arm in ARMS}
    out["watch_equal"] = out["watch"]["plants"] == out["native"]["plants"] and out["watch"]["writes"] == 0
    for arm in ARMS:
        out[arm].pop("mean_power", None)
    return out


# ---------------------------------------------------------------------------------------------------------------
def paired(arm_m, nat_m):
    """Per-seed contrasts of one muscle: primary, work change, violation-share change (percentage points)."""
    w = arm_m["work"] / nat_m["work"] if nat_m["work"] > 0 else (1.0 if arm_m["work"] == 0 else math.inf)
    e = arm_m["energy_j"] / nat_m["energy_j"] if nat_m["energy_j"] > 0 else math.nan
    v = (arm_m["viol"] / arm_m["steps"] - nat_m["viol"] / nat_m["steps"]) * 100.0
    return {"primary": w / e - 1.0, "work": w - 1.0, "energy": e - 1.0, "viol_pp": v}


def paired_organism(arm, nat):
    ws = [a["work"] / n["work"] for a, n in zip(arm["plants"], nat["plants"]) if n["work"] > 0]
    w = sum(ws) / len(ws)
    e = sum(a["energy_j"] for a in arm["plants"]) / sum(n["energy_j"] for n in nat["plants"])
    va = sum(a["viol"] for a in arm["plants"]) / sum(a["steps"] for a in arm["plants"])
    vn = sum(n["viol"] for n in nat["plants"]) / sum(n["steps"] for n in nat["plants"])
    return {"primary": w / e - 1.0, "work": w - 1.0, "energy": e - 1.0, "viol_pp": (va - vn) * 100.0}


def interval(xs):
    n = len(xs)
    m = sum(xs) / n
    if n < 2:
        return m, m, m
    sd = math.sqrt(sum((x - m) ** 2 for x in xs) / (n - 1))
    t = T95.get(n - 1, 1.96)
    h = t * sd / math.sqrt(n)
    return m, m - h, m + h


def label(per_seed, valid=True):
    """Result label by rule (the GPU bench's rule, docs/GPU_PREREGISTRATION.md, amendment 1)."""
    if not valid or not all(all(math.isfinite(c[k]) for k in c) for c in per_seed):
        return "INVALID"
    p = interval([c["primary"] for c in per_seed])
    w = interval([c["work"] for c in per_seed])
    v = interval([c["viol_pp"] for c in per_seed])
    guard = w[1] >= -0.01 and v[0] <= 0.0        # band first: time over the line no higher than native's (mean)
    if p[2] < 0:
        # the mirror of the energy tradeoff: less work per energy, but no work lost and the time over the line proven
        # lower (the energy bought service; a battery's round trip is the usual price). Without that proof: work per
        # energy away from its aim, and nothing bought with it
        if w[1] >= -0.01 and v[2] < 0.0:
            return "SERVICE IMPROVEMENT WITH ENERGY TRADEOFF"
        return "AWAY FROM ITS AIM"
    if p[1] > 0:
        return "SUPERIOR WITHIN GUARDRAILS" if guard else "ENERGY IMPROVEMENT WITH SERVICE TRADEOFF"
    return "NONINFERIOR / INCONCLUSIVE" if guard else "NOT ESTABLISHED"


def summarize(per_seed):
    return {k: interval([c[k] for c in per_seed]) for k in ("primary", "work", "energy", "viol_pp")}


# ---------------------------------------------------------------------------------------------------------------
def run_stack(realm_rows, seed) -> Dict:
    """The four realm organisms stacked on one clock, every muscle as often as it appears (duplicates included), each
    realm keeping its own internal coupling. Arms:
      native     no governor
      separate   one governor per realm (as if each realm had its own Omni)
      one        one governor over the whole stack
    native_equal: the stacked native run reproduces each realm's own native run exactly, plant by plant."""
    out = {}
    for arm, groups in (("native", None), ("separate", [[i] for i in range(len(realm_rows))]),
                        ("one", [list(range(len(realm_rows)))])):
        bodies = [Body(rows, seed) for rows in realm_rows]
        out[arm] = run_bodies(bodies, "native" if arm == "native" else "omni", groups or [])
    alone = []
    for rows in realm_rows:
        alone += run_organism_arm(rows, seed, "native")["plants"]
    out["native_equal"] = alone == out["native"]["plants"]
    for arm in ("native", "separate", "one"):
        out[arm].pop("mean_power", None)
    return out
