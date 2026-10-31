# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Checks the live benchmark engine page (docs/engine/OMNI_COMPASS_LIVE_ENGINE.html) against the engine's own Python.

The page carries a JavaScript port of the governor (omnicompass/adapter.py, core.py), the nerves
(nervous_system.py), the compass law (compass_law.py) and the verdict (verdict.py). This script draws seeded inputs,
runs the Python, runs the page's own script on the same inputs under Node, and compares every number:

  governor   200 trajectories x 40 decisions: the six states, push, rho*, kappa, h, sigma, nu, calm
  nerves     the expand and hand-back grant of six organs at every one of those decisions
  compass    60 trajectories x 80 readings: the force F and k_d
  verdict    300 intervals and medians; 400 whole trials, the decision and the number of costs measured
  t95        the exact two-sided 95% point of Student's t (omnicompass/student_t.py), 500 degrees of freedom
  C++ core   the six-state derivative and RK4 step against the C++ twin (cpp/src/core.cpp, compiled with
             docs/engine/cpp_core_probe.cpp), 2,000 seeded states, where a C++ compiler is installed

Usage: python3 docs/engine/check_live_engine.py   (needs node on the PATH). Exit 0 when nothing differs past 1e-12.
"""
from __future__ import annotations

import json
import math
import random
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT))

from omnicompass.adapter import Governor                     # noqa: E402
from omnicompass.compass_law import Band, CompassLaw         # noqa: E402
from omnicompass.nervous_system import from_governor         # noqa: E402
from omnicompass.verdict import Verdict, change_interval, median  # noqa: E402
from omnicompass.student_t import t95 as py_t95  # noqa: E402

ORGANS = ("pods", "nodes", "cpufreq", "gpu", "power", "routing")


def port_js(page: Path) -> str:
    s = page.read_text(encoding="utf-8")
    js = s[s.index("<script>") + 8:s.rindex("</script>")]
    a = js.index("// ============================================================== the engine")
    b = js.index("// ============================================================== the body")
    v0, v1 = js.index("const median = xs"), js.index("function runTrialSync")
    return js[a:b] + "\n" + js[v0:v1] + "\nmodule.exports={Brain,CompassLaw,median,interval,judge,t95,deriv,rk4};\n"


def cases(seed: int = 20261017) -> dict:
    rng = random.Random(seed)
    out = {"brain": [], "law": [], "verdict": [], "trial": [], "t95": [[df, py_t95(df)] for df in range(1, 501)]}
    for _ in range(200):
        g, seq = Governor(), []
        for _ in range(40):
            o = {"q": rng.choice([0, 0, rng.uniform(0, 0.6)]), "load": rng.uniform(0.2, 1.4), "power": rng.uniform(0, 1.1),
                 "thermal": rng.uniform(0, 1.1), "network": rng.uniform(0, 0.4), "drift": rng.uniform(0, 0.5),
                 "stale": rng.choice([0, 0, 0, 1]), "security": rng.choice([0, 0, 0, 1]), "sloClean": rng.random() < 0.8}
            obs = {"queue_ratio": o["q"], "load_ratio": o["load"], "power_stress": o["power"], "thermal": o["thermal"],
                   "network_stress": o["network"], "drift_ratio": o["drift"], "stale": o["stale"],
                   "security_block": o["security"], "slo_clean": o["sloClean"]}
            d = g.step(obs, 0)
            a = from_governor(g, obs, d)
            L = g.law
            rho = min(L.rho0, max(L.rho_min, L.rho0 - L.kI * g.x.I_U - L.kE * g.x.E))
            seq.append({"in": o, "x": list(g.x.as_tuple()), "push": g.last_push, "rho": rho, **a["scalars"],
                        "organs": {k: [a["organs"][k]["expand"], a["organs"][k]["contract"]] for k in ORGANS}})
        out["brain"].append(seq)
    for _ in range(60):
        tau = rng.uniform(1, 8)
        law, rs, fs, r = CompassLaw(Band(0.2, 1.0), dt=1.0, tau=tau), [], [], rng.uniform(0.2, 1.1)
        for _ in range(80):
            r = max(0.0, r + rng.gauss(0, 0.06))
            rs.append(r)
            fs.append(law.force(r))
        out["law"].append({"tau": tau, "r": rs, "F": fs, "kd": law.kd})
    for _ in range(300):
        ref = [math.exp(rng.gauss(0, 0.25)) for _ in range(rng.randint(30, 90))]
        got = [math.exp(rng.gauss(0.02, 0.25)) for _ in range(rng.randint(30, 90))]
        out["verdict"].append({"ref": ref, "got": got, "iv": change_interval(ref, got), "m": [median(ref), median(got)]})
    for _ in range(400):
        cost = rng.choice([-0.04, 0, 0.01, 0.02, 0.03, 0.05, 0.08])
        tol, sig = rng.choice([0.005, 0.01, 0.02, 0.03]), rng.choice([0.1, 0.25, 0.4])
        ref = [math.exp(rng.gauss(0, sig)) for _ in range(30)]
        extra = [math.exp(rng.gauss(0, sig)) * (1 + cost) for _ in range(90)]
        v = Verdict(tolerance=tol, min_samples=30, probe_every=1, max_trial=10 ** 6, judge="interval")
        v.tick(True); v.observe(ref); v.tick(True); v.observe(extra[:30])
        used = 30
        while True:
            _, _, ev = v.tick(True)
            if ev and ev.get("verdict", "").startswith("step"):
                break
            v.observe([extra[used]]); used += 1
        out["trial"].append({"ref": ref, "extra": extra, "tol": tol, "allowed": ev["verdict"] == "step allowed", "used": used})
    return out


CORE_JS = r"""
const P = require('./port.js'); const D = require('./core.json'); let wd = 0, ws = 0;
const rel = (a, b) => Math.abs(a - b) / Math.max(1, Math.abs(b));
D.cases.forEach((c, i) => { const p = {...c.p}; const want = D.cpp[i];
  const d = P.deriv(c.x, p, c.t, c.u); d.forEach((v, j) => { wd = Math.max(wd, rel(v, want[j])); });
  if (c.u === 0) { const n = P.rk4(c.x, p, c.t, c.h); n.forEach((v, j) => { ws = Math.max(ws, rel(v, want[6 + j])); }); } });
