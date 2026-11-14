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
| response time (ms), 95th percentile | 3371 | 5354 | 3244 | 3389 | 3476 | 4090 | 3616 | 3524 | 3626 | 4660 |
| response time (ms), 99th percentile | 5028 | 7390 | 4814 | 5535 | 5122 | 5998 | 5357 | 5642 | 5376 | 6707 |
| time over the response line (% of samples) | 48.72 | 64.59 | 53 | 53.59 | 54.97 | 54.01 | 57.31 | 56.76 | 57.14 | 52.83 |
| failed requests (%) | 37.6 | 48.82 | 40.73 | 40.99 | 41.49 | 40.65 | 41.21 | 43.04 | 44.1 | 36.66 |
| HPA replicas, mean | 9.899 | 15.46 | 9.901 | 12.91 | 9.905 | 13.58 | 9.906 | 13.44 | 9.921 | 13.57 |
| pods started | 5.32 | 10.48 | 5.6 | 10.29 | 5.36 | 10.67 | 5.36 | 10.71 | 5.4 | 10.54 |
| worker nodes in service, mean | 6 | 5.998 | 6 | 6 | 6 | 6 | 6 | 5.999 | 6 | 5.999 |
| energy, parked workers still on at idle power (Wh, declared model) | 1373 | 1386 | 1380 | 1379 | 1382 | 1377 | 1383 | 1380 | 1381 | 1378 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1373 | 1386 | 1380 | 1379 | 1381 | 1377 | 1383 | 1380 | 1381 | 1378 |
| CPU used with Omni's own (cores), mean | 2.403 | 2.628 | 2.497 | 2.525 | 2.515 | 2.497 | 2.533 | 2.55 | 2.505 | 2.505 |
| host CPU busy, the real machine under kind (%) | 71.56 | 82.53 | 76.02 | 84.32 | 77 | 81.28 | 78.11 | 83.9 | 75.98 | 82.68 |
| organism work | 1.044e+13 | 1.044e+13 | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 3.317e+13 | 3.317e+13 | 1.082e+13 | 1.082e+13 |
| organism energy (J) | 6.905e+12 | 6.909e+12 | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 5.512e+15 | 5.512e+15 | 2.854e+13 | 2.855e+13 |
| organism time over the line (% of steps) | 2.335 | 2.205 | 1.943 | 1.874 | 4.602 | 4.511 | 1.469 | 1.382 | 2.451 | 2.367 |
| organism work per energy | 1.511 | 1.511 | 1.375 | 1.374 | 1.116 | 1.115 | 0.006018 | 0.006018 | 0.3789 | 0.3788 |
| organism behind its window (s) | 2.284 | 3.208 | 4.656 | 6.308 | 3.396 | 4.242 | 3.824 | 5.046 | 4.212 | 5.612 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples)), power given on 5 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3371 | 5354 | +58.8% | +291.1 to +3674 | LOSS |
| response time (ms), 99th percentile | 5028 | 7390 | +47.0% | +271 to +4454 | LOSS |
| time over the response line (% of samples) | 48.72 | 64.59 | +32.6% | +0.01603 to +31.72 | LOSS |
| failed requests (%) | 37.6 | 48.82 | +29.8% | -2.476 to +24.91 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.899 | 15.46 | +56.1% | +5.043 to +6.074 | power given |
| pods started | 5.32 | 10.48 | +97.0% | +4.522 to +5.798 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.006704 to +0.002409 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1373 | 1386 | +1.0% | +0.3327 to +26.73 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1373 | 1386 | +1.0% | -0.07954 to +26.5 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.403 | 2.628 | +9.4% | +0.0481 to +0.4023 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.56 | 82.53 | +15.3% | +5.632 to +16.31 | shown, not judged |
| organism work | 1.044e+13 | 1.044e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 6.905e+12 | 6.909e+12 | +0.1% | +4.063e+09 to +4.063e+09 | power given |
| organism time over the line (% of steps) | 2.335 | 2.205 | -5.6% | -0.13 to -0.13 | GAIN |
| organism work per energy | 1.511 | 1.511 | -0.1% | -0.0008889 to -0.0008889 | power given |
| organism behind its window (s) | 2.284 | 3.208 | +40.5% | +0.7084 to +1.14 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

