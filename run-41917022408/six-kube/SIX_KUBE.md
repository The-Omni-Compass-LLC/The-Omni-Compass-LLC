# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 10 copies: native | The spine, the muscles every stack runs on, 10 copies: omni | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2609 | 4021 | 2119 | 2728 | 2565 | 3205 | 2090 | 2723 | 2516 | 3953 | 2914 | 3028 | 2015 | 3354 |
| response time (ms), 99th percentile | 4697 | 6729 | 4397 | 5237 | 4610 | 5690 | 3973 | 4829 | 5109 | 6182 | 5215 | 5196 | 3983 | 5162 |
| time over the response line (% of samples) | 41.79 | 40.44 | 32.49 | 30.63 | 41.79 | 40.65 | 31.23 | 30.33 | 41.45 | 38.71 | 39.62 | 36.41 | 46.6 | 49.45 |
| failed requests (%) | 27 | 25.77 | 14.7 | 15.84 | 27.9 | 28.62 | 19.82 | 19.7 | 22.86 | 23.56 | 21.94 | 22.63 | 26.4 | 29.31 |
| HPA replicas, mean | 9.632 | 14.19 | 9.644 | 13.81 | 9.654 | 14.05 | 9.58 | 14.39 | 9.65 | 13.54 | 9.632 | 12.43 | 9.748 | 11.88 |
| pods started | 5.2 | 11.43 | 5.114 | 10.94 | 4.629 | 10.31 | 5.429 | 11.46 | 4.886 | 11.03 | 5.229 | 10.4 | 3.543 | 8.286 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 5.998 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 5.993 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.5 | 183 | 183.3 | 183.5 | 184 | 182.6 | 182.5 | 184 | 184.5 | 183.7 | 184.2 | 184.3 | 184.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.5 | 183 | 183.3 | 183.5 | 184 | 182.6 | 182.5 | 184 | 184.5 | 183.7 | 184.2 | 184.1 | 184.9 |
| CPU used with Omni's own (cores), mean | 2.37 | 2.425 | 2.266 | 2.317 | 2.332 | 2.386 | 2.206 | 2.257 | 2.363 | 2.422 | 2.334 | 2.37 | 2.417 | 2.47 |
| host CPU busy, the real machine under kind (%) | 69.79 | 71.82 | 66.48 | 68.85 | 69.47 | 71.32 | 65.42 | 67.53 | 69.17 | 71.6 | 69.12 | 71.41 | 72.55 | 76.74 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.002857 | 0 | 0.002857 | 0.008571 | 0.01143 | 0.01714 | 0.01143 | 0.008571 | 0.005714 | 0.005714 | 0.1 | 0.2057 | 0.1686 | 0.1971 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2609 | 4021 | +54.1% | +712.4 to +2111 | LOSS |
| response time (ms), 99th percentile | 4697 | 6729 | +43.3% | +1233 to +2831 | LOSS |
| time over the response line (% of samples) | 41.79 | 40.44 | -3.2% | -2.31 to -0.3922 | GAIN |
| failed requests (%) | 27 | 25.77 | -4.6% | -2.054 to -0.4065 | GAIN |
| HPA replicas, mean | 9.632 | 14.19 | +47.3% | +4.28 to +4.834 | power given |
| pods started | 5.2 | 11.43 | +119.8% | +5.25 to +7.207 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.24e-16 to -1.403e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.5 | +0.2% | -0.2495 to +0.8833 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.5 | +0.2% | -0.2495 to +0.8833 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.37 | 2.425 | +2.4% | +0.04729 to +0.06415 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.79 | 71.82 | +2.9% | +1.803 to +2.259 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0.002857 | 0 | -100.0% | -0.008663 to +0.002949 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2119 | 2728 | +28.7% | +232.8 to +984.6 | LOSS |
| response time (ms), 99th percentile | 4397 | 5237 | +19.1% | +225.7 to +1455 | LOSS |
| time over the response line (% of samples) | 32.49 | 30.63 | -5.7% | -3.111 to -0.6164 | GAIN |
| failed requests (%) | 14.7 | 15.84 | +7.7% | +0.3049 to +1.971 | LOSS |
| HPA replicas, mean | 9.644 | 13.81 | +43.2% | +3.671 to +4.662 | power given |
| pods started | 5.114 | 10.94 | +114.0% | +5.319 to +6.339 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.205e-16 to +1.084e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183 | 183.3 | +0.2% | -0.1347 to +0.7168 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183 | 183.3 | +0.2% | -0.1347 to +0.7168 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.266 | 2.317 | +2.2% | +0.03952 to +0.0616 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.48 | 68.85 | +3.6% | +2.037 to +2.713 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.002857 | 0.008571 | +200.0% | -0.005897 to +0.01733 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2565 | 3205 | +24.9% | -43.94 to +1323 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4610 | 5690 | +23.4% | +285 to +1875 | LOSS |
| time over the response line (% of samples) | 41.79 | 40.65 | -2.7% | -2.182 to -0.1073 | GAIN |
| failed requests (%) | 27.9 | 28.62 | +2.6% | -0.5401 to +1.983 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.654 | 14.05 | +45.6% | +4.136 to +4.665 | power given |
| pods started | 4.629 | 10.31 | +122.8% | +5.147 to +6.224 | power given |
| worker nodes in service, mean | 5.998 | 6 | +0.0% | -0.002115 to +0.006213 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 184 | +0.3% | +0.01227 to +0.9646 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 184 | +0.3% | +0.0505 to +1.01 | power given |
| CPU used with Omni's own (cores), mean | 2.332 | 2.386 | +2.3% | +0.04237 to +0.06567 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.47 | 71.32 | +2.7% | +1.499 to +2.202 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.01143 | 0.01714 | +50.0% | -0.008576 to +0.02 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2090 | 2723 | +30.3% | +75.13 to +1192 | LOSS |
| response time (ms), 99th percentile | 3973 | 4829 | +21.5% | +201.3 to +1510 | LOSS |
| time over the response line (% of samples) | 31.23 | 30.33 | -2.9% | -2.015 to +0.204 | STEADY, inside the noise (cut) |
| failed requests (%) | 19.82 | 19.7 | -0.6% | -0.7844 to +0.555 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.58 | 14.39 | +50.2% | +4.603 to +5.011 | power given |
| pods started | 5.429 | 11.46 | +111.1% | +5.381 to +6.676 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.031e-16 to +1.986e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.6 | 182.5 | -0.1% | -0.7354 to +0.3806 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.6 | 182.5 | -0.1% | -0.7354 to +0.3806 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.206 | 2.257 | +2.3% | +0.03728 to +0.06544 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.42 | 67.53 | +3.2% | +1.663 to +2.543 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.01143 | 0.008571 | -25.0% | -0.01841 to +0.0127 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2516 | 3953 | +57.2% | +658.3 to +2217 | LOSS |
| response time (ms), 99th percentile | 5109 | 6182 | +21.0% | +403.2 to +1741 | LOSS |
| time over the response line (% of samples) | 41.45 | 38.71 | -6.6% | -4.453 to -1.029 | GAIN |
| failed requests (%) | 22.86 | 23.56 | +3.1% | -0.5613 to +1.972 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.65 | 13.54 | +40.3% | +3.408 to +4.37 | power given |
| pods started | 4.886 | 11.03 | +125.7% | +5.374 to +6.912 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.348e-16 to +2.84e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 184.5 | +0.2% | -0.1406 to +1.01 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 184.5 | +0.2% | -0.1406 to +1.01 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.363 | 2.422 | +2.5% | +0.04238 to +0.07468 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.17 | 71.6 | +3.5% | +1.978 to +2.876 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.005714 | 0.005714 | +0.0% | -0.01178 to +0.01178 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2914 | 3028 | +3.9% | -501.7 to +728.8 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5215 | 5196 | -0.4% | -578.2 to +540.4 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 39.62 | 36.41 | -8.1% | -4.764 to -1.656 | GAIN |
| failed requests (%) | 21.94 | 22.63 | +3.2% | -0.3656 to +1.761 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.632 | 12.43 | +29.1% | +2.153 to +3.449 | power given |
| pods started | 5.229 | 10.4 | +98.9% | +4.727 to +5.616 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.54e-16 to +2.495e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 184.2 | +0.3% | +0.09234 to +0.8821 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 184.2 | +0.3% | +0.09234 to +0.8821 | power given |
| CPU used with Omni's own (cores), mean | 2.334 | 2.37 | +1.5% | +0.0248 to +0.047 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.12 | 71.41 | +3.3% | +1.908 to +2.677 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.1 | 0.2057 | +105.7% | +0.08917 to +0.1223 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2015 | 3354 | +66.5% | +782.6 to +1897 | LOSS |
| response time (ms), 99th percentile | 3983 | 5162 | +29.6% | +450.8 to +1907 | LOSS |
| time over the response line (% of samples) | 46.6 | 49.45 | +6.1% | +0.6972 to +5 | LOSS |
| failed requests (%) | 26.4 | 29.31 | +11.0% | +1.136 to +4.693 | LOSS |
| HPA replicas, mean | 9.748 | 11.88 | +21.8% | +1.324 to +2.936 | power given |
| pods started | 3.543 | 8.286 | +133.9% | +3.973 to +5.512 | power given |
| worker nodes in service, mean | 5.993 | 6 | +0.1% | -0.006924 to +0.02034 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 184.9 | +0.3% | +0.1 to +1.103 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.9 | +0.4% | +0.08577 to +1.389 | power given |
| CPU used with Omni's own (cores), mean | 2.417 | 2.47 | +2.2% | +0.03859 to +0.06792 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.55 | 76.74 | +5.8% | +3.765 to +4.607 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1686 | 0.1971 | +16.9% | -0.000965 to +0.05811 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
