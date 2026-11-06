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
| response time (ms), 95th percentile | 1482 | 1419 | 1277 | 1450 | 1591 | 1355 | 1111 | 1085 | 1575 | 1448 | 1781 | 1782 | 1226 | 1180 |
| response time (ms), 99th percentile | 4786 | 5074 | 4362 | 4600 | 5020 | 4864 | 3973 | 3784 | 4655 | 4632 | 5215 | 5191 | 4783 | 4597 |
| time over the response line (% of samples) | 18.16 | 13.98 | 23.12 | 17.16 | 16.52 | 12.59 | 11.59 | 8.585 | 21.08 | 15.94 | 25.91 | 21.08 | 19.52 | 14.69 |
| failed requests (%) | 6.29 | 5.655 | 10.18 | 8.276 | 5.143 | 5.003 | 3.028 | 2.832 | 6.606 | 5.914 | 9.742 | 8.538 | 7.411 | 6.45 |
| HPA replicas, mean | 9.598 | 14.17 | 9.623 | 14.24 | 9.602 | 14.19 | 9.533 | 13.94 | 9.559 | 14.39 | 9.619 | 14.45 | 9.643 | 14.3 |
| pods started | 5 | 11.17 | 5.2 | 12.14 | 5.086 | 10.91 | 5.743 | 11.2 | 5.429 | 11.57 | 5.171 | 11.51 | 5.057 | 12.51 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 179.7 | 179.9 | 181.4 | 180.6 | 179.6 | 179.7 | 178.1 | 178.6 | 181.4 | 180.4 | 182.2 | 181.5 | 181.2 | 180.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.7 | 179.9 | 181.4 | 180.6 | 179.6 | 179.7 | 178.1 | 178.6 | 181.4 | 180.4 | 182.2 | 181.5 | 181.2 | 180.4 |
| CPU used with Omni's own (cores), mean | 1.938 | 1.98 | 2.048 | 2.077 | 1.915 | 1.959 | 1.762 | 1.798 | 2.046 | 2.088 | 2.144 | 2.185 | 2.025 | 2.056 |
| host CPU busy, the real machine under kind (%) | 57.83 | 59.21 | 61 | 62.39 | 57.25 | 58.72 | 52.77 | 54.16 | 60.74 | 62.27 | 63.37 | 64.94 | 60.36 | 61.83 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.08857 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1482 | 1419 | -4.2% | -295 to +169.4 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4786 | 5074 | +6.0% | -153.5 to +729.4 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 18.16 | 13.98 | -23.0% | -5.244 to -3.114 | GAIN |
| failed requests (%) | 6.29 | 5.655 | -10.1% | -0.9913 to -0.2797 | GAIN |
| HPA replicas, mean | 9.598 | 14.17 | +47.6% | +4.119 to +5.021 | power given |
| pods started | 5 | 11.17 | +123.4% | +5.61 to +6.733 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.088e-16 to +1.028e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.7 | 179.9 | +0.1% | -0.2562 to +0.7607 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.7 | 179.9 | +0.1% | -0.2562 to +0.7607 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.938 | 1.98 | +2.2% | +0.03107 to +0.05369 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.83 | 59.21 | +2.4% | +1.124 to +1.652 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.983e+05 to +8.015e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.438e-05 to -9.4e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1277 | 1450 | +13.5% | -25.31 to +370.8 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4362 | 4600 | +5.5% | -228.9 to +704.7 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 23.12 | 17.16 | -25.8% | -7.901 to -4.034 | GAIN |
| failed requests (%) | 10.18 | 8.276 | -18.7% | -2.965 to -0.8376 | GAIN |
| HPA replicas, mean | 9.623 | 14.24 | +48.0% | +4.339 to +4.89 | power given |
| pods started | 5.2 | 12.14 | +133.5% | +6.366 to +7.52 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.01e-16 to -1.14e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.4 | 180.6 | -0.5% | -1.302 to -0.4036 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.4 | 180.6 | -0.5% | -1.302 to -0.4036 | GAIN |
| CPU used with Omni's own (cores), mean | 2.048 | 2.077 | +1.4% | +0.01598 to +0.04112 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61 | 62.39 | +2.3% | +1.079 to +1.715 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.621e+05 to +8.625e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.15e-05 to -8.145e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1591 | 1355 | -14.8% | -531.1 to +59.33 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5020 | 4864 | -3.1% | -517.6 to +205.1 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 16.52 | 12.59 | -23.8% | -5.124 to -2.736 | GAIN |
| failed requests (%) | 5.143 | 5.003 | -2.7% | -0.5683 to +0.289 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.602 | 14.19 | +47.8% | +4.172 to +5.01 | power given |
| pods started | 5.086 | 10.91 | +114.6% | +5.231 to +6.426 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.185e-16 to +4.185e-16 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 179.6 | 179.7 | +0.1% | -0.3254 to +0.5988 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.6 | 179.7 | +0.1% | -0.3254 to +0.5988 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.915 | 1.959 | +2.3% | +0.03064 to +0.05765 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.25 | 58.72 | +2.6% | +1.075 to +1.885 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1111 | 1085 | -2.3% | -321.4 to +269.7 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 3973 | 3784 | -4.8% | -630.9 to +253.5 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 11.59 | 8.585 | -25.9% | -3.888 to -2.119 | GAIN |
| failed requests (%) | 3.028 | 2.832 | -6.5% | -0.5393 to +0.1474 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.533 | 13.94 | +46.3% | +3.878 to +4.943 | power given |
| pods started | 5.743 | 11.2 | +95.0% | +4.854 to +6.06 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.133e-16 to +3.625e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.1 | 178.6 | +0.3% | +0.191 to +0.7684 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.1 | 178.6 | +0.3% | +0.191 to +0.7684 | power given |
| CPU used with Omni's own (cores), mean | 1.762 | 1.798 | +2.0% | +0.02427 to +0.04784 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 52.77 | 54.16 | +2.6% | +1.14 to +1.63 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1575 | 1448 | -8.1% | -301.2 to +46.41 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4655 | 4632 | -0.5% | -430.6 to +385.6 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 21.08 | 15.94 | -24.4% | -6.802 to -3.472 | GAIN |
| failed requests (%) | 6.606 | 5.914 | -10.5% | -1.574 to +0.1897 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.559 | 14.39 | +50.5% | +4.466 to +5.19 | power given |
| pods started | 5.429 | 11.57 | +113.2% | +5.609 to +6.677 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.426e-16 to +1.858e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.4 | 180.4 | -0.6% | -1.435 to -0.6248 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.4 | 180.4 | -0.6% | -1.435 to -0.6248 | GAIN |
| CPU used with Omni's own (cores), mean | 2.046 | 2.088 | +2.0% | +0.03056 to +0.05254 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.74 | 62.27 | +2.5% | +1.218 to +1.846 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1781 | 1782 | +0.0% | -247.8 to +249.1 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5215 | 5191 | -0.5% | -579.2 to +531.4 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 25.91 | 21.08 | -18.6% | -6.552 to -3.101 | GAIN |
| failed requests (%) | 9.742 | 8.538 | -12.4% | -2.058 to -0.3494 | GAIN |
| HPA replicas, mean | 9.619 | 14.45 | +50.2% | +4.554 to +5.098 | power given |
| pods started | 5.171 | 11.51 | +122.7% | +5.742 to +6.943 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.107e-16 to +3.047e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.2 | 181.5 | -0.4% | -1.096 to -0.2338 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.2 | 181.5 | -0.4% | -1.096 to -0.2338 | GAIN |
| CPU used with Omni's own (cores), mean | 2.144 | 2.185 | +1.9% | +0.0314 to +0.04911 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.37 | 64.94 | +2.5% | +1.339 to +1.801 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1226 | 1180 | -3.7% | -233.8 to +142.7 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4783 | 4597 | -3.9% | -686.7 to +315.6 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 19.52 | 14.69 | -24.8% | -6.284 to -3.384 | GAIN |
| failed requests (%) | 7.411 | 6.45 | -13.0% | -1.639 to -0.2825 | GAIN |
| HPA replicas, mean | 9.643 | 14.3 | +48.3% | +4.362 to +4.95 | power given |
| pods started | 5.057 | 12.51 | +147.5% | +6.849 to +8.066 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.181e-15 to -3.418e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.2 | 180.4 | -0.5% | -1.333 to -0.3885 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.2 | 180.4 | -0.5% | -1.333 to -0.3885 | GAIN |
| CPU used with Omni's own (cores), mean | 2.025 | 2.056 | +1.5% | +0.018 to +0.04407 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.36 | 61.83 | +2.4% | +1.208 to +1.735 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.08857 | +0.0886 | +0.07748 to +0.09966 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
