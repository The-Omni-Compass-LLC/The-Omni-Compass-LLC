# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The live benchmark engine page's C++ twin panel: the Python's own runs fed through the C++ engine, every number compared.

The engine is written twice, in Python (omnicompass/, omni_controller/, realms/) and in C++ (cpp/), line for line where a
C++ twin exists (tools/seal.py lists them, and every mechanism that runs in Python only). This record is made on every
rebuild of the page, on the checkout the page is built from, with the C++ compiled there:

  twins      every twin's own parity check (the tests verify.py runs): the Python and the C++ on the same seeded inputs,
             the number of cases and the largest difference
  live       every compass law the page's own runs used while the page was built (the shipped Kubernetes controller on
             the model cluster, the GPU card, any other run that wires the law), each law's readings, in the order they came,
             with the band's center, cushion and push as they stood at each reading, fed through the C++ law
             (cpp/src/compass_law.cpp) and through the Python again; the force, position and velocity compared with the
             run's own, decision by decision
  engine runs the Python's seeded runs (tools/engine_runs.py, the newest record the page shows: 500 runs from the jump
             generator): their draws, the Python's injection, are the input of the C++ harness (cpp/tools/engine_runs.cpp: the
             governor, the nervous system, the compass law and the verdict, all C++), every receipt compared with the
             record's and the two SHA-256 digests
  organisms  the seven organisms (the spine, the four realms, the four stacked, the whole tower) at the tune-down, where
             every muscle runs the compass law (realms/compass_arm_v5.py compass_apply_v5 with V5SAVE), on the climb, seed
             3000: every muscle's law fed through the C++ the same way, organism by organism and muscle by muscle

At the max, the default brain, each organism's muscles are decided by the edge and the bone (realms/compass_arm_v5.py
max_apply, max_body_step), which have no C++ twin yet; the record says so and names them (tools/seal.py PYTHON_ONLY).
Evidence class S. Usage: python3 docs/engine/export_cpp_twins.py OUT.json
"""
from __future__ import annotations

import contextlib
import io
import json
import math
import shutil
import subprocess
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT))

from omnicompass import compass_law as CL  # noqa: E402
from tests import test_cpp_compass_law_parity as LP  # noqa: E402

GITHUB = "https://github.com/the-omni-compass-llc/the-omni-compass/blob/main/"
SEED = 3000


def g(x):
    return repr(float(x))


class LawRecorder:
    """While open, every CompassLaw made anywhere is recorded with the file that wired it, and every force it gives with the
    band and push as they stood at that reading; the law itself runs exactly as it would."""

    def __init__(self):
        self.laws = []

    def __enter__(self):
        rec, init0, force0 = self, CL.CompassLaw.__post_init__, CL.CompassLaw.force

        def post_init(law):
            kd_arg = law.kd
            init0(law)
            wired = "unknown"
            f = sys._getframe(1)
            while f is not None:
                fn = f.f_code.co_filename
                if not fn.endswith("compass_law.py") and "<string>" not in fn and not fn.endswith("dataclasses.py"):
                    try:
                        wired = str(Path(fn).resolve().relative_to(ROOT))
                    except ValueError:
                        wired = Path(fn).name
                    break
                f = f.f_back
            law._twin = {"wired": wired, "organism": None, "muscle": None,
                         "L": LP.law_line(law.band, law.dt, law.tau, law.kp, kd_arg, law.authority, law.smooth),
                         "kd": law.kd, "F": [], "own": []}
            rec.laws.append(law._twin)

        def force(law, reading):
            t = getattr(law, "_twin", None)
            if t is not None:
                t["F"].append(f"F,{g(reading)},{g(law.band.center)},{g(law.band.cushion)},{g(law.kd)}")
            out = force0(law, reading)
            if t is not None:
                t["own"].append(["F", out, law.p, law.v])
            return out

        self._saved = (init0, force0)
        CL.CompassLaw.__post_init__, CL.CompassLaw.force = post_init, force
        return self

    def __exit__(self, *exc):
        CL.CompassLaw.__post_init__, CL.CompassLaw.force = self._saved
        return False


def build_cpp(tmp: Path):
    """The repository's C++, compiled as verify.py compiles it, or None where no C++ compiler is installed."""
    if not (shutil.which("g++") or shutil.which("clang++")):
        return None
    import verify
    return verify.build_cpp(tmp)


def worst_of(a, b):
    """The largest absolute difference between two answer lists, inf where their shape differs."""
    if len(a) != len(b):
        return math.inf
    w = 0.0
    for x, y in zip(a, b):
        if x[0] != y[0] or len(x) != len(y):
            return math.inf
        for u, v in zip(x[1:], y[1:]):
            if u is None or v is None:
                if u is not v:
                    return math.inf
                continue
            w = max(w, abs(float(u) - float(v)))
    return w


