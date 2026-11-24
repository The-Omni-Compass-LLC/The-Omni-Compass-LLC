# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 10 copies: native | The spine, the muscles every stack runs on, 10 copies: omni | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2744 | 4196 | 2499 | 3694 | 1708 | 2993 | 2861 | 4048 | 2723 | 3282 | 3164 | 2856 | 2237 | 2953 |
| response time (ms), 99th percentile | 5862 | 7034 | 5161 | 6246 | 3487 | 5096 | 5708 | 6897 | 5238 | 5800 | 5746 | 5019 | 4076 | 4825 |
| time over the response line (% of samples) | 44.06 | 42 | 38.24 | 35.64 | 38.81 | 39.18 | 45.78 | 45.45 | 43.47 | 37.33 | 46.64 | 42.28 | 39.9 | 39.88 |
| failed requests (%) | 26.27 | 25.34 | 17.81 | 17.39 | 27.04 | 26.77 | 30.24 | 30.56 | 24.16 | 23.63 | 27.67 | 28.48 | 20.34 | 23.07 |
| HPA replicas, mean | 9.666 | 14.32 | 9.644 | 14.33 | 9.663 | 14.33 | 9.667 | 14.1 | 9.651 | 13.18 | 9.677 | 12.14 | 9.665 | 12.29 |
| pods started | 4.8 | 10.67 | 5.333 | 11.4 | 4.4 | 10.53 | 4.667 | 10.33 | 4.933 | 10.73 | 4.533 | 9.133 | 4.733 | 8.667 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.8 | 185.1 | 184.6 | 185 | 182.7 | 182.7 | 184.9 | 184.9 | 184 | 184.7 | 184.1 | 184.1 | 183.3 | 182.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.8 | 185.1 | 184.6 | 185 | 182.7 | 182.7 | 184.9 | 184.9 | 184 | 184.7 | 184.1 | 184.1 | 183.3 | 182.7 |
| CPU used with Omni's own (cores), mean | 2.434 | 2.482 | 2.43 | 2.475 | 2.264 | 2.31 | 2.424 | 2.473 | 2.385 | 2.443 | 2.358 | 2.404 | 2.262 | 2.298 |
| host CPU busy, the real machine under kind (%) | 72.13 | 74.15 | 71.23 | 73.67 | 67.62 | 69.75 | 72.22 | 74.28 | 70.16 | 72.75 | 70.54 | 73.3 | 68.2 | 71.94 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0.006667 | 0 | 0.06667 | 0.006667 | 0.006667 | 0.01333 | 0.006667 | 0 | 0.03333 | 0.1 | 0.1 | 0.1667 | 0.1733 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

15 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2744 | 4196 | +52.9% | -8.712 to +2912 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5862 | 7034 | +20.0% | -348.8 to +2693 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 44.06 | 42 | -4.7% | -3.717 to -0.3895 | GAIN |
| failed requests (%) | 26.27 | 25.34 | -3.5% | -3.231 to +1.367 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.666 | 14.32 | +48.1% | +4.292 to +5.01 | power given |
| pods started | 4.8 | 10.67 | +122.2% | +4.982 to +6.751 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.531e-16 to +4.979e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.8 | 185.1 | +0.2% | -0.6144 to +1.195 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.8 | 185.1 | +0.2% | -0.6144 to +1.195 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.434 | 2.482 | +2.0% | +0.03789 to +0.05862 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.13 | 74.15 | +2.8% | +1.786 to +2.257 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0.006667 | +0.00667 | -0.007633 to +0.02097 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

15 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2499 | 3694 | +47.8% | +81.47 to +2308 | LOSS |
| response time (ms), 99th percentile | 5161 | 6246 | +21.0% | -224.7 to +2396 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 38.24 | 35.64 | -6.8% | -5.02 to -0.184 | GAIN |
| failed requests (%) | 17.81 | 17.39 | -2.3% | -2.761 to +1.926 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.644 | 14.33 | +48.5% | +4.116 to +5.247 | power given |
| pods started | 5.333 | 11.4 | +113.8% | +5.12 to +7.014 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.323e-15 to -2.161e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.6 | 185 | +0.2% | -0.3489 to +1.186 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.6 | 185 | +0.2% | -0.3489 to +1.186 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.43 | 2.475 | +1.9% | +0.03444 to +0.0565 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.23 | 73.67 | +3.4% | +2.124 to +2.761 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0 | 0.06667 | +0.0667 | +0.03248 to +0.1009 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

