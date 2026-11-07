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
| response time (ms), 95th percentile | 2722 | 3078 | 3396 | 3808 | 2485 | 3108 | 2640 | 3465 | 3010 | 3064 | 2441 | 3539 |
| response time (ms), 99th percentile | 4638 | 5085 | 6210 | 6579 | 4452 | 5545 | 5425 | 6002 | 5430 | 5539 | 4416 | 5460 |
| time over the response line (% of samples) | 32.41 | 31.63 | 42.67 | 41.81 | 33.62 | 32.87 | 40.39 | 36.5 | 40.94 | 38.59 | 40.24 | 41.03 |
| failed requests (%) | 19.68 | 19.91 | 27.79 | 28.22 | 20.99 | 21.87 | 21.2 | 21.5 | 23.03 | 23.07 | 19.85 | 23.81 |
| HPA replicas, mean | 9.556 | 14.21 | 9.666 | 14.16 | 9.591 | 14.17 | 9.641 | 13.39 | 9.659 | 12.36 | 9.695 | 12.55 |
| pods started | 5.78 | 11.93 | 4.561 | 10.51 | 5.39 | 11.56 | 5.244 | 11.34 | 4.854 | 10.41 | 4.317 | 9.39 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 182.7 | 182.9 | 184.2 | 184.4 | 182.8 | 183.1 | 184.2 | 184.5 | 183.6 | 184 | 183.9 | 183.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.7 | 182.9 | 184.2 | 184.4 | 182.8 | 183.1 | 184.2 | 184.5 | 183.6 | 184 | 183.9 | 183.6 |
| CPU used with Omni's own (cores), mean | 2.239 | 2.285 | 2.398 | 2.446 | 2.24 | 2.282 | 2.368 | 2.426 | 2.341 | 2.386 | 2.332 | 2.382 |
| host CPU busy, the real machine under kind (%) | 65.82 | 67.62 | 70.78 | 72.68 | 66.23 | 67.97 | 69.2 | 71.71 | 69.3 | 72.06 | 69.85 | 73.9 |
| organism work | 2.148e+11 | 2.148e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0 | 0.002439 | 0.007317 | 0.004878 | 0.01463 | 0.009756 | 0.01463 | 0.8439 | 0.2317 | 0.1634 | 0.161 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2722 | 3078 | +13.1% | -271.4 to +984.2 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4638 | 5085 | +9.7% | -98.76 to +994.2 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 32.41 | 31.63 | -2.4% | -1.763 to +0.2182 | STEADY, inside the noise (cut) |
| failed requests (%) | 19.68 | 19.91 | +1.2% | -0.7882 to +1.246 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.556 | 14.21 | +48.7% | +4.379 to +4.925 | power given |
| pods started | 5.78 | 11.93 | +106.3% | +5.453 to +6.84 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.933e-16 to +5.676e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.7 | 182.9 | +0.1% | -0.3303 to +0.6296 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.7 | 182.9 | +0.1% | -0.3303 to +0.6296 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.239 | 2.285 | +2.1% | +0.03324 to +0.05953 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.82 | 67.62 | +2.7% | +1.379 to +2.23 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3396 | 3808 | +12.1% | -375.4 to +1199 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6210 | 6579 | +6.0% | -271.1 to +1010 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 42.67 | 41.81 | -2.0% | -1.795 to +0.07513 | STEADY, inside the noise (cut) |
| failed requests (%) | 27.79 | 28.22 | +1.5% | -0.4292 to +1.281 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.666 | 14.16 | +46.4% | +4.259 to +4.719 | power given |
| pods started | 4.561 | 10.51 | +130.5% | +5.264 to +6.639 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.671e-16 to +1.172e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.4 | +0.1% | -0.2933 to +0.6951 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.4 | +0.1% | -0.2933 to +0.6951 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.398 | 2.446 | +2.0% | +0.0396 to +0.05748 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.78 | 72.68 | +2.7% | +1.714 to +2.102 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.002439 | 0.007317 | +200.0% | -0.00498 to +0.01474 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2485 | 3108 | +25.0% | -13.32 to +1258 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4452 | 5545 | +24.6% | +445.9 to +1741 | LOSS |
| time over the response line (% of samples) | 33.62 | 32.87 | -2.3% | -1.462 to -0.05569 | GAIN |
| failed requests (%) | 20.99 | 21.87 | +4.2% | +0.1099 to +1.648 | LOSS |
| HPA replicas, mean | 9.591 | 14.17 | +47.8% | +4.336 to +4.825 | power given |
| pods started | 5.39 | 11.56 | +114.5% | +5.524 to +6.817 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.426e-16 to -1.105e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.8 | 183.1 | +0.2% | -0.1674 to +0.7245 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.8 | 183.1 | +0.2% | -0.1674 to +0.7245 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.24 | 2.282 | +1.9% | +0.03099 to +0.05268 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.23 | 67.97 | +2.6% | +1.376 to +2.098 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.004878 | 0.01463 | +200.0% | -0.002064 to +0.02158 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2640 | 3465 | +31.3% | +199.5 to +1451 | LOSS |
| response time (ms), 99th percentile | 5425 | 6002 | +10.6% | -3.575 to +1157 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 40.39 | 36.5 | -9.6% | -5.337 to -2.444 | GAIN |
| failed requests (%) | 21.2 | 21.5 | +1.4% | -0.7309 to +1.344 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.641 | 13.39 | +38.9% | +3.172 to +4.33 | power given |
| pods started | 5.244 | 11.34 | +116.3% | +5.429 to +6.766 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.347e-16 to -1.318e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.5 | +0.2% | -0.1249 to +0.8198 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.5 | +0.2% | -0.1249 to +0.8198 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.368 | 2.426 | +2.5% | +0.04637 to +0.0697 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.2 | 71.71 | +3.6% | +2.2 to +2.809 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.009756 | 0.01463 | +50.0% | -0.01083 to +0.02058 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3010 | 3064 | +1.8% | -409.8 to +516.3 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5430 | 5539 | +2.0% | -402.7 to +620.7 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 40.94 | 38.59 | -5.8% | -3.642 to -1.066 | GAIN |
| failed requests (%) | 23.03 | 23.07 | +0.2% | -0.8979 to +0.9798 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.659 | 12.36 | +28.0% | +2.08 to +3.323 | power given |
| pods started | 4.854 | 10.41 | +114.6% | +4.941 to +6.18 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.335e-16 to +3.601e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.6 | 184 | +0.2% | -0.1165 to +0.8474 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.6 | 184 | +0.2% | -0.1165 to +0.8474 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.341 | 2.386 | +1.9% | +0.03397 to +0.05529 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.3 | 72.06 | +4.0% | +2.44 to +3.096 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.8439 | 0.2317 | -72.5% | -2.128 to +0.9032 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2441 | 3539 | +45.0% | +597.2 to +1598 | LOSS |
| response time (ms), 99th percentile | 4416 | 5460 | +23.6% | +386.8 to +1701 | LOSS |
| time over the response line (% of samples) | 40.24 | 41.03 | +2.0% | -0.844 to +2.439 | STEADY, inside the noise (up) |
| failed requests (%) | 19.85 | 23.81 | +20.0% | +2.372 to +5.558 | LOSS |
| HPA replicas, mean | 9.695 | 12.55 | +29.4% | +2.154 to +3.548 | power given |
| pods started | 4.317 | 9.39 | +117.5% | +4.305 to +5.841 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.237e-16 to +4.671e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.9 | 183.6 | -0.1% | -0.6189 to +0.1472 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.9 | 183.6 | -0.1% | -0.6189 to +0.1472 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.332 | 2.382 | +2.2% | +0.04299 to +0.05838 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.85 | 73.9 | +5.8% | +3.822 to +4.293 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1634 | 0.161 | -1.5% | -0.02175 to +0.01687 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
