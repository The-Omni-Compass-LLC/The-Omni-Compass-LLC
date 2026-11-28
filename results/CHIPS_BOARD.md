# Every chip, every run: the GPU benchmark board

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License, or, for a pilot, a signed, paid pilot agreement for the systems and dates it names, from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

Each chip is its own benchmark: **arm A**, the card under its own firmware (native), against **arm B**, the same card with Omni-Compass on top, three runs on rented machines (A, B and C), every row read by the one key (`tools/readings.py`) in the table its runs wrote. The cloud's two arms (C, native on a cloud cluster; D, Omni-Compass on top of it) are the cloud's own tables (`results/TWO_BILLS.md`). Nothing here is computed but counts; every row that is not STEADY is listed with its word, LOSS rows included. The card's own meter is evidence class P; the stacks' models around the card are class S (our own models, never proof). A table is its engine's record: the combined board adds chips together on one engine, never across engines. Written by `tools/chips_board.py` from `results/gpu/*_ABC.json`.

## 1. Every chip

| Chip | Where | Machine | Workflow | Status | Tables | Engines |
|---|---|---|---|---|---:|---|
| NVIDIA A10, 24 GB | Lambda | gpu_1x_a10 (one card) | `lambda-gpu.yml` (test 1card) | run | 5 | omni-v21, omni-v23 |
| NVIDIA A100, 40 GB SXM4 | Lambda | gpu_1x_a100_sxm4 (one card) | `lambda-gpu.yml` (test 1card, instance_type) | run | 3 | omni-v21 |
| NVIDIA A100, 80 GB SXM4, eight cards | Lambda | gpu_8x_a100_80gb_sxm4 | `lambda-gpu.yml` (test 8card); not now, the founder's word of 14 November, for its cost an hour | run | 1 | omni-v23 |
| NVIDIA A10G, 24 GB | Amazon | g5.xlarge, g5.2xlarge (one card) | `aws-gpu.yml` (14 November) | wired, not yet run | 0 | none |
| NVIDIA L4, 24 GB | Amazon | g6.xlarge (one card) | `aws-gpu.yml` (instance_type g6.xlarge) | wired, not yet run | 0 | none |
| NVIDIA T4, 16 GB | Amazon | g4dn.xlarge (one card) | `aws-gpu.yml` (instance_type g4dn.xlarge) | wired, not yet run | 0 | none |
| NVIDIA H100, 80 GB PCIe | Lambda | gpu_1x_h100_pcie (one card) | `lambda-gpu.yml` (test 1card, instance_type) | wired, not yet run | 0 | none |

## 2. Every table, each chip its own scenario

### NVIDIA A10, 24 GB

| Table | Engine | Runs (A, B, C) | The card's own meter (class P) | The stacks' models (class S) | Both together |
|---|---|---|---|---|---|
| [V21_STACKS_A10_ABC.md](gpu/V21_STACKS_A10_ABC.md) | omni-v21 | 40394988327, 40394992822, 40394997159 | GAIN 1, LOSS 3, power given 2, the runs disagree 1, STEADY 63, shown, not judged 30 | STEADY 56, shown, not judged 24 | STEADY 56, shown, not judged 24 |
| [V23_A10_CAP_ABC.md](gpu/V23_A10_CAP_ABC.md) | omni-v23 | 41243352339, 41243355485, 41243358705 | GAIN 3, the runs disagree 3, STEADY 7 | none | none |
| [V23_A10_CAP_FULL_ABC.md](gpu/V23_A10_CAP_FULL_ABC.md) | omni-v23 | 41243352339, 41243355485, 41243358705 | GAIN 7, the runs disagree 5, STEADY 1 | none | none |
| [V23_A10_FAST_ABC.md](gpu/V23_A10_FAST_ABC.md) | omni-v23 | 41243361994, 41243364991, 41243368008 | the runs disagree 1, STEADY 12 | none | none |
| [V23_A10_STACKS_FULL_ABC.md](gpu/V23_A10_STACKS_FULL_ABC.md) | omni-v23 | 41271470803, 41271473309, 41271475877 | GAIN 1, LOSS 7, power given 6, STEADY 84, shown, not judged 42 | STEADY 56, shown, not judged 24 | STEADY 56, shown, not judged 24 |

Every row that is not STEADY:

