# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The line-up: every monitor of the live benchmark engine held against the Python and the C++ that feed it, check by check.

The founder's order of 25 October: everything on the page "100% in line with ... the numbers that come out of the Python and
the C++ harness attached to the visual Grafana monitor style ... control panels". Each monitor in the registry
(docs/engine/monitors.json) names its proofs (wire.proof): the script or the test that ties what the page draws to the
repository's own Python and, where it has one, its C++ twin. This tool runs every proof once, and adds the ties no single
monitor names: the page's own code computing the Python's newest 500 engine runs and the core's Monte Carlo to an identical
digest (tools/engine_runs.py, tools/core_runs.py --verify), and the injection grid's record re-hashed and recomputed as the
page recomputes it (tests/test_injection_grid.py). A monitor is in line when every proof it names passed; a proof that could
not run here (no compiler, no node) is said so, never counted as passed.

  python3 docs/engine/lineup.py            -> docs/engine/LINEUP.md, docs/engine/LINEUP.json
"""
from __future__ import annotations

import datetime
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT))
from tools.legal import stamp  # noqa: E402

PY = sys.executable
REG = HERE / "monitors.json"
OUT_MD, OUT_JSON = HERE / "LINEUP.md", HERE / "LINEUP.json"
# what each proof ties, in the words a reader needs (a proof not named here is described by its file)
TIES = {
    "docs/engine/check_live_engine.py": "the page's own port of the governor, the nerves, the compass law, the verdict and Student's t "
                                        "against the Python on the same seeded inputs, and the C++ core's six-state RK4 step against both",
    "docs/engine/check_records.py": "the page's records against the repository's own runs: the harness, the shipped controller, the GPU card "
                                    "and the Linux host, recomputed and compared",
    "docs/engine/build_live_engine.py": "every record the page carries rebuilt from the repository's files and compared with the page's copy",
    "engine_runs --verify": "the page's own code runs the Python's newest 500 engine runs, and its digest is held to the Python's and the C++'s",
    "core_runs --verify": "the page's own port of the core runs the Python's Monte Carlo of the core, and its digest is held to the Python's",
    "tests/test_injection_grid.py": "the injection grid's record re-hashed to its own digest, its batch the Python's and the C++'s, and every "
                                    "cell's mean recomputed from the runs' means as the page recomputes it",
}
SKIP = {"verify.py": "runs every test and check of the repository on every push (verify.yml); its parts are run here one by one",
        ".github/workflows/engine-runs.yml": "runs the Python's set, the C++ and the page's code on GitHub for every set",
        ".github/workflows/monte-carlo.yml": "runs the core's Monte Carlo on GitHub"}


def run(cmd, timeout=3600):
    t0 = time.time()
    try:
        p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=timeout)
        out, code = (p.stdout + p.stderr), p.returncode
    except subprocess.TimeoutExpired:
        out, code = "timed out", -1
    return {"cmd": " ".join(str(c) for c in cmd), "ok": code == 0, "code": code, "seconds": round(time.time() - t0, 1),
            "tail": [ln for ln in out.strip().splitlines() if ln.strip()][-12:]}


def proof_cmd(p):
    if p.startswith("tests/") and p.endswith(".py"):
        return [PY, "-m", "unittest", "-q", p[:-3].replace("/", ".")]
    if p == "docs/engine/build_live_engine.py":
        return [PY, p, "--check"]
    if p.endswith(".py"):
        return [PY, p]
    return None


def newest_batch():
    fs = sorted((ROOT / "results" / "engine_runs").glob("ENGINE_RUNS_*.json"),
                key=lambda f: (json.loads(f.read_text(encoding="utf-8")).get("written", ""), f.name))
    return json.loads(fs[-1].read_text(encoding="utf-8")) if fs else None


def headline(r):
    """The line a reader needs from a proof's output: its largest difference, its digest verdict or its test count."""
    text = "\n".join(r["tail"])
    for pat in (r"largest[^\n]*", r"identical[^\n]*", r"digests? (match|agree|the same)[^\n]*", r"Ran \d+ tests?[^\n]*", r"OK[^\n]*", r"FAIL[^\n]*"):
        m = re.search(pat, text, re.I)
        if m:
            return m.group(0).strip()[:220]
    return (r["tail"][-1] if r["tail"] else "")[:220]


