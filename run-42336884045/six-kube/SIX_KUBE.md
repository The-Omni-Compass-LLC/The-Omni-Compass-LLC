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
| response time (ms), 95th percentile | 2929 | 3581 | 1860 | 2027 | 3035 | 3427 | 2600 | 3252 | 2561 | 3525 | 3194 | 3405 | 2555 | 3614 |
| response time (ms), 99th percentile | 5488 | 6160 | 3640 | 4055 | 5250 | 5788 | 4880 | 5750 | 5217 | 5873 | 5525 | 5719 | 5017 | 5808 |
| time over the response line (% of samples) | 37.65 | 35.34 | 28.75 | 25.2 | 34.24 | 32.97 | 39.3 | 38.53 | 41.21 | 38.53 | 45.58 | 42.48 | 41.22 | 42.48 |
| failed requests (%) | 22.36 | 22.29 | 12.88 | 13.51 | 21.65 | 20.32 | 25.43 | 25.89 | 23.8 | 23.88 | 26.99 | 27.16 | 19.78 | 23.85 |
| HPA replicas, mean | 9.601 | 14.28 | 9.592 | 13.89 | 9.567 | 14.35 | 9.624 | 14.23 | 9.628 | 13.38 | 9.686 | 12.26 | 9.689 | 12.39 |
| pods started | 5.286 | 11.4 | 5.676 | 10.88 | 5.686 | 11.71 | 5.029 | 11.26 | 5.314 | 11.14 | 4.457 | 9.914 | 4.457 | 9.171 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 184.1 | 182.1 | 182.3 | 183.2 | 183.1 | 183.6 | 183.8 | 183.8 | 184 | 184.4 | 184.6 | 183.9 | 184.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 184.1 | 182.1 | 182.3 | 183.2 | 183.1 | 183.6 | 183.8 | 183.8 | 184 | 184.4 | 184.6 | 183.9 | 184.5 |
| CPU used with Omni's own (cores), mean | 2.328 | 2.369 | 2.182 | 2.234 | 2.269 | 2.313 | 2.333 | 2.377 | 2.333 | 2.386 | 2.386 | 2.425 | 2.386 | 2.442 |
| host CPU busy, the real machine under kind (%) | 68.16 | 69.88 | 63.95 | 66.23 | 66.84 | 68.62 | 68.82 | 70.73 | 68.33 | 70.56 | 70.75 | 73.19 | 71.2 | 75.37 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0.002857 | 0.02059 | 0.005882 | 0.005714 | 0.005714 | 0.008571 | 0.02571 | 0.002857 | 0 | 0.09429 | 0.22 | 0.1429 | 0.1829 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2929 | 3581 | +22.3% | -46.99 to +1351 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5488 | 6160 | +12.3% | -133.2 to +1478 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 37.65 | 35.34 | -6.1% | -3.291 to -1.323 | GAIN |
| failed requests (%) | 22.36 | 22.29 | -0.3% | -1.281 to +1.139 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.601 | 14.28 | +48.7% | +4.402 to +4.957 | power given |
| pods started | 5.286 | 11.4 | +115.7% | +5.753 to +6.475 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.223e-16 to -2.451e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 184.1 | +0.1% | -0.3225 to +0.8707 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 184.1 | +0.1% | -0.3225 to +0.8707 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.328 | 2.369 | +1.7% | +0.03145 to +0.04911 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.16 | 69.88 | +2.5% | +1.494 to +1.959 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0.002857 | +0.00286 | -0.002949 to +0.008663 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

