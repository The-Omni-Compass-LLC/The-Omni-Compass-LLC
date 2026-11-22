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
| response time (ms), 95th percentile | 1781 | 1339 | 1137 | 1191 | 1245 | 1021 | 1422 | 1319 | 1666 | 1748 | 1597 | 1816 | 1354 | 1464 |
| response time (ms), 99th percentile | 5521 | 5455 | 4525 | 4582 | 4262 | 3841 | 4664 | 4661 | 5198 | 5591 | 4654 | 5168 | 4945 | 5262 |
| time over the response line (% of samples) | 18.31 | 13.24 | 18.97 | 14.78 | 12.71 | 9.345 | 16.28 | 12.33 | 24.81 | 19.52 | 24.13 | 20.61 | 23.21 | 17.79 |
| failed requests (%) | 5.739 | 5.22 | 7.431 | 6.528 | 3.577 | 3.344 | 5.204 | 4.876 | 7.826 | 7.433 | 9.175 | 8.126 | 9.355 | 7.969 |
| HPA replicas, mean | 9.619 | 14.75 | 9.631 | 14.5 | 9.545 | 14.17 | 9.591 | 14.32 | 9.613 | 14.56 | 9.602 | 14.42 | 9.676 | 14.42 |
| pods started | 5.086 | 11.43 | 5.4 | 12.09 | 5.6 | 11.69 | 5.257 | 11.29 | 5.029 | 11.2 | 4.971 | 11.26 | 4.886 | 12.26 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 180.4 | 181.1 | 181 | 180.2 | 178.2 | 178.8 | 179.3 | 179.6 | 182.5 | 181.7 | 181.5 | 180.9 | 182.4 | 181.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.4 | 181.1 | 181 | 180.2 | 178.2 | 178.8 | 179.3 | 179.6 | 182.5 | 181.7 | 181.5 | 180.9 | 182.4 | 181.3 |
| CPU used with Omni's own (cores), mean | 2.005 | 2.053 | 2.009 | 2.048 | 1.8 | 1.844 | 1.897 | 1.939 | 2.167 | 2.213 | 2.059 | 2.105 | 2.122 | 2.158 |
| host CPU busy, the real machine under kind (%) | 59.72 | 61.49 | 59.91 | 61.63 | 54.1 | 55.58 | 56.75 | 58.31 | 64.21 | 66.08 | 61.22 | 63 | 63.48 | 64.84 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0.002857 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1781 | 1339 | -24.8% | -682.5 to -202.4 | GAIN |
| response time (ms), 99th percentile | 5521 | 5455 | -1.2% | -452.7 to +319.8 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 18.31 | 13.24 | -27.7% | -6.656 to -3.499 | GAIN |
| failed requests (%) | 5.739 | 5.22 | -9.1% | -1.477 to +0.4379 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.619 | 14.75 | +53.3% | +4.979 to +5.282 | power given |
| pods started | 5.086 | 11.43 | +124.7% | +5.935 to +6.75 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.561e-16 to +1.486e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.4 | 181.1 | +0.4% | +0.1972 to +1.083 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.4 | 181.1 | +0.4% | +0.1972 to +1.083 | power given |
| CPU used with Omni's own (cores), mean | 2.005 | 2.053 | +2.4% | +0.03485 to +0.06244 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.72 | 61.49 | +3.0% | +1.505 to +2.043 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.981e+05 to +8.001e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.421e-05 to -9.398e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1137 | 1191 | +4.8% | -148.9 to +257.7 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4525 | 4582 | +1.3% | -383.7 to +497.2 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 18.97 | 14.78 | -22.1% | -5.926 to -2.457 | GAIN |
| failed requests (%) | 7.431 | 6.528 | -12.2% | -1.957 to +0.1492 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.631 | 14.5 | +50.6% | +4.647 to +5.095 | power given |
| pods started | 5.4 | 12.09 | +123.8% | +6.209 to +7.163 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.316e-16 to +4.839e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 180.2 | -0.4% | -1.206 to -0.2721 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181 | 180.2 | -0.4% | -1.206 to -0.2721 | GAIN |
| CPU used with Omni's own (cores), mean | 2.009 | 2.048 | +1.9% | +0.02812 to +0.05 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.91 | 61.63 | +2.9% | +1.455 to +1.981 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.622e+05 to +8.626e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.15e-05 to -8.146e-05 | power given |
| organism behind its window (s) | 0.002857 | 0 | -100.0% | -0.008663 to +0.002949 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1245 | 1021 | -18.0% | -388.8 to -59.01 | GAIN |
| response time (ms), 99th percentile | 4262 | 3841 | -9.9% | -811.2 to -31.61 | GAIN |
| time over the response line (% of samples) | 12.71 | 9.345 | -26.5% | -4.348 to -2.391 | GAIN |
| failed requests (%) | 3.577 | 3.344 | -6.5% | -0.5336 to +0.0687 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.545 | 14.17 | +48.4% | +4.233 to +5.011 | power given |
| pods started | 5.6 | 11.69 | +108.7% | +5.477 to +6.694 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.205e-16 to +1.13e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.2 | 178.8 | +0.3% | +0.2317 to +0.9387 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.2 | 178.8 | +0.3% | +0.2317 to +0.9387 | power given |
| CPU used with Omni's own (cores), mean | 1.8 | 1.844 | +2.4% | +0.02775 to +0.05868 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 54.1 | 55.58 | +2.7% | +1.117 to +1.839 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1422 | 1319 | -7.2% | -323.7 to +117.8 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4664 | 4661 | -0.1% | -464.2 to +457.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 16.28 | 12.33 | -24.3% | -4.998 to -2.896 | GAIN |
| failed requests (%) | 5.204 | 4.876 | -6.3% | -0.7227 to +0.06578 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.591 | 14.32 | +49.3% | +4.37 to +5.094 | power given |
| pods started | 5.257 | 11.29 | +114.7% | +5.467 to +6.59 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.607e-16 to +2.054e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.3 | 179.6 | +0.1% | -0.119 to +0.6433 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.3 | 179.6 | +0.1% | -0.119 to +0.6433 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.897 | 1.939 | +2.2% | +0.03264 to +0.05222 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.75 | 58.31 | +2.7% | +1.325 to +1.78 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1666 | 1748 | +4.9% | -163.9 to +328.1 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5198 | 5591 | +7.6% | -29.36 to +816.2 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 24.81 | 19.52 | -21.3% | -6.677 to -3.907 | GAIN |
| failed requests (%) | 7.826 | 7.433 | -5.0% | -0.8126 to +0.02667 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.613 | 14.56 | +51.4% | +4.648 to +5.239 | power given |
| pods started | 5.029 | 11.2 | +122.7% | +5.61 to +6.733 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.453e-16 to -1.603e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.5 | 181.7 | -0.4% | -1.24 to -0.2833 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.5 | 181.7 | -0.4% | -1.24 to -0.2833 | GAIN |
| CPU used with Omni's own (cores), mean | 2.167 | 2.213 | +2.1% | +0.03122 to +0.06089 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.21 | 66.08 | +2.9% | +1.476 to +2.261 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 0

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1597 | 1816 | +13.7% | +5.042 to +433.3 | LOSS |
| response time (ms), 99th percentile | 4654 | 5168 | +11.1% | +35.96 to +992.8 | LOSS |
| time over the response line (% of samples) | 24.13 | 20.61 | -14.6% | -5.195 to -1.846 | GAIN |
| failed requests (%) | 9.175 | 8.126 | -11.4% | -1.887 to -0.2108 | GAIN |
| HPA replicas, mean | 9.602 | 14.42 | +50.2% | +4.498 to +5.136 | power given |
| pods started | 4.971 | 11.26 | +126.4% | +5.768 to +6.803 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.881e-16 to +3.866e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.5 | 180.9 | -0.4% | -1.06 to -0.2515 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.5 | 180.9 | -0.4% | -1.06 to -0.2515 | GAIN |
| CPU used with Omni's own (cores), mean | 2.059 | 2.105 | +2.2% | +0.03388 to +0.05687 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.22 | 63 | +2.9% | +1.411 to +2.149 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1354 | 1464 | +8.1% | -125.6 to +346.2 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4945 | 5262 | +6.4% | -287.5 to +922.2 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 23.21 | 17.79 | -23.4% | -7.11 to -3.745 | GAIN |
| failed requests (%) | 9.355 | 7.969 | -14.8% | -2.178 to -0.5946 | GAIN |
| HPA replicas, mean | 9.676 | 14.42 | +49.1% | +4.487 to +5.008 | power given |
| pods started | 4.886 | 12.26 | +150.9% | +6.71 to +8.033 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.084e-15 to -2.861e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.4 | 181.3 | -0.6% | -1.497 to -0.6263 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.4 | 181.3 | -0.6% | -1.497 to -0.6263 | GAIN |
| CPU used with Omni's own (cores), mean | 2.122 | 2.158 | +1.7% | +0.02252 to +0.04949 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.48 | 64.84 | +2.1% | +0.666 to +2.058 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
