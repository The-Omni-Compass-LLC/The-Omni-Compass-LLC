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
| response time (ms), 95th percentile | 2615 | 3989 | 1728 | 2605 | 3147 | 4174 | 2878 | 3709 | 2404 | 4124 | 3740 | 2968 | 2083 | 3752 |
| response time (ms), 99th percentile | 5572 | 6936 | 3670 | 4469 | 6115 | 6839 | 5346 | 6064 | 5688 | 6445 | 6539 | 6152 | 4532 | 6248 |
| time over the response line (% of samples) | 43.72 | 42.7 | 33.82 | 33.1 | 42.46 | 41.02 | 38.5 | 36.54 | 46.31 | 44.53 | 47.97 | 43.59 | 42.17 | 44.96 |
| failed requests (%) | 28.12 | 27.35 | 17.38 | 19.08 | 27.21 | 26.19 | 22.03 | 22.37 | 28.15 | 27.54 | 26.3 | 26.14 | 22.1 | 26.56 |
| HPA replicas, mean | 9.65 | 14.35 | 9.643 | 13.29 | 9.626 | 14.51 | 9.623 | 14.27 | 9.691 | 13.05 | 9.699 | 12.32 | 9.733 | 12.86 |
| pods started | 4.971 | 10.63 | 5.086 | 10.57 | 5.143 | 11.17 | 5.029 | 10.94 | 4.514 | 10.29 | 4.486 | 9.657 | 3.914 | 8.743 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.6 | 184.8 | 182.9 | 183.2 | 184.6 | 184.7 | 184 | 183.6 | 184.4 | 184.7 | 185.3 | 185 | 184.7 | 184.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.6 | 184.8 | 182.9 | 183.2 | 184.6 | 184.7 | 184 | 183.6 | 184.4 | 184.7 | 185.3 | 185 | 184.7 | 184.7 |
| CPU used with Omni's own (cores), mean | 2.415 | 2.472 | 2.263 | 2.316 | 2.408 | 2.463 | 2.348 | 2.39 | 2.416 | 2.47 | 2.456 | 2.499 | 2.407 | 2.466 |
| host CPU busy, the real machine under kind (%) | 71.31 | 73.57 | 66.93 | 69.39 | 71.26 | 73.57 | 69.84 | 71.75 | 71.34 | 73.78 | 73.04 | 75.85 | 72.63 | 77.02 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.005714 | 0 | 0.01143 | 0.02 | 0.008571 | 0.008571 | 0.008571 | 0.008571 | 0.01714 | 0.02571 | 0.1 | 0.1086 | 0.1886 | 0.2171 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2615 | 3989 | +52.5% | +643 to +2105 | LOSS |
| response time (ms), 99th percentile | 5572 | 6936 | +24.5% | +651.2 to +2077 | LOSS |
| time over the response line (% of samples) | 43.72 | 42.7 | -2.3% | -2.07 to +0.04574 | STEADY, inside the noise (cut) |
| failed requests (%) | 28.12 | 27.35 | -2.8% | -2.207 to +0.6537 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.65 | 14.35 | +48.7% | +4.442 to +4.962 | power given |
| pods started | 4.971 | 10.63 | +113.8% | +5.233 to +6.081 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.797e-16 to +3.812e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.6 | 184.8 | +0.1% | -0.4648 to +0.698 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.6 | 184.8 | +0.1% | -0.4648 to +0.698 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.415 | 2.472 | +2.4% | +0.04508 to +0.06884 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.31 | 73.57 | +3.2% | +1.924 to +2.597 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0.005714 | 0 | -100.0% | -0.0138 to +0.002375 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1728 | 2605 | +50.7% | +440.1 to +1313 | LOSS |
| response time (ms), 99th percentile | 3670 | 4469 | +21.8% | +179.8 to +1419 | LOSS |
| time over the response line (% of samples) | 33.82 | 33.1 | -2.1% | -2.281 to +0.8291 | STEADY, inside the noise (cut) |
| failed requests (%) | 17.38 | 19.08 | +9.8% | +0.6782 to +2.72 | LOSS |
| HPA replicas, mean | 9.643 | 13.29 | +37.8% | +3.001 to +4.285 | power given |
| pods started | 5.086 | 10.57 | +107.9% | +4.963 to +6.008 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.133e-16 to +3.625e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.9 | 183.2 | +0.2% | -0.197 to +0.8018 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.9 | 183.2 | +0.2% | -0.197 to +0.8018 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.263 | 2.316 | +2.4% | +0.03879 to +0.06802 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.93 | 69.39 | +3.7% | +2.014 to +2.891 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.01143 | 0.02 | +75.0% | -0.008846 to +0.02599 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3147 | 4174 | +32.6% | +141.3 to +1912 | LOSS |
| response time (ms), 99th percentile | 6115 | 6839 | +11.9% | -21.07 to +1470 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 42.46 | 41.02 | -3.4% | -2.535 to -0.3423 | GAIN |
| failed requests (%) | 27.21 | 26.19 | -3.7% | -2.172 to +0.1368 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.626 | 14.51 | +50.8% | +4.673 to +5.1 | power given |
| pods started | 5.143 | 11.17 | +117.2% | +5.455 to +6.603 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.881e-16 to +3.866e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.6 | 184.7 | +0.0% | -0.4774 to +0.6192 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.6 | 184.7 | +0.0% | -0.4774 to +0.6192 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.408 | 2.463 | +2.3% | +0.04237 to +0.06602 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.26 | 73.57 | +3.3% | +1.959 to +2.678 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.008571 | 0.008571 | +0.0% | -0.01178 to +0.01178 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2878 | 3709 | +28.9% | +24.4 to +1637 | LOSS |
| response time (ms), 99th percentile | 5346 | 6064 | +13.4% | -118.5 to +1553 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 38.5 | 36.54 | -5.1% | -3.229 to -0.7072 | GAIN |
| failed requests (%) | 22.03 | 22.37 | +1.5% | -0.5788 to +1.252 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.623 | 14.27 | +48.3% | +4.403 to +4.887 | power given |
| pods started | 5.029 | 10.94 | +117.6% | +5.419 to +6.41 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.687e-16 to +4.657e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 183.6 | -0.2% | -0.7886 to +0.0915 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 183.6 | -0.2% | -0.7886 to +0.0915 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.348 | 2.39 | +1.8% | +0.03396 to +0.0495 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.84 | 71.75 | +2.7% | +1.673 to +2.156 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.008571 | 0.008571 | +0.0% | -0.01443 to +0.01443 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2404 | 4124 | +71.5% | +939.2 to +2499 | LOSS |
| response time (ms), 99th percentile | 5688 | 6445 | +13.3% | +72.95 to +1442 | LOSS |
| time over the response line (% of samples) | 46.31 | 44.53 | -3.8% | -3.435 to -0.1226 | GAIN |
| failed requests (%) | 28.15 | 27.54 | -2.2% | -1.703 to +0.4818 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.691 | 13.05 | +34.7% | +2.767 to +3.955 | power given |
| pods started | 4.514 | 10.29 | +127.8% | +5.045 to +6.498 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.843e-16 to +2.813e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184.7 | +0.2% | -0.211 to +0.788 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184.7 | +0.2% | -0.211 to +0.788 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.416 | 2.47 | +2.2% | +0.04453 to +0.06334 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.34 | 73.78 | +3.4% | +2.187 to +2.695 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.01714 | 0.02571 | +50.0% | -0.006724 to +0.02387 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3740 | 2968 | -20.6% | -1190 to -352.2 | GAIN |
| response time (ms), 99th percentile | 6539 | 6152 | -5.9% | -945.7 to +170.3 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 47.97 | 43.59 | -9.1% | -6.543 to -2.205 | GAIN |
| failed requests (%) | 26.3 | 26.14 | -0.6% | -2.303 to +1.989 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.699 | 12.32 | +27.1% | +1.881 to +3.366 | power given |
| pods started | 4.486 | 9.657 | +115.3% | +4.497 to +5.846 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.702e-16 to +3.18e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.3 | 185 | -0.2% | -0.7295 to +0.1614 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.3 | 185 | -0.2% | -0.7295 to +0.1614 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.456 | 2.499 | +1.7% | +0.03216 to +0.05268 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.04 | 75.85 | +3.8% | +2.547 to +3.068 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.1 | 0.1086 | +8.6% | -0.008846 to +0.02599 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2083 | 3752 | +80.1% | +1110 to +2227 | LOSS |
| response time (ms), 99th percentile | 4532 | 6248 | +37.9% | +1075 to +2357 | LOSS |
| time over the response line (% of samples) | 42.17 | 44.96 | +6.6% | +0.7442 to +4.836 | LOSS |
| failed requests (%) | 22.1 | 26.56 | +20.2% | +2.699 to +6.213 | LOSS |
| HPA replicas, mean | 9.733 | 12.86 | +32.2% | +2.38 to +3.884 | power given |
| pods started | 3.914 | 8.743 | +123.4% | +4.054 to +5.603 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.314e-16 to +4.314e-16 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 184.7 | 184.7 | -0.0% | -0.4109 to +0.3541 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.7 | 184.7 | -0.0% | -0.4109 to +0.3541 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.407 | 2.466 | +2.4% | +0.04631 to +0.07074 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.63 | 77.02 | +6.0% | +4.046 to +4.731 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1886 | 0.2171 | +15.2% | -0.03008 to +0.08722 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
