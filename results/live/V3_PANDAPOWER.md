# The power grid, every untouched SimBench grid: the A/B/C three-run table (Omni v3)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

pandapower (Fraunhofer IEE and the University of Kassel) with the SimBench benchmark grids: an independent, deterministic grid simulator with the grid's own voltage control as native. Omni sits on top of it, moving the substation setpoint one whole tap at a time under the frozen rules (`docs/PANDAPOWER_PREREGISTRATION.md`). The same grids ran three times as separate GitHub runs on the same frozen engine, a full year each, both load models. Because the simulator is deterministic, the runs must reproduce each other: a gauge reads **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number (a resource spent that rose reads **power given**, never a loss; the key: `docs/HOW_TO_READ_THE_RESULTS.md`)) when all three runs give the same sign, **STEADY, the same** when the change is under one part in a million, and **the runs differ** when they do not reproduce. Energy drawn, losses and import: the aim is lower. Bus-steps outside 0.95-1.05: any increase is marked. Tap operations: the aim is lower, and more of them was declared in advance as Omni's expected cost. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Grids in the run |
|---|---|---|---|---:|
| A | 38013399224 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 11 |
| B | 38013404663 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 11 |
| C | 38013410574 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 11 |

## ZIP loads (40% Z, 30% I, 30% P)

### 1-MV-comm--0-sw: 8,784 hourly steps

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy the loads drew (MWh) | 5.737e+04 | 5.652e+04 | -1.48% | -1.48% | -1.48% | **GAIN in all three of our runs** |
| energy dissipated in lines and transformers (MWh) | 540.8 | 535.6 | -0.96% | -0.96% | -0.96% | **GAIN in all three of our runs** |
| net import from the upstream grid (MWh) | 2.923e+04 | 2.838e+04 | -2.93% | -2.93% | -2.93% | **GAIN in all three of our runs** |
| bus-steps outside 0.95-1.05 (share) | 0 | 0 | +0.0e+00 | +0.0e+00 | +0.0e+00 | STEADY, the same |
| tap operations (wear; declared cost) | 1,728 | 1,148 | -33.56% | -33.56% | -33.56% | **GAIN in all three of our runs** |
| lowest voltage seen (per unit) | 0.9773 | 0.9629 | -1.46% | -1.46% | -1.46% | shown, not judged |
| highest voltage seen (per unit) | 1.047 | 1.047 | +0.00% | +0.00% | +0.00% | shown, not judged |

### 1-MV-comm--1-sw: 8,784 hourly steps

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy the loads drew (MWh) | 5.865e+04 | 5.78e+04 | -1.45% | -1.45% | -1.45% | **GAIN in all three of our runs** |
| energy dissipated in lines and transformers (MWh) | 570.7 | 565.9 | -0.83% | -0.83% | -0.83% | **GAIN in all three of our runs** |
| net import from the upstream grid (MWh) | 5,873 | 5,018 | -14.56% | -14.56% | -14.56% | **GAIN in all three of our runs** |
| bus-steps outside 0.95-1.05 (share) | 0 | 0 | +0.0e+00 | +0.0e+00 | +0.0e+00 | STEADY, the same |
| tap operations (wear; declared cost) | 1,528 | 980 | -35.86% | -35.86% | -35.86% | **GAIN in all three of our runs** |
| lowest voltage seen (per unit) | 0.9773 | 0.963 | -1.46% | -1.46% | -1.46% | shown, not judged |
| highest voltage seen (per unit) | 1.032 | 1.032 | +0.00% | +0.00% | +0.00% | shown, not judged |

