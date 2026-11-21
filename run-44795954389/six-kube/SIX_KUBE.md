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
| response time (ms), 95th percentile | 1191 | 1107 | 1327 | 1358 | 1134 | 1153 | 1324 | 1180 | 1143 | 1069 | 1240 | 1302 | 1531 | 1594 |
| response time (ms), 99th percentile | 4607 | 4565 | 4701 | 5015 | 4470 | 4569 | 3992 | 3927 | 3505 | 3505 | 4460 | 4917 | 5075 | 5247 |
| time over the response line (% of samples) | 15.06 | 11.05 | 22.57 | 16.76 | 14.37 | 10.84 | 14.08 | 11.13 | 16.42 | 12.77 | 17.67 | 14.02 | 27.25 | 19.29 |
| failed requests (%) | 4.607 | 4.053 | 8.757 | 7.854 | 4.079 | 3.878 | 4.804 | 4.678 | 5.078 | 5.168 | 5.497 | 5.124 | 11.66 | 8.813 |
| HPA replicas, mean | 9.602 | 14.45 | 9.648 | 14.56 | 9.567 | 14.26 | 9.554 | 13.91 | 9.505 | 13.72 | 9.579 | 14.46 | 9.679 | 14.29 |
| pods started | 5.114 | 11.29 | 5.257 | 12.06 | 5.571 | 11.14 | 5.314 | 11.34 | 5.771 | 12 | 5.429 | 11.77 | 4.857 | 11.86 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 179.2 | 179.4 | 182.1 | 180.9 | 179.1 | 179.2 | 177.9 | 178.5 | 179.4 | 178.7 | 180.8 | 180.2 | 182.8 | 181.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.2 | 179.4 | 182.1 | 180.9 | 179.1 | 179.2 | 177.9 | 178.5 | 179.4 | 178.7 | 180.8 | 180.2 | 182.8 | 181.9 |
| CPU used with Omni's own (cores), mean | 1.889 | 1.939 | 2.103 | 2.137 | 1.87 | 1.916 | 1.765 | 1.819 | 1.849 | 1.891 | 1.982 | 2.025 | 2.181 | 2.199 |
| host CPU busy, the real machine under kind (%) | 56.62 | 58.22 | 62.45 | 63.97 | 55.99 | 57.62 | 53.32 | 55.08 | 55.6 | 57.33 | 59.12 | 60.88 | 65.04 | 66.4 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.002857 | 0.09143 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1191 | 1107 | -7.1% | -304.1 to +135.6 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4607 | 4565 | -0.9% | -304.7 to +220.8 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 15.06 | 11.05 | -26.6% | -5.069 to -2.947 | GAIN |
| failed requests (%) | 4.607 | 4.053 | -12.0% | -0.9218 to -0.1858 | GAIN |
| HPA replicas, mean | 9.602 | 14.45 | +50.5% | +4.516 to +5.188 | power given |
| pods started | 5.114 | 11.29 | +120.7% | +5.743 to +6.6 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.674e-16 to +2.629e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.2 | 179.4 | +0.1% | -0.1988 to +0.5834 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.2 | 179.4 | +0.1% | -0.1988 to +0.5834 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.889 | 1.939 | +2.6% | +0.03989 to +0.05918 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.62 | 58.22 | +2.8% | +1.392 to +1.803 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.981e+05 to +7.999e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.42e-05 to -9.398e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1327 | 1358 | +2.3% | -178.6 to +240.7 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4701 | 5015 | +6.7% | -265.2 to +893.6 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 22.57 | 16.76 | -25.7% | -7.331 to -4.281 | GAIN |
| failed requests (%) | 8.757 | 7.854 | -10.3% | -1.442 to -0.3638 | GAIN |
| HPA replicas, mean | 9.648 | 14.56 | +50.9% | +4.677 to +5.154 | power given |
| pods started | 5.257 | 12.06 | +129.3% | +6.302 to +7.298 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.383e-16 to +4.905e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.1 | 180.9 | -0.7% | -1.644 to -0.7769 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.1 | 180.9 | -0.7% | -1.644 to -0.7769 | GAIN |
| CPU used with Omni's own (cores), mean | 2.103 | 2.137 | +1.6% | +0.02027 to +0.04667 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.45 | 63.97 | +2.4% | +1.169 to +1.885 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.621e+05 to +8.626e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.15e-05 to -8.146e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1134 | 1153 | +1.7% | -166.4 to +204.7 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4470 | 4569 | +2.2% | -261.4 to +461.3 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 14.37 | 10.84 | -24.6% | -4.575 to -2.482 | GAIN |
| failed requests (%) | 4.079 | 3.878 | -4.9% | -0.5427 to +0.141 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.567 | 14.26 | +49.0% | +4.247 to +5.131 | power given |
| pods started | 5.571 | 11.14 | +100.0% | +4.975 to +6.168 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.859e-16 to +1.291e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.1 | 179.2 | +0.0% | -0.3361 to +0.4819 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.1 | 179.2 | +0.0% | -0.3361 to +0.4819 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.87 | 1.916 | +2.4% | +0.02825 to +0.0628 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.99 | 57.62 | +2.9% | +1.178 to +2.089 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1324 | 1180 | -10.9% | -370.1 to +82.22 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 3992 | 3927 | -1.6% | -301.4 to +172.4 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 14.08 | 11.13 | -20.9% | -4.01 to -1.891 | GAIN |
| failed requests (%) | 4.804 | 4.678 | -2.6% | -0.4793 to +0.2275 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.554 | 13.91 | +45.6% | +3.881 to +4.829 | power given |
| pods started | 5.314 | 11.34 | +113.4% | +5.486 to +6.572 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.578e-16 to +4.101e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 177.9 | 178.5 | +0.3% | +0.1756 to +1.069 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 177.9 | 178.5 | +0.3% | +0.1756 to +1.069 | power given |
| CPU used with Omni's own (cores), mean | 1.765 | 1.819 | +3.0% | +0.04291 to +0.06411 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 53.32 | 55.08 | +3.3% | +1.433 to +2.09 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1143 | 1069 | -6.4% | -219.8 to +73.3 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 3505 | 3505 | -0.0% | -404.2 to +404 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 16.42 | 12.77 | -22.3% | -5.057 to -2.254 | GAIN |
| failed requests (%) | 5.078 | 5.168 | +1.8% | -0.1351 to +0.3149 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.505 | 13.72 | +44.4% | +3.699 to +4.74 | power given |
| pods started | 5.771 | 12 | +107.9% | +5.551 to +6.906 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.745e-16 to +4.222e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.4 | 178.7 | -0.4% | -1.057 to -0.2546 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.4 | 178.7 | -0.4% | -1.057 to -0.2546 | GAIN |
| CPU used with Omni's own (cores), mean | 1.849 | 1.891 | +2.3% | +0.02978 to +0.05456 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.6 | 57.33 | +3.1% | +1.352 to +2.106 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1240 | 1302 | +5.0% | -94.81 to +218.7 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4460 | 4917 | +10.3% | +21.48 to +893 | LOSS |
| time over the response line (% of samples) | 17.67 | 14.02 | -20.7% | -5.083 to -2.222 | GAIN |
| failed requests (%) | 5.497 | 5.124 | -6.8% | -0.9559 to +0.2097 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.579 | 14.46 | +51.0% | +4.675 to +5.091 | power given |
| pods started | 5.429 | 11.77 | +116.8% | +5.81 to +6.876 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.95e-16 to +6.502e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.8 | 180.2 | -0.3% | -1.006 to -0.1013 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.8 | 180.2 | -0.3% | -1.006 to -0.1013 | GAIN |
| CPU used with Omni's own (cores), mean | 1.982 | 2.025 | +2.2% | +0.03379 to +0.05313 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.12 | 60.88 | +3.0% | +1.495 to +2.027 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1531 | 1594 | +4.1% | -282.6 to +409.3 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5075 | 5247 | +3.4% | -349.3 to +692.9 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 27.25 | 19.29 | -29.2% | -10.16 to -5.772 | GAIN |
| failed requests (%) | 11.66 | 8.813 | -24.4% | -4.184 to -1.519 | GAIN |
| HPA replicas, mean | 9.679 | 14.29 | +47.7% | +4.337 to +4.888 | power given |
| pods started | 4.857 | 11.86 | +144.1% | +6.417 to +7.583 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.02e-16 to +1.96e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.8 | 181.9 | -0.5% | -1.486 to -0.4559 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.8 | 181.9 | -0.5% | -1.486 to -0.4559 | GAIN |
| CPU used with Omni's own (cores), mean | 2.181 | 2.199 | +0.8% | +0.005124 to +0.03145 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.04 | 66.4 | +2.1% | +1.043 to +1.682 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.984e-09 | power given |
| organism behind its window (s) | 0.002857 | 0.09143 | +3100.0% | +0.07748 to +0.09966 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
