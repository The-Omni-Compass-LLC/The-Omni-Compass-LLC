# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on: native | The spine, the muscles every stack runs on: omni | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1769 | 1528 | 1099 | 1331 | 1806 | 1296 | 1787 | 1202 | 1437 | 1261 | 1850 | 2043 | 1467 | 1436 |
| response time (ms), 99th percentile | 5751 | 5641 | 4246 | 4222 | 5303 | 4840 | 4686 | 4413 | 4502 | 4801 | 4835 | 4829 | 4398 | 4915 |
| time over the response line (% of samples) | 19.52 | 15.16 | 19.26 | 16.04 | 18.59 | 14.04 | 16.77 | 12.42 | 18.76 | 14.58 | 27.42 | 23.38 | 22.07 | 17.78 |
| failed requests (%) | 6.396 | 6.109 | 7.981 | 7.386 | 6.132 | 6.139 | 5.14 | 5.125 | 5.007 | 5.197 | 10.5 | 10.42 | 8.538 | 8.312 |
| HPA replicas, mean | 9.64 | 14.58 | 9.606 | 14.54 | 9.621 | 14.37 | 9.575 | 13.99 | 9.574 | 14.46 | 9.607 | 14.4 | 9.648 | 14.43 |
| pods started | 4.933 | 11.4 | 5.6 | 12.2 | 4.867 | 10.93 | 5.4 | 10.73 | 5.333 | 11.6 | 4.929 | 11.4 | 4.933 | 11.53 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 180.8 | 180.6 | 180.9 | 180.4 | 180.4 | 180.6 | 179.3 | 179.7 | 181.3 | 180.7 | 181.7 | 181.3 | 181.7 | 180.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.8 | 180.6 | 180.9 | 180.4 | 180.4 | 180.6 | 179.3 | 179.7 | 181.3 | 180.7 | 181.7 | 181.3 | 181.7 | 180.9 |
| CPU used with Omni's own (cores), mean | 2.031 | 2.065 | 1.993 | 2.048 | 2.002 | 2.056 | 1.885 | 1.941 | 2.024 | 2.077 | 2.065 | 2.141 | 2.055 | 2.103 |
| host CPU busy, the real machine under kind (%) | 60.81 | 61.86 | 59.79 | 61.57 | 59.88 | 61.54 | 56.69 | 58.61 | 60.56 | 62.36 | 61.67 | 64.5 | 61.79 | 63.73 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.006667 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

15 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1769 | 1528 | -13.6% | -807.5 to +325.4 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5751 | 5641 | -1.9% | -736.5 to +516.6 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 19.52 | 15.16 | -22.3% | -5.975 to -2.736 | GAIN |
| failed requests (%) | 6.396 | 6.109 | -4.5% | -0.7946 to +0.2209 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.64 | 14.58 | +51.3% | +4.505 to +5.381 | power given |
| pods started | 4.933 | 11.4 | +131.1% | +5.607 to +7.326 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.904e-16 to +6.72e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.8 | 180.6 | -0.1% | -0.8585 to +0.4312 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.8 | 180.6 | -0.1% | -0.8585 to +0.4312 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.031 | 2.065 | +1.7% | +0.01544 to +0.05327 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.81 | 61.86 | +1.7% | +0.4594 to +1.628 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.968e+05 to +8.011e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.433e-05 to -9.383e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

15 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1099 | 1331 | +21.1% | -225.4 to +689.9 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4246 | 4222 | -0.6% | -575.8 to +528.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 19.26 | 16.04 | -16.7% | -4.995 to -1.454 | GAIN |
| failed requests (%) | 7.981 | 7.386 | -7.5% | -1.584 to +0.3936 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.606 | 14.54 | +51.4% | +4.497 to +5.37 | power given |
| pods started | 5.6 | 12.2 | +117.9% | +5.692 to +7.508 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.933e-16 to +4.196e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.9 | 180.4 | -0.3% | -1.172 to +0.08496 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.9 | 180.4 | -0.3% | -1.172 to +0.08496 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.993 | 2.048 | +2.7% | +0.03951 to +0.06961 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.79 | 61.57 | +3.0% | +1.354 to +2.211 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.624e+05 to +8.63e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.154e-05 to -8.148e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

