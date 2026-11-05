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
| response time (ms), 95th percentile | 4212 | 4323 | 4520 | 3188 | 4797 | 4395 | 5643 | 4905 | 4104 | 3828 |
| response time (ms), 99th percentile | 6489 | 6184 | 6368 | 5455 | 6812 | 6361 | 7806 | 6908 | 6014 | 5645 |
| time over the response line (% of samples) | 61.88 | 55.74 | 64.28 | 50.06 | 66.03 | 56.17 | 70.79 | 62.56 | 58.78 | 48.31 |
| failed requests (%) | 49.83 | 44.54 | 49.72 | 41.71 | 53.11 | 45.45 | 56.46 | 50.53 | 46.62 | 38.73 |
| HPA replicas, mean | 9.915 | 14.73 | 9.913 | 12.14 | 9.914 | 13.73 | 9.92 | 14.45 | 9.921 | 13.26 |
| pods started | 4.96 | 10.79 | 5.24 | 10.09 | 5.208 | 11.08 | 4.92 | 12.12 | 5.48 | 10.36 |
| worker nodes in service, mean | 6 | 5.999 | 6 | 5.999 | 5.999 | 5.999 | 6 | 5.999 | 6 | 5.998 |
| energy, parked workers still on at idle power (Wh, declared model) | 1385 | 1378 | 1388 | 1373 | 1385 | 1376 | 1387 | 1382 | 1380 | 1373 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1385 | 1378 | 1388 | 1373 | 1385 | 1376 | 1387 | 1382 | 1380 | 1373 |
| CPU used with Omni's own (cores), mean | 2.565 | 2.52 | 2.598 | 2.459 | 2.556 | 2.493 | 2.585 | 2.569 | 2.494 | 2.441 |
| host CPU busy, the real machine under kind (%) | 75.33 | 78.09 | 78.18 | 81 | 78 | 80.15 | 79.69 | 83.62 | 74.62 | 79.19 |
| organism work | 1.044e+13 | 1.044e+13 | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 3.317e+13 | 3.317e+13 | 1.082e+13 | 1.082e+13 |
| organism energy (J) | 6.905e+12 | 6.909e+12 | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 5.512e+15 | 5.512e+15 | 2.854e+13 | 2.855e+13 |
| organism time over the line (% of steps) | 2.335 | 2.205 | 1.943 | 1.874 | 4.602 | 4.511 | 1.469 | 1.382 | 2.451 | 2.367 |
| organism work per energy | 1.511 | 1.511 | 1.375 | 1.374 | 1.116 | 1.115 | 0.006018 | 0.006018 | 0.3789 | 0.3788 |
| organism behind its window (s) | 2.172 | 3.038 | 4.524 | 5.952 | 3.333 | 4.129 | 3.716 | 4.732 | 3.928 | 5.172 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

