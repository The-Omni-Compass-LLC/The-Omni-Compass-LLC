# The heartbeat dial in our own models: every beat beside native and beside the main engine's 60 s

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The Kubernetes governor's full decision, its heartbeat, is a dial from omni-v17 on (`docs/OMNI_V17.md`; the founder's order of 22 October): any beat can be set, the main engine ships at 60 s, and every beat is shown beside native with what it buys and what it costs, because an operator may want a fast beat for its reads and accept what it costs, or a slow one, and each beat may want its own combination of the other knobs. This page reads the beats in our own models (evidence class S): the engine alone on a plant that moves every 5 s (the model cluster's step cut to 5 s), the fast checks every 5 s at every beat, seeds 1 to 8, 1 day each, the same seeds and plant at every beat. Each beat is paired by seed against the main engine's 60 s and against native (the mean change, its 95% interval over the seeds, the word by the gauge's aim: `tools/readings.py`). A reading here says what a beat does in a model, never what a benchmark found; the real runs at every beat are `docs/PACE_PREREGISTRATION.md`, amendment 3.

Built by `tools/beat_ladder.py` from `results/model_gate/V16_PACE.json` and `the 30 and 75 s run of 22 October on omni-v16, whose counts at those beats omni-v17 keeps (tools/model_gate.py --models pace_cloud,pace_kind --pace-periods 60,30,75 --seeds 1-8 --days 1)` and `the 90 and 120 s run of 22 October on omni-v17 with the cruise fix (tools/model_gate.py --models pace_cloud,pace_kind --pace-periods 60,90,120 --seeds 1-8 --days 1)` and `the side study of 23 October on omni-v17, the beats between 15 and 60 s the ladder had not read, 20, 40, 45 and 50 s (tools/model_gate.py --models pace_cloud,pace_kind --pace-periods 60,45,40,50,20 --seeds 1-8 --days 1; the founder's words: 'I think 45 you didn't try'); its native and 60 s rows read the same seed by seed on every modelled gauge, the power cap's travel to its last bits and the governor's own processor apart, which is read against its own report's 60 s`. What two of them share (native and the 60 s beat) reads the same seed by seed on every modelled gauge, to the twelfth digit (the power cap's travel, a long sum of moves, differs in its last bits between Python 3.11's float sum and 3.12's); Omni's own processor is timed on the machine that ran each report, so each beat's processor is read against the 60 s beat of its own report.

## The cloud's setting

The cloud's setting: the compass law at the tune-down, the machines alone.

What each beat buys and what it costs, against native (the value, then the word):

| Beat | Reads a day | Omni's own processor (s an hour) | Pods waiting for a place (minutes an hour) | 95th percentile response (ms) | Minutes over the line (a day) | Pod autoscaler short of its target (minutes an hour) | Machine hours (a day) | Energy per core-hour (kWh) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| native | | | 8.18 | 79.94 | 27.00 | 1.20 | 133.08 | 0.0357 |
| every 5 s | 86,412 | 5.51 | 16.52 LOSS | 80.18 STEADY | 27.50 LOSS | 1.20 STEADY | 129.67 GAIN | 0.0344 GAIN |
| every 10 s | 60,924 | 3.38 | 15.92 LOSS | 80.11 STEADY | 27.12 STEADY | 1.20 STEADY | 133.40 STEADY | 0.0346 GAIN |
| every 15 s | 52,545 | 2.68 | 18.36 LOSS | 80.31 STEADY | 27.62 LOSS | 1.20 STEADY | 131.48 GAIN | 0.0341 GAIN |
| every 20 s | 48,082 | 1.54 | 15.13 LOSS | 80.16 STEADY | 27.25 LOSS | 1.20 STEADY | 131.80 GAIN | 0.0348 GAIN |
| every 30 s | 44,009 | 2.07 | 18.59 LOSS | 80.22 STEADY | 27.38 LOSS | 1.20 STEADY | 132.19 GAIN | 0.0347 GAIN |
| every 40 s | 41,810 | 1.19 | 21.40 LOSS | 80.25 STEADY | 27.50 LOSS | 1.20 STEADY | 129.84 GAIN | 0.0345 GAIN |
| every 45 s | 41,204 | 1.16 | 18.62 LOSS | 80.27 STEADY | 27.50 LOSS | 1.20 STEADY | 128.44 GAIN | 0.0345 GAIN |
| every 50 s | 40,664 | 1.12 | 25.69 LOSS | 80.51 LOSS | 27.25 LOSS | 1.21 STEADY | 133.25 STEADY | 0.0349 GAIN |
| every 60 s (the main engine) | 39,691 | 1.69 | 20.88 LOSS | 80.33 STEADY | 27.50 LOSS | 1.20 STEADY | 131.98 GAIN | 0.0350 GAIN |
| every 75 s | 38,928 | 1.66 | 19.30 LOSS | 80.20 STEADY | 27.38 LOSS | 1.20 STEADY | 131.21 GAIN | 0.0350 GAIN |
| every 90 s | 38,396 | 1.60 | 18.27 LOSS | 80.35 LOSS | 27.62 LOSS | 1.20 STEADY | 131.29 GAIN | 0.0350 GAIN |
| every 120 s | 37,415 | 1.58 | 14.01 LOSS | 80.08 STEADY | 27.12 STEADY | 1.20 STEADY | 130.93 GAIN | 0.0352 GAIN |

Each beat against the main engine's 60 s:

| Beat | Reads a day | Omni's own processor | Pods waiting for a place (minutes an hour) | 95th percentile response (ms) | Minutes over the line (a day) | Pod autoscaler short of its target (minutes an hour) | Machine hours (a day) | Energy per core-hour (kWh) |
|---|---|---|---|---|---|---|---|---|
| every 5 s | 117.71% power given | 227.12% power given | 20.91% GAIN | 0.19% STEADY | 0.00% STEADY | 0.11% STEADY | 1.75% GAIN | 1.79% GAIN |
| every 10 s | 53.50% power given | 100.45% power given | 23.75% GAIN | 0.28% STEADY | 1.36% GAIN | 0.14% STEADY | 1.08% power given | 1.12% GAIN |
| every 15 s | 32.39% power given | 59.14% power given | 12.08% GAIN | 0.02% STEADY | 0.45% STEADY | 0.18% STEADY | 0.38% STEADY | 2.57% GAIN |
| every 20 s | 21.14% power given | 42.05% power given | 27.55% GAIN | 0.21% STEADY | 0.91% GAIN | 0.07% STEADY | 0.14% STEADY | 0.48% STEADY |
| every 30 s | 10.88% power given | 16.57% power given | 11.00% GAIN | 0.14% STEADY | 0.45% STEADY | 0.18% STEADY | 0.15% STEADY | 0.95% GAIN |
| every 40 s | 5.34% power given | 9.78% power given | 2.49% LOSS | 0.11% STEADY | 0.00% STEADY | 0.00% STEADY | 1.62% GAIN | 1.45% GAIN |
| every 45 s | 3.81% power given | 6.93% power given | 10.85% GAIN | 0.08% STEADY | 0.00% STEADY | 0.07% STEADY | 2.69% GAIN | 1.55% GAIN |
| every 50 s | 2.45% power given | 3.88% power given | 23.01% LOSS | 0.22% STEADY | 0.91% GAIN | 0.14% STEADY | 0.96% power given | 0.22% STEADY |
| every 75 s | 1.92% GAIN | 6.31% GAIN | 7.57% GAIN | 0.17% STEADY | 0.45% STEADY | 0.22% STEADY | 0.59% GAIN | 0.13% STEADY |
| every 90 s | 3.26% GAIN | 6.07% GAIN | 12.52% GAIN | 0.02% STEADY | 0.45% STEADY | 0.11% STEADY | 0.53% GAIN | 0.06% STEADY |
| every 120 s | 5.73% GAIN | 7.37% GAIN | 32.91% GAIN | 0.31% STEADY | 1.36% GAIN | 0.11% STEADY | 0.80% GAIN | 0.66% power given |

### Every 5 s

| Gauge | Native | Every 60 s | Every 5 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 133.08 | 131.98 | 129.67 | 1.75% GAIN | 2.56% GAIN |
| Energy per core-hour (kWh) | 0.0357 | 0.0350 | 0.0344 | 1.79% GAIN | 3.70% GAIN |
| Pods waiting for a place (minutes an hour) | 8.18 | 20.88 | 16.52 | 20.91% GAIN | 101.84% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.20 | 1.20 | 1.20 | 0.11% STEADY | 0.11% STEADY |
| 95th percentile response (ms) | 79.94 | 80.33 | 80.18 | 0.19% STEADY | 0.30% STEADY |
| Minutes over the line (a day) | 27.00 | 27.50 | 27.50 | 0.00% STEADY | 1.85% LOSS |
| Power-cap request: moves (a day) | 0.00 | 63.50 | 114.38 | 80.12% power given | power given |
| Power-cap request: reversals (a day) | 0.00 | 62.50 | 111.88 | 79.00% power given | power given |
| Power-cap request: travel (a day) | 0.00 | 19.22 | 33.28 | 73.10% power given | power given |
| Omni's own processor (s an hour) | 0.00 | 1.69 | 5.51 | 227.12% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,653.79 | 3,600.50 | 117.71% power given |  |

### Every 10 s

| Gauge | Native | Every 60 s | Every 10 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 133.08 | 131.98 | 133.40 | 1.08% power given | 0.24% STEADY |
| Energy per core-hour (kWh) | 0.0357 | 0.0350 | 0.0346 | 1.12% GAIN | 3.04% GAIN |
| Pods waiting for a place (minutes an hour) | 8.18 | 20.88 | 15.92 | 23.75% GAIN | 94.59% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.20 | 1.20 | 1.20 | 0.14% STEADY | 0.07% STEADY |
| 95th percentile response (ms) | 79.94 | 80.33 | 80.11 | 0.28% STEADY | 0.21% STEADY |
| Minutes over the line (a day) | 27.00 | 27.50 | 27.12 | 1.36% GAIN | 0.46% STEADY |
| Power-cap request: moves (a day) | 0.00 | 63.50 | 115.88 | 82.48% power given | power given |
| Power-cap request: reversals (a day) | 0.00 | 62.50 | 113.62 | 81.80% power given | power given |
| Power-cap request: travel (a day) | 0.00 | 19.22 | 33.95 | 76.61% power given | power given |
| Omni's own processor (s an hour) | 0.00 | 1.69 | 3.38 | 100.45% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,653.79 | 2,538.52 | 53.50% power given |  |

### Every 15 s

| Gauge | Native | Every 60 s | Every 15 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 133.08 | 131.98 | 131.48 | 0.38% STEADY | 1.20% GAIN |
| Energy per core-hour (kWh) | 0.0357 | 0.0350 | 0.0341 | 2.57% GAIN | 4.46% GAIN |
| Pods waiting for a place (minutes an hour) | 8.18 | 20.88 | 18.36 | 12.08% GAIN | 124.39% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.20 | 1.20 | 1.20 | 0.18% STEADY | 0.04% STEADY |
| 95th percentile response (ms) | 79.94 | 80.33 | 80.31 | 0.02% STEADY | 0.47% STEADY |
| Minutes over the line (a day) | 27.00 | 27.50 | 27.62 | 0.45% STEADY | 2.31% LOSS |
| Power-cap request: moves (a day) | 0.00 | 63.50 | 104.12 | 63.98% power given | power given |
| Power-cap request: reversals (a day) | 0.00 | 62.50 | 101.62 | 62.60% power given | power given |
| Power-cap request: travel (a day) | 0.00 | 19.22 | 31.00 | 61.27% power given | power given |
| Omni's own processor (s an hour) | 0.00 | 1.69 | 2.68 | 59.14% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,653.79 | 2,189.38 | 32.39% power given |  |

### Every 20 s

| Gauge | Native | Every 60 s | Every 20 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 133.08 | 131.98 | 131.80 | 0.14% STEADY | 0.96% GAIN |
| Energy per core-hour (kWh) | 0.0357 | 0.0350 | 0.0348 | 0.48% STEADY | 2.42% GAIN |
| Pods waiting for a place (minutes an hour) | 8.18 | 20.88 | 15.13 | 27.55% GAIN | 84.89% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.20 | 1.20 | 1.20 | 0.07% STEADY | 0.14% STEADY |
| 95th percentile response (ms) | 79.94 | 80.33 | 80.16 | 0.21% STEADY | 0.28% STEADY |
| Minutes over the line (a day) | 27.00 | 27.50 | 27.25 | 0.91% GAIN | 0.93% LOSS |
| Power-cap request: moves (a day) | 0.00 | 63.50 | 72.50 | 14.17% power given | power given |
| Power-cap request: reversals (a day) | 0.00 | 62.50 | 70.62 | 13.00% power given | power given |
| Power-cap request: travel (a day) | 0.00 | 19.22 | 21.63 | 12.49% power given | power given |
| Omni's own processor (s an hour) | 0.00 | 1.08 | 1.54 | 42.05% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,653.79 | 2,003.40 | 21.14% power given |  |

### Every 30 s

| Gauge | Native | Every 60 s | Every 30 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 133.08 | 131.98 | 132.19 | 0.15% STEADY | 0.67% GAIN |
| Energy per core-hour (kWh) | 0.0357 | 0.0350 | 0.0347 | 0.95% GAIN | 2.88% GAIN |
| Pods waiting for a place (minutes an hour) | 8.18 | 20.88 | 18.59 | 11.00% GAIN | 127.13% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.20 | 1.20 | 1.20 | 0.18% STEADY | 0.04% STEADY |
| 95th percentile response (ms) | 79.94 | 80.33 | 80.22 | 0.14% STEADY | 0.36% STEADY |
| Minutes over the line (a day) | 27.00 | 27.50 | 27.38 | 0.45% STEADY | 1.39% LOSS |
| Power-cap request: moves (a day) | 0.00 | 63.50 | 81.12 | 27.76% power given | power given |
| Power-cap request: reversals (a day) | 0.00 | 62.50 | 79.50 | 27.20% power given | power given |
| Power-cap request: travel (a day) | 0.00 | 19.22 | 24.33 | 26.53% power given | power given |
| Omni's own processor (s an hour) | 0.00 | 1.78 | 2.07 | 16.57% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,653.79 | 1,833.70 | 10.88% power given |  |

### Every 40 s

| Gauge | Native | Every 60 s | Every 40 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 133.08 | 131.98 | 129.84 | 1.62% GAIN | 2.43% GAIN |
| Energy per core-hour (kWh) | 0.0357 | 0.0350 | 0.0345 | 1.45% GAIN | 3.36% GAIN |
| Pods waiting for a place (minutes an hour) | 8.18 | 20.88 | 21.40 | 2.49% LOSS | 161.58% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.20 | 1.20 | 1.20 | 0.00% STEADY | 0.22% STEADY |
| 95th percentile response (ms) | 79.94 | 80.33 | 80.25 | 0.11% STEADY | 0.39% STEADY |
| Minutes over the line (a day) | 27.00 | 27.50 | 27.50 | 0.00% STEADY | 1.85% LOSS |
| Power-cap request: moves (a day) | 0.00 | 63.50 | 71.38 | 12.40% power given | power given |
| Power-cap request: reversals (a day) | 0.00 | 62.50 | 70.25 | 12.40% power given | power given |
| Power-cap request: travel (a day) | 0.00 | 19.22 | 21.67 | 12.70% power given | power given |
| Omni's own processor (s an hour) | 0.00 | 1.08 | 1.19 | 9.78% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,653.79 | 1,742.08 | 5.34% power given |  |

### Every 45 s

| Gauge | Native | Every 60 s | Every 45 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 133.08 | 131.98 | 128.44 | 2.69% GAIN | 3.48% GAIN |
| Energy per core-hour (kWh) | 0.0357 | 0.0350 | 0.0345 | 1.55% GAIN | 3.47% GAIN |
| Pods waiting for a place (minutes an hour) | 8.18 | 20.88 | 18.62 | 10.85% GAIN | 127.52% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.20 | 1.20 | 1.20 | 0.07% STEADY | 0.14% STEADY |
| 95th percentile response (ms) | 79.94 | 80.33 | 80.27 | 0.08% STEADY | 0.41% STEADY |
| Minutes over the line (a day) | 27.00 | 27.50 | 27.50 | 0.00% STEADY | 1.85% LOSS |
| Power-cap request: moves (a day) | 0.00 | 63.50 | 57.88 | 8.86% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 62.50 | 56.75 | 9.20% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 19.22 | 17.61 | 8.38% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.08 | 1.16 | 6.93% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,653.79 | 1,716.85 | 3.81% power given |  |

### Every 50 s

| Gauge | Native | Every 60 s | Every 50 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 133.08 | 131.98 | 133.25 | 0.96% power given | 0.13% STEADY |
| Energy per core-hour (kWh) | 0.0357 | 0.0350 | 0.0349 | 0.22% STEADY | 2.17% GAIN |
| Pods waiting for a place (minutes an hour) | 8.18 | 20.88 | 25.69 | 23.01% LOSS | 213.92% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.20 | 1.20 | 1.21 | 0.14% STEADY | 0.36% STEADY |
| 95th percentile response (ms) | 79.94 | 80.33 | 80.51 | 0.22% STEADY | 0.72% LOSS |
| Minutes over the line (a day) | 27.00 | 27.50 | 27.25 | 0.91% GAIN | 0.93% LOSS |
| Power-cap request: moves (a day) | 0.00 | 63.50 | 84.25 | 32.68% power given | power given |
| Power-cap request: reversals (a day) | 0.00 | 62.50 | 82.75 | 32.40% power given | power given |
| Power-cap request: travel (a day) | 0.00 | 19.22 | 25.31 | 31.67% power given | power given |
| Omni's own processor (s an hour) | 0.00 | 1.08 | 1.12 | 3.88% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,653.79 | 1,694.33 | 2.45% power given |  |

### Every 60 s (the main engine)

| Gauge | Native | Every 60 s | Against native |
|---|---:|---:|---|
| Machine hours (a day) | 133.08 | 131.98 | 0.82% GAIN |
| Energy per core-hour (kWh) | 0.0357 | 0.0350 | 1.95% GAIN |
| Pods waiting for a place (minutes an hour) | 8.18 | 20.88 | 155.21% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.20 | 1.20 | 0.22% STEADY |
| 95th percentile response (ms) | 79.94 | 80.33 | 0.49% STEADY |
| Minutes over the line (a day) | 27.00 | 27.50 | 1.85% LOSS |
| Power-cap request: moves (a day) | 0.00 | 63.50 | power given |
| Power-cap request: reversals (a day) | 0.00 | 62.50 | power given |
| Power-cap request: travel (a day) | 0.00 | 19.22 | power given |
| Omni's own processor (s an hour) | 0.00 | 1.69 |  |
| Reads of the cluster (an hour) | 0.00 | 1,653.79 |  |

### Every 75 s

| Gauge | Native | Every 60 s | Every 75 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 133.08 | 131.98 | 131.21 | 0.59% GAIN | 1.40% GAIN |
| Energy per core-hour (kWh) | 0.0357 | 0.0350 | 0.0350 | 0.13% STEADY | 2.07% GAIN |
| Pods waiting for a place (minutes an hour) | 8.18 | 20.88 | 19.30 | 7.57% GAIN | 135.88% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.20 | 1.20 | 1.20 | 0.22% STEADY | 0.00% STEADY |
| 95th percentile response (ms) | 79.94 | 80.33 | 80.20 | 0.17% STEADY | 0.33% STEADY |
| Minutes over the line (a day) | 27.00 | 27.50 | 27.38 | 0.45% STEADY | 1.39% LOSS |
| Power-cap request: moves (a day) | 0.00 | 63.50 | 53.75 | 15.35% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 62.50 | 52.75 | 15.60% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 19.22 | 16.28 | 15.33% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.78 | 1.66 | 6.31% GAIN |  |
| Reads of the cluster (an hour) | 0.00 | 1,653.79 | 1,621.98 | 1.92% GAIN |  |

### Every 90 s

| Gauge | Native | Every 60 s | Every 90 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 133.08 | 131.98 | 131.29 | 0.53% GAIN | 1.34% GAIN |
| Energy per core-hour (kWh) | 0.0357 | 0.0350 | 0.0350 | 0.06% STEADY | 2.01% GAIN |
| Pods waiting for a place (minutes an hour) | 8.18 | 20.88 | 18.27 | 12.52% GAIN | 123.25% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.20 | 1.20 | 1.20 | 0.11% STEADY | 0.11% STEADY |
| 95th percentile response (ms) | 79.94 | 80.33 | 80.35 | 0.02% STEADY | 0.51% LOSS |
| Minutes over the line (a day) | 27.00 | 27.50 | 27.62 | 0.45% STEADY | 2.31% LOSS |
| Power-cap request: moves (a day) | 0.00 | 63.50 | 46.38 | 26.97% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 62.50 | 45.25 | 27.60% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 19.22 | 14.03 | 27.01% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.71 | 1.60 | 6.07% GAIN |  |
| Reads of the cluster (an hour) | 0.00 | 1,653.79 | 1,599.81 | 3.26% GAIN |  |

### Every 120 s

| Gauge | Native | Every 60 s | Every 120 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 133.08 | 131.98 | 130.93 | 0.80% GAIN | 1.61% GAIN |
| Energy per core-hour (kWh) | 0.0357 | 0.0350 | 0.0352 | 0.66% power given | 1.30% GAIN |
| Pods waiting for a place (minutes an hour) | 8.18 | 20.88 | 14.01 | 32.91% GAIN | 71.22% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.20 | 1.20 | 1.20 | 0.11% STEADY | 0.11% STEADY |
| 95th percentile response (ms) | 79.94 | 80.33 | 80.08 | 0.31% STEADY | 0.18% STEADY |
| Minutes over the line (a day) | 27.00 | 27.50 | 27.12 | 1.36% GAIN | 0.46% STEADY |
| Power-cap request: moves (a day) | 0.00 | 63.50 | 29.62 | 53.35% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 62.50 | 28.50 | 54.40% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 19.22 | 8.51 | 55.75% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.71 | 1.58 | 7.37% GAIN |  |
| Reads of the cluster (an hour) | 0.00 | 1,653.79 | 1,558.96 | 5.73% GAIN |  |

Counts over all seeds, by beat: decisions 5 s 138,240, 10 s 69,120, 15 s 46,080, 20 s 34,560, 30 s 23,040, 40 s 17,280, 45 s 15,360, 50 s 13,824, 60 s 11,520, 75 s 9,216, 90 s 7,680, 120 s 5,760; machines_parked 5 s 1,654, 10 s 1,706, 15 s 1,712, 20 s 1,571, 30 s 1,509, 40 s 1,304, 45 s 1,664, 50 s 1,714, 60 s 1,486, 75 s 1,056, 90 s 886, 120 s 722; errors 5 s 0, 10 s 0, 15 s 0, 20 s 0, 30 s 0, 40 s 0, 45 s 0, 50 s 0, 60 s 0, 75 s 0, 90 s 0, 120 s 0; steps_allowed 5 s 66, 10 s 67, 15 s 73, 20 s 50, 30 s 62, 40 s 68, 45 s 62, 50 s 48, 60 s 54, 75 s 50, 90 s 63, 120 s 56; steps_refused 5 s 78, 10 s 76, 15 s 68, 20 s 76, 30 s 75, 40 s 76, 45 s 79, 50 s 74, 60 s 78, 75 s 83, 90 s 82, 120 s 85; trials_abandoned 5 s 127, 10 s 137, 15 s 259, 20 s 159, 30 s 151, 40 s 147, 45 s 97, 50 s 199, 60 s 125, 75 s 90, 90 s 63, 120 s 17

## The kind benchmark's setting

The kind benchmark's setting: the compass law at the max, every autoscaler sensed.

What each beat buys and what it costs, against native (the value, then the word):

| Beat | Reads a day | Omni's own processor (s an hour) | Pods waiting for a place (minutes an hour) | 95th percentile response (ms) | Minutes over the line (a day) | Pod autoscaler short of its target (minutes an hour) | Machine hours (a day) | Energy per core-hour (kWh) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| native | | | 8.18 | 79.94 | 27.00 | 1.20 | 133.08 | 0.0357 |
| every 5 s | 86,412 | 5.55 | 28.55 LOSS | 76.88 GAIN | 19.38 GAIN | 1.12 GAIN | 149.67 power given | 0.0385 power given |
| every 10 s | 60,942 | 3.43 | 28.80 LOSS | 76.85 GAIN | 19.38 GAIN | 1.12 GAIN | 149.17 power given | 0.0384 power given |
| every 15 s | 52,490 | 2.66 | 33.51 LOSS | 76.93 GAIN | 20.25 GAIN | 1.14 GAIN | 151.78 power given | 0.0389 power given |
| every 20 s | 48,154 | 1.55 | 29.80 LOSS | 76.83 GAIN | 20.25 GAIN | 1.13 GAIN | 150.15 power given | 0.0386 power given |
| every 30 s | 43,869 | 2.01 | 34.09 LOSS | 76.99 GAIN | 21.25 GAIN | 1.16 GAIN | 151.78 power given | 0.0389 power given |
| every 40 s | 41,460 | 1.19 | 32.91 LOSS | 76.83 GAIN | 20.62 GAIN | 1.15 GAIN | 151.74 power given | 0.0389 power given |
| every 45 s | 41,090 | 1.18 | 32.65 LOSS | 77.04 GAIN | 21.62 GAIN | 1.17 GAIN | 151.26 power given | 0.0388 power given |
| every 50 s | 40,011 | 1.12 | 33.62 LOSS | 76.95 GAIN | 22.38 GAIN | 1.17 GAIN | 151.94 power given | 0.0389 power given |
| every 60 s (the main engine) | 39,444 | 1.58 | 31.96 LOSS | 77.18 GAIN | 23.75 GAIN | 1.19 GAIN | 151.29 power given | 0.0388 power given |
| every 75 s | 38,836 | 1.66 | 29.15 LOSS | 77.17 GAIN | 21.75 GAIN | 1.19 GAIN | 149.50 power given | 0.0384 power given |
| every 90 s | 38,254 | 1.52 | 28.10 LOSS | 77.01 GAIN | 22.62 GAIN | 1.20 STEADY | 148.78 power given | 0.0383 power given |
| every 120 s | 37,536 | 1.47 | 22.51 LOSS | 76.99 GAIN | 22.88 GAIN | 1.24 LOSS | 148.18 power given | 0.0382 power given |

Each beat against the main engine's 60 s:

| Beat | Reads a day | Omni's own processor | Pods waiting for a place (minutes an hour) | 95th percentile response (ms) | Minutes over the line (a day) | Pod autoscaler short of its target (minutes an hour) | Machine hours (a day) | Energy per core-hour (kWh) |
|---|---|---|---|---|---|---|---|---|
| every 5 s | 119.08% power given | 250.98% power given | 10.66% GAIN | 0.39% STEADY | 18.42% GAIN | 5.78% GAIN | 1.07% GAIN | 0.66% GAIN |
| every 10 s | 54.50% power given | 117.14% power given | 9.89% GAIN | 0.44% STEADY | 18.42% GAIN | 6.00% GAIN | 1.40% GAIN | 0.92% GAIN |
| every 15 s | 33.07% power given | 68.11% power given | 4.84% LOSS | 0.33% STEADY | 14.74% GAIN | 4.13% GAIN | 0.33% STEADY | 0.30% STEADY |
| every 20 s | 22.08% power given | 43.17% power given | 6.75% GAIN | 0.46% STEADY | 14.74% GAIN | 5.05% GAIN | 0.76% GAIN | 0.44% STEADY |
| every 30 s | 11.22% power given | 17.25% power given | 6.65% LOSS | 0.26% STEADY | 10.53% GAIN | 2.52% GAIN | 0.32% STEADY | 0.29% STEADY |
| every 40 s | 5.11% power given | 9.93% power given | 2.97% LOSS | 0.46% STEADY | 13.16% GAIN | 2.93% GAIN | 0.30% STEADY | 0.25% STEADY |
| every 45 s | 4.17% power given | 8.85% power given | 2.17% LOSS | 0.19% STEADY | 8.95% GAIN | 1.68% GAIN | 0.02% STEADY | 0.05% STEADY |
| every 50 s | 1.44% power given | 3.84% power given | 5.18% LOSS | 0.31% STEADY | 5.79% GAIN | 1.72% GAIN | 0.43% STEADY | 0.33% STEADY |
| every 75 s | 1.54% GAIN | 3.07% STEADY | 8.79% GAIN | 0.01% STEADY | 8.42% GAIN | 0.11% STEADY | 1.18% GAIN | 0.84% GAIN |
| every 90 s | 3.02% GAIN | 12.37% GAIN | 12.07% GAIN | 0.23% STEADY | 4.74% GAIN | 1.46% LOSS | 1.66% GAIN | 1.21% GAIN |
| every 120 s | 4.84% GAIN | 15.56% GAIN | 29.56% GAIN | 0.25% STEADY | 3.68% GAIN | 4.17% LOSS | 2.06% GAIN | 1.35% GAIN |

### Every 5 s

| Gauge | Native | Every 60 s | Every 5 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 133.08 | 151.29 | 149.67 | 1.07% GAIN | 12.47% power given |
| Energy per core-hour (kWh) | 0.0357 | 0.0388 | 0.0385 | 0.66% GAIN | 7.86% power given |
| Pods waiting for a place (minutes an hour) | 8.18 | 31.96 | 28.55 | 10.66% GAIN | 248.94% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.20 | 1.19 | 1.12 | 5.78% GAIN | 6.97% GAIN |
| 95th percentile response (ms) | 79.94 | 77.18 | 76.88 | 0.39% STEADY | 3.82% GAIN |
| Minutes over the line (a day) | 27.00 | 23.75 | 19.38 | 18.42% GAIN | 28.24% GAIN |
| Power-cap request: moves (a day) | 0.00 | 33.25 | 33.62 | 1.13% power given | power given |
| Power-cap request: reversals (a day) | 0.00 | 32.25 | 32.62 | 1.16% power given | power given |
| Power-cap request: travel (a day) | 0.00 | 10.14 | 10.26 | 1.13% power given | power given |
| Omni's own processor (s an hour) | 0.00 | 1.58 | 5.55 | 250.98% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,643.50 | 3,600.50 | 119.08% power given |  |

### Every 10 s

| Gauge | Native | Every 60 s | Every 10 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 133.08 | 151.29 | 149.17 | 1.40% GAIN | 12.10% power given |
| Energy per core-hour (kWh) | 0.0357 | 0.0388 | 0.0384 | 0.92% GAIN | 7.58% power given |
| Pods waiting for a place (minutes an hour) | 8.18 | 31.96 | 28.80 | 9.89% GAIN | 251.95% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.20 | 1.19 | 1.12 | 6.00% GAIN | 7.18% GAIN |
| 95th percentile response (ms) | 79.94 | 77.18 | 76.85 | 0.44% STEADY | 3.87% GAIN |
| Minutes over the line (a day) | 27.00 | 23.75 | 19.38 | 18.42% GAIN | 28.24% GAIN |
| Power-cap request: moves (a day) | 0.00 | 33.25 | 32.88 | 1.13% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 32.25 | 31.88 | 1.16% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 10.14 | 10.03 | 1.13% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.58 | 3.43 | 117.14% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,643.50 | 2,539.23 | 54.50% power given |  |

### Every 15 s

| Gauge | Native | Every 60 s | Every 15 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 133.08 | 151.29 | 151.78 | 0.33% STEADY | 14.06% power given |
| Energy per core-hour (kWh) | 0.0357 | 0.0388 | 0.0389 | 0.30% STEADY | 8.91% power given |
| Pods waiting for a place (minutes an hour) | 8.18 | 31.96 | 33.51 | 4.84% LOSS | 309.47% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.20 | 1.19 | 1.14 | 4.13% GAIN | 5.34% GAIN |
| 95th percentile response (ms) | 79.94 | 77.18 | 76.93 | 0.33% STEADY | 3.76% GAIN |
| Minutes over the line (a day) | 27.00 | 23.75 | 20.25 | 14.74% GAIN | 25.00% GAIN |
| Power-cap request: moves (a day) | 0.00 | 33.25 | 33.38 | 0.38% STEADY | power given |
| Power-cap request: reversals (a day) | 0.00 | 32.25 | 32.38 | 0.39% STEADY | power given |
| Power-cap request: travel (a day) | 0.00 | 10.14 | 10.18 | 0.38% STEADY | power given |
| Omni's own processor (s an hour) | 0.00 | 1.58 | 2.66 | 68.11% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,643.50 | 2,187.08 | 33.07% power given |  |

### Every 20 s

| Gauge | Native | Every 60 s | Every 20 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 133.08 | 151.29 | 150.15 | 0.76% GAIN | 12.83% power given |
| Energy per core-hour (kWh) | 0.0357 | 0.0388 | 0.0386 | 0.44% STEADY | 8.10% power given |
| Pods waiting for a place (minutes an hour) | 8.18 | 31.96 | 29.80 | 6.75% GAIN | 264.21% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.20 | 1.19 | 1.13 | 5.05% GAIN | 6.25% GAIN |
| 95th percentile response (ms) | 79.94 | 77.18 | 76.83 | 0.46% STEADY | 3.89% GAIN |
| Minutes over the line (a day) | 27.00 | 23.75 | 20.25 | 14.74% GAIN | 25.00% GAIN |
| Power-cap request: moves (a day) | 0.00 | 33.25 | 32.38 | 2.63% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 32.25 | 31.38 | 2.71% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 10.14 | 9.87 | 2.63% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.08 | 1.55 | 43.17% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,643.50 | 2,006.43 | 22.08% power given |  |

### Every 30 s

| Gauge | Native | Every 60 s | Every 30 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 133.08 | 151.29 | 151.78 | 0.32% STEADY | 14.05% power given |
| Energy per core-hour (kWh) | 0.0357 | 0.0388 | 0.0389 | 0.29% STEADY | 8.90% power given |
| Pods waiting for a place (minutes an hour) | 8.18 | 31.96 | 34.09 | 6.65% LOSS | 316.55% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.20 | 1.19 | 1.16 | 2.52% GAIN | 3.75% GAIN |
| 95th percentile response (ms) | 79.94 | 77.18 | 76.99 | 0.26% STEADY | 3.69% GAIN |
| Minutes over the line (a day) | 27.00 | 23.75 | 21.25 | 10.53% GAIN | 21.30% GAIN |
| Power-cap request: moves (a day) | 0.00 | 33.25 | 33.50 | 0.75% power given | power given |
| Power-cap request: reversals (a day) | 0.00 | 32.25 | 32.50 | 0.78% power given | power given |
| Power-cap request: travel (a day) | 0.00 | 10.14 | 10.22 | 0.75% power given | power given |
| Omni's own processor (s an hour) | 0.00 | 1.72 | 2.01 | 17.25% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,643.50 | 1,827.86 | 11.22% power given |  |

### Every 40 s

| Gauge | Native | Every 60 s | Every 40 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 133.08 | 151.29 | 151.74 | 0.30% STEADY | 14.03% power given |
| Energy per core-hour (kWh) | 0.0357 | 0.0388 | 0.0389 | 0.25% STEADY | 8.85% power given |
| Pods waiting for a place (minutes an hour) | 8.18 | 31.96 | 32.91 | 2.97% LOSS | 302.17% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.20 | 1.19 | 1.15 | 2.93% GAIN | 4.15% GAIN |
| 95th percentile response (ms) | 79.94 | 77.18 | 76.83 | 0.46% STEADY | 3.89% GAIN |
| Minutes over the line (a day) | 27.00 | 23.75 | 20.62 | 13.16% GAIN | 23.61% GAIN |
| Power-cap request: moves (a day) | 0.00 | 33.25 | 32.75 | 1.50% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 32.25 | 31.75 | 1.55% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 10.14 | 9.99 | 1.50% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.08 | 1.19 | 9.93% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,643.50 | 1,727.52 | 5.11% power given |  |

### Every 45 s

| Gauge | Native | Every 60 s | Every 45 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 133.08 | 151.29 | 151.26 | 0.02% STEADY | 13.66% power given |
| Energy per core-hour (kWh) | 0.0357 | 0.0388 | 0.0388 | 0.05% STEADY | 8.64% power given |
| Pods waiting for a place (minutes an hour) | 8.18 | 31.96 | 32.65 | 2.17% LOSS | 299.05% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.20 | 1.19 | 1.17 | 1.68% GAIN | 2.92% GAIN |
| 95th percentile response (ms) | 79.94 | 77.18 | 77.04 | 0.19% STEADY | 3.62% GAIN |
| Minutes over the line (a day) | 27.00 | 23.75 | 21.62 | 8.95% GAIN | 19.91% GAIN |
| Power-cap request: moves (a day) | 0.00 | 33.25 | 32.50 | 2.26% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 32.25 | 31.50 | 2.33% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 10.14 | 9.91 | 2.26% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.08 | 1.18 | 8.85% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,643.50 | 1,712.06 | 4.17% power given |  |

### Every 50 s

| Gauge | Native | Every 60 s | Every 50 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 133.08 | 151.29 | 151.94 | 0.43% STEADY | 14.17% power given |
| Energy per core-hour (kWh) | 0.0357 | 0.0388 | 0.0389 | 0.33% STEADY | 8.94% power given |
| Pods waiting for a place (minutes an hour) | 8.18 | 31.96 | 33.62 | 5.18% LOSS | 310.82% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.20 | 1.19 | 1.17 | 1.72% GAIN | 2.96% GAIN |
| 95th percentile response (ms) | 79.94 | 77.18 | 76.95 | 0.31% STEADY | 3.74% GAIN |
| Minutes over the line (a day) | 27.00 | 23.75 | 22.38 | 5.79% GAIN | 17.13% GAIN |
| Power-cap request: moves (a day) | 0.00 | 33.25 | 33.25 | 0.00% STEADY | power given |
| Power-cap request: reversals (a day) | 0.00 | 32.25 | 32.25 | 0.00% STEADY | power given |
| Power-cap request: travel (a day) | 0.00 | 10.14 | 10.14 | 0.00% STEADY | power given |
| Omni's own processor (s an hour) | 0.00 | 1.08 | 1.12 | 3.84% power given |  |
| Reads of the cluster (an hour) | 0.00 | 1,643.50 | 1,667.14 | 1.44% power given |  |

### Every 60 s (the main engine)

| Gauge | Native | Every 60 s | Against native |
|---|---:|---:|---|
| Machine hours (a day) | 133.08 | 151.29 | 13.69% power given |
| Energy per core-hour (kWh) | 0.0357 | 0.0388 | 8.58% power given |
| Pods waiting for a place (minutes an hour) | 8.18 | 31.96 | 290.57% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.20 | 1.19 | 1.26% GAIN |
| 95th percentile response (ms) | 79.94 | 77.18 | 3.44% GAIN |
| Minutes over the line (a day) | 27.00 | 23.75 | 12.04% GAIN |
| Power-cap request: moves (a day) | 0.00 | 33.25 | power given |
| Power-cap request: reversals (a day) | 0.00 | 32.25 | power given |
| Power-cap request: travel (a day) | 0.00 | 10.14 | power given |
| Omni's own processor (s an hour) | 0.00 | 1.58 |  |
| Reads of the cluster (an hour) | 0.00 | 1,643.50 |  |

### Every 75 s

| Gauge | Native | Every 60 s | Every 75 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 133.08 | 151.29 | 149.50 | 1.18% GAIN | 12.34% power given |
| Energy per core-hour (kWh) | 0.0357 | 0.0388 | 0.0384 | 0.84% GAIN | 7.67% power given |
| Pods waiting for a place (minutes an hour) | 8.18 | 31.96 | 29.15 | 8.79% GAIN | 256.23% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.20 | 1.19 | 1.19 | 0.11% STEADY | 1.37% GAIN |
| 95th percentile response (ms) | 79.94 | 77.18 | 77.17 | 0.01% STEADY | 3.46% GAIN |
| Minutes over the line (a day) | 27.00 | 23.75 | 21.75 | 8.42% GAIN | 19.44% GAIN |
| Power-cap request: moves (a day) | 0.00 | 33.25 | 29.75 | 10.53% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 32.25 | 28.75 | 10.85% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 10.14 | 9.07 | 10.53% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.72 | 1.66 | 3.07% STEADY |  |
| Reads of the cluster (an hour) | 0.00 | 1,643.50 | 1,618.17 | 1.54% GAIN |  |

### Every 90 s

| Gauge | Native | Every 60 s | Every 90 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 133.08 | 151.29 | 148.78 | 1.66% GAIN | 11.80% power given |
| Energy per core-hour (kWh) | 0.0357 | 0.0388 | 0.0383 | 1.21% GAIN | 7.27% power given |
| Pods waiting for a place (minutes an hour) | 8.18 | 31.96 | 28.10 | 12.07% GAIN | 243.43% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.20 | 1.19 | 1.20 | 1.46% LOSS | 0.18% STEADY |
| 95th percentile response (ms) | 79.94 | 77.18 | 77.01 | 0.23% STEADY | 3.66% GAIN |
| Minutes over the line (a day) | 27.00 | 23.75 | 22.62 | 4.74% GAIN | 16.20% GAIN |
| Power-cap request: moves (a day) | 0.00 | 33.25 | 28.00 | 15.79% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 32.25 | 27.00 | 16.28% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 10.14 | 8.54 | 15.79% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.74 | 1.52 | 12.37% GAIN |  |
| Reads of the cluster (an hour) | 0.00 | 1,643.50 | 1,593.94 | 3.02% GAIN |  |

### Every 120 s

| Gauge | Native | Every 60 s | Every 120 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| Machine hours (a day) | 133.08 | 151.29 | 148.18 | 2.06% GAIN | 11.35% power given |
| Energy per core-hour (kWh) | 0.0357 | 0.0388 | 0.0382 | 1.35% GAIN | 7.12% power given |
| Pods waiting for a place (minutes an hour) | 8.18 | 31.96 | 22.51 | 29.56% GAIN | 175.13% LOSS |
| Pod autoscaler short of its target (minutes an hour) | 1.20 | 1.19 | 1.24 | 4.17% LOSS | 2.85% LOSS |
| 95th percentile response (ms) | 79.94 | 77.18 | 76.99 | 0.25% STEADY | 3.69% GAIN |
| Minutes over the line (a day) | 27.00 | 23.75 | 22.88 | 3.68% GAIN | 15.28% GAIN |
| Power-cap request: moves (a day) | 0.00 | 33.25 | 21.75 | 34.59% GAIN | power given |
| Power-cap request: reversals (a day) | 0.00 | 32.25 | 20.75 | 35.66% GAIN | power given |
| Power-cap request: travel (a day) | 0.00 | 10.14 | 6.63 | 34.59% GAIN | power given |
| Omni's own processor (s an hour) | 0.00 | 1.74 | 1.47 | 15.56% GAIN |  |
| Reads of the cluster (an hour) | 0.00 | 1,643.50 | 1,564.00 | 4.84% GAIN |  |

Counts over all seeds, by beat: decisions 5 s 138,240, 10 s 69,120, 15 s 46,080, 20 s 34,560, 30 s 23,040, 40 s 17,280, 45 s 15,360, 50 s 13,824, 60 s 11,520, 75 s 9,216, 90 s 7,680, 120 s 5,760; machines_parked 5 s 341, 10 s 357, 15 s 338, 20 s 355, 30 s 339, 40 s 290, 45 s 375, 50 s 423, 60 s 329, 75 s 196, 90 s 190, 120 s 119; errors 5 s 0, 10 s 0, 15 s 0, 20 s 0, 30 s 0, 40 s 0, 45 s 0, 50 s 0, 60 s 0, 75 s 0, 90 s 0, 120 s 0; steps_allowed 5 s 80, 10 s 65, 15 s 68, 20 s 57, 30 s 72, 40 s 58, 45 s 64, 50 s 57, 60 s 56, 75 s 57, 90 s 50, 120 s 52; steps_refused 5 s 87, 10 s 90, 15 s 88, 20 s 89, 30 s 86, 40 s 89, 45 s 88, 50 s 89, 60 s 85, 75 s 89, 90 s 86, 120 s 85; trials_abandoned 5 s 15, 10 s 7, 15 s 12, 20 s 18, 30 s 17, 40 s 12, 45 s 15, 50 s 17, 60 s 21, 75 s 13, 90 s 14, 120 s 14

## The first reading of every 90 and 120 s, before the fix

The 90 and 120 s beats as first run, before the cruise fix (docs/OMNI_V17.md, section 3): the cruise wait (120 s) rounded to one decision at those beats, so one reading with a pod waiting put every machine in service and one empty reading let them go. Kept here as the reading that caught the fault; the beats above are read from the corrected rule.

From `the first 90 and 120 s run of 22 October, on omni-v16's rule`; its native and 60 s read the same as this page's, seed by seed.

The cloud's setting, against native and against 60 s:

| Beat | Pods waiting for a place (minutes an hour) | 95th percentile response (ms) | Minutes over the line (a day) | Pod autoscaler short of its target (minutes an hour) | Machine hours (a day) | Energy per core-hour (kWh) |
|---|---|---|---|---|---|---|
| every 90 s, first | 18.27: 123.25% STEADY; 12.52% STEADY | 80.35: 0.51% STEADY; 0.02% STEADY | 27.62: 2.31% STEADY; 0.45% STEADY | 1.20: 0.11% STEADY; 0.11% STEADY | 131.29: 1.34% GAIN; 0.53% STEADY | 0.0350: 2.01% GAIN; 0.06% STEADY |
| every 120 s, first | 14.01: 71.22% STEADY; 32.91% STEADY | 80.08: 0.18% STEADY; 0.31% STEADY | 27.12: 0.46% STEADY; 1.36% STEADY | 1.20: 0.11% STEADY; 0.11% STEADY | 130.93: 1.61% STEADY; 0.80% STEADY | 0.0352: 1.30% STEADY; 0.66% STEADY |

The kind benchmark's setting, against native and against 60 s:

| Beat | Pods waiting for a place (minutes an hour) | 95th percentile response (ms) | Minutes over the line (a day) | Pod autoscaler short of its target (minutes an hour) | Machine hours (a day) | Energy per core-hour (kWh) |
|---|---|---|---|---|---|---|
| every 90 s, first | 12.98: 58.65% STEADY; 59.38% GAIN | 65.28: 18.33% GAIN; 15.42% GAIN | 6.75: 75.00% GAIN; 71.58% GAIN | 1.11: 7.91% GAIN; 6.73% GAIN | 177.23: 33.18% power given; 17.15% power given | 0.0434: 21.44% power given; 11.84% power given |
| every 120 s, first | 9.36: 14.40% STEADY; 70.71% GAIN | 60.75: 24.00% GAIN; 21.29% GAIN | 6.75: 75.00% GAIN; 71.58% GAIN | 1.10: 8.70% GAIN; 7.53% STEADY | 183.62: 37.98% power given; 21.37% power given | 0.0443: 24.00% power given; 14.20% power given |

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
