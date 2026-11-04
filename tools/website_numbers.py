#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The only numbers the website may print, each with its words and its receipt (the founder's words of 4 November: "every number
that's in this website, if you don't have the receipt for it ... cannot live nowhere in this website"; "it's four arms, A, B, C
and D"). Written from the records, never typed: the Omni index and its six categories, the four arms (A the chip native, B the
chip with Omni-Compass on native, C the cloud native, D the cloud with Omni-Compass on native), the oversight line, and the
numbers that must not appear, each with where it came from. The website reads results/WEBSITE_NUMBERS.json from main and prints
nothing else; A, B and C of a three-run table are three runs of one test, never arms.

    python3 tools/website_numbers.py          writes results/WEBSITE_NUMBERS.json and docs/WEBSITE_NUMBERS.md
    python3 tools/website_numbers.py --check  fails when either differs from the records
"""
import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT_JSON = ROOT / "results" / "WEBSITE_NUMBERS.json"
OUT_MD = ROOT / "docs" / "WEBSITE_NUMBERS.md"
sys.path.insert(0, str(ROOT / "tools"))
from legal import PLAIN, stamp  # noqa: E402

OWN_RUNS = "Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results."
CLOUD_TABLE = ROOT / "results" / "live" / "AKS_STEADY_100_OMNI_V18.md"


def _j(rel):
    p = ROOT / rel
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def _pct(x, digits=1):
    return f"{abs(x):.{digits}f}%"


def _word(pct, aim="higher"):
    """The one key on an index or category change in percent: from 0.5% up GAIN or LOSS by the aim, under it STEADY."""
    if abs(pct) < 0.5:
        return "STEADY, under the floor"
    good = pct > 0 if aim == "higher" else pct < 0
    return "GAIN" if good else "LOSS"


def _standing():
    vs = [int(m.group(1)) for f in ROOT.glob("OMNI_V*.json") if (m := re.fullmatch(r"OMNI_V(\d+)", f.stem))]
    return f"omni-v{max(vs)}" if vs else "unknown"


def _cloud_rows():
    """Arm C against arm D, gauge by gauge, as the cloud's table prints them (one set of paired repetitions)."""
    rows = []
    if not CLOUD_TABLE.exists():
        return rows
    for line in CLOUD_TABLE.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 6 or cells[0] in ("Gauge", "") or set(cells[0]) <= set("-: "):
            continue
        gauge, native, omni, change, interval, sig = cells
        word = ("GAIN" if "GAIN" in sig else "LOSS" if "LOSS" in sig else "shown, not judged" if "shown" in sig
                else "STEADY, no difference beyond the noise")
        rows.append({"gauge": gauge, "C_native": native, "D_omni_on_native": omni, "change": change, "interval_95": interval,
                     "reading": word})
    return rows


