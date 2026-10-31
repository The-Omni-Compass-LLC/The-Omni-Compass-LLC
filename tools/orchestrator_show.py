# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The first showing of Omni-Compass's own orchestrator (omni_orchestrator/), on this one host, every piece a real
process, every answer checked.

Six machines of half a processor each (the kernel's CPU quotas; two machines on each of cores 0, 1 and 2); the control
plane, the front, the machines' hands and the clients on core 3. The service: units of 250 millicores (request and
limit), each answer a 40 ms chain of hashes whose digest the client checks.

  1. native         the yardstick: Kubernetes' published autoscaling rule (every 15 s, 50% target, 300 s before a fall),
                    the units spread as Kubernetes' scheduler spreads them, every machine on (a fixed cluster)
  1b. Omni on native  Omni on top of that rule, the engine's strict form as on the kind rigs: the units are the rule's
                    (never fewer); Omni adds a unit when work waits and past the wall, conveys each unit's CPU wall to
                    the room its machine can spare, places by the busy rule, packs, parks and wakes machines
  2. Omni direct    Omni alone on the machines, at a 5 s beat: the reflex on work in line, the compass law on the 95th
                    percentile, the yardstick twin less the depth the verdict allows on the service's own response
                    times, each unit's CPU wall conveyed (the engine's rule), units packed, machines parked and woken
                    (two at least, a 10 s boot)
     the same clients for all three: 1 2 3 2 3 4 3 4 5 4 5 6 5 6 7 6 7 8, 25 s a step
  3. one body       a batch job of 16 tasks beside the service, Omni deciding; the service grows midway
  4. the drills     with Omni: a unit killed, a machine lost and repaired, the control plane killed and started
                    again, the kill switch on and off, the clients running through all of it

