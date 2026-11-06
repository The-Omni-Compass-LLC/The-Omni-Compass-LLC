# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Build the Omni v2 catalog (realms/catalog.csv) from three committed sources, by the same rules as v1:

  realms/catalog_v1.csv                 the v1 tower (656 rows), kept byte for byte: every v1 muscle keeps its id, realm,
                                        plant, preset and knob
  docs/realm_study/TRUE_MUSCLES.csv     the realm study's rows marked "added (real, not in the 656)": real controls the
                                        study found in waves 1 to 3 that the tower lacked, each with its system, setting
                                        and source; they join the family the study filed them under (ids 1001 upward)
  realms/wave4_families.csv             wave 4: the thirteen families the tower did not cover (hospitals, clinical
                                        systems, farms, pipelines, rail, ships, ports, mines, district heat, power plants,
                                        renewables and inverters, elevators, pharmaceutical and food plants), each muscle
                                        with its real system, setting and source (ids 2001 upward)

Realm, membership (the spine is in every realm), plant, preset and knob come from tools/realms_catalog.py's FAMILY,
SPINE and knob rules, unchanged. The result is committed as data, so every row can be read and contested; the
provenance (realms/catalog_provenance.json) names the three sources and their digests.

  python3 tools/realms_catalog_v2.py          # rewrite realms/catalog.csv and the provenance; add the wave-4 rows to
                                              # docs/realm_study/TRUE_MUSCLES.csv if they are not there yet
  python3 tools/realms_catalog_v2.py --check  # rebuild in memory and compare with the committed catalog (verify.py)
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.realms_catalog import ALL_REALMS, FAMILY, SPINE, knob_for  # noqa: E402

V1 = ROOT / "realms" / "catalog_v1.csv"
STUDY = ROOT / "docs" / "realm_study" / "TRUE_MUSCLES.csv"
WAVE4 = ROOT / "realms" / "wave4_families.csv"
OUT = ROOT / "realms" / "catalog.csv"
PROV = ROOT / "realms" / "catalog_provenance.json"
FIELDS = ["muscle_id", "family_id", "family", "muscle", "realm", "realms", "template", "preset", "knob"]

# the realm study's short family codes (docs/realm_study/) to the tower's family names
STUDY_FAMILY = {
    "k8s_workload": "Kubernetes Workload Scaling", "k8s_container": "Container Resources", "cgroup": "Container Resources",
    "k8s_sched": "Kubernetes Placement & Scheduling", "nodes": "Node Fleet & Karpenter-Class Control", "vm": "Cloud VM & Capacity",
    "cpu": "Host CPU & Memory", "gpu": "NVIDIA GPU Hardware", "fabric": "GPU Fabric & RDMA", "inference": "AI Inference Serving",
    "training": "AI Training", "hpc": "HPC & Distributed Compute", "clustermgr": "Distributed Cluster Managers",
    "network": "Network Routing & Switching", "mesh": "Service Mesh & API Reliability", "storage": "Storage Block/File/Object",
    "database": "Database & Transactions", "messaging": "Messaging & Streaming", "cache": "Cache & Memory Services",
    "search": "Search, Indexing & Vector DB", "runtime": "Runtime & Application", "observe": "Observability & Telemetry",
    "admission": "Work Admission & Demand Shaping", "power": "PDU, UPS & Electrical Distribution",
    "cooling": "Cooling, Chillers & Thermodynamics", "building": "Building & Critical Environment HVAC",
    "storage_grid": "Energy Storage & Microgrid", "process": "Industrial PLC & Process Automation",
    "fab": "Semiconductor Fab & Precision Manufacturing", "flight": "Aviation & Autonomous Flight",
    "robot_motion": "Robotics Motion Control", "ev": "Automotive EV & Mobile Powertrain",
}
WAVE4_FAMILY_ID = {f: 40 + i for i, f in enumerate([
    "Healthcare Critical Environments", "Medical Imaging & Clinical Systems", "Agriculture & Irrigation", "Oil & Gas Pipelines",
    "Rail Traction & Train Control", "Marine Propulsion & Vessel Automation", "Ports & Maritime Logistics",
    "Mining & Mineral Processing", "District Heating & Cooling", "Power Generation & Turbine Control",
    "Renewable Generation & Inverter Control", "Elevators & Vertical Transport", "Pharmaceutical & Food Manufacturing"])}


