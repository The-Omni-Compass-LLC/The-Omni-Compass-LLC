# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The Python's Monte Carlo of the engine's core from the jump generator: N runs, one digest, the live engine's own port held to it.

The founder's words of 24 October: "the Python's Monte Carlo, our 4K Runge-Kutta, 20-step macro, 10-step micro in each macro ... how
each Python run comes out and starts at zero, and how long in steps OmniCompass gets it into the basin and holds it there and
certifies the count"; and "some button that allows them to activate the Python's jump generator ... running it again and again".

Run k draws its seed from the jump generator (seed_k = base + k·0x9E3779B9, mod 2³²) and its starting state and its parameters from
that seed's mulberry32 stream (the live engine's own generator, written here bit for bit, as tools/engine_runs.py does): E, U, I_U,
S, B, Ḃ uniform on the ranges benchmarks/core_evidence.py draws, then the 22 parameters in omnicompass/core.py's PARAMETER_RANGES
order. Each run goes through omnicompass/core.simulate itself (six states, the fourth-order Runge–Kutta step, 20 macro steps of 10
micro steps, the bounded command held across the four stages) in the four ways benchmarks/core_evidence.py runs its population:
controlled (toward the nearest basin), uncontrolled (u = 0: the plant alone, native), aimed at the wrong basin, and with the double
well's μ at 0. A run is conveyed when its U has stayed in one basin (|U ∓ 1| ≤ 0.10) for 5 macro steps in a row and certified at
10. The digest is the SHA-256 of every run's U at every macro step (six decimals), its convey step and its cert step, one line a
run, the four ways in order; the live engine's page runs the same set through its own port of the core and must give the same
digest (--verify), and the same draws go through the C++ twin of the core (cpp/tools/core_runs.cpp on cpp/src/core.cpp, --cpp): the
Python writes every draw (the injection), the C++ puts the mechanism on, and its digest must be the Python's.

Your own system (--system): the same Monte Carlo on ranges you write for your own stack, a JSON block or a file under systems/
(systems/README.md): a name, and for any of the six states and the 22 parameters a range [low, high] or one value; the rest keep the
engine's own. The draws keep their one order, so the jump generator gives the same streams; only the ranges they are spread over
change. It is read as numbers only, never run as code. The live engine's "Your own system" panel writes the block, runs it in the
page and sends it to GitHub (.github/workflows/monte-carlo.yml), where the Python and the C++ run it and the record is committed.
Class S: the engine's own mathematics on draws, never a measurement of anyone's stack.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import math
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import replace
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from omnicompass import core as C  # noqa: E402
from tools.engine_runs import jump, mulberry32  # noqa: E402
from tools.legal import NOTICE, TOP  # noqa: E402

DEFAULT_RUNS = 500
DEFAULT_BASE = 20261024
OUT_DIR = ROOT / "results" / "core_runs"
WAYS = ("controlled", "uncontrolled", "wrong_target", "controlled_mu0")
STATE_RANGES = ((0.0, 1.0), (-1.0, 1.0), (0.0, 1.0), (-1.0, 1.0), (-1.0, 1.0), (-1.0, 1.0))   # E, U, I_U, S, B, Ḃ (core.sample_state)
STATE_NAMES = ("E", "U", "I_U", "S", "B", "B_dot")
ENGINE_SYSTEM = "the engine's own ranges"
CPP = ROOT / "cpp" / "build" / "oc_core_runs"
BOUND = 1e6                                   # a range's ends are finite numbers within ±10⁶


