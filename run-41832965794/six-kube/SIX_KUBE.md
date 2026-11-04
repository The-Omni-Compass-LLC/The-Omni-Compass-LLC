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
| response time (ms), 95th percentile | 1277 | 1101 | 1488 | 1649 | 1464 | 1458 | 1629 | 1147 | 1711 | 1920 | 1405 | 1878 | 1464 | 1521 |
| response time (ms), 99th percentile | 3689 | 3759 | 6103 | 6306 | 4920 | 4971 | 5390 | 4986 | 5544 | 5045 | 3992 | 5719 | 5111 | 4882 |
| time over the response line (% of samples) | 11.94 | 8.923 | 25.86 | 20.79 | 17.89 | 15.19 | 18.66 | 13.54 | 28.34 | 21.68 | 27.07 | 20.03 | 25.94 | 19.29 |
| failed requests (%) | 3.372 | 3.012 | 10.37 | 9.374 | 5.637 | 6.577 | 5.894 | 5.632 | 8.964 | 8.512 | 9.896 | 7.838 | 11.01 | 8.657 |
| HPA replicas, mean | 9.533 | 14.32 | 9.675 | 14.68 | 9.62 | 14.29 | 9.573 | 13.85 | 9.603 | 14.49 | 9.644 | 14.68 | 9.681 | 14.08 |
| pods started | 5.8 | 12.4 | 4.9 | 11.7 | 4.8 | 10.8 | 5.5 | 10.8 | 5.1 | 11.4 | 5.1 | 10.7 | 4.9 | 11.9 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 178.3 | 178.1 | 183.6 | 182.3 | 179.8 | 180.6 | 179.5 | 179.6 | 182.8 | 182 | 182.7 | 182.2 | 182.5 | 181.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.3 | 178.1 | 183.6 | 182.3 | 179.8 | 180.6 | 179.5 | 179.6 | 182.8 | 182 | 182.7 | 182.2 | 182.5 | 181.7 |
| CPU used with Omni's own (cores), mean | 1.779 | 1.811 | 2.246 | 2.277 | 1.958 | 2.028 | 1.901 | 1.942 | 2.197 | 2.233 | 2.217 | 2.242 | 2.18 | 2.211 |
| host CPU busy, the real machine under kind (%) | 53.81 | 54.64 | 66.7 | 68.13 | 58.03 | 60.38 | 56.85 | 58.55 | 64.91 | 66.5 | 65.43 | 66.71 | 65.04 | 66.34 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.09 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1277 | 1101 | -13.8% | -520.6 to +168.4 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 3689 | 3759 | +1.9% | -395.7 to +536.1 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 11.94 | 8.923 | -25.2% | -4.747 to -1.279 | GAIN |
| failed requests (%) | 3.372 | 3.012 | -10.7% | -1.169 to +0.4487 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.533 | 14.32 | +50.2% | +4.242 to +5.337 | power given |
| pods started | 5.8 | 12.4 | +113.8% | +5.695 to +7.505 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.718e-16 to +8.494e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.3 | 178.1 | -0.1% | -1.037 to +0.8305 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.3 | 178.1 | -0.1% | -1.037 to +0.8305 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.779 | 1.811 | +1.8% | +0.003143 to +0.0605 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 53.81 | 54.64 | +1.6% | -0.0539 to +1.73 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.96e+05 to +8.054e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.484e-05 to -9.373e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1488 | 1649 | +10.8% | -212.4 to +534.4 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6103 | 6306 | +3.3% | -196.8 to +602.6 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 25.86 | 20.79 | -19.6% | -7.867 to -2.258 | GAIN |
| failed requests (%) | 10.37 | 9.374 | -9.6% | -2.311 to +0.3185 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.675 | 14.68 | +51.8% | +4.617 to +5.402 | power given |
| pods started | 4.9 | 11.7 | +138.8% | +6.061 to +7.539 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.355e-15 to +4.668e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.6 | 182.3 | -0.7% | -2.09 to -0.3463 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.6 | 182.3 | -0.7% | -2.09 to -0.3463 | GAIN |
| CPU used with Omni's own (cores), mean | 2.246 | 2.277 | +1.4% | +0.01923 to +0.04356 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.7 | 68.13 | +2.2% | +1.009 to +1.862 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.62e+05 to +8.625e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.149e-05 to -8.144e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1464 | 1458 | -0.4% | -708.5 to +697.7 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4920 | 4971 | +1.0% | -1277 to +1377 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 17.89 | 15.19 | -15.1% | -5.432 to +0.03002 | STEADY, inside the noise (cut) |
| failed requests (%) | 5.637 | 6.577 | +16.7% | -0.7357 to +2.615 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.62 | 14.29 | +48.6% | +3.689 to +5.655 | power given |
| pods started | 4.8 | 10.8 | +125.0% | +4.882 to +7.118 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.785e-16 to +8.338e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.8 | 180.6 | +0.4% | -0.1343 to +1.718 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.8 | 180.6 | +0.4% | -0.1343 to +1.718 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.958 | 2.028 | +3.5% | +0.02193 to +0.1164 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.03 | 60.38 | +4.1% | +0.8889 to +3.823 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.409e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.248e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1629 | 1147 | -29.6% | -1071 to +107.6 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5390 | 4986 | -7.5% | -989.7 to +181.9 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 18.66 | 13.54 | -27.4% | -8.067 to -2.171 | GAIN |
| failed requests (%) | 5.894 | 5.632 | -4.5% | -1.124 to +0.5985 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.573 | 13.85 | +44.7% | +3.119 to +5.43 | power given |
| pods started | 5.5 | 10.8 | +96.4% | +3.867 to +6.733 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.733e-16 to +4.044e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.5 | 179.6 | +0.1% | -0.9344 to +1.224 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.5 | 179.6 | +0.1% | -0.9344 to +1.224 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.901 | 1.942 | +2.1% | +0.02345 to +0.05804 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.85 | 58.55 | +3.0% | +1.192 to +2.224 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1711 | 1920 | +12.2% | -119.7 to +537.3 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5544 | 5045 | -9.0% | -1609 to +610.5 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 28.34 | 21.68 | -23.5% | -10.11 to -3.214 | GAIN |
| failed requests (%) | 8.964 | 8.512 | -5.0% | -1.014 to +0.1092 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.603 | 14.49 | +50.9% | +4.031 to +5.75 | power given |
| pods started | 5.1 | 11.4 | +123.5% | +5.286 to +7.314 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.318e-16 to +1.009e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.8 | 182 | -0.4% | -1.577 to -0.006892 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.8 | 182 | -0.4% | -1.577 to -0.006892 | GAIN |
| CPU used with Omni's own (cores), mean | 2.197 | 2.233 | +1.7% | +0.01439 to +0.05846 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.91 | 66.5 | +2.5% | +1.068 to +2.119 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.377e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1405 | 1878 | +33.6% | -170.2 to +1116 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3992 | 5719 | +43.3% | +766.8 to +2687 | LOSS |
| time over the response line (% of samples) | 27.07 | 20.03 | -26.0% | -10.14 to -3.936 | GAIN |
| failed requests (%) | 9.896 | 7.838 | -20.8% | -3.937 to -0.1786 | GAIN |
| HPA replicas, mean | 9.644 | 14.68 | +52.3% | +4.615 to +5.465 | power given |
| pods started | 5.1 | 10.7 | +109.8% | +4.76 to +6.44 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.56e-15 to -3.874e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.7 | 182.2 | -0.3% | -1.389 to +0.2796 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.7 | 182.2 | -0.3% | -1.389 to +0.2796 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.217 | 2.242 | +1.1% | +0.005566 to +0.04507 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.43 | 66.71 | +2.0% | +0.4793 to +2.091 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1464 | 1521 | +3.9% | -223.6 to +337.7 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5111 | 4882 | -4.5% | -1288 to +829.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 25.94 | 19.29 | -25.6% | -10.47 to -2.826 | GAIN |
| failed requests (%) | 11.01 | 8.657 | -21.4% | -4.261 to -0.439 | GAIN |
| HPA replicas, mean | 9.681 | 14.08 | +45.4% | +3.409 to +5.389 | power given |
| pods started | 4.9 | 11.9 | +142.9% | +5.53 to +8.47 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.446e-15 to -5.082e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.5 | 181.7 | -0.5% | -2.013 to +0.2979 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.5 | 181.7 | -0.5% | -2.013 to +0.2979 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.18 | 2.211 | +1.4% | +0.003563 to +0.05943 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.04 | 66.34 | +2.0% | +0.679 to +1.934 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.984e-09 | power given |
| organism behind its window (s) | 0 | 0.09 | +0.09 | +0.06738 to +0.1126 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
