# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Rebuilds the live benchmark engine page (docs/engine/OMNI_COMPASS_LIVE_ENGINE.html) from the engine that stands and the
repository's own results: the page is a monitor of the engine, never a drawing of it.

Every record the page replays is made again here by the repository's own code on the checkout it runs in:

  harness    docs/engine/export_harness_trace.py: the realms harness (realms/harness.py, the max of
             realms/compass_arm_v5.py with the bone, the twins and the immune system), one organism and each muscle alone
  ctlrec     docs/engine/export_controller_trace.py: the shipped controller (omni_controller/controller.py) on the model
             cluster, on top of the HPA (the max) and in the cloud's setting, every tick and every audited decision
  runs       docs/engine/export_runs.py: the official runs as recorded, every three-run table's runs A, B and C read
             back from their raw files, every file's SHA-256 matched against the run's own list, every Kubernetes
             repetition scored by the repository's own scorer (tools/live_reps.py) and checked against the run's result
  scen       docs/engine/export_scenarios.py: the GPU card (realms/gpu_card.py), the Linux host (tools/model_gate.py's
             conveyance), every muscle and organism of the realms table (results/realms_v5) and every judged row of the
             newest engine's receipts (results/live/V<n>_*.md)
  cpptwin    docs/engine/export_cpp_twins.py: the Python's own runs fed through the C++ engine (cpp/): every Python/C++
             twin's parity check, every compass law the runs above wired (recorded as they ran), and the seven organisms
             at the tune-down, every muscle's law, reading by reading through the C++ compass law
  dial       the heartbeat dial (omni-v17): every beat of the Kubernetes governor in our own models, from the newest
             beat ladder (results/model_gate/V<n>_LADDER.json, tools/beat_ladder.py), beside native and the main engine's 60 s
  build      what was built and from what: the engine (tools/omni_version.py), the commit, the time, and, where a GitHub
             token is present, the runs GitHub is running now (gh run list) and every run started for the chips and the
             clouds (the ledger, kept in docs/engine/github_ledger.json for a build without a token)

