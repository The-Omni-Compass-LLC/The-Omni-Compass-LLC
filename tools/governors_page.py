# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The governors and orchestrators on one page (the founder's list of 19 October, night): every one he named, what it
governs, what native is under it and what Omni-Compass does on top, where its test stands, and, once its three runs are in,
its readings by the one key, every row counted, losses included (results/live/GOVERNORS.md).

A governor's result is its three-run table on the engine that stands (tools/confirm_abc.py writes results/live/V12_<NAME>.md
and .json), one table for each setting it is read in (the Kubernetes scheduler: as shipped and with the operator's
bin-packing profile); until the table exists the page says where the runs stand, never a number. The runs started are listed
in results/live/governors_runs.json by setting, written when they are started.
Usage: python3 tools/governors_page.py [--check]"""
from __future__ import annotations

import argparse, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from tools.legal import stamp  # noqa: E402
from tools.readings import labelled, receipt_key  # noqa: E402

OUT = ROOT / "results" / "live" / "GOVERNORS.md"
RUNS = ROOT / "results" / "live" / "governors_runs.json"
CATALOG_FILE = ROOT / "realms" / "catalog_v5.csv"
ENGINE = "omni-v12"
from tools.repo import RUNS as REPO_RUNS  # noqa: E402  (the repository's name, written once)

# (slug, name, register row, what it governs, native under it, its test) in the founder's order of naming, the
# Kubernetes scheduler first because every other one stands on it
GOVERNORS = [
    ("scheduler", "The Kubernetes scheduler (vanilla, and its bin-packing profile)", 88, "pod placement",
     "the default scheduler of Kubernetes 1.35 as shipped, which places every pod of every Kubernetes set; and the same "
     "release's scheduler with the operator's bin-packing profile (NodeResourcesFit, MostAllocated)",
     "the batch stream placed by the scheduler alone, in each setting (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 3)"),
    ("kueue", "Kueue", 63, "batch admission (a job at a time, by queue quota)",
     "Kueue v0.20.2 with the operator's single ClusterQueue sized to the workers",
     "`docs/BATCH_QUEUE_PREREGISTRATION.md`"),
    ("volcano", "Volcano", 63, "batch scheduling (queues, gangs)", "Volcano v1.16.0 with its default queue as shipped",
     "`docs/BATCH_QUEUE_PREREGISTRATION.md`"),
    ("kai", "KAI scheduler", 91, "AI workload scheduling (queues, fair share, gangs)",
     "the KAI scheduler v0.18.6 with its chart's default queues", "`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 1"),
    ("koordinator", "Koordinator", 89, "QoS colocation (batch work on what latency-sensitive pods leave unused)",
     "Koordinator 1.8.0, colocation on as shipped, the operator's colocation profile",
     "`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 2"),
    ("cruisekube", "CruiseKube", 81, "rightsizing (requests and limits, in place)",
     "CruiseKube applying its own recommendations as shipped", "`docs/CRUISEKUBE_PREREGISTRATION.md`"),
    ("crane", "Crane", 90, "predictive autoscaling and resource governance",
     "Crane 0.11.0 and the Prometheus it reads, as its installation guide installs them, the service's autoscaler handed to its "
     "Effective HPA in auto mode (its own example for this service), on Kubernetes 1.25.16 (Crane builds its HPA as "
     "autoscaling/v2beta2, which 1.26 removed)",
     "the served app under the closed load of the add-on sets, four ways (`docs/CRANE_PREREGISTRATION.md`)"),
    ("kuberay", "KubeRay", 92, "Ray clusters (the Ray autoscaler)",
     "KubeRay 1.7.1 and one Ray cluster (Ray 2.52.0) from KubeRay's own autoscaling sample, the Ray autoscaler as shipped",
     "the batch stream as Ray jobs (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 7)"),
    ("godel", "Gödel scheduler", 93, "unified online and offline scheduling",
     "the Gödel scheduler built from its pinned source and deployed by its own manifests, its placement as shipped, on "
     "Kubernetes 1.24.17 (it supports 1.21.4 to 1.24.6)",
     "the batch stream placed by Gödel, four ways (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 8)"),
    ("armada", "Armada", 94, "multi-cluster batch",
     "Armada v0.22.14 as its own local stack runs it (its server, scheduler, ingesters, Pulsar, Redis and PostgreSQL as "
     "containers on the runner, one executor per member cluster), one queue, each batch of the stream a job set of its pods",
     "the batch stream sent to a group of two clusters through Armada's queue, four ways (`docs/GROUP_PREREGISTRATION.md`, amendment 2)"),
    ("karmada", "Karmada", 95, "multi-cluster placement",
     "Karmada v1.19.0 on a cluster of its own, two member clusters joined, its placement of the stream as shipped with the "
     "operator's one propagation policy",
     "the batch stream sent to a group of two clusters, four ways (`docs/GROUP_PREREGISTRATION.md`)"),
    ("ocm", "Open Cluster Management", 96, "multi-cluster management",
     "OCM's hub (bundle 1.4.0, clusteradm v1.4.0) on a cluster of its own, two member clusters registered and accepted, a "
     "Placement per job with its default prioritizers and the job as a ManifestWork where it decided",
     "the batch stream sent to a group of two clusters placed by OCM, four ways (`docs/GROUP_PREREGISTRATION.md`, amendment 1)"),
    ("kubeedge", "KubeEdge", 97, "edge nodes", "its edge sync and offline autonomy", "not yet written"),
    ("nephio", "Nephio", 98, "network-function automation", "its intent-driven deployment and scaling",
     "not yet written (a candidate: its sandbox asks more than a free runner gives)"),
]

# The muscles of the catalog (realms/catalog_v5.csv) that stand for each governor's knobs in the modelled organisms (class S):
# they run in the realms, the spine and the whole tower, native and with Omni-Compass on top (results/realms_v5/REALMS_V5.md)
CATALOG = {
    "scheduler": (4, ["node_selector", "node_affinity", "pod_anti_affinity", "topology_spread", "taint_toleration",
                      "priority_class", "preemption_policy", "scheduler_backoff", "scheduler_scoring_strategy",
                      "scheduler_plugin_weights", "scheduling_gates", "deschedule"]),
    "kueue": (1, ["job_admission", "batch_admission", "queue_concurrency", "queue_backpressure", "tenant_admission"]),
    "volcano": (14, ["gang_schedule", "queue_fairness", "task_priority", "task_preemption", "binpack_pressure"]),
    "kai": (14, ["gang_schedule", "queue_fairness", "cluster_quota", "task_preemption"]),
    "koordinator": (14, ["oversubscription", "resource_reclaim", "binpack_pressure", "spread_pressure"]),
    "cruisekube": (3, ["cruisekube_request_rightsizing", "in_place_resize", "cpu_request", "memory_request"]),
    "crane": (2, ["hpa_cpu_target", "hpa_custom_target", "hpa_scaling_rate_policies", "hpa_min_replicas", "hpa_max_replicas"]),
    "kuberay": (12, ["training_workers", "elastic_worker_count", "training_gang_size"]),
    "godel": (14, ["gang_schedule", "task_admission", "binpack_pressure", "resource_reservation"]),
    "armada": (39, ["multi_cluster_dispatch", "federation_quota", "global_admission"]),
    "karmada": (39, ["multi_cluster_dispatch", "region_dispatch", "global_failover", "cross_cluster_replication"]),
    "ocm": (39, ["multi_cluster_dispatch", "workload_migrate_region", "federation_quota"]),
    "kubeedge": (39, ["edge_dispatch", "edge_offload", "edge_sync_interval", "edge_site_node_pool"]),
    "nephio": (66, ["ran_slice_resource_budget", "ran_du_cu_placement", "ran_cell_sleep", "ran_carrier_enable"]),
}

# A governor read in more than one setting: one three-run table for each (V12_<SETTING>.json), its runs listed by setting
SETTINGS = {"scheduler": (("vanilla", "as shipped"), ("binpack", "bin-packing profile"))}

# The four ways (docs/BATCH_QUEUE_PREREGISTRATION.md, amendment 6; the founder's order of 20 October): every comparison's
# three-run table, V12_<SYSTEM>_4W_<TAG>.json (tools/confirm_abc.py --pair), its column on the page, in this order
FOUR_WAYS = (("TOP", "compass", "Omni-Compass on top of it, against it as shipped"),
             ("ORCH", "native|nativebare", "it as shipped, against the organism alone"),
             ("BARE", "compassbare|nativebare", "Omni-Compass on the organism alone, against the organism alone"),
             ("VS", "compassbare|native", "Omni-Compass on the organism alone, against it as shipped"),
             ("BOTH", "compass|nativebare", "Omni-Compass on top of it, against the organism alone"))
FOUR_SYSTEMS = (("kai", "The KAI scheduler"), ("koordinator", "Koordinator"), ("kueue", "Kueue"), ("volcano", "Volcano"),
                ("binpack", "The scheduler's bin-packing profile"), ("kuberay", "KubeRay"), ("crane", "Crane"),
                ("godel", "The Gödel scheduler"), ("karmada", "Karmada"), ("ocm", "Open Cluster Management"),
                ("armada", "Armada"))

WORDS = ("GAIN", "LOSS", "power given", "STEADY", "the runs disagree", "shown, not judged")


def word_of(reading: str) -> str:
    r = reading.strip()
    if r.startswith("GAIN"):
        return "GAIN"
    if r.startswith("LOSS"):
        return "LOSS"
    if r.startswith("power given"):
        return "power given"
    if r.startswith("STEADY"):
        return "STEADY"
    if "disagree" in r:
        return "the runs disagree"
    return "shown, not judged"


def table_of(slug: str):
    """The governor's three-run table on the engine that stands, as tools/confirm_abc.py wrote it, or None."""
    p = ROOT / "results" / "live" / f"V12_{slug.upper()}.json"
    if not p.exists():
        return None
    return json.loads(p.read_text())


