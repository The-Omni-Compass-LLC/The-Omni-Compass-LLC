# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on: native | The spine, the muscles every stack runs on: omni | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1568 | 1172 | 950.9 | 934.2 | 1656 | 1507 | 1074 | 982.7 | 1672 | 1568 | 1376 | 1524 |
| response time (ms), 99th percentile | 4838 | 4391 | 3679 | 3908 | 5213 | 5100 | 3535 | 3343 | 4777 | 4838 | 4806 | 5146 |
| time over the response line (% of samples) | 15.21 | 11.6 | 15 | 10.72 | 19.79 | 15.29 | 11.62 | 9.218 | 24.61 | 19.72 | 23.82 | 18.05 |
| failed requests (%) | 4.345 | 4.27 | 5.477 | 4.457 | 6.788 | 6.418 | 3.773 | 3.563 | 9.171 | 8.221 | 9.816 | 8.633 |
| HPA replicas, mean | 9.576 | 14.22 | 9.572 | 14.06 | 9.621 | 14.46 | 9.517 | 13.84 | 9.611 | 14.49 | 9.659 | 14.26 |
| pods started | 5.293 | 11.68 | 5.756 | 12.71 | 4.976 | 11 | 5.659 | 11.59 | 4.951 | 11.17 | 4.854 | 11.88 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 179 | 179.5 | 179.5 | 178.6 | 180.6 | 180.6 | 177.3 | 177.4 | 181.6 | 180.8 | 181.8 | 180.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179 | 179.5 | 179.5 | 178.6 | 180.6 | 180.6 | 177.3 | 177.4 | 181.6 | 180.8 | 181.8 | 180.9 |
| CPU used with Omni's own (cores), mean | 1.872 | 1.923 | 1.863 | 1.885 | 2.014 | 2.068 | 1.692 | 1.739 | 2.073 | 2.115 | 2.107 | 2.147 |
| host CPU busy, the real machine under kind (%) | 55.9 | 57.61 | 55.8 | 56.94 | 59.93 | 61.78 | 51.12 | 52.81 | 61.53 | 63.21 | 62.76 | 64.35 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.1 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1568 | 1172 | -25.2% | -663.5 to -128.3 | GAIN |
| response time (ms), 99th percentile | 4838 | 4391 | -9.2% | -954.3 to +60.21 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 15.21 | 11.6 | -23.7% | -4.586 to -2.625 | GAIN |
| failed requests (%) | 4.345 | 4.27 | -1.7% | -0.3608 to +0.2119 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.576 | 14.22 | +48.5% | +4.261 to +5.023 | power given |
| pods started | 5.293 | 11.68 | +120.7% | +5.907 to +6.873 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.49e-16 to +3.49e-16 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 179 | 179.5 | +0.3% | +0.05208 to +0.8992 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179 | 179.5 | +0.3% | +0.05208 to +0.8992 | power given |
| CPU used with Omni's own (cores), mean | 1.872 | 1.923 | +2.7% | +0.04119 to +0.06142 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.9 | 57.61 | +3.1% | +1.479 to +1.932 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.985e+05 to +8.004e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.425e-05 to -9.403e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 950.9 | 934.2 | -1.8% | -181.9 to +148.5 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 3679 | 3908 | +6.2% | -112.6 to +569.5 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 15 | 10.72 | -28.5% | -5.685 to -2.876 | GAIN |
| failed requests (%) | 5.477 | 4.457 | -18.6% | -1.618 to -0.4207 | GAIN |
| HPA replicas, mean | 9.572 | 14.06 | +46.9% | +4.194 to +4.789 | power given |
| pods started | 5.756 | 12.71 | +120.8% | +6.409 to +7.493 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.826e-16 to +7.6e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.5 | 178.6 | -0.5% | -1.305 to -0.438 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.5 | 178.6 | -0.5% | -1.305 to -0.438 | GAIN |
| CPU used with Omni's own (cores), mean | 1.863 | 1.885 | +1.2% | +0.005439 to +0.03819 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.8 | 56.94 | +2.0% | +0.6675 to +1.607 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.618e+05 to +8.624e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.148e-05 to -8.143e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1656 | 1507 | -9.0% | -411.5 to +114.4 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5213 | 5100 | -2.2% | -448 to +222.9 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 19.79 | 15.29 | -22.7% | -5.602 to -3.394 | GAIN |
| failed requests (%) | 6.788 | 6.418 | -5.4% | -1.041 to +0.3015 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.621 | 14.46 | +50.3% | +4.524 to +5.145 | power given |
| pods started | 4.976 | 11 | +121.1% | +5.471 to +6.578 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.244e-16 to +3.377e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.6 | 180.6 | +0.0% | -0.4111 to +0.5295 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.6 | 180.6 | +0.0% | -0.4111 to +0.5295 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.014 | 2.068 | +2.7% | +0.04342 to +0.06454 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.93 | 61.78 | +3.1% | +1.524 to +2.164 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1074 | 982.7 | -8.5% | -246.6 to +63.37 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 3535 | 3343 | -5.4% | -423.9 to +39.9 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 11.62 | 9.218 | -20.7% | -3.401 to -1.409 | GAIN |
| failed requests (%) | 3.773 | 3.563 | -5.6% | -0.405 to -0.01417 | GAIN |
| HPA replicas, mean | 9.517 | 13.84 | +45.5% | +3.906 to +4.749 | power given |
| pods started | 5.659 | 11.59 | +104.7% | +5.478 to +6.375 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.556e-16 to +4.289e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 177.3 | 177.4 | +0.1% | -0.2818 to +0.4833 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 177.3 | 177.4 | +0.1% | -0.2818 to +0.4833 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.692 | 1.739 | +2.8% | +0.03652 to +0.05727 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 51.12 | 52.81 | +3.3% | +1.399 to +1.972 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1672 | 1568 | -6.2% | -297.6 to +90.63 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4777 | 4838 | +1.3% | -440 to +561.7 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 24.61 | 19.72 | -19.9% | -6.365 to -3.426 | GAIN |
| failed requests (%) | 9.171 | 8.221 | -10.4% | -1.609 to -0.2914 | GAIN |
| HPA replicas, mean | 9.611 | 14.49 | +50.8% | +4.64 to +5.121 | power given |
| pods started | 4.951 | 11.17 | +125.6% | +5.662 to +6.778 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.516e-16 to +3.05e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.6 | 180.8 | -0.4% | -1.096 to -0.3995 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.6 | 180.8 | -0.4% | -1.096 to -0.3995 | GAIN |
| CPU used with Omni's own (cores), mean | 2.073 | 2.115 | +2.0% | +0.03226 to +0.05141 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.53 | 63.21 | +2.7% | +1.45 to +1.913 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1376 | 1524 | +10.8% | -109.4 to +405.4 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4806 | 5146 | +7.1% | -108.2 to +789.6 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 23.82 | 18.05 | -24.2% | -7.535 to -4.005 | GAIN |
| failed requests (%) | 9.816 | 8.633 | -12.1% | -2.005 to -0.3615 | GAIN |
| HPA replicas, mean | 9.659 | 14.26 | +47.6% | +4.313 to +4.884 | power given |
| pods started | 4.854 | 11.88 | +144.7% | +6.57 to +7.479 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -0.0004078 to +0.001207 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.8 | 180.9 | -0.5% | -1.341 to -0.5617 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.8 | 180.9 | -0.5% | -1.329 to -0.5574 | GAIN |
| CPU used with Omni's own (cores), mean | 2.107 | 2.147 | +1.9% | +0.02536 to +0.05391 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.76 | 64.35 | +2.5% | +1.196 to +2.001 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.1 | +0.1 | +0.08778 to +0.1122 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Distribution / Specialized

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
