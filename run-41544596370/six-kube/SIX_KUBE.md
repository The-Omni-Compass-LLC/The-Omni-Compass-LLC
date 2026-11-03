# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on: native | The spine, the muscles every stack runs on: omni | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1983 | 1652 | 1355 | 1581 | 1960 | 2331 | 1837 | 1418 | 2058 | 2032 | 1766 | 2047 | 1225 | 1315 |
| response time (ms), 99th percentile | 5793 | 6111 | 4456 | 4537 | 7031 | 7221 | 5367 | 5043 | 5837 | 5778 | 4749 | 5288 | 4072 | 4648 |
| time over the response line (% of samples) | 23.19 | 17.88 | 27.44 | 21.12 | 26.01 | 20.93 | 17.73 | 13.58 | 31.86 | 24.18 | 28.11 | 22.13 | 19.26 | 15.21 |
| failed requests (%) | 8.668 | 8.102 | 12.69 | 11.41 | 8.798 | 8.406 | 5.721 | 5.424 | 10.41 | 9.968 | 11.4 | 8.965 | 7.445 | 6.838 |
| HPA replicas, mean | 9.675 | 14.84 | 9.623 | 14.25 | 9.742 | 14.88 | 9.6 | 14.56 | 9.665 | 14.71 | 9.587 | 14.45 | 9.619 | 14.14 |
| pods started | 4.3 | 10.2 | 5.1 | 11.5 | 3.9 | 11.2 | 5.3 | 10.8 | 4.4 | 10.8 | 5.2 | 11.3 | 5.4 | 11.8 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 181.1 | 182.3 | 181.9 | 181.4 | 182.8 | 183.1 | 179.8 | 180.6 | 183.3 | 182.6 | 182.2 | 181.6 | 180.9 | 179.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.1 | 182.3 | 181.9 | 181.4 | 182.8 | 183.1 | 179.8 | 180.6 | 183.3 | 182.6 | 182.2 | 181.6 | 180.9 | 179.9 |
| CPU used with Omni's own (cores), mean | 2.114 | 2.178 | 2.095 | 2.154 | 2.259 | 2.313 | 1.952 | 1.997 | 2.275 | 2.321 | 2.139 | 2.185 | 1.984 | 2.021 |
| host CPU busy, the real machine under kind (%) | 62.66 | 64.36 | 62.78 | 64.54 | 66.78 | 68.53 | 58 | 59.52 | 67.12 | 68.79 | 63.47 | 65.37 | 59.44 | 61.12 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.09 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1983 | 1652 | -16.7% | -908.9 to +247.8 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5793 | 6111 | +5.5% | -870.1 to +1506 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 23.19 | 17.88 | -22.9% | -7.548 to -3.068 | GAIN |
| failed requests (%) | 8.668 | 8.102 | -6.5% | -1.519 to +0.3874 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.675 | 14.84 | +53.4% | +4.726 to +5.614 | power given |
| pods started | 4.3 | 10.2 | +137.2% | +4.663 to +7.137 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.492e-15 to +7.044e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.1 | 182.3 | +0.7% | +0.5837 to +1.897 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.1 | 182.3 | +0.7% | +0.5837 to +1.897 | power given |
| CPU used with Omni's own (cores), mean | 2.114 | 2.178 | +3.0% | +0.04775 to +0.07994 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.66 | 64.36 | +2.7% | +1.248 to +2.146 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.982e+05 to +8.005e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.427e-05 to -9.399e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1355 | 1581 | +16.7% | -271.2 to +723.1 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4456 | 4537 | +1.8% | -740 to +902 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 27.44 | 21.12 | -23.0% | -10.52 to -2.123 | GAIN |
| failed requests (%) | 12.69 | 11.41 | -10.1% | -3.31 to +0.7402 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.623 | 14.25 | +48.0% | +3.87 to +5.376 | power given |
| pods started | 5.1 | 11.5 | +125.5% | +5.175 to +7.625 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.484e-16 to +1.159e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.9 | 181.4 | -0.3% | -1.703 to +0.6769 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.9 | 181.4 | -0.3% | -1.703 to +0.6769 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.095 | 2.154 | +2.8% | +0.01167 to +0.1047 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.78 | 64.54 | +2.8% | +0.6069 to +2.915 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.618e+05 to +8.635e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.158e-05 to -8.143e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1960 | 2331 | +18.9% | -220.1 to +961.3 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 7031 | 7221 | +2.7% | -498.2 to +878.3 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 26.01 | 20.93 | -19.5% | -6.858 to -3.3 | GAIN |
| failed requests (%) | 8.798 | 8.406 | -4.4% | -1.357 to +0.5739 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.742 | 14.88 | +52.7% | +4.939 to +5.329 | power given |
| pods started | 3.9 | 11.2 | +187.2% | +6.471 to +8.129 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.246e-16 to +1.102e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.8 | 183.1 | +0.2% | -0.5854 to +1.26 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.8 | 183.1 | +0.2% | -0.5854 to +1.26 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.259 | 2.313 | +2.3% | +0.03327 to +0.07292 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.78 | 68.53 | +2.6% | +1.288 to +2.212 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.409e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.247e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1837 | 1418 | -22.8% | -706.9 to -131.4 | GAIN |
| response time (ms), 99th percentile | 5367 | 5043 | -6.0% | -1007 to +359.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 17.73 | 13.58 | -23.4% | -6.681 to -1.626 | GAIN |
| failed requests (%) | 5.721 | 5.424 | -5.2% | -1.34 to +0.7457 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.6 | 14.56 | +51.6% | +4.493 to +5.418 | power given |
| pods started | 5.3 | 10.8 | +103.8% | +4.273 to +6.727 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.159e-15 to +4.484e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.8 | 180.6 | +0.5% | +0.1781 to +1.491 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.8 | 180.6 | +0.5% | +0.1781 to +1.491 | power given |
| CPU used with Omni's own (cores), mean | 1.952 | 1.997 | +2.3% | +0.02534 to +0.06559 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58 | 59.52 | +2.6% | +0.9378 to +2.11 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2058 | 2032 | -1.3% | -342.8 to +289.1 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5837 | 5778 | -1.0% | -1047 to +929.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 31.86 | 24.18 | -24.1% | -10.65 to -4.698 | GAIN |
| failed requests (%) | 10.41 | 9.968 | -4.3% | -1.123 to +0.2348 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.665 | 14.71 | +52.2% | +4.419 to +5.675 | power given |
| pods started | 4.4 | 10.8 | +145.5% | +5.129 to +7.671 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.159e-15 to +4.484e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.3 | 182.6 | -0.4% | -1.627 to +0.1353 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.3 | 182.6 | -0.4% | -1.627 to +0.1353 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.275 | 2.321 | +2.0% | +0.03415 to +0.05766 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.12 | 68.79 | +2.5% | +1.361 to +1.969 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1766 | 2047 | +15.9% | -155.6 to +718.4 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4749 | 5288 | +11.3% | -619.3 to +1696 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 28.11 | 22.13 | -21.3% | -10.13 to -1.824 | GAIN |
| failed requests (%) | 11.4 | 8.965 | -21.3% | -4.705 to -0.1594 | GAIN |
| HPA replicas, mean | 9.587 | 14.45 | +50.7% | +4.209 to +5.514 | power given |
| pods started | 5.2 | 11.3 | +117.3% | +4.732 to +7.468 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.014e-15 to +6.588e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.2 | 181.6 | -0.4% | -1.537 to +0.1796 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.2 | 181.6 | -0.4% | -1.537 to +0.1796 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.139 | 2.185 | +2.2% | +0.02896 to +0.06401 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.47 | 65.37 | +3.0% | +1.318 to +2.482 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1225 | 1315 | +7.4% | -359.6 to +540.7 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4072 | 4648 | +14.2% | -313.6 to +1467 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 19.26 | 15.21 | -21.0% | -8.5 to +0.3913 | STEADY, inside the noise (cut) |
| failed requests (%) | 7.445 | 6.838 | -8.2% | -1.834 to +0.6189 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.619 | 14.14 | +47.0% | +3.788 to +5.262 | power given |
| pods started | 5.4 | 11.8 | +118.5% | +4.776 to +8.024 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.066e-15 to +7.108e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.9 | 179.9 | -0.5% | -1.969 to +0.03758 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.9 | 179.9 | -0.5% | -1.969 to +0.03758 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.984 | 2.021 | +1.8% | +0.00969 to +0.06364 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.44 | 61.12 | +2.8% | +1.19 to +2.183 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.09 | +0.09 | +0.06738 to +0.1126 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
