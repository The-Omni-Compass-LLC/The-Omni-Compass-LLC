#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Conservative causal proof gate for an Omni physical arm receipt.

It never declares Omni globally superior. It answers only: how far does THIS receipt support
THIS actuator chain?  Every promotion requires all lower links.  Adverse performance is kept.
"""
import sys as _sys, pathlib as _pl; _sys.path.insert(0, str(_pl.Path(__file__).resolve().parents[1]))
import argparse, json, math, pathlib, sys
from omnicompass.authority_contract import ClaimLevel

def finite(x): return isinstance(x,(int,float)) and math.isfinite(x)
def gate(r):
    arm=r.get('arm'); reasons=[]; links={}
    links['computed']=bool(r.get('canonical_u_provenance',{}).get('present'))
    if not links['computed']: reasons.append('missing canonical held-u provenance')
    writes=r.get('omni_pl_writes',0) if arm=='omni' else r.get('watch_pl_writes',0)
    links['requested']=links['computed'] and (arm!='omni' or isinstance(writes,int) and writes>0)
    if arm=='omni' and not links['requested']: reasons.append('no physical Omni -pl write recorded')
    act=r.get('actuator') or {}
    enforced_ok=bool(act.get('enforced_matches_requested',False))
    links['enforced']=links['requested'] and (arm!='omni' or enforced_ok)
    if arm=='omni' and not enforced_ok: reasons.append('requested/enforced authority not established')
    health=r.get('health') or {}
    hostile=bool(health.get('thermal_slowdown') or health.get('hw_power_brake') or health.get('foreign_writer') or health.get('application_clocks_conflict'))
    links['attributed']=links['enforced'] and not hostile and (arm!='watch' or r.get('watch_pl_writes')==0)
    if hostile: reasons.append('hostile/confounding limiter or writer present')
    if arm=='watch' and r.get('watch_pl_writes')!=0: reasons.append('Watch wrote power limit')
    energy=r.get('energy_device_j'); work=r.get('work_units'); slo=bool(r.get('slo_ok'))
    links['measured']=finite(energy) and energy>0 and finite(work) and work>=0
    links['guardrails']=slo
    links['beneficial_candidate']=links['attributed'] and links['measured'] and links['guardrails']
    # Cross-arm benefit is intentionally NOT decided here; gpu_reps.py owns preregistered statistics.
    links['restored']=links['beneficial_candidate'] and bool(r.get('restore_ok'))
    if not links['measured']: reasons.append('physical device energy/work pair missing')
    if not slo: reasons.append('SLO guardrail not held')
    if not r.get('restore_ok'): reasons.append('restoration not verified')
    level='COMPUTED'
    for name,key in [('REQUESTED','requested'),('ENFORCED','enforced'),('ATTRIBUTED','attributed')]:
        if links[key]: level=name
        else: break
    if links['beneficial_candidate']: level='BENEFIT_CANDIDATE_REQUIRES_CROSS_ARM_STATISTICS'
    if links['restored']: level='RESTORED_CANDIDATE_REQUIRES_CROSS_ARM_STATISTICS'
    return {'schema':'omnicompass.causal_evidence_gate.v1','arm':arm,'claim_level':level,'links':links,'reasons':reasons,
            'global_superiority_claimed':False,'physical_benefit_decided_here':False}

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('receipt'); ap.add_argument('--out'); a=ap.parse_args(); p=pathlib.Path(a.receipt); r=json.loads(p.read_text()); o=gate(r); out=pathlib.Path(a.out) if a.out else p.with_name('CAUSAL_EVIDENCE_GATE.json'); out.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n'); print(json.dumps(o,indent=2)); return 0
if __name__=='__main__': sys.exit(main())
