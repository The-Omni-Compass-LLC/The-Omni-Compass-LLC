#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The whole organism, two ways, for the live benchmark engine page (docs/engine/OMNI_COMPASS_LIVE_ENGINE.html, section 11).

The repository composes the layers of the whole system by the product law in one place, tools/whole_system.py, which writes
results/WHOLE_SYSTEM.json and results/WHOLE_SYSTEM.md: for every gauge g and layer ℓ an oriented ratio Rℓ(g) (above 1 is
toward the aim at every layer alike), the layers composed by R(g) = ∏ℓ Rℓ(g), every interval carried in logarithms (the
delta method, A, B and C pooled by inverse variance, the layers' variances added), two readings of the same numbers (by the
index's rule: only what held the same way in all three of our runs; with every interval carried), two scopes (with the
card's one old run; without it) and the separability assumption tested on the governors' four ways.

This file recomputes nothing from the tables. It reads that file and regroups its layers into the two ways a stack is bought:

  on-site bare metal   the software on the bare metal:                          software (the cluster, the services) × bare metal (the card, the machine)
  through the cloud    the cloud's build, its bare metal at the back end,
                       the software:                                            cloud × bare metal × software
                       and the cloud as two pieces beside it (the back-end bare metal left to the provider): cloud × software

For a scenario the factors of the layers it stacks are summed in the logarithm, their variances added, exactly as the file's
rule composes any set of layers; the index over the gauges is the mean of the gauge logarithms, its interval given under the
file's two bounds (the gauges independent; the gauges perfectly correlated). A layer the file lists as not yet run (the
machine) enters as exactly 1 and is named. Every layer's tests, the separability test and what stands beside the total are
carried through for the page to show, word for word.

  python3 docs/engine/export_whole.py [out.json]
"""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT))

from tools.readings import GAIN, STEADY, LOSS, GIVEN  # noqa: E402

WS = ROOT / "results" / "WHOLE_SYSTEM.json"
GAUGES = ("work", "speed", "machines", "energy", "bill")
SPENT = {"machines", "energy", "bill"}
GAUGE_WORDS = {"work": "work (more)", "speed": "speed (the 95th percentile response, shorter)", "machines": "machines (fewer)",
               "energy": "energy (held at native's: the same power)", "bill": "the bill (held at native's: the same bill)"}
# the founder's order of 31 October 2026 (tools/whole_system.py, COMPOSED and HELD): the whole organism is shown at the software end;
# work, speed and machines are composed; the energy and the bill are held at native's, exactly 1, and never enter the index
COMPOSED = ("work", "speed", "machines")
HELD = ("energy", "bill")
# the three pieces a stack is bought in, each a group of the file's layers (matched by the layer's number in the file's own names)
GROUPS = [
    ("software", "Software", (3, 4)),
    ("hardware", "Bare Metal", (1, 2)),
    ("cloud", "Cloud", (5,)),
]
# every way a stack is bought (the founder's order of 20 October): on-site bare metal; through the cloud (three pieces, and the
# cloud as two pieces beside it); in the device (the bare metal alone: Omni-Compass built into the card and the machine, nothing
# else wired); as a service (the software alone: the owner has neither the bare metal nor the cloud account, Omni-Compass sits in
# the software run for them). Each sums the layers of the pieces it names; a piece with no factor counts as exactly 1.
SCENARIOS = [
    ("onsite", "On-Site Bare Metal", ("software", "hardware"), None),
    ("cloud", "Through the Cloud", ("cloud", "hardware", "software"), ("cloud", "software")),
    ("device", "In the Device", ("hardware",), None),
    ("service", "As a Service", ("software",), None),
]
NOT_RUN = {2: "the machine (the kernel, bare metal, Kepler): not yet run (register row 79), enters as exactly 1"}
Z95 = 1.959963984540054


def layer_no(name: str) -> int | None:
    m = re.match(r"\s*(\d+)\.", name)
    return int(m.group(1)) if m else None


def word_of(gauge: str, mu: float, sigma: float) -> str:
    """The word of a composed factor by the key's floor (tools/readings.py, the founder's order of 24 October 2026; the mathematics
    seat of 24 October): a change of 0.5% or more reads by the gauge's aim, whatever its interval, STEADY only under 0.5%. Whether
    its 95% interval stands clear of no change is carried beside it (clear_of), never as the word."""
    from tools.readings import SIZE_FLOOR
    if abs(math.exp(mu) - 1) < SIZE_FLOOR:
        return STEADY
    if mu > 0:
        return GAIN
    return GIVEN if gauge in SPENT else LOSS


def clear_of(mu: float, sigma: float) -> bool:
    """True when the composed factor's 95% interval stands clear of no change (a ratio of 1)."""
    return mu - Z95 * sigma > 0 or mu + Z95 * sigma < 0


