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
| response time (ms), 95th percentile | 1271 | 1019 | 1189 | 1174 | 1281 | 1164 | 1207 | 1168 | 1290 | 1519 | 1400 | 1631 | 1232 | 1370 |
| response time (ms), 99th percentile | 4083 | 3804 | 4712 | 4250 | 4646 | 4307 | 4669 | 4522 | 4273 | 4882 | 3841 | 4008 | 5031 | 5394 |
| time over the response line (% of samples) | 13.61 | 10.01 | 18.47 | 14.77 | 14.66 | 11.4 | 15.97 | 11.52 | 20.83 | 16.15 | 20.98 | 17.93 | 20.15 | 16.72 |
| failed requests (%) | 3.926 | 3.686 | 6.946 | 6.603 | 4.649 | 4.504 | 4.812 | 4.303 | 6.288 | 5.778 | 8.195 | 7.234 | 7.788 | 7.374 |
| HPA replicas, mean | 9.562 | 14.3 | 9.608 | 14.35 | 9.583 | 14.01 | 9.585 | 14.26 | 9.551 | 14.23 | 9.589 | 14.13 | 9.637 | 14.2 |
| pods started | 5.45 | 11.4 | 5.5 | 12.4 | 5.2 | 10.9 | 5.4 | 10.95 | 5.5 | 11 | 4.9 | 12 | 5.15 | 12.7 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 5.999 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 178.5 | 178.7 | 180.9 | 180.2 | 178.9 | 179.1 | 179.3 | 179.9 | 181.4 | 180.5 | 180.4 | 180 | 181.6 | 180.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.5 | 178.7 | 180.9 | 180.2 | 178.9 | 179.1 | 179.3 | 179.9 | 181.4 | 180.5 | 180.4 | 179.9 | 181.6 | 180.6 |
| CPU used with Omni's own (cores), mean | 1.814 | 1.857 | 1.984 | 2.023 | 1.853 | 1.898 | 1.898 | 1.932 | 2.055 | 2.101 | 1.955 | 1.999 | 2.051 | 2.092 |
| host CPU busy, the real machine under kind (%) | 54.59 | 56.05 | 59.23 | 60.84 | 55.75 | 57.22 | 56.74 | 58.12 | 61.28 | 62.97 | 58.65 | 60.42 | 61.3 | 63.07 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.08 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1271 | 1019 | -19.8% | -585.2 to +81.07 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4083 | 3804 | -6.8% | -836.3 to +277.3 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 13.61 | 10.01 | -26.4% | -5.104 to -2.089 | GAIN |
| failed requests (%) | 3.926 | 3.686 | -6.1% | -0.9932 to +0.5149 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.562 | 14.3 | +49.5% | +4.201 to +5.273 | power given |
| pods started | 5.45 | 11.4 | +109.2% | +5.098 to +6.802 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.265e-16 to +4.265e-16 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 178.5 | 178.7 | +0.1% | -0.2526 to +0.7578 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.5 | 178.7 | +0.1% | -0.2526 to +0.7578 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.814 | 1.857 | +2.4% | +0.02826 to +0.05877 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 54.59 | 56.05 | +2.7% | +1.063 to +1.861 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.974e+05 to +8.008e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.43e-05 to -9.389e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1189 | 1174 | -1.2% | -227.5 to +198 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4712 | 4250 | -9.8% | -963 to +40.55 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 18.47 | 14.77 | -20.0% | -5.355 to -2.042 | GAIN |
| failed requests (%) | 6.946 | 6.603 | -4.9% | -1.127 to +0.4395 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.608 | 14.35 | +49.3% | +4.245 to +5.236 | power given |
| pods started | 5.5 | 12.4 | +125.5% | +6.295 to +7.505 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.836e-16 to +6.561e-18 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.9 | 180.2 | -0.4% | -1.36 to -0.144 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.9 | 180.2 | -0.4% | -1.36 to -0.144 | GAIN |
| CPU used with Omni's own (cores), mean | 1.984 | 2.023 | +2.0% | +0.02336 to +0.05449 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.23 | 60.84 | +2.7% | +1.236 to +1.989 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.622e+05 to +8.627e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.151e-05 to -8.146e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1281 | 1164 | -9.1% | -463.4 to +229.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4646 | 4307 | -7.3% | -963.4 to +284.4 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 14.66 | 11.4 | -22.3% | -4.661 to -1.866 | GAIN |
| failed requests (%) | 4.649 | 4.504 | -3.1% | -0.7133 to +0.4233 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.583 | 14.01 | +46.2% | +3.713 to +5.134 | power given |
| pods started | 5.2 | 10.9 | +109.6% | +4.895 to +6.505 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.353e-16 to +6.241e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.9 | 179.1 | +0.1% | -0.4824 to +0.7416 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.9 | 179.1 | +0.1% | -0.4824 to +0.7416 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.853 | 1.898 | +2.4% | +0.0263 to +0.06329 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.75 | 57.22 | +2.6% | +0.9707 to +1.969 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1207 | 1168 | -3.2% | -417.1 to +340 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4669 | 4522 | -3.1% | -713.9 to +420.1 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 15.97 | 11.52 | -27.8% | -6.046 to -2.835 | GAIN |
| failed requests (%) | 4.812 | 4.303 | -10.6% | -0.9189 to -0.09851 | GAIN |
| HPA replicas, mean | 9.585 | 14.26 | +48.7% | +4.12 to +5.224 | power given |
| pods started | 5.4 | 10.95 | +102.8% | +4.726 to +6.374 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.238e-16 to +1.797e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.3 | 179.9 | +0.4% | +0.1397 to +1.166 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.3 | 179.9 | +0.4% | +0.1397 to +1.166 | power given |
| CPU used with Omni's own (cores), mean | 1.898 | 1.932 | +1.8% | +0.006326 to +0.06142 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.74 | 58.12 | +2.4% | +0.6081 to +2.168 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1290 | 1519 | +17.8% | -82.16 to +541.3 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4273 | 4882 | +14.2% | -116.1 to +1333 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 20.83 | 16.15 | -22.5% | -6.284 to -3.073 | GAIN |
| failed requests (%) | 6.288 | 5.778 | -8.1% | -0.8751 to -0.1456 | GAIN |
| HPA replicas, mean | 9.551 | 14.23 | +49.0% | +3.978 to +5.38 | power given |
| pods started | 5.5 | 11 | +100.0% | +4.733 to +6.267 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.458e-16 to +2.018e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.4 | 180.5 | -0.5% | -1.586 to -0.3362 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.4 | 180.5 | -0.5% | -1.586 to -0.3362 | GAIN |
| CPU used with Omni's own (cores), mean | 2.055 | 2.101 | +2.2% | +0.02922 to +0.06204 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.28 | 62.97 | +2.7% | +1.35 to +2.013 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1400 | 1631 | +16.5% | -74.13 to +536.4 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3841 | 4008 | +4.4% | -385.4 to +719.9 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 20.98 | 17.93 | -14.5% | -4.743 to -1.344 | GAIN |
| failed requests (%) | 8.195 | 7.234 | -11.7% | -1.846 to -0.07529 | GAIN |
| HPA replicas, mean | 9.589 | 14.13 | +47.4% | +4.159 to +4.93 | power given |
| pods started | 4.9 | 12 | +144.9% | +6.327 to +7.873 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003697 to +0.001307 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.4 | 180 | -0.3% | -1.415 to +0.504 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.4 | 179.9 | -0.3% | -1.481 to +0.5221 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.955 | 1.999 | +2.2% | +0.03114 to +0.05657 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.65 | 60.42 | +3.0% | +1.414 to +2.133 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1232 | 1370 | +11.2% | -174 to +450.5 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5031 | 5394 | +7.2% | -197.1 to +922.7 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 20.15 | 16.72 | -17.0% | -4.819 to -2.031 | GAIN |
| failed requests (%) | 7.788 | 7.374 | -5.3% | -1.514 to +0.6868 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.637 | 14.2 | +47.3% | +4.084 to +5.035 | power given |
| pods started | 5.15 | 12.7 | +146.6% | +6.698 to +8.402 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.178e-16 to +2.073e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.6 | 180.6 | -0.5% | -1.633 to -0.2843 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.6 | 180.6 | -0.5% | -1.633 to -0.2843 | GAIN |
| CPU used with Omni's own (cores), mean | 2.051 | 2.092 | +2.0% | +0.01949 to +0.06194 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.3 | 63.07 | +2.9% | +1.277 to +2.265 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.08 | +0.08 | +0.06079 to +0.09921 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
