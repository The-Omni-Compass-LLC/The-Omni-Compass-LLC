#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""How much of the engine the tests run: line coverage of every Python file in the engine that stands, under the whole
test suite (docs/ENGINE_COVERAGE.md).

The measurement runs every test the repository has (the unittest suite, then each file tools/function_tests.py runs) under
coverage.py, counting only the engine's fingerprinted Python files, and keeps one line per file in
results/ENGINE_COVERAGE.json. It takes about a quarter of an hour, so verify.py checks only that the page is what the record
says; the record names the commit it was measured on.

  python3 tools/engine_coverage.py --measure   run the whole suite under coverage and write the record and the page
  python3 tools/engine_coverage.py             write the page from the record
  python3 tools/engine_coverage.py --check     exit 1 if the page is not what the record gives
"""
from __future__ import annotations

import argparse, json, os, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.legal import stamp  # noqa: E402

DATA = ROOT / "results" / "ENGINE_COVERAGE.json"
PAGE = ROOT / "docs" / "ENGINE_COVERAGE.md"


def engine_manifest():
    from tools import omni_version as ov
    ver = ov.version_of(ov.engine_files()) or "unversioned"
    files = json.loads((ROOT / f"OMNI_V{ver.split('v')[-1]}.json").read_text())["files"] if ver.startswith("omni-v") else []
    return ver, sorted(f for f in files if f.endswith(".py"))


def measure() -> dict:
    ver, files = engine_manifest()
    inc = ",".join(files)
    with tempfile.TemporaryDirectory() as t:
        env = {**os.environ, "COVERAGE_FILE": str(Path(t) / ".coverage")}
        py = [sys.executable, "-m", "coverage", "run", f"--include={inc}"]
        subprocess.run(py + ["-m", "unittest", "discover", "-s", "tests", "-t", "."], cwd=ROOT, env=env,
                       capture_output=True, text=True)
        listed = subprocess.run([sys.executable, "tools/function_tests.py", "--list"], cwd=ROOT, capture_output=True,
                                text=True).stdout.split("\n")
        for ln in listed:
            parts = ln.split()
            if len(parts) == 2 and parts[1].startswith("tests/") and parts[1].endswith(".py"):
                # `coverage run --append`: without `run` coverage refuses the option and the file runs untraced
                r = subprocess.run(py[:4] + ["--append", f"--include={inc}", "tools/function_tests.py", "--one", parts[1]],
                                   cwd=ROOT, env=env, capture_output=True, text=True, timeout=900)
                if "no such option" in r.stderr or "Unknown command" in r.stderr:
                    raise SystemExit(f"coverage refused the command for {parts[1]}: {r.stderr.strip()[:200]}")
        out = Path(t) / "cov.json"
        subprocess.run([sys.executable, "-m", "coverage", "json", "-o", str(out)], cwd=ROOT, env=env, capture_output=True)
        rep = json.loads(out.read_text())
    sha = "commit `" + subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()[:12] + "`"
    per = {f: {"statements": v["summary"]["num_statements"], "missed": v["summary"]["missing_lines"]}
           for f, v in sorted(rep["files"].items())}
    return {"engine": ver, "commit": sha, "files": per}


def late_wires_line(d: dict) -> list[str]:
    """The share the eight runners omni-v15 took into the fingerprint hold (tools/omni_version.py, LATE_WIRES), apart from
    the rest: they are run chiefly by their own benchmarks on GitHub, so the whole engine's figure fell when they came in
    while the files that were in it before kept theirs."""
    from tools import omni_version as ov
    late = [f for f in d["files"] if f in ov.LATE_WIRES]
    if not late:
        return []
    def share(fs):
        s = sum(d["files"][f]["statements"] for f in fs); m = sum(d["files"][f]["missed"] for f in fs)
        return s, 100 * (s - m) / max(1, s)
    ls, lp = share(late)
    rs, rp = share([f for f in d["files"] if f not in ov.LATE_WIRES])
    return [f"The {len(late)} runners omni-v15 took into the fingerprint (the data stores', the swarm's, MuJoCo's and the CPU "
            f"power runner, `tools/run_*.py`) hold {ls:,} of these statements, {lp:.0f}% of them run under the tests: each is "
            f"run whole by its own benchmark on GitHub, A, B and C, rather than by a unit test. The other {len(d['files']) - len(late)} Python "
            f"files, the engine as it stood before them, hold {rs:,}, {rp:.0f}% run. The whole figure fell when those runners "
            "came in; no test was lost.", ""]


def page(d: dict) -> str:
    tot = sum(v["statements"] for v in d["files"].values())
    miss = sum(v["missed"] for v in d["files"].values())
    rows = sorted(((f, v) for f, v in d["files"].items() if v["statements"]),        # an empty __init__.py has nothing to run
                  key=lambda kv: (kv[1]["statements"] - kv[1]["missed"]) / kv[1]["statements"])
    from tools.omni_version import VERSIONS                     # newest first: the engine that stands
    newest = f"omni-{next(iter(VERSIONS))}"
    # the record names the engine it was measured on; after a landing it is the engine before the one that stands until the
    # next --measure, and the page says so rather than calling the measured engine the one that stands (24 October, omni-v19)
    which = (f"the engine that stands ({d['engine']})" if d["engine"] == newest else
             f"the engine it was measured on ({d['engine']}; {newest}, the engine that stands since, is measured at the next `--measure`)")
    L = ["# How much of the engine the tests run", "",
         f"Line coverage of every Python file in {which}, under the whole test suite: the "
         "unittest suite and every file `tools/function_tests.py` runs. Measured with coverage.py by `python3 "
         f"tools/engine_coverage.py --measure` on {d['commit']}; `tools/engine_coverage.py --check`, run by "
         "`verify.py`, fails a push where this page is not what `results/ENGINE_COVERAGE.json` records.", "",
         f"**{100 * (tot - miss) / tot:.0f}% of the engine's {tot:,} statements run under the tests** "
         f"({tot - miss:,} run, {miss:,} not). Coverage counts lines a test executes, not what it asserts: the properties "
         "the tests check are in `tests/test_engine_properties.py`, and the proofs of the core in `docs/ENGINE_PROOFS.md`.", "",
         *late_wires_line(d),
         "| Engine file | Statements | Run by the tests | Coverage |", "|---|---:|---:|---:|"]
    for f, v in rows:
        s, m = v["statements"], v["missed"]
        L.append(f"| `{f}` | {s:,} | {s - m:,} | {100 * (s - m) / max(1, s):.0f}% |")
    low = [f for f, v in rows if v["statements"] and (v["statements"] - v["missed"]) / v["statements"] < 0.6]
    L += ["", "## Where the tests reach least", "",
          "Files under 60%: " + (", ".join(f"`{f}`" for f in low) if low else "none") + ". The CityLearn runner and the "
          "runners of the data stores and the swarm are exercised by their own benchmarks on GitHub (`citylearn.yml`, "
          "`redis.yml` and the rest, three runs on every engine) rather than by a unit test; "
          "the stack simulator, the shield and the speed and mathdrive modules hold paths the live governors do not call. "
          "Raising each to the level of the rest is the next tests' work: no engine file changes for a test.", ""]
    return "\n".join(L) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--measure", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--from-json", help="a coverage.py JSON report to record instead of measuring (its engine and commit given)")
    a = ap.parse_args(argv)
    if a.measure:
        d = measure()
        DATA.write_text(json.dumps(d, indent=1) + "\n")
    elif a.from_json:
        rep = json.loads(Path(a.from_json).read_text())
        ver, _ = engine_manifest()
        sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()[:12]
        d = {"engine": ver, "commit": sha, "files": {f: {"statements": v["summary"]["num_statements"],
                                                        "missed": v["summary"]["missing_lines"]}
                                                    for f, v in sorted(rep["files"].items())}}
        DATA.write_text(json.dumps(d, indent=1) + "\n")
    d = json.loads(DATA.read_text())
    text = "\n".join(stamp(page(d).split("\n"))) + "\n"
    if a.check:
        ok = PAGE.exists() and PAGE.read_text(encoding="utf-8") == text
        print("engine coverage page: current" if ok else "engine coverage page: out of date (python3 tools/engine_coverage.py)")
        return 0 if ok else 1
    PAGE.write_text(text, encoding="utf-8")
    tot = sum(v["statements"] for v in d["files"].values()); miss = sum(v["missed"] for v in d["files"].values())
    print(f"engine coverage: {100 * (tot - miss) / tot:.0f}% of {tot:,} statements -> {PAGE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
