#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Every set the jump generator ever ran, run again on another machine: the Python, the C++ harness and the page's own code.

A set's record (results/engine_runs/ENGINE_RUNS_<runs>_<base>.json, results/core_runs/CORE_RUNS_<runs>_<base>.json) was written
on the machine that ran it, GitHub's for nearly all. This tool runs every recorded set again from its base on the machine it is
started on, three ways, and compares each digest with the record's:

  the Python      tools/engine_runs.py (the brain's RK4, the compass law, the verdict) and tools/core_runs.py (the core's Monte Carlo)
  the C++         cpp/build/oc_engine_runs and cpp/build/oc_core_runs, the C++ twins, fed the Python's draws
  the page        the live engine page's own ported engine and loop, and its own port of the core, run in node

A set whose record was made on an engine whose law differs from the checkout's gives another digest here: it reads "another
engine's law" and is run again with --at-own-commit, from the commit its own record names, so that every digest is reproduced
from the code that made it. Nothing in a record is changed: what is found is written to its own dated file.

  python3 tools/runs_reproof.py [--workers 2] [--out results/runs_reproof/REPROOF_<UTC date>.json]
  python3 tools/runs_reproof.py --at-own-commit      the sets that read another engine's law: each from its own commit (the Python)
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
import platform
import re
import subprocess
import sys
import tempfile
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
PAGE = ROOT / "docs" / "engine" / "OMNI_COMPASS_LIVE_ENGINE.html"
CPP_E, CPP_C = ROOT / "cpp" / "build" / "oc_engine_runs", ROOT / "cpp" / "build" / "oc_core_runs"
OUT_DIR = ROOT / "results" / "runs_reproof"


def _quiet(fn, *a, **k):
    """Call a tool's function with its printing held back; returns (its value, what it printed)."""
    import contextlib
    import io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        v = fn(*a, **k)
    return v, buf.getvalue()


def engine_set(path: str) -> dict:
    from tools import engine_runs as E
    rec = json.loads(Path(path).read_text(encoding="utf-8"))
    n, base = rec["runs"], rec["base"]
    out = {"kind": "engine", "file": str(Path(path).relative_to(ROOT)), "base": base, "runs": n, "engine": rec.get("engine", ""),
           "recorded": rec["digest"]}
    sets = [E.draws(k, base) for k in range(n)]
    runs = [E.run_draws(dr) for dr in sets]
    out["python"] = E.digest(runs)
    out["python_same"] = out["python"] == rec["digest"]
    out["ladder_same"] = all(E.digest(runs[:g["runs"]]) == g["digest"] for g in rec.get("ladder") or [])
    if CPP_E.exists():
        c = E.cpp_runs(sets, CPP_E)
        out["cpp"], out["cpp_same"] = c["digest"], c["digest"] == rec["digest"]
        if rec.get("inputs_digest"):
            out["draws_same"] = c["inputs_digest"] == rec["inputs_digest"]
    if PAGE.exists() and out["python_same"]:     # the page carries the checkout's law: read only where the Python's is the record's
        with tempfile.TemporaryDirectory() as t:
            tmp = Path(t) / "r.json"
            tmp.write_text(json.dumps({"runs": n, "base": base, "digest": rec["digest"],     # every rung against the Python's own
                                       "ladder": [{"runs": m, "digest": E.digest(runs[:m])} for m in E.LADDER if m <= n]}))
            _quiet(E.verify, PAGE, n, base, tmp)
            pg = json.loads(tmp.read_text()).get("page") or {}
        out["page"], out["page_same"] = pg.get("digest"), pg.get("same")
        out["page_ladder_same"] = all(g.get("same") for g in pg.get("ladder") or [])
    return out