def factor(mu: float | None, sigma: float | None, gauge: str) -> dict | None:
    if mu is None:
        return None
    sigma = sigma or 0.0
    return {"mu": mu, "sigma": sigma, "ratio": math.exp(mu), "pct": 100 * (math.exp(mu) - 1),
            "lo_pct": 100 * (math.exp(mu - Z95 * sigma) - 1), "hi_pct": 100 * (math.exp(mu + Z95 * sigma) - 1), "word": word_of(gauge, mu, sigma),
            "clear": clear_of(mu, sigma)}


def compose(parts: list[dict]) -> dict:
    """The product over layers (a sum of logarithms, the variances added), per gauge, and the index over the gauges with the file's two bounds."""
    out = {"gauges": {}}
    for g in GAUGES:
        have = [p[g] for p in parts if p.get(g)]
        if not have:
            continue
        mu = sum(x[0] for x in have)
        var = sum((x[1] or 0.0) ** 2 for x in have)
        out["gauges"][g] = dict(factor(mu, math.sqrt(var), g), layers=len(have))
    for g in HELD:
        if g in out["gauges"]:
            out["gauges"][g]["held"] = True
    comp = [v for g, v in out["gauges"].items() if g in COMPOSED]
    k = len(comp)
    if k:
        mus = [v["mu"] for v in comp]
        sig = [v["sigma"] for v in comp]
        mu = sum(mus) / k
        s_ind, s_cor = math.sqrt(sum(s * s for s in sig)) / k, sum(sig) / k
        out["index"] = {"mu": mu, "ratio": math.exp(mu), "pct": 100 * (math.exp(mu) - 1), "gauges": k,
                        "independent": [100 * (math.exp(mu - Z95 * s_ind) - 1), 100 * (math.exp(mu + Z95 * s_ind) - 1)],
                        "correlated": [100 * (math.exp(mu - Z95 * s_cor) - 1), 100 * (math.exp(mu + Z95 * s_cor) - 1)],
                        "word": word_of("index", mu, s_cor), "clear": clear_of(mu, s_cor)}
    return out


