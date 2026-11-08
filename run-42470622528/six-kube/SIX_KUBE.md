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
| response time (ms), 95th percentile | 1704 | 1392 | 1171 | 1013 | 1400 | 1387 | 1427 | 1318 | 1658 | 1581 | 1293 | 1422 | 1159 | 1139 |
| response time (ms), 99th percentile | 5110 | 4956 | 4370 | 4155 | 4599 | 4457 | 5079 | 5075 | 4644 | 4655 | 4686 | 4606 | 4236 | 4529 |
| time over the response line (% of samples) | 18.6 | 14.23 | 17.58 | 12.98 | 16.73 | 12.7 | 15.77 | 12.11 | 24.23 | 19.12 | 20.12 | 16.63 | 18.53 | 14.86 |
| failed requests (%) | 6.192 | 6.019 | 6.437 | 5.699 | 5.535 | 5.004 | 4.601 | 4.369 | 7.963 | 7.724 | 6.915 | 6.241 | 6.877 | 6.363 |
| HPA replicas, mean | 9.589 | 14.26 | 9.606 | 14.26 | 9.58 | 14.22 | 9.596 | 14.4 | 9.588 | 14.06 | 9.585 | 14.36 | 9.614 | 14.08 |
| pods started | 5.171 | 10.74 | 5.412 | 12.74 | 5.294 | 11.24 | 5.257 | 11.43 | 5.029 | 10.74 | 5.314 | 11.77 | 5.457 | 12.49 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 179.7 | 180.5 | 180.3 | 180.1 | 179.3 | 180 | 179.3 | 180.1 | 181.4 | 180.9 | 181.2 | 181 | 181.1 | 180.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.7 | 180.5 | 180.3 | 180.1 | 179.3 | 180 | 179.3 | 180.1 | 181.4 | 180.9 | 181.2 | 181 | 181.1 | 180.4 |
| CPU used with Omni's own (cores), mean | 1.952 | 2.011 | 1.955 | 1.981 | 1.903 | 1.953 | 1.921 | 1.966 | 2.079 | 2.119 | 2.035 | 2.083 | 2.002 | 2.039 |
| host CPU busy, the real machine under kind (%) | 58.3 | 59.97 | 58.04 | 59.35 | 56.77 | 58.32 | 57.1 | 58.66 | 61.55 | 63.13 | 60.41 | 62 | 59.65 | 61.35 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.09429 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1704 | 1392 | -18.4% | -579.9 to -45.62 | GAIN |
| response time (ms), 99th percentile | 5110 | 4956 | -3.0% | -584.2 to +276.3 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 18.6 | 14.23 | -23.5% | -5.578 to -3.171 | GAIN |
| failed requests (%) | 6.192 | 6.019 | -2.8% | -0.5321 to +0.1864 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.589 | 14.26 | +48.7% | +4.234 to +5.105 | power given |
| pods started | 5.171 | 10.74 | +107.7% | +4.941 to +6.202 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.562e-16 to +3.532e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.7 | 180.5 | +0.5% | +0.4383 to +1.278 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.7 | 180.5 | +0.5% | +0.4383 to +1.278 | power given |
| CPU used with Omni's own (cores), mean | 1.952 | 2.011 | +3.0% | +0.04794 to +0.07012 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.3 | 59.97 | +2.9% | +1.366 to +1.978 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.986e+05 to +7.997e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.416e-05 to -9.404e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

34 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1171 | 1021 | -12.8% | -325.4 to +25.73 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4370 | 4121 | -5.7% | -596 to +97.51 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 17.58 | 13.11 | -25.4% | -6.522 to -2.421 | GAIN |
| failed requests (%) | 6.437 | 5.797 | -9.9% | -1.395 to +0.1156 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.606 | 14.24 | +48.3% | +4.296 to +4.978 | power given |
| pods started | 5.412 | 12.74 | +135.3% | +6.769 to +7.878 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.824e-16 to -1.308e-18 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.3 | 180.1 | -0.1% | -0.6712 to +0.2987 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.3 | 180.1 | -0.1% | -0.6712 to +0.2987 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.955 | 1.979 | +1.2% | +0.009776 to +0.03819 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.04 | 59.31 | +2.2% | +0.9005 to +1.64 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.619e+05 to +8.624e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.148e-05 to -8.144e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

