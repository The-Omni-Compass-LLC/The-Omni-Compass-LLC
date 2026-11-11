# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Derive a portable, immutable-at-commit website surface contract from actual receipt rows.

    python3 tools/site_surface_contract.py --check
    python3 tools/site_surface_contract.py --write

--check fails when the committed contract diverges from the latest permitted
SITE_NUMBERS feed. The published website can consume this JSON directly.
Neither mode modifies a benchmark, accepts typed fallback statistics or
attests that a production website deploy has taken place.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/WEBSITE_SURFACE_CONTRACT.json"
PUBLISHER = "Dubra Software Inc. / The Omni-Compass LLC"
REQUIRED_IDS = (
    "omni_index", "work_and_speed", "kubernetes", "alert_minutes", "pages",
    "chip_energy_per_request", "chip_work_for_the_bill", "cloud_bill",
    "arm_b_vs_a", "arm_d_vs_c",
)
SURFACES = {
    "homepage.hero": ["omni_index", "kubernetes"],
    "homepage.ticker": ["omni_index", "kubernetes", "chip_energy_per_request", "cloud_bill"],
    "homepage.carousel": ["omni_index", "work_and_speed", "kubernetes", "chip_work_for_the_bill"],
    "virtual_tour": ["omni_index", "kubernetes", "chip_energy_per_request", "cloud_bill"],
    "virtual_guide": ["omni_index", "work_and_speed", "chip_work_for_the_bill", "cloud_bill"],
    "investors": ["omni_index", "kubernetes", "chip_work_for_the_bill", "cloud_bill"],
    "press": ["omni_index", "kubernetes"],
    "case_studies": ["kubernetes", "chip_energy_per_request", "cloud_bill"],
    "whitepaper": ["omni_index", "work_and_speed", "kubernetes"],
    "awards": ["omni_index"],
    "market.licensing": [],
}
SCRIPTS = {
    "what_is_omni": (
        "Omni-Compass is supervisory software from Dubra Software Inc. / The Omni-Compass LLC. "
        "It observes native controllers, proposes permitted setting changes, and retains rollback. "
        "It does not replace the underlying hardware or pass user data through a new data plane."
    ),
    "where_numbers_come_from": (
        "Every displayed number comes from a named paired-run receipt and scoring rule, "
        "with its version and evidence class. The software index is not a whole-system "
        "bill reduction. Physical meters, cloud billing and models are separate readings."
    ),
    "what_is_measured": (
        "Useful completed work in the same interval, service latency, energy, resources "
        "and total bill are distinct metrics. Gains and adverse outcomes are reported "
        "under their own measurement definitions, not added together."
    ),
    "licensing": (
        "Proposed commercial terms are a 25 percent share of contractually verified "
        "eligible savings and a separately negotiated 5 percent embedded-hardware "
        "royalty on an expressly agreed base. These are proposals, not measured benefits."
    ),
}


def build_contract(root: Path = ROOT) -> dict:
    feed = json.loads((root / "results/SITE_NUMBERS.json").read_text(encoding="utf-8"))
    index = json.loads((root / "results/OMNI_INDEX.json").read_text(encoding="utf-8"))
    rows = feed["show"]
    by_id = {r["id"]: r for r in rows}
    if len(by_id) != len(rows) or set(by_id) != set(REQUIRED_IDS):
        raise ValueError("public feed IDs changed: review the website contract before publication")
    if feed["source"] != "tools/site_numbers.py":
        raise ValueError("source of public metrics is not the measured feed generator")
    for key, expected in (
        ("omni_index", index["headline_pct"]),
        ("work_and_speed", index["service_headline_pct"]),
        ("kubernetes", next(v for k, v in index["categories"].items()
                            if k.startswith("Real Kubernetes"))),
    ):
        value = by_id[key]["value_pct"]
        if value is None or not math.isclose(value, round(expected, 1), abs_tol=1e-9):
            raise ValueError(f"{key}: public value diverges from indexed receipt")
    claims = []
    for key in REQUIRED_IDS:
        r = by_id[key]
        if r["cls"] not in ("L", "P"):
            raise ValueError(f"{key}: model or unknown class cannot be displayed as measurement")
        if not r["sentence"] or not r["engine"] or not r["receipt"]:
            raise ValueError(f"{key}: missing statement, engine or evidence citation")
        receipt = r["receipt"].split(" (")[0]
        if not (root / receipt).is_file():
            raise ValueError(f"{key}: missing original receipt {receipt}")
        claims.append({
            "id": key,
            "value_pct": r.get("value_pct"),
            "sentence": r["sentence"],
            "evidence_class": r["cls"],
            "engine": r["engine"],
            "receipt": r["receipt"],
            "scope": r["place"],
            "verdict": r["word"],
        })
    for surface, ids in SURFACES.items():
        for key in ids:
            if key not in by_id:
                raise ValueError(f"{surface}: missing evidence {key}")
    return {
        "schema_version": 1,
        "publisher": PUBLISHER,
        "product": "Omni-Compass",
        "product_definition": "Pure supervisory software for existing native-controlled infrastructure; no rip and replace.",
        "upstream_feed": "results/SITE_NUMBERS.json",
        "upstream_index": "results/OMNI_INDEX.json",
        "evidence_rule": (
            "Display only the identified receipt sentence, engine, class, and scope. "
            "A composite index is not raw work gain, a bill saving or cross-layer physical proof. "
            "Show both gains and adverse results. Never silently use typed fallbacks."
        ),
        "unavailable_message": "The record could not be read just now.",
        "claims": claims,
        "surfaces": SURFACES,
        "virtual_guide_scripts": SCRIPTS,
        "commercial_proposal": {
            "status": "proposed_not_executed",
            "savings_participation_rate": 0.25,
            "hardware_embedding_royalty_rate": 0.05,
            "royalty_base": "defined by signed agreement, not assumed gross hardware sales",
            "savings_base": "contractually verified attributable eligible net savings",
            "additional_work_same_time": "separately measure completed goodput per equal-duration interval",
            "reference": "docs/COMMERCIAL_TERMS_PROPOSAL.md",
        },
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--write", action="store_true")
    args = ap.parse_args(argv)
    expected = json.dumps(build_contract(), indent=2, ensure_ascii=False) + "\n"
    if args.write:
        OUT.write_text(expected, encoding="utf-8")
        print(f"WROTE {OUT.relative_to(ROOT)}")
        return 0
    if not OUT.exists() or OUT.read_text(encoding="utf-8") != expected:
        print("FAIL: website contract differs from the evidence feed; run --write and review the diff")
        return 1
    print("PASS: website surfaces, dialogue, attribution and fees match current receipt-derived contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
