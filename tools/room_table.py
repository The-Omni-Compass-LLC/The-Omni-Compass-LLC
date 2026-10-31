# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The room table (docs/THE_ROOM.md, section 5.1): for every family of the catalog, the band of its knob, native's point in
it, the room above and below, where the wall comes from (the design, movable by a muscle of our own; or the physics, not
movable by any muscle), and what the realms result read on the family's muscles by the one key.

Everything comes from files that exist: the catalog (realms/catalog_v5.csv), each muscle's preset as the realms runner
builds it (realms/presets.params_for), the at-limit rule the runner applies (realms/compass_arm_v5.native_at_limit) and the
realms result on the engine that stands (results/realms_v5/MUSCLES_V5.csv). Nothing is typed by hand but the wall's kind
for each template and knob (WALL below), which is a statement about the machine, not a measurement.

  python3 tools/room_table.py            writes docs/THE_ROOM_TABLE.md
  python3 tools/room_table.py --check    exit 1 if the page differs from what the files give
"""
from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from realms.compass_arm_v5 import native_at_limit  # noqa: E402
from realms.presets import params_for  # noqa: E402
from tools.legal import stamp  # noqa: E402

CATALOG = ROOT / "realms" / "catalog_v5.csv"
RESULT = ROOT / "results" / "realms_v5" / "MUSCLES_V5.csv"
PAGE = ROOT / "docs" / "THE_ROOM_TABLE.md"

# where the wall of each knob comes from: the design (a vendor's default, an operator's cap, a protocol's rule: a muscle of
# our own can move it) or the physics (a machine's own limit: no muscle moves it)
WALL = {
    ("compute_pool", "capacity"): ("the operator's cap on machines or replicas (n_max)", "design"),
    ("compute_pool", "power"): ("the machine's power ceiling; native runs it at full", "physics"),
    ("compute_pool", "admission"): ("the gate is open on native; nothing is paced or turned away", "design"),
    ("compute_pool", "setpoint"): ("the autoscaler's own target (busy share) the operator set", "design"),
    ("thermal_zone", "setpoint"): ("the zone's band from its cold end to its warm end, set by the operator", "design"),
    ("thermal_zone", "power"): ("the cooling plant's power share; native runs it at full", "physics"),
    ("energy_storage", "setpoint"): ("the reserve the store holds back, between its stress and calm ends", "design"),
    ("energy_storage", "power"): ("the battery's power rating; native runs it at full", "physics"),
    ("motion_axis", "capacity"): ("the axis's peak speed is the machine's own; native's everyday setting is the limit where no peak lies above it", "physics"),
    ("motion_axis", "power"): ("the drive's torque or power limit at full on native", "physics"),
    ("process_loop", "setpoint"): ("the loop's band, half a band each side of the middle", "design"),
    ("process_loop", "capacity"): ("the actuator's full range; native already has it", "physics"),
    ("process_loop", "power"): ("the drive's power at full on native", "physics"),
}


def band(template: str, knob: str, P: dict):
    """(lo, hi, native, unit) of a muscle's knob from its preset, or None where the knob has no band (at its limit)."""
    if knob == "capacity" and template == "compute_pool":
        return float(P["n_min"]), float(P["n_max"]), float(P["n0"]), "machines"
    if knob == "setpoint" and template == "thermal_zone":
        return float(P["stress"]), float(P["calm"]), float(P["t_set"]), "°C"
    if knob == "setpoint" and template == "energy_storage":
        return float(P["stress"]), float(P["calm"]), float(P["reserve"]), "share of charge"
    if knob == "setpoint" and template == "process_loop":
        return float(P["mid"]) - float(P["half"]), float(P["mid"]) + float(P["half"]), float(P["sp"]), "of setpoint"
    return None


def fmt(x: float) -> str:
    return f"{x:,.0f}" if abs(x) >= 100 else f"{x:.3g}"


