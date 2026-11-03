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
| response time (ms), 95th percentile | 1230 | 2611 | 1808 | 2996 | 3186 | 3025 | 2516 | 4074 | 2373 | 4026 | 3733 | 3174 | 2049 | 2769 |
| response time (ms), 99th percentile | 3111 | 4892 | 3620 | 5393 | 5528 | 5407 | 5636 | 6761 | 4295 | 5165 | 7126 | 6074 | 4229 | 4814 |
| time over the response line (% of samples) | 33.12 | 30.72 | 42.78 | 41.14 | 35.43 | 34.31 | 45.5 | 45.29 | 41.56 | 42.78 | 70.46 | 66.24 | 36.11 | 36.35 |
| failed requests (%) | 21.1 | 21.32 | 25.4 | 25.61 | 21.48 | 22.6 | 30.43 | 31.43 | 28.14 | 28.78 | 48.5 | 50.96 | 16.86 | 20.86 |
| HPA replicas, mean | 9.612 | 13.93 | 9.644 | 13.39 | 9.585 | 14.15 | 9.642 | 14.15 | 9.678 | 13.18 | 9.805 | 10.71 | 9.655 | 12.76 |
| pods started | 4.8 | 11.1 | 5 | 10.2 | 5.3 | 11 | 4.9 | 10.1 | 4.5 | 10.5 | 3 | 7.4 | 4.8 | 10.4 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 5.991 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 182.2 | 182.6 | 183.4 | 184 | 183.7 | 183.5 | 184.1 | 184.9 | 182.9 | 183.6 | 186.8 | 187 | 182.9 | 183 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.2 | 182.6 | 183.4 | 184 | 183.7 | 183.5 | 184.1 | 184.9 | 182.9 | 183.4 | 186.8 | 187 | 182.9 | 183 |
| CPU used with Omni's own (cores), mean | 2.206 | 2.26 | 2.312 | 2.376 | 2.329 | 2.365 | 2.374 | 2.442 | 2.29 | 2.331 | 2.629 | 2.66 | 2.264 | 2.322 |
| host CPU busy, the real machine under kind (%) | 65.56 | 67.43 | 68.24 | 70.78 | 68.78 | 70.24 | 70.47 | 72.92 | 67.69 | 69.67 | 78.22 | 80.84 | 67.71 | 72.23 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0.01 | 0.02 | 0.03 | 0.01 | 0.01 | 0.01 | 0.02 | 0 | 0.01 | 0.1 | 0.21 | 0.15 | 0.17 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1230 | 2611 | +112.3% | +34.71 to +2727 | LOSS |
| response time (ms), 99th percentile | 3111 | 4892 | +57.2% | -54.91 to +3616 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 33.12 | 30.72 | -7.2% | -5.456 to +0.6625 | STEADY, inside the noise (cut) |
| failed requests (%) | 21.1 | 21.32 | +1.1% | -2.744 to +3.194 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.612 | 13.93 | +44.9% | +3.759 to +4.869 | power given |
| pods started | 4.8 | 11.1 | +131.2% | +4.483 to +8.117 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.99e-16 to +5.99e-16 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 182.2 | 182.6 | +0.2% | -0.7731 to +1.496 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.2 | 182.6 | +0.2% | -0.7731 to +1.496 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.206 | 2.26 | +2.5% | +0.0375 to +0.07084 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.56 | 67.43 | +2.9% | +1.304 to +2.442 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0.01 | +0.01 | -0.01262 to +0.03262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1808 | 2996 | +65.7% | +177.8 to +2199 | LOSS |
| response time (ms), 99th percentile | 3620 | 5393 | +49.0% | +437 to +3110 | LOSS |
| time over the response line (% of samples) | 42.78 | 41.14 | -3.8% | -4.374 to +1.094 | STEADY, inside the noise (cut) |
| failed requests (%) | 25.4 | 25.61 | +0.8% | -1.417 to +1.838 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.644 | 13.39 | +38.9% | +2.984 to +4.519 | power given |
| pods started | 5 | 10.2 | +104.0% | +4.092 to +6.308 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.924e-16 to +7.924e-16 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 183.4 | 184 | +0.4% | -0.6224 to +1.935 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.4 | 184 | +0.4% | -0.6224 to +1.935 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.312 | 2.376 | +2.8% | +0.04733 to +0.08169 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.24 | 70.78 | +3.7% | +2.122 to +2.97 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.02 | 0.03 | +50.0% | -0.04278 to +0.06278 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3186 | 3025 | -5.1% | -1477 to +1155 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5528 | 5407 | -2.2% | -1254 to +1012 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 35.43 | 34.31 | -3.2% | -2.157 to -0.09043 | GAIN |
| failed requests (%) | 21.48 | 22.6 | +5.2% | -1.127 to +3.35 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.585 | 14.15 | +47.6% | +3.784 to +5.342 | power given |
| pods started | 5.3 | 11 | +107.5% | +5.111 to +6.289 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.793e-16 to +1.057e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 183.5 | -0.1% | -1.416 to +0.898 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 183.5 | -0.1% | -1.416 to +0.898 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.329 | 2.365 | +1.5% | +0.01953 to +0.05155 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.78 | 70.24 | +2.1% | +0.9163 to +2.008 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.01 | 0.01 | +0.0% | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2516 | 4074 | +62.0% | -17.11 to +3134 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5636 | 6761 | +20.0% | -77.03 to +2327 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 45.5 | 45.29 | -0.5% | -1.669 to +1.252 | STEADY, inside the noise (cut) |
| failed requests (%) | 30.43 | 31.43 | +3.3% | -1.27 to +3.276 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.642 | 14.15 | +46.7% | +4.05 to +4.963 | power given |
| pods started | 4.9 | 10.1 | +106.1% | +3.738 to +6.662 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.575e-15 to +6.865e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 184.9 | +0.4% | -0.3089 to +1.877 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.9 | +0.4% | -0.3089 to +1.877 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.374 | 2.442 | +2.8% | +0.02663 to +0.1084 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.47 | 72.92 | +3.5% | +1.205 to +3.703 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.01 | 0.02 | +100.0% | -0.0306 to +0.0506 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2373 | 4026 | +69.6% | -155.3 to +3461 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4295 | 5165 | +20.3% | -886.9 to +2627 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 41.56 | 42.78 | +2.9% | -2.107 to +4.554 | STEADY, inside the noise (up) |
| failed requests (%) | 28.14 | 28.78 | +2.3% | -1.74 to +3.029 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.678 | 13.18 | +36.2% | +2.315 to +4.683 | power given |
| pods started | 4.5 | 10.5 | +133.3% | +4.455 to +7.545 | power given |
| worker nodes in service, mean | 6 | 5.991 | -0.1% | -0.02853 to +0.01104 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.9 | 183.6 | +0.4% | -0.545 to +1.907 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.9 | 183.4 | +0.3% | -0.7356 to +1.743 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.29 | 2.331 | +1.8% | +0.02654 to +0.05472 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.69 | 69.67 | +2.9% | +1.595 to +2.372 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0 | 0.01 | +0.01 | -0.01262 to +0.03262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 3 (response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 3 (pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3733 | 3174 | -15.0% | -1514 to +396.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 7126 | 6074 | -14.8% | -2093 to -10.85 | GAIN |
| time over the response line (% of samples) | 70.46 | 66.24 | -6.0% | -6.826 to -1.623 | GAIN |
| failed requests (%) | 48.5 | 50.96 | +5.1% | -1.791 to +6.698 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.805 | 10.71 | +9.2% | -0.418 to +2.228 | STEADY, inside the noise (up) |
| pods started | 3 | 7.4 | +146.7% | +3.272 to +5.528 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.336e-16 to +7.336e-16 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 186.8 | 187 | +0.2% | -0.6171 to +1.191 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.8 | 187 | +0.2% | -0.6171 to +1.191 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.629 | 2.66 | +1.2% | +0.02002 to +0.04315 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 78.22 | 80.84 | +3.3% | +2.456 to +2.777 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.1 | 0.21 | +110.0% | +0.08738 to +0.1326 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2049 | 2769 | +35.2% | +109.2 to +1331 | LOSS |
| response time (ms), 99th percentile | 4229 | 4814 | +13.8% | -488.3 to +1658 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 36.11 | 36.35 | +0.7% | -2.447 to +2.935 | STEADY, inside the noise (up) |
| failed requests (%) | 16.86 | 20.86 | +23.8% | +1.013 to +7.003 | LOSS |
| HPA replicas, mean | 9.655 | 12.76 | +32.2% | +1.223 to +4.987 | power given |
| pods started | 4.8 | 10.4 | +116.7% | +4.202 to +6.998 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.104e-16 to +7.88e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.9 | 183 | +0.1% | -0.7349 to +1.034 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.9 | 183 | +0.1% | -0.7349 to +1.034 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.264 | 2.322 | +2.5% | +0.03264 to +0.08208 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.71 | 72.23 | +6.7% | +3.958 to +5.092 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.15 | 0.17 | +13.3% | -0.02524 to +0.06524 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
