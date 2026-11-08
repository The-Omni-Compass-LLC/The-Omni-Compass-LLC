# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 500 copies: native | The spine, the muscles every stack runs on, 500 copies: omni | Compute / AI / Cloud, 500 copies: native | Compute / AI / Cloud, 500 copies: omni | Physics / Robotics / Autonomous, 500 copies: native | Physics / Robotics / Autonomous, 500 copies: omni | Energy / Facility / Industrial, 500 copies: native | Energy / Facility / Industrial, 500 copies: omni | Distribution / Specialized, 500 copies: native | Distribution / Specialized, 500 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3035 | 3168 | 4257 | 4503 | 2276 | 2855 | 1193 | 5131 | 4456 | 3318 |
| response time (ms), 99th percentile | 4551 | 5629 | 5442 | 7083 | 3732 | 4700 | 1938 | 6011 | 6071 | 5118 |
| time over the response line (% of samples) | 43.25 | 53.23 | 47.56 | 69.27 | 42.86 | 33.91 | 16.25 | 52.98 | 59.57 | 44.31 |
| failed requests (%) | 35.22 | 43.93 | 37.7 | 55.25 | 33.47 | 21.8 | 0 | 44.48 | 47.72 | 35.03 |
| HPA replicas, mean | 9.893 | 15.61 | 9.892 | 12.85 | 9.888 | 14.86 | 9.87 | 13.82 | 9.928 | 15 |
| pods started | 5.6 | 12 | 5.6 | 9.8 | 5.8 | 13.25 | 6.5 | 9.667 | 5 | 15.2 |
| worker nodes in service, mean | 6 | 6 | 6 | 5.998 | 6 | 6 | 6 | 6 | 6 | 5.998 |
| energy, parked workers still on at idle power (Wh, declared model) | 1366 | 1377 | 1366 | 1392 | 1372 | 1364 | 1362 | 1368 | 1381 | 1375 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1366 | 1377 | 1366 | 1392 | 1372 | 1364 | 1362 | 1368 | 1381 | 1375 |
| CPU used with Omni's own (cores), mean | 2.314 | 2.506 | 2.312 | 2.696 | 2.393 | 2.32 | 2.24 | 2.384 | 2.499 | 2.479 |
| host CPU busy, the real machine under kind (%) | 68.05 | 76.97 | 70.4 | 87.27 | 71.65 | 74.73 | 67.14 | 78.29 | 74.56 | 79.59 |
| organism work | 1.044e+13 | 1.044e+13 | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 3.317e+13 | 3.317e+13 | 1.082e+13 | 1.082e+13 |
| organism energy (J) | 6.905e+12 | 6.909e+12 | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 5.512e+15 | 5.512e+15 | 2.854e+13 | 2.855e+13 |
| organism time over the line (% of steps) | 2.335 | 2.205 | 1.943 | 1.874 | 4.602 | 4.511 | 1.469 | 1.382 | 2.451 | 2.367 |
| organism work per energy | 1.511 | 1.511 | 1.375 | 1.374 | 1.116 | 1.115 | 0.006018 | 0.006018 | 0.3789 | 0.3788 |
| organism behind its window (s) | 2.14 | 2.75 | 4.72 | 5.86 | 3.08 | 4.125 | 3.45 | 4.9 | 4.14 | 4.98 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 500 copies: ONE REPETITION

1 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 246.6 | 5209 | +2012.7% |  | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 373.1 | 9734 | +2508.8% |  | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 0.2621 | 77.26 | +29373.1% |  | STEADY, inside the noise (up) |
| failed requests (%) | 0 | 65.48 | +65.5 |  | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.841 | 15.79 | +60.4% |  | STEADY, inside the noise (up) |
| pods started | 7 | 11 | +57.1% |  | STEADY, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | -0.0% |  | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 1323 | 1390 | +5.1% |  | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1323 | 1390 | +5.1% |  | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.714 | 2.688 | +56.8% |  | shown, not judged |
| host CPU busy, the real machine under kind (%) | 49.96 | 83.78 | +67.7% |  | shown, not judged |
| organism work | 1.044e+13 | 1.044e+13 | +0.0% |  | STEADY, the same |
| organism energy (J) | 6.905e+12 | 6.909e+12 | +0.1% |  | STEADY, inside the noise (up) |
| organism time over the line (% of steps) | 2.335 | 2.205 | -5.6% |  | STEADY, inside the noise (cut) |
| organism work per energy | 1.511 | 1.511 | -0.1% |  | STEADY, inside the noise (cut) |
| organism behind its window (s) | 1.9 | 2.9 | +52.6% |  | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

