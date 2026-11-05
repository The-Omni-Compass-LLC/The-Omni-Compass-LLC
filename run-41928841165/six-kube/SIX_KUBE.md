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
| response time (ms), 95th percentile | 3064 | 4240 | 2020 | 2489 | 3436 | 3935 | 1542 | 2248 | 2882 | 3586 | 3405 | 3845 | 2536 | 4457 |
| response time (ms), 99th percentile | 5428 | 6422 | 3726 | 4807 | 6360 | 6895 | 3332 | 4334 | 5527 | 5707 | 5933 | 6064 | 5129 | 7152 |
| time over the response line (% of samples) | 46.56 | 45.58 | 38.8 | 35.94 | 44.25 | 41.18 | 33.38 | 31.61 | 46.25 | 44.47 | 43.84 | 40.56 | 55.46 | 57.96 |
| failed requests (%) | 30.12 | 29.81 | 20.66 | 22.32 | 26.88 | 27.5 | 22.35 | 21.93 | 28.39 | 30.66 | 23.44 | 23.56 | 30.86 | 34.82 |
| HPA replicas, mean | 9.618 | 14.43 | 9.65 | 13.12 | 9.651 | 14.23 | 9.575 | 13.98 | 9.662 | 12.7 | 9.685 | 12.89 | 9.786 | 12.27 |
| pods started | 5.35 | 11 | 4.95 | 10.65 | 5 | 10.85 | 5.55 | 11.45 | 4.9 | 10.6 | 4.55 | 9.9 | 3.15 | 7.5 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.7 | 184.8 | 182.9 | 183.3 | 184.8 | 184.8 | 182.5 | 182.4 | 183.6 | 184.8 | 184.6 | 184.5 | 185.9 | 185.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.7 | 184.8 | 182.9 | 183.3 | 184.8 | 184.8 | 182.5 | 182.4 | 183.6 | 184.8 | 184.6 | 184.5 | 185.9 | 185.8 |
| CPU used with Omni's own (cores), mean | 2.436 | 2.477 | 2.277 | 2.324 | 2.446 | 2.489 | 2.2 | 2.247 | 2.374 | 2.422 | 2.409 | 2.445 | 2.552 | 2.601 |
| host CPU busy, the real machine under kind (%) | 71.52 | 73.17 | 66.96 | 69.13 | 72.12 | 73.89 | 65.51 | 67.46 | 69.63 | 71.84 | 71.25 | 73.78 | 76.33 | 80.49 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0 | 0.005 | 0.01 | 0 | 0.015 | 0 | 0.015 | 0.005 | 0.005 | 0.1 | 0.205 | 0.195 | 0.2 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3064 | 4240 | +38.4% | +188.1 to +2164 | LOSS |
| response time (ms), 99th percentile | 5428 | 6422 | +18.3% | +144.5 to +1844 | LOSS |
| time over the response line (% of samples) | 46.56 | 45.58 | -2.1% | -2.505 to +0.5461 | STEADY, inside the noise (cut) |
| failed requests (%) | 30.12 | 29.81 | -1.0% | -1.809 to +1.188 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.618 | 14.43 | +50.1% | +4.527 to +5.105 | power given |
| pods started | 5.35 | 11 | +105.6% | +4.887 to +6.413 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.027e-15 to -3.923e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.7 | 184.8 | +0.1% | -0.6012 to +0.8422 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.7 | 184.8 | +0.1% | -0.6012 to +0.8422 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.436 | 2.477 | +1.7% | +0.02714 to +0.05498 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.52 | 73.17 | +2.3% | +1.264 to +2.041 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2020 | 2489 | +23.2% | +121.1 to +817.8 | LOSS |
| response time (ms), 99th percentile | 3726 | 4807 | +29.0% | +163.3 to +1998 | LOSS |
| time over the response line (% of samples) | 38.8 | 35.94 | -7.4% | -4.835 to -0.8798 | GAIN |
| failed requests (%) | 20.66 | 22.32 | +8.0% | -0.03812 to +3.353 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.65 | 13.12 | +36.0% | +2.601 to +4.338 | power given |
| pods started | 4.95 | 10.65 | +115.2% | +5.054 to +6.346 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.918e-16 to +5.03e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.9 | 183.3 | +0.3% | -0.1953 to +1.14 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.9 | 183.3 | +0.3% | -0.1953 to +1.14 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.277 | 2.324 | +2.1% | +0.03607 to +0.0581 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.96 | 69.13 | +3.3% | +1.856 to +2.499 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.005 | 0.01 | +100.0% | -0.01344 to +0.02344 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3436 | 3935 | +14.5% | -556.7 to +1556 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6360 | 6895 | +8.4% | -330.3 to +1400 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 44.25 | 41.18 | -6.9% | -4.357 to -1.775 | GAIN |
| failed requests (%) | 26.88 | 27.5 | +2.3% | -1.108 to +2.338 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.651 | 14.23 | +47.5% | +4.187 to +4.981 | power given |
| pods started | 5 | 10.85 | +117.0% | +5.183 to +6.517 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.005e-16 to +3.675e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.8 | 184.8 | -0.0% | -0.7056 to +0.6946 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.8 | 184.8 | -0.0% | -0.7056 to +0.6946 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.446 | 2.489 | +1.8% | +0.03045 to +0.05607 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.12 | 73.89 | +2.4% | +1.406 to +2.123 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0 | 0.015 | +0.015 | -0.002145 to +0.03215 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1542 | 2248 | +45.8% | -14.88 to +1428 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3332 | 4334 | +30.1% | -336.3 to +2340 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 33.38 | 31.61 | -5.3% | -2.796 to -0.7427 | GAIN |
| failed requests (%) | 22.35 | 21.93 | -1.9% | -1.729 to +0.8798 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.575 | 13.98 | +46.1% | +4.058 to +4.762 | power given |
| pods started | 5.55 | 11.45 | +106.3% | +4.621 to +7.179 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.859e-16 to +3.53e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.5 | 182.4 | -0.1% | -0.8751 to +0.6414 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.5 | 182.4 | -0.1% | -0.8751 to +0.6414 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.2 | 2.247 | +2.1% | +0.03425 to +0.05971 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.51 | 67.46 | +3.0% | +1.586 to +2.314 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0 | 0.015 | +0.015 | -0.002145 to +0.03215 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2882 | 3586 | +24.4% | -318.2 to +1727 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5527 | 5707 | +3.3% | -648.7 to +1009 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 46.25 | 44.47 | -3.8% | -3.572 to +0.01172 | STEADY, inside the noise (cut) |
| failed requests (%) | 28.39 | 30.66 | +8.0% | +0.2146 to +4.33 | LOSS |
| HPA replicas, mean | 9.662 | 12.7 | +31.5% | +2.205 to +3.873 | power given |
| pods started | 4.9 | 10.6 | +116.3% | +4.826 to +6.574 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.752e-16 to +5.975e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.6 | 184.8 | +0.6% | +0.5717 to +1.787 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.6 | 184.8 | +0.6% | +0.5717 to +1.787 | power given |
| CPU used with Omni's own (cores), mean | 2.374 | 2.422 | +2.0% | +0.03333 to +0.0622 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.63 | 71.84 | +3.2% | +1.713 to +2.701 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.005 | 0.005 | +0.0% | -0.01518 to +0.01518 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3405 | 3845 | +12.9% | -484.3 to +1363 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5933 | 6064 | +2.2% | -504.9 to +766.5 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 43.84 | 40.56 | -7.5% | -4.934 to -1.615 | GAIN |
| failed requests (%) | 23.44 | 23.56 | +0.5% | -1.445 to +1.683 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.685 | 12.89 | +33.1% | +2.434 to +3.976 | power given |
| pods started | 4.55 | 9.9 | +117.6% | +4.572 to +6.128 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.041e-15 to +4.188e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.6 | 184.5 | -0.1% | -0.7969 to +0.5796 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.6 | 184.5 | -0.1% | -0.7969 to +0.5796 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.409 | 2.445 | +1.5% | +0.02749 to +0.0462 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.25 | 73.78 | +3.5% | +2.253 to +2.801 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.1 | 0.205 | +105.0% | +0.08656 to +0.1234 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2536 | 4457 | +75.8% | +1347 to +2495 | LOSS |
| response time (ms), 99th percentile | 5129 | 7152 | +39.5% | +1018 to +3029 | LOSS |
| time over the response line (% of samples) | 55.46 | 57.96 | +4.5% | -0.1865 to +5.173 | STEADY, inside the noise (up) |
| failed requests (%) | 30.86 | 34.82 | +12.8% | +1.825 to +6.098 | LOSS |
| HPA replicas, mean | 9.786 | 12.27 | +25.4% | +1.446 to +3.529 | power given |
| pods started | 3.15 | 7.5 | +138.1% | +3.161 to +5.539 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.549e-16 to +2.332e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.9 | 185.8 | -0.0% | -0.6839 to +0.5586 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.9 | 185.8 | -0.0% | -0.6839 to +0.5586 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.552 | 2.601 | +1.9% | +0.04317 to +0.05439 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.33 | 80.49 | +5.5% | +4.035 to +4.294 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.195 | 0.2 | +2.6% | -0.04863 to +0.05863 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