console.log(JSON.stringify({cppN: D.cases.length, cppDeriv: wd, cppStep: ws}));
"""


COMPARE = r"""
const P = require('./port.js'); const C = require('./cases.json');
const w = {state: 0, push: 0, rho: 0, nerves: 0, force: 0, kd: 0, interval: 0, median: 0}; let grants = 0, grantMis = 0, trialMis = 0;
for (const seq of C.brain) { const b = new P.Brain(); for (const st of seq) { const o = b.step(st.in);
  for (let i = 0; i < 6; i++) w.state = Math.max(w.state, Math.abs(o.xn[i] - st.x[i]));
  w.push = Math.max(w.push, Math.abs(o.push - st.push)); w.rho = Math.max(w.rho, Math.abs(o.rho - st.rho));
  for (const k of ["kappa", "h", "sigma", "nu", "calm"]) w.nerves = Math.max(w.nerves, Math.abs(o[k] - st[k]));
  for (const k in st.organs) { grants++; if (o.organs[k].expand !== st.organs[k][0] || o.organs[k].contract !== st.organs[k][1]) grantMis++; } } }
for (const c of C.law) { const L = new P.CompassLaw(c.tau); w.kd = Math.max(w.kd, Math.abs(L.kd - c.kd));
  c.r.forEach((r, k) => { w.force = Math.max(w.force, Math.abs(L.force(r) - c.F[k])); }); }
for (const c of C.verdict) { const iv = P.interval(c.ref, c.got);
  w.interval = Math.max(w.interval, Math.abs(iv[0] - c.iv[0]), Math.abs(iv[1] - c.iv[1]));
  w.median = Math.max(w.median, Math.abs(P.median(c.ref) - c.m[0]), Math.abs(P.median(c.got) - c.m[1])); }
for (const c of C.trial) { const Pp = {tol: c.tol, min: 30}; const got = c.extra.slice(0, 30); let J = P.judge(c.ref, got, Pp);
  while (J.reading !== "LOSS" && J.wide && got.length < 90) { got.push(c.extra[got.length]); J = P.judge(c.ref, got, Pp); }
  if (J.allowed !== c.allowed || got.length !== c.used) trialMis++; }
