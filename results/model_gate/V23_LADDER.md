# The heartbeat dial in our own models: every beat beside native and beside the main engine's 60 s

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The Kubernetes governor's full decision, its heartbeat, is a dial from omni-v17 on (`docs/OMNI_V17.md`; the founder's order of 22 October): any beat can be set, the main engine ships at 60 s, and every beat is shown beside native with what it buys and what it costs, because an operator may want a fast beat for its reads and accept what it costs, or a slow one, and each beat may want its own combination of the other knobs. This page reads the beats in our own models (evidence class S): the engine alone on a plant that moves every 5 s (the model cluster's step cut to 5 s), the fast checks every 5 s at every beat, seeds 101 to 108, 1 day each, the same seeds and plant at every beat. Each beat is paired by seed against the main engine's 60 s and against native (the mean change, its 95% interval over the seeds, the word by the gauge's aim: `tools/readings.py`). A reading here says what a beat does in a model, never what a benchmark found; the real runs at every beat are `docs/PACE_PREREGISTRATION.md`, amendment 3.

Built by `tools/beat_ladder.py` from `the ladder of 31 October on the omni-v23 tree (tools/model_gate.py --models pace_kind --pace-periods 60,5,10,15,20,30,40,45,50,75,90,120 --seeds 101-108 --days 1; docs/PACE_PREREGISTRATION.md amendments 4 and 5)`. What two of them share (native and the 60 s beat) reads the same seed by seed on every modelled gauge, to the twelfth digit (the power cap's travel, a long sum of moves, differs in its last bits between Python 3.11's float sum and 3.12's); Omni's own processor is timed on the machine that ran each report, so each beat's processor is read against the 60 s beat of its own report.

## The kind benchmark's setting

The kind benchmark's setting: the compass law at the max, every autoscaler sensed, on the plant with the cloud's own autoscaler (from 31 October the same model as the cloud's at the max, docs/PACE_PREREGISTRATION.md amendment 5).

What each beat buys and what it costs, against native (the value, then the word):

| Beat | Reads a day | Omni's own processor (s an hour) | Pods waiting for a place (minutes an hour) | 95th percentile response (ms) | Minutes over the line (a day) | Pod autoscaler short of its target (minutes an hour) | Machine hours (a day) | Energy per core-hour (kWh) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| native | | | 11.01 | 150.17 | 46.25 | 1.16 | 114.92 | 0.0375 |
| every 5 s | 198,990 | 32.65 | 8.53 GAIN | 105.28 GAIN | 19.62 GAIN | 1.03 GAIN | 151.21 power given | 0.0442 power given |
| every 10 s | 107,631 | 9.77 | 9.22 GAIN | 104.93 GAIN | 19.25 GAIN | 1.04 GAIN | 154.72 power given | 0.0452 power given |
| every 15 s | 78,472 | 4.82 | 11.18 LOSS | 109.72 GAIN | 21.75 GAIN | 1.07 GAIN | 141.23 power given | 0.0423 power given |
| every 20 s | 62,141 | 3.26 | 11.98 LOSS | 112.96 GAIN | 27.50 GAIN | 1.10 GAIN | 133.97 power given | 0.0410 power given |
| every 30 s | 53,464 | 2.07 | 10.90 GAIN | 110.73 GAIN | 26.50 GAIN | 1.09 GAIN | 138.12 power given | 0.0416 power given |
| every 40 s | 48,277 | 1.65 | 12.43 LOSS | 114.50 GAIN | 27.88 GAIN | 1.10 GAIN | 133.22 power given | 0.0407 power given |
| every 45 s | 47,904 | 1.49 | 11.46 LOSS | 114.43 GAIN | 27.62 GAIN | 1.10 GAIN | 132.74 power given | 0.0408 power given |
| every 50 s | 45,106 | 1.41 | 10.93 GAIN | 126.79 GAIN | 33.62 GAIN | 1.11 GAIN | 128.30 power given | 0.0399 power given |
| every 60 s (the main engine) | 43,997 | 1.26 | 10.82 GAIN | 115.37 GAIN | 32.12 GAIN | 1.12 GAIN | 131.40 power given | 0.0404 power given |
| every 75 s | 42,671 | 1.20 | 11.46 LOSS | 123.44 GAIN | 30.88 GAIN | 1.11 GAIN | 131.77 power given | 0.0403 power given |
| every 90 s | 41,279 | 1.12 | 10.55 GAIN | 120.29 GAIN | 30.88 GAIN | 1.11 GAIN | 128.73 power given | 0.0398 power given |
| every 120 s | 39,124 | 1.03 | 11.85 LOSS | 124.08 GAIN | 33.75 GAIN | 1.12 GAIN | 125.47 power given | 0.0392 power given |

Each beat against the main engine's 60 s:

| Beat | Reads a day | Omni's own processor | Pods waiting for a place (minutes an hour) | 95th percentile response (ms) | Minutes over the line (a day) | Pod autoscaler short of its target (minutes an hour) | Machine hours (a day) | Energy per core-hour (kWh) |
|---|---|---|---|---|---|---|---|---|
| every 5 s | 352.28% power given | 2486.26% power given | 21.23% GAIN | 8.75% GAIN | 38.91% GAIN | 8.16% GAIN | 15.08% power given | 9.44% power given |
| every 10 s | 144.63% power given | 673.65% power given | 14.85% GAIN | 9.05% GAIN | 40.08% GAIN | 6.80% GAIN | 17.75% power given | 11.75% power given |
| every 15 s | 78.36% power given | 282.14% power given | 3.32% LOSS | 4.90% GAIN | 32.30% GAIN | 4.51% GAIN | 7.49% power given | 4.76% power given |
| every 20 s | 41.24% power given | 158.26% power given | 10.67% LOSS | 2.09% GAIN | 14.40% GAIN | 1.71% GAIN | 1.96% power given | 1.32% power given |
| every 30 s | 21.52% power given | 64.24% power given | 0.74% LOSS | 4.02% GAIN | 17.51% GAIN | 2.29% GAIN | 5.12% power given | 3.02% power given |
| every 40 s | 9.73% power given | 30.35% power given | 14.84% LOSS | 0.76% GAIN | 13.23% GAIN | 1.48% GAIN | 1.39% power given | 0.65% power given |
| every 45 s | 8.88% power given | 17.89% power given | 5.85% LOSS | 0.82% GAIN | 14.01% GAIN | 1.56% GAIN | 1.02% power given | 1.01% power given |
| every 50 s | 2.52% power given | 11.65% power given | 1.03% LOSS | 9.90% LOSS | 4.67% LOSS | 0.97% GAIN | 2.36% GAIN | 1.31% GAIN |
| every 75 s | 3.01% GAIN | 4.80% GAIN | 5.92% LOSS | 7.00% LOSS | 3.89% GAIN | 0.86% GAIN | 0.29% STEADY | 0.30% STEADY |
| every 90 s | 6.18% GAIN | 11.24% GAIN | 2.49% GAIN | 4.26% LOSS | 3.89% GAIN | 0.89% GAIN | 2.03% GAIN | 1.57% GAIN |
| every 120 s | 11.07% GAIN | 18.69% GAIN | 9.44% LOSS | 7.55% LOSS | 5.06% LOSS | 0.00% STEADY | 4.51% GAIN | 2.90% GAIN |

### Every 5 s

| Gauge | Native | Every 60 s | Every 5 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 114.92 | 131.40 | 151.21 | 15.08% power given | 31.58% power given |
| Energy per core-hour (kWh) | 0.0375 | 0.0404 | 0.0442 | 9.44% power given | 18.08% power given |
| Pods waiting for a place (minutes an hour) | 11.01 | 10.82 | 8.53 | 21.23% GAIN | 22.58% GAIN |
| Pod autoscaler short of its target (minutes an hour) | 1.16 | 1.12 | 1.03 | 8.16% GAIN | 11.54% GAIN |
| 95th percentile response (ms) | 150.17 | 115.37 | 105.28 | 8.75% GAIN | 29.89% GAIN |
| Minutes over the line (a day) | 46.25 | 32.12 | 19.62 | 38.91% GAIN | 57.57% GAIN |
| Power-cap request: moves (a day) | 0.00 | 27.12 | 13.25 | 51.15% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 26.12 | 12.25 | 53.11% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 8.27 | 4.04 | 51.15% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.26 | 32.65 | 2486.26% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,833.20 | 8,291.23 | 352.28% power given |  |

### Every 10 s

| Gauge | Native | Every 60 s | Every 10 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 114.92 | 131.40 | 154.72 | 17.75% power given | 34.63% power given |
| Energy per core-hour (kWh) | 0.0375 | 0.0404 | 0.0452 | 11.75% power given | 20.57% power given |
| Pods waiting for a place (minutes an hour) | 11.01 | 10.82 | 9.22 | 14.85% GAIN | 16.31% GAIN |
| Pod autoscaler short of its target (minutes an hour) | 1.16 | 1.12 | 1.04 | 6.80% GAIN | 10.22% GAIN |
| 95th percentile response (ms) | 150.17 | 115.37 | 104.93 | 9.05% GAIN | 30.13% GAIN |
| Minutes over the line (a day) | 46.25 | 32.12 | 19.25 | 40.08% GAIN | 58.38% GAIN |
| Power-cap request: moves (a day) | 0.00 | 27.12 | 14.00 | 48.39% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 26.12 | 13.00 | 50.24% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 8.27 | 4.27 | 48.39% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.26 | 9.77 | 673.65% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,833.20 | 4,484.63 | 144.63% power given |  |

### Every 15 s

| Gauge | Native | Every 60 s | Every 15 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 114.92 | 131.40 | 141.23 | 7.49% power given | 22.90% power given |
| Energy per core-hour (kWh) | 0.0375 | 0.0404 | 0.0423 | 4.76% power given | 13.02% power given |
| Pods waiting for a place (minutes an hour) | 11.01 | 10.82 | 11.18 | 3.32% LOSS | 1.54% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.16 | 1.12 | 1.07 | 4.51% GAIN | 8.01% GAIN |
| 95th percentile response (ms) | 150.17 | 115.37 | 109.72 | 4.90% GAIN | 26.94% GAIN |
| Minutes over the line (a day) | 46.25 | 32.12 | 21.75 | 32.30% GAIN | 52.97% GAIN |
| Power-cap request: moves (a day) | 0.00 | 27.12 | 19.75 | 27.19% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 26.12 | 18.75 | 28.23% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 8.27 | 6.02 | 27.19% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.26 | 4.82 | 282.14% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,833.20 | 3,269.65 | 78.36% power given |  |

### Every 20 s

| Gauge | Native | Every 60 s | Every 20 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 114.92 | 131.40 | 133.97 | 1.96% power given | 16.57% power given |
| Energy per core-hour (kWh) | 0.0375 | 0.0404 | 0.0410 | 1.32% power given | 9.32% power given |
| Pods waiting for a place (minutes an hour) | 11.01 | 10.82 | 11.98 | 10.67% LOSS | 8.77% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.16 | 1.12 | 1.10 | 1.71% GAIN | 5.32% GAIN |
| 95th percentile response (ms) | 150.17 | 115.37 | 112.96 | 2.09% GAIN | 24.77% GAIN |
| Minutes over the line (a day) | 46.25 | 32.12 | 27.50 | 14.40% GAIN | 40.54% GAIN |
| Power-cap request: moves (a day) | 0.00 | 27.12 | 21.38 | 21.20% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 26.12 | 20.38 | 22.01% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 8.27 | 6.52 | 21.20% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.26 | 3.26 | 158.26% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,833.20 | 2,589.20 | 41.24% power given |  |

### Every 30 s

| Gauge | Native | Every 60 s | Every 30 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 114.92 | 131.40 | 138.12 | 5.12% power given | 20.19% power given |
| Energy per core-hour (kWh) | 0.0375 | 0.0404 | 0.0416 | 3.02% power given | 11.15% power given |
| Pods waiting for a place (minutes an hour) | 11.01 | 10.82 | 10.90 | 0.74% LOSS | 0.99% GAIN |
| Pod autoscaler short of its target (minutes an hour) | 1.16 | 1.12 | 1.09 | 2.29% GAIN | 5.88% GAIN |
| 95th percentile response (ms) | 150.17 | 115.37 | 110.73 | 4.02% GAIN | 26.26% GAIN |
| Minutes over the line (a day) | 46.25 | 32.12 | 26.50 | 17.51% GAIN | 42.70% GAIN |
| Power-cap request: moves (a day) | 0.00 | 27.12 | 24.12 | 11.06% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 26.12 | 23.12 | 11.48% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 8.27 | 7.36 | 11.06% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.26 | 2.07 | 64.24% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,833.20 | 2,227.66 | 21.52% power given |  |

### Every 40 s

| Gauge | Native | Every 60 s | Every 40 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 114.92 | 131.40 | 133.22 | 1.39% power given | 15.93% power given |
| Energy per core-hour (kWh) | 0.0375 | 0.0404 | 0.0407 | 0.65% power given | 8.59% power given |
| Pods waiting for a place (minutes an hour) | 11.01 | 10.82 | 12.43 | 14.84% LOSS | 12.87% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.16 | 1.12 | 1.10 | 1.48% GAIN | 5.09% GAIN |
| 95th percentile response (ms) | 150.17 | 115.37 | 114.50 | 0.76% GAIN | 23.76% GAIN |
| Minutes over the line (a day) | 46.25 | 32.12 | 27.88 | 13.23% GAIN | 39.73% GAIN |
| Power-cap request: moves (a day) | 0.00 | 27.12 | 24.12 | 11.06% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 26.12 | 23.12 | 11.48% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 8.27 | 7.36 | 11.06% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.26 | 1.65 | 30.35% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,833.20 | 2,011.53 | 9.73% power given |  |

### Every 45 s

| Gauge | Native | Every 60 s | Every 45 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 114.92 | 131.40 | 132.74 | 1.02% power given | 15.51% power given |
| Energy per core-hour (kWh) | 0.0375 | 0.0404 | 0.0408 | 1.01% power given | 8.98% power given |
| Pods waiting for a place (minutes an hour) | 11.01 | 10.82 | 11.46 | 5.85% LOSS | 4.04% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.16 | 1.12 | 1.10 | 1.56% GAIN | 5.17% GAIN |
| 95th percentile response (ms) | 150.17 | 115.37 | 114.43 | 0.82% GAIN | 23.80% GAIN |
| Minutes over the line (a day) | 46.25 | 32.12 | 27.62 | 14.01% GAIN | 40.27% GAIN |
| Power-cap request: moves (a day) | 0.00 | 27.12 | 23.50 | 13.36% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 26.12 | 22.50 | 13.88% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 8.27 | 7.17 | 13.36% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.26 | 1.49 | 17.89% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,833.20 | 1,996.01 | 8.88% power given |  |

### Every 50 s

| Gauge | Native | Every 60 s | Every 50 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 114.92 | 131.40 | 128.30 | 2.36% GAIN | 11.64% power given |
| Energy per core-hour (kWh) | 0.0375 | 0.0404 | 0.0399 | 1.31% GAIN | 6.48% power given |
| Pods waiting for a place (minutes an hour) | 11.01 | 10.82 | 10.93 | 1.03% LOSS | 0.71% GAIN |
| Pod autoscaler short of its target (minutes an hour) | 1.16 | 1.12 | 1.11 | 0.97% GAIN | 4.61% GAIN |
| 95th percentile response (ms) | 150.17 | 115.37 | 126.79 | 9.90% LOSS | 15.57% GAIN |
| Minutes over the line (a day) | 46.25 | 32.12 | 33.62 | 4.67% LOSS | 27.30% GAIN |
| Power-cap request: moves (a day) | 0.00 | 27.12 | 27.88 | 2.76% power given | power given |
| Power-cap request: reversals (a day) | 0.00 | 26.12 | 26.88 | 2.87% power given | power given |
| Power-cap request: travel (a day) | 0.00 | 8.27 | 8.50 | 2.76% power given | power given |
| Omni's own processor (s an hour) | 0.00 | 1.26 | 1.41 | 11.65% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,833.20 | 1,879.43 | 2.52% power given |  |

### Every 60 s (the main engine)

| Gauge | Native | Every 60 s | Against native |
|---|---:|---:|---|
| Machine hours (a day) | 114.92 | 131.40 | 14.34% power given |
| Energy per core-hour (kWh) | 0.0375 | 0.0404 | 7.89% power given |
| Pods waiting for a place (minutes an hour) | 11.01 | 10.82 | 1.71% GAIN |
| Pod autoscaler short of its target (minutes an hour) | 1.16 | 1.12 | 3.67% GAIN |
| 95th percentile response (ms) | 150.17 | 115.37 | 23.17% GAIN |
| Minutes over the line (a day) | 46.25 | 32.12 | 30.54% GAIN |
| Power-cap request: moves (a day) | 0.00 | 27.12 | power given |
| Power-cap request: reversals (a day) | 0.00 | 26.12 | power given |
| Power-cap request: travel (a day) | 0.00 | 8.27 | power given |
| Omni's own processor (s an hour) | 0.00 | 1.26 |  |
| Reads of the cluster (an hour) | 0.00 | 1,833.20 |  |

### Every 75 s

| Gauge | Native | Every 60 s | Every 75 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 114.92 | 131.40 | 131.77 | 0.29% STEADY | 14.66% power given |
| Energy per core-hour (kWh) | 0.0375 | 0.0404 | 0.0403 | 0.30% STEADY | 7.57% power given |
| Pods waiting for a place (minutes an hour) | 11.01 | 10.82 | 11.46 | 5.92% LOSS | 4.11% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.16 | 1.12 | 1.11 | 0.86% GAIN | 4.49% GAIN |
| 95th percentile response (ms) | 150.17 | 115.37 | 123.44 | 7.00% LOSS | 17.80% GAIN |
| Minutes over the line (a day) | 46.25 | 32.12 | 30.88 | 3.89% GAIN | 33.24% GAIN |
| Power-cap request: moves (a day) | 0.00 | 27.12 | 27.50 | 1.38% power given | power given |
| Power-cap request: reversals (a day) | 0.00 | 26.12 | 26.50 | 1.44% power given | power given |
| Power-cap request: travel (a day) | 0.00 | 8.27 | 8.39 | 1.38% power given | power given |
| Omni's own processor (s an hour) | 0.00 | 1.26 | 1.20 | 4.80% GAIN |  |
| Reads of the cluster (an hour) | 0.00 | 1,833.20 | 1,777.95 | 3.01% GAIN |  |

### Every 90 s

| Gauge | Native | Every 60 s | Every 90 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 114.92 | 131.40 | 128.73 | 2.03% GAIN | 12.01% power given |
| Energy per core-hour (kWh) | 0.0375 | 0.0404 | 0.0398 | 1.57% GAIN | 6.20% power given |
| Pods waiting for a place (minutes an hour) | 11.01 | 10.82 | 10.55 | 2.49% GAIN | 4.16% GAIN |
| Pod autoscaler short of its target (minutes an hour) | 1.16 | 1.12 | 1.11 | 0.89% GAIN | 4.53% GAIN |
| 95th percentile response (ms) | 150.17 | 115.37 | 120.29 | 4.26% LOSS | 19.90% GAIN |
| Minutes over the line (a day) | 46.25 | 32.12 | 30.88 | 3.89% GAIN | 33.24% GAIN |
| Power-cap request: moves (a day) | 0.00 | 27.12 | 22.50 | 17.05% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 26.12 | 21.50 | 17.70% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 8.27 | 6.86 | 17.05% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.26 | 1.12 | 11.24% GAIN |  |
| Reads of the cluster (an hour) | 0.00 | 1,833.20 | 1,719.97 | 6.18% GAIN |  |

### Every 120 s

| Gauge | Native | Every 60 s | Every 120 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 114.92 | 131.40 | 125.47 | 4.51% GAIN | 9.18% power given |
| Energy per core-hour (kWh) | 0.0375 | 0.0404 | 0.0392 | 2.90% GAIN | 4.76% power given |
| Pods waiting for a place (minutes an hour) | 11.01 | 10.82 | 11.85 | 9.44% LOSS | 7.56% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.16 | 1.12 | 1.12 | 0.00% STEADY | 3.67% GAIN |
| 95th percentile response (ms) | 150.17 | 115.37 | 124.08 | 7.55% LOSS | 17.37% GAIN |
| Minutes over the line (a day) | 46.25 | 32.12 | 33.75 | 5.06% LOSS | 27.03% GAIN |
| Power-cap request: moves (a day) | 0.00 | 27.12 | 23.88 | 11.98% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 26.12 | 22.88 | 12.44% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 8.27 | 7.28 | 11.98% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.26 | 1.03 | 18.69% GAIN |  |
| Reads of the cluster (an hour) | 0.00 | 1,833.20 | 1,630.17 | 11.07% GAIN |  |

Counts over all seeds, by beat: decisions 5 s 138,240, 10 s 69,120, 15 s 46,080, 20 s 34,560, 30 s 23,040, 40 s 17,280, 45 s 15,360, 50 s 13,824, 60 s 11,520, 75 s 9,216, 90 s 7,680, 120 s 5,760; machines_parked 5 s 64,131, 10 s 31,116, 15 s 24,009, 20 s 17,716, 30 s 14,041, 40 s 9,406, 45 s 11,169, 50 s 9,966, 60 s 8,830, 75 s 7,027, 90 s 5,986, 120 s 4,009; errors 5 s 1,883, 10 s 873, 15 s 623, 20 s 440, 30 s 398, 40 s 214, 45 s 211, 50 s 197, 60 s 156, 75 s 115, 90 s 106, 120 s 74; steps_allowed 5 s 85, 10 s 119, 15 s 106, 20 s 83, 30 s 91, 40 s 72, 45 s 81, 50 s 62, 60 s 74, 75 s 58, 90 s 78, 120 s 60; steps_refused 5 s 70, 10 s 68, 15 s 66, 20 s 67, 30 s 68, 40 s 69, 45 s 70, 50 s 73, 60 s 65, 75 s 72, 90 s 63, 120 s 67; trials_abandoned 5 s 5, 10 s 2, 15 s 8, 20 s 6, 30 s 11, 40 s 7, 45 s 10, 50 s 5, 60 s 15, 75 s 10, 90 s 10, 120 s 9

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
