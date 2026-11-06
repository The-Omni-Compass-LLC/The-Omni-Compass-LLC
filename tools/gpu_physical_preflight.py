#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Physical NVIDIA qualification receipt for Omni-Compass Native/Watch/Omni trials.
Read-only except an optional idempotent persistence-mode enable requested by the operator.
No benchmark result is created by this tool."""
import argparse, json, os, pathlib, shutil, subprocess, time

def run(cmd):
    p=subprocess.run(cmd,capture_output=True,text=True)
    return p.returncode,p.stdout.strip(),p.stderr.strip()

def q(smi,gpu,field):
    rc,out,err=run([smi,"-i",str(gpu),f"--query-gpu={field}","--format=csv,noheader,nounits"])
    bad=(not out) or out.startswith("[") or "not supported" in out.lower() or "n/a"==out.lower()
    return {"supported": rc==0 and not bad,"value": out if out else None,"rc":rc,"stderr":err[:300] or None}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--gpu',default='0'); ap.add_argument('--smi',default=os.environ.get('NVIDIA_SMI','nvidia-smi'))
    ap.add_argument('--out',required=True); ap.add_argument('--require-wall',action='store_true'); ap.add_argument('--wall-meter',default=os.environ.get('WALL_METER',''))
    ap.add_argument('--one-job-per-gpu',action='store_true'); ap.add_argument('--enable-persistence',action='store_true')
    a=ap.parse_args(); out=pathlib.Path(a.out); out.parent.mkdir(parents=True,exist_ok=True)
    r={"schema":"omnicompass.gpu_physical_preflight.v1","epoch_s":time.time(),"gpu":a.gpu,"smi":a.smi,"checks":{},"warnings":[]}
    if not shutil.which(a.smi): r["checks"]["nvidia_smi"]={"pass":False,"detail":"not found"}; return finish(r,out)
    r["checks"]["nvidia_smi"]={"pass":True}
    fields=['uuid','name','driver_version','vbios_version','persistence_mode','power.management','power.limit','enforced.power.limit','power.default_limit','power.min_limit','power.max_limit','compute_mode','clocks_event_reasons.active','clocks.applications.graphics','clocks.applications.memory','clocks.default_applications.graphics','clocks.default_applications.memory']
    r['gpu_fields']={f:q(a.smi,a.gpu,f) for f in fields}
    if not r['gpu_fields']['clocks_event_reasons.active']['supported']:
        r['gpu_fields']['clocks_throttle_reasons.active']=q(a.smi,a.gpu,'clocks_throttle_reasons.active')
    if a.enable_persistence and r['gpu_fields']['persistence_mode']['value']!='Enabled':
        rc,so,se=run([a.smi,'-i',a.gpu,'-pm','1']); r['persistence_enable']={'rc':rc,'stdout':so,'stderr':se}; r['gpu_fields']['persistence_mode_after']=q(a.smi,a.gpu,'persistence_mode')
    persistence=(r['gpu_fields'].get('persistence_mode_after') or r['gpu_fields']['persistence_mode']).get('value')
    r['checks']['persistence_enabled']={'pass':persistence=='Enabled','value':persistence}
    r['checks']['power_management']={'pass':r['gpu_fields']['power.management']['value']=='Enabled','value':r['gpu_fields']['power.management']['value']}
    r['checks']['enforced_limit_readable']={'pass':r['gpu_fields']['enforced.power.limit']['supported'],'value':r['gpu_fields']['enforced.power.limit']['value']}
    ce=r['gpu_fields']['clocks_event_reasons.active']['supported'] or r['gpu_fields'].get('clocks_throttle_reasons.active',{}).get('supported',False)
    r['checks']['clock_event_reasons_readable']={'pass':bool(ce)}
    # Application clocks are a second authority. Where the driver exposes both current and default values, require equality.
    ac_pairs=[('clocks.applications.graphics','clocks.default_applications.graphics'),('clocks.applications.memory','clocks.default_applications.memory')]
    ac=[]
    for cur,default in ac_pairs:
        c,d=r['gpu_fields'][cur],r['gpu_fields'][default]
        if c['supported'] and d['supported']: ac.append(c['value']==d['value'])
    r['checks']['application_clocks_default']={'pass':all(ac) if ac else True,'required':bool(ac),'comparable_fields':len(ac)}
    r['checks']['one_job_per_gpu_declared']={'pass':bool(a.one_job_per_gpu),'value':bool(a.one_job_per_gpu)}
    # RAPL is secondary but record exact zones and capability.
    zones=[]
    for p in pathlib.Path(os.environ.get('RAPL_ROOT','/sys/class/powercap')).glob('intel-rapl:*'):
        try:
            if (p/'energy_uj').is_file(): zones.append({'path':str(p),'name':(p/'name').read_text().strip(),'max_energy_range_uj':(p/'max_energy_range_uj').read_text().strip() if (p/'max_energy_range_uj').exists() else None})
        except OSError: pass
    r['rapl_zones']=zones; r['checks']['rapl_available']={'pass':bool(zones),'required':False}
    # DCGM is an observer. Freeze local catalogue because field support/names vary by release/hardware.
    if shutil.which(os.environ.get('DCGMI','dcgmi')):
        rc,so,se=run([os.environ.get('DCGMI','dcgmi'),'dmon','--list']); r['dcgm']={'available':True,'catalogue_rc':rc,'catalogue':so,'stderr':se[:500]}
    else: r['dcgm']={'available':False}
    r['checks']['dcgm_available']={'pass':r['dcgm']['available'],'required':False}
    r['wall_meter']={'configured':bool(a.wall_meter),'spec':a.wall_meter.split(':',1)[0] if a.wall_meter else None}
    r['checks']['wall_meter_configured']={'pass':bool(a.wall_meter),'required':bool(a.require_wall)}
    required=['nvidia_smi','persistence_enabled','power_management','enforced_limit_readable','clock_event_reasons_readable','one_job_per_gpu_declared']
    if r['checks']['application_clocks_default']['required']: required.append('application_clocks_default')
    if a.require_wall: required.append('wall_meter_configured')
    r['required_checks']=required; r['qualified']=all(r['checks'][x]['pass'] for x in required)
    finish(r,out)

def finish(r,out):
    if 'qualified' not in r: r['qualified']=False
    out.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n'); print(json.dumps({'qualified':r['qualified'],'receipt':str(out)})); raise SystemExit(0 if r['qualified'] else 2)
if __name__=='__main__': main()
