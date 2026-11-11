# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 10 copies: native | The spine, the muscles every stack runs on, 10 copies: omni | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2670 | 3579 | 2011 | 2850 | 2736 | 3705 | 2435 | 3311 | 3002 | 3273 | 3219 | 3960 |
| response time (ms), 99th percentile | 4950 | 5848 | 3987 | 4832 | 5421 | 6446 | 4763 | 5685 | 5390 | 5598 | 5547 | 6403 |
| time over the response line (% of samples) | 38.59 | 37.55 | 37.99 | 37.52 | 42.72 | 40.67 | 36.01 | 32.33 | 44.48 | 41.98 | 40 | 41.1 |
| failed requests (%) | 24.66 | 23.47 | 20.77 | 22.76 | 28.6 | 28.06 | 17.85 | 18.1 | 26.13 | 27.62 | 17.46 | 22.21 |
| HPA replicas, mean | 9.6 | 14.43 | 9.641 | 13.06 | 9.639 | 14.28 | 9.633 | 13.7 | 9.677 | 12.71 | 9.694 | 13.07 |
| pods started | 5.415 | 11.24 | 5.103 | 10.25 | 5.025 | 11.03 | 5.171 | 11.41 | 4.61 | 9.195 | 4.39 | 10.34 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 183.8 | 183.1 | 183.6 | 184.5 | 184.2 | 183.3 | 183.9 | 184.5 | 184.4 | 184.4 | 184.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 183.8 | 183.1 | 183.6 | 184.5 | 184.2 | 183.3 | 183.9 | 184.5 | 184.4 | 184.4 | 184.6 |
| CPU used with Omni's own (cores), mean | 2.322 | 2.375 | 2.277 | 2.342 | 2.384 | 2.431 | 2.319 | 2.366 | 2.395 | 2.439 | 2.405 | 2.46 |
| host CPU busy, the real machine under kind (%) | 68.43 | 70.38 | 67.26 | 69.98 | 70.55 | 72.49 | 68.07 | 70.31 | 71.3 | 73.99 | 71.83 | 75.98 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0.002439 | 0.02308 | 0.0125 | 0.0075 | 0.0075 | 0.01707 | 0.0122 | 0.1 | 0.2195 | 0.1732 | 0.1902 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2670 | 3579 | +34.1% | +305.7 to +1514 | LOSS |
| response time (ms), 99th percentile | 4950 | 5848 | +18.1% | +208.6 to +1586 | LOSS |
| time over the response line (% of samples) | 38.59 | 37.55 | -2.7% | -2.035 to -0.03945 | GAIN |
| failed requests (%) | 24.66 | 23.47 | -4.8% | -2.407 to +0.02587 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.6 | 14.43 | +50.3% | +4.655 to +5.011 | power given |
| pods started | 5.415 | 11.24 | +107.7% | +5.243 to +6.415 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.513e-16 to +5.412e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 183.8 | +0.1% | -0.387 to +0.7128 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 183.8 | +0.1% | -0.387 to +0.7128 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.322 | 2.375 | +2.3% | +0.04168 to +0.06339 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.43 | 70.38 | +2.9% | +1.634 to +2.27 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0.002439 | +0.00244 | -0.00249 to +0.007368 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

