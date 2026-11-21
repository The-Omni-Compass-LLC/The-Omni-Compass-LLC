# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 10 copies: native | The spine, the muscles every stack runs on, 10 copies: omni | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1920 | 3308 | 2495 | 2488 | 2674 | 2575 | 1476 | 1889 | 3003 | 3007 | 2343 | 3573 | 1904 | 3468 |
| response time (ms), 99th percentile | 4065 | 5691 | 4768 | 5505 | 5068 | 5484 | 3716 | 3761 | 5372 | 5766 | 5411 | 5993 | 4965 | 6036 |
| time over the response line (% of samples) | 46.12 | 44.04 | 40.04 | 35.36 | 44.29 | 40.84 | 30.34 | 28.91 | 46.53 | 41.71 | 45.73 | 43.57 | 55.09 | 55.65 |
| failed requests (%) | 32.83 | 32.4 | 21.18 | 20.9 | 28.89 | 28.92 | 20.42 | 20.03 | 29.69 | 28.54 | 32.44 | 33.07 | 34.75 | 37.75 |
| HPA replicas, mean | 9.654 | 13.8 | 9.653 | 14.11 | 9.625 | 13.69 | 9.577 | 12.49 | 9.66 | 13.42 | 9.766 | 14.34 | 9.888 | 13.17 |
| pods started | 4.9 | 9.2 | 5.2 | 9.4 | 5.5 | 9.8 | 5.4 | 8.7 | 5.1 | 9.3 | 3.5 | 8.1 | 1.8 | 4.8 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.7 | 185 | 183.4 | 183.3 | 184.4 | 184 | 182.7 | 182.2 | 183.8 | 183.6 | 184.8 | 184.8 | 186.1 | 185.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.7 | 185 | 183.4 | 183.3 | 184.4 | 184 | 182.7 | 182.2 | 183.8 | 183.6 | 184.8 | 184.8 | 186.1 | 185.4 |
| CPU used with Omni's own (cores), mean | 2.392 | 2.414 | 2.293 | 2.316 | 2.377 | 2.404 | 2.192 | 2.205 | 2.346 | 2.354 | 2.412 | 2.436 | 2.521 | 2.535 |
| host CPU busy, the real machine under kind (%) | 71.16 | 72.11 | 67.45 | 69.02 | 70.6 | 71.8 | 65.01 | 65.92 | 68.68 | 69.82 | 71.94 | 74.04 | 76.04 | 79.04 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.01 | 0 | 0.02 | 0.01 | 0 | 0.01 | 0.01 | 0 | 0.01 | 0 | 0.1 | 0.21 | 0.18 | 0.19 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1920 | 3308 | +72.3% | +572.4 to +2204 | LOSS |
| response time (ms), 99th percentile | 4065 | 5691 | +40.0% | +357.3 to +2895 | LOSS |
| time over the response line (% of samples) | 46.12 | 44.04 | -4.5% | -4.457 to +0.3005 | EVEN, inside the noise (cut) |
| failed requests (%) | 32.83 | 32.4 | -1.3% | -1.428 to +0.5688 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.654 | 13.8 | +43.0% | +2.565 to +5.734 | power given |
| pods started | 4.9 | 9.2 | +87.8% | +2.193 to +6.407 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.788e-16 to +3.235e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.7 | 185 | +0.2% | -0.4182 to +1.084 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.7 | 185 | +0.2% | -0.4182 to +1.084 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.392 | 2.414 | +0.9% | -0.0003897 to +0.04423 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.16 | 72.11 | +1.3% | +0.4101 to +1.49 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008375 to -0.0008374 | power given |
| organism behind its window (s) | 0.01 | 0 | -100.0% | -0.03262 to +0.01262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2495 | 2488 | -0.3% | -812.3 to +797.4 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4768 | 5505 | +15.4% | -663 to +2136 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 40.04 | 35.36 | -11.7% | -8.224 to -1.126 | GAIN |
| failed requests (%) | 21.18 | 20.9 | -1.3% | -1.218 to +0.651 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.653 | 14.11 | +46.1% | +3.288 to +5.619 | power given |
| pods started | 5.2 | 9.4 | +80.8% | +2.59 to +5.81 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.318e-16 to +1.009e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.4 | 183.3 | -0.1% | -1.087 to +0.7168 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.4 | 183.3 | -0.1% | -1.087 to +0.7168 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.293 | 2.316 | +1.0% | -0.001418 to +0.04607 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.45 | 69.02 | +2.3% | +0.9332 to +2.205 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.02 | 0.01 | -50.0% | -0.03262 to +0.01262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2674 | 2575 | -3.7% | -923.4 to +724.7 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5068 | 5484 | +8.2% | -148.8 to +979.5 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 44.29 | 40.84 | -7.8% | -4.887 to -2.016 | GAIN |
| failed requests (%) | 28.89 | 28.92 | +0.1% | -1.88 to +1.948 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.625 | 13.69 | +42.3% | +2.599 to +5.54 | power given |
| pods started | 5.5 | 9.8 | +78.2% | +2.828 to +5.772 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.436e-16 to +8.989e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184 | -0.2% | -1.558 to +0.8935 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184 | -0.2% | -1.558 to +0.8935 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.377 | 2.404 | +1.1% | +0.009962 to +0.04351 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.6 | 71.8 | +1.7% | +0.8742 to +1.516 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0 | 0.01 | +0.01 | -0.01262 to +0.03262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1476 | 1889 | +28.0% | -199.9 to +1025 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 3716 | 3761 | +1.2% | -864.8 to +954.3 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 30.34 | 28.91 | -4.7% | -2.936 to +0.07171 | EVEN, inside the noise (cut) |
| failed requests (%) | 20.42 | 20.03 | -1.9% | -2.76 to +1.985 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.577 | 12.49 | +30.4% | +1.126 to +4.696 | power given |
| pods started | 5.4 | 8.7 | +61.1% | +1.391 to +5.209 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.818e-16 to +9.594e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.7 | 182.2 | -0.3% | -1.364 to +0.3131 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.7 | 182.2 | -0.3% | -1.364 to +0.3131 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.192 | 2.205 | +0.6% | -0.0004323 to +0.0266 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.01 | 65.92 | +1.4% | +0.4883 to +1.343 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.01 | 0 | -100.0% | -0.03262 to +0.01262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3003 | 3007 | +0.2% | -891.1 to +900.2 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5372 | 5766 | +7.3% | -335.8 to +1125 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 46.53 | 41.71 | -10.4% | -7.656 to -1.997 | GAIN |
| failed requests (%) | 29.69 | 28.54 | -3.9% | -3.404 to +1.103 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.66 | 13.42 | +38.9% | +1.933 to +5.589 | power given |
| pods started | 5.1 | 9.3 | +82.4% | +1.869 to +6.531 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.718e-16 to +8.494e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 183.6 | -0.1% | -1.292 to +0.9321 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 183.6 | -0.1% | -1.292 to +0.9321 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.346 | 2.354 | +0.3% | -0.01151 to +0.02612 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.68 | 69.82 | +1.7% | +0.6181 to +1.649 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.01 | 0 | -100.0% | -0.03262 to +0.01262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2343 | 3573 | +52.5% | +255.9 to +2204 | LOSS |
| response time (ms), 99th percentile | 5411 | 5993 | +10.7% | -429.8 to +1593 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 45.73 | 43.57 | -4.7% | -4.244 to -0.08718 | GAIN |
| failed requests (%) | 32.44 | 33.07 | +1.9% | -1.499 to +2.747 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.766 | 14.34 | +46.8% | +4.184 to +4.96 | power given |
| pods started | 3.5 | 8.1 | +131.4% | +3.523 to +5.677 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.358e-15 to +1.149e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.8 | 184.8 | -0.0% | -1.177 to +1.092 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.8 | 184.8 | -0.0% | -1.177 to +1.092 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.412 | 2.436 | +1.0% | +0.0129 to +0.03471 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.94 | 74.04 | +2.9% | +1.721 to +2.485 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.1 | 0.21 | +110.0% | +0.08738 to +0.1326 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 3 (energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), EVEN (inside the noise) on 2

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1904 | 3468 | +82.2% | +572.1 to +2556 | LOSS |
| response time (ms), 99th percentile | 4965 | 6036 | +21.6% | -113.2 to +2255 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 55.09 | 55.65 | +1.0% | -2.667 to +3.77 | EVEN, inside the noise (up) |
| failed requests (%) | 34.75 | 37.75 | +8.6% | +1.711 to +4.292 | LOSS |
| HPA replicas, mean | 9.888 | 13.17 | +33.2% | +2.484 to +4.076 | power given |
| pods started | 1.8 | 4.8 | +166.7% | +2.174 to +3.826 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.167e-15 to +6.345e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186.1 | 185.4 | -0.4% | -1.173 to -0.1977 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.1 | 185.4 | -0.4% | -1.173 to -0.1977 | GAIN |
| CPU used with Omni's own (cores), mean | 2.521 | 2.535 | +0.5% | -0.02511 to +0.05226 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.04 | 79.04 | +3.9% | +1.887 to +4.12 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.18 | 0.19 | +5.6% | -0.01262 to +0.03262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
