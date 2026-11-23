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
| response time (ms), 95th percentile | 2082 | 3005 | 2301 | 2760 | 2497 | 3817 | 2541 | 2863 | 2147 | 3396 | 2442 | 2795 | 2446 | 3358 |
| response time (ms), 99th percentile | 4313 | 5396 | 4601 | 5274 | 5504 | 6736 | 5003 | 5283 | 4593 | 5561 | 4779 | 5436 | 4562 | 5445 |
| time over the response line (% of samples) | 36.83 | 35.2 | 32.7 | 30.02 | 46.02 | 44.67 | 36.31 | 35.42 | 41.22 | 39.82 | 48.06 | 44.52 | 39.31 | 42.19 |
| failed requests (%) | 23.48 | 23.57 | 13.89 | 14.69 | 30.32 | 30.03 | 22.82 | 23.86 | 24.2 | 26.15 | 31.36 | 30.92 | 20.52 | 24.34 |
| HPA replicas, mean | 9.602 | 14.26 | 9.612 | 13.8 | 9.68 | 14.37 | 9.618 | 14.18 | 9.674 | 13.03 | 9.675 | 11.86 | 9.696 | 12.72 |
| pods started | 5.286 | 11.17 | 5.571 | 11.11 | 4.486 | 10.4 | 5.029 | 11.14 | 4.686 | 10.57 | 4.629 | 9.571 | 4.343 | 9.371 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.4 | 183.4 | 183.5 | 183.8 | 184.6 | 184.8 | 183.4 | 183.2 | 183.5 | 184.2 | 184.4 | 184.4 | 183.5 | 183.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.4 | 183.4 | 183.5 | 183.8 | 184.6 | 184.8 | 183.4 | 183.2 | 183.5 | 184.2 | 184.4 | 184.4 | 183.5 | 183.7 |
| CPU used with Omni's own (cores), mean | 2.297 | 2.344 | 2.306 | 2.365 | 2.421 | 2.482 | 2.277 | 2.333 | 2.349 | 2.401 | 2.386 | 2.421 | 2.324 | 2.377 |
| host CPU busy, the real machine under kind (%) | 68.1 | 70.04 | 67.74 | 70.48 | 72.21 | 74.4 | 67.85 | 70.08 | 69.37 | 71.73 | 71.49 | 74 | 69.86 | 74.01 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.002857 | 0 | 0.01429 | 0.02857 | 0.008571 | 0.008571 | 0.008571 | 0.008571 | 0.005714 | 0.01714 | 0.09714 | 0.1086 | 0.14 | 0.1971 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2082 | 3005 | +44.3% | +262.9 to +1583 | LOSS |
| response time (ms), 99th percentile | 4313 | 5396 | +25.1% | +307 to +1858 | LOSS |
| time over the response line (% of samples) | 36.83 | 35.2 | -4.4% | -2.559 to -0.7044 | GAIN |
| failed requests (%) | 23.48 | 23.57 | +0.4% | -1.08 to +1.263 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.602 | 14.26 | +48.5% | +4.392 to +4.915 | power given |
| pods started | 5.286 | 11.17 | +111.4% | +5.36 to +6.411 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.674e-16 to +2.629e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.4 | 183.4 | +0.0% | -0.5436 to +0.6325 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.4 | 183.4 | +0.0% | -0.5436 to +0.6325 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.297 | 2.344 | +2.1% | +0.03785 to +0.05697 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.1 | 70.04 | +2.8% | +1.691 to +2.18 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0.002857 | 0 | -100.0% | -0.008663 to +0.002949 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2301 | 2760 | +19.9% | +46.04 to +870.5 | LOSS |
| response time (ms), 99th percentile | 4601 | 5274 | +14.6% | +72.62 to +1275 | LOSS |
| time over the response line (% of samples) | 32.7 | 30.02 | -8.2% | -3.75 to -1.617 | GAIN |
| failed requests (%) | 13.89 | 14.69 | +5.8% | +0.06124 to +1.547 | LOSS |
| HPA replicas, mean | 9.612 | 13.8 | +43.6% | +3.634 to +4.747 | power given |
| pods started | 5.571 | 11.11 | +99.5% | +4.859 to +6.226 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.641e-16 to -1.525e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 183.8 | +0.2% | -0.06596 to +0.7955 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 183.8 | +0.2% | -0.06596 to +0.7955 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.306 | 2.365 | +2.6% | +0.04798 to +0.07096 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.74 | 70.48 | +4.0% | +2.391 to +3.077 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.01429 | 0.02857 | +100.0% | -0.009486 to +0.03806 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2497 | 3817 | +52.9% | +628.9 to +2012 | LOSS |
| response time (ms), 99th percentile | 5504 | 6736 | +22.4% | +480.8 to +1983 | LOSS |
| time over the response line (% of samples) | 46.02 | 44.67 | -2.9% | -2.702 to +0.0008715 | STEADY, inside the noise (cut) |
| failed requests (%) | 30.32 | 30.03 | -0.9% | -1.315 to +0.751 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.68 | 14.37 | +48.4% | +4.441 to +4.935 | power given |
| pods started | 4.486 | 10.4 | +131.8% | +5.353 to +6.475 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.423e-16 to +1.347e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.6 | 184.8 | +0.1% | -0.3578 to +0.7348 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.6 | 184.8 | +0.1% | -0.3578 to +0.7348 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.421 | 2.482 | +2.5% | +0.05066 to +0.07066 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.21 | 74.4 | +3.0% | +1.878 to +2.491 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.008571 | 0.008571 | +0.0% | -0.01443 to +0.01443 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2541 | 2863 | +12.7% | -264.9 to +907.9 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5003 | 5283 | +5.6% | -379.2 to +939.2 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 36.31 | 35.42 | -2.4% | -1.878 to +0.1082 | STEADY, inside the noise (cut) |
| failed requests (%) | 22.82 | 23.86 | +4.6% | -0.1622 to +2.249 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.618 | 14.18 | +47.5% | +4.27 to +4.861 | power given |
| pods started | 5.029 | 11.14 | +121.6% | +5.623 to +6.606 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.815e-16 to +2.263e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.4 | 183.2 | -0.1% | -0.6282 to +0.2002 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.4 | 183.2 | -0.1% | -0.6282 to +0.2002 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.277 | 2.333 | +2.5% | +0.04842 to +0.06399 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.85 | 70.08 | +3.3% | +2.008 to +2.461 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.008571 | 0.008571 | +0.0% | -0.01443 to +0.01443 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2147 | 3396 | +58.2% | +516.9 to +1982 | LOSS |
| response time (ms), 99th percentile | 4593 | 5561 | +21.1% | +314.6 to +1622 | LOSS |
| time over the response line (% of samples) | 41.22 | 39.82 | -3.4% | -2.979 to +0.1785 | STEADY, inside the noise (cut) |
| failed requests (%) | 24.2 | 26.15 | +8.0% | +0.5989 to +3.293 | LOSS |
| HPA replicas, mean | 9.674 | 13.03 | +34.6% | +2.741 to +3.96 | power given |
| pods started | 4.686 | 10.57 | +125.6% | +5.275 to +6.497 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.679e-16 to +4.679e-16 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 184.2 | +0.4% | +0.3124 to +1.131 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 184.2 | +0.4% | +0.3124 to +1.131 | power given |
| CPU used with Omni's own (cores), mean | 2.349 | 2.401 | +2.2% | +0.03893 to +0.06535 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.37 | 71.73 | +3.4% | +1.895 to +2.812 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.005714 | 0.01714 | +200.0% | -0.00244 to +0.0253 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2442 | 2795 | +14.5% | -177.8 to +883.9 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4779 | 5436 | +13.7% | +14.49 to +1299 | LOSS |
| time over the response line (% of samples) | 48.06 | 44.52 | -7.4% | -4.997 to -2.083 | GAIN |
| failed requests (%) | 31.36 | 30.92 | -1.4% | -1.353 to +0.4796 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.675 | 11.86 | +22.6% | +1.441 to +2.934 | power given |
| pods started | 4.629 | 9.571 | +106.8% | +4.131 to +5.755 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.973e-16 to +2.958e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184.4 | +0.0% | -0.394 to +0.4751 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184.4 | +0.0% | -0.394 to +0.4751 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.386 | 2.421 | +1.5% | +0.02426 to +0.04733 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.49 | 74 | +3.5% | +2.113 to +2.917 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.09714 | 0.1086 | +11.8% | +0.0003412 to +0.02252 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2446 | 3358 | +37.3% | +375.8 to +1448 | LOSS |
| response time (ms), 99th percentile | 4562 | 5445 | +19.4% | +251.8 to +1514 | LOSS |
| time over the response line (% of samples) | 39.31 | 42.19 | +7.3% | +1.167 to +4.589 | LOSS |
| failed requests (%) | 20.52 | 24.34 | +18.6% | +2.5 to +5.126 | LOSS |
| HPA replicas, mean | 9.696 | 12.72 | +31.2% | +2.245 to +3.804 | power given |
| pods started | 4.343 | 9.371 | +115.8% | +4.223 to +5.834 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.177e-16 to +6.76e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 183.7 | +0.1% | -0.1965 to +0.6823 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 183.7 | +0.1% | -0.1965 to +0.6823 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.324 | 2.377 | +2.3% | +0.0417 to +0.06388 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.86 | 74.01 | +5.9% | +3.862 to +4.443 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.14 | 0.1971 | +40.8% | +0.02251 to +0.09178 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