15 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1806 | 1296 | -28.2% | -1090 to +70.31 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5303 | 4840 | -8.7% | -1292 to +365.4 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 18.59 | 14.04 | -24.5% | -6.363 to -2.732 | GAIN |
| failed requests (%) | 6.132 | 6.139 | +0.1% | -0.7375 to +0.7516 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.621 | 14.37 | +49.4% | +4.085 to +5.413 | power given |
| pods started | 4.867 | 10.93 | +124.7% | +4.892 to +7.241 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.1e-16 to +3.548e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.4 | 180.6 | +0.1% | -0.3449 to +0.749 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.4 | 180.6 | +0.1% | -0.3449 to +0.749 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.002 | 2.056 | +2.7% | +0.03797 to +0.06919 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.88 | 61.54 | +2.8% | +1.223 to +2.086 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

15 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1787 | 1202 | -32.7% | -1219 to +50.9 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4686 | 4413 | -5.8% | -1253 to +706.5 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 16.77 | 12.42 | -25.9% | -6.148 to -2.551 | GAIN |
| failed requests (%) | 5.14 | 5.125 | -0.3% | -0.6584 to +0.6297 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.575 | 13.99 | +46.1% | +3.472 to +5.359 | power given |
| pods started | 5.4 | 10.73 | +98.8% | +4.193 to +6.473 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.248e-15 to +1.824e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.3 | 179.7 | +0.2% | -0.4836 to +1.272 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.3 | 179.7 | +0.2% | -0.4836 to +1.272 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.885 | 1.941 | +3.0% | +0.03485 to +0.07675 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.69 | 58.61 | +3.4% | +1.361 to +2.488 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

15 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1437 | 1261 | -12.2% | -405.1 to +53.03 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4502 | 4801 | +6.6% | -507.1 to +1105 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 18.76 | 14.58 | -22.3% | -5.893 to -2.473 | GAIN |
| failed requests (%) | 5.007 | 5.197 | +3.8% | -0.2399 to +0.6214 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.574 | 14.46 | +51.0% | +4.387 to +5.383 | power given |
| pods started | 5.333 | 11.6 | +117.5% | +5.32 to +7.214 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.904e-16 to +6.72e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.3 | 180.7 | -0.3% | -1.349 to +0.2352 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.3 | 180.7 | -0.3% | -1.349 to +0.2352 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.024 | 2.077 | +2.6% | +0.03119 to +0.074 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.56 | 62.36 | +3.0% | +1.3 to +2.312 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

14 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1850 | 1888 | +2.1% | -240.7 to +316.9 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4835 | 4707 | -2.6% | -880.3 to +624.9 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 27.42 | 22.2 | -19.1% | -8.237 to -2.212 | GAIN |
| failed requests (%) | 10.5 | 9.605 | -8.6% | -2.298 to +0.5019 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.607 | 14.35 | +49.3% | +4.177 to +5.302 | power given |
| pods started | 4.929 | 11.43 | +131.9% | +5.494 to +7.506 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.252e-15 to -1.689e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.7 | 180.9 | -0.4% | -1.375 to -0.06544 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.7 | 180.9 | -0.4% | -1.375 to -0.06544 | GAIN |
| CPU used with Omni's own (cores), mean | 2.065 | 2.11 | +2.2% | +0.03058 to +0.06022 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.67 | 63.6 | +3.1% | +1.505 to +2.371 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

15 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1467 | 1436 | -2.1% | -516 to +454.3 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4398 | 4915 | +11.8% | -111 to +1145 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 22.07 | 17.78 | -19.4% | -7.122 to -1.459 | GAIN |
| failed requests (%) | 8.538 | 8.312 | -2.6% | -1.053 to +0.6014 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.648 | 14.43 | +49.5% | +4.121 to +5.433 | power given |
| pods started | 4.933 | 11.53 | +133.8% | +5.669 to +7.531 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.913e-16 to +5.176e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.7 | 180.9 | -0.5% | -1.547 to -0.1199 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.7 | 180.9 | -0.5% | -1.547 to -0.1199 | GAIN |
| CPU used with Omni's own (cores), mean | 2.055 | 2.103 | +2.3% | +0.0356 to +0.06044 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.79 | 63.73 | +3.1% | +1.566 to +2.327 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.006667 | +0.00667 | -0.007633 to +0.02097 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