def core_set(path: str) -> dict:
    from tools import core_runs as C
    rec = json.loads(Path(path).read_text(encoding="utf-8"))
    n, base = rec["runs"], rec["base"]
    out = {"kind": "core", "file": str(Path(path).relative_to(ROOT)), "base": base, "runs": n, "recorded": rec["digest"]}
    if rec.get("system"):                        # a set of someone's own system: its ranges are its record's, not run again here
        out["own_system"] = rec["system"].get("name", "")
        return out
    runs = [C.one(k, base) for k in range(n)]
    out["python"] = C.digest(runs)
    out["python_same"] = out["python"] == rec["digest"]
    if CPP_C.exists():
        c = C.cpp_runs(n, base, None, CPP_C)
        out["cpp"], out["cpp_same"] = c["digest"], c["digest"] == rec["digest"]
    if PAGE.exists() and out["python_same"]:
        with tempfile.TemporaryDirectory() as t:
            tmp = Path(t) / "r.json"
            tmp.write_text(json.dumps({"runs": n, "base": base, "digest": rec["digest"]}))
            _quiet(C.verify, PAGE, n, base, None, tmp)
            pg = json.loads(tmp.read_text()).get("page") or {}
        out["page"], out["page_same"] = pg.get("digest"), pg.get("same")
    return out


def one(job):
    kind, path = job
    try:
        return engine_set(path) if kind == "engine" else core_set(path)
    except Exception as e:                       # a set that cannot be run again says so; it never passes silently
        return {"kind": kind, "file": str(Path(path).relative_to(ROOT)), "error": f"{type(e).__name__}: {str(e)[:300]}"}


def machine() -> dict:
    def first(cmd):
        try:
            return (subprocess.run(cmd, capture_output=True, text=True, timeout=30).stdout.strip().splitlines() or [""])[0]
        except (OSError, subprocess.SubprocessError):
            return ""
    return {"platform": platform.platform(), "processor": platform.machine(), "python": platform.python_version(),
            "compiler": first(["c++", "--version"]), "node": first(["node", "--version"]),
            "checkout": first(["git", "-C", str(ROOT), "rev-parse", "HEAD"]),
            "engine": first([sys.executable, str(ROOT / "tools" / "omni_version.py")]),
            "page_sha256": hashlib.sha256(PAGE.read_bytes()).hexdigest() if PAGE.exists() else None}


