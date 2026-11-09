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
| response time (ms), 95th percentile | 4355 | 3619 | 4329 | 3105 | 3112 | 4727 | 3162 | 4177 | 3878 | 3753 |
| response time (ms), 99th percentile | 6500 | 6045 | 6302 | 5576 | 4764 | 6577 | 4598 | 5916 | 5898 | 5336 |
| time over the response line (% of samples) | 63.73 | 52.71 | 61.88 | 53.56 | 51.02 | 60.23 | 48.83 | 52.06 | 65.66 | 44.25 |
| failed requests (%) | 51.17 | 37.08 | 49.93 | 44.14 | 38.96 | 45.85 | 36.73 | 39.98 | 52.52 | 33.59 |
| HPA replicas, mean | 9.913 | 14.18 | 9.907 | 13.11 | 9.898 | 14.24 | 9.891 | 13.52 | 9.934 | 13.32 |
| pods started | 5.16 | 10.52 | 5.24 | 10.4 | 5.56 | 10.44 | 5.76 | 10 | 5.261 | 10.39 |
| worker nodes in service, mean | 6 | 5.999 | 6 | 5.999 | 6 | 5.998 | 6 | 5.999 | 6 | 5.999 |
| energy, parked workers still on at idle power (Wh, declared model) | 1385 | 1381 | 1383 | 1378 | 1378 | 1381 | 1375 | 1372 | 1390 | 1368 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1385 | 1381 | 1383 | 1378 | 1378 | 1381 | 1375 | 1372 | 1390 | 1368 |
| CPU used with Omni's own (cores), mean | 2.56 | 2.557 | 2.541 | 2.511 | 2.467 | 2.566 | 2.424 | 2.479 | 2.637 | 2.377 |
| host CPU busy, the real machine under kind (%) | 75.46 | 78.38 | 76.72 | 82.18 | 74.5 | 82.12 | 73.36 | 80.08 | 78.38 | 77.45 |
| organism work | 1.044e+13 | 1.044e+13 | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 3.317e+13 | 3.317e+13 | 1.082e+13 | 1.082e+13 |
| organism energy (J) | 6.905e+12 | 6.909e+12 | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 5.512e+15 | 5.512e+15 | 2.854e+13 | 2.855e+13 |
| organism time over the line (% of steps) | 2.335 | 2.205 | 1.943 | 1.874 | 4.602 | 4.511 | 1.469 | 1.382 | 2.451 | 2.367 |
| organism work per energy | 1.511 | 1.511 | 1.375 | 1.374 | 1.116 | 1.115 | 0.006018 | 0.006018 | 0.3789 | 0.3788 |
| organism behind its window (s) | 2.18 | 3.004 | 4.612 | 5.752 | 3.224 | 4.076 | 3.508 | 4.67 | 4.096 | 5.248 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4355 | 3619 | -16.9% | -2643 to +1170 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6500 | 6045 | -7.0% | -2901 to +1991 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 63.73 | 52.71 | -17.3% | -28.14 to +6.093 | STEADY, inside the noise (cut) |
| failed requests (%) | 51.17 | 37.08 | -27.5% | -28.3 to +0.1368 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.913 | 14.18 | +43.1% | +3.252 to +5.286 | power given |
| pods started | 5.16 | 10.52 | +103.9% | +4.607 to +6.113 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002864 to +0.0005546 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1385 | 1381 | -0.3% | -17.21 to +9.715 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1385 | 1381 | -0.3% | -17.36 to +9.515 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.56 | 2.557 | -0.1% | -0.1883 to +0.1821 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.46 | 78.38 | +3.9% | -2.674 to +8.523 | shown, not judged |
| organism work | 1.044e+13 | 1.044e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 6.905e+12 | 6.909e+12 | +0.1% | +4.063e+09 to +4.063e+09 | power given |
| organism time over the line (% of steps) | 2.335 | 2.205 | -5.6% | -0.13 to -0.13 | GAIN |
| organism work per energy | 1.511 | 1.511 | -0.1% | -0.0008889 to -0.0008889 | power given |
| organism behind its window (s) | 2.18 | 3.004 | +37.8% | +0.6524 to +0.9956 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4329 | 3105 | -28.3% | -3056 to +606.9 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6302 | 5576 | -11.5% | -3104 to +1651 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 61.88 | 53.56 | -13.5% | -27.13 to +10.48 | STEADY, inside the noise (cut) |
| failed requests (%) | 49.93 | 44.14 | -11.6% | -22.26 to +10.69 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.907 | 13.11 | +32.3% | +2.124 to +4.279 | power given |
| pods started | 5.24 | 10.4 | +98.5% | +4.038 to +6.282 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001615 to +0.0005609 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1383 | 1378 | -0.4% | -18.1 to +7.872 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1383 | 1378 | -0.4% | -18.11 to +7.723 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.541 | 2.511 | -1.2% | -0.2061 to +0.1461 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.72 | 82.18 | +7.1% | -0.459 to +11.38 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.612 | 5.752 | +24.7% | +0.8218 to +1.458 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3112 | 4727 | +51.9% | +92.06 to +3139 | LOSS |
| response time (ms), 99th percentile | 4764 | 6577 | +38.0% | -96.76 to +3722 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 51.02 | 60.23 | +18.1% | -7.185 to +25.62 | STEADY, inside the noise (up) |
| failed requests (%) | 38.96 | 45.85 | +17.7% | -6.665 to +20.46 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.898 | 14.24 | +43.8% | +3.375 to +5.303 | power given |
| pods started | 5.56 | 10.44 | +87.8% | +4.069 to +5.691 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.004754 to +0.0008354 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1378 | 1381 | +0.2% | -11.32 to +17.96 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1378 | 1381 | +0.2% | -11.62 to +17.67 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.467 | 2.566 | +4.0% | -0.09739 to +0.2941 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.5 | 82.12 | +10.2% | +1.668 to +13.58 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.224 | 4.076 | +26.4% | +0.6594 to +1.045 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

