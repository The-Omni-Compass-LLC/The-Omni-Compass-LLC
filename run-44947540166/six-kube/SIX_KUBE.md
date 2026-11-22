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
| response time (ms), 95th percentile | 1468 | 1268 | 1305 | 1740 | 1534 | 1314 | 1679 | 1325 | 1351 | 1354 | 1476 | 1638 | 1158 | 1379 |
| response time (ms), 99th percentile | 4371 | 4239 | 4341 | 5413 | 5240 | 4936 | 5494 | 5232 | 3867 | 4029 | 4166 | 4310 | 4260 | 4468 |
| time over the response line (% of samples) | 14.74 | 11.4 | 24.56 | 20.25 | 17.62 | 13.36 | 17.61 | 13.27 | 19.79 | 14.79 | 21.23 | 17.96 | 20.58 | 16.11 |
| failed requests (%) | 4.656 | 4.427 | 10.5 | 9.269 | 5.721 | 5.24 | 5.275 | 5.086 | 6.063 | 5.742 | 7.515 | 6.885 | 8.076 | 7.021 |
| HPA replicas, mean | 9.551 | 14.14 | 9.668 | 14.55 | 9.606 | 14.44 | 9.598 | 14.44 | 9.541 | 13.92 | 9.571 | 14.34 | 9.632 | 14.4 |
| pods started | 5.429 | 11.74 | 5.086 | 11.37 | 5.2 | 10.89 | 5.4 | 11.66 | 5.486 | 12.03 | 5.429 | 11.49 | 5.343 | 12.2 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 178.5 | 179 | 182.5 | 181.8 | 180.1 | 180.1 | 179.9 | 180.5 | 180.5 | 179.7 | 180.8 | 180.5 | 181.7 | 181 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.5 | 179 | 182.5 | 181.8 | 180.1 | 180.1 | 179.9 | 180.5 | 180.5 | 179.7 | 180.8 | 180.5 | 181.7 | 181 |
| CPU used with Omni's own (cores), mean | 1.823 | 1.878 | 2.15 | 2.192 | 1.967 | 2.014 | 1.962 | 2.015 | 1.962 | 2.005 | 2.008 | 2.052 | 2.07 | 2.103 |
| host CPU busy, the real machine under kind (%) | 54.77 | 56.43 | 63.93 | 65.74 | 59 | 60.48 | 58.57 | 60.34 | 58.71 | 60.39 | 60.02 | 61.82 | 61.91 | 63.46 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1468 | 1268 | -13.6% | -448.9 to +49.19 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4371 | 4239 | -3.0% | -455.2 to +190.6 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 14.74 | 11.4 | -22.7% | -4.296 to -2.382 | GAIN |
| failed requests (%) | 4.656 | 4.427 | -4.9% | -0.5554 to +0.09916 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.551 | 14.14 | +48.0% | +4.187 to +4.991 | power given |
| pods started | 5.429 | 11.74 | +116.3% | +5.739 to +6.89 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.639e-16 to +5.162e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.5 | 179 | +0.3% | +0.1089 to +0.8825 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.5 | 179 | +0.3% | +0.1089 to +0.8825 | power given |
| CPU used with Omni's own (cores), mean | 1.823 | 1.878 | +3.0% | +0.04632 to +0.06306 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 54.77 | 56.43 | +3.0% | +1.395 to +1.932 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.985e+05 to +8.003e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.424e-05 to -9.402e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 0

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1305 | 1740 | +33.4% | +206 to +664.3 | LOSS |
| response time (ms), 99th percentile | 4341 | 5413 | +24.7% | +514.4 to +1629 | LOSS |
| time over the response line (% of samples) | 24.56 | 20.25 | -17.5% | -5.941 to -2.675 | GAIN |
| failed requests (%) | 10.5 | 9.269 | -11.7% | -2.084 to -0.3803 | GAIN |
| HPA replicas, mean | 9.668 | 14.55 | +50.5% | +4.652 to +5.111 | power given |
| pods started | 5.086 | 11.37 | +123.6% | +5.768 to +6.803 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.488e-16 to +3.473e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.5 | 181.8 | -0.4% | -1.079 to -0.2879 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.5 | 181.8 | -0.4% | -1.079 to -0.2879 | GAIN |
| CPU used with Omni's own (cores), mean | 2.15 | 2.192 | +1.9% | +0.03151 to +0.05129 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.93 | 65.74 | +2.8% | +1.511 to +2.117 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.622e+05 to +8.626e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.15e-05 to -8.147e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1534 | 1314 | -14.3% | -489.7 to +50.62 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5240 | 4936 | -5.8% | -741.6 to +133.2 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 17.62 | 13.36 | -24.2% | -5.244 to -3.276 | GAIN |
| failed requests (%) | 5.721 | 5.24 | -8.4% | -0.7638 to -0.1983 | GAIN |
| HPA replicas, mean | 9.606 | 14.44 | +50.3% | +4.422 to +5.242 | power given |
| pods started | 5.2 | 10.89 | +109.3% | +5.098 to +6.273 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.437e-16 to +4.467e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.1 | 180.1 | -0.0% | -0.5047 to +0.3769 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.1 | 180.1 | -0.0% | -0.5047 to +0.3769 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.967 | 2.014 | +2.4% | +0.03891 to +0.05621 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59 | 60.48 | +2.5% | +1.265 to +1.679 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1679 | 1325 | -21.1% | -578.5 to -131 | GAIN |
| response time (ms), 99th percentile | 5494 | 5232 | -4.8% | -665.1 to +140.6 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 17.61 | 13.27 | -24.6% | -5.476 to -3.206 | GAIN |
| failed requests (%) | 5.275 | 5.086 | -3.6% | -0.5183 to +0.1393 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.598 | 14.44 | +50.5% | +4.542 to +5.146 | power given |
| pods started | 5.4 | 11.66 | +115.9% | +5.776 to +6.738 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.608e-16 to +2.563e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.9 | 180.5 | +0.4% | +0.2742 to +1.057 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.9 | 180.5 | +0.4% | +0.2742 to +1.057 | power given |
| CPU used with Omni's own (cores), mean | 1.962 | 2.015 | +2.7% | +0.0434 to +0.06188 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.57 | 60.34 | +3.0% | +1.516 to +2.023 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1351 | 1354 | +0.2% | -179.8 to +185.8 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3867 | 4029 | +4.2% | -226.3 to +549.6 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 19.79 | 14.79 | -25.3% | -6.62 to -3.38 | GAIN |
| failed requests (%) | 6.063 | 5.742 | -5.3% | -0.584 to -0.05802 | GAIN |
| HPA replicas, mean | 9.541 | 13.92 | +45.9% | +3.888 to +4.873 | power given |
| pods started | 5.486 | 12.03 | +119.3% | +5.929 to +7.157 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.203e-16 to +3.188e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.5 | 179.7 | -0.5% | -1.195 to -0.4399 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.5 | 179.7 | -0.5% | -1.195 to -0.4399 | GAIN |
| CPU used with Omni's own (cores), mean | 1.962 | 2.005 | +2.2% | +0.03229 to +0.05399 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.71 | 60.39 | +2.9% | +1.35 to +2.02 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1476 | 1638 | +10.9% | -89.63 to +412.4 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4166 | 4310 | +3.5% | -401.7 to +690.2 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 21.23 | 17.96 | -15.4% | -4.537 to -1.989 | GAIN |
| failed requests (%) | 7.515 | 6.885 | -8.4% | -1.629 to +0.368 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.571 | 14.34 | +49.8% | +4.422 to +5.113 | power given |
| pods started | 5.429 | 11.49 | +111.6% | +5.558 to +6.557 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.292e-16 to +1.201e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.8 | 180.5 | -0.2% | -0.7557 to +0.08641 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.8 | 180.5 | -0.2% | -0.7557 to +0.08641 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.008 | 2.052 | +2.2% | +0.03324 to +0.05517 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.02 | 61.82 | +3.0% | +1.516 to +2.076 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 1

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1158 | 1379 | +19.2% | +33.56 to +410.2 | LOSS |
| response time (ms), 99th percentile | 4260 | 4468 | +4.9% | -302.9 to +717 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 20.58 | 16.11 | -21.7% | -5.928 to -3.021 | GAIN |
| failed requests (%) | 8.076 | 7.021 | -13.1% | -1.825 to -0.284 | GAIN |
| HPA replicas, mean | 9.632 | 14.4 | +49.5% | +4.464 to +5.075 | power given |
| pods started | 5.343 | 12.2 | +128.3% | +6.343 to +7.372 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.286e-16 to +2.226e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.7 | 181 | -0.4% | -1.159 to -0.2782 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.7 | 181 | -0.4% | -1.159 to -0.2782 | GAIN |
| CPU used with Omni's own (cores), mean | 2.07 | 2.103 | +1.6% | +0.02199 to +0.04327 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.91 | 63.46 | +2.5% | +1.275 to +1.813 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
