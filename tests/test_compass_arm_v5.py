# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Tests for the Omni v5 law (realms/compass_arm_v5.py), the engine change that makes this tree omni-v5.

The default is the max (V5CFG): for EVERY muscle alone in the catalog, on a development seed, the omni arm does no less
work than native and is over its line no more often, hands every knob back to native before the run ends (the lease),
and acts somewhere; its energy may rise (power given). Inside an organism the bone grants the max only the power the body
can carry, and a pool never has fewer machines than its twin. The tune-down (V5SAVE, the dial turned to save) keeps its
own promise: no more energy than native, no less work, no more time over the line, on every muscle. Run directly or under
pytest. The preregistered seeds 3000-3009 are never used here.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import realms.harness as H                                   # noqa: E402
import realms.compass_arm_v5 as L                            # noqa: E402

SEED = 7100
ETOL = 1e-6          # energy may not exceed native beyond rounding (the tune-down)
WTOL = 1e-4          # work may not fall below native beyond rounding
CAT = str(ROOT / "realms" / "catalog_v5.csv")


def _harms(row, arm, load=None):
    nat = H.run_muscle_arm(row, SEED, "native", load)
    got = H.run_muscle_arm(row, SEED, arm, load)
    harms = []
    if arm == "v5save" and got["energy_j"] > nat["energy_j"] * (1 + ETOL) + 1e-9:
        harms.append(f"energy +{got['energy_j'] / nat['energy_j'] - 1:.4%}")
    if nat["work"] > 0 and got["work"] < nat["work"] * (1 - WTOL) - 1e-9:
        harms.append(f"work {got['work'] / nat['work'] - 1:.4%}")
    if got["viol"] > nat["viol"]:
        harms.append(f"over the line {got['viol'] - nat['viol']:+d}")
    if not got["restore_ok"]:
        harms.append("not handed back by the lease")
    if "line_k" in nat and got["line_k"] > nat["line_k"]:
        harms.append(f"the line cleared later ({nat['line_k']} -> {got['line_k']})")
    return harms, got["writes"]


def _all_muscles(arm, load=None, templates=None):
    bad, acted = [], 0
    for row in H.catalog(CAT):
        if templates and row["template"] not in templates:
            continue
        harms, writes = _harms(row, arm, load)
        acted += int(writes > 0)
        if harms:
            bad.append(f"{row['muscle_id']} {row['family']}/{row['muscle']} ({row['knob']}): {', '.join(harms)}")
    return bad, acted


def test_max_does_no_harm_to_any_muscle_alone():
    bad, acted = _all_muscles("v5")
    assert not bad, "the max harmed muscles vs native:\n" + "\n".join(bad[:30])
    assert acted > 0, "the max never acted on any muscle (silent no-op)"


def test_max_does_no_harm_with_work_waiting_in_line():
    # every plant with a line (pools, axes, battery sites) starts with the same work waiting in both arms: the max does
    # no less work, is over its line no more often and clears the line no later than native, and it clears some sooner
    bad, acted = _all_muscles("v5", "line", ("compute_pool", "motion_axis", "energy_storage"))
    assert not bad, "the max harmed muscles with work waiting in line:\n" + "\n".join(bad[:30])
    rows = {r["muscle_id"]: r for r in H.catalog(CAT)}
    nat = H.run_muscle_arm(rows["161"], SEED, "native", "line")      # an inference pool's replicas
    mx = H.run_muscle_arm(rows["161"], SEED, "v5", "line")
    assert mx["line_k"] < nat["line_k"] and mx["line_left"] == 0.0, "the max clears an inference pool's line sooner"


def test_axis_peak_only_where_the_machine_has_one_and_handed_back():
    rows = {r["muscle_id"]: r for r in H.catalog(CAT)}
    joint = H.scale_load_plant(H.make_plant(rows["433"], SEED), "line")   # a robot joint: a drive peak above its profile
    assert L.max_apply(joint, "capacity", L.V5CFG) == {"capacity": joint.P["s_peak"]}
    wheel = H.scale_load_plant(H.make_plant(rows["497"], SEED), "line")   # a reaction wheel: its limit is its setting
    assert L.max_apply(wheel, "capacity", L.V5CFG) == {}
    got = H.run_muscle_arm(rows["433"], SEED, "v5", "line")
    assert got["writes"] > 0 and got["restore_ok"], "the joint's peak is used and handed back by the lease"
    assert L.native_at_limit("motion_axis", "power") and not L.native_at_limit("compute_pool", "capacity")


def test_guard_floor_let_go_at_once_at_the_kill():
    rows = {r["muscle_id"]: r for r in H.catalog(CAT)}
    pool = H.make_plant(rows["161"], SEED)
    pool.override, pool._mx_guard = {"floor": 9.0}, True                # held only at the twin's count
    assert H.walk_back(pool, H.WALK) == {}
    pool.override, pool._mx_guard = {"floor": 9.0}, False               # machines the max added walk back
    assert 0 < H.walk_back(pool, H.WALK)["floor"] < 9.0


