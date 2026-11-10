# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on: native | The spine, the muscles every stack runs on: omni | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1533 | 1240 | 1164 | 1127 | 1367 | 1359 | 1521 | 1490 | 1413 | 1729 |
| response time (ms), 99th percentile | 4663 | 4254 | 4578 | 4830 | 4456 | 4173 | 3861 | 4016 | 4737 | 5253 |
| time over the response line (% of samples) | 15.67 | 12.14 | 19.45 | 14.38 | 15.07 | 11.6 | 20.43 | 17.18 | 24.8 | 19.33 |
| failed requests (%) | 5.005 | 4.873 | 7.465 | 6.346 | 4.651 | 4.419 | 7.685 | 7.231 | 10.41 | 8.987 |
| HPA replicas, mean | 9.566 | 14.08 | 9.623 | 14.34 | 9.557 | 14.06 | 9.543 | 13.88 | 9.675 | 14.34 |
| pods started | 5.36 | 11.36 | 5.38 | 12.42 | 5.46 | 11.12 | 5.42 | 12.02 | 4.78 | 11.96 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 178.7 | 179.3 | 181.1 | 180.5 | 178.8 | 178.9 | 180 | 179.7 | 182.3 | 181.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.7 | 179.3 | 181.1 | 180.5 | 178.8 | 178.9 | 180 | 179.7 | 182.3 | 181.5 |
| CPU used with Omni's own (cores), mean | 1.853 | 1.895 | 2.016 | 2.051 | 1.849 | 1.893 | 1.932 | 1.98 | 2.132 | 2.174 |
| host CPU busy, the real machine under kind (%) | 55.41 | 56.8 | 60.04 | 61.44 | 55.21 | 56.94 | 57.72 | 59.53 | 63.54 | 65.19 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.09 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1533 | 1240 | -19.1% | -541.4 to -45.82 | GAIN |
| response time (ms), 99th percentile | 4663 | 4254 | -8.8% | -703.3 to -115.2 | GAIN |
| time over the response line (% of samples) | 15.67 | 12.14 | -22.6% | -4.398 to -2.672 | GAIN |
| failed requests (%) | 5.005 | 4.873 | -2.7% | -0.4424 to +0.177 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.566 | 14.08 | +47.2% | +4.128 to +4.896 | power given |
| pods started | 5.36 | 11.36 | +111.9% | +5.559 to +6.441 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.258e-16 to +9.944e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.7 | 179.3 | +0.3% | +0.1304 to +0.8919 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.7 | 179.3 | +0.3% | +0.1304 to +0.8919 | power given |
| CPU used with Omni's own (cores), mean | 1.853 | 1.895 | +2.3% | +0.03031 to +0.0542 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.41 | 56.8 | +2.5% | +1.113 to +1.656 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.983e+05 to +8.009e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.431e-05 to -9.4e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1164 | 1127 | -3.2% | -188.7 to +114.9 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4578 | 4830 | +5.5% | -123.6 to +627.5 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 19.45 | 14.38 | -26.1% | -6.328 to -3.804 | GAIN |
| failed requests (%) | 7.465 | 6.346 | -15.0% | -1.714 to -0.5253 | GAIN |
| HPA replicas, mean | 9.623 | 14.34 | +49.0% | +4.472 to +4.957 | power given |
| pods started | 5.38 | 12.42 | +130.9% | +6.52 to +7.56 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.383e-16 to +2.962e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.1 | 180.5 | -0.3% | -0.9983 to -0.1952 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.1 | 180.5 | -0.3% | -0.9983 to -0.1952 | GAIN |
| CPU used with Omni's own (cores), mean | 2.016 | 2.051 | +1.7% | +0.02528 to +0.04431 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.04 | 61.44 | +2.3% | +1.168 to +1.627 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.622e+05 to +8.625e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.15e-05 to -8.147e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1367 | 1359 | -0.6% | -259.2 to +242.7 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4456 | 4173 | -6.3% | -585.5 to +20.87 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 15.07 | 11.6 | -23.0% | -4.464 to -2.479 | GAIN |
| failed requests (%) | 4.651 | 4.419 | -5.0% | -0.5082 to +0.04356 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.557 | 14.06 | +47.2% | +4.109 to +4.905 | power given |
| pods started | 5.46 | 11.12 | +103.7% | +5.138 to +6.182 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.392e-16 to +2.326e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.8 | 178.9 | +0.1% | -0.2812 to +0.4717 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.8 | 178.9 | +0.1% | -0.2812 to +0.4717 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.849 | 1.893 | +2.4% | +0.03564 to +0.05325 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.21 | 56.94 | +3.1% | +1.472 to +1.99 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1521 | 1490 | -2.1% | -165.7 to +102.3 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 3861 | 4016 | +4.0% | -158.8 to +469.3 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 20.43 | 17.18 | -15.9% | -4.498 to -2.011 | GAIN |
| failed requests (%) | 7.685 | 7.231 | -5.9% | -1.08 to +0.1728 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.543 | 13.88 | +45.5% | +4.01 to +4.669 | power given |
| pods started | 5.42 | 12.02 | +121.8% | +6.031 to +7.169 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.146e-16 to +4.277e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180 | 179.7 | -0.2% | -0.6935 to +0.0258 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180 | 179.7 | -0.2% | -0.6935 to +0.0258 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.932 | 1.98 | +2.5% | +0.0369 to +0.0585 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.72 | 59.53 | +3.1% | +1.529 to +2.081 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 0

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1413 | 1729 | +22.4% | +99.93 to +531.9 | LOSS |
| response time (ms), 99th percentile | 4737 | 5253 | +10.9% | +59.95 to +973.7 | LOSS |
| time over the response line (% of samples) | 24.8 | 19.33 | -22.1% | -6.929 to -4.009 | GAIN |
| failed requests (%) | 10.41 | 8.987 | -13.6% | -2.215 to -0.6239 | GAIN |
| HPA replicas, mean | 9.675 | 14.34 | +48.2% | +4.45 to +4.879 | power given |
| pods started | 4.78 | 11.96 | +150.2% | +6.595 to +7.765 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.429e-16 to +7.443e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.3 | 181.5 | -0.5% | -1.224 to -0.4435 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.3 | 181.5 | -0.5% | -1.224 to -0.4435 | GAIN |
| CPU used with Omni's own (cores), mean | 2.132 | 2.174 | +2.0% | +0.03136 to +0.05395 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.54 | 65.19 | +2.6% | +1.362 to +1.95 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.09 | +0.09 | +0.07965 to +0.1004 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Energy / Facility / Industrial
- Distribution / Specialized

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
