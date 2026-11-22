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
| response time (ms), 95th percentile | 1449 | 1292 | 1158 | 1443 | 1470 | 1200 | 1637 | 1246 | 1416 | 1500 | 1635 | 1807 | 1067 | 1078 |
| response time (ms), 99th percentile | 4848 | 4750 | 3849 | 4594 | 4968 | 4719 | 5532 | 5051 | 4838 | 5160 | 4444 | 4664 | 4167 | 4260 |
| time over the response line (% of samples) | 15.95 | 12.1 | 20.42 | 15.3 | 15.95 | 12.32 | 17.39 | 13.74 | 21.88 | 17.57 | 24.92 | 19.76 | 17.52 | 13.57 |
| failed requests (%) | 4.941 | 4.671 | 8.461 | 6.876 | 4.713 | 4.702 | 5.302 | 5.542 | 6.546 | 6.601 | 9.813 | 8.39 | 6.355 | 5.618 |
| HPA replicas, mean | 9.583 | 14.53 | 9.632 | 14.32 | 9.581 | 14.49 | 9.594 | 14.49 | 9.595 | 14.38 | 9.587 | 14.14 | 9.605 | 14.41 |
| pods started | 5.457 | 11.37 | 5.286 | 12.06 | 5.429 | 11 | 5.343 | 11.49 | 5.114 | 11.09 | 5.4 | 11.69 | 5.543 | 12.46 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 179.2 | 180 | 180.8 | 180.6 | 179.5 | 180 | 179.8 | 180.2 | 181.7 | 181.1 | 181.3 | 180.6 | 180.5 | 179.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.2 | 180 | 180.8 | 180.6 | 179.5 | 180 | 179.8 | 180.2 | 181.7 | 181.1 | 181.3 | 180.6 | 180.5 | 179.6 |
| CPU used with Omni's own (cores), mean | 1.907 | 1.962 | 2 | 2.043 | 1.93 | 1.982 | 1.959 | 2.016 | 2.087 | 2.141 | 2.054 | 2.089 | 1.948 | 1.993 |
| host CPU busy, the real machine under kind (%) | 56.99 | 58.74 | 59.81 | 61.56 | 57.66 | 59.36 | 58.48 | 60.41 | 62.07 | 64.14 | 61.33 | 62.86 | 58.56 | 60.46 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1449 | 1292 | -10.9% | -400 to +85.38 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4848 | 4750 | -2.0% | -464.2 to +268.6 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 15.95 | 12.1 | -24.1% | -4.826 to -2.868 | GAIN |
| failed requests (%) | 4.941 | 4.671 | -5.5% | -0.5653 to +0.02487 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.583 | 14.53 | +51.6% | +4.631 to +5.257 | power given |
| pods started | 5.457 | 11.37 | +108.4% | +5.419 to +6.41 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.749e-16 to +5.809e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.2 | 180 | +0.4% | +0.4274 to +1.115 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.2 | 180 | +0.4% | +0.4274 to +1.115 | power given |
| CPU used with Omni's own (cores), mean | 1.907 | 1.962 | +2.9% | +0.04392 to +0.06754 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.99 | 58.74 | +3.1% | +1.444 to +2.062 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.976e+05 to +7.995e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.414e-05 to -9.392e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1158 | 1443 | +24.6% | +44.41 to +525.8 | LOSS |
| response time (ms), 99th percentile | 3849 | 4594 | +19.4% | +256.6 to +1233 | LOSS |
| time over the response line (% of samples) | 20.42 | 15.3 | -25.1% | -7.184 to -3.072 | GAIN |
| failed requests (%) | 8.461 | 6.876 | -18.7% | -2.846 to -0.3241 | GAIN |
| HPA replicas, mean | 9.632 | 14.32 | +48.7% | +4.349 to +5.025 | power given |
| pods started | 5.286 | 12.06 | +128.1% | +6.188 to +7.355 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.12e-16 to +4.12e-16 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 180.8 | 180.6 | -0.1% | -0.6674 to +0.2967 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.8 | 180.6 | -0.1% | -0.6674 to +0.2967 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2 | 2.043 | +2.2% | +0.02861 to +0.05795 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.81 | 61.56 | +2.9% | +1.405 to +2.099 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.622e+05 to +8.627e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.151e-05 to -8.146e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1470 | 1200 | -18.3% | -551.8 to +13.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4968 | 4719 | -5.0% | -644.8 to +146.8 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 15.95 | 12.32 | -22.8% | -4.63 to -2.634 | GAIN |
| failed requests (%) | 4.713 | 4.702 | -0.2% | -0.4202 to +0.3998 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.581 | 14.49 | +51.2% | +4.551 to +5.26 | power given |
| pods started | 5.429 | 11 | +102.6% | +5.077 to +6.066 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.881e-16 to +1.821e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.5 | 180 | +0.3% | +0.03451 to +0.9036 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.5 | 180 | +0.3% | +0.03451 to +0.9036 | power given |
| CPU used with Omni's own (cores), mean | 1.93 | 1.982 | +2.7% | +0.04172 to +0.06246 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.66 | 59.36 | +3.0% | +1.452 to +1.965 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1637 | 1246 | -23.9% | -587.9 to -194.5 | GAIN |
| response time (ms), 99th percentile | 5532 | 5051 | -8.7% | -977.3 to +14.39 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 17.39 | 13.74 | -21.0% | -4.627 to -2.685 | GAIN |
| failed requests (%) | 5.302 | 5.542 | +4.5% | -0.1218 to +0.6018 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.594 | 14.49 | +51.1% | +4.572 to +5.225 | power given |
| pods started | 5.343 | 11.49 | +115.0% | +5.751 to +6.535 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.538e-16 to +9.702e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.8 | 180.2 | +0.2% | -0.07394 to +0.9266 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.8 | 180.2 | +0.2% | -0.07394 to +0.9266 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.959 | 2.016 | +2.9% | +0.04549 to +0.06925 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.48 | 60.41 | +3.3% | +1.639 to +2.229 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1416 | 1500 | +5.9% | -97.14 to +265.2 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4838 | 5160 | +6.7% | -236.9 to +881.6 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 21.88 | 17.57 | -19.7% | -5.521 to -3.086 | GAIN |
| failed requests (%) | 6.546 | 6.601 | +0.8% | -0.3057 to +0.4163 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.595 | 14.38 | +49.8% | +4.327 to +5.238 | power given |
| pods started | 5.114 | 11.09 | +116.8% | +5.302 to +6.64 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.984e-16 to +2.954e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.7 | 181.1 | -0.3% | -0.9808 to -0.237 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.7 | 181.1 | -0.3% | -0.9808 to -0.237 | GAIN |
| CPU used with Omni's own (cores), mean | 2.087 | 2.141 | +2.6% | +0.03862 to +0.06838 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.07 | 64.14 | +3.3% | +1.69 to +2.46 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1635 | 1807 | +10.5% | -41.43 to +385.9 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4444 | 4664 | +4.9% | -131.6 to +571.1 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 24.92 | 19.76 | -20.7% | -6.969 to -3.341 | GAIN |
| failed requests (%) | 9.813 | 8.39 | -14.5% | -2.606 to -0.2388 | GAIN |
| HPA replicas, mean | 9.587 | 14.14 | +47.5% | +4.179 to +4.929 | power given |
| pods started | 5.4 | 11.69 | +116.4% | +5.736 to +6.836 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.377e-16 to +4.377e-16 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 181.3 | 180.6 | -0.4% | -1.047 to -0.3193 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.3 | 180.6 | -0.4% | -1.047 to -0.3193 | GAIN |
| CPU used with Omni's own (cores), mean | 2.054 | 2.089 | +1.7% | +0.02566 to +0.0437 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.33 | 62.86 | +2.5% | +1.229 to +1.831 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1067 | 1078 | +1.0% | -133.7 to +154.7 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4167 | 4260 | +2.2% | -208.8 to +394.7 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 17.52 | 13.57 | -22.6% | -5.735 to -2.172 | GAIN |
| failed requests (%) | 6.355 | 5.618 | -11.6% | -1.519 to +0.04439 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.605 | 14.41 | +50.0% | +4.484 to +5.119 | power given |
| pods started | 5.543 | 12.46 | +124.7% | +6.206 to +7.623 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.846e-16 to -2.334e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.5 | 179.6 | -0.5% | -1.321 to -0.4688 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.5 | 179.6 | -0.5% | -1.321 to -0.4688 | GAIN |
| CPU used with Omni's own (cores), mean | 1.948 | 1.993 | +2.3% | +0.03335 to +0.05637 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.56 | 60.46 | +3.2% | +1.592 to +2.213 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
