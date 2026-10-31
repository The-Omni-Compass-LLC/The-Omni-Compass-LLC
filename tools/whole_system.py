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
GPU_RUN = ROOT / "results" / "gpu" / "run-20261024T091235Z"

GAUGES = ("work", "speed", "machines", "energy", "bill")
AIM = {"work": "higher", "speed": "lower", "machines": "spent", "energy": "spent", "bill": "spent"}
GAUGE_WORDS = {"work": "work (more)", "speed": "speed (the 95th percentile response, lower)", "machines": "machines (fewer)",
               "energy": "energy (less)", "bill": "the bill (smaller)"}
Z = 1.959964

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
    p = GPU_RUN / "GPU_REPS.json"
    if not p.exists():
        return []
    d = json.loads(p.read_text())
    paired = (d.get("paired") or {}).get("omni") or {}
    n = len([x for x in GPU_RUN.iterdir() if x.name.startswith("rep-")]) or 10
    t = {"test": (f"NVIDIA A100 (SXM4, 40 GB) on Lambda, the card's own meter, Omni-Compass on the power limit and the clock ceiling, "
                  f"{n} paired repetitions, one run (24 October; at its limit on native: the governor wrote nothing)"),
         "source": str((GPU_RUN / "GPU_REPS.md").relative_to(ROOT)), "runs": [], "engine": "omni-v18 (the card governor at commit e3b05dc, the branch gpu-omni-v18)",
         "pairs": [n], "gauges": {}, "primary": None}
    for g, key in CARD_MEASURES.items():
        row = paired.get(key)
        if row:
            lo, hi = row.get("ci95") or (None, None)
            t["gauges"][g] = {"row": key, "reading": "one run: clear of the noise" if (lo is not None and (lo > 0 or hi < 0)) else "one run: the interval includes zero",
                              "judged": False, "est": log_ratio(AIM[g], row["native"], row["omni"], lo, hi, n), "runs": [(row["native"], row["omni"])]}
    row = paired.get(CARD_PRIMARY)
    if row:
        lo, hi = row.get("ci95") or (None, None)
        t["primary"] = {"row": CARD_PRIMARY, "est": log_ratio("higher", row["native"], row["omni"], lo, hi, n), "runs": [(row["native"], row["omni"])]}
    return [t]


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


