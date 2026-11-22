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
| response time (ms), 95th percentile | 4356 | 4270 | 3009 | 3476 | 4507 | 4749 | 2888 | 3922 | 2578 | 3329 |
| response time (ms), 99th percentile | 6108 | 6171 | 4585 | 6134 | 6512 | 6817 | 4338 | 5970 | 4167 | 5101 |
| time over the response line (% of samples) | 56.27 | 62.11 | 48.22 | 60.12 | 62.58 | 60.71 | 47.65 | 52.61 | 45.06 | 43.64 |
| failed requests (%) | 43.27 | 50.08 | 31.14 | 52.47 | 46.41 | 49.85 | 38.04 | 39.36 | 34.34 | 33.77 |
| HPA replicas, mean | 9.909 | 14.98 | 9.898 | 12.89 | 9.916 | 13.78 | 9.893 | 13.63 | 9.909 | 13.21 |
| pods started | 5.067 | 10.33 | 5.533 | 9.667 | 5.067 | 10.47 | 5.667 | 10.27 | 5.533 | 11.2 |
| worker nodes in service, mean | 6 | 5.999 | 6 | 5.998 | 6 | 5.999 | 6 | 5.999 | 6 | 5.999 |
| energy, parked workers still on at idle power (Wh, declared model) | 1380 | 1383 | 1380 | 1378 | 1390 | 1379 | 1373 | 1377 | 1374 | 1373 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1380 | 1382 | 1380 | 1378 | 1390 | 1378 | 1373 | 1377 | 1374 | 1373 |
| CPU used with Omni's own (cores), mean | 2.49 | 2.576 | 2.503 | 2.51 | 2.623 | 2.522 | 2.397 | 2.506 | 2.409 | 2.442 |
| host CPU busy, the real machine under kind (%) | 73.98 | 80.81 | 75.62 | 84.69 | 80.47 | 82.81 | 73.8 | 82.52 | 72.46 | 80.43 |
| organism work | 1.044e+13 | 1.044e+13 | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 3.317e+13 | 3.317e+13 | 1.082e+13 | 1.082e+13 |
| organism energy (J) | 6.905e+12 | 6.909e+12 | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 5.512e+15 | 5.512e+15 | 2.854e+13 | 2.855e+13 |
| organism time over the line (% of steps) | 2.335 | 2.205 | 1.943 | 1.874 | 4.602 | 4.511 | 1.469 | 1.382 | 2.451 | 2.367 |
| organism work per energy | 1.511 | 1.511 | 1.375 | 1.374 | 1.116 | 1.115 | 0.006018 | 0.006018 | 0.3789 | 0.3788 |
| organism behind its window (s) | 2.173 | 3.12 | 4.547 | 6.247 | 3.427 | 4.493 | 3.767 | 4.9 | 4.12 | 5.613 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

15 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4356 | 4270 | -2.0% | -2660 to +2487 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6108 | 6171 | +1.0% | -3158 to +3284 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 56.27 | 62.11 | +10.4% | -19.43 to +31.11 | STEADY, inside the noise (up) |
| failed requests (%) | 43.27 | 50.08 | +15.7% | -14.71 to +28.34 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.909 | 14.98 | +51.2% | +3.903 to +6.236 | power given |
| pods started | 5.067 | 10.33 | +103.9% | +3.84 to +6.694 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003185 to +0.001817 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1380 | 1383 | +0.2% | -18.51 to +24.24 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1380 | 1382 | +0.2% | -18.64 to +24.16 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.49 | 2.576 | +3.4% | -0.2023 to +0.3736 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.98 | 80.81 | +9.2% | -1.94 to +15.6 | shown, not judged |
| organism work | 1.044e+13 | 1.044e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 6.905e+12 | 6.909e+12 | +0.1% | +4.063e+09 to +4.063e+09 | power given |
| organism time over the line (% of steps) | 2.335 | 2.205 | -5.6% | -0.13 to -0.13 | GAIN |
| organism work per energy | 1.511 | 1.511 | -0.1% | -0.0008889 to -0.0008889 | power given |
| organism behind its window (s) | 2.173 | 3.12 | +43.6% | +0.6982 to +1.195 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

