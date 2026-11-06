# The heartbeat dial in our own models: every beat beside native and beside the main engine's 60 s

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The Kubernetes governor's full decision, its heartbeat, is a dial from omni-v17 on (`docs/OMNI_V17.md`; the founder's order of 22 October): any beat can be set, the main engine ships at 60 s, and every beat is shown beside native with what it buys and what it costs, because an operator may want a fast beat for its reads and accept what it costs, or a slow one, and each beat may want its own combination of the other knobs. This page reads the beats in our own models (evidence class S): the engine alone on a plant that moves every 5 s (the model cluster's step cut to 5 s), the fast checks every 5 s at every beat, seeds 101 to 108, 1 day each, the same seeds and plant at every beat. Each beat is paired by seed against the main engine's 60 s and against native (the mean change, its 95% interval over the seeds, the word by the gauge's aim: `tools/readings.py`). A reading here says what a beat does in a model, never what a benchmark found; the real runs at every beat are `docs/PACE_PREREGISTRATION.md`, amendment 3.

Built by `tools/beat_ladder.py` from `the corrected model of amendment 6 (on site: the omni-v23 tree, a278eac262; through a cloud: the candidate tree ebf83ecaf9, which runs every pace exactly as omni-v23; seeds 101 to 108, one day each): results/model_gate/V23_LADDER_CORRECTED_SOURCE.json`. What two of them share (native and the 60 s beat) reads the same seed by seed on every modelled gauge, to the twelfth digit (the power cap's travel, a long sum of moves, differs in its last bits between Python 3.11's float sum and 3.12's); Omni's own processor is timed on the machine that ran each report, so each beat's processor is read against the 60 s beat of its own report.

## The cloud's setting

The cloud's setting: the compass law on top of the cloud's own autoscaler (the ladder of 22 and 23 October read it at the tune-down on the machines alone, the cloud's rule of 14 October; from 31 October, the founder's order of that day, the max with every muscle, the bill judged).

What each beat buys and what it costs, against native (the value, then the word):

| Beat | Reads a day | Omni's own processor (s an hour) | Pods waiting for a place (minutes an hour) | 95th percentile response (ms) | Minutes over the line (a day) | Pod autoscaler short of its target (minutes an hour) | Machine hours (a day) | Energy per core-hour (kWh) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| native | | | 11.01 | 150.17 | 46.25 | 1.16 | 114.92 | 0.0375 |
| every 5 s | 234,715 | 32.52 | 11.50 LOSS | 56.07 GAIN | 5.75 GAIN | 1.04 GAIN | 152.41 power given | 0.0442 power given |
| every 10 s | 132,197 | 9.98 | 12.06 LOSS | 56.58 GAIN | 6.12 GAIN | 1.06 GAIN | 153.67 power given | 0.0447 power given |
| every 15 s | 105,422 | 5.15 | 11.72 LOSS | 57.85 GAIN | 8.00 GAIN | 1.06 GAIN | 149.44 power given | 0.0437 power given |
| every 20 s | 82,923 | 3.30 | 12.60 LOSS | 61.34 GAIN | 12.12 GAIN | 1.09 GAIN | 138.68 power given | 0.0417 power given |
| every 30 s | 66,775 | 2.16 | 13.43 LOSS | 61.01 GAIN | 12.38 GAIN | 1.11 GAIN | 140.53 power given | 0.0420 power given |
| every 40 s | 53,964 | 1.68 | 13.93 LOSS | 64.91 GAIN | 13.88 GAIN | 1.11 GAIN | 133.96 power given | 0.0408 power given |
| every 45 s | 53,550 | 1.56 | 13.05 LOSS | 64.27 GAIN | 14.12 GAIN | 1.10 GAIN | 132.33 power given | 0.0407 power given |
| every 50 s | 49,950 | 1.44 | 12.68 LOSS | 69.33 GAIN | 20.75 GAIN | 1.12 GAIN | 123.89 power given | 0.0391 power given |
| every 60 s (the main engine) | 47,377 | 1.29 | 12.70 LOSS | 66.59 GAIN | 18.50 GAIN | 1.13 GAIN | 131.78 power given | 0.0403 power given |
| every 75 s | 44,623 | 1.19 | 12.82 LOSS | 66.89 GAIN | 16.88 GAIN | 1.12 GAIN | 129.77 power given | 0.0400 power given |
| every 90 s | 43,284 | 1.11 | 10.91 GAIN | 69.33 GAIN | 18.25 GAIN | 1.12 GAIN | 127.07 power given | 0.0397 power given |
| every 120 s | 40,010 | 1.02 | 12.50 LOSS | 70.91 GAIN | 19.75 GAIN | 1.13 GAIN | 126.92 power given | 0.0395 power given |

Each beat against the main engine's 60 s:

| Beat | Reads a day | Omni's own processor | Pods waiting for a place (minutes an hour) | 95th percentile response (ms) | Minutes over the line (a day) | Pod autoscaler short of its target (minutes an hour) | Machine hours (a day) | Energy per core-hour (kWh) |
|---|---|---|---|---|---|---|---|---|
| every 5 s | 395.42% power given | 2415.19% power given | 9.51% GAIN | 15.81% GAIN | 68.92% GAIN | 7.32% GAIN | 15.66% power given | 9.71% power given |
| every 10 s | 179.03% power given | 672.12% power given | 5.04% GAIN | 15.04% GAIN | 66.89% GAIN | 5.74% GAIN | 16.61% power given | 10.98% power given |
| every 15 s | 122.52% power given | 298.64% power given | 7.75% GAIN | 13.14% GAIN | 56.76% GAIN | 6.12% GAIN | 13.40% power given | 8.37% power given |
| every 20 s | 75.03% power given | 155.39% power given | 0.84% GAIN | 7.89% GAIN | 34.46% GAIN | 3.43% GAIN | 5.24% power given | 3.48% power given |
| every 30 s | 40.94% power given | 66.96% power given | 5.74% LOSS | 8.38% GAIN | 33.11% GAIN | 1.73% GAIN | 6.64% power given | 4.23% power given |
| every 40 s | 13.90% power given | 30.23% power given | 9.66% LOSS | 2.53% GAIN | 25.00% GAIN | 1.58% GAIN | 1.66% power given | 1.12% power given |
| every 45 s | 13.03% power given | 20.42% power given | 2.74% LOSS | 3.49% GAIN | 23.65% GAIN | 2.39% GAIN | 0.42% STEADY | 0.97% power given |
| every 50 s | 5.43% power given | 11.06% power given | 0.22% STEADY | 4.11% LOSS | 12.16% LOSS | 0.65% GAIN | 5.99% GAIN | 2.87% GAIN |
| every 75 s | 5.81% GAIN | 8.32% GAIN | 0.95% LOSS | 0.44% STEADY | 8.78% GAIN | 0.42% STEADY | 1.52% GAIN | 0.77% GAIN |
| every 90 s | 8.64% GAIN | 13.99% GAIN | 14.15% GAIN | 4.11% LOSS | 1.35% GAIN | 0.50% GAIN | 3.57% GAIN | 1.57% GAIN |
| every 120 s | 15.55% GAIN | 20.90% GAIN | 1.64% GAIN | 6.48% LOSS | 6.76% LOSS | 0.39% STEADY | 3.68% GAIN | 1.96% GAIN |

### Every 5 s

| Gauge | Native | Every 60 s | Every 5 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 114.92 | 131.78 | 152.41 | 15.66% power given | 32.63% power given |
| Energy per core-hour (kWh) | 0.0375 | 0.0403 | 0.0442 | 9.71% power given | 18.02% power given |
| Pods waiting for a place (minutes an hour) | 11.01 | 12.70 | 11.50 | 9.51% GAIN | 4.39% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.16 | 1.13 | 1.04 | 7.32% GAIN | 9.89% GAIN |
| 95th percentile response (ms) | 150.17 | 66.59 | 56.07 | 15.81% GAIN | 62.67% GAIN |
| Minutes over the line (a day) | 46.25 | 18.50 | 5.75 | 68.92% GAIN | 87.57% GAIN |
| Power-cap request: moves (a day) | 0.00 | 28.38 | 12.75 | 55.07% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 27.38 | 11.75 | 57.08% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 8.65 | 3.89 | 55.07% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.29 | 32.52 | 2415.19% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,974.06 | 9,779.79 | 395.42% power given |  |

### Every 10 s

| Gauge | Native | Every 60 s | Every 10 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 114.92 | 131.78 | 153.67 | 16.61% power given | 33.72% power given |
| Energy per core-hour (kWh) | 0.0375 | 0.0403 | 0.0447 | 10.98% power given | 19.39% power given |
| Pods waiting for a place (minutes an hour) | 11.01 | 12.70 | 12.06 | 5.04% GAIN | 9.55% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.16 | 1.13 | 1.06 | 5.74% GAIN | 8.35% GAIN |
| 95th percentile response (ms) | 150.17 | 66.59 | 56.58 | 15.04% GAIN | 62.32% GAIN |
| Minutes over the line (a day) | 46.25 | 18.50 | 6.12 | 66.89% GAIN | 86.76% GAIN |
| Power-cap request: moves (a day) | 0.00 | 28.38 | 15.50 | 45.37% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 27.38 | 14.50 | 47.03% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 8.65 | 4.73 | 45.37% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.29 | 9.98 | 672.12% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,974.06 | 5,508.20 | 179.03% power given |  |

### Every 15 s

| Gauge | Native | Every 60 s | Every 15 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 114.92 | 131.78 | 149.44 | 13.40% power given | 30.04% power given |
| Energy per core-hour (kWh) | 0.0375 | 0.0403 | 0.0437 | 8.37% power given | 16.57% power given |
| Pods waiting for a place (minutes an hour) | 11.01 | 12.70 | 11.72 | 7.75% GAIN | 6.42% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.16 | 1.13 | 1.06 | 6.12% GAIN | 8.73% GAIN |
| 95th percentile response (ms) | 150.17 | 66.59 | 57.85 | 13.14% GAIN | 61.48% GAIN |
| Minutes over the line (a day) | 46.25 | 18.50 | 8.00 | 56.76% GAIN | 82.70% GAIN |
| Power-cap request: moves (a day) | 0.00 | 28.38 | 18.25 | 35.68% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 27.38 | 17.25 | 36.99% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 8.65 | 5.57 | 35.68% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.29 | 5.15 | 298.64% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,974.06 | 4,392.58 | 122.52% power given |  |

### Every 20 s

| Gauge | Native | Every 60 s | Every 20 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 114.92 | 131.78 | 138.68 | 5.24% power given | 20.68% power given |
| Energy per core-hour (kWh) | 0.0375 | 0.0403 | 0.0417 | 3.48% power given | 11.31% power given |
| Pods waiting for a place (minutes an hour) | 11.01 | 12.70 | 12.60 | 0.84% GAIN | 14.39% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.16 | 1.13 | 1.09 | 3.43% GAIN | 6.10% GAIN |
| 95th percentile response (ms) | 150.17 | 66.59 | 61.34 | 7.89% GAIN | 59.15% GAIN |
| Minutes over the line (a day) | 46.25 | 18.50 | 12.12 | 34.46% GAIN | 73.78% GAIN |
| Power-cap request: moves (a day) | 0.00 | 28.38 | 21.12 | 25.55% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 27.38 | 20.12 | 26.48% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 8.65 | 6.44 | 25.55% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.29 | 3.30 | 155.39% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,974.06 | 3,455.12 | 75.03% power given |  |

### Every 30 s

| Gauge | Native | Every 60 s | Every 30 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 114.92 | 131.78 | 140.53 | 6.64% power given | 22.28% power given |
| Energy per core-hour (kWh) | 0.0375 | 0.0403 | 0.0420 | 4.23% power given | 12.13% power given |
| Pods waiting for a place (minutes an hour) | 11.01 | 12.70 | 13.43 | 5.74% LOSS | 21.98% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.16 | 1.13 | 1.11 | 1.73% GAIN | 4.46% GAIN |
| 95th percentile response (ms) | 150.17 | 66.59 | 61.01 | 8.38% GAIN | 59.37% GAIN |
| Minutes over the line (a day) | 46.25 | 18.50 | 12.38 | 33.11% GAIN | 73.24% GAIN |
| Power-cap request: moves (a day) | 0.00 | 28.38 | 23.12 | 18.50% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 27.38 | 22.12 | 19.18% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 8.65 | 7.05 | 18.50% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.29 | 2.16 | 66.96% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,974.06 | 2,782.30 | 40.94% power given |  |

### Every 40 s

| Gauge | Native | Every 60 s | Every 40 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 114.92 | 131.78 | 133.96 | 1.66% power given | 16.57% power given |
| Energy per core-hour (kWh) | 0.0375 | 0.0403 | 0.0408 | 1.12% power given | 8.79% power given |
| Pods waiting for a place (minutes an hour) | 11.01 | 12.70 | 13.93 | 9.66% LOSS | 26.50% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.16 | 1.13 | 1.11 | 1.58% GAIN | 4.31% GAIN |
| 95th percentile response (ms) | 150.17 | 66.59 | 64.91 | 2.53% GAIN | 56.78% GAIN |
| Minutes over the line (a day) | 46.25 | 18.50 | 13.88 | 25.00% GAIN | 70.00% GAIN |
| Power-cap request: moves (a day) | 0.00 | 28.38 | 22.88 | 19.38% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 27.38 | 21.88 | 20.09% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 8.65 | 6.98 | 19.38% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.29 | 1.68 | 30.23% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,974.06 | 2,248.51 | 13.90% power given |  |

### Every 45 s

| Gauge | Native | Every 60 s | Every 45 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 114.92 | 131.78 | 132.33 | 0.42% STEADY | 15.15% power given |
| Energy per core-hour (kWh) | 0.0375 | 0.0403 | 0.0407 | 0.97% power given | 8.62% power given |
| Pods waiting for a place (minutes an hour) | 11.01 | 12.70 | 13.05 | 2.74% LOSS | 18.52% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.16 | 1.13 | 1.10 | 2.39% GAIN | 5.09% GAIN |
| 95th percentile response (ms) | 150.17 | 66.59 | 64.27 | 3.49% GAIN | 57.20% GAIN |
| Minutes over the line (a day) | 46.25 | 18.50 | 14.12 | 23.65% GAIN | 69.46% GAIN |
| Power-cap request: moves (a day) | 0.00 | 28.38 | 22.75 | 19.82% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 27.38 | 21.75 | 20.55% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 8.65 | 6.94 | 19.82% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.29 | 1.56 | 20.42% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,974.06 | 2,231.26 | 13.03% power given |  |

### Every 50 s

| Gauge | Native | Every 60 s | Every 50 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 114.92 | 131.78 | 123.89 | 5.99% GAIN | 7.80% power given |
| Energy per core-hour (kWh) | 0.0375 | 0.0403 | 0.0391 | 2.87% GAIN | 4.48% power given |
| Pods waiting for a place (minutes an hour) | 11.01 | 12.70 | 12.68 | 0.22% STEADY | 15.10% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.16 | 1.13 | 1.12 | 0.65% GAIN | 3.41% GAIN |
| 95th percentile response (ms) | 150.17 | 66.59 | 69.33 | 4.11% LOSS | 53.83% GAIN |
| Minutes over the line (a day) | 46.25 | 18.50 | 20.75 | 12.16% LOSS | 55.14% GAIN |
| Power-cap request: moves (a day) | 0.00 | 28.38 | 27.88 | 1.76% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 27.38 | 26.88 | 1.83% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 8.65 | 8.50 | 1.76% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.29 | 1.44 | 11.06% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,974.06 | 2,081.23 | 5.43% power given |  |

### Every 60 s (the main engine)

| Gauge | Native | Every 60 s | Against native |
|---|---:|---:|---|
| Machine hours (a day) | 114.92 | 131.78 | 14.67% power given |
| Energy per core-hour (kWh) | 0.0375 | 0.0403 | 7.58% power given |
| Pods waiting for a place (minutes an hour) | 11.01 | 12.70 | 15.35% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.16 | 1.13 | 2.77% GAIN |
| 95th percentile response (ms) | 150.17 | 66.59 | 55.65% GAIN |
| Minutes over the line (a day) | 46.25 | 18.50 | 60.00% GAIN |
| Power-cap request: moves (a day) | 0.00 | 28.38 | power given |
| Power-cap request: reversals (a day) | 0.00 | 27.38 | power given |
| Power-cap request: travel (a day) | 0.00 | 8.65 | power given |
| Omni's own processor (s an hour) | 0.00 | 1.29 |  |
| Reads of the cluster (an hour) | 0.00 | 1,974.06 |  |

### Every 75 s

| Gauge | Native | Every 60 s | Every 75 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 114.92 | 131.78 | 129.77 | 1.52% GAIN | 12.92% power given |
| Energy per core-hour (kWh) | 0.0375 | 0.0403 | 0.0400 | 0.77% GAIN | 6.74% power given |
| Pods waiting for a place (minutes an hour) | 11.01 | 12.70 | 12.82 | 0.95% LOSS | 16.45% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.16 | 1.13 | 1.12 | 0.42% STEADY | 3.18% GAIN |
| 95th percentile response (ms) | 150.17 | 66.59 | 66.89 | 0.44% STEADY | 55.46% GAIN |
| Minutes over the line (a day) | 46.25 | 18.50 | 16.88 | 8.78% GAIN | 63.51% GAIN |
| Power-cap request: moves (a day) | 0.00 | 28.38 | 27.75 | 2.20% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 27.38 | 26.75 | 2.28% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 8.65 | 8.46 | 2.20% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.29 | 1.19 | 8.32% GAIN |  |
| Reads of the cluster (an hour) | 0.00 | 1,974.06 | 1,859.29 | 5.81% GAIN |  |

### Every 90 s

| Gauge | Native | Every 60 s | Every 90 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 114.92 | 131.78 | 127.07 | 3.57% GAIN | 10.57% power given |
| Energy per core-hour (kWh) | 0.0375 | 0.0403 | 0.0397 | 1.57% GAIN | 5.88% power given |
| Pods waiting for a place (minutes an hour) | 11.01 | 12.70 | 10.91 | 14.15% GAIN | 0.97% GAIN |
| Pod autoscaler short of its target (minutes an hour) | 1.16 | 1.13 | 1.12 | 0.50% GAIN | 3.26% GAIN |
| 95th percentile response (ms) | 150.17 | 66.59 | 69.33 | 4.11% LOSS | 53.83% GAIN |
| Minutes over the line (a day) | 46.25 | 18.50 | 18.25 | 1.35% GAIN | 60.54% GAIN |
| Power-cap request: moves (a day) | 0.00 | 28.38 | 22.25 | 21.59% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 27.38 | 21.25 | 22.37% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 8.65 | 6.79 | 21.59% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.29 | 1.11 | 13.99% GAIN |  |
| Reads of the cluster (an hour) | 0.00 | 1,974.06 | 1,803.51 | 8.64% GAIN |  |

### Every 120 s

| Gauge | Native | Every 60 s | Every 120 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 114.92 | 131.78 | 126.92 | 3.68% GAIN | 10.45% power given |
| Energy per core-hour (kWh) | 0.0375 | 0.0403 | 0.0395 | 1.96% GAIN | 5.47% power given |
| Pods waiting for a place (minutes an hour) | 11.01 | 12.70 | 12.50 | 1.64% GAIN | 13.46% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.16 | 1.13 | 1.13 | 0.39% STEADY | 2.40% GAIN |
| 95th percentile response (ms) | 150.17 | 66.59 | 70.91 | 6.48% LOSS | 52.78% GAIN |
| Minutes over the line (a day) | 46.25 | 18.50 | 19.75 | 6.76% LOSS | 57.30% GAIN |
| Power-cap request: moves (a day) | 0.00 | 28.38 | 24.38 | 14.10% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 27.38 | 23.38 | 14.61% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 8.65 | 7.43 | 14.10% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.29 | 1.02 | 20.90% GAIN |  |
| Reads of the cluster (an hour) | 0.00 | 1,974.06 | 1,667.09 | 15.55% GAIN |  |

Counts over all seeds, by beat: decisions 5 s 138,240, 10 s 69,120, 15 s 46,080, 20 s 34,560, 30 s 23,040, 40 s 17,280, 45 s 15,360, 50 s 13,824, 60 s 11,520, 75 s 9,216, 90 s 7,680, 120 s 5,760; machines_parked 5 s 64,204, 10 s 29,925, 15 s 22,917, 20 s 18,430, 30 s 13,542, 40 s 9,490, 45 s 11,034, 50 s 10,010, 60 s 8,560, 75 s 6,707, 90 s 5,875, 120 s 3,905; errors 5 s 0, 10 s 0, 15 s 0, 20 s 0, 30 s 0, 40 s 0, 45 s 0, 50 s 0, 60 s 0, 75 s 0, 90 s 0, 120 s 0; steps_allowed 5 s 78, 10 s 92, 15 s 100, 20 s 74, 30 s 76, 40 s 67, 45 s 67, 50 s 73, 60 s 74, 75 s 79, 90 s 70, 120 s 56; steps_refused 5 s 69, 10 s 69, 15 s 67, 20 s 70, 30 s 70, 40 s 66, 45 s 71, 50 s 71, 60 s 64, 75 s 70, 90 s 63, 120 s 65; trials_abandoned 5 s 5, 10 s 1, 15 s 9, 20 s 7, 30 s 8, 40 s 7, 45 s 12, 50 s 4, 60 s 14, 75 s 10, 90 s 8, 120 s 7

## On site

On site: the kind rig's own machines, made at the start, no cluster autoscaler, the compass law at the max (docs/PACE_PREREGISTRATION.md amendment 6, the corrected model).

What each beat buys and what it costs, against native (the value, then the word):

| Beat | Reads a day | Omni's own processor (s an hour) | Pods waiting for a place (minutes an hour) | 95th percentile response (ms) | Minutes over the line (a day) | Pod autoscaler short of its target (minutes an hour) | Machine hours (a day) | Energy per core-hour (kWh) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| native | | | 0.00 | 149.70 | 45.12 | 1.15 | 288.00 | 0.0786 |
| every 5 s | 297,057 | 31.85 | 0.00 STEADY (identical) | 56.59 GAIN | 5.25 GAIN | 1.05 GAIN | 288.00 STEADY (identical) | 0.0786 STEADY |
| every 10 s | 165,540 | 10.30 | 0.00 STEADY (identical) | 53.40 GAIN | 2.38 GAIN | 1.02 GAIN | 288.00 STEADY (identical) | 0.0786 STEADY |
| every 15 s | 132,646 | 5.48 | 0.00 STEADY (identical) | 58.88 GAIN | 5.75 GAIN | 1.06 GAIN | 288.00 STEADY (identical) | 0.0786 STEADY |
| every 20 s | 102,970 | 3.58 | 0.00 STEADY (identical) | 57.86 GAIN | 4.50 GAIN | 1.07 GAIN | 288.00 STEADY (identical) | 0.0786 STEADY |
| every 30 s | 78,539 | 2.25 | 0.00 STEADY (identical) | 57.94 GAIN | 5.88 GAIN | 1.08 GAIN | 288.00 STEADY (identical) | 0.0786 STEADY |
| every 40 s | 67,340 | 1.73 | 0.00 STEADY (identical) | 57.26 GAIN | 6.25 GAIN | 1.08 GAIN | 288.00 STEADY (identical) | 0.0786 STEADY |
| every 45 s | 64,552 | 1.58 | 0.00 STEADY (identical) | 58.41 GAIN | 6.38 GAIN | 1.10 GAIN | 288.00 STEADY (identical) | 0.0786 STEADY |
| every 50 s | 60,576 | 1.46 | 0.00 STEADY (identical) | 58.04 GAIN | 6.88 GAIN | 1.08 GAIN | 288.00 STEADY (identical) | 0.0786 STEADY |
| every 60 s (the main engine) | 55,608 | 1.31 | 0.00 STEADY (identical) | 59.25 GAIN | 6.88 GAIN | 1.09 GAIN | 288.00 STEADY (identical) | 0.0786 STEADY |
| every 75 s | 50,256 | 1.20 | 0.00 STEADY (identical) | 58.38 GAIN | 7.88 GAIN | 1.09 GAIN | 288.00 STEADY (identical) | 0.0786 STEADY |
| every 90 s | 46,507 | 1.10 | 0.00 STEADY (identical) | 61.56 GAIN | 7.25 GAIN | 1.09 GAIN | 288.00 STEADY (identical) | 0.0786 STEADY |
| every 120 s | 43,465 | 1.01 | 0.00 STEADY (identical) | 59.59 GAIN | 8.62 GAIN | 1.09 GAIN | 288.00 STEADY (identical) | 0.0786 STEADY |

Each beat against the main engine's 60 s:

| Beat | Reads a day | Omni's own processor | Pods waiting for a place (minutes an hour) | 95th percentile response (ms) | Minutes over the line (a day) | Pod autoscaler short of its target (minutes an hour) | Machine hours (a day) | Energy per core-hour (kWh) |
|---|---|---|---|---|---|---|---|---|
| every 5 s | 434.20% power given | 2324.75% power given | STEADY (identical) | 4.49% GAIN | 23.64% GAIN | 3.83% GAIN | 0.00% STEADY (identical) | 0.00% STEADY |
| every 10 s | 197.69% power given | 684.11% power given | STEADY (identical) | 9.88% GAIN | 65.45% GAIN | 6.22% GAIN | 0.00% STEADY (identical) | 0.00% STEADY |
| every 15 s | 138.54% power given | 317.61% power given | STEADY (identical) | 0.62% GAIN | 16.36% GAIN | 2.47% GAIN | 0.00% STEADY (identical) | 0.00% STEADY |
| every 20 s | 85.17% power given | 172.64% power given | STEADY (identical) | 2.35% GAIN | 34.55% GAIN | 2.11% GAIN | 0.00% STEADY (identical) | 0.00% STEADY |
| every 30 s | 41.24% power given | 71.34% power given | STEADY (identical) | 2.22% GAIN | 14.55% GAIN | 1.24% GAIN | 0.00% STEADY (identical) | 0.00% STEADY |
| every 40 s | 21.10% power given | 31.48% power given | STEADY (identical) | 3.36% GAIN | 9.09% GAIN | 0.76% GAIN | 0.00% STEADY (identical) | 0.00% STEADY |
| every 45 s | 16.08% power given | 20.23% power given | STEADY (identical) | 1.42% GAIN | 7.27% GAIN | 0.84% LOSS | 0.00% STEADY (identical) | 0.00% STEADY |
| every 50 s | 8.93% power given | 11.22% power given | STEADY (identical) | 2.04% GAIN | 0.00% STEADY | 0.80% GAIN | 0.00% STEADY (identical) | 0.00% STEADY |
| every 75 s | 9.62% GAIN | 8.91% GAIN | STEADY (identical) | 1.48% GAIN | 14.55% LOSS | 0.16% STEADY | 0.00% STEADY (identical) | 0.00% STEADY |
| every 90 s | 16.37% GAIN | 16.04% GAIN | STEADY (identical) | 3.89% LOSS | 5.45% LOSS | 0.12% STEADY | 0.00% STEADY (identical) | 0.00% STEADY |
| every 120 s | 21.84% GAIN | 23.10% GAIN | STEADY (identical) | 0.57% LOSS | 25.45% LOSS | 0.48% STEADY | 0.00% STEADY (identical) | 0.00% STEADY |

### Every 5 s

| Gauge | Native | Every 60 s | Every 5 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 288.00 | 288.00 | 288.00 | 0.00% STEADY (identical) | 0.00% STEADY (identical) |
| Energy per core-hour (kWh) | 0.0786 | 0.0786 | 0.0786 | 0.00% STEADY | 0.00% STEADY |
| Pods waiting for a place (minutes an hour) | 0.00 | 0.00 | 0.00 | STEADY (identical) | STEADY (identical) |
| Pod autoscaler short of its target (minutes an hour) | 1.15 | 1.09 | 1.05 | 3.83% GAIN | 9.05% GAIN |
| 95th percentile response (ms) | 149.70 | 59.25 | 56.59 | 4.49% GAIN | 62.19% GAIN |
| Minutes over the line (a day) | 45.12 | 6.88 | 5.25 | 23.64% GAIN | 88.37% GAIN |
| Power-cap request: moves (a day) | 0.00 | 9.00 | 8.38 | 6.94% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 8.00 | 7.38 | 7.81% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 2.75 | 2.55 | 6.94% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.31 | 31.85 | 2324.75% power given |  |
| Reads of the cluster (an hour) | 0.00 | 2,317.01 | 12,377.37 | 434.20% power given |  |

### Every 10 s

| Gauge | Native | Every 60 s | Every 10 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 288.00 | 288.00 | 288.00 | 0.00% STEADY (identical) | 0.00% STEADY (identical) |
| Energy per core-hour (kWh) | 0.0786 | 0.0786 | 0.0786 | 0.00% STEADY | 0.00% STEADY |
| Pods waiting for a place (minutes an hour) | 0.00 | 0.00 | 0.00 | STEADY (identical) | STEADY (identical) |
| Pod autoscaler short of its target (minutes an hour) | 1.15 | 1.09 | 1.02 | 6.22% GAIN | 11.31% GAIN |
| 95th percentile response (ms) | 149.70 | 59.25 | 53.40 | 9.88% GAIN | 64.33% GAIN |
| Minutes over the line (a day) | 45.12 | 6.88 | 2.38 | 65.45% GAIN | 94.74% GAIN |
| Power-cap request: moves (a day) | 0.00 | 9.00 | 4.75 | 47.22% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 8.00 | 3.75 | 53.12% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 2.75 | 1.45 | 47.22% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.31 | 10.30 | 684.11% power given |  |
| Reads of the cluster (an hour) | 0.00 | 2,317.01 | 6,897.48 | 197.69% power given |  |

### Every 15 s

| Gauge | Native | Every 60 s | Every 15 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 288.00 | 288.00 | 288.00 | 0.00% STEADY (identical) | 0.00% STEADY (identical) |
| Energy per core-hour (kWh) | 0.0786 | 0.0786 | 0.0786 | 0.00% STEADY | 0.00% STEADY |
| Pods waiting for a place (minutes an hour) | 0.00 | 0.00 | 0.00 | STEADY (identical) | STEADY (identical) |
| Pod autoscaler short of its target (minutes an hour) | 1.15 | 1.09 | 1.06 | 2.47% GAIN | 7.77% GAIN |
| 95th percentile response (ms) | 149.70 | 59.25 | 58.88 | 0.62% GAIN | 60.67% GAIN |
| Minutes over the line (a day) | 45.12 | 6.88 | 5.75 | 16.36% GAIN | 87.26% GAIN |
| Power-cap request: moves (a day) | 0.00 | 9.00 | 9.75 | 8.33% power given | power given |
| Power-cap request: reversals (a day) | 0.00 | 8.00 | 8.75 | 9.38% power given | power given |
| Power-cap request: travel (a day) | 0.00 | 2.75 | 2.97 | 8.33% power given | power given |
| Omni's own processor (s an hour) | 0.00 | 1.31 | 5.48 | 317.61% power given |  |
| Reads of the cluster (an hour) | 0.00 | 2,317.01 | 5,526.94 | 138.54% power given |  |

### Every 20 s

| Gauge | Native | Every 60 s | Every 20 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 288.00 | 288.00 | 288.00 | 0.00% STEADY (identical) | 0.00% STEADY (identical) |
| Energy per core-hour (kWh) | 0.0786 | 0.0786 | 0.0786 | 0.00% STEADY | 0.00% STEADY |
| Pods waiting for a place (minutes an hour) | 0.00 | 0.00 | 0.00 | STEADY (identical) | STEADY (identical) |
| Pod autoscaler short of its target (minutes an hour) | 1.15 | 1.09 | 1.07 | 2.11% GAIN | 7.43% GAIN |
| 95th percentile response (ms) | 149.70 | 59.25 | 57.86 | 2.35% GAIN | 61.35% GAIN |
| Minutes over the line (a day) | 45.12 | 6.88 | 4.50 | 34.55% GAIN | 90.03% GAIN |
| Power-cap request: moves (a day) | 0.00 | 9.00 | 8.50 | 5.56% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 8.00 | 7.50 | 6.25% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 2.75 | 2.59 | 5.56% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.31 | 3.58 | 172.64% power given |  |
| Reads of the cluster (an hour) | 0.00 | 2,317.01 | 4,290.40 | 85.17% power given |  |

### Every 30 s

| Gauge | Native | Every 60 s | Every 30 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 288.00 | 288.00 | 288.00 | 0.00% STEADY (identical) | 0.00% STEADY (identical) |
| Energy per core-hour (kWh) | 0.0786 | 0.0786 | 0.0786 | 0.00% STEADY | 0.00% STEADY |
| Pods waiting for a place (minutes an hour) | 0.00 | 0.00 | 0.00 | STEADY (identical) | STEADY (identical) |
| Pod autoscaler short of its target (minutes an hour) | 1.15 | 1.09 | 1.08 | 1.24% GAIN | 6.60% GAIN |
| 95th percentile response (ms) | 149.70 | 59.25 | 57.94 | 2.22% GAIN | 61.30% GAIN |
| Minutes over the line (a day) | 45.12 | 6.88 | 5.88 | 14.55% GAIN | 86.98% GAIN |
| Power-cap request: moves (a day) | 0.00 | 9.00 | 9.38 | 4.17% power given | power given |
| Power-cap request: reversals (a day) | 0.00 | 8.00 | 8.38 | 4.69% power given | power given |
| Power-cap request: travel (a day) | 0.00 | 2.75 | 2.86 | 4.17% power given | power given |
| Omni's own processor (s an hour) | 0.00 | 1.31 | 2.25 | 71.34% power given |  |
| Reads of the cluster (an hour) | 0.00 | 2,317.01 | 3,272.45 | 41.24% power given |  |

### Every 40 s

| Gauge | Native | Every 60 s | Every 40 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 288.00 | 288.00 | 288.00 | 0.00% STEADY (identical) | 0.00% STEADY (identical) |
| Energy per core-hour (kWh) | 0.0786 | 0.0786 | 0.0786 | 0.00% STEADY | 0.00% STEADY |
| Pods waiting for a place (minutes an hour) | 0.00 | 0.00 | 0.00 | STEADY (identical) | STEADY (identical) |
| Pod autoscaler short of its target (minutes an hour) | 1.15 | 1.09 | 1.08 | 0.76% GAIN | 6.15% GAIN |
| 95th percentile response (ms) | 149.70 | 59.25 | 57.26 | 3.36% GAIN | 61.75% GAIN |
| Minutes over the line (a day) | 45.12 | 6.88 | 6.25 | 9.09% GAIN | 86.15% GAIN |
| Power-cap request: moves (a day) | 0.00 | 9.00 | 9.25 | 2.78% power given | power given |
| Power-cap request: reversals (a day) | 0.00 | 8.00 | 8.25 | 3.12% power given | power given |
| Power-cap request: travel (a day) | 0.00 | 2.75 | 2.82 | 2.78% power given | power given |
| Omni's own processor (s an hour) | 0.00 | 1.31 | 1.73 | 31.48% power given |  |
| Reads of the cluster (an hour) | 0.00 | 2,317.01 | 2,805.82 | 21.10% power given |  |

### Every 45 s

| Gauge | Native | Every 60 s | Every 45 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 288.00 | 288.00 | 288.00 | 0.00% STEADY (identical) | 0.00% STEADY (identical) |
| Energy per core-hour (kWh) | 0.0786 | 0.0786 | 0.0786 | 0.00% STEADY | 0.00% STEADY |
| Pods waiting for a place (minutes an hour) | 0.00 | 0.00 | 0.00 | STEADY (identical) | STEADY (identical) |
| Pod autoscaler short of its target (minutes an hour) | 1.15 | 1.09 | 1.10 | 0.84% LOSS | 4.64% GAIN |
| 95th percentile response (ms) | 149.70 | 59.25 | 58.41 | 1.42% GAIN | 60.98% GAIN |
| Minutes over the line (a day) | 45.12 | 6.88 | 6.38 | 7.27% GAIN | 85.87% GAIN |
| Power-cap request: moves (a day) | 0.00 | 9.00 | 9.50 | 5.56% power given | power given |
| Power-cap request: reversals (a day) | 0.00 | 8.00 | 8.50 | 6.25% power given | power given |
| Power-cap request: travel (a day) | 0.00 | 2.75 | 2.90 | 5.56% power given | power given |
| Omni's own processor (s an hour) | 0.00 | 1.31 | 1.58 | 20.23% power given |  |
| Reads of the cluster (an hour) | 0.00 | 2,317.01 | 2,689.66 | 16.08% power given |  |

### Every 50 s

| Gauge | Native | Every 60 s | Every 50 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 288.00 | 288.00 | 288.00 | 0.00% STEADY (identical) | 0.00% STEADY (identical) |
| Energy per core-hour (kWh) | 0.0786 | 0.0786 | 0.0786 | 0.00% STEADY | 0.00% STEADY |
| Pods waiting for a place (minutes an hour) | 0.00 | 0.00 | 0.00 | STEADY (identical) | STEADY (identical) |
| Pod autoscaler short of its target (minutes an hour) | 1.15 | 1.09 | 1.08 | 0.80% GAIN | 6.18% GAIN |
| 95th percentile response (ms) | 149.70 | 59.25 | 58.04 | 2.04% GAIN | 61.23% GAIN |
| Minutes over the line (a day) | 45.12 | 6.88 | 6.88 | 0.00% STEADY | 84.76% GAIN |
| Power-cap request: moves (a day) | 0.00 | 9.00 | 10.25 | 13.89% power given | power given |
| Power-cap request: reversals (a day) | 0.00 | 8.00 | 9.25 | 15.62% power given | power given |
| Power-cap request: travel (a day) | 0.00 | 2.75 | 3.13 | 13.89% power given | power given |
| Omni's own processor (s an hour) | 0.00 | 1.31 | 1.46 | 11.22% power given |  |
| Reads of the cluster (an hour) | 0.00 | 2,317.01 | 2,524.01 | 8.93% power given |  |

### Every 60 s (the main engine)

| Gauge | Native | Every 60 s | Against native |
|---|---:|---:|---|
| Machine hours (a day) | 288.00 | 288.00 | 0.00% STEADY (identical) |
| Energy per core-hour (kWh) | 0.0786 | 0.0786 | 0.00% STEADY |
| Pods waiting for a place (minutes an hour) | 0.00 | 0.00 | STEADY (identical) |
| Pod autoscaler short of its target (minutes an hour) | 1.15 | 1.09 | 5.43% GAIN |
| 95th percentile response (ms) | 149.70 | 59.25 | 60.42% GAIN |
| Minutes over the line (a day) | 45.12 | 6.88 | 84.76% GAIN |
| Power-cap request: moves (a day) | 0.00 | 9.00 | power given |
| Power-cap request: reversals (a day) | 0.00 | 8.00 | power given |
| Power-cap request: travel (a day) | 0.00 | 2.75 | power given |
| Omni's own processor (s an hour) | 0.00 | 1.31 |  |
| Reads of the cluster (an hour) | 0.00 | 2,317.01 |  |

### Every 75 s

| Gauge | Native | Every 60 s | Every 75 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 288.00 | 288.00 | 288.00 | 0.00% STEADY (identical) | 0.00% STEADY (identical) |
| Energy per core-hour (kWh) | 0.0786 | 0.0786 | 0.0786 | 0.00% STEADY | 0.00% STEADY |
| Pods waiting for a place (minutes an hour) | 0.00 | 0.00 | 0.00 | STEADY (identical) | STEADY (identical) |
| Pod autoscaler short of its target (minutes an hour) | 1.15 | 1.09 | 1.09 | 0.16% STEADY | 5.58% GAIN |
| 95th percentile response (ms) | 149.70 | 59.25 | 58.38 | 1.48% GAIN | 61.00% GAIN |
| Minutes over the line (a day) | 45.12 | 6.88 | 7.88 | 14.55% LOSS | 82.55% GAIN |
| Power-cap request: moves (a day) | 0.00 | 9.00 | 11.00 | 22.22% power given | power given |
| Power-cap request: reversals (a day) | 0.00 | 8.00 | 10.00 | 25.00% power given | power given |
| Power-cap request: travel (a day) | 0.00 | 2.75 | 3.36 | 22.22% power given | power given |
| Omni's own processor (s an hour) | 0.00 | 1.31 | 1.20 | 8.91% GAIN |  |
| Reads of the cluster (an hour) | 0.00 | 2,317.01 | 2,094.02 | 9.62% GAIN |  |

### Every 90 s

| Gauge | Native | Every 60 s | Every 90 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 288.00 | 288.00 | 288.00 | 0.00% STEADY (identical) | 0.00% STEADY (identical) |
| Energy per core-hour (kWh) | 0.0786 | 0.0786 | 0.0786 | 0.00% STEADY | 0.00% STEADY |
| Pods waiting for a place (minutes an hour) | 0.00 | 0.00 | 0.00 | STEADY (identical) | STEADY (identical) |
| Pod autoscaler short of its target (minutes an hour) | 1.15 | 1.09 | 1.09 | 0.12% STEADY | 5.54% GAIN |
| 95th percentile response (ms) | 149.70 | 59.25 | 61.56 | 3.89% LOSS | 58.88% GAIN |
| Minutes over the line (a day) | 45.12 | 6.88 | 7.25 | 5.45% LOSS | 83.93% GAIN |
| Power-cap request: moves (a day) | 0.00 | 9.00 | 8.50 | 5.56% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 8.00 | 7.50 | 6.25% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 2.75 | 2.59 | 5.56% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.31 | 1.10 | 16.04% GAIN |  |
| Reads of the cluster (an hour) | 0.00 | 2,317.01 | 1,937.80 | 16.37% GAIN |  |

### Every 120 s

| Gauge | Native | Every 60 s | Every 120 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 288.00 | 288.00 | 288.00 | 0.00% STEADY (identical) | 0.00% STEADY (identical) |
| Energy per core-hour (kWh) | 0.0786 | 0.0786 | 0.0786 | 0.00% STEADY | 0.00% STEADY |
| Pods waiting for a place (minutes an hour) | 0.00 | 0.00 | 0.00 | STEADY (identical) | STEADY (identical) |
| Pod autoscaler short of its target (minutes an hour) | 1.15 | 1.09 | 1.09 | 0.48% STEADY | 4.98% GAIN |
| 95th percentile response (ms) | 149.70 | 59.25 | 59.59 | 0.57% LOSS | 60.19% GAIN |
| Minutes over the line (a day) | 45.12 | 6.88 | 8.62 | 25.45% LOSS | 80.89% GAIN |
| Power-cap request: moves (a day) | 0.00 | 9.00 | 8.75 | 2.78% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 8.00 | 7.75 | 3.12% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 2.75 | 2.67 | 2.78% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.31 | 1.01 | 23.10% GAIN |  |
| Reads of the cluster (an hour) | 0.00 | 2,317.01 | 1,811.06 | 21.84% GAIN |  |

Counts over all seeds, by beat: decisions 5 s 138,240, 10 s 69,120, 15 s 46,080, 20 s 34,560, 30 s 23,040, 40 s 17,280, 45 s 15,360, 50 s 13,824, 60 s 11,520, 75 s 9,216, 90 s 7,680, 120 s 5,760; machines_parked 5 s 0, 10 s 0, 15 s 0, 20 s 0, 30 s 0, 40 s 0, 45 s 0, 50 s 0, 60 s 0, 75 s 0, 90 s 0, 120 s 0; errors 5 s 0, 10 s 0, 15 s 0, 20 s 0, 30 s 0, 40 s 0, 45 s 0, 50 s 0, 60 s 0, 75 s 0, 90 s 0, 120 s 0; steps_allowed 5 s 99, 10 s 112, 15 s 80, 20 s 80, 30 s 76, 40 s 75, 45 s 54, 50 s 88, 60 s 106, 75 s 64, 90 s 70, 120 s 70; steps_refused 5 s 77, 10 s 78, 15 s 79, 20 s 78, 30 s 80, 40 s 80, 45 s 81, 50 s 79, 60 s 76, 75 s 80, 90 s 79, 120 s 78; trials_abandoned 5 s 3, 10 s 2, 15 s 3, 20 s 4, 30 s 2, 40 s 2, 45 s 2, 50 s 0, 60 s 6, 75 s 4, 90 s 1, 120 s 7

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
