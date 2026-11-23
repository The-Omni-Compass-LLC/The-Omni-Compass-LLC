# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 10 copies: native | The spine, the muscles every stack runs on, 10 copies: omni | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2370 | 3184 | 2919 | 3784 | 2435 | 3152 | 2387 | 2889 | 2363 | 3865 | 2614 | 2966 | 1958 | 3194 |
| response time (ms), 99th percentile | 4360 | 5709 | 5231 | 6591 | 4918 | 5730 | 4495 | 4913 | 5109 | 6108 | 5372 | 5578 | 3864 | 5151 |
| time over the response line (% of samples) | 37.04 | 35.96 | 49.08 | 46.26 | 34.1 | 32.33 | 35.31 | 33.89 | 44.88 | 42.14 | 41.56 | 38.13 | 38.41 | 41.74 |
| failed requests (%) | 22.82 | 22.6 | 25.77 | 26.55 | 21.38 | 20.1 | 22.51 | 23.08 | 26.14 | 26.94 | 23.27 | 22.54 | 21.18 | 25.09 |
| HPA replicas, mean | 9.608 | 14.26 | 9.714 | 13.04 | 9.596 | 14.66 | 9.6 | 14.27 | 9.681 | 13.21 | 9.64 | 12.7 | 9.698 | 12.49 |
| pods started | 5.2 | 11.49 | 4.286 | 9.829 | 5.457 | 11.43 | 5.286 | 11.14 | 4.714 | 10.51 | 5.143 | 10.29 | 4.343 | 8.971 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 5.996 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.3 | 183.3 | 185.1 | 185.5 | 183.5 | 183.4 | 183 | 182.8 | 184.3 | 184.8 | 184.3 | 184.1 | 183.5 | 183.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.3 | 183.3 | 185.1 | 185.5 | 183.5 | 183.4 | 183 | 182.8 | 184.3 | 184.7 | 184.3 | 184.1 | 183.5 | 183.7 |
| CPU used with Omni's own (cores), mean | 2.273 | 2.332 | 2.492 | 2.543 | 2.298 | 2.349 | 2.258 | 2.304 | 2.424 | 2.473 | 2.366 | 2.419 | 2.306 | 2.359 |
| host CPU busy, the real machine under kind (%) | 67.33 | 69.52 | 73.27 | 75.71 | 68.15 | 70.27 | 67.38 | 69.44 | 71.24 | 73.6 | 70.56 | 73.64 | 69.56 | 73.76 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.002857 | 0 | 0.02286 | 0.04 | 0.005714 | 0.008571 | 0.002857 | 0.008571 | 0.005714 | 0.01429 | 0.1 | 0.1171 | 0.1429 | 0.1857 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2370 | 3184 | +34.4% | +248.9 to +1380 | LOSS |
| response time (ms), 99th percentile | 4360 | 5709 | +30.9% | +593.7 to +2104 | LOSS |
| time over the response line (% of samples) | 37.04 | 35.96 | -2.9% | -2.212 to +0.05414 | STEADY, inside the noise (cut) |
| failed requests (%) | 22.82 | 22.6 | -1.0% | -1.148 to +0.7061 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.608 | 14.26 | +48.4% | +4.416 to +4.884 | power given |
| pods started | 5.2 | 11.49 | +120.9% | +5.676 to +6.895 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.051e-16 to +3.036e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.3 | 183.3 | +0.0% | -0.4785 to +0.4894 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.3 | 183.3 | +0.0% | -0.4785 to +0.4894 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.273 | 2.332 | +2.6% | +0.04794 to +0.06959 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.33 | 69.52 | +3.3% | +1.846 to +2.538 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0.002857 | 0 | -100.0% | -0.008663 to +0.002949 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2919 | 3784 | +29.6% | +330.9 to +1398 | LOSS |
| response time (ms), 99th percentile | 5231 | 6591 | +26.0% | +694.9 to +2025 | LOSS |
| time over the response line (% of samples) | 49.08 | 46.26 | -5.8% | -4.618 to -1.033 | GAIN |
| failed requests (%) | 25.77 | 26.55 | +3.0% | -0.0745 to +1.624 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.714 | 13.04 | +34.2% | +2.664 to +3.984 | power given |
| pods started | 4.286 | 9.829 | +129.3% | +4.829 to +6.256 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.026e-16 to +9.353e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.1 | 185.5 | +0.2% | -0.04647 to +0.8709 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.1 | 185.5 | +0.2% | -0.04647 to +0.8709 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.492 | 2.543 | +2.0% | +0.04218 to +0.05876 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.27 | 75.71 | +3.3% | +2.18 to +2.706 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.02286 | 0.04 | +75.0% | -0.004072 to +0.03836 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2435 | 3152 | +29.5% | +110.9 to +1324 | LOSS |
| response time (ms), 99th percentile | 4918 | 5730 | +16.5% | +176.5 to +1448 | LOSS |
| time over the response line (% of samples) | 34.1 | 32.33 | -5.2% | -2.746 to -0.7883 | GAIN |
| failed requests (%) | 21.38 | 20.1 | -6.0% | -2.314 to -0.2383 | GAIN |
| HPA replicas, mean | 9.596 | 14.66 | +52.8% | +4.922 to +5.203 | power given |
| pods started | 5.457 | 11.43 | +109.4% | +5.689 to +6.254 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.63e-16 to +2.047e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 183.4 | -0.1% | -0.6242 to +0.3483 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 183.4 | -0.1% | -0.6242 to +0.3483 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.298 | 2.349 | +2.2% | +0.03902 to +0.06289 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.15 | 70.27 | +3.1% | +1.753 to +2.488 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.005714 | 0.008571 | +50.0% | -0.01028 to +0.01599 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2387 | 2889 | +21.0% | -86.45 to +1091 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4495 | 4913 | +9.3% | -443.6 to +1280 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 35.31 | 33.89 | -4.0% | -2.51 to -0.3351 | GAIN |
| failed requests (%) | 22.51 | 23.08 | +2.5% | -0.4619 to +1.604 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.6 | 14.27 | +48.7% | +4.444 to +4.901 | power given |
| pods started | 5.286 | 11.14 | +110.8% | +5.164 to +6.55 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.488e-16 to +3.473e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183 | 182.8 | -0.1% | -0.6131 to +0.1738 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183 | 182.8 | -0.1% | -0.6131 to +0.1738 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.258 | 2.304 | +2.0% | +0.03022 to +0.0612 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.38 | 69.44 | +3.1% | +1.616 to +2.51 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.002857 | 0.008571 | +200.0% | -0.005897 to +0.01733 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2363 | 3865 | +63.6% | +717.8 to +2287 | LOSS |
| response time (ms), 99th percentile | 5109 | 6108 | +19.5% | +295.3 to +1702 | LOSS |
| time over the response line (% of samples) | 44.88 | 42.14 | -6.1% | -4.589 to -0.8989 | GAIN |
| failed requests (%) | 26.14 | 26.94 | +3.1% | -0.255 to +1.856 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.681 | 13.21 | +36.5% | +2.92 to +4.147 | power given |
| pods started | 4.714 | 10.51 | +123.0% | +5.114 to +6.486 | power given |
| worker nodes in service, mean | 6 | 5.996 | -0.1% | -0.01218 to +0.004147 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 184.8 | +0.2% | -0.006173 to +0.9009 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.3 | 184.7 | +0.2% | -0.1321 to +0.8649 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.424 | 2.473 | +2.0% | +0.04099 to +0.05749 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.24 | 73.6 | +3.3% | +2.18 to +2.537 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.005714 | 0.01429 | +150.0% | -0.004257 to +0.0214 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2614 | 2966 | +13.4% | -121.8 to +824.4 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5372 | 5578 | +3.8% | -449.8 to +861.9 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 41.56 | 38.13 | -8.3% | -4.583 to -2.286 | GAIN |
| failed requests (%) | 23.27 | 22.54 | -3.1% | -1.658 to +0.193 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.64 | 12.7 | +31.8% | +2.352 to +3.776 | power given |
| pods started | 5.143 | 10.29 | +100.0% | +4.416 to +5.87 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.513e-16 to +5.035e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 184.1 | -0.1% | -0.7212 to +0.2137 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.3 | 184.1 | -0.1% | -0.7212 to +0.2137 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.366 | 2.419 | +2.2% | +0.0415 to +0.06456 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.56 | 73.64 | +4.4% | +2.789 to +3.367 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.1 | 0.1171 | +17.1% | +0.004009 to +0.03028 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1958 | 3194 | +63.1% | +642.8 to +1829 | LOSS |
| response time (ms), 99th percentile | 3864 | 5151 | +33.3% | +682.3 to +1892 | LOSS |
| time over the response line (% of samples) | 38.41 | 41.74 | +8.7% | +1.156 to +5.49 | LOSS |
| failed requests (%) | 21.18 | 25.09 | +18.4% | +2.132 to +5.681 | LOSS |
| HPA replicas, mean | 9.698 | 12.49 | +28.8% | +2.014 to +3.568 | power given |
| pods started | 4.343 | 8.971 | +106.6% | +3.902 to +5.355 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.223e-16 to +1.655e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 183.7 | +0.1% | -0.2446 to +0.5598 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 183.7 | +0.1% | -0.2446 to +0.5598 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.306 | 2.359 | +2.3% | +0.04425 to +0.06202 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.56 | 73.76 | +6.0% | +3.893 to +4.489 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1429 | 0.1857 | +30.0% | +0.02197 to +0.06374 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
