#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The whole stacks with the real card inside: one harness, one engine, one set of receipts.

Each of seven organisms (the spine, the four realms, the four stacked, each realm keeping its own body so every muscle
runs exactly its own realm's native, and the whole tower; the v5 catalog, realms/catalog_v5.csv) runs on one clock as in the realm
harness, and the real GPU on this machine is wired into it as one more muscle of its GPU Hardware family (a spine family,
so the card sits in every organism; in the four stacked, in the first body): the card serves the pinned request stream
(tools/gpu_workload.py), its own power.draw is heat in the organism's thermal zones and load on its storage sites, and
its meter and its requests are counted in the organism's receipt.

Arms, the same organism, the same seed, the same request stream:
  native  the stacks' own controllers and the card's own firmware, no Omni
  omni    one engine on everything: the v5 law (realms/compass_arm_v5.py) on every simulated muscle and the v5 edge on the
          card's two wires (omni_controller/gpu_compass.py, omnicompass/edge.py); at 90% of the arm every knob and both
          wires are handed back, and the harness checks they were

Sizes (--scales, default 1,10,100): each organism is run as 1, 10 and 100 copies governed together on one clock (100
copies of the whole tower is about 110,000 muscles), with the one real card inside as one more muscle; no 1,000-copy
size is run (the founder's order of 12 October; amendment 13 of docs/GPU_PREREGISTRATION.md). Each size runs its own
number of paired repetitions (--reps-by-scale, default 5,3,2; amendment 11).

Each organism step is --step-s seconds of wall clock (240 steps: 8 minutes at 2 s). A size whose simulated step takes
longer than that gets a longer step, measured on this machine before the run (1.5 times the time the simulation needs
per muscle, times its muscles); the card's request stream runs for the same 240 steps, so the card and the stacks stay
on one clock. Every size's step is in the receipt. The simulated plants are evidence class S (models); the card's
energy and requests are class P (its own meter). The receipt keeps them apart and also adds them up.

  python3 tools/run_hil.py --out results/hil/run-STAMP [--scales 1,10,100] [--reps-by-scale 5,3,2] [--sim]
  python3 tools/run_hil.py --rescore results/hil/run-STAMP      (a finished run reported in full from its own files)
"""
from __future__ import annotations

import argparse

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
import datetime
import hashlib
import json
import math
import os
import shlex
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from realms.harness import catalog, Body, KILL_AT, T95, label  # noqa: E402
from realms.compass_arm_v5 import apply_v5  # noqa: E402  (the engine's law, omni-v5)
from realms.harness import omni_bones, omni_step  # noqa: E402  (the max with its bone, the lease's walk back)
from realms.harness import STACK, TOWER, organism_name  # noqa: E402
from realms.presets import ORGANISM_STEPS  # noqa: E402
from tools.readings import labelled, GAIN, STEADY, LOSS, GIVEN  # noqa: E402  (the words every table uses)
from tools.run_realms_v5 import SPINE, spine_rows  # noqa: E402  (the spine, the seventh organism)

REALMS = ("compute_ai_cloud", "physics_robotics_autonomous", "energy_facility_industrial", "distribution_specialized")
NAMES = {SPINE: "The spine, the muscles every stack runs on",
         "compute_ai_cloud": "Compute / AI / Cloud", "physics_robotics_autonomous": "Physics / Robotics / Autonomous",
         "energy_facility_industrial": "Energy / Facility / Industrial", "distribution_specialized": "Distribution / Specialized",
         STACK: "The four stacked, duplicates kept", TOWER: "The whole tower, every muscle once"}
SEED0 = 6000
SMI_FIELDS = "timestamp,power.draw,clocks.sm,power.limit,utilization.gpu,temperature.gpu"


def smi(a, *args, check=False):
    return subprocess.run(shlex.split(a.smi) + list(args), capture_output=True, text=True, timeout=30, check=check)


def limit(a):
    return float(smi(a, "-i", str(a.gpu), "--query-gpu=power.limit", "--format=csv,noheader,nounits", check=True).stdout.strip())


def parse_ts(s):
    return datetime.datetime.strptime(s.strip(), "%Y/%m/%d %H:%M:%S.%f").timestamp()


def card_energy(path):
    """Joules from the card's own power.draw samples (trapezoid over their timestamps)."""
    pts = []
    for line in open(path):
        v = [x.strip() for x in line.split(",")]
        try:
            pts.append((parse_ts(v[0]), float(v[1])))
        except (ValueError, IndexError):
            continue
    return sum(0.5 * (p0 + p1) * (t1 - t0) for (t0, p0), (t1, p1) in zip(pts, pts[1:]) if t1 > t0), len(pts)


def last_draw(path, fallback):
    try:
        with open(path, "rb") as f:
            f.seek(0, 2); n = f.tell(); f.seek(max(0, n - 400))
            line = f.read().decode(errors="ignore").strip().splitlines()[-1]
        return float(line.split(",")[1])
    except (OSError, ValueError, IndexError):
        return fallback


CATALOG = str(ROOT / "realms" / "catalog_v5.csv")             # the v5 muscle set


def groups(scale=1):
    """Each organism's muscles. The four stacked are each realm's own muscles side by side (every shared muscle in each,
    with the same id it has in its own realm, so its native is identical there); bodies_for builds their four bodies."""
    rows = catalog(CATALOG)
    g = {SPINE: spine_rows(rows)}                        # the base every stack runs on, an organism of its own
    g.update({r: [x for x in rows if r in x["realms"].split(";")] for r in REALMS})
    g[STACK] = [x for realm in REALMS for x in g[realm]]
    g[TOWER] = rows
    # scale copies of each organism on one clock, each copy its own seeds (as tools/run_scale.py)
    return {k: [dict(r, muscle_id=r["muscle_id"] + (f"~{c}" if c else "")) for c in range(scale) for r in v]
            for k, v in g.items()}


def bodies_for(name, scale, seed, rows=None):
    """The organism's bodies on one clock: the four stacked keep each realm's own body, so every muscle runs exactly the
    native of its own realm, plant by plant; every other organism is one body. The real cluster or card lives in the
    first body (the Compute realm's in the stack)."""
    if organism_name(name) == STACK:
        g = groups(scale)
        return [Body(g[realm], seed) for realm in REALMS]
    return [Body(rows if rows is not None else groups(scale)[name], seed)]


def per_muscle_step_s():
    """What one simulated step costs per muscle on this machine (the whole tower, a few steps, both laws' work)."""
    rows = groups(1)[TOWER]
    body = Body(rows, SEED0)
    t = time.time()
    for _ in range(5):
        body.couple()
        for p, knob in zip(body.plants, body.knobs):
            apply_v5(p, knob)
        body.step()
    return (time.time() - t) / 5 / len(rows)


def run_arm(a, name, rows, seed, arm, d, slo_ms, start_w, step_s=None, scale=1):
    step_s = step_s or a.step_s
    d.mkdir(parents=True, exist_ok=True)
    bodies = bodies_for(name, scale, seed, rows)
    body = bodies[0]                                              # the body the card lives in
    for f in ("kill",):
        (d / f).unlink(missing_ok=True)
    smi(a, "-i", str(a.gpu), "-rgc")
    w0 = limit(a)
    sampler = subprocess.Popen(shlex.split(a.smi) + ["-i", str(a.gpu), f"--query-gpu={SMI_FIELDS}", "--format=csv,noheader,nounits",
                                                     "-lms", "200"], stdout=open(d / "smi.csv", "w"), stderr=subprocess.DEVNULL)
    dur = ORGANISM_STEPS * step_s
    wl = [sys.executable, str(ROOT / "tools" / "gpu_workload.py"), "run", "--calib-file", str(a.out / "calib.json"),
          "--out", str(d), "--device", f"cuda:{a.gpu}", "--duration", str(dur), "--drain", str(a.drain)]
    if a.sim:
        wl.append("--sim")
    work = subprocess.Popen(wl, stdout=open(d / "workload.log", "w"), stderr=subprocess.STDOUT)
    gov = None
    if arm == "omni":
        gov = subprocess.Popen([sys.executable, "-m", "omni_controller.gpu_compass", "--mode", "cap", "--gpus", str(a.gpu),
                                "--smi", a.smi, "--interval", str(a.interval), "--audit", str(d / "audit.jsonl"),
                                "--kill-file", str(d / "kill"), "--latency-file", str(d / "latency.csv"),
                                "--slo-ms", str(slo_ms), "--floor-w", str(a.floor_w)], cwd=ROOT,
                               stdout=open(d / "governor.log", "w"), stderr=subprocess.STDOUT)
    kill_at = int(KILL_AT * ORGANISM_STEPS)
    writes = after_kill = 0
    restore_ok = True
    last = {}
    t0 = time.time()
    draw = 0.0
    bones = omni_bones(bodies) if arm == "omni" else []
    for k in range(ORGANISM_STEPS):
        for b in bodies:
            b.couple()
        if arm == "omni":
            if k == kill_at:
                (d / "kill").touch()                              # the card's governor hands both wires back
            writes += omni_step(bodies, bones, k, kill_at)        # the max with its bone; after the kill the walk back
        for b in bodies:
            b.step()
        draw = last_draw(d / "smi.csv", draw)
        body.src_w += draw; body.sz_w += draw; body.all_w += draw      # the card's watts in the organism
        wait = t0 + (k + 1) * step_s - time.time()
        if wait > 0:
            time.sleep(wait)
    plants = [p for b in bodies for p in b.plants]
    for p in plants:
        p.finalize()
        restore_ok = restore_ok and (arm != "omni" or p.override == {})
    work.wait()
    gov_exit = None
    if gov is not None:
        (d / "kill").touch(); gov.wait(timeout=120); gov_exit = gov.returncode
    sampler.terminate(); sampler.wait()
    smi(a, "-i", str(a.gpu), "-rgc")
    w1 = limit(a)
    if abs(w1 - start_w) >= 1.0:
        smi(a, "-i", str(a.gpu), "-pl", str(int(start_w)))
    joules, samples = card_energy(d / "smi.csv")
    summ = json.loads((d / "summary.json").read_text()) if (d / "summary.json").exists() else {}
    lat = sorted(float(x.split(",")[1]) for x in list(open(d / "latency.csv"))[1:] if x.strip()) if (d / "latency.csv").exists() else []
    over = 100.0 * sum(1 for x in lat if x > slo_ms) / len(lat) if lat else 0.0      # the card's time over its line
    rec = {"organism": name, "arm": arm, "seed": seed, "muscles": len(plants), "step_s": step_s,
           "plants": [dict(p.m) for p in plants], "sim_writes": writes, "sim_restore_ok": restore_ok,
           "card": {"energy_j": joules, "samples": samples, "served": summ.get("served", 0),
                    "not_served": summ.get("not_served", summ.get("requests", 0) - summ.get("served", 0)),
                    "p95_ms": lat[int(0.95 * (len(lat) - 1))] if lat else None, "over_line_pct": over, "limit_start_w": w0, "limit_end_w": w1,
                    "restored": abs(w1 - start_w) < 1.0, "governor_exit": gov_exit},
           "wall_s": round(time.time() - t0, 1)}
    (d / "arm.json").write_text(json.dumps(rec, indent=1))
    return rec


def ci(xs):
    n = len(xs); m = sum(xs) / n
    if n < 2:
        return m, m, m
    sd = math.sqrt(sum((x - m) ** 2 for x in xs) / (n - 1)); h = T95.get(n - 1, 2.0) * sd / math.sqrt(n)
    return m, m - h, m + h


def contrast(o, n):
    """Per-seed contrasts: the simulated stacks, the card, and both together (the card as one more plant)."""
    rs = [(a["work"] / b["work"]) if b["work"] else 1.0 for a, b in zip(o["plants"], n["plants"])]
    es, en = sum(p["energy_j"] for p in o["plants"]), sum(p["energy_j"] for p in n["plants"])
    va = sum(p["viol"] for p in o["plants"]) / sum(p["steps"] for p in o["plants"])
    vn = sum(p["viol"] for p in n["plants"]) / sum(p["steps"] for p in n["plants"])
    cw = (o["card"]["served"] / n["card"]["served"]) if n["card"]["served"] else 1.0
    ce = (o["card"]["energy_j"] / n["card"]["energy_j"]) if n["card"]["energy_j"] else 1.0
    w_all = (sum(rs) + cw) / (len(rs) + 1)
    e_all = (es + o["card"]["energy_j"]) / (en + n["card"]["energy_j"])
    sim_w = sum(rs) / len(rs)
    # the card is judged on its own response time as well as its work and energy: its time over the line (requests
    # slower than the line, percent) and its 95th percentile, Omni against native
    po, pn = o["card"].get("p95_ms"), n["card"].get("p95_ms")
    p95 = (po / pn - 1) if po and pn else 0.0
    cv = o["card"].get("over_line_pct", 0.0) - n["card"].get("over_line_pct", 0.0)
    nc = len(rs) + 1                                               # both: the card as one more plant in the share
    v_all = (va * (nc - 1) + o["card"].get("over_line_pct", 0.0) / 100) / nc - (vn * (nc - 1) + n["card"].get("over_line_pct", 0.0) / 100) / nc
    return {"sim": {"primary": sim_w / (es / en) - 1, "work": sim_w - 1, "energy": es / en - 1, "viol_pp": 100 * (va - vn), "p95": 0.0},
            "card": {"primary": cw / ce - 1, "work": cw - 1, "energy": ce - 1, "viol_pp": cv, "p95": p95},
            "all": {"primary": w_all / e_all - 1, "work": w_all - 1, "energy": e_all - 1, "viol_pp": 100 * v_all, "p95": p95}}


# each measure's declared aim, in words, so a sign is never read on its own (tools/readings.py): work per energy and work aim
# higher; energy is a resource spent (a cut is a GAIN, a rise is power given); time over the line and p95 aim lower
AIM_UP = {"primary": "more work per energy", "work": "more work"}
AIM_DOWN = {"energy": "less energy spent", "viol_pp": "late less often", "p95": "faster"}
AWAY = {"primary": "less work per energy", "work": "less work", "energy": "more energy spent", "viol_pp": "late more often",
        "p95": "slower"}


def away_word(k):
    """The word a measure reads when it moves away from its aim: power given for the energy spent, LOSS for the rest."""
    return GIVEN if k == "energy" else LOSS


def reading(k, v, eps=1e-9):
    """A measure's change against native, read in words: its word (GAIN, LOSS, power given) and what it means, or STEADY."""
    if abs(v) <= eps:
        return f"({STEADY})"
    toward = v > 0 if k in AIM_UP else v < 0
    return f"({GAIN}: {AIM_UP.get(k) or AIM_DOWN.get(k)})" if toward else f"({away_word(k)}: {AWAY[k]})"


def away_on(xs):
    """Every measure that read LOSS or power given against native on the mean, by any amount, in words (no line drawn: the
    reader sees what it takes beside what it gives)."""
    m = lambda k: sum(x[k] for x in xs) / len(xs)
    return [f"{away_word(k)}: {AWAY[k]} ({100 * m(k):+.2f}%)" if k != "viol_pp" else f"{away_word(k)}: {AWAY[k]} ({m(k):+.2f} pp)"
            for k in ("primary", "work", "energy", "p95", "viol_pp") if reading(k, m(k)) == f"({away_word(k)}: {AWAY[k]})"]


def write_prefixes(root, res):
    """Report actual first 1/10/100 paired repetitions; missing pairs never shift later runs into a prefix."""
    rows = []
    lines = ["# GPU organism nested repetition prefixes", "",
             "Requested prefixes are 1, 10 and 100 runs. Incomplete prefixes retain their actual completed count.", "",
             "| Copies | Organism | Prefix | Paired runs | Part | Reading |",
             "|---:|---|---:|---:|---|---|"]
    for (scale, name), reps in sorted(res.items()):
        for n in (1, 10, 100):
            pairs = []
            for rep, arms in reps.items():
                index = int(rep[4:]) - 1 if isinstance(rep, str) else rep
                if 0 <= index < n and "omni" in arms and "native" in arms:
                    pairs.append(contrast(arms["omni"], arms["native"]))
            for part in ("sim", "card", "all"):
                xs = [p[part] for p in pairs]
                word = labelled(label(xs)) if len(xs) >= 2 else ("ONE REPETITION (no label)" if xs else "INCOMPLETE")
                rows.append({"copies": scale, "organism": name, "prefix": n, "paired_runs": len(xs),
                             "part": part, "reading": word, "complete": len(xs) == n})
                lines.append(f"| {scale} | {name} | {n} | {len(xs)} of {n} | {part} | {word} |")
    root = Path(root)
    (root / "HIL_PREFIXES.json").write_text(json.dumps(rows, indent=2) + "\n")
    (root / "HIL_PREFIXES.md").write_text("\n".join(_legal_stamp(lines)) + "\n")


def rescore(root):
    """A finished card run reported in full from its own raw files (arm.json and latency.csv): the card's
    time over the line is counted from latency.csv where the run did not record it. Writes HIL_RESCORED.md."""
    root = Path(root)
    meta = json.loads((root / "HIL.json").read_text())["run"] if (root / "HIL.json").exists() else {}
    slo = float(meta.get("slo_ms") or json.loads((root / "calib.json").read_text())["service_ms"] * 10)
    res = {}
    for f in sorted(root.rglob("arm.json")):
        r = json.loads(f.read_text())
        if "over_line_pct" not in r["card"] and (f.parent / "latency.csv").exists():
            lat = [float(x.split(",")[1]) for x in list(open(f.parent / "latency.csv"))[1:] if x.strip()]
            r["card"]["over_line_pct"] = 100.0 * sum(1 for x in lat if x > slo) / len(lat) if lat else 0.0
        size = next((int(p.name[5:]) for p in f.parents if p.name.startswith("size-")), 1)
        rep = next((p.name for p in f.parents if p.name.startswith("rep-")), "rep-1")
        res.setdefault((size, r["organism"]), {}).setdefault(rep, {})[r["arm"]] = r
    L = [f"# The card run in full, from its own files (amendment 11)", "",
         f"Run `{root.name}`, commit `{str(meta.get('commit', ''))[:12]}`, line {slo} ms. Every measure from the run's "
         "own files, the card's response times included; every measure that read LOSS or power given is named.", "",
         "| Size | Organism | Part | Repetitions | Reading | Work per energy | Energy | Time over the line (pp) | p95 |",
         "|---:|---|---|---:|---|---:|---:|---:|---:|"]
    for (sc, name), reps in sorted(res.items()):
        per = [contrast(a["omni"], a["native"]) for a in reps.values() if "omni" in a and "native" in a]
        if not per:
            continue
        for part, pname in (("sim", "stacks (model)"), ("card", "card (meter)"), ("all", "both")):
            xs = [p[part] for p in per]
            bad = away_on(xs)
            lab = (labelled(label(xs)) if len(xs) >= 2 else "ONE REPETITION (no label)") + (("; " + ", ".join(bad)) if bad else "")
            mm = lambda k: sum(x[k] for x in xs) / len(xs)
            L.append(f"| {sc}x | {NAMES[name]} | {pname} | {len(xs)} | {lab} | {100 * mm('primary'):+.2f}% | {100 * mm('energy'):+.2f}% | "
                     f"{mm('viol_pp'):+.2f} | {100 * mm('p95'):+.1f}% |")
    write_prefixes(root, res)
    (root / "HIL_RESCORED.md").write_text("\n".join(_legal_stamp(L)) + "\n")
    print("\n".join(L))
    return 0


def main(argv=None):
    if argv is None and len(sys.argv) > 2 and sys.argv[1] == "--rescore":
        return rescore(sys.argv[2])
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True)
    ap.add_argument("--reps", type=int, default=None, help="one number of repetitions for every size (overrides --reps-by-scale)")
    ap.add_argument("--scales", default=os.environ.get("HIL_SCALES", "1,10,100"))
    ap.add_argument("--reps-by-scale", default=os.environ.get("HIL_REPS_BY_SCALE", "5,3,2"))
    ap.add_argument("--step-s", type=float, default=float(os.environ.get("HIL_STEP_S", 2.0)))
    ap.add_argument("--organisms", default=os.environ.get("HIL_ORGANISMS", ",".join((SPINE,) + REALMS + (STACK, TOWER))))
    ap.add_argument("--gpu", type=int, default=int(os.environ.get("GPU", 0)))
    ap.add_argument("--smi", default=os.environ.get("NVIDIA_SMI", "nvidia-smi"))
    ap.add_argument("--interval", type=float, default=2.0)
    ap.add_argument("--drain", type=float, default=10.0)
    ap.add_argument("--floor-w", type=float, default=float(os.environ.get("ENV_FLOOR_W", 0.0)))
    ap.add_argument("--sim", action="store_true", default=bool(os.environ.get("SIM")))
    ap.add_argument("--workload-args", default=os.environ.get("WORKLOAD_ARGS", ""))
    a = ap.parse_args(argv)
    scales = [int(x) for x in a.scales.split(",") if x.strip()]
    if not scales or any(x not in (1, 10, 100) for x in scales):
        ap.error("organism scales must be drawn from 1,10,100")
    rbs = [int(x) for x in a.reps_by_scale.split(",") if x.strip()]
    if not rbs:
        ap.error("repetitions by scale must not be empty")
    reps_of = {sc: (a.reps if a.reps is not None else (rbs[i] if i < len(rbs) else rbs[-1])) for i, sc in enumerate(scales)}
    if not rbs or any(n < 1 or n > 100 for n in reps_of.values()):
        ap.error("paid GPU repetitions must be between 1 and 100")
    a.out = Path(a.out); a.out.mkdir(parents=True, exist_ok=True)
    start_w = limit(a)
    cal = [sys.executable, str(ROOT / "tools" / "gpu_workload.py"), "calibrate", "--out", str(a.out), "--device",
           f"cuda:{a.gpu}"] + shlex.split(a.workload_args) + (["--sim"] if a.sim else [])
    subprocess.run(cal, check=True, capture_output=True)
    service = json.loads((a.out / "calib.json").read_text())["service_ms"]
    slo_ms = round(10 * service, 1)
    commit = subprocess.run(["git", "-c", "safe.directory=*", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    cost = per_muscle_step_s()
    names = [n for n in a.organisms.split(",") if n]
    sizes = {sc: {n: len(r) for n, r in groups(sc).items() if n in names} for sc in scales}
    steps_of = {sc: {n: round(max(a.step_s, 1.5 * cost * m), 2) for n, m in sizes[sc].items()} for sc in scales}
    from tools.omni_version import engine_files, version_of, digest
    engine_snapshot = engine_files()
    run = {"started": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()), "commit": commit, "scales": scales,
           "engine": version_of(engine_snapshot) or "undeclared", "engine_digest": digest(engine_snapshot),
           "reps_by_scale": reps_of, "step_s_by_scale": steps_of, "sim_step_s_per_muscle": cost,
           "steps": ORGANISM_STEPS, "start_limit_w": start_w, "slo_ms": slo_ms, "sim_card": a.sim}
    res = {}
    for sc in scales:
        g = groups(sc)
        for rep in range(reps_of[sc]):
            seed = SEED0 + rep
            for i, name in enumerate(names):
                order = ("native", "omni") if (rep + i) % 2 == 0 else ("omni", "native")
                for arm in order:
                    print(f"== size {sc}x, rep {rep + 1}, {NAMES[name]}, arm {arm} (step {steps_of[sc][name]} s)", flush=True)
                    res.setdefault((sc, name), {}).setdefault(rep, {})[arm] = run_arm(
                        a, name, g[name], seed, arm, a.out / f"size-{sc}" / f"rep-{rep + 1}" / name / arm, slo_ms, start_w,
                        steps_of[sc][name], scale=sc)
    problems = []
    for (sc, name), reps in res.items():
        for rep, arms in reps.items():
            for arm, r in arms.items():
                tag = f"{sc}x {name} rep {rep + 1}"
                if not r["card"]["restored"]:
                    problems.append(f"{tag} {arm}: power limit {r['card']['limit_end_w']} W at the end, start {start_w} W")
                if arm == "omni" and not r["sim_restore_ok"]:
                    problems.append(f"{tag}: a simulated knob was not handed back")
                if arm == "omni" and r["card"]["governor_exit"] not in (0,):
                    problems.append(f"{tag}: the card's governor exited {r['card']['governor_exit']}")
    L = ["# The whole stacks with the real card inside", "",
         f"Run {run['started']}, commit `{commit[:12]}`, sizes {scales} (copies of each organism on one clock), paired "
         f"repetitions by size {reps_of}, seeds from {SEED0}, {ORGANISM_STEPS} steps per arm; step length by size and organism "
         f"(seconds, measured on this machine): {steps_of}. Card: {'SIMULATED (standin nvidia-smi)' if a.sim else 'the real GPU, its own meter'}; "
         f"start power limit {start_w} W; response-time line {slo_ms} ms (ten bare service times). One engine on everything "
         "in the Omni arm: the compass law on every simulated muscle and on the card's two wires. Harness `tools/run_hil.py`.", "",
         "The simulated stacks are models (evidence S). The card's energy and requests are its own meter (evidence P). "
         "Work per energy: (work Omni / work native) / (energy Omni / energy native) - 1; for the stacks work is the mean "
         "over plants of each plant's ratio; *both* counts the card as one more plant and adds its joules.", "",
         "## Omni against native, by organism (mean over repetitions, 95% interval when there are two or more)", "",
         "The reading is the preregistered label (the primary outcome and its interval, the time over the line first), its word "
         "first; beside it, every measure that read LOSS or power given, by any amount, is named, so what Omni takes is read "
         "beside what it gives.", "",
         "How to read a row: each change is Omni against native on the same organism, seed and requests, and carries its word, "
         "GAIN, STEADY or LOSS, by what the measure is for, never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`). Work "
         "per energy and work aim higher. Energy is a resource spent: a cut is a GAIN (a lower power bill, or longer on the same "
         "supply), a rise is power given. Time over the line and p95 aim lower (faster answers). So a minus is a GAIN on energy, "
         "lateness and p95, and a LOSS on work.", "",
         "| Size | Organism | Part | Reading | Work per energy | Work | Energy | Time over the line (pp) | p95 |", "|---:|---|---|---|---:|---:|---:|---:|---:|"]
    out = {}
    for (sc, name) in res:
        per = [contrast(res[(sc, name)][r]["omni"], res[(sc, name)][r]["native"]) for r in sorted(res[(sc, name)])]
        key = f"{sc}x/{name}"
        out[key] = {}
        for part, pname in (("sim", "stacks (model)"), ("card", "card (meter)"), ("all", "both")):
            xs = [p[part] for p in per]
            m = {k: ci([x[k] for x in xs]) for k in ("primary", "work", "energy", "viol_pp", "p95")}
            bad = away_on(xs)
            lab = (labelled(label(xs)) if len(xs) >= 2 else "ONE REPETITION (no label)") + (("; " + ", ".join(bad)) if bad else "")
            out[key][part] = {"label": lab, "away_on": bad, **{k: list(v) for k, v in m.items()}}
            f = lambda k, s=100.0, u="%": (f"{s * m[k][0]:+.2f}{u}" + (f" ({s * m[k][1]:+.2f} to {s * m[k][2]:+.2f})" if len(xs) > 1 else "")
                                            + f" {reading(k, m[k][0])}")
            L.append(f"| {sc}x | {NAMES[name]} | {pname} | {lab} | {f('primary')} | {f('work')} | {f('energy')} | {f('viol_pp', 1.0, '')} | {f('p95')} |")
    L += ["", "## The card's receipts, by arm", "", "| Size | Organism | Rep | Arm | Card energy (J) | Requests served | Not served | p95 (ms) | Over the line (%) | Limit start → end (W) | Governor exit |",
          "|---:|---|---:|---|---:|---:|---:|---:|---:|---|---|"]
    for (sc, name) in res:
        for rep in sorted(res[(sc, name)]):
            for arm in ("native", "omni"):
                c = res[(sc, name)][rep][arm]["card"]
                L.append(f"| {sc}x | {NAMES[name]} | {rep + 1} | {arm} | {c['energy_j']:.0f} | {c['served']} | {c['not_served']} | "
                         f"{c['p95_ms'] if c['p95_ms'] is None else round(c['p95_ms'], 1)} | {c.get('over_line_pct', 0.0):.2f} | {c['limit_start_w']} → {c['limit_end_w']} | {c['governor_exit']} |")
    L += ["", "## Validity", ""] + ([f"- {p}" for p in problems] or ["- Every arm ended with the card at its start limit and its own clock range; every simulated knob was handed back; the card's governor exited cleanly."])
    L += ["", "Raw: every arm's `arm.json`, `smi.csv` (the card's own samples), `latency.csv`, `requests.csv`, `audit.jsonl`; checksums in `SHA256SUMS.txt`."]
    (a.out / "HIL.md").write_text("\n".join(_legal_stamp(L)) + "\n")
    write_prefixes(a.out, res)
    (a.out / "HIL.json").write_text(json.dumps({"run": run, "results": out, "problems": problems}, indent=1) + "\n")
    sums = [f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(a.out)}" for p in sorted(a.out.rglob("*"))
            if p.is_file() and p.name != "SHA256SUMS.txt"]
    (a.out / "SHA256SUMS.txt").write_text("\n".join(sums) + "\n")
    print("\n".join(L))
    return 2 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
