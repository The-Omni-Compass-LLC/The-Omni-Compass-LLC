# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 500 copies: native | The spine, the muscles every stack runs on, 500 copies: omni | Compute / AI / Cloud, 500 copies: native | Compute / AI / Cloud, 500 copies: omni | Physics / Robotics / Autonomous, 500 copies: native | Physics / Robotics / Autonomous, 500 copies: omni | Energy / Facility / Industrial, 500 copies: native | Energy / Facility / Industrial, 500 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 5538 | 2715 | 5604 | 3330 | 4679 | 5060 | 4217 | 4848 |
| response time (ms), 99th percentile | 7728 | 4045 | 8148 | 6643 | 6776 | 7257 | 5807 | 7034 |
| time over the response line (% of samples) | 69.1 | 33.38 | 74.86 | 66.23 | 64.16 | 66.93 | 60.01 | 60.61 |
| failed requests (%) | 53.04 | 23.79 | 60.05 | 57.97 | 47.56 | 52.59 | 49.15 | 49.53 |
| HPA replicas, mean | 9.925 | 13.36 | 9.926 | 13.34 | 9.912 | 15.64 | 9.905 | 14.16 |
| pods started | 4.6 | 11.3 | 4.889 | 10.38 | 5.2 | 11.2 | 5.5 | 11.11 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 5.999 |
| energy, parked workers still on at idle power (Wh, declared model) | 1391 | 1365 | 1393 | 1385 | 1387 | 1387 | 1378 | 1380 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1391 | 1365 | 1393 | 1385 | 1387 | 1387 | 1378 | 1380 |
| CPU used with Omni's own (cores), mean | 2.643 | 2.328 | 2.666 | 2.606 | 2.581 | 2.649 | 2.47 | 2.538 |
| host CPU busy, the real machine under kind (%) | 77.91 | 71.71 | 80.36 | 85.91 | 78.37 | 84.86 | 75.55 | 83.12 |
| organism work | 1.044e+13 | 1.044e+13 | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 3.317e+13 | 3.317e+13 |
| organism energy (J) | 6.905e+12 | 6.909e+12 | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 5.512e+15 | 5.512e+15 |
| organism time over the line (% of steps) | 2.335 | 2.205 | 1.943 | 1.874 | 4.602 | 4.511 | 1.469 | 1.382 |
| organism work per energy | 1.511 | 1.511 | 1.375 | 1.374 | 1.116 | 1.115 | 0.006018 | 0.006018 |
| organism behind its window (s) | 2.28 | 2.74 | 4.611 | 5.838 | 3.37 | 4.08 | 3.44 | 4.811 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 500 copies: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 5538 | 2715 | -51.0% | -5826 to +180.4 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 7728 | 4045 | -47.7% | -7462 to +97.15 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 69.1 | 33.38 | -51.7% | -69.24 to -2.203 | GAIN |
| failed requests (%) | 53.04 | 23.79 | -55.1% | -59.45 to +0.9547 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.925 | 13.36 | +34.6% | +0.6727 to +6.198 | power given |
| pods started | 4.6 | 11.3 | +145.7% | +5.482 to +7.918 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +3.452e-16 to +1.609e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 1391 | 1365 | -1.9% | -48.66 to -4.442 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1391 | 1365 | -1.9% | -48.66 to -4.442 | GAIN |
| CPU used with Omni's own (cores), mean | 2.643 | 2.328 | -11.9% | -0.6211 to -0.007829 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.91 | 71.71 | -8.0% | -15.72 to +3.31 | shown, not judged |
| organism work | 1.044e+13 | 1.044e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 6.905e+12 | 6.909e+12 | +0.1% | +4.063e+09 to +4.063e+09 | power given |
| organism time over the line (% of steps) | 2.335 | 2.205 | -5.6% | -0.13 to -0.13 | GAIN |
| organism work per energy | 1.511 | 1.511 | -0.1% | -0.0008889 to -0.0008889 | power given |
| organism behind its window (s) | 2.28 | 2.74 | +20.2% | +0.1599 to +0.7601 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 5479 | 3330 | -39.2% | -4686 to +387.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 8010 | 6643 | -17.1% | -4356 to +1621 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 74.49 | 66.23 | -11.1% | -33.56 to +17.05 | STEADY, inside the noise (cut) |
| failed requests (%) | 59.68 | 57.97 | -2.9% | -26.05 to +22.63 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.927 | 13.34 | +34.4% | +1.302 to +5.528 | power given |
| pods started | 4.875 | 10.38 | +112.8% | +4.018 to +6.982 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.346e-16 to +2.011e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 1393 | 1385 | -0.6% | -22.86 to +6.872 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1393 | 1385 | -0.6% | -22.86 to +6.872 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.667 | 2.606 | -2.3% | -0.2499 to +0.1271 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 80.31 | 85.91 | +7.0% | -0.9561 to +12.15 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.65 | 5.838 | +25.5% | +0.4974 to +1.878 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4679 | 5060 | +8.1% | -3181 to +3943 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6776 | 7257 | +7.1% | -3338 to +4300 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 64.16 | 66.93 | +4.3% | -26.03 to +31.58 | STEADY, inside the noise (up) |
| failed requests (%) | 47.56 | 52.59 | +10.6% | -22.69 to +32.77 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.912 | 15.64 | +57.8% | +5.486 to +5.977 | power given |
| pods started | 5.2 | 11.2 | +115.4% | +4.569 to +7.431 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.0008715 to +0.0008159 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1387 | 1387 | +0.0% | -15.11 to +15.71 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1387 | 1387 | +0.0% | -15.08 to +15.67 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.581 | 2.649 | +2.6% | -0.1378 to +0.2731 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 78.37 | 84.86 | +8.3% | -0.4699 to +13.44 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.37 | 4.08 | +21.1% | +0.241 to +1.179 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

9 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4654 | 4848 | +4.2% | -2913 to +3302 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6404 | 7034 | +9.8% | -3735 to +4996 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 66.63 | 60.61 | -9.0% | -43.08 to +31.02 | STEADY, inside the noise (cut) |
| failed requests (%) | 54.61 | 49.53 | -9.3% | -37.46 to +27.29 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.913 | 14.16 | +42.8% | +2.443 to +6.041 | power given |
| pods started | 5.333 | 11.11 | +108.3% | +2.076 to +9.48 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002602 to +0.001028 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1384 | 1380 | -0.3% | -31.08 to +23.05 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1384 | 1380 | -0.3% | -31.21 to +22.94 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.547 | 2.538 | -0.4% | -0.3655 to +0.3467 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.96 | 83.12 | +6.6% | -7.257 to +17.58 | shown, not judged |
| organism work | 3.317e+13 | 3.317e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.512e+15 | 5.512e+15 | +0.0% | +4.35e+09 to +4.35e+09 | power given |
| organism time over the line (% of steps) | 1.469 | 1.382 | -5.9% | -0.0869 to -0.0869 | GAIN |
| organism work per energy | 0.006018 | 0.006018 | -0.0% | -4.749e-09 to -4.749e-09 | power given |
| organism behind its window (s) | 3.478 | 4.811 | +38.3% | +0.733 to +1.934 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Distribution / Specialized
- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
