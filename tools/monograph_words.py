#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Every count the live engine's monograph quotes, written from the record that holds it, so the words follow the numbers.

The founder's order of 6 November 2026: when the numbers change, the words follow by themselves. The referee's report on
`docs/engine/LIVE_ENGINE_MONOGRAPH.md` of 7 November (grade C+) found its do-no-harm record printed by hand and overtaken
within minutes by the record it described (273 LOSS rows where the ledger held 287, the omni-v25 fault that explains half of
them unnamed, the appraisal, oversight, manifest and Python 500 figures of an earlier build). Every such figure is written
here instead, from its record, between its markers:

    <!-- monograph: NAME (tools/monograph_words.py) -->TEXT<!-- end of monograph: NAME -->

A block whose text is one line sits inline, inside a sentence. A block whose text spans lines (a table, a list) is written
with each marker on its own line and the text between them. Nothing here decides a word of its own: every word is the one
key's (`tools/readings.py`), every LOSS row and its cause the ledger's (`tools/loss_ledger.py` on the verdict audit's record,
`results/verdict_audit/VERDICT_AUDIT.json`), the index the index's (`tools/omni_index.py`, its own functions). Where a
record carries a figure only in a generated page (the appraisal's counts, the verification receipt) the page is read where
its writer put it; a figure no record holds has no block and is not written.

    python3 tools/monograph_words.py --fix     write every block in docs/engine/LIVE_ENGINE_MONOGRAPH.md from its record
    python3 tools/monograph_words.py --check   exit 1 naming every block whose text differs from its record, every broken
                                               marker pair and every unknown name; exit 0 when all match or no block stands
    python3 tools/monograph_words.py --list    a JSON list of {name, text, source} for every block this tool computes
    --file PATH                                read and write PATH in place of the monograph (the tests use a copy)
"""
from __future__ import annotations

import argparse
import ast
import csv
import json
import math
import re
import sys
from collections import Counter, OrderedDict, defaultdict
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import loss_ledger as LL                                       # noqa: E402
from tools import omni_index as OI                                        # noqa: E402
from tools import verdict_audit as VA                                     # noqa: E402
from tools.readings import (DISAGREE, GAIN, GIVEN, LOSS, SIZE_FLOOR, SPENT, STEADY, HIGHER, LOWER, WORK_PER,  # noqa: E402
                            word as key_word)
from tools.reread import bare                                             # noqa: E402

MONOGRAPH = ROOT / "docs" / "engine" / "LIVE_ENGINE_MONOGRAPH.md"
BEGIN = "<!-- monograph: {} (tools/monograph_words.py) -->"
END = "<!-- end of monograph: {} -->"
OPEN = re.compile(r"<!-- monograph: ([A-Za-z0-9_]+) \(tools/monograph_words\.py\) -->")
CLOSE = re.compile(r"<!-- end of monograph: ([A-Za-z0-9_]+) -->")

AUDIT = ROOT / "results" / "verdict_audit" / "VERDICT_AUDIT.json"
DISCREPANCIES = ROOT / "results" / "verdict_audit" / "DISCREPANCIES.json"
LEDGER = ROOT / "docs" / "LOSS_LEDGER.md"
FLIP_PAGE = ROOT / LL.FLIP_PAGE
INDEX_JSON = ROOT / "results" / "OMNI_INDEX.json"
OVERSIGHT = ROOT / "results" / "OVERSIGHT.json"
SITE = ROOT / "results" / "SITE_NUMBERS.json"
TWO_BILLS = ROOT / "results" / "TWO_BILLS.json"
WHOLE = ROOT / "results" / "WHOLE_SYSTEM.json"
SEAL = ROOT / "results" / "SEAL.json"
CORE_EVIDENCE = ROOT / "results" / "core_evidence.json"
CORE_EVIDENCE_PY = ROOT / "benchmarks" / "core_evidence.py"
TRACKING = ROOT / "results" / "TRACKING_BOUNDS.json"
MANIFEST = ROOT / "RELEASE_MANIFEST.json"
RECEIPT = ROOT / "results" / "VERIFY_RECEIPT.txt"
APPRAISAL = ROOT / "docs" / "engine" / "APPRAISAL.md"
PAGE = ROOT / "docs" / "engine" / "OMNI_COMPASS_LIVE_ENGINE.html"
STAMP = ROOT / "docs" / "engine" / "LIVE_ENGINE_VERSION.json"
CATALOG = ROOT / "realms" / "catalog_v5.csv"
CARDS = ROOT / "realms" / "muscle_cards_v5.csv"
RECIPES = ROOT / "docs" / "wiring_recipes.csv"
VERDICTS_CSV = ROOT / "results" / "WIRING_VERDICTS.csv"
REALMS = ROOT / "results" / "realms_v5" / "REALMS_V5.json"
ORCHESTRA = ROOT / "results" / "orchestra" / "ORCHESTRA.json"
AKS_JSON = ROOT / "results" / "live" / "AKS_STEADY_100_OMNI_V18.json"
AKS_MD = ROOT / "results" / "live" / "AKS_STEADY_100_OMNI_V18.md"
WORKFLOWS = ROOT / ".github" / "workflows"

JUDGED_WORDS = (GAIN, GIVEN, STEADY, LOSS, DISAGREE)
COUNT_WORDS = (GAIN, GIVEN, STEADY, LOSS, DISAGREE, "shown")
NATIVE = "against its native"

# names a reader knows a table by (display only; every count is the record's)
PRODUCT = {"VANILLA": "the Kubernetes scheduler as shipped", "BINPACK": "the scheduler's bin-packing profile", "KUEUE": "Kueue",
           "VOLCANO": "Volcano", "KAI": "the KAI scheduler", "KOORDINATOR": "Koordinator",
           "KOORDINATOR_CGROUP": "Koordinator on the cgroup root its own tests use", "CRUISEKUBE": "CruiseKube",
           "CRUISEKUBE_RECORDER": "CruiseKube, a worker it marks overloaded counted as in service", "CRANE": "Crane",
           "KUBERAY": "KubeRay", "GODEL": "the Gödel scheduler", "ARMADA": "Armada", "KARMADA": "Karmada",
           "OCM": "Open Cluster Management"}
TEST = {"ALL_FOUR": "all four in one run", "BATCH": "the batch queue", "CAPACITY": "the capacity test",
        "COST_TO_MATCH": "the cost to match", "CRUISEKUBE": "CruiseKube", "CRUISEKUBE_RECORDER": "CruiseKube with the recorder",
        "FAIRNESS": "the noisy neighbour", "FAULTS": "the four faults", "FAULTS_EXTENDED": "the extended faults",
        "GOLDILOCKS": "Goldilocks", "KEDA_CPU_REQUESTS": "KEDA on the CPU target and requests in flight",
        "KEDA_REQUESTS": "KEDA's HTTP add-on", "ROBUST_KILL": "the kill test", "ROBUST_LONG": "the long run",
        "STEADY": "the steady load", "TRACE_GOOGLE2011": "the Google trace of 2011", "WANDERING": "demand that wanders",
        "PGBENCH": "PostgreSQL behind PgBouncer", "PGBENCH_SERVICE": "PostgreSQL behind PgBouncer, the service objective",
        "KAFKA": "Apache Kafka", "KAFKA_SERVICE": "Apache Kafka, the service objective", "REDIS": "Redis",
        "REDIS_SERVICE": "Redis, the service objective", "REDIS_SHIPPED": "Redis as shipped", "YCSB": "MongoDB under YCSB",
        "YCSB_SERVICE": "MongoDB under YCSB, the service objective", "YCSB_SHIPPED": "MongoDB under YCSB as shipped",
        "SYSBENCH": "MySQL under sysbench", "SYSBENCH_SERVICE": "MySQL under sysbench, the service objective",
        "SYSBENCH_SHIPPED": "MySQL under sysbench as shipped"}
WAY = {"TOP": ("on top", "four ways"), "BARE": ("on the organism alone", "four ways"), None: ("on top", "two ways")}
ORDER = ("VANILLA", "BINPACK", "KUEUE", "VOLCANO", "KAI", "KOORDINATOR", "KOORDINATOR_CGROUP", "CRUISEKUBE",
         "CRUISEKUBE_RECORDER", "CRANE", "KUBERAY", "GODEL", "ARMADA", "KARMADA", "OCM")
CATEGORY = {"Real Kubernetes (GitHub)": ("Kubernetes", "machines in service"),
            "Real database (PostgreSQL behind PgBouncer, GitHub)": ("PostgreSQL behind PgBouncer", "connections"),
            "Real messaging (Apache Kafka, GitHub)": ("Apache Kafka", "consumers"),
            "Real cache (Redis, GitHub)": ("Redis", "memory ceiling"),
            "Real database cache (MongoDB under YCSB, GitHub)": ("MongoDB under YCSB", "cache"),
            "Real database buffer pool (MySQL under sysbench, GitHub)": ("MySQL under sysbench", "buffer pool")}
STORE_GAUGE = {"p50_ms": "median response", "p95_ms": "95th percentile", "p99_ms": "99th percentile", "mean_ms": "mean response",
               "work_inside_line_ops": "work inside the line", "work_inside_line_tps": "work inside the line",
               "work_inside_line_rps": "work inside the line", "work_inside_line_mps": "work inside the line",
               "ops": "operations done"}
REALM = OrderedDict([("compute_ai_cloud", "Compute / AI / Cloud"), ("physics_robotics_autonomous", "Physics / Robotics / Autonomous"),
                     ("energy_facility_industrial", "Energy / Facility / Industrial"),
                     ("distribution_specialized", "Distribution / Specialized")])


class RecordError(Exception):
    """A record does not hold what a block reads from it: the block cannot be written, and --check says so."""


# ---------------------------------------------------------------------------------------------------------------- words
def pct(v: float, d: int = 1) -> str:
    """A size, no sign: the direction is said in words beside it."""
    return f"{abs(v):,.{d}f}%"


def updown(v: float) -> str:
    return "up" if v > 0 else "down" if v < 0 else "unchanged"


def n(v) -> str:
    return f"{v:,}"


def num(v: float) -> str:
    """A measured value as the tables print it: four significant figures, thousands separated."""
    if v is None:
        return "no value"
    return f"{v:,.0f}" if abs(v) >= 1000 else f"{v:.4g}"


def short(h: str, k: int = 16) -> str:
    return f"`{h[:k]}…`"


def plural(k: int, one: str, many: str) -> str:
    return f"{n(k)} {one if k == 1 else many}"


def series(items) -> str:
    items = [x for x in items if x]
    if len(items) <= 1:
        return "".join(items)
    return ", ".join(items[:-1]) + " and " + items[-1]


def combined(x, s=None) -> str:
    """A combined number (an index, a category, a test) by the key: GAIN, up; LOSS, down (its service reading below 1 too);
    power given, the index down (the resources put in outweigh what they bought on the index's equal weights); a change
    under the 0.5% floor STEADY."""
    if x is None:
        return "not read"
    ch = x - 1.0
    if ch == 0:
        return STEADY
    if abs(ch) < SIZE_FLOOR:
        return f"STEADY, under the floor ({pct(100 * ch)})"
    w = OI.index_word(x, s)
    if w == GAIN:
        return f"GAIN, up {pct(100 * ch)}"
    if w == LOSS:
        return f"LOSS, down {pct(100 * ch)}"
    return f"power given, the index down {pct(100 * ch)}"


def run_size(r: dict) -> str:
    """One run's raw change in words: up or down by its size, or from one value to the other where native stood at zero."""
    nat, omn = r.get("native"), r.get("omni")
    if nat is None or omn is None:
        return "no value"
    if nat == 0:
        return "none in either arm" if omn == 0 else f"from 0 to {num(omn)}"
    ch = 100 * (omn - nat) / abs(nat)
    return "the same" if ch == 0 else f"{updown(ch)} {pct(ch, 2 if abs(ch) < 0.05 else 1)}"


def reading(r: dict) -> str:
    """A three-run row's reading as the key stored it, with its size in words: the range of the runs' changes where they all
    point one way, else each run's own change."""
    rd = bare(r.get("recomputed") or r.get("stored") or "")
    w = r["word"]
    if w == STEADY:
        return rd
    rel = [None if x.get("native") in (None, 0) or x.get("omni") is None else 100 * (x["omni"] - x["native"]) / abs(x["native"])
           for x in r["runs"]]
    if w in (GAIN, LOSS, GIVEN) and all(v is not None for v in rel) and len({v > 0 for v in rel}) == 1 and all(rel):
        lo, hi = min(abs(v) for v in rel), max(abs(v) for v in rel)
        d = 2 if lo < 0.05 else 1
        size = pct(lo, d) if f"{lo:.{d}f}" == f"{hi:.{d}f}" else f"{pct(lo, d)} to {pct(hi, d)}"
        return f"{rd}, {updown(rel[0])} {size}"
    return f"{rd} ({', '.join(f'run {t} {run_size(x)}' for t, x in zip('ABC', r['runs']))})"


WHY = {("time waited, missed or failed", GAIN): "less time waited, missed or failed than native",
       ("time waited, missed or failed", LOSS): "more time waited, missed or failed than native",
       ("work done", GAIN): "more work done than native", ("work done", LOSS): "less work done than native",
       ("resource spent or held", GAIN): "less of the resource held: a cut",
       ("resource spent or held", GIVEN): "more of the resource held: what Omni-Compass put in, shown beside what it bought",
       ("work per resource", GAIN): "more work for each unit of the resource",
       ("work per resource", GIVEN): "less work for each unit of the resource: power given",
       ("a count that must never rise", LOSS): "a count that must never rise rose in a run"}


def why(r: dict) -> str:
    """The reason a reading reads so, from what its gauge is for (the founder's order: the why stands where the number sits)."""
    w = r["word"]
    if w == STEADY:
        return "the two arms the same" if "the same" in bare(r.get("recomputed") or "") else "no change of 0.5% or more"
    if w == DISAGREE:
        return "runs that moved 0.5% or more in opposite directions: unresolved"
    return WHY.get((r.get("direction"), w), "")


def gauge_name(r: dict) -> str:
    g = r["gauge"]
    if g.startswith("robust: "):
        g = g[len("robust: "):]
    g = STORE_GAUGE.get(g, g)
    return f"{r['section']}: {g}" if r.get("section") else g


# ---------------------------------------------------------------------------------------------------------------- records
def load(p: Path):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise RecordError(f"{p.relative_to(ROOT)} cannot be read: {e}")


@lru_cache(None)
def engine():
    """The engine that stands: the newest OMNI_V<n>.json, its number, digest and files."""
    found = sorted((int(m.group(1)), p) for p in ROOT.glob("OMNI_V*.json") if (m := re.fullmatch(r"OMNI_V(\d+)\.json", p.name)))
    if not found:
        raise RecordError("no OMNI_V<n>.json in the repository's root")
    k, p = found[-1]
    d = load(p)
    return {"n": k, "name": d["version"], "digest": d["digest"][:16], "files": len(d["files"]), "path": p, "hashes": d["files"]}


@lru_cache(None)
def audit():
    return load(AUDIT)


@lru_cache(None)
def tables():
    return {t["stem"]: t for t in audit()["tables"]}


def standing_native(stem: str) -> bool:
    t = tables().get(stem)
    return bool(t) and t["status"] == "standing" and t["comparison"] == NATIVE


@lru_cache(None)
def native_losses():
    """Every LOSS row of the standing tables against Omni-Compass's own native: the one list (tools/verdict_audit.py)."""
    return VA.loss_rows(audit())


def rows_of(stem: str):
    return [r for r in audit()["rows"] if r["table"] == stem]


@lru_cache(None)
def ledger():
    """The LOSS ledger exactly as tools/loss_ledger.py builds it, on the verdict audit's stored record (its build() reads the
    audit's build(); here that build is the record the audit wrote, so the ledger and the record cannot part)."""
    rec = audit()
    original = VA.build
    VA.build = lambda *a, **k: rec
    try:
        rows, engines = LL.build()
    finally:
        VA.build = original
    return rows, dict(engines)


def cause_kind(c) -> str:
    if c is None:
        return "none"
    if c is LL.FLIP:
        return "flip"
    if c is LL.FLIP_QUEUE:
        return "flip_queue"
    if c is LL.BEAT_LOAD:
        return "beat"
    if c is LL.SCHED_SUSPECT:
        return "suspected"
    return "other"


@lru_cache(None)
def ledger_native():
    """(table stem, gauge as the ledger writes it, the audit's row, its cause, its kind) for every row against native."""
    rows, _ = ledger()
    out = []
    for k, name, _p, gauge, row, _title in rows[LL.SECTIONS[0]]:
        c = LL.cause(name, gauge, k)
        out.append((f"V{k}_{name}", gauge, row, c, cause_kind(c)))
    return out


def place(stem: str) -> str:
    """Where a table sits: the cluster's own tests, the data stores, the two-way tables of the batch-stream rigs, or the four
    ways (Omni-Compass on top of the product, or on the organism alone)."""
    t = tables()[stem]
    m = re.search(r"_4W_([A-Z]+)$", stem)
    if m:
        return {"TOP": "top", "BARE": "bare"}.get(m.group(1), m.group(1).lower())
    if t["stack"] == "Linux services":
        return "stores"
    if t["stack"] != "Kubernetes":
        return "simulators"
    return "two_way" if "under the batch stream" in (t.get("title") or "") else "cluster"


def base_of(stem: str) -> tuple:
    """(the table's benchmark without its engine and way, its way: TOP, BARE or None)."""
    b = stem.split("_", 1)[1]
    m = re.search(r"_4W_([A-Z]+)$", b)
    return (b[:m.start()], m.group(1)) if m else (b, None)


def named(stem: str, ref: bool = False) -> str:
    """A table as a reader knows it: the product and the way Omni-Compass sits on it, or the test; with ref, its stem too."""
    b, w = base_of(stem)
    if b in PRODUCT and (w or place(stem) == "two_way"):
        on, ways = WAY[w]
        return f"{PRODUCT[b]} {on} ({ways}" + (f", `{stem}`)" if ref else ")")
    name = TEST.get(b, PRODUCT.get(b, b))
    return f"{name} (`{stem}`)" if ref else name


def order_key(stem: str):
    b = base_of(stem)[0]
    return (ORDER.index(b) if b in ORDER else len(ORDER), stem)


def gauge_group(r: dict) -> str:
    g = r["gauge"].lower()
    if r.get("direction") == "work done":
        return "work done"
    if "pod start wait" in g:
        return "the pod start wait"
    if "queue finished" in g:
        return "the queue's finish"
    if g.startswith("queue:"):
        return "the jobs' wait, turnaround or count unfinished"
    if "alert minutes" in g:
        return "alert minutes"
    if "time over" in g:
        return "time over the response line"
    if "failed requests" in g:
        return "failed requests"
    if "response time" in g or g.endswith("_ms"):
        return "a slower response"
    return "another gauge"


GROUP_ORDER = ("the pod start wait", "failed requests", "time over the response line", "alert minutes", "a slower response",
               "the queue's finish", "the jobs' wait, turnaround or count unfinished", "work done", "another gauge")


def grouped(rows, sep: str = "; ") -> str:
    c = Counter(gauge_group(r) for r in rows)
    return sep.join(f"{g} {c[g]}" for g in GROUP_ORDER if c[g])


# ---------------------------------------------------------------------------------------------------------------- the index
@lru_cache(None)
def index_tests():
    """tools/omni_index.py's own tests(), each test as the index reads it."""
    return OI.tests()


def real_categories():
    ts = index_tests()
    return [c for c in OI.REAL if any(t["category"] == c for t in ts)]


@lru_cache(None)
def index_record():
    """The headline, its service reading, the reading of 4 October and every category, composed from tests() exactly as
    tools/omni_index.py main() composes them (each category the geometric mean of its tests; the headline the geometric
    mean of the real categories)."""
    ts = index_tests()
    cats = OrderedDict((c, [t for t in ts if t["category"] == c]) for c in real_categories())
    g = lambda c, k: OI.gmean([1 + t[k] / 100 for t in cats[c] if t.get(k) is not None])
    cat_g = OrderedDict((c, g(c, "index_pct")) for c in cats)
    cat_s = OrderedDict((c, g(c, "service_pct")) for c in cats)
    cat_r = OrderedDict((c, g(c, "resource_pct")) for c in cats)
    rec = {"cats": cat_g, "scats": cat_s, "tests": cats, "head": OI.gmean(list(cat_g.values())),
           "service": OI.gmean([v for v in cat_s.values() if v]), "resource": OI.gmean([v for v in cat_r.values() if v])}
    stored = load(INDEX_JSON)
    if stored.get("headline_pct") is not None and abs(100 * (rec["head"] - 1) - stored["headline_pct"]) > 1e-6:
        raise RecordError("results/OMNI_INDEX.json is not what tools/omni_index.py computes from the tables "
                          "(run python3 tools/omni_index.py)")
    return rec


def _source_of(t: dict):
    for cat, name, f, measures, work in OI.SOURCES:
        if cat == t["category"] and name == t["test"]:
            return ("rows", measures, work)
    for cat, fname, label, measures in OI.WORKLOAD_TABLES:
        if cat == t["category"] and t["test"].startswith(label.split("`{wl}`")[0]):
            m = re.search(r"`([^`]+)`", t["test"])
            return ("workload", measures, m.group(1) if m else None)
    raise RecordError(f"tools/omni_index.py names no source for the test {t['test']!r}")


def _run_ratios(t: dict) -> dict:
    """{measure: [each run's ratio]} for one test, each measure admitted exactly as tools/omni_index.py admits it (its
    three-run reading judged, else 1 in every run)."""
    data = load(ROOT / t["source"])
    kind, measures, extra = _source_of(t)
    out = {}
    if kind == "rows":
        rows = data["rows"]
        keys = dict(measures)
        if extra == "capacity":
            keys["work"] = OI.CAPACITY if OI.CAPACITY in rows else OI.CAPACITY_NOW
        for m, key in keys.items():
            if key not in rows:
                continue
            row = rows[key]
            rs = [OI.ratio(m, r["native"], r["omni"]) for r in row["runs"]]
            out[m] = rs if OI.judged(row["reading"]) and all(rs) else [1.0] * len(rs)
        if extra == "equal":
            out["work"] = [1.0] * len(data["runs"])
        return out
    gauges = data["workloads"][extra]
    for m, key in measures.items():
        g = OI.workload_gauge(gauges, key)
        if not g or any(x is None for x in g["runs"]):
            continue
        if OI.judged(g["reading"]):
            rr = [(x["omni"] / x["native"]) if m == "work" else (x["native"] / x["omni"]) for x in g["runs"] if x["native"] and x["omni"]]
            out[m] = rr if len(rr) == len(g["runs"]) else [OI.gmean(rr) or 1.0] * len(g["runs"])
        else:
            out[m] = [1.0] * len(g["runs"])
    return out


@lru_cache(None)
def index_by_run():
    """Each run's own index (A, B, C): every measure at that run's own ratio where the index admits it, composed as the
    headline is. The three runs' geometric mean is the headline exactly, or the record is refused."""
    rec = index_record()
    per_cat = OrderedDict()
    for c, ts in rec["tests"].items():
        runs = []
        for t in ts:
            rr = _run_ratios(t)
            for m, v in rr.items():
                if abs((OI.gmean(v) or 1.0) - t["measures"][m]["ratio"]) > 1e-9:
                    raise RecordError(f"the runs of {t['test']!r}, {m}, do not compose to its ratio")
            k = {len(v) for v in rr.values()}
            if k != {3}:
                raise RecordError(f"{t['test']!r} does not carry three runs on every measure")
            runs.append([OI.gmean([OI.scored_ratio(c, m, rr[m][i]) for m in rr]) for i in range(3)])
        per_cat[c] = [OI.gmean([r[i] for r in runs]) for i in range(3)]
    head = [OI.gmean([per_cat[c][i] for c in per_cat]) for i in range(3)]
    if abs(OI.gmean(head) - rec["head"]) > 1e-9:
        raise RecordError("the three runs' own indexes do not compose to the headline")
    return {"head": head, "cats": per_cat}


def cat_name(c: str) -> str:
    return CATEGORY.get(c, (c, "resource"))[0]


def cat_resource(c: str) -> str:
    return CATEGORY.get(c, (c, "the resource held"))[1]


def avg(c: str, m: str):
    return OI.gmean([t["measures"][m]["ratio"] for t in index_record()["tests"][c] if m in t["measures"]])


def work_cell(r):
    if r is None:
        return "not taken"
    if r == 1.0:
        return STEADY
    if abs(r - 1) < SIZE_FLOOR:
        return f"STEADY, under the floor ({pct(100 * (r - 1))})"
    return f"GAIN, {pct(100 * (r - 1))} more" if r > 1 else f"LOSS, {pct(100 * (1 - r))} less"


def speed_cell(r):
    if r is None:
        return "not taken"
    if r == 1.0:
        return STEADY
    if abs(r - 1) < SIZE_FLOOR:
        return f"STEADY, under the floor ({pct(100 * (r - 1))})"
    return (f"GAIN, native's {pct(100 * (r - 1))} longer" if r > 1 else f"LOSS, native's {pct(100 * (1 - r))} shorter")


def held_cell(r, what):
    if r is None:
        return "not taken"
    if r == 1.0:
        return STEADY
    if abs(r - 1) < SIZE_FLOOR:
        return f"STEADY, under the floor ({pct(100 * (r - 1))})"
    return (f"GAIN, a cut: native's {what} {pct(100 * (r - 1))} above" if r > 1
            else f"power given: native's {what} {pct(100 * (1 - r))} below")


def measure_cell(t: dict, m: str, what: str) -> str:
    """One measure of one test as the index read it: judged, its ratio in words; otherwise its own three-run reading."""
    x = t["measures"].get(m)
    if x is None:
        return "not taken"
    rd = bare(x.get("reading", ""))
    if rd.startswith("the same fixed-rate work"):
        return "STEADY, equal by design"
    if not OI.judged(x["reading"]):
        return rd + (" (entered as 1)" if rd.startswith("the runs disagree") else "")
    cell = {"work": work_cell, "speed": speed_cell}.get(m)
    out = cell(x["ratio"]) if cell else held_cell(x["ratio"], what)
    return out + (" (shown, not scored)" if m == "energy" and OI.scored_ratio(t["category"], m, x["ratio"]) == 1.0 else "")


# ---------------------------------------------------------------------------------------------------------------- blocks
BLOCKS: "OrderedDict[str, tuple]" = OrderedDict()


def block(name: str, *sources):
    """Register a block: its name, the records it reads (paths, or a callable giving them), and the function that writes it."""
    def wrap(fn):
        BLOCKS[name] = (sources, fn)
        return fn
    return wrap


def rel(p) -> str:
    return str(Path(p).relative_to(ROOT)) if Path(p).is_absolute() else str(p)


def sources_of(name: str) -> list:
    out = []
    for s in BLOCKS[name][0]:
        s = s() if callable(s) else s
        out += [rel(x) for x in (s if isinstance(s, (list, tuple)) else [s])]
    return out


# ---- the validity line and the engine
@block("validity", lambda: engine()["path"], AUDIT)
def b_validity():
    e, a = engine(), audit()
    return (f"Valid for {e['name']} (`{e['path'].name}`, digest `{e['digest']}`, {e['files']} fingerprinted files) and the verdict "
            f"audit's record `{a['digest']}` (`results/verdict_audit/VERDICT_AUDIT.json`); every count marked in this monograph is "
            "written from its record by `tools/monograph_words.py`, whose `--check` fails when one falls out of step.")


@block("engine", lambda: engine()["path"])
def b_engine():
    e = engine()
    return f"{e['name']}, digest `{e['digest']}`, {e['files']} files"


@block("engine_name", lambda: engine()["path"])
def b_engine_name():
    return engine()["name"]


def gate_path():
    k = engine()["n"]
    return ROOT / "results" / "model_gate" / f"V{k}_VS_V{k - 1}.json"


@block("model_gate", gate_path)
def b_model_gate():
    g = load(gate_path())
    total = same = 0
    for m in g["models"].values():
        for x in (m.get("gauges") or {}).values():
            if "cand_vs_base" in x:
                total += 1
                same += str(x["cand_vs_base"].get("word", "")).startswith("STEADY (identical)")
    k = len(g["models"])
    verdict = "identical" if same == total else f"identical on {n(same)} of {n(total)} readings"
    return (f"the model gate read {g['cand_engine']} against {g['base_engine']} {verdict} on all {n(k)} models, {n(total)} "
            f"readings and {'none' if total == same else n(total - same)} different (`{rel(gate_path()).replace('.json', '.md')}`, "
            "class S, modelled)")


# ---- the page, its stamp and its appraisal
@lru_cache(None)
def page_text():
    try:
        return PAGE.read_text(encoding="utf-8")
    except OSError as e:
        raise RecordError(f"the page cannot be read: {e}")


def embedded(key: str):
    page = page_text()
    tag = f'<script type="application/json" id="{key}">'
    if tag not in page:
        raise RecordError(f"the page carries no {key} record")
    a = page.index(tag) + len(tag)
    return json.loads(page[a:page.index("</script>", a)])


@block("page_stamp", STAMP)
def b_page_stamp():
    v = load(STAMP)
    pid = v.get("page_id")
    return (f"{v['engine']} (digest `{v['digest']}`), built {v['built_at']}, {n(v['bytes'])} bytes, SHA-256 {short(v['sha256'])}"
            + (f", page identity {short(pid)}" if pid else ", no page identity"))


@block("page_records", PAGE)
def b_page_records():
    ids = re.findall(r'<script type="application/json" id="([^"]+)">', page_text())
    runs = embedded("runs")
    rs = [r for bm in runs["benchmarks"] for r in bm["runs"]]
    files, ok = sum(r["checked"] for r in rs), sum(r["ok"] for r in rs)
    b = embedded("build")
    return (f"the page built {b['built_at']} carries {n(len(ids))} records; it plays back {n(len(runs['benchmarks']))} three-run "
            f"tables with {n(len(rs))} runs, and {n(ok)} of {n(files)} raw files matched their runs' own sums")


MANUAL = ROOT / "docs" / "OMNI_COMPASS_LIVE_ENGINE_MANUAL.md"


@lru_cache(None)
def manual_chapters() -> dict:
    """{anchor: chapter} as the Live Engine Manual names them ("This chapter reads the page's section …, (`#s-…`)")."""
    out, chapter = {}, None
    for line in MANUAL.read_text(encoding="utf-8").splitlines():
        h = re.match(r"## (\d+)\. ", line)
        if h:
            chapter = h.group(1)
        m = re.match(r"This chapter reads the page's sections? .*?\(`#(s-[\w-]+)`", line)
        if m and chapter:
            for a in re.findall(r"`#(s-[\w-]+)`", line):
                out.setdefault(a, chapter)
    return out


@block("page_sections", PAGE, MANUAL)
def b_page_sections():
    """Every section of the page in its own order: its number and title, its anchor, the monitors it draws (each monitor's
    number on the wall, its name and its evidence class, from the page's own monitor registry), the page's code and the
    Python each monitor names in its wiring, and the Live Engine Manual's chapter that reads it."""
    page = page_text()
    reg = {m["id"]: m for m in embedded("monitors")["monitors"]}
    secs = [(m.start(), m.group(1)) for m in re.finditer(r'<section[^>]*id="(s-[^"]+)"', page)]
    if not secs:
        raise RecordError("the page carries no section anchors")
    chapters = manual_chapters()
    L = ["| Section | Anchor | Monitors (number on the wall, name, class) | The page's code; the Python it ports or reads | "
         "Live Engine Manual |", "|---|---|---|---|---|"]
    for i, (at, sid) in enumerate(secs):
        chunk = page[at:secs[i + 1][0] if i + 1 < len(secs) else len(page)]
        h = re.search(r'<h[1-4][^>]*>\s*<span class="sn">([^<]*)</span>(.*?)</h[1-4]>', chunk, re.S)
        num, title = (h.group(1).strip(), re.sub(r"<[^>]+>", "", h.group(2)).strip()) if h else ("", sid)
        mons = [reg[c] for c in dict.fromkeys(re.findall(r'<canvas[^>]*id="([^"]+)"', chunk)) if c in reg]
        shown = "; ".join(f"{m['n']} {m['name']} ({m['cls']})" for m in mons) or "none (text, tables and controls)"
        code = sorted({c.strip() for m in mons for c in str((m.get("wire") or {}).get("code", "")).split(",") if c.strip()})
        py = sorted({p for m in mons for p in (m.get("wire") or {}).get("python") or []})
        wire = "; ".join(x for x in (", ".join(f"`{c}`" for c in code), ", ".join(f"`{p}`" for p in py)) if x) or "—"
        ch = chapters.get(sid)
        L.append(f"| {num} {title} | `#{sid}` | {shown} | {wire} | {'chapter ' + ch if ch else 'not named'} |")
    return "\n".join(L)


@lru_cache(None)
def appraisal_rows():
    """The appraisal's counts as docs/engine/build_live_engine.py wrote them between its markers at its last build."""
    t = APPRAISAL.read_text(encoding="utf-8")
    a = t.find("<!-- counts:")
    z = t.find("<!-- end counts -->")
    if a < 0 or z < 0:
        raise RecordError("docs/engine/APPRAISAL.md carries no counts block")
    rows = {}
    for line in t[a:z].splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 2 and line.startswith("| "):
            rows[cells[0]] = "|".join(cells[1:])
    return rows


def appraisal_row(prefix: str) -> str:
    for k, v in appraisal_rows().items():
        if k.startswith(prefix):
            return v
    raise RecordError(f"the appraisal's counts carry no row {prefix!r}")


@block("appraisal_counts", APPRAISAL)
def b_appraisal_counts():
    played = re.match(r"([\d,]+), with ([\d,]+) runs", appraisal_row("Three-run tables played back"))
    files = re.match(r"([\d,]+) of ([\d,]+) matched; ([\d,]+) unmatched", appraisal_row("Raw files checked"))
    key = next(k for k in appraisal_rows() if k.startswith("Omni-Compass against its native ("))
    tabs = re.search(r"\((\d+) tables\)", key)
    nat = appraisal_rows()[key]
    wrote = re.search(r"([\d,]+) LOSS", nat.split("(the page applies")[0])
    after = re.search(r"after it:.*?([\d,]+) LOSS", nat)
    floor = re.search(r"the floor of ([\d.]+)%", nat)
    same = appraisal_row("The page's receipts against the audit")
    if not (played and files and tabs and wrote):
        raise RecordError("the appraisal's counts are not in the form docs/engine/build_live_engine.py writes")
    return (f"{played.group(1)} three-run tables with {played.group(2)} runs played back from their raw files; {files.group(1)} of "
            f"{files.group(2)} raw files matched their runs' own sums, {files.group(3)} unmatched; Omni-Compass against its native "
            f"over {tabs.group(1)} tables, {wrote.group(1)} LOSS rows as the tables wrote them"
            + (f" and {after.group(1)} after the page's own {floor.group(1)}% floor at load" if after and floor else "")
            + f"; the page's receipts against the verdict audit: {same}")


@block("appraisal_method", APPRAISAL)
def b_appraisal_method():
    t = APPRAISAL.read_text(encoding="utf-8")
    py = re.search(r"the Python itself, on seeded inputs: ([^|]+?) \| largest difference ([^;|]+); ([^|]+?) \|", t)
    cc = re.search(r"\| ([\d,]+) seeded states and parameters \| largest relative difference ([^|]+?) \|", t)
    if not (py and cc):
        raise RecordError("the appraisal's method table is not in the form it was written in")
    return (f"against the Python on seeded inputs ({py.group(1).strip()}) the largest difference is {py.group(2).strip()}, and "
            f"{py.group(3).strip()}; against the C++ twin of the core on {cc.group(1)} seeded states, the largest relative "
            f"difference is {cc.group(2).strip()}")


# ---- the Omni index
@block("index_headline", INDEX_JSON, "tools/omni_index.py")
def b_index_headline():
    r = index_record()
    return combined(r["head"], r["service"])


@block("index_service", INDEX_JSON, "tools/omni_index.py")
def b_index_service():
    r = index_record()
    return combined(r["service"], r["service"])


@block("index_resource", INDEX_JSON, "tools/omni_index.py")
def b_index_resource():
    r = index_record()
    return combined(r["resource"], r["service"])


@block("index_tests", INDEX_JSON, "tools/omni_index.py")
def b_index_tests():
    ts = index_tests()
    stems = sorted({Path(t["source"]).stem for t in ts})
    eng = Counter(re.match(r"V(\d+)_", s).group(1) for s in stems)
    engines = series([f"{plural(k, 'table', 'tables')} on omni-v{e}" for e, k in sorted(eng.items(), key=lambda kv: -int(kv[0]))])
    per = Counter(t["category"] for t in ts)
    return (f"{plural(len(ts), 'test', 'tests')} from {plural(len(stems), 'three-run table', 'three-run tables')} ({engines}): "
            + "; ".join(f"{cat_name(c)} {per[c]}" for c in real_categories()))


@block("index_categories", INDEX_JSON, "tools/omni_index.py")
def b_index_categories():
    r = index_record()
    return "; ".join(f"{cat_name(c)} {combined(v, r['scats'].get(c))} over {plural(len(r['tests'][c]), 'test', 'tests')}"
                     for c, v in r["cats"].items())


@block("index_check", INDEX_JSON, "tools/omni_index.py")
def b_index_check():
    r = index_record()
    vals = [round(v, 3) for v in r["cats"].values()]
    gm = math.exp(sum(math.log(v) for v in vals) / len(vals))
    return f"({' × '.join(f'{v:.3f}' for v in vals)})^(1/{len(vals)}) ≈ {gm:.3f}"


@block("index_categories_table", INDEX_JSON, "tools/omni_index.py")
def b_index_categories_table():
    r = index_record()
    L = ["| Product | Tests | Index | Service reading (work and speed) | Work | Speed (native's 95th percentile against "
         "Omni-Compass's) | Resource held (native's against Omni-Compass's) |", "|---|---:|---|---|---|---|---|"]
    for c, v in r["cats"].items():
        L.append(f"| {cat_name(c)} | {len(r['tests'][c])} | {combined(v, r['scats'].get(c))} | "
                 f"{combined(r['scats'].get(c), r['scats'].get(c))} | {work_cell(avg(c, 'work'))} | {speed_cell(avg(c, 'speed'))} | "
                 f"{held_cell(avg(c, 'machines'), cat_resource(c))} |")
    return "\n".join(L)


def short_test(t: dict) -> str:
    return TEST.get(base_of(Path(t["source"]).stem)[0], t["test"].split(",")[0])


@block("index_kubernetes_table", INDEX_JSON, "tools/omni_index.py")
def b_index_kubernetes_table():
    c = OI.REAL[0]
    ts = index_record()["tests"].get(c) or []
    L = ["| Test | Index | Work | Speed (native's 95th percentile against Omni-Compass's) | Machines in service | Energy "
         "(a declared model) |", "|---|---|---|---|---|---|"]
    for t in ts:
        x = 1 + t["index_pct"] / 100
        s = None if t["service_pct"] is None else 1 + t["service_pct"] / 100
        L.append(f"| {short_test(t)} (`{Path(t['source']).stem}`) | {combined(x, s)} | {measure_cell(t, 'work', 'work')} | "
                 f"{measure_cell(t, 'speed', 'response')} | {measure_cell(t, 'machines', 'machines')} | "
                 f"{measure_cell(t, 'energy', 'energy')} |")
    return "\n".join(L)


@block("index_interval", INDEX_JSON, "tools/omni_index.py", "tools/readings.py", "omnicompass/student_t.py")
def b_index_interval():
    from omnicompass.student_t import t95
    r, runs = index_record(), index_by_run()["head"]
    logs = [math.log(x) for x in runs]
    mu = sum(logs) / 3
    sd = (sum((x - mu) ** 2 for x in logs) / 2) ** 0.5
    half = t95(2) * sd / 3 ** 0.5
    lo, hi = math.exp(mu - half) - 1, math.exp(mu + half) - 1
    def end(v):
        return f"{updown(v)} {pct(100 * v)}" if v else "no change"
    return (f"{combined(r['head'], r['service'])}, the three runs as replicates: each run's own index (every measure entering "
            f"at that run's ratio where its three-run reading is judged, else 1; composed as the headline is) reads run A "
            f"{end(runs[0] - 1)}, run B {end(runs[1] - 1)} and run C {end(runs[2] - 1)}, and the 95% interval of their mean runs "
            f"from {end(lo)} to {end(hi)} (Student t on 2 degrees of freedom, t = {t95(2):.3f}, as `evidence()` in "
            "`tools/readings.py` reads a gauge's runs, taken on the log of each run's index so that its centre is the "
            "headline); it measures how far the three runs' own indexes spread, not the choice of categories, their equal "
            "weights or which measures the key admits")


@block("index_leave_one_out", INDEX_JSON, "tools/omni_index.py")
def b_index_leave_one_out():
    r = index_record()
    cats = list(r["cats"])
    L = [f"- All {len(cats)} categories: {combined(r['head'], r['service'])}"]
    for c in cats:
        rest = [r["cats"][o] for o in cats if o != c]
        srest = [r["scats"][o] for o in cats if o != c and r["scats"].get(o)]
        x, s = OI.gmean(rest), OI.gmean(srest)
        line = f"- Without {cat_name(c)}, the other {len(rest)}: {combined(x, s)}"
        if x is not None and x < 1 and OI.index_word(x, s) == GIVEN:
            line += (f" (its service reading {combined(s, s)}: the resources put in outweigh what they bought on the index's "
                     "equal weights, so the word is power given, not LOSS)")
        L.append(line)
    return "\n".join(L)


@lru_cache(None)
def scored_gauges() -> frozenset:
    """(table, section, gauge) of every measure the index scores (work, speed, machines; energy only where a meter read it),
    as tools/omni_index.py picks each one's row."""
    out = set()
    for t in index_tests():
        stem = Path(t["source"]).stem
        kind, measures, extra = _source_of(t)
        data = load(ROOT / t["source"])
        for m, key in measures.items():
            if m == "energy" and OI.scored_ratio(t["category"], m, 0.5) == 1.0:
                continue
            if kind == "rows":
                out.add((stem, "", key))
            else:
                gauges = data["workloads"][extra]
                for k in (key if isinstance(key, tuple) else (key,)):
                    g = gauges.get(k)
                    if g and g.get("runs") and not any(x is None for x in g["runs"]):
                        out.add((stem, extra, k))
                        break
        if kind == "rows" and extra == "capacity":
            out.add((stem, "", OI.CAPACITY if OI.CAPACITY in data["rows"] else OI.CAPACITY_NOW))
    return frozenset(out)


@block("index_loss_rows", AUDIT, INDEX_JSON, LEDGER)
def b_index_loss_rows():
    stems = {Path(t["source"]).stem for t in index_tests()}
    rows = [r for r in native_losses() if r["table"] in stems]
    scored = [r for r in rows if (r["table"], r["section"], r["gauge"]) in scored_gauges()]
    which = series([f"{named(r['table'])}'s {gauge_name(r)}" for r in scored])
    return (f"{n(len(rows))} of the {n(len(native_losses()))} rows against native sit in the index's own "
            f"{n(len(stems))} tables: {grouped(rows)}; {n(len(scored))} of the {n(len(rows))} on a measure the index scores"
            + (f" ({which})" if scored else ""))


@block("index_loss_table", AUDIT, INDEX_JSON)
def b_index_loss_table():
    stems = {Path(t["source"]).stem for t in index_tests()}
    rows = sorted((r for r in native_losses() if r["table"] in stems), key=lambda r: (r["table"], r["section"], r["gauge"]))
    L = ["| Table | Gauge | Reading | Runs A, B and C | Strength |", "|---|---|---|---|---|"]
    for r in rows:
        ev = r.get("evidence") or {}
        L.append(f"| {named(r['table'], ref=True)} | {gauge_name(r)} | {bare(r['recomputed'])} | "
                 f"{', '.join(run_size(x) for x in r['runs'])} | {ev.get('strength') or 'not given'} |")
    return "\n".join(L)


# ---- the LOSS ledger
@block("loss_all", LEDGER, AUDIT, "tools/loss_ledger.py")
def b_loss_all():
    rows, _ = ledger()
    a, b, c = (len(rows[s]) for s in LL.SECTIONS)
    return (f"{n(a + b + c)} rows read LOSS across their three runs in every benchmark's newest table: {n(a)} against "
            f"Omni-Compass's own native, the rows do no harm is judged by; {n(b)} in place of a controller; {n(c)} without "
            "Omni-Compass, or with two changes at once")


@block("loss_against_native", LEDGER, AUDIT)
def b_loss_against_native():
    return n(len(native_losses()))


@block("loss_by_engine", AUDIT)
def b_loss_by_engine():
    c = audit()["counts"]["standing_against_native_by_engine"]
    parts = sorted(((int(e.split("v")[-1]), e, v.get(LOSS, 0)) for e, v in c.items() if v.get(LOSS)), reverse=True)
    return series([f"{n(k)} on {e}" for _, e, k in parts])


@block("loss_by_aim", AUDIT)
def b_loss_by_aim():
    c = audit()["counts"]["standing_against_native_by_direction"]
    parts = sorted(((v.get(LOSS, 0), d) for d, v in c.items() if v.get(LOSS)), reverse=True)
    return series([f"{n(k)} on {d}" for k, d in parts])


@block("loss_by_strength", AUDIT)
def b_loss_by_strength():
    c = audit()["counts"]["standing_against_native_strength"].get(LOSS, {})
    order = ("strong", "moderate", "weak", "inconclusive")
    return series([f"{n(c.get(k, 0))} {k}" for k in order] + [f"{n(v)} {k}" for k, v in c.items() if k not in order])


@block("loss_by_class", AUDIT)
def b_loss_by_class():
    c = audit()["counts"]["standing_against_native_by_class"]
    parts = [(cl, v.get(LOSS, 0)) for cl, v in c.items() if v.get(LOSS)]
    total = sum(k for _, k in parts)
    if len(parts) == 1:
        return f"all {n(total)} class {parts[0][0]}"
    return series([f"{n(k)} class {cl}" for cl, k in parts])


PLACE_ORDER = (("cluster", "the cluster's own tests"), ("stores", "the data stores"),
               ("two_way", "the two-way tables of the batch-stream rigs"), ("top", "the four ways, Omni-Compass on top of the product"),
               ("bare", "the four ways, Omni-Compass on the organism alone"), ("simulators", "the outside simulators"))


@block("loss_by_place", AUDIT, LEDGER)
def b_loss_by_place():
    by = defaultdict(Counter)
    for r in native_losses():
        by[place(r["table"])][r["table"]] += 1
    have = Counter(place(s) for s in tables() if standing_native(s))
    parts = []
    for key, label in PLACE_ORDER:
        if not by[key]:
            continue
        txt = f"{n(sum(by[key].values()))} on {label}, in {len(by[key])} of their {have[key]} tables"
        if key == "two_way":
            txt += " (" + ", ".join(f"{PRODUCT.get(base_of(s)[0], s)} {k}" for s, k in sorted(by[key].items(), key=lambda kv: order_key(kv[0]))) + ")"
        parts.append(txt)
    return "; ".join(parts)


@block("loss_most", AUDIT)
def b_loss_most():
    c = Counter(r["table"] for r in native_losses())
    top = max(c.values())
    names = [named(s, ref=True) for s, k in sorted(c.items()) if k == top]
    return f"{series(names)}, {n(top)} {'each' if len(names) > 1 else ''}".rstrip()


@block("loss_cluster_by_gauge", AUDIT)
def b_loss_cluster_by_gauge():
    rows = [r for r in native_losses() if place(r["table"]) == "cluster"]
    by = defaultdict(list)
    for r in rows:
        by[gauge_group(r)].append(r["table"])
    parts = []
    for g in GROUP_ORDER:
        if by[g]:
            c = Counter(by[g])
            parts.append(f"{g} {len(by[g])} (" + ", ".join(f"{named(s)} {k}" for s, k in sorted(c.items())) + ")")
    return f"{n(len(rows))} on the cluster's own tests: " + "; ".join(parts)


@block("loss_stores", AUDIT, INDEX_JSON)
def b_loss_stores():
    counted = {Path(OI.newest(f)).stem for _, f, _, _ in OI.WORKLOAD_TABLES}
    rows = [r for r in native_losses() if place(r["table"]) == "stores"]
    a = [r for r in rows if r["table"] in counted]
    b = [r for r in rows if r["table"] not in counted]
    def by(rs):
        c = Counter(TEST.get(base_of(r["table"])[0].split("_")[0], r["table"]) for r in rs)
        return ", ".join(f"{k} {v}" for k, v in sorted(c.items()))
    return (f"{n(len(rows))} on the stores' tables: {n(len(a))} on the counted tables ({by(a)}) and {n(len(b))} on the "
            f"service-objective and shipped-native sets ({by(b)})")


@block("loss_stores_rows", AUDIT)
def b_loss_stores_rows():
    rows = sorted((r for r in native_losses() if place(r["table"]) == "stores"), key=lambda r: (r["table"], r["section"], r["gauge"]))
    L = ["| Table | Workload | Gauge | Reading | Strength |", "|---|---|---|---|---|"]
    for r in rows:
        L.append(f"| {named(r['table'], ref=True)} | `{r['section']}` | {STORE_GAUGE.get(r['gauge'], r['gauge'])} | {reading(r)} | "
                 f"{(r.get('evidence') or {}).get('strength') or '—'} |")
    return "\n".join(L)


@block("loss_causes", LEDGER, "tools/loss_ledger.py", AUDIT)
def b_loss_causes():
    rows = ledger_native()
    c = Counter(k for *_, k in rows)
    total = len(rows)
    written = total - c["none"]
    parts = []
    if c["flip"]:
        parts.append(f"{n(c['flip'])} an engine fault of {engine()['name']} found in the files (the web service's autoscaler target "
                     "flipping at the fail-up's floor)")
    if c["flip_queue"]:
        parts.append(f"{n(c['flip_queue'])} queue rows that name the same flip, the control plane's reads suspected beside it")
    if c["suspected"]:
        parts.append(f"{n(c['suspected'])} queue rows suspected, not yet measured (the control plane's reads at the 10 s beat)")
    if c["beat"]:
        parts.append(f"{n(c['beat'])} measured (the plain batch queue: Omni-Compass's own processor on a shared runner)")
    if c["other"]:
        parts.append(f"{n(c['other'])} with another cause written")
    return (f"{n(written)} of the {n(total)} carry a written cause and {n(c['none'])} read \"not yet written\": "
            + "; ".join(parts))


def flip_rows():
    return [x for x in ledger_native() if x[4] in ("flip", "flip_queue")]


@block("flip_rows", LEDGER, "tools/loss_ledger.py", FLIP_PAGE)
def b_flip_rows():
    rows = ledger_native()
    web = [x for x in rows if x[4] == "flip"]
    queue = [x for x in rows if x[4] == "flip_queue"]
    nxt = f"omni-v{engine()['n'] + 1}"
    fix = [x for x in rows if x[3] and nxt in (x[3][2] + " " + x[3][3])]
    return (f"{n(len(web))} rows on {plural(len({x[0] for x in web}), 'table', 'tables')} carry the fault as their cause, all on "
            f"the web service ({grouped([x[2] for x in web], ', ')}), and {n(len(queue))} queue rows on "
            f"{plural(len({x[0] for x in queue}), 'table', 'tables')} name it beside the control plane's reads "
            f"({grouped([x[2] for x in queue], ', ')}); together {n(len(web) + len(queue))} of the {n(len(rows))} rows against "
            f"native, and {n(len(fix))} name {nxt} as their fix")


@block("flip_tables", LEDGER, "tools/loss_ledger.py")
def b_flip_tables():
    c = defaultdict(lambda: [0, 0])
    for stem, _g, _r, _c, k in flip_rows():
        c[stem][0 if k == "flip" else 1] += 1
    return "; ".join(f"{named(s, ref=True)}: {plural(w, 'web row', 'web rows')}, {plural(q, 'queue row', 'queue rows')}"
                     for s, (w, q) in sorted(c.items(), key=lambda kv: order_key(kv[0])))


def grab(pattern: str, text: str, what: str):
    m = re.search(pattern, text)
    if not m:
        raise RecordError(f"the cause text in tools/loss_ledger.py no longer states {what}")
    return m


@block("flip_evidence", "tools/loss_ledger.py", FLIP_PAGE)
def b_flip_evidence():
    t, q = LL.FLIP[0], LL.FLIP_QUEUE[0]
    cover = grab(r"floor \((\d+%)\) and native's \((\d+%)\)", t, "the two targets")
    flips = grab(r"(\d[\d,]*) flips over (\d+) repetitions, the hold caught on (\d+) times", t, "the count of flips")
    rep = grab(r"run (\d+), repetition (\d+): (\d+) target writes in (\d+) s, the hold only at ([\d.]+) s, with (\d+) of the "
               r"queue's pods waiting and all (\d+) web pods Ready", t, "the repetition read write by write")
    after = grab(r"serve (\d+% to \d+%) faster than native in all (\d+) repetitions", t, "the reading after the queue")
    queue = grab(r"the queue finished (\d[\d.]*% to \d[\d.]*%) later", q, "the queue's delay")
    return (f"the target flips between the cover's floor ({cover.group(1)}) and native's ({cover.group(2)}) every one or two "
            f"decisions: {flips.group(1)} flips over {flips.group(2)} repetitions of the KAI scheduler's four ways, the hold caught "
            f"on {flips.group(3)} times; in run {rep.group(1)}, repetition {rep.group(2)}, {rep.group(3)} target writes in "
            f"{rep.group(4)} s and the hold only at {rep.group(5)} s, with {rep.group(6)} of the queue's pods waiting and all "
            f"{rep.group(7)} web pods Ready; where the queue ran long the queue finished {queue.group(1)} later; after the queue "
            f"the same arms served {after.group(1)} faster than native in all {after.group(2)} repetitions")


@block("beat_load_cause", "tools/loss_ledger.py", "docs/LOSS_CAUSES_2026-11-05.md")
def b_beat_load_cause():
    t = LL.BEAT_LOAD[0]
    own = grab(r"(\d\.\d+ to \d\.\d+) of a core over each window", t, "its own processor at the beat")
    old = grab(r"against (\d\.\d+ to \d\.\d+) at omni-v(\d+)'s (\d+) s beat", t, "the older beat's processor")
    pods = grab(r"about (\d[\d.]*) of the runner's (\w+) cores, so about (\d[\d.]*%)", t, "the batch pods' share")
    return (f"Omni-Compass's own processor read {own.group(1)} of a core over each window at the 10 s beat, against {old.group(1)} "
            f"at omni-v{old.group(2)}'s {old.group(3)} s beat; the batch pods ran on about {pods.group(1)} of the runner's "
            f"{pods.group(2)} cores, so about {pods.group(3)} of their processor went to it, the size of the queue's rise")


# ---- the verdict audit
@block("audit_tables", AUDIT)
def b_audit_tables():
    c = audit()["counts"]
    st = c["tables"]
    return (f"{n(sum(st.values()))} three-run tables ("
            + ", ".join(f"{n(st.get(k, 0))} {k}" for k in VA.STATUSES) + f"); {n(c['recomputed'])} of their {n(c['rows'])} rows "
            f"recomputed by the one key, {n(c['stored_readings_the_key_reads_otherwise'])} stored readings the key reads otherwise "
            f"and {n(c['markdown_readings_unlike_their_json'])} Markdown readings unlike their JSON twin")


@block("audit_standing", AUDIT)
def b_audit_standing():
    c = audit()["counts"]
    st = c["tables"].get("standing", 0)
    return (f"{n(c['standing_tables_against_native'])} standing tables against native; {n(c['standing_tables_on_the_engine_that_stands'])} "
            f"of the {n(st)} standing tables on {audit()['engine_standing']}, {n(c['standing_tables_not_yet_rerun'])} not yet run "
            "again on it")


@block("audit_counts_table", AUDIT)
def b_audit_counts_table():
    w = audit()["counts"]["words"]
    L = ["| Comparison | GAIN | power given | STEADY | LOSS | the runs disagree | shown |", "|---|---:|---:|---:|---:|---:|---:|"]
    for comp in VA.COMPARISONS:
        c = w.get(f"standing | {comp}", {})
        L.append(f"| {comp} | " + " | ".join(n(c.get(k, 0)) for k in COUNT_WORDS) + " |")
    first = w.get(f"standing | {VA.COMPARISONS[0]}", {})
    extra = [f"{n(first[k])} *{k}*" for k in ("the runs differ", "tuning") if first.get(k)]
    if extra:
        L += ["", f"The first row also carries {series(extra)} (a tuning workload is shown and never counted)."]
    return "\n".join(L)


@block("audit_by_class", AUDIT)
def b_audit_by_class():
    c = audit()["counts"]["standing_against_native_by_class"]
    def say(cl):
        v = c.get(cl, {})
        parts = [f"{n(v[k])} {k}" for k in (GAIN, GIVEN, STEADY, LOSS, DISAGREE, "the runs differ") if v.get(k)]
        return series(parts + ([] if v.get(LOSS) else ["no LOSS"]))
    out = [f"class {cl} reads {say(cl)}" for cl in sorted(c)]
    return "; ".join(out)


@block("audit_inconclusive", AUDIT)
def b_audit_inconclusive():
    c = audit()["counts"]
    s = c["standing_against_native_strength"]
    return (f"{n(s.get(LOSS, {}).get('inconclusive', 0))} LOSS and {n(s.get(GAIN, {}).get('inconclusive', 0))} GAIN rows are "
            f"inconclusive, and {n(c['standing_against_native'].get(DISAGREE, 0))} rows read the runs disagree")


@block("audit_steady_kinds", AUDIT)
def b_audit_steady_kinds():
    c = audit()["counts"]
    s = c["standing_against_native_steady"]
    return (f"{n(c['standing_against_native'].get(STEADY, 0))} STEADY rows: {n(s.get('exactly the same', 0))} exactly the same and "
            f"{n(s.get('under the floor', 0))} under the floor")


@block("audit_discrepancies", DISCREPANCIES)
def b_audit_discrepancies():
    d = load(DISCREPANCIES)
    k = lambda kind: sum(1 for x in d["rows"] if kind in x["kinds"] and x["status"] == "standing")
    return (f"against the tables as committed at `{d['base']}`, {n(k('sign'))} rows of the standing tables whose printed change "
            f"had worn the word's sign now carry the raw change's true sign, and {n(k('renamed'))} changed only by the rename to "
            "STEADY; no raw measurement changed")


# ---- the oversight line
@block("oversight", OVERSIGHT)
def b_oversight():
    o = load(OVERSIGHT)
    p = o["pooled"]
    return (f"over {n(o['count']['tests'])} {o['engine']} Kubernetes tests the alert minutes of a repetition, summed, fall from "
            f"{p['native']:.1f} on native to {p['omni']:.1f} with Omni-Compass on top: {bare(p['reading'])}, "
            f"{updown(p['change'])} {pct(100 * p['change'])}")


@block("oversight_runs_table", OVERSIGHT)
def b_oversight_runs_table():
    p = load(OVERSIGHT)["pooled"]
    L = ["| Run | Native → Omni-Compass, summed | Reading | 95% interval, minutes fewer |", "|---|---|---|---|"]
    for tag, r in zip("ABC", p["runs"]):
        w = key_word(r["change"] < 0, LOWER) if abs(r["change"]) >= SIZE_FLOOR else STEADY
        lo, hi = sorted(-x for x in r["ci95"])
        L.append(f"| {tag} | {r['native']:.2f} → {r['omni']:.2f} | {w}, {updown(r['change'])} {pct(100 * r['change'])} | "
                 f"{lo:.2f} to {hi:.2f} |")
    return "\n".join(L)


@block("oversight_count", OVERSIGHT)
def b_oversight_count():
    c = load(OVERSIGHT)["count"]
    return (f"fewer in {n(c['fewer'])} tests, falling to none in {n(c['to_zero'])}; the same in {n(c['same'])}; more in "
            f"{n(c['more'])}")


@block("oversight_loss_all_three", OVERSIGHT)
def b_oversight_loss_all_three():
    rows = [r for r in load(OVERSIGHT)["rows"] if bare(r["reading"]).startswith(f"{LOSS} in all three")]
    each = [f"{named(Path(r['record']).stem)}, {updown(r['change'])} {pct(100 * r['change'])}" for r in rows]
    return f"{plural(len(rows), 'test reads', 'tests read')} LOSS in all three of our runs, more minutes over the line: " + "; ".join(each)


@block("oversight_largest_share", OVERSIGHT)
def b_oversight_largest_share():
    o = load(OVERSIGHT)
    r = max(o["rows"], key=lambda x: x["native"])
    return (f"{named(Path(r['record']).stem)} holds {pct(100 * r['native'] / o['pooled']['native'])} of native's minutes, the "
            "largest share of any test")


@block("oversight_example", OVERSIGHT)
def b_oversight_example():
    e = load(OVERSIGHT)["example"]
    return f"{e['share'] * 100:.0f}%"


# ---- the four arms, the chip and the cloud
@block("four_arms_table", SITE)
def b_four_arms_table():
    a = load(SITE)["four_arms"]
    L = ["| Arm | What it is | Place and bill | Class | Engine | Receipt |", "|---|---|---|---|---|---|"]
    for k in ("A", "B", "C", "D"):
        x = a[k]
        rec = ", ".join(f"`{r}`" for r in re.findall(r"results/[\w./-]+\.md", x["receipt"]))
        L.append(f"| {k} | {x['name']} | {x['place']} | {x['class']} | {x['engine']} | {rec} |")
    return "\n".join(L)


def chip_rows():
    return load(TWO_BILLS)["chip"]["rows"]


def chip_row(prefix: str):
    for k, v in chip_rows().items():
        if k.startswith(prefix):
            return v
    raise RecordError(f"results/TWO_BILLS.json carries no chip row {prefix!r}")


def one_word(change: float, aim_: str) -> str:
    if round(100 * change, 2) == 0:
        return "STEADY, unchanged (0.00%)"
    if abs(change) < SIZE_FLOOR:
        return f"STEADY, {updown(change)} {pct(100 * change, 2)}"
    return f"{key_word(change < 0, aim_)}, {updown(change)} {pct(100 * change, 2)}"


@block("chip_bill_table", SITE, TWO_BILLS)
def b_chip_bill_table():
    a = load(SITE)["four_arms"]
    tb = load(TWO_BILLS)
    L = ["| Place | Run | Work, ΔW | Bill, ΔB | G, the work for the bill |", "|---|---|---|---|---|"]
    for i, (ra, rb) in enumerate(zip(a["A"]["runs"], a["B"]["runs"]), 1):
        dw, db = rb["work"] / ra["work"] - 1, rb["bill_usd"] / ra["bill_usd"] - 1
        g = rb["work_per_dollar"] / ra["work_per_dollar"] - 1
        L.append(f"| the chip, arm B against arm A | {i} | {one_word(dw, HIGHER)} | {one_word(db, SPENT)} | {one_word(g, HIGHER)} |")
    L.append(f"| the chip, three runs | | **{bare(chip_row('work done')['reading'])}** | {bare(chip_row('bill')['reading'])} | "
             f"**{bare(chip_row('work per dollar')['reading'])}** |")
    cl = tb["cloud"]
    b = cl["bill"]
    db = b["diff"] / b["native"]
    noise = "beyond the noise" if b.get("significant") else "inside the noise"
    work = "not counted" if not cl.get("work") else "counted"
    L.append(f"| the cloud, arm D against arm C | one set of {cl['repetitions']} paired repetitions | {work} | "
             f"{one_word(db, SPENT)}, {noise} | {'not read' if work == 'not counted' else 'read'} |")
    return "\n".join(L)


@block("chip_energy", TWO_BILLS)
def b_chip_energy():
    r = chip_row("energy per served request")
    ch = [100 * (x["omni"] - x["native"]) / x["native"] for x in r["runs"]]
    return (f"{bare(r['reading'])}, {updown(sum(ch))} {pct(sum(ch) / 3)} by the mean ("
            + ", ".join(f"{updown(c)} {pct(c, 2)}" for c in ch) + " by run)")


@block("chip_card_energy", TWO_BILLS)
def b_chip_card_energy():
    r = chip_row("energy, GPU")
    ch = [100 * (x["omni"] - x["native"]) / x["native"] for x in r["runs"]]
    under = [i + 1 for i, c in enumerate(ch) if abs(c) < 100 * SIZE_FLOOR]
    return (f"the card's energy {bare(r['reading'])}, {series([f'{updown(c)} {pct(c, 2)}' for c in ch])} by run"
            + (f"; run {series([str(i) for i in under])}'s own word STEADY, under the floor" if under else ""))


@block("chip_requests", TWO_BILLS)
def b_chip_requests():
    r = chip_row("work done")
    return "; ".join(f"from {x['native']:,.0f} to {x['omni']:,.0f}" for x in r["runs"]) + f": {bare(r['reading'])}"


@block("chip_p95", TWO_BILLS)
def b_chip_p95():
    r = chip_row("response time, 95th percentile")
    ch = [100 * (x["omni"] - x["native"]) / x["native"] for x in r["runs"]]
    return (f"{bare(r['reading'])} (" + ", ".join(f"run {i} {'shorter' if c < 0 else 'longer'} by {pct(c, 2)}"
                                                for i, c in enumerate(ch, 1)) + ")")


@lru_cache(None)
def gauge_directions():
    """Each gauge's declared direction as the three-run tables on Kubernetes record it (the same scorer, tools/live_reps.py)."""
    out = {}
    for r in audit()["rows"]:
        t = tables()[r["table"]]
        if t["stack"] == "Kubernetes" and not r.get("section") and r.get("direction"):
            out.setdefault(r["gauge"], r["direction"])
    return out


DIRECTION_AIM = {"work done": HIGHER, "time waited, missed or failed": LOWER, "resource spent or held": SPENT,
                 "work per resource": WORK_PER}


@block("cloud_set", AKS_JSON, AKS_MD, SITE)
def b_cloud_set():
    c = load(SITE)["four_arms"]["C"]
    m = re.search(r"Run (\d{8,})", AKS_MD.read_text(encoding="utf-8"))
    return (f"one set of {c['repetitions']} paired repetitions" + (f", run {m.group(1)}" if m else "") + f", on {c['engine']}")


@block("cloud_table", AKS_JSON, AUDIT)
def b_cloud_table():
    p = load(AKS_JSON)["paired"]["compass"]
    dirs = gauge_directions()
    L = ["| Gauge | C, native | D, Omni-Compass on native | Reading | Why |", "|---|---:|---:|---|---|"]
    for g, x in p.items():
        d = dirs.get(g) or ("resource spent or held" if g in ("machines billed, machine-hours", "compute bill at list price ($)") else None)
        aim_ = DIRECTION_AIM.get(d)
        if aim_ is None or x.get("native") in (None, 0) or x.get("omni") is None or x["native"] != x["native"]:
            continue
        ch = x["diff"] / abs(x["native"])
        noise = "beyond the noise" if x.get("significant") else "inside the noise"
        if abs(ch) < SIZE_FLOOR:
            w, txt = STEADY, f"STEADY, under the floor ({pct(100 * ch)})"
        else:
            w = key_word(ch < 0, aim_)
            txt = f"{w}, {updown(ch)} {pct(100 * ch)}, {noise}"
        L.append(f"| {g} | {num(x['native'])} | {num(x['omni'])} | {txt} | {why({'word': w, 'direction': d, 'recomputed': ''})} |")
    L += ["", f"Every judged gauge of the set: the mean of the {load(SITE)['four_arms']['C']['repetitions']} paired repetitions with its "
          "95% interval, one run, so no three-run reading exists; the energy rows are declared models, never a meter."]
    return "\n".join(L)


# ---- the whole-system composition
def whole_key():
    t = load(WHOLE)["totals"]
    for k in t:
        if k.startswith("without the card") and k.endswith("| index"):
            return k
    raise RecordError("results/WHOLE_SYSTEM.json carries no reading without the card by the index's rule")


@block("whole_system", WHOLE)
def b_whole_system():
    w = load(WHOLE)
    x = w["totals"][whole_key()]
    mu, si, sc = x["index"]["mu"], x["index"]["sigma_independent"], x["index"]["sigma_correlated"]
    e = lambda v: math.exp(v) - 1
    work, speed, mach = (math.exp(x["total"][g][0]) for g in ("work", "speed", "machines"))
    lay = {k.split(". ", 1)[1].split(",")[0]: len(v) for k, v in w["layers"].items()}
    cluster = next((v for k, v in lay.items() if k.startswith("the cluster")), 0)
    services = next((v for k, v in lay.items() if k.startswith("the services")), 0)
    word = GAIN if mu > 0 else LOSS
    span = lambda s: f"{updown(e(mu - 1.96 * s))} {pct(100 * e(mu - 1.96 * s))} to {updown(e(mu + 1.96 * s))} {pct(100 * e(mu + 1.96 * s))}"
    held = (f"power given, native's {pct(100 * (1 - mach))} below Omni-Compass's (×{mach:.4f}), that is, "
            f"{pct(100 * (1 / mach - 1))} more held" if mach < 1 else
            f"GAIN, a cut, native's {pct(100 * (mach - 1))} above Omni-Compass's (×{mach:.4f})")
    return (f"{word}, {updown(mu)} {pct(100 * e(mu))} (×{math.exp(mu):.4f}; gauges independent, {span(si)}; gauges correlated, "
            f"{span(sc)}); work {work_cell(work)}; speed {speed_cell(speed)}, that is, the 95th-percentile response "
            f"{pct(100 * abs(1 - 1 / speed))} {'shorter' if speed > 1 else 'longer'}; machines and resources held {held}; the "
            f"cluster's {cluster} tests and the services' {services} (`results/WHOLE_SYSTEM.md`, class S: a composition of "
            "measured layers, never one stacked run)")


@block("whole_separability", WHOLE)
def b_whole_separability():
    s = load(WHOLE)["separability"]
    agree = sum(1 for x in s if x["agree"])
    return f"{n(agree)} of {n(len(s))} pairs of orchestrator and gauge agree within the noise; {n(len(s) - agree)} do not"


@block("whole_on_top_ratios", WHOLE)
def b_whole_on_top_ratios():
    by = defaultdict(dict)
    for x in load(WHOLE)["separability"]:
        by[x["governor"]][x["gauge"]] = math.exp(x["top"][0])
    return ("the factors measured with Omni-Compass on top of each product, oriented so that above 1 is a GAIN (native's over "
            "Omni-Compass's for speed, machines and energy): "
            + "; ".join(f"{g}, " + ", ".join(f"{k} ×{v:.4f}" for k, v in sorted(d.items(), key=lambda kv: ("speed", "machines", "energy").index(kv[0]) if kv[0] in ("speed", "machines", "energy") else 9)) for g, d in by.items()))


# ---- the Python's 500 runs, the core's twin and the injection grid
@lru_cache(None)
def newest_by_written(pattern: str):
    found = []
    for p in ROOT.glob(pattern):
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if d.get("written"):
            found.append((d["written"], p.name, p, d))
    if not found:
        raise RecordError(f"no record matches {pattern}")
    return max(found)[2:]


@block("engine_runs", lambda: newest_by_written("results/engine_runs/ENGINE_RUNS_*.json")[0])
def b_engine_runs():
    p, d = newest_by_written("results/engine_runs/ENGINE_RUNS_*.json")
    c = d.get("cpp") or {}
    sets = len(list((ROOT / "results" / "engine_runs").glob("ENGINE_RUNS_*.json")))
    twin = (f"the C++ harness gave the same digest on the same draws, {n(c.get('agree', 0))} of {n(d['runs'])} runs agreeing to 1e-9, "
            f"largest difference {c.get('largest_difference', float('nan')):.1e}" if c.get("same") else
            "the C++ harness's digest differs")
    return (f"the newest record, base {d['base']}, written {d['written']} on {d['engine'].split(' (')[0]}: {n(d['runs'])} runs, "
            f"{d['decisions']} decisions of the brain, {d['law_steps']} steps of the compass law and one give-back trial each, "
            f"digest {short(d['digest'])}; {twin} (`{rel(p).replace('.json', '.md')}`, the newest of {n(sets)} sets on file)")


@block("core_runs", lambda: newest_by_written("results/core_runs/CORE_RUNS_500_*.json")[0])
def b_core_runs():
    p, d = newest_by_written("results/core_runs/CORE_RUNS_500_*.json")
    s, c = d["summary"], d.get("cpp") or {}
    return (f"base {d['base']}, written {d['written']}: Omni-Compass on top conveyed {n(s['controlled']['conveyed'])} and certified "
            f"{n(s['controlled']['certified'])} of {n(d['runs'])}, the plant alone conveyed {n(s['uncontrolled']['conveyed'])} and "
            f"certified {n(s['uncontrolled']['certified'])}; the C++ twin {n(c.get('agree', 0))} of {n(c.get('of', 0))} run-ways "
            f"agreeing to 1e-9, " + ("one digest " if c.get("same") else "the digests differ, ") + f"{short(d['digest'])} "
            f"(`{rel(p).replace('.json', '.md')}`)")


def core_seed() -> int:
    tree = ast.parse(CORE_EVIDENCE_PY.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "main":
            args = node.args.args[-len(node.args.defaults):]
            for a, v in zip(args, node.args.defaults):
                if a.arg == "seed":
                    return ast.literal_eval(v)
    raise RecordError("benchmarks/core_evidence.py's main() names no seed")


@block("core_evidence", CORE_EVIDENCE, CORE_EVIDENCE_PY)
def b_core_evidence():
    e = load(CORE_EVIDENCE)
    c, u = e["controlled"], e["uncontrolled"]
    return (f"seed {core_seed()}: Omni-Compass on top conveyed {n(c['convey5'])} and certified {n(c['cert10'])} of {n(c['runs'])} "
            f"runs, its command peaking at {c['actuator_peak']:.2f}; the plant alone conveyed {n(u['convey5'])} and certified "
            f"{n(u['cert10'])}")


@lru_cache(None)
def newest_grid():
    found = []
    for p in (ROOT / "results" / "injection_grid").glob("INJECTION_GRID_*.json"):
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        found.append(((d.get("run") or {}).get("started", ""), (d.get("batch") or {}).get("written", ""), p.name, p, d))
    if not found:
        raise RecordError("no injection grid on file")
    return max(found)[3:]


@block("injection_grid", lambda: newest_grid()[0])
def b_injection_grid():
    p, d = newest_grid()
    b, t, lc = d["batch"], d["tiers"], d.get("loss_cells") or {}
    same = "the same" if b.get("cpp_same") else "different"
    return (f"the newest grid, run {d['run']['started']} on batch {b['base']} ({n(b['runs'])} injections; the Python's and the C++'s "
            f"digests {same}, {n(b.get('cpp_agree', 0))} runs agreeing): {n(len(d['organisms']))} organisms and "
            f"{n(len(d['governors']))} governors at {series([n(x) for x in t['runs']])} runs × {series([n(x) for x in t['copies']])} "
            f"copies, class {d['class']}; {n(lc.get('omni', 0))} LOSS cells for Omni-Compass on native and "
            f"{n(lc.get('governors', 0))} among the governors' own ways against native (`{rel(p).replace('.json', '.md')}`)")


# ---- the release, the receipt and the seal
@block("release_manifest", MANIFEST)
def b_release_manifest():
    m = load(MANIFEST)
    r = m["verification_receipt"]
    return (f"release `{m['release_id']}`, written at commit `{m['written_at_commit'][:12]}` on {m['written_at']}; its receipt "
            f"`{r['file']}` (SHA-256 {short(r['sha256'])}) marked " + ("passed" if r.get("passed") else "not passed"))


@block("verify_receipt", RECEIPT)
def b_verify_receipt():
    t = RECEIPT.read_text(encoding="utf-8")
    head = re.match(r"verify\.py( --quick)? at commit ([0-9a-f]{7,40}), (\S+)", t)
    passes, fails = len(re.findall(r"^PASS", t, re.M)), len(re.findall(r"^FAIL", t, re.M))
    last = [x for x in t.strip().splitlines() if x.strip()][-1].strip()
    core = re.search(r"C\+\+ core vs (\d+) fixtures\s+\(max abs ([0-9.e+-]+)\)", t)
    gov = re.findall(r"C\+\+ vs Python governor \((\w+), a step every 60 s\): (\d+) directives, discrete mismatches = 0", t)
    seal = re.search(r"seal: all (\d+) Python/C\+\+ twins unchanged", t)
    shield = re.search(r"shield properties over ([\d,]+) cases: \{([^}]*)\}", t)
    neg = len(re.findall(r"PASS\s+negative control", t))
    if not head:
        raise RecordError("results/VERIFY_RECEIPT.txt does not open with verify.py's own line")
    parts = [f"`verify.py{head.group(1) or ''}` at commit `{head.group(2)[:12]}` on {head.group(3).rstrip(',')}: {n(passes)} "
             f"checks PASS, {n(fails)} FAIL, the last line \"{last}\""]
    if core:
        parts.append(f"the C++ core against {core.group(1)} fixtures to a largest absolute difference of {core.group(2)}")
    if gov:
        parts.append(f"the C++ twins against the Python in {len(gov)} profiles, {n(int(gov[0][1]))} directives each with 0 discrete "
                     "mismatches")
    if seal:
        parts.append(f"all {seal.group(1)} Python/C++ twins unchanged under the seal")
    if shield:
        bad = sum(int(x) for x in re.findall(r":\s*(\d+)", shield.group(2)))
        parts.append(f"the shield's {len(re.findall(r':', shield.group(2)))} properties over {shield.group(1)} cases, "
                     f"{'none violated' if not bad else f'{bad} violations'}")
    lines = t.splitlines()
    counted = []
    for i, line in enumerate(lines):
        m = re.match(r"PASS\s+negative control: parity test detects (.+)$", line)
        if m and i and (c := re.search(r"mismatches = (\d+)", lines[i - 1])):
            counted.append(f"{m.group(1)}, {n(int(c.group(1)))} mismatches")
    parts.append(f"{n(neg)} negative controls, each caught" + (f" ({'; '.join(counted)})" if counted else ""))
    return "; ".join(parts)


@block("seal", SEAL, lambda: engine()["path"])
def b_seal():
    s, e = load(SEAL), engine()
    py = {}
    for tw in s["twins"].values():
        for f, h in (tw.get("sha256") or {}).items():
            if f.endswith(".py"):
                py[f] = h
    inside = [f for f in py if f in e["hashes"]]
    same = [f for f in inside if e["hashes"][f] == py[f]]
    outside = sorted(f for f in py if f not in e["hashes"])
    return (f"sealed {s['sealed_at']}: {n(len(s['twins']))} twins; of the {n(len(py))} Python files it records, the "
            f"{n(len(inside))} that {e['name']}'s fingerprint also holds carry "
            + ("the same hash there" if len(same) == len(inside) else f"the same hash in {n(len(same))} cases")
            + (f"; {n(len(outside))} lie outside the fingerprint ({', '.join(f'`{f}`' for f in outside)})" if outside else "")
            + f"; {n(len(s.get('python_only') or {}))} parts have no twin (`python_only`)")


@block("formal_bounds", TRACKING)
def b_formal_bounds():
    t = load(TRACKING)
    x = t["nearest_target"]
    inside = "inside" if x["ultimate_bound_inside_basin"] else "outside"
    return (f"over the declared parameter box F̄ = {x['F_bar_global']:.2f} < {t['U_AUTHORITY']:g}; the sampled-data error "
            f"contracts by {t['rho']:g} a step, ε[h] = {x['epsilon_h']:.4f} over the frozen fixtures ({t['population']}), and the "
            f"ultimate bound {x['ultimate_bound']:.4f} lies {inside} the {x['basin_tol']:.2f} basin")


# ---- the catalogue, the organisms and the orchestra
@lru_cache(None)
def catalog():
    with CATALOG.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def realms_of(r):
    return [x for x in re.split(r"[;|, ]+", r["realms"]) if x]


@block("catalogue_size", CATALOG)
def b_catalogue_size():
    rows = catalog()
    return f"{n(len(rows))} muscles in {n(len({r['family_id'] for r in rows}))} families"


@block("catalogue_kinds", CATALOG)
def b_catalogue_kinds():
    c = Counter(r["knob"] for r in catalog())
    return series([f"{k} {n(v)}" for k, v in c.most_common()])


@block("catalogue_plants", CATALOG)
def b_catalogue_plants():
    c = Counter(r["template"] for r in catalog())
    return series([f"`{k}` {n(v)}" for k, v in c.most_common()])


@block("catalogue_home_realms", CATALOG)
def b_catalogue_home_realms():
    c = Counter(r["realm"] for r in catalog())
    return series([f"{REALM.get(k, k)} {n(c[k])}" for k in list(REALM) + [k for k in c if k not in REALM] if c[k]])


@block("catalogue_realms", CATALOG)
def b_catalogue_realms():
    rows = catalog()
    keys = list(REALM)
    size = [sum(1 for r in rows if k in realms_of(r)) for k in keys]
    spine = sum(1 for r in rows if all(k in realms_of(r) for k in keys))
    one = sum(1 for r in rows if len(set(realms_of(r))) == 1)
    stacked = sum(size)
    sub = "₁₂₃₄"
    identity = (f"{n(stacked)} = {n(len(rows))} + {len(keys) - 1} × {n(spine)}"
                if stacked == len(rows) + (len(keys) - 1) * spine and spine + one == len(rows) else "the realms overlap otherwise")
    return (", ".join(f"|R{sub[i]}| = {n(v)}" for i, v in enumerate(size)) + f"; the spine, in all four, {n(spine)}; in one realm "
            f"only, {n(one)}; the whole tower {n(len(rows))}; the four stacked {n(stacked)}, and {identity}")


@block("catalogue_cards", CARDS)
def b_catalogue_cards():
    with CARDS.open(encoding="utf-8") as f:
        k = sum(1 for _ in csv.DictReader(f))
    return f"{n(k)} muscles carry a card of their own"


@block("wiring_families", RECIPES)
def b_wiring_families():
    with RECIPES.open(encoding="utf-8") as f:
        k = sum(1 for _ in csv.DictReader(f))
    return f"{n(k)} families, one row each"


@lru_cache(None)
def verdict_rows():
    with VERDICTS_CSV.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


@block("catalogue_verdicts", VERDICTS_CSV)
def b_catalogue_verdicts():
    rows = [r for r in verdict_rows() if r["kind"] == "modelled muscle"]
    write = sum(1 for r in rows if r["verdict"] == "write")
    rest = [r for r in rows if r["verdict"] != "write"]
    limit = sum(1 for r in rest if r["why"].startswith("at its limit on native"))
    loss = sum(1 for r in rows if r.get("loss_all_three") not in ("", "0", None))
    return (f"of the {n(len(rows))} modelled muscles, {n(write)} read GAIN and earn a wire in; {n(len(rest))} stay native: "
            f"{n(limit)} at their limit on native and {n(len(rest) - limit)} the same as native"
            + ("; none read LOSS" if not loss else f"; {n(loss)} read LOSS"))


@block("real_knob_verdicts", VERDICTS_CSV)
def b_real_knob_verdicts():
    rows = [r for r in verdict_rows() if r["kind"] == "real knob" and r["counted"] == "yes"]
    c = Counter(r["verdict"] for r in rows)
    return (f"of {n(len(rows))} knob-cases on the real stacks, " + series([f"{n(c[k])} {k}" for k in ("write", "operator's choice", "watch") if c[k]]))


@block("organisms_v8", REALMS)
def b_organisms_v8():
    r = load(REALMS)
    loads = list(r["organisms"])
    labels = {(ld, o): x.get("label", "") for ld in loads for o, x in r["organisms"][ld].items()}
    gain = all(("FEWER MISSES" in v or "MORE WORK" in v or "FASTER" in v) and "LOSS" not in v for v in labels.values())
    energy = max(x["summary"]["energy"][0] for ld in loads for x in r["organisms"][ld].values())
    work = max(abs(x["summary"]["work"][0]) for ld in loads for x in r["organisms"][ld].values())
    tower = r["organisms"].get("climb", {}).get("tower", {}).get("summary", {}).get("viol_pp", [None])[0]
    orgs = len(r["organisms"][loads[0]])
    head = (f"on {r['run']['engine']}, seeds {r['run']['seeds'][0]} to {r['run']['seeds'][-1]}, each of the {n(orgs)} organisms read "
            + ("GAIN, fewer misses," if gain else "a reading other than GAIN on some load,") + f" under each of its {len(loads)} loads")
    e = (f"energy STEADY, under the floor, up at most {pct(100 * energy, 3)}" if 100 * energy < 100 * SIZE_FLOOR
         else f"energy power given, up at most {pct(100 * energy, 3)}")
    return (f"{head}; {e}; the work moved at most {pct(100 * work, 3)}"
            + (f"; the whole tower under the climb read misses down {abs(tower):.3f} percentage points" if tower is not None else ""))


@block("orchestra", ORCHESTRA)
def b_orchestra():
    o = load(ORCHESTRA)
    k = len(o["run"]["bodies"].get("orchestra") or [])
    loads = {"normal": "its own load", "climb": "the climb", "line": "work waiting in line"}
    e = [(loads.get(ld, ld), o["bodies"][ld]["orchestra"]["summary"]["energy"][0]) for ld in o["bodies"]]
    return (f"{n(k)} muscles in one body, on {o['run']['engine']}: its energy power given, "
            + series([f"up {pct(100 * v)} under {ld}" for ld, v in e]))


# ---- the products Omni-Compass sits on, run live
def governor_tables():
    """(the product's register name, what it acts on, its table stems) for every product tools/governors_page.py names:
    its two-way tables where it runs two ways, else its four ways' table of Omni-Compass on top."""
    from tools.governors_page import GOVERNORS
    standing = sorted(s for s in tables() if standing_native(s))
    out = []
    for slug, name, _row, acts, _native, test in GOVERNORS:
        bases = ("VANILLA", "BINPACK") if slug == "scheduler" else (slug.upper(),)
        two = [s for s in standing if base_of(s)[1] is None and any(base_of(s)[0] == b or base_of(s)[0].startswith(b + "_") for b in bases)
               and place(s) in ("two_way", "cluster")]
        top = [s for s in standing if base_of(s)[1] == "TOP" and base_of(s)[0] in bases]
        out.append((name, acts, sorted(two or top, key=order_key), test))
    return out


def word_counts(stem: str) -> Counter:
    return Counter(r["word"] for r in rows_of(stem))


def counts_text(c: Counter) -> str:
    parts = [f"{n(c.get(GAIN, 0))} GAIN", f"{n(c.get(LOSS, 0))} LOSS"]
    parts += [f"{n(c[k])} {k}" for k in (GIVEN, STEADY, DISAGREE) if c.get(k)]
    return ", ".join(parts)


@block("governors_table", AUDIT, "tools/governors_page.py")
def b_governors_table():
    L = ["| Product | What it acts on | Omni-Compass on top, against it as shipped | Table |", "|---|---|---|---|"]
    for name, acts, stems, test in governor_tables():
        if not stems:
            plain = re.sub(r" [(](.*)[)]$", r", \1", test)
            L.append(f"| {name} | {acts} | not yet run; its test {plain} | — |")
            continue
        for s in stems:
            label = PRODUCT.get(base_of(s)[0], name) if len(stems) > 1 or base_of(s)[0] in ("VANILLA", "BINPACK") else name
            L.append(f"| {label} | {acts} | {counts_text(word_counts(s))} | `{rel(tables()[s]['file'])}` |")
    return "\n".join(L)


@block("governors_loss_outnumber", AUDIT, "tools/governors_page.py")
def b_governors_loss_outnumber():
    rigs = [s for *_x, stems, _t in governor_tables() for s in stems]
    more = [s for s in rigs if word_counts(s).get(LOSS, 0) > word_counts(s).get(GAIN, 0)]
    rest = [named(s) for s in rigs if s not in more]
    return (f"on {n(len(more))} of these {n(len(rigs))} tables LOSS rows outnumber GAIN rows"
            + (f"; the exceptions are {series(rest)}" if rest else ""))


# ---- the worked example and the kill test
def three_run_table(stem: str, gauges=None) -> str:
    rows = [r for r in rows_of(stem) if r["word"] in JUDGED_WORDS and (gauges is None or r["gauge"] in gauges)]
    if gauges:
        rows.sort(key=lambda r: gauges.index(r["gauge"]))
    if not rows:
        raise RecordError(f"{stem} carries no judged row")
    L = ["| Gauge | Reading | Strength | Why |", "|---|---|---|---|"]
    for r in rows:
        L.append(f"| {gauge_name(r)} | {reading(r)} | {(r.get('evidence') or {}).get('strength') or '—'} | {why(r)} |")
    return "\n".join(L)


FAIRNESS = "FAIRNESS"
FAIR_GAUGES = ["HPA replicas, mean", "failed requests (%)", "response time (ms), mean", "response time (ms), 95th percentile"]


def standing_stem(base: str) -> str:
    found = sorted((int(t["engine"].split("v")[-1]), s) for s, t in tables().items()
                   if t["status"] == "standing" and s.split("_", 1)[1] == base)
    if not found:
        raise RecordError(f"no standing table of {base}")
    return found[-1][1]


@block("fairness_table", AUDIT)
def b_fairness_table():
    stem = standing_stem(FAIRNESS)
    rows = {r["gauge"]: r for r in rows_of(stem)}
    L = ["| Gauge (what it is for) | Raw change, runs A / B / C | Raw mean of three | Reading | Strength |",
         "|---|---|---|---|---|"]
    for g in FAIR_GAUGES:
        r = rows.get(g)
        if r is None:
            raise RecordError(f"{stem} carries no row {g!r}")
        ev = r["evidence"]
        rp = " / ".join(f"{updown(x)} {pct(x, 2)}" for x in ev["run_pct"])
        L.append(f"| {g} ({r['direction']}) | {rp} | {updown(ev['mean_pct'])} {pct(ev['mean_pct'], 2)} | **{bare(r['recomputed'])}** "
                 f"| {ev.get('strength') or '—'} |")
    return "\n".join(L)


@block("fairness_numbers", AUDIT)
def b_fairness_numbers():
    stem = standing_stem(FAIRNESS)
    rows = {r["gauge"]: r for r in rows_of(stem)}
    rep, fail = rows["HPA replicas, mean"], rows["failed requests (%)"]
    own = rows.get("Omni's own CPU (cores), mean")
    lo, hi = fail["evidence"]["mean_ci95_pct"]
    nat = [x["native"] for x in fail["runs"]]
    before = ", ".join(f"{x['native']:.2f}" for x in rep["runs"])
    after = ", ".join(f"{x['omni']:.2f}" for x in rep["runs"])
    out = [f"the autoscaler's mean count rose from {before} to {after}",
           f"native failed {min(nat):.1f}% to {max(nat):.1f}% of requests, and the interval of the three runs' mean change runs "
           f"from {updown(lo)} {pct(lo)} to {updown(hi)} {pct(hi)}"]
    if own:
        v = [x["omni"] for x in own["runs"]]
        out.append(f"Omni-Compass's own processor read {min(v):.4g} to {max(v):.4g} of a core")
    return "; ".join(out) + f" (`{rel(tables()[stem]['file'])}`)"


@block("kill_table", AUDIT)
def b_kill_table():
    return three_run_table(standing_stem("ROBUST_KILL"))


@block("kill_numbers", lambda: ROOT / tables()[standing_stem("ROBUST_KILL")]["json"])
def b_kill_numbers():
    d = load(ROOT / tables()[standing_stem("ROBUST_KILL")]["json"])
    rows = d["rows"]
    cmds = next(v for k, v in rows.items() if k.startswith("settings commands"))
    hb = next(v for k, v in rows.items() if k.startswith("robust: every setting back"))
    over = rows["time over the response line (% of samples)"]
    c = [x["omni"] for x in cmds["runs"]]
    mean = [x["handed_back_s_mean"] for x in hb["runs"]]
    mx = [x["handed_back_s_max"] for x in hb["runs"]]
    allow = hb["runs"][0]["allowance_s"]
    ok = all(x["handed_back_within_allowance_all"] for x in hb["runs"])
    o, nv = [x["omni"] for x in over["runs"]], [x["native"] for x in over["runs"]]
    return (f"{min(c):.1f} to {max(c):.1f} settings commands a repetition written on its own; "
            + (f"every setting back at the operator's inside the {allow:g} s allowance in every repetition of all three runs"
               if ok else "not every setting back inside the allowance")
            + f", at a mean of {min(mean):.1f} to {max(mean):.1f} s and at most {min(mx):g} to {max(mx):g} s; over the response line "
            f"{min(o):.2f}% to {max(o):.2f}% of samples against native's {min(nv):.2f}% to {max(nv):.2f}%")


def table_losses(base: str) -> str:
    """A standing table's LOSS rows, each with its reading and the ledger's word on its cause."""
    stem = standing_stem(base)
    causes = {(s, r["gauge"], r["section"]): c for s, _g, r, c, _k in ledger_native()}
    rows = [r for r in native_losses() if r["table"] == stem]
    written = sum(1 for r in rows if causes.get((stem, r["gauge"], r["section"])))
    each = "; ".join(f"{gauge_name(r)}, {reading(r)}" for r in rows)
    cause = ("no cause yet written for any of them" if not written else
             f"a cause written for {n(written)} of them" if written < len(rows) else "a cause written for each")
    return f"{plural(len(rows), 'LOSS row', 'LOSS rows')} in {named(stem, ref=True)}, {cause} (`docs/LOSS_LEDGER.md`): {each}"


@block("kill_losses", AUDIT, LEDGER)
def b_kill_losses():
    return table_losses("ROBUST_KILL")


@block("long_losses", AUDIT, LEDGER)
def b_long_losses():
    return table_losses("ROBUST_LONG")


@block("fairness_losses", AUDIT, LEDGER)
def b_fairness_losses():
    return table_losses(FAIRNESS)


@block("fairness_rows", AUDIT)
def b_fairness_rows():
    return three_run_table(standing_stem(FAIRNESS))


@block("kai_queue", AUDIT)
def b_kai_queue():
    out = []
    for base in ("KAI", "KAI_4W_TOP", "KAI_4W_BARE"):
        stem = standing_stem(base)
        for r in rows_of(stem):
            g = r["gauge"]
            if g.startswith("batch: queue finished") or g.startswith("queue: job turnaround"):
                what = "the queue's finish" if "queue finished" in g else "the jobs' mean turnaround"
                out.append(f"{named(stem)}: {what} {reading(r)}")
    if not out:
        raise RecordError("the KAI scheduler's tables carry no queue rows")
    return "; ".join(out)


def stacks(name: str) -> dict:
    return load(ROOT / "results" / "gpu" / name)


@block("a10_stacks", "results/gpu/V23_A10_STACKS_FULL_ABC.json")
def b_a10_stacks():
    d = stacks("V23_A10_STACKS_FULL_ABC.json")
    def tally(part):
        c = Counter()
        for r in d["rows"]:
            if r["part"] != part:
                continue
            rd = bare(r["reading"])
            w = next((x for x in (GAIN, LOSS, GIVEN, STEADY, DISAGREE) if rd.startswith(x)), "shown, not judged")
            c[w] += 1
        return series([f"{n(c[w])} {w}" for w in (GAIN, GIVEN, STEADY, LOSS, DISAGREE, "shown, not judged") if c[w]])
    writes = d.get("card_writes") or []
    w = ("Omni-Compass's card-side process wrote nothing in any of the "
         + series(sorted({n(x['arms']) for x in writes})) + " Omni-Compass arms of each run"
         if writes and not any(x["writes"] for x in writes) else
         "the card-side process wrote " + ", ".join(f"{n(x['writes'])} in {n(x['arms'])} arms" for x in writes))
    return (f"{n(len(d['rows']))} rows on {d['engine'].split(' (')[0]}: the organisms (our own models, class S) {tally('sim')}; "
            f"the card (its own meter, class P) {tally('card')}; {w}")


@block("card_writes", "results/gpu/V23_A10_STACKS_FULL_ABC.json", "results/gpu/V23_A100_8CARD_STACKS_ABC.json")
def b_card_writes():
    a10 = stacks("V23_A10_STACKS_FULL_ABC.json").get("card_writes") or []
    a100 = stacks("V23_A100_8CARD_STACKS_ABC.json").get("card_writes") or []
    say = lambda ws: ", ".join(f"{n(x['writes'])} in {n(x['arms'])}" for x in ws)
    return (f"writes of the card-side process in the Omni-Compass arms, run by run: the eight-card machine {say(a100)} arms; the "
            f"fully loaded A10 {say(a10)} arms")


# ---- the repository
@block("workflows", WORKFLOWS)
def b_workflows():
    k = len(list(WORKFLOWS.glob("*.yml"))) + len(list(WORKFLOWS.glob("*.yaml")))
    return f"{n(k)} workflows"


@block("deviations", "tools/deviations.py", "docs/DEVIATIONS.md")
def b_deviations():
    from tools import deviations as DV
    rows = DV.amendments()
    c = Counter(r["timing"] for r in rows)
    files = len({r["file"] for r in rows})
    say = {"before the runs it governs": "written before the runs they apply to", "not stated in its heading":
           "whose heading states no timing", "after runs began": "written after runs began"}
    return (f"{n(len(rows))} amendments in {n(files)} preregistrations: "
            + series([f"{n(v)} {say.get(k, k)}" for k, v in sorted(c.items(), key=lambda kv: -kv[1])]))


# ---------------------------------------------------------------------------------------------------------------- the file
def compute(name: str):
    """(text, None) or (None, the reason it cannot be computed)."""
    try:
        text = BLOCKS[name][1]()
    except RecordError as e:
        return None, str(e)
    except (KeyError, ValueError, TypeError, StopIteration, ZeroDivisionError, OSError, IndexError, AttributeError) as e:
        return None, f"{type(e).__name__}: {e}"
    return text, None


def markers(text: str):
    """(blocks, problems): blocks as (name, start of its text, end of its text) in order; problems as words."""
    out, problems = [], []
    opens = list(OPEN.finditer(text))
    closes = list(CLOSE.finditer(text))
    events = sorted([(m.start(), "open", m) for m in opens] + [(m.start(), "close", m) for m in closes], key=lambda e: e[0])
    current = None
    for at, kind, m in events:
        line = text.count("\n", 0, at) + 1
        if kind == "open":
            if current is not None:
                problems.append(f"line {line}: {m.group(1)} opens inside {current[0]}, which has no end marker before it")
            current = (m.group(1), m.end(), line)
        else:
            if current is None:
                problems.append(f"line {line}: an end marker for {m.group(1)} with no block open")
            elif current[0] != m.group(1):
                problems.append(f"line {line}: {current[0]} (opened on line {current[2]}) is closed as {m.group(1)}")
                current = None
            else:
                out.append((current[0], current[1], m.start()))
                current = None
    if current is not None:
        problems.append(f"line {current[2]}: {current[0]} has no end marker")
    return out, problems


def inner(text: str) -> str:
    """The text a block's markers hold, a multi-line block read without the line breaks after its open and before its end."""
    if text.startswith("\n"):
        text = text[1:]
    if text.endswith("\n"):
        text = text[:-1]
    return text


def placed(text: str) -> str:
    return f"\n{text}\n" if "\n" in text else text


def run(path: Path, fix: bool) -> int:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as e:
        print(f"{path}: cannot be read ({e})")
        return 1
    found, problems = markers(text)
    if problems:
        for p in problems:
            print(f"{path.name}: broken marker pair, {p}")
        return 1
    if not found:
        print(f"{path.name}: no monograph block yet")
        return 0
    bad, new, last = [], [], 0
    for name, a, z in found:
        new.append(text[last:a])
        last = z
        if name not in BLOCKS:
            bad.append(f"{name}: no such block (python3 tools/monograph_words.py --list names every block)")
            new.append(text[a:z])
            continue
        want, err = compute(name)
        if err:
            bad.append(f"{name}: cannot be written from its record ({err})")
            new.append(text[a:z])
            continue
        if inner(text[a:z]) != want:
            if not fix:
                bad.append(f"{name}: differs from its record ({'; '.join(sources_of(name))})")
            new.append(placed(want))
        else:
            new.append(text[a:z])
    new.append(text[last:])
    out = "".join(new)
    if fix and out != text:
        path.write_text(out, encoding="utf-8")
        print(f"{path.name}: {len(found)} blocks written from their records")
    elif fix:
        print(f"{path.name}: every block already in step with its record")
    for b in bad:
        print(f"{path.name}: {b}")
    if not fix and not bad:
        print(f"{path.name}: all {len(found)} blocks in step with their records")
    return 1 if bad else 0


def listing() -> list:
    out = []
    for name in BLOCKS:
        text, err = compute(name)
        try:
            src = "; ".join(sources_of(name))
        except RecordError as e:
            src, err = "", err or str(e)
        item = {"name": name, "text": text, "source": src}
        if err:
            item["error"] = err
        out.append(item)
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--fix", action="store_true", help="write every block from its record")
    g.add_argument("--check", action="store_true", help="exit 1 when a block differs from its record")
    g.add_argument("--list", action="store_true", help="print every block this tool computes, as JSON")
    ap.add_argument("--file", type=Path, default=MONOGRAPH, help="the file to read and write (default: the monograph)")
    a = ap.parse_args(argv)
    if a.list:
        print(json.dumps(listing(), ensure_ascii=False, indent=1))
        return 0
    return run(a.file.resolve(), fix=a.fix)


if __name__ == "__main__":
    sys.exit(main())

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