15 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3009 | 3476 | +15.5% | -1600 to +2535 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4585 | 6134 | +33.8% | -1077 to +4176 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 48.22 | 60.12 | +24.7% | -14.94 to +38.75 | STEADY, inside the noise (up) |
| failed requests (%) | 31.14 | 52.47 | +68.5% | -2.985 to +45.65 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.898 | 12.89 | +30.2% | +1.644 to +4.34 | power given |
| pods started | 5.533 | 9.667 | +74.7% | +2.88 to +5.387 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.003 to +0.0003377 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1380 | 1378 | -0.1% | -23.25 to +19.52 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1380 | 1378 | -0.1% | -23.45 to +19.32 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.503 | 2.51 | +0.3% | -0.2866 to +0.3013 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.62 | 84.69 | +12.0% | -0.1372 to +18.26 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.547 | 6.247 | +37.4% | +1.284 to +2.116 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

15 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4507 | 4749 | +5.4% | -2120 to +2604 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6512 | 6817 | +4.7% | -2661 to +3271 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 62.58 | 60.71 | -3.0% | -23.54 to +19.79 | STEADY, inside the noise (cut) |
| failed requests (%) | 46.41 | 49.85 | +7.4% | -14.89 to +21.77 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.916 | 13.78 | +38.9% | +2.229 to +5.493 | power given |
| pods started | 5.067 | 10.47 | +106.6% | +4.4 to +6.4 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002617 to +0.0005664 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1390 | 1379 | -0.8% | -26.07 to +3.167 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1390 | 1378 | -0.8% | -26.16 to +2.945 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.623 | 2.522 | -3.9% | -0.2982 to +0.09593 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 80.47 | 82.81 | +2.9% | -3.829 to +8.507 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.427 | 4.493 | +31.1% | +0.7326 to +1.401 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

15 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2888 | 3922 | +35.8% | -1246 to +3315 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4338 | 5970 | +37.6% | -1252 to +4516 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 47.65 | 52.61 | +10.4% | -20.79 to +30.71 | STEADY, inside the noise (up) |
| failed requests (%) | 38.04 | 39.36 | +3.5% | -20.8 to +23.43 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.893 | 13.63 | +37.7% | +2.408 to +5.057 | power given |
| pods started | 5.667 | 10.27 | +81.2% | +2.839 to +6.361 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001368 to +0.0003128 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1373 | 1377 | +0.3% | -17.77 to +26.93 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1373 | 1377 | +0.3% | -17.86 to +26.87 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.397 | 2.506 | +4.5% | -0.1887 to +0.4066 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.8 | 82.52 | +11.8% | -0.5122 to +17.96 | shown, not judged |
| organism work | 3.317e+13 | 3.317e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.512e+15 | 5.512e+15 | +0.0% | +4.35e+09 to +4.35e+09 | power given |
| organism time over the line (% of steps) | 1.469 | 1.382 | -5.9% | -0.0869 to -0.0869 | GAIN |
| organism work per energy | 0.006018 | 0.006018 | -0.0% | -4.749e-09 to -4.749e-09 | power given |
| organism behind its window (s) | 3.767 | 4.9 | +30.1% | +0.6715 to +1.595 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

15 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2578 | 3329 | +29.1% | -1582 to +3084 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4167 | 5101 | +22.4% | -2055 to +3922 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 45.06 | 43.64 | -3.1% | -26.67 to +23.83 | STEADY, inside the noise (cut) |
| failed requests (%) | 34.34 | 33.77 | -1.6% | -21.38 to +20.26 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.909 | 13.21 | +33.3% | +1.476 to +5.131 | power given |
| pods started | 5.533 | 11.2 | +102.4% | +3.619 to +7.714 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001526 to +0.0003047 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1374 | 1373 | -0.0% | -22.09 to +20.97 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1374 | 1373 | -0.0% | -22.15 to +20.85 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.409 | 2.442 | +1.4% | -0.2581 to +0.3239 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.46 | 80.43 | +11.0% | -1.024 to +16.95 | shown, not judged |
| organism work | 1.082e+13 | 1.082e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.854e+13 | 2.855e+13 | +0.0% | +4.369e+09 to +4.369e+09 | power given |
| organism time over the line (% of steps) | 2.451 | 2.367 | -3.4% | -0.08396 to -0.08396 | GAIN |
| organism work per energy | 0.3789 | 0.3788 | -0.0% | -5.798e-05 to -5.798e-05 | power given |
| organism behind its window (s) | 4.12 | 5.613 | +36.2% | +0.8775 to +2.109 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
