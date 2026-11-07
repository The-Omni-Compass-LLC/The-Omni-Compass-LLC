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
| response time (ms), 95th percentile | 3015 | 3339 | 2228 | 3379 | 2688 | 3555 | 2411 | 3077 | 2965 | 4209 | 3170 | 3330 | 2785 | 3908 |
| response time (ms), 99th percentile | 4958 | 5734 | 4259 | 5891 | 5163 | 6029 | 4256 | 5201 | 6061 | 6980 | 5921 | 5809 | 5128 | 6118 |
| time over the response line (% of samples) | 38.8 | 37.1 | 41.55 | 40.22 | 41.29 | 39.79 | 35.01 | 34.06 | 48.56 | 43.82 | 44.77 | 41.26 | 43.95 | 45.37 |
| failed requests (%) | 24.29 | 24.48 | 22.28 | 22.05 | 26.5 | 26.14 | 22.41 | 22.6 | 25.96 | 26.59 | 24.91 | 25.07 | 20.89 | 24.83 |
| HPA replicas, mean | 9.605 | 14.33 | 9.677 | 13.43 | 9.638 | 14.34 | 9.61 | 14.17 | 9.693 | 13.52 | 9.652 | 12.75 | 9.724 | 12.73 |
| pods started | 5.314 | 11.2 | 4.829 | 10.54 | 4.8 | 11.26 | 5 | 11.29 | 4.6 | 10.74 | 4.943 | 9.943 | 4.057 | 9.229 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 5.997 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.6 | 183.9 | 184.3 | 185 | 183.9 | 183.8 | 182.5 | 182.7 | 185.3 | 186 | 184.2 | 184.4 | 184.4 | 185.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.6 | 183.9 | 184.3 | 185 | 183.9 | 183.7 | 182.5 | 182.7 | 185.3 | 186 | 184.2 | 184.4 | 184.4 | 185.1 |
| CPU used with Omni's own (cores), mean | 2.33 | 2.377 | 2.401 | 2.455 | 2.348 | 2.382 | 2.238 | 2.295 | 2.53 | 2.571 | 2.385 | 2.432 | 2.428 | 2.481 |
| host CPU busy, the real machine under kind (%) | 68.48 | 70.25 | 70.35 | 72.79 | 69.63 | 71.26 | 66.72 | 68.57 | 73.72 | 75.73 | 70.53 | 73.18 | 72.3 | 76.34 |
| organism work | 2.148e+11 | 2.148e+11 | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.421e+11 | 1.422e+11 | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.391 | 2.252 | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.512 | 1.511 | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0.002857 | 0.01714 | 0.005714 | 0.01143 | 0.01143 | 0.01143 | 0.01714 | 0.01429 | 0.008571 | 0.09429 | 0.2286 | 0.1457 | 0.1686 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3015 | 3339 | +10.8% | -343.5 to +992.5 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4958 | 5734 | +15.7% | +58.61 to +1495 | LOSS |
| time over the response line (% of samples) | 38.8 | 37.1 | -4.4% | -2.715 to -0.6829 | GAIN |
| failed requests (%) | 24.29 | 24.48 | +0.8% | -0.7372 to +1.121 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.605 | 14.33 | +49.2% | +4.457 to +4.996 | power given |
| pods started | 5.314 | 11.2 | +110.8% | +5.455 to +6.317 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.825e-16 to +1.749e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.6 | 183.9 | +0.1% | -0.2346 to +0.7418 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.6 | 183.9 | +0.1% | -0.2346 to +0.7418 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.33 | 2.377 | +2.0% | +0.03624 to +0.05902 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.48 | 70.25 | +2.6% | +1.496 to +2.049 | shown, not judged |
| organism work | 2.148e+11 | 2.148e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.421e+11 | 1.422e+11 | +0.1% | +7.875e+07 to +7.875e+07 | power given |
| organism time over the line (% of steps) | 2.391 | 2.252 | -5.8% | -0.1384 to -0.1384 | GAIN |
| organism work per energy | 1.512 | 1.511 | -0.1% | -0.0008374 to -0.0008374 | power given |
| organism behind its window (s) | 0 | 0.002857 | +0.00286 | -0.002949 to +0.008663 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2228 | 3379 | +51.6% | +583.9 to +1717 | LOSS |
| response time (ms), 99th percentile | 4259 | 5891 | +38.3% | +886.7 to +2378 | LOSS |
| time over the response line (% of samples) | 41.55 | 40.22 | -3.2% | -2.807 to +0.1548 | STEADY, inside the noise (cut) |
| failed requests (%) | 22.28 | 22.05 | -1.0% | -1.128 to +0.6622 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.677 | 13.43 | +38.8% | +3.156 to +4.357 | power given |
| pods started | 4.829 | 10.54 | +118.3% | +4.913 to +6.516 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.266e-16 to -3.315e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 185 | +0.3% | +0.08759 to +1.193 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.3 | 185 | +0.3% | +0.08759 to +1.193 | power given |
| CPU used with Omni's own (cores), mean | 2.401 | 2.455 | +2.2% | +0.02982 to +0.07813 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.35 | 72.79 | +3.5% | +1.697 to +3.178 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.01714 | 0.005714 | -66.7% | -0.02761 to +0.004749 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2688 | 3555 | +32.2% | +201.4 to +1533 | LOSS |
| response time (ms), 99th percentile | 5163 | 6029 | +16.8% | +203.4 to +1529 | LOSS |
| time over the response line (% of samples) | 41.29 | 39.79 | -3.6% | -2.489 to -0.5112 | GAIN |
| failed requests (%) | 26.5 | 26.14 | -1.4% | -1.345 to +0.6288 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.638 | 14.34 | +48.8% | +4.435 to +4.968 | power given |
| pods started | 4.8 | 11.26 | +134.5% | +5.815 to +7.099 | power given |
| worker nodes in service, mean | 6 | 5.997 | -0.0% | -0.009048 to +0.00308 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.9 | 183.8 | -0.1% | -0.6741 to +0.4213 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.9 | 183.7 | -0.1% | -0.787 to +0.414 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.348 | 2.382 | +1.4% | +0.01857 to +0.04856 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.63 | 71.26 | +2.4% | +1.16 to +2.115 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.01143 | 0.01143 | +0.0% | -0.01666 to +0.01666 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2411 | 3077 | +27.7% | -47.56 to +1381 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4256 | 5201 | +22.2% | +252.6 to +1637 | LOSS |
| time over the response line (% of samples) | 35.01 | 34.06 | -2.7% | -1.785 to -0.1076 | GAIN |
| failed requests (%) | 22.41 | 22.6 | +0.8% | -0.8675 to +1.242 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.61 | 14.17 | +47.5% | +4.298 to +4.823 | power given |
| pods started | 5 | 11.29 | +125.7% | +5.616 to +6.955 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.472e-16 to +2.426e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.5 | 182.7 | +0.1% | -0.4384 to +0.7769 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.5 | 182.7 | +0.1% | -0.4384 to +0.7769 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.238 | 2.295 | +2.5% | +0.03215 to +0.08149 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.72 | 68.57 | +2.8% | +1.325 to +2.383 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | power given |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | power given |
| organism behind its window (s) | 0.01143 | 0.01714 | +50.0% | -0.01459 to +0.02602 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2965 | 4209 | +41.9% | +479.8 to +2008 | LOSS |
| response time (ms), 99th percentile | 6061 | 6980 | +15.2% | +270.5 to +1567 | LOSS |
| time over the response line (% of samples) | 48.56 | 43.82 | -9.8% | -6.459 to -3.023 | GAIN |
| failed requests (%) | 25.96 | 26.59 | +2.4% | -0.5308 to +1.792 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.693 | 13.52 | +39.5% | +3.26 to +4.391 | power given |
| pods started | 4.6 | 10.74 | +133.5% | +5.445 to +6.841 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.3e-15 to -4.762e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.3 | 186 | +0.4% | +0.2593 to +1.142 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.3 | 186 | +0.4% | +0.2593 to +1.142 | power given |
| CPU used with Omni's own (cores), mean | 2.53 | 2.571 | +1.6% | +0.03224 to +0.04898 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.72 | 75.73 | +2.7% | +1.745 to +2.283 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.01429 | 0.008571 | -40.0% | -0.02226 to +0.01083 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3170 | 3330 | +5.0% | -519.7 to +839.8 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5921 | 5809 | -1.9% | -758 to +533.8 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 44.77 | 41.26 | -7.8% | -5.167 to -1.842 | GAIN |
| failed requests (%) | 24.91 | 25.07 | +0.6% | -1.13 to +1.445 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.652 | 12.75 | +32.1% | +2.447 to +3.753 | power given |
| pods started | 4.943 | 9.943 | +101.2% | +4.303 to +5.697 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.871e-16 to +1.826e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.4 | +0.1% | -0.2779 to +0.6759 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.4 | +0.1% | -0.2779 to +0.6759 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.385 | 2.432 | +2.0% | +0.03203 to +0.06178 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.53 | 73.18 | +3.8% | +2.215 to +3.087 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | power given |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | power given |
| organism behind its window (s) | 0.09429 | 0.2286 | +142.4% | +0.1094 to +0.1592 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2785 | 3908 | +40.3% | +616.5 to +1630 | LOSS |
| response time (ms), 99th percentile | 5128 | 6118 | +19.3% | +342 to +1639 | LOSS |
| time over the response line (% of samples) | 43.95 | 45.37 | +3.2% | -0.0651 to +2.907 | STEADY, inside the noise (up) |
| failed requests (%) | 20.89 | 24.83 | +18.9% | +2.489 to +5.387 | LOSS |
| HPA replicas, mean | 9.724 | 12.73 | +30.9% | +2.196 to +3.813 | power given |
| pods started | 4.057 | 9.229 | +127.5% | +4.424 to +5.919 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.927e-16 to +5.942e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 185.1 | +0.3% | +0.07461 to +1.162 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 185.1 | +0.3% | +0.07461 to +1.162 | power given |
| CPU used with Omni's own (cores), mean | 2.428 | 2.481 | +2.2% | +0.0436 to +0.06374 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.3 | 76.34 | +5.6% | +3.72 to +4.344 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1457 | 0.1686 | +15.7% | -0.004879 to +0.05059 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