def main(out):
    if not WS.exists():
        Path(out).write_text(json.dumps({"missing": str(WS.relative_to(ROOT))}), encoding="utf-8")
        print("whole: results/WHOLE_SYSTEM.json is not in this checkout (python3 tools/whole_system.py)")
        return
    d = json.loads(WS.read_text(encoding="utf-8"))
    layer_names = {layer_no(n): n for n in d["layers"]}
    # every layer the file knows, grouped into the three pieces; a layer missing from the file's tables is not yet run
    groups = []
    for key, name, nos in GROUPS:
        layers = []
        for n in nos:
            if n in layer_names:
                ln = layer_names[n]
                tests = d["layers"][ln]
                for t in tests:   # a table's title as the page prints it: the word "brake" is retired (the founder's order of 12 October)
                    for k in ("test", "title"):
                        if isinstance(t.get(k), str):
                            t[k] = t[k].replace("emergency brake", "emergency stop")
                layers.append({"no": n, "name": ln, "state": "measured", "tests": tests, "n_tests": len(tests),
                               "cls": (re.search(r"class ([PLS])", ln) or [None, None])[1]})
            else:
                layers.append({"no": n, "name": NOT_RUN.get(n, f"layer {n}: not yet run"), "state": "not yet run", "tests": [], "n_tests": 0, "cls": None})
        groups.append({"key": key, "name": name, "layers": layers})
    # the file's totals: scope × reading, each with its factors per layer and gauge
    scopes = {}
    for tk, tv in d["totals"].items():
        scope, reading = [s.strip() for s in tk.split("|")]
        scopes.setdefault(scope, {})[reading] = tv
    scope_keys = {"with": next((s for s in scopes if s.startswith("with the card")), None), "without": next((s for s in scopes if s.startswith("without")), None)}
    readings = ("index", "carried")
    results = {}                                              # results[scope][reading] = {groups: {key: compose}, layers: {no: {gauge: factor}}, scenarios: {key: compose}, file_total: ...}
    for sk, sname in scope_keys.items():
        if not sname:
            continue
        results[sk] = {"name": sname}
        for rd in readings:
            tv = scopes[sname].get(rd)
            if not tv:
                continue
            by_layer = {layer_no(n): v for n, v in tv["by_layer"].items()}
            per_layer = {str(n): {g: factor(*(v[g] or [None, None]), g) if v.get(g) else None for g in GAUGES} for n, v in by_layer.items()}
            grp = {}
            for g_ in groups:
                parts = [by_layer[l["no"]] for l in g_["layers"] if l["no"] in by_layer]
                grp[g_["key"]] = dict(compose(parts), layers_in=[l["no"] for l in g_["layers"] if l["no"] in by_layer])
            scen = {}
            for key, name, gks, two in SCENARIOS:
                parts = [by_layer[l["no"]] for gk in gks for l in next(x for x in groups if x["key"] == gk)["layers"] if l["no"] in by_layer]
                sc = dict(compose(parts), name=name, groups=list(gks))
                if two:
                    p2 = [by_layer[l["no"]] for gk in two for l in next(x for x in groups if x["key"] == gk)["layers"] if l["no"] in by_layer]
                    sc["two_piece"] = dict(compose(p2), groups=list(two))
                scen[key] = sc
            ft = {g: factor(*(tv["total"][g] or [None, None]), g) if tv["total"].get(g) else None for g in GAUGES}
            fi = tv.get("index") or {}
            file_total = {"gauges": ft, "index": {"mu": fi.get("mu"), "pct": None if fi.get("mu") is None else 100 * (math.exp(fi["mu"]) - 1),
                          "independent": None if fi.get("mu") is None else [100 * (math.exp(fi["mu"] - Z95 * fi["sigma_independent"]) - 1), 100 * (math.exp(fi["mu"] + Z95 * fi["sigma_independent"]) - 1)],
                          "correlated": None if fi.get("mu") is None else [100 * (math.exp(fi["mu"] - Z95 * fi["sigma_correlated"]) - 1), 100 * (math.exp(fi["mu"] + Z95 * fi["sigma_correlated"]) - 1)]}}
            results[sk][rd] = {"layers": per_layer, "groups": grp, "scenarios": scen, "file_total": file_total}
    sep = d.get("separability") or []
    data = {"file": "results/WHOLE_SYSTEM.md", "json": "results/WHOLE_SYSTEM.json", "tool": "tools/whole_system.py", "gauges": list(GAUGES), "gauge_words": GAUGE_WORDS,
            "groups": groups, "scenarios": [{"key": k, "name": n, "groups": list(g), "two_piece": list(t) if t else None} for k, n, g, t in SCENARIOS],
            "results": results, "separability": {"pairs": sep, "n": len(sep), "agree": sum(1 for s in sep if s.get("agree"))}, "beside": d.get("beside") or {},
            "cost": d.get("cost") or [], "held_why": d.get("held") or {}, "held_layers": d.get("held_layers") or {},
            "composed": list(COMPOSED), "held": list(HELD),
            "rule": "R(g) = ∏ℓ Rℓ(g), log R = Σℓ log Rℓ, the variances added; a scenario sums the layers it stacks; work, speed and machines are composed at the software end, "
                    "the energy and the bill held at native's (exactly 1) and the chip and the wire entered as exactly 1 (the founder's order of 31 October 2026); "
                    "the index is the mean of the three composed gauges' logarithms, "
                    "its 95% interval under two bounds (the gauges independent; perfectly correlated); two readings: by the index's rule, only what held the same way "
                    "in all three of our runs enters; with every interval carried, everything measured enters with its interval; each composed factor's word by the key's "
                    "floor (0.5% or more by the gauge's aim, STEADY under it), whether its interval stands clear of no change said beside it"}
    Path(out).write_text(json.dumps(data, separators=(",", ":"), ensure_ascii=False, allow_nan=False), encoding="utf-8")
    for sk, R in results.items():
        for rd in readings:
            if rd not in R:
                continue
            S = R[rd]["scenarios"]
            print(f"{sk:8s} {rd:8s} " + " · ".join(f"{k} {v['index']['pct']:+.2f}% {v['index']['word']} ({v['index']['correlated'][0]:+.1f} to {v['index']['correlated'][1]:+.1f})" for k, v in S.items() if v.get("index")))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "whole.json")
