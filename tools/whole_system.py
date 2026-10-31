#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The whole system: Omni-Compass at every layer, the layers composed by the product law, every number with its interval.

The founder's question of 20 October 2026: the cloud is the wire between the chip at one end and the software at the other;
Omni-Compass sits at both ends and at every layer between; what is the total? This tool answers it from the tables that stand,
by one rule, written here once.

The layers, bottom to top, each measured against its own native with the layer under it as native runs it:

  1  the card (the chip): the GPU's own meter                         results/gpu/<run>/GPU_REPS.json           class P
  2  the machine (the kernel, bare metal, Kepler): not yet run        register row 79                           (factor 1)
  3  the cluster (Kubernetes, its add-ons, its governors on top)      results/live/V<n>_*.json                  class L
  4  the services on it (PostgreSQL, Kafka, Redis, MongoDB, MySQL)    results/live/V<n>_{PGBENCH,...}.json      class L
  5  the cloud (Azure, the bill the cloud metered)                    results/live/AKS_BILL.md, V1_AKS_*.json   class L

and beside them, never inside: the organisms (our own models, class S), the organisms with the real cluster inside (omni-v3).

The product law. For a gauge g with declared aim a(g) (higher for work; lower for a wait; spent for a resource or a bill), a
layer ℓ measured native nℓ and omni oℓ has the ratio Rℓ(g) = oℓ/nℓ when the aim is higher and nℓ/oℓ otherwise, so that
Rℓ(g) > 1 is toward the aim (a GAIN) at every layer alike. The layers compose by multiplication:

  R(g) = ∏ℓ Rℓ(g),      G(g) = R(g) − 1,      log R(g) = Σℓ log Rℓ(g).

The interval. Each table gives, per run, the paired difference d = o − n with its 95% interval [lo, hi] on n paired
repetitions (the exact Student t, omnicompass/student_t.py), so SE(d) = (hi − lo) / (2 t₀.₉₇₅,ₙ₋₁); the delta method gives
SE(log R) = SE(d) / o (d log(n/o)/do = −1/o and d log(o/n)/do = 1/o). The three runs A, B and C of a test are pooled by
inverse variance (a fixed effect: μ = Σwᵢμᵢ/Σwᵢ, Var = 1/Σwᵢ, wᵢ = 1/σᵢ²); a layer with several tests takes the mean of
their log ratios (the geometric mean of the ratios, the Omni index's rule) with Var = Σσᵢ²/k²; the layers add in the log,
and their variances add, because every layer was measured in its own runs (independent sampling noise). The 95% interval
of the total is exp(μ ± 1.96 σ). The index over the gauges is the mean of the gauge logs; its interval is given under
two bounds, the gauges independent (Var = Σσ²/k²) and the gauges perfectly correlated inside a run (σ = Σσ/k).

Two readings of the same numbers. By the index's rule a gauge of a test enters only when its three-run reading is GAIN,
LOSS or power given in all three of our runs; a STEADY gauge, a disagreement, or a table of one run enters as exactly 1 with
no variance (nothing inside the noise is claimed either way). With every interval carried, every measured gauge enters with
its pooled estimate and its variance whatever its reading, and the total's interval says what the noise allows.

What the composition is. No run here stacked the layers: each factor is one layer's own measurement with the layer under
it native. The product is therefore a modelled composition (class S) of class P and L measurements, under the assumption
that a layer's ratio does not change when the layers under or over it also carry Omni-Compass (separability). Where the
tables can test that assumption they do: the governors' four ways measure Omni-Compass on the organism alone (compassbare
against nativebare) and on top of the orchestrator (compass against native) in the same repetitions; the two agree within
the noise where separability holds, and the page says where they do not. The stacked run (Omni-Compass at every layer at
once, against native at every layer) is the measurement that would replace this composition; until it exists this page is
the answer the standing tables give, with its assumptions in the open.

What is composed (the founder's order of 31 October 2026). The whole organism is shown at the software end: work, speed and machines are
composed. The energy and the bill are held at native's (exactly 1, shown beside, never composed): on the cluster the energy is a declared
model of the machines row, never a meter, so composing it would count the fewer machines twice and claim a saving at the chip that no
meter read; the cloud is the wire, and its bill is kept exactly as native's (the benefit is more work for the same bill). The chip (the
card) and the wire (the cloud) enter as exactly 1 on every gauge: the chip is kept exactly as native runs it, and its own meter at the
factory tune reads it so (the omni-v21 A100 three runs, results/gpu/V21_A100_CAP_ABC.md); the cloud's runs are the check that the
software end's benefit holds through the wire. Both are shown beside, every row.

