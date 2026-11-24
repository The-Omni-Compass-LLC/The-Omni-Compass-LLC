# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 100 copies: native | The spine, the muscles every stack runs on, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni |
|---|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3155 | 3044 | 4072 | 3696 |
| response time (ms), 99th percentile | 5734 | 5542 | 6380 | 6009 |
| time over the response line (% of samples) | 51.29 | 50.31 | 54.17 | 53.95 |
| failed requests (%) | 36.43 | 38.45 | 37.72 | 39.59 |
| HPA replicas, mean | 9.803 | 12.66 | 9.802 | 12.22 |
| pods started | 4.12 | 9.132 | 4.261 | 8.848 |
| worker nodes in service, mean | 5.999 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.5 | 276.5 | 277.1 | 276.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.5 | 276.5 | 277 | 276.8 |
| CPU used with Omni's own (cores), mean | 2.434 | 2.489 | 2.458 | 2.507 |
| host CPU busy, the real machine under kind (%) | 72.55 | 77.53 | 75.17 | 80.91 |
| organism work | 2.094e+12 | 2.094e+12 | 2.214e+12 | 2.214e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.98e+12 | 1.981e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 4.564 | 4.47 |
| organism work per energy | 1.514 | 1.513 | 1.118 | 1.117 |
| organism behind its window (s) | 0.4424 | 0.5308 | 0.6576 | 0.4076 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

91 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3145 | 3044 | -3.2% | -557.6 to +356.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5712 | 5542 | -3.0% | -571.7 to +233.6 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 51.04 | 50.31 | -1.4% | -1.504 to +0.04412 | STEADY, inside the noise (cut) |
| failed requests (%) | 36.19 | 38.45 | +6.2% | +1.178 to +3.336 | LOSS |
| HPA replicas, mean | 9.801 | 12.66 | +29.2% | +2.424 to +3.294 | power given |
| pods started | 4.165 | 9.132 | +119.3% | +4.416 to +5.518 | power given |
| worker nodes in service, mean | 5.999 | 6 | +0.0% | -0.0005818 to +0.001761 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.5 | 276.5 | +0.0% | -0.3413 to +0.3936 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.4 | 276.5 | +0.0% | -0.3274 to +0.4155 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.432 | 2.489 | +2.3% | +0.04695 to +0.06717 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.48 | 77.53 | +7.0% | +4.778 to +5.323 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.4429 | 0.5308 | +19.9% | +0.05464 to +0.1212 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

92 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4072 | 3696 | -9.2% | -861.3 to +109.4 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6380 | 6009 | -5.8% | -803 to +60.52 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 54.17 | 53.95 | -0.4% | -1.202 to +0.7533 | STEADY, inside the noise (cut) |
| failed requests (%) | 37.72 | 39.59 | +5.0% | +0.1721 to +3.578 | LOSS |
| HPA replicas, mean | 9.802 | 12.22 | +24.7% | +1.987 to +2.853 | power given |
| pods started | 4.261 | 8.848 | +107.7% | +3.927 to +5.247 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -0.0003096 to +0.0009375 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.1 | 276.8 | -0.1% | -0.5326 to +0.09661 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277 | 276.8 | -0.1% | -0.5214 to +0.1045 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.458 | 2.507 | +2.0% | +0.03648 to +0.06133 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.17 | 80.91 | +7.6% | +5.419 to +6.072 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.6576 | 0.4076 | -38.0% | -0.2873 to -0.2127 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Energy / Facility / Industrial
- Distribution / Specialized
- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