The page names the engine it stands on (data-engine on its <html>); the build stamps the engine tools/omni_version.py reads on
the page and rebuilds every record on it, and when that engine is newer than the one the page's prose was written for, the page
says so in a banner until the prose is realigned; --check fails a page whose engine differs from the one that stands.
Usage: python3 docs/engine/build_live_engine.py [--check] [--no-runs]. --check rebuilds in memory and exits 1 if any record
differs from the page (nothing written). Evidence class S for the models; the receipts keep their own classes.
"""
from __future__ import annotations

import argparse
import datetime
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PAGE = HERE / "OMNI_COMPASS_LIVE_ENGINE.html"
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(HERE))

CDEC = ["E", "U", "calm", "kappa", "h", "sigma", "nu", "gate", "gate_ok", "nodes_ok", "rec", "seen", "rho", "cp", "cv", "cF",
        "cc", "cw", "vs", "va", "verdict", "writes", "q", "law"]       # the page's order of an audited decision (its CDEC)
TICK = ["nodes", "boot", "parked", "pods", "pending", "ms"]


def pack_controller(data: dict) -> dict:
    """export_controller_trace.py's record in the page's compact form: per run, each arm's ticks as columns and each
    decision's audit as one row in CDEC's order."""
    def dec(d):
        sc, ct = d.get("sc", {}), d.get("contract", {})
        val = {**d, "kappa": sc.get("kappa"), "h": sc.get("h"), "sigma": sc.get("sigma"), "nu": sc.get("nu"),
               "gate_ok": int(bool(d.get("gate_ok"))), "nodes_ok": int(bool(ct.get("nodes"))), "verdict": d.get("verdict", "")}
        return [val.get(k) for k in CDEC]
    out = {"slo": data["slo_ms"], "seeds": data["seeds"], "interval_s": data.get("interval_s", 60.0), "settings": {}}
    for name, sec in data["settings"].items():
        runs = {sd: {arm: {k: [t[k] for t in r[arm]] for k in TICK} for arm in ("native", "omni")} for sd, r in sec["runs"].items()}
        for sd, r in sec["runs"].items():
            runs[sd]["dec"] = [dec(d) for d in r["decisions"]]
        out["settings"][name] = {"readings": sec["readings"], "runs": runs}
    return out


def git(*args) -> str:
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True).stdout.strip()


def engine() -> tuple:
    """(name, digest) of the engine the checkout stands on, as tools/omni_version.py reads it."""
    out = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py")], capture_output=True, text=True, cwd=ROOT).stdout
    m = re.search(r"(omni-v\d+) \(digest ([0-9a-f]+)", out)
    return (m.group(1), m.group(2)) if m else ("unknown", "")


def github_runs() -> list | None:
    """The runs GitHub is running or queueing now (gh run list), where a token is present; None otherwise (not read)."""
    if not (shutil.which("gh") and (os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN"))):
        return None
    out = []
    for status in ("in_progress", "queued"):
        r = subprocess.run(["gh", "run", "list", "--status", status, "--limit", "100", "--json",
                            "databaseId,workflowName,displayTitle,status,createdAt,headBranch"], capture_output=True, text=True, cwd=ROOT)
        if r.returncode != 0:
            return None          # GitHub not read: never an empty list under a fresh stamp
        try:
            out += json.loads(r.stdout or "[]")
        except json.JSONDecodeError:
            return None
    return [{"id": r["databaseId"], "workflow": r["workflowName"], "title": r["displayTitle"][:140], "status": r["status"],
             "since": r["createdAt"], "branch": r["headBranch"]} for r in out]


LEDGER = {"aks-metered.yml": "Azure", "gke-metered.yml": "Google Cloud", "eks-metered.yml": "Amazon Web Services",
          "cloud-check.yml": "the $0 cloud check", "lambda-gpu.yml": "the GPU on Lambda", "cpu-power.yml": "the CPU package"}
LEDGER_CACHE = HERE / "github_ledger.json"
from tools.repo import NAME as REPO   # noqa: E402  (the repository, written once in tools/repo.py)
LEDGER_GAUGES = ["machines billed, machine-hours", "compute bill at list price ($)", "worker nodes in service, mean", "response time (ms), 95th percentile",
                 "failed requests (%)", "time over the response line (% of samples)"]


CHECKING = False      # --check: a check reads and compares, it never fetches or writes anything


def ledger(camp: dict | None = None) -> dict:
    """Every run GitHub was asked to start for the chips and the clouds (gh run list --event workflow_dispatch, newest
    first), each with the engine its commit stands on (tools/omni_version.py --commit) and whether its raw files are on the
    branch raw. Read from GitHub where a token is present, and kept in docs/engine/github_ledger.json; without a token the
    last reading kept there is used, and the page says when it was read. Under --check only the kept reading is used."""
    data = None
    if not CHECKING and shutil.which("gh") and (os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")):
        got = {}
        for wf in LEDGER:
            r = subprocess.run(["gh", "run", "list", "--workflow", wf, "--event", "workflow_dispatch", "--limit", "60", "--json",
                                "databaseId,displayTitle,status,conclusion,createdAt,updatedAt,headSha,headBranch"],
                               capture_output=True, text=True, cwd=ROOT)
            if r.returncode != 0:            # not read: the last reading kept stands, with its own time
                got = None
                break
            try:
                got[wf] = [{"id": x["databaseId"], "title": x["displayTitle"], "status": x["status"], "conclusion": x["conclusion"] or None,
                            "created": x["createdAt"], "updated": x["updatedAt"], "sha": x["headSha"], "branch": x["headBranch"]}
                           for x in json.loads(r.stdout or "[]")]
            except json.JSONDecodeError:
                got = None
                break
        if got:
            data = {"read_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "source": "GitHub Actions, workflow_dispatch runs of each workflow, newest first", "workflows": got,
                    "campaign": camp if camp is not None else campaign_reading(), "grid": grid_reading()}
            # kept for a build without a token; GitHub's own rebuild reads the list fresh every time and commits only the page,
            # so it never rewrites the cache (19 October: the rewritten cache, left uncommitted, stopped the job's push)
            if os.environ.get("GITHUB_ACTIONS") != "true":
                LEDGER_CACHE.write_text(json.dumps(data, indent=1) + "\n", encoding="utf-8")
    if data is None and LEDGER_CACHE.exists():
        data = json.loads(LEDGER_CACHE.read_text(encoding="utf-8"))
    if data is None:
        return {"read_at": None, "workflows": {}, "campaign": None}
    sys.path.insert(0, str(ROOT / "scripts"))
    import dispatch_grid as D
    if (data.get("campaign") or {}).get("since") != D.RERUN_SINCE:
        data["campaign"] = None
    if (data.get("grid") or {}).get("since") != D.SINCE:      # a kept grid reading counts only for its own campaign
        data["grid"] = None
    import export_runs as XR
    ref, pre = XR.raw_ref()
    raw = set(git("ls-tree", "--name-only", f"{ref}:{pre.rstrip('/')}" if pre else ref).split())
    eng = {}
    for wf, rs in data["workflows"].items():
        for r in rs:
            if r["sha"] not in eng:
                if not CHECKING and subprocess.run(["git", "-C", str(ROOT), "cat-file", "-e", r["sha"] + "^{commit}"], capture_output=True).returncode:
                    # fetch that one commit; --depth only where the checkout is already shallow (a full clone given --depth turns shallow)
                    shallow = git("rev-parse", "--is-shallow-repository") == "true"
                    subprocess.run(["git", "-C", str(ROOT), "fetch", "-q", *(["--depth", "1"] if shallow else []), "origin", r["sha"]], capture_output=True)
                out = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py"), "--commit", r["sha"]],
                                     capture_output=True, text=True, cwd=ROOT).stdout
                m = re.search(r"(omni-v\d+) \(digest", out)
                eng[r["sha"]] = m.group(1) if m else None
            r["engine"] = eng[r["sha"]]
            r["raw"] = any(f"run-{r['id']}" in x for x in raw)
            if wf in ("aks-metered.yml", "gke-metered.yml", "eks-metered.yml") and r["status"] != "completed" and shutil.which("gh") and not CHECKING:
                # a cloud set runs its repetitions one at a time, and GitHub lists the whole run as queued while it does: its
                # jobs say where it is (the repetitions measured to the end, the one running, how many it may take)
                jobs, page = [], 1
                while page < 5:
                    got = subprocess.run(["gh", "api", f"repos/{REPO}/actions/runs/{r['id']}/jobs?filter=latest&per_page=100&page={page}"],
                                         capture_output=True, text=True, cwd=ROOT)
                    try:
                        js = json.loads(got.stdout or "{}").get("jobs") or []
                    except json.JSONDecodeError:
                        break
                    jobs += js
                    if len(js) < 100:
                        break
                    page += 1
                reps = [j for j in jobs if re.match(r"run \(\d+\)$", j.get("name") or "")]
                if reps:
                    r["progress"] = {"total": len(reps), "done": sum(j["status"] == "completed" and j["conclusion"] == "success" for j in reps),
                                     "running": sum(j["status"] == "in_progress" for j in reps)}
            if wf == "cloud-check.yml" and r["conclusion"] == "failure" and not r.get("reason") and shutil.which("gh") and not CHECKING \
                    and r is next((x for x in rs if x["title"] == r["title"] and x["status"] == "completed"), None):
                # the newest finished check of each cloud: the reason its failed job wrote (its own error annotations), so the page can say why the gate holds
                got = subprocess.run(["gh", "api", f"repos/{REPO}/actions/runs/{r['id']}/jobs"], capture_output=True, text=True, cwd=ROOT)
                try:
                    jobs = json.loads(got.stdout or "{}").get("jobs") or []
                except json.JSONDecodeError:
                    jobs = []
                msgs = []
                for j in jobs:
                    if j.get("conclusion") != "failure":
                        continue
                    an = subprocess.run(["gh", "api", f"repos/{REPO}/check-runs/{j['id']}/annotations"], capture_output=True, text=True, cwd=ROOT)
                    try:
                        msgs += [a["message"] for a in json.loads(an.stdout or "[]") if a.get("annotation_level") == "failure" and not str(a.get("message", "")).startswith("Process completed")]
                    except (json.JSONDecodeError, TypeError, KeyError):
                        pass
                if msgs:
                    r["reason"] = " ".join(dict.fromkeys(msgs))
                    r["reason_read"] = f"the job's error annotations, read {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}"
            if wf == "aks-metered.yml" and r["raw"] and r["conclusion"] == "success":   # the bill as the run's own LIVE_REPS.json reads it
                src = f"{ref}:{pre}run-{r['id']}/live-reps-aks/LIVE_REPS.json"
                try:
                    lr = json.loads(git("show", src) or "{}")
                except json.JSONDecodeError:
                    lr = {}
                arm = next(iter((lr.get("paired") or {}).values()), {})
                if arm:
                    r["result"] = {"reps": len((lr.get("repetitions") or {}).get("native") or []),
                                   "gauges": {g: {k: arm[g].get(k) for k in ("native", "omni", "ci95", "significant")} for g in LEDGER_GAUGES if g in arm}}
                    # the machines Azure billed every 15 s in each arm of each repetition (billed_nodes.csv), for the bill monitor's replay
                    billed = []
                    for i in range(1, 101):
                        arms = {}
                        for arm_key, names in (("native", ("native",)), ("omni", ("compass", "omni"))):
                            for nm in names:
                                txt = git("show", f"{ref}:{pre}run-{r['id']}/aks-{i}/bench-{nm}-{i}/billed_nodes.csv")
                                if txt:
                                    pts = [ln.split(",") for ln in txt.splitlines()[1:] if "," in ln]
                                    try:
                                        t0 = int(pts[0][0])
                                        arms[arm_key] = [[int(a) - t0, int(b)] for a, b in pts]
                                    except (ValueError, IndexError):
                                        pass
                                    break
                        if not arms:
                            break
                        billed.append({"rep": i, **arms})
                    if billed:
                        r["result"]["billed"] = billed
    # the page shows the runs on omni-v8 and newer, each with its engine; the earlier engines' runs stay in GitHub's own list
    # and in docs/history (the founder's order of 19 October: no version 7 on the page)
    def recent(r):
        m = re.match(r"omni-v(\d+)$", r.get("engine") or "")
        return bool(m) and int(m.group(1)) >= 8
    data["workflows"] = {wf: [r for r in rs if recent(r)] for wf, rs in data["workflows"].items()}
    queues = {}
    for wf, f in (("aks-metered.yml", "azure_queue.txt"), ("gke-metered.yml", "google_queue.txt"), ("eks-metered.yml", "amazon_queue.txt")):
        q = ROOT / "scripts" / f
        sets = []
        for x in (q.read_text(encoding="utf-8").splitlines() if q.exists() else []):
            if "|" in x and not x.startswith("#"):
                label, kv = x.split("|", 1)
                steps = dict(p.split("=", 1) for p in kv.split(";") if "=" in p).get("load_steps")
                sets.append({"label": label, "key": f"burst {steps}" if steps else label})
        queues[wf] = sets
    data["queues"] = queues
    return data


TABLE_OF = {   # a benchmark in scripts/reruns.txt -> the file name of its three-run table(s) in results/live (V<n>_<stem>.md), as the
    # person who ran tools/confirm_abc.py (or the benchmark's own *_abc.py) named it; a table no entry names is still listed
    # (board() below), and an entry no longer in scripts/reruns.txt fails the build
    "Kubernetes CruiseKube": ["CRUISEKUBE"], "Kubernetes Goldilocks": ["GOLDILOCKS"], "Kubernetes fixed capacity": ["CAPACITY"],
    "kubernetes steady": ["STEADY"], "kubernetes wandering": ["WANDERING"],
    "kubernetes all four": ["ALL_FOUR"], "kubernetes fairness": ["FAIRNESS"], "kubernetes faults": ["FAULTS"],
    "kubernetes batch": ["BATCH"], "kubernetes google 2011 trace": ["TRACE_GOOGLE2011"],
    "kubernetes keda add-ons": ["KEDA_REQUESTS", "KEDA_CPU_REQUESTS"], "redis resource": ["REDIS"], "redis service": ["REDIS_SERVICE"],
    "kafka resource": ["KAFKA"], "kafka service": ["KAFKA_SERVICE"], "postgresql resource": ["PGBENCH"], "mysql resource": ["SYSBENCH"],
    "mongodb resource": ["YCSB"], "mysql resource, native as shipped": ["SYSBENCH_SHIPPED"],
    "redis resource, native as shipped": ["REDIS_SHIPPED"], "mongodb resource, native as shipped": ["YCSB_SHIPPED"],
    "mysql service": ["SYSBENCH_SERVICE"], "mongodb service": ["YCSB_SERVICE"], "postgresql service": ["PGBENCH_SERVICE"],
    "robot arms": ["MUJOCO"], "power grids": ["PANDAPOWER"], "buildings and batteries": ["CITYLEARN"],
    "drone swarms": ["SWARM"], "robustness kill": ["ROBUST_KILL"], "robustness long": ["ROBUST_LONG"],
    # the governors (tools/governors_page.py: a governor's table V12_<SETTING>.json, its four ways V12_<SYSTEM>_4W_<TAG>.json)
    "kubernetes batch through kueue": ["KUEUE"], "kubernetes batch through volcano": ["VOLCANO"], "kubernetes batch through kai": ["KAI"],
    "kubernetes batch through koordinator, on the cgroup root its own tests use": ["KOORDINATOR"],
    "kubernetes batch through the default scheduler": ["VANILLA"], "kubernetes batch through the bin-packing scheduler": ["BINPACK"],
    **{f"kubernetes batch four ways through {who}": [f"{sys_}_4W_{tag}" for tag in ("TOP", "ORCH", "BARE", "VS", "BOTH")]
       for who, sys_ in (("the KAI scheduler", "KAI"), ("Koordinator", "KOORDINATOR"), ("Kueue", "KUEUE"), ("Volcano", "VOLCANO"),
                         ("the bin-packing scheduler", "BINPACK"))}}


RUN_STATE = {"in_progress": "running", "queued": "waiting", "waiting": "waiting", "pending": "waiting", "requested": "waiting"}


def entry_runs(camp) -> dict:
    """{(entry name, run letter): (run id, state)} for every entry of the campaign, from the campaign's runs read from GitHub:
    a run whose workflow titles it from its inputs by that title (the k-th entry of a title is its k-th run), every other by
    its count in its workflow in release order, as the conductor reads them back (scripts/dispatch_grid.py rerun_queue). The
    state is "measured" (finished to the end), "stopped short", "running" or "waiting"; a run not yet started is absent."""
    out = {}
    for c in campaign_places():
        rs = (camp.get("workflows") or {}).get(c["wf"]) or []
        if c["title"]:
            same = [x for x in rs if x.get("title") == c["title"]]
            r = same[c["occ"]] if c["occ"] < len(same) else None
        else:
            r = rs[c["pos"]] if c["pos"] < len(rs) else None
        if r:
            out[(c["name"], c["run"])] = (r["id"], RUN_STATE.get(r["status"]) or ("measured" if r["conclusion"] == "success" else "stopped short"))
    return out


def board(runs: list, camp: dict | None = None) -> list:
    """Every benchmark the repository holds a place for, and where it stands: its newest three-run table and that table's
    engine, whether GitHub is running it now, or that it is queued, switched off or not yet launched. Read from
    scripts/reruns.txt, the cloud queues, the GPU campaign's profiles and the results themselves; nothing is written here
    that the repository does not say."""
    import export_scenarios as XS
    wf_name = {}
    for y in (ROOT / ".github" / "workflows").glob("*.yml"):
        m = re.search(r"^name:\s*(\S+)", y.read_text(encoding="utf-8"), re.M)
        if m:
            wf_name[y.name] = m.group(1)
    live = {r["workflow"] for r in runs if r["status"] == "in_progress"}
    waiting = {r["workflow"] for r in runs if r["status"] == "queued"}
    out = []
    def state(wf):
        n = wf_name.get(wf, wf.removesuffix(".yml"))
        return "running now" if n in live else "queued on GitHub" if n in waiting else None
    found = {t["base"]: t for t in XS.tables()}
    stands = engine()[0]
    er = entry_runs(camp) if camp else None
    names = [ln.split("|")[0] for ln in (ROOT / "scripts" / "reruns.txt").read_text(encoding="utf-8").splitlines()
             if ln.strip() and not ln.startswith("#") and "|" in ln]
    gone = sorted(set(TABLE_OF) - set(names))
    if gone:
        raise SystemExit(f"TABLE_OF names benchmarks scripts/reruns.txt no longer holds: {gone}")
    for ln in (ROOT / "scripts" / "reruns.txt").read_text(encoding="utf-8").splitlines():
        if not ln.strip() or ln.startswith("#") or "|" not in ln:
            continue
        name, wf = ln.split("|")[:2]
        if "by itself" in name or re.search(r"\barms=[^;]*\bsolo\b", ln):   # Omni-Compass is never by itself (the founder's order of 25 October): not on this page
            continue
        tables = []
        for stem in TABLE_OF.get(name, []):
            t = found.pop(stem, None)
            if t:
                tables.append({"file": f"results/live/{t['stem']}.md", "engine": f"omni-v{t['n']}"})
        if name == "1107 muscles and seven organisms":
            rj = ROOT / "results" / "realms_v5" / "REALMS_V5.json"
            if rj.exists():
                tables.append({"file": "results/realms_v5/REALMS_V5.md", "engine": json.loads(rj.read_text(encoding="utf-8"))["run"]["engine"]})
        if er is None:     # the campaign's runs not read at this build: GitHub's run list for the workflow as a whole
            now, abc = state(wf) or ("in the reruns queue" if not tables else None), None
        else:              # its own A, B and C, read from GitHub
            abc = {L: list(er[(name, L)]) for L in "ABC" if (name, L) in er}
            sts = [v[1] for v in abc.values()]
            now = ("running now" if "running" in sts else "queued on GitHub" if "waiting" in sts
                   else None if any(t["engine"] == stands for t in tables)
                   else ("run: every run stopped short" if "measured" not in sts else "run: its three-run table not yet written") if len(sts) == 3
                   else "in the reruns queue")
        out.append({"group": "Reruns on the Engine That Stands", "name": name, "workflow": wf,
                    "tables": tables, "now": now, **({"abc": abc} if abc is not None else {})})
        if name == "1107 muscles and seven organisms":    # the eighth organism, the orchestra, beside the seven: its own runner
            oj = ROOT / "results" / "orchestra" / "ORCHESTRA.json"
            out.append({"group": "Reruns on the Engine That Stands", "name": "Orchestra Organism · Class S",
                        "workflow": "orchestra.yml", "tables": ([{"file": "results/orchestra/ORCHESTRA.md", "engine": json.loads(oj.read_text(encoding="utf-8"))["run"]["engine"]}]
                                                               if oj.exists() else []), "now": state("orchestra.yml") or (None if oj.exists() else "not yet run")})
    for t in found.values():   # a three-run table no campaign entry names: listed all the same, never left out
        out.append({"group": "Reruns on the Engine That Stands", "name": XS.table_title(t["stem"]), "workflow": "",
                    "tables": [{"file": f"results/live/{t['stem']}.md", "engine": f"omni-v{t['n']}"}], "now": None})
    for cloud, f, wf in (("Azure", "azure_queue.txt", "aks-metered.yml"), ("Google Cloud", "google_queue.txt", "gke-metered.yml"),
                         ("Amazon Web Services", "amazon_queue.txt", "eks-metered.yml")):
        q = ROOT / "scripts" / f
        if not q.exists():
            continue
        lines = [x for x in q.read_text(encoding="utf-8").splitlines() if x.strip() and not x.startswith("#")]
        on = any(x.strip() == "switch=on" for x in lines)
        running_titles = " ".join(r["title"] for r in runs if r["status"] == "in_progress" and r["workflow"] == wf_name.get(wf, wf[:-4]))
        for x in lines:
            if "|" not in x:
                continue
            label = x.split("|")[0]
            out.append({"group": f"{cloud} Bill at the Tune-Down", "name": label, "workflow": wf,
                        "tables": [], "now": ("running now" if label.split()[0] in running_titles else "in the queue") if on else
                        "not yet run: its queue's switch is off"})
    gp = ROOT / "scripts" / "gpu_campaign_profiles.json"
    if gp.exists():
        g = json.loads(gp.read_text(encoding="utf-8"))
        for prof, v in g.get("profiles", {}).items():
            for scale in g.get("organism_scales", []):
                out.append({"group": "GPU Chips on Lambda · Class P", "name": f"{prof} ({v.get('physical_gpus')} "
                            f"GPU{'s' if v.get('physical_gpus', 1) > 1 else ''}), {scale} cop{'y' if scale == 1 else 'ies'} of each organism",
                            "workflow": v.get("script", ""), "tables": [], "now": "launched" if g.get("launch") else "not yet launched: its runs start from one exact commit of the engine that stands"})
    return out


# Words a record carries from the repository's documents that name a person or an order instead of saying what is there; the page
# prints the rest of each sentence as written (T35 to T38: docs/REGISTER.md, the preregistrations, results/scenarios, the grid's rule).
PLAIN = ((", the gap the tree showed at the founder's reading", ", the gap the tree showed"), (" at the founder's second sweep", ""),
         (" at the founder's final sweep", ""), (" at the founder's sweep", ""), (", the founder's list, ", ", "), (", the founder's list (", " ("),
         (", the founder's list; ", "; "), (", the founder's list)", ")"), ("of the founder's list", "on the list"),
         (", the founder's order to run every product", ", to run every product"),
         ("until the founder opens an account and", "until an account is opened and"),
         ("the founder's own laptop can run it", "a Windows laptop can run it"), ("on the founder's own laptop or tower", "on a Windows laptop or tower"),
         ("the founder's own tower or laptop", "a tower or laptop"), (", at the founder's order of that night", ""),
         ("the governors and orchestrators the founder named", "the fourteen governors and orchestrators of section 4e"),
         ("by the founder's rule of 24 October", "by the key and its 0.5% floor"))


def plain(t):
    for a, b in PLAIN:
        t = t.replace(a, b)
    return t


def _clean(v):
    """NaN and infinity, which JSON cannot carry, as null."""
    if isinstance(v, float):
        return v if math.isfinite(v) else None
    if isinstance(v, dict):
        return {k: _clean(x) for k, x in v.items()}
    if isinstance(v, list):
        return [_clean(x) for x in v]
    return v


def beat_sweep() -> dict:
    """The heartbeat sweep's record (tools/heartbeat_sweep.py --table, results/model_gate/HEARTBEAT_SWEEP.json) as the page's
    heartbeat monitor reads it: every beat of each engine in each setting, each gauge's change in percent against native and
    against the same engine at 15 s and at 60 s, with its 95% interval and its word, and the engine's own cost a day."""
    f = ROOT / "results" / "model_gate" / "HEARTBEAT_SWEEP.json"
    if not f.exists():
        return {"missing": str(f.relative_to(ROOT)), "periods": [], "rows": {}}
    rec = json.loads(f.read_text(encoding="utf-8"))
    fin = lambda v: v if isinstance(v, (int, float)) and math.isfinite(v) else None

    def pct(x, base):
        # the gate's reading (tools/model_gate.py reading) in percent of the zero line's mean over the same seeds: the change is
        # mean_change/relative's base; where the change is nought, the zero line's mean as recorded
        m, (lo, hi), rel = x["mean_change"], x["ci95"], x["relative"]
        b = m / rel if fin(rel) and rel and m else base
        out = {"word": x["word"], "pct": fin(100 * rel) if fin(rel) is not None else None,
               "lo": fin(100 * lo / b) if b else None, "hi": fin(100 * hi / b) if b else None}
        return {k: (round(v, 3) if isinstance(v, float) else v) for k, v in out.items()}
    rows, periods, seeds = {}, set(), 0
    for key, v in rec.items():
        parts = key.split("|")
        if len(parts) != 3:
            continue
        setting, eng, p = parts
        nat = rec.get(f"{setting}|native", {})
        mean_at = lambda q: (rec.get(f"{setting}|{eng}|{q}") or {}).get("mean", {})
        rows.setdefault(setting, {}).setdefault(eng, {})[p] = {
            "vs": {g: pct(x, nat.get(g)) for g, x in v["vs_native"].items()},
            "vs15": {g: pct(x, mean_at(15).get(g)) for g, x in (v.get("vs_15") or {}).items()} or None,
            "vs60": {g: pct(x, mean_at(60).get(g)) for g, x in (v.get("vs_60") or {}).items()} or None,
            "cost": {c: round(x, 3) for c, x in v["cost"].items()}}
        periods.add(float(p))
        seeds = max(seeds, len(v["seeds"]))
    return {"file": str(f.relative_to(ROOT)), "seeds": seeds, "rows": rows,
            "periods": [int(p) if p == int(p) else p for p in sorted(periods)]}


