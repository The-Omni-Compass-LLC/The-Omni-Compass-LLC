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
| response time (ms), 95th percentile | 2784 | 3850 | 1647 | 2603 | 3002 | 3423 | 2472 | 3492 | 2436 | 3554 | 2627 | 2881 | 2237 | 3486 |
| response time (ms), 99th percentile | 5372 | 6273 | 3471 | 5022 | 6035 | 6430 | 4822 | 6212 | 5365 | 5893 | 4651 | 4860 | 4654 | 5588 |
| time over the response line (% of samples) | 41.15 | 39.29 | 39.26 | 37.98 | 44.76 | 42.42 | 40.94 | 39.76 | 40.81 | 38.13 | 36.04 | 33.23 | 45.76 | 47.59 |
| failed requests (%) | 25.72 | 25.47 | 22.81 | 24.3 | 28.73 | 28.97 | 26.95 | 26.34 | 22.67 | 22.94 | 21.09 | 21.05 | 23.76 | 27.65 |
| HPA replicas, mean | 9.632 | 14.24 | 9.667 | 13.22 | 9.627 | 14.37 | 9.636 | 14.48 | 9.645 | 13.44 | 9.64 | 13.11 | 9.744 | 12.28 |
| pods started | 5.057 | 11.03 | 4.714 | 10.26 | 5.143 | 10.71 | 4.971 | 10.89 | 5.057 | 10.97 | 5.086 | 10.4 | 3.743 | 8.114 |
| worker nodes in service, mean | 5.998 | 6 | 6 | 6 | 6 | 6 | 6 | 5.997 | 6 | 6 | 5.998 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.9 | 183.9 | 183 | 183.6 | 184.7 | 184.9 | 184.2 | 183.8 | 183.7 | 184.4 | 183 | 183 | 184.9 | 185.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.9 | 183.9 | 183 | 183.6 | 184.7 | 184.9 | 184.2 | 183.8 | 183.7 | 184.4 | 182.9 | 183 | 184.9 | 185.1 |
| CPU used with Omni's own (cores), mean | 2.352 | 2.402 | 2.307 | 2.351 | 2.414 | 2.469 | 2.376 | 2.431 | 2.352 | 2.407 | 2.229 | 2.28 | 2.445 | 2.498 |
| host CPU busy, the real machine under kind (%) | 69.75 | 71.61 | 68.15 | 70.28 | 71.55 | 73.69 | 70.8 | 72.98 | 69.3 | 71.7 | 66.84 | 69.64 | 73.66 | 77.88 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.002857 | 0 | 0.005714 | 0.04 | 0.008571 | 0.01714 | 0.01143 | 0.01714 | 0.005714 | 0.01429 | 0.09143 | 0.1 | 0.16 | 0.1971 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2784 | 3850 | +38.3% | +271.8 to +1860 | LOSS |
| response time (ms), 99th percentile | 5372 | 6273 | +16.8% | +228.2 to +1575 | LOSS |
| time over the response line (% of samples) | 41.15 | 39.29 | -4.5% | -2.854 to -0.878 | GAIN |
| failed requests (%) | 25.72 | 25.47 | -1.0% | -1.498 to +0.9911 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.632 | 14.24 | +47.9% | +4.359 to +4.863 | power given |
| pods started | 5.057 | 11.03 | +118.1% | +5.468 to +6.475 | power given |
| worker nodes in service, mean | 5.998 | 6 | +0.0% | -0.002313 to +0.006794 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.9 | 183.9 | -0.0% | -0.5186 to +0.4991 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.9 | 183.9 | +0.0% | -0.499 to +0.57 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.352 | 2.402 | +2.1% | +0.04061 to +0.05885 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.75 | 71.61 | +2.7% | +1.553 to +2.158 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008375 to -0.0008374 | power given |
| organism behind its window (s) | 0.002857 | 0 | -100.0% | -0.008663 to +0.002949 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1647 | 2603 | +58.1% | +456 to +1457 | LOSS |
| response time (ms), 99th percentile | 3471 | 5022 | +44.7% | +713 to +2389 | LOSS |
| time over the response line (% of samples) | 39.26 | 37.98 | -3.3% | -3.1 to +0.5278 | STEADY, inside the noise (cut) |
| failed requests (%) | 22.81 | 24.3 | +6.5% | +0.3714 to +2.607 | LOSS |
| HPA replicas, mean | 9.667 | 13.22 | +36.7% | +3.051 to +4.053 | power given |
| pods started | 4.714 | 10.26 | +117.6% | +4.89 to +6.195 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.656e-16 to +2.596e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183 | 183.6 | +0.3% | +0.1212 to +1.157 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183 | 183.6 | +0.3% | +0.1212 to +1.157 | power given |
| CPU used with Omni's own (cores), mean | 2.307 | 2.351 | +1.9% | +0.02754 to +0.06196 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.15 | 70.28 | +3.1% | +1.665 to +2.609 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.005714 | 0.04 | +600.0% | +0.01577 to +0.05281 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3002 | 3423 | +14.0% | -431.2 to +1274 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6035 | 6430 | +6.6% | -281.5 to +1073 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 44.76 | 42.42 | -5.2% | -3.513 to -1.163 | GAIN |
| failed requests (%) | 28.73 | 28.97 | +0.8% | -0.9156 to +1.391 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.627 | 14.37 | +49.2% | +4.483 to +4.999 | power given |
| pods started | 5.143 | 10.71 | +108.3% | +5.049 to +6.094 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.322e-16 to +7.393e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.7 | 184.9 | +0.1% | -0.4053 to +0.7192 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.7 | 184.9 | +0.1% | -0.4053 to +0.7192 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.414 | 2.469 | +2.3% | +0.04626 to +0.06435 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.55 | 73.69 | +3.0% | +1.861 to +2.427 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.008571 | 0.01714 | +100.0% | -0.006724 to +0.02387 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2472 | 3492 | +41.2% | +377.4 to +1662 | LOSS |
| response time (ms), 99th percentile | 4822 | 6212 | +28.8% | +583.7 to +2197 | LOSS |
| time over the response line (% of samples) | 40.94 | 39.76 | -2.9% | -2.296 to -0.05142 | GAIN |
| failed requests (%) | 26.95 | 26.34 | -2.2% | -1.944 to +0.7332 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.636 | 14.48 | +50.2% | +4.596 to +5.082 | power given |
| pods started | 4.971 | 10.89 | +119.0% | +5.463 to +6.366 | power given |
| worker nodes in service, mean | 6 | 5.997 | -0.0% | -0.008404 to +0.00286 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 183.8 | -0.2% | -0.8214 to -0.03117 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 183.8 | -0.3% | -0.8764 to -0.08805 | GAIN |
| CPU used with Omni's own (cores), mean | 2.376 | 2.431 | +2.3% | +0.04324 to +0.06625 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.8 | 72.98 | +3.1% | +1.868 to +2.503 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.01143 | 0.01714 | +50.0% | -0.01083 to +0.02226 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2436 | 3554 | +45.9% | +437.2 to +1798 | LOSS |
| response time (ms), 99th percentile | 5365 | 5893 | +9.8% | -38.63 to +1093 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 40.81 | 38.13 | -6.6% | -4.451 to -0.9021 | GAIN |
| failed requests (%) | 22.67 | 22.94 | +1.2% | -1.08 to +1.622 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.645 | 13.44 | +39.3% | +3.252 to +4.328 | power given |
| pods started | 5.057 | 10.97 | +116.9% | +5.191 to +6.638 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.014e-16 to +2.461e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 184.4 | +0.4% | +0.2602 to +1.194 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 184.4 | +0.4% | +0.2602 to +1.194 | power given |
| CPU used with Omni's own (cores), mean | 2.352 | 2.407 | +2.3% | +0.04621 to +0.06402 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.3 | 71.7 | +3.5% | +2.14 to +2.671 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.005714 | 0.01429 | +150.0% | -0.004257 to +0.0214 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2627 | 2881 | +9.7% | -308.3 to +815.7 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4651 | 4860 | +4.5% | -326.1 to +745.4 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 36.04 | 33.23 | -7.8% | -3.894 to -1.733 | GAIN |
| failed requests (%) | 21.09 | 21.05 | -0.2% | -1.438 to +1.358 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.64 | 13.11 | +36.0% | +2.866 to +4.079 | power given |
| pods started | 5.086 | 10.4 | +104.5% | +4.609 to +6.02 | power given |
| worker nodes in service, mean | 5.998 | 6 | +0.0% | -0.002302 to +0.006764 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 183 | 183 | -0.0% | -0.4647 to +0.4617 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.9 | 183 | +0.0% | -0.3869 to +0.4768 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.229 | 2.28 | +2.3% | +0.03523 to +0.06753 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.84 | 69.64 | +4.2% | +2.373 to +3.225 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.09143 | 0.1 | +9.4% | -0.001184 to +0.01833 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2237 | 3486 | +55.9% | +792.5 to +1706 | LOSS |
| response time (ms), 99th percentile | 4654 | 5588 | +20.1% | +251.1 to +1617 | LOSS |
| time over the response line (% of samples) | 45.76 | 47.59 | +4.0% | -0.03759 to +3.7 | STEADY, inside the noise (up) |
| failed requests (%) | 23.76 | 27.65 | +16.4% | +2.618 to +5.164 | LOSS |
| HPA replicas, mean | 9.744 | 12.28 | +26.0% | +1.726 to +3.343 | power given |
| pods started | 3.743 | 8.114 | +116.8% | +3.659 to +5.084 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.713e-16 to +3.728e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.9 | 185.1 | +0.1% | -0.2199 to +0.6038 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.9 | 185.1 | +0.1% | -0.2199 to +0.6038 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.445 | 2.498 | +2.1% | +0.0422 to +0.06222 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.66 | 77.88 | +5.7% | +3.923 to +4.507 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.16 | 0.1971 | +23.2% | +0.01069 to +0.0636 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