### 1-MV-comm--2-sw: 8,784 hourly steps

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy the loads drew (MWh) | 6.074e+04 | 5.987e+04 | -1.43% | -1.43% | -1.43% | **GAIN in all three of our runs** |
| energy dissipated in lines and transformers (MWh) | 660.9 | 659.1 | -0.28% | -0.28% | -0.28% | STEADY, under the floor (the three runs' mean 0.28%) |
| net import from the upstream grid (MWh) | -1.366e+04 | -1.453e+04 | -6.38% | -6.38% | -6.38% | **GAIN in all three of our runs** |
| bus-steps outside 0.95-1.05 (share) | 0 | 0 | +0.0e+00 | +0.0e+00 | +0.0e+00 | STEADY, the same |
| tap operations (wear; declared cost) | 1,904 | 1,220 | -35.92% | -35.92% | -35.92% | **GAIN in all three of our runs** |
| lowest voltage seen (per unit) | 0.9745 | 0.9602 | -1.47% | -1.47% | -1.47% | shown, not judged |
| highest voltage seen (per unit) | 1.034 | 1.034 | +0.00% | +0.00% | +0.00% | shown, not judged |

### 1-MV-rural--1-sw: 8,784 hourly steps

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy the loads drew (MWh) | 3.215e+04 | 3.172e+04 | -1.35% | -1.35% | -1.35% | **GAIN in all three of our runs** |
| energy dissipated in lines and transformers (MWh) | 730.4 | 735.9 | +0.76% | +0.76% | +0.76% | **power given in all three of our runs** |
| net import from the upstream grid (MWh) | -2.947e+04 | -2.99e+04 | -1.45% | -1.45% | -1.45% | **GAIN in all three of our runs** |
| bus-steps outside 0.95-1.05 (share) | 2.3e-06 | 2.3e-06 | +0.0e+00 | +0.0e+00 | +0.0e+00 | STEADY, the same |
| tap operations (wear; declared cost) | 4 | 8 | +100.00% | +100.00% | +100.00% | **power given in all three of our runs** |
| lowest voltage seen (per unit) | 0.9768 | 0.9625 | -1.47% | -1.47% | -1.47% | shown, not judged |
| highest voltage seen (per unit) | 1.061 | 1.061 | +0.00% | +0.00% | +0.00% | shown, not judged |

### 1-MV-rural--2-sw: 8,784 hourly steps

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy the loads drew (MWh) | 3.48e+04 | 3.433e+04 | -1.34% | -1.34% | -1.34% | **GAIN in all three of our runs** |
| energy dissipated in lines and transformers (MWh) | 1,144 | 1,161 | +1.46% | +1.46% | +1.46% | **power given in all three of our runs** |
| net import from the upstream grid (MWh) | -4.125e+04 | -4.17e+04 | -1.09% | -1.09% | -1.09% | **GAIN in all three of our runs** |
| bus-steps outside 0.95-1.05 (share) | 0.000154 | 1.38e-05 | -1.4e-04 | -1.4e-04 | -1.4e-04 | **GAIN in all three of our runs** |
| tap operations (wear; declared cost) | 88 | 64 | -27.27% | -27.27% | -27.27% | **GAIN in all three of our runs** |
| lowest voltage seen (per unit) | 0.9709 | 0.9566 | -1.47% | -1.47% | -1.47% | shown, not judged |
| highest voltage seen (per unit) | 1.078 | 1.078 | +0.00% | +0.00% | +0.00% | shown, not judged |

### 1-MV-semiurb--0-sw: 8,784 hourly steps

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy the loads drew (MWh) | 4.552e+04 | 4.489e+04 | -1.37% | -1.37% | -1.37% | **GAIN in all three of our runs** |
| energy dissipated in lines and transformers (MWh) | 475 | 470.1 | -1.03% | -1.03% | -1.03% | **GAIN in all three of our runs** |
| net import from the upstream grid (MWh) | 9,007 | 8,380 | -6.96% | -6.96% | -6.96% | **GAIN in all three of our runs** |
| bus-steps outside 0.95-1.05 (share) | 0 | 0 | +0.0e+00 | +0.0e+00 | +0.0e+00 | STEADY, the same |
| tap operations (wear; declared cost) | 756 | 472 | -37.57% | -37.57% | -37.57% | **GAIN in all three of our runs** |
| lowest voltage seen (per unit) | 0.9771 | 0.9629 | -1.46% | -1.46% | -1.46% | shown, not judged |
| highest voltage seen (per unit) | 1.049 | 1.049 | +0.00% | +0.00% | +0.00% | shown, not judged |

### 1-MV-semiurb--1-sw: 8,784 hourly steps

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy the loads drew (MWh) | 4.821e+04 | 4.753e+04 | -1.39% | -1.39% | -1.39% | **GAIN in all three of our runs** |
| energy dissipated in lines and transformers (MWh) | 844.4 | 850.1 | +0.67% | +0.67% | +0.67% | **power given in all three of our runs** |
| net import from the upstream grid (MWh) | -6.034e+04 | -6.1e+04 | -1.10% | -1.10% | -1.10% | **GAIN in all three of our runs** |
| bus-steps outside 0.95-1.05 (share) | 0 | 0 | +0.0e+00 | +0.0e+00 | +0.0e+00 | STEADY, the same |
| tap operations (wear; declared cost) | 840 | 556 | -33.81% | -33.81% | -33.81% | **GAIN in all three of our runs** |
| lowest voltage seen (per unit) | 0.9735 | 0.9559 | -1.81% | -1.81% | -1.81% | shown, not judged |
| highest voltage seen (per unit) | 1.049 | 1.049 | +0.00% | +0.00% | +0.00% | shown, not judged |

### 1-MV-semiurb--2-sw: 8,784 hourly steps

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy the loads drew (MWh) | 5.109e+04 | 5.038e+04 | -1.39% | -1.39% | -1.39% | **GAIN in all three of our runs** |
| energy dissipated in lines and transformers (MWh) | 1,021 | 1,032 | +1.05% | +1.05% | +1.05% | **power given in all three of our runs** |
| net import from the upstream grid (MWh) | -8.089e+04 | -8.159e+04 | -0.87% | -0.87% | -0.87% | **GAIN in all three of our runs** |
| bus-steps outside 0.95-1.05 (share) | 1.4e-05 | 0 | -1.4e-05 | -1.4e-05 | -1.4e-05 | **GAIN in all three of our runs** |
| tap operations (wear; declared cost) | 1,988 | 1,516 | -23.74% | -23.74% | -23.74% | **GAIN in all three of our runs** |
| lowest voltage seen (per unit) | 0.967 | 0.9528 | -1.47% | -1.47% | -1.47% | shown, not judged |
| highest voltage seen (per unit) | 1.052 | 1.049 | -0.31% | -0.31% | -0.31% | shown, not judged |

### 1-MV-urban--0-sw: 8,784 hourly steps

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy the loads drew (MWh) | 7.015e+04 | 6.907e+04 | -1.54% | -1.54% | -1.54% | **GAIN in all three of our runs** |
| energy dissipated in lines and transformers (MWh) | 459.4 | 448.4 | -2.38% | -2.38% | -2.38% | **GAIN in all three of our runs** |
| net import from the upstream grid (MWh) | 5.544e+04 | 5.435e+04 | -1.97% | -1.97% | -1.97% | **GAIN in all three of our runs** |
| bus-steps outside 0.95-1.05 (share) | 0 | 0 | +0.0e+00 | +0.0e+00 | +0.0e+00 | STEADY, the same |
| tap operations (wear; declared cost) | 2,686 | 1,858 | -30.83% | -30.83% | -30.83% | **GAIN in all three of our runs** |
| lowest voltage seen (per unit) | 0.981 | 0.9641 | -1.73% | -1.73% | -1.73% | shown, not judged |
| highest voltage seen (per unit) | 1.042 | 1.042 | +0.00% | +0.00% | +0.00% | shown, not judged |

### 1-MV-urban--1-sw: 8,784 hourly steps

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy the loads drew (MWh) | 7.284e+04 | 7.172e+04 | -1.54% | -1.54% | -1.54% | **GAIN in all three of our runs** |
| energy dissipated in lines and transformers (MWh) | 458 | 447 | -2.39% | -2.39% | -2.39% | **GAIN in all three of our runs** |
| net import from the upstream grid (MWh) | 5.082e+04 | 4.969e+04 | -2.22% | -2.22% | -2.22% | **GAIN in all three of our runs** |
| bus-steps outside 0.95-1.05 (share) | 0 | 0 | +0.0e+00 | +0.0e+00 | +0.0e+00 | STEADY, the same |
| tap operations (wear; declared cost) | 2,986 | 2,104 | -29.54% | -29.54% | -29.54% | **GAIN in all three of our runs** |
| lowest voltage seen (per unit) | 0.9809 | 0.964 | -1.72% | -1.72% | -1.72% | shown, not judged |
| highest voltage seen (per unit) | 1.041 | 1.041 | +0.00% | +0.00% | +0.00% | shown, not judged |

### 1-MV-urban--2-sw: 8,784 hourly steps

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy the loads drew (MWh) | 7.658e+04 | 7.542e+04 | -1.51% | -1.51% | -1.51% | **GAIN in all three of our runs** |
| energy dissipated in lines and transformers (MWh) | 468.3 | 458.2 | -2.16% | -2.16% | -2.16% | **GAIN in all three of our runs** |
| net import from the upstream grid (MWh) | 3.757e+04 | 3.64e+04 | -3.10% | -3.10% | -3.10% | **GAIN in all three of our runs** |
| bus-steps outside 0.95-1.05 (share) | 0 | 0 | +0.0e+00 | +0.0e+00 | +0.0e+00 | STEADY, the same |
| tap operations (wear; declared cost) | 3,821 | 2,943 | -22.98% | -22.98% | -22.98% | **GAIN in all three of our runs** |
| lowest voltage seen (per unit) | 0.9784 | 0.9633 | -1.54% | -1.54% | -1.54% | shown, not judged |
| highest voltage seen (per unit) | 1.042 | 1.042 | +0.00% | +0.00% | +0.00% | shown, not judged |


## constant-power loads (SimBench as shipped)

### 1-MV-comm--0-sw: 8,784 hourly steps

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy the loads drew (MWh) | 5.763e+04 | 5.763e+04 | +0.00% | +0.00% | +0.00% | STEADY, the same |
| energy dissipated in lines and transformers (MWh) | 542.5 | 539.6 | -0.53% | -0.53% | -0.53% | **GAIN in all three of our runs** |
| net import from the upstream grid (MWh) | 2.949e+04 | 2.949e+04 | -0.01% | -0.01% | -0.01% | STEADY, under the floor (the three runs' mean 0.01%) |
| bus-steps outside 0.95-1.05 (share) | 0 | 0 | +0.0e+00 | +0.0e+00 | +0.0e+00 | STEADY, the same |
| tap operations (wear; declared cost) | 1,824 | 1,260 | -30.92% | -30.92% | -30.92% | **GAIN in all three of our runs** |
| lowest voltage seen (per unit) | 0.9768 | 0.9621 | -1.50% | -1.50% | -1.50% | shown, not judged |
| highest voltage seen (per unit) | 1.047 | 1.047 | +0.00% | +0.00% | +0.00% | shown, not judged |

### 1-MV-comm--1-sw: 8,784 hourly steps

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy the loads drew (MWh) | 5.897e+04 | 5.897e+04 | +0.00% | +0.00% | +0.00% | STEADY, the same |
| energy dissipated in lines and transformers (MWh) | 571.9 | 569.6 | -0.40% | -0.40% | -0.40% | STEADY, under the floor (the three runs' mean 0.40%) |
| net import from the upstream grid (MWh) | 6,198 | 6,195 | -0.04% | -0.04% | -0.04% | STEADY, under the floor (the three runs' mean 0.04%) |
| bus-steps outside 0.95-1.05 (share) | 0 | 0 | +0.0e+00 | +0.0e+00 | +0.0e+00 | STEADY, the same |
| tap operations (wear; declared cost) | 1,660 | 1,148 | -30.84% | -30.84% | -30.84% | **GAIN in all three of our runs** |
| lowest voltage seen (per unit) | 0.9769 | 0.9622 | -1.50% | -1.50% | -1.50% | shown, not judged |
| highest voltage seen (per unit) | 1.032 | 1.032 | +0.00% | +0.00% | +0.00% | shown, not judged |

### 1-MV-comm--2-sw: 8,784 hourly steps

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy the loads drew (MWh) | 6.106e+04 | 6.106e+04 | +0.00% | +0.00% | +0.00% | STEADY, the same |
| energy dissipated in lines and transformers (MWh) | 662.2 | 662 | -0.02% | -0.02% | -0.02% | STEADY, under the floor (the three runs' mean 0.02%) |
| net import from the upstream grid (MWh) | -1.334e+04 | -1.334e+04 | -0.00% | -0.00% | -0.00% | STEADY, under the floor (the three runs' mean 0.00%) |
| bus-steps outside 0.95-1.05 (share) | 0 | 0 | +0.0e+00 | +0.0e+00 | +0.0e+00 | STEADY, the same |
| tap operations (wear; declared cost) | 2,036 | 1,396 | -31.43% | -31.43% | -31.43% | **GAIN in all three of our runs** |
| lowest voltage seen (per unit) | 0.9738 | 0.959 | -1.51% | -1.51% | -1.51% | shown, not judged |
| highest voltage seen (per unit) | 1.034 | 1.034 | +0.00% | +0.00% | +0.00% | shown, not judged |

### 1-MV-rural--1-sw: 8,784 hourly steps

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy the loads drew (MWh) | 3.22e+04 | 3.22e+04 | +0.00% | +0.00% | +0.00% | STEADY, the same |
| energy dissipated in lines and transformers (MWh) | 733 | 737.1 | +0.56% | +0.56% | +0.56% | **power given in all three of our runs** |
| net import from the upstream grid (MWh) | -2.941e+04 | -2.941e+04 | +0.01% | +0.01% | +0.01% | STEADY, under the floor (the three runs' mean 0.01%) |
| bus-steps outside 0.95-1.05 (share) | 2.3e-06 | 2.3e-06 | +0.0e+00 | +0.0e+00 | +0.0e+00 | STEADY, the same |
| tap operations (wear; declared cost) | 4 | 8 | +100.00% | +100.00% | +100.00% | **power given in all three of our runs** |
| lowest voltage seen (per unit) | 0.9763 | 0.9616 | -1.51% | -1.51% | -1.51% | shown, not judged |
| highest voltage seen (per unit) | 1.061 | 1.061 | +0.00% | +0.00% | +0.00% | shown, not judged |

### 1-MV-rural--2-sw: 8,784 hourly steps

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy the loads drew (MWh) | 3.483e+04 | 3.483e+04 | +0.00% | +0.00% | +0.00% | STEADY, the same |
| energy dissipated in lines and transformers (MWh) | 1,150 | 1,163 | +1.18% | +1.18% | +1.18% | **power given in all three of our runs** |
| net import from the upstream grid (MWh) | -4.122e+04 | -4.12e+04 | +0.03% | +0.03% | +0.03% | STEADY, under the floor (the three runs' mean 0.03%) |
| bus-steps outside 0.95-1.05 (share) | 0.000162 | 1.84e-05 | -1.4e-04 | -1.4e-04 | -1.4e-04 | **GAIN in all three of our runs** |
| tap operations (wear; declared cost) | 100 | 84 | -16.00% | -16.00% | -16.00% | **GAIN in all three of our runs** |
| lowest voltage seen (per unit) | 0.97 | 0.9552 | -1.53% | -1.53% | -1.53% | shown, not judged |
| highest voltage seen (per unit) | 1.078 | 1.078 | +0.00% | +0.00% | +0.00% | shown, not judged |

### 1-MV-semiurb--0-sw: 8,784 hourly steps

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy the loads drew (MWh) | 4.577e+04 | 4.577e+04 | +0.00% | +0.00% | +0.00% | STEADY, the same |
| energy dissipated in lines and transformers (MWh) | 476.1 | 471.8 | -0.90% | -0.90% | -0.90% | **GAIN in all three of our runs** |
| net import from the upstream grid (MWh) | 9,265 | 9,260 | -0.05% | -0.05% | -0.05% | STEADY, under the floor (the three runs' mean 0.05%) |
| bus-steps outside 0.95-1.05 (share) | 0 | 0 | +0.0e+00 | +0.0e+00 | +0.0e+00 | STEADY, the same |
| tap operations (wear; declared cost) | 808 | 572 | -29.21% | -29.21% | -29.21% | **GAIN in all three of our runs** |
| lowest voltage seen (per unit) | 0.9766 | 0.962 | -1.50% | -1.50% | -1.50% | shown, not judged |
| highest voltage seen (per unit) | 1.049 | 1.049 | +0.00% | +0.00% | +0.00% | shown, not judged |

### 1-MV-semiurb--1-sw: 8,784 hourly steps

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy the loads drew (MWh) | 4.843e+04 | 4.843e+04 | +0.00% | +0.00% | +0.00% | STEADY, the same |
| energy dissipated in lines and transformers (MWh) | 845.8 | 850.7 | +0.58% | +0.58% | +0.58% | **power given in all three of our runs** |
| net import from the upstream grid (MWh) | -6.012e+04 | -6.011e+04 | +0.01% | +0.01% | +0.01% | STEADY, under the floor (the three runs' mean 0.01%) |
| bus-steps outside 0.95-1.05 (share) | 0 | 0 | +0.0e+00 | +0.0e+00 | +0.0e+00 | STEADY, the same |
| tap operations (wear; declared cost) | 888 | 612 | -31.08% | -31.08% | -31.08% | **GAIN in all three of our runs** |
| lowest voltage seen (per unit) | 0.9729 | 0.9582 | -1.51% | -1.51% | -1.51% | shown, not judged |
| highest voltage seen (per unit) | 1.049 | 1.049 | +0.00% | +0.00% | +0.00% | shown, not judged |

### 1-MV-semiurb--2-sw: 8,784 hourly steps

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy the loads drew (MWh) | 5.126e+04 | 5.126e+04 | +0.00% | +0.00% | +0.00% | STEADY, the same |
| energy dissipated in lines and transformers (MWh) | 1,023 | 1,032 | +0.89% | +0.89% | +0.89% | **power given in all three of our runs** |
| net import from the upstream grid (MWh) | -8.072e+04 | -8.071e+04 | +0.01% | +0.01% | +0.01% | STEADY, under the floor (the three runs' mean 0.01%) |
| bus-steps outside 0.95-1.05 (share) | 1.68e-05 | 0 | -1.7e-05 | -1.7e-05 | -1.7e-05 | **GAIN in all three of our runs** |
| tap operations (wear; declared cost) | 2,048 | 1,616 | -21.09% | -21.09% | -21.09% | **GAIN in all three of our runs** |
| lowest voltage seen (per unit) | 0.966 | 0.9512 | -1.54% | -1.54% | -1.54% | shown, not judged |
| highest voltage seen (per unit) | 1.052 | 1.049 | -0.31% | -0.31% | -0.31% | shown, not judged |

### 1-MV-urban--0-sw: 8,784 hourly steps

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy the loads drew (MWh) | 7.027e+04 | 7.027e+04 | +0.00% | +0.00% | +0.00% | STEADY, the same |
| energy dissipated in lines and transformers (MWh) | 459.6 | 450.9 | -1.89% | -1.89% | -1.89% | **GAIN in all three of our runs** |
| net import from the upstream grid (MWh) | 5.557e+04 | 5.556e+04 | -0.02% | -0.02% | -0.02% | STEADY, under the floor (the three runs' mean 0.02%) |
| bus-steps outside 0.95-1.05 (share) | 0 | 0 | +0.0e+00 | +0.0e+00 | +0.0e+00 | STEADY, the same |
| tap operations (wear; declared cost) | 2,820 | 1,986 | -29.57% | -29.57% | -29.57% | **GAIN in all three of our runs** |
| lowest voltage seen (per unit) | 0.9807 | 0.9634 | -1.77% | -1.77% | -1.77% | shown, not judged |
| highest voltage seen (per unit) | 1.042 | 1.042 | +0.00% | +0.00% | +0.00% | shown, not judged |

### 1-MV-urban--1-sw: 8,784 hourly steps

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy the loads drew (MWh) | 7.291e+04 | 7.291e+04 | +0.00% | +0.00% | +0.00% | STEADY, the same |
| energy dissipated in lines and transformers (MWh) | 458.1 | 449.3 | -1.94% | -1.94% | -1.94% | **GAIN in all three of our runs** |
| net import from the upstream grid (MWh) | 5.089e+04 | 5.088e+04 | -0.02% | -0.02% | -0.02% | STEADY, under the floor (the three runs' mean 0.02%) |
| bus-steps outside 0.95-1.05 (share) | 0 | 0 | +0.0e+00 | +0.0e+00 | +0.0e+00 | STEADY, the same |
| tap operations (wear; declared cost) | 3,114 | 2,284 | -26.65% | -26.65% | -26.65% | **GAIN in all three of our runs** |
| lowest voltage seen (per unit) | 0.9806 | 0.9633 | -1.76% | -1.76% | -1.76% | shown, not judged |
| highest voltage seen (per unit) | 1.042 | 1.042 | +0.00% | +0.00% | +0.00% | shown, not judged |

### 1-MV-urban--2-sw: 8,784 hourly steps

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| energy the loads drew (MWh) | 7.664e+04 | 7.664e+04 | +0.00% | +0.00% | +0.00% | STEADY, the same |
| energy dissipated in lines and transformers (MWh) | 468.5 | 460 | -1.82% | -1.82% | -1.82% | **GAIN in all three of our runs** |
| net import from the upstream grid (MWh) | 3.763e+04 | 3.762e+04 | -0.02% | -0.02% | -0.02% | STEADY, under the floor (the three runs' mean 0.02%) |
| bus-steps outside 0.95-1.05 (share) | 0 | 0 | +0.0e+00 | +0.0e+00 | +0.0e+00 | STEADY, the same |
| tap operations (wear; declared cost) | 3,943 | 3,091 | -21.61% | -21.61% | -21.61% | **GAIN in all three of our runs** |
| lowest voltage seen (per unit) | 0.978 | 0.9625 | -1.58% | -1.58% | -1.58% | shown, not judged |
| highest voltage seen (per unit) | 1.042 | 1.042 | +0.00% | +0.00% | +0.00% | shown, not judged |

## Across the grids

A grid counts only when all three runs agree.

| Load model | Gauge | GAIN in all three of our runs | LOSS in all three of our runs | Power given in all three of our runs | STEADY | The runs differ |
|---|---|---:|---:|---:|---:|---:|
| ZIP loads | energy the loads drew (MWh) | 11 | 0 | 0 | 0 | 0 |
| ZIP loads | energy dissipated in lines and transformers (MWh) | 7 | 0 | 4 (1-MV-rural--1-sw, 1-MV-rural--2-sw, 1-MV-semiurb--1-sw, 1-MV-semiurb--2-sw) | 0 | 0 |
| ZIP loads | net import from the upstream grid (MWh) | 11 | 0 | 0 | 0 | 0 |
| ZIP loads | bus-steps outside 0.95-1.05 (share) | 2 | 0 | 0 | 9 | 0 |
| ZIP loads | tap operations (wear; declared cost) | 10 | 0 | 1 (1-MV-rural--1-sw) | 0 | 0 |
| constant-power loads | energy the loads drew (MWh) | 0 | 0 | 0 | 11 | 0 |
| constant-power loads | energy dissipated in lines and transformers (MWh) | 7 | 0 | 4 (1-MV-rural--1-sw, 1-MV-rural--2-sw, 1-MV-semiurb--1-sw, 1-MV-semiurb--2-sw) | 0 | 0 |
| constant-power loads | net import from the upstream grid (MWh) | 7 | 0 | 4 (1-MV-rural--1-sw, 1-MV-rural--2-sw, 1-MV-semiurb--1-sw, 1-MV-semiurb--2-sw) | 0 | 0 |
| constant-power loads | bus-steps outside 0.95-1.05 (share) | 2 | 0 | 0 | 9 | 0 |
| constant-power loads | tap operations (wear; declared cost) | 10 | 0 | 1 (1-MV-rural--1-sw) | 0 | 0 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
