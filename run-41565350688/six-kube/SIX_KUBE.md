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
| response time (ms), 95th percentile | 1826 | 1918 | 1311 | 1481 | 1573 | 1505 | 1572 | 1611 | 1550 | 1664 | 2017 | 2060 | 1438 | 1630 |
| response time (ms), 99th percentile | 5990 | 5976 | 4811 | 4767 | 5239 | 5004 | 5405 | 5161 | 4656 | 4560 | 5271 | 5132 | 5071 | 5273 |
| time over the response line (% of samples) | 24.2 | 18.49 | 22.19 | 17.22 | 17.58 | 14.18 | 18.8 | 14.78 | 23.21 | 18.55 | 28.54 | 24.07 | 26.56 | 20.82 |
| failed requests (%) | 9.255 | 8.149 | 9.521 | 7.989 | 6.089 | 5.803 | 6.372 | 6.112 | 7.524 | 7.401 | 11.17 | 10.1 | 11.4 | 9.883 |
| HPA replicas, mean | 9.643 | 14.59 | 9.652 | 14.13 | 9.585 | 13.96 | 9.628 | 14.45 | 9.59 | 14.17 | 9.639 | 14.41 | 9.672 | 14.16 |
| pods started | 4.714 | 10.23 | 4.971 | 11.91 | 5.114 | 10.94 | 4.857 | 11.23 | 4.943 | 10.94 | 4.629 | 11.37 | 4.857 | 11.69 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 181.1 | 181.5 | 181.4 | 180.5 | 179.4 | 179.8 | 180 | 180.8 | 181.4 | 180.9 | 182.4 | 182 | 182.5 | 181.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.1 | 181.5 | 181.4 | 180.5 | 179.4 | 179.8 | 180 | 180.8 | 181.4 | 180.9 | 182.4 | 182 | 182.5 | 181.5 |
| CPU used with Omni's own (cores), mean | 2.103 | 2.145 | 2.056 | 2.089 | 1.916 | 1.97 | 1.984 | 2.036 | 2.066 | 2.12 | 2.158 | 2.203 | 2.157 | 2.191 |
| host CPU busy, the real machine under kind (%) | 62.35 | 64.01 | 60.98 | 62.44 | 57.21 | 58.9 | 59.03 | 60.56 | 61.3 | 63.17 | 63.84 | 65.41 | 64.2 | 65.7 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.08857 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1826 | 1918 | +5.0% | -201.7 to +384.8 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5990 | 5976 | -0.2% | -428.6 to +400 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 24.2 | 18.49 | -23.6% | -7.166 to -4.265 | GAIN |
| failed requests (%) | 9.255 | 8.149 | -12.0% | -1.832 to -0.38 | GAIN |
| HPA replicas, mean | 9.643 | 14.59 | +51.3% | +4.656 to +5.229 | power given |
| pods started | 4.714 | 10.23 | +117.0% | +4.959 to +6.069 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.983e-16 to +2.416e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.1 | 181.5 | +0.2% | -0.1007 to +0.777 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.1 | 181.5 | +0.2% | -0.1007 to +0.777 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.103 | 2.145 | +2.0% | +0.02794 to +0.05575 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.35 | 64.01 | +2.7% | +1.306 to +2.01 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.976e+05 to +7.997e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.416e-05 to -9.393e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1311 | 1481 | +12.9% | -67.77 to +407.2 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4811 | 4767 | -0.9% | -641.3 to +552.6 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 22.19 | 17.22 | -22.4% | -6.857 to -3.092 | GAIN |
| failed requests (%) | 9.521 | 7.989 | -16.1% | -2.611 to -0.4531 | GAIN |
| HPA replicas, mean | 9.652 | 14.13 | +46.4% | +4.098 to +4.86 | power given |
| pods started | 4.971 | 11.91 | +139.7% | +6.403 to +7.482 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.309e-16 to +1.757e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.4 | 180.5 | -0.5% | -1.401 to -0.5225 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.4 | 180.5 | -0.5% | -1.401 to -0.5225 | GAIN |
| CPU used with Omni's own (cores), mean | 2.056 | 2.089 | +1.6% | +0.02159 to +0.04423 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.98 | 62.44 | +2.4% | +1.2 to +1.722 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.622e+05 to +8.626e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.15e-05 to -8.146e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1573 | 1505 | -4.4% | -335.8 to +198.7 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5239 | 5004 | -4.5% | -590.3 to +119.3 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 17.58 | 14.18 | -19.3% | -4.38 to -2.401 | GAIN |
| failed requests (%) | 6.089 | 5.803 | -4.7% | -0.6779 to +0.1068 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.585 | 13.96 | +45.6% | +3.888 to +4.852 | power given |
| pods started | 5.114 | 10.94 | +114.0% | +5.077 to +6.581 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.532e-16 to -6.184e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.4 | 179.8 | +0.2% | -0.0335 to +0.9175 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.4 | 179.8 | +0.2% | -0.0335 to +0.9175 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.916 | 1.97 | +2.8% | +0.04263 to +0.06456 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.21 | 58.9 | +3.0% | +1.398 to +1.991 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1572 | 1611 | +2.5% | -292 to +369.4 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5405 | 5161 | -4.5% | -580.3 to +91.96 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 18.8 | 14.78 | -21.4% | -5.145 to -2.897 | GAIN |
| failed requests (%) | 6.372 | 6.112 | -4.1% | -0.7067 to +0.1859 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.628 | 14.45 | +50.1% | +4.521 to +5.133 | power given |
| pods started | 4.857 | 11.23 | +131.2% | +5.8 to +6.943 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.698e-16 to +2.667e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180 | 180.8 | +0.4% | +0.3018 to +1.141 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180 | 180.8 | +0.4% | +0.3018 to +1.141 | power given |
| CPU used with Omni's own (cores), mean | 1.984 | 2.036 | +2.6% | +0.03964 to +0.0643 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.03 | 60.56 | +2.6% | +1.143 to +1.922 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1550 | 1664 | +7.4% | -133.2 to +361.8 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4656 | 4560 | -2.1% | -501.7 to +310.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 23.21 | 18.55 | -20.1% | -5.977 to -3.357 | GAIN |
| failed requests (%) | 7.524 | 7.401 | -1.6% | -0.3802 to +0.1339 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.59 | 14.17 | +47.7% | +4.109 to +5.046 | power given |
| pods started | 4.943 | 10.94 | +121.4% | +5.399 to +6.601 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.553e-16 to +2.538e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.4 | 180.9 | -0.3% | -1.035 to -0.1231 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.4 | 180.9 | -0.3% | -1.035 to -0.1231 | GAIN |
| CPU used with Omni's own (cores), mean | 2.066 | 2.12 | +2.6% | +0.04378 to +0.06383 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.3 | 63.17 | +3.0% | +1.553 to +2.179 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2017 | 2060 | +2.1% | -324.1 to +409.8 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5271 | 5132 | -2.6% | -694.9 to +416.5 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 28.54 | 24.07 | -15.7% | -6.102 to -2.834 | GAIN |
| failed requests (%) | 11.17 | 10.1 | -9.6% | -1.981 to -0.1588 | GAIN |
| HPA replicas, mean | 9.639 | 14.41 | +49.5% | +4.425 to +5.108 | power given |
| pods started | 4.629 | 11.37 | +145.7% | +6.118 to +7.368 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.333e-16 to +4.348e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.4 | 182 | -0.2% | -0.8025 to -0.007231 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.4 | 182 | -0.2% | -0.8025 to -0.007231 | GAIN |
| CPU used with Omni's own (cores), mean | 2.158 | 2.203 | +2.1% | +0.03505 to +0.05505 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.84 | 65.41 | +2.5% | +1.322 to +1.811 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1438 | 1630 | +13.3% | -32.55 to +416.3 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5071 | 5273 | +4.0% | -190.9 to +593.5 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 26.56 | 20.82 | -21.6% | -7.238 to -4.234 | GAIN |
| failed requests (%) | 11.4 | 9.883 | -13.3% | -2.197 to -0.8311 | GAIN |
| HPA replicas, mean | 9.672 | 14.16 | +46.4% | +4.159 to +4.815 | power given |
| pods started | 4.857 | 11.69 | +140.6% | +6.197 to +7.46 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.414e-16 to +2.891e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.5 | 181.5 | -0.5% | -1.347 to -0.5521 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.5 | 181.5 | -0.5% | -1.347 to -0.5521 | GAIN |
| CPU used with Omni's own (cores), mean | 2.157 | 2.191 | +1.6% | +0.02331 to +0.04363 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.2 | 65.7 | +2.3% | +1.216 to +1.777 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.08857 | +0.0886 | +0.07748 to +0.09966 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
