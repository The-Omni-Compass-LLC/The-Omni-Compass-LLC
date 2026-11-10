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
| response time (ms), 95th percentile | 1890 | 1594 | 1309 | 1155 | 1478 | 1490 | 1561 | 1786 | 1197 | 1432 |
| response time (ms), 99th percentile | 5361 | 5298 | 4539 | 4669 | 5044 | 4987 | 4512 | 4741 | 4083 | 4716 |
| time over the response line (% of samples) | 18.32 | 14.25 | 18.34 | 14.11 | 17.52 | 13.11 | 23.86 | 20.43 | 20.93 | 16.56 |
| failed requests (%) | 5.791 | 5.608 | 6.909 | 6.361 | 5.45 | 5.022 | 8.855 | 8.826 | 8.567 | 7.565 |
| HPA replicas, mean | 9.59 | 14.45 | 9.622 | 14.37 | 9.595 | 14.32 | 9.595 | 14.32 | 9.627 | 14.19 |
| pods started | 5.3 | 11.2 | 5.32 | 12.44 | 5.2 | 11.16 | 5.08 | 11.34 | 5.18 | 11.98 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 179.9 | 180.4 | 180.9 | 180.1 | 179.8 | 180.1 | 181.4 | 181 | 181 | 180.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.9 | 180.4 | 180.9 | 180.1 | 179.8 | 180.1 | 181.4 | 181 | 181 | 180.4 |
| CPU used with Omni's own (cores), mean | 1.974 | 2.025 | 2.005 | 2.046 | 1.948 | 1.998 | 2.061 | 2.11 | 2.01 | 2.046 |
| host CPU busy, the real machine under kind (%) | 58.63 | 60.54 | 59.62 | 61.21 | 58.07 | 59.59 | 61.17 | 62.98 | 60.01 | 61.68 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.084 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1890 | 1594 | -15.7% | -598.3 to +6.241 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5361 | 5298 | -1.2% | -394.9 to +269.5 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 18.32 | 14.25 | -22.2% | -4.906 to -3.242 | GAIN |
| failed requests (%) | 5.791 | 5.608 | -3.2% | -0.4926 to +0.1272 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.59 | 14.45 | +50.7% | +4.59 to +5.128 | power given |
| pods started | 5.3 | 11.2 | +111.3% | +5.497 to +6.303 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.133e-16 to +8.043e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.9 | 180.4 | +0.3% | +0.1908 to +0.887 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.9 | 180.4 | +0.3% | +0.1908 to +0.887 | power given |
| CPU used with Omni's own (cores), mean | 1.974 | 2.025 | +2.6% | +0.04254 to +0.05884 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.63 | 60.54 | +3.3% | +1.646 to +2.185 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.984e+05 to +7.996e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.416e-05 to -9.401e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 6 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 1

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1309 | 1155 | -11.7% | -290.4 to -15.83 | GAIN |
| response time (ms), 99th percentile | 4539 | 4669 | +2.9% | -263.8 to +523.3 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 18.34 | 14.11 | -23.1% | -5.363 to -3.101 | GAIN |
| failed requests (%) | 6.909 | 6.361 | -7.9% | -1.042 to -0.0553 | GAIN |
| HPA replicas, mean | 9.622 | 14.37 | +49.3% | +4.492 to +4.994 | power given |
| pods started | 5.32 | 12.44 | +133.8% | +6.719 to +7.521 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.498e-16 to +2.787e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.9 | 180.1 | -0.5% | -1.288 to -0.4055 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.9 | 180.1 | -0.5% | -1.288 to -0.4055 | GAIN |
| CPU used with Omni's own (cores), mean | 2.005 | 2.046 | +2.0% | +0.03169 to +0.04916 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.62 | 61.21 | +2.7% | +1.355 to +1.839 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.623e+05 to +8.626e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.151e-05 to -8.148e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1478 | 1490 | +0.8% | -239.3 to +262.8 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5044 | 4987 | -1.1% | -395.6 to +280.3 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 17.52 | 13.11 | -25.2% | -5.345 to -3.483 | GAIN |
| failed requests (%) | 5.45 | 5.022 | -7.9% | -0.7833 to -0.0736 | GAIN |
| HPA replicas, mean | 9.595 | 14.32 | +49.2% | +4.394 to +5.056 | power given |
| pods started | 5.2 | 11.16 | +114.6% | +5.504 to +6.416 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +3.229e-17 to +6.072e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.8 | 180.1 | +0.2% | -0.06051 to +0.6325 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.8 | 180.1 | +0.2% | -0.06051 to +0.6325 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.948 | 1.998 | +2.5% | +0.04315 to +0.05619 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.07 | 59.59 | +2.6% | +1.325 to +1.705 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1561 | 1786 | +14.4% | +20.14 to +429.3 | LOSS |
| response time (ms), 99th percentile | 4512 | 4741 | +5.1% | -118.2 to +576.5 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 23.86 | 20.43 | -14.4% | -4.683 to -2.181 | GAIN |
| failed requests (%) | 8.855 | 8.826 | -0.3% | -0.7392 to +0.6817 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.595 | 14.32 | +49.2% | +4.462 to +4.98 | power given |
| pods started | 5.08 | 11.34 | +123.2% | +5.823 to +6.697 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.623e-16 to +3.202e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.4 | 181 | -0.2% | -0.7611 to -0.07799 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.4 | 181 | -0.2% | -0.7611 to -0.07799 | GAIN |
| CPU used with Omni's own (cores), mean | 2.061 | 2.11 | +2.4% | +0.04137 to +0.05671 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.17 | 62.98 | +3.0% | +1.58 to +2.046 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 0

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1197 | 1432 | +19.6% | +48.63 to +421.4 | LOSS |
| response time (ms), 99th percentile | 4083 | 4716 | +15.5% | +190.7 to +1075 | LOSS |
| time over the response line (% of samples) | 20.93 | 16.56 | -20.9% | -5.509 to -3.238 | GAIN |
| failed requests (%) | 8.567 | 7.565 | -11.7% | -1.599 to -0.4047 | GAIN |
| HPA replicas, mean | 9.627 | 14.19 | +47.4% | +4.283 to +4.839 | power given |
| pods started | 5.18 | 11.98 | +131.3% | +6.348 to +7.252 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.86e-16 to +5.31e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 180.4 | -0.3% | -0.9858 to -0.2214 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181 | 180.4 | -0.3% | -0.9858 to -0.2214 | GAIN |
| CPU used with Omni's own (cores), mean | 2.01 | 2.046 | +1.8% | +0.02766 to +0.04556 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.01 | 61.68 | +2.8% | +1.431 to +1.907 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.084 | +0.084 | +0.0707 to +0.0973 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Energy / Facility / Industrial
- Distribution / Specialized

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