def four_way_table(system: str, tag: str):
    """One comparison of the four ways, as tools/confirm_abc.py --pair wrote it, or None."""
    return table_of(f"{system}_4W_{tag}")


def counts(table) -> dict:
    out = {w: 0 for w in WORDS}
    for row in (table.get("rows") or {}).values():
        out[word_of(row.get("reading", ""))] += 1
    return out


# after the queue's own gauges, the rows a reader looks at next: machines, energy, speed, failures (in this order)
KEY = ("worker nodes in service", "node-hours", "energy", "response time (ms), mean", "response time (ms), 95th",
       "failed requests", "alert minutes")


def key_rows(table, limit=14):
    """The rows a reader looks at first: the queue's own gauges, then machines, energy, speed and failures; each with its
    reading."""
    rows = table.get("rows") or {}
    first = [k for k in rows if k.startswith("queue:")] + [k for k in rows if k.startswith("batch:")]
    rest = [k for key in KEY for k in rows if k.startswith(key) and k not in first]
    seen = list(dict.fromkeys(first + rest))
    return [(k, rows[k].get("reading", "")) for k in seen[:limit]]


def runs_line(table):
    """The table's runs as the page names them ("A [id](link) (10 pairs), ..."), and the engines they ran on."""
    out, engines = [], set(table.get("engines", []))
    for r in table.get("runs", []):
        if isinstance(r, dict):
            pairs = f" ({r['paired_repetitions']} pairs)" if r.get("paired_repetitions") else ""
            out.append(f"{r.get('tag', '?')} [{r.get('run')}]({REPO_RUNS}{r.get('run')}){pairs}")
            if r.get("engine"):
                engines.add(r["engine"])
        else:
            out.append(str(r))
    return ", ".join(out), ", ".join(sorted(engines)) or ENGINE


