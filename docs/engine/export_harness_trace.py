# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Records the realms harness, decision by decision, as an organism and muscle by muscle alone, for the live benchmark engine page (docs/engine/OMNI_COMPASS_LIVE_ENGINE.html).

The sixty muscles the page draws (twelve from the spine, twelve from each realm, named in MUSCLES below) are put in one
organism of the realms harness (realms/harness.py Body: the plants of realms/plants.py, coupled through their heat and
their power) under the climb, on seeds 3000, 3001 and 3002 (runs A, B and C). Two arms on each seed, the same demand:

  native  the plants and their native controllers alone
  omni    Omni-Compass on top: the max (realms/compass_arm_v5.py max_body_step with the body's Bone, its twins and the
          muscles' cards), exactly as run_bodies runs the arm v5; at 80% of the run the brain goes silent and the lease
          walks every setting back to native over 24 decisions (KILL_AT, WALK)

Every decision it records, for each plant: the service position the law reads (v5_position: 1 or more is past the
line), whether the decision was over the line, whether Omni-Compass held a setting away from native and whether it
wrote one, and whether the plant's own native controller changed what it commands (own_cmd: in both arms, so native's
side has its own moves to show beside Omni-Compass's writes); for the body: its electrical power and the harness's aggregate observation (what a governor would read).
The work each plant did is recorded per decision so the page can show work against native's. Omni-Compass's organism
also records its immune system, read as max_body_step reads it, never stepping it again (realms/compass_arm_v5.py, V6
to V13): every room against its twin (the same room under its operator's settings and native's heat), the rooms that
stand warmer than their twins (inflamed), the body's heat debt (the signal that makes the other muscles give back),
whether the body gave back (no room on the bone's lines, or a heat debt), and the machines held over the pools' twins.

The three-run readings: for each gauge, the paired change per decision, averaged over blocks of ten decisions, with its
95% interval (Student's t over the blocks), in each run; read by the one rule (tools/readings.py three_run_reading, the
founder's order of 24 October 2026): the mean of the three runs' changes, under 0.5% STEADY, from 0.5% up the word by the gauge's
aim; "the runs disagree" when runs that moved 0.5% or more point different ways. Evidence class S. Usage: python3 docs/engine/export_harness_trace.py OUT.json
"""
from __future__ import annotations

import json
import math
import statistics as st
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from realms.harness import (Body, KILL_AT, WALK, aggregate, catalog, make_plant, scale_load, scale_load_plant,  # noqa: E402
                            walk_back)
from realms.compass_arm_v5 import Bone, V5CFG, heat_debt, machines, max_apply, max_body_step, v5_position   # noqa: E402
from realms.presets import ORGANISM_STEPS                                                     # noqa: E402

SEEDS = (3000, 3001, 3002)
MUSCLES = {
    "spine": ["pump_speed", "pdb_policy", "unhealthy_pod_eviction_policy", "memory_high", "cpu_idle_policy", "node_selector",
              "generator_dispatch", "cpu_quota", "ear_cpu_frequency_policy", "expire_after", "memory_limit", "transparent_hugepages"],
    "compute": ["model_replicas", "tls_session_cache", "edge_dispatch", "qubit_mapping", "global_admission", "retry_budget_window",
                "training_precision", "task_preemption", "machine_remediation", "compute_comm_overlap", "memory_ballooning", "checkpoint_trigger"],
    "physics": ["altitude_target", "velocity_target", "force_limit", "px4_mpc_xy_vel_max", "amr_fleet_active_robots", "regen_drive_mode",
                "smart_charging_schedule", "ros2_executor_threads", "motor_thermal_derate", "timetable_recovery_margin", "horizontal_speed_limit", "space_power_budget"],
    "energy": ["chromatography_flow_setpoint", "boiler_steam_pressure_setpoint", "inverter_real_power", "storage_dispatch", "flotation_aeration_rate",
               "mill_speed_target", "heat_pump_staging", "feeder_voltage_target", "controller_mode", "energy_load_shed",
               "heater_outlet_temperature_setpoint", "reserve_dispatch_priority"],
    "distribution": ["lock_timeout", "cache_compression", "dispatch_priority", "shuffle_bandwidth", "broker_failover", "service_timeout",
                     "stage_parallelism", "inventory_allocation", "executor_size", "compensation_action", "gc_budget", "shipment_batch"],
}
from omnicompass.student_t import t95 as _t95    # noqa: E402  (the exact two-sided 95% point of Student's t, omni-v9)


def t95(df):
    """The two-sided 95% quantile of Student's t for df degrees of freedom (omnicompass/student_t.py, exact)."""
    return _t95(df)


def own_cmd(p, st):
    """What a plant's own native controller commands now, read the same way in both arms (st: the plant's own memory): a
    pool's machines in service and starting (its autoscaler), a room's cooling units staged (its staging), a battery's
    dispatch, charging, holding or discharging (read from its charge's change over the decision), an axis's move under
    way (its next task dispatched), a loop's actuator, counted each time it has moved 2% of its range since the last count
    (its PI controller). A change from the previous decision is one move of the native controller."""
    t = p.template
    if t == "compute_pool":
        return machines(p)
    if t == "thermal_zone":
        return p.units_on
    if t == "energy_storage":
        d = p.soc - st.get("soc", p.soc); st["soc"] = p.soc
        return 1 if d > 1e-9 else -1 if d < -1e-9 else 0
    if t == "motion_axis":
        return None if p.move is None else (round(p.move["start"], 6), p.move["sgn"])
    if t == "process_loop":
        ref = st.setdefault("u", p.u_avg)
        if abs(p.u_avg - ref) >= 0.02 * p.P["u_max"]:
            st["u"] = ref = p.u_avg
        return round(ref, 9)
    return None


def rows():
    by = {r["muscle"]: r for r in catalog(ROOT / "realms" / "catalog_v5.csv")}
    out = []
    for part, names in MUSCLES.items():
        for n in names:
            r = dict(by[n]); r["part"] = part; out.append(r)
    return out


def run(rs, seed, arm):
    b = Body(rs, seed)
    scale_load(b, "climb")
    n, kill_at = len(b.plants), int(KILL_AT * ORGANISM_STEPS)
    bone = Bone(b, V5CFG) if arm == "omni" else None
    last = [None] * n
    rec = {"p": [], "over": [], "held": [], "wrote": [], "work": [], "power_kw": [], "obs": [], "imm": [], "mach": [], "troom": [], "own": []}
    own_st = [{} for _ in b.plants]
    own_last = [own_cmd(p, s0) for p, s0 in zip(b.plants, own_st)]
    # each side's own pools and rooms, read the way the bone reads them: the machines in service and starting over every compute
    # pool, and the warmest room; native's are its own controllers', Omni-Compass's carry what it added and gave back
    pools = [i for i, (p, r) in enumerate(zip(b.plants, b.rows)) if p.template == "compute_pool" and r["knob"] not in ("power", "admission")]
    rooms = [i for i, p in enumerate(b.plants) if p.template == "thermal_zone"]
    if bone is not None:                     # the bone's own reading of its lines, kept as max_body_step reads it (no extra call)
        seen = {}
        cls_room = bone.room
        def room():
            r = cls_room(); seen["room"] = r; return r
        bone.room = room
    prev_viol, prev_work = [0] * n, [0.0] * n
    for k in range(ORGANISM_STEPS):
        b.couple()
        wrote = [0] * n
        if arm == "omni":
            if k >= kill_at:
                for p in b.plants:
                    walk_back(p, kill_at + WALK - k)
            else:
                bone.advance_twin()
                # the immune system's reading before the step (read only): every room against its twin, the body's heat debt
                inflamed = [(i, b.plants[i].T - getattr(tw, "T_read", tw.T)) for i, tw in bone.room_twins.items()]
                inflamed = [(i, e) for i, e in inflamed if e > 1e-9]
                debt = heat_debt(b, bone)
                seen.clear()
                max_body_step(b, V5CFG, bone)
                r_src, r_all = seen.get("room", (0.0, 0.0))
                extra = sum(max(0, machines(b.plants[i]) - machines(tw)) for i, tw in bone.twins.items())
                worst = max(inflamed, key=lambda x: x[1]) if inflamed else (-1, 0.0)
                rec["imm"].append([round(debt, 3), len(inflamed), worst[0], float(f"{worst[1]:.3g}"),
                                   1 if (r_src < 0.0 or r_all < 0.0 or debt > 0.0) else 0, extra])
                for i, p in enumerate(b.plants):
                    v = p.override
                    if v and v != last[i]:
                        wrote[i] = 1
                    last[i] = dict(v)
        b.step()
        ps, ov, wk = [], [], []
        for i, p in enumerate(b.plants):
            ps.append(round(min(2.0, max(-0.5, v5_position(p))), 3))
            ov.append(p.m["viol"] - prev_viol[i]); prev_viol[i] = p.m["viol"]
            wk.append(p.m["work"] - prev_work[i]); prev_work[i] = p.m["work"]
        o = aggregate([b])
        rec["p"].append(ps); rec["over"].append(ov); rec["wrote"].append(wrote)
        rec["held"].append([1 if p.override else 0 for p in b.plants]); rec["work"].append(wk)
        own = []
        for i, p in enumerate(b.plants):
            c = own_cmd(p, own_st[i]); own.append(int(c != own_last[i])); own_last[i] = c
        rec["own"].append(own)
        rec["power_kw"].append(round(b.all_w / 1000.0, 3))
        rec["mach"].append(sum(machines(b.plants[i]) for i in pools))
        rec["troom"].append(round(max((b.plants[i].T for i in rooms), default=0.0), 3))
        rec["obs"].append({k2: round(o[k2], 4) for k2 in ("queue_ratio", "load_ratio", "power_stress", "thermal",
                                                         "network_stress", "drift_ratio")})
    return rec


FRAMES = 240          # each muscle alone is drawn on the organism's 240 frames (a frame: the last decision it covers,
                      # over the line if any decision it covers was)


def run_alone(row, seed, arm, load="line"):
    """One muscle alone, as realms/harness.py run_muscle_arm runs it (native, or the max with its twin; the lease's walk
    back after 80%), under the line load of the preregistered muscle table; recorded per decision."""
    plant = make_plant(row, seed)
    scale_load_plant(plant, load)
    knob, steps = row["knob"], plant.steps
    kill_at = int(KILL_AT * steps)
    twin = None
    if arm == "omni":
        twin = make_plant(row, seed)
        scale_load_plant(twin, load)
    last, rec, pv, pw = None, {"p": [], "over": [], "held": [], "wrote": [], "work": [], "power": [], "obs": [], "own": []}, 0, 0.0
    own_st = {}
    own_last = own_cmd(plant, own_st)
    for k in range(steps):
        wrote = 0
        if arm == "omni":
            if k < kill_at:
                twin.step()
                v = max_apply(plant, knob, V5CFG, twin)
                wrote = int(bool(v) and v != last)
            else:
                v = walk_back(plant, kill_at + WALK - k)
            last = v
        plant.step()
        rec["p"].append(min(2.0, max(-0.5, v5_position(plant)))); rec["over"].append(plant.m["viol"] - pv); pv = plant.m["viol"]
        rec["held"].append(1 if plant.override else 0); rec["wrote"].append(wrote)
        rec["work"].append(plant.m["work"] - pw); pw = plant.m["work"]; rec["power"].append(plant.power_w)
        c = own_cmd(plant, own_st); rec["own"].append(int(c != own_last)); own_last = c
        rec["obs"].append(plant.observe())
    line_k = getattr(plant, "line_k", None)
    return rec, steps, (line_k if line_k is not None else steps) if getattr(plant, "line_n", 0) or getattr(plant, "line_e", 0.0) or getattr(plant, "line0", 0.0) else None


def frames(rec, steps):
    """A muscle's own decisions onto the 240 frames."""
    out = {"p": [], "over": [], "held": [], "wrote": [], "work": [], "power": [], "obs": [], "own": []}
    for f in range(FRAMES):
        a, b = f * steps // FRAMES, max(f * steps // FRAMES + 1, (f + 1) * steps // FRAMES)
        out["p"].append(rec["p"][b - 1]); out["over"].append(int(any(rec["over"][a:b]))); out["held"].append(rec["held"][b - 1])
        out["wrote"].append(int(any(rec["wrote"][a:b]))); out["work"].append(sum(rec["work"][a:b])); out["power"].append(sum(rec["power"][a:b]) / (b - a))
        out["obs"].append(rec["obs"][b - 1]); out["own"].append(int(any(rec["own"][a:b])))
    return out


def alone_body(rs, seed, arm):
    """Sixty muscles each alone, laid side by side on the 240 frames, in the organism record's shape."""
    per, lines = [], []
    for r in rs:
        rec, steps, lk = run_alone(r, seed, arm)
        per.append(frames(rec, steps)); lines.append(None if lk is None else lk / steps)
    T = lambda key: [[per[i][key][f] for i in range(len(rs))] for f in range(FRAMES)]
    out = {"p": T("p"), "over": T("over"), "held": T("held"), "wrote": T("wrote"), "work": T("work"), "own": T("own"),
           "power_kw": [round(sum(per[i]["power"][f] for i in range(len(rs))) / 1000.0, 4) for f in range(FRAMES)],
           # what a governor would read of the sixty muscles: the mean of their own observations (realms/harness.py
           # aggregate), each muscle's power stress against its own budget
           "obs": [{k: sum(per[i]["obs"][f][k] for i in range(len(rs))) / len(rs) for k in
                    ("queue_ratio", "load_ratio", "power_stress", "thermal", "network_stress", "drift_ratio")} for f in range(FRAMES)],
           "line": lines}
    return out


def blocks(xs, size=10):
    return [sum(xs[i:i + size]) / size for i in range(0, len(xs) - size + 1, size)]


def interval(d):
    b = blocks(d)
    m = st.mean(b)
    half = t95(len(b) - 1) * st.stdev(b) / math.sqrt(len(b))
    return m, m - half, m + half


def gauges(nat, omn):
    """The per-decision gauges, native and omni, for one seed."""
    steps, n = len(nat["p"]), len(nat["p"][0])
    tot_nat = [max(sum(nat["work"][k][i] for k in range(steps)), 1e-12) for i in range(n)]
    def work(rec):
        return [sum(rec["work"][k][i] / (tot_nat[i] / steps) for i in range(n)) / n for k in range(steps)]
    return {
        "work": (work(nat), work(omn), "up"),
        "over": ([sum(x) for x in nat["over"]], [sum(x) for x in omn["over"]], "down"),
        "spread": ([st.pstdev([min(p, 1.5) for p in x]) for x in nat["p"]], [st.pstdev([min(p, 1.5) for p in x]) for x in omn["p"]], "shown"),
        "power": (nat["power_kw"], omn["power_kw"], "spent"),
    }


def reading(per_run, aim):
    """The one three-run rule (tools/readings.py three_run_reading, the founder's order of 24 October 2026) on the per-run
    changes [(change, lo, hi)], each relative to native: the mean of the three changes; under 0.5% STEADY; from 0.5% up the word
    by the gauge's aim; runs that moved 0.5% or more in opposite directions disagree."""
    from tools.readings import SIZE_FLOOR, HIGHER, LOWER, SPENT, word
    if aim == "shown":
        return "shown"          # a gauge no rule of the engine aims at: its change is shown, never judged
    ch = [m for m, _, _ in per_run]
    if len({m > 0 for m in ch if abs(m) >= SIZE_FLOOR}) > 1:
        return "the runs disagree"
    mean = sum(ch) / len(ch)
    if abs(mean) < SIZE_FLOOR:
        return "STEADY"
    return word(mean < 0, {"up": HIGHER, "down": LOWER, "spent": SPENT}.get(aim, LOWER))


def pack(rec, n):
    """The page's compact form: positions as int16 thousandths and four flags a byte (1 over the line, 2 a setting held
    away from native, 4 a write, 8 the plant's own native controller moved), each base64; the body's power, the aggregate
    observation, and the work index."""
    import base64, array
    pos = array.array("h", [int(round(max(-0.5, min(2.0, x)) * 1000)) for row in rec["p"] for x in row])
    own = rec.get("own") or [[0] * len(r) for r in rec["over"]]
    fl = bytes((1 if o else 0) | (2 if h else 0) | (4 if w else 0) | (8 if m else 0)
               for ro, rh, rw, rm in zip(rec["over"], rec["held"], rec["wrote"], own) for o, h, w, m in zip(ro, rh, rw, rm))
    return {"p": base64.b64encode(pos.tobytes()).decode(), "f": base64.b64encode(fl).decode(), "kw": rec["power_kw"],
            "obs": [[o["queue_ratio"], o["load_ratio"], o["power_stress"], o["thermal"], o["network_stress"], o["drift_ratio"]]
                    for o in rec["obs"]], **({"imm": rec["imm"]} if rec.get("imm") else {}),
            **({"mach": rec["mach"], "troom": rec["troom"]} if rec.get("mach") else {})}


def section(rs, runner, steps, kill_at):
    sec = {"steps": steps, "kill_at": kill_at, "walk": WALK, "seeds": list(SEEDS), "runs": {}, "readings": {}}
    per = {}
    for sd in SEEDS:
        nat, omn = runner(rs, sd, "native"), runner(rs, sd, "omni")
        g = gauges(nat, omn)
        if "line" in nat:            # each muscle alone: the share of its run each arm took to clear its line
            pairs = [(x, y) for x, y in zip(nat["line"], omn["line"]) if x is not None and y is not None]
            g["line"] = ([x for x, _ in pairs], [y for _, y in pairs], "down")
        pn, po = pack(nat, len(rs)), pack(omn, len(rs))
        pn["wk"], po["wk"] = [round(x, 6) for x in g["work"][0]], [round(x, 6) for x in g["work"][1]]
        if "line" in nat:
            pn["line"], po["line"] = nat["line"], omn["line"]
        sec["runs"][str(sd)] = {"native": pn, "omni": po}
        for key, (x, y, aim) in g.items():
            d = [b2 - a2 for a2, b2 in zip(x, y)]
            if key == "line":            # paired over the muscles that hold a line, not over blocks of decisions
                m = st.mean(d); half = t95(len(d) - 1) * st.stdev(d) / math.sqrt(len(d)); lo, hi = m - half, m + half
            else:
                m, lo, hi = interval(d)
            base = st.mean(x) or 1e-12
            per.setdefault(key, {"aim": aim, "runs": []})["runs"].append(
                {"seed": sd, "native": st.mean(x), "omni": st.mean(y), "change": m / base, "lo": lo / base, "hi": hi / base})
    for key, v in per.items():
        v["reading"] = reading([(r["change"], r["lo"], r["hi"]) for r in v["runs"]], v["aim"])
        print(f"  {key:7s} {v['reading']:18s} " + "  ".join(f"{r['change']*100:+.4f}% [{r['lo']*100:+.4f}, {r['hi']*100:+.4f}]" for r in v["runs"]))
    sec["readings"] = per
    return sec


def prereg_labels(names):
    """Each muscle's own reading in the engine's preregistered realms table (results/realms_v5/MUSCLES_V5.csv)."""
    import csv
    import io, subprocess
    path = ROOT / "results" / "realms_v5" / "MUSCLES_V5.csv"
    text = path.read_text(encoding="utf-8") if path.exists() else subprocess.run(
        ["git", "show", "HEAD:results/realms_v5/MUSCLES_V5.csv"], cwd=ROOT, capture_output=True, text=True).stdout
    out = {}
    if text:
        for r in csv.DictReader(io.StringIO(text)):
            if r["muscle"] in names:
                out.setdefault(r["muscle"], {})[r["load"]] = r["label"]
                out[r["muscle"]]["all"] = r["label_all_loads"]
    return out


def main(out):
    rs = rows()
    data = {"muscles": [{"name": r["muscle"], "family": r["family"], "part": r["part"], "template": r["template"],
                         "knob": r["knob"], "id": r["muscle_id"]} for r in rs],
            "prereg": prereg_labels({r["muscle"] for r in rs})}
    print("the organism (the climb):")
    data["organism"] = section(rs, run, ORGANISM_STEPS, int(KILL_AT * ORGANISM_STEPS))
    print("each muscle alone (the line):")
    data["alone"] = section(rs, alone_body, FRAMES, int(KILL_AT * FRAMES))
    Path(out).write_text(json.dumps(data, separators=(",", ":")), encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "harness_trace.json")
