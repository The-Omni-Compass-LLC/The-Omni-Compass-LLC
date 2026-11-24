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
| response time (ms), 95th percentile | 3812 | 3810 | 1999 | 2680 | 2931 | 4101 | 2515 | 3679 | 2641 | 3928 | 2598 | 3075 | 2297 | 3367 |
| response time (ms), 99th percentile | 6259 | 6451 | 4009 | 4630 | 5560 | 6619 | 4986 | 6425 | 5174 | 6090 | 5356 | 5341 | 4639 | 5305 |
| time over the response line (% of samples) | 42.67 | 40.5 | 34.08 | 32.31 | 49.69 | 48.19 | 44.27 | 43.26 | 43.92 | 41.46 | 48.37 | 45.89 | 37.35 | 38.42 |
| failed requests (%) | 24.98 | 25.61 | 17.15 | 17.85 | 33.18 | 32.74 | 29.2 | 29.1 | 25.99 | 25.98 | 32.19 | 33.02 | 17.69 | 20.61 |
| HPA replicas, mean | 9.627 | 14.45 | 9.633 | 13.22 | 9.676 | 14.46 | 9.655 | 14.24 | 9.645 | 13.39 | 9.703 | 12.17 | 9.664 | 13.14 |
| pods started | 5.2 | 11.34 | 5.257 | 10.57 | 4.543 | 10.23 | 4.8 | 10.49 | 5.143 | 10.63 | 4.343 | 9.743 | 4.857 | 9.971 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 5.999 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.6 | 184.4 | 183 | 183.4 | 184.9 | 184.7 | 184.5 | 184.1 | 184.1 | 184.3 | 184.6 | 184.7 | 183.6 | 183.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.6 | 184.4 | 183 | 183.4 | 184.9 | 184.7 | 184.5 | 184.1 | 184.1 | 184.3 | 184.6 | 184.7 | 183.6 | 183.8 |
| CPU used with Omni's own (cores), mean | 2.419 | 2.467 | 2.269 | 2.314 | 2.447 | 2.503 | 2.396 | 2.443 | 2.369 | 2.418 | 2.409 | 2.45 | 2.325 | 2.393 |
| host CPU busy, the real machine under kind (%) | 71.27 | 73.25 | 66.8 | 69.19 | 73.16 | 75.21 | 71.31 | 73.31 | 69.85 | 72.06 | 72.1 | 74.93 | 69.99 | 74.65 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0 | 0.01714 | 0.03429 | 0.002857 | 0.005714 | 0.005714 | 0.01143 | 0.01143 | 0.01714 | 0.1 | 0.1057 | 0.1543 | 0.18 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3812 | 3810 | -0.0% | -591.4 to +588.1 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6259 | 6451 | +3.1% | -408.2 to +791.4 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 42.67 | 40.5 | -5.1% | -3.257 to -1.084 | GAIN |
| failed requests (%) | 24.98 | 25.61 | +2.5% | -0.6517 to +1.914 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.627 | 14.45 | +50.1% | +4.565 to +5.074 | power given |
| pods started | 5.2 | 11.34 | +118.1% | +5.663 to +6.622 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.844e-16 to +4.336e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.6 | 184.4 | -0.1% | -0.6617 to +0.4258 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.6 | 184.4 | -0.1% | -0.6617 to +0.4258 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.419 | 2.467 | +2.0% | +0.04163 to +0.05565 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.27 | 73.25 | +2.8% | +1.804 to +2.153 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1999 | 2680 | +34.1% | +215.4 to +1147 | LOSS |
| response time (ms), 99th percentile | 4009 | 4630 | +15.5% | +57.78 to +1185 | LOSS |
| time over the response line (% of samples) | 34.08 | 32.31 | -5.2% | -3.103 to -0.4319 | GAIN |
| failed requests (%) | 17.15 | 17.85 | +4.1% | -0.3758 to +1.768 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.633 | 13.22 | +37.3% | +2.926 to +4.254 | power given |
| pods started | 5.257 | 10.57 | +101.1% | +4.681 to +5.947 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.154e-16 to +7.214e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183 | 183.4 | +0.2% | -0.01022 to +0.8857 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183 | 183.4 | +0.2% | -0.01022 to +0.8857 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.269 | 2.314 | +2.0% | +0.03668 to +0.053 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.8 | 69.19 | +3.6% | +2.142 to +2.624 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.01714 | 0.03429 | +100.0% | -0.004072 to +0.03836 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2931 | 4101 | +39.9% | +486.7 to +1853 | LOSS |
| response time (ms), 99th percentile | 5560 | 6619 | +19.1% | +446.1 to +1674 | LOSS |
| time over the response line (% of samples) | 49.69 | 48.19 | -3.0% | -3.028 to +0.02919 | STEADY, inside the noise (cut) |
| failed requests (%) | 33.18 | 32.74 | -1.3% | -1.551 to +0.673 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.676 | 14.46 | +49.4% | +4.566 to +5 | power given |
| pods started | 4.543 | 10.23 | +125.2% | +5.104 to +6.267 | power given |
| worker nodes in service, mean | 5.999 | 6 | +0.0% | -0.001211 to +0.003558 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.9 | 184.7 | -0.1% | -0.7064 to +0.1758 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.9 | 184.7 | -0.1% | -0.685 to +0.202 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.447 | 2.503 | +2.3% | +0.04934 to +0.06317 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.16 | 75.21 | +2.8% | +1.938 to +2.165 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.002857 | 0.005714 | +100.0% | -0.007297 to +0.01301 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2515 | 3679 | +46.2% | +595.2 to +1731 | LOSS |
| response time (ms), 99th percentile | 4986 | 6425 | +28.9% | +683.4 to +2195 | LOSS |
| time over the response line (% of samples) | 44.27 | 43.26 | -2.3% | -1.875 to -0.1359 | GAIN |
| failed requests (%) | 29.2 | 29.1 | -0.3% | -1.395 to +1.192 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.655 | 14.24 | +47.5% | +4.274 to +4.897 | power given |
| pods started | 4.8 | 10.49 | +118.5% | +5.092 to +6.279 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.608e-16 to +4.623e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.5 | 184.1 | -0.2% | -0.8518 to +0.0535 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.5 | 184.1 | -0.2% | -0.8518 to +0.0535 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.396 | 2.443 | +2.0% | +0.03848 to +0.05586 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.31 | 73.31 | +2.8% | +1.766 to +2.248 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.005714 | 0.01143 | +100.0% | -0.008576 to +0.02 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2641 | 3928 | +48.7% | +542.1 to +2030 | LOSS |
| response time (ms), 99th percentile | 5174 | 6090 | +17.7% | +355.9 to +1476 | LOSS |
| time over the response line (% of samples) | 43.92 | 41.46 | -5.6% | -4.002 to -0.9239 | GAIN |
| failed requests (%) | 25.99 | 25.98 | -0.1% | -1.379 to +1.348 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.645 | 13.39 | +38.8% | +3.287 to +4.201 | power given |
| pods started | 5.143 | 10.63 | +106.7% | +4.787 to +6.185 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.184e-16 to +2.139e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 184.3 | +0.1% | -0.3376 to +0.7728 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.3 | +0.1% | -0.3376 to +0.7728 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.369 | 2.418 | +2.1% | +0.04263 to +0.05495 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.85 | 72.06 | +3.2% | +1.999 to +2.425 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.01143 | 0.01714 | +50.0% | -0.01281 to +0.02423 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2598 | 3075 | +18.3% | -277.8 to +1231 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5356 | 5341 | -0.3% | -750 to +720.2 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 48.37 | 45.89 | -5.1% | -3.846 to -1.133 | GAIN |
| failed requests (%) | 32.19 | 33.02 | +2.6% | -0.7559 to +2.412 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.703 | 12.17 | +25.5% | +1.688 to +3.256 | power given |
| pods started | 4.343 | 9.743 | +124.3% | +4.822 to +5.978 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.113e-16 to +3.067e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.6 | 184.7 | +0.1% | -0.3207 to +0.5601 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.6 | 184.7 | +0.1% | -0.3207 to +0.5601 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.409 | 2.45 | +1.7% | +0.03154 to +0.05038 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.1 | 74.93 | +3.9% | +2.575 to +3.069 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.1 | 0.1057 | +5.7% | -0.008576 to +0.02 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2297 | 3367 | +46.6% | +429.8 to +1711 | LOSS |
| response time (ms), 99th percentile | 4639 | 5305 | +14.4% | +142.5 to +1189 | LOSS |
| time over the response line (% of samples) | 37.35 | 38.42 | +2.9% | -1.054 to +3.197 | STEADY, inside the noise (up) |
| failed requests (%) | 17.69 | 20.61 | +16.5% | +1.69 to +4.156 | LOSS |
| HPA replicas, mean | 9.664 | 13.14 | +36.0% | +2.709 to +4.251 | power given |
| pods started | 4.857 | 9.971 | +105.3% | +4.423 to +5.805 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.413e-16 to +2.352e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.6 | 183.8 | +0.1% | -0.2463 to +0.6911 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.6 | 183.8 | +0.1% | -0.2463 to +0.6911 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.325 | 2.393 | +2.9% | +0.05415 to +0.08173 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.99 | 74.65 | +6.7% | +4.316 to +5.005 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1543 | 0.18 | +16.7% | -0.005835 to +0.05726 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
