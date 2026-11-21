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
| response time (ms), 95th percentile | 3098 | 3703 | 2278 | 3048 | 3425 | 3571 | 2723 | 3642 | 2327 | 2583 | 2958 | 2631 | 1965 | 3300 |
| response time (ms), 99th percentile | 6185 | 6355 | 4298 | 5732 | 5855 | 5987 | 5213 | 5633 | 5124 | 5194 | 5161 | 5295 | 4197 | 5299 |
| time over the response line (% of samples) | 37.25 | 35.35 | 38.43 | 36.24 | 33.89 | 32.04 | 38.97 | 38.25 | 39.4 | 36.46 | 44.07 | 40.7 | 46.15 | 49.92 |
| failed requests (%) | 20.78 | 20.86 | 18.72 | 20.55 | 20.1 | 19.41 | 24.49 | 24.98 | 22.26 | 23.11 | 26.8 | 26.72 | 25.87 | 30.45 |
| HPA replicas, mean | 9.599 | 14.39 | 9.659 | 13.42 | 9.578 | 14.39 | 9.618 | 14.12 | 9.651 | 13.1 | 9.66 | 12.08 | 9.758 | 12.22 |
| pods started | 5.5 | 11.4 | 4.85 | 11.1 | 5.7 | 11.65 | 5.1 | 10.85 | 5 | 11.3 | 4.8 | 10.05 | 3.45 | 7.75 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 183.9 | 183.3 | 183.8 | 183.5 | 183.7 | 183.6 | 183.9 | 183.3 | 183.7 | 184.2 | 184 | 184.5 | 185 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 183.9 | 183.3 | 183.8 | 183.5 | 183.7 | 183.6 | 183.9 | 183.3 | 183.7 | 184.2 | 184 | 184.5 | 185 |
| CPU used with Omni's own (cores), mean | 2.352 | 2.402 | 2.313 | 2.373 | 2.298 | 2.337 | 2.314 | 2.367 | 2.323 | 2.367 | 2.365 | 2.399 | 2.43 | 2.489 |
| host CPU busy, the real machine under kind (%) | 69.07 | 71.26 | 68.14 | 70.62 | 67.67 | 69.3 | 68.47 | 70.56 | 68.24 | 70.3 | 70.38 | 72.86 | 73.17 | 77.71 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0 | 0 | 0.04 | 0.01 | 0.015 | 0.005 | 0.015 | 0.005 | 0.01 | 0.095 | 0.095 | 0.17 | 0.18 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3098 | 3703 | +19.5% | -441.2 to +1652 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6185 | 6355 | +2.7% | -721 to +1061 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 37.25 | 35.35 | -5.1% | -3.532 to -0.2798 | GAIN |
| failed requests (%) | 20.78 | 20.86 | +0.4% | -1.405 to +1.576 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.599 | 14.39 | +49.9% | +4.436 to +5.153 | power given |
| pods started | 5.5 | 11.4 | +107.3% | +5.003 to +6.797 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.339e-15 to +6.493e-18 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 183.9 | +0.1% | -0.6357 to +0.9074 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 183.9 | +0.1% | -0.6357 to +0.9074 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.352 | 2.402 | +2.1% | +0.03415 to +0.06608 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.07 | 71.26 | +3.2% | +1.871 to +2.511 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2278 | 3048 | +33.8% | +369.5 to +1170 | LOSS |
| response time (ms), 99th percentile | 4298 | 5732 | +33.3% | +549.1 to +2317 | LOSS |
| time over the response line (% of samples) | 38.43 | 36.24 | -5.7% | -4.286 to -0.1024 | GAIN |
| failed requests (%) | 18.72 | 20.55 | +9.8% | +0.6087 to +3.056 | LOSS |
| HPA replicas, mean | 9.659 | 13.42 | +38.9% | +3.073 to +4.447 | power given |
| pods started | 4.85 | 11.1 | +128.9% | +5.524 to +6.976 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.284e-15 to +4.034e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.3 | 183.8 | +0.3% | -0.2666 to +1.268 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.3 | 183.8 | +0.3% | -0.2666 to +1.268 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.313 | 2.373 | +2.6% | +0.04717 to +0.07294 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.14 | 70.62 | +3.6% | +2.096 to +2.87 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0 | 0.04 | +0.04 | +0.01648 to +0.06352 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3425 | 3571 | +4.3% | -607.8 to +899.9 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5855 | 5987 | +2.2% | -485.5 to +748.1 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 33.89 | 32.04 | -5.5% | -3.123 to -0.5892 | GAIN |
| failed requests (%) | 20.1 | 19.41 | -3.4% | -1.851 to +0.4694 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.578 | 14.39 | +50.3% | +4.498 to +5.131 | power given |
| pods started | 5.7 | 11.65 | +104.4% | +5.393 to +6.507 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.794e-16 to +1.8e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 183.7 | +0.1% | -0.5548 to +1.002 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 183.7 | +0.1% | -0.5548 to +1.002 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.298 | 2.337 | +1.7% | +0.03023 to +0.04827 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.67 | 69.3 | +2.4% | +1.287 to +1.97 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.01 | 0.015 | +50.0% | -0.01344 to +0.02344 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2723 | 3642 | +33.7% | +60.87 to +1777 | LOSS |
| response time (ms), 99th percentile | 5213 | 5633 | +8.1% | -505.1 to +1345 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 38.97 | 38.25 | -1.8% | -1.882 to +0.4538 | STEADY, inside the noise (cut) |
| failed requests (%) | 24.49 | 24.98 | +2.0% | -1.056 to +2.05 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.618 | 14.12 | +46.8% | +4.024 to +4.976 | power given |
| pods started | 5.1 | 10.85 | +112.7% | +4.978 to +6.522 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.332e-16 to +8.549e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.6 | 183.9 | +0.2% | -0.4222 to +1.097 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.6 | 183.9 | +0.2% | -0.4222 to +1.097 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.314 | 2.367 | +2.3% | +0.03432 to +0.07049 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.47 | 70.56 | +3.1% | +1.751 to +2.433 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.005 | 0.015 | +200.0% | -0.01093 to +0.03093 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2327 | 2583 | +11.0% | -410.2 to +921.8 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5124 | 5194 | +1.4% | -662.2 to +801.6 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 39.4 | 36.46 | -7.5% | -4.851 to -1.029 | GAIN |
| failed requests (%) | 22.26 | 23.11 | +3.8% | -0.3038 to +2.004 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.651 | 13.1 | +35.7% | +2.529 to +4.362 | power given |
| pods started | 5 | 11.3 | +126.0% | +5.327 to +7.273 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.38e-16 to +2.162e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.3 | 183.7 | +0.2% | -0.2232 to +1.052 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.3 | 183.7 | +0.2% | -0.2232 to +1.052 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.323 | 2.367 | +1.9% | +0.03647 to +0.05105 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.24 | 70.3 | +3.0% | +1.89 to +2.243 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.005 | 0.01 | +100.0% | -0.01344 to +0.02344 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2958 | 2631 | -11.1% | -919.2 to +265.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5161 | 5295 | +2.6% | -611.5 to +880 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 44.07 | 40.7 | -7.6% | -4.933 to -1.796 | GAIN |
| failed requests (%) | 26.8 | 26.72 | -0.3% | -1.689 to +1.529 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.66 | 12.08 | +25.0% | +1.406 to +3.429 | power given |
| pods started | 4.8 | 10.05 | +109.4% | +4.095 to +6.405 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.263e-16 to +6.486e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184 | -0.1% | -0.8699 to +0.4692 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184 | -0.1% | -0.8699 to +0.4692 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.365 | 2.399 | +1.5% | +0.02274 to +0.04585 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.38 | 72.86 | +3.5% | +2.114 to +2.843 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.095 | 0.095 | +0.0% | -0.02147 to +0.02147 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1965 | 3300 | +68.0% | +569.7 to +2100 | LOSS |
| response time (ms), 99th percentile | 4197 | 5299 | +26.2% | +22.42 to +2180 | LOSS |
| time over the response line (% of samples) | 46.15 | 49.92 | +8.2% | +1.372 to +6.171 | LOSS |
| failed requests (%) | 25.87 | 30.45 | +17.7% | +2.256 to +6.913 | LOSS |
| HPA replicas, mean | 9.758 | 12.22 | +25.2% | +1.371 to +3.55 | power given |
| pods started | 3.45 | 7.75 | +124.6% | +3.065 to +5.535 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.75e-16 to +8.687e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.5 | 185 | +0.3% | -0.01389 to +0.9759 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.5 | 185 | +0.3% | -0.01389 to +0.9759 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.43 | 2.489 | +2.4% | +0.04558 to +0.07296 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.17 | 77.71 | +6.2% | +4.149 to +4.914 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.17 | 0.18 | +5.9% | -0.01586 to +0.03586 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