Every result is read from a table that names its engine; the layers stand on different engines (the card on the controller
of 2 October, the cluster on omni-v10 and omni-v11, the governors on omni-v12), so the composition is also across engines,
said so, and remade as each layer's omni-v12 three runs land (`python3 tools/whole_system.py`).
"""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))

import legal                                      # noqa: E402
import readings                                   # noqa: E402
from omnicompass.student_t import t95             # noqa: E402
from omni_index import SOURCES, WORKLOAD_TABLES, newest, CAPACITY, CAPACITY_NOW, P95, NODES, ENERGY, STANDBY  # noqa: E402

LIVE = ROOT / "results" / "live"
OUT_MD = ROOT / "results" / "WHOLE_SYSTEM.md"
OUT_JSON = ROOT / "results" / "WHOLE_SYSTEM.json"
GPU_ABC = ROOT / "results" / "gpu" / "V21_A100_CAP_ABC.json"   # the card at the factory tune (the dial at the max), three runs, its own meter

GAUGES = ("work", "speed", "machines", "energy", "bill")
AIM = {"work": "higher", "speed": "lower", "machines": "spent", "energy": "spent", "bill": "spent"}
GAUGE_WORDS = {"work": "work (more)", "speed": "speed (the 95th percentile response, lower)", "machines": "machines (fewer)",
               "energy": "energy (a declared model on the cluster, the card's own meter on the chip)", "bill": "the bill (the cloud's metered bill)"}
Z = 1.959964

# The founder's order of 31 October 2026: the whole organism is shown at the software end only. Omni-Compass makes the software
# do more work, faster, on fewer machines; the chip is kept exactly as native runs it and the cloud's wire bill exactly as native's,
# so the benefit is more work for the same power and the same bill. Composed: work, speed and machines. Held at native's (exactly 1,
# shown beside, never composed): the energy (on the cluster a declared model of the machines row, never a meter: composed, it would
# count the fewer machines twice and claim a saving at the chip that no meter read) and the bill (the cloud is the wire; the benefit
# is more work for the same bill). The card (the chip) and the cloud (the wire) enter as exactly 1 on every gauge; their own runs are
# shown beside, the card's as the chip measured and left as native runs it, the cloud's as the check that the software end's benefit
# holds through the wire.
COMPOSED = ("work", "speed", "machines")
HELD = {"energy": "held at native's, the same power: on the cluster a declared model of the machines row, never a meter, so it is shown, not composed",
        "bill": "held at native's, the same bill: the cloud is the wire, and the benefit is more work for the same bill"}
SCOPE_WITH = "with the card (the chip held exactly as native runs it)"
SCOPE_WITHOUT = "without the card (the cluster, the services and the cloud)"
HELD_LAYERS = {"1.": "the chip, kept exactly as native runs it: enters as exactly 1, its three runs shown beside",
               "5.": "the wire, its bill kept exactly as native's: enters as exactly 1, its runs shown beside as the check that the benefit holds"}
GAUGE_WORDS_HELD = {"energy": "energy (held at native's: the same power)", "bill": "the bill (held at native's: the same bill)"}

# the cluster layer: the Omni index's Kubernetes tests, the add-on and rightsizing tests, and the governors with Omni-Compass on
# top of each (the four ways' TOP comparison: compass against native, the orchestrator as shipped under both)
CLUSTER_EXTRA = [
    ("Goldilocks and the VPA's recommender, Omni-Compass on top", "V11_GOLDILOCKS.json", {"speed": P95, "machines": NODES, "energy": ENERGY}, None),
    ("CruiseKube applying its own recommendations, Omni-Compass on top", "V10_CRUISEKUBE.json", {"speed": P95, "machines": NODES, "energy": ENERGY}, None),
]
GOVERNORS = [("Kueue", "KUEUE"), ("Volcano", "VOLCANO"), ("the KAI scheduler", "KAI"), ("Koordinator", "KOORDINATOR"),
             ("the scheduler's bin-packing profile", "BINPACK"), ("Crane", "CRANE"), ("KubeRay", "KUBERAY"),
             ("the Gödel scheduler", "GODEL"), ("Karmada", "KARMADA"), ("Open Cluster Management", "OCM"), ("Armada", "ARMADA")]
GOV_MEASURES = {"speed": P95, "machines": NODES, "energy": STANDBY}
GOV_SINGLE = [("the Kubernetes scheduler as shipped", "V12_VANILLA.json")]

# the cloud layer, the gauges of the billed tables
CLOUD_MEASURES = {"speed": P95, "machines": "machines billed, machine-hours", "bill": "compute bill at list price ($)"}
CLOUD_V1_MEASURES = {"speed": P95, "machines": "node-hours"}
# the card: the GPU's own meter
CARD_MEASURES = {"work": "requests served", "speed": "response time, 95th percentile (ms)", "energy": "energy, GPU (J)"}
CARD_PRIMARY = "work per energy (served requests per kJ)"


# ----------------------------------------------------------------------------------------------------------------------- statistics
def log_ratio(aim, native, omni, lo, hi, n):
    """(μ, σ) of the log ratio oriented toward the aim, from one run's paired difference and its 95% interval on n pairs."""
    if native is None or omni is None or native <= 0 or omni <= 0 or n is None or n < 2:
        return None
    if lo is None or hi is None or any(isinstance(x, float) and math.isnan(x) for x in (lo, hi)):
        return None
    t = t95(n - 1)
    se_d = (hi - lo) / (2.0 * t)
    sigma = se_d / omni
    mu = math.log(omni / native) if aim == "higher" else math.log(native / omni)
    return mu, sigma


def pool(estimates):
    """Fixed-effect pooling of (μ, σ) pairs; an exact estimate (σ = 0) decides alone."""
    es = [e for e in estimates if e is not None]
    if not es:
        return None
    exact = [m for m, s in es if s == 0.0]
    if exact:
        return sum(exact) / len(exact), 0.0
    w = [1.0 / (s * s) for _, s in es]
    mu = sum(wi * m for wi, (m, _) in zip(w, es)) / sum(w)
    return mu, math.sqrt(1.0 / sum(w))


def combine_mean(estimates):
    """The mean of k log ratios (the geometric mean of the ratios), Var = Σσ²/k²."""
    es = [e for e in estimates if e is not None]
    if not es:
        return None
    k = len(es)
    return sum(m for m, _ in es) / k, math.sqrt(sum(s * s for _, s in es)) / k


def combine_sum(estimates):
    es = [e for e in estimates if e is not None]
    if not es:
        return None
    return sum(m for m, _ in es), math.sqrt(sum(s * s for _, s in es))


def interval(est):
    if est is None:
        return None
    mu, s = est
    return math.exp(mu), math.exp(mu - Z * s), math.exp(mu + Z * s)


def word_for(gauge, est):
    """The word for a composed ratio by the one key that stands (the founder's order of 24 October 2026): a change of 0.5% or more
    either way is a change, STEADY only under it. Above 1 a GAIN; below 1 a LOSS for work and speed and power given for a resource or
    the bill; the interval is printed beside it, the word does not wait on it."""
    if est is None:
        return "not measured"
    r, lo, hi = interval(est)
    if abs(r - 1.0) < readings.SIZE_FLOOR:
        return readings.STEADY
    if r > 1.0:
        return readings.GAIN
    return readings.LOSS if AIM[gauge] in ("higher", "lower") else readings.GIVEN


def pct(r):
    return f"{100 * (r - 1):+.1f}%" if abs(100 * (r - 1)) >= 0.05 else f"{100 * (r - 1):+.2f}%"


def fmt(est):
    if est is None:
        return "not measured"
    r, lo, hi = interval(est)
    return f"×{r:.4f} ({pct(r)}; {pct(lo)} to {pct(hi)})"


# ----------------------------------------------------------------------------------------------------------------------- the tables
def abc_rows(path):
    d = json.loads(path.read_text())
    n = [r.get("paired_repetitions") for r in d["runs"]]
    return d, n


