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
| response time (ms), 95th percentile | 2610 | 3557 | 2289 | 2985 | 2746 | 3422 | 2449 | 3228 | 2621 | 3842 | 2760 | 3137 | 2320 | 3342 |
| response time (ms), 99th percentile | 5428 | 6471 | 4475 | 5601 | 5260 | 6127 | 4932 | 5927 | 5611 | 6461 | 4961 | 5353 | 4209 | 5344 |
| time over the response line (% of samples) | 43.26 | 42.28 | 37.55 | 34.38 | 37.37 | 35.19 | 39.38 | 38.32 | 42.38 | 40.02 | 45.87 | 43.72 | 40.79 | 41.82 |
| failed requests (%) | 28.46 | 28.24 | 18.37 | 19.12 | 23.11 | 23.26 | 24.72 | 25.35 | 22.99 | 22.44 | 30.07 | 30 | 20.61 | 24.24 |
| HPA replicas, mean | 9.636 | 14.25 | 9.627 | 13.52 | 9.614 | 14.25 | 9.632 | 14.32 | 9.64 | 13.75 | 9.677 | 12.22 | 9.675 | 12.55 |
| pods started | 5.114 | 10.49 | 5.486 | 10.74 | 5.229 | 11 | 4.857 | 11.17 | 5.257 | 11.49 | 4.657 | 9.857 | 4.676 | 9.588 |
| worker nodes in service, mean | 5.999 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 5.999 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 184.3 | 183.9 | 184.5 | 183.7 | 183.7 | 183.7 | 183.8 | 184.4 | 184.9 | 184.1 | 184.2 | 183.8 | 184 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.3 | 183.9 | 184.5 | 183.7 | 183.7 | 183.7 | 183.8 | 184.4 | 184.9 | 184.1 | 184.2 | 183.8 | 184 |
| CPU used with Omni's own (cores), mean | 2.374 | 2.419 | 2.349 | 2.399 | 2.34 | 2.38 | 2.329 | 2.377 | 2.428 | 2.472 | 2.365 | 2.403 | 2.358 | 2.414 |
| host CPU busy, the real machine under kind (%) | 70 | 71.78 | 68.77 | 70.96 | 69 | 70.77 | 68.94 | 70.89 | 70.87 | 73.08 | 70.41 | 72.94 | 70.55 | 74.82 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.002857 | 0.002857 | 0.01714 | 0.01429 | 0.005714 | 0.005714 | 0.002857 | 0.01143 | 0.01429 | 0.008571 | 0.1 | 0.2343 | 0.1647 | 0.5824 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2610 | 3557 | +36.2% | +275.9 to +1617 | LOSS |
| response time (ms), 99th percentile | 5428 | 6471 | +19.2% | +385.7 to +1700 | LOSS |
| time over the response line (% of samples) | 43.26 | 42.28 | -2.3% | -1.941 to -0.01128 | GAIN |
| failed requests (%) | 28.46 | 28.24 | -0.8% | -1.153 to +0.6998 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.636 | 14.25 | +47.9% | +4.349 to +4.888 | power given |
| pods started | 5.114 | 10.49 | +105.0% | +4.825 to +5.918 | power given |
| worker nodes in service, mean | 5.999 | 6 | +0.0% | -0.0005173 to +0.00152 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 184.3 | +0.1% | -0.3783 to +0.7712 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.3 | +0.1% | -0.3707 to +0.7839 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.374 | 2.419 | +1.9% | +0.03739 to +0.0525 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70 | 71.78 | +2.5% | +1.539 to +2.014 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0.002857 | 0.002857 | +0.0% | -0.00833 to +0.00833 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 0

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2289 | 2985 | +30.4% | +248.5 to +1144 | LOSS |
| response time (ms), 99th percentile | 4475 | 5601 | +25.2% | +277.5 to +1974 | LOSS |
| time over the response line (% of samples) | 37.55 | 34.38 | -8.5% | -4.094 to -2.255 | GAIN |
| failed requests (%) | 18.37 | 19.12 | +4.1% | +0.08398 to +1.409 | LOSS |
| HPA replicas, mean | 9.627 | 13.52 | +40.4% | +3.346 to +4.441 | power given |
| pods started | 5.486 | 10.74 | +95.8% | +4.534 to +5.98 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.474e-16 to +8.911e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.9 | 184.5 | +0.4% | +0.1405 to +1.168 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.9 | 184.5 | +0.4% | +0.1405 to +1.168 | power given |
| CPU used with Omni's own (cores), mean | 2.349 | 2.399 | +2.1% | +0.0414 to +0.05736 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.77 | 70.96 | +3.2% | +1.976 to +2.408 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.01714 | 0.01429 | -16.7% | -0.02237 to +0.01665 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2746 | 3422 | +24.6% | -219 to +1572 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5260 | 6127 | +16.5% | +215.1 to +1519 | LOSS |
| time over the response line (% of samples) | 37.37 | 35.19 | -5.8% | -3.211 to -1.15 | GAIN |
| failed requests (%) | 23.11 | 23.26 | +0.6% | -0.839 to +1.139 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.614 | 14.25 | +48.2% | +4.351 to +4.917 | power given |
| pods started | 5.229 | 11 | +110.4% | +5.176 to +6.367 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.517e-17 to +7.15e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 183.7 | +0.0% | -0.4989 to +0.6636 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 183.7 | +0.0% | -0.4989 to +0.6636 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.34 | 2.38 | +1.7% | +0.02896 to +0.0514 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69 | 70.77 | +2.6% | +1.432 to +2.105 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.005714 | 0.005714 | +0.0% | -0.01178 to +0.01178 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2449 | 3228 | +31.8% | +146.9 to +1412 | LOSS |
| response time (ms), 99th percentile | 4932 | 5927 | +20.2% | +333.7 to +1657 | LOSS |
| time over the response line (% of samples) | 39.38 | 38.32 | -2.7% | -2.22 to +0.09993 | STEADY, inside the noise (cut) |
| failed requests (%) | 24.72 | 25.35 | +2.6% | -0.2976 to +1.566 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.632 | 14.32 | +48.6% | +4.422 to +4.945 | power given |
| pods started | 4.857 | 11.17 | +130.0% | +5.837 to +6.791 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.099e-16 to +3.576e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 183.8 | +0.1% | -0.4326 to +0.7541 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 183.8 | +0.1% | -0.4326 to +0.7541 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.329 | 2.377 | +2.0% | +0.03679 to +0.05776 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.94 | 70.89 | +2.8% | +1.632 to +2.272 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.002857 | 0.01143 | +300.0% | -0.004257 to +0.0214 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2621 | 3842 | +46.6% | +510.2 to +1932 | LOSS |
| response time (ms), 99th percentile | 5611 | 6461 | +15.2% | +213 to +1489 | LOSS |
| time over the response line (% of samples) | 42.38 | 40.02 | -5.6% | -3.764 to -0.9581 | GAIN |
| failed requests (%) | 22.99 | 22.44 | -2.4% | -1.87 to +0.7641 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.64 | 13.75 | +42.6% | +3.75 to +4.468 | power given |
| pods started | 5.257 | 11.49 | +118.5% | +5.594 to +6.863 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.407e-16 to +3.915e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184.9 | +0.3% | -0.0404 to +1.062 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184.9 | +0.3% | -0.0404 to +1.062 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.428 | 2.472 | +1.8% | +0.03699 to +0.05096 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.87 | 73.08 | +3.1% | +2.047 to +2.362 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.01429 | 0.008571 | -40.0% | -0.02226 to +0.01083 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2760 | 3137 | +13.7% | -346.1 to +1100 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4961 | 5353 | +7.9% | -385.5 to +1169 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 45.87 | 43.72 | -4.7% | -3.572 to -0.7303 | GAIN |
| failed requests (%) | 30.07 | 30 | -0.2% | -1.519 to +1.383 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.677 | 12.22 | +26.2% | +1.825 to +3.253 | power given |
| pods started | 4.657 | 9.857 | +111.7% | +4.753 to +5.647 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.608e-16 to +2.563e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 184.2 | +0.0% | -0.3677 to +0.5069 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.2 | +0.0% | -0.3677 to +0.5069 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.365 | 2.403 | +1.6% | +0.0288 to +0.04753 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.41 | 72.94 | +3.6% | +2.225 to +2.832 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.1 | 0.2343 | +134.3% | +0.1094 to +0.1592 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

34 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2320 | 3342 | +44.1% | +421.6 to +1624 | LOSS |
| response time (ms), 99th percentile | 4209 | 5344 | +27.0% | +373.9 to +1895 | LOSS |
| time over the response line (% of samples) | 40.79 | 41.82 | +2.5% | -0.5624 to +2.623 | STEADY, inside the noise (up) |
| failed requests (%) | 20.61 | 24.24 | +17.6% | +1.877 to +5.382 | LOSS |
| HPA replicas, mean | 9.675 | 12.55 | +29.7% | +2.055 to +3.694 | power given |
| pods started | 4.676 | 9.588 | +105.0% | +4.176 to +5.648 | power given |
| worker nodes in service, mean | 5.999 | 6 | +0.0% | -0.0005335 to +0.001564 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 184 | +0.1% | -0.3641 to +0.7701 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 184 | +0.1% | -0.3516 to +0.7784 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.358 | 2.414 | +2.4% | +0.04152 to +0.07097 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.55 | 74.82 | +6.1% | +3.842 to +4.701 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1647 | 0.5824 | +253.6% | -0.4019 to +1.237 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