def totals(layers, rule):
    by_layer = {name: layer_gauges(tests, rule) for name, tests in layers.items()}
    total = {}
    for g in GAUGES:
        total[g] = combine_sum([by_layer[n][g] for n in by_layer if by_layer[n][g] is not None])
    idx_es = [total[g] for g in GAUGES if total[g] is not None]
    k = len(idx_es)
    idx_mu = sum(m for m, _ in idx_es) / k if k else None
    idx_ind = math.sqrt(sum(s * s for _, s in idx_es)) / k if k else None
    idx_cor = sum(s for _, s in idx_es) / k if k else None
    return by_layer, total, (idx_mu, idx_ind, idx_cor)


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

    results = {}
    for scope, layers in (("with the card's one run", layers_all), ("without the card (the cluster, the services and the cloud)", layers_real)):
        for rule in ("index", "carried"):
            by_layer, total, idx = totals(layers, rule)
            results[(scope, rule)] = (by_layer, total, idx)

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
             "also stand on different engines, each named in its row below (the card on omni-v18's card governor, the A100 run of 24 October), so the "
             "composition is across engines, said so here, and remade as each layer's three runs on the engine that stands land.")
    L.append("")

    L.append("## 2. The layers, each from its own table")
    L.append("")
    L.append("| Layer | Tests | Gauge | By the index's rule | With every interval carried | Word (carried) |")
    L.append("|---|---:|---|---|---|---|")
    by_idx = results[("with the card's one run", "index")][0]
    by_car = results[("with the card's one run", "carried")][0]
    for name, tests in layers_all.items():
        first = True
        for g in GAUGES:
            a, b = by_idx[name].get(g), by_car[name].get(g)
            if a is None and b is None:
                continue
            L.append(f"| {name if first else ''} | {len(tests) if first else ''} | {GAUGE_WORDS[g]} | {fmt(a)} | {fmt(b)} | {word_for(g, b)} |")
            first = False
    L.append("| 2. the machine (the kernel, bare metal, Kepler) | 0 | every gauge | not yet run (register row 79): enters as exactly 1 | not yet run | not measured |")
    L.append("")
    card = layers_all["1. the card (the chip), class P"]
    if card and card[0].get("primary"):
        pr = card[0]["primary"]
        sp, en = card[0]["gauges"].get("speed"), card[0]["gauges"].get("energy")
        sp_pct = pct(1.0 / interval(sp["est"])[0]) if sp and sp["est"] else "?"
        en_pct = pct(1.0 / interval(en["est"])[0]) if en and en["est"] else "?"
        r_pr = interval(pr["est"])[0]
        w_pr = (readings.STEADY if abs(r_pr - 1.0) < readings.SIZE_FLOOR else readings.GAIN if r_pr > 1.0 else readings.GIVEN)
        L.append(f"The card's primary gauge, work per energy (served requests per kJ): {fmt(pr['est'])} in its one run, native {pr['runs'][0][0]:.2f} → "
                 f"{pr['runs'][0][1]:.2f}, {w_pr} by the one key; the same run read the 95th percentile response {sp_pct} "
                 f"({word_for('speed', sp['est']) if sp else 'not measured'}) and the energy drawn {en_pct} "
                 f"({word_for('energy', en['est']) if en else 'not measured'}). It is omni-v18's card governor at the factory tune, one run (B and C "
                 "not yet run): the card's own setting already holds both knobs at their top, so the governor wrote nothing (at its limit on native). It is "
                 "carried here because it is the only real-meter measurement of the chip layer, and the totals are given with and without it.")
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
            r, lo, hi = interval(total[g])
            L.append(f"| {scope} | {rule_w} | {GAUGE_WORDS[g]} | ×{r:.4f} | {pct(r)} ({pct(lo)} to {pct(hi)}) | {word_for(g, total[g])} |")
        mu, s_ind, s_cor = idx
        if mu is not None:
            r = math.exp(mu)
            L.append(f"| {scope} | {rule_w} | **the index over the gauges** | **×{r:.4f}** | **{pct(r)}** (gauges independent {pct(math.exp(mu - Z * s_ind))} to "
                     f"{pct(math.exp(mu + Z * s_ind))}; gauges correlated {pct(math.exp(mu - Z * s_cor))} to {pct(math.exp(mu + Z * s_cor))}) | "
                     f"{word_for('work', (mu, s_cor))} |")
    L.append("")
    (by_layer, total, idx) = results[("without the card (the cluster, the services and the cloud)", "index")]
    (by_layer_c, total_c, idx_c) = results[("without the card (the cluster, the services and the cloud)", "carried")]
    (by_layer_a, total_a, idx_a) = results[("with the card's one run", "carried")]
    L.append("Read: the headline is the row **without the card, by the index's rule**: it counts only what held the same way in all three of our runs, "
             f"on real machines (class L), and composes the cluster, the services on it and the cloud: **{pct(math.exp(idx[0]))}** over the gauges, "
             f"speed {pct(interval(total['speed'])[0])}, machines {pct(interval(total['machines'])[0])}, energy {pct(interval(total['energy'])[0])}, "
             f"work {pct(interval(total['work'])[0]) if total['work'] else 'not taken'}, the bill {pct(interval(total['bill'])[0]) if total['bill'] else 'not taken'}. "
             "With every interval carried the same layers read "
             f"**{pct(math.exp(idx_c[0]))}** (gauges correlated: {pct(math.exp(idx_c[0] - Z * idx_c[2]))} to {pct(math.exp(idx_c[0] + Z * idx_c[2]))}); the cloud's "
             "wide one-run intervals (4 and 5 paired repetitions) are what widen it. With the card's one old run carried the chip's speed LOSS of that "
             f"run pulls the index to **{pct(math.exp(idx_a[0]))}** and its energy GAIN adds to the energy row; the card's omni-v12 run replaces that row.")
    L.append("")
    L.append("The cloud is the wire, and it has its own factor: the bill. On Azure's own autoscaler the bill read STEADY (×1.000 inside the noise, four "
             "paired repetitions on the compass law; the v1 fleet's steady set and burst STEADY too), so the cloud layer multiplies the total by 1 so far: "
             "the benefit measured is at the two ends and the layers between, and the cloud carries it without adding or taking. The omni-v12 Azure "
             "sets at the tune-down (the bill at native's work, `scripts/azure_queue.txt`) are the measurement of that factor; the bill row here changes "
             "the day their three-run tables land.")
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
    L.append(f"- **The card on the engine that stands**: the {standing} run on Lambda (`gpu-{standing}`, one exact commit) replaces the 2 October row.")
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
    (by_layer, total, idx) = results[("without the card (the cluster, the services and the cloud)", "index")]
    print(f"whole system, without the card, by the index's rule: {pct(math.exp(idx[0]))} over the gauges; "
          + "; ".join(f"{g} {pct(interval(total[g])[0])}" for g in GAUGES if total[g]))
    (by_layer, total, idx) = results[("without the card (the cluster, the services and the cloud)", "carried")]
    print(f"whole system, without the card, every interval carried: {pct(math.exp(idx[0]))} "
          f"({pct(math.exp(idx[0] - Z * idx[2]))} to {pct(math.exp(idx[0] + Z * idx[2]))}, gauges correlated)")
    print(f"wrote {OUT_MD.relative_to(ROOT)} and {OUT_JSON.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