def load_system(arg: str) -> dict:
    """A system: a JSON block, or a file holding one (systems/README.md). Numbers only, checked, never run as code. Returns
    {"name", "slug", "about", "state": [[lo, hi] × 6], "params": [[name, lo, hi] × 22]} in the draws' own order."""
    if not arg:
        return {"name": ENGINE_SYSTEM, "slug": "", "about": "", "state": [list(r) for r in STATE_RANGES],
                "params": [[n, lo, hi] for n, (lo, hi) in C.PARAMETER_RANGES.items()]}
    text = arg if arg.lstrip()[:1] in ("{", "[") else Path(arg).read_text(encoding="utf-8")   # a block, or a file holding one
    d = json.loads(text)
    if not isinstance(d, dict):
        raise ValueError("a system is a JSON object: {\"name\": ..., \"state\": {...}, \"params\": {...}}")
    d = {k: v for k, v in d.items() if k not in ("notice", "notice_end")}    # the legal notice a saved system carries at its top and end
    extra = set(d) - {"name", "about", "state", "params"}
    if extra:
        raise ValueError(f"unknown keys: {sorted(extra)} (a system holds name, about, state and params)")
    name = str(d.get("name") or "").strip()
    if not name or len(name) > 80:
        raise ValueError("a system needs a name of 1 to 80 characters")
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")[:40].strip("-") or "system"

    def rng(key, v, lo0, hi0):
        if isinstance(v, (int, float)) and not isinstance(v, bool):
            lo, hi = float(v), float(v)
        elif isinstance(v, list) and len(v) == 2 and all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in v):
            lo, hi = float(v[0]), float(v[1])
        else:
            raise ValueError(f"{key}: a range [low, high] or one number")
        if not (math.isfinite(lo) and math.isfinite(hi)) or abs(lo) > BOUND or abs(hi) > BOUND or lo > hi:
            raise ValueError(f"{key}: low ≤ high, both finite and within ±{BOUND:g}")
        return [lo, hi]

    st, pr = d.get("state") or {}, d.get("params") or {}
    if not isinstance(st, dict) or not isinstance(pr, dict):
        raise ValueError("state and params are objects: {\"U\": [-1, 1], ...}")
    bad = (set(st) - set(STATE_NAMES)) | {f"params.{k}" for k in set(pr) - set(C.PARAMETER_RANGES)}
    if bad:
        raise ValueError(f"unknown names: {sorted(bad)} (the states are {', '.join(STATE_NAMES)}; the parameters those of omnicompass/core.py)")
    return {"name": name, "slug": slug, "about": str(d.get("about") or "")[:400],
            "state": [rng(f"state.{n}", st[n], *STATE_RANGES[i]) if n in st else list(STATE_RANGES[i]) for i, n in enumerate(STATE_NAMES)],
            "params": [[n, *(rng(f"params.{n}", pr[n], lo, hi) if n in pr else [lo, hi])] for n, (lo, hi) in C.PARAMETER_RANGES.items()]}


SYSTEM = load_system("")


def draw(k: int, base: int, system: dict = None):
    """Run k's starting state and parameters from its own stream, in the one order the page draws them, spread over the system's
    ranges (the engine's own unless one is given)."""
    sysd = system or SYSTEM
    seed = jump(base, k)
    r = mulberry32(seed)
    st = [lo + (hi - lo) * r() for lo, hi in sysd["state"]]
    pr = {name: lo + (hi - lo) * r() for name, lo, hi in sysd["params"]}
    return seed, C.State(*st), C.Params(**pr)


def one(k: int, base: int, system: dict = None) -> dict:
    seed, x0, p = draw(k, base, system)
    out = {"k": k, "seed": seed}
    for way in WAYS:
        pp = replace(p, mu=0.0) if way == "controlled_mu0" else p
        tgt = -C.nearest_basin_sign(x0.U) if way == "wrong_target" else None
        r = C.simulate(x0, pp, target=tgt, controlled=(way != "uncontrolled"))
        out[way] = {"U": [float(u) for u in r.U_hist], "convey": int(r.convey_confirm) if r.convey else 0, "cert": int(r.cert_complete) if r.cert else 0}
    return out


def f6(v: float) -> str:
    if not math.isfinite(v):
        return "nan"                          # a run that leaves the numbers is written alike by the Python, the C++ and the page
    s = f"{float(v):.6f}"
    return "0.000000" if s == "-0.000000" else s


def canonical(runs: list) -> str:
    """One line a run and a way: the way, the run, its seed, U at every macro step (six decimals), the convey step and the cert step
    (0 when never), the four ways in order; as the page writes it too."""
    return "\n".join(f"{w}:{r['k']}:{r['seed']}:" + ",".join(f6(u) for u in r[w]["U"]) + f":{r[w]['convey']}:{r[w]['cert']}" for w in WAYS for r in runs)


def digest(runs: list) -> str:
    return hashlib.sha256(canonical(runs).encode("utf-8")).hexdigest()


def summary(runs: list) -> dict:
    out = {}
    for w in WAYS:
        cv = [r[w]["convey"] for r in runs]
        ce = [r[w]["cert"] for r in runs]
        hist = [0] * (C.MACRO_STEPS + 1)
        for c in cv:
            if c:
                hist[c] += 1
        got = [c for c in cv if c]
        out[w] = {"conveyed": len(got), "certified": sum(1 for c in ce if c), "convey_hist": hist,
                  "mean_convey_step": round(sum(got) / len(got), 6) if got else None,
                  "in_basin_at_end": sum(1 for r in runs if C.basin_sign(r[w]["U"][-1]) != 0)}
    return out


