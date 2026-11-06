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
| response time (ms), 95th percentile | 1353 | 1178 | 1132 | 1237 | 1215 | 1025 | 1600 | 1453 | 1379 | 1320 | 1497 | 1648 | 1277 | 1318 |
| response time (ms), 99th percentile | 4764 | 4547 | 4302 | 4254 | 4024 | 3923 | 5182 | 5021 | 4250 | 4150 | 4392 | 4774 | 4059 | 4173 |
| time over the response line (% of samples) | 16.66 | 12.44 | 18.15 | 14.19 | 13.12 | 10.03 | 16.89 | 13.12 | 20.56 | 16.09 | 23.9 | 19.08 | 21.44 | 16.7 |
| failed requests (%) | 5.482 | 5.06 | 7.773 | 6.553 | 3.918 | 3.839 | 5.112 | 4.958 | 6.444 | 6.232 | 8.996 | 7.631 | 9.127 | 8.014 |
| HPA replicas, mean | 9.576 | 14.15 | 9.591 | 14.33 | 9.54 | 13.77 | 9.595 | 14.1 | 9.567 | 14.14 | 9.58 | 14.3 | 9.626 | 13.94 |
| pods started | 5.171 | 11.46 | 5.571 | 12.34 | 5.4 | 11.23 | 5.086 | 11.14 | 5.086 | 11.31 | 5.286 | 11.77 | 5.143 | 12.37 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 178.8 | 179.2 | 180.6 | 179.9 | 177.8 | 178.3 | 179.4 | 180.1 | 180.7 | 180.1 | 181.2 | 180.4 | 180.8 | 180.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.8 | 179.2 | 180.6 | 179.9 | 177.8 | 178.3 | 179.4 | 180.1 | 180.7 | 180.1 | 181.2 | 180.4 | 180.8 | 180.4 |
| CPU used with Omni's own (cores), mean | 1.855 | 1.9 | 1.948 | 1.983 | 1.759 | 1.813 | 1.912 | 1.957 | 1.985 | 2.027 | 2.057 | 2.1 | 2 | 2.036 |
| host CPU busy, the real machine under kind (%) | 55.41 | 56.86 | 58.16 | 59.64 | 52.66 | 54.21 | 56.81 | 58.43 | 59.03 | 60.65 | 60.98 | 62.66 | 59.79 | 61.44 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.09714 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1353 | 1178 | -12.9% | -400.9 to +51.38 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4764 | 4547 | -4.5% | -540.8 to +107.5 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 16.66 | 12.44 | -25.4% | -5.594 to -2.856 | GAIN |
| failed requests (%) | 5.482 | 5.06 | -7.7% | -0.8706 to +0.02496 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.576 | 14.15 | +47.7% | +4.137 to +5.004 | power given |
| pods started | 5.171 | 11.46 | +121.5% | +5.654 to +6.918 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.063e-16 to +5.108e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.8 | 179.2 | +0.2% | -0.02496 to +0.827 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.8 | 179.2 | +0.2% | -0.02496 to +0.827 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.855 | 1.9 | +2.4% | +0.0336 to +0.0564 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.41 | 56.86 | +2.6% | +1.135 to +1.76 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.981e+05 to +8e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.42e-05 to -9.398e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1132 | 1237 | +9.3% | -93.46 to +303.9 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4302 | 4254 | -1.1% | -665.4 to +569.6 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 18.15 | 14.19 | -21.9% | -5.536 to -2.399 | GAIN |
| failed requests (%) | 7.773 | 6.553 | -15.7% | -2.339 to -0.1016 | GAIN |
| HPA replicas, mean | 9.591 | 14.33 | +49.4% | +4.449 to +5.022 | power given |
| pods started | 5.571 | 12.34 | +121.5% | +6.131 to +7.412 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.424e-16 to +8.263e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.6 | 179.9 | -0.3% | -1.061 to -0.1758 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.6 | 179.9 | -0.3% | -1.061 to -0.1758 | GAIN |
| CPU used with Omni's own (cores), mean | 1.948 | 1.983 | +1.8% | +0.02346 to +0.04723 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.16 | 59.64 | +2.5% | +1.144 to +1.808 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.622e+05 to +8.626e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.15e-05 to -8.146e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1215 | 1025 | -15.6% | -422.1 to +42.02 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4024 | 3923 | -2.5% | -579.2 to +377.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 13.12 | 10.03 | -23.6% | -4.176 to -2.019 | GAIN |
| failed requests (%) | 3.918 | 3.839 | -2.0% | -0.3686 to +0.2102 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.54 | 13.77 | +44.4% | +3.717 to +4.75 | power given |
| pods started | 5.4 | 11.23 | +107.9% | +5.175 to +6.482 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.757e-16 to +5.309e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 177.8 | 178.3 | +0.3% | +0.1893 to +0.9075 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 177.8 | 178.3 | +0.3% | +0.1893 to +0.9075 | power given |
| CPU used with Omni's own (cores), mean | 1.759 | 1.813 | +3.1% | +0.04058 to +0.0668 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 52.66 | 54.21 | +2.9% | +1.17 to +1.92 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1600 | 1453 | -9.2% | -295.6 to +2.227 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5182 | 5021 | -3.1% | -454 to +132.5 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 16.89 | 13.12 | -22.3% | -4.819 to -2.715 | GAIN |
| failed requests (%) | 5.112 | 4.958 | -3.0% | -0.4147 to +0.1063 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.595 | 14.1 | +47.0% | +4.046 to +4.964 | power given |
| pods started | 5.086 | 11.14 | +119.1% | +5.418 to +6.697 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.44e-16 to +3.41e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.4 | 180.1 | +0.4% | +0.3761 to +1.068 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.4 | 180.1 | +0.4% | +0.3761 to +1.068 | power given |
| CPU used with Omni's own (cores), mean | 1.912 | 1.957 | +2.4% | +0.03297 to +0.05707 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.81 | 58.43 | +2.9% | +1.299 to +1.945 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1379 | 1320 | -4.3% | -271.8 to +153.8 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4250 | 4150 | -2.4% | -525.2 to +324.2 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 20.56 | 16.09 | -21.8% | -5.839 to -3.111 | GAIN |
| failed requests (%) | 6.444 | 6.232 | -3.3% | -0.5301 to +0.1072 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.567 | 14.14 | +47.8% | +4.149 to +5.002 | power given |
| pods started | 5.086 | 11.31 | +122.5% | +5.605 to +6.852 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.599e-16 to +4.091e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.7 | 180.1 | -0.3% | -1.047 to -0.1546 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.7 | 180.1 | -0.3% | -1.047 to -0.1546 | GAIN |
| CPU used with Omni's own (cores), mean | 1.985 | 2.027 | +2.1% | +0.03037 to +0.05461 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.03 | 60.65 | +2.7% | +1.344 to +1.896 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1497 | 1648 | +10.1% | -65.45 to +368 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4392 | 4774 | +8.7% | -142.7 to +907 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 23.9 | 19.08 | -20.2% | -6.462 to -3.183 | GAIN |
| failed requests (%) | 8.996 | 7.631 | -15.2% | -2.156 to -0.5744 | GAIN |
| HPA replicas, mean | 9.58 | 14.3 | +49.3% | +4.434 to +5.01 | power given |
| pods started | 5.286 | 11.77 | +122.7% | +6.004 to +6.967 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.524e-16 to -1.044e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.2 | 180.4 | -0.4% | -1.296 to -0.2595 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.2 | 180.4 | -0.4% | -1.296 to -0.2595 | GAIN |
| CPU used with Omni's own (cores), mean | 2.057 | 2.1 | +2.1% | +0.03125 to +0.05446 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.98 | 62.66 | +2.8% | +1.395 to +1.979 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1277 | 1318 | +3.2% | -169.4 to +251.1 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4059 | 4173 | +2.8% | -471.5 to +700.5 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 21.44 | 16.7 | -22.1% | -6.345 to -3.12 | GAIN |
| failed requests (%) | 9.127 | 8.014 | -12.2% | -1.832 to -0.3931 | GAIN |
| HPA replicas, mean | 9.626 | 13.94 | +44.8% | +3.939 to +4.684 | power given |
| pods started | 5.143 | 12.37 | +140.6% | +6.627 to +7.83 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.116e-16 to +1.105e-18 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.8 | 180.4 | -0.2% | -0.8957 to +0.06494 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.8 | 180.4 | -0.2% | -0.8957 to +0.06494 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2 | 2.036 | +1.8% | +0.02203 to +0.04971 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.79 | 61.44 | +2.8% | +1.329 to +1.978 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.09714 | +0.0971 | +0.08699 to +0.1073 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
