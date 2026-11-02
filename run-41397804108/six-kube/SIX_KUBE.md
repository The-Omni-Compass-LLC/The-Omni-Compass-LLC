# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1945 | 2181 | 2013 | 2128 | 3164 | 2483 | 2399 | 3339 | 3194 | 5227 | 2026 | 3705 |
| response time (ms), 99th percentile | 3934 | 4462 | 4847 | 4615 | 5594 | 5739 | 5150 | 5794 | 6347 | 8040 | 4007 | 6321 |
| time over the response line (% of samples) | 30.04 | 26.39 | 40.27 | 34.44 | 47.88 | 42.76 | 51.86 | 49.25 | 64.43 | 61.06 | 41.95 | 42.37 |
| failed requests (%) | 14.79 | 13.77 | 25.51 | 24.79 | 31.72 | 31.48 | 35.54 | 32.78 | 43.64 | 40.27 | 22.62 | 22.43 |
| HPA replicas, mean | 9.611 | 12.51 | 9.634 | 11.26 | 9.661 | 11.65 | 9.705 | 13.37 | 9.795 | 14.14 | 9.709 | 12.28 |
| pods started | 5.55 | 8.7 | 4.75 | 6.6 | 4.7 | 6.4 | 4.35 | 8.4 | 3.05 | 7.65 | 4.2 | 6.4 |
| worker nodes in service, mean | 5.997 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 182.3 | 182.5 | 182.8 | 183.7 | 184.5 | 185 | 184.7 | 185.2 | 185.7 | 186.7 | 183.9 | 184.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.2 | 182.5 | 182.8 | 183.7 | 184.5 | 185 | 184.7 | 185.2 | 185.7 | 186.7 | 183.9 | 184.4 |
| CPU used with Omni's own (cores), mean | 2.193 | 2.196 | 2.277 | 2.287 | 2.431 | 2.447 | 2.427 | 2.433 | 2.574 | 2.587 | 2.374 | 2.401 |
| host CPU busy, the real machine under kind (%) | 64.54 | 65.38 | 67.83 | 68.54 | 72.01 | 73.23 | 71.34 | 72.34 | 76.71 | 78.37 | 71.29 | 74.48 |
| organism work | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.01 | 0.01 | 0.005 | 0.015 | 0.01 | 0.01 | 0.01 | 0.01 | 0.105 | 0.23 | 0.155 | 0.18 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1945 | 2181 | +12.1% | -182.6 to +654.2 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3934 | 4462 | +13.4% | -483.8 to +1538 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 30.04 | 26.39 | -12.2% | -5.235 to -2.076 | GAIN |
| failed requests (%) | 14.79 | 13.77 | -6.9% | -2.082 to +0.05388 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.611 | 12.51 | +30.1% | +1.749 to +4.046 | power given |
| pods started | 5.55 | 8.7 | +56.8% | +1.815 to +4.485 | power given |
| worker nodes in service, mean | 5.997 | 6 | +0.0% | -0.003058 to +0.008654 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.3 | 182.5 | +0.2% | -0.4465 to +1.038 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.2 | 182.5 | +0.2% | -0.4407 to +1.145 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.193 | 2.196 | +0.2% | -0.007971 to +0.01463 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.54 | 65.38 | +1.3% | +0.4338 to +1.252 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.01 | 0.01 | +0.0% | -0.01518 to +0.01518 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2013 | 2128 | +5.7% | -580.2 to +810.7 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4847 | 4615 | -4.8% | -1277 to +813.1 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 40.27 | 34.44 | -14.5% | -8.554 to -3.1 | GAIN |
| failed requests (%) | 25.51 | 24.79 | -2.8% | -2.211 to +0.7667 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.634 | 11.26 | +16.9% | +0.5381 to +2.709 | power given |
| pods started | 4.75 | 6.6 | +38.9% | +0.5953 to +3.105 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.964e-16 to +8.74e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.8 | 183.7 | +0.5% | +0.4633 to +1.297 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.8 | 183.7 | +0.5% | +0.4633 to +1.297 | power given |
| CPU used with Omni's own (cores), mean | 2.277 | 2.287 | +0.4% | -0.002081 to +0.02103 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.83 | 68.54 | +1.0% | +0.2862 to +1.134 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.005 | 0.015 | +200.0% | -0.01093 to +0.03093 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3164 | 2483 | -21.5% | -1439 to +77.62 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5594 | 5739 | +2.6% | -893 to +1183 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 47.88 | 42.76 | -10.7% | -7.569 to -2.67 | GAIN |
| failed requests (%) | 31.72 | 31.48 | -0.8% | -1.683 to +1.206 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.661 | 11.65 | +20.6% | +0.7896 to +3.197 | power given |
| pods started | 4.7 | 6.4 | +36.2% | +0.2115 to +3.189 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.773e-16 to +4.108e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.5 | 185 | +0.2% | -0.2074 to +1.097 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.5 | 185 | +0.2% | -0.2074 to +1.097 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.431 | 2.447 | +0.7% | +0.003866 to +0.02974 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.01 | 73.23 | +1.7% | +0.8396 to +1.61 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.01 | 0.01 | +0.0% | -0.02147 to +0.02147 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2399 | 3339 | +39.2% | +65.18 to +1817 | LOSS |
| response time (ms), 99th percentile | 5150 | 5794 | +12.5% | -247.8 to +1536 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 51.86 | 49.25 | -5.0% | -4.6 to -0.6258 | GAIN |
| failed requests (%) | 35.54 | 32.78 | -7.8% | -4.683 to -0.8401 | GAIN |
| HPA replicas, mean | 9.705 | 13.37 | +37.7% | +2.535 to +4.789 | power given |
| pods started | 4.35 | 8.4 | +93.1% | +2.731 to +5.369 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.273e-16 to +6.938e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.7 | 185.2 | +0.3% | -0.09394 to +1.133 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.7 | 185.2 | +0.3% | -0.09394 to +1.133 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.427 | 2.433 | +0.2% | -0.004582 to +0.01525 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.34 | 72.34 | +1.4% | +0.6095 to +1.383 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.01 | 0.01 | +0.0% | -0.02147 to +0.02147 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 0

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3194 | 5227 | +63.7% | +1054 to +3012 | LOSS |
| response time (ms), 99th percentile | 6347 | 8040 | +26.7% | +851.3 to +2534 | LOSS |
| time over the response line (% of samples) | 64.43 | 61.06 | -5.2% | -5.093 to -1.65 | GAIN |
| failed requests (%) | 43.64 | 40.27 | -7.7% | -4.827 to -1.918 | GAIN |
| HPA replicas, mean | 9.795 | 14.14 | +44.3% | +3.73 to +4.95 | power given |
| pods started | 3.05 | 7.65 | +150.8% | +3.684 to +5.516 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.714e-16 to +2.497e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.7 | 186.7 | +0.5% | +0.235 to +1.627 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.7 | 186.7 | +0.5% | +0.235 to +1.627 | power given |
| CPU used with Omni's own (cores), mean | 2.574 | 2.587 | +0.5% | +0.005285 to +0.02068 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.71 | 78.37 | +2.2% | +1.557 to +1.757 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.105 | 0.23 | +119.0% | +0.09511 to +0.1549 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2026 | 3705 | +82.9% | +816 to +2542 | LOSS |
| response time (ms), 99th percentile | 4007 | 6321 | +57.8% | +1181 to +3448 | LOSS |
| time over the response line (% of samples) | 41.95 | 42.37 | +1.0% | -2.765 to +3.595 | STEADY, inside the noise (up) |
| failed requests (%) | 22.62 | 22.43 | -0.9% | -1.642 to +1.25 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.709 | 12.28 | +26.5% | +1.629 to +3.509 | power given |
| pods started | 4.2 | 6.4 | +52.4% | +1.068 to +3.332 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.948e-16 to +1.955e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.9 | 184.4 | +0.2% | -0.1852 to +1.054 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.9 | 184.4 | +0.2% | -0.1852 to +1.054 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.374 | 2.401 | +1.1% | +0.01182 to +0.04265 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.29 | 74.48 | +4.5% | +2.615 to +3.758 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.155 | 0.18 | +16.1% | +0.004208 to +0.04579 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The spine, the muscles every stack runs on

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
