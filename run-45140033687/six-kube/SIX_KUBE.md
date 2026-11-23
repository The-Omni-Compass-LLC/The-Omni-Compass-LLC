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
| response time (ms), 95th percentile | 2531 | 3561 | 2445 | 3201 | 2878 | 3831 | 2651 | 3585 | 2934 | 4492 | 2908 | 3396 | 2367 | 3648 |
| response time (ms), 99th percentile | 5181 | 6041 | 4844 | 6005 | 5367 | 6232 | 4851 | 6173 | 5651 | 6733 | 5642 | 6282 | 4374 | 5626 |
| time over the response line (% of samples) | 42.76 | 41.1 | 43.14 | 41.27 | 45.87 | 44.52 | 40.29 | 38.69 | 46.93 | 43.79 | 43.56 | 40.04 | 37.62 | 41.19 |
| failed requests (%) | 27.54 | 27.09 | 22.76 | 23.66 | 30.01 | 30.08 | 25.64 | 24.96 | 26.33 | 26.49 | 23.94 | 24.23 | 18.98 | 23.04 |
| HPA replicas, mean | 9.644 | 14.2 | 9.656 | 13.42 | 9.655 | 14.37 | 9.641 | 14.47 | 9.669 | 13.3 | 9.685 | 12.82 | 9.696 | 12.78 |
| pods started | 4.829 | 10.63 | 5.029 | 10.26 | 4.943 | 10.69 | 5 | 10.8 | 4.829 | 10.34 | 4.629 | 10.06 | 4.257 | 9.886 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 184.1 | 184.1 | 184.5 | 184.6 | 184.5 | 184.1 | 184.5 | 184.5 | 185.6 | 184.7 | 184.5 | 183.6 | 183.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 184.1 | 184.1 | 184.5 | 184.6 | 184.5 | 184.1 | 184.5 | 184.5 | 185.6 | 184.7 | 184.5 | 183.6 | 183.7 |
| CPU used with Omni's own (cores), mean | 2.366 | 2.408 | 2.373 | 2.425 | 2.426 | 2.478 | 2.368 | 2.41 | 2.449 | 2.502 | 2.415 | 2.469 | 2.327 | 2.372 |
| host CPU busy, the real machine under kind (%) | 70.21 | 71.94 | 69.93 | 72.35 | 72.1 | 74.29 | 70.44 | 72.19 | 71.95 | 74.26 | 71.89 | 74.92 | 70.07 | 74 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0 | 0.01714 | 0.05429 | 0.01429 | 0.005714 | 0 | 0.008571 | 0.005714 | 0.02286 | 0.09429 | 0.1 | 0.1543 | 0.1914 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2531 | 3561 | +40.7% | +298.6 to +1762 | LOSS |
| response time (ms), 99th percentile | 5181 | 6041 | +16.6% | +30.12 to +1691 | LOSS |
| time over the response line (% of samples) | 42.76 | 41.1 | -3.9% | -2.827 to -0.4893 | GAIN |
| failed requests (%) | 27.54 | 27.09 | -1.6% | -1.586 to +0.6942 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.644 | 14.2 | +47.3% | +4.277 to +4.842 | power given |
| pods started | 4.829 | 10.63 | +120.1% | +5.302 to +6.298 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.467e-16 to +2.437e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 184.1 | +0.2% | -0.1846 to +0.8539 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 184.1 | +0.2% | -0.1846 to +0.8539 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.366 | 2.408 | +1.8% | +0.02715 to +0.05577 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.21 | 71.94 | +2.5% | +1.267 to +2.187 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2445 | 3201 | +30.9% | +132.9 to +1380 | LOSS |
| response time (ms), 99th percentile | 4844 | 6005 | +24.0% | +489.1 to +1833 | LOSS |
| time over the response line (% of samples) | 43.14 | 41.27 | -4.3% | -3.745 to -0.0002299 | GAIN |
| failed requests (%) | 22.76 | 23.66 | +4.0% | -0.4896 to +2.293 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.656 | 13.42 | +39.0% | +3.184 to +4.341 | power given |
| pods started | 5.029 | 10.26 | +104.0% | +4.557 to +5.901 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.739e-16 to -1.396e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 184.5 | +0.2% | -0.1255 to +0.8493 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.5 | +0.2% | -0.1255 to +0.8493 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.373 | 2.425 | +2.2% | +0.04169 to +0.06285 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.93 | 72.35 | +3.5% | +2.124 to +2.725 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.01714 | 0.05429 | +216.7% | +0.01346 to +0.06083 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2878 | 3831 | +33.1% | +225 to +1681 | LOSS |
| response time (ms), 99th percentile | 5367 | 6232 | +16.1% | +184.8 to +1544 | LOSS |
| time over the response line (% of samples) | 45.87 | 44.52 | -3.0% | -2.676 to -0.0362 | GAIN |
| failed requests (%) | 30.01 | 30.08 | +0.2% | -1.189 to +1.334 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.655 | 14.37 | +48.8% | +4.453 to +4.972 | power given |
| pods started | 4.943 | 10.69 | +116.2% | +5.269 to +6.217 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.128e-16 to +3.113e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.6 | 184.5 | -0.0% | -0.5418 to +0.4386 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.6 | 184.5 | -0.0% | -0.5418 to +0.4386 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.426 | 2.478 | +2.1% | +0.04406 to +0.05948 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.1 | 74.29 | +3.0% | +2 to +2.367 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.01429 | 0.005714 | -60.0% | -0.02387 to +0.006724 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2651 | 3585 | +35.2% | +286.3 to +1581 | LOSS |
| response time (ms), 99th percentile | 4851 | 6173 | +27.2% | +519.1 to +2124 | LOSS |
| time over the response line (% of samples) | 40.29 | 38.69 | -4.0% | -2.721 to -0.4922 | GAIN |
| failed requests (%) | 25.64 | 24.96 | -2.6% | -1.554 to +0.1971 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.641 | 14.47 | +50.1% | +4.585 to +5.083 | power given |
| pods started | 5 | 10.8 | +116.0% | +5.255 to +6.345 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.457e-16 to +3.412e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 184.5 | +0.2% | -0.1333 to +0.9477 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.5 | +0.2% | -0.1333 to +0.9477 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.368 | 2.41 | +1.8% | +0.0321 to +0.05228 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.44 | 72.19 | +2.5% | +1.485 to +2.016 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0 | 0.008571 | +0.00857 | -0.001184 to +0.01833 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2934 | 4492 | +53.1% | +833.7 to +2283 | LOSS |
| response time (ms), 99th percentile | 5651 | 6733 | +19.1% | +486.6 to +1677 | LOSS |
| time over the response line (% of samples) | 46.93 | 43.79 | -6.7% | -4.685 to -1.592 | GAIN |
| failed requests (%) | 26.33 | 26.49 | +0.6% | -0.9954 to +1.321 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.669 | 13.3 | +37.5% | +3.092 to +4.166 | power given |
| pods started | 4.829 | 10.34 | +114.2% | +4.782 to +6.247 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.919e-16 to -2.262e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.5 | 185.6 | +0.6% | +0.7552 to +1.605 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.5 | 185.6 | +0.6% | +0.7552 to +1.605 | power given |
| CPU used with Omni's own (cores), mean | 2.449 | 2.502 | +2.2% | +0.0413 to +0.0644 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.95 | 74.26 | +3.2% | +1.892 to +2.726 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.005714 | 0.02286 | +300.0% | +0.00159 to +0.0327 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2908 | 3396 | +16.8% | -204.2 to +1181 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5642 | 6282 | +11.4% | -133 to +1414 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 43.56 | 40.04 | -8.1% | -4.906 to -2.132 | GAIN |
| failed requests (%) | 23.94 | 24.23 | +1.2% | -1.132 to +1.706 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.685 | 12.82 | +32.4% | +2.472 to +3.794 | power given |
| pods started | 4.629 | 10.06 | +117.3% | +4.73 to +6.127 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.057e-15 to -2.121e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.7 | 184.5 | -0.1% | -0.7495 to +0.318 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.7 | 184.5 | -0.1% | -0.7495 to +0.318 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.415 | 2.469 | +2.2% | +0.04347 to +0.06436 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.89 | 74.92 | +4.2% | +2.735 to +3.319 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.09429 | 0.1 | +6.1% | -0.005897 to +0.01733 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2367 | 3648 | +54.1% | +767.3 to +1795 | LOSS |
| response time (ms), 99th percentile | 4374 | 5626 | +28.6% | +585.3 to +1919 | LOSS |
| time over the response line (% of samples) | 37.62 | 41.19 | +9.5% | +1.744 to +5.388 | LOSS |
| failed requests (%) | 18.98 | 23.04 | +21.4% | +2.619 to +5.51 | LOSS |
| HPA replicas, mean | 9.696 | 12.78 | +31.8% | +2.247 to +3.926 | power given |
| pods started | 4.257 | 9.886 | +132.2% | +5.128 to +6.129 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.629e-16 to +5.674e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.6 | 183.7 | +0.1% | -0.4377 to +0.6437 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.6 | 183.7 | +0.1% | -0.4377 to +0.6437 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.327 | 2.372 | +1.9% | +0.02818 to +0.06074 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.07 | 74 | +5.6% | +3.416 to +4.453 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1543 | 0.1914 | +24.1% | +0.01069 to +0.0636 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
