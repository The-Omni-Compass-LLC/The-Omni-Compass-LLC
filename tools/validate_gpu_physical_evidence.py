#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Validate structure/provenance of a completed physical Native/Watch/Omni GPU run.
This does not decide scientific superiority; gpu_reps.py owns preregistered statistics/labels."""
import argparse, hashlib, json, pathlib, sys

def sha(p):
 h=hashlib.sha256();
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1<<20),b''): h.update(b)
 return h.hexdigest()

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('run_dir'); ap.add_argument('--out'); a=ap.parse_args(); root=pathlib.Path(a.run_dir)
 issues=[]; reps=sorted([p for p in root.glob('rep-*') if p.is_dir()]);
 if not reps: issues.append('no rep-* directories')
 required_common=['smi.csv','smi_fields.txt','window_start.txt','window_end.txt','limit_start.txt','limit_end.txt','requests.csv','device_start.txt','device_end.txt','rapl_start.tsv','rapl_end.tsv','compute_apps_prearm.csv','compute_apps_postwork.csv','ARM_RECEIPT.json']
 for rep in reps:
  for arm in ('native','watch','omni'):
   d=rep/arm
   if not d.is_dir(): issues.append(f'{rep.name}/{arm}: missing arm'); continue
   for f in required_common:
    if not (d/f).exists(): issues.append(f'{rep.name}/{arm}: missing {f}')
   if (d/'compute_apps_invalid.txt').exists(): issues.append(f'{rep.name}/{arm}: pre-existing compute process detected')
   if arm!='native':
    for f in ('audit.jsonl','governor_exit.txt','watchdog.jsonl'):
     if not (d/f).exists(): issues.append(f'{rep.name}/{arm}: missing {f}')
   if (d/'limit_start.txt').exists() and (d/'limit_end.txt').exists() and (d/'limit_start.txt').read_text().strip()!=(d/'limit_end.txt').read_text().strip(): issues.append(f'{rep.name}/{arm}: restoration mismatch')
   if (d/'ARM_RECEIPT.json').exists():
    try:
     ar=json.loads((d/'ARM_RECEIPT.json').read_text())
     if not ar.get('restore_ok'): issues.append(f'{rep.name}/{arm}: receipt restore_ok false')
     if arm=='watch' and ar.get('watch_pl_writes')!=0: issues.append(f'{rep.name}/watch: receipt write count nonzero')
     if not ar.get('slo_ok'): issues.append(f'{rep.name}/{arm}: SLO not held')
    except Exception: issues.append(f'{rep.name}/{arm}: malformed ARM_RECEIPT.json')
  w=rep/'watch'/'audit.jsonl'
  if w.exists():
   writes=0
   for line in w.read_text().splitlines():
    try: writes += 'write' in json.loads(line)
    except Exception: issues.append(f'{rep.name}/watch: malformed audit JSON'); break
   if writes: issues.append(f'{rep.name}/watch: {writes} write records')
 for f in ('FREEZE.json','FREEZE_END.json','receipt.json','GPU_REPS.json','GPU_REPS.md','SHA256SUMS.txt','PHYSICAL_PREFLIGHT.json'):
  if not (root/f).exists(): issues.append(f'missing root {f}')
 if (root/'PHYSICAL_PREFLIGHT.json').exists():
  try:
   if not json.loads((root/'PHYSICAL_PREFLIGHT.json').read_text()).get('qualified'): issues.append('physical preflight not qualified')
  except Exception: issues.append('malformed PHYSICAL_PREFLIGHT.json')
 # Verify checksum manifest for files it names.
 if (root/'SHA256SUMS.txt').exists():
  for line in (root/'SHA256SUMS.txt').read_text().splitlines():
   try: expected,rel=line.split(None,1); rel=rel.lstrip('*').lstrip('./'); p=root/rel
   except ValueError: issues.append('malformed SHA256SUMS line'); continue
   if not p.exists(): issues.append(f'checksum target missing: {rel}')
   elif sha(p)!=expected: issues.append(f'checksum mismatch: {rel}')
 verdict={'schema':'omnicompass.gpu_physical_evidence_validation.v1','run_dir':str(root),'repetitions':len(reps),'valid_structure':not issues,'issues':issues}
 out=pathlib.Path(a.out) if a.out else root/'PHYSICAL_EVIDENCE_VALIDATION.json'; out.write_text(json.dumps(verdict,indent=2)+'\n'); print(json.dumps(verdict,indent=2)); return 0 if not issues else 2
if __name__=='__main__': sys.exit(main())
