#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Independent GPU power-limit restoration watchdog.

Runs outside the Omni governor.  It never optimizes and never lowers a limit.
It only watches the governor PID; if that process disappears, it reads the GPU
power limit and restores the frozen start limit when necessary.  The receipt is
JSONL so the paired bench can prove whether the second restoration path fired.
"""
from __future__ import annotations
import argparse, fcntl, json, os, subprocess, time
from pathlib import Path


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def query(smi, gpu):
    r = run([smi, "-i", str(gpu), "--query-gpu=power.limit", "--format=csv,noheader,nounits"])
    if r.returncode:
        raise RuntimeError(r.stderr.strip() or "power-limit query failed")
    return float(r.stdout.strip().splitlines()[0].strip())


def alive(pid):
    try:
        os.kill(pid, 0); return True
    except ProcessLookupError:
        return False
    except PermissionError:
        return True


def emit(path, obj):
    obj = {"t": time.time(), **obj}
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(obj, sort_keys=True) + "\n")


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--pid", type=int, required=True)
    p.add_argument("--gpu", required=True)
    p.add_argument("--start-w", type=float, required=True)
    p.add_argument("--smi", default=os.environ.get("NVIDIA_SMI", "nvidia-smi"))
    p.add_argument("--receipt", required=True)
    p.add_argument("--poll", type=float, default=0.25)
    p.add_argument("--timeout", type=float, default=0.0)
    a = p.parse_args(argv)
    t0 = time.time(); emit(a.receipt, {"event":"armed", "pid":a.pid, "gpu":a.gpu, "start_w":a.start_w})
    while alive(a.pid):
        if a.timeout and time.time() - t0 > a.timeout:
            emit(a.receipt, {"event":"timeout_while_governor_alive"}); return 3
        time.sleep(a.poll)
    try:
        before = query(a.smi, a.gpu)
        restored = abs(before - a.start_w) < 1.0
        rc = 0
        if not restored:
            lock_path = f"/tmp/omnicompass-gpu-{a.gpu}.power-limit.lock"
            with open(lock_path, "a+", encoding="utf-8") as lock:
                fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
                r = run([a.smi, "-i", str(a.gpu), "-pl", str(int(a.start_w))]); rc = r.returncode
                fcntl.flock(lock.fileno(), fcntl.LOCK_UN)
            after = query(a.smi, a.gpu)
            restored = rc == 0 and abs(after - a.start_w) < 1.0
        else:
            after = before
        emit(a.receipt, {"event":"governor_exit", "before_w":before, "after_w":after,
                         "restore_attempted": abs(before-a.start_w) >= 1.0, "restore_rc":rc, "restored":restored})
        return 0 if restored else 2
    except Exception as e:
        emit(a.receipt, {"event":"watchdog_error", "error":f"{type(e).__name__}: {e}", "restored":False}); return 2

if __name__ == "__main__":
    raise SystemExit(main())
