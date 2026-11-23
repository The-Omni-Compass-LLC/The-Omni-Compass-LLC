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
| response time (ms), 95th percentile | 1916 | 1780 | 1327 | 1457 | 1486 | 1394 | 1257 | 1156 | 1312 | 1412 | 1372 | 1493 | 1339 | 1513 |
| response time (ms), 99th percentile | 5736 | 5341 | 4616 | 5062 | 4869 | 4623 | 4295 | 4159 | 4297 | 4568 | 4691 | 4669 | 4983 | 5466 |
| time over the response line (% of samples) | 20.65 | 15.53 | 24.28 | 18.94 | 16.33 | 12.91 | 14.35 | 10.82 | 19.63 | 15.16 | 19.88 | 16.68 | 24.76 | 19.13 |
| failed requests (%) | 6.942 | 6.513 | 10.71 | 9.445 | 5.166 | 4.979 | 4.318 | 4.277 | 5.585 | 5.502 | 7.23 | 6.151 | 10.65 | 8.718 |
| HPA replicas, mean | 9.639 | 14.53 | 9.648 | 14.46 | 9.583 | 14.37 | 9.567 | 14.17 | 9.566 | 14.34 | 9.579 | 14.42 | 9.663 | 14.3 |
| pods started | 4.857 | 11.23 | 5.229 | 11.97 | 5.257 | 11.26 | 5.371 | 11.31 | 5.514 | 11.46 | 5.429 | 12.06 | 4.857 | 11.89 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 180.7 | 181.2 | 182 | 181.5 | 179.5 | 179.8 | 178.8 | 178.8 | 181 | 180.5 | 181 | 180.3 | 182.5 | 181.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.7 | 181.2 | 182 | 181.5 | 179.5 | 179.8 | 178.8 | 178.8 | 181 | 180.5 | 181 | 180.3 | 182.5 | 181.5 |
| CPU used with Omni's own (cores), mean | 2.046 | 2.101 | 2.122 | 2.162 | 1.912 | 1.972 | 1.836 | 1.892 | 2.028 | 2.076 | 2.006 | 2.051 | 2.15 | 2.179 |
| host CPU busy, the real machine under kind (%) | 60.96 | 62.88 | 63.33 | 64.93 | 57.2 | 59.1 | 55.44 | 57.34 | 60.49 | 62.48 | 59.87 | 61.67 | 64.18 | 65.75 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1916 | 1780 | -7.1% | -409.5 to +136.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5736 | 5341 | -6.9% | -819 to +30.24 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 20.65 | 15.53 | -24.8% | -6.313 to -3.928 | GAIN |
| failed requests (%) | 6.942 | 6.513 | -6.2% | -0.8512 to -0.008065 | GAIN |
| HPA replicas, mean | 9.639 | 14.53 | +50.7% | +4.546 to +5.233 | power given |
| pods started | 4.857 | 11.23 | +131.2% | +5.851 to +6.892 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.221e-16 to +2.191e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.7 | 181.2 | +0.3% | +0.0614 to +0.894 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.7 | 181.2 | +0.3% | +0.0614 to +0.894 | power given |
| CPU used with Omni's own (cores), mean | 2.046 | 2.101 | +2.7% | +0.04494 to +0.06529 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.96 | 62.88 | +3.2% | +1.667 to +2.183 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.984e+05 to +8.001e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.422e-05 to -9.402e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1327 | 1457 | +9.9% | -58.05 to +319.5 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4616 | 5062 | +9.7% | -63.53 to +954.7 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 24.28 | 18.94 | -22.0% | -6.769 to -3.916 | GAIN |
| failed requests (%) | 10.71 | 9.445 | -11.8% | -2.005 to -0.5155 | GAIN |
| HPA replicas, mean | 9.648 | 14.46 | +49.9% | +4.514 to +5.111 | power given |
| pods started | 5.229 | 11.97 | +129.0% | +6.164 to +7.322 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.223e-16 to +1.655e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182 | 181.5 | -0.3% | -0.9966 to -0.03229 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182 | 181.5 | -0.3% | -0.9966 to -0.03229 | GAIN |
| CPU used with Omni's own (cores), mean | 2.122 | 2.162 | +1.9% | +0.02837 to +0.0506 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.33 | 64.93 | +2.5% | +1.329 to +1.88 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.621e+05 to +8.626e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.15e-05 to -8.146e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1486 | 1394 | -6.1% | -348.3 to +165.7 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4869 | 4623 | -5.1% | -689.8 to +196.1 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 16.33 | 12.91 | -20.9% | -4.265 to -2.567 | GAIN |
| failed requests (%) | 5.166 | 4.979 | -3.6% | -0.5979 to +0.2238 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.583 | 14.37 | +50.0% | +4.442 to +5.136 | power given |
| pods started | 5.257 | 11.26 | +114.1% | +5.355 to +6.645 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.762e-16 to +3.255e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.5 | 179.8 | +0.1% | -0.2063 to +0.7113 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.5 | 179.8 | +0.1% | -0.2063 to +0.7113 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.912 | 1.972 | +3.2% | +0.05023 to +0.07119 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.2 | 59.1 | +3.3% | +1.566 to +2.245 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1257 | 1156 | -8.1% | -402.9 to +199.7 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4295 | 4159 | -3.2% | -494.9 to +222.8 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 14.35 | 10.82 | -24.6% | -4.499 to -2.559 | GAIN |
| failed requests (%) | 4.318 | 4.277 | -1.0% | -0.3538 to +0.2715 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.567 | 14.17 | +48.1% | +4.164 to +5.038 | power given |
| pods started | 5.371 | 11.31 | +110.6% | +5.43 to +6.456 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.695e-16 to +1.62e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.8 | 178.8 | -0.0% | -0.4751 to +0.3849 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.8 | 178.8 | -0.0% | -0.4751 to +0.3849 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.836 | 1.892 | +3.0% | +0.04556 to +0.06542 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.44 | 57.34 | +3.4% | +1.669 to +2.122 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1312 | 1412 | +7.6% | -71.62 to +271.1 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4297 | 4568 | +6.3% | -171.2 to +712.8 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 19.63 | 15.16 | -22.8% | -5.715 to -3.229 | GAIN |
| failed requests (%) | 5.585 | 5.502 | -1.5% | -0.3624 to +0.1978 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.566 | 14.34 | +49.9% | +4.359 to +5.189 | power given |
| pods started | 5.514 | 11.46 | +107.8% | +5.423 to +6.463 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.943e-16 to -2.074e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 180.5 | -0.3% | -1.001 to -0.0488 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181 | 180.5 | -0.3% | -1.001 to -0.0488 | GAIN |
| CPU used with Omni's own (cores), mean | 2.028 | 2.076 | +2.4% | +0.03268 to +0.06358 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.49 | 62.48 | +3.3% | +1.614 to +2.371 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1372 | 1493 | +8.8% | -84.91 to +326.1 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4691 | 4669 | -0.5% | -510.6 to +465.3 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 19.88 | 16.68 | -16.1% | -4.464 to -1.933 | GAIN |
| failed requests (%) | 7.23 | 6.151 | -14.9% | -2.082 to -0.07759 | GAIN |
| HPA replicas, mean | 9.579 | 14.42 | +50.6% | +4.539 to +5.149 | power given |
| pods started | 5.429 | 12.06 | +122.1% | +6.069 to +7.188 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.018e-16 to +2.495e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 180.3 | -0.4% | -1.137 to -0.2779 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181 | 180.3 | -0.4% | -1.137 to -0.2779 | GAIN |
| CPU used with Omni's own (cores), mean | 2.006 | 2.051 | +2.3% | +0.03515 to +0.05541 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.87 | 61.67 | +3.0% | +1.464 to +2.137 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1339 | 1513 | +13.0% | -89.51 to +437 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4983 | 5466 | +9.7% | -186.4 to +1153 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 24.76 | 19.13 | -22.8% | -7.402 to -3.869 | GAIN |
| failed requests (%) | 10.65 | 8.718 | -18.1% | -2.923 to -0.939 | GAIN |
| HPA replicas, mean | 9.663 | 14.3 | +48.0% | +4.308 to +4.97 | power given |
| pods started | 4.857 | 11.89 | +144.7% | +6.505 to +7.552 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.25e-16 to +4.25e-16 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 182.5 | 181.5 | -0.6% | -1.535 to -0.4933 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.5 | 181.5 | -0.6% | -1.535 to -0.4933 | GAIN |
| CPU used with Omni's own (cores), mean | 2.15 | 2.179 | +1.4% | +0.01395 to +0.0454 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.18 | 65.75 | +2.4% | +1.205 to +1.928 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.984e-09 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
