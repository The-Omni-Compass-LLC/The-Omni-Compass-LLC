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
| response time (ms), 95th percentile | 2206 | 3663 | 2768 | 4091 | 2041 | 2795 | 2999 | 4475 | 2732 | 3461 | 2005 | 2338 | 3135 | 5114 |
| response time (ms), 99th percentile | 5006 | 5975 | 5572 | 6640 | 4551 | 5483 | 5521 | 6987 | 4977 | 4950 | 4704 | 4351 | 5623 | 7485 |
| time over the response line (% of samples) | 49.56 | 47.61 | 49.36 | 44.82 | 42.88 | 42.04 | 50.64 | 49.95 | 43.91 | 43.04 | 51.39 | 50 | 45.63 | 46.69 |
| failed requests (%) | 33.84 | 33.06 | 25.72 | 26.27 | 28.66 | 29.77 | 34.07 | 35.06 | 27.87 | 27.2 | 36.55 | 37.98 | 21.51 | 24.97 |
| HPA replicas, mean | 9.681 | 14.17 | 9.706 | 12.97 | 9.7 | 13.97 | 9.69 | 13.92 | 9.657 | 12.93 | 9.73 | 11.37 | 9.728 | 12.9 |
| pods started | 4.5 | 9.9 | 4.4 | 9.3 | 4 | 9.3 | 4.5 | 9.5 | 4.9 | 10.9 | 3.8 | 8.6 | 4.2 | 9.9 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.9 | 184.8 | 185.3 | 185.9 | 183.7 | 184 | 185 | 185.1 | 183.2 | 183.1 | 183.9 | 184.2 | 185.1 | 185.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.9 | 184.8 | 185.3 | 185.9 | 183.7 | 184 | 185 | 185.1 | 183.2 | 183.1 | 183.9 | 184.2 | 185.1 | 185.8 |
| CPU used with Omni's own (cores), mean | 2.445 | 2.508 | 2.506 | 2.554 | 2.348 | 2.402 | 2.472 | 2.527 | 2.308 | 2.357 | 2.342 | 2.373 | 2.47 | 2.524 |
| host CPU busy, the real machine under kind (%) | 72.72 | 74.97 | 73.3 | 75.53 | 69.92 | 71.84 | 73.44 | 75.71 | 68.07 | 70.36 | 70.25 | 72.82 | 73.69 | 77.89 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.01 | 0 | 0.02 | 0.02 | 0.01 | 0.02 | 0.01 | 0.03 | 0 | 0 | 0.09 | 0.21 | 0.16 | 0.2 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2206 | 3663 | +66.0% | +398.7 to +2515 | LOSS |
| response time (ms), 99th percentile | 5006 | 5975 | +19.3% | -353.1 to +2290 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 49.56 | 47.61 | -3.9% | -4.887 to +0.9757 | STEADY, inside the noise (cut) |
| failed requests (%) | 33.84 | 33.06 | -2.3% | -3.575 to +2.015 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.681 | 14.17 | +46.4% | +3.797 to +5.187 | power given |
| pods started | 4.5 | 9.9 | +120.0% | +4.002 to +6.798 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.81e-17 to +1.617e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.9 | 184.8 | -0.0% | -1.235 to +1.068 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.9 | 184.8 | -0.0% | -1.235 to +1.068 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.445 | 2.508 | +2.6% | +0.04929 to +0.07656 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.72 | 74.97 | +3.1% | +1.893 to +2.594 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008375 to -0.0008374 | power given |
| organism behind its window (s) | 0.01 | 0 | -100.0% | -0.03262 to +0.01262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2768 | 4091 | +47.8% | +18.67 to +2627 | LOSS |
| response time (ms), 99th percentile | 5572 | 6640 | +19.2% | -875.6 to +3012 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 49.36 | 44.82 | -9.2% | -7.81 to -1.277 | GAIN |
| failed requests (%) | 25.72 | 26.27 | +2.2% | -0.962 to +2.068 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.706 | 12.97 | +33.6% | +1.838 to +4.689 | power given |
| pods started | 4.4 | 9.3 | +111.4% | +3.07 to +6.73 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.69e-16 to +2.585e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.3 | 185.9 | +0.3% | -0.4895 to +1.683 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.3 | 185.9 | +0.3% | -0.4895 to +1.683 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.506 | 2.554 | +1.9% | +0.03114 to +0.06405 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.3 | 75.53 | +3.0% | +1.917 to +2.532 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.02 | 0.02 | +0.0% | -0.03372 to +0.03372 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2041 | 2795 | +36.9% | -175.6 to +1682 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4551 | 5483 | +20.5% | -330.1 to +2195 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 42.88 | 42.04 | -2.0% | -2.813 to +1.118 | STEADY, inside the noise (cut) |
| failed requests (%) | 28.66 | 29.77 | +3.9% | -1.024 to +3.25 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.7 | 13.97 | +44.0% | +3.699 to +4.846 | power given |
| pods started | 4 | 9.3 | +132.5% | +4.405 to +6.195 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.779e-16 to +1.599e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 184 | +0.2% | -0.9219 to +1.638 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 184 | +0.2% | -0.9219 to +1.638 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.348 | 2.402 | +2.3% | +0.02596 to +0.08016 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.92 | 71.84 | +2.8% | +1.479 to +2.37 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.01 | 0.02 | +100.0% | -0.0306 to +0.0506 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2999 | 4475 | +49.2% | -426.3 to +3378 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5521 | 6987 | +26.6% | -1176 to +4108 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 50.64 | 49.95 | -1.4% | -3.774 to +2.392 | STEADY, inside the noise (cut) |
| failed requests (%) | 34.07 | 35.06 | +2.9% | -1.214 to +3.199 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.69 | 13.92 | +43.7% | +3.498 to +4.964 | power given |
| pods started | 4.5 | 9.5 | +111.1% | +3.694 to +6.306 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.187e-15 to +1.01e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185 | 185.1 | +0.0% | -1.125 to +1.296 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185 | 185.1 | +0.0% | -1.125 to +1.296 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.472 | 2.527 | +2.2% | +0.04288 to +0.06734 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.44 | 75.71 | +3.1% | +1.825 to +2.72 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.01 | 0.03 | +200.0% | -0.01016 to +0.05016 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2732 | 3461 | +26.7% | -928.7 to +2387 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4977 | 4950 | -0.5% | -1636 to +1582 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 43.91 | 43.04 | -2.0% | -3.908 to +2.16 | STEADY, inside the noise (cut) |
| failed requests (%) | 27.87 | 27.2 | -2.4% | -4.558 to +3.213 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.657 | 12.93 | +33.9% | +1.906 to +4.641 | power given |
| pods started | 4.9 | 10.9 | +122.4% | +4.418 to +7.582 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.066e-16 to +9.395e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.2 | 183.1 | -0.1% | -0.9146 to +0.7313 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.2 | 183.1 | -0.1% | -0.9146 to +0.7313 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.308 | 2.357 | +2.1% | +0.02991 to +0.06757 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.07 | 70.36 | +3.4% | +1.76 to +2.807 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 3 (pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2005 | 2338 | +16.6% | -486.1 to +1152 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4704 | 4351 | -7.5% | -1640 to +933.8 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 51.39 | 50 | -2.7% | -3.556 to +0.7738 | STEADY, inside the noise (cut) |
| failed requests (%) | 36.55 | 37.98 | +3.9% | -1.545 to +4.412 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.73 | 11.37 | +16.8% | -0.112 to +3.382 | STEADY, inside the noise (up) |
| pods started | 3.8 | 8.6 | +126.3% | +3.744 to +5.856 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +1.546e-16 to +1.622e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.9 | 184.2 | +0.2% | -0.5027 to +1.072 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.9 | 184.2 | +0.2% | -0.5027 to +1.072 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.342 | 2.373 | +1.3% | +0.008858 to +0.05414 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.25 | 72.82 | +3.7% | +1.87 to +3.276 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.09 | 0.21 | +133.3% | +0.08984 to +0.1502 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3135 | 5114 | +63.1% | +259.4 to +3697 | LOSS |
| response time (ms), 99th percentile | 5623 | 7485 | +33.1% | -440.7 to +4165 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 45.63 | 46.69 | +2.3% | -4.52 to +6.633 | STEADY, inside the noise (up) |
| failed requests (%) | 21.51 | 24.97 | +16.1% | -0.8493 to +7.78 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.728 | 12.9 | +32.7% | +1.475 to +4.877 | power given |
| pods started | 4.2 | 9.9 | +135.7% | +4.117 to +7.283 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.579e-15 to +5.132e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.1 | 185.8 | +0.3% | -0.3231 to +1.573 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.1 | 185.8 | +0.3% | -0.3231 to +1.573 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.47 | 2.524 | +2.2% | +0.0447 to +0.06328 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.69 | 77.89 | +5.7% | +4.011 to +4.383 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.16 | 0.2 | +25.0% | -0.01001 to +0.09001 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
