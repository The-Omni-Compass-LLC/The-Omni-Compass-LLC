# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 100 copies: native | The spine, the muscles every stack runs on, 100 copies: omni | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3738 | 3126 | 4158 | 3709 | 4101 | 2765 | 3986 | 3185 |
| response time (ms), 99th percentile | 5646 | 5349 | 6533 | 6050 | 6076 | 4981 | 5958 | 5518 |
| time over the response line (% of samples) | 45.99 | 46.69 | 53.42 | 55.39 | 51.96 | 51.19 | 53.46 | 52.44 |
| failed requests (%) | 30.66 | 33.6 | 36.34 | 40.62 | 35.16 | 40.21 | 37.93 | 39.38 |
| HPA replicas, mean | 9.781 | 12.98 | 9.792 | 11.29 | 9.799 | 11.98 | 9.815 | 11.62 |
| pods started | 4.548 | 10.13 | 4.548 | 7.726 | 4.242 | 9 | 3.935 | 8.21 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.7 | 275.8 | 277.4 | 277.2 | 276.4 | 276.3 | 276.6 | 276.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.7 | 275.8 | 277.4 | 277.2 | 276.4 | 276.3 | 276.6 | 276.5 |
| CPU used with Omni's own (cores), mean | 2.389 | 2.441 | 2.482 | 2.534 | 2.411 | 2.462 | 2.434 | 2.481 |
| host CPU busy, the real machine under kind (%) | 70.76 | 75.58 | 75.18 | 83.6 | 74.08 | 79.8 | 75.09 | 81.62 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 |
| organism behind its window (s) | 0.4323 | 0.5 | 0.8952 | 1.179 | 0.5935 | 0.4097 | 0.7613 | 0.4581 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 2 (response time (ms), 95th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3738 | 3126 | -16.4% | -1060 to -164.7 | GAIN |
| response time (ms), 99th percentile | 5646 | 5349 | -5.3% | -684.4 to +90.37 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 45.99 | 46.69 | +1.5% | -0.3282 to +1.725 | STEADY, inside the noise (up) |
| failed requests (%) | 30.66 | 33.6 | +9.6% | +0.908 to +4.982 | LOSS |
| HPA replicas, mean | 9.781 | 12.98 | +32.7% | +2.742 to +3.663 | power given |
| pods started | 4.548 | 10.13 | +122.7% | +4.85 to +6.312 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -0.0003572 to +0.001072 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.7 | 275.8 | +0.0% | -0.298 to +0.4228 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.7 | 275.8 | +0.0% | -0.2888 to +0.435 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.389 | 2.441 | +2.2% | +0.04151 to +0.06315 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.76 | 75.58 | +6.8% | +4.527 to +5.099 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.4323 | 0.5 | +15.7% | +0.02824 to +0.1072 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (time over the response line (% of samples); failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4158 | 3709 | -10.8% | -1083 to +183.5 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6533 | 6050 | -7.4% | -999.1 to +31.98 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 53.42 | 55.39 | +3.7% | +0.08957 to +3.852 | LOSS |
| failed requests (%) | 36.34 | 40.62 | +11.8% | +1.594 to +6.978 | LOSS |
| HPA replicas, mean | 9.792 | 11.29 | +15.3% | +0.9523 to +2.037 | power given |
| pods started | 4.548 | 7.726 | +69.9% | +2.478 to +3.877 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +2.657e-16 to +1.195e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.4 | 277.2 | -0.1% | -0.6214 to +0.2673 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.4 | 277.2 | -0.1% | -0.6214 to +0.2673 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.482 | 2.534 | +2.1% | +0.03429 to +0.07062 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.18 | 83.6 | +11.2% | +7.973 to +8.874 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.8952 | 1.179 | +31.7% | +0.2343 to +0.3334 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4101 | 2765 | -32.6% | -1953 to -719.8 | GAIN |
| response time (ms), 99th percentile | 6076 | 4981 | -18.0% | -1712 to -477.2 | GAIN |
| time over the response line (% of samples) | 51.96 | 51.19 | -1.5% | -1.681 to +0.1481 | STEADY, inside the noise (cut) |
| failed requests (%) | 35.16 | 40.21 | +14.4% | +3.107 to +7.007 | LOSS |
| HPA replicas, mean | 9.799 | 11.98 | +22.2% | +1.637 to +2.721 | power given |
| pods started | 4.242 | 9 | +112.2% | +3.871 to +5.645 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.001134 to +0.0003779 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.4 | 276.3 | -0.1% | -0.551 to +0.2629 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.4 | 276.3 | -0.1% | -0.5641 to +0.2532 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.411 | 2.462 | +2.1% | +0.03852 to +0.06319 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.08 | 79.8 | +7.7% | +5.424 to +6.011 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.5935 | 0.4097 | -31.0% | -0.2229 to -0.1448 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3986 | 3185 | -20.1% | -1438 to -164.6 | GAIN |
| response time (ms), 99th percentile | 5958 | 5518 | -7.4% | -1023 to +142.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 53.46 | 52.44 | -1.9% | -1.975 to -0.05195 | GAIN |
| failed requests (%) | 37.93 | 39.38 | +3.8% | -0.5864 to +3.499 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.815 | 11.62 | +18.4% | +1.22 to +2.386 | power given |
| pods started | 3.935 | 8.21 | +108.6% | +3.383 to +5.165 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -0.0004999 to +0.0015 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.6 | 276.5 | -0.1% | -0.6733 to +0.3359 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.6 | 276.5 | -0.1% | -0.6601 to +0.353 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.434 | 2.481 | +1.9% | +0.03263 to +0.0619 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.09 | 81.62 | +8.7% | +6.175 to +6.889 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | power given |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | power given |
| organism behind its window (s) | 0.7613 | 0.4581 | -39.8% | -0.3588 to -0.2477 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Distribution / Specialized
- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
