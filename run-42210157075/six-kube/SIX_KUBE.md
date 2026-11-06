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
| response time (ms), 95th percentile | 1448 | 1155 | 1087 | 1196 | 1514 | 1470 | 1586 | 1576 | 1640 | 1552 | 1209 | 1331 |
| response time (ms), 99th percentile | 4635 | 4463 | 4107 | 4405 | 4970 | 4936 | 4986 | 5182 | 4348 | 4314 | 4782 | 4571 |
| time over the response line (% of samples) | 15.66 | 11.72 | 19.24 | 15.31 | 17.72 | 13.26 | 17.83 | 13.74 | 23.09 | 18.84 | 22.47 | 17.72 |
| failed requests (%) | 4.619 | 4.568 | 7.989 | 7.273 | 5.638 | 5.31 | 6.064 | 5.509 | 8.696 | 7.545 | 9.607 | 8.509 |
| HPA replicas, mean | 9.584 | 14.1 | 9.609 | 14.18 | 9.604 | 14.25 | 9.604 | 14.25 | 9.578 | 14.22 | 9.643 | 13.76 |
| pods started | 5.293 | 11.29 | 5.415 | 12.66 | 5.073 | 11.02 | 5.024 | 11.24 | 5.244 | 11.37 | 4.976 | 12.51 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 179.2 | 179.6 | 180.3 | 180 | 179.8 | 180.2 | 179.4 | 180.2 | 180.9 | 180.3 | 181.4 | 180.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.2 | 179.6 | 180.3 | 180 | 179.8 | 180.2 | 179.4 | 180.2 | 180.9 | 180.3 | 181.4 | 180.5 |
| CPU used with Omni's own (cores), mean | 1.885 | 1.926 | 1.958 | 2.007 | 1.941 | 1.991 | 1.931 | 1.979 | 2.022 | 2.065 | 2.048 | 2.075 |
| host CPU busy, the real machine under kind (%) | 56.17 | 57.65 | 58.36 | 60.23 | 57.82 | 59.5 | 57.57 | 59.06 | 60.06 | 61.65 | 61.05 | 62.5 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.08537 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1448 | 1155 | -20.2% | -549.4 to -35.57 | GAIN |
| response time (ms), 99th percentile | 4635 | 4463 | -3.7% | -574.4 to +229.4 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 15.66 | 11.72 | -25.2% | -5.02 to -2.87 | GAIN |
| failed requests (%) | 4.619 | 4.568 | -1.1% | -0.4118 to +0.3101 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.584 | 14.1 | +47.1% | +4.078 to +4.948 | power given |
| pods started | 5.293 | 11.29 | +113.4% | +5.463 to +6.537 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.092e-16 to +7.592e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.2 | 179.6 | +0.2% | +0.04431 to +0.7704 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.2 | 179.6 | +0.2% | +0.04431 to +0.7704 | power given |
| CPU used with Omni's own (cores), mean | 1.885 | 1.926 | +2.2% | +0.02967 to +0.05267 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.17 | 57.65 | +2.6% | +1.171 to +1.79 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.977e+05 to +8.008e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.43e-05 to -9.393e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1087 | 1196 | +10.0% | -46.69 to +264.9 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4107 | 4405 | +7.2% | -154.1 to +749.6 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 19.24 | 15.31 | -20.4% | -5.297 to -2.554 | GAIN |
| failed requests (%) | 7.989 | 7.273 | -9.0% | -1.214 to -0.2174 | GAIN |
| HPA replicas, mean | 9.609 | 14.18 | +47.6% | +4.275 to +4.865 | power given |
| pods started | 5.415 | 12.66 | +133.8% | +6.722 to +7.766 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.524e-16 to +1.625e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.3 | 180 | -0.2% | -0.6852 to +0.1159 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.3 | 180 | -0.2% | -0.6852 to +0.1159 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.958 | 2.007 | +2.5% | +0.03803 to +0.05941 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.36 | 60.23 | +3.2% | +1.587 to +2.147 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.624e+05 to +8.628e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.152e-05 to -8.149e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1514 | 1470 | -2.9% | -336.1 to +248.7 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4970 | 4936 | -0.7% | -510.8 to +441.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 17.72 | 13.26 | -25.2% | -5.464 to -3.457 | GAIN |
| failed requests (%) | 5.638 | 5.31 | -5.8% | -0.8358 to +0.1801 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.604 | 14.25 | +48.4% | +4.257 to +5.043 | power given |
| pods started | 5.073 | 11.02 | +117.3% | +5.405 to +6.498 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.457e-16 to +2.724e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.8 | 180.2 | +0.2% | +0.01591 to +0.8005 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.8 | 180.2 | +0.2% | +0.01591 to +0.8005 | power given |
| CPU used with Omni's own (cores), mean | 1.941 | 1.991 | +2.6% | +0.03935 to +0.06051 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.82 | 59.5 | +2.9% | +1.388 to +1.987 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1586 | 1576 | -0.7% | -256.8 to +235.3 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4986 | 5182 | +3.9% | -148.9 to +540.4 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 17.83 | 13.74 | -22.9% | -5.084 to -3.087 | GAIN |
| failed requests (%) | 6.064 | 5.509 | -9.2% | -0.9446 to -0.1654 | GAIN |
| HPA replicas, mean | 9.604 | 14.25 | +48.4% | +4.289 to +5.007 | power given |
| pods started | 5.024 | 11.24 | +123.8% | +5.556 to +6.884 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.12e-16 to -1.845e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.4 | 180.2 | +0.5% | +0.4912 to +1.134 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.4 | 180.2 | +0.5% | +0.4912 to +1.134 | power given |
| CPU used with Omni's own (cores), mean | 1.931 | 1.979 | +2.5% | +0.0408 to +0.05617 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.57 | 59.06 | +2.6% | +1.269 to +1.717 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1640 | 1552 | -5.4% | -250.6 to +74.93 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4348 | 4314 | -0.8% | -501.3 to +433.2 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 23.09 | 18.84 | -18.4% | -5.635 to -2.868 | GAIN |
| failed requests (%) | 8.696 | 7.545 | -13.2% | -1.959 to -0.3425 | GAIN |
| HPA replicas, mean | 9.578 | 14.22 | +48.5% | +4.349 to +4.939 | power given |
| pods started | 5.244 | 11.37 | +116.7% | +5.548 to +6.696 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.213e-16 to +5.08e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.9 | 180.3 | -0.3% | -0.9392 to -0.2305 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.9 | 180.3 | -0.3% | -0.9392 to -0.2305 | GAIN |
| CPU used with Omni's own (cores), mean | 2.022 | 2.065 | +2.1% | +0.03349 to +0.05251 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.06 | 61.65 | +2.6% | +1.329 to +1.851 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1209 | 1331 | +10.1% | -33.29 to +277.5 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4782 | 4571 | -4.4% | -657.1 to +235.4 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 22.47 | 17.72 | -21.1% | -6.125 to -3.371 | GAIN |
| failed requests (%) | 9.607 | 8.509 | -11.4% | -1.836 to -0.3602 | GAIN |
| HPA replicas, mean | 9.643 | 13.76 | +42.7% | +3.725 to +4.511 | power given |
| pods started | 4.976 | 12.51 | +151.5% | +6.763 to +8.31 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.444e-16 to +3.782e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.4 | 180.5 | -0.5% | -1.234 to -0.403 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.4 | 180.5 | -0.5% | -1.234 to -0.403 | GAIN |
| CPU used with Omni's own (cores), mean | 2.048 | 2.075 | +1.3% | +0.01414 to +0.03921 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.05 | 62.5 | +2.4% | +1.101 to +1.792 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.08537 | +0.0854 | +0.07407 to +0.09666 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Distribution / Specialized

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
