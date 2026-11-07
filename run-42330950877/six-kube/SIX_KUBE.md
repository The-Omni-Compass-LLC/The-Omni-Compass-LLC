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
| response time (ms), 95th percentile | 2583 | 3618 | 1836 | 2574 | 3032 | 3057 | 2380 | 3448 | 2194 | 3244 | 2334 | 2195 | 2107 | 2749 |
| response time (ms), 99th percentile | 4906 | 5681 | 3948 | 4919 | 5319 | 5596 | 4735 | 5852 | 4548 | 5754 | 4667 | 4939 | 4082 | 4401 |
| time over the response line (% of samples) | 40.75 | 38.77 | 33.85 | 31.29 | 36.05 | 34.13 | 38.2 | 36.52 | 37.4 | 34.45 | 40.15 | 36.7 | 31.06 | 30.98 |
| failed requests (%) | 26.24 | 26.4 | 16.7 | 17.59 | 23.57 | 23.72 | 23.88 | 23.95 | 21.2 | 21.92 | 25.02 | 24.58 | 14.74 | 16.54 |
| HPA replicas, mean | 9.625 | 14.14 | 9.624 | 13.41 | 9.587 | 14.35 | 9.626 | 14.25 | 9.635 | 13.42 | 9.658 | 12.14 | 9.641 | 13.19 |
| pods started | 5.057 | 10.86 | 5.257 | 10.49 | 5.429 | 11.2 | 5 | 10.94 | 5.2 | 10.91 | 4.714 | 10.06 | 5.057 | 10.09 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 184.2 | 182.7 | 183.2 | 183.3 | 183.5 | 183.8 | 183.4 | 183.5 | 184 | 183.1 | 183.7 | 182.6 | 183 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 184.2 | 182.7 | 183.2 | 183.3 | 183.5 | 183.8 | 183.4 | 183.5 | 184 | 183.1 | 183.7 | 182.6 | 183 |
| CPU used with Omni's own (cores), mean | 2.329 | 2.374 | 2.244 | 2.286 | 2.293 | 2.337 | 2.323 | 2.37 | 2.305 | 2.348 | 2.284 | 2.328 | 2.233 | 2.292 |
| host CPU busy, the real machine under kind (%) | 68.49 | 70.3 | 65.81 | 67.9 | 67.57 | 69.26 | 68.84 | 70.82 | 67.54 | 69.59 | 68 | 70.56 | 66.71 | 70.93 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.005714 | 0 | 0.005714 | 0.01714 | 0.002857 | 0.008571 | 0.01714 | 0.01143 | 0.005714 | 0.01143 | 0.09143 | 0.22 | 0.1486 | 0.1686 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2583 | 3618 | +40.1% | +404.9 to +1665 | LOSS |
| response time (ms), 99th percentile | 4906 | 5681 | +15.8% | +105.3 to +1446 | LOSS |
| time over the response line (% of samples) | 40.75 | 38.77 | -4.9% | -3.207 to -0.7702 | GAIN |
| failed requests (%) | 26.24 | 26.4 | +0.6% | -0.8938 to +1.215 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.625 | 14.14 | +46.9% | +4.237 to +4.784 | power given |
| pods started | 5.057 | 10.86 | +114.7% | +5.23 to +6.37 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.516e-16 to +4.546e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 184.2 | +0.3% | +0.07248 to +1.178 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 184.2 | +0.3% | +0.07248 to +1.178 | power given |
| CPU used with Omni's own (cores), mean | 2.329 | 2.374 | +1.9% | +0.03088 to +0.05877 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.49 | 70.3 | +2.6% | +1.359 to +2.25 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0.005714 | 0 | -100.0% | -0.0138 to +0.002375 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1836 | 2574 | +40.2% | +273.3 to +1203 | LOSS |
| response time (ms), 99th percentile | 3948 | 4919 | +24.6% | +327.2 to +1616 | LOSS |
| time over the response line (% of samples) | 33.85 | 31.29 | -7.6% | -4.087 to -1.037 | GAIN |
| failed requests (%) | 16.7 | 17.59 | +5.4% | -0.04458 to +1.837 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.624 | 13.41 | +39.4% | +3.196 to +4.384 | power given |
| pods started | 5.257 | 10.49 | +99.5% | +4.657 to +5.8 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.815e-16 to +2.263e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.7 | 183.2 | +0.3% | -0.0423 to +0.9648 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.7 | 183.2 | +0.3% | -0.0423 to +0.9648 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.244 | 2.286 | +1.9% | +0.03284 to +0.0503 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.81 | 67.9 | +3.2% | +1.828 to +2.362 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.005714 | 0.01714 | +200.0% | -0.004749 to +0.02761 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3032 | 3057 | +0.8% | -838.5 to +888.1 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5319 | 5596 | +5.2% | -532 to +1086 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 36.05 | 34.13 | -5.3% | -2.727 to -1.117 | GAIN |
| failed requests (%) | 23.57 | 23.72 | +0.6% | -1.097 to +1.403 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.587 | 14.35 | +49.7% | +4.503 to +5.028 | power given |
| pods started | 5.429 | 11.2 | +106.3% | +5.12 to +6.423 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.073e-16 to +1.998e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.3 | 183.5 | +0.1% | -0.4028 to +0.6155 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.3 | 183.5 | +0.1% | -0.4028 to +0.6155 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.293 | 2.337 | +1.9% | +0.02799 to +0.05918 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.57 | 69.26 | +2.5% | +1.237 to +2.147 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.002857 | 0.008571 | +200.0% | -0.005897 to +0.01733 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2380 | 3448 | +44.9% | +310.4 to +1825 | LOSS |
| response time (ms), 99th percentile | 4735 | 5852 | +23.6% | +417.1 to +1817 | LOSS |
| time over the response line (% of samples) | 38.2 | 36.52 | -4.4% | -2.727 to -0.6389 | GAIN |
| failed requests (%) | 23.88 | 23.95 | +0.3% | -0.9977 to +1.141 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.626 | 14.25 | +48.0% | +4.322 to +4.927 | power given |
| pods started | 5 | 10.94 | +118.9% | +5.298 to +6.588 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.155e-16 to +2.095e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 183.4 | -0.2% | -0.7873 to +0.1481 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 183.4 | -0.2% | -0.7873 to +0.1481 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.323 | 2.37 | +2.0% | +0.03499 to +0.05899 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.84 | 70.82 | +2.9% | +1.569 to +2.385 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.01714 | 0.01143 | -33.3% | -0.02423 to +0.01281 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2194 | 3244 | +47.9% | +338.2 to +1762 | LOSS |
| response time (ms), 99th percentile | 4548 | 5754 | +26.5% | +499.6 to +1911 | LOSS |
| time over the response line (% of samples) | 37.4 | 34.45 | -7.9% | -4.462 to -1.44 | GAIN |
| failed requests (%) | 21.2 | 21.92 | +3.4% | -0.186 to +1.626 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.635 | 13.42 | +39.3% | +3.194 to +4.371 | power given |
| pods started | 5.2 | 10.91 | +109.9% | +5.035 to +6.394 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.651e-16 to +6.203e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 184 | +0.3% | +0.002782 to +1.039 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 184 | +0.3% | +0.002782 to +1.039 | power given |
| CPU used with Omni's own (cores), mean | 2.305 | 2.348 | +1.9% | +0.02818 to +0.05819 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.54 | 69.59 | +3.0% | +1.574 to +2.535 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.005714 | 0.01143 | +100.0% | -0.008576 to +0.02 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2334 | 2195 | -6.0% | -610.1 to +331.8 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4667 | 4939 | +5.8% | -345.3 to +889.9 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 40.15 | 36.7 | -8.6% | -5.001 to -1.903 | GAIN |
| failed requests (%) | 25.02 | 24.58 | -1.7% | -1.459 to +0.5842 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.658 | 12.14 | +25.7% | +1.762 to +3.198 | power given |
| pods started | 4.714 | 10.06 | +113.3% | +4.81 to +5.876 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.725e-16 to +5.263e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.1 | 183.7 | +0.3% | +0.1545 to +1.028 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.1 | 183.7 | +0.3% | +0.1545 to +1.028 | power given |
| CPU used with Omni's own (cores), mean | 2.284 | 2.328 | +1.9% | +0.03498 to +0.05392 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68 | 70.56 | +3.8% | +2.243 to +2.879 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.09143 | 0.22 | +140.6% | +0.1042 to +0.153 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2107 | 2749 | +30.5% | +59.83 to +1225 | LOSS |
| response time (ms), 99th percentile | 4082 | 4401 | +7.8% | -346.2 to +983.9 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 31.06 | 30.98 | -0.2% | -1.784 to +1.635 | STEADY, inside the noise (cut) |
| failed requests (%) | 14.74 | 16.54 | +12.2% | +0.3971 to +3.19 | LOSS |
| HPA replicas, mean | 9.641 | 13.19 | +36.9% | +2.828 to +4.278 | power given |
| pods started | 5.057 | 10.09 | +99.4% | +4.272 to +5.785 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.227e-16 to +1.137e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.6 | 183 | +0.2% | -0.07145 to +0.8147 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.6 | 183 | +0.2% | -0.07145 to +0.8147 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.233 | 2.292 | +2.6% | +0.04239 to +0.07557 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.71 | 70.93 | +6.3% | +3.713 to +4.726 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1486 | 0.1686 | +13.5% | -0.003266 to +0.04327 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
