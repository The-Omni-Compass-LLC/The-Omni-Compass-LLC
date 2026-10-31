# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Run the realm harness on Omni v5 at the max and write its tables (results/realms_v5/).

  python3 tools/run_realms_v5.py                      # the preregistered run: seeds 3000-3009, the v5 catalog (1,107), results/realms_v5/
  python3 tools/run_realms_v5.py --seeds 7100 7101 --out /tmp/realms5-dev   # a look on development seeds (never reported)

Two arms, native and omni (Omni-Compass on top of native), on the same seeds. The omni arm is the engine's default, the
max (realms/compass_arm_v5.py, V5CFG): every muscle pushed toward its own limit for the most work, faster, never past its
limit and never below native; the energy that takes is shown as power given. Three panels:

  every muscle alone      each plant with only its own native controller around it (its own natural clock and horizon)
  the organisms           the spine (the muscles every stack runs on), the four realms, the four stacked (each realm's
                          own body on one clock) and the whole tower, on one 15 s clock for an hour around each battery
                          site's daily peak, every plant coupled (the
                          machines' power is heat in the rooms, the body's power swing is load on every site's line):
                          the bone (realms/compass_arm_v5.py, Bone) grants the max only the power the lines and the
                          rooms have room for
  the climb               the same organisms with their work demand stepping by one, up and down (1 2 3 2 3 4 ..., level
                          4 their own load, level 8 twice it): past what native can carry, so the most each arm can do shows
  the line                work waiting in line when the run starts (realms/harness.py, LINE: a quarter of the run's own
                          work), for every muscle alone and every organism: the arm that clears it sooner is faster