def test_save_dial_does_no_harm_to_any_muscle_alone():
    bad, acted = _all_muscles("v5save")
    assert not bad, "the tune-down harmed muscles vs native:\n" + "\n".join(bad[:30])
    assert acted > 0


def test_max_is_the_default_and_never_shaves():
    assert L.V5CFG.dial == "max", "the engine's default brain is the max"
    assert L.V5SAVE.dial == "save"
    # a muscle native already runs flat out asks the max for nothing
    rows = {r["muscle_id"]: r for r in H.catalog(CAT)}
    loop = H.make_plant(rows["2121"], SEED)                  # a generating unit's steam pressure: full actuator natively
    assert L.max_ask(loop, "setpoint", L.V5CFG) is None
    assert L.max_apply(loop, "setpoint", L.V5CFG) == {}


def test_bone_never_leaves_a_pool_below_its_twin():
    # inside an organism, every pool the max holds has at least the machines its twin (native) runs, every decision
    rows = [r for r in H.catalog(CAT) if "compute_ai_cloud" in r["realms"].split(";")]
    b = H.scale_load(H.Body(rows, SEED), "climb")
    bone = L.Bone(b, L.V5CFG)
    kill = int(H.KILL_AT * H.ORGANISM_STEPS)
    for k in range(kill):
        b.couple()
        bone.advance_twin()
        L.max_body_step(b, L.V5CFG, bone)
        b.step()
        for i, tw in bone.twins.items():
            p = b.plants[i]
            assert L.machines(p) >= min(L.machines(tw), p.P["n_max"]), f"pool {rows[i]['muscle_id']} below its twin at {k}"


def test_tower_max_does_no_less_work_and_hands_back():
    rows = H.catalog(CAT)
    nat = H.run_organism_arm(rows, SEED, "native")
    mx = H.run_organism_arm(rows, SEED, "v5")
    assert sum(p["work"] for p in mx["plants"]) >= sum(p["work"] for p in nat["plants"]) * (1 - WTOL), "tower work below native"
    assert mx["restore_ok"], "the tower's knobs were not all handed back by the lease"


def test_walk_back_is_gradual_and_complete():
    rows = {r["muscle_id"]: r for r in H.catalog(CAT)}
    zone = H.make_plant(rows["547"], SEED)                   # a data hall's setpoint
    zone.override = {"setpoint": zone.P["t_set"] - 2.0}
    seen = []
    for left in range(H.WALK, 0, -1):
        H.walk_back(zone, left)
        seen.append(zone.override.get("setpoint", zone.P["t_set"]))
    assert seen[0] < zone.P["t_set"] and seen[-1] == zone.P["t_set"] and zone.override == {}
    assert all(b >= a - 1e-12 for a, b in zip(seen, seen[1:])), "the walk back moves one way, toward native"



def test_room_twins_equal_native_when_the_max_writes_nothing():
    # V8's sense: with every knob left at native, each room's twin is the room itself, to the last digit, every decision
    # (the twin starts from the body's own reading of its sources, nominal before the first step)
    rows = [r for r in H.catalog(CAT) if "physics_robotics_autonomous" in r["realms"].split(";")]
    for load in ("climb", "line"):
        b = H.scale_load(H.Body(rows, SEED), load)
        bone = L.Bone(b, L.V5CFG)
        assert bone.room_twins, "every room has a twin"
        for k in range(12):
            b.couple()
            bone.advance_twin()
            for p in b.plants:
                p.override = {}
            b.step()
            for i, tw in bone.room_twins.items():
                assert b.plants[i].T == tw.T and b.plants[i].power_w == tw.power_w, f"room {rows[i]['muscle_id']} at {k}"


def test_battery_forecast_starts_at_its_first_reading():
    # V13: the jump from a plant's initial values to its first reading is no climb of its line (it once locked every
    # battery's timed discharge for the whole run)
    rows = {r["muscle_id"]: r for r in H.catalog(CAT)}
    site = H.make_plant(rows["530"], SEED)                   # a rack's power cap on a UPS
    for _ in range(3):
        L.max_hold(site, L.V5CFG, "power")
        site.step()
    st = site._mx_s
    assert st["rise"] < 0.5 * site.P["p_lim_w"], "the first reading was taken as a climb of the line"


def test_battery_holds_only_after_reading_its_line():
    # V12: a battery wired by its power holds nothing until it has read its line for a window, then holds only while the
    # line has room
    rows = {r["muscle_id"]: r for r in H.catalog(CAT)}
    site = H.make_plant(rows["530"], SEED)
    for k in range(L.V5CFG.window + 2):
        ov = L.max_hold(site, L.V5CFG, "power")
        if k <= L.V5CFG.window:
            assert ov == {}, f"held at decision {k}, before the line was read for a window"
        site.override = ov
        site.step()