def test_from_abc(name, fname, measures, work, engine_note=None):
    """One test from a three-run table (tools/confirm_abc.py): per gauge the pooled (μ, σ), whether judged, and the words."""
    path = LIVE / fname
    if not path.exists():
        return None
    d, ns = abc_rows(path)
    rows = d["rows"]
    out = {"test": name, "source": f"results/live/{fname}", "runs": [r["run"] for r in d["runs"]],
           "engine": d["runs"][0].get("engine", "").split(" (")[0] or "unknown", "pairs": ns, "gauges": {}}
    for g, key in measures.items():
        if key == "equal":
            out["gauges"][g] = {"row": "the same fixed-rate work sent to both arms", "reading": "the same by design", "judged": False,
                                "est": (0.0, 0.0), "exact": True}
            continue
        row = rows.get(key)
        if row is None:
            continue
        ests = [log_ratio(AIM[g], r["native"], r["omni"], *(r.get("ci95") or (None, None)), n) for r, n in zip(row["runs"], ns)]
        est = pool(ests)
        out["gauges"][g] = {"row": key, "reading": row["reading"], "judged": readings.judged(row["reading"]), "est": est,
                            "runs": [(r["native"], r["omni"]) for r in row["runs"]]}
    if work == "equal":
        out["gauges"]["work"] = {"row": "the same fixed-rate work sent to both arms", "reading": "the same by design", "judged": False,
                                 "est": (0.0, 0.0), "exact": True}
    elif work == "capacity":
        row = rows.get(CAPACITY) or rows.get(CAPACITY_NOW)
        if row:
            ests = [log_ratio("higher", r["native"], r["omni"], *(r.get("ci95") or (None, None)), n) for r, n in zip(row["runs"], ns)]
            out["gauges"]["work"] = {"row": CAPACITY_NOW, "reading": row["reading"], "judged": readings.judged(row["reading"]),
                                     "est": pool(ests), "runs": [(r["native"], r["omni"]) for r in row["runs"]]}
    return out


def cluster_tests():
    out = []
    for cat, name, f, measures, work in SOURCES:
        t = test_from_abc(name, newest(f), measures, work)
        if t:
            out.append(t)
    for name, f, measures, work in CLUSTER_EXTRA:
        t = test_from_abc(name, newest(f), measures, work)
        if t:
            out.append(t)
    for name, f in GOV_SINGLE:
        t = test_from_abc(f"Omni-Compass on top of {name}", f, GOV_MEASURES, None)
        if t:
            out.append(t)
    for name, tag in GOVERNORS:
        f = f"V12_{tag}_4W_TOP.json"
        t = test_from_abc(f"Omni-Compass on top of {name} (the four ways, compass against native)", f, GOV_MEASURES, None)
        if t:
            out.append(t)
    return out


def service_tests():
    out = []
    for cat, fname, label, measures in WORKLOAD_TABLES:
        fname = newest(fname)
        path = LIVE / fname
        if not path.exists():
            continue
        d = json.loads(path.read_text())
        engine = d["runs"][0].get("engine", "").split(" (")[0]
        for wl, gauges in sorted(d["workloads"].items()):
            if wl == "tuning":
                continue
            t = {"test": label.format(wl=wl), "source": f"results/live/{fname}", "runs": [r["run"] for r in d["runs"]],
                 "engine": engine, "pairs": [3, 3, 3], "gauges": {}}
            for g, key in measures.items():
                row = gauges.get(key)
                if not row or any(x is None for x in row["runs"]):
                    continue
                ests = [log_ratio(AIM[g], r["native"], r["omni"], *(r.get("ci95") or (None, None)), 3) for r in row["runs"]]
                t["gauges"][g] = {"row": key, "reading": row["reading"], "judged": readings.judged(row["reading"]), "est": pool(ests),
                                  "runs": [(r["native"], r["omni"]) for r in row["runs"]]}
            out.append(t)
    return out


def parse_md_table(text, heading):
    """The rows of the table under a heading in a results page: gauge → (native, omni, lo, hi)."""
    sec = text.split(heading, 1)
    if len(sec) < 2:
        return {}
    rows = {}
    for ln in sec[1].split("\n"):
        if ln.startswith("## "):
            break
        m = re.match(r"\|\s*(.+?)\s*\|\s*([-+0-9.e]+)\s*\|\s*([-+0-9.e]+)\s*\|\s*[^|]*\|\s*([-+0-9.e]+) to ([-+0-9.e]+)\s*\|", ln)
        if m:
            rows[m.group(1).strip()] = tuple(float(m.group(i)) for i in (2, 3, 4, 5))
    return rows


def cloud_tests():
    out = []
    bill = LIVE / "AKS_BILL.md"
    if bill.exists():
        rows = parse_md_table(bill.read_text(), "## B with the compass law vs native")
        t = {"test": "Azure Kubernetes Service, Azure's own cluster autoscaler underneath, the compass law, 4 paired repetitions, one run",
             "source": "results/live/AKS_BILL.md", "runs": ["37187059424"], "engine": "the engine of commit 5b2832f (4 October 2026)",
             "pairs": [4], "gauges": {}}
        for g, key in CLOUD_MEASURES.items():
            if key in rows:
                n_, o_, lo, hi = rows[key]
                t["gauges"][g] = {"row": key, "reading": "one run: the interval includes zero" if lo < 0 < hi else "one run: clear of the noise",
                                  "judged": False, "est": log_ratio(AIM[g], n_, o_, lo, hi, 4), "runs": [(n_, o_)]}
        out.append(t)
    for name, f in (("the steady set", "V1_AKS_STEADY.json"), ("the burst", "V1_AKS_BURST.json")):
        p = LIVE / f
        if not p.exists():
            continue
        d = json.loads(p.read_text())
        rows = (d.get("paired") or {}).get("compass") or {}
        n = len((d.get("repetitions") or {}).get("compass") or []) or 5
        t = {"test": f"Azure Kubernetes Service, a 4-worker fleet, {name}, {n} paired repetitions, one run", "source": f"results/live/{f}",
             "runs": [], "engine": "omni-v1", "pairs": [n], "gauges": {}}
        for g, key in CLOUD_V1_MEASURES.items():
            row = rows.get(key)
            if row:
                lo, hi = row.get("ci95") or (None, None)
                t["gauges"][g] = {"row": key, "reading": "one run: the interval includes zero" if not row.get("significant") else "one run: clear of the noise",
                                  "judged": False, "est": log_ratio(AIM[g], row["native"], row["omni"], lo, hi, n), "runs": [(row["native"], row["omni"])]}
        out.append(t)
    return out