def injection(runs_in: list) -> str:
    """The Python's draws as the C++ harness reads them: every run's starting state and 22 parameters (repr round-trips exactly)."""
    L = [f"OCCORE 1 {len(runs_in)}"]
    for k, seed, x0, p in runs_in:
        L.append(f"R {k} {seed} " + " ".join(repr(float(v)) for v in x0.as_tuple()) + " "
                 + " ".join(repr(float(getattr(p, n))) for n in C.PARAMETER_RANGES))
    return "\n".join(L) + "\n"


def cpp_runs(n: int, base: int, system: dict = None, binary: Path = CPP) -> dict:
    """The same draws through the C++ twin of the core: its canonical text, its digest, every U at full precision, the injection's digest."""
    runs_in = [(k, *draw(k, base, system)) for k in range(n)]
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        inj = injection(runs_in)
        (t / "in.txt").write_text(inj, encoding="utf-8")
        subprocess.run([str(binary), str(t / "in.txt"), str(t / "canon.txt"), str(t / "full.txt")], check=True, capture_output=True, text=True)
        canon = (t / "canon.txt").read_text(encoding="utf-8")
        full = {}
        for line in (t / "full.txt").read_text(encoding="utf-8").splitlines():
            w, k, *us = line.split()
            full[(w, int(k))] = [float(u) for u in us]
    return {"canon": canon, "digest": hashlib.sha256(canon.encode("utf-8")).hexdigest(), "full": full,
            "inputs_digest": hashlib.sha256(inj.encode("utf-8")).hexdigest()}


def cpp_compare(runs: list, c: dict) -> dict:
    """The Python's runs against the C++'s: the largest difference over every U of every run and way, and how many run-ways agree to 1e-9."""
    worst, agree, total = 0.0, 0, 0
    for r in runs:
        for w in WAYS:
            a, b = r[w]["U"], c["full"].get((w, r["k"]), [])
            d = max((abs(x - y) if math.isfinite(x) and math.isfinite(y) else (0.0 if (math.isnan(x) and math.isnan(y)) else math.inf)
                     for x, y in zip(a, b)), default=math.inf) if len(a) == len(b) else math.inf
            worst, agree, total = max(worst, d), agree + (d < 1e-9), total + 1
    return {"largest_difference": worst, "agree": agree, "of": total, "same": c["digest"] == digest(runs)}


def cpp_check(n: int, base: int, system: dict = None, binary: Path = CPP) -> int:
    if not Path(binary).exists():
        print(f"the C++ harness is not built: cmake -S cpp -B cpp/build && cmake --build cpp/build --target oc_core_runs ({binary})")
        return 2
    runs = [one(k, base, system) for k in range(n)]
    c = cpp_runs(n, base, system, Path(binary))
    m = cpp_compare(runs, c)
    print(f"the C++ twin of the core on the Python's {n} runs (base {base}, {(system or SYSTEM)['name']}): {m['agree']} of {m['of']} run-ways agree to "
          f"1e-9, largest difference {m['largest_difference']:.1e}; the digests {'match' if m['same'] else 'DIFFER'} "
          f"(Python {digest(runs)[:16]}…, C++ {c['digest'][:16]}…; the injection {c['inputs_digest'][:16]}…)")
    return 0 if m["same"] and m["largest_difference"] < 1e-9 else 1


def page_system(system: dict) -> str:
    """The system as the page's port takes it (a JS literal), or null for the engine's own ranges."""
    if not system or not system.get("slug"):
        return "null"
    return json.dumps({"state": system["state"], "ranges": system["params"]})


