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
| response time (ms), 95th percentile | 3676 | 3811 | 3433 | 3288 | 4413 | 4545 | 3342 | 3839 | 4063 | 5799 |
| response time (ms), 99th percentile | 5787 | 5508 | 5280 | 6369 | 5967 | 6673 | 5098 | 5523 | 5981 | 8119 |
| time over the response line (% of samples) | 55.6 | 55.09 | 57.71 | 58.11 | 56.12 | 56.44 | 54.12 | 51.88 | 57.15 | 68.78 |
| failed requests (%) | 43.98 | 43.72 | 44.13 | 51.09 | 43.32 | 41.23 | 42.04 | 41.37 | 42.93 | 53.6 |
| HPA replicas, mean | 9.907 | 14.33 | 9.905 | 13.5 | 9.902 | 14.14 | 9.901 | 13.82 | 9.919 | 14.68 |
| pods started | 5.24 | 10.55 | 5.52 | 10.44 | 5.48 | 11.13 | 5.6 | 10.75 | 5.4 | 10.6 |
| worker nodes in service, mean | 6 | 6 | 6 | 5.999 | 6 | 6 | 6 | 5.998 | 6 | 5.999 |
| energy, parked workers still on at idle power (Wh, declared model) | 1380 | 1378 | 1385 | 1381 | 1377 | 1382 | 1380 | 1374 | 1381 | 1386 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1380 | 1378 | 1385 | 1381 | 1377 | 1381 | 1380 | 1374 | 1381 | 1386 |
| CPU used with Omni's own (cores), mean | 2.491 | 2.519 | 2.557 | 2.558 | 2.453 | 2.562 | 2.493 | 2.462 | 2.502 | 2.62 |
| host CPU busy, the real machine under kind (%) | 73.07 | 77.86 | 76.51 | 84.1 | 74.73 | 82.03 | 75.55 | 80.3 | 74.83 | 85.27 |
| organism work | 1.044e+13 | 1.044e+13 | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 3.317e+13 | 3.317e+13 | 1.082e+13 | 1.082e+13 |
| organism energy (J) | 6.905e+12 | 6.909e+12 | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 5.512e+15 | 5.512e+15 | 2.854e+13 | 2.855e+13 |
| organism time over the line (% of steps) | 2.335 | 2.205 | 1.943 | 1.874 | 4.602 | 4.511 | 1.469 | 1.382 | 2.451 | 2.367 |
| organism work per energy | 1.511 | 1.511 | 1.375 | 1.374 | 1.116 | 1.115 | 0.006018 | 0.006018 | 0.3789 | 0.3788 |
| organism behind its window (s) | 2.156 | 3.041 | 4.496 | 5.856 | 3.296 | 4.126 | 3.588 | 4.733 | 4.116 | 5.472 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

22 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3862 | 3811 | -1.3% | -1303 to +1202 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5995 | 5508 | -8.1% | -2207 to +1233 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 56.84 | 55.09 | -3.1% | -19.42 to +15.91 | STEADY, inside the noise (cut) |
| failed requests (%) | 44.72 | 43.72 | -2.2% | -16.55 to +14.56 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.909 | 14.33 | +44.6% | +3.257 to +5.577 | power given |
| pods started | 5.182 | 10.55 | +103.5% | +4.43 to +6.297 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -0.0001157 to +0.00033 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 1381 | 1378 | -0.2% | -18.58 to +12.81 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1381 | 1378 | -0.2% | -18.55 to +12.81 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.508 | 2.519 | +0.4% | -0.2001 to +0.2217 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.62 | 77.86 | +5.8% | -1.832 to +10.32 | shown, not judged |
| organism work | 1.044e+13 | 1.044e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 6.905e+12 | 6.909e+12 | +0.1% | +4.063e+09 to +4.063e+09 | power given |
| organism time over the line (% of steps) | 2.335 | 2.205 | -5.6% | -0.13 to -0.13 | GAIN |
| organism work per energy | 1.511 | 1.511 | -0.1% | -0.0008889 to -0.0008889 | power given |
| organism behind its window (s) | 2.168 | 3.041 | +40.3% | +0.7614 to +0.9841 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

