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
| response time (ms), 95th percentile | 1435 | 1098 | 1142 | 1219 | 1038 | 881.7 | 1471 | 1697 | 1263 | 1402 |
| response time (ms), 99th percentile | 4390 | 4272 | 4396 | 4744 | 4112 | 3783 | 4412 | 4524 | 4555 | 5030 |
| time over the response line (% of samples) | 15.33 | 11.54 | 19.67 | 15.06 | 11.5 | 8.466 | 22.95 | 19.53 | 21.82 | 16.73 |
| failed requests (%) | 4.72 | 4.685 | 8.167 | 6.819 | 2.658 | 2.635 | 8.622 | 8.214 | 8.805 | 7.469 |
| HPA replicas, mean | 9.566 | 14.27 | 9.618 | 14.2 | 9.551 | 14.17 | 9.572 | 14.3 | 9.657 | 14.26 |
| pods started | 5.34 | 11 | 5.36 | 12.16 | 5.64 | 11.62 | 5.36 | 11.38 | 5 | 12.38 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 178.9 | 179.4 | 180.6 | 180.3 | 178.4 | 178.7 | 181.3 | 180.7 | 181.6 | 180.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.9 | 179.4 | 180.6 | 180.3 | 178.4 | 178.7 | 181.3 | 180.7 | 181.6 | 180.7 |
| CPU used with Omni's own (cores), mean | 1.859 | 1.905 | 1.983 | 2.019 | 1.782 | 1.825 | 2.044 | 2.093 | 2.08 | 2.109 |
| host CPU busy, the real machine under kind (%) | 55.61 | 57.21 | 59.08 | 60.51 | 53.42 | 54.91 | 60.81 | 62.59 | 62.12 | 63.39 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.084 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1435 | 1098 | -23.5% | -604 to -70 | GAIN |
| response time (ms), 99th percentile | 4390 | 4272 | -2.7% | -474.3 to +238.4 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 15.33 | 11.54 | -24.7% | -4.81 to -2.765 | GAIN |
| failed requests (%) | 4.72 | 4.685 | -0.7% | -0.2576 to +0.189 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.566 | 14.27 | +49.2% | +4.373 to +5.036 | power given |
| pods started | 5.34 | 11 | +106.0% | +5.171 to +6.149 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.347e-16 to +1.794e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.9 | 179.4 | +0.3% | +0.1125 to +0.8596 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.9 | 179.4 | +0.3% | +0.1125 to +0.8596 | power given |
| CPU used with Omni's own (cores), mean | 1.859 | 1.905 | +2.5% | +0.03465 to +0.05798 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.61 | 57.21 | +2.9% | +1.3 to +1.891 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.985e+05 to +8.005e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.427e-05 to -9.403e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1142 | 1219 | +6.7% | -59.61 to +213.1 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4396 | 4744 | +7.9% | -48.09 to +744.2 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 19.67 | 15.06 | -23.4% | -5.853 to -3.373 | GAIN |
| failed requests (%) | 8.167 | 6.819 | -16.5% | -1.999 to -0.6961 | GAIN |
| HPA replicas, mean | 9.618 | 14.2 | +47.7% | +4.309 to +4.859 | power given |
| pods started | 5.36 | 12.16 | +126.9% | +6.351 to +7.249 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.364e-16 to -3.206e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.6 | 180.3 | -0.2% | -0.7001 to +0.03588 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.6 | 180.3 | -0.2% | -0.7001 to +0.03588 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.983 | 2.019 | +1.8% | +0.02739 to +0.04422 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.08 | 60.51 | +2.4% | +1.21 to +1.646 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.622e+05 to +8.625e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.149e-05 to -8.146e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1038 | 881.7 | -15.1% | -276.8 to -36.02 | GAIN |
| response time (ms), 99th percentile | 4112 | 3783 | -8.0% | -633.6 to -23.62 | GAIN |
| time over the response line (% of samples) | 11.5 | 8.466 | -26.4% | -3.743 to -2.327 | GAIN |
| failed requests (%) | 2.658 | 2.635 | -0.9% | -0.3114 to +0.2659 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.551 | 14.17 | +48.3% | +4.301 to +4.927 | power given |
| pods started | 5.64 | 11.62 | +106.0% | +5.568 to +6.392 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.89e-16 to +4.311e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.4 | 178.7 | +0.1% | +0.01354 to +0.5086 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.4 | 178.7 | +0.1% | +0.01354 to +0.5086 | power given |
| CPU used with Omni's own (cores), mean | 1.782 | 1.825 | +2.4% | +0.03343 to +0.0516 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 53.42 | 54.91 | +2.8% | +1.222 to +1.747 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1471 | 1697 | +15.4% | +40.19 to +411.7 | LOSS |
| response time (ms), 99th percentile | 4412 | 4524 | +2.5% | -240.9 to +464.4 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 22.95 | 19.53 | -14.9% | -4.592 to -2.232 | GAIN |
| failed requests (%) | 8.622 | 8.214 | -4.7% | -1.046 to +0.2289 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.572 | 14.3 | +49.3% | +4.443 to +5.003 | power given |
| pods started | 5.36 | 11.38 | +112.3% | +5.604 to +6.436 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.931e-16 to +2.089e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.3 | 180.7 | -0.3% | -0.8771 to -0.1721 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.3 | 180.7 | -0.3% | -0.8771 to -0.1721 | GAIN |
| CPU used with Omni's own (cores), mean | 2.044 | 2.093 | +2.4% | +0.03966 to +0.05919 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.81 | 62.59 | +2.9% | +1.53 to +2.031 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 1

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1263 | 1402 | +11.0% | -52.8 to +330.6 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4555 | 5030 | +10.4% | +22.43 to +926.8 | LOSS |
| time over the response line (% of samples) | 21.82 | 16.73 | -23.3% | -6.635 to -3.551 | GAIN |
| failed requests (%) | 8.805 | 7.469 | -15.2% | -2.064 to -0.6088 | GAIN |
| HPA replicas, mean | 9.657 | 14.26 | +47.7% | +4.378 to +4.829 | power given |
| pods started | 5 | 12.38 | +147.6% | +6.978 to +7.782 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.16e-16 to +1.607e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.6 | 180.7 | -0.5% | -1.335 to -0.5361 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.6 | 180.7 | -0.5% | -1.335 to -0.5361 | GAIN |
| CPU used with Omni's own (cores), mean | 2.08 | 2.109 | +1.4% | +0.01575 to +0.04209 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.12 | 63.39 | +2.0% | +0.8858 to +1.649 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.084 | +0.084 | +0.07201 to +0.09599 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Energy / Facility / Industrial
- Distribution / Specialized

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