3 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4689 | 6493 | +38.5% | -6156 to +9763 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5944 | 9197 | +54.7% | -9002 to +1.551e+04 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 52.97 | 75.01 | +41.6% | -98.4 to +142.5 | STEADY, inside the noise (up) |
| failed requests (%) | 42.17 | 58.78 | +39.4% | -107.1 to +140.4 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.899 | 14.82 | +49.7% | +2.366 to +7.476 | power given |
| pods started | 5.333 | 11 | +106.3% | +1.872 to +9.462 | power given |
| worker nodes in service, mean | 6 | 5.997 | -0.0% | -0.01472 to +0.009167 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1369 | 1392 | +1.6% | -75.21 to +120.3 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1369 | 1391 | +1.6% | -76.74 to +121 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.342 | 2.69 | +14.8% | -0.9449 to +1.64 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.28 | 88.09 | +23.6% | -27.61 to +61.24 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.9 | 6.1 | +24.5% | -1.533 to +3.933 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

3 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2591 | 1544 | -40.4% | -1.452e+04 to +1.242e+04 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 3274 | 3092 | -5.5% | -1.938e+04 to +1.902e+04 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 27.58 | 18.38 | -33.3% | -169.6 to +151.2 | STEADY, inside the noise (cut) |
| failed requests (%) | 20.72 | 7.865 | -62.0% | -122.9 to +97.2 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.872 | 14.52 | +47.1% | +2.024 to +7.278 | power given |
| pods started | 6.333 | 14 | +121.1% | +1.415 to +13.92 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.525e-15 to +5.301e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 1358 | 1355 | -0.2% | -161.3 to +155.8 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1358 | 1355 | -0.2% | -161.3 to +155.8 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.2 | 2.202 | +0.1% | -2.131 to +2.136 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.17 | 69.99 | +5.8% | -61.66 to +69.28 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3 | 3.7 | +23.3% | +0.04271 to +1.357 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 500 copies: ONE REPETITION

0 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|

### Distribution / Specialized, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 3 (HPA replicas, mean; organism energy (J); organism work per energy), STEADY (inside the noise) on 8

3 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4726 | 4125 | -12.7% | -5189 to +3985 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6068 | 5822 | -4.1% | -2794 to +2302 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 52.25 | 48.07 | -8.0% | -23.88 to +15.52 | STEADY, inside the noise (cut) |
| failed requests (%) | 41.67 | 35.18 | -15.6% | -39.33 to +26.34 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.916 | 15.16 | +52.9% | +3.8 to +6.682 | power given |
| pods started | 5.333 | 13.33 | +150.0% | -0.9574 to +16.96 | STEADY, inside the noise (up) |
| worker nodes in service, mean | 6 | 5.997 | -0.0% | -0.01471 to +0.009164 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1372 | 1380 | +0.6% | -36.52 to +52.2 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1372 | 1379 | +0.5% | -37.92 to +52.77 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.384 | 2.544 | +6.7% | -0.4314 to +0.7522 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.23 | 81.49 | +14.4% | -5.297 to +25.81 | shown, not judged |
| organism work | 1.082e+13 | 1.082e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.854e+13 | 2.855e+13 | +0.0% | +4.369e+09 to +4.369e+09 | power given |
| organism time over the line (% of steps) | 2.451 | 2.367 | -3.4% | -0.08396 to -0.08396 | GAIN |
| organism work per energy | 0.3789 | 0.3788 | -0.0% | -5.798e-05 to -5.798e-05 | power given |
| organism behind its window (s) | 3.933 | 5.033 | +28.0% | +0.4427 to +1.757 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
