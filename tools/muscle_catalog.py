#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The catalog of the muscles, explained: what each is for, what Omni-Compass reads and writes on it, how it is
wired, and which organisms it belongs to. Read from realms/catalog_v5.csv (the catalog the engine that stands, omni-v23, carries: the v5 law at its
default, the max); writes docs/MUSCLE_CATALOG.md.

    python3 tools/muscle_catalog.py
"""
from __future__ import annotations

import csv

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp, TOP as _LEGAL_TOP
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp, TOP as _LEGAL_TOP
from collections import OrderedDict
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from realms.presets import PRESETS  # noqa: E402  (an axis's own peak speed, s_peak)
from realms.compass_arm_v5 import load_cards, V5CFG  # noqa: E402  (every muscle's own card)
OUT = ROOT / "docs" / "MUSCLE_CATALOG.md"
REALMS = OrderedDict([("compute_ai_cloud", "Compute / AI / Cloud"), ("physics_robotics_autonomous", "Physics / Robotics / Autonomous"),
                      ("energy_facility_industrial", "Energy / Facility / Industrial"), ("distribution_specialized", "Distribution / Specialized")])
BANNER = f"> {_LEGAL_TOP}"                 # the one notice (tools/legal.py); stamp() keeps one copy of it

# the plant each muscle is modelled on (realms/plants.py): what it is, what its service reading is, what its lever does
TEMPLATE = {
    "compute_pool": ("a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs",
                     "how far its queue and its load sit toward the service line (queue or lateness, and load above half)",
                     "the capacity it may use: its replica or instance count (through its autoscaler's target or floor), its power share, or one unit given back through the release gate"),
    "thermal_zone": ("a data hall or building zone cooled by chillers, air handlers or fans",
                     "its temperature against its limit",
                     "its supply setpoint (colder is more cooling), its power share, or one cooling unit given back when the room has margin"),
    "energy_storage": ("a battery, UPS or microgrid store with a load and a grid connection",
                       "its draw on the grid connection and its reserve",
                       "its reserve setpoint (how much charge it holds back); its power limit is left native"),
    "motion_axis": ("a motor-driven axis: a robot joint, a flight-control surface, a reaction wheel, a traction motor",
                    "its tracking error and its load",
                    "its speed and effort share, or its power share"),
    "process_loop": ("a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint",
                     "how far the process sits from its band",
                     "its setpoint within its safe band, its actuator range, or its power share"),
}
KNOB = {
    "capacity": "**capacity**: how much of the machine is in service (replicas, instances, units, speed). At the max Omni-Compass pushes it to the machine's own limit for the most work, never past it and never below native.",
    "admission": "**admission**: what is let in (queues, rate limits, admission control). Native already lets everything in: the knob is at its limit on native, and Omni-Compass reads it and leaves it native.",
    "power": "**power**: the power share or limit the machine may draw. Native already runs it at full: at its limit on native, read and left native.",
    "setpoint": "**setpoint**: the target the machine's own loop holds (a temperature, a reserve, a process value). At the max a room is cooled ahead of the heat and a battery's charge is held for its line, inside the safe band, never behind native on its line.",
}


def does(r):
    """What the max does with one muscle (realms/compass_arm_v5.py)."""
    t, k = r["template"], r["knob"]
    if k == "admission":
        return "at its limit on native (nothing paced or turned away): read and left native"
    if t == "compute_pool":
        if k == "power":
            return "at its limit on native (the full clock): read and left native"
        return ("starts the machines the forecast needs before the rush lands and clears work waiting in line within one "
                "machine start, never fewer than native runs; hands back what it no longer needs at once")
    if t == "thermal_zone":
        return {"setpoint": "cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native",
                "capacity": "left to its own staging (native already has the cooling it needs: nothing to win)",
                "power": "at its limit on native (the site envelope at full): read and left native"}[k]
    if t == "energy_storage":
        if k == "power":
            return "at its limit on native (full battery power): read and left native"
        return "holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor"
    if t == "motion_axis":
        if k == "power":
            return "at its limit on native (full torque): read and left native"
        if PRESETS.get(r["preset"], {}).get("s_peak", 1.0) > 1.0:
            return ("its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its "
                    "tracking strains (alone; inside a body, its everyday speed)")
        return "at its limit on native (its everyday speed is the machine's limit): read and left native"
    if k == "setpoint":
        return "left native: native already holds it inside its band (nothing to win)"
    return "at its limit on native (the full actuator): read and left native"
# the class of machine each preset stands for (realms/presets.py), and how such a muscle is reached in a real stack
PRESET = {
    "server": ("an application service on servers or pods", "the Kubernetes API (HPA target and floor, pod resize)"),
    "node": ("a fleet of machines or VMs that boot in minutes", "the node pool's size command (Karpenter, Cluster Autoscaler, MachineSet, cloud ASG)"),
    "cpu_host": ("a CPU host whose clock and power can be set", "Linux cpufreq and RAPL"),
    "gpu": ("GPU serving with a response-time target", "nvidia-smi (clock ceiling and power limit) or the serving autoscaler"),
    "gpu_batch": ("GPU training and batch work", "nvidia-smi, the job scheduler's pause and resume"),
    "batch": ("batch and queued jobs", "the job queue (Kubernetes Jobs, Slurm, Spark)"),
    "fabric": ("a high-speed fabric (RDMA, DPU, SmartNIC)", "the fabric manager's API"),
    "robot_fleet": ("a fleet of robots or vehicles taking tasks", "the fleet manager's dispatch API"),
    "qpu": ("a quantum or specialised accelerator queue", "the accelerator's job queue"),
    "network": ("network routing and switching", "the network controller (SDN, routing API)"),
    "storage": ("block, file or object storage", "the storage system's QoS and tiering API"),
    "database": ("a database cluster", "the database operator (replicas, connection pools)"),
    "commerce": ("a customer-facing service with bursts", "the Kubernetes API"),
    "workflow": ("a workflow or pipeline engine", "the workflow engine's concurrency settings"),
    "ran": ("a radio access network cell or site", "the RAN controller (O-RAN interfaces)"),
    "data_hall": ("a data hall cooling plant", "the building management system (BACnet, Modbus) or its command line"),
    "building": ("a building zone", "the building management system"),
    "microgrid": ("a microgrid battery and loads", "the inverter or energy management system (IEEE 2030.5, SunSpec, OpenADR)"),
    "ups": ("an uninterruptible power supply", "the UPS and PDU management interface (SNMP, Modbus)"),
    "facility": ("a facility battery behind the meter", "the energy management system"),
    "robot_joint": ("a robot joint servo", "the robot controller (ROS 2, EtherCAT, the drive's fieldbus)"),
    "flight_axis": ("a flight-control axis", "the flight controller (modelled only)"),
    "reaction_wheel": ("a spacecraft reaction wheel", "the attitude controller (modelled only)"),
    "ev_traction": ("an electric vehicle traction motor", "the vehicle's motor controller (CAN; modelled only)"),
    "process": ("an industrial process loop", "the PLC or DCS (OPC UA, EtherNet/IP, PROFINET)"),
    "water": ("a water or pumping process", "the SCADA system (Modbus, DNP3)"),
    "chamber": ("a controlled chamber (clean room, kiln, reactor)", "the PLC or DCS"),
    "feeder_voltage": ("a distribution feeder's voltage", "the distribution management system (IEC 61850, DNP3; modelled only)"),
    # Omni v2, wave 4
    "hospital": ("a hospital's critical rooms (operating rooms, isolation, pharmacy, imaging suites)", "the hospital's building management system (BACnet)"),
    "clinical": ("clinical systems: imaging archives, records, interface engines, monitoring gateways", "the application's own scaling and admission settings (Kubernetes, the vendor console)"),
    "port": ("a container terminal's cranes and vehicles taking moves", "the terminal operating system and fleet controllers"),
    "irrigation": ("pumps, pressure and climate on a farm or in a greenhouse", "the pump station controller, the pivot panel or the climate computer (Modbus, the vendor cloud)"),
    "pipeline": ("a pipeline segment with its compressors, pumps and valves", "pipeline SCADA (DNP3, Modbus, OPC UA)"),
    "mill": ("a grinding, flotation or materials-handling circuit", "the plant DCS or PLC (OPC UA)"),
    "district_heat": ("a district heating or cooling network", "the network control system and substation controllers (Modbus, M-Bus)"),
    "turbine": ("a generating unit's governor, boiler or excitation loop", "the plant DCS and governor (OPC UA, IEC 61850; modelled only)"),
    "inverter": ("a plant of grid-support inverters or wind turbines", "the plant controller and inverter settings (SunSpec, IEC 61850, IEEE 1547)"),
    "batch_reactor": ("a GMP batch reactor, fermenter or food process", "the batch control system (ISA-88, OPC UA)"),
    "rail_traction": ("a train's traction and auxiliary systems", "the train control and management system and ATO (modelled only)"),
    "marine_propulsion": ("a ship's propulsion shaft and power plant", "the vessel automation and power management system (modelled only)"),
    "elevator_hoist": ("an elevator or escalator drive and its group control", "the lift controller and destination dispatch (modelled only)"),
}


def card_text(c):
    """A muscle's own card in plain words; "global" where it runs the global setting."""
    if not c:
        return "global"
    parts = []
    if "edge_util" in c:
        parts.append(f"machines started at {c['edge_util'] * 100:.0f}% full")
    if "window" in c:
        parts.append(f"reads the last {c['window']} decisions")
    if "line_z" in c:
        parts.append(f"{c['line_z']:g} wobbles of margin on its line")
    if "hold_window" in c:
        parts.append(f"reads its line {c['hold_window']} decisions before it holds")
    if "hold_margin" in c:
        parts.append(f"keeps {c['hold_margin'] * 100:.0f}% of its line clear")
    if "heat_head" in c:
        parts.append(f"pushed under {c['heat_head'] * 100:.0f}% of its heat rise")
    if "strain" in c:
        parts.append(f"tracking under {c['strain'] * 100:.0f}% of its line")
    return "; ".join(parts)