def card_tests():
    """The chip: the card governor at the factory tune (the dial at the max) on an A100, three runs, the card's own meter (class P)."""
    if not GPU_ABC.exists():
        return []
    d = json.loads(GPU_ABC.read_text())
    md = GPU_ABC.with_suffix(".md")
    m = re.search(r"(\d+) paired repetitions each", md.read_text()) if md.exists() else None
    n = int(m.group(1)) if m else None
    engine = (d.get("engine") or ["unknown"])[0].split(" (")[0]
    t = {"test": (f"NVIDIA A100 (SXM4, 40 GB) on Lambda, the card's own meter, Omni-Compass on the power limit and the clock ceiling at the "
                  f"factory tune (the dial at the max), native's power cap at 70% of the card's top, {n} paired repetitions in each of three runs"),
         "source": str(md.relative_to(ROOT)), "runs": list(d.get("runs") or []), "engine": engine, "pairs": [n] * len(d.get("runs") or []),
         "gauges": {}, "primary": None}
    rows = d.get("rows") or {}
    for g, key in CARD_MEASURES.items():
        row = rows.get(key)
        if not row:
            continue
        ests = [log_ratio(AIM[g], r["native"], r["omni"], *(r.get("ci95") or (None, None)), n) for r in row["runs"]]
        t["gauges"][g] = {"row": key, "reading": row["reading"], "judged": readings.judged(row["reading"]), "est": pool(ests),
                          "runs": [(r["native"], r["omni"]) for r in row["runs"]]}
    row = rows.get(CARD_PRIMARY)
    if row:
        ests = [log_ratio("higher", r["native"], r["omni"], *(r.get("ci95") or (None, None)), n) for r in row["runs"]]
        t["primary"] = {"row": CARD_PRIMARY, "reading": row["reading"], "est": pool(ests), "runs": [(r["native"], r["omni"]) for r in row["runs"]]}
    return [t]


# ----------------------------------------------------------------------------------------------------------------------- what it cost
# The founder's words of 31 October 2026: the hardware is shown so a buyer sees the benefit and what it cost: that the software end's
# gain was not bought by hurting the chip (its heat, its power, its service), by more energy, or by a bigger bill on the wire. Every
# row of the chip's own meter is listed, every LOSS named; the energy and the bill as measured; the machine's layer as not yet run.
COST_CARD = [("the factory tune (the dial at the max), native's power cap at 70% of the card's top", "V21_A100_CAP_ABC"),
             ("the factory tune, the same runs' full-load part", "V21_A100_CAP_FULL_ABC"),
             ("the tune-down (the dial at save), its own three runs", "V21_A100_SAVE_ABC")]


def reading_word(r):
    r = (r or "").strip("* ")
    for w in (readings.GAIN, readings.LOSS, readings.STEADY, readings.GIVEN, "the runs disagree"):
        if r.startswith(w):
            return w
    return r.split(",")[0]


def cost_ledger(measured):
    """Per hardware piece and the wire, every reading against native, its word, and the LOSS rows named."""
    pieces = []
    rows, srcs = [], []
    for label, stem in COST_CARD:
        p = ROOT / "results" / "gpu" / f"{stem}.json"
        if not p.exists():
            continue
        d = json.loads(p.read_text())
        srcs.append(f"results/gpu/{stem}.md")
        for g, row in d["rows"].items():
            ch = [100 * (r["omni"] - r["native"]) / r["native"] for r in row["runs"] if r.get("native")]
            rows.append({"part": label, "gauge": g, "reading": row["reading"], "word": reading_word(row["reading"]), "changes": ch})
    if rows:
        pieces.append({"piece": "the chip (an NVIDIA A100, the card's own meter, class P, omni-v21)", "sources": srcs, "rows": rows})
    lay = {n.split(".")[0]: v for n, v in measured.items()}
    def mrow(layer, g, label, note):
        e = (lay.get(layer) or {}).get(g)
        if e is None:
            return None
        r, lo, hi = interval(e)                         # native over Omni-Compass for a resource; said here as Omni-Compass against native
        o, olo, ohi = 1.0 / r - 1.0, 1.0 / hi - 1.0, 1.0 / lo - 1.0
        def way(x):
            return f"{abs(100 * x):.1f}% {'less' if x < 0 else 'more'}"
        w = word_for(g, e)
        noise = "; its 95% interval includes no change" if olo < 0 < ohi else ""
        return {"part": note, "gauge": label, "word": w, "est": list(e),
                "reading": f"{w}: Omni-Compass {way(o)} than native (95%: {way(olo)} to {way(ohi)}){noise}"}
    sw = [r for r in (mrow("3", "energy", "energy, parked workers at standby power (Wh)", "the cluster: a declared model of the machines row, never a meter"),
                      mrow("4", "energy", "the host's processor seconds", "the services: the host's own count of processor time, a stand-in for energy, never a meter")) if r]
    if sw:
        pieces.append({"piece": "the energy the software end drew (class L inputs, no meter)", "sources": ["results/live (the cluster and service tables)"], "rows": sw})
    cl = [r for r in (mrow("5", "bill", "the compute bill at list price", "Azure, one run of four paired repetitions, and the v1 fleet's one-run sets"),
                      mrow("5", "machines", "machines billed", "the same runs")) if r]
    if cl:
        pieces.append({"piece": "the wire (the cloud's metered bill, class L)", "sources": ["results/live/AKS_BILL.md", "results/live/V1_AKS_STEADY.json", "results/live/V1_AKS_BURST.json"], "rows": cl})
    pieces.append({"piece": "the machine (the kernel, bare metal, Kepler and the machine's own meter)", "sources": ["register row 79"], "rows": [],
                   "state": "not yet run"})
    for pc in pieces:
        pc["count"] = {w: sum(1 for r in pc["rows"] if r["word"] == w) for w in (readings.GAIN, readings.STEADY, readings.GIVEN, readings.LOSS, "the runs disagree")}
        pc["loss"] = [f"{r['gauge']} ({r['part']}): {r['reading']}" for r in pc["rows"] if r["word"] == readings.LOSS]
        pc["disagree"] = [f"{r['gauge']} ({r['part']})" for r in pc["rows"] if r["word"] == "the runs disagree"]
    return pieces