Judged on work, on speed (the line cleared sooner) and on time over the line (misses); energy is shown, as power given,
beside the work it bought. A muscle whose knob native already runs at the top of its range is labelled at its limit on
native. Every plant inside each organism that did less work or spent more decisions over its line than native is listed,
whatever it shows.
Writes MUSCLES_V5.csv, REALMS_V5.json, REALMS_V5.md, RUN.json, SHA256SUMS.txt. Evidence class S (modelled). The
preregistered seeds run only on committed code.
"""
import argparse, csv, hashlib, json, os, subprocess, sys, time
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

try:
    from tools.legal import stamp as _legal_stamp
except ImportError:
    from tools.legal import stamp as _legal_stamp  # pragma: no cover

from tools.readings import GAIN, LOSS, GAIN_AND_LOSS, labelled, receipt_key  # noqa: E402  (the words every table uses)
from realms.harness import (catalog, run_muscle_arm, run_bodies, Body, paired, paired_organism, interval, scale_load,
                            TOWER, STACK, KILL_AT, WALK, LINE, SOLO, native_off_pool)
from realms.compass_arm_v5 import native_at_limit
from realms.presets import PRESETS

PREREG_SEEDS = list(range(3000, 3010))
REALMS = ["compute_ai_cloud", "physics_robotics_autonomous", "energy_facility_industrial", "distribution_specialized"]
# the seventh organism (the founder's order of 16 October): the spine, every muscle that sits in all four realms, the base
# every stack runs on (as an operating system is the base of every program), run native and with Omni-Compass on top like
# the other six. The organisms are groupings of catalog rows made here; no engine file names them
SPINE = "spine"
ORGANISMS = [SPINE] + REALMS + [STACK, TOWER]           # the seven, in the order every table lists them
NAMES = {SPINE: "The spine, the muscles every stack runs on",
         "compute_ai_cloud": "Compute / AI / Cloud", "physics_robotics_autonomous": "Physics / Robotics / Autonomous",
         "energy_facility_industrial": "Energy / Facility / Industrial",
         "distribution_specialized": "Distribution / Specialized", STACK: "The four stacked, every shared muscle in each",
         TOWER: "The whole tower, every muscle once"}
GAINS = ["MORE WORK", "FASTER", "FEWER MISSES"]
# The kinds, by the muscle's three aims (more work, faster, fewer misses), in the words every table uses (tools/readings.py):
# GAIN (some aim toward and none away), STEADY (the same as native, or at its limit on native), GAIN AND LOSS, LOSS
TOWARD, BOTH, AWAY = GAIN, GAIN_AND_LOSS, LOSS
SAME, AT_LIMIT = "SAME AS NATIVE", "AT ITS LIMIT ON NATIVE"
KINDS = [TOWARD, SAME, AT_LIMIT, BOTH, AWAY, "INVALID"]
# the same kinds as the results written before (13 October and earlier) named them, read as they were written
RECORDED = {"MIXED": BOTH, "WORSE": AWAY, "BOTH WAYS": BOTH, "AWAY FROM ITS AIMS": AWAY, "TOWARD ITS AIMS": TOWARD}
LOADS = {"normal": "the organism's own load", "climb": "the climb (1 2 3 2 3 4 ..., level 4 = own load, 8 = twice it)",
         "line": f"work waiting in line (a {LINE:.0%} share of the run's own work waiting when it starts)"}
MUSCLE_LOADS = {"normal": "its own load", "line": f"work waiting in line ({LINE:.0%} of the run's own work at the start)"}
ORGANISM_LOADS = ["normal", "climb", "line"]
# the engine and the files it stands on; the engine fingerprint is tools/omni_version.py (OMNI_V5.json)
FROZEN = ["realms", "omnicompass", "tools/run_realms_v5.py"]


def spine_rows(rows):
    """The spine: every muscle whose realm list names all four realms (Kubernetes, containers, placement, node fleets, cloud
    capacity, hosts, GPUs, network, storage, observability, reliability and security, electrical distribution, cooling)."""
    return [r for r in rows if set(REALMS) <= set(r["realms"].split(";"))]


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def tree_sha(paths):
    h = hashlib.sha256()
    for p in sorted(paths):
        h.update(p.encode()); h.update(sha(ROOT / p).encode())
    return h.hexdigest()


def gains_losses(per_seed):
    """What the max did against native, by rule (95% intervals over seeds, each clear of zero): more work (or less),
    faster (the line cleared sooner, or later; only where there is a line) and fewer misses (or more)."""
    w = interval([c["work"] for c in per_seed])
    v = interval([c["viol_pp"] for c in per_seed])
    gains = {"MORE WORK": w[1] > 1e-12, "FEWER MISSES": v[2] < -1e-12}
    losses = {"LESS WORK": w[2] < -1e-12, "MORE MISSES": v[1] > 1e-12}
    if all("speed" in c for c in per_seed):
        s = interval([c["speed"] for c in per_seed])
        gains["FASTER"], losses["SLOWER"] = s[2] < -1e-12, s[1] > 1e-12
    return [g for g in GAINS if gains.get(g)], [l for l, x in losses.items() if x]


def label_max(per_seed, valid=True, at_limit=False):
    """The max's label by rule, against the muscle's three aims (more work, its line cleared sooner, fewer misses):
      the gains, joined (MORE WORK + FASTER + FEWER MISSES, or any of them)   at least one toward its aim and none away:
                               kind GAIN
      SAME AS NATIVE           no difference beyond the noise: STEADY
      AT ITS LIMIT ON NATIVE   no difference, and native already runs the knob at the top of its range (the max wrote
                               nothing: there is nothing above native to give it): STEADY
      GAIN AND LOSS            one toward its aim and one away (less work, slower or more misses)
      LOSS                     one away and none toward
      INVALID                  a knob not handed back to native by the lease"""
    if not valid:
        return "INVALID"
    gains, losses = gains_losses(per_seed)
    if losses:
        return BOTH if gains else AWAY
    if gains:
        return " + ".join(gains)
    return AT_LIMIT if at_limit else SAME


def kind_of(label):
    label = RECORDED.get(label, label)
    return TOWARD if label not in KINDS else label


def summarize(per_seed):
    return {k: interval([c[k] for c in per_seed]) for k in ("primary", "work", "energy", "viol_pp")}


def decision_s(row):
    """The length of one decision of a muscle alone, in seconds (its plant's own natural clock)."""
    P = PRESETS[row["preset"]]
    return P.get("dt_dec", P.get("dt", 1.0))


def muscle_load(row, seeds, load):
    """Native against the max for one muscle under one load, over the seeds. valid: the lease hands every knob back to
    native after the brain goes silent, proven each seed. Under the line, speed is how long the line took to clear,
    omni against native (negative: faster)."""
    arg = None if load == "normal" else load
    nat = [run_muscle_arm(row, s, "native", arg) for s in seeds]
    mx = [run_muscle_arm(row, s, "v5", arg) for s in seeds]
    valid = all(r["restore_ok"] for r in mx)
    per = [paired(a, n) for a, n in zip(mx, nat)]
    wear = [a["wear"] / n["wear"] - 1.0 for a, n in zip(mx, nat) if n["wear"] > 0]   # shown beside the work, never judged
    line = None
    if all("line_k" in n for n in nat):
        for c, a, n in zip(per, mx, nat):
            c["speed"] = (a["line_k"] + 1) / (n["line_k"] + 1) - 1.0
        dmin = decision_s(row) / 60.0
        line = [sum(n["line_k"] + 1 for n in nat) / len(nat) * dmin, sum(a["line_k"] + 1 for a in mx) / len(mx) * dmin,
                sum(n["line_left"] for n in nat) / len(nat), sum(a["line_left"] for a in mx) / len(mx)]
    writes = sum(r["writes"] for r in mx) / len(mx)
    at_limit = writes == 0 and native_at_limit(row["template"], row["knob"])
    solo = solo_load(row, seeds, arg, nat, mx) if native_off_pool(row["template"], row["knob"]) else None
    return {"valid": valid, "label": label_max(per, valid, at_limit), "summary": summarize(per), "per_seed": per, "solo": solo,
            "writes": writes, "native_viol_share": sum(n["viol"] / n["steps"] for n in nat) / len(nat),
            "viol_native": sum(n["viol"] for n in nat), "viol_max": sum(m["viol"] for m in mx),
            "steps": sum(n["steps"] for n in nat), "line": line,
            "wear": sum(wear) / len(wear) if wear else 0.0}


def solo_load(row, seeds, arg, nat, mx):
    """Omni-Compass by itself on one muscle under one load (the founder's order of 23 October, docs/SOLO_PREREGISTRATION.md):
    the pool's own autoscaler switched off, the brain the only controller of its count, against native and against
    Omni-Compass and native on the same seeds."""
    so = [run_muscle_arm(row, s, SOLO, arg) for s in seeds]
    per = [paired(a, n) for a, n in zip(so, nat)]
    per_m = [paired(a, m) for a, m in zip(so, mx)]
    if all("line_k" in n for n in nat):
        for c, a, n in zip(per, so, nat):
            c["speed"] = (a["line_k"] + 1) / (n["line_k"] + 1) - 1.0
        for c, a, m in zip(per_m, so, mx):
            c["speed"] = (a["line_k"] + 1) / (m["line_k"] + 1) - 1.0
    valid = all(r["restore_ok"] for r in so)
    return {"valid": valid, "label": label_max(per, valid), "summary": summarize(per), "per_seed": per,
            "vs_omni": {"label": label_max(per_m, valid), "summary": summarize(per_m), "per_seed": per_m},
            "viol_solo": sum(r["viol"] for r in so), "writes": sum(r["writes"] for r in so) / len(so)}


def label_over_loads(by, key=None):
    """One muscle's word over all its loads: toward its aims under some load and away under none is GAIN."""
    pick = (lambda o: o) if key is None else key
    os_ = [pick(o) for o in by.values()]
    if not all(o["valid"] for o in os_):
        return "INVALID"
    gains, losses = set(), set()
    for o in os_:
        g, l = gains_losses(o["per_seed"])
        gains.update(g); losses.update(l)
    if losses:
        return BOTH if gains else AWAY
    if gains:
        return " + ".join(g for g in GAINS if g in gains)
    return AT_LIMIT if all(o["label"] == AT_LIMIT for o in os_) else SAME


def muscle_job(args):
    """Every load of one muscle, and its label over all of them: toward its aims under some load and away under none is
    GAIN."""
    row, seeds = args
    by = {load: muscle_load(row, seeds, load) for load in MUSCLE_LOADS}
    valid = all(o["valid"] for o in by.values())
    gains, losses = set(), set()
    for o in by.values():
        g, l = gains_losses(o["per_seed"])
        gains.update(g); losses.update(l)
    if not valid:
        label = "INVALID"
    elif losses:
        label = BOTH if gains else AWAY
    elif gains:
        label = " + ".join(g for g in GAINS if g in gains)
    else:
        label = AT_LIMIT if all(o["label"] == AT_LIMIT for o in by.values()) else SAME
    solo = None
    if all(o.get("solo") for o in by.values()):
        solo = {"label": label_over_loads(by, lambda o: o["solo"]),
                "vs_omni": label_over_loads(by, lambda o: dict(o["solo"]["vs_omni"], valid=o["solo"]["valid"]))}
    return {"row": row, "valid": valid, "label": label, "loads": by, "solo": solo,
            "writes": max(o["writes"] for o in by.values())}


def plant_harms(arm, nat, ids):
    """Every plant inside the organism that did less work than native or spent more decisions over its line."""
    out = []
    for i, (a, n) in enumerate(zip(arm["plants"], nat["plants"])):
        dw = a["work"] / n["work"] - 1.0 if n["work"] > 0 else 0.0
        dv = a["viol"] - n["viol"]
        if dw < -1e-9 or dv > 0:
            out.append([ids[i], dw, dv])
    return out


def organism_run(name, rows, seed, arm, load):
    """One organism, one arm, one load. The four stacked keep each realm's own body on one clock, so every muscle in the
    stack runs exactly the native it runs in its own realm, plant by plant (the founder's order: the native identical in
    all seven)."""
    if name == STACK:
        bodies = [Body(rs, seed) for rs in rows]
    else:
        bodies = [Body(rows, seed)]
    if load != "normal":
        for b in bodies:
            scale_load(b, load)
    return run_bodies(bodies, arm, [list(range(len(bodies)))])


def organism_job(args):
    name, rows, seed, load = args
    ids = ([f"{r['muscle_id']}@{realm}" for realm, rs in zip(REALMS, rows) for r in rs] if name == STACK
           else [r["muscle_id"] for r in rows])
    nat = organism_run(name, rows, seed, "native", load)
    mx = organism_run(name, rows, seed, "v5", load)
    so = organism_run(name, rows, seed, SOLO, load)      # Omni-Compass by itself: every pool's own autoscaler off
    vn = sum(p["viol"] for p in nat["plants"]); vm = sum(p["viol"] for p in mx["plants"])
    wear = [a["wear"] / n["wear"] - 1.0 for a, n in zip(mx["plants"], nat["plants"]) if n["wear"] > 0]
    wear_s = [a["wear"] / n["wear"] - 1.0 for a, n in zip(so["plants"], nat["plants"]) if n["wear"] > 0]
    return name, seed, load, {"max": paired_organism(mx, nat), "restore_ok": mx["restore_ok"],
                              "harms": plant_harms(mx, nat, ids), "viol_native": vn, "viol_max": vm,
                              "steps": sum(p["steps"] for p in nat["plants"]),
                              "wear": sum(wear) / len(wear) if wear else 0.0,
                              "solo": {"vs_native": paired_organism(so, nat), "vs_omni": paired_organism(so, mx),
                                       "restore_ok": so["restore_ok"], "harms": plant_harms(so, nat, ids),
                                       "viol_solo": sum(p["viol"] for p in so["plants"]),
                                       "wear": sum(wear_s) / len(wear_s) if wear_s else 0.0}}


def fmt(m, scale=100.0, unit="%"):
    return f"{m[0] * scale:+.2f}{unit} ({m[1] * scale:+.2f} to {m[2] * scale:+.2f})"


def misses_line(o):
    vn, vm, st = o["viol_native"], o["viol_max"], o["steps"]
    cut = (1.0 - vm / vn) * 100.0 if vn else 0.0
    return f"{100.0 * vn / st:.2f}% → {100.0 * vm / st:.2f}% ({'−' if cut >= 0 else '+'}{abs(cut):.1f}%)"


def write_md(out, res, orgs, run):
    L = []
    w = L.append
    w(f"# The realms on {run['engine']} at the max: {len(res)} muscles and seven organisms, three ways: native, Omni-Compass "
      "and native, and Omni-Compass by itself")
    w("")
    for ln in receipt_key():
        w(ln)
    w("")
    w(f"Evidence class **S** (modelled). Run {run['started']}, commit `{run['commit'][:12]}`, seeds "
      f"{run['seeds'][0]}-{run['seeds'][-1]} ({len(run['seeds'])} paired seeds per muscle, per organism and per load), "
      f"catalog `{run['catalog']}`. The engine is **{run['engine']}** (`tools/omni_version.py`) at its default, "
      "**the max** (`realms/compass_arm_v5.py`, `V5CFG`), on top of each plant's own native controller. Harness `realms/`.")
    w("")
    w("**The max.** Every muscle is pushed toward its own limit for the most work, faster: a pool's machines are started "
      "before the rush lands (the recent peak arrivals widened by the largest rise the pool has shown within one machine "
      "start, at 95% utilisation), never fewer than its twin runs (the brain's model of native: the same pool under its "
      "own autoscaler alone, on the same arrivals); a room is cooled ahead of the heat as it nears its limit or its cooling "
      "nears flat out; a battery's line is clipped from its charge, a UPS lending only the charge above its outage floor. "
      "Work waiting in line is cleared within one machine start, and the machines it no longer needs go back at once (never "
      "below the twin). A muscle native already runs flat out (full clock, full speed, full actuator, nothing turned "
      "away) is wired, watched and native: there is nothing above native to give it. Nothing is taken from one muscle to "
      "give to another; the max never shaves. The energy the max takes is reported as **power given**, beside the work "
      "and the speed it bought.")
    w("")
    w(f"**The line.** Under the line load, every plant starts with work already waiting, a {LINE:.0%} share of the work its "
      "own run brings: a pool's jobs submitted before the start (its machines take them from what the requests leave "
      "them), an axis's tasks queued, a site's flexible load held over. A room's heat and a loop's demand cannot wait, so "
      "they have none. Both arms start with the same line; the one that clears it sooner is **faster**.")
    w("")
    w("**The bone.** Inside an organism the max may give only the power the body can carry: a site's grid line and a "
      "room's cooling are loaded by the whole body (the machines' power is heat in every room, the body's power swing is "
      "load on every site's line), so machines and cooling are granted out of the room the most loaded line has left, "
      "read one decision ahead (its latest reading plus the larger of 3.09 of its own step-to-step wobbles and the largest "
      "single climb it has shown, the wobbles counted on the line without the max's own machines: its own steps are not "
      "the line's). A site with flexible load waiting gives its catch-up the room first. With no room, what the max added "
      "goes back, as much as the shortfall needs (the pools holding the most extra machines first, the machines started "
      "last first), never below a pool's twin: nothing native has is taken. The organisms run the hour around each "
      "battery site's daily peak, where the UPS lines carry most of their rating: the bone is tight there, and the max "
      "gives only what it can carry.")
    w("")
    w(f"**The lease.** At {int(KILL_AT * 100)}% of every run the brain is cut; the plug walks every setting back to "
      f"native over {WALK} decisions (a jump the body would have to absorb at once is the swing the founder ordered "
      "gone), and the run goes on native until it ends; every knob must be back at the operator's own before then "
      "(valid). A floor that only held a pool at its twin's count adds nothing to walk back and is let go at once (a "
      "walking floor would hold machines native had already released). The security kill switch is instant "
      "(`omnicompass/master.py`).")
    w("")
    w("These are models; a model's energy is not a meter's, and a plant written by the same people who wrote the law is not "
      "an independent test. What a row shows is whether the max, applied to that knob, helps or hurts the model.")
    w("")
    for load in run["loads"]:
        w(f"## The seven organisms: {LOADS[load]}")
        w("")
        w("Work: the mean over the organism's plants of each plant's work against native's. Misses: the share of plant "
          "decisions over their line, native → Omni-Compass and native (the change in misses). Power given: the organism's energy against "
          "native's. Wear: the mean over its plants of each plant's wear against native's (machine-hours, cooling "
          "unit-hours, battery throughput, motor heat, actuator duty), shown beside the work, never judged. 95% intervals "
          "over seeds.")
        w("")
        w("| Organism | Muscles | Reading | Work | Misses, native → Omni-Compass and native | Misses (pp) | Power given | Wear | Work per energy | Valid |")
        w("|---|---:|---|---:|---|---:|---:|---:|---:|---|")
        for name in [n for n in ORGANISMS if n in orgs[load]]:
            o = orgs[load][name]; s = o["summary"]
            w(f"| {NAMES[name]} | {o['n']} | **{labelled(o['label'])}** | {fmt(s['work'], 100.0)} | {misses_line(o['totals'])} | "
              f"{fmt(s['viol_pp'], 1.0, '')} | {fmt(s['energy'])} | {o['wear'] * 100:+.2f}% | {fmt(s['primary'])} | "
              f"{'yes' if o['valid'] else 'NO'} |")
        w("")
        if any(orgs[load][n].get("solo") for n in ORGANISMS if n in orgs[load]):
            w(f"**Omni-Compass by itself**, {LOADS[load]} (the founder's order of 23 October, `docs/SOLO_PREREGISTRATION.md`): "
              "every pool's own autoscaler switched off and the brain the only controller of its count; every other muscle "
              "as in Omni-Compass and native, because its native is a setting native holds still or its own actuator. Read "
              "against native and against Omni-Compass and native, on the same seeds.")
            w("")
            w("| Organism | Against native | Work | Misses, native → by itself | Misses (pp) | Power given | Wear | "
              "Against Omni-Compass and native | Valid |")
            w("|---|---|---:|---|---:|---:|---:|---|---|")
            for name in [n for n in ORGANISMS if n in orgs[load]]:
                so = orgs[load][name].get("solo")
                if not so:
                    continue
                s_, t_ = so["summary"], so["totals"]
                ml = misses_line({"viol_native": t_["viol_native"], "viol_max": t_["viol_solo"], "steps": t_["steps"]})
                w(f"| {NAMES[name]} | **{labelled(so['label'])}** | {fmt(s_['work'], 100.0)} | {ml} | "
                  f"{fmt(s_['viol_pp'], 1.0, '')} | {fmt(s_['energy'])} | {so['wear'] * 100:+.2f}% | "
                  f"{labelled(so['vs_omni']['label'])} | {'yes' if so['valid'] else 'NO'} |")
            w("")
    w("## Inside the organisms: every plant that did less work than native or missed its line more often")
    w("")
    w("A stricter look than an organism's total: every plant inside each organism, over all seeds, that did less work "
      "than native or spent more decisions over its own line, under each load. Reported whatever it shows.")
    w("")
    w("| Load | Organism | Plants | Plants with less work or more misses | The plants (work change, extra decisions over the line, all seeds) |")
    w("|---|---|---:|---:|---|")
    for load in run["loads"]:
        for name in [n for n in ORGANISMS if n in orgs[load]]:
            o = orgs[load][name]; h = o.get("plants_flagged", o.get("plants_worse", {}))   # the older results' field, read as written
            lst = "; ".join(f"{mid} ({v[0] * 100:+.3f}%, {v[1]:+d})" for mid, v in sorted(h.items(), key=lambda kv: kv[1][0])) or "none"
            w(f"| {load} | {NAMES[name]} | {o['n']} | {len(h)} | {lst} |")
    w("")
    w("## Every muscle alone, by home realm")
    w("")
    w(f"Each muscle runs under {len(MUSCLE_LOADS)} loads, " + " and ".join(f"{v} ({k})" for k, v in MUSCLE_LOADS.items())
      + ". Each muscle's word is judged by its three aims, never by the sign of a number (the key: "
      "`docs/HOW_TO_READ_THE_RESULTS.md`). **GAIN**: at least one of its three aims moved beyond the noise under some load "
      "(more work, faster: the line cleared sooner, fewer misses) and none the other way under any. **GAIN AND LOSS**: one "
      "toward its aim and one away (less work, slower or more misses). **LOSS**: one away and none toward. **STEADY, at its "
      "limit on native**: native already runs the knob at the top of its range (full clock, full speed, full torque, full "
      "battery power, nothing paced or turned away), so the max has nothing above native to give it and writes nothing. "
      "**STEADY, the same as native**: the max acted or could, and the result is no different beyond the noise (native "
      "already did all the work that came and was almost never over its line). The energy the max takes is power given, "
      "shown beside the work, never judged.")
    w("")
    w("| Realm | Muscles | GAIN | of them: more work | faster | fewer misses | STEADY, the same as native | STEADY, at its limit on native | GAIN AND LOSS | LOSS | Invalid |")
    w("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")

    def count_row(rs):
        c = Counter(kind_of(r["label"]) for r in rs)
        g = [sum(1 for r in rs if kind_of(r["label"]) == TOWARD and x in r["label"]) for x in GAINS]
        return [len(rs), c.get(TOWARD, 0), *g, c.get(SAME, 0), c.get(AT_LIMIT, 0),
                c.get(BOTH, 0), c.get(AWAY, 0), c.get("INVALID", 0)]
    for realm in REALMS:
        w(f"| {NAMES[realm]} | " + " | ".join(str(x) for x in count_row([r for r in res if r["row"]["realm"] == realm])) + " |")
    w("| **All** | " + " | ".join(f"**{x}**" for x in count_row(res)) + " |")
    w("")
    if any(r.get("solo") for r in res):
        w("**Omni-Compass by itself, every muscle alone.** By itself differs from Omni-Compass and native only where the "
          "muscle's own native controller can be switched off: a pool whose knob is its count, its autoscaler off and the "
          "brain the only controller. Every other muscle's native is a setting native holds still or its own actuator, so "
          "by itself is the same arm there, and is counted so.")
        w("")
        w("| Realm | Muscles | The same arm | By itself | GAIN | STEADY, the same as native | GAIN AND LOSS | LOSS | Invalid | "
          "Against Omni-Compass and native: GAIN | STEADY | GAIN AND LOSS or LOSS |")
        w("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|")

        def solo_row(rs):
            so = [r for r in rs if r.get("solo")]
            c = Counter(kind_of(r["solo"]["label"]) for r in so)
            cm = Counter(kind_of(r["solo"]["vs_omni"]) for r in so)
            return [len(rs), len(rs) - len(so), len(so), c.get(TOWARD, 0), c.get(SAME, 0) + c.get(AT_LIMIT, 0), c.get(BOTH, 0),
                    c.get(AWAY, 0), c.get("INVALID", 0), cm.get(TOWARD, 0), cm.get(SAME, 0) + cm.get(AT_LIMIT, 0),
                    cm.get(BOTH, 0) + cm.get(AWAY, 0)]
        for realm in REALMS:
            w(f"| {NAMES[realm]} | " + " | ".join(str(x) for x in solo_row([r for r in res if r["row"]["realm"] == realm])) + " |")
        w("| **All** | " + " | ".join(f"**{x}**" for x in solo_row(res)) + " |")
        w("")
    for load, what in MUSCLE_LOADS.items():
        w(f"## Every muscle alone under {what}, by kind of plant and knob")
        w("")
        w("Misses: the share of decisions over the line, native → Omni-Compass and native. Line: minutes to clear the work waiting at the "
          "start, native → Omni-Compass and native (and the share still waiting at the end, where it did not clear). Power given: energy "
          "against native's.")
        w("")
        w("| Plant | Knob | Muscles | Omni-Compass acts on | GAIN | STEADY, at its limit on native | Misses, native → Omni-Compass and native | Work | Line, native → Omni-Compass and native | Power given | Wear |")
        w("|---|---|---:|---:|---:|---:|---|---:|---|---:|---:|")
        groups = defaultdict(list)
        for r in res:
            groups[(r["row"]["template"], r["row"]["knob"])].append(r)
        for (t, k), rs in sorted(groups.items()):
            os_ = [r["loads"][load] for r in rs]
            vn = sum(o["viol_native"] for o in os_); vm = sum(o["viol_max"] for o in os_)
            st = max(1, sum(o["steps"] for o in os_))
            wk = sum(o["summary"]["work"][0] for o in os_) / len(os_)
            en = sum(o["summary"]["energy"][0] for o in os_) / len(os_)
            lines = [o["line"] for o in os_ if o["line"]]
            if lines:
                ln = (f"{sum(x[0] for x in lines) / len(lines):.1f} → {sum(x[1] for x in lines) / len(lines):.1f} min"
                      + (f" ({sum(x[2] for x in lines) / len(lines):.0%} → {sum(x[3] for x in lines) / len(lines):.0%} left)"
                         if any(x[2] > 0 or x[3] > 0 for x in lines) else ""))
            else:
                ln = "no line"
            toward = sum(1 for o in os_ if kind_of(o["label"]) == TOWARD)
            lim = sum(1 for o in os_ if o["label"] == AT_LIMIT)
            w(f"| {t} | {k} | {len(rs)} | {sum(1 for o in os_ if o['writes'] > 0)} | {toward} | {lim} | "
              f"{100.0 * vn / st:.2f}% → {100.0 * vm / st:.2f}% | {wk * 100:+.3f}% | {ln} | {en * 100:+.2f}% | "
              f"{sum(o['wear'] for o in os_) / len(os_) * 100:+.2f}% |")
        w("")
    w("## No-harm check")
    w("")
    away = [r for r in res if kind_of(r["label"]) in (AWAY, BOTH)]
    acted = sum(1 for r in res if r["writes"] > 0)
    lim = sum(1 for r in res if r["label"] == AT_LIMIT)
    w(f"- Omni acts on **{acted}** of {len(res)} muscles alone. **{lim}** are at their limit on native (the knob is "
      "already at the top of its range: STEADY); the rest it could act on show nothing beyond the noise to gain.")
    w(f"- Muscles alone that read **LOSS** or **GAIN AND LOSS** under any load: **{len(away)}**"
      + ("." if not away else ": " + ", ".join(f"{r['row']['muscle']} ({r['row']['knob']}, {kind_of(r['label'])})" for r in away) + "."))
    s_away = [r for r in res if r.get("solo") and kind_of(r["solo"]["label"]) in (AWAY, BOTH)]
    if any(r.get("solo") for r in res):
        w(f"- Muscles alone by themselves (Omni-Compass with the pool's own autoscaler off) that read **LOSS** or **GAIN AND "
          f"LOSS** against native under any load: **{len(s_away)}**"
          + ("." if not s_away else ": " + ", ".join(f"{r['row']['muscle']} ({r['row']['knob']}, {kind_of(r['solo']['label'])})"
                                                    for r in s_away[:40]) + ("; and more in `MUSCLES_V5.csv`." if len(s_away) > 40 else ".")))
    w("- The lease hands every knob back to native before each run ends: "
      f"{sum(1 for r in res if r['valid'])} of {len(res)} muscles under every load; "
      + ", ".join(f"{sum(1 for o in orgs[load].values() if o['valid'])} of {len(orgs[load])} organisms under {load}"
                  for load in run["loads"]) + ".")
    w("")
    w("## Largest changes (muscles alone, own load, by mean change in misses)")
    w("")
    srt = sorted(res, key=lambda r: r["loads"]["normal"]["summary"]["viol_pp"][0])
    w("| Muscle | Family | Knob | Label (all loads) | Misses (pp) | Work | Power given |")
    w("|---|---|---|---|---:|---:|---:|")
    for r in srt[:10] + srt[-10:][::-1]:
        s = r["loads"]["normal"]["summary"]
        w(f"| {r['row']['muscle']} | {r['row']['family']} | {r['row']['knob']} | {r['label']} | {fmt(s['viol_pp'], 1.0, '')} | "
          f"{fmt(s['work'])} | {fmt(s['energy'])} |")
    w("")
    w("Raw per-seed contrasts: `REALMS_V5.json`. One row per muscle: `MUSCLES_V5.csv`. Fingerprints: `RUN.json`, "
      "`SHA256SUMS.txt`.")
    (out / "REALMS_V5.md").write_text("\n".join(_legal_stamp(L)) + "\n")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--seeds", type=int, nargs="+", default=PREREG_SEEDS)
    ap.add_argument("--out", default=str(ROOT / "results" / "realms_v5"))
    ap.add_argument("--catalog", default=str(ROOT / "realms" / "catalog_v5.csv"))   # the v5 muscle set (1,097)
    ap.add_argument("--workers", type=int, default=os.cpu_count() or 2)
    ap.add_argument("--loads", default=",".join(ORGANISM_LOADS), help="organism loads, comma separated (normal, climb, line)")
    ap.add_argument("--limit", type=int, default=0, help="first N muscles only (a look; never reported)")
    a = ap.parse_args(argv)
    loads = [x for x in a.loads.split(",") if x]
    prereg = (a.seeds == PREREG_SEEDS and not a.limit and a.catalog == str(ROOT / "realms" / "catalog_v5.csv")
              and loads == ORGANISM_LOADS)
    dirty = subprocess.run(["git", "status", "--porcelain", "--"] + FROZEN, cwd=ROOT, capture_output=True,
                           text=True).stdout.strip()
    if prereg and dirty:
        print("the preregistered seeds run only on committed code; uncommitted changes in:\n" + dirty)
        return 1
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    rows = catalog(a.catalog)
    if a.limit:
        rows = rows[:a.limit]
    commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    frozen_files = [str(p.relative_to(ROOT)) for d in ("realms", "omnicompass") for p in sorted((ROOT / d).rglob("*"))
                    if p.is_file() and p.suffix in (".py", ".csv", ".json")]
    from tools.omni_version import engine_files, version_of, digest
    engine_snapshot = engine_files()
    run = {"started": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()), "commit": commit, "seeds": a.seeds,
           "preregistered": prereg, "dirty": bool(dirty), "muscles": len(rows), "engine": version_of(engine_snapshot) or "undeclared", "engine_digest": digest(engine_snapshot), "dial": "max",
           "loads": loads, "muscle_loads": list(MUSCLE_LOADS), "line": LINE, "kill_at": KILL_AT, "walk": WALK,
           "catalog": str(Path(a.catalog).relative_to(ROOT)) if Path(a.catalog).is_absolute() else a.catalog,
           "frozen_tree_sha256": tree_sha(frozen_files + ["tools/run_realms_v5.py"]),
           "law_sha256": sha(ROOT / "realms" / "compass_arm_v5.py")}
    t0 = time.time()
    with ProcessPoolExecutor(a.workers) as ex:
        res = list(ex.map(muscle_job, [(r, a.seeds) for r in rows], chunksize=4))
        print(f"muscles: {len(res)} in {time.time() - t0:.0f} s", flush=True)
        groups = {SPINE: spine_rows(rows)}                            # the base every stack runs on, an organism of its own
        groups.update({realm: [r for r in rows if realm in r["realms"].split(";")] for realm in REALMS})
        groups[STACK] = [groups[realm] for realm in REALMS]           # each realm's own body, the realm's own native
        groups[TOWER] = rows
        jobs = [(name, rs, s, load) for load in loads for name, rs in groups.items() if rs for s in a.seeds]
        raw = defaultdict(lambda: defaultdict(dict))
        for name, seed, load, o in ex.map(organism_job, jobs):
            raw[load][name][seed] = o
    print(f"organisms done in {time.time() - t0:.0f} s", flush=True)
    orgs = {}
    for load, by_name in raw.items():
        orgs[load] = {}
        for name, by_seed in by_name.items():
            runs = [by_seed[s] for s in a.seeds]
            valid = all(o["restore_ok"] for o in runs)
            per = [o["max"] for o in runs]
            agg = defaultdict(lambda: [0.0, 0, 0])
            for o in runs:
                for mid, dw, dv in o["harms"]:
                    agg[mid][0] += dw / len(runs)
                    agg[mid][1] += dv
                    agg[mid][2] += 1
            harms = {mid: v for mid, v in agg.items() if v[0] < -1e-9 or v[1] > 0}
            sruns = [o["solo"] for o in runs]
            s_valid = all(o["restore_ok"] for o in sruns)
            s_agg = defaultdict(lambda: [0.0, 0, 0])
            for o in sruns:
                for mid, dw, dv in o["harms"]:
                    s_agg[mid][0] += dw / len(sruns)
                    s_agg[mid][1] += dv
                    s_agg[mid][2] += 1
            s_per, s_per_m = [o["vs_native"] for o in sruns], [o["vs_omni"] for o in sruns]
            solo = {"valid": s_valid, "label": label_max(s_per, s_valid), "summary": summarize(s_per), "per_seed": s_per,
                    "vs_omni": {"label": label_max(s_per_m, s_valid), "summary": summarize(s_per_m), "per_seed": s_per_m},
                    "plants_flagged": {mid: v for mid, v in s_agg.items() if v[0] < -1e-9 or v[1] > 0},
                    "wear": sum(o["wear"] for o in sruns) / len(sruns),
                    "totals": {"viol_native": sum(o["viol_native"] for o in runs), "viol_solo": sum(o["viol_solo"] for o in sruns),
                               "steps": sum(o["steps"] for o in runs)}}
            orgs[load][name] = {"n": sum(len(g) for g in groups[name]) if name == STACK else len(groups[name]), "solo": solo,
                                "valid": valid, "label": label_max(per, valid), "summary": summarize(per),
                                "per_seed": per, "plants_flagged": harms,
                                "wear": sum(o["wear"] for o in runs) / len(runs),
                                "totals": {"viol_native": sum(o["viol_native"] for o in runs),
                                           "viol_max": sum(o["viol_max"] for o in runs),
                                           "steps": sum(o["steps"] for o in runs)}}
    run["elapsed_s"] = round(time.time() - t0)
    with (out / "MUSCLES_V5.csv").open("w", newline="") as f:
        cols = ["muscle_id", "family", "muscle", "realm", "template", "preset", "knob", "label_all_loads", "load", "label",
                "work", "work_lo", "work_hi", "viol_pp", "viol_pp_lo", "viol_pp_hi", "line_native_min", "line_omni_min",
                "power_given", "wear", "work_per_energy", "writes_per_run", "native_viol_share", "valid",
                "solo_label_all_loads", "solo_label", "solo_work", "solo_viol_pp", "solo_power_given", "solo_vs_omni_label"]
        wr = csv.writer(f); wr.writerow(cols)
        for r in res:
            row = r["row"]
            for load, o in r["loads"].items():
                s, ln = o["summary"], o["line"]
                wr.writerow([row["muscle_id"], row["family"], row["muscle"], row["realm"], row["template"], row["preset"],
                             row["knob"], r["label"], load, o["label"], *(f"{x:.5f}" for x in s["work"]),
                             *(f"{x:.3f}" for x in s["viol_pp"]), *((f"{ln[0]:.2f}", f"{ln[1]:.2f}") if ln else ("", "")),
                             f"{s['energy'][0]:.5f}", f"{o['wear']:.5f}", f"{s['primary'][0]:.5f}", f"{o['writes']:.1f}",
                             f"{o['native_viol_share']:.4f}", o["valid"],
                             *((r["solo"]["label"], o["solo"]["label"], f"{o['solo']['summary']['work'][0]:.5f}",
                                f"{o['solo']['summary']['viol_pp'][0]:.3f}", f"{o['solo']['summary']['energy'][0]:.5f}",
                                o["solo"]["vs_omni"]["label"]) if r.get("solo") and o.get("solo")
                               else ("the same arm", "", "", "", "", ""))])
    (out / "REALMS_V5.json").write_text(json.dumps({"run": run, "organisms": orgs, "muscles": res}, indent=1) + "\n")
    (out / "RUN.json").write_text(json.dumps(run, indent=1) + "\n")
    write_md(out, res, orgs, run)
    files = sorted(p for p in out.iterdir() if p.is_file() and p.name != "SHA256SUMS.txt")
    (out / "SHA256SUMS.txt").write_text("".join(f"{sha(p)}  {p.name}\n" for p in files))
    print((out / "REALMS_V5.md").read_text().split("## Inside the organisms")[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
