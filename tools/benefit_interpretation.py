# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Turn a paired native/Omni metric into an objective-specific, plain-language reading.

This helper reports measured/modelled values supplied by the caller; it does not infer missing evidence. For a resource
cut at equal work, it also calculates the *conditional* work capacity at the same resource budget. That derived number is
an arithmetic scenario, not observed extra work. Example: python3 tools/benefit_interpretation.py resource 100 95
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.legal import PLAIN  # noqa: E402


def interpret_pair(objective: str, native: float, omni: float) -> dict:
    """Return raw change, objective classification, and a carefully bounded interpretation.

    Objectives are declared per gauge before interpreting the result: work (higher), latency (lower), resource (lower;
    an increase is power given), or safety (lower; a rise is LOSS). Values must share units and workload.
    """
    if objective not in {"work", "latency", "resource", "safety"}:
        raise ValueError("objective must be work, latency, resource, or safety")
    if native < 0 or omni < 0:
        raise ValueError("paired values must be non-negative")
    if native == 0:
        raise ValueError("native must be greater than zero to compute a percentage")
    change_pct = (omni / native - 1.0) * 100.0
    if abs(change_pct) < 1e-12:
        classification = "STEADY"
    elif objective == "work":
        classification = "GAIN" if change_pct > 0 else "LOSS"
    elif objective == "resource":
        classification = "GAIN" if change_pct < 0 else "POWER GIVEN"
    else:
        classification = "GAIN" if change_pct < 0 else "LOSS"

    result = {"objective": objective, "native": native, "omni": omni,
              "change_pct": change_pct, "classification": classification}
    if objective == "resource" and omni < native:
        result["resource_saved_pct"] = (native - omni) / native * 100.0
        if omni > 0:
            result["conditional_work_capacity_pct"] = (native / omni - 1.0) * 100.0
            estimate = (f" If the saved resource is redeployed and the system scales linearly, the same native resource "
                        f"budget could support up to {result['conditional_work_capacity_pct']:.2f}% more work; this is "
                        "conditional, not work observed in this paired run.")
        else:
            result["conditional_work_capacity_pct"] = None
            estimate = " A percentage capacity estimate is undefined because Omni resource use is zero."
        result["interpretation"] = f"Resource use fell {result['resource_saved_pct']:.2f}% for the compared work (GAIN)." + estimate
    elif objective == "resource" and omni > native:
        result["interpretation"] = f"Resource use rose {change_pct:.2f}% (POWER GIVEN); report what service gain it bought."
    elif objective == "work":
        result["interpretation"] = f"Work changed {change_pct:+.2f}% under the compared workload."
    else:
        result["interpretation"] = f"{objective.capitalize()} changed {change_pct:+.2f}% under the compared workload."
    return result


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("objective", choices=("work", "latency", "resource", "safety"))
    ap.add_argument("native", type=float)
    ap.add_argument("omni", type=float)
    ap.add_argument("--unit", default="units", help="shared unit for the paired values")
    ap.add_argument("--evidence", choices=("P", "L", "S"), default="S",
                    help="P physical meter, L live software, S model/simulation")
    a = ap.parse_args(argv)
    r = interpret_pair(a.objective, a.native, a.omni)
    delta = r["omni"] - r["native"]
    print(PLAIN)
    print(f"Evidence class {a.evidence}; objective {a.objective}; units {a.unit}.")
    print(f"Native {a.native:g}; Omni {a.omni:g}; change {delta:+g} {a.unit} ({r['change_pct']:+.2f}%); {r['classification']}.")
    print(r["interpretation"])
    print(PLAIN)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
