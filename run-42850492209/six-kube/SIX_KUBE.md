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
| response time (ms), 95th percentile | 3346 | 3866 | 2498 | 3045 | 3102 | 3329 | 2639 | 3833 | 3427 | 3837 | 2153 | 3348 |
| response time (ms), 99th percentile | 6081 | 6935 | 4580 | 5245 | 5471 | 5682 | 5705 | 6424 | 5854 | 6324 | 4325 | 5468 |
| time over the response line (% of samples) | 44.25 | 41.09 | 31.95 | 29.97 | 39.52 | 37.96 | 45.51 | 41.83 | 50.67 | 48.42 | 43.21 | 45.61 |
| failed requests (%) | 26.93 | 25.88 | 13.49 | 13.99 | 25.65 | 26.28 | 25.93 | 26.05 | 30.34 | 31.13 | 23.17 | 26.84 |
| HPA replicas, mean | 9.627 | 14.42 | 9.636 | 13.87 | 9.615 | 14.36 | 9.676 | 13.15 | 9.717 | 12.29 | 9.742 | 12.26 |
| pods started | 5.171 | 10.95 | 5.317 | 11.32 | 5.098 | 11.12 | 4.683 | 10.27 | 4.075 | 9.45 | 3.707 | 8.341 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.8 | 184.6 | 182.8 | 182.9 | 183.8 | 183.6 | 184.5 | 184.9 | 184.9 | 184.8 | 184.1 | 184.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.8 | 184.6 | 182.8 | 182.9 | 183.8 | 183.6 | 184.5 | 184.9 | 184.9 | 184.8 | 184.1 | 184.2 |
| CPU used with Omni's own (cores), mean | 2.439 | 2.483 | 2.252 | 2.295 | 2.33 | 2.377 | 2.43 | 2.48 | 2.448 | 2.491 | 2.381 | 2.428 |
| host CPU busy, the real machine under kind (%) | 71.73 | 73.47 | 66.16 | 68.24 | 69.14 | 71.07 | 71.34 | 73.68 | 72.98 | 75.61 | 71.61 | 75.75 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0.0025 | 0.007317 | 0.01707 | 0 | 0.004878 | 0.0122 | 0.002439 | 0.105 | 0.23 | 0.1732 | 0.178 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3375 | 3866 | +14.6% | -72.35 to +1056 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6131 | 6935 | +13.1% | +68.72 to +1540 | LOSS |
| time over the response line (% of samples) | 43.89 | 41.09 | -6.4% | -3.577 to -2.028 | GAIN |
| failed requests (%) | 26.59 | 25.88 | -2.7% | -2.078 to +0.6643 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.626 | 14.42 | +49.7% | +4.552 to +5.026 | power given |
| pods started | 5.175 | 10.95 | +111.6% | +5.356 to +6.194 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.398e-16 to -5.955e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.8 | 184.6 | -0.1% | -0.7858 to +0.3574 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.8 | 184.6 | -0.1% | -0.7858 to +0.3574 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.436 | 2.483 | +1.9% | +0.04117 to +0.05292 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.61 | 73.47 | +2.6% | +1.718 to +2 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0.0025 | +0.0025 | -0.002557 to +0.007557 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2498 | 3045 | +21.9% | +143.4 to +951.7 | LOSS |
| response time (ms), 99th percentile | 4580 | 5245 | +14.5% | +125.1 to +1205 | LOSS |
| time over the response line (% of samples) | 31.95 | 29.97 | -6.2% | -3.299 to -0.6555 | GAIN |
| failed requests (%) | 13.49 | 13.99 | +3.7% | -0.1524 to +1.149 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.636 | 13.87 | +43.9% | +3.776 to +4.687 | power given |
| pods started | 5.317 | 11.32 | +112.8% | +5.501 to +6.499 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.412e-16 to +1.513e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.8 | 182.9 | +0.0% | -0.4179 to +0.4778 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.8 | 182.9 | +0.0% | -0.4179 to +0.4778 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.252 | 2.295 | +1.9% | +0.02866 to +0.05658 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.16 | 68.24 | +3.2% | +1.661 to +2.513 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.007317 | 0.01707 | +133.3% | -0.004011 to +0.02352 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3102 | 3329 | +7.3% | -477.1 to +929.8 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5471 | 5682 | +3.9% | -395.7 to +817.7 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 39.52 | 37.96 | -3.9% | -2.525 to -0.5915 | GAIN |
| failed requests (%) | 25.65 | 26.28 | +2.5% | -0.5108 to +1.774 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.615 | 14.36 | +49.3% | +4.527 to +4.953 | power given |
| pods started | 5.098 | 11.12 | +118.2% | +5.499 to +6.55 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.284e-16 to +4.584e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 183.6 | -0.1% | -0.6246 to +0.2397 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 183.6 | -0.1% | -0.6246 to +0.2397 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.33 | 2.377 | +2.0% | +0.03744 to +0.05667 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.14 | 71.07 | +2.8% | +1.624 to +2.22 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0 | 0.004878 | +0.00488 | -0.002005 to +0.01176 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2639 | 3833 | +45.2% | +504.1 to +1883 | LOSS |
| response time (ms), 99th percentile | 5705 | 6424 | +12.6% | +80.62 to +1357 | LOSS |
| time over the response line (% of samples) | 45.51 | 41.83 | -8.1% | -5.022 to -2.345 | GAIN |
| failed requests (%) | 25.93 | 26.05 | +0.5% | -1.091 to +1.329 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.676 | 13.15 | +36.0% | +2.901 to +4.057 | power given |
| pods started | 4.683 | 10.27 | +119.3% | +4.923 to +6.247 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.672e-16 to +4.105e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.5 | 184.9 | +0.2% | -0.08449 to +0.8556 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.5 | 184.9 | +0.2% | -0.08449 to +0.8556 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.43 | 2.48 | +2.0% | +0.04103 to +0.05826 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.34 | 73.68 | +3.3% | +2.098 to +2.571 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.0122 | 0.002439 | -80.0% | -0.02158 to +0.002064 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3427 | 3837 | +11.9% | -126.5 to +945 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5854 | 6324 | +8.0% | -139.2 to +1081 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 50.67 | 48.42 | -4.4% | -3.732 to -0.7718 | GAIN |
| failed requests (%) | 30.34 | 31.13 | +2.6% | -0.6914 to +2.272 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.717 | 12.29 | +26.5% | +1.989 to +3.164 | power given |
| pods started | 4.075 | 9.45 | +131.9% | +4.875 to +5.875 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.406e-16 to -1.364e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.9 | 184.8 | -0.0% | -0.4812 to +0.3388 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.9 | 184.8 | -0.0% | -0.4812 to +0.3388 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.448 | 2.491 | +1.7% | +0.03222 to +0.05203 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.98 | 75.61 | +3.6% | +2.354 to +2.909 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.105 | 0.23 | +119.0% | +0.1036 to +0.1464 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2153 | 3348 | +55.5% | +670.2 to +1720 | LOSS |
| response time (ms), 99th percentile | 4325 | 5468 | +26.4% | +520.7 to +1765 | LOSS |
| time over the response line (% of samples) | 43.21 | 45.61 | +5.5% | +0.9312 to +3.86 | LOSS |
| failed requests (%) | 23.17 | 26.84 | +15.8% | +2.543 to +4.779 | LOSS |
| HPA replicas, mean | 9.742 | 12.26 | +25.9% | +1.803 to +3.243 | power given |
| pods started | 3.707 | 8.341 | +125.0% | +3.846 to +5.422 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.179e-16 to +2.279e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 184.2 | +0.0% | -0.4259 to +0.5089 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.2 | +0.0% | -0.4259 to +0.5089 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.381 | 2.428 | +2.0% | +0.03653 to +0.05726 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.61 | 75.75 | +5.8% | +3.813 to +4.476 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1732 | 0.178 | +2.8% | -0.01083 to +0.02058 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Energy / Facility / Industrial

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
