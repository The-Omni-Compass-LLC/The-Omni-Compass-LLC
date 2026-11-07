#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""More work at the end of the day: every test's work, native against Omni-Compass on native, from the records alone.

The founder's words of 2 November: "we need to see if we're doing more work at the end of the day. That's all that matters
when we're governing." This page reads the work row of every test the repository holds (results/OMNI_INDEX.json, the
orchestrator showing's three runs, the chip's receipt, the cloud's) and sorts them three ways: the work was counted and grew,
the work was counted and held, or the test sent a fixed load or did not count its work, so it could not show more work
whatever the governor did. Nothing here is a new measurement.

    python3 tools/work_today.py          writes results/WORK_TODAY.md and results/WORK_TODAY.json
    python3 tools/work_today.py --check  fails when either differs from the records
"""
import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT_MD, OUT_JSON = ROOT / "results" / "WORK_TODAY.md", ROOT / "results" / "WORK_TODAY.json"
sys.path.insert(0, str(ROOT / "tools"))
from legal import stamp  # noqa: E402

OWN_RUNS = "Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results."


def _pct(x: float) -> str:
    return f"{abs(x) * 100:.1f}%"


def _word(reading: str) -> str:
    for w in ("GAIN", "LOSS", "the runs disagree", "STEADY"):
        if reading.startswith(w) or w in reading.split(",")[0]:
            return w
    return reading


def build() -> dict:
    idx = json.loads((ROOT / "results" / "OMNI_INDEX.json").read_text(encoding="utf-8"))
    counted, blind, taken_out = [], [], []
    for t in idx["tests"]:
        w = t["measures"].get("work")
        row = {"place": "the software end (GitHub's machines, class L)", "category": t["category"], "test": t["test"], "source": t["source"]}
        if not w or w.get("ratio") is None:
            blind.append({**row, "why": "the test does not count its work (it reads time, misses and machines)"})
        elif "fixed-rate work" in (w.get("reading") or ""):
            blind.append({**row, "why": "the same fixed-rate work sent to both arms, equal by design"})
        else:
            what = ("the requests answered inside the response line, the load stepping up and down (the work meter)" if t["category"].startswith("Real Kubernetes")
                    else "the work answered inside the response line, at a load offered at a fixed rate, the same in both arms")
            counted.append({**row, "what": what, "ratio": w["ratio"], "change": w["ratio"] - 1, "reading": w["reading"], "word": _word(w["reading"])})
    orch_f = ROOT / "results" / "orchestrator" / "V21_THREE_ARMS_ABC.json"
    if orch_f.exists():
        o = json.loads(orch_f.read_text(encoding="utf-8"))
        r = next((x for x in o["rows"] if x["pair"] == "Omni on native against native" and x["gauge"] == "requests"), None)
        if r:
            rel = [r["runs"][k]["rel"] for k in ("A", "B", "C")]
            taken_out.append({"why": "the verdict audit took its table out of the count (results/verdict_audit/VERDICT_AUDIT.json, status taken out): shown, never counted",
                            "place": "the software end (GitHub's machines, class L)", "category": "Omni-Compass's own orchestrator showing",
                            "test": "18 steps of 25 s, clients stepping 1 2 3 2 3 4 …", "what": "the requests served a step by clients that send again as soon as they are answered", "source": "results/orchestrator/V21_THREE_ARMS_ABC.json",
                            "ratio": 1 + sum(rel) / 3, "change": sum(rel) / 3, "runs": rel, "reading": r["reading"], "word": _word(r["reading"])})
    wpb = json.loads((ROOT / "results" / "WORK_PER_BILL.json").read_text(encoding="utf-8"))
    bm, cl = wpb["places"].get("bare_metal"), wpb["places"].get("cloud")
    if bm:
        rel = [x["w"] for x in bm["runs"]]
        counted.append({"place": "bare metal (one A10 card on Lambda, class L)", "category": "the chip", "test": bm["title"], "what": "the requests the card served in the same metered window", "source": bm["source"],
                        "ratio": 1 + sum(rel) / 3, "change": sum(rel) / 3, "runs": rel, "reading": bm["reading"], "word": _word(bm["reading"])})
    if cl:
        blind.append({"place": "through the cloud (Azure, billed)", "category": "the cloud", "test": f"{cl['engine']}, {cl['repetitions']} paired repetitions",
                      "source": cl["source"], "why": "the work was not counted (a fixed rate of requests); the work meter runs in every cloud set from 31 October"})
    counted.sort(key=lambda r: -r["change"])
    tally = {}
    for r in counted:
        tally[r["word"]] = tally.get(r["word"], 0) + 1
    return {"question": "we need to see if we're doing more work at the end of the day. That's all that matters when we're governing.",
            "said": "the founder, 2 November 2026", "counted": counted, "blind": blind, "taken_out": taken_out, "tally": tally,
            "sources": ["results/OMNI_INDEX.json", "results/orchestrator/V21_THREE_ARMS_ABC.json", "results/WORK_PER_BILL.json"]}


def markdown(d: dict) -> str:
    c, b, t = d["counted"], d["blind"], d["tally"]
    grew = [r for r in c if r["word"] == "GAIN"]
    L = ["# More Work at the End of the Day: Every Test, Native Against Omni-Compass on Native", "",
         f"> \"{d['question'][0].upper() + d['question'][1:]}\" ({d['said']})", "",
         "Every test the repository holds, read by its work row alone: the work done with Omni-Compass on top of native against "
         "native on the same machines, by the one key (a change of 0.5% or more is a change). Nothing here is a new measurement; "
         "each row names its record.", "",
         f"**The answer today: more work in {len(grew)} of the {len(c)} tests that counted their work, less work in "
         f"{t.get('LOSS', 0) or 'none'}.** The work held in {t.get('STEADY', 0)}: each of those offers its load at a fixed rate, the same "
         f"in both arms, so the most either arm can do is answer all of it inside the line. In {t.get('the runs disagree', 0)} the runs "
         f"disagree. {len(b)} more tests could not show more work whatever Omni-Compass did: they sent a fixed load or did not count "
         "the work." + (f" {len(d.get('taken_out') or [])} more, taken out of the count by the verdict audit, is shown at the end and never counted." if d.get("taken_out") else ""), "",
         "## The tests that counted their work", "",
         "| Where | Test | What the work is | Work, Omni-Compass on native against native | Reading (the one key) | Record |", "|---|---|---|---|---|---|"]
    for r in c:
        size = ("held" if r["word"] == "STEADY" else "the runs disagree" if r["change"] == 0 else
                ("up " if r["change"] > 0 else "down ") + _pct(r["change"]) + (", by the mean" if r["word"] == "the runs disagree" else ""))
        runs = (" (runs: " + ", ".join(("up " if x > 0 else "down ") + _pct(x) for x in r["runs"]) + ")") if r.get("runs") else ""
        L.append(f"| {r['place']}, {r['category']} | {r['test']} | {r['what']} | {size}{runs} | {r['reading']} | `{r['source']}` |")
    L += ["", "## The tests that could not show more work", "",
          "A test that sends the same fixed load to both arms, or reads only time, misses and machines, cannot show more work, however "
          "well the system is supervised: it can show only the same work done faster, with fewer alert minutes or with fewer machines in "
          "service. To answer "
          "the question in these tests too, each needs a load whose work grows when the system serves faster (the work meter, "
          "`LOADGEN=meter` in `scripts/kind_bench.sh`, as every cloud set carries from 31 October).", "",
          "| Where | Test | Why it could not show more work | Record |", "|---|---|---|---|"]
    for r in b:
        L.append(f"| {r['place']}, {r['category']} | {r['test']} | {r['why']} | `{r['source']}` |")
    if d.get("taken_out"):
        L += ["", "## The test taken out of the count", "",
              "| Where | Test | Work, Omni-Compass on native against native | Reading (the one key) | Why it is not counted | Record |", "|---|---|---|---|---|---|"]
        for r in d["taken_out"]:
            runs = (" (runs: " + ", ".join(("up " if x > 0 else "down ") + _pct(x) for x in r["runs"]) + ")") if r.get("runs") else ""
            L.append(f"| {r['place']}, {r['category']} | {r['test']} | {('up ' if r['change'] > 0 else 'down ') + _pct(r['change'])}{runs} | {r['reading']} | {r['why']} | `{r['source']}` |")
    soft = sorted({int(x) for x in re.findall(r"/V(\d+)_", " ".join(r["source"] for r in c + b if r["place"].startswith("the software end")))})
    L += ["", "Engines: each record names the engine it ran on (the software end's tables on "
          + (", ".join(f"omni-v{v}" for v in soft) or "the engines their files name") + ", the chip and the cloud on the engines their "
          "rows name above); every benchmark runs again on the engine that stands, and this page is written again from the records when "
          "they land (`python3 tools/work_today.py`).", "", OWN_RUNS]
    return "\n".join(stamp(L)) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    d = build()
    js, md = json.dumps(d, indent=1, ensure_ascii=False) + "\n", markdown(d)
    if a.check:
        bad = [p.relative_to(ROOT).as_posix() for p, s in ((OUT_JSON, js), (OUT_MD, md)) if not p.exists() or p.read_text(encoding="utf-8") != s]
        print("work at the end of the day: " + ("in line with the records" if not bad else ", ".join(bad) + " differ (python3 tools/work_today.py)"))
        return 1 if bad else 0
    OUT_JSON.write_text(js, encoding="utf-8")
    OUT_MD.write_text(md, encoding="utf-8")
    print(f"{OUT_MD.relative_to(ROOT)}: {len(d['counted'])} tests counted their work ({d['tally']}); {len(d['blind'])} could not show it")
    return 0


if __name__ == "__main__":
    sys.exit(main())
