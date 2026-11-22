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
| response time (ms), 95th percentile | 1028 | 1006 | 1219 | 1318 | 1246 | 1252 | 1148 | 1014 | 1872 | 1770 | 1831 | 1932 | 1260 | 1359 |
| response time (ms), 99th percentile | 3797 | 3610 | 4780 | 4862 | 4182 | 4084 | 4038 | 4036 | 5842 | 5286 | 4711 | 4981 | 4854 | 4845 |
| time over the response line (% of samples) | 12.43 | 9.284 | 21.39 | 16.6 | 14.38 | 10.88 | 12.3 | 9.006 | 26.82 | 20.78 | 25.11 | 20.5 | 20.32 | 16.69 |
| failed requests (%) | 3.815 | 3.534 | 8.58 | 7.678 | 4.264 | 3.996 | 3.261 | 3.043 | 8.488 | 8.101 | 9.797 | 8.617 | 7.973 | 7.498 |
| HPA replicas, mean | 9.52 | 14.19 | 9.651 | 14.43 | 9.547 | 14.08 | 9.535 | 13.96 | 9.628 | 14.63 | 9.599 | 14.46 | 9.643 | 14.27 |
| pods started | 5.771 | 11.69 | 5.057 | 12.46 | 5.543 | 11.66 | 5.629 | 11.6 | 4.971 | 11.31 | 5.029 | 11.31 | 5.171 | 12.6 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 5.996 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 177.7 | 178.4 | 181.7 | 180.8 | 178.5 | 178.9 | 178 | 178.4 | 183 | 182.5 | 181.6 | 180.9 | 181.5 | 180.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 177.7 | 178.4 | 181.7 | 180.8 | 178.5 | 178.9 | 178 | 178.4 | 183 | 182.5 | 181.6 | 180.9 | 181.4 | 180.8 |
| CPU used with Omni's own (cores), mean | 1.747 | 1.799 | 2.065 | 2.101 | 1.816 | 1.866 | 1.76 | 1.808 | 2.225 | 2.272 | 2.065 | 2.106 | 2.051 | 2.093 |
| host CPU busy, the real machine under kind (%) | 52.74 | 54.32 | 61.42 | 62.98 | 54.71 | 56.29 | 53 | 54.52 | 65.8 | 67.64 | 61.74 | 63.52 | 61.51 | 63.33 |
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
| response time (ms), 95th percentile | 1028 | 1006 | -2.1% | -213.2 to +169.8 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 3797 | 3610 | -4.9% | -534.5 to +160.8 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 12.43 | 9.284 | -25.3% | -4.166 to -2.128 | GAIN |
| failed requests (%) | 3.815 | 3.534 | -7.4% | -0.6369 to +0.07453 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.52 | 14.19 | +49.1% | +4.289 to +5.059 | power given |
| pods started | 5.771 | 11.69 | +102.5% | +5.398 to +6.43 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.203e-16 to +3.695e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 177.7 | 178.4 | +0.4% | +0.4225 to +1.072 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 177.7 | 178.4 | +0.4% | +0.4225 to +1.072 | power given |
| CPU used with Omni's own (cores), mean | 1.747 | 1.799 | +3.0% | +0.04006 to +0.06348 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 52.74 | 54.32 | +3.0% | +1.32 to +1.848 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.977e+05 to +8e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.42e-05 to -9.394e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1219 | 1318 | +8.1% | -96.31 to +293.5 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4780 | 4862 | +1.7% | -480.3 to +644.1 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 21.39 | 16.6 | -22.4% | -6.189 to -3.395 | GAIN |
| failed requests (%) | 8.58 | 7.678 | -10.5% | -1.579 to -0.2248 | GAIN |
| HPA replicas, mean | 9.651 | 14.43 | +49.5% | +4.524 to +5.032 | power given |
| pods started | 5.057 | 12.46 | +146.3% | +6.583 to +8.217 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.865e-16 to +1.267e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.7 | 180.8 | -0.5% | -1.211 to -0.4276 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.7 | 180.8 | -0.5% | -1.211 to -0.4276 | GAIN |
| CPU used with Omni's own (cores), mean | 2.065 | 2.101 | +1.8% | +0.02378 to +0.04907 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.42 | 62.98 | +2.5% | +1.231 to +1.893 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.622e+05 to +8.626e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.151e-05 to -8.146e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1246 | 1252 | +0.4% | -257 to +267.3 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4182 | 4084 | -2.3% | -466.2 to +270.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 14.38 | 10.88 | -24.3% | -4.578 to -2.421 | GAIN |
| failed requests (%) | 4.264 | 3.996 | -6.3% | -0.5615 to +0.02564 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.547 | 14.08 | +47.5% | +4.114 to +4.947 | power given |
| pods started | 5.543 | 11.66 | +110.3% | +5.7 to +6.529 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.821e-16 to +5.881e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.5 | 178.9 | +0.2% | -0.0535 to +0.7782 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.5 | 178.9 | +0.2% | -0.0535 to +0.7782 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.816 | 1.866 | +2.7% | +0.03895 to +0.05972 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 54.71 | 56.29 | +2.9% | +1.328 to +1.82 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1148 | 1014 | -11.7% | -353.4 to +85.66 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4038 | 4036 | -0.1% | -410.8 to +406.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 12.3 | 9.006 | -26.8% | -4.303 to -2.282 | GAIN |
| failed requests (%) | 3.261 | 3.043 | -6.7% | -0.5394 to +0.1036 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.535 | 13.96 | +46.4% | +3.963 to +4.889 | power given |
| pods started | 5.629 | 11.6 | +106.1% | +5.292 to +6.651 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.822e-16 to +5.345e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178 | 178.4 | +0.2% | -0.04369 to +0.7525 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178 | 178.4 | +0.2% | -0.04369 to +0.7525 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.76 | 1.808 | +2.7% | +0.03727 to +0.05782 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 53 | 54.52 | +2.9% | +1.247 to +1.789 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 5 (response time (ms), 99th percentile; time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1872 | 1770 | -5.4% | -336.4 to +132.5 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5842 | 5286 | -9.5% | -930.7 to -182.3 | GAIN |
| time over the response line (% of samples) | 26.82 | 20.78 | -22.5% | -7.661 to -4.41 | GAIN |
| failed requests (%) | 8.488 | 8.101 | -4.6% | -0.7966 to +0.02282 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.628 | 14.63 | +52.0% | +4.67 to +5.342 | power given |
| pods started | 4.971 | 11.31 | +127.6% | +5.661 to +7.024 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.095e-16 to +6.155e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183 | 182.5 | -0.3% | -0.9738 to -0.1142 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183 | 182.5 | -0.3% | -0.9738 to -0.1142 | GAIN |
| CPU used with Omni's own (cores), mean | 2.225 | 2.272 | +2.1% | +0.04124 to +0.05344 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.8 | 67.64 | +2.8% | +1.628 to +2.051 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1831 | 1932 | +5.5% | -139.4 to +342.3 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4711 | 4981 | +5.7% | -102.3 to +642.2 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 25.11 | 20.5 | -18.4% | -6.132 to -3.091 | GAIN |
| failed requests (%) | 9.797 | 8.617 | -12.0% | -2.026 to -0.3333 | GAIN |
| HPA replicas, mean | 9.599 | 14.46 | +50.6% | +4.591 to +5.132 | power given |
| pods started | 5.029 | 11.31 | +125.0% | +5.616 to +6.955 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.315e-16 to +3.285e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.6 | 180.9 | -0.4% | -1.097 to -0.3407 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.6 | 180.9 | -0.4% | -1.097 to -0.3407 | GAIN |
| CPU used with Omni's own (cores), mean | 2.065 | 2.106 | +2.0% | +0.02912 to +0.05362 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.74 | 63.52 | +2.9% | +1.517 to +2.052 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 3 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1260 | 1359 | +7.8% | -122.5 to +320 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4854 | 4845 | -0.2% | -470.7 to +454.6 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 20.32 | 16.69 | -17.9% | -5.374 to -1.88 | GAIN |
| failed requests (%) | 7.973 | 7.498 | -6.0% | -1.174 to +0.2244 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.643 | 14.27 | +48.0% | +4.273 to +4.988 | power given |
| pods started | 5.171 | 12.6 | +143.6% | +6.766 to +8.091 | power given |
| worker nodes in service, mean | 5.996 | 6 | +0.1% | -0.004121 to +0.01211 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.5 | 180.8 | -0.4% | -1.145 to -0.145 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.4 | 180.8 | -0.3% | -1.159 to +0.0292 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.051 | 2.093 | +2.0% | +0.02759 to +0.05565 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.51 | 63.33 | +3.0% | +1.463 to +2.18 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
