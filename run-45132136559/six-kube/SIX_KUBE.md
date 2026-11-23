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
| response time (ms), 95th percentile | 3633 | 4252 | 2016 | 2726 | 2860 | 3811 | 2499 | 3236 | 2511 | 3555 | 2835 | 3237 | 2742 | 3748 |
| response time (ms), 99th percentile | 6840 | 7411 | 4050 | 4894 | 5643 | 6460 | 4912 | 5874 | 5446 | 5770 | 5423 | 5915 | 5098 | 6022 |
| time over the response line (% of samples) | 50.55 | 48.68 | 38.33 | 35.61 | 44.05 | 43.44 | 44.12 | 43.7 | 47.75 | 45.33 | 49.17 | 46.44 | 43.73 | 45.9 |
| failed requests (%) | 32.04 | 31.69 | 19.8 | 20.66 | 29.14 | 29.19 | 28.73 | 30.33 | 29.23 | 29.73 | 31.18 | 31.63 | 21.19 | 25 |
| HPA replicas, mean | 9.665 | 14.55 | 9.65 | 13.47 | 9.694 | 14.4 | 9.658 | 14.28 | 9.664 | 12.6 | 9.713 | 12.23 | 9.715 | 12.65 |
| pods started | 4.971 | 10.77 | 5.057 | 10.86 | 4.257 | 10.4 | 4.743 | 10.66 | 4.886 | 10.31 | 4.229 | 9.171 | 4.171 | 9.229 |
| worker nodes in service, mean | 6 | 5.998 | 6 | 6 | 6 | 6 | 6 | 5.999 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 185.8 | 185.8 | 183.2 | 183.7 | 184.6 | 184.7 | 184.2 | 184.3 | 184.3 | 184.5 | 184.7 | 184.8 | 184.9 | 184.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.8 | 185.8 | 183.2 | 183.7 | 184.6 | 184.7 | 184.2 | 184.3 | 184.3 | 184.5 | 184.7 | 184.8 | 184.9 | 184.8 |
| CPU used with Omni's own (cores), mean | 2.542 | 2.59 | 2.302 | 2.358 | 2.417 | 2.465 | 2.394 | 2.44 | 2.409 | 2.454 | 2.416 | 2.46 | 2.439 | 2.491 |
| host CPU busy, the real machine under kind (%) | 74.85 | 76.87 | 68.01 | 70.4 | 71.93 | 73.97 | 71.44 | 73.53 | 71.09 | 73.44 | 72.32 | 75.11 | 73.19 | 77.36 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.008571 | 0.008571 | 0.008571 | 0.04571 | 0.008571 | 0.005714 | 0.002857 | 0.008571 | 0.005714 | 0.01429 | 0.09714 | 0.1171 | 0.1486 | 0.2 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3633 | 4252 | +17.0% | -138.8 to +1376 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6840 | 7411 | +8.4% | -72.56 to +1215 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 50.55 | 48.68 | -3.7% | -3.121 to -0.6239 | GAIN |
| failed requests (%) | 32.04 | 31.69 | -1.1% | -1.627 to +0.9349 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.665 | 14.55 | +50.6% | +4.644 to +5.131 | power given |
| pods started | 4.971 | 10.77 | +116.7% | +5.459 to +6.141 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.005353 to +0.001822 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.8 | 185.8 | +0.0% | -0.5222 to +0.6392 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.8 | 185.8 | +0.0% | -0.5722 to +0.6177 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.542 | 2.59 | +1.9% | +0.04104 to +0.05575 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.85 | 76.87 | +2.7% | +1.9 to +2.15 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.874e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008375 to -0.0008373 | power given |
| organism behind its window (s) | 0.008571 | 0.008571 | +0.0% | -0.01178 to +0.01178 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2016 | 2726 | +35.2% | +210.3 to +1210 | LOSS |
| response time (ms), 99th percentile | 4050 | 4894 | +20.8% | +72.42 to +1615 | LOSS |
| time over the response line (% of samples) | 38.33 | 35.61 | -7.1% | -4.473 to -0.9729 | GAIN |
| failed requests (%) | 19.8 | 20.66 | +4.3% | -0.4977 to +2.218 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.65 | 13.47 | +39.6% | +3.237 to +4.402 | power given |
| pods started | 5.057 | 10.86 | +114.7% | +5.261 to +6.339 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.717e-16 to +1.165e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.2 | 183.7 | +0.3% | +0.08806 to +1.007 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.2 | 183.7 | +0.3% | +0.08806 to +1.007 | power given |
| CPU used with Omni's own (cores), mean | 2.302 | 2.358 | +2.4% | +0.04748 to +0.06425 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.01 | 70.4 | +3.5% | +2.167 to +2.625 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.008571 | 0.04571 | +433.3% | +0.0203 to +0.05398 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2860 | 3811 | +33.3% | +423 to +1480 | LOSS |
| response time (ms), 99th percentile | 5643 | 6460 | +14.5% | +277.3 to +1357 | LOSS |
| time over the response line (% of samples) | 44.05 | 43.44 | -1.4% | -1.91 to +0.6876 | STEADY, inside the noise (cut) |
| failed requests (%) | 29.14 | 29.19 | +0.2% | -1.232 to +1.331 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.694 | 14.4 | +48.6% | +4.486 to +4.93 | power given |
| pods started | 4.257 | 10.4 | +144.3% | +5.734 to +6.552 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.161e-16 to +6.221e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.6 | 184.7 | +0.0% | -0.4954 to +0.6687 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.6 | 184.7 | +0.0% | -0.4954 to +0.6687 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.417 | 2.465 | +2.0% | +0.03736 to +0.05962 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.93 | 73.97 | +2.8% | +1.764 to +2.302 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.008571 | 0.005714 | -33.3% | -0.01301 to +0.007297 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2499 | 3236 | +29.5% | +19.94 to +1453 | LOSS |
| response time (ms), 99th percentile | 4912 | 5874 | +19.6% | +198 to +1727 | LOSS |
| time over the response line (% of samples) | 44.12 | 43.7 | -0.9% | -1.636 to +0.7988 | STEADY, inside the noise (cut) |
| failed requests (%) | 28.73 | 30.33 | +5.6% | +0.4531 to +2.749 | LOSS |
| HPA replicas, mean | 9.658 | 14.28 | +47.8% | +4.336 to +4.902 | power given |
| pods started | 4.743 | 10.66 | +124.7% | +5.359 to +6.469 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.00303 to +0.001031 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.3 | +0.1% | -0.3868 to +0.5746 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.3 | +0.0% | -0.4023 to +0.5496 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.394 | 2.44 | +1.9% | +0.03786 to +0.05321 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.44 | 73.53 | +2.9% | +1.879 to +2.308 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.002857 | 0.008571 | +200.0% | -0.008576 to +0.02 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2511 | 3555 | +41.6% | +302.5 to +1786 | LOSS |
| response time (ms), 99th percentile | 5446 | 5770 | +5.9% | -399.1 to +1047 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 47.75 | 45.33 | -5.1% | -3.721 to -1.128 | GAIN |
| failed requests (%) | 29.23 | 29.73 | +1.7% | -0.6832 to +1.683 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.664 | 12.6 | +30.4% | +2.223 to +3.645 | power given |
| pods started | 4.886 | 10.31 | +111.1% | +4.725 to +6.132 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.099e-16 to +1.501e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 184.5 | +0.1% | -0.3284 to +0.5657 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.3 | 184.5 | +0.1% | -0.3284 to +0.5657 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.409 | 2.454 | +1.9% | +0.03847 to +0.05233 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.09 | 73.44 | +3.3% | +2.176 to +2.522 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.005714 | 0.01429 | +150.0% | -0.006724 to +0.02387 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2835 | 3237 | +14.2% | -393.7 to +1199 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5423 | 5915 | +9.1% | -219.3 to +1202 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 49.17 | 46.44 | -5.6% | -4.36 to -1.115 | GAIN |
| failed requests (%) | 31.18 | 31.63 | +1.5% | -1.022 to +1.93 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.713 | 12.23 | +25.9% | +1.782 to +3.255 | power given |
| pods started | 4.229 | 9.171 | +116.9% | +4.207 to +5.678 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.868e-16 to +2.822e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.7 | 184.8 | +0.0% | -0.3439 to +0.4823 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.7 | 184.8 | +0.0% | -0.3439 to +0.4823 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.416 | 2.46 | +1.8% | +0.0355 to +0.05287 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.32 | 75.11 | +3.9% | +2.548 to +3.045 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.09714 | 0.1171 | +20.6% | +0.003761 to +0.03624 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2742 | 3748 | +36.7% | +418.6 to +1594 | LOSS |
| response time (ms), 99th percentile | 5098 | 6022 | +18.1% | +94.15 to +1755 | LOSS |
| time over the response line (% of samples) | 43.73 | 45.9 | +5.0% | +0.1745 to +4.177 | LOSS |
| failed requests (%) | 21.19 | 25 | +17.9% | +2.361 to +5.244 | LOSS |
| HPA replicas, mean | 9.715 | 12.65 | +30.2% | +2.115 to +3.762 | power given |
| pods started | 4.171 | 9.229 | +121.2% | +4.108 to +6.007 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.302e-16 to +1.196e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.9 | 184.8 | -0.0% | -0.497 to +0.3228 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.9 | 184.8 | -0.0% | -0.497 to +0.3228 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.439 | 2.491 | +2.1% | +0.04066 to +0.06355 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.19 | 77.36 | +5.7% | +3.791 to +4.552 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1486 | 0.2 | +34.6% | +0.01877 to +0.08409 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
