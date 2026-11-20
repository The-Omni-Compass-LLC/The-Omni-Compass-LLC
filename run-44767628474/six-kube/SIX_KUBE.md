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
| response time (ms), 95th percentile | 3860 | 2456 | 1719 | 2744 | 1925 | 2663 | 1726 | 3575 | 2515 | 2588 | 4132 | 4594 | 2616 | 3651 |
| response time (ms), 99th percentile | 5470 | 4791 | 3078 | 4700 | 4379 | 4800 | 4751 | 5978 | 4694 | 4897 | 7316 | 6958 | 5155 | 5757 |
| time over the response line (% of samples) | 30.24 | 29.06 | 44.73 | 43.19 | 40.9 | 41.06 | 42.69 | 41.55 | 33.29 | 30.13 | 65.6 | 61.55 | 38.88 | 40.48 |
| failed requests (%) | 17.48 | 17.5 | 27.53 | 26.73 | 27.86 | 28.68 | 29.94 | 30.34 | 15.91 | 17.05 | 41.68 | 41.33 | 16.74 | 21.3 |
| HPA replicas, mean | 9.585 | 14.47 | 9.67 | 13.26 | 9.659 | 14.26 | 9.679 | 13.56 | 9.653 | 13.33 | 9.767 | 11.77 | 9.754 | 13.15 |
| pods started | 5.2 | 12.4 | 4.9 | 10.2 | 4.5 | 9.9 | 4.3 | 9.4 | 4.9 | 12.6 | 3.5 | 6.8 | 3.6 | 9.6 |
| worker nodes in service, mean | 6 | 6 | 5.996 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 182.9 | 181.5 | 184.8 | 184.8 | 183.5 | 183.2 | 183.4 | 182.9 | 183 | 183.6 | 186.4 | 186.8 | 184.2 | 184.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.9 | 181.5 | 184.8 | 184.8 | 183.5 | 183.2 | 183.4 | 182.9 | 183 | 183.6 | 186.4 | 186.8 | 184.2 | 184.3 |
| CPU used with Omni's own (cores), mean | 2.187 | 2.217 | 2.39 | 2.437 | 2.321 | 2.367 | 2.29 | 2.338 | 2.284 | 2.325 | 2.613 | 2.659 | 2.351 | 2.408 |
| host CPU busy, the real machine under kind (%) | 64.13 | 65.6 | 70.52 | 72.73 | 69.25 | 71.18 | 68.89 | 70.68 | 67.13 | 69.26 | 78.02 | 80.47 | 70.6 | 75.05 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0 | 0.05 | 0.01 | 0 | 0 | 0 | 0.01 | 0.01 | 0 | 0.1 | 0.14 | 0.15 | 0.17 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 3 (energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3860 | 2456 | -36.4% | -2994 to +186.3 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5470 | 4791 | -12.4% | -1360 to +2.504 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 30.24 | 29.06 | -3.9% | -2.485 to +0.1106 | STEADY, inside the noise (cut) |
| failed requests (%) | 17.48 | 17.5 | +0.1% | -2.652 to +2.699 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.585 | 14.47 | +51.0% | +4.659 to +5.119 | power given |
| pods started | 5.2 | 12.4 | +138.5% | +6.2 to +8.2 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.216e-15 to +1.5e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.9 | 181.5 | -0.8% | -2.114 to -0.8201 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.9 | 181.5 | -0.8% | -2.114 to -0.8201 | GAIN |
| CPU used with Omni's own (cores), mean | 2.187 | 2.217 | +1.4% | -0.006879 to +0.06864 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.13 | 65.6 | +2.3% | +0.5707 to +2.357 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1719 | 2744 | +59.6% | -166.1 to +2216 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3078 | 4700 | +52.7% | +100.2 to +3145 | LOSS |
| time over the response line (% of samples) | 44.73 | 43.19 | -3.4% | -4.632 to +1.568 | STEADY, inside the noise (cut) |
| failed requests (%) | 27.53 | 26.73 | -2.9% | -4.243 to +2.651 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.67 | 13.26 | +37.1% | +2.063 to +5.117 | power given |
| pods started | 4.9 | 10.2 | +108.2% | +3.908 to +6.692 | power given |
| worker nodes in service, mean | 5.996 | 6 | +0.1% | -0.00534 to +0.0138 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.8 | 184.8 | -0.0% | -0.9335 to +0.7701 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.8 | 184.8 | +0.0% | -0.9507 to +0.9581 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.39 | 2.437 | +1.9% | +0.03942 to +0.05297 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.52 | 72.73 | +3.1% | +1.942 to +2.491 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.05 | 0.01 | -80.0% | -0.07694 to -0.003062 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1925 | 2663 | +38.3% | -378.9 to +1855 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4379 | 4800 | +9.6% | -832.6 to +1673 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 40.9 | 41.06 | +0.4% | -1.769 to +2.097 | STEADY, inside the noise (up) |
| failed requests (%) | 27.86 | 28.68 | +3.0% | -0.717 to +2.368 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.659 | 14.26 | +47.7% | +3.951 to +5.258 | power given |
| pods started | 4.5 | 9.9 | +120.0% | +4.129 to +6.671 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.116e-15 to +5.833e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 183.2 | -0.2% | -1.251 to +0.5309 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 183.2 | -0.2% | -1.251 to +0.5309 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.321 | 2.367 | +2.0% | +0.02865 to +0.06359 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.25 | 71.18 | +2.8% | +1.543 to +2.321 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1726 | 3575 | +107.1% | +585.8 to +3112 | LOSS |
| response time (ms), 99th percentile | 4751 | 5978 | +25.8% | -521.7 to +2975 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 42.69 | 41.55 | -2.7% | -3.626 to +1.342 | STEADY, inside the noise (cut) |
| failed requests (%) | 29.94 | 30.34 | +1.3% | -1.374 to +2.182 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.679 | 13.56 | +40.1% | +3.261 to +4.495 | power given |
| pods started | 4.3 | 9.4 | +118.6% | +3.863 to +6.337 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.436e-16 to +8.989e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.4 | 182.9 | -0.3% | -1.084 to +0.1539 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.4 | 182.9 | -0.3% | -1.084 to +0.1539 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.29 | 2.338 | +2.1% | +0.03334 to +0.0629 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.89 | 70.68 | +2.6% | +1.387 to +2.187 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0 | 0.01 | +0.01 | -0.01262 to +0.03262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2515 | 2588 | +2.9% | -1575 to +1720 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4694 | 4897 | +4.3% | -645.1 to +1050 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 33.29 | 30.13 | -9.5% | -6.604 to +0.284 | STEADY, inside the noise (cut) |
| failed requests (%) | 15.91 | 17.05 | +7.2% | -0.5625 to +2.839 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.653 | 13.33 | +38.1% | +2.184 to +5.17 | power given |
| pods started | 4.9 | 12.6 | +157.1% | +5.979 to +9.421 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.286e-16 to +9.063e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183 | 183.6 | +0.3% | -0.277 to +1.413 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183 | 183.6 | +0.3% | -0.277 to +1.413 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.284 | 2.325 | +1.8% | +0.02104 to +0.06188 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.13 | 69.26 | +3.2% | +1.287 to +2.979 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.01 | 0 | -100.0% | -0.03262 to +0.01262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4132 | 4594 | +11.2% | -693.5 to +1619 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 7316 | 6958 | -4.9% | -1636 to +919.8 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 65.6 | 61.55 | -6.2% | -9.188 to +1.071 | STEADY, inside the noise (cut) |
| failed requests (%) | 41.68 | 41.33 | -0.9% | -6.105 to +5.394 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.767 | 11.77 | +20.5% | +1.05 to +2.963 | power given |
| pods started | 3.5 | 6.8 | +94.3% | +1.753 to +4.847 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.187e-16 to +5.187e-16 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 186.4 | 186.8 | +0.2% | -0.685 to +1.509 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.4 | 186.8 | +0.2% | -0.685 to +1.509 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.613 | 2.659 | +1.8% | +0.03931 to +0.05285 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 78.02 | 80.47 | +3.1% | +1.993 to +2.906 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.1 | 0.14 | +40.0% | -0.02911 to +0.1091 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2616 | 3651 | +39.6% | +259.4 to +1811 | LOSS |
| response time (ms), 99th percentile | 5155 | 5757 | +11.7% | -162.5 to +1367 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 38.88 | 40.48 | +4.1% | -0.4257 to +3.628 | STEADY, inside the noise (up) |
| failed requests (%) | 16.74 | 21.3 | +27.3% | +1.9 to +7.221 | LOSS |
| HPA replicas, mean | 9.754 | 13.15 | +34.8% | +1.65 to +5.142 | power given |
| pods started | 3.6 | 9.6 | +166.7% | +4.832 to +7.168 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.471e-16 to +9.471e-16 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.3 | +0.0% | -0.6336 to +0.7632 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.3 | +0.0% | -0.6336 to +0.7632 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.351 | 2.408 | +2.4% | +0.0341 to +0.08085 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.6 | 75.05 | +6.3% | +3.665 to +5.228 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.15 | 0.17 | +13.3% | -0.02524 to +0.06524 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
