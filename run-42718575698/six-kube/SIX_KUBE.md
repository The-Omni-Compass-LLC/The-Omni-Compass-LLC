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
| response time (ms), 95th percentile | 1130 | 1010 | 1427 | 1314 | 1379 | 1482 | 1351 | 1236 | 1461 | 1505 | 1269 | 1354 | 1305 | 1410 |
| response time (ms), 99th percentile | 4215 | 3871 | 4197 | 4129 | 4549 | 4645 | 4760 | 4602 | 4491 | 4532 | 3959 | 4259 | 4645 | 5078 |
| time over the response line (% of samples) | 12.54 | 9.809 | 23.37 | 17.74 | 15.84 | 11.98 | 14.84 | 11.19 | 21.44 | 16.52 | 17.81 | 14.17 | 22.71 | 17.21 |
| failed requests (%) | 3.6 | 3.838 | 10.16 | 8.688 | 4.718 | 4.553 | 4.225 | 3.843 | 6.294 | 6.184 | 6.015 | 5.299 | 9.142 | 7.837 |
| HPA replicas, mean | 9.547 | 14.12 | 9.634 | 14.19 | 9.567 | 13.96 | 9.577 | 14.38 | 9.568 | 14.26 | 9.551 | 13.91 | 9.662 | 14.19 |
| pods started | 5.514 | 11.94 | 4.943 | 12.23 | 5.457 | 11.2 | 5.429 | 11.26 | 5.314 | 11.11 | 5.371 | 12.2 | 4.743 | 11.8 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 178.2 | 178.6 | 181 | 180.5 | 179.1 | 179.1 | 179.3 | 179.8 | 180.9 | 180.6 | 179.8 | 179.3 | 181.6 | 180.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.2 | 178.6 | 181 | 180.5 | 179.1 | 179.1 | 179.3 | 179.8 | 180.9 | 180.6 | 179.8 | 179.3 | 181.6 | 180.9 |
| CPU used with Omni's own (cores), mean | 1.773 | 1.837 | 2.019 | 2.052 | 1.879 | 1.925 | 1.889 | 1.922 | 2.043 | 2.082 | 1.907 | 1.939 | 2.072 | 2.107 |
| host CPU busy, the real machine under kind (%) | 53.13 | 55.04 | 60.14 | 61.71 | 56.04 | 57.73 | 56.22 | 57.53 | 60.77 | 62.38 | 56.87 | 58.21 | 61.6 | 63.18 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.07429 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1130 | 1010 | -10.6% | -339.6 to +99.93 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4215 | 3871 | -8.2% | -693.1 to +4.184 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 12.54 | 9.809 | -21.8% | -3.852 to -1.617 | GAIN |
| failed requests (%) | 3.6 | 3.838 | +6.6% | -0.2451 to +0.7201 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.547 | 14.12 | +47.9% | +4.178 to +4.966 | power given |
| pods started | 5.514 | 11.94 | +116.6% | +6.001 to +6.856 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.299e-16 to -3.136e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.2 | 178.6 | +0.2% | -0.04453 to +0.8818 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.2 | 178.6 | +0.2% | -0.04453 to +0.8818 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.773 | 1.837 | +3.6% | +0.04992 to +0.07916 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 53.13 | 55.04 | +3.6% | +1.556 to +2.265 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.994e+05 to +8.02e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.444e-05 to -9.414e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1427 | 1314 | -7.9% | -346.7 to +120.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4197 | 4129 | -1.6% | -607.2 to +471.9 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 23.37 | 17.74 | -24.1% | -7.599 to -3.662 | GAIN |
| failed requests (%) | 10.16 | 8.688 | -14.5% | -2.238 to -0.704 | GAIN |
| HPA replicas, mean | 9.634 | 14.19 | +47.3% | +4.233 to +4.88 | power given |
| pods started | 4.943 | 12.23 | +147.4% | +6.682 to +7.89 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.081e-16 to +1.514e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 180.5 | -0.2% | -0.9084 to +0.01103 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181 | 180.5 | -0.2% | -0.9084 to +0.01103 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.019 | 2.052 | +1.6% | +0.0199 to +0.04646 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.14 | 61.71 | +2.6% | +1.225 to +1.919 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.621e+05 to +8.625e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.149e-05 to -8.145e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1379 | 1482 | +7.4% | -149.2 to +354.2 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4549 | 4645 | +2.1% | -307.1 to +498.2 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 15.84 | 11.98 | -24.4% | -4.842 to -2.873 | GAIN |
| failed requests (%) | 4.718 | 4.553 | -3.5% | -0.5062 to +0.1751 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.567 | 13.96 | +45.9% | +3.876 to +4.903 | power given |
| pods started | 5.457 | 11.2 | +105.2% | +5.085 to +6.401 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.36e-16 to +5.898e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.1 | 179.1 | +0.0% | -0.4285 to +0.4903 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.1 | 179.1 | +0.0% | -0.4285 to +0.4903 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.879 | 1.925 | +2.5% | +0.03561 to +0.05675 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.04 | 57.73 | +3.0% | +1.417 to +1.955 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1351 | 1236 | -8.5% | -350.7 to +121.4 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4760 | 4602 | -3.3% | -544.7 to +229 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 14.84 | 11.19 | -24.6% | -4.725 to -2.577 | GAIN |
| failed requests (%) | 4.225 | 3.843 | -9.0% | -1.002 to +0.2377 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.577 | 14.38 | +50.2% | +4.477 to +5.139 | power given |
| pods started | 5.429 | 11.26 | +107.4% | +5.286 to +6.372 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.397e-16 to -7.231e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.3 | 179.8 | +0.3% | +0.1598 to +0.87 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.3 | 179.8 | +0.3% | +0.1598 to +0.87 | power given |
| CPU used with Omni's own (cores), mean | 1.889 | 1.922 | +1.7% | +0.01888 to +0.04558 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.22 | 57.53 | +2.3% | +0.9244 to +1.694 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1461 | 1505 | +3.0% | -129.1 to +217.5 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4491 | 4532 | +0.9% | -331 to +411.8 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 21.44 | 16.52 | -22.9% | -6.266 to -3.57 | GAIN |
| failed requests (%) | 6.294 | 6.184 | -1.7% | -0.4186 to +0.1996 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.568 | 14.26 | +49.1% | +4.229 to +5.163 | power given |
| pods started | 5.314 | 11.11 | +109.1% | +5.156 to +6.444 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.885e-16 to -1.788e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.9 | 180.6 | -0.2% | -0.818 to +0.02198 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.9 | 180.6 | -0.2% | -0.818 to +0.02198 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.043 | 2.082 | +1.9% | +0.03091 to +0.04816 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.77 | 62.38 | +2.7% | +1.403 to +1.827 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1269 | 1354 | +6.7% | -154.3 to +323.3 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3959 | 4259 | +7.6% | -204 to +804.3 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 17.81 | 14.17 | -20.5% | -4.954 to -2.335 | GAIN |
| failed requests (%) | 6.015 | 5.299 | -11.9% | -1.371 to -0.06015 | GAIN |
| HPA replicas, mean | 9.551 | 13.91 | +45.6% | +3.958 to +4.754 | power given |
| pods started | 5.371 | 12.2 | +127.1% | +6.279 to +7.378 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.338e-16 to +2.816e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.8 | 179.3 | -0.3% | -1.016 to +0.01109 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.8 | 179.3 | -0.3% | -1.016 to +0.01109 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.907 | 1.939 | +1.6% | +0.01822 to +0.04471 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.87 | 58.21 | +2.3% | +0.9645 to +1.707 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1305 | 1410 | +8.0% | -165.1 to +374.5 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4645 | 5078 | +9.3% | -53.26 to +919.2 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 22.71 | 17.21 | -24.2% | -7.729 to -3.269 | GAIN |
| failed requests (%) | 9.142 | 7.837 | -14.3% | -2.298 to -0.3124 | GAIN |
| HPA replicas, mean | 9.662 | 14.19 | +46.9% | +4.215 to +4.844 | power given |
| pods started | 4.743 | 11.8 | +148.8% | +6.486 to +7.628 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.6e-16 to -1.311e-18 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.6 | 180.9 | -0.4% | -1.251 to -0.2183 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.6 | 180.9 | -0.4% | -1.251 to -0.2183 | GAIN |
| CPU used with Omni's own (cores), mean | 2.072 | 2.107 | +1.7% | +0.01558 to +0.05482 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.6 | 63.18 | +2.6% | +1.104 to +2.047 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.07429 | +0.0743 | +0.05905 to +0.08952 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