# ----------------------------------------------------------------------------------------------------------------------- the layers
def layer_gauges(tests, rule):
    """Per gauge the layer's (μ, σ): the mean of its tests' log ratios. rule 'index': an unjudged gauge enters as exactly 1 with
    no variance; rule 'carried': every measured gauge enters with its estimate and variance."""
    out = {}
    for g in GAUGES:
        es = []
        for t in tests:
            m = t["gauges"].get(g)
            if not m or m.get("est") is None:
                continue
            if rule == "index":
                es.append(m["est"] if (m["judged"] or m.get("exact")) else (0.0, 0.0))
            else:
                es.append(m["est"])
        out[g] = combine_mean(es) if es else None
    return out


def separability():
    """The governors' four ways: Omni-Compass on the organism alone (BARE) against on top of the orchestrator (TOP), per gauge; the
    two agree within the noise where the layers do not interact."""
    out = []
    for name, tag in GOVERNORS:
        top = LIVE / f"V12_{tag}_4W_TOP.json"
        bare = LIVE / f"V12_{tag}_4W_BARE.json"
        if not (top.exists() and bare.exists()):
            continue
        tt = test_from_abc(name, top.name, GOV_MEASURES, None)
        tb = test_from_abc(name, bare.name, GOV_MEASURES, None)
        for g in ("speed", "machines", "energy"):
            a, b = tt["gauges"].get(g), tb["gauges"].get(g)
            if not a or not b or a["est"] is None or b["est"] is None:
                continue
            dmu = a["est"][0] - b["est"][0]
            s = math.sqrt(a["est"][1] ** 2 + b["est"][1] ** 2)
            out.append({"governor": name, "gauge": g, "top": a["est"], "bare": b["est"], "delta": dmu, "sigma": s,
                        "agree": abs(dmu) <= Z * s if s > 0 else dmu == 0.0})
    return out


def beside():
    """The modelled organisms (class S) and the organisms with the real cluster inside (omni-v3): shown beside the total."""
    out = {}
    p = ROOT / "results" / "realms_v5" / "REALMS_V5.json"
    if p.exists():
        d = json.loads(p.read_text())
        orgs = {}
        for org in ("spine", "tower"):
            o = d["organisms"]["normal"].get(org)
            if o:
                s = o["summary"]
                orgs[org] = {"label": o["label"], "misses_pp": s["viol_pp"], "work": s["work"], "energy": s["energy"], "n": o["n"]}
        out["realms_v5"] = {"source": "results/realms_v5/REALMS_V5.md", "commit": d["run"].get("commit", "")[:12], "organisms": orgs}
    p = LIVE / "V3_SIX_KUBE.json"
    if p.exists():
        d = json.loads(p.read_text())
        rows = {}
        for key in ("tower@10", "tower@100", "stack@10", "stack@100"):
            o = d["organisms"].get(key)
            if o:
                r = o["rows"].get(P95)
                if r:
                    rows[key] = {"n": r["n"], "native": r["native"], "omni": r["omni"], "lo": r["lo"], "hi": r["hi"],
                                 "est": log_ratio("lower", r["native"], r["omni"], r["lo"], r["hi"], r["n"])}
        out["six_kube_v3"] = {"source": "results/live/V3_SIX_KUBE.md", "p95": rows}
    return out


# ----------------------------------------------------------------------------------------------------------------------- the page
def test_line(t):
    parts = []
    for g in GAUGES:
        m = t["gauges"].get(g)
        if not m:
            continue
        if m.get("exact"):
            parts.append(f"{g}: the same by design")
            continue
        parts.append(f"{g}: {fmt(m['est'])}, {m['reading'].split(' (')[0]}")
    return "; ".join(parts)


def held_layer(name):
    return next((why for pre, why in HELD_LAYERS.items() if name.startswith(pre)), None)


def composed(name, g, est):
    """What a layer's measured gauge enters the composition as: its own factor at the software end; exactly 1 (no variance) for a
    held gauge (energy, the bill) or a held layer (the chip, the wire); None where nothing was measured."""
    if est is None:
        return None
    if g in HELD or held_layer(name):
        return (0.0, 0.0)
    return est


def totals(layers, rule):
    measured = {name: layer_gauges(tests, rule) for name, tests in layers.items()}
    by_layer = {name: {g: composed(name, g, e) for g, e in gs.items()} for name, gs in measured.items()}
    total = {}
    for g in GAUGES:
        total[g] = combine_sum([by_layer[n][g] for n in by_layer if by_layer[n][g] is not None])
        if g in HELD:
            total[g] = (0.0, 0.0)
    idx_es = [total[g] for g in COMPOSED if total[g] is not None]
    k = len(idx_es)
    idx_mu = sum(m for m, _ in idx_es) / k if k else None
    idx_ind = math.sqrt(sum(s * s for _, s in idx_es)) / k if k else None
    idx_cor = sum(s for _, s in idx_es) / k if k else None
    return by_layer, total, (idx_mu, idx_ind, idx_cor), measured


