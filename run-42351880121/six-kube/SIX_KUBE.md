# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 10 copies: native | The spine, the muscles every stack runs on, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2329 | 3415 | 3087 | 3535 | 3073 | 3814 | 2482 | 3471 | 2870 | 3135 | 2448 | 3475 |
| response time (ms), 99th percentile | 4540 | 5677 | 5541 | 6130 | 5523 | 6222 | 4950 | 5461 | 5465 | 5501 | 4715 | 5460 |
| time over the response line (% of samples) | 38.22 | 37.18 | 42.04 | 39.85 | 39.44 | 38.73 | 37.28 | 35.06 | 53.34 | 49.76 | 40.04 | 42.5 |
| failed requests (%) | 24.99 | 24.92 | 27.4 | 27.81 | 25.25 | 24.5 | 21.35 | 21.1 | 35.15 | 35.26 | 20.01 | 23.45 |
| HPA replicas, mean | 9.618 | 14.12 | 9.622 | 14.28 | 9.619 | 14.11 | 9.622 | 13.62 | 9.711 | 11.86 | 9.7 | 12.63 |
| pods started | 5.122 | 10.95 | 5.122 | 11.24 | 5.146 | 11.27 | 5.317 | 11.17 | 4.22 | 8.951 | 4.244 | 9.22 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.3 | 183.5 | 184.1 | 184.1 | 184 | 183.8 | 183.3 | 183.7 | 184.8 | 185.2 | 183.8 | 183.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.3 | 183.5 | 184.1 | 184.1 | 184 | 183.8 | 183.3 | 183.7 | 184.8 | 185.2 | 183.8 | 183.9 |
| CPU used with Omni's own (cores), mean | 2.281 | 2.349 | 2.362 | 2.401 | 2.342 | 2.384 | 2.288 | 2.347 | 2.443 | 2.484 | 2.349 | 2.4 |
| host CPU busy, the real machine under kind (%) | 67.29 | 69.7 | 69.64 | 71.4 | 69.15 | 70.99 | 67.04 | 69.56 | 72.64 | 75.38 | 70.23 | 74.29 |
| organism work | 2.148e+11 | 2.148e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0 | 0.007317 | 0.01463 | 0 | 0.007317 | 0.007317 | 0.0122 | 0.1 | 0.2195 | 0.1537 | 0.1732 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2329 | 3415 | +46.6% | +530.4 to +1641 | LOSS |
| response time (ms), 99th percentile | 4540 | 5677 | +25.0% | +456.9 to +1815 | LOSS |
| time over the response line (% of samples) | 38.22 | 37.18 | -2.7% | -2.012 to -0.07595 | GAIN |
| failed requests (%) | 24.99 | 24.92 | -0.3% | -1.121 to +0.9806 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.618 | 14.12 | +46.8% | +4.255 to +4.748 | power given |
| pods started | 5.122 | 10.95 | +113.8% | +5.256 to +6.402 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.506e-16 to +2.039e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.3 | 183.5 | +0.1% | -0.2208 to +0.7385 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.3 | 183.5 | +0.1% | -0.2208 to +0.7385 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.281 | 2.349 | +3.0% | +0.05194 to +0.08326 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.29 | 69.7 | +3.6% | +1.97 to +2.855 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008375 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3087 | 3535 | +14.5% | -270.8 to +1168 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5541 | 6130 | +10.6% | +36.21 to +1140 | LOSS |
| time over the response line (% of samples) | 42.04 | 39.85 | -5.2% | -3.164 to -1.218 | GAIN |
| failed requests (%) | 27.4 | 27.81 | +1.5% | -0.7583 to +1.571 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.622 | 14.28 | +48.4% | +4.374 to +4.935 | power given |
| pods started | 5.122 | 11.24 | +119.5% | +5.556 to +6.687 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.361e-16 to +2.028e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 184.1 | -0.0% | -0.5225 to +0.5036 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.1 | -0.0% | -0.5225 to +0.5036 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.362 | 2.401 | +1.6% | +0.02814 to +0.04934 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.64 | 71.4 | +2.5% | +1.447 to +2.074 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.007317 | 0.01463 | +100.0% | -0.007471 to +0.0221 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3073 | 3814 | +24.1% | +146 to +1336 | LOSS |
| response time (ms), 99th percentile | 5523 | 6222 | +12.7% | +178.3 to +1220 | LOSS |
| time over the response line (% of samples) | 39.44 | 38.73 | -1.8% | -1.597 to +0.1912 | STEADY, inside the noise (cut) |
| failed requests (%) | 25.25 | 24.5 | -3.0% | -1.894 to +0.3961 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.619 | 14.11 | +46.6% | +4.218 to +4.756 | power given |
| pods started | 5.146 | 11.27 | +119.0% | +5.251 to +6.993 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.055e-16 to +3.621e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 183.8 | -0.1% | -0.7204 to +0.391 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 183.8 | -0.1% | -0.7204 to +0.391 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.342 | 2.384 | +1.8% | +0.03298 to +0.05244 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.15 | 70.99 | +2.7% | +1.57 to +2.11 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0 | 0.007317 | +0.00732 | -0.001004 to +0.01564 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2482 | 3471 | +39.8% | +426.2 to +1551 | LOSS |
| response time (ms), 99th percentile | 4950 | 5461 | +10.3% | +37.45 to +984.6 | LOSS |
| time over the response line (% of samples) | 37.28 | 35.06 | -6.0% | -3.586 to -0.8625 | GAIN |
| failed requests (%) | 21.35 | 21.1 | -1.1% | -1.848 to +1.36 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.622 | 13.62 | +41.6% | +3.553 to +4.453 | power given |
| pods started | 5.317 | 11.17 | +110.1% | +5.201 to +6.506 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.412e-16 to +1.513e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.3 | 183.7 | +0.2% | -0.004834 to +0.8382 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.3 | 183.7 | +0.2% | -0.004834 to +0.8382 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.288 | 2.347 | +2.6% | +0.04496 to +0.07407 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.04 | 69.56 | +3.8% | +2.117 to +2.922 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.007317 | 0.0122 | +66.7% | -0.009151 to +0.01891 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2870 | 3135 | +9.2% | -369.8 to +900.1 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5465 | 5501 | +0.6% | -698.6 to +769.4 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 53.34 | 49.76 | -6.7% | -5.235 to -1.92 | GAIN |
| failed requests (%) | 35.15 | 35.26 | +0.3% | -1.083 to +1.302 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.711 | 11.86 | +22.1% | +1.482 to +2.811 | power given |
| pods started | 4.22 | 8.951 | +112.1% | +4.029 to +5.434 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.686e-16 to +4.869e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.8 | 185.2 | +0.2% | -0.02611 to +0.7245 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.8 | 185.2 | +0.2% | -0.02611 to +0.7245 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.443 | 2.484 | +1.7% | +0.02663 to +0.0549 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.64 | 75.38 | +3.8% | +2.307 to +3.171 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.1 | 0.2195 | +119.5% | +0.1034 to +0.1356 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2448 | 3475 | +41.9% | +619.1 to +1434 | LOSS |
| response time (ms), 99th percentile | 4715 | 5460 | +15.8% | +201.1 to +1288 | LOSS |
| time over the response line (% of samples) | 40.04 | 42.5 | +6.1% | +0.8057 to +4.113 | LOSS |
| failed requests (%) | 20.01 | 23.45 | +17.2% | +1.951 to +4.931 | LOSS |
| HPA replicas, mean | 9.7 | 12.63 | +30.2% | +2.169 to +3.685 | power given |
| pods started | 4.244 | 9.22 | +117.2% | +4.331 to +5.62 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.168e-16 to +2.359e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 183.9 | +0.0% | -0.364 to +0.4767 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 183.9 | +0.0% | -0.364 to +0.4767 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.349 | 2.4 | +2.2% | +0.03885 to +0.06312 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.23 | 74.29 | +5.8% | +3.709 to +4.4 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1537 | 0.1732 | +12.7% | -0.001917 to +0.04094 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
