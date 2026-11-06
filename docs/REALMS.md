# The realms

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The muscle tower on modelled plants: **1,107 distinct muscles in 70 families** (`realms/catalog_v5.csv`, the catalog the
engine that stands carries), run as **seven organisms**, each native and with Omni-Compass on top of native: the **spine**
(`spine`, the 267 muscles every real stack runs on, every one in all four realms; an organism of its own and the base of
the other six, as an operating system is the base of every program: `docs/THE_SPINE.md`), each realm's organism (its own
families on the spine: Compute / AI / Cloud 540, Physics / Robotics / Autonomous 404, Energy / Facility / Industrial 480,
Distribution / Specialized 484), the four stacked on one clock with every duplicate of the spine kept (`stack`, 1,908)
and the whole tower, every muscle once (`tower`, 1,107). Every muscle also
runs alone on its own plant. Each is run natively (the plant's own controller alone) and with Omni-Compass on top, with
meters and receipts, under three loads: the organism's own load, the climb (the load stepping by one, 1 2 3 2 3 4 …)
and work waiting in line. Evidence class **S** (modelled: our own models of these machines, never counted in the
headline and never presented as proof). The word "simulation" is not used for them; a live stack is class L, a meter
class P.

## Run it

```
pip install -r requirements.txt
python3 tools/run_realms_v5.py --out realms5-out     # the preregistered run: every muscle alone and the seven organisms, seeds 3000-3009
python3 tests/test_realms.py                         # the harness's own checks (also inside verify.py)
python3 tools/realm_muscles.py                       # docs/REALM_MUSCLES.md: every organism written out, muscle by muscle
python3 tools/muscle_catalog.py                      # docs/MUSCLE_CATALOG.md: every muscle explained, wired and carded
```

The run is deterministic: `realms-v5.yml` (GitHub) runs it again and fails if any label or number differs from the
table committed in `results/realms_v5/`.

Results, each named for the engine it ran on: `results/realms_v5/REALMS_V5.md` (the tables: every muscle alone over its
loads, and the seven organisms under the normal, climb and line loads), `MUSCLES_V5.csv` (one row per muscle and load),
`REALMS_V5.json` (every per-seed contrast), `RUN.json` and `SHA256SUMS.txt` (commit and fingerprints). The grid of
copies and runs (1, 10 and 100 copies × 1, 10 and 100 runs, modelled and with the real cluster inside) is
`results/grid_v5/GRID.md`. The earlier catalogs' results stay as the road to 1.0: v3's in `results/realms/`, v2's in
`results/realms/v2/`, v1's in `results/realms/v1/`; nothing is read across engines, and every result runs again on the
engine that stands (`scripts/reruns.txt`).

## What is where

| File | What it is |
|---|---|
| `realms/catalog_v5.csv` | the 1,107 muscles: family, name, realm, plant, parameter set, knob (v1's 656: `realms/catalog_v1.csv`; v2/v3's 945: `realms/catalog.csv`) |
| `realms/muscle_cards_v5.csv` | every muscle's own card: the factory setting it runs on, found on development seeds and kept only when it wins twice and never falls behind native on any seed |
| `docs/wiring_recipes.csv` | every family's wiring on a real stack: the native controller, the wire out, the wire in, the restore, run live or modelled |
| `realms/plants.py` | the five plants and their native controllers; the four knobs; the capacity law for one plant |
| `realms/presets.py` | every parameter, one set per family class |
| `realms/compass_arm_v5.py` | the law on every muscle at its default, the max, and the dial's tune-down (`V5CFG`, `V5SAVE`) |
| `realms/harness.py` | the arms (native, omni), the organisms, the three loads, the outcome and the label rule |
| `docs/REALMS_PREREGISTRATION.md` | the question, the rules, the seeds and the development history, frozen before the run |
| `docs/THE_SPINE.md` | the spine, the seventh organism: what it is, why it is an organism, how it is wired, where it stands in the runners |
| `docs/REALM_MUSCLES.md`, `docs/MUSCLE_CATALOG.md` | every organism written out muscle by muscle, the spine first; every muscle explained, wired and carded (the manuals' appendix) |

## How it relates to the rest

| Layer | Realm harness | Elsewhere in this repository |
|---|---|---|
| Mathematics (T, V) | uses the engine and governor unchanged | `docs/TRACKING_THEOREM.md`, `verify.py` |
| Modelled (S) | **this** | the fleet and cluster models, the GPU model, the independent simulators (robot arms, grids, districts, swarms) |
| Real software (L) | not here | real Kubernetes and the live stacks (`results/live/`, newest engine first on the benefit sheet, `docs/BENEFIT_SHEET.md`) |
| Physical (P) | not here | the card: every earlier card result is obsolete and runs again on rented cards at one named commit (`docs/GPU_PREREGISTRATION.md`) |

A realm result that reads GAIN is a reason to test that knob on a real machine, not a substitute for it. The realms
whose knobs can be tested for real first are the compute realm's (Kubernetes on kind, the card), because the tools
already exist.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
