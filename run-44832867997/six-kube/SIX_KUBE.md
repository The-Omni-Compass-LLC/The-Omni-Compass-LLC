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
| response time (ms), 95th percentile | 2647 | 3583 | 2570 | 3245 | 2920 | 3718 | 3074 | 3505 | 2005 | 2971 | 3600 | 3639 | 2238 | 3468 |
| response time (ms), 99th percentile | 4714 | 5523 | 5360 | 6319 | 5662 | 6520 | 5355 | 6070 | 4890 | 5361 | 5947 | 6377 | 4199 | 5145 |
| time over the response line (% of samples) | 34.82 | 33.33 | 40.9 | 38.18 | 45.74 | 44.03 | 41 | 39.76 | 40.17 | 36.83 | 48.51 | 44.07 | 35.68 | 37.9 |
| failed requests (%) | 21.77 | 20.7 | 19.44 | 20.6 | 30.38 | 29.98 | 25.62 | 24.98 | 23.63 | 24.57 | 26.22 | 25.83 | 17.19 | 21.11 |
| HPA replicas, mean | 9.576 | 14.38 | 9.667 | 13.96 | 9.665 | 14.5 | 9.634 | 14.54 | 9.671 | 13.09 | 9.693 | 12.28 | 9.683 | 12.64 |
| pods started | 5.6 | 11.94 | 5.086 | 10.74 | 4.657 | 10.77 | 5.029 | 10.83 | 4.714 | 10.46 | 4.429 | 9.943 | 4.429 | 9.514 |
| worker nodes in service, mean | 6 | 6 | 5.994 | 6 | 6 | 6 | 6 | 6 | 5.999 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.2 | 183 | 184.8 | 185.5 | 184.5 | 184.4 | 184.1 | 183.8 | 183.5 | 184.1 | 185.3 | 184.8 | 183 | 182.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.2 | 183 | 184.7 | 185.5 | 184.5 | 184.4 | 184.1 | 183.8 | 183.4 | 184.1 | 185.3 | 184.8 | 183 | 182.9 |
| CPU used with Omni's own (cores), mean | 2.249 | 2.302 | 2.454 | 2.511 | 2.406 | 2.457 | 2.366 | 2.423 | 2.329 | 2.383 | 2.452 | 2.495 | 2.253 | 2.304 |
| host CPU busy, the real machine under kind (%) | 66.18 | 68.28 | 71.71 | 74.32 | 71.47 | 73.63 | 70.2 | 72.49 | 68.68 | 70.92 | 72.85 | 75.76 | 67.66 | 71.66 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0 | 0.01429 | 0.02857 | 0 | 0.005714 | 0.005714 | 0.01429 | 0.002857 | 0.01429 | 0.1086 | 0.1 | 0.1457 | 0.1686 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2647 | 3583 | +35.4% | +335.4 to +1537 | LOSS |
| response time (ms), 99th percentile | 4714 | 5523 | +17.2% | +260.8 to +1358 | LOSS |
| time over the response line (% of samples) | 34.82 | 33.33 | -4.3% | -2.484 to -0.4923 | GAIN |
| failed requests (%) | 21.77 | 20.7 | -4.9% | -1.972 to -0.1689 | GAIN |
| HPA replicas, mean | 9.576 | 14.38 | +50.2% | +4.572 to +5.039 | power given |
| pods started | 5.6 | 11.94 | +113.3% | +5.725 to +6.96 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.999e-16 to -9.092e-18 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.2 | 183 | -0.1% | -0.6748 to +0.2813 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.2 | 183 | -0.1% | -0.6748 to +0.2813 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.249 | 2.302 | +2.3% | +0.0435 to +0.06166 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.18 | 68.28 | +3.2% | +1.806 to +2.403 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2570 | 3245 | +26.3% | +236.5 to +1113 | LOSS |
| response time (ms), 99th percentile | 5360 | 6319 | +17.9% | +340.1 to +1578 | LOSS |
| time over the response line (% of samples) | 40.9 | 38.18 | -6.7% | -4.12 to -1.322 | GAIN |
| failed requests (%) | 19.44 | 20.6 | +6.0% | +0.3675 to +1.946 | LOSS |
| HPA replicas, mean | 9.667 | 13.96 | +44.4% | +3.773 to +4.818 | power given |
| pods started | 5.086 | 10.74 | +111.2% | +4.965 to +6.349 | power given |
| worker nodes in service, mean | 5.994 | 6 | +0.1% | -0.006195 to +0.0182 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.8 | 185.5 | +0.4% | +0.2359 to +1.226 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.7 | 185.5 | +0.5% | +0.2796 to +1.425 | power given |
| CPU used with Omni's own (cores), mean | 2.454 | 2.511 | +2.3% | +0.04824 to +0.06589 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.71 | 74.32 | +3.6% | +2.348 to +2.873 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.01429 | 0.02857 | +100.0% | -0.006361 to +0.03493 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2920 | 3718 | +27.3% | +115.2 to +1482 | LOSS |
| response time (ms), 99th percentile | 5662 | 6520 | +15.2% | +249.2 to +1467 | LOSS |
| time over the response line (% of samples) | 45.74 | 44.03 | -3.7% | -3.052 to -0.3633 | GAIN |
| failed requests (%) | 30.38 | 29.98 | -1.3% | -1.612 to +0.8055 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.665 | 14.5 | +50.1% | +4.604 to +5.074 | power given |
| pods started | 4.657 | 10.77 | +131.3% | +5.465 to +6.764 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.622e-16 to +3.592e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.5 | 184.4 | -0.1% | -0.644 to +0.3547 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.5 | 184.4 | -0.1% | -0.644 to +0.3547 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.406 | 2.457 | +2.1% | +0.04282 to +0.05872 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.47 | 73.63 | +3.0% | +1.971 to +2.345 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0 | 0.005714 | +0.00571 | -0.002375 to +0.0138 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3074 | 3505 | +14.0% | -419.8 to +1282 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5355 | 6070 | +13.4% | -56.23 to +1488 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 41 | 39.76 | -3.0% | -2.439 to -0.04795 | GAIN |
| failed requests (%) | 25.62 | 24.98 | -2.5% | -1.761 to +0.4909 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.634 | 14.54 | +51.0% | +4.702 to +5.121 | power given |
| pods started | 5.029 | 10.83 | +115.3% | +5.295 to +6.305 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.301e-16 to +5.838e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 183.8 | -0.2% | -0.7792 to +0.1008 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 183.8 | -0.2% | -0.7792 to +0.1008 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.366 | 2.423 | +2.4% | +0.04545 to +0.06805 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.2 | 72.49 | +3.3% | +1.961 to +2.62 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.005714 | 0.01429 | +150.0% | -0.006724 to +0.02387 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2005 | 2971 | +48.2% | +198.7 to +1735 | LOSS |
| response time (ms), 99th percentile | 4890 | 5361 | +9.6% | -323.2 to +1265 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 40.17 | 36.83 | -8.3% | -4.893 to -1.782 | GAIN |
| failed requests (%) | 23.63 | 24.57 | +4.0% | -0.3632 to +2.259 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.671 | 13.09 | +35.4% | +2.784 to +4.063 | power given |
| pods started | 4.714 | 10.46 | +121.8% | +5.075 to +6.411 | power given |
| worker nodes in service, mean | 5.999 | 6 | +0.0% | -0.00152 to +0.004465 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 184.1 | +0.4% | +0.1853 to +1.174 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.4 | 184.1 | +0.4% | +0.1891 to +1.23 | power given |
| CPU used with Omni's own (cores), mean | 2.329 | 2.383 | +2.3% | +0.04562 to +0.06234 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.68 | 70.92 | +3.3% | +2.081 to +2.405 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.002857 | 0.01429 | +400.0% | -0.00244 to +0.0253 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3600 | 3639 | +1.1% | -455.3 to +535.1 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5947 | 6377 | +7.2% | -162.6 to +1024 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 48.51 | 44.07 | -9.2% | -6.577 to -2.304 | GAIN |
| failed requests (%) | 26.22 | 25.83 | -1.5% | -1.806 to +1.033 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.693 | 12.28 | +26.7% | +1.917 to +3.253 | power given |
| pods started | 4.429 | 9.943 | +124.5% | +4.872 to +6.156 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.242e-16 to +4.227e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.3 | 184.8 | -0.3% | -0.9041 to -0.09104 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.3 | 184.8 | -0.3% | -0.9041 to -0.09104 | GAIN |
| CPU used with Omni's own (cores), mean | 2.452 | 2.495 | +1.7% | +0.03129 to +0.0541 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.85 | 75.76 | +4.0% | +2.62 to +3.203 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.1086 | 0.1 | -7.9% | -0.0214 to +0.004257 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2238 | 3468 | +55.0% | +665.1 to +1795 | LOSS |
| response time (ms), 99th percentile | 4199 | 5145 | +22.5% | +388.7 to +1503 | LOSS |
| time over the response line (% of samples) | 35.68 | 37.9 | +6.2% | +0.2967 to +4.155 | LOSS |
| failed requests (%) | 17.19 | 21.11 | +22.8% | +2.489 to +5.357 | LOSS |
| HPA replicas, mean | 9.683 | 12.64 | +30.6% | +2.187 to +3.73 | power given |
| pods started | 4.429 | 9.514 | +114.8% | +4.316 to +5.855 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.826e-16 to +4.871e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183 | 182.9 | -0.1% | -0.5832 to +0.3407 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183 | 182.9 | -0.1% | -0.5832 to +0.3407 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.253 | 2.304 | +2.3% | +0.03544 to +0.06595 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.66 | 71.66 | +5.9% | +3.499 to +4.503 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1457 | 0.1686 | +15.7% | +0.002307 to +0.04341 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
