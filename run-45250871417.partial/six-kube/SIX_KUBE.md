# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 100 copies: native | The spine, the muscles every stack runs on, 100 copies: omni | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3571 | 2986 | 4206 | 4322 | 3802 | 2999 |
| response time (ms), 99th percentile | 6124 | 5772 | 6489 | 6575 | 5710 | 5363 |
| time over the response line (% of samples) | 55.04 | 54.86 | 56.03 | 58.38 | 48.35 | 47.35 |
| failed requests (%) | 38.92 | 42.08 | 39.45 | 42.22 | 33.12 | 34.35 |
| HPA replicas, mean | 9.822 | 12.63 | 9.809 | 11.36 | 9.79 | 12.17 |
| pods started | 3.663 | 8.928 | 4.337 | 7.434 | 4.542 | 9.494 |
| worker nodes in service, mean | 6 | 5.998 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 277.2 | 277.3 | 277.5 | 277.6 | 275.9 | 275.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.2 | 277.2 | 277.5 | 277.6 | 275.9 | 275.6 |
| CPU used with Omni's own (cores), mean | 2.48 | 2.528 | 2.497 | 2.549 | 2.383 | 2.433 |
| host CPU busy, the real machine under kind (%) | 73.87 | 78.69 | 75.83 | 84.43 | 73.11 | 78.78 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 |
| organism behind its window (s) | 0.4313 | 0.5325 | 0.806 | 1.199 | 0.6675 | 0.3964 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 2 (response time (ms), 95th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

83 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3571 | 2986 | -16.4% | -1036 to -133 | GAIN |
| response time (ms), 99th percentile | 6124 | 5772 | -5.7% | -877.6 to +175 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 55.04 | 54.86 | -0.3% | -1.135 to +0.7895 | STEADY, inside the noise (cut) |
| failed requests (%) | 38.92 | 42.08 | +8.1% | +1.794 to +4.521 | LOSS |
| HPA replicas, mean | 9.822 | 12.63 | +28.6% | +2.362 to +3.248 | power given |
| pods started | 3.663 | 8.928 | +143.8% | +4.747 to +5.783 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.005571 to +0.001843 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.2 | 277.3 | +0.0% | -0.3246 to +0.4896 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.2 | 277.2 | +0.0% | -0.4334 to +0.4859 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.48 | 2.528 | +2.0% | +0.04098 to +0.05655 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.87 | 78.69 | +6.5% | +4.628 to +4.994 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.4313 | 0.5325 | +23.5% | +0.07024 to +0.1322 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (time over the response line (% of samples); failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

83 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4206 | 4322 | +2.8% | -451.2 to +683.1 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6489 | 6575 | +1.3% | -376.6 to +547.3 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 56.03 | 58.38 | +4.2% | +0.7143 to +3.977 | LOSS |
| failed requests (%) | 39.45 | 42.22 | +7.0% | +0.1631 to +5.381 | LOSS |
| HPA replicas, mean | 9.809 | 11.36 | +15.8% | +1.08 to +2.016 | power given |
| pods started | 4.337 | 7.434 | +71.4% | +2.419 to +3.774 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +4.872e-16 to +1.204e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.5 | 277.6 | +0.0% | -0.359 to +0.4287 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.5 | 277.6 | +0.0% | -0.359 to +0.4287 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.497 | 2.549 | +2.1% | +0.03635 to +0.06805 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.83 | 84.43 | +11.3% | +8.174 to +9.025 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.806 | 1.199 | +48.7% | +0.3472 to +0.4384 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

83 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3802 | 2999 | -21.1% | -1340 to -265.1 | GAIN |
| response time (ms), 99th percentile | 5710 | 5363 | -6.1% | -816.3 to +122.3 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 48.35 | 47.35 | -2.1% | -1.919 to -0.08461 | GAIN |
| failed requests (%) | 33.12 | 34.35 | +3.7% | -0.931 to +3.383 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.79 | 12.17 | +24.3% | +1.909 to +2.857 | power given |
| pods started | 4.542 | 9.494 | +109.0% | +4.33 to +5.574 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.933e-16 to +4.715e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.9 | 275.6 | -0.1% | -0.6732 to +0.03431 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.9 | 275.6 | -0.1% | -0.6732 to +0.03431 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.383 | 2.433 | +2.1% | +0.03911 to +0.06106 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.11 | 78.78 | +7.8% | +5.383 to +5.959 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.6675 | 0.3964 | -40.6% | -0.3011 to -0.2411 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Energy / Facility / Industrial
- Distribution / Specialized
- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
