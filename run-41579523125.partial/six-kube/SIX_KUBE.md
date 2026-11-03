# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 100 copies: native | The spine, the muscles every stack runs on, 100 copies: omni | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3767 | 3154 | 3966 | 3675 | 3797 | 2948 | 3770 | 3269 | 3042 | 2945 |
| response time (ms), 99th percentile | 5782 | 5566 | 5674 | 5426 | 5886 | 5613 | 6132 | 5734 | 5046 | 5142 |
| time over the response line (% of samples) | 53.92 | 53.13 | 52.1 | 51.49 | 54.47 | 53.56 | 57.37 | 55.93 | 50.22 | 49.45 |
| failed requests (%) | 38.7 | 42.53 | 38.05 | 39.74 | 38.15 | 42.55 | 41.36 | 43.81 | 38.95 | 38.05 |
| HPA replicas, mean | 9.805 | 12.58 | 9.802 | 11.58 | 9.799 | 11.81 | 9.824 | 11.42 | 9.785 | 11.71 |
| pods started | 4.1 | 8.918 | 4.18 | 7.3 | 4.32 | 8.94 | 3.74 | 7.06 | 4.56 | 8.04 |
| worker nodes in service, mean | 6 | 5.998 | 6 | 6 | 6 | 6 | 6 | 6 | 5.999 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.8 | 276.5 | 275.9 | 276 | 276.9 | 276.7 | 277.2 | 277.1 | 276 | 276.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.8 | 276.4 | 275.9 | 276 | 276.9 | 276.7 | 277.2 | 277.1 | 276 | 276.2 |
| CPU used with Omni's own (cores), mean | 2.434 | 2.47 | 2.402 | 2.457 | 2.46 | 2.505 | 2.461 | 2.509 | 2.417 | 2.459 |
| host CPU busy, the real machine under kind (%) | 72.08 | 76.35 | 72.87 | 81.02 | 75.11 | 80.64 | 75.78 | 82.11 | 73 | 80.43 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.428 | 0.5 | 0.88 | 1.148 | 0.59 | 0.416 | 0.712 | 0.436 | 0.498 | 1.046 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

49 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3774 | 3154 | -16.4% | -1318 to +78.64 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5766 | 5566 | -3.5% | -799.5 to +398.3 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 53.51 | 53.13 | -0.7% | -1.487 to +0.7393 | STEADY, inside the noise (cut) |
| failed requests (%) | 38.27 | 42.53 | +11.1% | +2.289 to +6.225 | LOSS |
| HPA replicas, mean | 9.803 | 12.58 | +28.3% | +2.193 to +3.365 | power given |
| pods started | 4.122 | 8.918 | +116.3% | +4.115 to +5.477 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.006301 to +0.001389 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.8 | 276.5 | -0.1% | -0.7748 to +0.193 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.8 | 276.4 | -0.1% | -0.8707 to +0.141 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.429 | 2.47 | +1.7% | +0.03021 to +0.05092 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.94 | 76.35 | +6.1% | +4.111 to +4.704 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.4286 | 0.5 | +16.7% | +0.03826 to +0.1046 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3966 | 3675 | -7.3% | -906.4 to +324.3 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5674 | 5426 | -4.4% | -828.7 to +333.1 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 52.1 | 51.49 | -1.2% | -1.6 to +0.3808 | STEADY, inside the noise (cut) |
| failed requests (%) | 38.05 | 39.74 | +4.4% | -0.6626 to +4.03 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.802 | 11.58 | +18.1% | +1.084 to +2.469 | power given |
| pods started | 4.18 | 7.3 | +74.6% | +2.261 to +3.979 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +2.405e-16 to +1.11e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.9 | 276 | +0.0% | -0.4173 to +0.5283 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.9 | 276 | +0.0% | -0.4173 to +0.5283 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.402 | 2.457 | +2.3% | +0.0367 to +0.07488 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.87 | 81.02 | +11.2% | +7.731 to +8.576 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.88 | 1.148 | +30.5% | +0.1997 to +0.3363 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 2 (response time (ms), 95th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3797 | 2948 | -22.4% | -1481 to -218.6 | GAIN |
| response time (ms), 99th percentile | 5886 | 5613 | -4.6% | -920.7 to +374.6 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 54.47 | 53.56 | -1.7% | -2.295 to +0.4841 | STEADY, inside the noise (cut) |
| failed requests (%) | 38.15 | 42.55 | +11.5% | +2.271 to +6.524 | LOSS |
| HPA replicas, mean | 9.799 | 11.81 | +20.6% | +1.403 to +2.626 | power given |
| pods started | 4.32 | 8.94 | +106.9% | +3.445 to +5.795 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.789e-16 to +7.119e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.9 | 276.7 | -0.1% | -0.6122 to +0.1655 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.9 | 276.7 | -0.1% | -0.6122 to +0.1655 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.46 | 2.505 | +1.8% | +0.0319 to +0.0583 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.11 | 80.64 | +7.4% | +5.176 to +5.898 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.59 | 0.416 | -29.5% | -0.2266 to -0.1214 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3770 | 3269 | -13.3% | -1056 to +55.07 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6132 | 5734 | -6.5% | -925.7 to +129.8 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 57.37 | 55.93 | -2.5% | -2.58 to -0.3055 | GAIN |
| failed requests (%) | 41.36 | 43.81 | +5.9% | +0.8634 to +4.049 | LOSS |
| HPA replicas, mean | 9.824 | 11.42 | +16.2% | +0.9895 to +2.193 | power given |
| pods started | 3.74 | 7.06 | +88.8% | +2.271 to +4.369 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +6.71e-17 to +9.277e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.2 | 277.1 | -0.0% | -0.4634 to +0.43 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.2 | 277.1 | -0.0% | -0.4634 to +0.43 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.461 | 2.509 | +2.0% | +0.03352 to +0.06298 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.78 | 82.11 | +8.4% | +5.964 to +6.702 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | power given |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | power given |
| organism behind its window (s) | 0.712 | 0.436 | -38.8% | -0.3192 to -0.2328 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3042 | 2945 | -3.2% | -715.3 to +521.7 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5046 | 5142 | +1.9% | -593.2 to +785.1 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 50.22 | 49.45 | -1.5% | -1.812 to +0.2728 | STEADY, inside the noise (cut) |
| failed requests (%) | 38.95 | 38.05 | -2.3% | -2.743 to +0.9396 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.785 | 11.71 | +19.6% | +1.231 to +2.611 | power given |
| pods started | 4.56 | 8.04 | +76.3% | +2.446 to +4.514 | power given |
| worker nodes in service, mean | 5.999 | 6 | +0.0% | -0.001092 to +0.002081 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 276 | 276.2 | +0.1% | -0.213 to +0.6044 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276 | 276.2 | +0.1% | -0.1995 to +0.6208 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.417 | 2.459 | +1.8% | +0.02746 to +0.05735 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73 | 80.43 | +10.2% | +7.038 to +7.82 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.498 | 1.046 | +110.0% | +0.4925 to +0.6035 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
