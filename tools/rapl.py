# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The machine's own energy meter (evidence class P): the processor's RAPL counters, read from Linux's powercap files
(/sys/class/powercap/intel-rapl:*; Intel, and AMD since Zen through the same driver). The machine's energy is the sum of
its package zones and its memory (dram) zones; the core and uncore zones are parts of a package and are never added
again; a platform (psys) zone is recorded beside it, never added. A counter wraps at its max_energy_range_uj: the sampler
reads every few seconds and adds each step's increase, a wrap counted as such, so a window of any length is measured
whole. Reading the counters needs root on Linux 5.10 and later. A virtual machine (GitHub's runners among them) shows no
zones: there is then no meter, and the run says so.

  python3 tools/rapl.py probe                       the zones, the counted ones marked; exit 2 when there is no meter
  python3 tools/rapl.py sample --out rapl.csv       sample every 5 s until stopped (epoch, cumulative joules per zone)
  python3 tools/rapl.py window rapl.csv T0 T1       joules and mean watts of the machine between two epochs (JSON)
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = os.environ.get("RAPL_ROOT", "/sys/class/powercap")   # RAPL_ROOT: a made-up tree, for the tests only
COUNTED = ("package", "dram")          # the machine's energy: its packages and its memory, nothing counted twice


def kind(name):
    """A zone's kind from its own name: package-0 -> package, dram -> dram, psys -> psys, core, uncore."""
    n = name.strip().lower()
    for k in ("package", "dram", "psys", "core", "uncore"):
        if n.startswith(k):
            return k
    return "other"


def zones(root=ROOT):
    """Every RAPL zone under the powercap root, top level and sub-zones, in a stable order."""
    out = []
    for p in sorted(Path(root).glob("intel-rapl:*")):
        if not (p / "energy_uj").exists():
            continue
        name = (p / "name").read_text().strip() if (p / "name").exists() else p.name
        try:
            rng = int((p / "max_energy_range_uj").read_text().split()[0])
        except (OSError, ValueError, IndexError):
            rng = 0
        out.append({"zone": p.name, "name": name, "kind": kind(name), "path": str(p), "max_range_uj": rng,
                    "counted": kind(name) in COUNTED})
    return out


def read_uj(z):
    return int(Path(z["path"], "energy_uj").read_text().split()[0])


def virt():
    """What the machine is, as systemd sees it ("none" on bare metal); empty when the tool is missing."""
    if not shutil.which("systemd-detect-virt"):
        return ""
    r = subprocess.run(["systemd-detect-virt"], capture_output=True, text=True)
    return (r.stdout or "").strip() or "none"


def probe(root=ROOT):
    zs = zones(root)
    readable = []
    for z in zs:
        try:
            read_uj(z)
            readable.append(z)
        except OSError:
            pass
    counted = [z for z in readable if z["counted"]]
    return {"zones": zs, "readable": [z["zone"] for z in readable], "counted": [z["zone"] for z in counted],
            "virtualization": virt(), "meter": bool([z for z in counted if z["kind"] == "package"])}


class Accumulator:
    """Cumulative joules per zone from raw counter readings, a wrap at max_range_uj counted as one wrap."""

    def __init__(self, zs):
        self.zs = zs
        self.last = {}
        self.total = {z["zone"]: 0.0 for z in zs}

    def add(self, raw):
        for z in self.zs:
            k, v = z["zone"], raw[z["zone"]]
            if k in self.last:
                d = v - self.last[k]
                if d < 0:                                  # the counter wrapped
                    d += z["max_range_uj"] if z["max_range_uj"] > 0 else 0
                    d = max(d, 0)
                self.total[k] += d / 1e6
            self.last[k] = v
        return dict(self.total)


def sample(out, interval=5.0, root=ROOT, count=None, clock=time.time, sleep=time.sleep):
    """Write epoch_s, machine_j (packages and memory) and each counted zone's cumulative joules, every interval."""
    zs = [z for z in zones(root) if z["counted"]]
    if not zs:
        raise SystemExit("no RAPL package or memory zone on this machine: no meter")
    acc = Accumulator(zs)
    names = [z["zone"] for z in zs]
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["epoch_s", "machine_j"] + [f"{z['zone']}:{z['name']}_j" for z in zs])
        n = 0
        while count is None or n < count:
            t = clock()
            tot = acc.add({z["zone"]: read_uj(z) for z in zs})
            w.writerow([f"{t:.3f}", f"{sum(tot.values()):.6f}"] + [f"{tot[k]:.6f}" for k in names])
            f.flush()
            n += 1
            if count is None or n < count:
                sleep(interval)


def at(rows, t):
    """Cumulative machine joules at epoch t, linear between the samples on either side; None outside the samples."""
    for (t0, j0), (t1, j1) in zip(rows, rows[1:]):
        if t0 <= t <= t1:
            return j0 if t1 == t0 else j0 + (j1 - j0) * (t - t0) / (t1 - t0)
    return None


def window(csv_path, t0, t1):
    rows = []
    with open(csv_path, newline="") as f:
        recs = list(csv.DictReader(f))
    for r in recs:
        try:                               # a last line cut short when the sampler was stopped is left out
            rows.append((float(r["epoch_s"]), float(r["machine_j"])))
        except (TypeError, ValueError):
            continue
    a, b = at(rows, t0), at(rows, t1)
    if a is None or b is None or t1 <= t0:
        return {"ok": False, "why": "the samples do not cover the window", "t0": t0, "t1": t1,
                "first": rows[0][0] if rows else None, "last": rows[-1][0] if rows else None}
    j = b - a
    return {"ok": True, "t0": t0, "t1": t1, "joules": j, "wh": j / 3600.0, "mean_w": j / (t1 - t0), "samples": len(rows)}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="what", required=True)
    p = sub.add_parser("probe"); p.add_argument("--root", default=ROOT)
    s = sub.add_parser("sample"); s.add_argument("--out", required=True); s.add_argument("--interval", type=float, default=5.0)
    s.add_argument("--root", default=ROOT)
    w = sub.add_parser("window"); w.add_argument("csv"); w.add_argument("t0", type=float); w.add_argument("t1", type=float)
    a = ap.parse_args(argv)
    if a.what == "probe":
        r = probe(a.root)
        print(json.dumps(r, indent=1))
        return 0 if r["meter"] else 2
    if a.what == "sample":
        sample(a.out, a.interval, a.root)
        return 0
    r = window(a.csv, a.t0, a.t1)
    print(json.dumps(r, indent=1))
    return 0 if r["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
