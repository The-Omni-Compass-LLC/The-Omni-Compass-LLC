# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on: native | The spine, the muscles every stack runs on: omni | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1322 | 1234 | 1181 | 1381 | 1229 | 938.6 | 1467 | 1430 | 1778 | 1813 | 1031 | 1088 |
| response time (ms), 99th percentile | 5020 | 4921 | 4159 | 4484 | 4429 | 4075 | 4196 | 4360 | 4970 | 5050 | 3703 | 4145 |
| time over the response line (% of samples) | 15.11 | 11.12 | 19.14 | 14.42 | 13.68 | 10.22 | 21.54 | 16.05 | 25.37 | 20.33 | 17.42 | 13.5 |
| failed requests (%) | 4.233 | 3.824 | 7.478 | 6.351 | 3.847 | 3.917 | 6.807 | 6.456 | 10.19 | 8.428 | 6.755 | 6.094 |
| HPA replicas, mean | 9.593 | 14.51 | 9.608 | 14.19 | 9.567 | 14.13 | 9.557 | 13.99 | 9.604 | 14.28 | 9.601 | 14.08 |
| pods started | 5.341 | 11.46 | 5.39 | 12.59 | 5.366 | 11.02 | 5.375 | 10.57 | 5.024 | 11.59 | 5.317 | 12.83 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 5.997 |
| energy, parked workers still on at idle power (Wh, declared model) | 179.4 | 179.9 | 180.5 | 179.9 | 178.7 | 179 | 180.8 | 179.9 | 181.7 | 181.3 | 180 | 179.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.4 | 179.9 | 180.5 | 179.9 | 178.7 | 179 | 180.8 | 179.9 | 181.7 | 181.3 | 180 | 179 |
| CPU used with Omni's own (cores), mean | 1.9 | 1.939 | 1.964 | 2.006 | 1.822 | 1.868 | 2.006 | 2.039 | 2.094 | 2.135 | 1.907 | 1.944 |
| host CPU busy, the real machine under kind (%) | 56.71 | 58 | 58.78 | 60.42 | 54.55 | 56.21 | 59.68 | 61 | 62.21 | 63.76 | 57.24 | 58.79 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.09024 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1322 | 1234 | -6.7% | -307.5 to +130 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5020 | 4921 | -2.0% | -465.7 to +267.8 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 15.11 | 11.12 | -26.4% | -4.998 to -2.975 | GAIN |
| failed requests (%) | 4.233 | 3.824 | -9.7% | -0.7186 to -0.09935 | GAIN |
| HPA replicas, mean | 9.593 | 14.51 | +51.2% | +4.66 to +5.172 | power given |
| pods started | 5.341 | 11.46 | +114.6% | +5.617 to +6.627 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.682e-16 to +2.382e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.4 | 179.9 | +0.2% | +0.02212 to +0.8402 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.4 | 179.9 | +0.2% | +0.02212 to +0.8402 | power given |
| CPU used with Omni's own (cores), mean | 1.9 | 1.939 | +2.1% | +0.02326 to +0.05515 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.71 | 58 | +2.3% | +0.9487 to +1.629 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.966e+05 to +8e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.421e-05 to -9.38e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1181 | 1381 | +17.0% | -4.695 to +405.7 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4159 | 4484 | +7.8% | -210.7 to +859.1 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 19.14 | 14.42 | -24.6% | -6.173 to -3.252 | GAIN |
| failed requests (%) | 7.478 | 6.351 | -15.1% | -1.837 to -0.4183 | GAIN |
| HPA replicas, mean | 9.608 | 14.19 | +47.7% | +4.315 to +4.842 | power given |
| pods started | 5.39 | 12.59 | +133.5% | +6.666 to +7.724 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.038e-16 to +2.438e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.5 | 179.9 | -0.3% | -0.9939 to -0.03805 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.5 | 179.9 | -0.3% | -0.9939 to -0.03805 | GAIN |
| CPU used with Omni's own (cores), mean | 1.964 | 2.006 | +2.1% | +0.03162 to +0.05231 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.78 | 60.42 | +2.8% | +1.374 to +1.899 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.623e+05 to +8.627e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.151e-05 to -8.147e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1229 | 938.6 | -23.6% | -518.5 to -61.93 | GAIN |
| response time (ms), 99th percentile | 4429 | 4075 | -8.0% | -797.7 to +88.68 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 13.68 | 10.22 | -25.3% | -4.417 to -2.512 | GAIN |
| failed requests (%) | 3.847 | 3.917 | +1.8% | -0.231 to +0.3708 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.567 | 14.13 | +47.7% | +4.16 to +4.97 | power given |
| pods started | 5.366 | 11.02 | +105.5% | +5.243 to +6.074 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.612e-16 to +4.645e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.7 | 179 | +0.2% | -0.04158 to +0.6615 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.7 | 179 | +0.2% | -0.04158 to +0.6615 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.822 | 1.868 | +2.5% | +0.03649 to +0.05374 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 54.55 | 56.21 | +3.0% | +1.429 to +1.89 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1467 | 1430 | -2.5% | -241.7 to +168 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4196 | 4360 | +3.9% | -242.8 to +570.2 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 21.54 | 16.05 | -25.5% | -7.175 to -3.815 | GAIN |
| failed requests (%) | 6.807 | 6.456 | -5.2% | -0.669 to -0.03245 | GAIN |
| HPA replicas, mean | 9.557 | 13.99 | +46.4% | +3.914 to +4.957 | power given |
| pods started | 5.375 | 10.57 | +96.7% | +4.602 to +5.798 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.403e-16 to +1.185e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.8 | 179.9 | -0.5% | -1.36 to -0.5897 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.8 | 179.9 | -0.5% | -1.36 to -0.5897 | GAIN |
| CPU used with Omni's own (cores), mean | 2.006 | 2.039 | +1.7% | +0.02389 to +0.04318 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.68 | 61 | +2.2% | +1.046 to +1.591 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1778 | 1813 | +2.0% | -205 to +275.9 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4970 | 5050 | +1.6% | -385.6 to +545.7 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 25.37 | 20.33 | -19.9% | -6.767 to -3.315 | GAIN |
| failed requests (%) | 10.19 | 8.428 | -17.3% | -2.837 to -0.6877 | GAIN |
| HPA replicas, mean | 9.604 | 14.28 | +48.7% | +4.384 to +4.964 | power given |
| pods started | 5.024 | 11.59 | +130.6% | +5.97 to +7.152 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.317e-16 to +3.317e-16 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 181.7 | 181.3 | -0.2% | -0.7708 to +0.08402 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.7 | 181.3 | -0.2% | -0.7708 to +0.08402 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.094 | 2.135 | +2.0% | +0.03155 to +0.05189 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.21 | 63.76 | +2.5% | +1.307 to +1.802 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1031 | 1088 | +5.5% | -120.7 to +234.5 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3703 | 4145 | +11.9% | -114.5 to +999.2 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 17.42 | 13.5 | -22.5% | -5.364 to -2.466 | GAIN |
| failed requests (%) | 6.755 | 6.094 | -9.8% | -1.075 to -0.2476 | GAIN |
| HPA replicas, mean | 9.601 | 14.08 | +46.6% | +4.174 to +4.776 | power given |
| pods started | 5.317 | 12.83 | +141.3% | +6.853 to +8.171 | power given |
| worker nodes in service, mean | 6 | 5.997 | -0.0% | -0.008458 to +0.002859 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 180 | 179.1 | -0.5% | -1.281 to -0.5141 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180 | 179 | -0.5% | -1.38 to -0.5273 | GAIN |
| CPU used with Omni's own (cores), mean | 1.907 | 1.944 | +1.9% | +0.02713 to +0.04576 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.24 | 58.79 | +2.7% | +1.283 to +1.825 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.09024 | +0.0902 | +0.07648 to +0.104 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Energy / Facility / Industrial

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