| Table | Class | Where | Gauge | Reading |
|---|---|---|---|---|
| V21_STACKS_A10_ABC | P | 1x energy_facility_industrial | p95 | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| V21_STACKS_A10_ABC | P | 1x stack | p95 | the runs disagree |
| V21_STACKS_A10_ABC | P | 10x energy_facility_industrial | p95 | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| V21_STACKS_A10_ABC | P | 10x physics_robotics_autonomous | primary | power given by the mean of our three runs, beyond the noise in 0 of 3 |
| V21_STACKS_A10_ABC | P | 10x physics_robotics_autonomous | energy | power given by the mean of our three runs, beyond the noise in 0 of 3 |
| V21_STACKS_A10_ABC | P | 10x physics_robotics_autonomous | p95 | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| V21_STACKS_A10_ABC | P | 10x tower | p95 | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| V23_A10_CAP_ABC | P | the card | response time, mean (ms) | the runs disagree |
| V23_A10_CAP_ABC | P | the card | response time, 95th percentile (ms) | the runs disagree |
| V23_A10_CAP_ABC | P | the card | response time, 99th percentile (ms) | the runs disagree |
| V23_A10_CAP_ABC | P | the card | temperature, mean (C) | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| V23_A10_CAP_ABC | P | the card | energy, GPU device counter (J) | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| V23_A10_CAP_ABC | P | the card | power-capped share of samples | GAIN in all three of our runs |
| V23_A10_CAP_FULL_ABC | P | the card | work per energy (served requests per kJ) | GAIN in all three of our runs |
| V23_A10_CAP_FULL_ABC | P | the card | energy, GPU (J) | GAIN in all three of our runs |
| V23_A10_CAP_FULL_ABC | P | the card | energy per served request (J) | GAIN in all three of our runs |
| V23_A10_CAP_FULL_ABC | P | the card | power, GPU mean (W) | GAIN in all three of our runs |
| V23_A10_CAP_FULL_ABC | P | the card | requests served | the runs disagree |
| V23_A10_CAP_FULL_ABC | P | the card | requests not served | the runs disagree |
| V23_A10_CAP_FULL_ABC | P | the card | response time, mean (ms) | the runs disagree |
| V23_A10_CAP_FULL_ABC | P | the card | response time, 95th percentile (ms) | the runs disagree |
| V23_A10_CAP_FULL_ABC | P | the card | response time, 99th percentile (ms) | the runs disagree |
| V23_A10_CAP_FULL_ABC | P | the card | temperature, peak (C) | GAIN by the mean of our three runs, beyond the noise in 1 of 3 |
| V23_A10_CAP_FULL_ABC | P | the card | energy, GPU device counter (J) | GAIN in all three of our runs |
| V23_A10_CAP_FULL_ABC | P | the card | power-capped share of samples | GAIN by the mean of our three runs, beyond the noise in 1 of 3 |
| V23_A10_FAST_ABC | P | the card | response time, 95th percentile (ms) | the runs disagree |
| V23_A10_STACKS_FULL_ABC | P | 1x physics_robotics_autonomous | p95 | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| V23_A10_STACKS_FULL_ABC | P | 1x spine | primary | power given by the mean of our three runs, beyond the noise in 0 of 3 |
| V23_A10_STACKS_FULL_ABC | P | 1x spine | work | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| V23_A10_STACKS_FULL_ABC | P | 1x spine | p95 | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| V23_A10_STACKS_FULL_ABC | P | 1x spine | per_dollar | power given by the mean of our three runs, beyond the noise in 0 of 3 |
| V23_A10_STACKS_FULL_ABC | P | 10x energy_facility_industrial | p95 | GAIN by the mean of our three runs, beyond the noise in 0 of 3 |
| V23_A10_STACKS_FULL_ABC | P | 10x physics_robotics_autonomous | primary | power given by the mean of our three runs, beyond the noise in 0 of 3 |
| V23_A10_STACKS_FULL_ABC | P | 10x physics_robotics_autonomous | work | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| V23_A10_STACKS_FULL_ABC | P | 10x physics_robotics_autonomous | p95 | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| V23_A10_STACKS_FULL_ABC | P | 10x physics_robotics_autonomous | per_dollar | power given by the mean of our three runs, beyond the noise in 0 of 3 |
| V23_A10_STACKS_FULL_ABC | P | 10x tower | primary | power given by the mean of our three runs, beyond the noise in 0 of 3 |
| V23_A10_STACKS_FULL_ABC | P | 10x tower | work | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| V23_A10_STACKS_FULL_ABC | P | 10x tower | p95 | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| V23_A10_STACKS_FULL_ABC | P | 10x tower | per_dollar | power given by the mean of our three runs, beyond the noise in 0 of 3 |

### NVIDIA A100, 40 GB SXM4

