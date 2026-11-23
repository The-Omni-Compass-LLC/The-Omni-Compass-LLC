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
| response time (ms), 95th percentile | 2574 | 3154 | 2155 | 3068 | 2685 | 3388 | 2394 | 3908 | 2427 | 4082 | 2859 | 2751 | 2518 | 3682 |
| response time (ms), 99th percentile | 5522 | 6071 | 4083 | 5568 | 5175 | 6300 | 4748 | 6369 | 5298 | 6465 | 5389 | 5260 | 4663 | 5567 |
| time over the response line (% of samples) | 34.48 | 32.65 | 36.65 | 35.49 | 46.13 | 44.9 | 45.37 | 44.5 | 46.1 | 43.15 | 39.87 | 36.77 | 38.15 | 39.31 |
| failed requests (%) | 19.79 | 18.99 | 18.64 | 19.61 | 30.6 | 30.74 | 28.97 | 29.21 | 27.28 | 28.1 | 23.81 | 22.83 | 17.3 | 21.21 |
| HPA replicas, mean | 9.592 | 14.46 | 9.634 | 13.61 | 9.669 | 14.27 | 9.676 | 14.45 | 9.656 | 13.08 | 9.668 | 12.77 | 9.681 | 13.31 |
| pods started | 5.536 | 11.68 | 5.257 | 10.74 | 4.543 | 10.23 | 4.429 | 10.4 | 4.971 | 10.77 | 4.781 | 10.44 | 4.657 | 9.543 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 183.5 | 182.9 | 183.6 | 184.4 | 184.6 | 184.4 | 184.4 | 184.3 | 185.2 | 183.7 | 183.6 | 184.1 | 184.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 183.5 | 182.9 | 183.6 | 184.4 | 184.6 | 184.4 | 184.4 | 184.3 | 185.2 | 183.7 | 183.6 | 184.1 | 184.1 |
| CPU used with Omni's own (cores), mean | 2.315 | 2.367 | 2.29 | 2.337 | 2.413 | 2.464 | 2.409 | 2.465 | 2.421 | 2.466 | 2.319 | 2.381 | 2.359 | 2.422 |
| host CPU busy, the real machine under kind (%) | 68.31 | 70.42 | 67.53 | 69.6 | 71.78 | 73.93 | 71.74 | 73.9 | 71.24 | 73.31 | 69.21 | 72.47 | 70.81 | 75.27 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.003571 | 0 | 0.005714 | 0.04 | 0.008571 | 0.02 | 0.01429 | 0.01429 | 0.002857 | 0.01429 | 0.09688 | 0.09688 | 0.14 | 0.1771 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