23 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3127 | 4177 | +33.6% | -821.4 to +2922 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4598 | 5916 | +28.7% | -900.4 to +3538 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 49.64 | 52.06 | +4.9% | -15.14 to +19.98 | STEADY, inside the noise (up) |
| failed requests (%) | 37.19 | 39.98 | +7.5% | -13.56 to +19.13 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.893 | 13.52 | +36.6% | +2.554 to +4.693 | power given |
| pods started | 5.739 | 10 | +74.2% | +3.184 to +5.338 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002645 to +0.0004494 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1376 | 1372 | -0.3% | -19.57 to +11 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1376 | 1372 | -0.3% | -19.73 to +10.83 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.444 | 2.479 | +1.4% | -0.1521 to +0.2212 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.89 | 80.08 | +8.4% | +0.1211 to +12.25 | shown, not judged |
| organism work | 3.317e+13 | 3.317e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.512e+15 | 5.512e+15 | +0.0% | +4.35e+09 to +4.35e+09 | power given |
| organism time over the line (% of steps) | 1.469 | 1.382 | -5.9% | -0.0869 to -0.0869 | GAIN |
| organism work per energy | 0.006018 | 0.006018 | -0.0% | -4.749e-09 to -4.749e-09 | power given |
| organism behind its window (s) | 3.526 | 4.67 | +32.4% | +0.8754 to +1.412 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 500 copies: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

21 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3880 | 3529 | -9.0% | -2588 to +1887 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5829 | 4982 | -14.5% | -3557 to +1864 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 65.29 | 40.95 | -37.3% | -44.86 to -3.821 | GAIN |
| failed requests (%) | 52.12 | 30.26 | -41.9% | -38.17 to -5.552 | GAIN |
| HPA replicas, mean | 9.934 | 13.08 | +31.7% | +1.688 to +4.606 | power given |
| pods started | 5.238 | 10.43 | +99.1% | +4.273 to +6.108 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003969 to +0.001895 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1390 | 1366 | -1.7% | -39.41 to -9.087 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1390 | 1366 | -1.8% | -39.31 to -9.492 | GAIN |
| CPU used with Omni's own (cores), mean | 2.633 | 2.348 | -10.8% | -0.4921 to -0.07832 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 78.28 | 76.44 | -2.4% | -8.565 to +4.884 | shown, not judged |
| organism work | 1.082e+13 | 1.082e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.854e+13 | 2.855e+13 | +0.0% | +4.369e+09 to +4.369e+09 | power given |
| organism time over the line (% of steps) | 2.451 | 2.367 | -3.4% | -0.08396 to -0.08396 | GAIN |
| organism work per energy | 0.3789 | 0.3788 | -0.0% | -5.798e-05 to -5.798e-05 | power given |
| organism behind its window (s) | 4.076 | 5.257 | +29.0% | +0.8677 to +1.494 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