def jsonable(o):
    if isinstance(o, dict):
        return {str(k): jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [jsonable(x) for x in o]
    if isinstance(o, float) and (math.isnan(o) or math.isinf(o)):
        return None
    return o


def main(argv=None):
    layers_all = {
        "1. the card (the chip), class P": card_tests(),
        "3. the cluster (Kubernetes, its add-ons, its governors), class L": cluster_tests(),
        "4. the services on the cluster, class L": service_tests(),
        "5. the cloud (Azure, the bill metered), class L": cloud_tests(),
    }
    layers_real = {k: v for k, v in layers_all.items() if not k.startswith("1.")}
    sep = separability()
    side = beside()
    from tools.omni_version import VERSIONS
    standing = f"omni-{next(iter(VERSIONS))}"    # the engine that stands: the version list's newest

    results, measured_all = {}, {}
    for scope, layers in ((SCOPE_WITH, layers_all), (SCOPE_WITHOUT, layers_real)):
        for rule in ("index", "carried"):
            by_layer, total, idx, measured = totals(layers, rule)
            results[(scope, rule)] = (by_layer, total, idx)
            measured_all[(scope, rule)] = measured

    L = []
    L.append("# The whole system: Omni-Compass at every layer, composed by the product law")
    L.append("")
    L.append(f"> {legal.TOP}")
    L.append("")
    L.extend(readings.receipt_key())
    L.append("")
    L.append("The founder's question of 20 October 2026: the cloud is the wire between the chip at one end and the software at the other; "
             "Omni-Compass sits at both ends and at every layer between; what is the total? This page answers it from the tables that stand, by "
             "one rule written once in `tools/whole_system.py`, which rebuilds the page and `results/WHOLE_SYSTEM.json` from them. Run and scored by "
             "The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.")
    L.append("")
    L.append("## 1. The equation")
    L.append("")
    L.append("For a gauge g with its declared aim a(g) (higher for work; lower for a wait; spent for a resource or a bill) and a layer ℓ measured "
             "native nℓ and with Omni-Compass oℓ, the layer's ratio is oriented toward the aim, so that above 1 is a GAIN at every layer alike:")
    L.append("")
    L.append("  Rℓ(g) = oℓ / nℓ when a(g) is higher;  Rℓ(g) = nℓ / oℓ when a(g) is lower or spent.")
    L.append("")
    L.append("Each layer is measured with the layer under it running as native runs it (the cluster's tests against the HPA; the governors' against the "
             "orchestrator as shipped; the cloud's against Azure's own autoscaler; the card's against the card's own limiter). The layers compose by "
             "multiplication, because each ratio is taken on what the layer under it hands up:")
    L.append("")
    L.append("  R(g) = ∏ℓ Rℓ(g),   G(g) = R(g) − 1,   log R(g) = Σℓ log Rℓ(g).")
    L.append("")
    L.append("The interval. A table gives, per run, the paired difference d = o − n with its 95% interval [lo, hi] over n paired repetitions (the exact "
             "Student t), so SE(d) = (hi − lo) / (2 t₀.₉₇₅,ₙ₋₁), and by the delta method SE(log R) = SE(d) / o. The three runs A, B and C of one test are "
             "pooled by inverse variance (μ = Σwᵢμᵢ / Σwᵢ, Var = 1 / Σwᵢ, wᵢ = 1/σᵢ²). A layer with k tests takes the mean of their log ratios (the "
             "geometric mean of the ratios, the Omni index's rule), Var = Σσᵢ² / k². The layers add in the log and their variances add, because every "
             "layer was measured in its own runs. The total's 95% interval is exp(μ ± 1.96 σ). The index over the gauges is the mean of the gauge logs; "
             "its interval is given under two bounds, the gauges independent (Var = Σσ² / k²) and the gauges perfectly correlated inside a run (σ = Σσ / k).")
    L.append("")
    L.append("What is composed (the founder's order of 31 October 2026). The whole organism is shown at the software end: **work, speed and machines "
             "are composed**. **The energy and the bill are held at native's** (exactly 1, shown beside, never composed): on the cluster the energy is a "
             "declared model of the machines row, never a meter, so composing it would count the fewer machines twice and claim a saving at the chip that "
             "no meter read; the cloud is the wire and its bill is kept exactly as native's, the benefit being more work for the same bill. **The chip and "
             "the wire enter as exactly 1 on every gauge**: the chip is kept exactly as native runs it (its own meter at the factory tune reads it so, "
             "section 2), and the cloud's runs are the check that the software end's benefit holds through the wire. The index over the gauges is the "
             "mean of the three composed gauges' logs: more work, faster, on fewer machines, for the same power and the same bill.")
    L.append("")
    L.append("Two readings of the same numbers. **By the index's rule** a gauge of a test enters only when its three-run reading is GAIN, LOSS or power "
             "given in all three of our runs; a STEADY gauge, a disagreement, or a table of one run enters as exactly 1 with no variance (nothing inside the "
             "noise is claimed either way). **With every interval carried**, every measured gauge enters with its pooled estimate and its variance whatever "
             "its reading, and the total's interval says what the noise allows.")
    L.append("")
    L.append("What the composition is, and is not. No run here stacked the layers: each factor is one layer's own measurement with the layer under it "
             "native. The product is a modelled composition (**class S**) of class P and class L measurements, under the assumption that a layer's ratio "
             "does not change when the layers under or over it also carry Omni-Compass (separability). Section 4 tests that assumption where the tables can "
             "(the governors' four ways). The stacked run, Omni-Compass at every layer at once against native at every layer, is the measurement that would "
             "replace this composition; until it exists this page is the answer the standing tables give, with its assumptions in the open. The layers "
             "also stand on different engines, each named in its row below (the card on omni-v21's card governor, the A100 three runs), so the "
             "composition is across engines, said so here, and remade as each layer's three runs on the engine that stands land.")
    L.append("")

    L.append("## 2. The layers, each from its own table")
    L.append("")
    L.append("Each layer's own measurement, read two ways, and what it enters the composition as (section 1).")
    L.append("")
    L.append("| Layer | Tests | Gauge | Measured, by the index's rule | Measured, every interval carried | Word (carried) | Enters the composition as |")
    L.append("|---|---:|---|---|---|---|---|")
    by_idx = measured_all[(SCOPE_WITH, "index")]
    by_car = measured_all[(SCOPE_WITH, "carried")]
    for name, tests in layers_all.items():
        first = True
        for g in GAUGES:
            a, b = by_idx[name].get(g), by_car[name].get(g)
            if a is None and b is None:
                continue
            how = held_layer(name) or HELD.get(g) or "its own factor"
            L.append(f"| {name if first else ''} | {len(tests) if first else ''} | {GAUGE_WORDS[g]} | {fmt(a)} | {fmt(b)} | {word_for(g, b)} | {how} |")
            first = False
    L.append("| 2. the machine (the kernel, bare metal, Kepler) | 0 | every gauge | not yet run (register row 79) | not yet run | not measured | exactly 1 |")
    L.append("")
    card = layers_all["1. the card (the chip), class P"]
    if card and card[0].get("primary"):
        pr = card[0]["primary"]
        sp, en = card[0]["gauges"].get("speed"), card[0]["gauges"].get("energy")
        sp_pct = pct(1.0 / interval(sp["est"])[0]) if sp and sp["est"] else "?"
        en_pct = pct(1.0 / interval(en["est"])[0]) if en and en["est"] else "?"
        r_pr = interval(pr["est"])[0]
        w_pr = (readings.STEADY if abs(r_pr - 1.0) < readings.SIZE_FLOOR else readings.GAIN if r_pr > 1.0 else readings.GIVEN)
        n_runs = len(pr["runs"])
        L.append(f"The card's primary gauge, work per energy (served requests per kJ): {fmt(pr['est'])} over its {n_runs} runs, "
                 f"{pr['reading']}; the same runs read the 95th percentile response {sp_pct} "
                 f"({sp['reading'] if sp else 'not measured'}) and the energy drawn {en_pct} "
                 f"({en['reading'] if en else 'not measured'}). It is omni-v21's card governor at the factory tune (the dial at the max) on top of "
                 "native's power cap at 70% of the card's top, read by the card's own meter (class P). The chip's work and energy read STEADY at the "
                 "factory tune, so the chip enters the composition as exactly 1: the chip kept exactly as native runs it is what its own meter reads. "
                 "The tune-down's three runs (results/gpu/V21_A100_SAVE_ABC.md) read the same requests served for 0.7% to 0.85% less of the card's "
                 "energy in each run, GAIN by the mean of the three runs: a changed tune, its own record, shown and never composed.")
        L.append("")

    L.append("### Every test behind the layers")
    L.append("")
    for name, tests in layers_all.items():
        L.append(f"**{name}**")
        L.append("")
        for t in tests:
            L.append(f"- {t['test']} ({t['engine']}; `{t['source']}`): {test_line(t)}")
        L.append("")

    L.append("## 3. The total")
    L.append("")
    L.append("| Scope | Reading | Gauge | R(g) | G(g), 95% interval | Word |")
    L.append("|---|---|---|---:|---|---|")
    for (scope, rule), (by_layer, total, idx) in results.items():
        rule_w = "by the index's rule" if rule == "index" else "every interval carried"
        for g in GAUGES:
            if total[g] is None:
                continue
            if g in HELD:
                L.append(f"| {scope} | {rule_w} | {GAUGE_WORDS_HELD[g]} | ×1 | exactly 1: {HELD[g]} | held |")
                continue
            r, lo, hi = interval(total[g])
            L.append(f"| {scope} | {rule_w} | {GAUGE_WORDS[g]} | ×{r:.4f} | {pct(r)} ({pct(lo)} to {pct(hi)}) | {word_for(g, total[g])} |")
        mu, s_ind, s_cor = idx
        if mu is not None:
            r = math.exp(mu)
            L.append(f"| {scope} | {rule_w} | **the index over work, speed and machines** | **×{r:.4f}** | **{pct(r)}** (gauges independent {pct(math.exp(mu - Z * s_ind))} to "
                     f"{pct(math.exp(mu + Z * s_ind))}; gauges correlated {pct(math.exp(mu - Z * s_cor))} to {pct(math.exp(mu + Z * s_cor))}) | "
                     f"{word_for('work', (mu, s_cor))} |")
    L.append("")
    (by_layer, total, idx) = results[(SCOPE_WITHOUT, "index")]
    (by_layer_c, total_c, idx_c) = results[(SCOPE_WITHOUT, "carried")]
    (by_layer_a, total_a, idx_a) = results[(SCOPE_WITH, "carried")]
    L.append("Read: the headline is the row **without the card, by the index's rule**: it counts only what held the same way in all three of our runs, "
             f"on real machines (class L), at the software end (the cluster and the services on it): **{pct(math.exp(idx[0]))}** over work, speed and "
             f"machines; work {pct(interval(total['work'])[0]) if total['work'] else 'not taken'}, speed {pct(interval(total['speed'])[0])} (native's "
             f"95th percentile response over Omni-Compass's), machines {pct(interval(total['machines'])[0])} (native's machines over Omni-Compass's), "
             "for the same power and the same bill (both held at native's, section 1). With every interval carried the same layers read "
             f"**{pct(math.exp(idx_c[0]))}** (gauges correlated: {pct(math.exp(idx_c[0] - Z * idx_c[2]))} to {pct(math.exp(idx_c[0] + Z * idx_c[2]))}). "
             f"With the card the index reads **{pct(math.exp(idx_a[0]))}** carried: the chip enters as exactly 1, so the two scopes read alike, and "
             "they are kept apart so the chip's own record stays in view.")
    L.append("")
    L.append("The cloud is the wire. Its bill is kept exactly as native's and the layer enters as exactly 1 on every gauge: the benefit lives at the "
             "software end and the wire carries it. The cloud's own runs are the check that it holds: on Azure's own autoscaler the bill read STEADY "
             "(four paired repetitions on the compass law, one run; the v1 fleet's steady set and burst STEADY too), shown in section 2 and never "
             "composed. Read through the cloud, the same index is more work for the same bill: the cost of each unit of work falls by the work's own "
             "factor while the bill stays native's.")
    L.append("")

    cost = cost_ledger(measured_all[(SCOPE_WITH, "carried")])
    L.append("## 3b. What the benefit cost: the chip, the energy and the wire against native")
    L.append("")
    L.append("The benefit above is the software end's. This section is the other half a buyer asks for: what it cost. Each hardware piece and the "
             "wire is read against native, every row of its own record, so it can be seen whether the software end's gain was bought by heating or "
             "wearing the chip, by drawing more power, by serving less, or by a bigger bill (do no harm, `DISCLOSURES.md` section 3). Nothing here is "
             "composed into the index; a LOSS row is shown and named, never cut.")
    L.append("")
    for pc in cost:
        L.append(f"**{pc['piece']}**" + (f": {pc['state']}." if pc.get("state") else f" (`{'`, `'.join(pc['sources'])}`)"))
        L.append("")
        if not pc["rows"]:
            continue
        L.append("| Part | Gauge | Reading against native |")
        L.append("|---|---|---|")
        for r in pc["rows"]:
            L.append(f"| {r['part']} | {r['gauge']} | {r['reading']} |")
        L.append("")
        c = pc["count"]
        L.append(f"{len(pc['rows'])} rows: {c[readings.GAIN]} GAIN, {c[readings.STEADY]} STEADY, {c[readings.GIVEN]} power given, {c[readings.LOSS]} LOSS, "
                 f"{c['the runs disagree']} where the runs disagree." + (f" The LOSS rows: {'; '.join(pc['loss'])}." if pc["loss"] else " No LOSS row."))
        L.append("")
    L.append("## 4. The assumption tested where the tables allow: separability, from the governors' four ways")
    L.append("")
    L.append("Omni-Compass on the organism alone (compassbare against nativebare) and on top of the orchestrator (compass against native), in the same "
             "repetitions, on omni-v12. If the layers did not interact the two ratios would agree; a difference clear of the noise says the orchestrator "
             "changes what Omni-Compass has to work with (a layer's factor is not a constant of the layer alone).")
    L.append("")
    L.append("| Governor | Gauge | On top of the orchestrator (TOP) | On the organism alone (BARE) | TOP ÷ BARE, 95% interval | Agree within the noise |")
    L.append("|---|---|---|---|---|---|")
    n_agree = 0
    for s in sep:
        r = math.exp(s["delta"])
        lo, hi = math.exp(s["delta"] - Z * s["sigma"]), math.exp(s["delta"] + Z * s["sigma"])
        n_agree += bool(s["agree"])
        L.append(f"| {s['governor']} | {GAUGE_WORDS[s['gauge']]} | {fmt(s['top'])} | {fmt(s['bare'])} | ×{r:.4f} ({pct(lo)} to {pct(hi)}) | {'yes' if s['agree'] else 'no'} |")
    if sep:
        L.append("")
        L.append(f"{n_agree} of {len(sep)} governor-gauge pairs agree within the noise. Where they do not, the orchestrator under Omni-Compass changed "
                 "its factor, and a product built from the organism-alone factor would misstate the stacked result there by the TOP ÷ BARE shown; the "
                 "composition in section 3 uses the TOP factors (Omni-Compass on top of what is actually there), which is the stacked measurement for that "
                 "pair of layers.")
    L.append("")

    L.append("## 5. Beside the total, never inside it")
    L.append("")
    rv = side.get("realms_v5")
    if rv:
        for org, o in rv["organisms"].items():
            m = o["misses_pp"]
            L.append(f"- The organisms, our own models (class S, `{rv['source']}`, commit {rv['commit']}): {'the spine' if org == 'spine' else 'the whole tower'} "
                     f"({o['n']} muscles) under its own load: {o['label'].lower().replace('_', ' ')}, misses {m[0]:+.3f} pp ({m[1]:+.3f} to {m[2]:+.3f}), "
                     f"work {100 * o['work'][0]:+.2f}%, power given {100 * o['energy'][0]:+.3f}%. A model's energy is not a meter's; these rows are shown, not composed.")
    sk = side.get("six_kube_v3")
    if sk:
        for key, r in sk["p95"].items():
            est = r["est"]
            L.append(f"- The organisms with the real cluster inside (omni-v3, `{sk['source']}`), {key.replace('@', ' at ')} copies, {r['n']} paired repetitions: "
                     f"the 95th percentile {fmt(est)}; an older engine's result, the road to this one, never composed with the rows above.")
    L.append("")

    L.append("## 6. What is missing, and what replaces what")
    L.append("")
    L.append("- **The machine** (the kernel, bare metal, Kepler and the machine's own meter; register row 79): not yet run. It enters as exactly 1.")
    L.append(f"- **The card on the engine that stands**: the {standing} runs on Lambda (one exact commit, on the founder's word) replace the omni-v21 rows; "
             "the chip enters as exactly 1 whatever they read, and they stand beside it.")
    L.append("- **The cloud at the tune-down**: the omni-v12 Azure sets (A, B and C of the steady set, the two bursts and the real day) give the bill its "
             "three-run reading; Google and Amazon follow on the same harness.")
    L.append("- **Every cluster and service table on omni-v12**: the campaign (`scripts/reruns.txt`) reruns every benchmark; each row above is replaced by "
             "its omni-v12 table as it lands, and this page is rebuilt (`python3 tools/whole_system.py`).")
    L.append("- **The stacked run**: Omni-Compass at every layer at once against native at every layer, the one measurement that makes the total class L "
             "and P instead of a composition. Preregistered before any run in `docs/WHOLE_SYSTEM_PREREGISTRATION.md` (three stacks: the cluster and "
             "its services on GitHub's machines; the cloud at the tune-down on Azure; the card beside the cluster on Lambda); its place is written "
             "here before its result exists.")
    L.append("")
    L.append("Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were "
             "written down in our own repository before the runs; nothing was filed with any outside body.")
    L.append("")
    L.append("---")
    L.append("")
    L.append(f"*{legal.NOTICE}*")
    L.append("")
    md_text = "\n".join(L)

    out = {"layers": {k: [{**t, "gauges": {g: {**m, "est": list(m["est"]) if m.get("est") else None} for g, m in t["gauges"].items()},
                           "primary": ({**t["primary"], "est": list(t["primary"]["est"])} if t.get("primary") else None)} for t in v]
                      for k, v in layers_all.items()},
           "totals": {f"{scope} | {rule}": {"by_layer": {n: {g: (list(e) if e else None) for g, e in bl.items()} for n, bl in by_layer.items()},
                                            "total": {g: (list(e) if e else None) for g, e in total.items()},
                                            "index": {"mu": idx[0], "sigma_independent": idx[1], "sigma_correlated": idx[2]}}
                      for (scope, rule), (by_layer, total, idx) in results.items()},
           "separability": [{**s, "top": list(s["top"]), "bare": list(s["bare"])} for s in sep],
           "cost": cost, "composed": list(COMPOSED), "held": HELD, "held_layers": HELD_LAYERS,
           "beside": side}
    js_text = json.dumps(jsonable(out), indent=1, ensure_ascii=False) + "\n"
    if "--check" in (argv if argv is not None else sys.argv[1:]):
        # 27 October 2026: the composition had stood on older tables while the engine that stands landed its own, because
        # nothing rebuilt it; verify.py now fails a push where it is not what the tables give
        bad = [str(q.relative_to(ROOT)) for q, t in ((OUT_MD, md_text), (OUT_JSON, js_text)) if not q.exists() or q.read_text(encoding="utf-8") != t]
        print("whole system: out of date (python3 tools/whole_system.py): " + ", ".join(bad) if bad else "whole system: in line with the tables")
        return 1 if bad else 0
    OUT_MD.write_text(md_text, encoding="utf-8")
    OUT_JSON.write_text(js_text, encoding="utf-8")
    (by_layer, total, idx) = results[(SCOPE_WITHOUT, "index")]
    print(f"whole system, without the card, by the index's rule: {pct(math.exp(idx[0]))} over the gauges; "
          + "; ".join(f"{g} {pct(interval(total[g])[0])}" for g in GAUGES if total[g]))
    (by_layer, total, idx) = results[(SCOPE_WITHOUT, "carried")]
    print(f"whole system, without the card, every interval carried: {pct(math.exp(idx[0]))} "
          f"({pct(math.exp(idx[0] - Z * idx[2]))} to {pct(math.exp(idx[0] + Z * idx[2]))}, gauges correlated)")
    print(f"wrote {OUT_MD.relative_to(ROOT)} and {OUT_JSON.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
