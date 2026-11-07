# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parents[1]))
import importlib.util, pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('gate',ROOT/'tools/causal_evidence_gate.py'); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

def base():
 return {'arm':'omni','canonical_u_provenance':{'present':True,'u_hold':3.2},'omni_pl_writes':2,'watch_pl_writes':0,
 'actuator':{'enforced_matches_requested':True},'health':{},'energy_device_j':1000.0,'work_units':100,'slo_ok':True,'restore_ok':True}

def test_complete_chain_is_only_candidate_not_global_win():
 o=m.gate(base()); assert o['claim_level']=='RESTORED_CANDIDATE_REQUIRES_CROSS_ARM_STATISTICS'; assert not o['global_superiority_claimed']; assert not o['physical_benefit_decided_here']

def test_successful_write_without_enforcement_stops_at_requested():
 r=base(); r['actuator']['enforced_matches_requested']=False; o=m.gate(r); assert o['claim_level']=='REQUESTED'

def test_thermal_confound_blocks_attribution():
 r=base(); r['health']['thermal_slowdown']=True; o=m.gate(r); assert o['claim_level']=='ENFORCED'

def test_missing_meter_cannot_be_benefit_candidate():
 r=base(); r['energy_device_j']=None; o=m.gate(r); assert not o['links']['beneficial_candidate']

def test_slo_miss_is_preserved():
 r=base(); r['slo_ok']=False; o=m.gate(r); assert not o['links']['beneficial_candidate']

def test_watch_write_is_invalid_for_attribution():
 r=base(); r.update(arm='watch',watch_pl_writes=1,omni_pl_writes=0); o=m.gate(r); assert not o['links']['attributed']

def test_missing_u_provenance_blocks_everything():
 r=base(); r['canonical_u_provenance']={'present':False}; o=m.gate(r); assert o['claim_level']=='COMPUTED'


def main():
    """Run every test in this file (it also runs under pytest)."""
    import inspect, pathlib, tempfile
    n = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            args = [pathlib.Path(tempfile.mkdtemp()) for p in inspect.signature(fn).parameters if p == "tmp_path"]
            fn(*args); n += 1
    print(f"PASS {pathlib.Path(__file__).stem}: {n} tests")


if __name__ == "__main__":
    main()
