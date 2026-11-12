# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The engine's runs, seeded, with one receipt and one digest: the Python here, the same runs in the live engine's page.

The founder's order of 20 October: whenever the Python runs its runs (500 by default), the live engine must be able to run the
same runs, from the same jump generator, and show the same receipts, so that a run of the Python and a run of the page prove
each other. One run k draws its seed from the jump generator (seed_k = base + k·0x9E3779B9, mod 2³²), feeds a mulberry32
stream (the page's own generator, written here in 32-bit arithmetic) through the engine that stands: the brain's state
equations integrated by RK4 (omnicompass/adapter.Governor, 288 decisions, a day at five minutes), the compass law's force on a
wandering ratio (omnicompass/compass_law.CompassLaw, 80 steps) and one give-back trial judged by the verdict
(omnicompass/verdict.Verdict). Every run's receipt holds the brain's final state, its pushes and grants, the law's mean force
and its last, the trial's answer and how many samples it took. The digest is the SHA-256 of the receipts with every number
rounded to six decimals; the page computes the same runs with its own ported engine (proven equal to this Python to 1e-12 by
docs/engine/check_live_engine.py) and compares receipt by receipt.

The ladder (the founder's order of 25 October): every set is read at its first 1, 10, 100 and 500 runs. With S_N = {0, …, N−1}
the first N runs and r_k run k's receipt, S_1 ⊂ S_10 ⊂ S_100 ⊂ S_500 (the rungs nest), and each rung has its own digest
D_N = SHA-256(canon(r_0) ‖ "\n" ‖ … ‖ canon(r_{N−1})); the record holds D_N for N in {1, 10, 100, 500}, the Python's and the C++
harness's, and the page computes its own D_N from the same runs: the three agree at every rung or the rung reads "differs".

  python3 tools/engine_runs.py --runs 500 --base 20261020           write results/engine_runs/ENGINE_RUNS_500_20261020.json and .md
  python3 tools/engine_runs.py --verify PAGE                        run the page's own loop in node on 20 runs and compare to the Python
  python3 tools/engine_runs.py --verify PAGE --all --runs 500 --base B   the same on every one of the 500
  python3 tools/engine_runs.py --cpp cpp/build/oc_engine_runs ...    write the record with the same runs through the C++ harness
  python3 tools/engine_runs.py --verify-cpp cpp/build/oc_engine_runs  the Python's first 20 runs (or --all) through the C++ harness

On GitHub (.github/workflows/engine-runs.yml, the founder's order of 21 October: every set the jump generator runs is linked to
the live engine) every push that changes the page or this file, and every dispatch, runs another set from a new base, checks the
page's own code on every run of it, and commits the record with the run that made it (its id, address and commit); the page
shows the newest record and the GitHub run beside it.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import math
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from omnicompass.adapter import Governor                     # noqa: E402
from omnicompass.compass_law import Band, CompassLaw         # noqa: E402
from omnicompass.nervous_system import from_governor         # noqa: E402
from omnicompass.verdict import Verdict                      # noqa: E402
from tools.legal import NOTICE, TOP                          # noqa: E402

M32 = 0xFFFFFFFF
ORGANS = ("pods", "nodes", "cpufreq", "gpu", "power", "routing")   # the organs the page's brain carries (docs/engine/check_live_engine.py)
DECISIONS = 288
LAW_STEPS = 80
DEFAULT_RUNS = 500
LADDER = (1, 10, 100, 500)          # the rungs read at every set: the first 1, 10, 100 and 500 runs (the founder's order of 25 October)
DEFAULT_BASE = 20261020
OUT_DIR = ROOT / "results" / "engine_runs"


def mulberry32(a: int):
    """The page's generator (function mulberry32 in the live engine), bit for bit, in unsigned 32-bit arithmetic."""
    a &= M32

    def rnd() -> float:
        nonlocal a
        a = (a + 0x6D2B79F5) & M32
        t = ((a ^ (a >> 15)) * (1 | a)) & M32
        t = ((t + (((t ^ (t >> 7)) * (61 | t)) & M32)) & M32) ^ t
        return ((t ^ (t >> 14)) & M32) / 4294967296.0
    return rnd


def jump(base: int, k: int) -> int:
    return (base + k * 0x9E3779B9) & M32


class Draw:
    """The draws every run makes, in one order, from one stream (the page draws the same, in the same order)."""

    def __init__(self, seed: int):
        self.r = mulberry32(seed)

    def uniform(self, a: float, b: float) -> float:
        return a + (b - a) * self.r()

    def choice(self, xs):
        return xs[int(self.r() * len(xs))]

    def gauss(self, mu: float, sigma: float) -> float:
        u1, u2 = self.r(), self.r()
        return mu + sigma * math.sqrt(-2.0 * math.log(1.0 - u1)) * math.cos(2.0 * math.pi * u2)


def draws(k: int, base: int) -> dict:
    """Every draw run k makes from its own stream, in the one order the page draws them too: the injection the C++ harness reads
    (cpp/tools/engine_runs.cpp). The senses of each of the 288 decisions; the compass law's tau, starting reading and 80 steps; the
    give-back trial's cost, allowance, noise, its 30 reference samples and 90 trial samples."""
    seed = jump(base, k)
    d = Draw(seed)
    obs = []
    for _ in range(DECISIONS):
        q = d.choice([0.0, 0.0, None])
        if q is None:
            q = d.uniform(0, 0.6)
        obs.append({"queue_ratio": q, "load_ratio": d.uniform(0.2, 1.4), "power_stress": d.uniform(0, 1.1), "thermal": d.uniform(0, 1.1),
                    "network_stress": d.uniform(0, 0.4), "drift_ratio": d.uniform(0, 0.5), "stale": d.choice([0, 0, 0, 1]),
                    "security_block": d.choice([0, 0, 0, 1]), "slo_clean": d.r() < 0.8})
    tau = d.uniform(1, 8)
    r0 = d.uniform(0.2, 1.1)
    inc = [d.gauss(0, 0.06) for _ in range(LAW_STEPS)]
    cost = d.choice([-0.04, 0, 0.01, 0.02, 0.03, 0.05, 0.08])
    tol, sig = d.choice([0.005, 0.01, 0.02, 0.03]), d.choice([0.1, 0.25, 0.4])
    ref = [math.exp(d.gauss(0, sig)) for _ in range(30)]
    extra = [math.exp(d.gauss(0, sig)) * (1 + cost) for _ in range(90)]
    return {"k": k, "seed": seed, "obs": obs, "tau": tau, "r0": r0, "inc": inc, "cost": cost, "tol": tol, "sig": sig, "ref": ref, "extra": extra}


def run_draws(dr: dict) -> dict:
    """One run of the engine that stands on its draws: the brain (omnicompass.adapter.Governor) and the nervous system's grants
    for every decision, the compass law, one give-back trial judged by the verdict."""
    g, push, expand, contract = Governor(), 0.0, 0, 0
    calm = 0.0
    for obs in dr["obs"]:
        dec = g.step(obs, 0)
        a = from_governor(g, obs, dec)
        push += g.last_push
        for o in ORGANS:
            expand += 1 if a["organs"][o]["expand"] else 0
            contract += 1 if a["organs"][o]["contract"] else 0
        calm = a["scalars"]["calm"]
    tau = dr["tau"]
    law, r, fs = CompassLaw(Band(0.2, 1.0), dt=1.0, tau=tau), dr["r0"], []
    for inc in dr["inc"]:
        r = max(0.0, r + inc)
        fs.append(law.force(r))
    ref, extra = dr["ref"], dr["extra"]
    v = Verdict(tolerance=dr["tol"], min_samples=30, probe_every=1, max_trial=10 ** 6, judge="interval")
    v.tick(True); v.observe(ref); v.tick(True); v.observe(extra[:30])
    used = 30
    while True:
        _, _, ev = v.tick(True)
        if ev and ev.get("verdict", "").startswith("step"):
            break
        if used >= len(extra):
            ev = {"verdict": "step refused: the trial ran out of samples"}
            break
        v.observe([extra[used]]); used += 1
    return {"k": dr["k"], "seed": dr["seed"], "x": list(g.x.as_tuple()), "push": push, "expand": expand, "contract": contract, "calm": calm,
            "tau": tau, "meanF": sum(abs(f) for f in fs) / len(fs), "lastF": fs[-1],
            "allowed": 1 if ev["verdict"] == "step allowed" else 0, "used": used}


def one_run(k: int, base: int) -> dict:
    return run_draws(draws(k, base))


def injection(sets: list) -> str:
    """The Python's runs as the C++ harness reads them: every draw at full precision (repr round-trips exactly)."""
    L = [f"OCRUNS 1 {len(sets)} {DECISIONS} {LAW_STEPS}"]
    for dr in sets:
        L.append(f"R {dr['k']} {dr['seed']}")
        for o in dr["obs"]:
            L.append("O " + " ".join(repr(float(o[key])) for key in ("queue_ratio", "load_ratio", "power_stress", "thermal", "network_stress",
                                                                        "drift_ratio", "stale", "security_block")) + (" 1" if o["slo_clean"] else " 0"))
        L.append("L " + " ".join(repr(float(x)) for x in [dr["tau"], dr["r0"], *dr["inc"]]))
        L.append("V " + " ".join(repr(float(x)) for x in [dr["cost"], dr["tol"], dr["sig"]]) + f" {len(dr['ref'])} "
                 + " ".join(repr(float(x)) for x in dr["ref"]) + f" {len(dr['extra'])} " + " ".join(repr(float(x)) for x in dr["extra"]))
    return "\n".join(L) + "\n"


CPP = ROOT / "cpp" / "build" / "oc_engine_runs"


def cpp_runs(sets: list, binary: Path = CPP) -> dict:
    """The C++ harness on the Python's injection: its canonical receipts, its digest, and every receipt at full precision."""
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        inj = injection(sets)
        (t / "in.txt").write_text(inj, encoding="utf-8")
        subprocess.run([str(binary), str(t / "in.txt"), str(t / "receipts.txt"), str(t / "full.jsonl")], check=True, capture_output=True, text=True)
        canon = (t / "receipts.txt").read_text(encoding="utf-8")
        full = [json.loads(line) for line in (t / "full.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    return {"canon": canon, "digest": hashlib.sha256(canon.encode("utf-8")).hexdigest(), "runs": full,
            "inputs_digest": hashlib.sha256(inj.encode("utf-8")).hexdigest()}


def largest(a: dict, b: dict) -> float:
    d = 0.0
    for key in KEYS:
        va, vb = a[key], b[key]
        if isinstance(va, list):
            d = max(d, max(abs(x - y) for x, y in zip(va, vb)))
        else:
            d = max(d, abs(float(va) - float(vb)))
    return d


def cpp_check(n: int, base: int, binary: Path = CPP) -> int:
    """The Python's runs through the C++ harness: every receipt to 1e-9 and the same digest."""
    if not Path(binary).exists():
        print(f"the C++ harness is not built: cmake -S cpp -B cpp/build && cmake --build cpp/build ({binary})")
        return 2
    sets = [draws(k, base) for k in range(n)]
    py = [run_draws(dr) for dr in sets]
    c = cpp_runs(sets, binary)
    worst = max((largest(a, b) for a, b in zip(py, c["runs"])), default=0.0)
    same = c["digest"] == digest(py) and len(c["runs"]) == n
    print(f"the C++ harness on the Python's {n} runs (base {base}): largest difference {worst:.1e}; the digests {'match' if same else 'DIFFER'} "
          f"(Python {digest(py)[:16]}…, C++ {c['digest'][:16]}…; the injection {c['inputs_digest'][:16]}…)")
    return 0 if same and worst < 1e-9 else 1


KEYS = ("x", "push", "expand", "contract", "calm", "tau", "meanF", "lastF", "allowed", "used")
INT_KEYS = ("seed", "expand", "contract", "allowed", "used")


def canonical(runs: list) -> str:
    """Every receipt's numbers in one order: the counts as integers, every other number rounded to six decimals (a negative zero
    written as zero), as the page writes them too."""
    def f(k, v):
        if k in INT_KEYS:
            return str(int(v))
        s = f"{float(v):.6f}"
        return "0.000000" if s == "-0.000000" else s
    return "\n".join(f"{r['k']}:{r['seed']}:" + ":".join(",".join(f(k, x) for x in r[k]) if isinstance(r[k], list) else f(k, r[k]) for k in KEYS)
                     for r in runs)


def digest(runs: list) -> str:
    return hashlib.sha256(canonical(runs).encode("utf-8")).hexdigest()


def engine():
    out = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py")], capture_output=True, text=True, cwd=ROOT).stdout
    return out.strip().split("\n")[0]


# the page's loop, the same draws in the same order (kept here so that --verify runs the very code the page carries)
PAGE_JS = r"""
function engineRuns(P, base, n, start, each) {   // the engine's runs in this page: the same jump generator, draws and receipts as tools/engine_runs.py
  const M = 0x100000000, jump = k => (base + k*0x9E3779B9) % M;
  const out = [];
  for (let k = start; k < start + n; k++) {
    const seed = jump(k), r = mulberry32(seed), U = (a, b) => a + (b - a)*r(), C = xs => xs[Math.floor(r()*xs.length)];
    const G = (mu, s) => { const u1 = r(), u2 = r(); return mu + s*Math.sqrt(-2*Math.log(1 - u1))*Math.cos(2*Math.PI*u2); };
    const b = new P.Brain(); let push = 0, expand = 0, contract = 0, calm = 0, o = null;
    for (let t = 0; t < 288; t++) {
      let q = C([0, 0, null]); if (q === null) q = U(0, 0.6);
      const inp = {q, load: U(0.2, 1.4), power: U(0, 1.1), thermal: U(0, 1.1), network: U(0, 0.4), drift: U(0, 0.5), stale: C([0, 0, 0, 1]), security: C([0, 0, 0, 1]), sloClean: r() < 0.8};
      o = b.step(inp); push += o.push; for (const g of ["pods", "nodes", "cpufreq", "gpu", "power", "routing"]) { expand += o.organs[g].expand ? 1 : 0; contract += o.organs[g].contract ? 1 : 0; } calm = o.calm;
    }
    const tau = U(1, 8), L = new P.CompassLaw(tau); let rr = U(0.2, 1.1); const fs = [];
    for (let i = 0; i < 80; i++) { rr = Math.max(0, rr + G(0, 0.06)); fs.push(L.force(rr)); }
    const cost = C([-0.04, 0, 0.01, 0.02, 0.03, 0.05, 0.08]), tol = C([0.005, 0.01, 0.02, 0.03]), sig = C([0.1, 0.25, 0.4]);
    const ref = [], extra = []; for (let i = 0; i < 30; i++) ref.push(Math.exp(G(0, sig))); for (let i = 0; i < 90; i++) extra.push(Math.exp(G(0, sig))*(1 + cost));
    const Pp = {tol, min: 30}, got = extra.slice(0, 30); let J = P.judge(ref, got, Pp);
    while (J.reading !== "LOSS" && J.wide && got.length < 90) { got.push(extra[got.length]); J = P.judge(ref, got, Pp); }
    const rec = {k, seed, x: o.xn.slice(0, 6), push, expand, contract, calm, tau, meanF: fs.reduce((a, f) => a + Math.abs(f), 0)/fs.length, lastF: fs[fs.length - 1], allowed: J.allowed ? 1 : 0, used: got.length};
    out.push(rec); if (each) each(rec);
  }
  return out;
}
function engineRunsCanonical(runs) {   // the receipts as tools/engine_runs.py writes them: the counts as integers, every other number six decimals, one order
  const INT = {seed: 1, expand: 1, contract: 1, allowed: 1, used: 1}, f = (k, v) => { if (INT[k]) return String(Math.round(v)); const s = Number(v).toFixed(6); return s === "-0.000000" ? "0.000000" : s; };
  return runs.map(r => `${r.k}:${r.seed}:` + ["x", "push", "expand", "contract", "calm", "tau", "meanF", "lastF", "allowed", "used"].map(k => Array.isArray(r[k]) ? r[k].map(v => f(k, v)).join(",") : f(k, r[k])).join(":")).join("\n");
}
"""


def verify(page: Path, n: int = 20, base: int = DEFAULT_BASE, record: Path = None) -> int:
    """The page's own loop (its ported engine and this file's loop, as the page carries it) in node against the Python."""
    sys.path.insert(0, str(ROOT / "docs" / "engine"))
    import check_live_engine as C
    node = shutil.which("node")
    if not node:
        print("node is not on the PATH")
        return 2
    s = page.read_text(encoding="utf-8")
    loop = PAGE_JS
    if "function engineRuns(" in s:      # the page carries the loop: verify the page's copy, not this file's
        js = s[s.index("<script>") + 8:s.rindex("</script>")]
        a = js.index("function engineRuns("); b = js.index("// ===== end engine runs")
        loop = js[a:b]
    py = [one_run(k, base) for k in range(n)]
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        port = C.port_js(page)
        port += "\n" + s[s.index("function mulberry32"):s.index("\n", s.index("function mulberry32"))] + "\n"
        port += loop + "\nmodule.exports.engineRuns=engineRuns;module.exports.engineRunsCanonical=engineRunsCanonical;module.exports.mulberry32=mulberry32;\n"
        (t / "port.js").write_text(port, encoding="utf-8")
        (t / "drive.js").write_text("const P=require('./port.js');const r=P.engineRuns(P,%d,%d,0,null);const g=P.mulberry32(12345);const s=[];for(let i=0;i<5;i++)s.push(g());"
                                    "console.log(JSON.stringify({runs:r,canon:P.engineRunsCanonical(r),gen:s}));" % (base, n), encoding="utf-8")
        r = json.loads(subprocess.run([node, "drive.js"], cwd=t, capture_output=True, text=True, check=True).stdout)
    g = mulberry32(12345)
    gen_ok = all(abs(g() - v) == 0 for v in r["gen"])
    worst = 0.0
    for a, b in zip(py, r["runs"]):
        for k in KEYS:
            va, vb = a[k], b[k]
            if isinstance(va, list):
                worst = max(worst, max(abs(x - y) for x, y in zip(va, vb)))
            else:
                worst = max(worst, abs(float(va) - float(vb)))
    page_digest = hashlib.sha256(r["canon"].encode("utf-8")).hexdigest()
    same_digest = page_digest == digest(py)
    print(f"generator bit for bit: {'yes' if gen_ok else 'NO'}; {n} runs: largest difference {worst:.1e}; the digests {'match' if same_digest else 'DIFFER'}")
    if record is not None:   # the third digest beside the Python's and the C++ harness's, in the set's own record (11 November)
        lines = r["canon"].split("\n")
        agree = sum(1 for a, b in zip(py, r["runs"]) if largest(a, b) < 1e-9)
        note_page(record, n, base, {
            "tool": "the page's own loop and ported engine, run in node (tools/engine_runs.py --verify --all)",
            "page": str(page.resolve().relative_to(ROOT)) if page.resolve().is_relative_to(ROOT) else page.name,
            "page_sha256": hashlib.sha256(page.read_bytes()).hexdigest(), "digest": page_digest, "same": same_digest,
            "largest_difference": float(f"{worst:.1e}"), "agree": agree, "of": n, "generator_bit_for_bit": gen_ok,
            "ladder": [{"runs": m, "digest": hashlib.sha256("\n".join(lines[:m]).encode("utf-8")).hexdigest()} for m in LADDER if m <= n]})
    return 0 if gen_ok and worst < 1e-9 and same_digest else 1


PAGE_MARK = "**The live engine page's own code**"


def note_page(record: Path, n: int, base: int, block: dict) -> bool:
    """The page's digest written into the set's record beside the Python's and the C++ harness's, and its line into the record's
    page. Only the record of the same set takes it (its runs and its base), and each rung reads the same or says it differs."""
    if not record.exists():
        return False
    data = json.loads(record.read_text(encoding="utf-8"))
    if data.get("runs") != n or data.get("base") != base:
        return False
    block["same"] = block["digest"] == data.get("digest")
    by = {g["runs"]: g for g in block["ladder"]}
    for rung in data.get("ladder") or []:
        if rung["runs"] in by:
            rung["page_digest"] = by[rung["runs"]]["digest"]
            rung["page_same"] = rung["page_digest"] == rung["digest"]
            by[rung["runs"]]["same"] = rung["page_same"]
    data["page"] = block
    record.write_text(json.dumps(data, separators=(",", ":"), ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
    md = record.with_suffix(".md")
    if md.exists():
        line = (f"{PAGE_MARK} (its ported engine and its loop, run in node) on the same {n} runs: digest {block['digest']}, "
                f"{'the same' if block['same'] else 'DIFFERENT'}; {block['agree']} of {block['of']} runs agree to 1e-9, largest difference "
                f"{block['largest_difference']:.1e}; the generator bit for bit {'the same' if block['generator_bit_for_bit'] else 'DIFFERENT'}. "
                f"The page checked: SHA-256 {block['page_sha256']}.")
        out, placed = [], False
        for ln in md.read_text(encoding="utf-8").split("\n"):
            if ln.startswith(PAGE_MARK):
                out.append(line); placed = True
            elif ln.startswith("**The ladder**") and not placed:
                out += [line, "", ln]; placed = True
            else:
                out.append(ln)
        md.write_text("\n".join(out), encoding="utf-8")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--runs", type=int, default=DEFAULT_RUNS)
    ap.add_argument("--base", type=int, default=DEFAULT_BASE, help="the jump generator's base seed")
    ap.add_argument("--verify", default="", help="the live engine page: run its loop in node and compare")
    ap.add_argument("--out", default="", help="where to write (default results/engine_runs/)")
    ap.add_argument("--all", action="store_true", help="with --verify or --verify-cpp: every run of the set, not the first 20")
    ap.add_argument("--cpp", default="", help="the C++ harness (cpp/build/oc_engine_runs): run the same set through it and record its digest")
    ap.add_argument("--verify-cpp", default="", help="the C++ harness: run the Python's runs through it and compare")
    a = ap.parse_args()
    if a.verify:   # with --all the page's digest goes into the set's own record, beside the Python's and the C++ harness's
        rec = (Path(a.out) if a.out else OUT_DIR / f"ENGINE_RUNS_{a.runs}_{a.base}.json") if a.all else None
        return verify(Path(a.verify), a.runs if a.all else min(a.runs, 20), a.base, rec)
    if a.verify_cpp:
        return cpp_check(a.runs if a.all else min(a.runs, 20), a.base, Path(a.verify_cpp))
    sets = [draws(k, a.base) for k in range(a.runs)]
    runs = [run_draws(dr) for dr in sets]
    dg = digest(runs)
    eng = engine()
    data = {"tool": "tools/engine_runs.py", "engine": eng, "runs": a.runs, "base": a.base, "jump": "seed_k = base + k·0x9E3779B9 mod 2^32",
            "generator": "mulberry32 (the page's own)", "decisions": DECISIONS, "law_steps": LAW_STEPS, "digest": dg,
            "digest_of": "SHA-256 of every receipt, numbers rounded to six decimals, one line a run (canonical())",
            "written": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "receipts": runs}
    if a.cpp:   # the same runs through the C++ harness: the Python's draws its input, the C++ twins of the engine the mechanism
        c = cpp_runs(sets, Path(a.cpp))
        diffs = [largest(x, y) for x, y in zip(runs, c["runs"])]
        data["inputs_digest"] = c["inputs_digest"]
        data["cpp"] = {"tool": "cpp/tools/engine_runs.cpp (oc_engine_runs)", "digest": c["digest"], "same": c["digest"] == dg and len(c["runs"]) == len(runs),
                       "largest_difference": max(diffs, default=0.0), "agree": sum(1 for x in diffs if x < 1e-9), "diff": [float(f"{x:.1e}") for x in diffs],
                       "twins": "omnicompass::Governor (sense, assimilate, the brain's RK4) and omnicompass::authority (the nervous system); "
                                "omnicompass::CompassLaw and omnicompass::Verdict (cpp/src/compass_law.cpp, cpp/src/verdict.cpp), sealed twins of their Python"}
        if not data["cpp"]["same"]:
            print(f"the C++ harness DIFFERS from the Python: digest {c['digest'][:16]}… against {dg[:16]}…, largest difference {data['cpp']['largest_difference']:.1e}")
    # the ladder: the first 1, 10, 100 and 500 runs of the same set, each with its own digest, the Python's and the C++ harness's
    # (the C++ writes one canonical line a run, the Python's own form, so each rung's digest is its first N lines)
    cpp_lines = c["canon"].split("\n") if "cpp" in data else None
    data["ladder"] = [{"runs": n, "digest": digest(runs[:n]), "allowed": sum(r["allowed"] for r in runs[:n]),
                       **({"cpp_digest": hashlib.sha256("\n".join(cpp_lines[:n]).encode("utf-8")).hexdigest()} if cpp_lines else {})}
                      for n in LADDER if n <= len(runs)]
    for rung in data["ladder"]:
        if "cpp_digest" in rung:
            rung["same"] = rung["cpp_digest"] == rung["digest"]
    if os.environ.get("GITHUB_RUN_ID"):   # made on GitHub: the run that made it, so the page links the record to it
        data["github"] = {"run_id": os.environ["GITHUB_RUN_ID"], "workflow": os.environ.get("GITHUB_WORKFLOW", ""),
                          "commit": os.environ.get("GITHUB_SHA", ""), "ref": os.environ.get("GITHUB_REF_NAME", ""),
                          "url": f"{os.environ.get('GITHUB_SERVER_URL', 'https://github.com')}/{os.environ.get('GITHUB_REPOSITORY', '')}/actions/runs/{os.environ['GITHUB_RUN_ID']}"}
    out = Path(a.out) if a.out else OUT_DIR / f"ENGINE_RUNS_{a.runs}_{a.base}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, separators=(",", ":"), ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
    allowed = sum(r["allowed"] for r in runs)
    md = [f"# The engine's runs: {a.runs} runs from the jump generator (base {a.base}), one digest", "", f"> {TOP}", "",
          f"Engine {eng}. Written {data['written']}. Each run: {DECISIONS} decisions of the brain (RK4), {LAW_STEPS} steps of the compass law, one give-back",
          "trial judged by the verdict; the seed of run k is base + k·0x9E3779B9 mod 2³², the stream mulberry32, the same in the live engine's page.", "",
          f"**Digest {dg}** (SHA-256 of the receipts, six decimals). The page runs the same {a.runs} and shows its own digest beside this one.", "",
          *([f"**The C++ harness** (`cpp/tools/engine_runs.cpp`, the C++ twins of the engine) on the same draws: digest {data['cpp']['digest']}, "
             f"{'the same' if data['cpp']['same'] else 'DIFFERENT'}; {data['cpp']['agree']} of {a.runs} runs agree to 1e-9, largest difference "
             f"{data['cpp']['largest_difference']:.1e}. The draws themselves, the injection: SHA-256 {data['inputs_digest']}.", ""] if "cpp" in data else []),
          "**The ladder**: the first 1, 10, 100 and 500 runs of the same set, each its own digest, so a rung read by the page or the C++ "
          "is checked against the Python's rung.", "",
          "| Rung | Runs | Trials allowed | The Python's digest | The C++ harness's digest | The same |", "|---:|---:|---:|---|---|---|",
          *[f"| {i + 1} | {g['runs']} | {g['allowed']} | `{g['digest'][:16]}…` | " + (f"`{g['cpp_digest'][:16]}…` | {'yes' if g['same'] else 'NO'} |" if "cpp_digest" in g else "not run | |")
            for i, g in enumerate(data["ladder"])], "",
          f"Trials allowed {allowed} of {a.runs}; the brain's pushes summed over all runs {sum(r['push'] for r in runs):.3f}; grants to expand {sum(r['expand'] for r in runs)}, to contract {sum(r['contract'] for r in runs)}.", "",
          "| run | seed | final state E U I S B C | pushes | expand | contract | calm | τ | mean force | last force | trial | samples |", "|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|"]
    for r in runs:
        md.append(f"| {r['k']} | {r['seed']} | " + " ".join(f"{x:.4f}" for x in r["x"]) + f" | {r['push']:.3f} | {r['expand']} | {r['contract']} | {r['calm']:.4f} | {r['tau']:.3f} | {r['meanF']:.4f} | {r['lastF']:.4f} | {'allowed' if r['allowed'] else 'refused'} | {r['used']} |")
    md += ["", "---", "", f"*{NOTICE}*"]
    out.with_suffix(".md").write_text("\n".join(md) + "\n", encoding="utf-8")
    shown = out.relative_to(ROOT) if out.is_relative_to(ROOT) else out
    print(f"{a.runs} runs written to {shown} (digest {dg[:16]}…, {allowed} trials allowed)"
          + (f"; the C++ harness: digest {data['cpp']['digest'][:16]}…, {'the same' if data['cpp']['same'] else 'DIFFERENT'}" if "cpp" in data else ""))
    return 0 if "cpp" not in data or data["cpp"]["same"] else 1


if __name__ == "__main__":
    sys.exit(main())
