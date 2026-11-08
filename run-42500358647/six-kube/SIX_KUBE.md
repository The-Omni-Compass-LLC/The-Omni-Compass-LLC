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
| response time (ms), 95th percentile | 1911 | 2862 | 1555 | 2173 | 2720 | 3869 | 3144 | 3862 | 2608 | 3436 | 2707 | 3113 | 2056 | 3315 |
| response time (ms), 99th percentile | 3903 | 5086 | 3567 | 4480 | 5277 | 6445 | 5630 | 6526 | 5336 | 6256 | 4812 | 5093 | 4413 | 5451 |
| time over the response line (% of samples) | 37.5 | 35.99 | 30.35 | 28.46 | 41.41 | 39.9 | 45.98 | 43.61 | 41.23 | 36.78 | 41.51 | 40.52 | 43.67 | 45.94 |
| failed requests (%) | 24.48 | 23.95 | 16.08 | 16.87 | 26.97 | 26.16 | 29.2 | 28.69 | 22.19 | 22.74 | 25.75 | 24.73 | 23.85 | 27.36 |
| HPA replicas, mean | 9.597 | 14.23 | 9.639 | 13.8 | 9.65 | 14.33 | 9.65 | 14.48 | 9.628 | 13.38 | 9.686 | 12.48 | 9.736 | 12.06 |
| pods started | 5.2 | 10.57 | 5.257 | 11.11 | 4.743 | 10.86 | 5.029 | 11.03 | 5.371 | 11.09 | 4.486 | 10.06 | 3.857 | 8.743 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 182.8 | 183.7 | 182.6 | 183.1 | 183.9 | 184 | 184.7 | 184.5 | 183.9 | 184.4 | 183.5 | 183.3 | 184.2 | 185.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.8 | 183.7 | 182.6 | 183.1 | 183.9 | 184 | 184.7 | 184.5 | 183.9 | 184.4 | 183.5 | 183.3 | 184.2 | 185.1 |
| CPU used with Omni's own (cores), mean | 2.266 | 2.315 | 2.219 | 2.265 | 2.368 | 2.416 | 2.422 | 2.463 | 2.359 | 2.402 | 2.296 | 2.34 | 2.407 | 2.463 |
| host CPU busy, the real machine under kind (%) | 67 | 69.1 | 65.18 | 67.43 | 69.96 | 71.82 | 71.57 | 73.31 | 68.94 | 71.03 | 68.32 | 71.06 | 72.03 | 76.4 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.005714 | 0.008571 | 0.01714 | 0.01143 | 0 | 0.005714 | 0.002857 | 0.008571 | 0.008571 | 0.01429 | 0.1029 | 0.2314 | 0.1571 | 0.1829 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1911 | 2862 | +49.8% | +251.3 to +1651 | LOSS |
| response time (ms), 99th percentile | 3903 | 5086 | +30.3% | +368.7 to +1997 | LOSS |
| time over the response line (% of samples) | 37.5 | 35.99 | -4.0% | -2.682 to -0.3469 | GAIN |
| failed requests (%) | 24.48 | 23.95 | -2.2% | -1.465 to +0.4011 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.597 | 14.23 | +48.3% | +4.332 to +4.929 | power given |
| pods started | 5.2 | 10.57 | +103.3% | +4.8 to +5.943 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.094e-16 to +1.003e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.8 | 183.7 | +0.4% | +0.2112 to +1.43 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.8 | 183.7 | +0.4% | +0.2112 to +1.43 | power given |
| CPU used with Omni's own (cores), mean | 2.266 | 2.315 | +2.1% | +0.03945 to +0.05791 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67 | 69.1 | +3.1% | +1.85 to +2.363 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0.005714 | 0.008571 | +50.0% | -0.01028 to +0.01599 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1555 | 2173 | +39.8% | +122.1 to +1115 | LOSS |
| response time (ms), 99th percentile | 3567 | 4480 | +25.6% | +271.7 to +1555 | LOSS |
| time over the response line (% of samples) | 30.35 | 28.46 | -6.2% | -2.769 to -1.02 | GAIN |
| failed requests (%) | 16.08 | 16.87 | +4.9% | +0.02094 to +1.551 | LOSS |
| HPA replicas, mean | 9.639 | 13.8 | +43.2% | +3.7 to +4.627 | power given |
| pods started | 5.257 | 11.11 | +111.4% | +5.175 to +6.54 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.868e-16 to +2.822e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.6 | 183.1 | +0.3% | -0.04679 to +1.053 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.6 | 183.1 | +0.3% | -0.04679 to +1.053 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.219 | 2.265 | +2.1% | +0.03392 to +0.05817 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.18 | 67.43 | +3.4% | +1.88 to +2.61 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.01714 | 0.01143 | -33.3% | -0.02226 to +0.01083 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2720 | 3869 | +42.3% | +417.7 to +1882 | LOSS |
| response time (ms), 99th percentile | 5277 | 6445 | +22.1% | +444.1 to +1890 | LOSS |
| time over the response line (% of samples) | 41.41 | 39.9 | -3.6% | -2.718 to -0.2991 | GAIN |
| failed requests (%) | 26.97 | 26.16 | -3.0% | -1.78 to +0.1613 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.65 | 14.33 | +48.5% | +4.431 to +4.923 | power given |
| pods started | 4.743 | 10.86 | +128.9% | +5.569 to +6.659 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.279e-16 to +1.204e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.9 | 184 | +0.1% | -0.4271 to +0.6389 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.9 | 184 | +0.1% | -0.4271 to +0.6389 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.368 | 2.416 | +2.0% | +0.04085 to +0.0551 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.96 | 71.82 | +2.7% | +1.598 to +2.129 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0 | 0.005714 | +0.00571 | -0.002375 to +0.0138 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3144 | 3862 | +22.8% | +3.399 to +1432 | LOSS |
| response time (ms), 99th percentile | 5630 | 6526 | +15.9% | +139.1 to +1653 | LOSS |
| time over the response line (% of samples) | 45.98 | 43.61 | -5.2% | -3.579 to -1.17 | GAIN |
| failed requests (%) | 29.2 | 28.69 | -1.7% | -1.794 to +0.7774 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.65 | 14.48 | +50.1% | +4.609 to +5.054 | power given |
| pods started | 5.029 | 11.03 | +119.3% | +5.536 to +6.464 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.009e-16 to +1.441e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.7 | 184.5 | -0.1% | -0.6952 to +0.3444 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.7 | 184.5 | -0.1% | -0.6952 to +0.3444 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.422 | 2.463 | +1.7% | +0.03313 to +0.04949 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.57 | 73.31 | +2.4% | +1.477 to +2 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.002857 | 0.008571 | +200.0% | -0.005897 to +0.01733 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2608 | 3436 | +31.8% | +159.5 to +1497 | LOSS |
| response time (ms), 99th percentile | 5336 | 6256 | +17.2% | +334.8 to +1506 | LOSS |
| time over the response line (% of samples) | 41.23 | 36.78 | -10.8% | -5.793 to -3.112 | GAIN |
| failed requests (%) | 22.19 | 22.74 | +2.5% | -0.5799 to +1.676 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.628 | 13.38 | +39.0% | +3.214 to +4.287 | power given |
| pods started | 5.371 | 11.09 | +106.4% | +4.913 to +6.516 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.88e-16 to +7.742e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.9 | 184.4 | +0.3% | +0.04686 to +1.063 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.9 | 184.4 | +0.3% | +0.04686 to +1.063 | power given |
| CPU used with Omni's own (cores), mean | 2.359 | 2.402 | +1.8% | +0.03593 to +0.0496 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.94 | 71.03 | +3.0% | +1.876 to +2.3 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.008571 | 0.01429 | +66.7% | -0.01083 to +0.02226 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2707 | 3113 | +15.0% | -205 to +1015 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4812 | 5093 | +5.8% | -372.9 to +935.1 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 41.51 | 40.52 | -2.4% | -2.761 to +0.7801 | STEADY, inside the noise (cut) |
| failed requests (%) | 25.75 | 24.73 | -4.0% | -2.286 to +0.2452 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.686 | 12.48 | +28.9% | +2.104 to +3.494 | power given |
| pods started | 4.486 | 10.06 | +124.2% | +4.958 to +6.185 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.739e-16 to +3.709e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 183.3 | -0.1% | -0.5819 to +0.277 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 183.3 | -0.1% | -0.5819 to +0.277 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.296 | 2.34 | +2.0% | +0.03086 to +0.05869 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.32 | 71.06 | +4.0% | +2.263 to +3.222 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.1029 | 0.2314 | +125.0% | +0.1072 to +0.1499 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 0

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2056 | 3315 | +61.2% | +653.2 to +1865 | LOSS |
| response time (ms), 99th percentile | 4413 | 5451 | +23.5% | +416.2 to +1660 | LOSS |
| time over the response line (% of samples) | 43.67 | 45.94 | +5.2% | +0.5406 to +4 | LOSS |
| failed requests (%) | 23.85 | 27.36 | +14.7% | +1.45 to +5.58 | LOSS |
| HPA replicas, mean | 9.736 | 12.06 | +23.8% | +1.495 to +3.148 | power given |
| pods started | 3.857 | 8.743 | +126.7% | +4.151 to +5.62 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.716e-17 to +8.385e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 185.1 | +0.5% | +0.3932 to +1.305 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 185.1 | +0.5% | +0.3932 to +1.305 | power given |
| CPU used with Omni's own (cores), mean | 2.407 | 2.463 | +2.3% | +0.04616 to +0.06588 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.03 | 76.4 | +6.1% | +4.122 to +4.622 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1571 | 0.1829 | +16.4% | +0.001653 to +0.04978 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
