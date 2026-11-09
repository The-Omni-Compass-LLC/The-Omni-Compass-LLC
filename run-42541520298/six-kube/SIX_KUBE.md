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
| response time (ms), 95th percentile | 3616 | 4079 | 3472 | 3281 | 4179 | 4900 | 3955 | 5198 | 3740 | 4432 |
| response time (ms), 99th percentile | 5612 | 6040 | 5194 | 6163 | 6276 | 7331 | 6076 | 7459 | 5531 | 6367 |
| time over the response line (% of samples) | 59 | 56.07 | 54.8 | 56.1 | 63.39 | 63.4 | 61.78 | 63.81 | 54.26 | 56.48 |
| failed requests (%) | 45.98 | 42.12 | 41.27 | 46.45 | 46.53 | 47.98 | 49.43 | 51.13 | 42.74 | 46.4 |
| HPA replicas, mean | 9.912 | 14.47 | 9.905 | 12.86 | 9.91 | 14.58 | 9.909 | 14.47 | 9.916 | 13.48 |
| pods started | 5.04 | 10.65 | 5.52 | 10.13 | 5.4 | 10.96 | 5.36 | 10.81 | 5.56 | 10.04 |
| worker nodes in service, mean | 6 | 5.999 | 6 | 5.998 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 1386 | 1379 | 1383 | 1379 | 1388 | 1386 | 1382 | 1384 | 1377 | 1376 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1386 | 1379 | 1383 | 1379 | 1388 | 1386 | 1382 | 1384 | 1377 | 1376 |
| CPU used with Omni's own (cores), mean | 2.575 | 2.545 | 2.534 | 2.52 | 2.602 | 2.623 | 2.523 | 2.594 | 2.458 | 2.483 |
| host CPU busy, the real machine under kind (%) | 75.25 | 78.47 | 75.94 | 82.81 | 78.6 | 83.82 | 77.01 | 84.66 | 73.56 | 81.49 |
| organism work | 1.044e+13 | 1.044e+13 | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 3.317e+13 | 3.317e+13 | 1.082e+13 | 1.082e+13 |
| organism energy (J) | 6.905e+12 | 6.909e+12 | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 5.512e+15 | 5.512e+15 | 2.854e+13 | 2.855e+13 |
| organism time over the line (% of steps) | 2.335 | 2.205 | 1.943 | 1.874 | 4.602 | 4.511 | 1.469 | 1.382 | 2.451 | 2.367 |
| organism work per energy | 1.511 | 1.511 | 1.375 | 1.374 | 1.116 | 1.115 | 0.006018 | 0.006018 | 0.3789 | 0.3788 |
| organism behind its window (s) | 2.2 | 2.957 | 4.488 | 5.987 | 3.248 | 4.191 | 3.808 | 4.762 | 4.064 | 5.391 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

23 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3872 | 4079 | +5.4% | -1198 to +1613 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5753 | 6040 | +5.0% | -1344 to +1918 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 61.39 | 56.07 | -8.7% | -18.02 to +7.383 | STEADY, inside the noise (cut) |
| failed requests (%) | 47.76 | 42.12 | -11.8% | -16.88 to +5.603 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.915 | 14.47 | +46.0% | +3.549 to +5.57 | power given |
| pods started | 4.957 | 10.65 | +114.9% | +4.909 to +6.483 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002783 to +0.0002253 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1388 | 1379 | -0.6% | -19.88 to +2.348 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1388 | 1379 | -0.6% | -20.1 to +2.182 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.6 | 2.545 | -2.1% | -0.2018 to +0.09155 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.04 | 78.47 | +3.2% | -1.843 to +6.71 | shown, not judged |
| organism work | 1.044e+13 | 1.044e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 6.905e+12 | 6.909e+12 | +0.1% | +4.063e+09 to +4.063e+09 | power given |
| organism time over the line (% of steps) | 2.335 | 2.205 | -5.6% | -0.13 to -0.13 | GAIN |
| organism work per energy | 1.511 | 1.511 | -0.1% | -0.0008889 to -0.0008889 | power given |
| organism behind its window (s) | 2.209 | 2.957 | +33.9% | +0.5621 to +0.9335 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