21 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2632 | 3383 | +28.6% | -205.2 to +1708 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5670 | 6370 | +12.3% | -230.3 to +1629 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 36.42 | 34.2 | -6.1% | -3.688 to -0.7432 | GAIN |
| failed requests (%) | 20.94 | 20.59 | -1.7% | -1.806 to +1.112 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.604 | 14.42 | +50.2% | +4.557 to +5.078 | power given |
| pods started | 5.476 | 11.33 | +107.0% | +5.052 to +6.662 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.728e-16 to +1.961e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.9 | 184 | +0.1% | -0.6609 to +0.9505 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.9 | 184 | +0.1% | -0.6609 to +0.9505 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.342 | 2.397 | +2.3% | +0.04406 to +0.06567 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.1 | 71.31 | +3.2% | +1.884 to +2.541 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0.004762 | 0 | -100.0% | -0.0147 to +0.005171 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2155 | 3068 | +42.4% | +362.2 to +1465 | LOSS |
| response time (ms), 99th percentile | 4083 | 5568 | +36.4% | +632.7 to +2337 | LOSS |
| time over the response line (% of samples) | 36.65 | 35.49 | -3.2% | -2.99 to +0.6626 | STEADY, inside the noise (cut) |
| failed requests (%) | 18.64 | 19.61 | +5.2% | -0.1064 to +2.052 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.634 | 13.61 | +41.3% | +3.46 to +4.491 | power given |
| pods started | 5.257 | 10.74 | +104.3% | +4.694 to +6.278 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.589e-16 to +4.988e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.9 | 183.6 | +0.4% | +0.3263 to +1.245 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.9 | 183.6 | +0.4% | +0.3263 to +1.245 | power given |
| CPU used with Omni's own (cores), mean | 2.29 | 2.337 | +2.1% | +0.03527 to +0.05866 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.53 | 69.6 | +3.1% | +1.725 to +2.416 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.005714 | 0.04 | +600.0% | +0.01577 to +0.05281 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2685 | 3388 | +26.2% | +128.7 to +1277 | LOSS |
| response time (ms), 99th percentile | 5175 | 6300 | +21.7% | +358.6 to +1892 | LOSS |
| time over the response line (% of samples) | 46.13 | 44.9 | -2.7% | -2.394 to -0.06838 | GAIN |
| failed requests (%) | 30.6 | 30.74 | +0.5% | -0.9559 to +1.237 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.669 | 14.27 | +47.6% | +4.329 to +4.873 | power given |
| pods started | 4.543 | 10.23 | +125.2% | +5.005 to +6.366 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.655e-16 to +6.223e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184.6 | +0.1% | -0.3695 to +0.6492 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184.6 | +0.1% | -0.3695 to +0.6492 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.413 | 2.464 | +2.1% | +0.03956 to +0.06315 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.78 | 73.93 | +3.0% | +1.75 to +2.545 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.008571 | 0.02 | +133.3% | -0.006768 to +0.02963 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2394 | 3908 | +63.3% | +961.5 to +2067 | LOSS |
| response time (ms), 99th percentile | 4748 | 6369 | +34.2% | +837.7 to +2405 | LOSS |
| time over the response line (% of samples) | 45.37 | 44.5 | -1.9% | -2.09 to +0.3532 | STEADY, inside the noise (cut) |
| failed requests (%) | 28.97 | 29.21 | +0.8% | -1.303 to +1.784 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.676 | 14.45 | +49.3% | +4.544 to +4.999 | power given |
| pods started | 4.429 | 10.4 | +134.8% | +5.543 to +6.4 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.36e-16 to +1.792e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184.4 | -0.0% | -0.6657 to +0.5233 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184.4 | -0.0% | -0.6657 to +0.5233 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.409 | 2.465 | +2.3% | +0.04283 to +0.06738 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.74 | 73.9 | +3.0% | +1.848 to +2.463 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.01429 | 0.01429 | +0.0% | -0.01443 to +0.01443 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2427 | 4082 | +68.2% | +931.8 to +2379 | LOSS |
| response time (ms), 99th percentile | 5298 | 6465 | +22.0% | +713.2 to +1619 | LOSS |
| time over the response line (% of samples) | 46.1 | 43.15 | -6.4% | -4.39 to -1.512 | GAIN |
| failed requests (%) | 27.28 | 28.1 | +3.0% | -0.2143 to +1.866 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.656 | 13.08 | +35.4% | +2.81 to +4.034 | power given |
| pods started | 4.971 | 10.77 | +116.7% | +5.061 to +6.539 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.184e-16 to +2.139e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 185.2 | +0.5% | +0.4821 to +1.46 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.3 | 185.2 | +0.5% | +0.4821 to +1.46 | power given |
| CPU used with Omni's own (cores), mean | 2.421 | 2.466 | +1.8% | +0.03233 to +0.0572 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.24 | 73.31 | +2.9% | +1.744 to +2.406 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.002857 | 0.01429 | +400.0% | -0.00244 to +0.0253 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

29 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2849 | 2907 | +2.0% | -456.9 to +573.1 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5298 | 5388 | +1.7% | -293.6 to +474.1 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 39.11 | 37.01 | -5.4% | -3.357 to -0.8343 | GAIN |
| failed requests (%) | 22.7 | 22.88 | +0.8% | -1.125 to +1.493 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.656 | 12.71 | +31.7% | +2.237 to +3.881 | power given |
| pods started | 4.966 | 10.41 | +109.7% | +4.825 to +6.071 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.612e-16 to +5.675e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 183.6 | -0.1% | -0.6338 to +0.3161 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 183.6 | -0.1% | -0.6338 to +0.3161 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.321 | 2.369 | +2.1% | +0.03421 to +0.06253 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.17 | 72.1 | +4.2% | +2.494 to +3.347 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.09655 | 0.09655 | +0.0% | -0.01016 to +0.01016 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2518 | 3682 | +46.2% | +637.7 to +1690 | LOSS |
| response time (ms), 99th percentile | 4663 | 5567 | +19.4% | +392.7 to +1416 | LOSS |
| time over the response line (% of samples) | 38.15 | 39.31 | +3.0% | -0.9288 to +3.244 | STEADY, inside the noise (up) |
| failed requests (%) | 17.3 | 21.21 | +22.6% | +2.397 to +5.41 | LOSS |
| HPA replicas, mean | 9.681 | 13.31 | +37.5% | +2.881 to +4.38 | power given |
| pods started | 4.657 | 9.543 | +104.9% | +4.316 to +5.455 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.263e-16 to +2.725e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 184.1 | +0.0% | -0.3562 to +0.372 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.1 | +0.0% | -0.3562 to +0.372 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.359 | 2.422 | +2.7% | +0.05371 to +0.07154 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.81 | 75.27 | +6.3% | +4.287 to +4.652 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.14 | 0.1771 | +26.5% | +0.008183 to +0.0661 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
