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
| response time (ms), 95th percentile | 1302 | 1064 | 1222 | 1275 | 1207 | 1106 | 1522 | 1183 | 1174 | 1126 | 1679 | 1817 | 1068 | 1058 |
| response time (ms), 99th percentile | 4452 | 4447 | 4122 | 4440 | 4540 | 4222 | 5013 | 4832 | 4132 | 4134 | 5133 | 5076 | 3677 | 3812 |
| time over the response line (% of samples) | 14.5 | 10.72 | 19.77 | 15.65 | 14.91 | 11.13 | 16.39 | 12.72 | 15.74 | 12.38 | 24.93 | 20.59 | 17.43 | 13.23 |
| failed requests (%) | 4.311 | 4.051 | 7.751 | 6.883 | 4.687 | 4.415 | 4.815 | 4.812 | 4.049 | 4.135 | 9.028 | 8.196 | 6.502 | 5.736 |
| HPA replicas, mean | 9.568 | 14.28 | 9.623 | 14.24 | 9.565 | 14.17 | 9.596 | 14.59 | 9.523 | 14.07 | 9.623 | 14.51 | 9.604 | 14.34 |
| pods started | 5.657 | 11.66 | 5.314 | 12.66 | 5.4 | 11.49 | 5.371 | 10.49 | 5.743 | 11.89 | 4.971 | 11.63 | 5.543 | 12.74 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 178.9 | 179.5 | 181 | 180.1 | 178.9 | 179.3 | 179.6 | 180.2 | 179.8 | 179.4 | 182 | 181.2 | 180.4 | 179.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.9 | 179.5 | 181 | 180.1 | 178.9 | 179.3 | 179.6 | 180.2 | 179.8 | 179.4 | 182 | 181.2 | 180.4 | 179.7 |
| CPU used with Omni's own (cores), mean | 1.857 | 1.901 | 2.007 | 2.046 | 1.85 | 1.897 | 1.933 | 1.994 | 1.912 | 1.964 | 2.102 | 2.144 | 1.945 | 1.982 |
| host CPU busy, the real machine under kind (%) | 55.56 | 57.18 | 59.83 | 61.46 | 55.58 | 57.32 | 57.9 | 59.85 | 57.28 | 59.06 | 62.39 | 64.14 | 58.48 | 60.12 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1302 | 1064 | -18.2% | -377.5 to -97.48 | GAIN |
| response time (ms), 99th percentile | 4452 | 4447 | -0.1% | -281.6 to +272.6 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 14.5 | 10.72 | -26.1% | -4.811 to -2.758 | GAIN |
| failed requests (%) | 4.311 | 4.051 | -6.0% | -0.5482 to +0.02905 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.568 | 14.28 | +49.3% | +4.333 to +5.1 | power given |
| pods started | 5.657 | 11.66 | +106.1% | +5.493 to +6.507 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.416e-16 to +6.983e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.9 | 179.5 | +0.4% | +0.3762 to +0.9553 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.9 | 179.5 | +0.4% | +0.3762 to +0.9553 | power given |
| CPU used with Omni's own (cores), mean | 1.857 | 1.901 | +2.4% | +0.03412 to +0.05417 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.56 | 57.18 | +2.9% | +1.382 to +1.854 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.98e+05 to +7.999e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.419e-05 to -9.397e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1222 | 1275 | +4.3% | -130 to +236 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4122 | 4440 | +7.7% | -206.4 to +842.8 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 19.77 | 15.65 | -20.8% | -5.634 to -2.609 | GAIN |
| failed requests (%) | 7.751 | 6.883 | -11.2% | -1.548 to -0.1864 | GAIN |
| HPA replicas, mean | 9.623 | 14.24 | +48.0% | +4.28 to +4.957 | power given |
| pods started | 5.314 | 12.66 | +138.2% | +6.641 to +8.045 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.839e-16 to -1.327e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 180.1 | -0.5% | -1.316 to -0.5142 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181 | 180.1 | -0.5% | -1.316 to -0.5142 | GAIN |
| CPU used with Omni's own (cores), mean | 2.007 | 2.046 | +2.0% | +0.02949 to +0.0491 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.83 | 61.46 | +2.7% | +1.367 to +1.884 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.622e+05 to +8.626e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.15e-05 to -8.146e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 3 (response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1207 | 1106 | -8.4% | -348.3 to +146.5 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4540 | 4222 | -7.0% | -618.3 to -15.97 | GAIN |
| time over the response line (% of samples) | 14.91 | 11.13 | -25.3% | -5.026 to -2.526 | GAIN |
| failed requests (%) | 4.687 | 4.415 | -5.8% | -0.7419 to +0.1989 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.565 | 14.17 | +48.2% | +4.212 to +5.002 | power given |
| pods started | 5.4 | 11.49 | +112.7% | +5.604 to +6.567 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.117e-16 to +5.655e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.9 | 179.3 | +0.2% | -0.01666 to +0.76 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.9 | 179.3 | +0.2% | -0.01666 to +0.76 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.85 | 1.897 | +2.5% | +0.0327 to +0.06005 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.58 | 57.32 | +3.1% | +1.444 to +2.03 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1522 | 1183 | -22.3% | -594.7 to -83.51 | GAIN |
| response time (ms), 99th percentile | 5013 | 4832 | -3.6% | -601 to +239.1 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 16.39 | 12.72 | -22.4% | -4.639 to -2.707 | GAIN |
| failed requests (%) | 4.815 | 4.812 | -0.1% | -0.2874 to +0.2807 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.596 | 14.59 | +52.0% | +4.695 to +5.294 | power given |
| pods started | 5.371 | 10.49 | +95.2% | +4.563 to +5.665 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.589e-16 to +2.052e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.6 | 180.2 | +0.3% | +0.1149 to +1.043 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.6 | 180.2 | +0.3% | +0.1149 to +1.043 | power given |
| CPU used with Omni's own (cores), mean | 1.933 | 1.994 | +3.2% | +0.0489 to +0.07302 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.9 | 59.85 | +3.4% | +1.646 to +2.255 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1174 | 1126 | -4.1% | -218.4 to +122.6 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4132 | 4134 | +0.1% | -448.3 to +453.1 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 15.74 | 12.38 | -21.4% | -4.59 to -2.14 | GAIN |
| failed requests (%) | 4.049 | 4.135 | +2.1% | -0.1935 to +0.3655 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.523 | 14.07 | +47.7% | +4.082 to +5.005 | power given |
| pods started | 5.743 | 11.89 | +107.0% | +5.44 to +6.845 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.014e-16 to +2.461e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.8 | 179.4 | -0.2% | -0.8613 to +0.02635 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.8 | 179.4 | -0.2% | -0.8613 to +0.02635 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.912 | 1.964 | +2.7% | +0.04025 to +0.06425 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.28 | 59.06 | +3.1% | +1.425 to +2.133 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1679 | 1817 | +8.2% | -97.22 to +373.6 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5133 | 5076 | -1.1% | -432.6 to +320.3 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 24.93 | 20.59 | -17.4% | -5.772 to -2.903 | GAIN |
| failed requests (%) | 9.028 | 8.196 | -9.2% | -1.7 to +0.03617 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.623 | 14.51 | +50.8% | +4.618 to +5.161 | power given |
| pods started | 4.971 | 11.63 | +133.9% | +6.111 to +7.203 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.005e-16 to +3.99e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182 | 181.2 | -0.5% | -1.225 to -0.4216 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182 | 181.2 | -0.5% | -1.225 to -0.4216 | GAIN |
| CPU used with Omni's own (cores), mean | 2.102 | 2.144 | +2.0% | +0.03064 to +0.0541 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.39 | 64.14 | +2.8% | +1.496 to +1.997 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1068 | 1058 | -0.9% | -171.6 to +151.6 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 3677 | 3812 | +3.7% | -364.1 to +633.7 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 17.43 | 13.23 | -24.1% | -5.647 to -2.758 | GAIN |
| failed requests (%) | 6.502 | 5.736 | -11.8% | -1.361 to -0.1711 | GAIN |
| HPA replicas, mean | 9.604 | 14.34 | +49.4% | +4.471 to +5.01 | power given |
| pods started | 5.543 | 12.74 | +129.9% | +6.63 to +7.77 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.011e-15 to -4.159e-18 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.4 | 179.7 | -0.4% | -1.173 to -0.2444 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.4 | 179.7 | -0.4% | -1.173 to -0.2444 | GAIN |
| CPU used with Omni's own (cores), mean | 1.945 | 1.982 | +1.9% | +0.02556 to +0.04778 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.48 | 60.12 | +2.8% | +1.276 to +2.002 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
