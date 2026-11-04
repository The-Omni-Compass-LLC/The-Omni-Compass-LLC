# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 500 copies: native | The spine, the muscles every stack runs on, 500 copies: omni | Compute / AI / Cloud, 500 copies: native | Compute / AI / Cloud, 500 copies: omni | Physics / Robotics / Autonomous, 500 copies: native | Physics / Robotics / Autonomous, 500 copies: omni | Energy / Facility / Industrial, 500 copies: native | Energy / Facility / Industrial, 500 copies: omni | Distribution / Specialized, 500 copies: native | Distribution / Specialized, 500 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3730 | 4359 | 4154 | 4478 | 4231 | 4808 | 4929 | 3985 | 3073 | 5322 |
| response time (ms), 99th percentile | 5597 | 6121 | 6067 | 6877 | 6268 | 6728 | 6837 | 6118 | 4593 | 7342 |
| time over the response line (% of samples) | 55.42 | 52.28 | 60.82 | 61.24 | 63.07 | 62.96 | 64.37 | 53.27 | 46.67 | 63.48 |
| failed requests (%) | 42.02 | 38.94 | 44.81 | 47.79 | 49.89 | 50.98 | 48.56 | 43.57 | 37.4 | 49.94 |
| HPA replicas, mean | 9.906 | 13.64 | 9.911 | 14.22 | 9.911 | 15.13 | 9.915 | 14 | 9.906 | 14.67 |
| pods started | 5.28 | 10.96 | 5.32 | 10.58 | 5.44 | 10.75 | 5.16 | 11.39 | 5.76 | 11.21 |
| worker nodes in service, mean | 6 | 6 | 6 | 5.997 | 6 | 5.999 | 6 | 5.999 | 6 | 5.999 |
| energy, parked workers still on at idle power (Wh, declared model) | 1384 | 1378 | 1387 | 1381 | 1386 | 1381 | 1386 | 1376 | 1370 | 1383 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1384 | 1378 | 1387 | 1381 | 1386 | 1381 | 1386 | 1375 | 1370 | 1382 |
| CPU used with Omni's own (cores), mean | 2.541 | 2.511 | 2.592 | 2.56 | 2.573 | 2.564 | 2.577 | 2.479 | 2.358 | 2.591 |
| host CPU busy, the real machine under kind (%) | 74.46 | 77.32 | 77.73 | 84.27 | 78.07 | 82.82 | 78.94 | 81.2 | 70.4 | 84.59 |
| organism work | 1.044e+13 | 1.044e+13 | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 3.317e+13 | 3.317e+13 | 1.082e+13 | 1.082e+13 |
| organism energy (J) | 6.905e+12 | 6.909e+12 | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 5.512e+15 | 5.512e+15 | 2.854e+13 | 2.855e+13 |
| organism time over the line (% of steps) | 2.335 | 2.205 | 1.943 | 1.874 | 4.602 | 4.511 | 1.469 | 1.382 | 2.451 | 2.367 |
| organism work per energy | 1.511 | 1.511 | 1.375 | 1.374 | 1.116 | 1.115 | 0.006018 | 0.006018 | 0.3789 | 0.3788 |
| organism behind its window (s) | 2.216 | 2.813 | 4.58 | 5.983 | 3.284 | 4.237 | 3.812 | 4.726 | 3.928 | 5.342 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

23 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3959 | 4359 | +10.1% | -1295 to +2095 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5774 | 6121 | +6.0% | -1757 to +2450 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 54.96 | 52.28 | -4.9% | -21.79 to +16.44 | STEADY, inside the noise (cut) |
| failed requests (%) | 41.19 | 38.94 | -5.5% | -19.68 to +15.19 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.906 | 13.64 | +37.7% | +2.442 to +5.032 | power given |
| pods started | 5.261 | 10.96 | +108.3% | +4.836 to +6.555 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.001056 to +0.0001878 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1382 | 1378 | -0.3% | -17.65 to +8.839 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1382 | 1378 | -0.3% | -17.71 to +8.769 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.526 | 2.511 | -0.6% | -0.1906 to +0.16 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.21 | 77.32 | +4.2% | -2.201 to +8.427 | shown, not judged |
| organism work | 1.044e+13 | 1.044e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 6.905e+12 | 6.909e+12 | +0.1% | +4.063e+09 to +4.063e+09 | power given |
| organism time over the line (% of steps) | 2.335 | 2.205 | -5.6% | -0.13 to -0.13 | GAIN |
| organism work per energy | 1.511 | 1.511 | -0.1% | -0.0008889 to -0.0008889 | power given |
| organism behind its window (s) | 2.23 | 2.813 | +26.1% | +0.4143 to +0.7509 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