23 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3169 | 3281 | +3.5% | -1517 to +1742 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4862 | 6163 | +26.8% | -863 to +3466 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 52.8 | 56.1 | +6.3% | -15.52 to +22.12 | STEADY, inside the noise (up) |
| failed requests (%) | 39.53 | 46.45 | +17.5% | -9.936 to +23.77 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.903 | 12.86 | +29.8% | +1.664 to +4.244 | power given |
| pods started | 5.565 | 10.13 | +82.0% | +3.565 to +5.565 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.004603 to +0.000271 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1382 | 1379 | -0.2% | -17.72 to +11.57 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1382 | 1379 | -0.2% | -18.02 to +11.21 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.524 | 2.52 | -0.2% | -0.1997 to +0.1916 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.51 | 82.81 | +9.7% | +1.353 to +13.25 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.483 | 5.987 | +33.6% | +1.271 to +1.738 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

23 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4263 | 4900 | +14.9% | -817.9 to +2092 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6405 | 7331 | +14.5% | -594.7 to +2446 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 65.53 | 63.4 | -3.2% | -11.48 to +7.23 | STEADY, inside the noise (cut) |
| failed requests (%) | 48.05 | 47.98 | -0.2% | -11.47 to +11.32 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.913 | 14.58 | +47.1% | +3.62 to +5.719 | power given |
| pods started | 5.348 | 10.96 | +104.9% | +5.143 to +6.074 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.0003151 to +0.0001101 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1390 | 1386 | -0.3% | -9.829 to +0.8098 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1390 | 1386 | -0.3% | -9.843 to +0.793 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.63 | 2.623 | -0.3% | -0.07679 to +0.06322 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 79.38 | 83.82 | +5.6% | +2.067 to +6.804 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.261 | 4.191 | +28.5% | +0.7278 to +1.133 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

21 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4063 | 5198 | +27.9% | -831.2 to +3100 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6234 | 7459 | +19.6% | -1251 to +3700 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 63.22 | 63.81 | +0.9% | -18.49 to +19.69 | STEADY, inside the noise (up) |
| failed requests (%) | 50.79 | 51.13 | +0.7% | -16.34 to +17.01 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.91 | 14.47 | +46.1% | +3.699 to +5.429 | power given |
| pods started | 5.333 | 10.81 | +102.7% | +4.515 to +6.438 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.001142 to +0.0007853 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1384 | 1384 | +0.0% | -13.76 to +14.9 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1384 | 1384 | +0.0% | -13.73 to +14.81 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.54 | 2.594 | +2.2% | -0.1381 to +0.2476 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.51 | 84.66 | +9.2% | +0.6613 to +13.64 | shown, not judged |
| organism work | 3.317e+13 | 3.317e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.512e+15 | 5.512e+15 | +0.0% | +4.35e+09 to +4.35e+09 | power given |
| organism time over the line (% of steps) | 1.469 | 1.382 | -5.9% | -0.0869 to -0.0869 | GAIN |
| organism work per energy | 0.006018 | 0.006018 | -0.0% | -4.749e-09 to -4.749e-09 | power given |
| organism behind its window (s) | 3.838 | 4.762 | +24.1% | +0.4682 to +1.379 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

23 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3779 | 4432 | +17.3% | -1596 to +2903 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5598 | 6367 | +13.7% | -1728 to +3266 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 55.58 | 56.48 | +1.6% | -20.44 to +22.23 | STEADY, inside the noise (up) |
| failed requests (%) | 43.77 | 46.4 | +6.0% | -15.24 to +20.5 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.918 | 13.48 | +35.9% | +2.267 to +4.849 | power given |
| pods started | 5.522 | 10.04 | +81.9% | +3.513 to +5.531 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.001243 to +0.000303 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1379 | 1376 | -0.2% | -18.72 to +13.36 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1379 | 1376 | -0.2% | -18.79 to +13.29 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.477 | 2.483 | +0.3% | -0.2088 to +0.2213 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.1 | 81.49 | +10.0% | +0.617 to +14.18 | shown, not judged |
| organism work | 1.082e+13 | 1.082e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.854e+13 | 2.855e+13 | +0.0% | +4.369e+09 to +4.369e+09 | power given |
| organism time over the line (% of steps) | 2.451 | 2.367 | -3.4% | -0.08396 to -0.08396 | GAIN |
| organism work per energy | 0.3789 | 0.3788 | -0.0% | -5.798e-05 to -5.798e-05 | power given |
| organism behind its window (s) | 4.083 | 5.391 | +32.1% | +1.002 to +1.616 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