def fleet() -> dict:
    """The benefit sheet (results/BENEFIT_SHEET.json, every benchmark's benefit in one row), the Omni index's headline
    (results/OMNI_INDEX.md) and the grid (results/grid_v5/GRID.json, the newest grid with squares; the dispatches of the
    engine that stands from results/grid_v<n>/DISPATCHED.json), each as the repository holds it."""
    out = {"benefit": [], "index": None, "grid": None}
    bs = ROOT / "results" / "BENEFIT_SHEET.json"
    if bs.exists():
        out["benefit"] = [{k: r.get(k) for k in ("date", "benchmark", "benefit", "pct", "gain", "loss", "given", "words", "what", "file", "engine")}
                          for r in json.loads(bs.read_text(encoding="utf-8")).get("rows", [])]
    oi = ROOT / "results" / "OMNI_INDEX.md"
    if oi.exists():
        t = oi.read_text(encoding="utf-8")
        m = re.search(r"## Headline:([^\n]*)", t); m2 = re.search(r"## The second reading[^\n]*?: ([^\n]*)", t)
        out["index"] = {"headline": m.group(1).strip() if m else None, "service": m2.group(1).strip() if m2 else None, "file": "results/OMNI_INDEX.md"}
        oj = ROOT / "results" / "OMNI_INDEX.json"
        if oj.exists():   # each category's own reading, so the page can say what carries the headline
            oij = json.loads(oj.read_text(encoding="utf-8"))
            out["index"]["categories"] = oij.get("categories") or {}
            # each category's service reading (work and speed), so the page words a category as the index does (tools/omni_index.py
            # index_word: a minus is a LOSS where the service reading is below one too, else power given; the referee of 30 October)
            out["index"]["service_categories"] = oij.get("service_categories") or {}
            # the figure of record as the index's own record holds it, never read back out of a sentence (the mathematics seat of
            # 24 October: the headline's first percent is the 0.5% floor it names, not the index)
            out["index"]["headline_pct"] = oij.get("headline_pct")
            out["index"]["service_pct"] = oij.get("service_headline_pct")
    # the grid: the engine that stands's own when its squares have landed, else the newest grid with squares, named by its
    # own engine (never read as the engine that stands's), with the dispatches of the engine that stands beside it
    stand_n = engine()[0].rsplit("v", 1)[-1]
    disp_f = ROOT / "results" / f"grid_v{stand_n}" / "DISPATCHED.json"
    grids = sorted((ROOT / "results").glob("grid_v*/GRID.json"), key=lambda q: int(re.sub(r"\D", "", q.parent.name)))
    gp = disp_f.with_name("GRID.json") if disp_f.with_name("GRID.json").exists() else (grids[-1] if grids else disp_f.with_name("GRID.json"))
    disp = len(json.loads(disp_f.read_text(encoding="utf-8")).get("dispatches", [])) if disp_f.exists() else 0
    out["grid"] = {"file": None, "engine": engine()[0], "squares": {"modelled": {}, "kube": {}}, "dispatched_on_engine_that_stands": disp}
    if gp.exists():
        md = gp.with_name("GRID.md"); eng = None
        if md.exists():
            m = re.search(r"engine (omni-v\d+)", md.read_text(encoding="utf-8")); eng = m.group(1) if m else None
        g = json.loads(gp.read_text(encoding="utf-8"))
        sq = {"modelled": {}, "kube": {}}
        for k, v in g.get("modelled", {}).items():
            sq["modelled"][k] = {n: {"label": c.get("label"), "runs": c.get("runs"), "viol_pp": (c.get("viol_pp") or [None])[0],
                                     "work": (c.get("work") or [None])[0], "energy": (c.get("energy") or [None])[0]} for n, c in v.items() if isinstance(c, dict)}
        for k, v in g.get("kube", {}).items():
            sq["kube"][k] = {n: {"verdict": c.get("verdict"), "reps": c.get("repetitions"), "GAIN": c.get("GAIN"), "LOSS": c.get("LOSS"), "given": c.get("power given"),
                                 "p95": {kk: c["rows"][kk].get(kk2) for kk in ["response time (ms), 95th percentile"] if kk in c.get("rows", {}) for kk2 in ["pct"]}.get("response time (ms), 95th percentile")}
                             for n, c in v.items() if isinstance(c, dict)}
        out["grid"] = {"file": str(gp.relative_to(ROOT)), "engine": eng, "squares": sq, "dispatched_on_engine_that_stands": disp}
    sp = ROOT / "results" / "STEERING.json"   # how steadily the governor steered: its own moves on every Kubernetes table of the engine that stands
    out["steering"] = json.loads(sp.read_text(encoding="utf-8")) if sp.exists() else None
    out["register"] = register_places()
    out["orchestrators"] = orchestrators()
    out["orchestra"] = orchestra()
    import brain_off   # what the brain's six-state equations change in the governor's decisions (class S, the fleet model)
    out["brain_off"] = brain_off.compare()
    return _clean(out)


# The governors and orchestrators the founder named for the benchmark of omni-v13 (19 October), in his order. Each is a place on the
# page before its result exists: what it is and who ships it (public facts), then everything the repository holds for it, read at
# every build (a register row naming it, its newest three-run table results/live/V<n>_<KEY>.md, its workflow on GitHub). Nothing of
# a run is written here: its runs fill the place the moment they land.
def _governors():
    """The governors and orchestrators as the repository's own governors page holds them (tools/governors_page.py: the
    founder's list of 19 October, night, each with what it governs, native under it, its test, its catalog muscles and the
    settings it is read in)."""
    sys.path.insert(0, str(ROOT))
    from tools import governors_page as GP
    return GP


def _orch_alias(GP, slug: str, name: str) -> tuple:
    """The words that name a governor in the register, the campaign and a file's path: its slug, its name without what is
    in brackets, and the settings it is read in (the scheduler's vanilla and bin-packing runs)."""
    base = re.sub(r"\s*\(.*?\)", "", name).replace("The Kubernetes scheduler", "kube-scheduler").strip()
    extra = {"scheduler": ("default scheduler", "bin-packing scheduler", "kube-scheduler"), "ocm": ("open cluster management", "open-cluster-management"),
             "godel": ("gödel", "godel-scheduler"), "kai": ("kai-scheduler", "kai scheduler"), "crane": ("gocrane",)}.get(slug, ())
    return tuple(dict.fromkeys(x.lower() for x in (slug, base, *extra, *(k for k, _ in GP.settings_of(slug) if k != slug)) if x))


def _orch_pattern(alias) -> "re.Pattern":
    norm = lambda x: re.sub(r"[-_]+", " ", x.lower())
    return re.compile(r"(?<![a-z0-9])(" + "|".join(re.escape(norm(a)) for a in alias) + r")(?![a-z0-9])")


def _norm(x: str) -> str:
    return re.sub(r"[-_]+", " ", x.lower())


def run_title(wf: str, kv: dict, run: str) -> str | None:
    """The title GitHub gives an entry's run, rendered from its workflow's own run-name (.github/workflows/<wf>), with the
    entry's inputs and, for a workflow the conductor labels (scripts/dispatch_grid.py LABELLED), the run's letter as its
    label; None where the run-name is not a plain template of inputs (the run is then read back by its count)."""
    sys.path.insert(0, str(ROOT / "scripts"))
    import dispatch_grid as D
    y = ROOT / ".github" / "workflows" / wf
    m = re.search(r'^run-name:\s*"([^"\n]*)"\s*$', y.read_text(encoding="utf-8"), re.M) if y.exists() else None
    if not m:
        return None
    vals = {**{k: str(v) for k, v in kv.items()}, **({"label": run} if wf in D.LABELLED else {})}
    parts = re.split(r"\$\{\{\s*inputs\.(\w+)\s*\}\}", m.group(1))
    if any(name not in vals for name in parts[1::2]):
        return None
    return "".join(p if i % 2 == 0 else vals[p] for i, p in enumerate(parts))


def campaign_places() -> list:
    """Every run of the campaign in release order (scripts/dispatch_grid.py rerun_queue): its letter, entry, workflow and
    inputs, its count in its workflow (how the conductor reads a run back) and, where the workflow titles its runs from their
    inputs, the title it carries and which run of that title it is (the k-th entry of a title is its k-th run)."""
    sys.path.insert(0, str(ROOT / "scripts"))
    import dispatch_grid as D
    seen, occ, out = {}, {}, []
    for run, name, wf, kv in D.rerun_queue():
        pos = seen.get(wf, 0); seen[wf] = pos + 1
        title = run_title(wf, kv, run)
        k = (wf, title); n = occ.get(k, 0); occ[k] = n + 1
        out.append({"run": run, "name": name, "wf": wf, "kv": kv, "pos": pos, "title": title, "occ": n if title else None})
    return out


def orch_campaign() -> dict:
    """{governor slug: [its entries in the campaign of the engine that stands]}: each entry of scripts/reruns.txt whose name or
    inputs name the governor, with its run letter and its place in its workflow's own line (the conductor reads a run back by
    its count in its workflow, in release order: scripts/dispatch_grid.py rerun_queue)."""
    sys.path.insert(0, str(ROOT / "scripts"))
    import dispatch_grid as D
    GP = _governors()
    pats = {slug: _orch_pattern(_orch_alias(GP, slug, name)) for slug, name, *_ in GP.GOVERNORS}
    out = {}
    for c in campaign_places():
        text = _norm(c["name"] + " " + " ".join(f"{k} {v}" for k, v in c["kv"].items()))
        for slug, pat in pats.items():
            if pat.search(text):
                out.setdefault(slug, []).append({"run": c["run"], "name": c["name"], "wf": c["wf"], "pos": c["pos"],
                                                 "inputs": ";".join(f"{k}={v}" for k, v in c["kv"].items()),
                                                 **({"title": c["title"], "occ": c["occ"]} if c["title"] else {})})
    return out