def replay(exe, laws, tmp):
    """Every law's readings through the Python again and through the C++; per law: (readings, C++ vs Python, Python vs the
    run's own). Laws that gave no force are left out."""
    laws = [t for t in laws if t["F"]]
    lines = [l for t in laws for l in [t["L"]] + t["F"]]
    py = LP.py_answers(lines)
    cpp = LP.cpp_answers(exe, lines, tmp) if exe else None
    out, i = [], 0
    for t in laws:
        n = len(t["F"])
        py_t, cpp_t = py[i:i + 1 + n], (cpp[i:i + 1 + n] if cpp is not None else None)
        own = [["L", t["kd"]]] + t["own"]
        out.append((t, n, None if cpp_t is None else worst_of(cpp_t, py_t), worst_of(py_t, own)))
        i += 1 + n
    return out


def fmt(w):
    return None if w is None else (0.0 if w == 0.0 else ("inf" if math.isinf(w) else float(f"{w:.3g}")))


def twins(b: Path, tmp: Path) -> list:
    """Every Python/C++ twin's own parity check on its seeded inputs (the sizes verify.py --quick uses)."""
    from tools import seal
    from tests import (test_cpp_governor_parity, test_cpp_shield_parity, test_cpp_hpa_parity, test_cpp_closure_parity,
                       test_cpp_conveyance_parity, test_cpp_twins_parity)
    rows = []

    def run(name, fn, cases, tol=1e-9):
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                w = fn()
            ok = True if not isinstance(w, float) else w < tol
            worst = w if isinstance(w, float) else None          # None: within the parity test's own tolerance, not measured here
        except AssertionError as e:
            ok, worst = False, str(e)[:200]
        t = seal.TWINS[name]
        rows.append({"twin": name, "python": t["python"], "cpp": t["cpp"], "proof": t["proof"], "cases": cases,
                     "same": ok, "worst": worst if isinstance(worst, str) else fmt(worst)})   # fmt(None) is None

    def core():
        subprocess.run([str(b / "oc_run_fixture"), str(ROOT / "fixtures/current_500_inputs.csv"), str(tmp / "cpp.csv")], check=True)
        subprocess.run([sys.executable, str(ROOT / "cpp/scripts/compare_results.py"), str(ROOT / "fixtures/current_500_expected.csv"),
                        str(tmp / "cpp.csv"), str(tmp / "cpp.json")], check=True, capture_output=True)
        r = json.loads((tmp / "cpp.json").read_text())
        assert r["pass"], f"max abs {r['max_abs_error']}"
        return float(r["max_abs_error"])
    run("core engine (six-state equations)", core, "500 fixtures", tol=math.inf)   # the fixtures' own tolerance decides (pass)
    run("governor (allocation laws)", lambda: [test_cpp_governor_parity.main(str(b / "oc_governor"), 20, m)
                                               for m in ("power_protect", "throughput", "fleet", "fleet_balanced", "fleet_wear")] and None,
        "5 modes x 20 trajectories")
    run("safety shield", lambda: test_cpp_shield_parity.main(str(b / "oc_shield"), 8) and None, "8 seeds")
    run("HPA replica law", lambda: test_cpp_hpa_parity.main(str(b / "oc_hpa"), (901,)) and None, "seed 901")
    run("closure law (machines)", lambda: test_cpp_closure_parity.main(str(b / "oc_closure"), 1) and None, "1 seed, every decision")
    run("conveyance law (the conserved budget)", lambda: float(test_cpp_conveyance_parity.main(str(b / "oc_conveyance"), 50)),
        "50 systems and the CPU+GPU layout")
    for name in ("nervous system (authority per organ, living band)", "compass and ledger (composite storage)",
                 "GPU governor rules (shield limit, busy gate, speed lock, window, baseline)"):
        run(name, lambda: test_cpp_twins_parity.main(str(b / "oc_twins"), 500) and None, "500 seeded cases")
    law = [k for k in seal.TWINS if k.startswith("compass law")][0]
    run(law, lambda: LP.main(str(b / "oc_compass_law"), 300) and 0.0, "300 random laws and plugs, 101 climbing")   # it asserts every answer identical
    from tests import test_cpp_verdict_parity, test_cpp_engine_runs_parity
    run([k for k in seal.TWINS if k.startswith("verdict")][0], lambda: test_cpp_verdict_parity.main(str(b / "oc_verdict"), 300) and 0.0,
        "300 random verdicts, both judges")
    run([k for k in seal.TWINS if k.startswith("the engine's seeded runs")][0],
        lambda: test_cpp_engine_runs_parity.main(str(b / "oc_engine_runs"), 50) and 0.0, "50 runs from the jump generator")
    return rows