def catalog_line(slug) -> str:
    import csv
    fid, muscles = CATALOG[slug]
    with CATALOG_FILE.open(encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if r["family_id"] == str(fid)]
    fam = rows[0]["family"] if rows else f"family {fid}"
    where = "the spine and every realm" if rows and len(rows[0]["realms"].split(";")) == 4 else "its realm and the whole tower"
    return (f"- **In the catalog (modelled, class S)**: family {fid}, {fam} ({len(rows)} muscles, in {where}): "
            + ", ".join(f"`{m}`" for m in muscles) + ".")


LOAD_WORDS = {"normal": "own load", "climb": "the climb", "line": "work in line"}


def orchestra():
    """The orchestra, the eighth organism (tools/run_orchestra.py): every governor's muscles as a body of its own and all of
    them together, native and with Omni-Compass on top, modelled; or None before its table is committed."""
    try:
        return json.loads((ROOT / "results" / "orchestra" / "ORCHESTRA.json").read_text())
    except (OSError, ValueError):
        return None


def orchestra_readings(orch, body):
    return [labelled(orch["bodies"][load][body]["label"]) if body in orch["bodies"].get(load, {}) else "not run"
            for load in LOAD_WORDS]


def settings_of(slug):
    return SETTINGS.get(slug, ((slug, ""),))


