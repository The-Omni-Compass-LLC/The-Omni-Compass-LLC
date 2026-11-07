# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 10 copies: native | The spine, the muscles every stack runs on, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2863 | 3691 | 2615 | 3619 | 2681 | 2908 | 2051 | 2903 | 3049 | 3100 | 2507 | 3281 |
| response time (ms), 99th percentile | 5318 | 6513 | 5449 | 6477 | 5078 | 5468 | 4468 | 4953 | 5378 | 5384 | 4724 | 5257 |
| time over the response line (% of samples) | 42.97 | 41.26 | 45.92 | 44.81 | 38.69 | 36.07 | 33.97 | 31.66 | 47.89 | 44.93 | 35.83 | 36.13 |
| failed requests (%) | 27.58 | 27.59 | 30.17 | 29.95 | 24.04 | 24.55 | 19.1 | 19.77 | 29.14 | 29.51 | 15.97 | 19.35 |
| HPA replicas, mean | 9.619 | 14.19 | 9.685 | 14.19 | 9.61 | 14.11 | 9.626 | 13.29 | 9.698 | 12.36 | 9.675 | 13.14 |
| pods started | 5.195 | 11.15 | 4.293 | 10.24 | 5.146 | 11.05 | 5.098 | 11.22 | 4.366 | 9.146 | 4.585 | 9.951 |
| worker nodes in service, mean | 6 | 6 | 6 | 5.999 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 184.3 | 184.5 | 184.9 | 183.6 | 183.4 | 182.6 | 182.9 | 184.3 | 184.6 | 183.3 | 183.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 184.3 | 184.5 | 184.8 | 183.6 | 183.4 | 182.6 | 182.9 | 184.3 | 184.6 | 183.3 | 183.6 |
| CPU used with Omni's own (cores), mean | 2.377 | 2.42 | 2.426 | 2.472 | 2.293 | 2.338 | 2.225 | 2.276 | 2.41 | 2.445 | 2.322 | 2.384 |
| host CPU busy, the real machine under kind (%) | 69.98 | 71.69 | 71.9 | 73.88 | 67.9 | 69.79 | 65.47 | 67.57 | 71.57 | 73.97 | 69.22 | 73.56 |
| organism work | 2.148e+11 | 2.148e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0 | 0.004878 | 0.01707 | 0.007317 | 0.007317 | 0.009756 | 0.0122 | 0.09756 | 0.2366 | 0.1488 | 0.1537 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2863 | 3691 | +28.9% | +219.2 to +1437 | LOSS |
| response time (ms), 99th percentile | 5318 | 6513 | +22.5% | +542.5 to +1848 | LOSS |
| time over the response line (% of samples) | 42.97 | 41.26 | -4.0% | -2.792 to -0.6222 | GAIN |
| failed requests (%) | 27.58 | 27.59 | +0.1% | -0.9935 to +1.022 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.619 | 14.19 | +47.5% | +4.339 to +4.809 | power given |
| pods started | 5.195 | 11.15 | +114.6% | +5.215 to +6.688 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.292e-16 to +5.324e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 184.3 | +0.1% | -0.2665 to +0.8148 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 184.3 | +0.1% | -0.2665 to +0.8148 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.377 | 2.42 | +1.8% | +0.03305 to +0.05229 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.98 | 71.69 | +2.4% | +1.477 to +1.949 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2615 | 3619 | +38.4% | +422 to +1587 | LOSS |
| response time (ms), 99th percentile | 5449 | 6477 | +18.9% | +315.1 to +1740 | LOSS |
| time over the response line (% of samples) | 45.92 | 44.81 | -2.4% | -2.19 to -0.02346 | GAIN |
| failed requests (%) | 30.17 | 29.95 | -0.7% | -1.416 to +0.9732 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.685 | 14.19 | +46.5% | +4.264 to +4.744 | power given |
| pods started | 4.293 | 10.24 | +138.6% | +5.353 to +6.55 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002732 to +0.0009233 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.5 | 184.9 | +0.2% | -0.1185 to +0.9074 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.5 | 184.8 | +0.2% | -0.1388 to +0.8911 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.426 | 2.472 | +1.9% | +0.03709 to +0.05571 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.9 | 73.88 | +2.7% | +1.719 to +2.232 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.004878 | 0.01707 | +250.0% | -0.0004203 to +0.02481 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2681 | 2908 | +8.5% | -427.4 to +881.3 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5078 | 5468 | +7.7% | -99.75 to +879.8 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 38.69 | 36.07 | -6.8% | -3.695 to -1.54 | GAIN |
| failed requests (%) | 24.04 | 24.55 | +2.1% | -0.7089 to +1.739 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.61 | 14.11 | +46.8% | +4.229 to +4.766 | power given |
| pods started | 5.146 | 11.05 | +114.7% | +5.334 to +6.471 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.7e-16 to +1.367e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.6 | 183.4 | -0.1% | -0.6703 to +0.2882 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.6 | 183.4 | -0.1% | -0.6703 to +0.2882 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.293 | 2.338 | +1.9% | +0.03355 to +0.05576 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.9 | 69.79 | +2.8% | +1.606 to +2.176 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.007317 | 0.007317 | +0.0% | -0.009981 to +0.009981 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2051 | 2903 | +41.6% | +224.5 to +1480 | LOSS |
| response time (ms), 99th percentile | 4468 | 4953 | +10.9% | -129.9 to +1100 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 33.97 | 31.66 | -6.8% | -3.755 to -0.8586 | GAIN |
| failed requests (%) | 19.1 | 19.77 | +3.5% | -0.5344 to +1.885 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.626 | 13.29 | +38.1% | +3.158 to +4.176 | power given |
| pods started | 5.098 | 11.22 | +120.1% | +5.486 to +6.758 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.235e-16 to +1.769e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.6 | 182.9 | +0.2% | -0.09466 to +0.7535 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.6 | 182.9 | +0.2% | -0.09466 to +0.7535 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.225 | 2.276 | +2.3% | +0.03623 to +0.06597 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.47 | 67.57 | +3.2% | +1.653 to +2.543 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.009756 | 0.0122 | +25.0% | -0.01251 to +0.01739 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3049 | 3100 | +1.7% | -451 to +554.7 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5378 | 5384 | +0.1% | -624.4 to +636.8 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 47.89 | 44.93 | -6.2% | -4.387 to -1.529 | GAIN |
| failed requests (%) | 29.14 | 29.51 | +1.3% | -1.707 to +2.441 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.698 | 12.36 | +27.4% | +2.038 to +3.28 | power given |
| pods started | 4.366 | 9.146 | +109.5% | +4.136 to +5.425 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.192e-16 to +3.325e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 184.6 | +0.2% | -0.09826 to +0.6716 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.3 | 184.6 | +0.2% | -0.09826 to +0.6716 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.41 | 2.445 | +1.5% | +0.02732 to +0.04305 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.57 | 73.97 | +3.3% | +2.136 to +2.65 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.09756 | 0.2366 | +142.5% | +0.1068 to +0.1713 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2507 | 3281 | +30.9% | +327.4 to +1222 | LOSS |
| response time (ms), 99th percentile | 4724 | 5257 | +11.3% | -29.62 to +1096 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 35.83 | 36.13 | +0.8% | -1.492 to +2.099 | STEADY, inside the noise (up) |
| failed requests (%) | 15.97 | 19.35 | +21.1% | +2.08 to +4.671 | LOSS |
| HPA replicas, mean | 9.675 | 13.14 | +35.8% | +2.766 to +4.169 | power given |
| pods started | 4.585 | 9.951 | +117.0% | +4.607 to +6.125 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.092e-16 to +4.659e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.3 | 183.6 | +0.2% | -0.1306 to +0.7287 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.3 | 183.6 | +0.2% | -0.1306 to +0.7287 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.322 | 2.384 | +2.7% | +0.04977 to +0.07485 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.22 | 73.56 | +6.3% | +4.001 to +4.68 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1488 | 0.1537 | +3.3% | -0.01848 to +0.02823 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
