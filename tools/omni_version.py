#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The engines, fingerprinted file by file: Omni v23, the engine that stands (OMNI_V23.json, docs/OMNI_V23.md), Omni v22 (OMNI_V22.json), Omni v21 (OMNI_V21.json), Omni v20 (OMNI_V20.json), Omni v19 (OMNI_V19.json), Omni v18 (OMNI_V18.json), Omni v17 (OMNI_V17.json), Omni v16 (OMNI_V16.json), Omni v15 (OMNI_V15.json), Omni v14 (OMNI_V14.json), Omni v13 (OMNI_V13.json), Omni v12 (OMNI_V12.json), Omni v11 (OMNI_V11.json), Omni v10 (OMNI_V10.json), Omni v9
(OMNI_V9.json), Omni v8 (OMNI_V8.json),
Omni v7 (OMNI_V7.json),
Omni v6 (OMNI_V6.json), Omni v5 (OMNI_V5.json,
docs/OMNI_V5.md), then the frozen v3 (OMNI_V3.json, docs/OMNI_V3.md), v2 (OMNI_V2.json, docs/OMNI_V2.md) and v1
(OMNI_V1.json, docs/OMNI_V1.md), each kept for its own results. v5 adds the v5 compass law (realms/compass_arm_v5.py) and its arm in the harness to v3's engine; while
v5 is in active development its fingerprint is re-declared on each engine change, and no v5 result is published until the
v5 freeze. No result is ever read across versions.

  python3 tools/omni_version.py                 check this checkout: prints "omni-v23", "omni-v22", "omni-v21", "omni-v20", "omni-v19", "omni-v18", "omni-v17", "omni-v16", "omni-v15", "omni-v14", "omni-v13", "omni-v12", "omni-v11", "omni-v10", "omni-v9", "omni-v8", "omni-v7", "omni-v6", "omni-v5", "omni-v3", "omni-v2" or "omni-v1", or what differs from the newest
  python3 tools/omni_version.py --commit <sha>  the same, for the engine as it stood at a git commit (any result's run)
  python3 tools/omni_version.py --write v5      write OMNI_V5.json from this checkout (only when a new version is declared or re-declared in development)

The engine is the compass law, the live controllers, the realms and their organisms, and the runners of the
independent simulators. One SHA-256 per file, and one over the sorted list. A result is a v2 result only if the commit
it ran on carries exactly v2's bytes; a v1 result only if it carries v1's. No result is read across versions.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSIONS = {"v23": ROOT / "OMNI_V23.json", "v22": ROOT / "OMNI_V22.json", "v21": ROOT / "OMNI_V21.json", "v20": ROOT / "OMNI_V20.json", "v19": ROOT / "OMNI_V19.json", "v18": ROOT / "OMNI_V18.json", "v17": ROOT / "OMNI_V17.json", "v16": ROOT / "OMNI_V16.json", "v15": ROOT / "OMNI_V15.json", "v14": ROOT / "OMNI_V14.json", "v13": ROOT / "OMNI_V13.json", "v12": ROOT / "OMNI_V12.json", "v11": ROOT / "OMNI_V11.json", "v10": ROOT / "OMNI_V10.json", "v9": ROOT / "OMNI_V9.json", "v8": ROOT / "OMNI_V8.json", "v7": ROOT / "OMNI_V7.json", "v6": ROOT / "OMNI_V6.json", "v5": ROOT / "OMNI_V5.json", "v3": ROOT / "OMNI_V3.json", "v2": ROOT / "OMNI_V2.json",
            "v1": ROOT / "OMNI_V1.json"}     # newest first
# omni-v15 (21 October): every wire that holds a governor's rules is in the fingerprint, so no rule can change without the
# version changing (docs/CHANGE_CONTROL.md, "Gaps this page names"). A version declared before them never covered them
LATE_WIRES = ("tools/run_redis.py", "tools/run_kafka.py", "tools/run_pgbench.py", "tools/run_sysbench.py", "tools/run_ycsb.py",
              "tools/run_swarm.py", "tools/run_mujoco.py", "tools/run_cpu_power.py")
# omni-v18 (23 October): Omni direct, Omni-Compass's own orchestrator run on the muscles with no Kubernetes, is part of the
# engine: its brain, control plane, room rule, hand, walls and front hold rules, so they are fingerprinted like every other
# wire (its showing's workload and clients, omni_orchestrator/workload.py and load.py, are the harness and stay outside).
# A version declared before omni-v18 never covered them
ORCHESTRATOR_WIRES = ("omni_orchestrator/__init__.py", "omni_orchestrator/agent.py", "omni_orchestrator/brain.py",
                      "omni_orchestrator/cgroup.py", "omni_orchestrator/control.py", "omni_orchestrator/front.py",
                      "omni_orchestrator/scheduler.py")
# omni-v22 (30 October): the store wires' shared rules are part of the engine: the max on a store's memory knob (the working set's
# floor, the store's own account of a miss's cost, the gate, the host's room) and the knob verdict every store wire's tune-down runs
# through, so neither changes without the version changing. A version declared before omni-v22 never covered them
STORE_WIRES = ("tools/store_brain.py", "tools/knob_verdict.py")
SCOPE = ("omnicompass", "omni_controller", "realms", "tools/run_kil.py", "tools/run_citylearn.py", "tools/run_pandapower.py",
         *LATE_WIRES, *ORCHESTRATOR_WIRES, *STORE_WIRES)


def engine_files(commit: str | None = None) -> dict[str, str]:
    ref = commit or "HEAD"
    # a commit's engine is what its tree holds; this checkout's engine is every tracked or staged file (so a file added
    # for a new version is fingerprinted before its first commit, never after)
    cmd = ["git", "ls-tree", "-r", "--name-only", ref, "--", *SCOPE] if commit else ["git", "ls-files", "--", *SCOPE]
    names = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, check=True).stdout.split()
    # a partial checkout (a workflow's sparse checkout) leaves some engine files out of the folder while the index still
    # holds them: those, and only those, are read from the index, so a sparse list that misses a folder a new version
    # took in is not a crash (24 October: omni_orchestrator/ was in no grid workflow's list, and every conductor and grid
    # run on omni-v18 stopped here); a file deleted by hand from a full checkout is still read from the folder and fails
    outside = set() if commit else {line[2:] for line in subprocess.run(
        ["git", "ls-files", "-t", "--", *SCOPE], cwd=ROOT, capture_output=True, text=True, check=True).stdout.splitlines()
        if line.startswith("S ")}
    out = {}
    for n in sorted(names):
        if not n.endswith((".py", ".csv")) or "__pycache__" in n:
            continue
        data = (subprocess.run(["git", "show", f"{ref}:{n}" if commit else f":{n}"], cwd=ROOT, capture_output=True,
                               check=True).stdout
                if commit or n in outside else (ROOT / n).read_bytes())
        out[n] = hashlib.sha256(data).hexdigest()
    return out


