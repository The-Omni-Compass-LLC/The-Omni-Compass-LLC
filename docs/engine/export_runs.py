# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The official runs, as recorded, for the live benchmark engine page (docs/engine/OMNI_COMPASS_LIVE_ENGINE.html): every three-run
table's runs A, B and C read back from their own raw files in results/live/raw, every file's SHA-256 computed and matched
against the run's own SHA256SUMS_ALL.txt, so what the page plays is the run itself and anyone can check it.

  Kubernetes (class L)  every paired repetition, native and Omni-Compass on top: each request's response time
                        (latency.csv, in 30-second windows: mean, 95th percentile, requests, failures), the cluster every
                        16 seconds (capture.csv: replicas, pods waiting for a place, nodes, processor used, the declared
                        power model), the host's processor (host_cpu.csv), the load generator's steps
                        (load_schedule.log), and Omni-Compass's own audit of every decision (audit.jsonl: the compass's
                        position and force, the writes)
  the databases (class L) every repetition of every workload, both arms: the arm's own result (arm.json)

Each benchmark's newest engine's table names its runs (results/live/V<n>_*.json). Raw files are read from the checkout
where present, else from git: main's tree while it carried them, else the branch raw (scripts/raw_archive.sh). Usage:
python3 docs/engine/export_runs.py OUT.json
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import statistics
import math
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(Path(__file__).resolve().parent))
RAW = "results/live/raw"
BIN = 30                     # seconds in a response-time window
NOISE_N = 200   # requests in the verdict's own window (omni_controller/controller.py --verdict-samples 200)
# The tables played back are found by export_scenarios.tables(): every newest three-run table of real Kubernetes (its JSON
# holds its rows) and of the Linux services (its JSON holds its workloads). One run of KEDA's add-ons holds both native setups,
# each in its own sub-folder (.github/workflows/kind-addons.yml): the HTTP add-on in http/, the CPU target with the requests in
# flight in both/; every other run holds its arms at its own root.
ADDON_SETUP = {"KEDA_REQUESTS": "http/", "KEDA_CPU_REQUESTS": "both/"}
# the four ways (docs/BATCH_QUEUE_PREREGISTRATION.md, amendment 6): each table's own two arms, (its reference, its candidate), so a
# table's replay plays the arms the table compares and never another table's of the same run
FOUR_WAYS = {"TOP": ("native", "compass"), "ORCH": ("nativebare", "native"), "BARE": ("nativebare", "compassbare"),
             "VS": ("native", "compassbare"), "BOTH": ("nativebare", "compass")}
DB_GAUGES = ["work_inside_line_rps", "rps", "p95_ms", "p99_ms", "mean_ms", "failed", "hit_rate", "cpu_busy_share", "writes"]


def raw_ref():
    """Where the raw files are read from when not checked out: main's own tree while it carried them, else the branch raw
    (fetched by scripts/raw_archive.sh fetch), whose root is what results/live/raw/ held: (ref, prefix inside that ref)."""
    def has(spec):
        return subprocess.run(["git", "-C", str(ROOT), "cat-file", "-e", spec], capture_output=True).returncode == 0
    if has(f"HEAD:{RAW}"):
        return "HEAD", RAW + "/"
    for ref in ("refs/remotes/origin/raw", "refs/heads/raw"):
        if has(ref):
            return ref, ""
    return "HEAD", RAW + "/"