def snake(name: str) -> str:
    return re.sub(r"_+", "_", re.sub(r"[^a-z0-9]+", "_", name.lower())).strip("_")


def row_for(muscle_id, family_id, family, muscle):
    realm, template, preset = FAMILY[family]
    member = ALL_REALMS if family in SPINE else (realm,)
    return dict(muscle_id=str(muscle_id), family_id=str(family_id), family=family, muscle=muscle, realm=realm,
                realms=";".join(member), template=template, preset=preset, knob=knob_for(template, muscle))


def build():
    v1 = list(csv.DictReader(V1.open()))
    assert len(v1) == 656, len(v1)
    rows = [dict(r) for r in v1]
    names = {r["muscle"] for r in rows}
    family_ids = {r["family"]: r["family_id"] for r in rows}
    study = [r for r in csv.DictReader(STUDY.open()) if r["origin"].startswith("added")]
    added, skipped = [], []
    for i, r in enumerate(study):
        name = snake(r["muscle"])
        family = STUDY_FAMILY[r["family"]]
        if name in names:
            skipped.append(name)                                   # the tower already has it under this name
            continue
        names.add(name)
        row = row_for(1001 + i, family_ids[family], family, name)
        rows.append(row); added.append((row, r))
    wave4 = list(csv.DictReader(WAVE4.open()))
    w4 = []
    for i, r in enumerate(wave4):
        assert r["muscle"] not in names, f"wave 4 name already in the tower: {r['muscle']}"
        names.add(r["muscle"])
        row = row_for(2001 + i, WAVE4_FAMILY_ID[r["family"]], r["family"], r["muscle"])
        rows.append(row); w4.append((row, r))
    return rows, added, skipped, w4


def main(argv=None):
    argv = argv or sys.argv[1:]
    rows, added, skipped, w4 = build()
    if "--check" in argv:
        have = list(csv.DictReader(OUT.open()))
        same = [dict(r) for r in have] == rows
        print(f"catalog {'matches' if same else 'DIFFERS FROM'} its sources: {len(rows)} rows")
        return 0 if same else 1
    with OUT.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS); w.writeheader(); w.writerows(rows)
    # the wave-4 muscles into the study's true-muscle list, once
    tm = list(csv.DictReader(STUDY.open()))
    have = {r["muscle"] for r in tm}
    new = [dict(muscle=row["muscle"], realm=row["realm"], family=row["family"], origin="wave 4 (v2 family)", verdict="real",
                control=src["setting"].split(" and ")[0], system=src["system"], setting=src["setting"], source=src["source"])
           for row, src in w4 if row["muscle"] not in have]
    if new:
        with STUDY.open("a", newline="") as f:
            csv.DictWriter(f, fieldnames=list(tm[0])).writerows(new)
    sizes = {rl: sum(1 for x in rows if rl in x["realms"].split(";")) for rl in ALL_REALMS}
    prov = {"version": "omni-v2", "rows": len(rows), "v1_rows": 656, "study_rows_added": len(added), "study_rows_already_in_tower": skipped,
            "wave4_rows": len(w4), "wave4_families": sorted(WAVE4_FAMILY_ID), "spine_rows": sum(1 for x in rows if ";" in x["realms"]),
            "organism_sizes": sizes, "stack_rows": sum(sizes.values()),
            "sources": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in (V1, STUDY, WAVE4)},
            "rules": "realm, membership, plant, preset and knob: tools/realms_catalog.py (FAMILY, SPINE, KNOB, OVERRIDE), unchanged from v1"}
    PROV.write_text(json.dumps(prov, indent=1) + "\n")
    print(f"catalog: {len(rows)} rows = 656 v1 + {len(added)} study-found + {len(w4)} wave 4; spine {prov['spine_rows']}; "
          f"organisms {sizes}; stack {prov['stack_rows']}; skipped (already in the tower): {skipped}")
    print(Counter((x["template"], x["knob"]) for x in rows))
    return 0


if __name__ == "__main__":
    sys.exit(main())