def nice(m):
    return m.replace("_", " ")


def main():
    rows = list(csv.DictReader(open(ROOT / "realms" / "catalog_v5.csv", encoding="utf-8")))
    cards = load_cards()
    spine = [r for r in rows if len(r["realms"].split(";")) == 4]
    counts = {k: sum(1 for r in rows if k in r["realms"].split(";")) for k in REALMS}
    L = [f"# The {len(rows)} Muscles: What Each Is For, and How It Is Wired", "", BANNER, "",
         "A **muscle** is one setting on one machine that already has its own control: a replica target, a node pool's size, "
         "a GPU's clock ceiling, a chiller's setpoint, a battery's reserve, a joint's effort. Omni-Compass does not replace "
         "that control. It reads the machine's meters and, at its default, the max, moves the setting the machine already "
         "accepts toward the machine's own limit for the most work, never past it and never below native, through a plug "
         "that reads the setting once before the first write, reads back every write, steps aside if another controller "
         "moves it, and walks it back to native at the end. A knob native already runs at the top of its range is at its "
         "limit on native and is left there.", "",
         f"This chapter lists all {len(rows)} muscles of the v5 catalog (`realms/catalog_v5.csv`); each run records its engine separately. For each one it says what kind of machine "
         "it is, which of the four kinds of knob it is, what Omni-Compass reads and does with it, how such a muscle is "
         "reached in a real stack, and which organisms it belongs to. The plants behind the benchmark numbers are models of "
         "these machines (evidence class **S**); a muscle in this list is wired on a real system only through the levels "
         "and the checks of the manual (chapters 4 and 6). See `DISCLOSURES.md`.", "",
         "## How to read an entry", "",
         "**The four kinds of knob.**", ""] + [f"- {v}" for v in KNOB.values()] + ["",
         "**The five kinds of plant.** Every muscle is modelled on one of five plants, each with its own service reading and "
         "lever:", "", "| Plant | What it is | What Omni-Compass reads | What Omni-Compass moves |", "|---|---|---|---|"]
    for k, (what, reads, moves) in TEMPLATE.items():
        L.append(f"| `{k}` | {what} | {reads} | {moves} |")
    g = V5CFG
    L += ["", "**Every muscle its own card.** The brain is one, its settings each muscle's own. A muscle's card holds the "
          "settings the max uses for that muscle (a machine pool: how full it runs on its forecast before it calls for more, "
          "and how many decisions of history it reads; a battery: how many wobbles of margin it keeps under its line, and, "
          "wired by its power, how long it reads its line before it holds and how much of it it keeps clear). The cards "
          "were found by an automatic search over every muscle on the development seeds, today's global setting always "
          "one of the choices, and kept only where the card beat the global setting beyond the noise on two separate sets "
          "of seeds and on no seed under any load fell behind native: never over its line more often, never less "
          "work, never its line cleared later (`tools/tune_cards.py`, `realms/muscle_cards_v5.csv`, "
          "`results/cards_v5/`). Inside a body, a battery wired by its power keeps the body's own margins on its line. "
          f"{len(cards)} muscles carry a card of their own; every other muscle runs the global setting (machines started "
          f"at {g.edge_util * 100:.0f}% full, the last {g.window} decisions read, {g.line_z:g} wobbles of margin on a "
          f"battery's line, {g.hold_margin * 100:.0f}% of it kept clear). Each muscle's card is in the last column of its "
          "family's table.", ""]
    L += ["", f"**The organisms.** The {len(rows)} muscles build seven organisms: the spine ({len(spine)} muscles, every muscle that sits "
          "in all four realms: the base every stack runs on, as an operating system is the base of every program), each of the four "
          f"realms (every muscle whose realm list includes it, the spine among them), the four stacked with every duplicate kept "
          f"({sum(counts.values()):,}), and the whole tower with every muscle once ({len(rows)}). Each is run native and with "
          "Omni-Compass on top of native (`docs/THE_SPINE.md`, `docs/REALMS.md`).", "",
          "| Organism | Muscles |", "|---|---:|", f"| The spine, the muscles every stack runs on | {len(spine)} |"]
    for k, n in REALMS.items():
        L.append(f"| {n} | {counts[k]} |")
    L += [f"| The four stacked, every duplicate kept | {sum(counts.values()):,} |", f"| The whole tower, every muscle once | {len(rows)} |", "",
          "**How a muscle is reached in a real stack.** The class of machine decides the wire:", "",
          "| Class of machine | What it is | The wire in a real stack |", "|---|---|---|"]
    for k in sorted({r["preset"] for r in rows}):
        what, wire = PRESET.get(k, (k, "see the manual, section 4.2"))
        L.append(f"| `{k}` | {what} | {wire} |")
    L += ["", "Wires marked *modelled only* exist as plants in the benchmark and are not built for live use.", ""]

    recipes = {r["family"]: r for r in csv.DictReader(open(ROOT / "docs" / "wiring_recipes.csv", encoding="utf-8"))}
    missing = sorted({r["family"] for r in rows} - set(recipes))
    if missing:
        raise SystemExit(f"docs/wiring_recipes.csv lacks a recipe for: {', '.join(missing)}")
    L += ["**How to wire any muscle on your own stack (the plug, chapter 4).** Every muscle below is wired the same way: "
          "Omni-Compass never replaces the native controller; it reads the controller's own meters (the wire out) and writes "
          "the one setting the controller already accepts (the wire in), through a plug that (1) reads the setting once before "
          "the first write and records it, (2) reads back every write and stops writing if another writer moved the setting, "
          "(3) renews a lease every decision so a dead governor's settings walk back to native by themselves, and (4) restores "
          "the recorded setting at the end. Each family's entry says which native controller owns its muscles, where the "
          "reading is tapped, where the setting is written, how it is restored, and whether that wire has run live in this "
          "repository or only on a model (`docs/wiring_recipes.csv`). The muscle's name is the setting's own name on that "
          "controller. Where the entry says *modelled only*, the plant exists in the benchmark and the wire is written against "
          "the controller's documented interface, not yet run on the machine.", ""]

    def family_tables(group, home_note):
        fams = OrderedDict()
        for r in group:
            fams.setdefault(r["family"], []).append(r)
        out = []
        for fam, rs in fams.items():
            t, p = rs[0]["template"], rs[0]["preset"]
            what = TEMPLATE[t][0]
            pw = PRESET.get(p, (p, "see the manual"))
            rc = recipes[fam]
            out += [f"### {fam} ({len(rs)} muscles)", "",
                    f"Each is {what}; its class is `{p}` ({pw[0]}), reached through {pw[1]}. Omni-Compass reads "
                    f"{TEMPLATE[t][1]}. {home_note}", "",
                    "**Wire it on your stack.**", "",
                    f"- **Native controller:** {rc['native_controller']}.",
                    f"- **Wire out (read):** {rc['read']}.",
                    f"- **Wire in (write):** {rc['write']}.",
                    f"- **Restore:** {rc['restore']}.",
                    f"- **Run live?** {rc['live']}.", "",
                    "| # | Muscle (the setting's own name) | Knob | What Omni-Compass does with it | Organisms | Its own card |",
                    "|---:|---|---|---|---|---|"]
            for r in sorted(rs, key=lambda r: (not r["muscle_id"].isdigit(), int("".join(c for c in r["muscle_id"] if c.isdigit()) or 0))):
                k = r["knob"]
                org = "the spine; all four realms" if len(r["realms"].split(";")) == 4 else ", ".join(REALMS[x].split(" / ")[0] for x in r["realms"].split(";"))
                out.append(f"| {r['muscle_id']} | {nice(r['muscle'])} | {k} | {does(r)} | {org}; stack; tower | "
                           f"{card_text(cards.get(r['muscle_id']))} |")
            out.append("")
        return out

    L += [f"## The spine: {len(spine)} muscles in all four realms, an organism of its own", "",
          "The machines every realm stands on: servers, machines, GPUs and CPUs, network, storage, observability, security, "
          "cooling and electrical distribution. The spine is the seventh organism (`spine`, the base every stack runs on, run "
          "native and with Omni-Compass on top like the other six; `docs/THE_SPINE.md`), and each spine muscle is also part of "
          "every realm's organism, counted once in the tower and four times in the stack.", ""]
    L += family_tables(spine, "It belongs to every organism.")
    for k, n in REALMS.items():
        own = [r for r in rows if r["realm"] == k and len(r["realms"].split(";")) < 4]
        L += [f"## Realm: {n} ({len(own)} muscles of its own, {counts[k]} in its organism with the spine)", ""]
        L += family_tables(own, f"Its home realm is {n}.")
    OUT.write_text("\n".join(_legal_stamp(L)) + "\n", encoding="utf-8")
    print(OUT, len(rows), "muscles")


if __name__ == "__main__":
    main()
