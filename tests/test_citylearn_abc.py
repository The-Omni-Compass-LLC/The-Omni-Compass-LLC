# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The CityLearn A/B/C rule (tools/citylearn_abc.py, docs/OMNI_V1.md): a deterministic simulator, so the three runs must
reproduce each other; a score reads GAIN or LOSS in all three of our runs by what it is for when they do (the bill, the electricity
bought, the carbon, the peaks, the swings and the unevenness are power spent or held: a fall is a cut, a GAIN, a rise is power given; the
energy not served and the time uncomfortable are misses, and a rise is a LOSS), STEADY under one
part in a million, and "the runs differ" when they do not; a district with no electric battery is listed as nothing for Omni to move, and a
district CityLearn cannot run is listed with its error, never dropped."""
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import citylearn_abc as C
from tools.run_citylearn import KPIS

COST, PEAK, MISS = "cost_total", "daily_peak_average", "annual_normalized_unserved_energy_total"


def arm(name, batteries, **kpis):
    base = {k: 1.0 for k in KPIS}; base.update(kpis)
    return {"arm": name, "buildings": 3, "steps": 720, "batteries": batteries, "thermal_stores_left_native": 1,
            "seconds": 1.0, "moved_hours": 100, "handed_back": True, "kpis": base}


def rec(batteries, omni_cost, omni_peak, omni_miss=1.0):
    return {"native": arm("native", batteries), "omni": arm("omni", batteries, **{COST: omni_cost, PEAK: omni_peak, MISS: omni_miss}),
            "citylearn_version": "3.0.2", "settings": {}}


def write(root, run, districts):
    d = Path(root) / f"run-{run}"
    for name, r in districts.items():
        (d / f"citylearn-{name}").mkdir(parents=True)
        (d / f"citylearn-{name}" / f"{name}.json").write_text(json.dumps(r))
    return d


def main():
    same = rec(3, 0.98, 1.03, 1.05)                         # cost 2% lower, daily peak 3% higher, energy not served 5% higher, every run alike
    assert C.verdict([same] * 3, COST) == "**GAIN in all three of our runs**", "a bill cut is a GAIN"
    assert C.verdict([same] * 3, PEAK) == "**power given in all three of our runs**", "a higher peak is power held: power given, never a LOSS"
    assert C.verdict([same] * 3, MISS) == "**LOSS in all three of our runs**", "more energy not served in all three is a LOSS"
    assert C.verdict([same] * 3, "carbon_emissions_total") == "STEADY, the same"
    other = rec(3, 0.98, 1.03, 1.05); other["omni"]["kpis"][COST] = 0.97
    assert C.verdict([same, same, other], COST) == "**the runs differ**", "a run that does not reproduce is a finding"
    tiny = rec(3, 1.0 + 1e-7, 1.0)                                       # measured past the ninth decimal: never "the same"
    assert C.verdict([tiny] * 3, COST) == "STEADY, under the floor (the three runs' mean 0.00%)", "a change under the floor, measured"
    same9 = rec(3, 1.0 + 1e-10, 1.0)                                     # equal to nine decimal places (the referee's work order of 25 October)
    assert C.verdict([same9] * 3, COST) == "STEADY, the same", "equal to nine decimal places"
    with tempfile.TemporaryDirectory() as t:
        broken = {"native": {"error": "ValueError: needs interface='entity'"}, "omni": {"error": "ValueError: needs interface='entity'"}}
        dirs = [write(t, i, {"d_bat": same, "d_nobat": rec(0, 1.0, 1.0), "d_broken": broken}) for i in (1, 2, 3)]
        out = Path(t) / "V1.md"
        assert C.main([str(d) for d in dirs] + ["--out", str(out)]) == 0
        txt = out.read_text()
        assert "| d_nobat | 3 | 1 | none | yes |" in txt, "no battery: nothing for Omni to move"
        assert "| d_broken | `ValueError: needs interface='entity'` |" in txt, "a district CityLearn cannot run is listed"
        assert "LOSS in all three of our runs" in txt and "GAIN in all three of our runs" in txt and "Not one engine's three runs" in txt
    print("PASS  CityLearn A/B/C rule: reproduced runs read GAIN, STEADY or LOSS by what each score is for, a run that differs is a finding, no battery means nothing to move, "
          "a district CityLearn cannot run is listed")


if __name__ == "__main__":
    main()