def campaign_reading() -> dict | None:
    """The campaign's runs of every workflow a governor's entry stands in, dispatched since the campaign opened
    (scripts/dispatch_grid.py RERUN_SINCE), oldest first, a cancelled run left out as the conductor leaves it out: the k-th
    of these is the run of the workflow's k-th entry in the line. Read from GitHub; None where it cannot be read."""
    sys.path.insert(0, str(ROOT / "scripts"))
    import dispatch_grid as D
    wfs = sorted({wf for _, _, wf, _ in D.rerun_queue()})       # every workflow of the campaign, the governors' among them
    got, carries = {}, {}
    for wf in wfs:
        rs, page = [], 1
        while page <= 5:
            r = subprocess.run(["gh", "api", f"repos/{REPO}/actions/workflows/{wf}/runs?event=workflow_dispatch&created=>={D.RERUN_SINCE}&per_page=100&page={page}"],
                               capture_output=True, text=True, cwd=ROOT)
            try:
                got_page = json.loads(r.stdout or "").get("workflow_runs")
            except (json.JSONDecodeError, AttributeError):
                return None
            if r.returncode != 0 or got_page is None:
                return None
            rs += got_page
            if len(got_page) < 100:
                break
            page += 1
        # counted as the conductor counts them (scripts/dispatch_grid.py reruns_started): a cancelled run is no run, and a kind
        # workflow's run counts only on a commit that carries the rig (RIG_FILE)
        try:
            keep = [x for x in rs if x.get("conclusion") != "cancelled" and (wf not in D.RIG_WORKFLOWS or D.on_rig(x.get("head_sha", ""), carries))]
        except Exception:
            return None
        got[wf] = [{"id": x["id"], "status": x["status"], "conclusion": x.get("conclusion"), "created": x["created_at"],
                    "updated": x["updated_at"], "sha": (x.get("head_sha") or "")[:12], "title": (x.get("display_title") or "")[:120]}
                   for x in sorted(keep, key=lambda x: x["created_at"])]
    return {"since": D.RERUN_SINCE, "read_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "workflows": got}


def grid_reading() -> dict | None:
    """The grid of the engine that stands, read the way the conductor reads it (scripts/dispatch_grid.py): every run of
    six.yml and six-kube.yml since its campaign opened (SINCE), the runs each square has started (coverage: a square of n
    runs counts the first n of its organism and size) and the ones measured to the end, and the cells too large for a free
    runner (free_runner_refusals), listed and never rented. Read from GitHub; None where it cannot be read."""
    sys.path.insert(0, str(ROOT / "scripts"))
    import dispatch_grid as D
    try:
        runs = D.grid_runs()
    except Exception:          # GitHub not reachable from this build: the page says the grid's campaign was not read
        return None
    # a grid run is one the conductor named (a push's own run of the workflow is skipped and names no square); cancelled
    # and skipped runs count for nothing, as the conductor counts them
    runs = [r for r in runs if (D.SIX_NAME.match(r.get("display_title") or "") or D.KUBE_NAME.match(r.get("display_title") or ""))
            and r.get("conclusion") not in ("cancelled", "skipped")]
    done = [r for r in runs if r.get("status") == "completed" and r.get("conclusion") == "success"]
    cov_all, cov_done = D.coverage(runs, {"dispatches": []}, {}), D.coverage(done, {"dispatches": []}, {})
    name = dict(zip(D.ORGS, D.KUBE))
    squares = {}
    for kind, key in (("modelled", "six"), ("kube", "kube")):
        for size in D.SIZES:
            for o in (D.ORGS if key == "six" else D.KUBE):
                org = name[o] if key == "six" else o
                for n in (1, 10, 100, 1000):
                    want = range(0, n) if key == "six" else range(1, n + 1)
                    st = len(cov_all.get((key, size, o), set()) & set(want)); dn = len(cov_done.get((key, size, o), set()) & set(want))
                    if st:
                        squares[f"{kind}|{org}|{size}|{n}"] = [st, dn]
    refused = sorted(f"{'modelled' if g == 'six' else 'kube'}|{name.get(o, o)}|{size}" for g, size, o in D.free_runner_refusals())
    return {"engine": D.ENGINE, "since": D.SINCE, "read_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "runs": {"six": sum(r.get("path", "").endswith("six.yml") for r in runs), "six-kube": sum(r.get("path", "").endswith("six-kube.yml") for r in runs),
                     "running": sum(r.get("status") != "completed" for r in runs), "done": len(done)},
            "sizes": list(D.SIZES), "squares": squares, "refused": refused}


