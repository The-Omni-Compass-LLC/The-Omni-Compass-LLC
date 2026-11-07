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
| response time (ms), 95th percentile | 2958 | 3727 | 2436 | 3209 | 2391 | 3291 | 3001 | 3247 | 2447 | 4094 | 3006 | 2917 | 2993 | 3620 |
| response time (ms), 99th percentile | 5331 | 6335 | 4890 | 5963 | 4831 | 6223 | 5198 | 5556 | 5156 | 6281 | 5564 | 5145 | 4906 | 5639 |
| time over the response line (% of samples) | 46.17 | 43.93 | 41.62 | 39.62 | 45.96 | 43.42 | 35 | 33.69 | 43.84 | 41.24 | 44.37 | 40.74 | 35.8 | 34.7 |
| failed requests (%) | 28.99 | 29.75 | 21.74 | 22.87 | 31.22 | 31.76 | 21.17 | 21.5 | 26.31 | 26.87 | 24.27 | 24.98 | 14.32 | 16.61 |
| HPA replicas, mean | 9.631 | 14.32 | 9.685 | 13.68 | 9.642 | 13.96 | 9.605 | 14.38 | 9.682 | 13.2 | 9.674 | 12.38 | 9.654 | 13.67 |
| pods started | 5.257 | 10.54 | 4.657 | 10 | 4.971 | 10.2 | 5.2 | 11.51 | 4.657 | 10.51 | 4.714 | 9.343 | 4.943 | 10.51 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 5.999 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.5 | 184.7 | 184 | 184.9 | 184 | 184.4 | 183.4 | 183.4 | 184 | 184.5 | 184.3 | 184.3 | 183.4 | 183.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.5 | 184.7 | 184 | 184.9 | 184 | 184.4 | 183.4 | 183.4 | 184 | 184.5 | 184.3 | 184.3 | 183.4 | 183.7 |
| CPU used with Omni's own (cores), mean | 2.424 | 2.469 | 2.413 | 2.457 | 2.394 | 2.435 | 2.291 | 2.338 | 2.367 | 2.419 | 2.378 | 2.419 | 2.308 | 2.366 |
| host CPU busy, the real machine under kind (%) | 71.35 | 73.1 | 70.63 | 72.64 | 70.77 | 72.51 | 67.59 | 69.53 | 69.34 | 71.62 | 70.46 | 73 | 68.63 | 72.69 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0 | 0.5629 | 0.02571 | 0.01429 | 0.02 | 0.002857 | 0.02571 | 0.01429 | 0.002857 | 0.09714 | 0.2314 | 0.1429 | 0.1571 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2958 | 3727 | +26.0% | +116.3 to +1422 | LOSS |
| response time (ms), 99th percentile | 5331 | 6335 | +18.8% | +311.9 to +1697 | LOSS |
| time over the response line (% of samples) | 46.17 | 43.93 | -4.8% | -3.53 to -0.9419 | GAIN |
| failed requests (%) | 28.99 | 29.75 | +2.6% | -0.6875 to +2.2 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.631 | 14.32 | +48.6% | +4.435 to +4.935 | power given |
| pods started | 5.257 | 10.54 | +100.5% | +4.611 to +5.96 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.299e-16 to -3.136e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.5 | 184.7 | +0.1% | -0.426 to +0.782 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.5 | 184.7 | +0.1% | -0.426 to +0.782 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.424 | 2.469 | +1.9% | +0.03536 to +0.05523 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.35 | 73.1 | +2.5% | +1.524 to +1.981 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 0

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2436 | 3209 | +31.8% | +185.8 to +1361 | LOSS |
| response time (ms), 99th percentile | 4890 | 5963 | +21.9% | +160.6 to +1985 | LOSS |
| time over the response line (% of samples) | 41.62 | 39.62 | -4.8% | -3.624 to -0.3603 | GAIN |
| failed requests (%) | 21.74 | 22.87 | +5.2% | +0.1766 to +2.078 | LOSS |
| HPA replicas, mean | 9.685 | 13.68 | +41.2% | +3.521 to +4.462 | power given |
| pods started | 4.657 | 10 | +114.7% | +4.754 to +5.932 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.548e-16 to +3.548e-16 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 184.9 | +0.5% | +0.2002 to +1.517 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 184.9 | +0.5% | +0.2002 to +1.517 | power given |
| CPU used with Omni's own (cores), mean | 2.413 | 2.457 | +1.8% | +0.03087 to +0.05733 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.63 | 72.64 | +2.9% | +1.623 to +2.409 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.5629 | 0.02571 | -95.4% | -1.653 to +0.5784 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2391 | 3291 | +37.7% | +331.1 to +1470 | LOSS |
| response time (ms), 99th percentile | 4831 | 6223 | +28.8% | +662.4 to +2121 | LOSS |
| time over the response line (% of samples) | 45.96 | 43.42 | -5.5% | -3.691 to -1.401 | GAIN |
| failed requests (%) | 31.22 | 31.76 | +1.7% | -0.8527 to +1.923 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.642 | 13.96 | +44.8% | +4.031 to +4.615 | power given |
| pods started | 4.971 | 10.2 | +105.2% | +4.675 to +5.782 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.728e-16 to +2.713e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 184.4 | +0.2% | -0.2335 to +0.9401 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 184.4 | +0.2% | -0.2335 to +0.9401 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.394 | 2.435 | +1.7% | +0.02722 to +0.05523 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.77 | 72.51 | +2.5% | +1.391 to +2.094 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.01429 | 0.02 | +40.0% | -0.01083 to +0.02226 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3001 | 3247 | +8.2% | -426.3 to +918.2 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5198 | 5556 | +6.9% | -252.6 to +968.3 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 35 | 33.69 | -3.7% | -2.263 to -0.3395 | GAIN |
| failed requests (%) | 21.17 | 21.5 | +1.6% | -0.5051 to +1.167 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.605 | 14.38 | +49.7% | +4.526 to +5.014 | power given |
| pods started | 5.2 | 11.51 | +121.4% | +5.802 to +6.826 | power given |
| worker nodes in service, mean | 5.999 | 6 | +0.0% | -0.0005793 to +0.001702 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.4 | 183.4 | -0.0% | -0.5956 to +0.5667 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.4 | 183.4 | -0.0% | -0.5911 to +0.5848 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.291 | 2.338 | +2.1% | +0.03443 to +0.0611 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.59 | 69.53 | +2.9% | +1.568 to +2.326 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.002857 | 0.02571 | +800.0% | +0.008224 to +0.03749 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2447 | 4094 | +67.3% | +796.6 to +2497 | LOSS |
| response time (ms), 99th percentile | 5156 | 6281 | +21.8% | +511.2 to +1738 | LOSS |
| time over the response line (% of samples) | 43.84 | 41.24 | -5.9% | -3.998 to -1.209 | GAIN |
| failed requests (%) | 26.31 | 26.87 | +2.1% | -0.8926 to +2.006 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.682 | 13.2 | +36.4% | +3.058 to +3.985 | power given |
| pods started | 4.657 | 10.51 | +125.8% | +5.267 to +6.447 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.683e-16 to +2.115e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 184.5 | +0.3% | -0.05754 to +1.139 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 184.5 | +0.3% | -0.05754 to +1.139 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.367 | 2.419 | +2.2% | +0.04498 to +0.0609 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.34 | 71.62 | +3.3% | +2.048 to +2.517 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.01429 | 0.002857 | -80.0% | -0.0253 to +0.00244 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3006 | 2917 | -3.0% | -398.7 to +220.3 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5564 | 5145 | -7.5% | -912.2 to +74.23 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 44.37 | 40.74 | -8.2% | -5.09 to -2.171 | GAIN |
| failed requests (%) | 24.27 | 24.98 | +2.9% | -0.7024 to +2.122 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.674 | 12.38 | +27.9% | +2.022 to +3.383 | power given |
| pods started | 4.714 | 9.343 | +98.2% | +3.829 to +5.428 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.717e-16 to +1.165e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 184.3 | +0.0% | -0.4671 to +0.4708 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.3 | 184.3 | +0.0% | -0.4671 to +0.4708 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.378 | 2.419 | +1.7% | +0.03009 to +0.0504 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.46 | 73 | +3.6% | +2.271 to +2.801 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.09714 | 0.2314 | +138.2% | +0.1067 to +0.1618 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2993 | 3620 | +21.0% | +199.8 to +1055 | LOSS |
| response time (ms), 99th percentile | 4906 | 5639 | +14.9% | +189.8 to +1277 | LOSS |
| time over the response line (% of samples) | 35.8 | 34.7 | -3.1% | -3.232 to +1.023 | STEADY, inside the noise (cut) |
| failed requests (%) | 14.32 | 16.61 | +16.0% | +1.027 to +3.553 | LOSS |
| HPA replicas, mean | 9.654 | 13.67 | +41.6% | +3.331 to +4.696 | power given |
| pods started | 4.943 | 10.51 | +112.7% | +4.919 to +6.224 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.815e-16 to +2.263e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.4 | 183.7 | +0.1% | -0.1946 to +0.6675 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.4 | 183.7 | +0.1% | -0.1946 to +0.6675 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.308 | 2.366 | +2.5% | +0.04578 to +0.07 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.63 | 72.69 | +5.9% | +3.704 to +4.424 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1429 | 0.1571 | +10.0% | -0.007978 to +0.03655 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
