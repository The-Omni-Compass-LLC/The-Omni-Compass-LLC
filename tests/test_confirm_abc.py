# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The A/B/C three-run table rule (tools/confirm_abc.py, docs/OMNI_V1.md): GAIN or LOSS in all three of our runs only when all
three runs move the same way with every 95% interval clear of zero, the word given by what the gauge is for (a response time
that fell is GAIN; a resource spent that fell is a cut, a GAIN, and one that rose is power given); a change of 0.5% or more,
the runs' mean, reads by its aim by the mean of the three runs with the count of runs beyond the noise (the founder's order of
24 October 2026); STEADY only under 0.5%; runs that moved 0.5% or more in opposite directions read as a disagreement; a rounding-level change reads STEADY, the same; unjudged rows stay unjudged."""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import confirm_abc as C

P95 = "response time (ms), 95th percentile"


def r(native, diff, lo, hi):
    return {"native": native, "omni": native + diff, "diff": diff, "ci95": [lo, hi], "significant": lo > 0 or hi < 0}


def main():
    fell = r(300, -150, -200, -100)
    assert C.verdict(P95, [fell] * 3) == "**GAIN in all three of our runs**", "a response time cut in all three is a GAIN (a minus that reads GAIN)"
    assert C.verdict(P95, [r(300, 30, 10, 50)] * 3) == "**LOSS in all three of our runs**", "a slower response in all three is a LOSS"
    # the founder's order of 24 October 2026: a change of 0.5% or more (the runs' mean) is a change; STEADY only under 0.5%
    assert C.verdict(P95, [fell, fell, r(300, -20, -60, 5)]) == "**GAIN by the mean of our three runs, beyond the noise in 2 of 3**", "one interval crosses zero: the mean still moved"
    assert C.verdict(P95, [r(300, -5, -40, 30), r(300, 8, -20, 36), r(300, -2, -30, 26)]) == "**the runs disagree**", "runs moved 0.5% or more both ways"
    assert C.verdict(P95, [r(300, -1, -40, 30), r(300, 0.5, -20, 36), r(300, -0.4, -30, 26)]) == "STEADY, under the floor (the three runs' mean 0.10%)"
    assert C.verdict(P95, [fell, fell, r(300, 40, 10, 70)]) == "**the runs disagree**", "one run flips the sign, clear of the noise"
    assert C.verdict(P95, [fell, r(300, -20, -60, 5), r(300, 40, 10, 70)]) == "**the runs disagree**", "a disagreement outranks a noisy run"
    assert C.verdict(P95, [fell, fell, r(300, 20, -5, 45)]) == "**the runs disagree**", "a run that moved 0.5% or more the other way disagrees, inside the noise or not"
    assert C.verdict(P95, [fell, fell, r(300, 1, -5, 7)]) == "**GAIN by the mean of our three runs, beyond the noise in 2 of 3**", "a run the other way under the floor does not disagree"
    assert C.verdict(P95, [r(300, 1e-7, 5e-8, 2e-7)] * 3) == "STEADY, the same", "a change under one part in a million"
    assert C.verdict("CPU used (cores), mean", [r(2.0, -0.5, -0.7, -0.3)] * 3) == "shown, not judged"
    # one pair a run (the 24-hour robustness run on rented machines): no interval, read by sign alone, never a confirmation
    nan = float("nan")
    single = {"native": 300.0, "omni": 150.0, "diff": -150.0, "ci95": [nan, nan], "significant": False}
    assert C.verdict(P95, [single] * 3) == "three single pairs agree: GAIN (one pair a run, no interval, so the noise cannot be judged)"
    assert C.verdict(P95, [single, single, dict(single, diff=20.0, omni=320.0)]) == "single pairs point different ways (one pair a run, no interval)"
    assert C.verdict(C.CAPACITY, [single] * 3).startswith("three single pairs agree: LOSS"), "less work inside the line from three single pairs reads LOSS, and still not a reading of all three of our runs"
    # the size beside a word carries no sign (tools/readings.py by_word, 25 October); with no word, its own direction
    # every cell: native → Omni-Compass, the raw change with its true sign and its interval as it lies, then the word apart
    # (the referee's work order of 25 October: a raw change is never turned to wear the verdict's sign)
    assert C.cell(fell) == "300 → 150; raw −50.0% (95%: −66.7% to −33.3%)", C.cell(fell)
    assert C.cell(fell, "GAIN") == "300 → 150; raw −50.0% (95%: −66.7% to −33.3%); GAIN", C.cell(fell, "GAIN")
    assert C.cell(fell, "LOSS") == "300 → 150; raw −50.0% (95%: −66.7% to −33.3%); LOSS", C.cell(fell, "LOSS")
    assert C.cell(r(300, -5, -40, 30), "STEADY, no difference beyond the noise") == "300 → 295; raw −1.7% (95%: −13.3% to +10.0%); STEADY, no difference beyond the noise", "STEADY: the raw change as it lies"
    with tempfile.TemporaryDirectory() as t:
        d = Path(t) / "run-123" / "live-reps"; d.mkdir(parents=True)
        (d / "LIVE_REPS.json").write_text(json.dumps({"repetitions": {"native": ["1", "2", "3"], "compass": ["1", "2"]},
                                                       "means": {}, "paired": {"compass": {P95: fell}}}))
        run, paired, n, _ = C.load(d.parent)
        assert (run, n, paired[P95]["diff"]) == ("123", 2, -150), (run, n)
    assert C.engine("1")[1] == "unknown", "a run whose commit cannot be read is never called v1 (GitHub's gh prints nothing for it)"
    assert C.verdict(C.CAPACITY, [r(18.6, 9.0, 6.0, 12.0)] * 3) == "**GAIN in all three of our runs**", "more work inside the line is a GAIN"
    assert C.verdict(C.CAPACITY, [r(18.6, -3.0, -5.0, -1.0)] * 3) == "**LOSS in all three of our runs**", "less work is a LOSS"
    assert C.verdict("batch: worker machines in service after the queue finished, mean", [r(6.0, -2.0, -2.5, -1.5)] * 3) == "**GAIN in all three of our runs**", "machines cut"
    assert C.verdict("batch: worker machines in service after the queue finished, mean", [r(6.0, 2.0, 1.5, 2.5)] * 3) == "**power given in all three of our runs**", "machines up: power given, never a LOSS"
    assert C.verdict("batch: queue finished (s)", [r(575.0, 5.0, 2.0, 8.0)] * 3) == "**LOSS in all three of our runs**", "a later finish is a LOSS"
    assert C.verdict("compute bill at list price ($)", [r(1.0, -0.1, -0.15, -0.05)] * 3) == "**GAIN in all three of our runs**", "a bill cut is a GAIN"
    assert C.verdict("energy (Wh)", [r(10.0, 1.0, 0.5, 1.5)] * 3) == "**power given in all three of our runs**", "energy up is power given"
    assert C.verdict("failed requests (%)", [r(1.0, 0.5, 0.2, 0.8)] * 3) == "**LOSS in all three of our runs**", "more failed requests is a LOSS"
    with tempfile.TemporaryDirectory() as t:
        d = Path(t) / "run-124" / "live-reps"; d.mkdir(parents=True)
        (d / "LIVE_REPS.json").write_text(json.dumps({"repetitions": {"native": ["1"], "compass": ["1"]}, "means": {}, "paired": {"compass": {}},
                                                       "capacity": {"native": {"capacity_rps": 18.6}, "compass": {"capacity_rps": 27.6, "change_pct": 48.4, "ci95": [6.0, 12.0]}}}))
        _, paired, _, _ = C.load(d.parent)
        assert paired[C.CAPACITY]["diff"] == 9.0 and paired[C.CAPACITY]["significant"], "the capacity block becomes a judged row"
    with tempfile.TemporaryDirectory() as t:                # the rig each run ran on (amendment of 18 October): never two in one table
        old, new = Path(t) / "run-1", Path(t) / "run-2"
        for d, line in ((old, ""), (new, "images=pre-pulled on every worker before the arm (deploy/kind/prepull.yaml)\n")):
            for arm in ("native", "compass"):
                (d / f"bench-{arm}-1").mkdir(parents=True)
                (d / f"bench-{arm}-1" / "preflight.txt").write_text("arm=" + arm + "\n" + line)
        assert C.rig(old) == "pulled by each node at each start", C.rig(old)
        assert C.rig(new) == "pre-pulled on every worker before the arm (deploy/kind/prepull.yaml)", C.rig(new)
        assert C.rig(Path(t) / "none") == "not recorded"
    print("PASS  A/B/C three-run table rule: GAIN or LOSS in all three of our runs only with the same sign and every interval clear of zero in all three, "
          "the word by what the gauge is for (a resource spent that rose: power given); a change of 0.5% or more reads by its aim, in all three runs or by their mean; STEADY only under 0.5%; clear runs pointing different ways read as a disagreement")


if __name__ == "__main__":
    main()