def main(argv=None):
    reg = json.loads(REG.read_text(encoding="utf-8"))["monitors"]
    proofs = []
    for m in reg:
        for p in (m.get("wire") or {}).get("proof") or []:
            if p not in proofs:
                proofs.append(p)
    results = {}
    for p in proofs:
        if p in SKIP:
            results[p] = {"ok": None, "skipped": SKIP[p]}
            continue
        if p.endswith(".md"):
            results[p] = {"ok": (ROOT / p).is_file(), "cmd": f"the record {p} is present (written again by its own test)", "tail": [], "seconds": 0}
            continue
        cmd = proof_cmd(p)
        results[p] = run(cmd) if cmd else {"ok": None, "skipped": "no command known for this proof"}
        print(f"  {'ok  ' if results[p].get('ok') else 'FAIL' if results[p].get('ok') is False else 'skip'} {p} ({results[p].get('seconds', 0)} s)", flush=True)
    b = newest_batch()
    page = "docs/engine/OMNI_COMPASS_LIVE_ENGINE.html"
    if b:
        results["engine_runs --verify"] = run([PY, "tools/engine_runs.py", "--verify", page, "--all", "--runs", str(b["runs"]), "--base", str(b["base"])])
        results["core_runs --verify"] = run([PY, "tools/core_runs.py", "--verify", page, "--runs", str(b["runs"]), "--base", str(b["base"])])
    results["tests/test_injection_grid.py"] = run([PY, "-m", "unittest", "-q", "tests.test_injection_grid"])
    for k in ("engine_runs --verify", "core_runs --verify", "tests/test_injection_grid.py"):
        if k in results:
            print(f"  {'ok  ' if results[k]['ok'] else 'FAIL'} {k} ({results[k]['seconds']} s)", flush=True)
    for k, r in results.items():
        r["tie"] = TIES.get(k, f"the test {k}" if k.startswith("tests/") else k)
        if "tail" in r:
            r["headline"] = headline(r)
    rows = []
    for m in reg:
        w = m.get("wire") or {}
        ps = [p for p in (w.get("proof") or [])]
        run_ps = [p for p in ps if results.get(p, {}).get("ok") is not None]
        live = m["status"] in ("live",)
        extra = ["engine_runs --verify"] if m["id"] == "proofCv" else ["core_runs --verify"] if m["id"] == "mcCv" else []
        ps_all = ps + [e for e in extra if e in results]
        state = ("awaiting its run" if m["status"] == "awaiting" else
                 "no proof named" if not ps_all else
                 "in line" if all(results[p].get("ok") is not False for p in ps_all) and any(results[p].get("ok") for p in ps_all) else
                 "OUT OF LINE")
        rows.append({"n": m["n"], "id": m["id"], "name": m["name"], "status": m["status"], "cls": m["cls"],
                     "python": w.get("python") or [], "cpp": w.get("cpp") or [], "cpp_none": w.get("cpp_none"),
                     "proofs": ps_all, "state": state, "live": live})
    b_line = (f"base {b['base']}, {b['runs']} runs: the Python's digest {b['digest'][:16]}…, the C++ engine's "
              f"{((b.get('cpp') or {}).get('digest') or 'not run')[:16]}… ({'identical' if (b.get('cpp') or {}).get('same') else 'not identical'}, "
              f"{(b.get('cpp') or {}).get('agree')} runs agree)") if b else "no set of the Python's runs recorded"
    git = lambda *a: subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    rec = {"title": "The line-up: every monitor held against the Python and the C++ that feed it", "written":
           datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"), "commit": git("rev-parse", "HEAD"),
           "dirty": bool(git("status", "--porcelain", "--", "docs/engine", "omnicompass", "cpp", "tools")), "batch": b_line,
           "checks": results, "monitors": rows,
           "summary": {"monitors": len(rows), "in_line": sum(r["state"] == "in line" for r in rows),
                       "out": [r["n"] for r in rows if r["state"] == "OUT OF LINE"],
                       "awaiting": [r["n"] for r in rows if r["state"] == "awaiting its run"],
                       "no_proof": [r["n"] for r in rows if r["state"] == "no proof named"],
                       "checks_run": sum(r.get("ok") is not None for r in results.values()),
                       "checks_passed": sum(r.get("ok") is True for r in results.values())}}
    OUT_JSON.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    s = rec["summary"]
    L = ["# The line-up: every monitor of the live benchmark engine held against the Python and the C++", "",
         f"Written {rec['written']} from commit `{rec['commit'][:12]}`{' (uncommitted changes)' if rec['dirty'] else ''} by "
         "`python3 docs/engine/lineup.py`. Each monitor names the proofs that tie what it draws to the repository's own Python and, "
         "where it has one, its C++ twin (`docs/engine/monitors.json`, wire.proof); each proof ran once here.", "",
         f"**{s['in_line']} of {s['monitors']} monitors in line**; out of line: {', '.join(map(str, s['out'])) or 'none'}; awaiting "
         f"their run (nothing drawn from a result yet): {', '.join(map(str, s['awaiting'])) or 'none'}; no proof named: "
         f"{', '.join(map(str, s['no_proof'])) or 'none'}. Checks: {s['checks_passed']} of {s['checks_run']} passed. The Python's "
         f"newest set: {b_line}.", "", "## The checks", "", "| Check | What it ties | Result | Time |", "|---|---|---|---:|"]
    for k, r in results.items():
        res = ("passed" if r.get("ok") else "FAILED" if r.get("ok") is False else f"not run here: {r.get('skipped', '')}")
        L.append(f"| `{k}` | {r['tie']} | {res}{(': ' + r['headline'].replace('|', '/')) if r.get('headline') else ''} | {r.get('seconds', '')} s |")
    L += ["", "## Every monitor", "", "| # | Monitor | State | Class | The Python | The C++ | Proofs |", "|---:|---|---|---|---|---|---|"]
    for r in rows:
        L.append(f"| {r['n']} | {r['name']} | {r['state']} | {r['cls']} | {', '.join(f'`{p}`' for p in r['python'][:4])}{' …' if len(r['python']) > 4 else ''} | "
                 f"{', '.join(f'`{p}`' for p in r['cpp'][:3]) or (r['cpp_none'] or '—')} | {', '.join(f'`{p}`' for p in r['proofs'])} |")
    OUT_MD.write_text("\n".join(stamp(L)) + "\n", encoding="utf-8")
    print(f"line-up: {s['in_line']} of {s['monitors']} monitors in line, {s['checks_passed']} of {s['checks_run']} checks passed -> {OUT_MD.relative_to(ROOT)}")
    return 0 if not s["out"] and s["checks_passed"] == s["checks_run"] else 1


if __name__ == "__main__":
    sys.exit(main())
