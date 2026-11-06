#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Every test file that `python -m unittest discover` never collects, run in its own process (verify.py).

unittest collects only TestCase classes. On 18 October 76 of the 124 files in tests/ held none: their checks are plain
test_* functions or a main() under `if __name__ == "__main__"`, so the whole-suite step passed without running them, and
verify.py called only some of them by name. This runs each such file that verify.py does not already call: its top-level
test_* functions in order (one parameter named tmp_path gets a fresh directory, as pytest gives), or else its main().
One file's failure fails the run, with the file's own last lines.

  python3 tools/function_tests.py            every such file, four at a time; exit 1 if any fails
  python3 tools/function_tests.py --list     which files, and how each is run
  python3 tools/function_tests.py --one F    one file, in this process
"""
from __future__ import annotations

import argparse
import ast
import importlib
import inspect
import os
import re
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TIMEOUT = 900


def how(path: Path) -> str:
    """unittest (a TestCase class), functions (top-level test_*), main, or none."""
    tree = ast.parse(path.read_text(), str(path))
    if any(isinstance(n, ast.ClassDef) and any("TestCase" in ast.unparse(b) for b in n.bases) for n in ast.walk(tree)):
        return "unittest"
    tops = [n.name for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
    if any(t.startswith("test_") for t in tops):
        return "functions"
    return "main" if "main" in tops else "none"


def called_by_verify() -> set[str]:
    text = (ROOT / "verify.py").read_text()                 # a whole name: test_robust is not test_robust_restart
    return {p.stem for p in (ROOT / "tests").glob("test_*.py") if re.search(rf"\b{p.stem}\b", text)}


def files() -> list[tuple[Path, str]]:
    skip = called_by_verify()
    out = []
    for p in sorted((ROOT / "tests").glob("test_*.py")):
        h = how(p)
        if h in ("functions", "main") and p.stem not in skip:
            out.append((p, h))
    return out


def one(path: Path) -> int:
    sys.path.insert(0, str(ROOT))
    os.chdir(ROOT)
    mod = importlib.import_module(f"tests.{path.stem}")
    h = how(path)
    if h == "main":
        r = mod.main()                                          # a check fails by raising; a main() that returns its
        failed = r is False or (type(r) is int and r != 0)      # result passes, one that returns an exit code is read
        return 1 if failed else 0
    for name, fn in [(n, getattr(mod, n)) for n in dir(mod) if n.startswith("test_")]:
        if not inspect.isfunction(fn) or fn.__module__ != mod.__name__:
            continue
        params = list(inspect.signature(fn).parameters)
        if params and params != ["tmp_path"]:
            print(f"{path.name}::{name} asks for {params}: only tmp_path is given here")
            return 1
        if params:
            with tempfile.TemporaryDirectory() as t:
                fn(Path(t))
        else:
            fn()
    return 0


def run(path: Path) -> tuple[Path, int, float, str]:
    t0 = time.time()
    try:
        r = subprocess.run([sys.executable, str(Path(__file__).resolve()), "--one", str(path)], cwd=ROOT,
                           capture_output=True, text=True, timeout=TIMEOUT)
        return path, r.returncode, time.time() - t0, (r.stdout + r.stderr)[-1500:]
    except subprocess.TimeoutExpired:
        return path, 124, time.time() - t0, f"over {TIMEOUT} s"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--one")
    ap.add_argument("--jobs", type=int, default=4)
    a = ap.parse_args(argv)
    if a.one:
        return one(Path(a.one))
    todo = files()
    if a.list:
        for p, h in todo:
            print(f"{h:9} {p.relative_to(ROOT)}")
        return 0
    with ThreadPoolExecutor(a.jobs) as ex:
        done = list(ex.map(run, [p for p, _ in todo]))
    bad = [d for d in done if d[1] != 0]
    for p, rc, s, _ in done:
        print(f"{'ok  ' if rc == 0 else 'FAIL'} {s:6.1f} s  {p.relative_to(ROOT)}")
    for p, rc, _, tail in bad:
        print(f"\n== {p.relative_to(ROOT)} (exit {rc})\n{tail}")
    print(f"\n{len(done) - len(bad)} of {len(done)} files pass")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