24 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4079 | 4323 | +6.0% | -1618 to +2107 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6373 | 6184 | -3.0% | -2309 to +1932 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 61.24 | 55.74 | -9.0% | -23.18 to +12.18 | STEADY, inside the noise (cut) |
| failed requests (%) | 49.4 | 44.54 | -9.9% | -19.94 to +10.2 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.914 | 14.73 | +48.6% | +4.032 to +5.598 | power given |
| pods started | 5 | 10.79 | +115.8% | +4.885 to +6.698 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001407 to +0.000355 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1385 | 1378 | -0.5% | -20.04 to +5.375 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1385 | 1378 | -0.5% | -20.05 to +5.233 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.562 | 2.52 | -1.6% | -0.2152 to +0.1313 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.18 | 78.09 | +3.9% | -2.443 to +8.269 | shown, not judged |
| organism work | 1.044e+13 | 1.044e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 6.905e+12 | 6.909e+12 | +0.1% | +4.063e+09 to +4.063e+09 | power given |
| organism time over the line (% of steps) | 2.335 | 2.205 | -5.6% | -0.13 to -0.13 | GAIN |
| organism work per energy | 1.511 | 1.511 | -0.1% | -0.0008889 to -0.0008889 | power given |
| organism behind its window (s) | 2.179 | 3.038 | +39.4% | +0.6564 to +1.06 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 500 copies: GAIN on 3 (energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

23 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4554 | 3188 | -30.0% | -3050 to +317.8 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6408 | 5455 | -14.9% | -3159 to +1252 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 63.79 | 50.06 | -21.5% | -33.19 to +5.728 | STEADY, inside the noise (cut) |
| failed requests (%) | 49.2 | 41.71 | -15.2% | -25.58 to +10.6 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.913 | 12.14 | +22.5% | +1.063 to +3.394 | power given |
| pods started | 5.217 | 10.09 | +93.3% | +3.954 to +5.785 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001501 to +0.0006335 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1387 | 1373 | -1.0% | -27.23 to -0.1107 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1387 | 1373 | -1.0% | -27.28 to -0.1873 | GAIN |
| CPU used with Omni's own (cores), mean | 2.592 | 2.459 | -5.1% | -0.3159 to +0.05112 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 78.03 | 81 | +3.8% | -2.956 to +8.897 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.548 | 5.952 | +30.9% | +1.119 to +1.69 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

23 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4730 | 4258 | -10.0% | -1991 to +1048 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6715 | 6217 | -7.4% | -2159 to +1162 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 65.48 | 55.74 | -14.9% | -21.32 to +1.859 | STEADY, inside the noise (cut) |
| failed requests (%) | 52.65 | 45.48 | -13.6% | -16.65 to +2.319 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.913 | 13.77 | +38.9% | +2.512 to +5.192 | power given |
| pods started | 5.261 | 11.17 | +112.4% | +4.956 to +6.87 | power given |
| worker nodes in service, mean | 5.999 | 5.999 | -0.0% | -0.002084 to +0.001745 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1385 | 1375 | -0.7% | -18.68 to +0.2186 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1385 | 1375 | -0.7% | -18.71 to +0.2024 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.552 | 2.483 | -2.7% | -0.1958 to +0.05762 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.84 | 79.96 | +2.7% | -1.858 to +6.097 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.33 | 4.143 | +24.4% | +0.5564 to +1.07 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 5643 | 4905 | -13.1% | -2422 to +945.8 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 7806 | 6908 | -11.5% | -2780 to +983.8 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 70.79 | 62.56 | -11.6% | -24.02 to +7.565 | STEADY, inside the noise (cut) |
| failed requests (%) | 56.46 | 50.53 | -10.5% | -19.28 to +7.413 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.92 | 14.45 | +45.7% | +3.573 to +5.486 | power given |
| pods started | 4.92 | 12.12 | +146.3% | +5.588 to +8.812 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002398 to +0.0007016 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1387 | 1382 | -0.3% | -15.94 to +7.263 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1387 | 1382 | -0.3% | -16.07 to +7.144 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.585 | 2.569 | -0.6% | -0.1704 to +0.1383 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 79.69 | 83.62 | +4.9% | -1.291 to +9.144 | shown, not judged |
| organism work | 3.317e+13 | 3.317e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.512e+15 | 5.512e+15 | +0.0% | +4.35e+09 to +4.35e+09 | power given |
| organism time over the line (% of steps) | 1.469 | 1.382 | -5.9% | -0.0869 to -0.0869 | GAIN |
| organism work per energy | 0.006018 | 0.006018 | -0.0% | -4.749e-09 to -4.749e-09 | power given |
| organism behind its window (s) | 3.716 | 4.732 | +27.3% | +0.7814 to +1.251 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4104 | 3828 | -6.7% | -2326 to +1775 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6014 | 5645 | -6.1% | -3020 to +2282 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 58.78 | 48.31 | -17.8% | -32.24 to +11.3 | STEADY, inside the noise (cut) |
| failed requests (%) | 46.62 | 38.73 | -16.9% | -26.29 to +10.51 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.921 | 13.26 | +33.7% | +2.164 to +4.519 | power given |
| pods started | 5.48 | 10.36 | +89.1% | +3.986 to +5.774 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.00362 to +0.0005029 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1380 | 1373 | -0.5% | -22.57 to +8.542 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1380 | 1373 | -0.5% | -22.79 to +8.297 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.494 | 2.441 | -2.1% | -0.2625 to +0.1554 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.62 | 79.19 | +6.1% | -2.343 to +11.49 | shown, not judged |
| organism work | 1.082e+13 | 1.082e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.854e+13 | 2.855e+13 | +0.0% | +4.369e+09 to +4.369e+09 | power given |
| organism time over the line (% of steps) | 2.451 | 2.367 | -3.4% | -0.08396 to -0.08396 | GAIN |
| organism work per energy | 0.3789 | 0.3788 | -0.0% | -5.798e-05 to -5.798e-05 | power given |
| organism behind its window (s) | 3.928 | 5.172 | +31.7% | +1.049 to +1.439 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