def numbers() -> dict:
    idx = _j("results/OMNI_INDEX.json")
    wpb = _j("results/WORK_PER_BILL.json").get("places", {})
    ov = _j("results/OVERSIGHT.json")
    chip, cloud = wpb.get("bare_metal") or {}, wpb.get("cloud") or {}
    tests = idx.get("tests", [])
    engines = sorted({m.group(1) for t in tests if (m := re.search(r"V(\d+)_", t.get("source", "")))}, key=int)
    rows = _cloud_rows()
    where = "real software on GitHub's own machines (never called bare metal, never the chip, never the cloud)"
    out = {
        "notice": PLAIN,
        "rule": ("The website prints these numbers in these words and no other. A, B and C of a three-run table are three runs of "
                 "one test (replications); the four arms are A, B, C and D. A number not in this file is not printed."),
        "engine_that_stands": _standing(),
        "index": {
            "figure_of_record": {"value_pct": round(idx.get("headline_pct", 0), 1), "words": f"{_word(idx.get('headline_pct', 0))}, up {_pct(idx.get('headline_pct', 0))}",
                                 "what": "the Omni index: work, speed and machines, every real test weighed together",
                                 "tests": len(tests), "tables_engine": ", ".join(f"omni-v{e}" for e in engines), "where": where,
                                 "record": "results/OMNI_INDEX.json headline_pct", "class": "L"},
            "second_reading": {"value_pct": round(idx.get("service_headline_pct", 0), 1),
                               "words": f"{_word(idx.get('service_headline_pct', 0))}, up {_pct(idx.get('service_headline_pct', 0))}",
                               "what": "the same index on work and speed alone (its second reading, never the headline)",
                               "record": "results/OMNI_INDEX.json service_headline_pct", "class": "L"},
            "categories": [{"category": k, "value_pct": round(v, 1),
                            "words": f"{_word(v)}, {'up' if v >= 0 else 'down'} {_pct(v)}",
                            "record": "results/OMNI_INDEX.json categories"} for k, v in (idx.get("categories") or {}).items()],
            "categories_rule": "all six categories are printed together, losses included, or none",
        },
        "arms": {
            "A": {"name": "the chip, native", "status": "read", "engine": chip.get("engine", ""),
                  "bill_per_run": [r["B"][0] for r in chip.get("runs", [])], "work_per_run": [r["W"][0] for r in chip.get("runs", [])],
                  "record": chip.get("source", ""), "class": "P (the card's own meter) and L"},
            "B": {"name": "the chip with Omni-Compass on native", "status": "read", "engine": chip.get("engine", ""),
                  "bill_per_run": [r["B"][1] for r in chip.get("runs", [])], "work_per_run": [r["W"][1] for r in chip.get("runs", [])],
                  "G_against_A_per_run": [("up " if r["G"] >= 0 else "down ") + _pct(r["G"] * 100) for r in chip.get("runs", [])],
                  "words": chip.get("reading", ""), "record": chip.get("source", ""), "class": "P and L"},
            "C": {"name": "the cloud, native", "status": "read", "engine": cloud.get("engine", ""),
                  "bill_per_repetition_usd": (cloud.get("bill") or [None])[0], "repetitions": cloud.get("repetitions"),
                  "conditions": cloud.get("conditions", ""), "record": cloud.get("source", ""), "class": "L (the cloud's own bill)"},
            "D": {"name": "the cloud with Omni-Compass on native",
                  "status": ("read: it holds (no judged gauge reads LOSS)" if rows and not any(r["reading"] == "LOSS" for r in rows)
                             else "read: a judged gauge reads LOSS (see against_C)" if rows else "not yet read"),
                  "engine": cloud.get("engine", ""), "bill_per_repetition_usd": (cloud.get("bill") or [None, None])[1],
                  "repetitions": cloud.get("repetitions"), "conditions": cloud.get("conditions", ""),
                  "against_C": rows,
                  "work_per_dollar": ("not read by the meter on this set: its load sent a fixed rate, the same in both arms; the "
                                      "sets with the work meter are queued (docs/K8S_COMPASS_PREREGISTRATION.md, the amendments of "
                                      "31 October, night, and 4 November)"),
                  "record": cloud.get("source", ""), "class": "L (the cloud's own bill)"},
            "google_amazon": "wired as Azure is, not yet run (their keys are not in the repository's secrets)",
        },
        "oversight": ({"words": f"{(ov.get('pooled') or {}).get('reading', '')}: the minutes an on-call page would be open, down "
                                f"{_pct((ov.get('pooled') or {}).get('change', 0) * 100)}",
                       "tests": (ov.get("count") or {}).get("tests"), "engine": ov.get("engine"), "record": "results/OVERSIGHT.json",
                       "class": "L"} if ov else {}),
        "not_allowed": [
            {"number": "47.2%", "source": "docs/history/model_tables/ABC_TABLE_MODEL.json (was results/ABC_TABLE.json): the web "
             "workload's mean response time, 215.1 ms for Kubernetes alone against 146.1 ms for Omni-Compass alone, in our own "
             "model (class S) of October; Omni-Compass alone is not an arm, and the same model reads its energy up 26%",
             "why": "a model's speed ratio, never a receipt, never whole-system, never bare metal"},
            {"number": "49.9%", "source": "the same model table, the multi workload (217.9 ms against 145.4 ms)",
             "why": "a model's speed ratio, never a receipt, never the cloud"},
            {"number": "+5.3% GPU energy", "source": "the same model table, the gpu workload (194.1 against 184.4 kWh, Omni-Compass alone)",
             "why": "a model, never the card's meter; the card's receipts are arms A and B"},
            {"number": "+28.0% Kubernetes alone", "source": "results/OMNI_INDEX.json, one of six categories",
             "why": "a category is printed only with the other five, losses included"},
            {"number": "+12.9% bare metal; +5.0% through the cloud", "source": "results/OMNI_INDEX.json",
             "why": "both are the Omni index over real tests on GitHub's own machines; neither is bare metal or the cloud"},
            {"number": "20% drain, 2.9% stack tax, 7% engineering, $16M, +33% free work, 13.1%, 140%", "source": "outside AI text",
             "why": "no record carries them (docs/WEBSITE_CLAIMS.md)"},
            {"number": "three arms", "source": "the website's own words", "why": "four arms, A, B, C and D; A, B and C of a table are runs"},
        ],
        "own_runs": OWN_RUNS,
    }
    return out


