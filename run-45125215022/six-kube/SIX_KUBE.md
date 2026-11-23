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
| response time (ms), 95th percentile | 2946 | 3161 | 2017 | 3097 | 2340 | 3764 | 2312 | 3445 | 2614 | 3867 | 2940 | 3172 | 2225 | 3494 |
| response time (ms), 99th percentile | 5322 | 5589 | 4064 | 5913 | 5289 | 6449 | 4420 | 5939 | 5274 | 6266 | 5528 | 6147 | 4430 | 5509 |
| time over the response line (% of samples) | 38.18 | 37.19 | 44.21 | 43.33 | 44.67 | 43.69 | 44.76 | 43.37 | 43.02 | 40.74 | 48.37 | 45.94 | 44.39 | 48.73 |
| failed requests (%) | 23.15 | 23.89 | 24.7 | 25.97 | 30.17 | 30.7 | 30.31 | 30.44 | 23.98 | 24.34 | 29.87 | 29.59 | 23.89 | 27.82 |
| HPA replicas, mean | 9.61 | 14.48 | 9.693 | 13.03 | 9.674 | 14.08 | 9.654 | 14.3 | 9.655 | 13.38 | 9.724 | 12.2 | 9.747 | 12.22 |
| pods started | 5.343 | 11.29 | 4.429 | 10.2 | 4.429 | 10.09 | 4.8 | 10.43 | 5.143 | 11.09 | 4.057 | 9.029 | 3.657 | 8.886 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 183.8 | 184 | 184.4 | 184.3 | 184.5 | 184.2 | 184.3 | 184.1 | 184.9 | 185.1 | 184.7 | 184.7 | 184.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 183.8 | 184 | 184.4 | 184.3 | 184.5 | 184.2 | 184.3 | 184.1 | 184.9 | 185.1 | 184.7 | 184.7 | 184.6 |
| CPU used with Omni's own (cores), mean | 2.333 | 2.385 | 2.388 | 2.447 | 2.387 | 2.437 | 2.386 | 2.44 | 2.414 | 2.467 | 2.449 | 2.492 | 2.415 | 2.467 |
| host CPU busy, the real machine under kind (%) | 69.02 | 71.11 | 70.51 | 73.07 | 71.24 | 73.2 | 71.2 | 73.56 | 71.03 | 73.32 | 73.14 | 75.82 | 72.73 | 77.06 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0 | 0.01714 | 0.02857 | 0.005714 | 0.01143 | 0.01143 | 0.02286 | 0.01143 | 0.01143 | 0.09714 | 0.1086 | 0.16 | 0.18 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2946 | 3161 | +7.3% | -572.3 to +1003 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5322 | 5589 | +5.0% | -434.8 to +968.8 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 38.18 | 37.19 | -2.6% | -2.092 to +0.1201 | STEADY, inside the noise (cut) |
| failed requests (%) | 23.15 | 23.89 | +3.2% | -0.5054 to +1.996 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.61 | 14.48 | +50.6% | +4.699 to +5.035 | power given |
| pods started | 5.343 | 11.29 | +111.2% | +5.43 to +6.456 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.891e-16 to +4.414e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 183.8 | +0.0% | -0.5736 to +0.6059 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 183.8 | +0.0% | -0.5736 to +0.6059 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.333 | 2.385 | +2.2% | +0.04307 to +0.05947 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.02 | 71.11 | +3.0% | +1.897 to +2.294 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2017 | 3097 | +53.5% | +599.2 to +1561 | LOSS |
| response time (ms), 99th percentile | 4064 | 5913 | +45.5% | +1170 to +2527 | LOSS |
| time over the response line (% of samples) | 44.21 | 43.33 | -2.0% | -2.68 to +0.9331 | STEADY, inside the noise (cut) |
| failed requests (%) | 24.7 | 25.97 | +5.1% | +0.2911 to +2.248 | LOSS |
| HPA replicas, mean | 9.693 | 13.03 | +34.5% | +2.7 to +3.982 | power given |
| pods started | 4.429 | 10.2 | +130.3% | +5.188 to +6.355 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.255e-16 to -3.73e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 184.4 | +0.2% | -0.03542 to +0.9255 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 184.4 | +0.2% | -0.03542 to +0.9255 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.388 | 2.447 | +2.5% | +0.05155 to +0.06626 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.51 | 73.07 | +3.6% | +2.34 to +2.766 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.01714 | 0.02857 | +66.7% | -0.01025 to +0.03311 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2340 | 3764 | +60.8% | +645.9 to +2201 | LOSS |
| response time (ms), 99th percentile | 5289 | 6449 | +21.9% | +441.9 to +1878 | LOSS |
| time over the response line (% of samples) | 44.67 | 43.69 | -2.2% | -2.389 to +0.4328 | STEADY, inside the noise (cut) |
| failed requests (%) | 30.17 | 30.7 | +1.8% | -0.6518 to +1.713 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.674 | 14.08 | +45.6% | +4.118 to +4.698 | power given |
| pods started | 4.429 | 10.09 | +127.7% | +5.074 to +6.24 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.062e-16 to +3.554e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 184.5 | +0.1% | -0.2712 to +0.7421 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.3 | 184.5 | +0.1% | -0.2712 to +0.7421 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.387 | 2.437 | +2.1% | +0.03606 to +0.06417 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.24 | 73.2 | +2.8% | +1.593 to +2.327 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.005714 | 0.01143 | +100.0% | -0.008576 to +0.02 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2312 | 3445 | +49.0% | +665.4 to +1601 | LOSS |
| response time (ms), 99th percentile | 4420 | 5939 | +34.4% | +822.8 to +2216 | LOSS |
| time over the response line (% of samples) | 44.76 | 43.37 | -3.1% | -2.274 to -0.4977 | GAIN |
| failed requests (%) | 30.31 | 30.44 | +0.4% | -1.115 to +1.38 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.654 | 14.3 | +48.1% | +4.376 to +4.913 | power given |
| pods started | 4.8 | 10.43 | +117.3% | +4.977 to +6.28 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +3.73e-17 to +8.255e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.3 | +0.1% | -0.2932 to +0.5956 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.3 | +0.1% | -0.2932 to +0.5956 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.386 | 2.44 | +2.3% | +0.04372 to +0.06424 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.2 | 73.56 | +3.3% | +2.057 to +2.677 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.01143 | 0.02286 | +100.0% | -0.00244 to +0.0253 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2614 | 3867 | +47.9% | +565.1 to +1940 | LOSS |
| response time (ms), 99th percentile | 5274 | 6266 | +18.8% | +217.7 to +1767 | LOSS |
| time over the response line (% of samples) | 43.02 | 40.74 | -5.3% | -3.864 to -0.6924 | GAIN |
| failed requests (%) | 23.98 | 24.34 | +1.5% | -0.5367 to +1.257 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.655 | 13.38 | +38.5% | +3.245 to +4.198 | power given |
| pods started | 5.143 | 11.09 | +115.6% | +5.11 to +6.776 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.22e-16 to +6.222e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 184.9 | +0.4% | +0.3335 to +1.286 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.9 | +0.4% | +0.3335 to +1.286 | power given |
| CPU used with Omni's own (cores), mean | 2.414 | 2.467 | +2.2% | +0.04568 to +0.05974 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.03 | 73.32 | +3.2% | +2.109 to +2.479 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.01143 | 0.01143 | +0.0% | -0.01666 to +0.01666 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2940 | 3172 | +7.9% | -460.7 to +924.8 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5528 | 6147 | +11.2% | -21.66 to +1259 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 48.37 | 45.94 | -5.0% | -3.845 to -1.011 | GAIN |
| failed requests (%) | 29.87 | 29.59 | -0.9% | -1.991 to +1.438 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.724 | 12.2 | +25.5% | +1.79 to +3.171 | power given |
| pods started | 4.057 | 9.029 | +122.5% | +4.224 to +5.719 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.905e-16 to +3.383e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.1 | 184.7 | -0.2% | -0.8619 to +0.05863 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.1 | 184.7 | -0.2% | -0.8619 to +0.05863 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.449 | 2.492 | +1.8% | +0.03368 to +0.05207 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.14 | 75.82 | +3.7% | +2.476 to +2.887 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.09714 | 0.1086 | +11.8% | -0.00244 to +0.0253 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2225 | 3494 | +57.0% | +825.8 to +1711 | LOSS |
| response time (ms), 99th percentile | 4430 | 5509 | +24.4% | +432.8 to +1727 | LOSS |
| time over the response line (% of samples) | 44.39 | 48.73 | +9.8% | +2.238 to +6.445 | LOSS |
| failed requests (%) | 23.89 | 27.82 | +16.5% | +2.432 to +5.433 | LOSS |
| HPA replicas, mean | 9.747 | 12.22 | +25.3% | +1.618 to +3.321 | power given |
| pods started | 3.657 | 8.886 | +143.0% | +4.395 to +6.062 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.071e-16 to +7.161e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.7 | 184.6 | -0.0% | -0.5319 to +0.4082 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.7 | 184.6 | -0.0% | -0.5319 to +0.4082 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.415 | 2.467 | +2.1% | +0.04224 to +0.06089 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.73 | 77.06 | +6.0% | +4.099 to +4.561 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.16 | 0.18 | +12.5% | -6.223e-05 to +0.04006 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