def verify(page: Path, n: int, base: int, system: dict = None) -> int:
    """The page's own port of the core (between its CORE-MC markers) run in node on the same set: the digest must be the Python's."""
    s = page.read_text(encoding="utf-8")
    try:
        block = s[s.index("// CORE-MC-BEGIN"):s.index("// CORE-MC-END")]
        gen = s[s.index("function mulberry32"):s.index("\n", s.index("function mulberry32"))]
    except ValueError:
        print("the page carries no port of the core (no CORE-MC markers)")
        return 1
    with tempfile.TemporaryDirectory() as t:
        (Path(t) / "port.js").write_text(gen + "\n" + block + "\nmodule.exports={coreSet,coreCanonical};\n", encoding="utf-8")
        (Path(t) / "drive.js").write_text("const P=require('./port.js');const runs=P.coreSet(%d,%d,0,%d,%s);process.stdout.write(P.coreCanonical(runs));"
                                          % (base, n, n, page_system(system)), encoding="utf-8")
        js = subprocess.run(["node", str(Path(t) / "drive.js")], capture_output=True, text=True, cwd=t)
    if js.returncode:
        print("the page's port did not run:", js.stderr[-400:])
        return 1
    py = [one(k, base, system) for k in range(n)]
    a, b = canonical(py), js.stdout
    same = hashlib.sha256(b.encode("utf-8")).hexdigest() == digest(py)
    worst, lines = 0.0, 0
    for la, lb in zip(a.split("\n"), b.split("\n")):
        if la != lb:
            lines += 1
            ua, ub = la.split(":")[3].split(","), lb.split(":")[3].split(",")
            worst = max([worst] + [abs(float(x) - float(y)) if "nan" not in (x, y) else (0.0 if x == y else math.inf) for x, y in zip(ua, ub)])
    print(f"the page's core and the Python's, {n} runs from base {base} in four ways ({(system or SYSTEM)['name']}): the digests {'match' if same else 'DIFFER'}; "
          f"{lines} of {4 * n} lines differ, largest difference {worst:.1e}")
    return 0 if same else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--runs", type=int, default=DEFAULT_RUNS)
    ap.add_argument("--base", type=int, default=DEFAULT_BASE, help="the jump generator's base seed")
    ap.add_argument("--verify", default="", help="the live engine page: run its port of the core in node and compare")
    ap.add_argument("--out", default="", help="where to write (default results/core_runs/)")
    ap.add_argument("--system", default="", help="your own system: a JSON block, or a file holding one (systems/README.md); empty: the engine's own ranges")
    ap.add_argument("--cpp", default="", help="the C++ harness (cpp/build/oc_core_runs): run the same draws through the C++ twin of the core and record its digest")
    ap.add_argument("--verify-cpp", default="", help="the C++ harness: run the Python's runs through it and compare")
    a = ap.parse_args()
    if not 1 <= a.runs <= 10000:
        print("runs: 1 to 10,000")
        return 2
    try:
        system = load_system(a.system)
    except (ValueError, OSError) as e:
        print(f"the system is not read: {e}")
        return 2
    if a.verify:
        return verify(Path(a.verify), a.runs, a.base, system)
    if a.verify_cpp:
        return cpp_check(a.runs, a.base, system, Path(a.verify_cpp))
    runs = [one(k, a.base, system) for k in range(a.runs)]
    dg, sm = digest(runs), summary(runs)
    data = {"tool": "tools/core_runs.py", "core": "omnicompass/core.py (simulate: RK4, 20 macro steps of 10 micro steps, the bounded command)",
            "runs": a.runs, "base": a.base, "jump": "seed_k = base + k·0x9E3779B9 mod 2^32", "generator": "mulberry32 (the page's own)",
            "macro": C.MACRO_STEPS, "micro": C.MICRO_STEPS, "dt": C.MACRO_DT, "tol": C.BASIN_TOL, "convey_window": C.CONVEY_WINDOW,
            "cert_window": C.CERT_WINDOW, "kp": C.KP, "authority": C.U_AUTHORITY, "ways": list(WAYS), "digest": dg,
            "digest_of": "SHA-256 of every run's U at every macro step (six decimals), its convey and cert steps, one line a run and a way (canonical())",
            "summary": sm, "written": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
    if system["slug"]:   # your own system: its ranges in the record, in the draws' own order
        data["system"] = {"name": system["name"], "slug": system["slug"], "about": system["about"], "state": dict(zip(STATE_NAMES, system["state"])),
                          "params": {n: [lo, hi] for n, lo, hi in system["params"]}}
    if a.cpp:   # the same draws through the C++ twin of the core
        c = cpp_runs(a.runs, a.base, system, Path(a.cpp))
        m = cpp_compare(runs, c)
        data["inputs_digest"] = c["inputs_digest"]
        data["cpp"] = {"tool": "cpp/tools/core_runs.cpp (oc_core_runs) on cpp/src/core.cpp", "digest": c["digest"], "same": m["same"],
                       "largest_difference": m["largest_difference"], "agree": m["agree"], "of": m["of"]}
        if not m["same"]:
            print(f"the C++ twin DIFFERS from the Python: digest {c['digest'][:16]}… against {dg[:16]}…, largest difference {m['largest_difference']:.1e}")
    if os.environ.get("GITHUB_RUN_ID"):
        data["github"] = {"run_id": os.environ["GITHUB_RUN_ID"], "workflow": os.environ.get("GITHUB_WORKFLOW", ""),
                          "commit": os.environ.get("GITHUB_SHA", ""), "ref": os.environ.get("GITHUB_REF_NAME", ""),
                          "url": f"{os.environ.get('GITHUB_SERVER_URL', 'https://github.com')}/{os.environ.get('GITHUB_REPOSITORY', '')}/actions/runs/{os.environ['GITHUB_RUN_ID']}"}
    out = Path(a.out) if a.out else OUT_DIR / (f"CORE_RUNS_{system['slug']}_{a.runs}_{a.base}.json" if system["slug"] else f"CORE_RUNS_{a.runs}_{a.base}.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, separators=(",", ":"), ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
    names = {"controlled": "Omni-Compass on top, toward the nearest basin", "uncontrolled": "native: the plant alone, u = 0",
             "wrong_target": "Omni-Compass aimed at the wrong basin", "controlled_mu0": "Omni-Compass on top, the double well's μ at 0"}
    md = [f"# The core's Monte Carlo: {a.runs} runs from the jump generator (base {a.base}), {system['name']}, one digest", "", f"> {TOP}", "",
          f"Each run: omnicompass/core.simulate, {C.MACRO_STEPS} macro steps of {C.MICRO_STEPS} fourth-order Runge–Kutta micro steps "
          f"(Δt {C.MACRO_DT} s a macro step), from the starting state and parameters its own stream draws (seed_k = base + k·0x9E3779B9 "
          f"mod 2³², mulberry32, the live engine's own generator). Conveyed: {C.CONVEY_WINDOW} macro steps in a row in one basin "
          f"(|U ∓ 1| ≤ {C.BASIN_TOL}); certified: {C.CERT_WINDOW}. Written {data['written']}. Class S.", "",
          f"**Digest {dg}** (SHA-256 of every run's path at six decimals). The live engine's page runs the same set through its own port "
          "of the core and shows its own digest beside this one.", "",
          *([f"**The C++ twin** (`cpp/tools/core_runs.cpp` on `cpp/src/core.cpp`) on the same draws: digest {data['cpp']['digest']}, "
             f"{'the same' if data['cpp']['same'] else 'DIFFERENT'}; {data['cpp']['agree']} of {data['cpp']['of']} run-ways agree to 1e-9, largest "
             f"difference {data['cpp']['largest_difference']:.1e}. The draws themselves, the injection: SHA-256 {data['inputs_digest']}.", ""] if "cpp" in data else []),
          *([f"**Your own system: {system['name']}.** {system['about']} Its ranges (the rest are the engine's own): "
             + "; ".join(f"{n} {lo:g} to {hi:g}" for n, (lo, hi) in [*zip(STATE_NAMES, system['state']), *[(n, (lo, hi)) for n, lo, hi in system['params']]]
                         if [lo, hi] != list(dict(zip(STATE_NAMES, STATE_RANGES)).get(n) or C.PARAMETER_RANGES.get(n))) + ".", ""] if system["slug"] else []),
          "| way | conveyed | certified | mean step conveyed | in a basin at step 20 |", "|---|---:|---:|---:|---:|"]
    for w in WAYS:
        m = sm[w]
        md.append(f"| {names[w]} | {m['conveyed']} of {a.runs} | {m['certified']} of {a.runs} | {m['mean_convey_step'] if m['mean_convey_step'] is not None else '—'} | {m['in_basin_at_end']} of {a.runs} |")
    md += ["", "---", "", f"*{NOTICE}*"]
    out.with_suffix(".md").write_text("\n".join(md), encoding="utf-8")
    print(f"{a.runs} runs from base {a.base}: digest {dg}; controlled {sm['controlled']['conveyed']} conveyed, {sm['controlled']['certified']} certified; "
          f"native (u = 0) {sm['uncontrolled']['conveyed']} conveyed, {sm['uncontrolled']['certified']} certified -> {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