def markdown(n: dict) -> str:
    i, a = n["index"], n["arms"]
    L = ["# The Website's Numbers, Each With Its Receipt", "",
         "The website prints only the numbers in `results/WEBSITE_NUMBERS.json`, in its words; this page is the same file for a "
         f"reader (`python3 tools/website_numbers.py`). The engine that stands: {n['engine_that_stands']}. {n['rule']}", "",
         "## The Omni index", "",
         f"- **{i['figure_of_record']['words']}** — {i['figure_of_record']['what']}; {i['figure_of_record']['tests']} tests on "
         f"{i['figure_of_record']['tables_engine']}'s tables, {i['figure_of_record']['where']} (`{i['figure_of_record']['record']}`).",
         f"- Its second reading: **{i['second_reading']['words']}** — {i['second_reading']['what']}.", "",
         "| Category | Reading |", "|---|---|"]
    L += [f"| {c['category']} | {c['words']} |" for c in i["categories"]]
    L += ["", f"{i['categories_rule'].capitalize()}.", "", "## The four arms", "",
          "| Arm | What it is | Status | Engine |", "|---|---|---|---|"]
    L += [f"| {k} | {a[k]['name']} | {a[k]['status']} | {a[k]['engine']} |" for k in "ABCD"]
    L += ["", f"B against A, the work for the bill per run: {', '.join(a['B'].get('G_against_A_per_run', []))}: {a['B'].get('words', '')}.",
          "", f"D against C ({a['D']['repetitions']} paired repetitions; {a['D']['conditions']}):", "",
          "| Gauge | C, native | D, Omni-Compass on native | Change | 95% interval | Reading |", "|---|---|---|---|---|---|"]
    L += [f"| {r['gauge']} | {r['C_native']} | {r['D_omni_on_native']} | {r['change']} | {r['interval_95']} | {r['reading']} |"
          for r in a["D"]["against_C"]]
    L += ["", f"D's work per dollar: {a['D']['work_per_dollar']}. Google and Amazon: {a['google_amazon']}.", ""]
    if n["oversight"]:
        L += ["## The people on call", "", f"{n['oversight']['words'].capitalize()}, {n['oversight']['tests']} tests on {n['oversight']['engine']} "
              f"(`{n['oversight']['record']}`).", ""]
    L += ["## Never printed", "", "| Number | Where it came from | Why not |", "|---|---|---|"]
    L += [f"| {x['number']} | {x['source']} | {x['why']} |" for x in n["not_allowed"]]
    L += ["", n["own_runs"]]
    return "\n".join(stamp(L)) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    n = numbers()
    js, md = json.dumps(n, indent=1, ensure_ascii=False) + "\n", markdown(n)
    if a.check:
        ok = OUT_JSON.exists() and OUT_JSON.read_text(encoding="utf-8") == js and OUT_MD.exists() and OUT_MD.read_text(encoding="utf-8") == md
        print("the website's numbers: " + ("in line with the records" if ok else "differ (python3 tools/website_numbers.py)"))
        return 0 if ok else 1
    OUT_JSON.write_text(js, encoding="utf-8")
    OUT_MD.write_text(md, encoding="utf-8")
    print(f"{OUT_JSON.relative_to(ROOT)} and {OUT_MD.relative_to(ROOT)} written from the records")
    return 0


if __name__ == "__main__":
    sys.exit(main())
