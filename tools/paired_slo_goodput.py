# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""SLO-constrained paired goodput and cost comparison; standard library only.

No simulated values are treated as hardware evidence. Never infer a benefit
from a resource cut if the declared service constraints were violated.
Input JSON: {"native":[{...},...],"omni":[{...},...],"limits":{...}}.
Each paired record has identical workload_id, hardware_id, and offered_requests.
Required numeric fields: completed, failed, p95_ms, energy_j, cost_usd.
Optional limits: max_p95_ratio, min_completed_ratio, max_failed_delta.
"""
import argparse
import json
import math
from pathlib import Path

FIELDS = ("completed", "failed", "p95_ms", "energy_j", "cost_usd")

def evaluate(data):
    native, omni = data["native"], data["omni"]
    if not native or len(native) != len(omni):
        raise ValueError("native and omni require equal nonzero paired repetitions")
    limits = data.get("limits", {})
    lp = float(limits.get("max_p95_ratio", 1.0))
    lc = float(limits.get("min_completed_ratio", 1.0))
    lf = float(limits.get("max_failed_delta", 0.0))
    if not all(math.isfinite(x) for x in (lp, lc, lf)) or min(lp, lc, lf) < 0:
        raise ValueError("invalid guardrails")
    pairs = []
    for index, (n, o) in enumerate(zip(native, omni)):
        for label, record in (("native", n), ("omni", o)):
            for field in FIELDS:
                value = record[field]
                if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
                    raise ValueError(f"pair {index} {label}.{field}: invalid measurement")
            if record["completed"] + record["failed"] > record["offered_requests"]:
                raise ValueError(f"pair {index}: impossible request accounting")
        for label, record in (("native", n), ("omni", o)):
            offered = record["offered_requests"]
            if isinstance(offered, bool) or not isinstance(offered, int) or offered < 0:
                raise ValueError(f"pair {index} {label}.offered_requests: invalid count")
        for identity in ("workload_id", "hardware_id", "offered_requests"):
            if n[identity] != o[identity]:
                raise ValueError(f"pair {index}: unmatched {identity}")
        if n["completed"] <= 0 or n["p95_ms"] <= 0 or n["energy_j"] <= 0 or n["cost_usd"] <= 0:
            raise ValueError(f"pair {index}: native denominator unavailable")
        guard = (o["p95_ms"] <= lp * n["p95_ms"]
                 and o["completed"] >= lc * n["completed"]
                 and o["failed"] - n["failed"] <= lf)
        pairs.append({
            "pair": index, "admissible": guard,
            "completed_delta_pct": 100 * (o["completed"] / n["completed"] - 1),
            "p95_delta_pct": 100 * (o["p95_ms"] / n["p95_ms"] - 1),
            "energy_delta_pct": 100 * (o["energy_j"] / n["energy_j"] - 1),
            "cost_delta_pct": 100 * (o["cost_usd"] / n["cost_usd"] - 1),
            "goodput_per_joule_delta_pct": 100 * ((o["completed"] / o["energy_j"]) / (n["completed"] / n["energy_j"]) - 1) if o["energy_j"] > 0 else None,
            "goodput_per_dollar_delta_pct": 100 * ((o["completed"] / o["cost_usd"]) / (n["completed"] / n["cost_usd"]) - 1) if o["cost_usd"] > 0 else None,
        })
    return {"status": "ADMISSIBLE" if all(p["admissible"] for p in pairs) else "GUARDRAIL_VIOLATION",
            "n_pairs": len(pairs), "pairs": pairs,
            "evidence": "paired measurements supplied by caller; provenance not independently verified",
            "note": "Descriptive ratios, not confidence intervals, causal proof, or production certification"}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = evaluate(json.loads(args.input.read_text()))
    serialized = json.dumps(result, indent=2, allow_nan=False) + "\n"
    if args.output:
        args.output.write_text(serialized)
    else:
        print(serialized, end="")

if __name__ == "__main__":
    main()