34 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1860 | 2027 | +8.9% | -134.5 to +467 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3640 | 4055 | +11.4% | -166 to +996.5 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 28.75 | 25.2 | -12.3% | -4.882 to -2.205 | GAIN |
| failed requests (%) | 12.88 | 13.51 | +4.9% | -0.2567 to +1.516 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.592 | 13.89 | +44.9% | +3.774 to +4.832 | power given |
| pods started | 5.676 | 10.88 | +91.7% | +4.707 to +5.705 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.848e-16 to +2.714e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.1 | 182.3 | +0.1% | -0.4551 to +0.6769 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.1 | 182.3 | +0.1% | -0.4551 to +0.6769 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.182 | 2.234 | +2.4% | +0.0381 to +0.06613 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.95 | 66.23 | +3.6% | +1.866 to +2.693 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.02059 | 0.005882 | -71.4% | -0.03217 to +0.00276 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3035 | 3427 | +12.9% | -480.1 to +1264 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5250 | 5788 | +10.2% | -96.6 to +1172 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 34.24 | 32.97 | -3.7% | -2.372 to -0.1826 | GAIN |
| failed requests (%) | 21.65 | 20.32 | -6.1% | -2.546 to -0.1151 | GAIN |
| HPA replicas, mean | 9.567 | 14.35 | +50.0% | +4.586 to +4.986 | power given |
| pods started | 5.686 | 11.71 | +106.0% | +5.414 to +6.643 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.717e-16 to +3.179e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.2 | 183.1 | -0.0% | -0.5705 to +0.4867 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.2 | 183.1 | -0.0% | -0.5705 to +0.4867 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.269 | 2.313 | +1.9% | +0.02963 to +0.05655 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.84 | 68.62 | +2.7% | +1.432 to +2.132 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.005714 | 0.005714 | +0.0% | -0.00833 to +0.00833 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2600 | 3252 | +25.1% | -54.27 to +1360 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4880 | 5750 | +17.8% | +103.9 to +1638 | LOSS |
| time over the response line (% of samples) | 39.3 | 38.53 | -1.9% | -1.921 to +0.3948 | STEADY, inside the noise (cut) |
| failed requests (%) | 25.43 | 25.89 | +1.8% | -0.7295 to +1.652 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.624 | 14.23 | +47.9% | +4.3 to +4.918 | power given |
| pods started | 5.029 | 11.26 | +123.9% | +5.605 to +6.852 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.839e-16 to +3.332e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.6 | 183.8 | +0.1% | -0.312 to +0.839 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.6 | 183.8 | +0.1% | -0.312 to +0.839 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.333 | 2.377 | +1.9% | +0.03224 to +0.05655 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.82 | 70.73 | +2.8% | +1.548 to +2.262 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.008571 | 0.02571 | +200.0% | +0.00159 to +0.0327 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2561 | 3525 | +37.6% | +374.4 to +1553 | LOSS |
| response time (ms), 99th percentile | 5217 | 5873 | +12.6% | +173.7 to +1138 | LOSS |
| time over the response line (% of samples) | 41.21 | 38.53 | -6.5% | -4.14 to -1.216 | GAIN |
| failed requests (%) | 23.8 | 23.88 | +0.3% | -1.334 to +1.491 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.628 | 13.38 | +38.9% | +3.27 to +4.225 | power given |
| pods started | 5.314 | 11.14 | +109.7% | +5.231 to +6.426 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.36e-16 to +1.792e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 184 | +0.1% | -0.2751 to +0.7754 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 184 | +0.1% | -0.2751 to +0.7754 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.333 | 2.386 | +2.2% | +0.04408 to +0.0607 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.33 | 70.56 | +3.3% | +1.959 to +2.508 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.002857 | 0 | -100.0% | -0.008663 to +0.002949 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3194 | 3405 | +6.6% | -464.5 to +886.5 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5525 | 5719 | +3.5% | -459 to +846.6 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 45.58 | 42.48 | -6.8% | -4.689 to -1.498 | GAIN |
| failed requests (%) | 26.99 | 27.16 | +0.6% | -1.109 to +1.45 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.686 | 12.26 | +26.6% | +1.898 to +3.248 | power given |
| pods started | 4.457 | 9.914 | +122.4% | +4.789 to +6.125 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.217e-16 to +1.634e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184.6 | +0.1% | -0.1763 to +0.6473 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184.6 | +0.1% | -0.1763 to +0.6473 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.386 | 2.425 | +1.6% | +0.03193 to +0.04611 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.75 | 73.19 | +3.4% | +2.267 to +2.606 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.09429 | 0.22 | +133.3% | +0.1017 to +0.1498 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2555 | 3614 | +41.4% | +613.1 to +1504 | LOSS |
| response time (ms), 99th percentile | 5017 | 5808 | +15.8% | +215.7 to +1367 | LOSS |
| time over the response line (% of samples) | 41.22 | 42.48 | +3.0% | -0.6884 to +3.202 | STEADY, inside the noise (up) |
| failed requests (%) | 19.78 | 23.85 | +20.6% | +2.311 to +5.829 | LOSS |
| HPA replicas, mean | 9.689 | 12.39 | +27.9% | +1.853 to +3.549 | power given |
| pods started | 4.457 | 9.171 | +105.8% | +3.913 to +5.516 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.402e-16 to +2.356e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.9 | 184.5 | +0.4% | +0.2212 to +1.086 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.9 | 184.5 | +0.4% | +0.2212 to +1.086 | power given |
| CPU used with Omni's own (cores), mean | 2.386 | 2.442 | +2.3% | +0.04231 to +0.06941 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.2 | 75.37 | +5.9% | +3.767 to +4.575 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1429 | 0.1829 | +28.0% | +0.01339 to +0.06661 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
