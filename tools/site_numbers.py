#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The numbers a website may show, each with its receipt: one file, written from the repository's own records, so no page
computes a headline of its own (the founder's words of 4 November: "every number that's in this website, if you don't have the
receipt for it ... cannot live nowhere in this website").

Each number carries its word (GAIN, STEADY, LOSS, power given, the runs disagree), the word first; its size and direction in
words; what it measures; where (the software end on GitHub's machines, the chip, through the cloud); its evidence class (L live
software, P a physical meter, S our own model); its engine; its receipt; and the one sentence a page may print. Beside them,
the numbers a page may not show as a result, each with the reason: our own model's columns (docs/history/model_tables/ABC_TABLE_MODEL.json) and
figures that no receipt carries.

The letters A, B and C mean three different things in this repository, and a page must never mix them:
  - in docs/history/model_tables/ABC_TABLE_MODEL.json (tools/abc_table.py, class S, our own model): A Kubernetes alone, B Omni-Compass on top of
    Kubernetes, C Omni-Compass alone (no Kubernetes);
  - in results/TWO_BILLS.json (the two bills): A the chip native, B the chip with Omni-Compass on native, C the cloud native,
    D the cloud with Omni-Compass on native;
  - in every three-run table: A, B and C are the three runs of one benchmark, each its own GitHub run.

    python3 tools/site_numbers.py           writes results/SITE_NUMBERS.json and results/SITE_NUMBERS.md
    python3 tools/site_numbers.py --check   exits 1 where either differs from the records
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from legal import PLAIN, stamp  # noqa: E402

OUT_JSON, OUT_MD = ROOT / "results" / "SITE_NUMBERS.json", ROOT / "results" / "SITE_NUMBERS.md"
R = lambda p: json.loads((ROOT / p).read_text(encoding="utf-8"))  # noqa: E731


def _dir(x: float) -> str:
    return "up" if x > 0 else "down" if x < 0 else "unchanged"


def _pct(x: float) -> str:
    return f"{abs(x):.1f}%"


def _engines(tests: list) -> str:
    vs = [int(m.group(1)) for t in tests for m in [re.search(r"/V(\d+)_", t.get("source") or "")] if m]
    if not vs:
        return "the tables' own engines"
    top = max(vs)
    rest = sorted({v for v in vs if v != top})
    return f"omni-v{top}" + (f" ({vs.count(top)} of its {len(vs)} benchmarks; {len(vs) - vs.count(top)} still on "
                             + ", ".join(f"omni-v{v}" for v in rest) + ")" if rest else "")


def _engine_words(tests: list) -> str:
    """The engines a composite is made of, in words: one engine by its name; several as each benchmark's newest engine with
    its count (the founder's order of 11 November: every number under its actual version, never the newest engine's name
    alone over tables an older engine made)."""
    vs = [int(m.group(1)) for t in tests for m in [re.search(r"/V(\d+)_", t.get("source") or "")] if m]
    if not vs:
        return "the tables' own engines"
    counts = sorted({v: vs.count(v) for v in vs}.items(), key=lambda kv: (-kv[1], -kv[0]))
    if len(counts) == 1:
        return f"omni-v{counts[0][0]}"
    return "each benchmark on its newest engine: " + ", ".join(f"{n} on omni-v{v}" for v, n in counts)


def build() -> dict:
    idx = R("results/OMNI_INDEX.json")
    ov = R("results/OVERSIGHT.json")
    a10 = R("results/gpu/V23_A10_CAP_FULL_ABC.json")
    wpb = R("results/WORK_PER_BILL.json")
    tb = R("results/TWO_BILLS.json")
    abc = R("docs/history/model_tables/ABC_TABLE_MODEL.json")
    eng = _engines(idx.get("tests") or [])
    soft = "the software end: real software on GitHub's own machines, never bare metal and never a cloud, with no bill in it"
    nums = []

    def add(**k):
        nums.append(k)

    h, s = idx["headline_pct"], idx["service_headline_pct"]
    add(id="omni_index", word="GAIN", value_pct=round(h, 1), direction=_dir(h), cls="L", place=soft, engine=eng,
        receipt="results/OMNI_INDEX.md", what="the Omni index: every real product counted once, work, speed and machines scored",
        sentence=f"The Omni index: GAIN, {_dir(h)} {_pct(h)} (work, speed and machines; real software on GitHub's machines; {_engine_words(idx.get('tests') or [])}).")
    add(id="work_and_speed", word="GAIN", value_pct=round(s, 1), direction=_dir(s), cls="L", place=soft, engine=eng,
        receipt="results/OMNI_INDEX.md", what="the same runs read on work and speed alone, the machines and energy shown and not scored",
        sentence=f"On work and speed alone, the same runs: GAIN, {_dir(s)} {_pct(s)} (real software on GitHub's machines; not a bill).")
    k8 = next((v for k, v in (idx.get("categories") or {}).items() if k.startswith("Real Kubernetes")), None)
    if k8 is not None:
        kt = [t for t in idx.get("tests") or [] if str(t.get("category", "")).startswith("Real Kubernetes")]
        # a test that reads LOSS by the index's own rule is named in the same sentence (the website seat of 7 November: the
        # sentence left out the fairness test's LOSS that docs/WEBSITE_CLAIMS.md and both fix sheets require)
        kl = [t for t in kt if t.get("index_pct") is not None and t["index_pct"] <= -0.5]
        kls = "; ".join(f"{t['test'].split(':')[0].strip().lower()}, {_dir(t['index_pct'])} {_pct(t['index_pct'])}" for t in kl)
        tail = (f"; {'one reads' if len(kl) == 1 else str(len(kl)) + ' read'} LOSS: {kls}" if kl else "")
        ke = _engine_words(kt)
        add(id="kubernetes", word="GAIN", value_pct=round(k8, 1), direction=_dir(k8), cls="L", place=soft, engine=ke,
            receipt="results/OMNI_INDEX.md", what="real Kubernetes, by the index's rule (work, speed and machines), the latest measured",
            losses=[{"test": t["test"], "value_pct": round(t["index_pct"], 1), "source": t.get("source")} for t in kl],
            sentence=f"Real Kubernetes on {ke}, the latest measured: GAIN, {_dir(k8)} {_pct(k8)} by the index's rule ({len(kt)} tests on "
                     f"GitHub's machines){tail}.")
    # the historical Kubernetes reading, under its own engine (the founder's determination of 11 November: both authentic
    # numbers kept, each labeled by its version, the older never written into the newer's file): read from the forensic record
    # of the fall between them, which holds both index files' Kubernetes values as committed
    fall = R("results/K8S_DECLINE_V21_V25.json") if (ROOT / "results" / "K8S_DECLINE_V21_V25.json").exists() else None
    if fall:
        v21 = fall["decomposition"]["index"]["omni-v21"]
        add(id="kubernetes_v21_historical", word="GAIN", value_pct=round(v21, 1), direction=_dir(v21), cls="L", place=soft,
            engine="omni-v21", receipt="docs/audits/K8S_V21_V25_DECLINE_2026-11-11.md",
            what="real Kubernetes on omni-v21, the historical reading of the same nine tests by the same rule (31 October)",
            sentence=f"Real Kubernetes on omni-v21, the historical reading of 31 October: GAIN, {_dir(v21)} {_pct(v21)} by the same "
                     f"rule on the same nine tests; why the later omni-v25 reading is lower is written in "
                     f"docs/audits/K8S_V21_V25_DECLINE_2026-11-11.md.")
    p, g = ov["pooled"], ov.get("pages") or {}
    add(id="alert_minutes", word=p["reading"].split(" ")[0], reading=p["reading"], value_pct=round(100 * p["change"], 1),
        direction=_dir(p["change"]), cls="L", place=soft, engine=ov["engine"], receipt="results/OVERSIGHT.md",
        what="the minutes a person on call would have a page open, all the Kubernetes tests together",
        sentence=f"The minutes a person would be paged: {p['reading']}, {_dir(p['change'])} {_pct(100 * p['change'])} ({ov['engine']}).")
    if g.get("change") is not None:
        add(id="pages", word=g["reading"].split(" ")[0], reading=g["reading"], value_pct=round(100 * g["change"], 1),
            direction=_dir(g["change"]), cls="L", place=soft, engine=ov["engine"], receipt="results/OVERSIGHT_PAGES.md",
            what="the pages a person would have been sent, counted from the raw files by the rule written before the count",
            sentence=f"The pages a person would be sent: {g['reading']}, {_dir(g['change'])} {_pct(100 * g['change'])} ({ov['engine']}).")
    row = a10["rows"]["energy per served request (J)"]
    ch = [100 * r["diff"] / r["native"] for r in row["runs"] if isinstance(r, dict) and r.get("native")]
    m = sum(ch) / len(ch)
    a10e = (a10["engine"][0] if isinstance(a10["engine"], list) else a10["engine"]).split(" ")[0]
    add(id="chip_energy_per_request", word=row["reading"].split(" ")[0], reading=row["reading"], value_pct=round(m, 1),
        direction=_dir(m), cls="P", place="the chip: one A10 card rented directly, its own power meter", engine=a10e,
        receipt="results/gpu/V23_A10_CAP_FULL_ABC.md",
        what="the energy for each request served, the power cap at 70% of the card's top, the full load",
        sentence=f"On one A10 card, its own meter: energy per request served {row['reading']}, {_dir(m)} {_pct(m)} ({a10e}).")
    bm = wpb["places"]["bare_metal"]
    gs = [r["G"] for r in eval_runs(bm.get("runs"))]
    add(id="chip_work_for_the_bill", word="the runs disagree" if bm.get("reading", "").startswith("the runs disagree") else bm.get("reading"),
        reading=bm.get("reading"), value_pct=None, runs_pct=[round(100 * x, 2) for x in gs], cls="P",
        place="the chip: one A10 card rented directly, its bill the rental", engine=bm.get("engine", "").split(" ")[0],
        receipt="results/TWO_BILLS.md", what="the work done for each dollar of the card's rental, G = (1 + ΔW) / (1 + ΔB) − 1",
        sentence="On the chip, the work for the bill: the runs disagree (" + ", ".join(f"{_dir(x)} {_pct(100 * x)}" for x in gs)
                 + "); not yet shown to rise.")
    cb = (tb.get("cloud") or {}).get("bill") or {}
    if cb.get("native"):
        bc = 100 * (cb["omni"] / cb["native"] - 1)
        add(id="cloud_bill", word="power given", reading="power given, inside the noise", value_pct=round(bc, 1),
            direction=_dir(bc), cls="L", place="through the cloud: Azure, its own bill", engine=(tb.get("cloud") or {}).get("engine"),
            receipt=(tb.get("cloud") or {}).get("page") or "results/TWO_BILLS.md",
            what="the cloud's bill, Omni-Compass on top of native against native, by the mean of the paired repetitions",
            sentence=f"Through the cloud (Azure): the bill power given, {_dir(bc)} {_pct(bc)}, inside the noise; the work was not counted, "
                     "so the work per dollar is not read yet.")
    w, mlt = abc["web"], abc["multi"]
    sp = lambda v: 100 * (v["A"]["mean_ms"] / v["C"]["mean_ms"] - 1)  # noqa: E731
    nh = lambda v: 100 * (v["C"]["node_hours"] / v["A"]["node_hours"] - 1)  # noqa: E731
    en = lambda v: 100 * (v["C"]["energy_kwh"] / v["A"]["energy_kwh"] - 1)  # noqa: E731
    gpu = abc["gpu"]
    gp = 100 * (gpu["A"]["energy_kwh"] / gpu["C"]["energy_kwh"] - 1)
    no = [
        {"id": "abc_web_speed", "value_pct": None, "receipt": "docs/history/model_tables/ABC_TABLE_MODEL.json (tools/abc_table.py)",
         "why": f"our own model (class S), Omni-Compass alone (its column C, no Kubernetes) against Kubernetes alone (column A): "
                f"the mean response time only, while the same column used {_pct(nh(w))} more machine-hours and {_pct(en(w))} more "
                "energy. Not a whole-system gain, not bare metal, not the cloud, and a model is never proof."},
        {"id": "abc_multi_speed", "value_pct": None, "receipt": "docs/history/model_tables/ABC_TABLE_MODEL.json (tools/abc_table.py)",
         "why": f"the same model's multi-service column: Omni-Compass alone against Kubernetes alone, the mean response time "
                f"only, with {_pct(nh(mlt))} more machine-hours and {_pct(en(mlt))} more energy. Class S, never a result."},
        {"id": "abc_gpu_energy", "value_pct": None, "receipt": "docs/history/model_tables/ABC_TABLE_MODEL.json (tools/abc_table.py)",
         "why": "the same model's GPU scenario (class S): Omni-Compass alone against Kubernetes alone, the energy. Not a GPU "
                "measurement: the card's own meter reads energy per request served as the chip number above says."},
        {"id": "abc_column_b", "value_pct": round(100 * (w["B"]["mean_ms"] / w["A"]["mean_ms"] - 1), 1),
         "receipt": "docs/history/model_tables/ABC_TABLE_MODEL.json (tools/abc_table.py)",
         "why": "in that model, Omni-Compass on top of Kubernetes (column B) reads the same as Kubernetes alone on web and "
                "multi; the model is a tuning bench, not the record."},
        {"id": "drain_20_percent", "value_pct": 20.0, "receipt": "none",
         "why": "a 20% operational drain (13% machines + 7% people) is not on the record: the Omni index (" + _pct(h) + ", "
                "results/OMNI_INDEX.md) is work, speed and machines on GitHub's machines, not a bill, and the people line measured is the pages (results/OVERSIGHT_PAGES.md), "
                "worth about 2% of a run cost at a 7% people share; percentages of different bills do not add."},
        {"id": "sixteen_million", "value_pct": None, "receipt": "none",
         "why": "$16 million is 20% of $100 million; the 20% has no receipt, so neither does the $16 million."},
        {"id": "free_work_33", "value_pct": 33.0, "receipt": "none",
         "why": "no table, chip receipt or cloud receipt carries a 33% rise in work for the bill."},
        {"id": "arm_d_work_per_dollar", "value_pct": None, "receipt": AKS.replace(".json", ".md"),
         "why": "arm D stands, from the Azure set on file (the four arms above, every gauge paired with arm C); what it cannot "
                "show yet is the work per dollar, because that set sent a fixed rate of requests and counted no work. Nor is "
                "there a column D in docs/history/model_tables/ABC_TABLE_MODEL.json, so no D may be read from our own model."},
        {"id": "thirteen_point_one", "value_pct": 13.1, "receipt": "results/WHOLE_SYSTEM.md (section 4)",
         "why": "no record carries 13.1% as a headline: it appears only inside single rows of the whole-system page's "
                "separability check (Kueue's machines on the organism alone; KubeRay's modelled energy), one-row readings "
                "on omni-v12 used to test an assumption, never a result to headline."},
    ]
    arms = four_arms(tb, a10)
    for ln in arms["sentences"]:
        nums.append(ln)
    for n in nums:                                  # every reading says why its word reads so (the founder's order of 6 November)
        n["why"] = why(n)
    return {"notice": PLAIN, "source": "tools/site_numbers.py", "four_arms": arms["arms"],
            "rule": ("Every number a page shows comes from 'show', with its word first, its class, its place, its engine and its "
                     "receipt, in its own sentence. Nothing in 'not_for_the_site' is shown as a result. Our own model (class S) "
                     "is never shown as proof. Percentages of different bills are never added."),
            "letters": {"docs/history/model_tables/ABC_TABLE_MODEL.json": "class S, our own model: A Kubernetes alone, B Omni-Compass on top of "
                        "Kubernetes, C Omni-Compass alone", "results/TWO_BILLS.json": "the two bills: A the chip native, B the chip "
                        "with Omni-Compass on native, C the cloud native, D the cloud with Omni-Compass on native",
                        "three-run tables": "A, B and C are the three runs of one benchmark"},
            "show": nums, "not_for_the_site": no}


AKS = "results/live/AKS_STEADY_100_OMNI_V18.json"

# what each gauge on the site is for (its aim), so the word is read from the aim and never from the sign of the number
AIMS = {
    "omni_index": "the index scores the work done, the response time and the machines against native's: above native is more work, a faster answer or fewer machines",
    "work_and_speed": "the same runs scored on the work done and the response time alone: above native is more work or a faster answer",
    "kubernetes": "the index's rule on the Kubernetes tests: above native is more work, a faster answer or fewer machines",
    "alert_minutes": "the minutes a person on call would have a page open: fewer minutes mean less waiting on a person",
    "pages": "the pages a person would be sent: fewer pages mean less oversight",
    "chip_energy_per_request": "the energy the card's own meter read for each request served: less energy for each request served is more work from each joule",
    "chip_work_for_the_bill": "the work done for each dollar of the card's rental: more work for the bill helps",
    "cloud_bill": "the cloud's bill is a resource spent, read beside the work it bought",
    "arm_b_vs_a": "the work done for each dollar on the chip, Omni-Compass on native (B) against native (A)",
    "arm_d_vs_c": "the cloud, Omni-Compass on native (D) against native (C), gauge by gauge",
}
VERDICT = {
    "GAIN": "the change helps the system, so it reads GAIN",
    "LOSS": "the change hurts the system, so it reads LOSS",
    "power given": "more of a resource was spent beside the work it bought, so it reads power given, never a loss",
    "STEADY": "no change beyond the 0.5% floor, so it reads STEADY",
    "the runs disagree": "the three runs moved in opposite directions, so the test is unstable there and no word is given",
    "one run": "one run so far, so there is no three-run reading yet",
}


def why(n: dict) -> str:
    """The reason a reading's word reads so: what its gauge is for, then whether the change helps or hurts the system."""
    w = str(n.get("word") or "")
    v = next((VERDICT[k] for k in VERDICT if w.startswith(k)), "")
    a = AIMS.get(n.get("id"), n.get("what") or "")
    return "; ".join(x for x in (a, v) if x) + "."
D_GAUGES = (("compute bill at list price ($)", "the bill", "usd"), ("machines billed, machine-hours", "machine-hours", "h"),
            ("response time (ms), mean", "the mean response time", "ms"), ("response time (ms), 95th percentile", "the 95th percentile", "ms"),
            ("response time (ms), 99th percentile", "the 99th percentile", "ms"), ("failed requests (%)", "failed requests", "%"),
            ("alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line)", "the alert minutes", "min"),
            ("energy (Wh)", "the energy", "Wh"))


def four_arms(tb: dict, a10: dict) -> dict:
    """The two bills' four arms, each from its receipt: A the chip native and B the chip with Omni-Compass on native (one A10,
    the card's rental and the requests it served, three runs); C the cloud native and D the cloud with Omni-Compass on native
    (Azure, one run of paired repetitions). Nothing is run again: D is the Omni-Compass side of the Azure set already on file."""
    ch = tb.get("chip") or {}
    runs = ch.get("runs") or []
    eng = (ch.get("engine") or "").split(" ")[0]
    rec_chip = "results/TWO_BILLS.md (" + "results/gpu/V23_A10_CAP_FULL_ABC.md" + ")"
    per = ch.get("per_run") or []
    A = [{"run": runs[i] if i < len(runs) else None, "work": r["native"]["work"], "bill_usd": round(r["native"]["bill"], 6),
          "work_per_dollar": round(r["native"]["per_dollar"], 1)} for i, r in enumerate(per)]
    B = [{"run": runs[i] if i < len(runs) else None, "work": r["omni"]["work"], "bill_usd": round(r["omni"]["bill"], 6),
          "work_per_dollar": round(r["omni"]["per_dollar"], 1)} for i, r in enumerate(per)]
    g = [b["work_per_dollar"] / a["work_per_dollar"] - 1 for a, b in zip(A, B)]
    aks = R(AKS)
    pc = (aks.get("paired") or {}).get("compass") or {}
    cl = tb.get("cloud") or {}
    C, D, dvc = {}, {}, []
    for key, name, unit in D_GAUGES:
        v = pc.get(key)
        if not isinstance(v, dict) or not v.get("native"):
            continue
        C[name] = {"value": round(v["native"], 4), "unit": unit}
        D[name] = {"value": round(v["omni"], 4), "unit": unit}
        chg = 100 * v["diff"] / v["native"]
        spent = unit in ("usd", "h", "Wh")                 # a resource: a rise is power given, a fall a GAIN; every other gauge here aims lower
        word = "STEADY" if abs(chg) < 0.5 else ("power given" if spent else "LOSS") if chg > 0 else "GAIN"
        dvc.append({"gauge": name, "word": word, "change_pct": round(chg, 1), "direction": _dir(chg), "beyond_the_noise": bool(v.get("significant"))})
    reps = cl.get("repetitions") or aks.get("repetitions")
    arms = {
        "A": {"name": "the chip native", "place": "one A10 card rented directly; its bill the rental", "class": "P", "engine": eng,
              "receipt": rec_chip, "runs": A},
        "B": {"name": "the chip with Omni-Compass on native", "place": "the same card, the same rented window", "class": "P",
              "engine": eng, "receipt": rec_chip, "runs": B,
              "against_A": {"work_for_the_bill_pct": [round(100 * x, 2) for x in g],
                            "reading": (tb.get("chip") or {}).get("reading") or "the runs disagree"}},
        "C": {"name": "the cloud native", "place": "Azure (AKS), its own bill", "class": "L", "engine": cl.get("engine"),
              "receipt": cl.get("page") or AKS.replace(".json", ".md"), "repetitions": reps, "values": C},
        "D": {"name": "the cloud with Omni-Compass on native", "place": "Azure (AKS), the same machines, paired with C",
              "class": "L", "engine": cl.get("engine"), "receipt": cl.get("page") or AKS.replace(".json", ".md"),
              "repetitions": reps, "values": D, "against_C": dvc,
              "note": "one run of paired repetitions on omni-v18 at the tune-down on the machines alone; the work was not counted "
                      "(a fixed rate of requests), so the work per dollar is not read; the counted runs on the engine that stands "
                      "are queued (scripts/azure_queue.txt)"},
    }
    sig = [x for x in dvc if x["beyond_the_noise"]]
    inside = [x for x in dvc if not x["beyond_the_noise"]]
    s_d = (f"Arm D, the cloud with Omni-Compass on native, against arm C, the cloud native (Azure, {reps} paired repetitions, one run, "
           f"{cl.get('engine')}): " + "; ".join(f"{x['gauge']} {x['word']}, {x['direction']} {_pct(x['change_pct'])}, beyond the noise" for x in sig)
           + ("; " if sig and inside else "") + "; ".join(f"{x['gauge']} {x['word']}, {x['direction']} {_pct(x['change_pct'])}, inside the noise" for x in inside)
           + "; the work not counted, so the work per dollar is not read yet.")
    s_b = ("Arm B, the chip with Omni-Compass on native, against arm A, the chip native (one A10, three runs, " + eng + "): the work for "
           "the bill " + ", ".join(f"{_dir(100 * x)} {_pct(100 * x)}" for x in g) + ": the runs disagree, not yet shown to rise.")
    sentences = [
        {"id": "arm_b_vs_a", "word": "the runs disagree", "reading": "the runs disagree", "value_pct": None,
         "runs_pct": [round(100 * x, 2) for x in g], "cls": "P", "place": arms["B"]["place"], "engine": eng, "receipt": rec_chip,
         "what": "the four arms: B against A", "sentence": s_b},
        {"id": "arm_d_vs_c", "word": "one run", "reading": "one run, read gauge by gauge: " + "; ".join(f"{w} on {', '.join(x['gauge'] for x in dvc if x['word'] == w)}" for w in ("LOSS", "GAIN", "power given", "STEADY") if any(x["word"] == w for x in dvc))
                   + ("; beyond the noise in " + ", ".join(x["gauge"] for x in sig) if sig else "; every gauge inside the noise"),
         "value_pct": None, "cls": "L", "place": arms["D"]["place"], "engine": cl.get("engine"), "receipt": arms["D"]["receipt"],
         "what": "the four arms: D against C", "sentence": s_d}]
    return {"arms": arms, "sentences": sentences}


def eval_runs(x):
    """The work-per-bill runs list, whether the record holds it as a list or as its printed form."""
    if isinstance(x, list):
        return [r for r in x if isinstance(r, dict) and "G" in r]
    return []


def markdown(d: dict) -> str:
    L = ["# The Numbers a Website May Show, Each With Its Receipt", "",
         "Written by `tools/site_numbers.py` from the repository's own records; `results/SITE_NUMBERS.json` is the same in a "
         "form a page reads. " + d["rule"], "",
         "| Number | Word | Why it reads so | Class | Where | Engine | Receipt |", "|---|---|---|---|---|---|---|"]
    for n in d["show"]:
        L.append(f"| {n['sentence']} | {n.get('reading') or n['word']} | {n.get('why', '')} | {n['cls']} | {n['place']} | {n['engine']} | `{n['receipt']}` |")
    fa = d.get("four_arms") or {}
    if fa:
        L += ["", "## The four arms, A, B, C and D, each from its receipt", "",
              "| Arm | What it is | Where | Class | Engine | Receipt |", "|---|---|---|---|---|---|"]
        for k in "ABCD":
            x = fa.get(k) or {}
            L.append(f"| {k} | {x.get('name')} | {x.get('place')} | {x.get('class')} | {x.get('engine')} | `{x.get('receipt')}` |")
        L += ["", "Arm D is the Omni-Compass side of the Azure set already on file, paired repetition by repetition with arm C: no run "
              "is needed to have it, and its counted runs on the engine that stands are queued.", ""]
    L += ["", "## Not for the site, and why", "", "| Figure | Why it is not a result | Where it comes from |", "|---|---|---|"]
    for n in d["not_for_the_site"]:
        v = "—" if n["value_pct"] is None else f"{n['value_pct']:.1f}%"
        L.append(f"| {n['id']} ({v}) | {n['why']} | `{n['receipt']}` |")
    L += ["", "## The letters A, B, C and D", ""] + [f"- `{k}`: {v}." for k, v in d["letters"].items()] + [
        "", "Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.", ""]
    return "\n".join(stamp(L)) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    d = build()
    js, md = json.dumps(d, indent=1, ensure_ascii=False) + "\n", markdown(d)
    if a.check:
        bad = [p.relative_to(ROOT).as_posix() for p, s in ((OUT_JSON, js), (OUT_MD, md)) if not p.exists() or p.read_text(encoding="utf-8") != s]
        print("the website's numbers: " + ("in line with the records" if not bad else "out of date: " + ", ".join(bad) + " (python3 tools/site_numbers.py)"))
        return 1 if bad else 0
    OUT_JSON.write_text(js, encoding="utf-8")
    OUT_MD.write_text(md, encoding="utf-8")
    print(f"{OUT_JSON.relative_to(ROOT)}: {len(d['show'])} numbers with receipts, {len(d['not_for_the_site'])} not for the site")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