| Table | Engine | Runs (A, B, C) | The card's own meter (class P) | The stacks' models (class S) | Both together |
|---|---|---|---|---|---|
| [V21_A100_CAP_ABC.md](gpu/V21_A100_CAP_ABC.md) | omni-v21 | 40485609401, 40485613546, 40485617318 | GAIN 2, LOSS 2, the runs disagree 1, STEADY 8 | none | none |
| [V21_A100_CAP_FULL_ABC.md](gpu/V21_A100_CAP_FULL_ABC.md) | omni-v21 | 40485609401, 40485613546, 40485617318 | GAIN 1, LOSS 2, STEADY 10 | none | none |
| [V21_A100_SAVE_ABC.md](gpu/V21_A100_SAVE_ABC.md) | omni-v21 | 40485597269, 40485602065, 40485605739 | GAIN 6, the runs disagree 1, STEADY 6 | none | none |

Every row that is not STEADY:

| Table | Class | Where | Gauge | Reading |
|---|---|---|---|---|
| V21_A100_CAP_ABC | P | the card | response time, mean (ms) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| V21_A100_CAP_ABC | P | the card | response time, 95th percentile (ms) | the runs disagree |
| V21_A100_CAP_ABC | P | the card | response time, 99th percentile (ms) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| V21_A100_CAP_ABC | P | the card | energy, GPU device counter (J) | GAIN by the mean of our three runs, beyond the noise in 1 of 3 |
| V21_A100_CAP_ABC | P | the card | power-capped share of samples | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| V21_A100_CAP_FULL_ABC | P | the card | requests not served | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| V21_A100_CAP_FULL_ABC | P | the card | response time, 95th percentile (ms) | LOSS by the mean of our three runs, beyond the noise in 0 of 3 |
| V21_A100_CAP_FULL_ABC | P | the card | power-capped share of samples | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| V21_A100_SAVE_ABC | P | the card | work per energy (served requests per kJ) | GAIN by the mean of our three runs, beyond the noise in 1 of 3 |
| V21_A100_SAVE_ABC | P | the card | energy, GPU (J) | GAIN by the mean of our three runs, beyond the noise in 1 of 3 |
| V21_A100_SAVE_ABC | P | the card | energy per served request (J) | GAIN by the mean of our three runs, beyond the noise in 1 of 3 |
| V21_A100_SAVE_ABC | P | the card | power, GPU mean (W) | GAIN by the mean of our three runs, beyond the noise in 1 of 3 |
| V21_A100_SAVE_ABC | P | the card | temperature, mean (C) | the runs disagree |
| V21_A100_SAVE_ABC | P | the card | energy, GPU device counter (J) | GAIN by the mean of our three runs, beyond the noise in 2 of 3 |
| V21_A100_SAVE_ABC | P | the card | power-capped share of samples | GAIN in all three of our runs |

### NVIDIA A100, 80 GB SXM4, eight cards

| Table | Engine | Runs (A, B, C) | The card's own meter (class P) | The stacks' models (class S) | Both together |
|---|---|---|---|---|---|
| [V23_A100_8CARD_STACKS_ABC.md](gpu/V23_A100_8CARD_STACKS_ABC.md) | omni-v23 | 41271477833, 41279081905, 41271481737 | shown, not judged 63, no value 42 | shown, not judged 36, no value 24 | shown, not judged 36, no value 24 |

## 3. All chips combined, engine by engine

| Engine | Chips | Tables | The card's own meter (class P) | The stacks' models (class S) | Both together |
|---|---|---:|---|---|---|
| omni-v21 | NVIDIA A10, 24 GB, NVIDIA A100, 40 GB SXM4 | 4 | GAIN 10, LOSS 7, power given 2, the runs disagree 3, STEADY 87, shown, not judged 30 | STEADY 56, shown, not judged 24 | STEADY 56, shown, not judged 24 |
| omni-v23 | NVIDIA A10, 24 GB, NVIDIA A100, 80 GB SXM4, eight cards | 5 | GAIN 11, LOSS 7, power given 6, the runs disagree 9, STEADY 104, shown, not judged 105, no value 42 | STEADY 56, shown, not judged 60, no value 24 | STEADY 56, shown, not judged 60, no value 24 |

## 4. Not yet run

Wired and not yet run, so no number stands for them: NVIDIA A10G, 24 GB; NVIDIA L4, 24 GB; NVIDIA T4, 16 GB; NVIDIA H100, 80 GB PCIe. The engine that stands runs on each the moment its workflow is started; the eight-card machine waits on the founder's word for its cost an hour.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License, or, for a pilot, a signed, paid pilot agreement for the systems and dates it names, from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