15 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1708 | 2993 | +75.3% | +455.5 to +2115 | LOSS |
| response time (ms), 99th percentile | 3487 | 5096 | +46.1% | +582.9 to +2635 | LOSS |
| time over the response line (% of samples) | 38.81 | 39.18 | +1.0% | -0.74 to +1.488 | STEADY, inside the noise (up) |
| failed requests (%) | 27.04 | 26.77 | -1.0% | -0.9701 to +0.4229 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.663 | 14.33 | +48.3% | +4.303 to +5.031 | power given |
| pods started | 4.4 | 10.53 | +139.4% | +5.354 to +6.913 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.699e-15 to -3.143e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.7 | 182.7 | +0.0% | -0.6721 to +0.7211 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.7 | 182.7 | +0.0% | -0.6721 to +0.7211 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.264 | 2.31 | +2.0% | +0.0254 to +0.06572 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.62 | 69.75 | +3.2% | +1.607 to +2.657 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.006667 | 0.006667 | +0.0% | -0.02093 to +0.02093 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

15 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2861 | 4048 | +41.5% | +0.08849 to +2374 | LOSS |
| response time (ms), 99th percentile | 5708 | 6897 | +20.8% | -291.2 to +2669 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 45.78 | 45.45 | -0.7% | -2.372 to +1.728 | STEADY, inside the noise (cut) |
| failed requests (%) | 30.24 | 30.56 | +1.1% | -1.325 to +1.965 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.667 | 14.1 | +45.8% | +3.956 to +4.901 | power given |
| pods started | 4.667 | 10.33 | +121.4% | +4.952 to +6.382 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.198e-15 to +1.323e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.9 | 184.9 | +0.0% | -0.674 to +0.7431 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.9 | 184.9 | +0.0% | -0.674 to +0.7431 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.424 | 2.473 | +2.0% | +0.03914 to +0.05888 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.22 | 74.28 | +2.9% | +1.865 to +2.263 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.01333 | 0.006667 | -50.0% | -0.03202 to +0.01868 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

15 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2723 | 3282 | +20.5% | -589.7 to +1708 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5238 | 5800 | +10.7% | -842.9 to +1967 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 43.47 | 37.33 | -14.1% | -8.84 to -3.439 | GAIN |
| failed requests (%) | 24.16 | 23.63 | -2.2% | -2.267 to +1.201 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.651 | 13.18 | +36.6% | +2.401 to +4.66 | power given |
| pods started | 4.933 | 10.73 | +117.6% | +4.489 to +7.111 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.589e-16 to +5.22e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 184.7 | +0.4% | -0.09783 to +1.478 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 184.7 | +0.4% | -0.09783 to +1.478 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.385 | 2.443 | +2.5% | +0.04112 to +0.07645 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.16 | 72.75 | +3.7% | +2.004 to +3.164 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0 | 0.03333 | +0.0333 | +0.006309 to +0.06036 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

15 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3164 | 2856 | -9.7% | -829.6 to +213.3 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5746 | 5019 | -12.6% | -1637 to +184.6 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 46.64 | 42.28 | -9.3% | -6.439 to -2.275 | GAIN |
| failed requests (%) | 27.67 | 28.48 | +2.9% | -1.414 to +3.024 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.677 | 12.14 | +25.4% | +1.303 to +3.619 | power given |
| pods started | 4.533 | 9.133 | +101.5% | +3.742 to +5.458 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.485e-16 to +7.853e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 184.1 | -0.0% | -0.6714 to +0.6292 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.1 | -0.0% | -0.6714 to +0.6292 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.358 | 2.404 | +2.0% | +0.03409 to +0.05877 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.54 | 73.3 | +3.9% | +2.379 to +3.135 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.1 | 0.1 | +0.0% | -0.02093 to +0.02093 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

15 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2237 | 2953 | +32.0% | +99.95 to +1333 | LOSS |
| response time (ms), 99th percentile | 4076 | 4825 | +18.4% | -380.9 to +1879 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 39.9 | 39.88 | -0.1% | -2.921 to +2.864 | STEADY, inside the noise (cut) |
| failed requests (%) | 20.34 | 23.07 | +13.4% | +0.08463 to +5.382 | LOSS |
| HPA replicas, mean | 9.665 | 12.29 | +27.1% | +1.33 to +3.91 | power given |
| pods started | 4.733 | 8.667 | +83.1% | +2.009 to +5.857 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.058e-16 to +1.172e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.3 | 182.7 | -0.3% | -1.201 to +0.0964 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.3 | 182.7 | -0.3% | -1.201 to +0.0964 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.262 | 2.298 | +1.6% | +0.01585 to +0.05658 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.2 | 71.94 | +5.5% | +3.129 to +4.338 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1667 | 0.1733 | +4.0% | -0.02621 to +0.03954 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
