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
| response time (ms), 95th percentile | 1701 | 1234 | 1290 | 1724 | 1722 | 1364 | 1204 | 989.7 | 1911 | 1948 | 1979 | 2596 | 1306 | 1447 |
| response time (ms), 99th percentile | 5156 | 4528 | 4889 | 5401 | 5847 | 5731 | 4155 | 4100 | 5968 | 5833 | 5178 | 5633 | 4689 | 4783 |
| time over the response line (% of samples) | 15.83 | 12.13 | 21.91 | 18.46 | 21.64 | 16.37 | 12.62 | 9.622 | 29.3 | 23.77 | 31.33 | 26.86 | 23.61 | 18.02 |
| failed requests (%) | 4.524 | 4.548 | 8.679 | 8.047 | 7.712 | 7.566 | 3.873 | 3.405 | 9.565 | 9.561 | 12.85 | 12.02 | 9.284 | 7.991 |
| HPA replicas, mean | 9.549 | 14.22 | 9.645 | 14.41 | 9.617 | 14.72 | 9.529 | 13.93 | 9.641 | 14.8 | 9.644 | 14.38 | 9.679 | 14.49 |
| pods started | 5.8 | 11.67 | 5.4 | 11.87 | 5.333 | 10.93 | 5.733 | 11.73 | 4.867 | 11.27 | 4.667 | 11.13 | 4.733 | 12.13 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 179 | 178.9 | 182.5 | 181.9 | 181.1 | 180.9 | 177.9 | 178.5 | 183.8 | 183 | 182.5 | 182.1 | 182 | 181.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179 | 178.9 | 182.5 | 181.9 | 181.1 | 180.9 | 177.9 | 178.5 | 183.8 | 183 | 182.5 | 182.1 | 182 | 181.4 |
| CPU used with Omni's own (cores), mean | 1.87 | 1.914 | 2.131 | 2.178 | 2.08 | 2.141 | 1.773 | 1.823 | 2.266 | 2.318 | 2.178 | 2.231 | 2.122 | 2.155 |
| host CPU busy, the real machine under kind (%) | 56.13 | 57.74 | 63.35 | 65.21 | 62.31 | 64.01 | 53.28 | 55.02 | 67.28 | 69.16 | 65 | 66.97 | 63.43 | 64.83 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 3 (response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

15 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1701 | 1234 | -27.5% | -939.4 to +4.471 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5156 | 4528 | -12.2% | -1105 to -152.1 | GAIN |
| time over the response line (% of samples) | 15.83 | 12.13 | -23.4% | -5.062 to -2.338 | GAIN |
| failed requests (%) | 4.524 | 4.548 | +0.5% | -0.6403 to +0.6884 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.549 | 14.22 | +48.9% | +3.958 to +5.377 | power given |
| pods started | 5.8 | 11.67 | +101.1% | +5.06 to +6.674 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.313e-16 to +5.128e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179 | 178.9 | -0.0% | -0.7597 to +0.641 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179 | 178.9 | -0.0% | -0.7597 to +0.641 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.87 | 1.914 | +2.3% | +0.0206 to +0.06666 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.13 | 57.74 | +2.9% | +0.9316 to +2.28 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.956e+05 to +8.014e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.437e-05 to -9.369e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

15 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1290 | 1724 | +33.6% | -9.481 to +877 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4889 | 5401 | +10.5% | -182 to +1206 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 21.91 | 18.46 | -15.7% | -6.274 to -0.6248 | GAIN |
| failed requests (%) | 8.679 | 8.047 | -7.3% | -2.118 to +0.8537 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.645 | 14.41 | +49.4% | +4.205 to +5.324 | power given |
| pods started | 5.4 | 11.87 | +119.8% | +5.145 to +7.788 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.373e-16 to +2.268e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.5 | 181.9 | -0.3% | -1.207 to -0.01198 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.5 | 181.9 | -0.3% | -1.207 to -0.01198 | GAIN |
| CPU used with Omni's own (cores), mean | 2.131 | 2.178 | +2.2% | +0.02354 to +0.07072 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.35 | 65.21 | +2.9% | +1.267 to +2.445 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.62e+05 to +8.629e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.153e-05 to -8.145e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

15 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1722 | 1364 | -20.8% | -654.8 to -61.33 | GAIN |
| response time (ms), 99th percentile | 5847 | 5731 | -2.0% | -1081 to +849 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 21.64 | 16.37 | -24.4% | -7.264 to -3.275 | GAIN |
| failed requests (%) | 7.712 | 7.566 | -1.9% | -0.9464 to +0.6542 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.617 | 14.72 | +53.0% | +4.697 to +5.501 | power given |
| pods started | 5.333 | 10.93 | +105.0% | +5.141 to +6.059 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.259e-16 to +5.259e-16 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 181.1 | 180.9 | -0.1% | -0.991 to +0.5067 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.1 | 180.9 | -0.1% | -0.991 to +0.5067 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.08 | 2.141 | +2.9% | +0.04676 to +0.07397 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.31 | 64.01 | +2.7% | +1.313 to +2.1 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.247e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

15 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1204 | 989.7 | -17.8% | -563.6 to +134.4 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4155 | 4100 | -1.3% | -396.4 to +286.4 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 12.62 | 9.622 | -23.7% | -4.639 to -1.354 | GAIN |
| failed requests (%) | 3.873 | 3.405 | -12.1% | -1.185 to +0.25 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.529 | 13.93 | +46.2% | +3.68 to +5.125 | power given |
| pods started | 5.733 | 11.73 | +104.7% | +5.408 to +6.592 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.446e-16 to +7.999e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 177.9 | 178.5 | +0.3% | +0.09484 to +1.129 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 177.9 | 178.5 | +0.3% | +0.09484 to +1.129 | power given |
| CPU used with Omni's own (cores), mean | 1.773 | 1.823 | +2.8% | +0.03033 to +0.06831 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 53.28 | 55.02 | +3.3% | +1.157 to +2.324 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

15 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1911 | 1948 | +1.9% | -340.6 to +413.5 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5968 | 5833 | -2.3% | -632.1 to +362 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 29.3 | 23.77 | -18.9% | -7.632 to -3.419 | GAIN |
| failed requests (%) | 9.565 | 9.561 | -0.0% | -0.3049 to +0.2967 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.641 | 14.8 | +53.5% | +4.891 to +5.434 | power given |
| pods started | 4.867 | 11.27 | +131.5% | +5.22 to +7.58 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.243e-15 to +4.142e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 183 | -0.4% | -1.455 to -0.1462 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 183 | -0.4% | -1.455 to -0.1462 | GAIN |
| CPU used with Omni's own (cores), mean | 2.266 | 2.318 | +2.3% | +0.04283 to +0.06204 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.28 | 69.16 | +2.8% | +1.562 to +2.188 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

15 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1979 | 2596 | +31.2% | +76.33 to +1158 | LOSS |
| response time (ms), 99th percentile | 5178 | 5633 | +8.8% | -594.1 to +1505 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 31.33 | 26.86 | -14.3% | -8.587 to -0.3599 | GAIN |
| failed requests (%) | 12.85 | 12.02 | -6.5% | -4.452 to +2.787 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.644 | 14.38 | +49.1% | +4.207 to +5.261 | power given |
| pods started | 4.667 | 11.13 | +138.6% | +5.248 to +7.685 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.647e-16 to +8.383e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.5 | 182.1 | -0.2% | -0.9971 to +0.2369 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.5 | 182.1 | -0.2% | -0.9971 to +0.2369 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.178 | 2.231 | +2.4% | +0.03572 to +0.07037 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65 | 66.97 | +3.0% | +1.392 to +2.55 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

15 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1306 | 1447 | +10.8% | -197.8 to +478.7 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4689 | 4783 | +2.0% | -806.2 to +994.4 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 23.61 | 18.02 | -23.7% | -7.421 to -3.746 | GAIN |
| failed requests (%) | 9.284 | 7.991 | -13.9% | -2.222 to -0.3621 | GAIN |
| HPA replicas, mean | 9.679 | 14.49 | +49.7% | +4.325 to +5.298 | power given |
| pods started | 4.733 | 12.13 | +156.3% | +6.257 to +8.543 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.401e-15 to -2.569e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182 | 181.4 | -0.4% | -1.525 to +0.225 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182 | 181.4 | -0.4% | -1.525 to +0.225 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.122 | 2.155 | +1.5% | +0.01219 to +0.05212 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.43 | 64.83 | +2.2% | +1.051 to +1.749 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.984e-09 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
