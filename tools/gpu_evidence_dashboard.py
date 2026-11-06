#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Generate a compact evidence dashboard only from completed arm receipts. Refuses empty/fabricated runs."""
import argparse,json,pathlib,sys
try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('run_dir'); a=ap.parse_args(); root=pathlib.Path(a.run_dir)
 rows=[]
 for rep in sorted(root.glob('rep-*')):
  for arm in ('native','watch','omni'):
   p=rep/arm/'ARM_RECEIPT.json'
   if not p.exists(): raise SystemExit(f'missing physical arm receipt: {p}')
   r=json.loads(p.read_text()); rows.append((rep.name,arm,r))
 if not rows: raise SystemExit('no physical arm receipts; dashboard refused')
 L=['# Physical GPU evidence dashboard','', '| Rep | Arm | Work | p95 ms | SLO | GPU device J | Wall J | CPU package J | Work/kJ | Writes | Restore |',
    '|---|---|---:|---:|:---:|---:|---:|---:|---:|---:|:---:|']
 for rep,arm,r in rows:
  f=lambda x:'UNAVAILABLE' if x is None else f'{x:.3f}' if isinstance(x,float) else str(x)
  writes=r.get('watch_pl_writes',0) if arm=='watch' else r.get('omni_pl_writes',0) if arm=='omni' else 0
  L.append(f"| {rep} | {arm} | {r.get('work_units')} | {f(r.get('p95_ms'))} | {'PASS' if r.get('slo_ok') else 'FAIL'} | {f(r.get('energy_device_j'))} | {f(r.get('energy_wall_j'))} | {f(r.get('energy_cpu_package_j'))} | {f(r.get('work_per_kj'))} | {writes} | {'PASS' if r.get('restore_ok') else 'FAIL'} |")
 # Qualification lights are factual structural lights, not a performance verdict.
 watch0=all(r.get('watch_pl_writes')==0 for _,a,r in rows if a=='watch')
 restore=all(r.get('restore_ok') for _,_,r in rows); slo=all(r.get('slo_ok') for _,_,r in rows)
 L += ['', '## Qualification lights','',f'- Watch writes zero: {"PASS" if watch0 else "FAIL"}',f'- Restore: {"PASS" if restore else "FAIL"}',f'- SLO held in every arm: {"PASS" if slo else "FAIL"}', '- Requested/enforced actuator fidelity and statistical verdict: see GPU_REPS.md / GPU_REPS.json.','']
 (root/'GPU_EVIDENCE_DASHBOARD.md').write_text('\n'.join(_legal_stamp(L)) + '\n'); print(root/'GPU_EVIDENCE_DASHBOARD.md')
if __name__=='__main__': main()
