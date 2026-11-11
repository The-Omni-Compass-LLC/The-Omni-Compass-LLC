#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Questions a buyer asks, answered from the record: what Omni-Compass is, what it shows today, where it does more work for the
bill, what it does to the pages a person answers, where it has read LOSS, what a person still does, what is not claimed, and how
to try it. Every number is read from its record when this page is written (the Omni index, the work for the bill, the oversight
line, the LOSS ledger, the engine that stands); nothing is typed in, so the page is written again whenever the records move.

    python3 tools/faq.py          writes docs/FAQ.md
    python3 tools/faq.py --check  fails when docs/FAQ.md differs from the records
"""
import argparse
import json
import pathlib
import re
import sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "FAQ.md"
sys.path.insert(0, str(ROOT / "tools"))
from legal import stamp  # noqa: E402

OWN_RUNS = "Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results."


def _j(rel):
    p = ROOT / rel
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def facts() -> dict:
    idx = _j("results/OMNI_INDEX.json")
    eng = Counter(m.group(1) for t in idx.get("tests", []) if (m := re.search(r"V(\d+)_", t.get("source", ""))))
    vs = [int(m.group(1)) for f in ROOT.glob("OMNI_V*.json") if (m := re.fullmatch(r"OMNI_V(\d+)", f.stem))]   # the newest declared engine
    standing = f"omni-v{max(vs)}" if vs else None
    wpb = _j("results/WORK_PER_BILL.json").get("places", {})
    ov = _j("results/OVERSIGHT.json")
    led = (ROOT / "docs" / "LOSS_LEDGER.md").read_text(encoding="utf-8") if (ROOT / "docs" / "LOSS_LEDGER.md").exists() else ""
    m = re.search(r"Rows that read LOSS across their three runs: \*\*(\d+)\*\*\. Against my own native[^*]*\*\*(\d+)\*\*", led)
    return {"index": idx.get("headline_pct"), "service": idx.get("service_headline_pct"), "index_tests": len(idx.get("tests", [])),
            "index_engines": ", ".join(f"omni-v{k}" for k in sorted(eng, key=int)), "standing": standing or "the engine that stands",
            "chip": wpb.get("bare_metal") or {}, "cloud": wpb.get("cloud") or {}, "ov": ov,
            "loss_all": int(m.group(1)) if m else None, "loss_own": int(m.group(2)) if m else None}


def _pc(x):
    return f"{abs(x) * 100:.1f}%"


def _word(pct):
    """The one key's word for an index in percent (tools/readings.py: under the 0.5% floor STEADY)."""
    return "GAIN" if pct >= 0.5 else "LOSS" if pct <= -0.5 else "STEADY"