def runs_of(slug, runs):
    r = runs.get(slug) or {}
    return " ".join(f"[{letter}]({REPO_RUNS}{rid})" for letter, rid in sorted(r.items()) if rid)


SAME = ROOT / "results" / "orchestrators" / "ORCHESTRATORS.json"


def same_organisms():
    """The third arm (the founder's order of 25 October): every orchestrator on the same organisms with the same injection, and
    Omni-Compass on top of each, in our own models (tools/orchestrators_arm.py); each cell the words over every gauge of every
    organism in that setting."""
    L = ["## The orchestrators on the same organisms, with the same injection (modelled, class S): the third arm", ""]
    if not SAME.exists():
        return L + ["Not yet run (`tools/orchestrators_arm.py`, `docs/ORCHESTRATORS_PREREGISTRATION.md`).", ""]
    d = json.loads(SAME.read_text())
    m = d["meta"]
    from tools.orchestrators_arm import ORCHESTRATORS as NAMES
    L += [f"The founder's order of 25 October: every orchestrator on the same organisms with the same injection, and Omni-Compass "
          f"on top of each. {len(m['organisms'])} injections in two settings (the kind rig and the cloud), {m['reps']} repetitions, "
          f"every arm of a repetition meeting the same random numbers; each orchestrator's rule written from its own release; "
          f"Omni-Compass the shipped governor of {m['engine']}. A model, never a measurement of the orchestrator itself; every "
          f"organism and gauge: [`results/orchestrators/ORCHESTRATORS.md`](../orchestrators/ORCHESTRATORS.md).", "",
          "| Orchestrator | Setting | Against Kubernetes alone | Omni-Compass on top of it, against it |", "|---|---|---|---|"]
    for orch in m["orchestrators"]:
        for s in m["settings"]:
            vs, top = {}, {}
            for o in m["organisms"]:
                e = d["readings"][s][o]
                for r in (e["vs_native"].get(orch) or {}).values():
                    if r:
                        vs[r["word"]] = vs.get(r["word"], 0) + 1
                for r in e["omni_vs_orch"][orch].values():
                    if r:
                        top[r["word"]] = top.get(r["word"], 0) + 1
            words = lambda c: ", ".join(f"{c.get(w, 0)} {w}" for w in ("GAIN", "LOSS", "power given", "STEADY"))
            L.append(f"| {NAMES[orch]} | {'on-site' if s == 'onsite' else 'cloud'} | "
                     f"{'it is native' if orch == 'default' else words(vs)} | {words(top)} |")
    return L + [""]


