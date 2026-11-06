#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""One arm of the group of clusters (scripts/kind_group.sh; docs/GROUP_PREREGISTRATION.md), merged from its members' records
into the files one cluster's arm has, so tools/live_reps.py reads the group as it reads any arm:

  window      opens when the group's stream starts (stream_start.txt, once every member's window is open), closes with the
              first member's window to close
  jobs.json   every job of the stream once: submitted when it was sent (to the orchestrator, or on the group alone to its
              member), done when every member's part of it is done (a part not done leaves the job unfinished)
  pods.json   every member's pods
  capture.csv the members' readings summed at each moment (the first member's clock; another member's reading within 20 s
              of it): machines in service, processors, pods waiting, the modelled watts
  latency.csv every member's probe of its own service; audit.jsonl every member's governor; host_cpu.csv the one runner's

    python3 tools/merge_group.py ARM_DIR MEMBERS ORCH"""
from __future__ import annotations

import csv
import datetime as dt
import json
import shutil
import sys
from pathlib import Path

SUM = ("nodes_ready", "nodes_total", "alloc_cpu_m", "req_cpu_m", "used_cpu_m", "pods_pending", "hpa_count",
       "hpa_current_replicas", "hpa_desired_replicas", "power_w")


def ts(s: str) -> float:
    return dt.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc).timestamp()


def iso(t: float) -> str:
    return dt.datetime.fromtimestamp(t, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def first_number(p: Path) -> float:
    return float(p.read_text().split()[0])


def items(p: Path) -> list:
    try:
        return json.loads(p.read_text()).get("items", [])
    except (OSError, ValueError):
        return []


def merge_jobs(d: Path, members: list, orch: str) -> list:
    parts: dict = {}                                       # job name -> [(member, job)]
    for m in members:
        for j in items(m / "jobs.json"):
            parts.setdefault(j["metadata"]["name"], []).append(j)
    sent, orch_done = {}, {}
    if orch != "none":                                     # the orchestrator's own record: when each job was sent to it, and,
        for j in items(d / "orch_jobs.json"):              # where its jobs are pods and not Jobs (Armada), when its last pod ended
            sent[j["metadata"]["name"]] = ts(j["metadata"]["creationTimestamp"])
            orch_done[j["metadata"]["name"]] = (j.get("status") or {}).get("completionTime")
    names = sorted(set(parts) | set(sent))
    out = []
    for n in names:
        ps = parts.get(n, [])
        sub = sent.get(n) if orch != "none" else min((ts(p["metadata"]["creationTimestamp"]) for p in ps), default=None)
        if sub is None:
            continue
        ends = [(p.get("status") or {}).get("completionTime") for p in ps]
        done = max(ts(e) for e in ends) if ps and all(ends) else None
        if done is None and not ps and orch_done.get(n):
            done = ts(orch_done[n])
        j = {"metadata": {"name": n, "creationTimestamp": iso(sub)}, "status": {"parts": len(ps)}}
        if done is not None:
            j["status"]["completionTime"] = iso(done)
        out.append(j)
    return out


def merge_capture(members: list) -> tuple:
    rows = []
    for m in members:
        try:
            with open(m / "capture.csv") as f:
                rows.append(list(csv.DictReader(f)))
        except OSError:
            rows.append([])
    if not rows or not rows[0]:
        return [], []
    fields = list(rows[0][0].keys())
    times = [[ts(r["timestamp"]) for r in rs] for rs in rows]
    merged = []
    for i, base in enumerate(rows[0]):
        t = times[0][i]
        picks = [base]
        for rs, tt in zip(rows[1:], times[1:]):
            near = min(range(len(tt)), key=lambda k: abs(tt[k] - t)) if tt else None
            if near is None or abs(tt[near] - t) > 20:
                picks = None
                break
            picks.append(rs[near])
        if picks is None:
            continue                                       # a moment some member did not read is no reading of the group
        row = dict(base)
        for k in SUM:
            vals = [p.get(k, "") for p in picks]
            try:
                row[k] = ("%.1f" if k == "power_w" else "%.0f") % sum(float(v) for v in vals) if all(v not in ("", None) for v in vals) else ""
            except ValueError:
                row[k] = ""
        merged.append(row)
    return fields, merged


def main(d: Path, n: int, orch: str) -> str:
    members = [d / f"m{i}" for i in range(1, n + 1)]
    for m in members:
        if not (m / "capture.csv").exists() or (m / "INVALID").exists():
            raise SystemExit(f"member {m.name} has no valid record")
    starts = [first_number(m / "window_start.txt") for m in members]
    ends = [first_number(m / "window_end.txt") for m in members]
    t0 = first_number(d / "stream_start.txt") if (d / "stream_start.txt").exists() else max(starts)
    t1 = min(ends)
    (d / "window_start.txt").write_text(f"{t0:.0f}\n")
    (d / "window_end.txt").write_text(f"{t1:.0f}\n")
    pre = [f"group: {n} members ({', '.join('omni-' + m.name for m in members)}), orchestrator {orch}; each member the batch rig's cluster"]
    if (d / "orch.txt").exists():
        pre += [ln for ln in (d / "orch.txt").read_text().splitlines() if ln.startswith(("orchestrator=", "members:", "propagation policy:", "placement:"))]
    pre += (members[0] / "preflight.txt").read_text().splitlines()
    (d / "preflight.txt").write_text("\n".join(pre) + "\n")
    jobs = merge_jobs(d, members, orch)
    (d / "jobs.json").write_text(json.dumps({"items": jobs}, indent=1) + "\n")
    pods = [p for m in members for p in items(m / "pods.json")]
    (d / "pods.json").write_text(json.dumps({"items": pods}) + "\n")
    fields, cap = merge_capture(members)
    with open(d / "capture.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(cap)
    lat = []
    for m in members:
        try:
            with open(m / "latency.csv") as f:
                r = list(csv.DictReader(f))
                lat_fields = list(r[0].keys()) if r else None
                lat += r
        except OSError:
            continue
    if lat:
        lat.sort(key=lambda r: float(r.get("elapsed_seconds") or 0))
        with open(d / "latency.csv", "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=lat_fields)
            w.writeheader()
            w.writerows(lat)
    for name in ("audit.jsonl", "pod_watch.json"):   # every governor's record; every serving pod's start (distinct ids)
        if any((m / name).exists() for m in members):
            with open(d / name, "w") as out:
                for m in members:
                    if (m / name).exists():
                        text = (m / name).read_text()
                        out.write(text if text.endswith("\n") or not text else text + "\n")
    if (members[0] / "host_cpu.csv").exists():
        shutil.copy(members[0] / "host_cpu.csv", d / "host_cpu.csv")
    stayed = [(m / "omni_stayed_native.txt").exists() for m in members]
    if all(stayed):
        (d / "omni_stayed_native.txt").write_text("every member's governor decided at every step and wrote nothing\n")
    done = sum(1 for j in jobs if "completionTime" in j["status"])
    return f"{len(jobs)} jobs ({done} done), {len(pods)} pods, {len(cap)} group readings, window {t1 - t0:.0f} s"


if __name__ == "__main__":
    print(main(Path(sys.argv[1]), int(sys.argv[2]), sys.argv[3]))

# © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
