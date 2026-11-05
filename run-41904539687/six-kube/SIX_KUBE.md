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
| response time (ms), 95th percentile | 2848 | 3856 | 2026 | 3124 | 3112 | 3352 | 2264 | 3116 | 2251 | 3075 | 2823 | 3718 | 1966 | 2939 |
| response time (ms), 99th percentile | 5224 | 6403 | 4201 | 5758 | 5710 | 6323 | 4509 | 5349 | 4838 | 5448 | 5229 | 6308 | 3870 | 4931 |
| time over the response line (% of samples) | 42.98 | 41.73 | 42.91 | 41.94 | 43.7 | 41.53 | 41.66 | 40.55 | 45.13 | 42 | 51.87 | 48.17 | 40.96 | 43.64 |
| failed requests (%) | 27.54 | 26.56 | 24.25 | 26.21 | 28.01 | 28.36 | 28.05 | 28.15 | 29.09 | 29.72 | 33.55 | 33.08 | 22.75 | 26.77 |
| HPA replicas, mean | 9.645 | 14.28 | 9.674 | 13.18 | 9.659 | 14.35 | 9.63 | 13.97 | 9.659 | 12.76 | 9.73 | 12.01 | 9.73 | 12.08 |
| pods started | 4.886 | 10.71 | 4.657 | 9.8 | 4.8 | 10.03 | 4.857 | 10.66 | 4.971 | 9.771 | 4 | 8.943 | 3.743 | 8.371 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 5.997 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 184.2 | 184 | 184.2 | 184.4 | 184.4 | 183.4 | 183.5 | 183.6 | 183.7 | 184.8 | 185.1 | 183.6 | 183.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.2 | 184 | 184.2 | 184.4 | 184.4 | 183.4 | 183.5 | 183.6 | 183.7 | 184.8 | 185.1 | 183.6 | 183.9 |
| CPU used with Omni's own (cores), mean | 2.377 | 2.425 | 2.361 | 2.413 | 2.394 | 2.446 | 2.323 | 2.369 | 2.34 | 2.376 | 2.443 | 2.477 | 2.318 | 2.367 |
| host CPU busy, the real machine under kind (%) | 69.95 | 71.93 | 69.46 | 71.67 | 71.02 | 73.01 | 69.05 | 70.92 | 68.86 | 70.74 | 72.77 | 75.17 | 69.56 | 73.68 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0.002857 | 0.02 | 0.01143 | 0.002857 | 0.01714 | 0.005714 | 0.01143 | 0.01429 | 0.008571 | 0.09714 | 0.2143 | 0.1629 | 0.1771 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2848 | 3856 | +35.4% | +292.6 to +1724 | LOSS |
| response time (ms), 99th percentile | 5224 | 6403 | +22.6% | +511.9 to +1845 | LOSS |
| time over the response line (% of samples) | 42.98 | 41.73 | -2.9% | -2.174 to -0.3215 | GAIN |
| failed requests (%) | 27.54 | 26.56 | -3.6% | -2.618 to +0.6507 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.645 | 14.28 | +48.1% | +4.363 to +4.918 | power given |
| pods started | 4.886 | 10.71 | +119.3% | +5.214 to +6.443 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.386e-16 to +1.833e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 184.2 | +0.1% | -0.4119 to +0.6958 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.2 | +0.1% | -0.4119 to +0.6958 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.377 | 2.425 | +2.0% | +0.03756 to +0.0595 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.95 | 71.93 | +2.8% | +1.667 to +2.289 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0.002857 | +0.00286 | -0.002949 to +0.008663 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2026 | 3124 | +54.2% | +502.3 to +1695 | LOSS |
| response time (ms), 99th percentile | 4201 | 5758 | +37.1% | +744.9 to +2371 | LOSS |
| time over the response line (% of samples) | 42.91 | 41.94 | -2.3% | -2.437 to +0.494 | STEADY, inside the noise (cut) |
| failed requests (%) | 24.25 | 26.21 | +8.1% | +0.8332 to +3.09 | LOSS |
| HPA replicas, mean | 9.674 | 13.18 | +36.3% | +3.022 to +3.993 | power given |
| pods started | 4.657 | 9.8 | +110.4% | +4.45 to +5.836 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.888e-16 to +1.813e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 184.2 | +0.1% | -0.1955 to +0.7217 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 184.2 | +0.1% | -0.1955 to +0.7217 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.361 | 2.413 | +2.2% | +0.04169 to +0.06141 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.46 | 71.67 | +3.2% | +1.878 to +2.537 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.02 | 0.01143 | -42.9% | -0.02599 to +0.008846 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3112 | 3352 | +7.7% | -513.7 to +994 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5710 | 6323 | +10.7% | -14.16 to +1240 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 43.7 | 41.53 | -5.0% | -3.309 to -1.039 | GAIN |
| failed requests (%) | 28.01 | 28.36 | +1.2% | -0.5446 to +1.233 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.659 | 14.35 | +48.6% | +4.43 to +4.951 | power given |
| pods started | 4.8 | 10.03 | +108.9% | +4.682 to +5.775 | power given |
| worker nodes in service, mean | 6 | 5.997 | -0.0% | -0.006597 to +0.001155 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184.4 | -0.0% | -0.5733 to +0.49 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184.4 | -0.1% | -0.6283 to +0.4355 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.394 | 2.446 | +2.2% | +0.04457 to +0.05955 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.02 | 73.01 | +2.8% | +1.797 to +2.18 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.002857 | 0.01714 | +500.0% | -0.0004825 to +0.02905 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2264 | 3116 | +37.6% | +285.8 to +1418 | LOSS |
| response time (ms), 99th percentile | 4509 | 5349 | +18.6% | +90.37 to +1589 | LOSS |
| time over the response line (% of samples) | 41.66 | 40.55 | -2.7% | -2.233 to +0.01289 | STEADY, inside the noise (cut) |
| failed requests (%) | 28.05 | 28.15 | +0.4% | -0.941 to +1.147 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.63 | 13.97 | +45.1% | +4.04 to +4.638 | power given |
| pods started | 4.857 | 10.66 | +119.4% | +5.114 to +6.486 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.674e-16 to +4.689e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.4 | 183.5 | +0.1% | -0.4175 to +0.6239 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.4 | 183.5 | +0.1% | -0.4175 to +0.6239 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.323 | 2.369 | +2.0% | +0.03897 to +0.05369 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.05 | 70.92 | +2.7% | +1.612 to +2.116 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.005714 | 0.01143 | +100.0% | -0.005897 to +0.01733 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2251 | 3075 | +36.6% | +161.5 to +1485 | LOSS |
| response time (ms), 99th percentile | 4838 | 5448 | +12.6% | -99.49 to +1320 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 45.13 | 42 | -6.9% | -4.665 to -1.601 | GAIN |
| failed requests (%) | 29.09 | 29.72 | +2.1% | -0.4834 to +1.732 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.659 | 12.76 | +32.1% | +2.484 to +3.709 | power given |
| pods started | 4.971 | 9.771 | +96.6% | +4.019 to +5.581 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.957e-16 to +3.419e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.6 | 183.7 | +0.1% | -0.3486 to +0.6151 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.6 | 183.7 | +0.1% | -0.3486 to +0.6151 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.34 | 2.376 | +1.5% | +0.02322 to +0.04813 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.86 | 70.74 | +2.7% | +1.51 to +2.249 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.01429 | 0.008571 | -40.0% | -0.02 to +0.008576 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2823 | 3718 | +31.7% | +80.92 to +1709 | LOSS |
| response time (ms), 99th percentile | 5229 | 6308 | +20.6% | +247.8 to +1910 | LOSS |
| time over the response line (% of samples) | 51.87 | 48.17 | -7.1% | -5.308 to -2.108 | GAIN |
| failed requests (%) | 33.55 | 33.08 | -1.4% | -1.869 to +0.9317 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.73 | 12.01 | +23.5% | +1.57 to +2.994 | power given |
| pods started | 4 | 8.943 | +123.6% | +4.18 to +5.706 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.56e-17 to +6.854e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.8 | 185.1 | +0.1% | -0.1439 to +0.6148 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.8 | 185.1 | +0.1% | -0.1439 to +0.6148 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.443 | 2.477 | +1.4% | +0.02665 to +0.04108 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.77 | 75.17 | +3.3% | +2.205 to +2.602 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.09714 | 0.2143 | +120.6% | +0.0995 to +0.1348 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1966 | 2939 | +49.5% | +451.2 to +1494 | LOSS |
| response time (ms), 99th percentile | 3870 | 4931 | +27.4% | +327.4 to +1796 | LOSS |
| time over the response line (% of samples) | 40.96 | 43.64 | +6.6% | +0.7519 to +4.616 | LOSS |
| failed requests (%) | 22.75 | 26.77 | +17.7% | +2.649 to +5.391 | LOSS |
| HPA replicas, mean | 9.73 | 12.08 | +24.1% | +1.56 to +3.138 | power given |
| pods started | 3.743 | 8.371 | +123.7% | +3.888 to +5.369 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.035e-16 to +3.513e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.6 | 183.9 | +0.2% | -0.1761 to +0.7841 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.6 | 183.9 | +0.2% | -0.1761 to +0.7841 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.318 | 2.367 | +2.1% | +0.03785 to +0.06004 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.56 | 73.68 | +5.9% | +3.797 to +4.432 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1629 | 0.1771 | +8.8% | -0.007978 to +0.03655 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
