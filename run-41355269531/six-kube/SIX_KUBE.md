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
| response time (ms), 95th percentile | 4734 | 3039 | 4393 | 3598 | 3391 | 4264 | 6250 | 3412 | 3729 | 5684 |
| response time (ms), 99th percentile | 6671 | 4863 | 6212 | 5721 | 5457 | 5866 | 8664 | 5637 | 5116 | 7265 |
| time over the response line (% of samples) | 60.32 | 33.35 | 59.96 | 59.32 | 57.12 | 52.95 | 77.45 | 51.15 | 51.78 | 57.18 |
| failed requests (%) | 48.49 | 19.45 | 47.59 | 51.66 | 45.83 | 42.44 | 62.09 | 43.02 | 41.45 | 44.7 |
| HPA replicas, mean | 9.913 | 12.46 | 9.91 | 10.05 | 9.901 | 10.41 | 9.928 | 11.8 | 9.916 | 10.86 |
| pods started | 4.8 | 9.3 | 5.2 | 6.2 | 5.6 | 6.9 | 4.7 | 8 | 5.6 | 6.556 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 5.999 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 1380 | 1369 | 1381 | 1381 | 1381 | 1377 | 1391 | 1376 | 1375 | 1381 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1380 | 1369 | 1381 | 1381 | 1381 | 1377 | 1391 | 1376 | 1375 | 1381 |
| CPU used with Omni's own (cores), mean | 2.495 | 2.36 | 2.511 | 2.509 | 2.506 | 2.457 | 2.65 | 2.454 | 2.427 | 2.514 |
| host CPU busy, the real machine under kind (%) | 73.87 | 72.02 | 75.64 | 82.62 | 75.57 | 79.12 | 81.86 | 79.84 | 72.57 | 80.8 |
| organism work | 1.044e+13 | 1.044e+13 | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 3.317e+13 | 3.317e+13 | 1.082e+13 | 1.082e+13 |
| organism energy (J) | 6.905e+12 | 6.909e+12 | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 5.512e+15 | 5.512e+15 | 2.854e+13 | 2.855e+13 |
| organism time over the line (% of steps) | 2.335 | 2.205 | 1.943 | 1.874 | 4.602 | 4.511 | 1.469 | 1.382 | 2.451 | 2.367 |
| organism work per energy | 1.511 | 1.511 | 1.375 | 1.374 | 1.116 | 1.115 | 0.006018 | 0.006018 | 0.3789 | 0.3788 |
| organism behind its window (s) | 2.15 | 2.85 | 4.35 | 5.98 | 3.07 | 4.01 | 3.66 | 4.62 | 3.94 | 5.289 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 500 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4734 | 3039 | -35.8% | -3706 to +317.6 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6671 | 4863 | -27.1% | -4837 to +1221 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 60.32 | 33.35 | -44.7% | -51.97 to -1.957 | GAIN |
| failed requests (%) | 48.49 | 19.45 | -59.9% | -51.61 to -6.473 | GAIN |
| HPA replicas, mean | 9.913 | 12.46 | +25.7% | +0.855 to +4.239 | power given |
| pods started | 4.8 | 9.3 | +93.8% | +2.708 to +6.292 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.0008136 to +0.0003148 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1380 | 1369 | -0.8% | -35.71 to +14.06 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1380 | 1369 | -0.8% | -35.74 to +14.01 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.495 | 2.36 | -5.4% | -0.4679 to +0.199 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.87 | 72.02 | -2.5% | -11.68 to +7.999 | shown, not judged |
| organism work | 1.044e+13 | 1.044e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 6.905e+12 | 6.909e+12 | +0.1% | +4.063e+09 to +4.063e+09 | power given |
| organism time over the line (% of steps) | 2.335 | 2.205 | -5.6% | -0.13 to -0.13 | GAIN |
| organism work per energy | 1.511 | 1.511 | -0.1% | -0.0008889 to -0.0008889 | power given |
| organism behind its window (s) | 2.15 | 2.85 | +32.6% | +0.4454 to +0.9546 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 2 (organism energy (J); organism work per energy), STEADY (inside the noise) on 8

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4393 | 3598 | -18.1% | -3218 to +1626 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6212 | 5721 | -7.9% | -3497 to +2516 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 59.96 | 59.32 | -1.1% | -25.52 to +24.23 | STEADY, inside the noise (cut) |
| failed requests (%) | 47.59 | 51.66 | +8.6% | -18.19 to +26.33 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.91 | 10.05 | +1.5% | -0.3196 to +0.6089 | STEADY, inside the noise (up) |
| pods started | 5.2 | 6.2 | +19.2% | -1.432 to +3.432 | STEADY, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.471e-16 to +8.471e-16 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 1381 | 1381 | +0.0% | -21.97 to +22.12 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1381 | 1381 | +0.0% | -21.97 to +22.12 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.511 | 2.509 | -0.1% | -0.2929 to +0.289 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.64 | 82.62 | +9.2% | -2.166 to +16.13 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.35 | 5.98 | +37.5% | +1.306 to +1.954 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 2 (organism energy (J); organism work per energy), STEADY (inside the noise) on 8

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3391 | 4264 | +25.7% | -1915 to +3660 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5457 | 5866 | +7.5% | -2980 to +3796 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 57.12 | 52.95 | -7.3% | -34.43 to +26.1 | STEADY, inside the noise (cut) |
| failed requests (%) | 45.83 | 42.44 | -7.4% | -27.66 to +20.88 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.901 | 10.41 | +5.1% | -0.5088 to +1.525 | STEADY, inside the noise (up) |
| pods started | 5.6 | 6.9 | +23.2% | -1.377 to +3.977 | STEADY, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.062e-16 to +7.615e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 1381 | 1377 | -0.3% | -28.71 to +20.67 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1381 | 1377 | -0.3% | -28.71 to +20.67 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.506 | 2.457 | -2.0% | -0.3805 to +0.2824 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.57 | 79.12 | +4.7% | -6.575 to +13.68 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.07 | 4.01 | +30.6% | +0.8043 to +1.076 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 500 copies: GAIN on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 6250 | 3412 | -45.4% | -4575 to -1101 | GAIN |
| response time (ms), 99th percentile | 8664 | 5637 | -34.9% | -5442 to -612.9 | GAIN |
| time over the response line (% of samples) | 77.45 | 51.15 | -33.9% | -50.28 to -2.304 | GAIN |
| failed requests (%) | 62.09 | 43.02 | -30.7% | -41.85 to +3.729 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.928 | 11.8 | +18.9% | +0.06306 to +3.682 | power given |
| pods started | 4.7 | 8 | +70.2% | +0.8673 to +5.733 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002921 to +0.0008138 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1391 | 1376 | -1.1% | -34.46 to +3.695 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1391 | 1376 | -1.1% | -34.57 to +3.494 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.65 | 2.454 | -7.4% | -0.4532 to +0.06162 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 81.86 | 79.84 | -2.5% | -10.05 to +6.01 | shown, not judged |
| organism work | 3.317e+13 | 3.317e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.512e+15 | 5.512e+15 | +0.0% | +4.35e+09 to +4.35e+09 | power given |
| organism time over the line (% of steps) | 1.469 | 1.382 | -5.9% | -0.0869 to -0.0869 | GAIN |
| organism work per energy | 0.006018 | 0.006018 | -0.0% | -4.749e-09 to -4.749e-09 | power given |
| organism behind its window (s) | 3.66 | 4.62 | +26.2% | +0.6397 to +1.28 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 2 (organism energy (J); organism work per energy), STEADY (inside the noise) on 8