class Git:
    """Raw files by path: from the working tree where checked out, else from git (main's tree or the branch raw) through
    one git cat-file process."""
    def __init__(self):
        self.p = subprocess.Popen(["git", "-C", str(ROOT), "cat-file", "--batch"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        self.tree = None
        self.ref, self.inside = raw_ref()

    def spec(self, path: str) -> str:
        return f"{self.ref}:{self.inside}{path[len(RAW) + 1:]}" if path.startswith(RAW + "/") else f"HEAD:{path}"

    def read(self, path: str):
        f = ROOT / path
        if f.is_file():
            return f.read_bytes()
        self.p.stdin.write(f"{self.spec(path)}\n".encode()); self.p.stdin.flush()
        head = self.p.stdout.readline().decode().split()
        if len(head) < 3 or head[1] == "missing":
            return None
        data = self.p.stdout.read(int(head[2])); self.p.stdout.read(1)
        return data

    def files(self, prefix: str) -> list:
        if self.tree is None:
            args = [self.ref, RAW + "/"] if self.inside else [self.ref]
            out = subprocess.run(["git", "-C", str(ROOT), "ls-tree", "-r", "--name-only", *args],
                                 capture_output=True, text=True).stdout.split("\n")
            self.tree = [x if self.inside else f"{RAW}/{x}" for x in out if x]
        return [x for x in self.tree if x.startswith(prefix)]


def run_dir(g: Git, run_id: str, pairs=None):
    """The run's own folder. A run re-run in part can sit twice on the branch raw (the first attempt, and the re-run the
    sweep kept under a suffixed name): the folder whose own LIVE_REPS.json holds the table's count of paired repetitions
    is taken, else the one the branch received last; never one picked by the order of a set."""
    found = sorted({"/".join(x.split("/")[:4]) for x in g.files(RAW + "/") if run_id in x.split("/")[3]})
    if len(found) <= 1:
        return found[0] if found else None

    def held(d):                     # the paired repetitions the folder's own LIVE_REPS.json counts
        n = 0
        for x in g.files(d + "/"):
            if x.endswith("LIVE_REPS.json"):
                try:
                    lr = json.loads((g.read(x) or b"{}").decode("utf-8").replace("NaN", "null"))
                except (UnicodeDecodeError, json.JSONDecodeError):
                    continue
                reps = lr.get("repetitions") or {}
                n = max(n, min(len(reps.get("native") or []), len(reps.get("compass") or reps.get("omni") or [])))
        return n

    def received(d):                 # when the branch received the folder (its newest commit there)
        spec = f"{g.inside}{d[len(RAW) + 1:]}" if g.inside else d[len(RAW) + 1:]
        out = subprocess.run(["git", "-C", str(ROOT), "log", "-1", "--format=%ct", g.ref, "--", spec],
                             capture_output=True, text=True).stdout.strip()
        return int(out) if out.isdigit() else 0

    if pairs:
        match = [d for d in found if held(d) == int(pairs)]
        if len(match) == 1:
            return match[0]
        found = match or found
    return max(found, key=lambda d: (received(d), d))


class Sums:
    """A run's own SHA256SUMS_ALL.txt, and every file read checked against it."""
    def __init__(self, g: Git, d: str):
        self.g, self.d, self.checked, self.ok, self.missing, self.stale = g, d, 0, 0, [], set()
        raw = g.read(f"{d}/SHA256SUMS_ALL.txt") or b""
        self.sha_of_list = hashlib.sha256(raw).hexdigest() if raw else None
        self.table = {}
        for ln in raw.decode("utf-8", "replace").splitlines():
            parts = ln.split(None, 1)
            if len(parts) == 2:
                self.table[parts[1].strip().lstrip("./")] = parts[0]

    def listed(self, rel: str) -> bool:
        """Whether the run's own SHA256SUMS_ALL.txt names the file (one it does not name is not the run's: a marker an
        earlier attempt left, say, which a re-run's commit did not remove)."""
        return rel in self.table

    def read(self, rel: str):
        data = self.g.read(f"{self.d}/{rel}")
        if data is None:
            return None
        self.checked += 1
        if self.table.get(rel) == hashlib.sha256(data).hexdigest():
            self.ok += 1
        else:
            self.missing.append(rel)
        return data


def serial(r):
    """The run's whole serial number: the full commit it ran (git), and the full SHA-256 fingerprint of the engine that
    commit carries (OMNI_V<n>.json), so anyone can rerun the same engine on the same commit and check every file."""
    out = {}
    c = str(r.get("commit") or "")
    if re.fullmatch(r"[0-9a-f]{7,40}", c):
        try:
            full = subprocess.run(["git", "rev-parse", "--verify", "--quiet", c + "^{commit}"], cwd=ROOT, capture_output=True, text=True, timeout=30).stdout.strip()
            if re.fullmatch(r"[0-9a-f]{40}", full):
                out["commit_full"] = full
        except (OSError, subprocess.SubprocessError):
            pass                                          # no git here: the short commit the table names stands alone
    m = re.match(r"omni-v(\d+)", str(r.get("engine") or ""))
    f = ROOT / f"OMNI_V{m.group(1)}.json" if m else None
    if f and f.exists():
        out["engine_digest_full"] = json.loads(f.read_text(encoding="utf-8")).get("digest")
    return out


HIST_MS = [50, 100, 200, 300, 500, 1000, 2000]                     # the heatmap's bucket edges (ms); 500 ms is the line


def pct(xs, q):
    if not xs:
        return None
    s = sorted(xs)
    return s[min(len(s) - 1, int(q * len(s)))]


OFFICIAL = ["response time (ms), mean", "response time (ms), 95th percentile", "response time (ms), 99th percentile",
            "time over the response line (% of samples)", "failed requests (%)",
            "alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line)",
            "HPA replicas, mean", "pods started", "worker nodes in service, mean", "node-hours", "energy (Wh)",
            "host CPU busy, the real machine under kind (%)",
            "settings commands the governor wrote on its own (no person touched either arm)"]


def official(s: Sums, rel: str, slo: float) -> dict:
    """The repository's own scorer (tools/live_reps.py arm_gauges) on this repetition's own files, as the three-run
    table's run was scored: every file of the folder laid out as the run wrote it, each SHA-256-checked as it is read."""
    import os
    import tempfile
    from tools import live_reps as LR
    with tempfile.TemporaryDirectory() as td:
        d = Path(td) / rel.rsplit("/", 1)[-1]
        d.mkdir(parents=True)
        for x in s.g.files(f"{s.d}/{rel}/"):
            if s.table and not s.listed(x[len(s.d) + 1:]):
                s.stale.add(x[len(s.d) + 1:])                           # not the run's own file: left out, and said
                continue
            data = s.read(x[len(s.d) + 1:])
            if data is not None:   # every file at its own place in the folder: a group's member clusters (m1/, m2/) never overwrite the group's own files
                f = d / x[len(s.d) + len(rel) + 2:]
                f.parent.mkdir(parents=True, exist_ok=True)
                f.write_bytes(data)
        old = os.environ.get("SLO_MS"); os.environ["SLO_MS"] = str(slo)
        try:
            import contextlib, io as _io
            with contextlib.redirect_stdout(_io.StringIO()):
                g = LR.arm_gauges(d)
        except Exception as e:                                      # a folder the scorer cannot read: said, never guessed
            return {"error": f"{type(e).__name__}: {e}"[:200]}
        finally:
            if old is None:
                os.environ.pop("SLO_MS", None)
            else:
                os.environ["SLO_MS"] = old
    return {k: (None if (isinstance(g.get(k), float) and math.isnan(g[k])) else g.get(k)) for k in OFFICIAL}


def arm_k8s(s: Sums, rel: str, omni: bool, slo: float = 500.0) -> dict:
    out = {"official": official(s, rel, slo)}
    lat = s.read(f"{rel}/latency.csv")
    if lat:
        rows = list(csv.DictReader(io.StringIO(lat.decode("utf-8", "replace"))))
        bins, allv, fails = {}, [], 0
        for r in rows:
            try:
                t, ms, ok = float(r["elapsed_seconds"]), float(r["latency_ms"]), r.get("ok", "1") == "1"
            except (KeyError, ValueError):
                continue
            b = bins.setdefault(int(t // BIN), [[], 0, []])
            b[0].append(ms); b[2].append((t, ms)); allv.append(ms)
            if not ok:
                b[1] += 1; fails += 1
        last = max(bins) if bins else -1
        # each half minute: mean, 95th percentile, requests, failed; then the candle (the first, highest, lowest and last
        # response of the window, in the order they were answered), the median, the 99th percentile, and the window's
        # responses counted in the buckets of HIST_MS (for the heatmap)
        def window(v, tv):
            tv = sorted(tv)
            return [round(sum(v) / len(v), 1), round(pct(v, 0.95), 1), len(v), None,
                    round(tv[0][1], 1), round(max(v), 1), round(min(v), 1), round(tv[-1][1], 1),
                    round(pct(v, 0.5), 1), round(pct(v, 0.99), 1), [sum(1 for x in v if lo <= x < hi) for lo, hi in zip([0] + HIST_MS, HIST_MS + [math.inf])]]
        out["lat"] = []
        for k in range(last + 1):
            if k in bins and bins[k][0]:
                row = window(bins[k][0], bins[k][2]); row[3] = bins[k][1]
            else:
                row = [None, None, 0, 0]
            out["lat"].append(row)
        out["sum"] = {"requests": len(allv), "failed": fails, "mean_ms": round(sum(allv) / len(allv), 2) if allv else None,
                      "p95_ms": round(pct(allv, 0.95), 1) if allv else None, "p99_ms": round(pct(allv, 0.99), 1) if allv else None}
        # the noise a give-back trial meets on this arm: every run of NOISE_N requests in the order they were sent, the standard
        # deviation of the log of their response times (the verdict's own window: omni_controller --verdict-samples 200);
        # gathered over the table's runs by main() into its median, never written into the page per arm
        seq = [ms for _, ms in sorted(tv for b in bins.values() for tv in b[2]) if ms > 0]
        out["_noise"] = [statistics.stdev(math.log(x) for x in seq[i:i + NOISE_N]) for i in range(0, len(seq) - NOISE_N + 1, NOISE_N)]
    cap = s.read(f"{rel}/capture.csv")
    if cap:
        rows = list(csv.DictReader(io.StringIO(cap.decode("utf-8", "replace"))))
        def f(r, k):
            try:
                return float(r.get(k) or "nan")
            except ValueError:
                return float("nan")
        out["cap"] = [[int(f(r, "elapsed_seconds")), f(r, "hpa_current_replicas"), f(r, "pods_pending"), f(r, "nodes_ready"),
                       f(r, "used_cpu_m"), f(r, "power_w")] for r in rows[::2]]
        out["cap"] = [[None if isinstance(v, float) and math.isnan(v) else v for v in row] for row in out["cap"]]
    host = s.read(f"{rel}/host_cpu.csv")
    if host:
        rows = list(csv.DictReader(io.StringIO(host.decode("utf-8", "replace"))))
        try:
            t0 = float(rows[0]["epoch_s"]); hb = {}
            for r in rows:
                hb.setdefault(int((float(r["epoch_s"]) - t0) // BIN), []).append(float(r["busy"]))
            out["host"] = [round(sum(hb[k]) / len(hb[k]), 3) if k in hb else None for k in range(max(hb) + 1)]
        except (IndexError, KeyError, ValueError):
            pass
    load = s.read(f"{rel}/load_schedule.log")
    if load:
        steps, t0 = [], None
        for ln in load.decode("utf-8", "replace").splitlines():
            m = re.match(r"(\d\d):(\d\d):(\d\d) .*-> *(\d+)", ln)
            if m:
                sec = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))
                t0 = sec if t0 is None else t0
                steps.append([(sec - t0) % 86400, int(m.group(4))])
        out["load"] = steps
    if omni:
        aud = s.read(f"{rel}/audit.jsonl")
        if aud:
            dec, writes, t0, beats, cores = [], 0, None, [], None
            for ln in aud.decode("utf-8", "replace").splitlines():
                try:
                    a = json.loads(ln)
                except json.JSONDecodeError:
                    continue
                if not isinstance(a, dict):
                    continue
                t0 = a.get("time", t0) if t0 is None else t0
                if "write" in a or "writes" in a:
                    writes += 1
                if isinstance(a.get("decision_ms"), (int, float)) and isinstance(a.get("time"), (int, float)):
                    beats.append([a["time"], a["decision_ms"]])          # the heart: one beat per decision, its own time
                if isinstance(a.get("overhead"), dict) and isinstance(a["overhead"].get("cores_mean"), (int, float)):
                    cores = a["overhead"]["cores_mean"]
                d = a.get("decision") if isinstance(a, dict) else None
                if isinstance(d, dict):
                    law = d.get("compass_law") if isinstance(d.get("compass_law"), dict) else {}
                    dec.append([round(a.get("time", t0) - t0, 1), law.get("position"), law.get("force"), d.get("nodes_recommended"),
                                law.get("verdict_state")])
            step = max(1, len(dec) // 150)
            out["dec"], out["writes"] = dec[::step], writes
            if beats and t0 is not None:
                bs = max(1, len(beats) // 400)
                out["beats"] = [[round(t - t0, 1), round(ms, 1)] for t, ms in beats][::bs]
                out["beats_n"], out["heart_cores"] = len(beats), cores
    return out


def k8s_run(g: Git, run: dict, sub: str, pair: tuple = ("native", "compass")):
    d = run_dir(g, str(run["run"]), run.get("paired_repetitions"))
    if not d:
        return None
    s = Sums(g, d)
    arms = sorted({x[len(d) + 1:].rsplit("/", 1)[0] for x in g.files(f"{d}/{sub}") if x.endswith("/latency.csv")})
    if not arms and sub:   # the kind runs from omni-v11 on keep each add-on's arms in <name>-<add-on>-<n>/ folders, not in <add-on>/
        stem = sub.strip("/")
        arms = sorted({x[len(d) + 1:].rsplit("/", 1)[0] for x in g.files(d + "/") if x.endswith("/latency.csv")
                       and re.match(rf"([^/]*-)?{re.escape(stem)}-\d+/", x[len(d) + 1:])})
    reps = {}
    for rel in arms:
        m = re.search(r"bench-(nativebare|compassbare|native|compass)-(\d+)$", rel)
        if not m or m.group(1) not in pair or s.listed(f"{rel}/INVALID"):   # a repetition the run itself marked invalid is left out, as live_reps does
            continue
        group = rel[:m.start()].strip("/")
        reps.setdefault((group, int(m.group(2))), {})["native" if m.group(1) == pair[0] else "omni"] = rel
    out = []
    for (group, n), pr in sorted(reps.items()):
        if "native" in pr and "omni" in pr:
            out.append({"group": group, "n": n, "native": arm_k8s(s, pr["native"], pair[0].startswith("compass")),
                        "omni": arm_k8s(s, pr["omni"], pair[1].startswith("compass"))})
    # the run's own scored result, and the page's per-repetition scoring checked against it: the mean over repetitions of
    # the scorer's gauges must equal the run's LIVE_REPS.json means (the table's own numbers)
    lr = None
    # the run's own scored summary: beside its arms, at the run's root, in live-reps/, or (the kind runs from omni-v11 on) in
    # the run's own <benchmark>-reps/ folder; one sub-folder's summary is preferred for a run whose arms sit in that sub-folder
    stem = sub.strip("/")
    found = sorted(k for k in s.table if k.endswith("LIVE_REPS.json"))
    own = [k for k in found if re.search(rf"(^|[/-]){re.escape(stem)}(/|-|$)", k.rsplit("/", 1)[0])] if stem else found
    for cand in [f"{sub}LIVE_REPS.json", "LIVE_REPS.json", "live-reps/LIVE_REPS.json"] + own:
        if cand in s.table:
            raw = s.read(cand)
            lr = json.loads(raw.decode("utf-8").replace("NaN", "null")) if raw else None
            break
    agree = None
    if lr and out:
        worst = 0.0
        for arm, key in (("native", pair[0]), ("omni", pair[1])):
            for k in OFFICIAL:
                vals = [r[arm]["official"].get(k) for r in out if isinstance(r[arm]["official"].get(k), (int, float))]
                ref = (lr.get("means", {}).get(key) or {}).get(k)
                if vals and isinstance(ref, (int, float)) and math.isfinite(ref):
                    m = sum(vals) / len(vals)
                    worst = max(worst, abs(m - ref) / max(1.0, abs(ref)))
        agree = worst
    pk = "compass" if pair == ("native", "compass") else f"{pair[1]}|{pair[0]}"   # the run's own paired reading of this table's two arms
    paired = {k: v for k, v in ((lr or {}).get("paired", {}).get(pk) or {}).items() if k in OFFICIAL}
    return {"dir": d, "sums_sha256": s.sha_of_list, "checked": s.checked, "ok": s.ok, "unmatched": s.missing[:5],
            "outside_list": sorted(s.stale)[:5], "outside_list_n": len(s.stale),
            "official_paired": paired, "official_agree": agree, "reps": out}


def db_run(g: Git, run: dict):
    d = run_dir(g, str(run["run"]), None)
    if not d:
        return None
    s = Sums(g, d)
    rows = []
    for x in sorted(g.files(d + "/")):
        m = re.search(r"/([^/]+)/rep-(\d+)/(native|omni)/arm\.json$", x)
        if not m:
            continue
        data = s.read(x[len(d) + 1:])
        try:
            a = json.loads(data)
        except (TypeError, json.JSONDecodeError):
            continue
        rows.append({"workload": m.group(1), "rep": int(m.group(2)), "arm": m.group(3),
                     **{k: a.get(k) for k in DB_GAUGES if isinstance(a.get(k), (int, float))}})
    return {"dir": d, "sums_sha256": s.sha_of_list, "checked": s.checked, "ok": s.ok, "unmatched": s.missing[:5], "rows": rows}


def table_commits(stem: str) -> dict:
    """The commit each run of a table names in the table's own run list (| Run | GitHub run | ... | Commit | ...), by run id."""
    out, hdr = {}, None
    for ln in (ROOT / "results" / "live" / f"{stem}.md").read_text(encoding="utf-8").splitlines():
        if not ln.startswith("|"):
            hdr = None if not ln.strip() else hdr
            continue
        cells = [c.strip().strip("`") for c in ln.strip().strip("|").split("|")]
        if "GitHub run" in cells and "Commit" in cells:
            hdr = cells
            continue
        if hdr and len(cells) == len(hdr) and re.fullmatch(r"\d+", cells[hdr.index("GitHub run")]):
            c = cells[hdr.index("Commit")]
            if re.fullmatch(r"[0-9a-f]{7,40}", c):
                out[cells[hdr.index("GitHub run")]] = c
    return out


def needed_dirs() -> list:
    """The raw folders the page plays back: the runs every benchmark's newest table names (for a sparse checkout)."""
    import export_scenarios as XS
    g, out = Git(), []
    for t in XS.tables():
        if not t["kind"]:
            continue
        stem = t["stem"]
        meta = json.loads((ROOT / "results" / "live" / f"{stem}.json").read_text(encoding="utf-8"))
        for r in meta.get("runs", []):
            d = run_dir(g, str(r.get("run") if isinstance(r, dict) else r))
            if d:
                out.append(d)
    return sorted(set(out))


def main(out_path):
    import export_scenarios as XS
    g = Git()
    benches = []
    for t in XS.tables():
        if not t["kind"]:
            continue
        base, kind, n, stem = t["base"], t["kind"], t["n"], t["stem"]
        way = re.search(r"_4W_(TOP|ORCH|BARE|VS|BOTH)$", stem)
        pair = FOUR_WAYS[way.group(1)] if way else ("native", "compass")
        meta = json.loads((ROOT / "results" / "live" / f"{stem}.json").read_text(encoding="utf-8"))
        runs, raw_runs = [], meta.get("runs", [])
        if raw_runs and not isinstance(raw_runs[0], dict):            # a table that lists its runs by id alone
            eng = meta.get("engines") or [None] * len(raw_runs)
            raw_runs = [{"tag": "ABC"[i] if i < 3 else str(i + 1), "run": x, "engine": eng[i] if i < len(eng) else None}
                        for i, x in enumerate(raw_runs)]
        sds = []
        for r in raw_runs:
            rec = k8s_run(g, r, ADDON_SETUP.get(base, ""), pair) if kind == "k8s" else db_run(g, r)
            if rec:
                for rep in rec.get("reps") or []:
                    for arm in ("native", "omni"):
                        sds += (rep.get(arm) or {}).pop("_noise", None) or []
                if not r.get("commit") and rec.get("dir"):          # a table that names its runs by id alone: its own run list, else the run's RUN.txt, names its commit
                    c = table_commits(stem).get(str(r.get("run")))
                    m = None if c else re.search(rb"^commit=([0-9a-f]{7,40})", g.read(f"{rec['dir']}/RUN.txt") or b"", re.M)
                    if c or m:
                        r = dict(r, commit=c or m.group(1).decode())
                runs.append({"tag": r.get("tag"), "id": str(r.get("run")), "commit": r.get("commit"), "engine": r.get("engine"), **serial(r), **rec})
        title = XS.table_title(stem)
        arms = None
        if way:   # the table's own words for its two arms, from its title: "the four ways: <candidate> against <reference> (register row N)"
            m = re.search(r"the four ways: (.+?) against (.+?) \(register", title)
            if m:
                arms = {"native": m.group(2)[:1].upper() + m.group(2)[1:], "omni": m.group(1)[:1].upper() + m.group(1)[1:],
                        "omniOn": pair[1].startswith("compass"), "way": way.group(1)}
        benches.append({"key": base, "kind": kind, "file": f"results/live/{stem}.md", "engine": f"omni-v{n}", "title": title, "runs": runs, "arms": arms,
                        # the noise measured on this table's own requests, both arms, runs A, B and C: the median over every window
                        "noise": {"sigma": round(statistics.median(sds), 3), "windows": len(sds), "window": NOISE_N} if sds else None})
        ck, okk = sum(r["checked"] for r in runs), sum(r["ok"] for r in runs)
        ag = [r.get("official_agree") for r in runs if r.get("official_agree") is not None]
        out_n = sum(r.get("outside_list_n") or 0 for r in runs)
        print(f"runs {stem:22s} {len(runs)} runs, {ck} files read, {okk} match their run's SHA-256 list"
              + (f", {out_n} on the branch outside the run's own list left out" if out_n else "")
              + (f"; the scorer per repetition against the run's own result: largest relative difference {max(ag):.1e}" if ag else ""))
    Path(out_path).write_text(json.dumps({"bin_s": BIN, "hist_ms": HIST_MS, "benchmarks": benches}, separators=(",", ":")), encoding="utf-8")


if __name__ == "__main__":
    if sys.argv[1:2] == ["--dirs"]:
        print("\n".join("/" + d + "/" for d in needed_dirs()))
    else:
        main(sys.argv[1] if len(sys.argv) > 1 else "runs.json")