let tMis = 0; for (const [df, t] of C.t95) if (P.t95(df) !== t) tMis++;
console.log(JSON.stringify({worst: w, grants, grantMis, trials: C.trial.length, trialMis, tN: C.t95.length, tMis}));
"""


CPP_KEYS = ["alpha_E", "mu", "E_max", "lambda_U", "sigma_1", "delta", "lambda_I", "alpha_s", "beta_s", "gamma_c", "omega_B", "Q_B",
            "lambda_0", "lambda_1", "lambda_2", "c", "beta_int", "beta_ext"]


def core_cases(seed: int = 20261018, n: int = 2000) -> list:
    """Seeded states and parameters around the engine's own (adapter.py), for the page's core against the C++ core."""
    rng = random.Random(seed)
    base = {"alpha_E": 3.487, "mu": 3.782, "E_max": 2.0, "lambda_U": 0.0, "sigma_1": 0.38, "delta": 0.705, "lambda_I": 0.719,
            "alpha_s": 0.12, "beta_s": 0.10, "gamma_c": 1.0, "omega_B": 1.0, "Q_B": 2.5, "lambda_0": -0.40, "lambda_1": 1.55,
            "lambda_2": 1.15, "c": 1.0, "beta_int": 0.0, "beta_ext": 0.0}
    out = []
    for _ in range(n):
        x = [rng.uniform(-0.5, 1.5), rng.uniform(-1.2, 1.2), rng.uniform(-1, 3), rng.uniform(-1, 3), rng.uniform(-1, 1), rng.uniform(-1, 1)]
        p = {k: v * rng.uniform(0.5, 1.5) if v else rng.uniform(0, 0.3) for k, v in base.items()}
        out.append({"x": x, "p": p, "t": rng.uniform(0, 500), "h": rng.choice([0.01, 0.1]), "u": rng.choice([0.0, rng.uniform(-25, 25)])})
    return out


def cpp_core(cases: list, tmp: Path):
    """The repository's C++ core (cpp/src/core.cpp) on the same cases, or None where no C++ compiler is installed."""
    cxx = shutil.which("g++") or shutil.which("c++") or shutil.which("clang++")
    if not cxx:
        return None
    cpp = ROOT / "cpp"
    exe = tmp / "oc_core_probe"
    subprocess.run([cxx, "-std=c++20", "-O2", "-I", str(cpp / "include"), str(cpp / "src" / "core.cpp"), str(cpp / "src" / "csv.cpp"),
                    str(HERE / "cpp_core_probe.cpp"), "-o", str(exe)], check=True, capture_output=True)
    lines = "\n".join(" ".join(repr(v) for v in c["x"] + [c["p"][k] for k in CPP_KEYS] + [c["t"], c["h"], c["u"]]) for c in cases)
    r = subprocess.run([str(exe)], input=lines + "\n", capture_output=True, text=True, check=True)
    return [[float(v) for v in ln.split()] for ln in r.stdout.strip().splitlines()]


def main() -> int:
    node = shutil.which("node")
    if not node:
        print("node is not on the PATH; the page's script cannot be run")
        return 2
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        (t / "port.js").write_text(port_js(HERE / "OMNI_COMPASS_LIVE_ENGINE.html"), encoding="utf-8")
        (t / "cases.json").write_text(json.dumps(cases()), encoding="utf-8")
        (t / "compare.js").write_text(COMPARE, encoding="utf-8")
        r = json.loads(subprocess.run([node, "compare.js"], cwd=t, capture_output=True, text=True, check=True).stdout)
        cc = core_cases(); cpp = cpp_core(cc, t)
        if cpp is not None:
            (t / "core.json").write_text(json.dumps({"cases": cc, "keys": CPP_KEYS, "cpp": cpp}), encoding="utf-8")
            (t / "core.js").write_text(CORE_JS, encoding="utf-8")
            r.update(json.loads(subprocess.run([node, "core.js"], cwd=t, capture_output=True, text=True, check=True).stdout))
    for k, v in r["worst"].items():
        print(f"{k:9s} largest difference {v:.1e}")
    print(f"grants    {r['grantMis']} of {r['grants']} differ")
    print(f"trials    {r['trialMis']} of {r['trials']} differ")
    print(f"t95       {r['tMis']} of {r['tN']} degrees of freedom differ (omnicompass/student_t.py)")
    if "cppN" in r:
        print(f"C++ core  {r['cppN']} states: derivative largest relative difference {r['cppDeriv']:.1e}, RK4 step {r['cppStep']:.1e} (cpp/src/core.cpp)")
    else:
        print("C++ core  no C++ compiler on this machine: the page against cpp/src/core.cpp is not run here")
    ok = (max(r["worst"].values()) < 1e-12 and r["grantMis"] == 0 and r["trialMis"] == 0 and r["tMis"] == 0
          and ("cppN" not in r or max(r["cppDeriv"], r["cppStep"]) < 1e-12))
    print("the page's engine matches the Python and the C++" if ok else "the page's engine differs from the Python or the C++")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