24 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3074 | 3389 | +10.3% | -1413 to +2044 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4626 | 5535 | +19.6% | -1196 to +3014 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 51.92 | 53.59 | +3.2% | -17.77 to +21.13 | STEADY, inside the noise (up) |
| failed requests (%) | 39.79 | 40.99 | +3.0% | -14.9 to +17.29 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.9 | 12.91 | +30.4% | +1.862 to +4.152 | power given |
| pods started | 5.625 | 10.29 | +83.0% | +3.357 to +5.977 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -0.001133 to +0.001202 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 1380 | 1379 | -0.0% | -14.12 to +12.94 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1380 | 1379 | -0.0% | -14.12 to +12.95 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.49 | 2.525 | +1.4% | -0.1436 to +0.2144 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.76 | 84.32 | +11.3% | +2.913 to +14.21 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.65 | 6.308 | +35.7% | +1.328 to +1.989 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

24 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3349 | 4090 | +22.1% | -1138 to +2619 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4997 | 5998 | +20.0% | -1325 to +3327 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 54 | 54.01 | +0.0% | -19.18 to +19.19 | STEADY, inside the noise (up) |
| failed requests (%) | 40.6 | 40.65 | +0.1% | -15.88 to +15.98 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.904 | 13.58 | +37.1% | +2.478 to +4.873 | power given |
| pods started | 5.375 | 10.67 | +98.4% | +3.891 to +6.692 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.001322 to +0.0007787 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1381 | 1377 | -0.3% | -19 to +11.04 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1381 | 1377 | -0.3% | -19.02 to +10.97 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.508 | 2.497 | -0.4% | -0.2123 to +0.1909 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.76 | 81.28 | +5.9% | -1.804 to +10.84 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.4 | 4.242 | +24.8% | +0.5973 to +1.086 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

24 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3741 | 3524 | -5.8% | -1959 to +1526 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5531 | 5642 | +2.0% | -2119 to +2341 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 59.37 | 56.76 | -4.4% | -20.1 to +14.86 | STEADY, inside the noise (cut) |
| failed requests (%) | 42.93 | 43.04 | +0.3% | -15.95 to +16.17 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.908 | 13.44 | +35.7% | +2.477 to +4.59 | power given |
| pods started | 5.333 | 10.71 | +100.8% | +4.269 to +6.481 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003209 to +0.0002944 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1384 | 1380 | -0.2% | -16.54 to +9.668 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1384 | 1380 | -0.3% | -16.68 to +9.37 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.543 | 2.55 | +0.3% | -0.169 to +0.1844 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 78.51 | 83.9 | +6.9% | -0.396 to +11.19 | shown, not judged |
| organism work | 3.317e+13 | 3.317e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.512e+15 | 5.512e+15 | +0.0% | +4.35e+09 to +4.35e+09 | power given |
| organism time over the line (% of steps) | 1.469 | 1.382 | -5.9% | -0.0869 to -0.0869 | GAIN |
| organism work per energy | 0.006018 | 0.006018 | -0.0% | -4.749e-09 to -4.749e-09 | power given |
| organism behind its window (s) | 3.829 | 5.046 | +31.8% | +0.9388 to +1.494 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

24 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3734 | 4660 | +24.8% | -831.5 to +2685 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5517 | 6707 | +21.6% | -1076 to +3455 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 56.88 | 52.83 | -7.1% | -21.44 to +13.34 | STEADY, inside the noise (cut) |
| failed requests (%) | 43.73 | 36.66 | -16.2% | -22.15 to +7.99 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.921 | 13.57 | +36.8% | +2.452 to +4.847 | power given |
| pods started | 5.375 | 10.54 | +96.1% | +4.091 to +6.243 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003262 to +0.001136 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1380 | 1378 | -0.2% | -15.77 to +10.65 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1380 | 1378 | -0.2% | -15.8 to +10.36 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.497 | 2.505 | +0.3% | -0.1683 to +0.185 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.82 | 82.68 | +9.0% | +1.377 to +12.34 | shown, not judged |
| organism work | 1.082e+13 | 1.082e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.854e+13 | 2.855e+13 | +0.0% | +4.369e+09 to +4.369e+09 | power given |
| organism time over the line (% of steps) | 2.451 | 2.367 | -3.4% | -0.08396 to -0.08396 | GAIN |
| organism work per energy | 0.3789 | 0.3788 | -0.0% | -5.798e-05 to -5.798e-05 | power given |
| organism behind its window (s) | 4.221 | 5.612 | +33.0% | +1.04 to +1.743 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
