#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The operator's rule of the Goldilocks test (docs/GOLDILOCKS_PREREGISTRATION.md): Goldilocks's recommendation for the
service's container applied as the Vertical Pod Autoscaler itself applies one (its default, RequestsAndLimits): each
request at the target, each limit kept in its proportion to its request. The operator's settings before are those of
deploy/kind/demo.yaml (CPU request 200m, limit 500m; no memory request or limit), so the CPU limit becomes the target x
500/200 and the memory request the target (there is no memory limit to keep).

    python3 tools/goldilocks_apply.py goldilocks_recommendation.json goldilocks_apply.json
"""
import json
import re
import sys

REQUEST_M, LIMIT_M = 200, 500            # deploy/kind/demo.yaml, the operator's settings before the recommendation
UNITS = {"": 1, "k": 10 ** 3, "M": 10 ** 6, "G": 10 ** 9, "Ki": 2 ** 10, "Mi": 2 ** 20, "Gi": 2 ** 30}


def milli(q) -> int:
    """A CPU quantity ("163m", "1", "0.5") in millicores."""
    q = str(q).strip()
    return int(round(float(q[:-1]))) if q.endswith("m") else int(round(float(q) * 1000))


def octets(q) -> int:
    """A memory quantity ("262144k", "64Mi", "104857600") in bytes."""
    m = re.fullmatch(r"([0-9.]+)([A-Za-z]*)", str(q).strip())
    if not m or m.group(2) not in UNITS:
        raise ValueError(f"not a memory quantity: {q!r}")
    return int(round(float(m.group(1)) * UNITS[m.group(2)]))


def apply_rule(rec: dict, request_m: int = REQUEST_M, limit_m: int = LIMIT_M) -> dict:
    """What the operator writes from one container's recommendation (the VPA's containerRecommendations entry)."""
    target = rec["target"]
    cpu = milli(target["cpu"])
    if cpu <= 0:
        raise ValueError(f"a CPU target of {target['cpu']!r} cannot be applied")
    mem = octets(target["memory"]) if "memory" in target else None
    return {"cpu_request_m": cpu, "cpu_limit_m": int(round(cpu * limit_m / request_m)), "memory_request_bytes": mem,
            "before": {"cpu_request_m": request_m, "cpu_limit_m": limit_m},
            "rule": f"request = target; limit = target x {limit_m}/{request_m} (the VPA's RequestsAndLimits)"}


def main(argv) -> int:
    rec = json.load(open(argv[1]))
    out = apply_rule(rec)
    json.dump(out, open(argv[2], "w"), indent=1)
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