def _prereg(path: Path) -> dict:
    """A preregistration as it writes itself: its title, when it was declared, its question, what is measured and its known
    limits (markdown stripped; each line cut at a sentence end where it runs long)."""
    t = path.read_text(encoding="utf-8")
    clean = lambda x: plain(re.sub(r"\s+", " ", re.sub(r"\*\*|`|\[([^\]]*)\]\([^)]*\)", lambda m: m.group(1) or "", x)).strip())
    def cut(x, n=320):
        x = clean(x)
        if len(x) <= n:
            return x
        k = x.rfind(". ", 0, n)
        return x[:k + 1] if k > 80 else x[:n].rsplit(" ", 1)[0] + " …"
    head = next((ln[2:] for ln in t.splitlines() if ln.startswith("# ")), path.stem)
    secs = {}
    for blk in re.split(r"\n## ", t)[1:]:
        h, _, body = blk.partition("\n")
        secs[h.strip()] = body
    def bullets(body, n):
        out = []
        for ln in body.splitlines():
            m = re.match(r"(\s*)- (.*)", ln)
            if m:
                out.append([len(m.group(1)), m.group(2)])
            elif out and ln.strip() and not ln.lstrip().startswith(("|", "#", "<", "---", "*©")):
                out[-1][1] += " " + ln.strip()
        if not out:   # a section written as prose: its paragraphs, each cut at a sentence end
            return [{"d": 0, "t": cut(x, 480)} for x in re.split(r"\n\s*\n", body.strip())
                    if x.strip() and not x.lstrip().startswith(("|", "#", "<", "---", "*©"))][:3]
        return [{"d": min(d // 2, 2), "t": cut(x)} for d, x in out][:n]
    q = next((b for h, b in secs.items() if h.lower().startswith("the question")), "")
    meas = next((b for h, b in secs.items() if h.lower().startswith(("the workload and the measure", "the measure"))), "")
    lim = next((b for h, b in secs.items() if h.lower().startswith("known limits")), "")
    decl = re.search(r"(Declared[^.]*\.)", t)
    amend = [h for h in secs if h.lower().startswith("amendment")]
    return {"file": str(path.relative_to(ROOT)), "title": clean(re.sub(r"\s*\(preregistration\)\s*$", "", head)),
            "declared": cut(decl.group(1), 240) if decl else None, "question": cut(q.strip().split("\n\n")[0], 520) if q.strip() else None,
            "measure": bullets(meas, 10), "limits": bullets(lim, 6), "amendments": [clean(h) for h in amend][:8]}


def _owner(bench: str, pat) -> dict:
    """A governor's project, owner and licence as its register row names them: the bracket after its name,
    (org/repo, owner; licence); the owner is the repository's organisation where the row names none."""
    m = pat.search(_norm(bench))
    tail = bench[m.start():] if m else bench
    b = re.search(r"\(`?([\w.-]+/[\w.-]+)`?(?:,\s*([^;)]+?))?(?:;\s*([^)]+?))?\)", tail)   # the register's markdown is stripped: no backticks
    if not b:
        return {"repo": None, "owner": None, "licence": None}
    return {"repo": b.group(1), "owner": (b.group(2) or b.group(1).split("/")[0]).strip(), "licence": (b.group(3) or "").strip() or None}


def orchestrators() -> list:
    """Each governor as the repository's own governors page holds it (tools/governors_page.py: the founder's list of 19
    October, night, what it governs, native under it, its test, its catalog muscles, the settings it is read in), and what the
    repository holds for it now, read at every build: its register row (whole; its project, owner and licence as the row names
    them), its preregistration (the question, what is measured, the known limits), its own rig files (a file of a shared rig
    that names another governor is that one's) and its own workflows (those its campaign entries run, or whose name names it),
    its entries in the campaign of the engine that stands, the runs started (results/live/governors_runs.json) and its newest
    three-run table with every judged row as written. Empty fields mean the repository holds nothing for it yet."""
    import csv
    import export_scenarios as XS
    GP = _governors()
    reg = {r["n"]: r for r in register_places(limit=False)}
    flows = sorted(p.name for p in (ROOT / ".github" / "workflows").glob("*.yml"))
    camp, started = orch_campaign(), (json.loads(GP.RUNS.read_text(encoding="utf-8")) if GP.RUNS.exists() else {})
    with GP.CATALOG_FILE.open(encoding="utf-8") as f:
        cat = list(csv.DictReader(f))
    pats = {slug: _orch_pattern(_orch_alias(GP, slug, name)) for slug, name, *_ in GP.GOVERNORS}
    tables = {}
    for f in (ROOT / "results" / "live").glob("V*_*.md"):
        m = re.fullmatch(r"V(\d+)_(.+)", f.stem)
        if m:
            tables.setdefault(m.group(2), []).append(int(m.group(1)))
    out = []
    for slug, name, row, field, native, test in GP.GOVERNORS:
        pat, r0 = pats[slug], reg.get(row)
        own = lambda path: (lambda hit: not hit or slug in hit)({k for k, q in pats.items() if q.search(_norm(path))})
        # its newest three-run table: the governors page's own (V12_<SETTING>.json), else the newest table whose name holds the
        # governor's slug or one of its settings (V10_CRUISEKUBE.md)
        table = None
        keys = [k for k, _ in GP.settings_of(slug)]
        # a governor's own table is its setting's (V12_KAI), else its four ways' TOP table (Omni-Compass on top of it against it as
        # shipped); the other four-ways tables (ORCH, BARE, VS, BOTH) compare other pairs of arms and never stand as the governor's reading
        cands = [(max(ns), 0 if "_4W_" not in st else -1, -len(st), st) for st, ns in tables.items()
                 if any(k.upper() in st.split("_") for k in keys) and ("_4W_" not in st or st.endswith("_4W_TOP"))]
        if cands:
            n, _, _, st = max(cands)
            rc = XS.receipt(f"V{n}_{st}")
            # every row as written: the judged ones that moved, the STEADY ones (no difference beyond the noise) and the rows shown unjudged
            table = {"file": rc["file"], "title": rc["title"], "engine": f"omni-v{n}", "count": rc["count"],
                     "rows": ([{"g": x["g"], "abc": x["abc"], "w": x["w"], "r": x["r"]} for x in rc["rows"]]
                              + [{"g": x["g"], "abc": x["abc"], "w": "STEADY", "r": x.get("kind")} for x in rc["even"]]
                              + [{"g": x["g"], "abc": x["abc"], "w": "shown", "r": x["r"]} for x in rc["shown"]])[:60]}
        named = re.findall(r"docs/[A-Z0-9_]+_PREREGISTRATION\.md", test + " " + (r0["status"] if r0 else ""))
        pp = [ROOT / x for x in named if (ROOT / x).exists()]
        prereg = _prereg(pp[0]) if pp else None
        text = (r0["status"] if r0 else "") + " " + (pp[0].read_text(encoding="utf-8") if pp else "")
        rig = sorted({x for x in re.findall(r"(?:scripts|deploy/kind)/[\w./-]+\.(?:sh|py|ya?ml)", text) if (ROOT / x).exists() and own(x)})
        wfs = sorted({c["wf"] for c in camp.get(slug, [])} | {f for f in flows if pat.search(_norm(f[:-4]))})
        st0 = (r0["status"].lower() if r0 else "")
        stage = ("measured" if table else "candidate" if "candidate" in test or "candidate" in st0[:40] else
                 "built" if pp and (rig or wfs) else "under" if st0.startswith("under every") else "queued" if r0 else "none")
        fam_id, muscles = GP.CATALOG.get(slug, (None, []))
        fam = [c for c in cat if c["family_id"] == str(fam_id)]
        who = _owner(r0["bench"], pat) if r0 else {"repo": None, "owner": None, "licence": None}
        out.append({"key": slug.upper(), "name": name, "owner": who["owner"] or "—", "repo": who["repo"], "licence": who["licence"],
                    "role": field, "native": native, "test": test, "table": table, "stage": stage,
                    "settings": [{"key": k, "label": lb, "started": started.get(k) or {}} for k, lb in GP.settings_of(slug)],
                    "catalog": {"family": fam_id, "name": fam[0]["family"] if fam else None, "n": len(fam), "muscles": muscles},
                    "register": [{"n": r0["n"], "domain": r0["domain"], "bench": r0["bench"], "native": r0["native"], "lever": r0["lever"], "status": r0["status"]}] if r0 else [],
                    "prereg": prereg, "rig": rig, "workflows": wfs, "campaign": camp.get(slug, []), "four": four_ways(GP, slug)})
    return out


def orchestra() -> dict | None:
    """The orchestra, the eighth organism (tools/run_orchestra.py, results/orchestra/ORCHESTRA.md): every governor's catalog
    muscles as a body of its own and all of them together, native and with Omni-Compass on top, modelled (class S); each load's
    table as the file writes it, row by row, and the run that made it. None before its table is committed."""
    md, js = ROOT / "results" / "orchestra" / "ORCHESTRA.md", ROOT / "results" / "orchestra" / "ORCHESTRA.json"
    if not (md.exists() and js.exists()):
        return None
    run = json.loads(js.read_text(encoding="utf-8"))["run"]
    clean = lambda t: re.sub(r"\s+", " ", re.sub(r"\*\*|`", "", t)).strip()
    loads, cur = [], None
    for ln in md.read_text(encoding="utf-8").splitlines():
        if ln.startswith("## "):
            cur = {"title": clean(ln[3:]), "note": "", "head": [], "rows": []}; loads.append(cur)
        elif cur is not None and ln.startswith("|") and not re.match(r"\|\s*-", ln):
            cells = [clean(x) for x in ln.strip().strip("|").split("|")]
            if not cur["head"]:
                cur["head"] = cells
            else:
                cur["rows"].append(cells)
        elif cur is not None and ln.strip() and not cur["head"] and not cur["note"]:
            cur["note"] = clean(ln)
    loads = [x for x in loads if x["head"] and x["rows"]]
    # each body's row named by its governor (the file writes the bodies in the run's order, the orchestra last): checked by its
    # muscle count, else left unnamed
    slugs = list(run.get("bodies") or {})
    for x in loads:
        if x["head"][:2] == ["Body", "Muscles"] and len(x["rows"]) == len(slugs) and all(r[1] == str(len(run["bodies"][sl])) for r, sl in zip(x["rows"], slugs)):
            x["slugs"] = slugs
    title = clean(md.read_text(encoding="utf-8").splitlines()[0].lstrip("# "))
    return {"file": "results/orchestra/ORCHESTRA.md", "title": title, "engine": run.get("engine"), "commit": (run.get("commit") or "")[:12],
            "started": run.get("started"), "seeds": run.get("seeds"), "dial": run.get("dial"),
            "bodies": {k: len(v) for k, v in (run.get("bodies") or {}).items()}, "loads": loads}


def run_engines(started: dict) -> dict:
    """The engine each run ran on, so a table read at the build names its engine like every other: the run's commit from GitHub's
    run record (its head_sha) read by tools/omni_version.py --commit, as tools/confirm_abc.py reads it; where GitHub cannot be asked,
    the engine CHANGELOG.md records the run started on (the entry that names the run and says "started on omni-vN"); else none.
    {"engines": {"A": "omni-v13", ...}, "engine_from": {"A": "where it was read", ...}}"""
    log = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8") if (ROOT / "CHANGELOG.md").exists() else ""
    items = re.split(r"\n(?=- )", log)
    out, src = {}, {}
    for L, rid in sorted((started or {}).items()):
        eng = None
        try:
            sha = subprocess.run(["gh", "api", f"repos/{REPO}/actions/runs/{rid}", "--jq", ".head_sha"], capture_output=True, text=True,
                                 cwd=ROOT, timeout=60).stdout.strip()
            if re.fullmatch(r"[0-9a-f]{40}", sha):
                v = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py"), "--commit", sha], cwd=ROOT,
                                   capture_output=True, text=True, timeout=120).stdout
                m = re.search(r"\b(omni-v\d+)\b", v)
                if m:
                    eng, src[L] = m.group(1), f"GitHub's run record (commit {sha[:12]}), read by tools/omni_version.py"
        except (OSError, subprocess.SubprocessError):
            pass                                            # GitHub not reachable from here: the repository's own record below
        if eng is None:
            for it in items:
                m = re.search(r"started on (omni-v\d+)", it) if str(rid) in it else None
                if m:
                    eng, src[L] = m.group(1), "CHANGELOG.md, its entry naming the run as started on that engine"
                    break
        out[L] = eng
    return {"engines": out, "engine_from": src}


def four_ways_from_runs(GP, system: str, started: dict) -> dict:
    """{way: receipt} for one system's four ways read at the build from its three runs' own scored files on the branch raw
    (each run's live-reps/LIVE_REPS.json and its arms' preflight.txt, byte for byte) by the repository's own three-run tool
    (tools/confirm_abc.py --pair), for the ways whose table the repository has not written yet; each run's repetitions as its
    own file counts them. Empty where a run's files are not on the branch raw."""
    import export_runs as XR
    import export_scenarios as XS
    if sorted(started) != ["A", "B", "C"]:
        return {}
    ref, pre = XR.raw_ref()
    out = {}
    with tempfile.TemporaryDirectory() as td:
        t, dirs, reps = Path(td), [], {}
        for L in "ABC":
            rid = str(started[L]); base = f"{pre}run-{rid}"
            names = [x for x in git("ls-tree", "-r", "--name-only", ref, base).splitlines() if x.endswith(("live-reps/LIVE_REPS.json", "/preflight.txt"))]
            if not any(x.endswith("LIVE_REPS.json") for x in names):
                return {}
            for x in names:
                p = t / x[len(pre):]; p.parent.mkdir(parents=True, exist_ok=True)
                p.write_bytes(subprocess.run(["git", "-C", str(ROOT), "show", f"{ref}:{x}"], capture_output=True).stdout)
            lr = json.loads((t / f"run-{rid}" / "live-reps" / "LIVE_REPS.json").read_text(encoding="utf-8").replace("NaN", "null"))
            reps[L] = len(next(iter((lr.get("repetitions") or {}).values()), []) or [])
            dirs.append(str(t / f"run-{rid}"))
        # the tool's engine line asks GitHub for each run's commit; the rows do not depend on it, so the tool is not let ask it, and
        # each run's engine is read once here instead (run_engines), so the table names the engine its runs ran on
        engines = run_engines(started)
        nogh = t / "nogh"; nogh.mkdir(); (nogh / "gh").write_text("#!/bin/sh\nexit 1\n"); (nogh / "gh").chmod(0o755)
        env = dict(os.environ, PATH=f"{nogh}:{os.environ.get('PATH', '')}")
        for tag, arms, label in GP.FOUR_WAYS:
            if (ROOT / "results" / "live" / f"V12_{system.upper()}_4W_{tag}.md").exists():
                continue
            md = t / f"{tag}.md"
            subprocess.run([sys.executable, str(ROOT / "tools" / "confirm_abc.py"), f"{system}, {label}", *dirs, "--pair", arms, "--out", str(md)],
                           capture_output=True, text=True, cwd=ROOT, env=env, timeout=600)
            if md.exists():
                rc = XS.receipt(md.stem, md)
                out[tag] = {"file": None, "count": rc["count"], "rows": [{"g": x["g"], "abc": x["abc"], "w": x["w"]} for x in rc["rows"]],
                            "read": "at the build, from runs A, B and C's own scored files on the branch raw, by tools/confirm_abc.py --pair; the repository's own table is not yet written",
                            "reps": reps} | engines
    return out


def four_ways(GP, slug: str) -> list:
    """The governor's four ways (docs/BATCH_QUEUE_PREREGISTRATION.md, amendment 6; tools/governors_page.py FOUR_WAYS): for each of
    its systems, the A, B and C started (results/live/governors_runs.json, <system>4) and each comparison's three-run table
    (V12_<SYSTEM>_4W_<TAG>.md) with its counts, or None while its runs are still to finish."""
    import export_scenarios as XS
    keys = {k for k, _ in GP.settings_of(slug)} | {slug}
    started = json.loads(GP.RUNS.read_text(encoding="utf-8")) if GP.RUNS.exists() else {}
    out = []
    for system, name in getattr(GP, "FOUR_SYSTEMS", ()):
        if system not in keys:
            continue
        ways, read = [], four_ways_from_runs(GP, system, started.get(f"{system}4") or {})
        for tag, arms, label in GP.FOUR_WAYS:
            stem = f"V12_{system.upper()}_4W_{tag}"
            t = read.get(tag)
            if (ROOT / "results" / "live" / f"{stem}.md").exists():
                rc = XS.receipt(stem)
                t = {"file": rc["file"], "count": rc["count"], "rows": [{"g": x["g"], "abc": x["abc"], "w": x["w"]} for x in rc["rows"]]}
            ways.append({"tag": tag, "arms": arms, "label": label, "table": t})
        out.append({"system": system, "name": name, "started": started.get(f"{system}4") or {}, "ways": ways})
    return out


def register_places(limit: bool = True) -> list:
    """Every open benchmark still to run, in the register's own order (docs/REGISTER.md, section 4): its domain, the open
    benchmark and its owner, the native it runs on top of, Omni-Compass's lever and its status, each as the register writes it
    (markdown stripped), so the benefit board lays out every place that is supposed to be there before its result exists."""
    reg = ROOT / "docs" / "REGISTER.md"
    if not reg.exists():
        return []
    text = reg.read_text(encoding="utf-8")
    sec = text[text.find("## 4."):] if "## 4." in text else ""
    sec = sec[:sec.find("\n## ", 5)] if "\n## " in sec[5:] else sec
    clean = lambda t: plain(re.sub(r"\s+", " ", re.sub(r"\*\*|`|\[([^\]]*)\]\([^)]*\)", lambda m: m.group(1) or "", t)).strip())
    out = []
    for ln in sec.splitlines():
        if not re.match(r"\|\s*\d+\s*\|", ln):
            continue
        c = [clean(x) for x in ln.strip().strip("|").split("|")]
        if len(c) >= 6:
            cut = (lambda x, n: x[:n]) if limit else (lambda x, n: x)
            out.append({"n": int(c[0]), "domain": c[1], "bench": cut(c[2], 220), "native": cut(c[3], 160), "lever": cut(c[4], 120), "status": cut(c[5], 260)})
    return out


def dial() -> dict:
    """The heartbeat dial (omni-v17): every beat of the Kubernetes governor read in our own models, from the newest ladder
    tools/beat_ladder.py wrote (results/model_gate/V<n>_LADDER.json), without its per-seed records; the real runs' place from
    the pace entry's three-run tables once they exist (results/live/V<n>_PACE*.md). Empty until a ladder exists."""
    lads = sorted((ROOT / "results" / "model_gate").glob("V*_LADDER.json"), key=lambda f: int(re.sub(r"\D", "", f.stem) or 0))
    if not lads:
        return {}
    lad = json.loads(lads[-1].read_text(encoding="utf-8"))
    pace = sorted((ROOT / "results" / "live").glob("V*_PACE*.md"))
    eng_of = _ladder_engines(lad)
    standing = engine()[0]
    newest = max((e for e in eng_of.values() if e), key=lambda e: int(e.split("-v")[1]), default=None)
    return {"file": str(lads[-1].relative_to(ROOT)), "seeds": lad["seeds"], "days": lad["days"], "main_s": lad["main_s"],
            "real": ("three-run tables in " + ", ".join(f"results/live/{f.name}" for f in pace)) if pace else
                    "not yet run (docs/PACE_PREREGISTRATION.md, amendment 3: eight arms in every repetition, three runs)",
            # the engine each beat was read on, from the ladder's own sources (the first source that holds a beat gives it, as
            # tools/beat_ladder.py merges them), and what the governor's files changed between the newest of them and the engine that
            # stands, read from the two fingerprints: a row is its own engine's, never read as the engine that stands's
            "engine_of_beat": eng_of, "standing": standing,
            "since": _engine_change(newest, standing, ("omni_controller/", "omnicompass/")) if newest else None,
            "newer_60": _newer_pace(lad),
            # the page's key is "models" (the editing seat of 24 October: the retired word is printed nowhere); the ladder file keeps its own
            "models": _clean({k: {"setting": t["setting"], "beats": t["beats"], "native": t["native"], "rows": t["rows"]}
                              for k, t in (lad.get("models") or lad.get("models") or {}).items()})}   # a change against a zero (native's power cap) is NaN: null


def _ladder_engines(lad: dict) -> dict:
    """{beat: engine} read from the ladder's own sources: a model-gate record by its candidate's engine, a run described in words by
    the engine it names ("on omni-vN") and its --pace-periods; the first source that holds a beat gives it, as tools/beat_ladder.py
    merges its reports (the first report holding a beat keeps it)."""
    out = {}
    for src in lad.get("sources") or []:
        eng, beats = None, set()
        f = ROOT / src
        if src.endswith(".json") and f.exists():
            r = json.loads(f.read_text(encoding="utf-8"))
            eng = r.get("cand_engine") if re.fullmatch(r"omni-v\d+", str(r.get("cand_engine") or "")) else None
            for t in (r.get("models") or {}).values():
                beats |= {k for k in (t.get("per_seed") or {}) if k != "native"}
        else:
            m = re.search(r"\bon (omni-v\d+)", src)
            eng = m.group(1) if m else None
            pm = re.search(r"--pace-periods ([\d,.]+)", src)
            beats = set(pm.group(1).split(",")) if pm else set()
        for b in beats:
            out.setdefault(f"{float(b):g}", eng)
    return out


def _engine_change(old: str, new: str, prefixes: tuple) -> dict | None:
    """The files under the given prefixes that changed, or were added, between two engines' fingerprints (OMNI_V<n>.json)."""
    def files(name):
        f = ROOT / f"OMNI_V{name.split('-v')[-1]}.json"
        if not f.exists():
            return None
        d = json.loads(f.read_text(encoding="utf-8")).get("files") or {}
        return d if isinstance(d, dict) else {x["path"]: x.get("sha256") for x in d}
    a, b = files(old), files(new)
    if a is None or b is None or old == new:
        return None
    keep = lambda k: k.startswith(prefixes)
    return {"from": old, "to": new, "changed": sorted(k for k in a if k in b and a[k] != b[k] and keep(k)),
            "added": sorted(k for k in b if k not in a and keep(k))}


def _newer_pace(lad: dict) -> dict | None:
    """The newest pace record of the model gate (results/model_gate/V<n>_PACE.json) newer than every source of the ladder: its
    decision every 60 s against native on the same seeds, setting by setting, read as its record writes it (its candidate's own words,
    its base engine), so the dial's 60 s row stands beside the newer reading of the same beat, never replaced by it."""
    srcs = [s for s in (lad.get("sources") or []) if s.endswith(".json")]
    top = max((int(m.group(1)) for s in srcs for m in [re.search(r"V(\d+)_", s)] if m), default=0)
    paces = sorted(((int(re.match(r"V(\d+)_", f.name).group(1)), f) for f in (ROOT / "results" / "model_gate").glob("V*_PACE.json")), key=lambda x: x[0])
    paces = [(n, f) for n, f in paces if n > top]
    if not paces:
        return None
    n, f = paces[-1]
    r = json.loads(f.read_text(encoding="utf-8"))
    if [int(s) for s in r.get("seeds") or []] != [int(s) for s in lad.get("seeds") or []]:
        return None
    return _clean({"file": str(f.relative_to(ROOT)), "candidate": r.get("cand_engine"), "base": r.get("base_engine"), "days": r.get("days"),
                   "models": {k: {g: {"value": v.get("ref"), "native": v.get("native"), "vs_native": v.get("ref_vs_native")}
                                  for g, v in (t.get("reference_rows") or {}).items()}
                              for k, t in (r.get("models") or {}).items() if float(t.get("reference") or 0) == float(lad.get("main_s") or 60)}})


def core_mc() -> dict:
    """The Python's Monte Carlo (benchmarks/core_evidence.py, the founder's words of 24 October: "the Python's Monte Carlo, our 4K
    Runge-Kutta, 20-step macro, 10-step micro in each macro ... how each Python run comes out and starts at zero, and how long in
    steps OmniCompass gets it into the basin and holds it there and certifies the count"): the canonical 500-run population
    (numpy's generator from seed 223387268, the record's own), each run through omnicompass/core.simulate, 20 macro steps of
    10 RK4 micro steps, in four variants (controlled; uncontrolled, u = 0; aimed at the wrong basin; the double well's mu at 0).
    Kept per run: U at every macro step (three decimals), the macro step its five-in-a-row in the basin completes (convey) and
    its ten-in-a-row (cert), and its basin; the counts beside the record's (results/core_evidence.json), one SHA-256 digest of
    the paths. Class S, the engine's own mathematics."""
    import hashlib
    from dataclasses import replace
    import numpy as np
    from omnicompass import core as C
    seed, runs = 223387268, 500
    rng = np.random.default_rng(seed)
    pop = [(C.sample_state(rng), C.sample_params(rng)) for _ in range(runs)]
    rec = json.loads((ROOT / "results" / "core_evidence.json").read_text(encoding="utf-8"))
    out = {}
    for name in ("controlled", "uncontrolled", "wrong_target", "controlled_mu0"):
        U, cv, ce, tg = [], [], [], []
        for x0, p in pop:
            pp = replace(p, mu=0.0) if name == "controlled_mu0" else p
            tgt = -C.nearest_basin_sign(x0.U) if name == "wrong_target" else None
            r = C.simulate(x0, pp, target=tgt, controlled=(name != "uncontrolled"))
            U.append([round(float(u), 3) for u in r.U_hist]); cv.append(int(r.convey_confirm) if r.convey else 0)
            ce.append(int(r.cert_complete) if r.cert else 0); tg.append(int(r.target_sign))
        out[name] = {"U": U, "convey": cv, "cert": ce, "target": tg, "n_convey": sum(1 for c in cv if c), "n_cert": sum(1 for c in ce if c),
                     "record": {"convey5": (rec.get(name) or {}).get("convey5"), "cert10": (rec.get(name) or {}).get("cert10")},
                     "digest": hashlib.sha256(json.dumps(U, separators=(",", ":")).encode()).hexdigest()}
    return {"seed": seed, "runs": runs, "macro": C.MACRO_STEPS, "micro": C.MICRO_STEPS, "dt": C.MACRO_DT, "tol": C.BASIN_TOL,
            "convey_window": C.CONVEY_WINDOW, "cert_window": C.CERT_WINDOW, "kp": C.KP, "file": "results/core_evidence.json",
            "tool": "benchmarks/core_evidence.py", "variants": out, "sets": core_sets()}


def core_sets() -> list:
    """Every set of the core's Monte Carlo that tools/core_runs.py has written from the jump generator (results/core_runs/), oldest
    first: its base, runs, digest and counts, the C++ twin's digest of the same draws, the system it ran (none: the engine's own
    ranges) and the GitHub run that wrote it, so a set the page runs is checked against the Python's and the C++'s."""
    out = []
    for f in sorted((ROOT / "results" / "core_runs").glob("CORE_RUNS_*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        c = d.get("cpp") or {}   # the C++ twin of the core on the same draws (cpp/tools/core_runs.cpp), and the system they were spread over
        out.append({"base": d.get("base"), "runs": d.get("runs"), "digest": d.get("digest"), "summary": d.get("summary"), "file": str(f.relative_to(ROOT)),
                    "written": d.get("written", ""), "github": (d.get("github") or {}).get("url"), "system": (d.get("system") or {}).get("name"),
                    "cpp": c.get("digest"), "cpp_agree": f"{c['agree']} of {c['of']}" if "agree" in c else None, "cpp_largest": c.get("largest_difference"),
                    "inputs": d.get("inputs_digest")})
    return sorted(out, key=lambda x: (x["written"], x["file"]))


ON_NATIVE_PAIR = "Omni on native against native"


def on_native_what(path: Path, d: dict) -> str:
    """Omni-Compass on native against native, in the record's own words: its 'what' after its lead ("three runs on GitHub's own
    machines ..., the full form: <steps> of <length>, clients ...") and native as its .md says it ("Native is ...;")."""
    w = str(d.get("what") or "")
    m = re.search(r"(three runs on GitHub.*)$", w)
    form = m.group(1) if m else w
    md = path.with_suffix(".md")
    nat = re.search(r"Native is (.+?);", md.read_text(encoding="utf-8")) if md.exists() else None
    return (f"Omni-Compass on native against native, {form.rstrip('.')}" + (f"; native is {nat.group(1)}, and Omni-Compass sits on top of it." if nat else "."))


def on_native_abc() -> dict:
    """The newest real three-run test on GitHub's own machines of Omni-Compass on native against native, the page's bottom line
    (results/orchestrator/*_THREE_ARMS_ABC.json, tools/orchestrator_abc.py, class L): native is Kubernetes' published autoscaling
    rule on the muscles, Omni-Compass on native is Omni-Compass on top of that rule. Only that pair and those two arms are carried:
    Omni-Compass is never by itself (the founder's order of 25 October), so the file's other arm stays in its file."""
    fs = sorted(ROOT.glob("results/orchestrator/*_THREE_ARMS_ABC.json"), key=lambda f: (int(re.search(r"V(\d+)_", f.name).group(1)) if re.search(r"V(\d+)_", f.name) else 0, f.name))
    if not fs:
        return {}
    d = json.loads(fs[-1].read_text(encoding="utf-8"))
    return {"file": str(fs[-1].relative_to(ROOT)), "class": d.get("class"), "commit": d.get("commit"), "engine": d.get("engine"),
            "runs": d.get("runs"),
            # the test as its record describes it, never typed here (the referee of 30 October): the record's own form (its steps, their
            # length, the clients) after its lead, and native's words from the record's own .md, the same ones tools/headline.py reads
            "what": on_native_what(fs[-1], d),
            "rows": [r for r in d.get("rows", []) if r.get("pair") == ON_NATIVE_PAIR],
            "totals": {k: {a: v.get(a) for a in ("yardstick", "omni_native") if a in v} for k, v in (d.get("totals") or {}).items()}}


def scenarios20() -> dict:
    """The twenty scenarios (results/scenarios/SCENARIOS_20.json, tools/scenarios_20.py, class S): ten organisms, each native and with
    Omni-Compass on native, every gauge's word and its three runs; the plants each reading flags stay in the record, not here."""
    f = ROOT / "results" / "scenarios" / "SCENARIOS_20.json"
    if not f.exists():
        return {}
    d = json.loads(f.read_text(encoding="utf-8"))
    def pair(p):
        if not isinstance(p, dict) or "gauges" not in p:
            return p
        return {"gauges": {k: {"word": g.get("word"), "reading": g.get("reading"), "mean": g.get("mean_change"),
                               "runs": {r: (v or {}).get("change") for r, v in (g.get("runs") or {}).items()}} for k, g in p["gauges"].items()}}
    orgs = []
    for o in d.get("organisms", []):
        x = {k: o.get(k) for k in ("no", "key", "name", "what", "class", "muscles", "source")}
        x["what"] = plain(x["what"]) if isinstance(x["what"], str) else x["what"]
        r = o.get("readings") or {}
        on = r.get("on_native_vs_native") if isinstance(r, dict) else None
        if isinstance(on, dict) and on.get("state") == "composed":   # the whole organism: its composition, the headline scope only
            wh = (((on.get("composition") or {}).get("scopes") or {}).get("without") or {}).get("carried", {}).get("whole", {})
            x["composed"] = {"index": wh.get("index"), "gauges": wh.get("gauges"), "note": "the whole organism in its three places, composed by tools/whole_system.py"}
        else:
            x["readings"] = {k: pair(v) for k, v in r.items()}
        orgs.append(x)
    return {"file": str(f.relative_to(ROOT)), "title": d.get("title"), "run": d.get("run"), "gauges": d.get("gauges"), "organisms": orgs}


def injection_grid() -> dict:
    """The injection grid (results/injection_grid/INJECTION_GRID_<base>.json, tools/injection_grid.py, class S): the Python's
    newest 500 injections through every organism, native and with Omni-Compass on native, and through every governor on each
    organism, at 1, 10, 100 and 500 runs and organisms stacked. The page carries every cell, every run's means (from which it
    recomputes every cell's mean and checks the Python's) and the batch's Python and C++ digests; the ranking it computes."""
    fs = [f for f in (ROOT / "results" / "injection_grid").glob("INJECTION_GRID_*.json") if "_look_" not in f.name]
    if not fs:
        return {}
    f = max(fs, key=lambda f: (json.loads(f.read_text(encoding="utf-8")).get("run", {}).get("started", ""), f.name))
    d = json.loads(f.read_text(encoding="utf-8").replace('"EVEN"', '"STEADY"').replace('"EVEN, ', '"STEADY, '))   # the grid's tool still writes EVEN, as a word and at the head of each reading; the page shows its name now, STEADY
    if isinstance(d.get("rule"), str):
        d["rule"] = plain(d["rule"])
    d.pop("best", None)
    return {"file": str(f.relative_to(ROOT)), **d}


def _wrote(path: Path) -> dict | None:
    """The commit that last wrote a file, its time and its parents (a merge has two: the second is the branch it merged)."""
    try:
        sha, when, parents = git("log", "-1", "--format=%H%x09%cI%x09%P", "--", str(path.relative_to(ROOT))).split("\t")
    except ValueError:
        return None
    return {"commit": sha, "at": when, "parents": parents.split()}


def verdict_audit() -> dict:
    """The verdict audit (tools/verdict_audit.py; the referee's work order of 25 October): every row of every three-run table
    recomputed from its stored native and Omni-Compass values, every count from one selection, and the discrepancy report
    against the tables as they were (results/verdict_audit/DISCREPANCIES.json)."""
    import sys as _s
    _s.path.insert(0, str(ROOT))
    from tools.verdict_audit import build as audit_build, digest as audit_digest, loss_rows
    from tools.loss_ledger import cause as ledger_cause
    rec = audit_build()
    by_t = {t["stem"]: t for t in rec["tables"]}
    r4 = lambda x: None if x is None else round(x, 4)

    def ledger_gauge(r, t):
        """The gauge as docs/LOSS_LEDGER.md names it (tools/loss_ledger.py build): its section first where the table has one."""
        where = (f"workload {r['section']} / " if t["stack"] == "Linux services" else f"{r['section']} / ") if r["section"] else ""
        return where + r["gauge"]

    def row(r, cz=False):
        t = by_t[r["table"]]
        out = {"t": r["table"], "f": t["file"], "e": t["engine"], "c": t["class"], "s": r["section"], "g": r["gauge"],
               "d": r["direction"], "w": r["word"], "rd": r["stored"],
               "runs": [[r4(x.get("native")), r4(x.get("omni")), r4(x.get("raw_pct")), r4(x.get("raw_unit")), bool(x.get("clear"))]
                        for x in r["runs"]], "ev": r.get("evidence")}
        if cz:   # the LOSS ledger's own cause, page, fix and what decides it (tools/loss_ledger.py CAUSES), never composed on the page
            c = ledger_cause(t["stem"].split("_", 1)[1], ledger_gauge(r, t))
            out["cz"] = list(c) if c else None
        return out
    disc = ROOT / "results" / "verdict_audit" / "DISCREPANCIES.json"
    dd = json.loads(disc.read_text(encoding="utf-8")) if disc.exists() else {"rows": []}
    kinds = {}
    for d in dd["rows"]:
        for k in d["kinds"]:
            kinds.setdefault(k, {"standing": 0, "all": 0})
            kinds[k]["all"] += 1
            kinds[k]["standing"] += d["status"] == "standing"
    return {"file": "results/verdict_audit/VERDICT_AUDIT.md", "digest": audit_digest(rec), "engine_standing": rec["engine_standing"],
            "rule": rec["rule"], "exact_rel": rec["exact_rel"], "floor": rec["floor"], "counts": rec["counts"],
            "tables": [{k: t[k] for k in ("stem", "file", "engine", "status", "comparison", "stack", "class", "on_the_engine_that_stands")}
                       | {"runs": [[x.get("tag"), x.get("run"), x.get("paired_repetitions"), str(x.get("commit") or "")[:12]] for x in t["runs"]]}
                       for t in rec["tables"]],
            "losses": [row(r, cz=True) for r in loss_rows(rec)],
            # the LOSS rows of the other three comparisons of the standing tables (docs/LOSS_LEDGER.md, its second and third parts):
            # in place of a controller (VS), the orchestrator's own (ORCH) and two changes at once (BOTH), each with its comparison
            "losses_apart": [row(r) | {"k": by_t[r["table"]]["comparison"]} for r in rec["rows"]
                             if r["word"] == "LOSS" and by_t[r["table"]]["status"] == "standing" and by_t[r["table"]]["comparison"] != "against its native"],
            "armada": [row(r) for r in rec["rows"] if r["table"] == "V12_ARMADA_4W_BARE" and r["word"] in ("LOSS", "GAIN", "power given")],
            # the report names its base as the tool was given it; where that is a moving name (origin/main), the commit that wrote the
            # report and that commit's parents are recorded beside it, so the comparison can be traced (the referee of 31 October)
            "discrepancies": {"base": dd.get("base"), "written_in": _wrote(disc), "kinds": kinds, "rows": len(dd["rows"]),
                              "words": [{k: (re.sub(r"\bEVEN\b", "STEADY", d[k]) if k == "old_reading" else d[k]) for k in ("table", "status", "gauge", "old_reading", "new_reading")}
                                        for d in dd["rows"] if d["word_changed"]]}}   # the old word EVEN is shown as STEADY, its name now (counted apart as "renamed")


def glossary() -> dict:
    """The glossary and index at the back of the page (tools/live_glossary.py, docs/engine/glossary.json): every term in the words of
    the file it names, the ten organisms, the two arms and their twenty scenarios, every muscle of the catalog, and the index."""
    f = ROOT / "docs" / "engine" / "glossary.json"
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}


def field() -> dict:
    """The ones that compete, as docs/THE_FIELD.md ranks them (section 3i's table, the referee of 31 October: never typed into the
    page): the five it names to run first, each with the ranked table's reason, rig and cost as that file reads them, the day the
    file was read, and whether results/ holds a table that names the product (none yet: "not yet run")."""
    f = ROOT / "docs" / "THE_FIELD.md"
    if not f.exists():
        return {"missing": "docs/THE_FIELD.md"}
    text = f.read_text(encoding="utf-8")
    read = re.search(r"Read on (\d{1,2} \w+ \d{4})", text)
    rows = {}
    for line in text.splitlines():
        m = re.match(r"\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$", line)
        if m:
            rows[m.group(2)] = {"rank": int(m.group(1)), "product": m.group(2), "why": m.group(3), "rig": m.group(4), "cost": m.group(5), "free": m.group(6)}
    first = []
    part = text.split("**The first five to run**", 1)
    for m in re.finditer(r"^\d+\.\s+\*\*(.+?)\*\*:\s*(.+?)(?=^\d+\.|^\s*$)", part[1] if len(part) > 1 else "", re.M | re.S):
        name = next((p for p in rows if m.group(1).startswith(p)), None)
        if name is None:
            continue
        slug = re.sub(r"[^a-z0-9]+", "", name.lower())
        hits = sorted(str(x.relative_to(ROOT)) for x in (ROOT / "results").rglob("*.md") if slug and slug in re.sub(r"[^a-z0-9]+", "", x.stem.lower()))
        first.append(dict(rows[name], plan=m.group(1), first=" ".join(m.group(2).split()), tables=hits))
    return {"file": "docs/THE_FIELD.md", "read": read.group(1) if read else None, "first": first}


LAW_SCOPE = ("omni_controller/*.py", "omni_orchestrator/*.py", "realms/*.py", "tools/run_*.py")


def law_wires() -> dict:
    """Every governor wire that builds the compass law (omnicompass/compass_law.py CompassLaw), read from its source at the build:
    the file and line, whether it multiplies k_d by three after building it (`<law>.kd *= 3`), sets k_d itself, or keeps the class's
    critical damping, and its velocity smoothing s (a literal, a module constant resolved from the same file, or the class default).
    Nothing typed: the page's words on k_d and s are this list, so a wire changed in the repository changes them at the next build."""
    law_src = (ROOT / "omnicompass" / "compass_law.py").read_text(encoding="utf-8")
    m = re.search(r"^\s*smooth:\s*float\s*=\s*([0-9.]+)", law_src, re.M)
    default_s = float(m.group(1)) if m else None
    num = r"-?[0-9]+(?:\.[0-9]+)?"
    out = []
    files = sorted({p for pat in LAW_SCOPE for p in ROOT.glob(pat)})
    for p in files:
        src = p.read_text(encoding="utf-8")
        if "CompassLaw(" not in src:
            continue
        lines = src.split("\n")
        consts = {}
        for ln in lines:                                     # module constants: NAME = 1.0, or NAME_A, NAME_B = 1.0, 0.5
            mm = re.match(r"^([A-Z_][A-Z0-9_]*(?:\s*,\s*[A-Z_][A-Z0-9_]*)*)\s*=\s*(" + num + r"(?:\s*,\s*" + num + r")*)\s*(?:#.*)?$", ln)
            if mm:
                for k, v in zip(re.split(r"\s*,\s*", mm.group(1)), re.split(r"\s*,\s*", mm.group(2))):
                    consts[k] = float(v)
        for i, ln in enumerate(lines):
            if "CompassLaw(" not in ln or re.match(r"\s*(class|from|import|#)", ln):
                continue
            j, depth, call = ln.index("CompassLaw(") + len("CompassLaw("), 1, ""
            text, k = ln, i
            while depth and k < len(lines):
                seg = text[j:] if k == i else lines[k]
                for ch in seg:
                    if ch == "(":
                        depth += 1
                    elif ch == ")":
                        depth -= 1
                        if not depth:
                            break
                    call += ch
                if depth:
                    k += 1
                    call += " "
            lhs = ln.split("CompassLaw(")[0]
            var = re.search(r"([\w.]+)\s*=\s*(?:[\w.]+\.)?$", lhs.strip())
            var = var.group(1) if var else None
            tail = "\n".join(lines[k + 1:k + 7])
            tripled = bool(var) and re.search(re.escape(var.split(".")[-1]) + r"\.kd\s*\*=\s*3(?:\.0)?\b", tail) is not None
            kd_arg = re.search(r"\bkd\s*=\s*([^,)]+)", call)
            sm = re.search(r"\bsmooth\s*=\s*([\w.]+)", call)
            if sm:
                e = sm.group(1); sv = float(e) if re.fullmatch(num, e) else consts.get(e.split(".")[-1])
                s_src = "literal" if re.fullmatch(num, e) else (f"{e}, the module's constant" if sv is not None else f"{e}, not resolved")
            else:
                sv, s_src = default_s, "the class default"
            out.append({"file": str(p.relative_to(ROOT)), "line": i + 1, "law": var,
                        "kd": "x3" if tripled else (f"set: {kd_arg.group(1).strip()}" if kd_arg else "critical"),
                        "smooth": sv, "smooth_from": s_src})
    return {"law": "omnicompass/compass_law.py", "default_smooth": default_s, "scope": list(LAW_SCOPE), "wires": out}


def records(runs: bool) -> dict:
    import export_controller_trace as XC
    import export_harness_trace as XH
    import export_scenarios as XS
    import export_whole as XW
    import export_gpu_run as XG
    import export_cpu_model as XCPU
    import export_grafana as XGF
    import export_heldout as XHO
    import export_cpp_twins as XT
    now = lambda: datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    # GitHub is read first: the ledger fetches the commit of every run it lists that the checkout lacks, and the runs' serial
    # numbers below (export_runs.py serial: the full commit, where git knows it) must be read on the commits the build leaves
    # behind, the same ones its --check reads them on; read after them, the check found commits the build had not
    gh = github_runs() if runs else None
    runs_read_at = now() if gh is not None else None
    camp = campaign_reading() if gh is not None else None      # the campaign's runs, read with the run list
    if gh is None and runs and not CHECKING and LEDGER_CACHE.exists():
        # no token here: the list of running and queued runs kept beside the ledger (its "now", read through GitHub's API by
        # whoever refreshed the cache), shown with its own reading time, never under this build's
        kept = (json.loads(LEDGER_CACHE.read_text(encoding="utf-8")).get("now") or {})
        if kept.get("read_at") and isinstance(kept.get("runs"), list):
            gh, runs_read_at = kept["runs"], kept["read_at"]
    led = None if CHECKING else ledger(camp)   # a check never reads GitHub: the ledger is a GitHub reading, compared by its own read time
    with tempfile.TemporaryDirectory() as td:
        t = Path(td)
        import export_runs as XR
        # every compass law the runs below wire is recorded as it runs, then fed through the C++ twin (export_cpp_twins.py)
        with XT.LawRecorder() as laws:
            XH.main(str(t / "h.json")); XC.main(str(t / "c.json")); XS.main(str(t / "s.json"))
        XR.main(str(t / "r.json")); XW.main(str(t / "w.json"))
        XG.main(str(t / "g.json")); XCPU.main(str(t / "cpu.json")); XHO.main(str(t / "ho.json"))
        # the Python's runs (tools/engine_runs.py): the newest record, for the page to run the same runs and compare
        er_files = sorted((ROOT / "results" / "engine_runs").glob("ENGINE_RUNS_*.json"),     # the newest written last, whatever its base
                          key=lambda f: (json.loads(f.read_text(encoding="utf-8")).get("written", ""), f.name))
        eruns = json.loads(er_files[-1].read_text(encoding="utf-8")) if er_files else {"missing": "results/engine_runs"}
        if er_files:
            eruns["file"] = str(er_files[-1].relative_to(ROOT))
            # every set the Python has run (the founder's words of 23 October: "running it again runs another 500 and again another
            # 500"): its base, its runs and its digest, so a set run again on the page is checked against the Python's own record
            eruns["sets"] = sorted(({"base": d.get("base"), "runs": d.get("runs"), "digest": d.get("digest"), "file": str(f.relative_to(ROOT)),
                                     "written": d.get("written", "")} for f in er_files for d in [json.loads(f.read_text(encoding="utf-8"))]),
                                   key=lambda x: (x["written"], x["file"]))
        # the same record's set through the C++ engine at this build (cpp/tools/engine_runs.cpp), receipt by receipt
        XT.main(str(t / "x.json"), live_laws=laws.laws, engine_runs=eruns if er_files else None)
        h, c, s, rr, wh, gpu, cpu, ho, x = (json.loads((t / f).read_text(encoding="utf-8")) for f in
                                           ("h.json", "c.json", "s.json", "r.json", "w.json", "g.json", "cpu.json", "ho.json", "x.json"))
        # the monitor registry with the wall's Grafana dashboard (written to deploy/grafana/omni-compass-wall.json by the build, read back by a check)
        reg = json.loads((HERE / "monitors.json").read_text(encoding="utf-8"))
        reg["grafana"] = XGF.main(str(t / "wall.json")) if CHECKING else XGF.main()
    name, digest = engine()
    from tools.readings import SIZE_FLOOR
    build = {"engine": name, "digest": digest, "commit": git("rev-parse", "HEAD"), "floor": SIZE_FLOOR,
             "built_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
             "realms_engine": s["realms"]["run"]["engine"], "receipts_engines": sorted({r["engine"] for r in s["receipts"]}),
             # GitHub's running and queued runs, with the moment they were read; None where this build did not read them (no token)
             "runs": gh or [], "runs_read_at": runs_read_at}
    build["board"] = board(build["runs"], camp)
    build["ledger"] = led
    return {"harness": h, "ctlrec": pack_controller(c), "scen": s, "runs": rr, "fleet": fleet(), "build": build, "whole": wh,
            "gpurun": gpu, "cpuhost": cpu, "monitors": reg, "engineruns": eruns, "heldout": ho, "cpptwin": x,
            "beatsweep": beat_sweep(), "dial": dial(), "coremc": core_mc(), "onnative": on_native_abc(), "scenarios": scenarios20(), "injgrid": injection_grid(), "audit": verdict_audit(), "glossary": glossary(),
            "lawwires": law_wires(), "field": field()}


def embedded(page: str, key: str):
    tag = f'<script type="application/json" id="{key}">'
    if tag not in page:
        return None
    a = page.index(tag) + len(tag)
    return json.loads(page[a:page.index("</script>", a)])


def first_difference(a, b, path="$"):
    """The first place two records differ, as (path, a's value, b's value) cut short, or None where they are equal."""
    if a == b:
        return None
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b), key=str):
            if k not in a or k not in b:
                return f"{path}.{k}", repr(a.get(k, "<absent>"))[:120], repr(b.get(k, "<absent>"))[:120]
            d = first_difference(a[k], b[k], f"{path}.{k}")
            if d:
                return d
    elif isinstance(a, list) and isinstance(b, list):
        for i, (x, y) in enumerate(zip(a, b)):
            d = first_difference(x, y, f"{path}[{i}]")
            if d:
                return d
        if len(a) != len(b):
            return f"{path} (length)", str(len(a)), str(len(b))
    return path, repr(a)[:120], repr(b)[:120]


def stamp_fallbacks(page: str, build: dict) -> str:
    """What a reader sees where the page's script does not run (the referee of 30 October): every element of the page's markup
    marked data-rec="build.engine" or data-rec="build.digest" carries the build record's own value, and the engine's two files
    (engJson, engDoc) their names, so no older engine is printed even before the script fills them. Only the markup before the
    first script is touched; the records and the engine's code are never rewritten here."""
    import html as _html
    cut = page.find("<script")
    cut = len(page) if cut < 0 else cut
    head, tail = page[:cut], page[cut:]
    head = re.sub(r'(<[^<>]*\bdata-rec="build\.(engine|digest)"[^<>]*>)[^<]*(?=<)',
                  lambda m: m.group(1) + _html.escape(str(build.get(m.group(2)) or "")), head)
    n = str(build.get("engine") or "").rsplit("v", 1)[-1]
    if n.isdigit():
        head = re.sub(r'(<code id="engJson">)[^<]*(?=<)', lambda m: m.group(1) + f"OMNI_V{n}.json", head)
        head = re.sub(r'(<code id="engDoc">)[^<]*(?=<)', lambda m: m.group(1) + f"docs/OMNI_V{n}.md", head)
    return head + tail


def inject(page: str, key: str, value) -> str:
    text = json.dumps(value, separators=(",", ":"), ensure_ascii=False)
    if "</" in text:
        raise ValueError(f"{key}: a record holds '</', which would end its script block")
    tag = f'<script type="application/json" id="{key}">'
    if tag in page:
        a = page.index(tag) + len(tag)
        return page[:a] + text + page[page.index("</script>", a):]
    anchor = '<script type="application/json" id="harness">'
    return page.replace(anchor, f"{tag}{text}</script>\n{anchor}", 1)


APPRAISAL = ROOT / "docs" / "engine" / "APPRAISAL.md"
COUNTS_BEGIN = "<!-- counts: written by docs/engine/build_live_engine.py at every build; never edited by hand -->"
COUNTS_END = "<!-- end counts -->"
WORDS = ("GAIN", "power given", "STEADY", "LOSS", "the runs disagree", "the runs differ", "shown", "tuning")


def table_way(file: str):
    """As the page reads it (tableWay): a four-ways table's tag, and whether Omni-Compass is read against its own native in it."""
    m = re.search(r"_4W_(TOP|ORCH|BARE|VS|BOTH)\.md$", file or "")
    return (m.group(1) if m else None), (not m or m.group(1) in ("TOP", "BARE"))


def _size(abc):
    """The largest size among a row's three runs, in percent, or None where a run is not a percentage."""
    out = []
    for c in abc or []:
        m = re.search(r"[-+\u2212]?\d[\d,]*(?:\.\d+)?", str(c or ""))
        if not m or "%" not in str(c):
            return None
        out.append(abs(float(m.group(0).replace(",", "").replace("\u2212", "-"))))
    return max(out) if out else None


def appraisal_counts(rec) -> str:
    """The appraisal's counts, from the records this build made: the runs and their files, the receipts by engine and by word
    (Omni-Compass against its native apart from the orchestrators' own cost, before and after the page's floor), and every LOSS
    row of Omni-Compass against its native. Written between COUNTS_BEGIN and COUNTS_END in docs/engine/APPRAISAL.md."""
    from collections import Counter
    b, R, S = rec["build"], rec["runs"], rec["scen"]
    runs = [r for bm in R["benchmarks"] for r in bm["runs"]]
    files, ok, unmatched = sum(r["checked"] for r in runs), sum(r["ok"] for r in runs), sum(len(r.get("unmatched") or []) for r in runs)
    recs = S["receipts"]; floor = rec["build"].get("floor")
    by_eng = Counter(r["engine"] for r in recs)

    def tally(rs, floored):
        c = Counter()
        for r in rs:
            cnt = dict(r.get("count") or {})
            if floored and floor is not None:
                for x in r["rows"]:
                    sz = _size(x.get("abc"))
                    if x["w"] in ("GAIN", "LOSS", "power given") and sz is not None and sz < 100 * floor:
                        cnt[x["w"]] = cnt.get(x["w"], 0) - 1; cnt["STEADY"] = cnt.get("STEADY", 0) + 1
            c.update({w: cnt.get(w, 0) for w in WORDS})
        return c

    def words(c):
        return ", ".join(f"{c[w]} {w}" for w in WORDS if c[w])
    omni = [r for r in recs if table_way(r["file"])[1]]; orch = [r for r in recs if not table_way(r["file"])[1]]
    losses = [f"{x['g']} under `{Path(r['file']).name}` ({r['engine']}: {', '.join(str(a) for a in (x.get('abc') or []))})"
              for r in omni for x in r["rows"] if x["w"] == "LOSS"]
    # the one count (the referee's work order of 25 October, item 4): the verdict audit's selection, which the LOSS ledger reads
    # too; the page's receipts are counted beside it and any difference is named, never hidden
    from tools.verdict_audit import build as audit_build, loss_rows as audit_losses
    au = audit_build(); ac = au["counts"]
    by_t = {t["stem"]: t for t in au["tables"]}
    a_nat = Counter(r["word"] for r in au["rows"] if by_t[r["table"]]["status"] == "standing" and by_t[r["table"]]["comparison"] == "against its native")
    page_nat = tally(omni, False)
    diff = {w: (page_nat[w], a_nat.get(w, 0)) for w in WORDS if page_nat[w] != a_nat.get(w, 0)}
    fl = f" (the page applies the floor of {100 * floor:g}% at load; after it: " if floor is not None else ""
    lines = [COUNTS_BEGIN,
             f"**The counts of the records on the page** ({b['engine']}, digest `{b['digest']}`), written by the build from the records it made, so a check rebuilds them exactly:",
             "", "| What | Count |", "|---|---|",
             f"| Three-run tables played back from their raw files (sections 5c and 5d) | {len(R['benchmarks'])}, with {len(runs)} runs |",
             f"| Raw files checked against their run's own `SHA256SUMS_ALL.txt` | {ok:,} of {files:,} matched; {unmatched} unmatched |",
             f"| Receipts (every judged row of each benchmark's newest table) | {len(recs)}: " + ", ".join(f"{e} {n}" for e, n in sorted(by_eng.items(), key=lambda kv: -int(re.sub(r'\D', '', kv[0]) or 0))) + " |",
             f"| Omni-Compass against its native ({len(omni)} tables), as the tables wrote them | {words(tally(omni, False))}{fl}{words(tally(omni, True)) + ')' if floor is not None else ''} |",
             f"| The orchestrators' own cost ({len(orch)} four-ways tables: the orchestrator as shipped against the organism alone, and the comparisons where Omni-Compass is on the other side), never a reading of Omni-Compass | {words(tally(orch, False))}{fl}{words(tally(orch, True)) + ')' if floor is not None else ''} |",
             f"| The verdict audit (`results/verdict_audit/VERDICT_AUDIT.md`, the one selection the LOSS ledger reads): standing tables, Omni-Compass against its native | {words(Counter(a_nat))}; {ac['standing_tables_on_the_engine_that_stands']} of {sum(1 for t in au['tables'] if t['status'] == 'standing')} standing tables on the engine that stands ({au['engine_standing']}) |",
             f"| The page's receipts against the audit | " + ("the same, word by word" if not diff else "differ: " + "; ".join(f"{w} {a} on the page, {b} in the audit" for w, (a, b) in diff.items())) + " |",
             f"| LOSS rows of Omni-Compass against its native | {len(audit_losses(au))} in the audit; on the page {len(losses)}: " + ("; ".join(losses) if losses else "none") + " |",
             "", COUNTS_END]
    return "\n".join(lines)


def write_appraisal(rec, check: bool = False) -> bool:
    """Rewrites the counts block of the appraisal (or, under --check, says whether it is current). True when current or written."""
    if not APPRAISAL.exists():
        return True
    t = APPRAISAL.read_text(encoding="utf-8")
    a, z = t.find(COUNTS_BEGIN), t.find(COUNTS_END)
    if a < 0 or z < 0:
        return True
    new = t[:a] + appraisal_counts(rec) + t[z + len(COUNTS_END):]
    if new == t:
        return True
    if check:
        return False
    APPRAISAL.write_text(new, encoding="utf-8")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="rebuild in memory; exit 1 if any record differs from the page")
    ap.add_argument("--no-runs", action="store_true", help="leave out GitHub's running and queued runs")
    a = ap.parse_args()
    global CHECKING
    CHECKING = a.check
    page = PAGE.read_text(encoding="utf-8")
    if re.search(r'prefers-color-scheme:\s*light|data-theme="light"\]', page):
        # the founder's orders of 17 and 20 October: the live benchmark engine is black on every viewer's theme, never white
        print("the page carries a light palette: the live benchmark engine renders dark on every viewer's theme")
        return 1
    named = re.search(r'<html[^>]*data-engine="(omni-v\d+)"', page)
    rec = records(not a.no_runs and not a.check)
    if not named or named.group(1) != rec["build"]["engine"]:
        # a new engine stands: the page adopts it at once (every record, the head's engine and the build line are rebuilt on
        # it); its prose keeps naming the engine it was written for in data-prose, and the page says so in a banner until
        # the prose is realigned (the build never stops the page on a new version)
        old = named.group(1) if named else None
        if a.check:
            print(f"the page names {old}, the repository stands on {rec['build']['engine']}: the next build adopts it")
            return 1
        if 'data-prose="' not in page:
            page = page.replace(f'data-engine="{old}"', f'data-engine="{old}" data-prose="{old}"', 1)
        page = re.sub(r'data-engine="omni-v\d+"', f'data-engine="{rec["build"]["engine"]}"', page, count=1)
        print(f"the engine that stands is now {rec['build']['engine']} (the page was built on {old}): records rebuilt on it; "
              "the prose stays as written for the older engine until it is realigned, and the page says so")
    if a.check:
        bad = [k for k in ("harness", "ctlrec", "scen", "runs", "fleet", "whole", "gpurun", "cpuhost", "monitors", "engineruns", "heldout", "cpptwin",
                          "beatsweep", "dial", "coremc", "onnative", "scenarios", "injgrid", "audit", "glossary", "field")
               if embedded(page, k) != rec[k]]
        # the build block: what the repository alone decides (the engine, its digest, the engines of the tables and the realms,
        # every benchmark's place and its tables) must be the page's; what GitHub said when the page was built (the run list,
        # the ledger, the commit and the time) is a reading with its own read time, not rebuilt by a check
        pb, keep = embedded(page, "build") or {}, ("engine", "digest", "realms_engine", "receipts_engines")
        strip = lambda bd: [{k: v for k, v in x.items() if k not in ("now", "abc")} for x in (bd or [])]
        if any(pb.get(k) != rec["build"][k] for k in keep) or strip(pb.get("board")) != strip(rec["build"]["board"]):
            bad.append("build")
        if not write_appraisal(rec, check=True):
            bad.append("the appraisal's counts (docs/engine/APPRAISAL.md)")
        if stamp_fallbacks(page, rec["build"]) != page:
            bad.append("the static fallbacks (the engine's name and digest in the markup)")
        print("every record on the page is the repository's own run" if not bad else "differs from the repository's own run: " + ", ".join(bad))
        for k in bad:
            if k not in rec:          # the appraisal's counts are a file, not a record: named above, no record to compare
                continue
            where = first_difference(embedded(page, k), rec[k])
            if where:
                print(f"  {k}: first difference at {where[0]}: the page {where[1]}, the rebuild {where[2]}")
        return 1 if bad else 0
    for k in ("harness", "ctlrec", "scen", "runs", "fleet", "build", "whole", "gpurun", "cpuhost", "monitors", "engineruns", "heldout", "cpptwin",
              "beatsweep", "dial", "coremc", "onnative", "scenarios", "injgrid", "audit", "glossary", "field"):
        page = inject(page, k, rec[k])
    page = stamp_fallbacks(page, rec["build"])   # the markup's fallbacks follow the build record, never a hand
    PAGE.write_text(page, encoding="utf-8")
    write_appraisal(rec)                      # the appraisal's counts follow the records, never a hand
    b = rec["build"]
    print(f"live benchmark engine rebuilt on {b['engine']} ({b['digest']}) at {b['commit'][:12]}, {b['built_at']}; "
          f"{len(b['runs'])} GitHub runs running or queued")
    return 0


if __name__ == "__main__":
    sys.exit(main())