def engine_runs(b: Path, er: dict) -> dict:
    """The record's set (the Python's receipts as GitHub or a person wrote them) run again by the C++ engine: its digest beside
    the record's, and each run's largest difference from the record's receipt (0 where every number is the same to the last bit)."""
    from tools import engine_runs as ER
    from tests.test_cpp_engine_runs_parity import compare
    digest = ER.digest
    py = er.get("receipts") or []
    c = ER.cpp_runs([ER.draws(r["k"], int(er["base"])) for r in py], b / "oc_engine_runs")   # the Python's injection in, the C++ out
    cdg = c["digest"]
    per = compare(py, c["runs"])
    return {"file": er.get("file"), "base": er["base"], "runs": len(py), "python_digest": er.get("digest"),
            "python_digest_recomputed": digest(py) if py else None, "cpp_digest": cdg, "same_digest": cdg == er.get("digest"),
            "identical_runs": sum(1 for w in per if w == 0.0), "largest_difference": fmt(max(per)) if per else 0.0,
            "per_run": [fmt(w) for w in per], "github": er.get("github"), "tool": "cpp/tools/engine_runs.cpp",
            "inputs_digest": c["inputs_digest"]}


def organisms():
    """The seven organisms at the tune-down on the climb (seed 3000), every muscle's compass law recorded."""
    from realms.harness import Body, catalog, run_bodies, scale_load
    from tools.run_realms_v5 import REALMS, SPINE, STACK, TOWER, ORGANISMS, NAMES, spine_rows
    rows = catalog(ROOT / "realms" / "catalog_v5.csv")
    groups = {SPINE: [spine_rows(rows)]}
    groups.update({r: [[x for x in rows if r in x["realms"].split(";")]] for r in REALMS})
    groups[STACK] = [[x for x in rows if r in x["realms"].split(";")] for r in REALMS]
    groups[TOWER] = [rows]
    out = {}
    for name in ORGANISMS:
        with LawRecorder() as rec:
            bodies = [Body(rs, SEED) for rs in groups[name]]
            for b in bodies:
                scale_load(b, "climb")
            run_bodies(bodies, "v5save", [[i] for i in range(len(bodies))])
        for bi, b in enumerate(bodies):
            for p, r in zip(b.plants, b.rows):
                law = getattr(p, "_v5", (None,))[0]
                if law is not None and getattr(law, "_twin", None) is not None:
                    law._twin["organism"] = name
                    law._twin["muscle"] = r["muscle_id"] + (f"@{REALMS[bi]}" if name == STACK else "")
        out[name] = {"title": {SPINE: "Spine", STACK: "Four Stacked", TOWER: "Whole Tower"}.get(name, NAMES[name]), "muscles": sum(len(rs) for rs in groups[name]), "laws": rec.laws}
    return out


def main(out_path, live_laws=(), engine_runs=None):
    from tools import seal
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        b = build_cpp(tmp)
        exe = None if b is None else b / "oc_compass_law"
        rec = {"compiler": None if b is None else (shutil.which("g++") or shutil.which("clang++")).rsplit("/", 1)[-1],
               "github": GITHUB, "seed": SEED, "python_only": seal.PYTHON_ONLY}
        rec["twins"] = twins(b, tmp) if b is not None else []
        rec["engine_runs"] = globals()["engine_runs"](b, engine_runs) if b is not None and engine_runs else None
        live = list(live_laws)
        by = defaultdict(lambda: {"laws": 0, "readings": 0, "cpp": 0.0, "own": 0.0})
        for t, n, wc, wo in replay(exe, live, tmp):
            s = by[t["wired"]]
            s["laws"] += 1; s["readings"] += n
            s["cpp"] = None if wc is None else max(s["cpp"], wc); s["own"] = max(s["own"], wo)
        rec["live"] = [{"wired": k, "laws": v["laws"], "readings": v["readings"], "cpp": fmt(v["cpp"]), "own": fmt(v["own"])}
                       for k, v in sorted(by.items())]
        rec["organisms"] = []
        for name, o in organisms().items():
            res = replay(exe, o["laws"], tmp)
            per = {t["muscle"]: n for t, n, _, _ in res}
            wc = [x for _, _, x, _ in res if x is not None]
            rec["organisms"].append({
                "organism": name, "title": o["title"], "muscles": o["muscles"], "with_law": len(per),
                "readings": sum(per.values()), "cpp": fmt(max(wc)) if wc else (None if exe is None else 0.0),
                "own": fmt(max([x for _, _, _, x in res], default=0.0)),
                "differ": sorted(t["muscle"] for t, _, x, y in res if (x or 0.0) > 0.0 or y > 0.0),
                "per_muscle": per})
    Path(out_path).write_text(json.dumps(rec, separators=(",", ":")), encoding="utf-8")
    n_live = sum(x["readings"] for x in rec["live"]); n_org = sum(x["readings"] for x in rec["organisms"])
    same = all(t["same"] for t in rec["twins"]) and all(x["cpp"] in (0.0, None) and x["own"] == 0.0 for x in rec["live"] + rec["organisms"])
    er = rec["engine_runs"]
    if er:
        same = same and er["same_digest"] and er["identical_runs"] == er["runs"]
    print(f"C++ twins: {len(rec['twins'])} parity checks, {n_live:,} live readings and {n_org:,} organism readings through the "
          f"C++ compass law" + (f", the Python's {er['runs']} runs (base {er['base']}) through the C++ engine" if er else "") + "; "
          + ("every number identical" if same else "A DIFFERENCE (see the record)"))
    return rec


if __name__ == "__main__":
    main(sys.argv[1])
