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
| response time (ms), 95th percentile | 2505 | 4107 | 2503 | 3706 | 4546 | 3925 | 3856 | 4555 | 3646 | 4497 |
| response time (ms), 99th percentile | 4299 | 6379 | 3991 | 6922 | 6620 | 5814 | 5306 | 6921 | 5353 | 7074 |
| time over the response line (% of samples) | 44.52 | 53.31 | 47.19 | 65.47 | 63.63 | 53.93 | 54.4 | 62.18 | 53.4 | 61.53 |
| failed requests (%) | 34.06 | 34.86 | 31.43 | 53.24 | 47.2 | 42.95 | 42.79 | 47.88 | 39.81 | 47.76 |
| HPA replicas, mean | 9.896 | 14.65 | 9.896 | 13.34 | 9.911 | 14.01 | 9.902 | 14.16 | 9.92 | 14.43 |
| pods started | 5.56 | 10.36 | 5.72 | 10.64 | 5.4 | 11.4 | 5.44 | 10.64 | 5.4 | 10.84 |
| worker nodes in service, mean | 6 | 6 | 6 | 5.999 | 6 | 5.999 | 6 | 5.999 | 6 | 5.998 |
| energy, parked workers still on at idle power (Wh, declared model) | 1377 | 1382 | 1381 | 1386 | 1385 | 1376 | 1375 | 1383 | 1381 | 1383 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1377 | 1382 | 1381 | 1386 | 1385 | 1376 | 1375 | 1383 | 1381 | 1383 |
| CPU used with Omni's own (cores), mean | 2.45 | 2.563 | 2.505 | 2.629 | 2.565 | 2.491 | 2.432 | 2.595 | 2.503 | 2.582 |
| host CPU busy, the real machine under kind (%) | 72.24 | 79.46 | 75.59 | 87.9 | 78.89 | 81.52 | 75.59 | 85.91 | 75.98 | 85.11 |
| organism work | 1.044e+13 | 1.044e+13 | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 3.317e+13 | 3.317e+13 | 1.082e+13 | 1.082e+13 |
| organism energy (J) | 6.905e+12 | 6.909e+12 | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 5.512e+15 | 5.512e+15 | 2.854e+13 | 2.855e+13 |
| organism time over the line (% of steps) | 2.335 | 2.205 | 1.943 | 1.874 | 4.602 | 4.511 | 1.469 | 1.382 | 2.451 | 2.367 |
| organism work per energy | 1.511 | 1.511 | 1.375 | 1.374 | 1.116 | 1.115 | 0.006018 | 0.006018 | 0.3789 | 0.3788 |
| organism behind its window (s) | 2.32 | 3.116 | 4.572 | 6.388 | 3.46 | 4.312 | 3.652 | 5.172 | 4.164 | 5.608 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2505 | 4107 | +64.0% | +30.58 to +3175 | LOSS |
| response time (ms), 99th percentile | 4299 | 6379 | +48.4% | -47.2 to +4207 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 44.52 | 53.31 | +19.7% | -9.201 to +26.77 | STEADY, inside the noise (up) |
| failed requests (%) | 34.06 | 34.86 | +2.3% | -15.6 to +17.19 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.896 | 14.65 | +48.1% | +3.923 to +5.588 | power given |
| pods started | 5.56 | 10.36 | +86.3% | +3.957 to +5.643 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -0.0003578 to +0.001079 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 1377 | 1382 | +0.4% | -9.793 to +19.66 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1377 | 1382 | +0.4% | -9.697 to +19.67 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.45 | 2.563 | +4.6% | -0.08349 to +0.3086 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.24 | 79.46 | +10.0% | +1.51 to +12.92 | shown, not judged |
| organism work | 1.044e+13 | 1.044e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 6.905e+12 | 6.909e+12 | +0.1% | +4.063e+09 to +4.063e+09 | power given |
| organism time over the line (% of steps) | 2.335 | 2.205 | -5.6% | -0.13 to -0.13 | GAIN |
| organism work per energy | 1.511 | 1.511 | -0.1% | -0.0008889 to -0.0008889 | power given |
| organism behind its window (s) | 2.32 | 3.116 | +34.3% | +0.6163 to +0.9757 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2503 | 3706 | +48.1% | -352.5 to +2759 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3991 | 6922 | +73.4% | +1040 to +4823 | LOSS |
| time over the response line (% of samples) | 47.19 | 65.47 | +38.7% | +1.687 to +34.88 | LOSS |
| failed requests (%) | 31.43 | 53.24 | +69.4% | +5.593 to +38.01 | LOSS |
| HPA replicas, mean | 9.896 | 13.34 | +34.8% | +2.754 to +4.142 | power given |
| pods started | 5.72 | 10.64 | +86.0% | +3.688 to +6.152 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002383 to +0.0002849 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1381 | 1386 | +0.4% | -5.55 to +16.95 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1381 | 1386 | +0.4% | -5.715 to +16.8 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.505 | 2.629 | +5.0% | -0.02502 to +0.2739 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.59 | 87.9 | +16.3% | +7.475 to +17.14 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.572 | 6.388 | +39.7% | +1.489 to +2.143 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4546 | 3925 | -13.7% | -2166 to +923.4 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6620 | 5814 | -12.2% | -2766 to +1155 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 63.63 | 53.93 | -15.3% | -27.39 to +7.977 | STEADY, inside the noise (cut) |
| failed requests (%) | 47.2 | 42.95 | -9.0% | -19.9 to +11.4 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.911 | 14.01 | +41.4% | +3.175 to +5.023 | power given |
| pods started | 5.4 | 11.4 | +111.1% | +4.652 to +7.348 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002029 to +0.0004433 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1385 | 1376 | -0.7% | -22.92 to +4.667 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1385 | 1376 | -0.7% | -22.98 to +4.491 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.565 | 2.491 | -2.9% | -0.2596 to +0.1128 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 78.89 | 81.52 | +3.3% | -3.254 to +8.504 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.46 | 4.312 | +24.6% | +0.565 to +1.139 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3856 | 4555 | +18.1% | -1245 to +2643 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5306 | 6921 | +30.4% | -684.2 to +3913 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 54.4 | 62.18 | +14.3% | -12.88 to +28.45 | STEADY, inside the noise (up) |
| failed requests (%) | 42.79 | 47.88 | +11.9% | -12.12 to +22.31 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.902 | 14.16 | +43.0% | +3.353 to +5.17 | power given |
| pods started | 5.44 | 10.64 | +95.6% | +3.75 to +6.65 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.004133 to +0.001614 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1375 | 1383 | +0.6% | -6.561 to +22.02 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1375 | 1383 | +0.5% | -6.719 to +21.8 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.432 | 2.595 | +6.7% | -0.034 to +0.3603 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.59 | 85.91 | +13.7% | +3.67 to +16.98 | shown, not judged |
| organism work | 3.317e+13 | 3.317e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.512e+15 | 5.512e+15 | +0.0% | +4.35e+09 to +4.35e+09 | power given |
| organism time over the line (% of steps) | 1.469 | 1.382 | -5.9% | -0.0869 to -0.0869 | GAIN |
| organism work per energy | 0.006018 | 0.006018 | -0.0% | -4.749e-09 to -4.749e-09 | power given |
| organism behind its window (s) | 3.652 | 5.172 | +41.6% | +1.198 to +1.842 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3646 | 4497 | +23.3% | -724.7 to +2426 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5353 | 7074 | +32.2% | -363.1 to +3807 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 53.4 | 61.53 | +15.2% | -11.71 to +27.96 | STEADY, inside the noise (up) |
| failed requests (%) | 39.81 | 47.76 | +20.0% | -10.17 to +26.06 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.92 | 14.43 | +45.4% | +3.726 to +5.287 | power given |
| pods started | 5.4 | 10.84 | +100.7% | +4.45 to +6.43 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.005192 to +0.0007297 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1381 | 1383 | +0.2% | -10.66 to +15.62 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1381 | 1383 | +0.2% | -10.83 to +15.12 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.503 | 2.582 | +3.2% | -0.1021 to +0.2602 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.98 | 85.11 | +12.0% | +3.16 to +15.1 | shown, not judged |
| organism work | 1.082e+13 | 1.082e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.854e+13 | 2.855e+13 | +0.0% | +4.369e+09 to +4.369e+09 | power given |
| organism time over the line (% of steps) | 2.451 | 2.367 | -3.4% | -0.08396 to -0.08396 | GAIN |
| organism work per energy | 0.3789 | 0.3788 | -0.0% | -5.798e-05 to -5.798e-05 | power given |
| organism behind its window (s) | 4.164 | 5.608 | +34.7% | +1.163 to +1.725 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