def test_heat_debt_only_for_rooms_that_cannot_cure_themselves():
    # V11: a room wired by its setpoint, its cooling not flat out, cures itself (no debt); the same room wired by a power
    # gate, warmer than its twin, puts a debt on the body
    rows = [r for r in H.catalog(CAT) if "energy_facility_industrial" in r["realms"].split(";")]
    b = H.scale_load(H.Body(rows, SEED), "climb")
    bone = L.Bone(b, L.V5CFG)
    b.couple()
    bone.advance_twin()
    i, tw = next((i, tw) for i, tw in bone.room_twins.items() if b.knobs[i] == "setpoint")
    tw.T_read = b.plants[i].T - 0.5                         # the room reads half a degree warmer than native's
    z = b.plants[i]
    assert z.qc_cmd_avg < z.units_on * z.P["q_unit_w"], "the room's cooling has room to cool it"
    assert L.heat_debt(b, bone) == 0.0, "a room that can cure itself put a debt on the body"
    b.knobs[i] = "power"
    assert L.heat_debt(b, bone) > 0.0, "a room that cannot cure itself puts no debt on the body"


def _first(template, knob):
    return next(r for r in H.catalog(CAT) if r["template"] == template and r["knob"] == knob)


def test_without_a_card_a_muscle_runs_the_global_setting():
    # the global setting is the one the engine had before cards: a battery reads its line for the window and keeps a
    # twentieth of it clear; an axis is pushed under 80% of its heat rise and half its tracking line
    g = L.V5CFG
    assert g.hold_window is None and g.hold_margin == 0.05 and g.heat_head == L.HEAT_HEAD and g.strain == L.STRAIN
    p = H.make_plant(_first("compute_pool", "capacity"), SEED)
    p._card = None
    assert L.card(p, g) is g and L.body_card(p, g, "capacity") is g


def test_a_card_is_the_muscles_own_and_the_tune_down_never_reads_it():
    p = H.make_plant(_first("compute_pool", "capacity"), SEED)
    p._card = {"edge_util": 0.8, "window": 40}
    c = L.card(p, L.V5CFG)
    assert (c.edge_util, c.window) == (0.8, 40) and c.line_z == L.V5CFG.line_z, "the card over the brain's own settings"
    assert L.card(p, L.V5CFG) is c, "the same card every decision"
    assert L.card(p, L.V5SAVE) is L.V5SAVE, "the tune-down read a card"
    for _ in range(30):
        p.step()
    assert L.max_pool_want(p, c) >= L.max_pool_want(p, L.V5CFG), "a slimmer edge asked for fewer machines"


def test_a_battery_wired_by_its_power_keeps_the_bodys_margins_inside_a_body():
    p = H.make_plant(_first("energy_storage", "power"), SEED)
    p._card = {"line_z": 1.0, "hold_window": 5, "hold_margin": 0.0}
    b = L.body_card(p, L.V5CFG, "power")
    assert b.line_z == L.V5CFG.line_z and b.hold_margin == L.V5CFG.hold_margin, "slimmer than the body on its line"
    assert b.hold_window == 5, "its own window"
    alone = L.card(p, L.V5CFG)
    assert alone.line_z == 1.0 and alone.hold_margin == 0.0, "alone, a battery runs its own card"
    q = H.make_plant(_first("energy_storage", "capacity"), SEED)
    q._card = {"line_z": 1.0}
    assert L.body_card(q, L.V5CFG, "capacity").line_z == 1.0, "only a battery wired by its power is held to the body"


def test_every_card_names_a_muscle_of_the_catalog_within_its_searched_range():
    from tools import tune_cards as T
    rows = {r["muscle_id"]: r for r in H.catalog(CAT)}
    import csv
    cards = []
    if L.CARD_FILE.exists():
        with open(L.CARD_FILE, newline="") as f:
            cards = list(csv.DictReader(f))
    for c in cards:
        r = rows[c["muscle_id"]]
        assert (c["template"], c["knob"]) == (r["template"], r["knob"]), c["muscle_id"]
        own = {k: L.CARD_KEYS[k](v) for k, v in c.items() if k in L.CARD_KEYS and v.strip()}
        assert own in T.candidates(r, wide=True), f"{c['muscle_id']}: a card outside the searched settings"
        assert L.CARDS[c["muscle_id"]] == own, "the engine reads the file as written"


if __name__ == "__main__":
    test_max_does_no_harm_to_any_muscle_alone()
    test_max_does_no_harm_with_work_waiting_in_line()
    test_axis_peak_only_where_the_machine_has_one_and_handed_back()
    test_guard_floor_let_go_at_once_at_the_kill()
    test_save_dial_does_no_harm_to_any_muscle_alone()
    test_max_is_the_default_and_never_shaves()
    test_bone_never_leaves_a_pool_below_its_twin()
    test_tower_max_does_no_less_work_and_hands_back()
    test_walk_back_is_gradual_and_complete()
    test_room_twins_equal_native_when_the_max_writes_nothing()
    test_battery_forecast_starts_at_its_first_reading()
    test_battery_holds_only_after_reading_its_line()
    test_heat_debt_only_for_rooms_that_cannot_cure_themselves()
    test_without_a_card_a_muscle_runs_the_global_setting()
    test_a_card_is_the_muscles_own_and_the_tune_down_never_reads_it()
    test_a_battery_wired_by_its_power_keeps_the_bodys_margins_inside_a_body()
    test_every_card_names_a_muscle_of_the_catalog_within_its_searched_range()
    print("test_compass_arm_v5: OK")
