# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Every serving pod of every arm, with the writes Omni-Compass made around it: the record behind the "pods started"
and "pod start wait" rows of tools/live_reps.py.

  python3 tools/pod_report.py reps            # reps/bench-<arm>-<rep>/ as benchmark-reps downloads them

For each arm and repetition: each pod's start (seconds into the measured window), its wait to Ready, the machine it
landed on; then each HPA target write and node-pool command of the controller (audit.jsonl) on the same clock; and the
per-arm totals of pods started in each fifth of the window, so it shows where the extra starts fall.
"""
from __future__ import annotations

import json, sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


def ts(s):
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp()


def pods(d):
    f = d / "pod_watch.json"
    if not f.exists():
        return []
    text = f.read_text(); dec = json.JSONDecoder(); i = 0; out = {}
    while i < len(text):
        while i < len(text) and text[i].isspace():
            i += 1
        if i >= len(text):
            break
        try:
            ev, i = dec.raw_decode(text, i)
        except ValueError:
            break
        o = ev.get("object", ev); m = o.get("metadata", {}); uid = m.get("uid")
        if not uid or not m.get("creationTimestamp"):
            continue
        r = out.setdefault(uid, {"created": ts(m["creationTimestamp"]), "ready": None, "node": "", "deleted": None})
        r["node"] = (o.get("spec") or {}).get("nodeName") or r["node"]
        if ev.get("type") == "DELETED" and r["deleted"] is None:
            r["deleted"] = ts(m.get("deletionTimestamp") or m["creationTimestamp"])
        for c in (o.get("status") or {}).get("conditions") or []:
            if c.get("type") == "Ready" and c.get("status") == "True" and c.get("lastTransitionTime") and r["ready"] is None:
                r["ready"] = ts(c["lastTransitionTime"])
    return list(out.values())


def writes(d):
    f = d / "audit.jsonl"
    out = []
    if not f.exists():
        return out
    for line in f.read_text().splitlines():
        try:
            a = json.loads(line)
        except ValueError:
            continue
        if "write" in a and a.get("time"):
            out.append((float(a["time"]), a.get("why", ""), " ".join(a["write"][1:])[:110]))
    return out


def main(root):
    root = Path(root); fifths = defaultdict(lambda: [0] * 5); removed = defaultdict(int)
    for d in sorted(root.glob("bench-*-*")):
        arm, rep = d.name.split("-")[1], d.name.split("-")[2]
        try:
            t0 = float((d / "window_start.txt").read_text().split()[0]); t1 = float((d / "window_end.txt").read_text().split()[0])
        except (OSError, ValueError, IndexError):
            continue
        ps = sorted((p for p in pods(d) if t0 <= p["created"] <= t1), key=lambda p: p["created"])
        print(f"\n## {arm} rep {rep}: {len(ps)} pods started in the window ({t1 - t0:.0f} s)")
        for p in ps:
            w = (p["ready"] if p["ready"] is not None else t1) - p["created"]
            gone = "" if p["deleted"] is None else f", removed at {p['deleted'] - t0:.0f} s"
            print(f"  pod   at {p['created'] - t0:6.0f} s  wait {max(0, w):4.0f} s  on {p['node']}{gone}")
            fifths[arm][min(4, int(5 * (p["created"] - t0) / max(1.0, t1 - t0)))] += 1
        for p in pods(d):
            if p["deleted"] is not None and t0 <= p["deleted"] <= t1:
                removed[arm] += 1
        for t, why, cmd in writes(d):
            if t0 - 60 <= t <= t1 and ("HPA target" in why or "node" in why.lower()):
                print(f"  write at {t - t0:6.0f} s  {why[:70]}")
    print("\n## pods started by fifth of the window (all repetitions), and pods removed in the window")
    for arm, f in sorted(fifths.items()):
        print(f"  {arm:7s} {f}  removed {removed[arm]}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "reps")
