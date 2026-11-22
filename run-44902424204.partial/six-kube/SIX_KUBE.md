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
| response time (ms), 95th percentile | 4115 | 4629 | 2461 | 2439 | 2351 | 4296 | 4259 | 3933 | 3067 | 4705 |
| response time (ms), 99th percentile | 6110 | 6830 | 4148 | 5304 | 3474 | 6313 | 6044 | 5829 | 4961 | 6785 |
| time over the response line (% of samples) | 63.28 | 58.07 | 48.72 | 48.81 | 39.87 | 50.09 | 65.26 | 52.6 | 56.99 | 59.63 |
| failed requests (%) | 48.7 | 41.78 | 35.59 | 38.81 | 29.04 | 35.95 | 51.67 | 38.53 | 43.52 | 45.66 |
| HPA replicas, mean | 9.917 | 14.74 | 9.896 | 13.84 | 9.886 | 13.23 | 9.916 | 14.36 | 9.922 | 14.24 |
| pods started | 5.04 | 10.76 | 5.68 | 10.56 | 5.92 | 11.08 | 5 | 11.32 | 5.36 | 12 |
| worker nodes in service, mean | 6 | 5.996 | 6 | 5.999 | 6 | 6 | 6 | 5.998 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 1390 | 1380 | 1380 | 1379 | 1369 | 1376 | 1387 | 1376 | 1385 | 1381 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1390 | 1379 | 1380 | 1379 | 1369 | 1376 | 1387 | 1376 | 1385 | 1380 |
| CPU used with Omni's own (cores), mean | 2.629 | 2.569 | 2.503 | 2.532 | 2.35 | 2.482 | 2.579 | 2.492 | 2.563 | 2.553 |
| host CPU busy, the real machine under kind (%) | 77.85 | 80.17 | 75.66 | 84.48 | 71.55 | 80.63 | 79.99 | 82.43 | 77.21 | 84.38 |
| organism work | 1.044e+13 | 1.044e+13 | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 3.317e+13 | 3.317e+13 | 1.082e+13 | 1.082e+13 |
| organism energy (J) | 6.905e+12 | 6.909e+12 | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 5.512e+15 | 5.512e+15 | 2.854e+13 | 2.855e+13 |
| organism time over the line (% of steps) | 2.335 | 2.205 | 1.943 | 1.874 | 4.602 | 4.511 | 1.469 | 1.382 | 2.451 | 2.367 |
| organism work per energy | 1.511 | 1.511 | 1.375 | 1.374 | 1.116 | 1.115 | 0.006018 | 0.006018 | 0.3789 | 0.3788 |
| organism behind its window (s) | 2.256 | 3.076 | 4.656 | 6.276 | 3.328 | 4.188 | 3.868 | 5.068 | 4.26 | 5.58 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 500 copies: GAIN on 2 (energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4115 | 4629 | +12.5% | -1192 to +2220 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6110 | 6830 | +11.8% | -1343 to +2782 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 63.28 | 58.07 | -8.2% | -20.55 to +10.13 | STEADY, inside the noise (cut) |
| failed requests (%) | 48.7 | 41.78 | -14.2% | -21.28 to +7.429 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.917 | 14.74 | +48.6% | +4.135 to +5.51 | power given |
| pods started | 5.04 | 10.76 | +113.5% | +5.106 to +6.334 | power given |
| worker nodes in service, mean | 6 | 5.996 | -0.1% | -0.01001 to +0.001913 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1390 | 1380 | -0.7% | -20.17 to +0.149 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1390 | 1379 | -0.8% | -20.77 to -0.4649 | GAIN |
| CPU used with Omni's own (cores), mean | 2.629 | 2.569 | -2.3% | -0.1934 to +0.07309 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.85 | 80.17 | +3.0% | -1.813 to +6.467 | shown, not judged |
| organism work | 1.044e+13 | 1.044e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 6.905e+12 | 6.909e+12 | +0.1% | +4.063e+09 to +4.063e+09 | power given |
| organism time over the line (% of steps) | 2.335 | 2.205 | -5.6% | -0.13 to -0.13 | GAIN |
| organism work per energy | 1.511 | 1.511 | -0.1% | -0.0008889 to -0.0008889 | power given |
| organism behind its window (s) | 2.256 | 3.076 | +36.3% | +0.6078 to +1.032 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2461 | 2439 | -0.9% | -1292 to +1249 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4148 | 5304 | +27.9% | -624.4 to +2936 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 48.72 | 48.81 | +0.2% | -16.95 to +17.14 | STEADY, inside the noise (up) |
| failed requests (%) | 35.59 | 38.81 | +9.1% | -13.75 to +20.19 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.896 | 13.84 | +39.8% | +2.894 to +4.988 | power given |
| pods started | 5.68 | 10.56 | +85.9% | +3.954 to +5.806 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001621 to +0.0009992 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1380 | 1379 | -0.1% | -13.57 to +11.53 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1380 | 1379 | -0.1% | -13.62 to +11.5 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.503 | 2.532 | +1.2% | -0.1363 to +0.1944 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.66 | 84.48 | +11.7% | +3.806 to +13.83 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.656 | 6.276 | +34.8% | +1.354 to +1.886 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2351 | 4296 | +82.7% | +211.8 to +3678 | LOSS |
| response time (ms), 99th percentile | 3474 | 6313 | +81.7% | +613 to +5065 | LOSS |
| time over the response line (% of samples) | 39.87 | 50.09 | +25.6% | -10.52 to +30.95 | STEADY, inside the noise (up) |
| failed requests (%) | 29.04 | 35.95 | +23.8% | -10.81 to +24.62 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.886 | 13.23 | +33.8% | +2.286 to +4.402 | power given |
| pods started | 5.92 | 11.08 | +87.2% | +3.862 to +6.458 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.0008258 to +0.0001606 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1369 | 1376 | +0.5% | -8.396 to +22.28 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1369 | 1376 | +0.5% | -8.422 to +22.21 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.35 | 2.482 | +5.6% | -0.07343 to +0.3389 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.55 | 80.63 | +12.7% | +2.28 to +15.88 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.328 | 4.188 | +25.8% | +0.5236 to +1.196 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4259 | 3933 | -7.7% | -2159 to +1507 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6044 | 5829 | -3.6% | -2349 to +1919 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 65.26 | 52.6 | -19.4% | -30 to +4.686 | STEADY, inside the noise (cut) |
| failed requests (%) | 51.67 | 38.53 | -25.4% | -26.68 to +0.4124 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.916 | 14.36 | +44.8% | +3.534 to +5.359 | power given |
| pods started | 5 | 11.32 | +126.4% | +5.569 to +7.071 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.003284 to +0.000254 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1387 | 1376 | -0.7% | -22.33 to +1.611 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1387 | 1376 | -0.8% | -22.53 to +1.364 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.579 | 2.492 | -3.4% | -0.2485 to +0.07487 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 79.99 | 82.43 | +3.0% | -2.899 to +7.779 | shown, not judged |
| organism work | 3.317e+13 | 3.317e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.512e+15 | 5.512e+15 | +0.0% | +4.35e+09 to +4.35e+09 | power given |
| organism time over the line (% of steps) | 1.469 | 1.382 | -5.9% | -0.0869 to -0.0869 | GAIN |
| organism work per energy | 0.006018 | 0.006018 | -0.0% | -4.749e-09 to -4.749e-09 | power given |
| organism behind its window (s) | 3.868 | 5.068 | +31.0% | +0.8969 to +1.503 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3067 | 4705 | +53.4% | -110.8 to +3386 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4961 | 6785 | +36.8% | -356.4 to +4005 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 56.99 | 59.63 | +4.6% | -15.48 to +20.76 | STEADY, inside the noise (up) |
| failed requests (%) | 43.52 | 45.66 | +4.9% | -14.4 to +18.67 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.922 | 14.24 | +43.5% | +3.466 to +5.172 | power given |
| pods started | 5.36 | 12 | +123.9% | +4.723 to +8.557 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.001091 to +0.0002707 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1385 | 1381 | -0.3% | -17.72 to +8.392 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1385 | 1380 | -0.3% | -17.78 to +8.335 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.563 | 2.553 | -0.4% | -0.1855 to +0.1661 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.21 | 84.38 | +9.3% | +1.583 to +12.77 | shown, not judged |
| organism work | 1.082e+13 | 1.082e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.854e+13 | 2.855e+13 | +0.0% | +4.369e+09 to +4.369e+09 | power given |
| organism time over the line (% of steps) | 2.451 | 2.367 | -3.4% | -0.08396 to -0.08396 | GAIN |
| organism work per energy | 0.3789 | 0.3788 | -0.0% | -5.798e-05 to -5.798e-05 | power given |
| organism behind its window (s) | 4.26 | 5.58 | +31.0% | +1.044 to +1.596 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