def collect() -> list[dict]:
    """One row per family, template and knob: the muscles of that kind, their band, native's point, the room and the reading."""
    rows = list(csv.DictReader(CATALOG.open()))
    labels = {r["muscle_id"]: r["label_all_loads"] for r in csv.DictReader(RESULT.open())}
    grp = defaultdict(lambda: {"muscles": set(), "bands": [], "labels": defaultdict(int), "realm": ""})
    for r in rows:
        g = grp[(r["family"], r["template"], r["knob"])]
        g["muscles"].add(r["muscle_id"]); g["realm"] = r["realm"]
        g["labels"][labels.get(r["muscle_id"], "not run")] += 1
        b = band(r["template"], r["knob"], params_for(r))
        if b:
            g["bands"].append(b)
    out = []
    for (family, template, knob), g in sorted(grp.items(), key=lambda kv: (kv[1]["realm"], kv[0])):
        up = down = 0.0; n = 0; lo = hi = nat = None; unit = ""
        for blo, bhi, bnat, u in g["bands"]:
            if bhi > blo:
                up += (bhi - bnat) / (bhi - blo); down += (bnat - blo) / (bhi - blo); n += 1
            lo = blo if lo is None else min(lo, blo); hi = bhi if hi is None else max(hi, bhi); nat = bnat; unit = u
        at_limit = native_at_limit(template, knob)
        out.append({"realm": g["realm"], "family": family, "template": template, "knob": knob, "muscles": len(g["muscles"]),
                    "at_limit": at_limit, "band": (lo, hi, nat, unit) if n else None,
                    "room_up": up / n if n else None, "room_down": down / n if n else None,
                    "wall": WALL.get((template, knob), ("unknown", "unknown")),
                    # the result file's own words (tools/run_realms_v5.py): MORE WORK, FASTER, FEWER MISSES and their joins are GAIN
                    "gain": sum(v for k, v in g["labels"].items() if "LOSS" not in k and any(w in k for w in ("MORE WORK", "FASTER", "FEWER MISSES"))),
                    "same": g["labels"].get("SAME AS NATIVE", 0), "limit": g["labels"].get("AT ITS LIMIT ON NATIVE", 0),
                    "loss": sum(v for k, v in g["labels"].items() if "LOSS" in k), "labels": dict(g["labels"])})
    return out


def page(rows: list[dict]) -> str:
    L = ["# The room table: every family's band, native's point, the room, the wall and the reading", "",
         "The table `docs/THE_ROOM.md` section 5.1 calls for, built by `tools/room_table.py` from the catalog, each muscle's preset "
         "as the realms runner builds it, the runner's own at-limit rule and the realms result on the engine that stands "
         "(`results/realms_v5/MUSCLES_V5.csv`, our own models, class S). The room is written as a share of the band: 1.0 means "
         "native sits at one end and the whole band lies the other way; 0 means native is at that end. Where every knob of a family "
         "is at its limit on native the band is one point and the room is none. The wall's kind (design or physics) is the one "
         "statement here that is not a measurement: it says what holds the wall, so the work of `docs/THE_ROOM.md` section 5.3 "
         "knows which walls a muscle of our own can move. Run and scored by The Omni-Compass LLC's own code. No outside party has "
         "reviewed or approved these results.", "",
         "| realm | family | plant | knob | muscles | band (lo → hi; native) | room up | room down | the wall | GAIN | same as native | at limit | LOSS |",
         "|---|---|---|---|---:|---|---:|---:|---|---:|---:|---:|---:|"]
    tot = defaultdict(int)
    for r in rows:
        b = r["band"]
        bs = (f"{fmt(b[0])} → {fmt(b[1])}; native {fmt(b[2])} {b[3]}" if b
              else "one point: at its limit on native" if r["at_limit"] else "a band the preset does not state; native's own setting")
        ru = f"{r['room_up']:.2f}" if r["room_up"] is not None else "0"
        rd = f"{r['room_down']:.2f}" if r["room_down"] is not None else "0"
        wall = f"{r['wall'][0]} ({r['wall'][1]})"
        L.append(f"| {r['realm']} | {r['family']} | {r['template']} | {r['knob']} | {r['muscles']} | {bs} | {ru} | {rd} | {wall} | "
                 f"{r['gain']} | {r['same']} | {r['limit']} | {r['loss']} |")
        for k in ("muscles", "gain", "same", "limit", "loss"):
            tot[k] += r[k]
    L += ["", f"**All rows:** {len(rows)} (family, plant, knob); muscles {tot['muscles']}; GAIN {tot['gain']}; STEADY, the same as native {tot['same']}; "
          f"STEADY, at its limit on native {tot['limit']}; LOSS {tot['loss']}.", "",
          "**How to read a row.** Room up or down near 1.0 with GAIN on most muscles: the law takes the room. Room with STEADY, the "
          "same as native: the room exists and the law does not take it; those muscles are the first work of `docs/THE_ROOM.md` "
          "section 5.2. A one-point band with STEADY at its limit: nothing to take; a muscle of our own can move the wall only where "
          "the wall is the design. A LOSS anywhere is a wiring fault to find (section 2 of that page), never the muscle's."]
    return "\n".join(stamp(L)) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    text = page(collect())
    if a.check:
        ok = PAGE.exists() and PAGE.read_text(encoding="utf-8") == text
        print("room table: current" if ok else "room table: out of date (python3 tools/room_table.py)")
        return 0 if ok else 1
    PAGE.write_text(text, encoding="utf-8")
    print(f"room table -> {PAGE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
