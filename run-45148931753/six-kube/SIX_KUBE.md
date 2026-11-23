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
| response time (ms), 95th percentile | 2628 | 3626 | 2398 | 3457 | 2292 | 2836 | 3535 | 4103 | 2420 | 3294 | 3042 | 3032 | 2147 | 3469 |
| response time (ms), 99th percentile | 5159 | 6303 | 4864 | 6264 | 4518 | 5488 | 6073 | 6740 | 4969 | 5740 | 5286 | 5460 | 4836 | 5523 |
| time over the response line (% of samples) | 43.01 | 42.58 | 44.04 | 41.2 | 35.61 | 34.21 | 44.32 | 43.91 | 40.13 | 37.02 | 49.65 | 47.57 | 43.65 | 46.16 |
| failed requests (%) | 27.42 | 27.34 | 21.73 | 22.83 | 23.35 | 23.86 | 28.54 | 28.16 | 22.96 | 22.97 | 31.09 | 31.8 | 22.73 | 26.6 |
| HPA replicas, mean | 9.653 | 14.45 | 9.691 | 13.42 | 9.608 | 14.09 | 9.654 | 14.42 | 9.658 | 13.23 | 9.721 | 11.76 | 9.735 | 12.36 |
| pods started | 4.857 | 10.86 | 4.629 | 10.11 | 5.114 | 10.83 | 4.714 | 10.54 | 4.886 | 10.71 | 4.057 | 9.371 | 3.886 | 8.314 |
| worker nodes in service, mean | 6 | 5.999 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.5 | 184.7 | 185.2 | 182.8 | 183.2 | 184.6 | 184.2 | 183.7 | 184.3 | 184.8 | 184.8 | 184.4 | 184.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.5 | 184.7 | 185.2 | 182.8 | 183.2 | 184.6 | 184.2 | 183.7 | 184.3 | 184.8 | 184.8 | 184.4 | 184.3 |
| CPU used with Omni's own (cores), mean | 2.398 | 2.452 | 2.45 | 2.516 | 2.256 | 2.308 | 2.413 | 2.459 | 2.346 | 2.396 | 2.417 | 2.45 | 2.405 | 2.458 |
| host CPU busy, the real machine under kind (%) | 70.97 | 73.17 | 72.18 | 74.8 | 67.18 | 69.1 | 71.57 | 73.43 | 69.12 | 71.27 | 72.31 | 74.8 | 72.48 | 76.69 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.002857 | 0.002857 | 0.01143 | 0.04286 | 0.008571 | 0.008571 | 0.005714 | 0.005714 | 0.008571 | 0.01429 | 0.09429 | 0.1029 | 0.16 | 0.1771 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2628 | 3626 | +38.0% | +313.2 to +1684 | LOSS |
| response time (ms), 99th percentile | 5159 | 6303 | +22.2% | +369 to +1919 | LOSS |
| time over the response line (% of samples) | 43.01 | 42.58 | -1.0% | -1.565 to +0.698 | STEADY, inside the noise (cut) |
| failed requests (%) | 27.42 | 27.34 | -0.3% | -1.243 to +1.081 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.653 | 14.45 | +49.7% | +4.552 to +5.049 | power given |
| pods started | 4.857 | 10.86 | +123.5% | +5.551 to +6.449 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001706 to +0.0005805 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.5 | +0.2% | -0.2325 to +0.807 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.5 | +0.1% | -0.2468 to +0.7987 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.398 | 2.452 | +2.3% | +0.04662 to +0.06182 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.97 | 73.17 | +3.1% | +2.017 to +2.38 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0.002857 | 0.002857 | +0.0% | -0.00833 to +0.00833 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2398 | 3457 | +44.2% | +459.5 to +1660 | LOSS |
| response time (ms), 99th percentile | 4864 | 6264 | +28.8% | +605.5 to +2195 | LOSS |
| time over the response line (% of samples) | 44.04 | 41.2 | -6.4% | -4.226 to -1.454 | GAIN |
| failed requests (%) | 21.73 | 22.83 | +5.1% | +0.4968 to +1.701 | LOSS |
| HPA replicas, mean | 9.691 | 13.42 | +38.5% | +3.12 to +4.336 | power given |
| pods started | 4.629 | 10.11 | +118.5% | +5.004 to +5.967 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.88e-16 to +5.91e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.7 | 185.2 | +0.2% | -0.04716 to +0.9554 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.7 | 185.2 | +0.2% | -0.04716 to +0.9554 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.45 | 2.516 | +2.7% | +0.05498 to +0.0775 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.18 | 74.8 | +3.6% | +2.268 to +2.974 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.01143 | 0.04286 | +275.0% | +0.01142 to +0.05144 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2292 | 2836 | +23.7% | -41.45 to +1130 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4518 | 5488 | +21.5% | +157.1 to +1784 | LOSS |
| time over the response line (% of samples) | 35.61 | 34.21 | -3.9% | -2.314 to -0.4898 | GAIN |
| failed requests (%) | 23.35 | 23.86 | +2.2% | -0.5284 to +1.554 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.608 | 14.09 | +46.6% | +4.2 to +4.757 | power given |
| pods started | 5.114 | 10.83 | +111.7% | +4.995 to +6.434 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.263e-16 to +2.725e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.8 | 183.2 | +0.3% | -0.3573 to +1.31 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.8 | 183.2 | +0.3% | -0.3573 to +1.31 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.256 | 2.308 | +2.3% | +0.04373 to +0.05994 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.18 | 69.1 | +2.9% | +1.7 to +2.157 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.008571 | 0.008571 | +0.0% | -0.01443 to +0.01443 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3535 | 4103 | +16.1% | -230.1 to +1366 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6073 | 6740 | +11.0% | -144.4 to +1479 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 44.32 | 43.91 | -0.9% | -1.339 to +0.5077 | STEADY, inside the noise (cut) |
| failed requests (%) | 28.54 | 28.16 | -1.3% | -1.518 to +0.7723 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.654 | 14.42 | +49.3% | +4.549 to +4.975 | power given |
| pods started | 4.714 | 10.54 | +123.6% | +5.249 to +6.409 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.915e-16 to +3.915e-16 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 184.6 | 184.2 | -0.2% | -0.8318 to +0.08897 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.6 | 184.2 | -0.2% | -0.8318 to +0.08897 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.413 | 2.459 | +1.9% | +0.03913 to +0.05245 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.57 | 73.43 | +2.6% | +1.74 to +1.981 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.005714 | 0.005714 | +0.0% | -0.01178 to +0.01178 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2420 | 3294 | +36.1% | +211 to +1536 | LOSS |
| response time (ms), 99th percentile | 4969 | 5740 | +15.5% | +61.11 to +1479 | LOSS |
| time over the response line (% of samples) | 40.13 | 37.02 | -7.7% | -4.592 to -1.619 | GAIN |
| failed requests (%) | 22.96 | 22.97 | +0.0% | -0.9145 to +0.9327 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.658 | 13.23 | +37.0% | +2.964 to +4.186 | power given |
| pods started | 4.886 | 10.71 | +119.3% | +5.149 to +6.508 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.62e-16 to +1.037e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 184.3 | +0.3% | +0.154 to +1.061 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 184.3 | +0.3% | +0.154 to +1.061 | power given |
| CPU used with Omni's own (cores), mean | 2.346 | 2.396 | +2.2% | +0.04109 to +0.06032 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.12 | 71.27 | +3.1% | +1.867 to +2.422 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.008571 | 0.01429 | +66.7% | -0.008576 to +0.02 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3042 | 3032 | -0.3% | -639.8 to +620.5 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5286 | 5460 | +3.3% | -577.8 to +926.1 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 49.65 | 47.57 | -4.2% | -3.485 to -0.67 | GAIN |
| failed requests (%) | 31.09 | 31.8 | +2.3% | -0.8031 to +2.219 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.721 | 11.76 | +20.9% | +1.303 to +2.765 | power given |
| pods started | 4.057 | 9.371 | +131.0% | +4.782 to +5.846 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.244e-16 to +6.609e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.8 | 184.8 | -0.0% | -0.4586 to +0.4435 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.8 | 184.8 | -0.0% | -0.4586 to +0.4435 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.417 | 2.45 | +1.4% | +0.02043 to +0.04662 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.31 | 74.8 | +3.4% | +2.102 to +2.882 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.09429 | 0.1029 | +9.1% | -0.001184 to +0.01833 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2147 | 3469 | +61.6% | +791.2 to +1854 | LOSS |
| response time (ms), 99th percentile | 4836 | 5523 | +14.2% | -7.551 to +1380 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 43.65 | 46.16 | +5.8% | +0.7549 to +4.269 | LOSS |
| failed requests (%) | 22.73 | 26.6 | +17.0% | +2.553 to +5.194 | LOSS |
| HPA replicas, mean | 9.735 | 12.36 | +27.0% | +1.843 to +3.413 | power given |
| pods started | 3.886 | 8.314 | +114.0% | +3.449 to +5.408 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +6.969e-17 to +8.439e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184.3 | -0.1% | -0.5173 to +0.2715 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184.3 | -0.1% | -0.5173 to +0.2715 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.405 | 2.458 | +2.2% | +0.0445 to +0.06146 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.48 | 76.69 | +5.8% | +3.944 to +4.475 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.16 | 0.1771 | +10.7% | -0.0005005 to +0.03479 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