def render(runs=None) -> str:
    runs = json.loads(RUNS.read_text()) if runs is None and RUNS.exists() else (runs or {})
    L = ["# The governors and orchestrators: native under them, Omni-Compass on top", ""]
    L += receipt_key() + [""]
    L += [f"The founder's list of 19 October, night: every governor and orchestrator he named runs with the organism native "
          f"under it, then with Omni-Compass on top of it, on the engine that stands ({ENGINE}). The organism is a six-worker "
          f"real Kubernetes cluster (kind v0.31.0, Kubernetes v1.35.0) on GitHub's machines, each arm on a fresh cluster, the "
          f"two arms back to back on one runner, ten paired repetitions a run, three runs (A, B and C) for a reading. Native is "
          f"the governor as its project ships it; Omni-Compass sits on top with its own levers (the node pool, the service's "
          f"autoscaler and processor limit, cruise and idle) and never writes the governor's objects, but where the governor owns "
          f"the service's autoscaler (Crane): there its autoscaler moves reach the autoscaler through the governor's own object, "
          f"by a plug, as on KEDA. Crane runs on Kubernetes 1.25.16 (its HPA is an API 1.26 removed) and Gödel on 1.24.17 (its "
          f"supported range), where no pod is resized in place, so no processor limit is moved in any of their arms. Cost: $0 (GitHub's free "
          f"machines). A governor's line reads only from its own three-run table; until then it says where its runs stand.", ""]
    L += ["| Governor | What it governs | Register row | Where it stands | Readings (A, B and C) |", "|---|---|---:|---|---|"]
    for slug, name, row, field, native, test in GOVERNORS:
        wheres, readings = [], []
        for key, label in settings_of(slug):
            tag = f"{label}: " if label else ""
            t, started = table_of(key), runs_of(key, runs)
            if t:
                c = counts(t)
                readings.append(f"{tag}{c['GAIN']} GAIN, {c['LOSS']} LOSS, {c['power given']} power given, {c['STEADY']} STEADY, "
                                f"{c['the runs disagree']} where the runs disagree ([table](V12_{key.upper()}.md))")
                wheres.append(f"{tag}three runs in")
            elif started:
                readings.append(f"{tag}runs not yet finished"); wheres.append(f"{tag}running: {started}")
            elif runs_of(f"{key}4", runs):
                readings.append(f"{tag}runs not yet finished"); wheres.append(f"{tag}running four ways (below)")
            elif test.startswith("not yet"):
                readings.append(f"{tag}not yet run"); wheres.append(f"{tag}its rig is not yet built")
            else:
                readings.append(f"{tag}not yet run"); wheres.append(f"{tag}built; its runs come in the campaign")
        L.append(f"| {name} | {field} | {row} | {'; '.join(wheres)} | {'; '.join(readings)} |")
    L.append("")
    L += ["## The four ways (the founder's order of 20 October)", "",
          "Each system runs four ways in every repetition, each way on a fresh cluster of the same configuration, back to back "
          "on one runner, the governor on its own core (`docs/BATCH_QUEUE_PREREGISTRATION.md`, amendments 5 and 6): the "
          "organism alone (the stream placed by Kubernetes' own scheduler, no orchestrator installed; for Crane, the service's HPA "
          "as Kubernetes ships it, `docs/CRANE_PREREGISTRATION.md`), the orchestrator as its "
          "project ships it, Omni-Compass on top of the organism alone, and Omni-Compass on top of the orchestrator. Each "
          "column is one comparison, the first against the second, paired within the repetition and read by the one key for "
          "the first; each cell reads only from its own three-run table. Omni-Compass never places a pod or admits a job: on "
          "the organism alone it sits on top of Kubernetes' own scheduler.", "",
          "| System | Runs (A, B and C) | " + " | ".join(t for _, _, t in FOUR_WAYS) + " |",
          "|---|---|" + "---|" * len(FOUR_WAYS)]
    for system, name in FOUR_SYSTEMS:
        started = runs_of(f"{system}4", runs)
        cells = []
        for tag, _, _ in FOUR_WAYS:
            t = four_way_table(system, tag)
            if t:
                c = counts(t)
                cells.append(f"{c['GAIN']} GAIN, {c['LOSS']} LOSS, {c['power given']} power given, {c['STEADY']} STEADY, "
                             f"{c['the runs disagree']} where the runs disagree ([table](V12_{system.upper()}_4W_{tag}.md))")
            else:
                cells.append("runs not yet finished" if started else "not yet run")
        L.append(f"| {name} | {started or 'not yet started'} | " + " | ".join(cells) + " |")
    L.append("")
    orch = orchestra()
    L += ["## The orchestra, the eighth organism (modelled, class S)", ""]
    if orch:
        L += [f"The founder's word of 19 October, night: the governors in a catalog group, an organism of their own. Every "
              f"catalog muscle that stands for a governor's knob (below, under each governor) runs in the modelled organisms "
              f"as the seven do: each governor's muscles as a body of its own, then all of them together as one body, the "
              f"orchestra, native and then with Omni-Compass on top at the max, on {orch['run']['engine']}, seeds "
              f"{orch['run']['seeds'][0]}-{orch['run']['seeds'][-1]}. A model, not a measurement of the governor itself; "
              f"every row: [`results/orchestra/ORCHESTRA.md`](../orchestra/ORCHESTRA.md).", "",
              "| Body | Muscles | Own load | The climb | Work in line |", "|---|---:|---|---|---|"]
        for slug, name, *_ in GOVERNORS:
            L.append(f"| {name} | {len(orch['run']['bodies'][slug])} | " + " | ".join(orchestra_readings(orch, slug)) + " |")
        L.append(f"| **The orchestra, every governor's muscle once** | {len(orch['run']['bodies']['orchestra'])} | "
                 + " | ".join(f"**{r}**" for r in orchestra_readings(orch, "orchestra")) + " |")
    else:
        L.append("Not yet run (`tools/run_orchestra.py`).")
    L.append("")
    L += same_organisms()
    for slug, name, row, field, native, test in GOVERNORS:
        L += [f"## {name}", "", f"- **Native**: {native}.", f"- **Its test on real Kubernetes (class L)**: {test}; register row {row}.",
              catalog_line(slug)]
        if orch:
            L.append("- **Its muscles as a body in the orchestra (modelled, class S)**: "
                     + "; ".join(f"{w}: {r}" for w, r in zip(LOAD_WORDS.values(), orchestra_readings(orch, slug))) + ".")
        for key, label in settings_of(slug):
            t, head = table_of(key), (f" ({label})" if label else "")
            if t:
                runs, engines = runs_line(t)
                L.append(f"- **Runs{head}**: {runs}; engine {engines}.")
                L += ["", "| Gauge | Reading |", "|---|---|"] + [f"| {k} | {r} |" for k, r in key_rows(t)]
                L += ["", f"Every row of the run: [`results/live/V12_{key.upper()}.md`](V12_{key.upper()}.md).", ""]
            else:
                L.append(f"- **Readings{head}**: none yet; nothing is written here before its three runs are in.")
        L.append("")
    return "\n".join(stamp(L)) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="fail if the page is not what the tables and runs give")
    a = ap.parse_args(argv)
    text = render()
    if a.check:
        if not OUT.exists() or OUT.read_text() != text:
            print("governors page: out of date (python3 tools/governors_page.py)")
            return 1
        print("governors page: current")
        return 0
    OUT.write_text(text)
    print(f"governors page -> {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
