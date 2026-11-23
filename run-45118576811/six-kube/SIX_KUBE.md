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
| response time (ms), 95th percentile | 2682 | 3816 | 2175 | 3065 | 3295 | 4024 | 2441 | 3621 | 2337 | 2270 | 2623 | 2472 | 2166 | 3676 |
| response time (ms), 99th percentile | 5340 | 6593 | 4453 | 5392 | 5896 | 6973 | 5319 | 6088 | 4846 | 4694 | 4602 | 4345 | 3934 | 5997 |
| time over the response line (% of samples) | 45.59 | 44.76 | 40.4 | 38.06 | 43.26 | 41.93 | 40.66 | 39.25 | 31.94 | 27.18 | 35.87 | 34.52 | 46.69 | 49.47 |
| failed requests (%) | 30.16 | 30.44 | 20.32 | 21.81 | 27.05 | 28.12 | 25.52 | 25.06 | 14.98 | 15.55 | 20.27 | 21.23 | 25.68 | 30.03 |
| HPA replicas, mean | 9.653 | 14.28 | 9.644 | 13.08 | 9.628 | 14.39 | 9.655 | 14.36 | 9.608 | 13.52 | 9.642 | 12.72 | 9.736 | 12.04 |
| pods started | 4.943 | 10.74 | 5.171 | 9.886 | 4.914 | 10.71 | 4.714 | 10.23 | 5.629 | 11.4 | 5.057 | 10.69 | 3.771 | 8.457 |
| worker nodes in service, mean | 6 | 6 | 5.998 | 6 | 6 | 6 | 6 | 5.999 | 6 | 6 | 6 | 6 | 6 | 5.999 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 184.6 | 183.4 | 184.5 | 184.7 | 184.1 | 184.3 | 183.8 | 183 | 183.3 | 183 | 183.2 | 185 | 184.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.3 | 184.6 | 183.4 | 184.5 | 184.7 | 184.1 | 184.3 | 183.8 | 183 | 183.3 | 183 | 183.2 | 185 | 184.8 |
| CPU used with Omni's own (cores), mean | 2.407 | 2.456 | 2.333 | 2.39 | 2.397 | 2.449 | 2.378 | 2.425 | 2.257 | 2.314 | 2.263 | 2.31 | 2.444 | 2.492 |
| host CPU busy, the real machine under kind (%) | 71.22 | 73.2 | 68.93 | 71.23 | 71.34 | 73.43 | 70.66 | 72.69 | 66.51 | 69.06 | 67.75 | 70.62 | 73.61 | 77.95 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0 | 0.01714 | 0.03429 | 0.008571 | 0.008571 | 0.008571 | 0.008571 | 0.005714 | 0.008571 | 0.1029 | 0.1057 | 0.1914 | 0.1971 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2682 | 3816 | +42.3% | +507.4 to +1761 | LOSS |
| response time (ms), 99th percentile | 5340 | 6593 | +23.4% | +552.1 to +1952 | LOSS |
| time over the response line (% of samples) | 45.59 | 44.76 | -1.8% | -2.06 to +0.3848 | STEADY, inside the noise (cut) |
| failed requests (%) | 30.16 | 30.44 | +0.9% | -1.066 to +1.623 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.653 | 14.28 | +47.9% | +4.354 to +4.899 | power given |
| pods started | 4.943 | 10.74 | +117.3% | +5.323 to +6.277 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.677e-16 to +2.125e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 184.6 | +0.2% | -0.2756 to +0.8339 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.3 | 184.6 | +0.2% | -0.2756 to +0.8339 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.407 | 2.456 | +2.1% | +0.04327 to +0.05587 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.22 | 73.2 | +2.8% | +1.838 to +2.121 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2175 | 3065 | +40.9% | +398.7 to +1380 | LOSS |
| response time (ms), 99th percentile | 4453 | 5392 | +21.1% | +125.3 to +1754 | LOSS |
| time over the response line (% of samples) | 40.4 | 38.06 | -5.8% | -4.121 to -0.559 | GAIN |
| failed requests (%) | 20.32 | 21.81 | +7.3% | +0.3014 to +2.675 | LOSS |
| HPA replicas, mean | 9.644 | 13.08 | +35.6% | +2.812 to +4.063 | power given |
| pods started | 5.171 | 9.886 | +91.2% | +4.055 to +5.373 | power given |
| worker nodes in service, mean | 5.998 | 6 | +0.0% | -0.002317 to +0.006808 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.4 | 184.5 | +0.6% | +0.5794 to +1.482 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.4 | 184.5 | +0.6% | +0.615 to +1.537 | power given |
| CPU used with Omni's own (cores), mean | 2.333 | 2.39 | +2.4% | +0.04746 to +0.06683 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.93 | 71.23 | +3.3% | +1.944 to +2.659 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.01714 | 0.03429 | +100.0% | -0.0005005 to +0.03479 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3295 | 4024 | +22.1% | -38.53 to +1495 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5896 | 6973 | +18.3% | +382.4 to +1772 | LOSS |
| time over the response line (% of samples) | 43.26 | 41.93 | -3.1% | -2.337 to -0.3298 | GAIN |
| failed requests (%) | 27.05 | 28.12 | +4.0% | +0.3013 to +1.843 | LOSS |
| HPA replicas, mean | 9.628 | 14.39 | +49.4% | +4.55 to +4.969 | power given |
| pods started | 4.914 | 10.71 | +118.0% | +5.316 to +6.284 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.128e-16 to +3.113e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.7 | 184.1 | -0.3% | -1.069 to -0.09781 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.7 | 184.1 | -0.3% | -1.069 to -0.09781 | GAIN |
| CPU used with Omni's own (cores), mean | 2.397 | 2.449 | +2.2% | +0.03007 to +0.0747 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.34 | 73.43 | +2.9% | +1.854 to +2.328 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.008571 | 0.008571 | +0.0% | -0.01443 to +0.01443 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2441 | 3621 | +48.3% | +493.6 to +1865 | LOSS |
| response time (ms), 99th percentile | 5319 | 6088 | +14.5% | +89.19 to +1448 | LOSS |
| time over the response line (% of samples) | 40.66 | 39.25 | -3.5% | -2.596 to -0.2292 | GAIN |
| failed requests (%) | 25.52 | 25.06 | -1.8% | -1.41 to +0.4887 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.655 | 14.36 | +48.8% | +4.41 to +5.01 | power given |
| pods started | 4.714 | 10.23 | +117.0% | +5.012 to +6.017 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003942 to +0.001342 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 183.8 | -0.2% | -0.953 to +0.04754 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.3 | 183.8 | -0.3% | -1.009 to +0.05156 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.378 | 2.425 | +2.0% | +0.03539 to +0.05803 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.66 | 72.69 | +2.9% | +1.73 to +2.32 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.008571 | 0.008571 | +0.0% | -0.01443 to +0.01443 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2337 | 2270 | -2.9% | -547.5 to +413.3 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4846 | 4694 | -3.1% | -755.3 to +451.3 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 31.94 | 27.18 | -14.9% | -6.535 to -2.994 | GAIN |
| failed requests (%) | 14.98 | 15.55 | +3.8% | -0.5236 to +1.669 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.608 | 13.52 | +40.8% | +3.269 to +4.561 | power given |
| pods started | 5.629 | 11.4 | +102.5% | +5.012 to +6.531 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.979e-16 to +2.441e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183 | 183.3 | +0.2% | -0.1378 to +0.7109 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183 | 183.3 | +0.2% | -0.1378 to +0.7109 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.257 | 2.314 | +2.5% | +0.03971 to +0.0739 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.51 | 69.06 | +3.8% | +2.062 to +3.037 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.005714 | 0.008571 | +50.0% | -0.01028 to +0.01599 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2623 | 2472 | -5.8% | -634.9 to +332.5 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4602 | 4345 | -5.6% | -830.4 to +315.2 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 35.87 | 34.52 | -3.8% | -2.316 to -0.3789 | GAIN |
| failed requests (%) | 20.27 | 21.23 | +4.7% | -0.216 to +2.137 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.642 | 12.72 | +31.9% | +2.377 to +3.77 | power given |
| pods started | 5.057 | 10.69 | +111.3% | +5.114 to +6.143 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.286e-16 to +5.346e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183 | 183.2 | +0.1% | -0.2169 to +0.6517 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183 | 183.2 | +0.1% | -0.2169 to +0.6517 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.263 | 2.31 | +2.1% | +0.02902 to +0.06496 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.75 | 70.62 | +4.2% | +2.298 to +3.453 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.1029 | 0.1057 | +2.8% | -0.01028 to +0.01599 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2166 | 3676 | +69.7% | +936.1 to +2084 | LOSS |
| response time (ms), 99th percentile | 3934 | 5997 | +52.4% | +1347 to +2779 | LOSS |
| time over the response line (% of samples) | 46.69 | 49.47 | +5.9% | +0.9299 to +4.622 | LOSS |
| failed requests (%) | 25.68 | 30.03 | +16.9% | +2.509 to +6.191 | LOSS |
| HPA replicas, mean | 9.736 | 12.04 | +23.6% | +1.521 to +3.078 | power given |
| pods started | 3.771 | 8.457 | +124.2% | +3.919 to +5.453 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.004438 to +0.001511 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 185 | 184.8 | -0.1% | -0.5868 to +0.2808 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185 | 184.8 | -0.1% | -0.6463 to +0.2809 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.444 | 2.492 | +1.9% | +0.03838 to +0.05674 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.61 | 77.95 | +5.9% | +4.138 to +4.543 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1914 | 0.1971 | +3.0% | -0.02055 to +0.03198 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
