# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 10 copies: native | The spine, the muscles every stack runs on, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2781 | 3635 | 3103 | 3211 | 2448 | 2824 | 2695 | 4649 | 2959 | 2699 | 2372 | 3508 |
| response time (ms), 99th percentile | 5457 | 6495 | 5728 | 6012 | 4563 | 5226 | 5549 | 6888 | 5580 | 5664 | 4543 | 5312 |
| time over the response line (% of samples) | 41.4 | 40.14 | 40.5 | 38.76 | 36.61 | 35.52 | 49.97 | 48.14 | 47.02 | 44.29 | 36.88 | 38.53 |
| failed requests (%) | 26.29 | 25.89 | 26.11 | 25.93 | 23.27 | 23.47 | 30.52 | 30.92 | 28.64 | 30.24 | 17.77 | 21.44 |
| HPA replicas, mean | 9.632 | 14.39 | 9.614 | 14.26 | 9.622 | 14.11 | 9.686 | 13.18 | 9.691 | 12.01 | 9.686 | 13 |
| pods started | 5.098 | 10.85 | 5.439 | 11.29 | 4.976 | 11 | 4.659 | 10.51 | 4.317 | 8.976 | 4.463 | 9.61 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.5 | 184.6 | 184.2 | 184.2 | 183.4 | 183.4 | 184.7 | 185.5 | 184.4 | 184.4 | 183.5 | 183.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.5 | 184.6 | 184.2 | 184.2 | 183.4 | 183.4 | 184.7 | 185.5 | 184.4 | 184.4 | 183.5 | 183.9 |
| CPU used with Omni's own (cores), mean | 2.389 | 2.439 | 2.38 | 2.422 | 2.294 | 2.339 | 2.466 | 2.51 | 2.4 | 2.438 | 2.321 | 2.376 |
| host CPU busy, the real machine under kind (%) | 70.18 | 72.14 | 70.19 | 71.92 | 67.76 | 69.7 | 72.06 | 74.16 | 71.4 | 73.82 | 69.45 | 73.62 |
| organism work | 2.148e+11 | 2.148e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0 | 0.004878 | 0.002439 | 0.004878 | 0.009756 | 0.007317 | 0.007317 | 0.09756 | 0.2195 | 0.1488 | 0.1707 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2781 | 3635 | +30.7% | +206 to +1501 | LOSS |
| response time (ms), 99th percentile | 5457 | 6495 | +19.0% | +409.3 to +1666 | LOSS |
| time over the response line (% of samples) | 41.4 | 40.14 | -3.0% | -2.252 to -0.2667 | GAIN |
| failed requests (%) | 26.29 | 25.89 | -1.5% | -1.475 to +0.6683 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.632 | 14.39 | +49.3% | +4.509 to +4.997 | power given |
| pods started | 5.098 | 10.85 | +112.9% | +5.248 to +6.264 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.951e-16 to +3.518e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.5 | 184.6 | +0.1% | -0.3947 to +0.7091 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.5 | 184.6 | +0.1% | -0.3947 to +0.7091 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.389 | 2.439 | +2.1% | +0.04143 to +0.05863 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.18 | 72.14 | +2.8% | +1.698 to +2.213 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3103 | 3211 | +3.5% | -543.7 to +760.9 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5728 | 6012 | +5.0% | -325.9 to +894.2 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 40.5 | 38.76 | -4.3% | -2.566 to -0.9236 | GAIN |
| failed requests (%) | 26.11 | 25.93 | -0.7% | -1.169 to +0.8115 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.614 | 14.26 | +48.3% | +4.39 to +4.893 | power given |
| pods started | 5.439 | 11.29 | +107.6% | +5.415 to +6.292 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.426e-16 to +2.393e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.2 | -0.0% | -0.526 to +0.4592 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.2 | -0.0% | -0.526 to +0.4592 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.38 | 2.422 | +1.7% | +0.02971 to +0.05356 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.19 | 71.92 | +2.5% | +1.347 to +2.112 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.004878 | 0.002439 | -50.0% | -0.01105 to +0.00617 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2448 | 2824 | +15.4% | -131.3 to +883.9 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4563 | 5226 | +14.5% | +9.481 to +1315 | LOSS |
| time over the response line (% of samples) | 36.61 | 35.52 | -3.0% | -1.819 to -0.3502 | GAIN |
| failed requests (%) | 23.27 | 23.47 | +0.9% | -0.7885 to +1.196 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.622 | 14.11 | +46.6% | +4.214 to +4.76 | power given |
| pods started | 4.976 | 11 | +121.1% | +5.48 to +6.569 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.887e-16 to -9.445e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.4 | 183.4 | -0.0% | -0.5207 to +0.496 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.4 | 183.4 | -0.0% | -0.5207 to +0.496 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.294 | 2.339 | +2.0% | +0.03317 to +0.05783 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.76 | 69.7 | +2.9% | +1.582 to +2.307 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.004878 | 0.009756 | +100.0% | -0.007246 to +0.017 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2695 | 4649 | +72.5% | +1174 to +2735 | LOSS |
| response time (ms), 99th percentile | 5549 | 6888 | +24.1% | +636.2 to +2042 | LOSS |
| time over the response line (% of samples) | 49.97 | 48.14 | -3.6% | -3.276 to -0.3704 | GAIN |
| failed requests (%) | 30.52 | 30.92 | +1.3% | -1.133 to +1.936 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.686 | 13.18 | +36.1% | +3.004 to +3.982 | power given |
| pods started | 4.659 | 10.51 | +125.7% | +5.328 to +6.38 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.581e-16 to +8.149e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.7 | 185.5 | +0.5% | +0.4355 to +1.32 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.7 | 185.5 | +0.5% | +0.4355 to +1.32 | power given |
| CPU used with Omni's own (cores), mean | 2.466 | 2.51 | +1.8% | +0.0364 to +0.05127 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.06 | 74.16 | +2.9% | +1.898 to +2.311 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.007317 | 0.007317 | +0.0% | -0.009981 to +0.009981 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2959 | 2699 | -8.8% | -822.9 to +303.3 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5580 | 5664 | +1.5% | -516 to +684.4 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 47.02 | 44.29 | -5.8% | -4.058 to -1.398 | GAIN |
| failed requests (%) | 28.64 | 30.24 | +5.6% | +0.1741 to +3.033 | LOSS |
| HPA replicas, mean | 9.691 | 12.01 | +24.0% | +1.662 to +2.984 | power given |
| pods started | 4.317 | 8.976 | +107.9% | +4.045 to +5.272 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.246e-16 to +3.513e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184.4 | +0.0% | -0.3722 to +0.5051 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184.4 | +0.0% | -0.3722 to +0.5051 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.4 | 2.438 | +1.6% | +0.0253 to +0.05056 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.4 | 73.82 | +3.4% | +2.009 to +2.835 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.09756 | 0.2195 | +125.0% | +0.1054 to +0.1385 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 0

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2372 | 3508 | +47.9% | +599.1 to +1673 | LOSS |
| response time (ms), 99th percentile | 4543 | 5312 | +16.9% | +176.3 to +1362 | LOSS |
| time over the response line (% of samples) | 36.88 | 38.53 | +4.5% | +0.3047 to +2.992 | LOSS |
| failed requests (%) | 17.77 | 21.44 | +20.6% | +2.1 to +5.226 | LOSS |
| HPA replicas, mean | 9.686 | 13 | +34.2% | +2.602 to +4.022 | power given |
| pods started | 4.463 | 9.61 | +115.3% | +4.428 to +5.865 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.281e-16 to +4.715e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 183.9 | +0.2% | +0.04452 to +0.8475 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 183.9 | +0.2% | +0.04452 to +0.8475 | power given |
| CPU used with Omni's own (cores), mean | 2.321 | 2.376 | +2.3% | +0.04402 to +0.06434 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.45 | 73.62 | +6.0% | +3.81 to +4.537 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1488 | 0.1707 | +14.8% | +0.003941 to +0.03996 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
