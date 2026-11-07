# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 10 copies: native | The spine, the muscles every stack runs on, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2719 | 3525 | 3114 | 3699 | 2398 | 3026 | 2464 | 3447 | 3293 | 2989 | 2582 | 3599 |
| response time (ms), 99th percentile | 5156 | 6396 | 5655 | 6483 | 4620 | 5126 | 5007 | 6058 | 5862 | 5478 | 4874 | 6013 |
| time over the response line (% of samples) | 44.82 | 42.9 | 40.24 | 38.32 | 35.34 | 33.3 | 42.62 | 39.69 | 42.35 | 39.72 | 40.84 | 42.55 |
| failed requests (%) | 29.12 | 28.51 | 25.58 | 25.58 | 22.03 | 22.82 | 24.61 | 26.34 | 23.1 | 23.18 | 19.87 | 23.28 |
| HPA replicas, mean | 9.637 | 14.22 | 9.63 | 14.17 | 9.571 | 14.11 | 9.66 | 13.1 | 9.659 | 12.21 | 9.709 | 12.51 |
| pods started | 4.951 | 10.56 | 5 | 11.22 | 5.537 | 11.46 | 4.878 | 10.85 | 4.902 | 9.634 | 4.268 | 9.634 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 5.999 | 6 | 5.997 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.6 | 183.8 | 184.1 | 182.8 | 182.9 | 183.5 | 184.4 | 184.1 | 184.3 | 184.4 | 184.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.6 | 183.8 | 184.1 | 182.8 | 182.9 | 183.5 | 184.4 | 184.1 | 184.3 | 184.4 | 184.4 |
| CPU used with Omni's own (cores), mean | 2.398 | 2.449 | 2.356 | 2.401 | 2.24 | 2.296 | 2.372 | 2.421 | 2.369 | 2.415 | 2.406 | 2.455 |
| host CPU busy, the real machine under kind (%) | 70.69 | 72.61 | 69.59 | 71.41 | 66.31 | 68.52 | 69.51 | 71.86 | 70.11 | 72.93 | 71.86 | 75.99 |
| organism work | 2.148e+11 | 2.148e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0.007317 | 0.002439 | 0.004878 | 0.007317 | 0.007317 | 0.6488 | 0.007317 | 0.09756 | 0.2293 | 0.1634 | 0.4829 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2719 | 3525 | +29.6% | +219.7 to +1392 | LOSS |
| response time (ms), 99th percentile | 5156 | 6396 | +24.1% | +600.7 to +1881 | LOSS |
| time over the response line (% of samples) | 44.82 | 42.9 | -4.3% | -3.145 to -0.6892 | GAIN |
| failed requests (%) | 29.12 | 28.51 | -2.1% | -1.77 to +0.5477 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.637 | 14.22 | +47.5% | +4.322 to +4.841 | power given |
| pods started | 4.951 | 10.56 | +113.3% | +5.175 to +6.044 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.633e-16 to +2.301e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.6 | +0.2% | -0.06538 to +0.9821 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.6 | +0.2% | -0.06538 to +0.9821 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.398 | 2.449 | +2.1% | +0.04332 to +0.05962 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.69 | 72.61 | +2.7% | +1.688 to +2.165 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0.007317 | +0.00732 | -0.001004 to +0.01564 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3114 | 3699 | +18.8% | -42.44 to +1213 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5655 | 6483 | +14.6% | +188.9 to +1466 | LOSS |
| time over the response line (% of samples) | 40.24 | 38.32 | -4.8% | -2.805 to -1.027 | GAIN |
| failed requests (%) | 25.58 | 25.58 | -0.0% | -1.015 to +1.012 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.63 | 14.17 | +47.1% | +4.302 to +4.777 | power given |
| pods started | 5 | 11.22 | +124.4% | +5.64 to +6.799 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.272e-16 to +2.24e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 184.1 | +0.1% | -0.3032 to +0.7349 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 184.1 | +0.1% | -0.3032 to +0.7349 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.356 | 2.401 | +1.9% | +0.03505 to +0.05403 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.59 | 71.41 | +2.6% | +1.508 to +2.134 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.002439 | 0.004878 | +100.0% | -0.00617 to +0.01105 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2398 | 3026 | +26.2% | -14.12 to +1271 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4620 | 5126 | +11.0% | -181 to +1193 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 35.34 | 33.3 | -5.8% | -3.037 to -1.038 | GAIN |
| failed requests (%) | 22.03 | 22.82 | +3.6% | -0.1744 to +1.761 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.571 | 14.11 | +47.4% | +4.272 to +4.806 | power given |
| pods started | 5.537 | 11.46 | +107.0% | +5.369 to +6.484 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.988e-16 to +2.089e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.8 | 182.9 | +0.1% | -0.3423 to +0.6395 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.8 | 182.9 | +0.1% | -0.3423 to +0.6395 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.24 | 2.296 | +2.5% | +0.0372 to +0.07382 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.31 | 68.52 | +3.3% | +1.674 to +2.729 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.007317 | 0.007317 | +0.0% | -0.009981 to +0.009981 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 0

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2464 | 3447 | +39.9% | +223.2 to +1744 | LOSS |
| response time (ms), 99th percentile | 5007 | 6058 | +21.0% | +503.2 to +1599 | LOSS |
| time over the response line (% of samples) | 42.62 | 39.69 | -6.9% | -4.882 to -0.9818 | GAIN |
| failed requests (%) | 24.61 | 26.34 | +7.0% | +0.3051 to +3.147 | LOSS |
| HPA replicas, mean | 9.66 | 13.1 | +35.6% | +2.867 to +4.019 | power given |
| pods started | 4.878 | 10.85 | +122.5% | +5.237 to +6.714 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.205e-16 to +3.772e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 184.4 | +0.5% | +0.1125 to +1.799 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 184.4 | +0.5% | +0.1125 to +1.799 | power given |
| CPU used with Omni's own (cores), mean | 2.372 | 2.421 | +2.1% | +0.03614 to +0.062 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.51 | 71.86 | +3.4% | +1.963 to +2.745 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.6488 | 0.007317 | -98.9% | -1.938 to +0.655 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3293 | 2989 | -9.2% | -702 to +93.99 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5862 | 5478 | -6.6% | -917.9 to +149.1 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 42.35 | 39.72 | -6.2% | -4.228 to -1.03 | GAIN |
| failed requests (%) | 23.1 | 23.18 | +0.3% | -0.8243 to +0.9758 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.659 | 12.21 | +26.4% | +1.925 to +3.172 | power given |
| pods started | 4.902 | 9.634 | +96.5% | +4.1 to +5.363 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002577 to +0.0008711 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 184.3 | +0.1% | -0.2016 to +0.6108 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.3 | +0.1% | -0.2113 to +0.586 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.369 | 2.415 | +1.9% | +0.03351 to +0.05842 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.11 | 72.93 | +4.0% | +2.447 to +3.181 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.09756 | 0.2293 | +135.0% | +0.09903 to +0.1644 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2582 | 3599 | +39.4% | +488.2 to +1545 | LOSS |
| response time (ms), 99th percentile | 4874 | 6013 | +23.4% | +464.8 to +1813 | LOSS |
| time over the response line (% of samples) | 40.84 | 42.55 | +4.2% | -0.1523 to +3.578 | STEADY, inside the noise (up) |
| failed requests (%) | 19.87 | 23.28 | +17.2% | +1.929 to +4.889 | LOSS |
| HPA replicas, mean | 9.709 | 12.51 | +28.9% | +2.043 to +3.568 | power given |
| pods started | 4.268 | 9.634 | +125.7% | +4.694 to +6.038 | power given |
| worker nodes in service, mean | 6 | 5.997 | -0.1% | -0.01044 to +0.003528 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184.5 | +0.1% | -0.2739 to +0.5217 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184.4 | +0.0% | -0.3786 to +0.4862 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.406 | 2.455 | +2.1% | +0.0386 to +0.06073 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.86 | 75.99 | +5.8% | +3.831 to +4.439 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1634 | 0.4829 | +195.5% | -0.2864 to +0.9255 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
