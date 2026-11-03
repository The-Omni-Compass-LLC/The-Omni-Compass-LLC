#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The oversight line: the pages a person would have answered, native against Omni-Compass on native, from the records alone,
and how that line enters the bill.

The founder's words of 3 November: the engineering share of an IT bill lives in the oversight, "they don't need a 3 a.m. call
and they don't need [anyone] to turn knobs when OmniCompass is ... self-gauging". GitHub's machines run unattended in both
arms, so no engineer's hour is on any receipt; what every real Kubernetes receipt does measure is what would have paged a
person (the alert minutes, tools/live_reps.py `babysitting`) and the settings the governor wrote on its own. This page reads
both from every Kubernetes three-run table on the newest engine that has them, and puts the pages through the one equation
as the bill's people line, b = Σₖ sₖ·bₖ, with the people's share an owner's own figure (the founder's example: 7%).

    python3 tools/oversight.py          writes results/OVERSIGHT.md and results/OVERSIGHT.json
    python3 tools/oversight.py --check  fails when either differs from the records
"""
import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT_MD, OUT_JSON = ROOT / "results" / "OVERSIGHT.md", ROOT / "results" / "OVERSIGHT.json"
sys.path.insert(0, str(ROOT / "tools"))
from legal import stamp  # noqa: E402

OWN_RUNS = "Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results."
ALERT, COMMANDS = "alert minutes", "settings commands the governor wrote on its own"
SHARE_EXAMPLE, SPEND_EXAMPLE = 0.07, 100.0   # the founder's example of 3 November (7% of the bill), on the $100 M example budget


def tables() -> tuple:
    """Every Kubernetes three-run table of the newest engine that carries the alert minutes (results/live/V<n>_*.json)."""
    by = {}
    for f in (ROOT / "results" / "live").glob("V*_*.json"):
        m = re.fullmatch(r"V(\d+)_.+", f.stem)
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        rows = d.get("rows")
        if not m or not isinstance(rows, dict) or not any(k.startswith(ALERT) for k in rows):
            continue
        by.setdefault(int(m.group(1)), []).append((f, d))
    if not by:
        return None, []
    v = max(by)
    return v, sorted(by[v], key=lambda x: x[0].name)


def _mean(runs, side):
    xs = [r[side] for r in runs if r.get(side) is not None]
    return sum(xs) / len(xs) if xs else None


def build() -> dict:
    v, found = tables()
    rows = []
    for f, d in found:
        R = d["rows"]
        a = R[next(k for k in R if k.startswith(ALERT))]
        c = next((R[k] for k in R if k.startswith(COMMANDS)), None)
        n, o = _mean(a["runs"], "native"), _mean(a["runs"], "omni")
        rows.append({"test": d.get("title") or f.stem, "record": f.relative_to(ROOT).as_posix(), "runs": len(a["runs"]),
                     "repetitions": [r.get("paired_repetitions") for r in d.get("runs") or []],
                     "native": n, "omni": o, "change": (o / n - 1) if n else None, "reading": a.get("reading"),
                     "per_run": [{"native": r["native"], "omni": r["omni"]} for r in a["runs"]],
                     "commands": _mean(c["runs"], "omni") if c else None})
    tn, to = sum(r["native"] for r in rows), sum(r["omni"] for r in rows)
    pooled = (to / tn - 1) if tn else None
    people = SHARE_EXAMPLE * pooled if pooled is not None else None
    return {"engine": f"omni-v{v}" if v else None, "question": "they don't need a 3 a.m. call and they don't need [anyone] to turn knobs "
            "when OmniCompass is ... self-gauging", "said": "the founder, 3 November 2026", "rows": rows,
            "pooled": {"native": tn, "omni": to, "change": pooled},
            "count": {"tests": len(rows), "fewer": sum(1 for r in rows if r["omni"] < r["native"]),
                      "to_zero": sum(1 for r in rows if r["native"] > 0 and r["omni"] == 0),
                      "same": sum(1 for r in rows if r["omni"] == r["native"]), "more": sum(1 for r in rows if r["omni"] > r["native"])},
            "equation": {"bill": "B = Σₖ cₖ; b = Σₖ sₖ·bₖ, sₖ = cₖ(native) / B(native)",
                         "people_line": "b(people) = the change in alert minutes (stated assumption: the time a page takes moves with the pages)",
                         "into_g": "G = (1 + ΔW) / (1 + ΔB) − 1, the people line inside ΔB as s(people)·b(people)"},
            "example": {"share": SHARE_EXAMPLE, "spend_musd": SPEND_EXAMPLE, "bill_change": people,
                        "musd": SPEND_EXAMPLE * people if people is not None else None,
                        "label": "an example, the founder's of 3 November: the people who watch and tune the stack at 7% of the bill; "
                                 "no receipt carries the 7%, and an owner puts in its own share"},
            "sources": sorted(r["record"] for r in rows)}


def _pc(x: float) -> str:
    return f"{abs(x) * 100:.1f}%"


def markdown(d: dict) -> str:
    rows, p, c, ex = d["rows"], d["pooled"], d["count"], d["example"]
    eng = d["engine"]
    L = ["# The Oversight Line: the Pages a Person Would Answer, Native Against Omni-Compass on Native", "",
         f"> \"{d['question'][0].upper() + d['question'][1:]}\" ({d['said']})", "",
         "## What GitHub's runs measure, and what they cannot", "",
         "Every benchmark runs on GitHub's own machines with nobody watching, in both arms: no person is on call, no person turns a "
         "knob, so no engineer's hour and no salary is on any receipt, and none can be. What every real Kubernetes receipt does "
         "measure is the event that calls a person: an **alert minute**, a whole minute of the measured window whose 95th "
         "percentile response time, failed requests counted over, was over the response line, the minute an on-call page would be "
         "open (`tools/live_reps.py`, `babysitting`; judged, fewer is GAIN). Beside it each receipt shows the settings the governor "
         "wrote on its own, each in its audit with its reason and read back (shown, not judged: native's own autoscaler runs "
         "untouched in both arms).", "",
         f"## The pages, test by test ({eng}, every real Kubernetes three-run table that carries them)", "",
         "| Test | Alert minutes a repetition, native → Omni-Compass on native (mean of the three runs) | Change | Reading (the table's own, the one key) | Settings the governor wrote on its own, a repetition | Record |",
         "|---|---|---|---|---|---|"]
    for r in rows:
        ch = ("none in either arm" if not r["native"] and not r["omni"] else "—" if not r["native"] else "the same" if r["change"] == 0
              else ("down " if r["change"] < 0 else "up ") + _pc(r["change"]))
        cm = "—" if r["commands"] is None else f"{r['commands']:.1f}"
        L.append(f"| {r['test']} | {r['native']:.2f} → {r['omni']:.2f} | {ch} | {r['reading']} | {cm} | `{r['record']}` |")
    L += ["", f"**Together.** Over the {c['tests']} tests the pages a repetition add up to {p['native']:.1f} alert minutes on native and "
          f"{p['omni']:.1f} with Omni-Compass on top: **down {_pc(p['change'])}** (our arithmetic over the tables, each test weighed by "
          f"its own minutes; the two-hour test holds {max(rows, key=lambda r: r['native'])['native'] / p['native'] * 100:.0f}% of "
          f"native's). Fewer pages in {c['fewer']} of the {c['tests']} tests, to none at all in {c['to_zero']}, the same in "
          f"{c['same']}, more in {c['more']}. Each test's word is its own table's, by the one key.", "",
          "## The people line, through the one equation", "",
          "The bill is the sum of its lines, B = Σₖ cₖ, and each line's change counts by its share of native's bill, "
          "b = Σₖ sₖ·bₖ (`docs/WORK_PER_BILL.md`). The people who watch and tune a stack are one line, k = people, with its share "
          "s(people) of the owner's bill. The receipts give that line's change only where the time spent moves with the pages; "
          "stated as the assumption it is: b(people) = the change in alert minutes. The line then moves the whole bill by "
          "s(people)·b(people), and it enters the benefit only through the bill: G = (1 + ΔW) / (1 + ΔB) − 1.", "",
          f"**The example, not a result.** At the founder's example share, 7% of the bill (no receipt carries it; it plays the part "
          f"the 2.9% plays in the $100 M example), the measured fall in pages moves the bill by 0.07 × (−{_pc(p['change'])}) = "
          f"**down {_pc(ex['bill_change'])} of the whole bill**: on the $100 M example, about ${abs(ex['musd']):.1f} M a year of the "
          "people's time no longer spent answering pages, at native's cost. A larger share gives a larger line in proportion "
          f"(10% gives down {_pc(0.10 * p['change'])}); an owner's own share and its own count of pages replace both numbers.", "",
          "## What is not claimed", "",
          "- **Not a 20% (13% + 7%).** The 12.9% is the software end's second reading of the Omni index (work and speed, on GitHub's "
          "machines), not a bill; 7% is a share of a bill, not a gain. A reading and a share do not add; the people line enters G "
          "only through ΔB, as above.",
          "- **Not the people removed.** The record counts pages, not heads or salaries. An on-call rotation is staffed whether or not "
          "it is paged; what falls is the time the pages take, the triage and the hand tuning after them.",
          "- **Not every page gone, and never nobody.** Pages fell in most tests and to none in some, not in all. A person keeps the "
          "kill switch (one hand, instant, security only), sets the response line and chooses the profile.", "",
          "## Questions and answers", "",
          "**Why do the benchmarks not show the engineering cost?** Because GitHub's machines run with nobody on call in either arm: "
          "there is no engineer's hour to count. The receipts count what would have called one, the alert minutes, and the settings "
          "the governor wrote itself.", "",
          "**What does self-gauging mean here?** At every beat the governor reads the system's own meters, decides, writes a setting "
          "only through the plug, reads the write back and records its reason in its audit; it acts on the reading before the line "
          "is crossed, where a person acts after the page. In the tests above it wrote its settings on its own, the number in the "
          "table, with no person touching either arm.", "",
          "**Could the real number be bigger?** It can. An owner's people share may be larger than 7%, and a stack carries many "
          "services, each with its own pages, where each test here reads one. It can also be smaller: the record measures pages, "
          "and how much of a person's time moves with them is the owner's to count.", "",
          "**Does Omni-Compass replace the on-call engineer?** No. It takes pages away where its reading acts before the line; the "
          "person keeps the switch, the line and the profile.", "",
          "**How does an owner measure it on its own stack?** Count the alert minutes with the same rule, native and with "
          "Omni-Compass on top, over the same load (the receipts' rule: a whole minute whose 95th percentile was over the line), "
          "and the time each page took from the on-call tool; s(people) is the owner's own payroll for that work over its bill.", "",
          f"Engines: the tables are {eng}'s, the newest engine whose Kubernetes tables have landed; every benchmark runs again on the "
          "engine that stands, and this page is written again from the records when they land (`python3 tools/oversight.py`).", "",
          OWN_RUNS]
    return "\n".join(stamp(L)) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    d = build()
    js, md = json.dumps(d, indent=1, ensure_ascii=False) + "\n", markdown(d)
    if a.check:
        bad = [p.relative_to(ROOT).as_posix() for p, s in ((OUT_JSON, js), (OUT_MD, md)) if not p.exists() or p.read_text(encoding="utf-8") != s]
        print("the oversight line: " + ("in line with the records" if not bad else ", ".join(bad) + " differ (python3 tools/oversight.py)"))
        return 1 if bad else 0
    OUT_JSON.write_text(js, encoding="utf-8")
    OUT_MD.write_text(md, encoding="utf-8")
    p = d["pooled"]
    print(f"{OUT_MD.relative_to(ROOT)}: {d['count']['tests']} tests on {d['engine']}; alert minutes {p['native']:.1f} → {p['omni']:.1f} "
          f"({p['change'] * 100:+.1f}%); at the 7% example the bill moves {d['example']['bill_change'] * 100:+.2f}%")
    return 0


if __name__ == "__main__":
    sys.exit(main())