34 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1400 | 1387 | -0.9% | -259.7 to +233.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4599 | 4457 | -3.1% | -575.7 to +292.4 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 16.73 | 12.7 | -24.1% | -5.154 to -2.907 | GAIN |
| failed requests (%) | 5.535 | 5.004 | -9.6% | -1.002 to -0.06144 | GAIN |
| HPA replicas, mean | 9.58 | 14.22 | +48.5% | +4.212 to +5.073 | power given |
| pods started | 5.294 | 11.24 | +112.2% | +5.207 to +6.675 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.393e-16 to +2.825e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.3 | 180 | +0.4% | +0.2745 to +1.043 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.3 | 180 | +0.4% | +0.2745 to +1.043 | power given |
| CPU used with Omni's own (cores), mean | 1.903 | 1.953 | +2.6% | +0.03982 to +0.06032 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.77 | 58.32 | +2.7% | +1.366 to +1.734 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1427 | 1318 | -7.6% | -419.5 to +202.8 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5079 | 5075 | -0.1% | -445.1 to +435.8 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 15.77 | 12.11 | -23.2% | -4.617 to -2.705 | GAIN |
| failed requests (%) | 4.601 | 4.369 | -5.0% | -0.6087 to +0.1446 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.596 | 14.4 | +50.1% | +4.43 to +5.177 | power given |
| pods started | 5.257 | 11.43 | +117.4% | +5.661 to +6.681 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.742e-16 to +1.286e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.3 | 180.1 | +0.4% | +0.4136 to +1.179 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.3 | 180.1 | +0.4% | +0.4136 to +1.179 | power given |
| CPU used with Omni's own (cores), mean | 1.921 | 1.966 | +2.4% | +0.03525 to +0.05506 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.1 | 58.66 | +2.7% | +1.289 to +1.823 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1658 | 1581 | -4.6% | -243.6 to +91.11 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4644 | 4655 | +0.2% | -451.1 to +473.3 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 24.23 | 19.12 | -21.1% | -6.511 to -3.704 | GAIN |
| failed requests (%) | 7.963 | 7.724 | -3.0% | -0.6301 to +0.1528 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.588 | 14.06 | +46.7% | +3.928 to +5.02 | power given |
| pods started | 5.029 | 10.74 | +113.6% | +4.926 to +6.503 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.951e-16 to +1.891e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.4 | 180.9 | -0.3% | -0.8793 to -0.08555 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.4 | 180.9 | -0.3% | -0.8793 to -0.08555 | GAIN |
| CPU used with Omni's own (cores), mean | 2.079 | 2.119 | +1.9% | +0.02981 to +0.05106 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.55 | 63.13 | +2.6% | +1.232 to +1.937 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1293 | 1422 | +9.9% | -61.93 to +318.8 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4686 | 4606 | -1.7% | -533.6 to +373.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 20.12 | 16.63 | -17.3% | -4.63 to -2.338 | GAIN |
| failed requests (%) | 6.915 | 6.241 | -9.8% | -1.474 to +0.1253 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.585 | 14.36 | +49.8% | +4.48 to +5.067 | power given |
| pods started | 5.314 | 11.77 | +121.5% | +6.12 to +6.794 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.345e-16 to +3.822e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.2 | 181 | -0.1% | -0.659 to +0.1288 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.2 | 181 | -0.1% | -0.659 to +0.1288 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.035 | 2.083 | +2.4% | +0.03692 to +0.05888 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.41 | 62 | +2.6% | +1.328 to +1.855 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1159 | 1139 | -1.8% | -225.5 to +183.9 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4236 | 4529 | +6.9% | -297.1 to +883.3 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 18.53 | 14.86 | -19.8% | -4.874 to -2.462 | GAIN |
| failed requests (%) | 6.877 | 6.363 | -7.5% | -1.06 to +0.03156 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.614 | 14.08 | +46.5% | +4.119 to +4.82 | power given |
| pods started | 5.457 | 12.49 | +128.8% | +6.492 to +7.565 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.026e-15 to -1.92e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.1 | 180.4 | -0.4% | -1.071 to -0.2174 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.1 | 180.4 | -0.4% | -1.071 to -0.2174 | GAIN |
| CPU used with Omni's own (cores), mean | 2.002 | 2.039 | +1.9% | +0.02539 to +0.04878 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.65 | 61.35 | +2.9% | +1.378 to +2.029 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.09429 | +0.0943 | +0.08267 to +0.1059 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