python3 tools/orchestrator_show.py --out DIR [--quick]; python3 tools/orchestrator_show.py --report DIR rebuilds the
report from the files of a finished showing. Run and scored by The Omni-Compass LLC's own code. No outside party has
reviewed or approved these results.
"""
from __future__ import annotations

import argparse
import csv
import html
import json
import math
import os
import signal
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from omni_orchestrator.cgroup import Walls  # noqa: E402
from omni_orchestrator.workload import calibrate  # noqa: E402

PY = sys.executable
STEPS = [1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5, 6, 7, 6, 7, 8]
MACHINES = [(f"m{i}", 7100 + i, (i - 1) // 2) for i in range(1, 7)]     # name, port, core
CTL_CORE = 3
TOP = ("© 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only. Any commercial use, "
       "commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass "
       "requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and "
       "printout carries this notice with LICENSE, NOTICE and DISCLOSURES.md. All patents, copyrights and trademarks "
       "filed in the USA. www.omni-compass.com")


class Show:
    def __init__(self, out: Path, quick: bool, room_rule: str = "requests"):
        self.out, self.quick, self.room_rule = out, quick, room_rule
        self.out.mkdir(parents=True, exist_ok=True)
        self.agents: dict[str, subprocess.Popen] = {}
        self.procs: list[subprocess.Popen] = []
        self.events: list[dict] = []
        self.t_show = time.time()

    def spawn(self, args: list[str], log: str, core: int = CTL_CORE) -> subprocess.Popen:
        f = open(self.out / log, "a")
        p = subprocess.Popen([PY, "-m", *args], cwd=ROOT, stdout=f, stderr=subprocess.STDOUT, start_new_session=True)
        try:
            os.sched_setaffinity(p.pid, {core})
        except OSError:
            pass                                          # a host with fewer cores: the piece runs where the kernel puts it
        self.procs.append(p)
        return p

    def start_agent(self, name: str, port: int, core: int) -> None:
        self.agents[name] = self.spawn(["omni_orchestrator.agent", "--name", name, "--port", str(port), "--cores",
                                        str(core), "--cpu-m", "500", "--mem-mb", "1024", "--state-dir",
                                        str(self.out / "machines" / name)], f"agent-{name}.log")

    def agent(self, name: str, path: str, method: str = "GET"):
        port = dict((n, p) for n, p, _ in MACHINES)[name]
        req = urllib.request.Request(f"http://127.0.0.1:{port}{path}", method=method, data=b"{}" if method == "POST" else None)
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.loads(r.read())

    def machine_cpu(self) -> dict[str, float]:
        return {n: Walls(n).cpu_s() for n, _, _ in MACHINES}

    def stop(self, p: subprocess.Popen, sig=signal.SIGTERM) -> None:
        try:
            os.killpg(p.pid, sig)
        except OSError:
            pass
        try:
            p.wait(10)
        except subprocess.TimeoutExpired:
            os.killpg(p.pid, signal.SIGKILL)

    def clear_units(self) -> None:
        for n, _, _ in MACHINES:
            try:
                self.agent(n, "/stop_all", "POST")
            except Exception:
                pass

    def spec(self, phase: str, front_port: int, jobs: list | None = None) -> Path:
        d = self.out / phase
        d.mkdir(parents=True, exist_ok=True)
        spec = {"routes": str(d / "routes.json"), "front_stats": f"http://127.0.0.1:{front_port}/_stats",
                "floor_machines": 2, "boot_s": 10, "drain_s": 2, "step_units": 2, "max_step": 3, "park_hold_beats": 3,
                "port_base": 9100 + 400 * len(list(self.out.glob("*/spec.json"))),
                "machines": [{"name": n, "url": f"http://127.0.0.1:{p}", "cpu_m": 500} for n, p, _ in MACHINES],
                "services": [{"name": "web", "replicas": 2, "min": 2, "max": 12, "req_m": 250, "limit_m": 250,
                              "mem_mb": 256, "k": self.k, "line_ms": 800, "health": "/health"}],
                "jobs": jobs or []}
        (d / "spec.json").write_text(json.dumps(spec, indent=1))
        return d

    def wait_ready(self, d: Path, n: int, timeout: float = 60) -> None:
        end = time.time() + timeout
        while time.time() < end:
            try:
                if len(json.loads((d / "routes.json").read_text()).get("web", [])) >= n:
                    return
            except (OSError, ValueError):
                pass
            time.sleep(0.5)
        raise SystemExit(f"{d.name}: the declared units were not ready in {timeout} s")

    def phase(self, name: str, brain: str, front_port: int, steps: list[int], step_s: float, jobs=None,
              during=None) -> dict:
        d = self.spec(name, front_port, jobs)
        front = self.spawn(["omni_orchestrator.front", "--port", str(front_port), "--service", "web", "--routes",
                            str(d / "routes.json"), "--stats", str(d / "front.jsonl")], f"{name}-front.log")
        ctl_args = ["omni_orchestrator.control", "--spec", str(d / "spec.json"), "--state-dir", str(d / "ctl"),
                    "--brain", brain, "--beat", "5", "--kill-file", str(d / "KILL")]
        # Omni's room rule is the engine's own (the machine's measured busy share under 75%); the yardstick places by
        # requests alone, as Kubernetes' scheduler does
        ctl_args += ["--room-rule", self.room_rule if brain in ("omni", "omni_native") else "requests"]
        ctl = self.spawn(ctl_args, f"{name}-control.log")
        self.wait_ready(d, 2)
        cpu0, t0 = self.machine_cpu(), time.time()
        load = self.spawn(["omni_orchestrator.load", "--port", str(front_port), "--k", str(self.k), "--steps",
                           ",".join(map(str, steps)), "--step-s", str(step_s), "--think-s", "0.1", "--out",
                           str(d / "requests.csv"), "--start-at", str(t0 + 6)], f"{name}-load.log")
        ctx = {"dir": d, "ctl": ctl, "ctl_args": ctl_args, "t0": t0 + 6}
        if during:
            during(self, ctx)
        load.wait(timeout=len(steps) * step_s + 180)
        cpu1, t1 = self.machine_cpu(), time.time()
        self.stop(ctx["ctl"])
        self.stop(front)
        self.clear_units()
        meta = {"phase": name, "brain": brain, "room_rule": self.room_rule if brain in ("omni", "omni_native") else "requests",
                "t_load": t0 + 6, "steps": steps, "step_s": step_s,
                # a machine lost and repaired inside a phase starts its kernel counter afresh: never a negative use
                "cpu_s": {m: max(0.0, cpu1[m] - cpu0[m]) for m in cpu0}, "wall_s": t1 - t0, "events": ctx.get("events", [])}
        (d / "meta.json").write_text(json.dumps(meta, indent=1))
        time.sleep(3)
        return meta

    def run(self) -> None:
        # a fresh rig: nothing left running in any machine's group from an earlier showing (the 23 October full run's batch
        # part failed to bind a port held by a unit the quick showing had left behind)
        for pid in Walls().pids():
            try:
                os.kill(pid, signal.SIGKILL)
            except OSError:
                pass
        Walls().remove()
        self.k = calibrate(40.0)
        self.k_task = calibrate(2000.0)
        (self.out / "calibration.json").write_text(json.dumps({"k_40ms": self.k, "k_task_2s": self.k_task}))
        for n, p, c in MACHINES:
            self.start_agent(n, p, c)
        time.sleep(2)
        steps, step_s = (STEPS[:6], 15.0) if self.quick else (STEPS, 25.0)
        try:
            self.phase("yardstick", "yardstick", 8101, steps, step_s)          # native: Kubernetes' rule alone
            self.phase("omni_native", "omni_native", 8105, steps, step_s)      # Omni on top of the native rule
            self.phase("omni", "omni", 8102, steps, step_s)                    # Omni direct: Omni alone on the machines
            job = [{"name": "crunch", "tasks": 16, "parallel": 4, "req_m": 250, "limit_m": 250, "k": self.k_task,
                    "out": str(self.out / "batch" / "results")}]
            self.phase("batch", "omni", 8103, [3, 3, 3, 6, 6, 6, 3, 3, 3, 3] if not self.quick else [3, 6, 3], 12.0, jobs=job)
            self.phase("drills", "omni", 8104, [4] * (17 if not self.quick else 9), 10.0, during=drills)
        finally:
            for p in self.agents.values():
                self.stop(p)
            for p in self.procs:
                if p.poll() is None:
                    self.stop(p, signal.SIGKILL)


def drills(show: Show, ctx: dict) -> None:
    d, t0, ev = ctx["dir"], ctx["t0"], []
    ctx["events"] = ev
    q = 0.5 if show.quick else 1.0

    def at(s: float) -> None:
        time.sleep(max(0.0, t0 + s * q - time.time()))

    def mark(kind: str, **kw) -> None:
        ev.append({"t": round(time.time() - t0, 2), "kind": kind, **kw})

    def units_by_machine() -> dict[str, list]:
        out = {}
        for n, _, _ in MACHINES:
            try:
                out[n] = show.agent(n, "/status")["units"]
            except Exception:
                out[n] = []
        return out

    at(15)
    um = units_by_machine()
    victim = next((u for us in um.values() for u in us if u["pid"] and u["kind"] == "service"), None)
    if victim:
        os.kill(victim["pid"], signal.SIGKILL)
        mark("unit killed", unit=victim["id"], pid=victim["pid"])
    at(45)
    um = units_by_machine()
    lost = max(um, key=lambda n: len(um[n]))
    show.stop(show.agents[lost], signal.SIGKILL)
    for pid in Walls(lost).pids():
        try:
            os.kill(pid, signal.SIGKILL)
        except OSError:
            pass
    mark("machine lost", machine=lost, units=[u["id"] for u in um[lost]])
    at(75)
    port, core = next((p, c) for n, p, c in MACHINES if n == lost)
    show.start_agent(lost, port, core)
    mark("machine repaired", machine=lost)
    at(90)
    before = sorted(u["id"] for us in units_by_machine().values() for u in us)
    show.stop(ctx["ctl"], signal.SIGKILL)
    mark("control plane killed", units=before)
    at(110)
    ctx["ctl"] = show.spawn(ctx["ctl_args"], "drills-control.log")
    mark("control plane started again")
    at(122)
    after = sorted(u["id"] for us in units_by_machine().values() for u in us)
    mark("units after the restart", units=after, same=[u for u in after if u in before])
    at(130)
    (d / "KILL").write_text("on")
    mark("kill switch on")
    at(150)
    (d / "KILL").unlink()
    mark("kill switch off")


# ---- reading the files ------------------------------------------------------------------------------------------------
def requests(d: Path) -> list[dict]:
    with open(d / "requests.csv") as f:
        return [{"t": float(r["sent_s"]), "ms": float(r["ms"]), "ok": r["status"] == "200", "right": r["right"] == "1"}
                for r in csv.DictReader(f)]


def jsonl(p: Path) -> list[dict]:
    if not p.exists():
        return []
    out = []
    for line in p.read_text().splitlines():
        try:
            out.append(json.loads(line))
        except ValueError:
            pass
    return out


def pct(xs: list[float], q: float) -> float:
    s = sorted(xs)
    return s[min(len(s) - 1, int(q * len(s)))] if s else float("nan")


def t95(df: int) -> float:
    from omnicompass.student_t import t95 as exact      # the exact Student t quantile every table of the repository uses
    return exact(df)


def summary(d: Path, meta: dict) -> dict:
    rq = requests(d)
    ok = [r["ms"] for r in rq if r["ok"]]
    tl = [r for r in jsonl(d / "ctl" / "timeline.jsonl") if r["t"] >= meta["t_load"]]
    end = meta["t_load"] + len(meta["steps"]) * meta["step_s"]
    tl = [r for r in tl if r["t"] <= end]
    on = lambda r: sum(v for k, v in r["machines"].items() if k in ("awake", "booting", "draining"))
    return {"requests": len(rq), "answered": len(ok), "failed": sum(1 for r in rq if not r["ok"]),
            "wrong": sum(1 for r in rq if r["ok"] and not r["right"]),
            "p50_ms": pct(ok, 0.5), "p95_ms": pct(ok, 0.95), "p99_ms": pct(ok, 0.99),
            "machine_min": sum(on(r) for r in tl) / 60.0, "unit_min": sum(r["units"]["web"] for r in tl) / 60.0,
            "conveyed_core_min": sum(r.get("conveyed_m", 0.0) for r in tl) / 1000.0 / 60.0,
            "depth_max": max([r.get("depth", {}).get("web", 0) for r in tl] or [0]),
            "cpu_s": sum(meta["cpu_s"].values()), "seconds": len(tl)}


def per_step(d: Path, meta: dict) -> dict[str, list[float]]:
    rq = requests(d)
    tl = jsonl(d / "ctl" / "timeline.jsonl")
    out = {"requests": [], "p95_ms": [], "machines": [], "units": []}
    for i in range(len(meta["steps"])):
        a, b = i * meta["step_s"], (i + 1) * meta["step_s"]
        xs = [r for r in rq if a <= r["t"] < b]
        out["requests"].append(float(sum(1 for r in xs if r["ok"])))
        out["p95_ms"].append(pct([r["ms"] for r in xs if r["ok"]], 0.95))
        rows = [r for r in tl if meta["t_load"] + a <= r["t"] < meta["t_load"] + b]
        ms = [sum(v for k, v in r["machines"].items() if k in ("awake", "booting", "draining")) for r in rows]
        out["machines"].append(sum(ms) / len(ms) if ms else float("nan"))
        us = [r["units"]["web"] for r in rows]
        out["units"].append(sum(us) / len(us) if us else float("nan"))
    return out


AIMS = {"requests": "work", "p95_ms": "wait", "machines": "resource", "units": "resource"}


def word(gauge: str, diffs: list[float], base: list[float]) -> dict:
    n = len(diffs)
    m = sum(diffs) / n
    sd = math.sqrt(sum((x - m) ** 2 for x in diffs) / (n - 1)) if n > 1 else 0.0
    half = t95(n - 1) * sd / math.sqrt(n) if n > 1 else float("inf")
    lo, hi = m - half, m + half
    rel = m / (sum(base) / n) if sum(base) else float("nan")
    aim = AIMS[gauge]
    if lo <= 0 <= hi:
        w = "STEADY"
    elif aim == "work":
        w = "GAIN" if lo > 0 else "LOSS"
    elif aim == "wait":
        w = "GAIN" if hi < 0 else "LOSS"
    else:
        w = "GAIN (a cut)" if hi < 0 else "power given"
    return {"mean": m, "lo": lo, "hi": hi, "rel": rel, "word": w}


# ---- the report ---------------------------------------------------------------------------------------------------------
AMBER, BLUE, GREEN, RED, GREY = "#c77d0a", "#2563c9", "#1e8e3e", "#c0392b", "#888888"


def svg_lines(series: list[tuple[str, str, list[tuple[float, float]]]], title: str, ylab: str, w=720, h=220,
              marks: list[tuple[float, str]] | None = None, ymin: float | None = 0.0) -> str:
    pts = [p for _, _, s in series for p in s if p[1] == p[1]]
    if not pts:
        return ""
    x0, x1 = min(p[0] for p in pts), max(p[0] for p in pts)
    y0 = ymin if ymin is not None else min(p[1] for p in pts)
    y1 = max(p[1] for p in pts) * 1.08 or 1.0
    L, R, T, B = 56, 12, 28, 34
    X = lambda x: L + (x - x0) / max(1e-9, x1 - x0) * (w - L - R)
    Y = lambda y: T + (1 - (y - y0) / max(1e-9, y1 - y0)) * (h - T - B)
    o = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{html.escape(title)}" class="chart">',
         f'<text x="{L}" y="16" class="ct">{html.escape(title)}</text>']
    for i in range(5):
        y = y0 + (y1 - y0) * i / 4
        o.append(f'<line x1="{L}" x2="{w - R}" y1="{Y(y):.1f}" y2="{Y(y):.1f}" class="grid"/>'
                 f'<text x="{L - 6}" y="{Y(y) + 4:.1f}" class="ax" text-anchor="end">{y:.0f}</text>')
    for i in range(6):
        x = x0 + (x1 - x0) * i / 5
        o.append(f'<text x="{X(x):.1f}" y="{h - 14}" class="ax" text-anchor="middle">{x:.0f}</text>')
    o.append(f'<text x="{w - R}" y="{h - 2}" class="ax" text-anchor="end">seconds · {html.escape(ylab)}</text>')
    for t, lab in marks or []:
        o.append(f'<line x1="{X(t):.1f}" x2="{X(t):.1f}" y1="{T}" y2="{h - B}" class="mark"/>'
                 f'<text x="{X(t) + 3:.1f}" y="{T + 10}" class="ml">{html.escape(lab)}</text>')
    for k, (name, color, s) in enumerate(series):
        s = [p for p in s if p[1] == p[1]]
        if not s:
            continue
        d = " ".join(f"{'M' if i == 0 else 'L'}{X(x):.1f},{Y(y):.1f}" for i, (x, y) in enumerate(s))
        o.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2"/>')
        o.append(f'<text x="{w - R - 4}" y="{T + 14 + 14 * k}" fill="{color}" class="lg" text-anchor="end">{html.escape(name)}</text>')
    o.append("</svg>")
    return "".join(o)


def windows(rq: list[dict], width: float, end: float) -> list[tuple[float, float]]:
    out = []
    t = 0.0
    while t < end:
        xs = [r["ms"] for r in rq if t <= r["t"] < t + width and r["ok"]]
        out.append((t + width / 2, pct(xs, 0.95) if xs else float("nan")))
        t += width
    return out


def rate(rq: list[dict], width: float, end: float, ok: bool = True) -> list[tuple[float, float]]:
    out = []
    t = 0.0
    while t < end:
        out.append((t + width / 2, sum(1 for r in rq if t <= r["t"] < t + width and r["ok"] == ok) / width))
        t += width
    return out


def line_series(tl: list[dict], t0: float, f) -> list[tuple[float, float]]:
    return [(r["t"] - t0, f(r)) for r in tl if r["t"] >= t0]


def build_report(out: Path) -> Path:
    metas = {m["phase"]: m for m in (json.loads((out / p / "meta.json").read_text()) for p in
                                     ("yardstick", "omni_native", "omni", "batch", "drills") if (out / p / "meta.json").exists())}
    S = {p: summary(out / p, m) for p, m in metas.items()}
    on = lambda r: sum(v for k, v in r["machines"].items() if k in ("awake", "booting", "draining"))
    y, o, on_ = metas.get("yardstick"), metas.get("omni"), metas.get("omni_native")
    # the three arms (the founder's order of 23 October): native (Kubernetes' rule on the machines), Omni on native (Omni on
    # top of that rule) and Omni direct (Omni alone on the machines); every pair of them read by the one key, paired by step
    ARMS = {"yardstick": "native", "omni_native": "Omni on native", "omni": "Omni direct"}
    COMPARISONS = [("omni_native", "yardstick"), ("omni", "yardstick"), ("omni", "omni_native")]
    steps_of = {p: per_step(out / p, metas[p]) for p in ARMS if p in metas}
    readings = {}
    for a, b in COMPARISONS:
        if a in steps_of and b in steps_of:
            for g in ("requests", "p95_ms", "machines", "units"):
                pairs = [(x, z) for x, z in zip(steps_of[a][g], steps_of[b][g]) if x == x and z == z]
                if pairs:
                    readings[f"{ARMS[a]} against {ARMS[b]}: {g}"] = word(g, [x - z for x, z in pairs], [z for _, z in pairs])
    arms = [p for p in ARMS if p in metas]
    rows = []
    if len(arms) >= 2:
        rel = lambda a, b: f"{100 * (a - b) / b:+.1f}%" if b else "—"
        for label, key, fmt in (("requests answered (work)", "answered", "{:,.0f}"), ("requests failed", "failed", "{:,.0f}"),
                                ("answers wrong", "wrong", "{:,.0f}"), ("response time, 50th percentile (ms)", "p50_ms", "{:,.0f}"),
                                ("response time, 95th percentile (ms)", "p95_ms", "{:,.0f}"),
                                ("response time, 99th percentile (ms)", "p99_ms", "{:,.0f}"),
                                ("machine-minutes on (the bill)", "machine_min", "{:,.1f}"),
                                ("unit-minutes", "unit_min", "{:,.1f}"), ("processor-seconds used by the units", "cpu_s", "{:,.0f}"),
                                ("processor conveyed above the requests (core-minutes)", "conveyed_core_min", "{:,.2f}"),
                                ("units below the twin the verdict allowed, at most", "depth_max", "{:,.0f}")):
            base = S[arms[0]][key]
            rows.append((label, *[fmt.format(S[p][key]) for p in arms], *[rel(S[p][key], base) for p in arms[1:]]))
    css = """