def at_own_commit(rows: list, workers: int) -> list:
    """The sets whose record another engine's law made: each engine's sets run again in a checkout of one of its own records'
    commits (the Python; the law's files are the fingerprint's, so every commit of one engine carries the same law)."""
    by = {}
    for r in rows:
        if r.get("kind") == "engine" and r.get("python_same") is False:
            v = re.search(r"omni-v\d+", r.get("engine", ""))
            by.setdefault(v.group(0) if v else "unversioned", []).append(r)
    done = []
    for eng, rs in sorted(by.items()):
        commit = None
        for r in rs:
            g = json.loads((ROOT / r["file"]).read_text(encoding="utf-8")).get("github") or {}
            if g.get("commit") and subprocess.run(["git", "-C", str(ROOT), "cat-file", "-e", g["commit"] + "^{commit}"], capture_output=True).returncode == 0:
                commit = g["commit"]
                break
        if not commit:
            done += [dict(r, own_commit=None, own_note="no commit of its record is in this checkout's history") for r in rs]
            continue
        with tempfile.TemporaryDirectory(dir=str(ROOT.parent)) as t:
            wt = Path(t) / "wt"
            subprocess.run(["git", "-C", str(ROOT), "worktree", "add", "-q", "--detach", "--no-checkout", str(wt), commit], check=True)
            try:
                subprocess.run(["git", "-C", str(wt), "sparse-checkout", "set", "--no-cone", "/omnicompass/", "/tools/", "/omni_controller/", "/realms/", "/*.json", "/*.py"], check=True)
                subprocess.run(["git", "-C", str(wt), "checkout", "-q"], check=True)
                code = ("import sys,json;sys.path.insert(0,'.');from tools import engine_runs as E;"
                        "b=int(sys.argv[1]);n=int(sys.argv[2]);print(E.digest([E.one_run(k,b) for k in range(n)]))")
                for r in rs:
                    p = subprocess.run([sys.executable, "-c", code, str(r["base"]), str(r["runs"])], cwd=wt, capture_output=True, text=True)
                    d = p.stdout.strip().splitlines()[-1] if p.returncode == 0 and p.stdout.strip() else None
                    done.append(dict(r, own_commit=commit, own_python=d, own_python_same=(d == r["recorded"]) if d else None,
                                     **({"own_note": (p.stderr or "")[-200:]} if not d else {})))
            finally:
                subprocess.run(["git", "-C", str(ROOT), "worktree", "remove", "--force", str(wt)], capture_output=True)
    return done


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--out", default="")
    ap.add_argument("--at-own-commit", action="store_true")
    ap.add_argument("--limit", type=int, default=0, help=argparse.SUPPRESS)
    a = ap.parse_args(argv)
    day = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    out = Path(a.out) if a.out else OUT_DIR / f"REPROOF_{day}.json"
    if a.at_own_commit:
        data = json.loads(out.read_text(encoding="utf-8"))
        own = at_own_commit(data["sets"], a.workers)
        by = {r["file"]: r for r in own}
        data["sets"] = [by.get(r["file"], r) for r in data["sets"]]
        out.write_text(json.dumps(data, indent=1) + "\n", encoding="utf-8")
        print(f"{len(own)} sets of other engines run again from their own commits: "
              f"{sum(1 for r in own if r.get('own_python_same'))} reproduce their record's digest")
        return 0
    jobs = [("engine", str(p)) for p in sorted((ROOT / "results" / "engine_runs").glob("ENGINE_RUNS_*.json"))]
    jobs += [("core", str(p)) for p in sorted((ROOT / "results" / "core_runs").glob("CORE_RUNS_*.json"))]
    if a.limit:
        jobs = jobs[:a.limit]
    # every set's row is kept as it lands (a line a set beside the record), so a machine that stops loses one set, not the hour
    part = out.with_suffix(".part.jsonl")
    out.parent.mkdir(parents=True, exist_ok=True)
    # a set already run again is not run twice: the rows of the file being written to (a run that added sets since) and of
    # the part file (a run that stopped); a row that ended in an error (a machine's fault, not the set's) is run again
    done = {}
    if out.exists():
        try:
            done.update({r["file"]: r for r in json.loads(out.read_text(encoding="utf-8")).get("sets") or [] if not r.get("error")})
        except (ValueError, KeyError):
            pass
    if part.exists():
        for line in part.read_text(encoding="utf-8").splitlines():
            try:
                r = json.loads(line)
                if not r.get("error"):
                    done[r["file"]] = r
            except (ValueError, KeyError):
                continue
    todo = [j for j in jobs if str(Path(j[1]).relative_to(ROOT)) not in done]
    with ProcessPoolExecutor(max_workers=a.workers) as ex, part.open("a", encoding="utf-8") as fh:
        for r in ex.map(one, todo, chunksize=1):
            done[r["file"]] = r
            fh.write(json.dumps(r) + "\n")
            fh.flush()
    rows = [done[str(Path(j[1]).relative_to(ROOT))] for j in jobs]
    data = {"tool": "tools/runs_reproof.py", "written": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "machine": machine(), "sets": rows}
    out.write_text(json.dumps(data, indent=1) + "\n", encoding="utf-8")
    part.unlink(missing_ok=True)
    e = [r for r in rows if r.get("kind") == "engine"]
    c = [r for r in rows if r.get("kind") == "core"]
    print(f"{out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}: engine sets {len(e)}, the Python the record's in "
          f"{sum(1 for r in e if r.get('python_same'))}, the C++ in {sum(1 for r in e if r.get('cpp_same'))}, the page in "
          f"{sum(1 for r in e if r.get('page_same'))}; core sets {len(c)}, the Python {sum(1 for r in c if r.get('python_same'))}, "
          f"the C++ {sum(1 for r in c if r.get('cpp_same'))}, the page {sum(1 for r in c if r.get('page_same'))}; "
          f"errors {sum(1 for r in rows if r.get('error'))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
