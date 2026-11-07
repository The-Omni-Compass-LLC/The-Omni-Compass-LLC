# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C confirmation

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **confirmed better** or **confirmed WORSE**; a run whose interval includes zero reads **no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed transactions: any increase in any run is WORSE. Every row is shown, losses included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 38013313943 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 3 |
| B | 38013319893 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 3 |
| C | 38013324861 | `3aac0ab7d384` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 25,799, 26,100, 16,340 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 11,348 | 11,350 | +0.0% (-0.0 to +0.1) | -0.1% (-0.4 to +0.2) | +0.0% (-0.2 to +0.2) | no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 11,351 | 11,351 | -0.0% (-0.1 to +0.1) | -0.0% (-0.2 to +0.1) | +0.0% (-0.2 to +0.2) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms, lag included) | 2 | 1.67 | -16.3% (-105.1 to +72.5) | +21.4% (-7.9 to +50.7) | +6.6% (-15.1 to +28.3) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 6.38 | 5.64 | -11.6% (-65.1 to +41.9) | +32.6% (-11.5 to +76.7) | +14.7% (-29.2 to +58.5) | no difference beyond the noise (3 of 3 runs) |
| latency, median (ms) | 0.252 | 0.251 | -0.1% (-2.2 to +1.9) | +0.4% (-0.6 to +1.4) | +0.5% (-2.1 to +3.0) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.622 | 0.539 | -13.3% (-83.0 to +56.4) | +25.6% (-33.5 to +84.8) | +1.5% (-18.6 to +21.6) | no difference beyond the noise (3 of 3 runs) |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.6 | 17.6 | -10.6% (-18.8 to -2.5) | -10.7% (-19.3 to -2.1) | -6.3% (-12.3 to -0.3) | **confirmed better** |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.43 | 0.43 | +0.0% (-2.2 to +2.2) | +0.1% (-0.2 to +0.4) | +0.8% (-3.0 to +4.6) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 739.3 | 738.9 | -0.1% (-2.4 to +2.3) | +0.1% (-0.1 to +0.3) | +0.9% (-3.7 to +5.5) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 0.145 | 0.145 | -0.1% (-2.4 to +2.3) | +0.2% (-0.3 to +0.7) | +0.9% (-3.9 to +5.6) | no difference beyond the noise (3 of 3 runs) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.93 | 3.58 | +22.3% (+14.0 to +30.6) | +21.4% (+19.0 to +23.9) | +30.1% (+27.1 to +33.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.2 | -9.0% (-16.3 to -1.7) | -10.6% (-11.8 to -9.3) | -5.0% (-5.0 to -4.9) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 13 to 20 (12 trials, 7 allowed, 4 refused); acting: 13 to 20 (12 trials, 7 allowed, 4 refused); acting: 18 to 20 (10 trials, 2 allowed, 5 refused); run B: acting: 15 to 20 (10 trials, 5 allowed, 4 refused); acting: 13 to 20 (12 trials, 7 allowed, 4 refused); acting: 13 to 20 (12 trials, 7 allowed, 4 refused); run C: acting: 19 to 20 (7 trials, 1 allowed, 6 refused); acting: 19 to 20 (7 trials, 1 allowed, 6 refused); acting: 19 to 20 (7 trials, 1 allowed, 6 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 7,549, 5,431, 3,602 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 3,124 | 3,133 | +0.3% (-5.3 to +5.9) | +0.0% (-2.6 to +2.7) | -0.1% (-0.9 to +0.8) | no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 3,322 | 3,319 | -0.1% (-0.5 to +0.3) | -0.1% (-0.2 to +0.0) | -0.1% (-0.6 to +0.5) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms, lag included) | 90.7 | 111.5 | +22.9% (-253.8 to +299.6) | -50.8% (-310.7 to +209.0) | +13.9% (-42.9 to +70.7) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 585.4 | 559.2 | -4.5% (-31.4 to +22.5) | -3.2% (-66.9 to +60.6) | -0.4% (-45.2 to +44.4) | no difference beyond the noise (3 of 3 runs) |
| latency, median (ms) | 0.707 | 0.711 | +0.7% (-3.7 to +5.0) | +0.7% (-3.2 to +4.6) | +2.1% (-0.3 to +4.5) | no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 21.6 | 20.8 | -3.5% (-87.5 to +80.6) | -0.3% (-94.5 to +93.8) | +2.0% (-48.3 to +52.3) | no difference beyond the noise (3 of 3 runs) |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 20.0 | 18.6 | -6.9% (-11.4 to -2.4) | -12.2% (-32.9 to +8.5) | -5.3% (-5.8 to -4.8) | no difference beyond the noise (1 of 3 runs) |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.353 | 0.356 | +0.7% (-4.1 to +5.6) | +0.7% (-5.0 to +6.5) | +2.6% (-1.4 to +6.6) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 602.1 | 606.2 | +0.7% (-4.1 to +5.4) | +0.7% (-5.2 to +6.5) | +2.8% (-1.6 to +7.2) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 0.428 | 0.43 | +0.4% (-3.3 to +4.1) | +0.7% (-7.9 to +9.2) | +2.9% (-2.0 to +7.8) | no difference beyond the noise (3 of 3 runs) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.87 | 1.48 | +69.6% (+61.5 to +77.7) | +79.7% (+61.6 to +97.7) | +85.9% (+79.6 to +92.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.8 | -6.2% (-10.4 to -2.0) | -11.4% (-29.9 to +7.1) | -4.6% (-5.3 to -3.9) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 16 to 20 (21 trials, 4 allowed, 3 refused); acting: 17 to 20 (28 trials, 3 allowed, 2 refused); acting: 16 to 20 (21 trials, 4 allowed, 4 refused); run B: acting: 18 to 20 (17 trials, 2 allowed, 4 refused); acting: 14 to 20 (24 trials, 6 allowed, 3 refused); acting: 12 to 20 (26 trials, 8 allowed, 1 refused); run C: acting: 19 to 20 (15 trials, 1 allowed, 5 refused); acting: 18 to 20 (16 trials, 2 allowed, 4 refused); acting: 19 to 20 (15 trials, 1 allowed, 5 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 2,530, 2,705, 1,962 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,107 | 1,112 | +0.4% (-2.1 to +2.9) | +0.7% (-2.7 to +4.1) | +0.1% (-2.0 to +2.2) | no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 1,114 | 1,115 | +0.1% (-0.5 to +0.7) | +0.2% (-0.2 to +0.5) | -0.1% (-0.7 to +0.5) | no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms, lag included) | 3.93 | 3.82 | -2.8% (-52.7 to +47.0) | -14.6% (-86.7 to +57.5) | -1.3% (-37.9 to +35.3) | no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 38.9 | 15.9 | -59.1% (-427.4 to +309.3) | -70.4% (-406.0 to +265.1) | -33.3% (-257.2 to +190.6) | no difference beyond the noise (3 of 3 runs) |
| latency, median (ms) | 1.39 | 1.41 | +1.2% (+0.1 to +2.4) | -0.6% (-2.2 to +0.9) | -0.3% (-4.3 to +3.7) | no difference beyond the noise (2 of 3 runs) |
| latency, mean (ms) | 2.48 | 2.17 | -12.4% (-151.2 to +126.4) | -22.4% (-158.6 to +113.7) | -2.6% (-125.7 to +120.5) | no difference beyond the noise (3 of 3 runs) |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.2 | 17.2 | -10.7% (-22.9 to +1.5) | -7.3% (-11.9 to -2.6) | -8.0% (-9.2 to -6.7) | no difference beyond the noise (1 of 3 runs) |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.263 | 0.267 | +1.4% (-0.0 to +2.8) | -0.4% (-1.9 to +1.0) | -0.5% (-5.7 to +4.6) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 459.9 | 466.2 | +1.4% (-0.0 to +2.7) | -0.4% (-1.9 to +1.0) | -0.6% (-6.1 to +5.0) | no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 0.923 | 0.932 | +1.0% (-2.7 to +4.6) | -1.1% (-5.3 to +3.0) | -0.6% (-8.3 to +7.0) | no difference beyond the noise (3 of 3 runs) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.691 | 1.31 | +89.1% (+85.7 to +92.6) | +82.6% (+80.8 to +84.3) | +93.9% (+87.7 to +100.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.7 | -11.6% (-14.3 to -8.9) | -7.4% (-12.5 to -2.3) | -5.2% (-5.3 to -5.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 13 to 20 (13 trials, 7 allowed, 4 refused); acting: 13 to 20 (14 trials, 7 allowed, 4 refused); acting: 13 to 20 (12 trials, 7 allowed, 4 refused); run B: acting: 17 to 20 (10 trials, 3 allowed, 5 refused); acting: 15 to 20 (13 trials, 5 allowed, 4 refused); acting: 14 to 20 (13 trials, 6 allowed, 4 refused); run C: acting: 19 to 20 (7 trials, 1 allowed, 6 refused); acting: 19 to 20 (7 trials, 1 allowed, 6 refused); acting: 19 to 20 (7 trials, 1 allowed, 6 refused).

**Across 3 workloads: 1 gauge-rows confirmed better, 0 confirmed worse, 0 where the runs disagree.**

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