39 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2011 | 2831 | +40.8% | +394.9 to +1245 | LOSS |
| response time (ms), 99th percentile | 3987 | 4837 | +21.3% | -4.023 to +1704 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 37.99 | 36.9 | -2.9% | -2.216 to +0.0403 | STEADY, inside the noise (cut) |
| failed requests (%) | 20.77 | 22.14 | +6.6% | +0.3495 to +2.401 | LOSS |
| HPA replicas, mean | 9.641 | 13.14 | +36.3% | +2.98 to +4.016 | power given |
| pods started | 5.103 | 10.36 | +103.0% | +4.64 to +5.873 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.076e-16 to +4.165e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.1 | 183.5 | +0.2% | -0.1531 to +0.8564 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.1 | 183.5 | +0.2% | -0.1531 to +0.8564 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.277 | 2.334 | +2.5% | +0.04771 to +0.06628 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.26 | 69.72 | +3.7% | +2.152 to +2.764 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.02308 | 0.01282 | -44.4% | -0.02816 to +0.007642 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2736 | 3705 | +35.4% | +304.7 to +1633 | LOSS |
| response time (ms), 99th percentile | 5421 | 6446 | +18.9% | +346.4 to +1704 | LOSS |
| time over the response line (% of samples) | 42.72 | 40.67 | -4.8% | -3.088 to -1.005 | GAIN |
| failed requests (%) | 28.6 | 28.06 | -1.9% | -1.631 to +0.5548 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.639 | 14.28 | +48.1% | +4.387 to +4.895 | power given |
| pods started | 5.025 | 11.03 | +119.4% | +5.473 to +6.527 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.765e-16 to +5.429e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.5 | 184.2 | -0.2% | -0.9135 to +0.1735 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.5 | 184.2 | -0.2% | -0.9135 to +0.1735 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.384 | 2.431 | +2.0% | +0.03839 to +0.05659 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.55 | 72.49 | +2.8% | +1.676 to +2.204 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.0075 | 0.0075 | +0.0% | -0.01255 to +0.01255 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2435 | 3311 | +36.0% | +275.8 to +1477 | LOSS |
| response time (ms), 99th percentile | 4763 | 5685 | +19.4% | +436.1 to +1408 | LOSS |
| time over the response line (% of samples) | 36.01 | 32.33 | -10.2% | -4.835 to -2.523 | GAIN |
| failed requests (%) | 17.85 | 18.1 | +1.4% | -0.5772 to +1.081 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.633 | 13.7 | +42.2% | +3.58 to +4.544 | power given |
| pods started | 5.171 | 11.41 | +120.8% | +5.689 to +6.799 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.99e-16 to -1.109e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.3 | 183.9 | +0.3% | +0.087 to +1.006 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.3 | 183.9 | +0.3% | +0.087 to +1.006 | power given |
| CPU used with Omni's own (cores), mean | 2.319 | 2.366 | +2.1% | +0.04016 to +0.05524 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.07 | 70.31 | +3.3% | +2.036 to +2.442 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.01707 | 0.0122 | -28.6% | -0.0221 to +0.01234 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3002 | 3273 | +9.0% | -309.3 to +850.6 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5390 | 5598 | +3.9% | -321.7 to +738.2 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 44.48 | 41.98 | -5.6% | -3.992 to -1.011 | GAIN |
| failed requests (%) | 26.13 | 27.62 | +5.7% | -0.09174 to +3.052 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.677 | 12.71 | +31.4% | +2.413 to +3.655 | power given |
| pods started | 4.61 | 9.195 | +99.5% | +3.79 to +5.381 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.832e-16 to +4.565e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.5 | 184.4 | -0.0% | -0.4507 to +0.2695 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.5 | 184.4 | -0.0% | -0.4507 to +0.2695 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.395 | 2.439 | +1.9% | +0.03171 to +0.05766 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.3 | 73.99 | +3.8% | +2.289 to +3.082 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.1 | 0.2195 | +119.5% | +0.1019 to +0.1371 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3219 | 3960 | +23.0% | +223.9 to +1258 | LOSS |
| response time (ms), 99th percentile | 5547 | 6403 | +15.4% | +401.8 to +1311 | LOSS |
| time over the response line (% of samples) | 40 | 41.1 | +2.7% | -0.955 to +3.148 | STEADY, inside the noise (up) |
| failed requests (%) | 17.46 | 22.21 | +27.2% | +3.11 to +6.376 | LOSS |
| HPA replicas, mean | 9.694 | 13.07 | +34.8% | +2.66 to +4.086 | power given |
| pods started | 4.39 | 10.34 | +135.6% | +5.195 to +6.708 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.948e-16 to +1.315e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184.6 | +0.1% | -0.1817 to +0.5978 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184.6 | +0.1% | -0.1817 to +0.5978 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.405 | 2.46 | +2.3% | +0.04562 to +0.06479 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.83 | 75.98 | +5.8% | +3.922 to +4.373 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1732 | 0.1902 | +9.9% | -0.01279 to +0.04693 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Energy / Facility / Industrial

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