def markdown(f: dict) -> str:
    chip, cloud, ov = f["chip"], f["cloud"], f["ov"]
    p = (ov.get("pooled") or {})
    L = ["# Questions a Buyer Asks, Answered from the Record", "",
         "Every number on this page is read from its record when the page is written (`python3 tools/faq.py`); each answer names the "
         "page that holds the whole story. Our own models (class S) are never offered as proof; live software is class L and a "
         "physical meter class P.", "",
         "**What is Omni-Compass, in one sentence?** A supervisory governor: one brain that sits on top of the controllers a stack "
         "already runs (the Kubernetes autoscaler, a card's power firmware, a database's pools) and turns their settings toward the "
         "founder's aim, more work, faster, on fewer machines, never past any part's own limit; it never replaces them and is never "
         "in the data path (`DISCLOSURES.md`). The aim is not yet the result: the record reads the work and the speed, and the "
         "whole organism's composition reads the machines more, not fewer, power given (`results/WHOLE_SYSTEM.md`).", "",
         f"**What does it show today, in one number?** The Omni index, every real test weighed together: **{_word(f['index'])} "
         f"{abs(f['index']):.1f}%** (work, speed and machines; its second reading, work and speed alone, {_word(f['service'])} "
         f"{abs(f['service']):.1f}%), over {f['index_tests']} real "
         f"tests on GitHub's own machines, on the tables of {f['index_engines']} (`results/OMNI_INDEX.md`). The engine that stands is "
         f"{f['standing']}; every benchmark runs again on it, and the index is written again as its tables land.", "",
         "**Does it do more work for the bill?** The one equation is G = (1 + ΔW) / (1 + ΔB) − 1, the work for each dollar against "
         "native (`docs/WORK_PER_BILL.md`). "
         + (f"On the chip (one A10 card on Lambda, {chip.get('engine', '').split(' (')[0]}) its three runs read G "
            f"{', '.join(('up ' if r['G'] >= 0 else 'down ') + _pc(r['G']) for r in chip.get('runs', []))}: {chip.get('reading')}. " if chip.get("runs") else "")
         + (f"Through the cloud (Azure, {cloud.get('engine')}) the set read the bill but not the work, so G is not read there yet; "
            "the sets with the work meter are queued." if cloud else ""), "",
         (f"**Does it take pages away from the people on call?** Over {ov['count']['tests']} real Kubernetes tests on {ov['engine']}, "
          f"{p.get('reading', 'by the mean')} pooled: the minutes an on-call page would be open {'down' if p.get('change', 0) < 0 else 'up'} "
          f"{_pc(p.get('change', 0))}, from {p.get('native', 0):.1f} to {p.get('omni', 0):.1f} a repetition (fewer minutes, fewer pages); "
          f"test by test fewer in {ov['count']['fewer']} (to none in {ov['count']['to_zero']}), the same in {ov['count'].get('same', 0)}, "
          f"more in {ov['count'].get('more', 0)}; Omni-Compass wrote its own settings with no person touching either arm. What that is worth is "
          "the owner's people share times that fall (`results/OVERSIGHT.md`)." if ov.get("count") else ""), "",
         (f"**Has it ever done harm?** Every LOSS row is kept and listed: {f['loss_all']} rows read LOSS across their three runs in "
          f"the newest tables, {f['loss_own']} of them Omni-Compass on top of its own native, each with its cause where one is written "
          "and the version that fixed it where one did (`docs/LOSS_LEDGER.md`). A LOSS at the factory tune is a fault to fix, never a "
          "number to accept; the open ones are on the next version's list (`docs/CHANGE_CONTROL.md`)." if f["loss_all"] is not None else ""), "",
         "**What does a person still do?** Hold the kill switch (one hand, instant, security only), set each service's response line "
         "and choose the profile. Everything else Omni-Compass does on its own: reads every gauge, writes only through the two-way "
         "plug, reads each write back, records its reason, and hands every setting back to native at the reset, after a crash "
         "gradually (the lease).", "",
         "**Where does it run, and where does the benefit live?** At the software end, wired in at any of three places: on site, "
         "through a cloud, or at the chip. The benefit is made and measured at the software end; at the chip and in the cloud's bill "
         "the record is read for whether it holds (a place holds when its runs read no LOSS) and for what the work per joule or per dollar does (`docs/HOW_TO_READ_THE_RESULTS.md`). "
         "GitHub's runners are never called bare metal.", "",
         "**What is not claimed?** No outside party has reviewed or approved these results; no model result is offered as proof; no "
         "figure without a record (a \"20% drain\", a 2.9% \"stack tax\", a projected percentage) is written anywhere "
         "(`docs/WEBSITE_CLAIMS.md`); turning any knob off the factory tune can change every metric, in any direction.", "",
         "**How do I see it work?** Open the live engine page (`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`) and press **Guided tour** "
         "on the right edge: a recorded voice walks every section, and every stop can be paused, replayed and read along. To put it on "
         "a system, the Operator's Manual starts it in watch mode first: it reads every gauge for days and writes nothing "
         "(`docs/OMNI_COMPASS_MANUAL.md`, chapter 6).", "",
         "**What comes next?** Every benchmark's three runs on the engine that stands, the cloud sets that count the work, Google's "
         "and Amazon's sets on the founder's word, and the next version's list (`docs/CHANGE_CONTROL.md`).", "", OWN_RUNS]
    return "\n".join(stamp([x for x in L])) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    md = markdown(facts())
    if a.check:
        ok = OUT.exists() and OUT.read_text(encoding="utf-8") == md
        print("the buyer's questions: " + ("in line with the records" if ok else "docs/FAQ.md differs (python3 tools/faq.py)"))
        return 0 if ok else 1
    OUT.write_text(md, encoding="utf-8")
    print(f"{OUT.relative_to(ROOT)} written from the records")
    return 0


if __name__ == "__main__":
    sys.exit(main())