18 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3486 | 3288 | -5.7% | -2188 to +1791 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5094 | 6369 | +25.0% | -1444 to +3993 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 53.08 | 58.11 | +9.5% | -21.41 to +31.47 | STEADY, inside the noise (up) |
| failed requests (%) | 39.44 | 51.09 | +29.5% | -14.24 to +37.54 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.9 | 13.5 | +36.3% | +2.555 to +4.634 | power given |
| pods started | 5.611 | 10.44 | +86.1% | +3.806 to +5.86 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.00191 to +0.0003228 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1381 | 1381 | -0.0% | -16.5 to +16.41 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1381 | 1381 | -0.0% | -16.61 to +16.28 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.513 | 2.558 | +1.8% | -0.1768 to +0.267 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.25 | 84.1 | +11.8% | +1.464 to +16.24 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.467 | 5.856 | +31.1% | +1.034 to +1.744 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

23 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4497 | 4545 | +1.1% | -1488 to +1584 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6093 | 6673 | +9.5% | -1324 to +2485 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 57.55 | 56.44 | -1.9% | -16.37 to +14.16 | STEADY, inside the noise (cut) |
| failed requests (%) | 44.45 | 41.23 | -7.2% | -17.23 to +10.8 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.903 | 14.14 | +42.8% | +3.033 to +5.449 | power given |
| pods started | 5.435 | 11.13 | +104.8% | +4.807 to +6.584 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.0009836 to +0.0003436 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1379 | 1382 | +0.2% | -9.598 to +14.94 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1379 | 1381 | +0.2% | -9.654 to +14.9 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.476 | 2.562 | +3.5% | -0.07401 to +0.2473 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.36 | 82.03 | +8.9% | +1.799 to +11.55 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.291 | 4.126 | +25.4% | +0.6133 to +1.056 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

24 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3436 | 3839 | +11.7% | -1543 to +2349 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5177 | 5523 | +6.7% | -1903 to +2597 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 53.81 | 51.88 | -3.6% | -21.51 to +17.65 | STEADY, inside the noise (cut) |
| failed requests (%) | 41.64 | 41.37 | -0.7% | -17.87 to +17.32 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.901 | 13.82 | +39.6% | +2.719 to +5.126 | power given |
| pods started | 5.625 | 10.75 | +91.1% | +3.742 to +6.508 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.004873 to +0.0008689 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1380 | 1374 | -0.4% | -19.17 to +9.009 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1380 | 1374 | -0.4% | -19.48 to +8.719 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.485 | 2.462 | -0.9% | -0.2126 to +0.1667 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.39 | 80.3 | +6.5% | -1.232 to +11.06 | shown, not judged |
| organism work | 3.317e+13 | 3.317e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.512e+15 | 5.512e+15 | +0.0% | +4.35e+09 to +4.35e+09 | power given |
| organism time over the line (% of steps) | 1.469 | 1.382 | -5.9% | -0.0869 to -0.0869 | GAIN |
| organism work per energy | 0.006018 | 0.006018 | -0.0% | -4.749e-09 to -4.749e-09 | power given |
| organism behind its window (s) | 3.6 | 4.733 | +31.5% | +0.9232 to +1.343 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4063 | 5799 | +42.7% | +270.6 to +3201 | LOSS |
| response time (ms), 99th percentile | 5981 | 8119 | +35.7% | +290.5 to +3984 | LOSS |
| time over the response line (% of samples) | 57.15 | 68.78 | +20.4% | -3.868 to +27.13 | STEADY, inside the noise (up) |
| failed requests (%) | 42.93 | 53.6 | +24.9% | -2.412 to +23.75 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.919 | 14.68 | +48.0% | +3.993 to +5.533 | power given |
| pods started | 5.4 | 10.6 | +96.3% | +4.428 to +5.972 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001358 to +0.001253 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1381 | 1386 | +0.4% | -7.809 to +19.39 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1381 | 1386 | +0.4% | -7.783 to +19.34 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.502 | 2.62 | +4.7% | -0.05592 to +0.2925 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.83 | 85.27 | +13.9% | +5.058 to +15.82 | shown, not judged |
| organism work | 1.082e+13 | 1.082e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.854e+13 | 2.855e+13 | +0.0% | +4.369e+09 to +4.369e+09 | power given |
| organism time over the line (% of steps) | 2.451 | 2.367 | -3.4% | -0.08396 to -0.08396 | GAIN |
| organism work per energy | 0.3789 | 0.3788 | -0.0% | -5.798e-05 to -5.798e-05 | power given |
| organism behind its window (s) | 4.116 | 5.472 | +32.9% | +1.136 to +1.576 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