24 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4315 | 4478 | +3.8% | -1241 to +1566 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6302 | 6877 | +9.1% | -1116 to +2266 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 63.33 | 61.24 | -3.3% | -16.41 to +12.23 | STEADY, inside the noise (cut) |
| failed requests (%) | 46.68 | 47.79 | +2.4% | -13.17 to +15.4 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.914 | 14.22 | +43.4% | +3.349 to +5.255 | power given |
| pods started | 5.25 | 10.58 | +101.6% | +4.727 to +5.939 | power given |
| worker nodes in service, mean | 6 | 5.997 | -0.0% | -0.00476 to +0.0001707 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1390 | 1381 | -0.6% | -19.14 to +1.723 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1390 | 1381 | -0.7% | -19.48 to +1.371 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.625 | 2.56 | -2.4% | -0.2041 to +0.07565 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 78.74 | 84.27 | +7.0% | +1.14 to +9.926 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.604 | 5.983 | +30.0% | +1.037 to +1.721 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

24 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4131 | 4808 | +16.4% | -1148 to +2502 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6156 | 6728 | +9.3% | -1621 to +2763 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 62.41 | 62.96 | +0.9% | -17.01 to +18.11 | STEADY, inside the noise (up) |
| failed requests (%) | 49.3 | 50.98 | +3.4% | -13.56 to +16.93 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.91 | 15.13 | +52.7% | +4.602 to +5.841 | power given |
| pods started | 5.458 | 10.75 | +96.9% | +4.398 to +6.185 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.00285 to +0.0003415 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1386 | 1381 | -0.4% | -17.76 to +7.885 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1386 | 1381 | -0.4% | -17.97 to +7.713 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.57 | 2.564 | -0.2% | -0.1749 to +0.1632 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.93 | 82.82 | +6.3% | -0.5822 to +10.38 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.279 | 4.237 | +29.2% | +0.6711 to +1.246 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

23 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 5032 | 3985 | -20.8% | -2880 to +787.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6953 | 6118 | -12.0% | -3185 to +1516 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 66.05 | 53.27 | -19.4% | -33.39 to +7.829 | STEADY, inside the noise (cut) |
| failed requests (%) | 50.04 | 43.57 | -12.9% | -24.19 to +11.24 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.915 | 14 | +41.2% | +2.934 to +5.24 | power given |
| pods started | 5.174 | 11.39 | +120.2% | +5.175 to +7.26 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003375 to +0.001179 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1387 | 1376 | -0.8% | -24.41 to +1.965 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1387 | 1375 | -0.8% | -24.57 to +1.792 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.585 | 2.479 | -4.1% | -0.2834 to +0.07158 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 79.23 | 81.2 | +2.5% | -4.068 to +8.015 | shown, not judged |
| organism work | 3.317e+13 | 3.317e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.512e+15 | 5.512e+15 | +0.0% | +4.35e+09 to +4.35e+09 | power given |
| organism time over the line (% of steps) | 1.469 | 1.382 | -5.9% | -0.0869 to -0.0869 | GAIN |
| organism work per energy | 0.006018 | 0.006018 | -0.0% | -4.749e-09 to -4.749e-09 | power given |
| organism behind its window (s) | 3.813 | 4.726 | +23.9% | +0.6196 to +1.206 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

24 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3190 | 5322 | +66.8% | +461.3 to +3803 | LOSS |
| response time (ms), 99th percentile | 4766 | 7342 | +54.0% | +576.4 to +4575 | LOSS |
| time over the response line (% of samples) | 48.59 | 63.48 | +30.7% | -2.406 to +32.19 | STEADY, inside the noise (up) |
| failed requests (%) | 38.96 | 49.94 | +28.2% | -2.91 to +24.87 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.908 | 14.67 | +48.1% | +3.727 to +5.8 | power given |
| pods started | 5.708 | 11.21 | +96.4% | +3.756 to +7.244 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001671 to +0.0008384 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1372 | 1383 | +0.8% | -4.425 to +25.89 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1372 | 1382 | +0.8% | -4.515 to +25.86 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.382 | 2.591 | +8.8% | +0.01044 to +0.4075 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.14 | 84.59 | +18.9% | +7.411 to +19.5 | shown, not judged |
| organism work | 1.082e+13 | 1.082e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.854e+13 | 2.855e+13 | +0.0% | +4.369e+09 to +4.369e+09 | power given |
| organism time over the line (% of steps) | 2.451 | 2.367 | -3.4% | -0.08396 to -0.08396 | GAIN |
| organism work per energy | 0.3789 | 0.3788 | -0.0% | -5.798e-05 to -5.798e-05 | power given |
| organism behind its window (s) | 3.946 | 5.342 | +35.4% | +1.148 to +1.644 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
