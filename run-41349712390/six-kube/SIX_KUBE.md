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
| response time (ms), 95th percentile | 3793 | 3239 | 2140 | 3125 | 2683 | 3214 | 2946 | 2835 | 1304 | 1528 | 2598 | 4364 | 2014 | 3530 |
| response time (ms), 99th percentile | 6582 | 5995 | 4500 | 5832 | 5427 | 5091 | 4758 | 5209 | 2547 | 2880 | 5483 | 6441 | 3870 | 5699 |
| time over the response line (% of samples) | 55.96 | 52.22 | 49.21 | 42.46 | 36.31 | 32.92 | 30.13 | 27.71 | 24.14 | 21.32 | 48.87 | 44.2 | 34.3 | 34.92 |
| failed requests (%) | 37.04 | 36.94 | 28.62 | 25 | 22.73 | 21.41 | 17.85 | 16.64 | 14.98 | 13.72 | 30.2 | 26.44 | 17.2 | 17.17 |
| HPA replicas, mean | 9.711 | 13.4 | 9.683 | 13.8 | 9.609 | 11.7 | 9.553 | 11.44 | 9.568 | 11.1 | 9.654 | 13.55 | 9.68 | 12.13 |
| pods started | 4.3 | 8 | 4.7 | 9 | 5.3 | 7.9 | 5.8 | 8.3 | 5.9 | 7.8 | 5 | 8.2 | 4.4 | 7.3 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 185.8 | 186.5 | 184.8 | 185.6 | 183.5 | 183.9 | 182.9 | 183.7 | 180.5 | 180.7 | 184.5 | 183.6 | 182.7 | 182.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.8 | 186.5 | 184.8 | 185.6 | 183.5 | 183.9 | 182.9 | 183.7 | 180.5 | 180.7 | 184.5 | 183.6 | 182.7 | 182.8 |
| CPU used with Omni's own (cores), mean | 2.567 | 2.586 | 2.465 | 2.482 | 2.307 | 2.313 | 2.238 | 2.232 | 2.026 | 2.011 | 2.388 | 2.396 | 2.235 | 2.259 |
| host CPU busy, the real machine under kind (%) | 75.68 | 76.68 | 72.78 | 74.19 | 68.1 | 68.76 | 65.8 | 66.05 | 59.81 | 59.84 | 71.09 | 72.59 | 67.02 | 70.07 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.01 | 0 | 0.02 | 0.02 | 0 | 0.03 | 0 | 0.01 | 0 | 0 | 0.1 | 0.21 | 0.13 | 0.15 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3793 | 3239 | -14.6% | -1999 to +891.4 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6582 | 5995 | -8.9% | -1690 to +517.2 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 55.96 | 52.22 | -6.7% | -7.333 to -0.144 | GAIN |
| failed requests (%) | 37.04 | 36.94 | -0.3% | -1.651 to +1.45 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.711 | 13.4 | +38.0% | +1.828 to +5.558 | power given |
| pods started | 4.3 | 8 | +86.0% | +1.791 to +5.609 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.318e-16 to +1.009e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.8 | 186.5 | +0.4% | -0.4572 to +1.895 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.8 | 186.5 | +0.4% | -0.4572 to +1.895 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.567 | 2.586 | +0.7% | +0.007897 to +0.03007 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.68 | 76.68 | +1.3% | +0.7321 to +1.271 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008375 to -0.0008374 | power given |
| organism behind its window (s) | 0.01 | 0 | -100.0% | -0.03262 to +0.01262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2140 | 3125 | +46.1% | -247.3 to +2218 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4500 | 5832 | +29.6% | +57.22 to +2607 | LOSS |
| time over the response line (% of samples) | 49.21 | 42.46 | -13.7% | -10.44 to -3.05 | GAIN |
| failed requests (%) | 28.62 | 25 | -12.7% | -5.439 to -1.805 | GAIN |
| HPA replicas, mean | 9.683 | 13.8 | +42.6% | +2.79 to +5.454 | power given |
| pods started | 4.7 | 9 | +91.5% | +2.949 to +5.651 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.697e-16 to +6.697e-16 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 184.8 | 185.6 | +0.4% | -0.2092 to +1.872 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.8 | 185.6 | +0.4% | -0.2092 to +1.872 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.465 | 2.482 | +0.7% | +0.008688 to +0.02579 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.78 | 74.19 | +1.9% | +1.197 to +1.637 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.02 | 0.02 | +0.0% | -0.04769 to +0.04769 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2683 | 3214 | +19.8% | -435.7 to +1497 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5427 | 5091 | -6.2% | -1328 to +656.5 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 36.31 | 32.92 | -9.3% | -6.248 to -0.5245 | GAIN |
| failed requests (%) | 22.73 | 21.41 | -5.8% | -2.428 to -0.2222 | GAIN |
| HPA replicas, mean | 9.609 | 11.7 | +21.7% | +0.1846 to +3.994 | power given |
| pods started | 5.3 | 7.9 | +49.1% | +0.2834 to +4.917 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.702e-16 to +1.003e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 183.9 | +0.2% | -0.422 to +1.291 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 183.9 | +0.2% | -0.422 to +1.291 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.307 | 2.313 | +0.3% | -0.01272 to +0.02578 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.1 | 68.76 | +1.0% | +0.1446 to +1.19 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0 | 0.03 | +0.03 | -0.004553 to +0.06455 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2946 | 2835 | -3.8% | -1300 to +1079 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4758 | 5209 | +9.5% | -430.8 to +1332 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 30.13 | 27.71 | -8.0% | -3.908 to -0.9368 | GAIN |
| failed requests (%) | 17.85 | 16.64 | -6.8% | -4.359 to +1.946 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.553 | 11.44 | +19.7% | +0.07353 to +3.695 | power given |
| pods started | 5.8 | 8.3 | +43.1% | +0.5266 to +4.473 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.449e-15 to +5.604e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.9 | 183.7 | +0.4% | +0.1422 to +1.386 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.9 | 183.7 | +0.4% | +0.1422 to +1.386 | power given |
| CPU used with Omni's own (cores), mean | 2.238 | 2.232 | -0.2% | -0.02868 to +0.01758 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.8 | 66.05 | +0.4% | -0.706 to +1.194 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0 | 0.01 | +0.01 | -0.01262 to +0.03262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 2 (organism energy (J); organism work per energy), STEADY (inside the noise) on 8

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1304 | 1528 | +17.2% | -756.1 to +1204 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 2547 | 2880 | +13.1% | -1093 to +1759 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 24.14 | 21.32 | -11.7% | -6.98 to +1.337 | STEADY, inside the noise (cut) |
| failed requests (%) | 14.98 | 13.72 | -8.4% | -3.133 to +0.6143 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.568 | 11.1 | +16.0% | -0.2361 to +3.307 | STEADY, inside the noise (up) |
| pods started | 5.9 | 7.8 | +32.2% | -0.5652 to +4.365 | STEADY, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.471e-16 to +8.471e-16 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 180.5 | 180.7 | +0.1% | -0.7886 to +1.207 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.5 | 180.7 | +0.1% | -0.7886 to +1.207 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.026 | 2.011 | -0.8% | -0.04981 to +0.01932 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.81 | 59.84 | +0.0% | -1.267 to +1.324 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2598 | 4364 | +68.0% | +137.4 to +3394 | LOSS |
| response time (ms), 99th percentile | 5483 | 6441 | +17.5% | -805.1 to +2721 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 48.87 | 44.2 | -9.6% | -7.969 to -1.373 | GAIN |
| failed requests (%) | 30.2 | 26.44 | -12.5% | -8.298 to +0.7722 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.654 | 13.55 | +40.3% | +2.414 to +5.371 | power given |
| pods started | 5 | 8.2 | +64.0% | +1.329 to +5.071 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.187e-15 to +1.01e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.5 | 183.6 | -0.5% | -1.727 to -0.1364 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.5 | 183.6 | -0.5% | -1.727 to -0.1364 | GAIN |
| CPU used with Omni's own (cores), mean | 2.388 | 2.396 | +0.3% | -0.03299 to +0.04839 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.09 | 72.59 | +2.1% | +0.329 to +2.666 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.1 | 0.21 | +110.0% | +0.0694 to +0.1506 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2014 | 3530 | +75.2% | +313.9 to +2717 | LOSS |
| response time (ms), 99th percentile | 3870 | 5699 | +47.2% | +108 to +3549 | LOSS |
| time over the response line (% of samples) | 34.3 | 34.92 | +1.8% | -3.045 to +4.28 | STEADY, inside the noise (up) |
| failed requests (%) | 17.2 | 17.17 | -0.2% | -1.087 to +1.026 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.68 | 12.13 | +25.3% | +0.8672 to +4.027 | power given |
| pods started | 4.4 | 7.3 | +65.9% | +0.9498 to +4.85 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.193e-15 to +3.046e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.7 | 182.8 | +0.1% | -0.4885 to +0.7293 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.7 | 182.8 | +0.1% | -0.4885 to +0.7293 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.235 | 2.259 | +1.1% | +0.008385 to +0.04015 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.02 | 70.07 | +4.6% | +2.503 to +3.601 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.13 | 0.15 | +15.4% | -0.01016 to +0.05016 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
