# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""External GPU actuator watchdog against the standin nvidia-smi."""
import json, os, subprocess, sys, tempfile, time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SMI=str(ROOT/'tests/standin_gpu/nvidia-smi')

def main():
    d=Path(tempfile.mkdtemp()); state=d/'state.json'
    state.write_text(json.dumps({"limit":{"0":220.0},"default":300,"min":100,"max":350,"draw_w":180.0,"util":40,"temp":60}))
    env=dict(os.environ, STANDIN_SMI_STATE=str(state))
    sleeper=subprocess.Popen([sys.executable,'-c','import time; time.sleep(60)'])
    receipt=d/'watchdog.jsonl'
    w=subprocess.Popen([sys.executable,str(ROOT/'tools/gpu_actuator_watchdog.py'),'--pid',str(sleeper.pid),'--gpu','0','--start-w','300','--smi',SMI,'--receipt',str(receipt),'--poll','0.05'],cwd=ROOT,env=env)
    time.sleep(.2); sleeper.kill(); sleeper.wait(); assert w.wait(timeout=5)==0
    st=json.loads(state.read_text()); assert st['limit']['0']==300.0, st
    rec=[json.loads(x) for x in receipt.read_text().splitlines()]
    assert rec[-1]['restore_attempted'] and rec[-1]['restored'], rec
    print('GPU WATCHDOG PASS: abnormal governor death restored 220 W -> 300 W')
if __name__=='__main__': main()