def digest(files: dict[str, str]) -> str:
    return hashlib.sha256("".join(f"{h}  {n}\n" for n, h in sorted(files.items())).encode()).hexdigest()


def own_files(files: dict[str, str], want: dict[str, str]) -> dict[str, str]:
    """A tree's engine files as a version's fingerprint covers them. A version declared before omni-v15 took the late wires
    into the scope (its list names none of them) is read without those eight files and only those: a tree carrying
    omni-v14's 47 files byte for byte is omni-v14 whatever the late wires hold, because its fingerprint never covered them,
    while any other file it does not list (a new rule, a new module) still makes it a different engine."""
    out = dict(files)
    if not any(n in want for n in LATE_WIRES):
        out = {n: h for n, h in out.items() if n not in LATE_WIRES}
    if not any(n in want for n in ORCHESTRATOR_WIRES):   # a version declared before omni-v18 took Omni direct in
        out = {n: h for n, h in out.items() if n not in ORCHESTRATOR_WIRES}
    if not any(n in want for n in STORE_WIRES):          # a version declared before omni-v22 took the store wires' shared rules in
        out = {n: h for n, h in out.items() if n not in STORE_WIRES}
    return out


def version_match(files: dict[str, str]) -> tuple[str, dict] | None:
    """('omni-vN', the version's record) for a set of engine files that carries a version's own files byte for byte, else None."""
    for v, path in VERSIONS.items():
        if not path.exists():
            continue
        rec = json.loads(path.read_text())
        own = own_files(files, rec["files"])
        if set(own) == set(rec["files"]) and digest(own) == rec["digest"]:
            return f"omni-{v}", rec
    return None


def version_of(files: dict[str, str]) -> str | None:
    """'omni-v2', 'omni-v1' or None, for a set of engine files."""
    m = version_match(files)
    return m[0] if m else None


def version_before(files: dict[str, str]) -> tuple[str | None, list[str]]:
    """('omni-vN', [files not yet written]) for a commit that holds a strict subset of a version's engine files, every
    one of them that version's bytes (the commits between a version's freeze and a runner added inside it); else (None, [])."""
    for v, path in VERSIONS.items():
        if not path.exists():
            continue
        want = json.loads(path.read_text())["files"]
        own = own_files(files, want)
        missing = sorted(set(want) - set(own))
        if missing and set(own) <= set(want) and all(want[n] == h for n, h in own.items()):
            return f"omni-{v}", missing
    return None, []


def main() -> int:
    args = sys.argv[1:]
    commit = args[args.index("--commit") + 1] if "--commit" in args and len(args) > args.index("--commit") + 1 else None
    if "--commit" in args and not (commit or "").strip():
        print("--commit needs a commit; an empty one is not the working tree", file=sys.stderr); return 2
    files = engine_files(commit)
    if "--write" in args:
        v = args[args.index("--write") + 1] if len(args) > args.index("--write") + 1 and not args[args.index("--write") + 1].startswith("-") else next(iter(VERSIONS))
        if v not in VERSIONS:
            print(f"unknown version {v}; one of {sorted(VERSIONS)}", file=sys.stderr); return 2
        VERSIONS[v].write_text(json.dumps({"version": f"omni-{v}", "digest": digest(files), "files": files}, indent=1) + "\n")
        print(f"{VERSIONS[v].name} written: {len(files)} files, digest {digest(files)[:16]}")
        return 0
    m = version_match(files)
    if m:                                             # the version's own digest and file count, as its fingerprint records them
        print(f"{m[0]} (digest {m[1]['digest'][:16]}, {len(m[1]['files'])} files)")
        return 0
    v, missing = version_before(files)
    if v:
        # a commit from before a runner was written, every other engine file that version's bytes: the version's result
        # for every test but the one that runner serves (which could not have run there), and the line says so
        print(f"{v} ({len(files)} of {len(files) + len(missing)} files, all {v[5:]} bytes; not yet in this commit: {', '.join(missing)})")
        return 0
    newest = next((v for v in VERSIONS if VERSIONS[v].exists()), None)
    if newest is None:                                 # no version declared yet (e.g. before the first --write)
        print(f"no declared version (digest {digest(files)[:16]}, {len(files)} files)")
        return 1
    want = json.loads(VERSIONS[newest].read_text())
    for n in sorted(set(files) | set(want["files"])):
        if files.get(n) != want["files"].get(n):
            print(f"differs from omni-{newest}: {n}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