9 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4108 | 5684 | +38.3% | -562 to +3712 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5631 | 7265 | +29.0% | -988.6 to +4256 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 57.44 | 57.18 | -0.5% | -25.83 to +25.3 | STEADY, inside the noise (cut) |
| failed requests (%) | 46.06 | 44.7 | -3.0% | -22.15 to +19.42 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.923 | 10.86 | +9.4% | -0.172 to +2.044 | STEADY, inside the noise (up) |
| pods started | 5.444 | 6.556 | +20.4% | -0.4941 to +2.716 | STEADY, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.087e-16 to +1.096e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 1379 | 1381 | +0.1% | -22.36 to +25.52 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1379 | 1381 | +0.1% | -22.36 to +25.52 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.486 | 2.514 | +1.2% | -0.287 to +0.3442 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.32 | 80.8 | +8.7% | -2.181 to +15.16 | shown, not judged |
| organism work | 1.082e+13 | 1.082e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.854e+13 | 2.855e+13 | +0.0% | +4.369e+09 to +4.369e+09 | power given |
| organism time over the line (% of steps) | 2.451 | 2.367 | -3.4% | -0.08396 to -0.08396 | GAIN |
| organism work per energy | 0.3789 | 0.3788 | -0.0% | -5.798e-05 to -5.798e-05 | power given |
| organism behind its window (s) | 3.956 | 5.289 | +33.7% | +0.9471 to +1.72 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
