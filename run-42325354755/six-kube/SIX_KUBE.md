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
| response time (ms), 95th percentile | 2612 | 4037 | 2257 | 2801 | 2778 | 3987 | 2648 | 3371 | 2393 | 3715 | 3008 | 3117 | 2326 | 3140 |
| response time (ms), 99th percentile | 5528 | 6801 | 4072 | 5362 | 5619 | 7232 | 4941 | 6222 | 4882 | 5781 | 5540 | 5979 | 4188 | 4832 |
| time over the response line (% of samples) | 45.74 | 44.06 | 37.17 | 33.66 | 45.58 | 44.08 | 42.14 | 41.49 | 40.78 | 37.88 | 46.73 | 44.11 | 30.56 | 30.93 |
| failed requests (%) | 30.19 | 30.41 | 18.3 | 19.01 | 29.02 | 28.78 | 27.82 | 27.56 | 23.52 | 23.66 | 27.95 | 28.32 | 13.09 | 15.28 |
| HPA replicas, mean | 9.63 | 14.03 | 9.665 | 13.6 | 9.664 | 14.49 | 9.644 | 14.35 | 9.632 | 13.07 | 9.697 | 12.37 | 9.643 | 13.6 |
| pods started | 5.143 | 10.6 | 4.829 | 10.46 | 4.8 | 10.37 | 4.914 | 10.69 | 5.343 | 10.74 | 4.4 | 9.657 | 5 | 10.77 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 5.999 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 184.6 | 183.4 | 183.5 | 185 | 185 | 184.2 | 184.3 | 183 | 183.7 | 184.3 | 184.5 | 182.7 | 182.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.6 | 183.4 | 183.5 | 185 | 185 | 184.2 | 184.3 | 183 | 183.7 | 184.3 | 184.5 | 182.7 | 182.7 |
| CPU used with Omni's own (cores), mean | 2.409 | 2.454 | 2.306 | 2.353 | 2.468 | 2.509 | 2.385 | 2.439 | 2.294 | 2.333 | 2.415 | 2.458 | 2.228 | 2.285 |
| host CPU busy, the real machine under kind (%) | 71.06 | 72.92 | 67.63 | 69.78 | 72.72 | 74.65 | 70.39 | 72.53 | 67.12 | 69.08 | 71.61 | 74.33 | 66.45 | 70.6 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0 | 0.008571 | 0.01429 | 0 | 0.002857 | 0.008571 | 0.01143 | 0.005714 | 0.005714 | 0.1 | 0.2229 | 0.1457 | 0.1514 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2612 | 4037 | +54.6% | +564.2 to +2287 | LOSS |
| response time (ms), 99th percentile | 5528 | 6801 | +23.0% | +606.5 to +1938 | LOSS |
| time over the response line (% of samples) | 45.74 | 44.06 | -3.7% | -2.838 to -0.5253 | GAIN |
| failed requests (%) | 30.19 | 30.41 | +0.8% | -0.8716 to +1.326 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.63 | 14.03 | +45.7% | +4.14 to +4.66 | power given |
| pods started | 5.143 | 10.6 | +106.1% | +4.657 to +6.258 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.473e-16 to +4.488e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 184.6 | +0.3% | +0.02501 to +1.046 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.6 | +0.3% | +0.02501 to +1.046 | power given |
| CPU used with Omni's own (cores), mean | 2.409 | 2.454 | +1.9% | +0.0349 to +0.0556 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.06 | 72.92 | +2.6% | +1.605 to +2.117 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2257 | 2801 | +24.1% | +222 to +867.2 | LOSS |
| response time (ms), 99th percentile | 4072 | 5362 | +31.7% | +618.3 to +1962 | LOSS |
| time over the response line (% of samples) | 37.17 | 33.66 | -9.4% | -4.986 to -2.015 | GAIN |
| failed requests (%) | 18.3 | 19.01 | +3.9% | -0.2014 to +1.616 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.665 | 13.6 | +40.7% | +3.396 to +4.466 | power given |
| pods started | 4.829 | 10.46 | +116.6% | +4.983 to +6.274 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.447e-16 to +3.462e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.4 | 183.5 | +0.1% | -0.4324 to +0.6753 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.4 | 183.5 | +0.1% | -0.4324 to +0.6753 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.306 | 2.353 | +2.1% | +0.03666 to +0.05884 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.63 | 69.78 | +3.2% | +1.824 to +2.474 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.008571 | 0.01429 | +66.7% | -0.01083 to +0.02226 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2778 | 3987 | +43.5% | +547.4 to +1871 | LOSS |
| response time (ms), 99th percentile | 5619 | 7232 | +28.7% | +828.9 to +2397 | LOSS |
| time over the response line (% of samples) | 45.58 | 44.08 | -3.3% | -2.862 to -0.1287 | GAIN |
| failed requests (%) | 29.02 | 28.78 | -0.8% | -1.338 to +0.8483 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.664 | 14.49 | +50.0% | +4.651 to +5.009 | power given |
| pods started | 4.8 | 10.37 | +116.1% | +4.993 to +6.15 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.004536 to +0.001544 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 185 | 185 | +0.0% | -0.4181 to +0.5788 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185 | 185 | +0.0% | -0.4433 to +0.5432 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.468 | 2.509 | +1.7% | +0.03325 to +0.04906 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.72 | 74.65 | +2.6% | +1.7 to +2.153 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0 | 0.002857 | +0.00286 | -0.002949 to +0.008663 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2648 | 3371 | +27.3% | +40.1 to +1405 | LOSS |
| response time (ms), 99th percentile | 4941 | 6222 | +25.9% | +499.2 to +2063 | LOSS |
| time over the response line (% of samples) | 42.14 | 41.49 | -1.5% | -1.881 to +0.583 | STEADY, inside the noise (cut) |
| failed requests (%) | 27.82 | 27.56 | -0.9% | -1.6 to +1.096 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.644 | 14.35 | +48.8% | +4.428 to +4.988 | power given |
| pods started | 4.914 | 10.69 | +117.4% | +5.17 to +6.373 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.81e-16 to +1.975e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.3 | +0.0% | -0.3912 to +0.5742 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.3 | +0.0% | -0.3912 to +0.5742 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.385 | 2.439 | +2.3% | +0.04231 to +0.06603 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.39 | 72.53 | +3.0% | +1.818 to +2.457 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.008571 | 0.01143 | +33.3% | -0.007297 to +0.01301 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2393 | 3715 | +55.2% | +655.4 to +1988 | LOSS |
| response time (ms), 99th percentile | 4882 | 5781 | +18.4% | +380.3 to +1418 | LOSS |
| time over the response line (% of samples) | 40.78 | 37.88 | -7.1% | -4.577 to -1.226 | GAIN |
| failed requests (%) | 23.52 | 23.66 | +0.6% | -0.9986 to +1.279 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.632 | 13.07 | +35.7% | +2.851 to +4.023 | power given |
| pods started | 5.343 | 10.74 | +101.1% | +4.816 to +5.984 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.954e-16 to +4.984e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183 | 183.7 | +0.3% | +0.1336 to +1.113 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183 | 183.7 | +0.3% | +0.1336 to +1.113 | power given |
| CPU used with Omni's own (cores), mean | 2.294 | 2.333 | +1.7% | +0.02298 to +0.05513 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.12 | 69.08 | +2.9% | +1.494 to +2.416 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.005714 | 0.005714 | +0.0% | -0.01178 to +0.01178 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3008 | 3117 | +3.6% | -365.1 to +583.5 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5540 | 5979 | +7.9% | +16.33 to +862 | LOSS |
| time over the response line (% of samples) | 46.73 | 44.11 | -5.6% | -3.844 to -1.387 | GAIN |
| failed requests (%) | 27.95 | 28.32 | +1.3% | -1.208 to +1.949 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.697 | 12.37 | +27.6% | +1.974 to +3.373 | power given |
| pods started | 4.4 | 9.657 | +119.5% | +4.51 to +6.004 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.971e-16 to +3.448e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 184.5 | +0.1% | -0.2974 to +0.5789 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.3 | 184.5 | +0.1% | -0.2974 to +0.5789 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.415 | 2.458 | +1.8% | +0.03175 to +0.05359 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.61 | 74.33 | +3.8% | +2.416 to +3.007 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.1 | 0.2229 | +122.9% | +0.0964 to +0.1493 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2326 | 3140 | +35.0% | +275.2 to +1352 | LOSS |
| response time (ms), 99th percentile | 4188 | 4832 | +15.4% | +81.68 to +1207 | LOSS |
| time over the response line (% of samples) | 30.56 | 30.93 | +1.2% | -1.253 to +2.006 | STEADY, inside the noise (up) |
| failed requests (%) | 13.09 | 15.28 | +16.7% | +1.061 to +3.322 | LOSS |
| HPA replicas, mean | 9.643 | 13.6 | +41.0% | +3.283 to +4.624 | power given |
| pods started | 5 | 10.77 | +115.4% | +5.089 to +6.454 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.815e-16 to +2.263e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.7 | 182.7 | +0.0% | -0.4208 to +0.5117 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.7 | 182.7 | +0.0% | -0.4208 to +0.5117 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.228 | 2.285 | +2.5% | +0.04396 to +0.06919 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.45 | 70.6 | +6.2% | +3.742 to +4.544 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1457 | 0.1514 | +3.9% | -0.02055 to +0.03198 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