:root{--bg:#ffffff;--fg:#1d2330;--muted:#5b6475;--line:#e3e6ec;--card:#f6f7f9}
@media (prefers-color-scheme: dark){:root{--bg:#12151b;--fg:#e8ebf0;--muted:#a0a8b8;--line:#2a2f3a;--card:#1a1e26}}
body{background:var(--bg);color:var(--fg);font:16px/1.55 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;margin:0;padding:0 16px}
main{max-width:860px;margin:0 auto;padding:12px 0 40px}
h1{font-size:1.5rem;margin:.6em 0 .2em}h2{font-size:1.2rem;margin:1.6em 0 .4em}
.legal{font-size:.78rem;color:var(--muted);border:1px solid var(--line);padding:8px 10px;border-radius:6px}
table{border-collapse:collapse;width:100%;font-size:.92rem;margin:.4em 0}
td,th{border-bottom:1px solid var(--line);padding:6px 6px;text-align:left;vertical-align:top}
th{color:var(--muted);font-weight:600}
.num{text-align:right;font-variant-numeric:tabular-nums}
.card{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px 12px;margin:10px 0}
.chart{width:100%;height:auto;background:var(--card);border:1px solid var(--line);border-radius:8px;margin:8px 0}
.chart .ct{font-size:13px;font-weight:600;fill:var(--fg)}.chart .ax{font-size:11px;fill:var(--muted)}
.chart .lg{font-size:12px;font-weight:600}.chart .grid{stroke:var(--line)}.chart .mark{stroke:#c0392b;stroke-dasharray:3 3}
.chart .ml{font-size:10px;fill:#c0392b}
.GAIN{color:#1e8e3e;font-weight:700}.STEADY{color:#b08900;font-weight:700}.LOSS{color:#c0392b;font-weight:700}
.given{color:#2563c9;font-weight:700}
code{font-size:.88em}
"""
    H = [f"<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
         f"<title>Omni Orchestrator Showing</title><style>{css}</style></head><body><main>",
         f"<p class='legal'>{html.escape(TOP)}</p>",
         "<h1>Omni-Compass's own orchestrator: the first showing</h1>",
         "<p>Built from scratch on 23 October 2026: Python's standard library and Omni-Compass's own compass law, no code of "
         "Kubernetes or any other orchestrator. Run on this one machine, every piece a real process, every answer checked. "
         "Local only, not pushed. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or "
         "approved these results.</p>"]
    cal = json.loads((out / "calibration.json").read_text()) if (out / "calibration.json").exists() else {}
    H.append("<div class='card'><b>The rig.</b> Six machines of half a processor each, walled by the kernel's own CPU quotas "
             "(two machines on each of three cores); the control plane, the front, the six machines' hands and the clients "
             "on the fourth core. The service's units: 250 millicores each (request and limit on the yardstick, as "
             "Kubernetes holds them; on Omni the wall is conveyed to the room the machine can spare). Each request: a chain of "
             f"{cal.get('k_40ms', '?'):,} SHA-256 hashes (about 40 ms of processor), its digest checked by the client. "
             "The clients: closed loop, 0.1 s of thought between requests, stepping by one.</div>")
    if rows:
        H.append("<h2>1. Native, Omni on native and Omni direct, the same clients</h2>")
        H.append("<p><b>Native</b> (the yardstick): Kubernetes' published autoscaling rule on the machines (every 15 s; 50% of "
                 "the request; 10% tolerance; a fall only to the highest count of the last 300 s), the units spread as "
                 "Kubernetes' scheduler spreads them, all six machines on, as a fixed cluster runs; written by us from its "
                 "documentation as the measure, it is not Kubernetes itself. <b>Omni on native:</b> Omni-Compass on top of "
                 "that rule, the engine's strict form as on the kind rigs: the units are the rule's, never fewer; Omni adds a "
                 "unit the beat work waits in line and past the wall, conveys each unit's CPU wall to the room its machine can "
                 "spare under 75% (the engine's rule: a unit answers at its machine's speed, not its paper quota's), places by "
                 "the busy rule, packs, parks and wakes machines. <b>Omni direct:</b> Omni-Compass alone on the machines, no "
                 "Kubernetes: every 5 s the reflex, the compass law on the 95th percentile, the yardstick twin (what "
                 "Kubernetes would hold for this work) less the depth the verdict has allowed on the service's own response "
                 "times (a unit fewer tried under the same traffic, kept only where the response time reads no LOSS within "
                 "2%), conveyance, packing, machines parked and woken (two at least; a parked machine takes 10 s to come back).</p>")
        heads = "".join(f"<th class='num'>{ARMS[p]}</th>" for p in arms) + "".join(f"<th class='num'>{ARMS[p]} against native</th>" for p in arms[1:])
        H.append(f"<table><tr><th>gauge</th>{heads}</tr>")
        for r in rows:
            H.append(f"<tr><td>{html.escape(r[0])}</td>" + "".join(f"<td class='num'>{c}</td>" for c in r[1:]) + "</tr>")
        H.append("</table>")
        if readings:
            H.append("<p><b>Read by the one key</b>, step by step (each step of the clients a pair, its 95% interval on "
                     f"{len(y['steps'])} pairs; one run of each arm, not yet the three-run reading):</p><table>"
                     "<tr><th>comparison and gauge</th><th class='num'>difference, mean a step</th><th class='num'>95% interval</th><th>reading</th></tr>")
            names = {"requests": "requests answered a step", "p95_ms": "95th percentile a step (ms)",
                     "machines": "machines on, mean a step", "units": "units standing, mean a step"}
            for key, r in readings.items():
                cmp_, g = key.rsplit(": ", 1)
                cls = "GAIN" if r["word"].startswith("GAIN") else "STEADY" if r["word"] == "STEADY" else "LOSS" if r["word"] == "LOSS" else "given"
                H.append(f"<tr><td>{html.escape(cmp_)}: {names[g]}</td><td class='num'>{r['mean']:+.1f} ({100 * r['rel']:+.1f}%)</td>"
                         f"<td class='num'>{r['lo']:+.1f} to {r['hi']:+.1f}</td><td class='{cls}'>{r['word']}</td></tr>")
            H.append("</table>")
        colours = {"yardstick": AMBER, "omni_native": GREEN, "omni": BLUE}
        end = len(y["steps"]) * y["step_s"]
        H.append(svg_lines([(ARMS[p], colours[p], windows(requests(out / p), 10, end)) for p in arms],
                           "95th percentile response time, 10 s windows", "ms"))
        tls = {p: jsonl(out / p / "ctl" / "timeline.jsonl") for p in arms}
        H.append(svg_lines([(ARMS[p], colours[p], line_series(tls[p], metas[p]["t_load"], lambda r: r["units"]["web"])) for p in arms],
                           "units of the service", "units"))
        H.append(svg_lines([(ARMS[p], colours[p], line_series(tls[p], metas[p]["t_load"], on)) for p in arms], "machines on", "machines"))
        H.append(svg_lines([("clients", GREY, [(i * y["step_s"] + d, c) for i, c in enumerate(y["steps"]) for d in (0, y["step_s"])])],
                           "the clients (the same in every arm)", "clients"))
    if "batch" in metas:
        b = metas["batch"]
        tl = jsonl(out / "batch" / "ctl" / "timeline.jsonl")
        au = jsonl(out / "batch" / "ctl" / "audit.jsonl")
        done = max((r["tasks_done"].get("crunch", 0) for r in tl), default=0)
        yields = sum(1 for a in au if a["kind"] == "unit retiring" and "yields" in a.get("why", ""))
        files = list((out / "batch" / "results").glob("crunch-*.json"))
        H.append("<h2>2. One body: a batch job beside the service</h2>")
        H.append(f"<p>A job of 16 tasks (about 2 s of processor each, 250 millicores each, four at a time) ran in the room "
                 f"the service left; the clients went from 3 to 6 midway. Tasks finished: <b>{done} of 16</b>; result files "
                 f"written: {len(files)}; tasks that gave their room to the service and went back in the queue: {yields}. "
                 f"Service in the same minutes: {S['batch']['answered']:,} requests answered, {S['batch']['failed']} failed, "
                 f"{S['batch']['wrong']} wrong, 95th percentile {S['batch']['p95_ms']:.0f} ms.</p>")
        H.append(svg_lines([("units of the service", BLUE, line_series(tl, b["t_load"], lambda r: r["units"]["web"])),
                            ("batch tasks running", AMBER, line_series(tl, b["t_load"], lambda r: r["tasks_running"])),
                            ("machines on", GREY, line_series(tl, b["t_load"], on))], "the service and the batch, one body", "count"))
    if "drills" in metas:
        dm = metas["drills"]
        rq = requests(out / "drills")
        tl = jsonl(out / "drills" / "ctl" / "timeline.jsonl")
        end = len(dm["steps"]) * dm["step_s"]
        ev = dm.get("events", [])
        H.append("<h2>3. The drills, with the clients running through all of them</h2><table>"
                 "<tr><th>at (s)</th><th>what was done</th><th>what followed</th></tr>")
        for e in ev:
            t = e["t"]
            win = [r for r in rq if t <= r["t"] < t + 20]
            fails = sum(1 for r in win if not r["ok"])
            note = f"next 20 s: {len(win)} requests, {fails} failed"
            if e["kind"] == "unit killed":
                note += "; the machine's hand started it again"
            if e["kind"] == "machine lost":
                note += f"; its {len(e.get('units', []))} units were placed again elsewhere"
            if e["kind"] == "units after the restart":
                note = f"{len(e['same'])} of {len(e['units'])} units the same as before the kill: none started again" \
                    if len(e["same"]) == len(e["units"]) else f"{len(e['same'])} of {len(e['units'])} units kept"
            if e["kind"] == "control plane killed":
                out_win = [r for r in rq if t <= r["t"] < t + 20]
                note = f"while it was down (20 s): {sum(1 for r in out_win if r['ok'])} requests answered, " \
                       f"{sum(1 for r in out_win if not r['ok'])} failed"
            H.append(f"<tr><td class='num'>{t:.0f}</td><td>{html.escape(e['kind'])}"
                     f"{(' (' + html.escape(str(e.get('unit') or e.get('machine'))) + ')') if (e.get('unit') or e.get('machine')) else ''}</td>"
                     f"<td>{html.escape(note)}</td></tr>")
        H.append("</table>")
        sd = S["drills"]
        H.append(f"<p>All drills together: {sd['requests']:,} requests, {sd['answered']:,} answered, <b>{sd['failed']} failed</b>, "
                 f"{sd['wrong']} wrong.</p>")
        short = {"unit killed": "unit killed", "machine lost": "machine lost", "machine repaired": "repaired",
                 "control plane killed": "control plane killed", "control plane started again": "restarted",
                 "kill switch on": "kill switch on", "kill switch off": "off"}
        marks = [(e["t"], short[e["kind"]]) for e in ev if e["kind"] in short]
        H.append(svg_lines([("answered a second", BLUE, rate(rq, 2, end)), ("failed a second", RED, rate(rq, 2, end, ok=False))],
                           "requests through the drills, 2 s windows", "per second", marks=marks))
        H.append(svg_lines([("units ready", BLUE, line_series(tl, dm["t_load"], lambda r: r["ready"]["web"])),
                            ("machines on", GREY, line_series(tl, dm["t_load"], on))], "units ready and machines on", "count", marks=marks))
    au = jsonl(out / "omni" / "ctl" / "audit.jsonl")
    if au:
        H.append("<h2>4. What Omni's brain decided, in its own words (the first 14 lines of the arm)</h2><table>"
                 "<tr><th>s</th><th>decision</th><th>why</th></tr>")
        t0 = metas["omni"]["t_load"]
        picked = [a for a in au if a["kind"] in ("units", "machine woken", "machine draining", "machine parked",
                                                 "limit conveyed", "limit handed back", "verdict")][:14]
        for a in picked:
            why = a.get("why")
            why = (f"force {why.get('force')}, p95 {why.get('p95_ms')} ms, twin {why.get('twin')}, floor {why.get('floor')} "
                   f"(depth {why.get('depth')}), busy {why.get('busy')}, waiting {why.get('waiting')}"
                   if isinstance(why, dict) else why)
            if a["kind"] == "units":
                what = f"units {a.get('was')} → {a.get('now')}"
            elif a["kind"] in ("limit conveyed", "limit handed back"):
                what = f"{a['kind']}: {a.get('unit')} {a.get('was'):.0f} → {a.get('now'):.0f} m"
            elif a["kind"] == "verdict":
                what, why = f"verdict: {a.get('verdict')}", f"step {a.get('step')}" + (f", {a.get('reading')}" if a.get("reading") else "")
            else:
                what = f"{a['kind']} {a.get('machine', '')}"
            H.append(f"<tr><td class='num'>{a['t'] - t0:.0f}</td><td>{html.escape(what)}</td><td>{html.escape(str(why))}</td></tr>")
        H.append("</table>")
    H.append("<h2>5. What it covers, and what it does not yet</h2><table><tr><th>what an orchestrator does</th><th>Omni's own piece</th><th>shown here</th></tr>")
    for a, b, c in (("keep the desired state, survive its own crash", "the ledger, journaled and replayed (control.py)", "yes: killed and started again, units kept"),
                    ("place work on machines", "the room rule, packed or spread (scheduler.py)", "yes"),
                    ("start, watch, restart, stop a unit", "the machine's hand (agent.py)", "yes: a unit killed and started again"),
                    ("health checks", "the hand's probe, three misses and it is restarted", "yes"),
                    ("isolation of processor and memory", "the kernel's control groups (cgroup.py)", "yes: CPU walls for every machine and unit"),
                    ("one address for a service, spread the load", "the front (front.py)", "yes"),
                    ("scale units with the load", "the reflex on work in line, the compass law, the yardstick twin less the verdict's depth (brain.py)", "yes"),
                    ("give a unit the processor its machine can spare", "conveyance, the engine's own rule (brain.py, control.py, the hand's wall)", "yes"),
                    ("scale machines", "wake before a unit waits, park after the load holds low", "yes"),
                    ("batch jobs and a queue", "tasks in the room the service leaves, yielding to it", "yes"),
                    ("a machine lost", "silent three times: its units placed again", "yes"),
                    ("a kill switch", "a file: the brain off, the declared state held", "yes"),
                    ("an audit of every decision", "audit.jsonl, one line each, with its reason", "yes"),
                    ("many hosts over a network", "the hands already answer over HTTP", "not yet: one host here"),
                    ("container images, a registry", "—", "not yet: units are processes"),
                    ("network isolation, service names, encryption", "—", "not yet"),
                    ("storage that follows a unit", "—", "not yet"),
                    ("rolling updates of a new version", "—", "not yet"),
                    ("secrets, users and permissions", "—", "not yet"),
                    ("the comparison against Kubernetes itself", "the kind rig on GitHub", "not yet: waits for your word to push")):
        H.append(f"<tr><td>{html.escape(a)}</td><td>{html.escape(b)}</td><td>{html.escape(c)}</td></tr>")
    H.append("</table>")
    H.append("<p>Every number above comes from the files of this showing: each request's record, the control plane's "
             "timeline and audit, the kernel's own processor counters. One run of each arm on one host: what it shows is "
             "that the mechanism works end to end and how it behaved here, not yet a three-run reading. Evidence class L "
             "(live software).</p>")
    H.append(f"<p class='legal'>{html.escape(TOP)}</p></main></body></html>")
    p = out / "report.html"
    p.write_text("\n".join(H), encoding="utf-8")
    (out / "summary.json").write_text(json.dumps({"summary": S, "readings": readings}, indent=1, default=str))
    return p


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--out", required=False)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--report", help="rebuild the report of a finished showing")
    ap.add_argument("--room-rule", choices=("requests", "busy"), default="busy",
                    help="Omni's room rule: the engine's own, under 75%% of a machine's measured busy share (busy), or by requests alone")
    a = ap.parse_args(argv)
    if a.report:
        print(build_report(Path(a.report)))
        return
    out = Path(a.out)
    Show(out, a.quick, a.room_rule).run()
    print(build_report(out))


if __name__ == "__main__":
    main()

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
