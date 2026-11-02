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
| response time (ms), 95th percentile | 1706 | 1690 | 1440 | 1466 | 1646 | 1642 | 1645 | 1596 | 1638 | 1696 | 1562 | 1483 | 1465 | 1739 |
| response time (ms), 99th percentile | 5008 | 5262 | 4764 | 4940 | 5241 | 5217 | 5087 | 5112 | 5041 | 4800 | 4610 | 4549 | 4400 | 5303 |
| time over the response line (% of samples) | 19.15 | 14.01 | 27.1 | 18.12 | 18.42 | 13.18 | 18.72 | 13.52 | 27.09 | 18.74 | 24.74 | 17.46 | 26.18 | 18.16 |
| failed requests (%) | 6.704 | 5.543 | 11.96 | 9.489 | 5.886 | 4.909 | 6.332 | 5.462 | 8.919 | 8.02 | 9.675 | 6.739 | 11.42 | 8.711 |
| HPA replicas, mean | 9.596 | 13.28 | 9.661 | 13.05 | 9.613 | 13.42 | 9.599 | 13.33 | 9.623 | 13.4 | 9.588 | 12.52 | 9.654 | 13 |
| pods started | 5.229 | 9.543 | 4.8 | 10.34 | 5 | 10.29 | 5.2 | 9.8 | 4.686 | 9.543 | 5.2 | 10.09 | 4.886 | 9.971 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 179.8 | 180.4 | 182.3 | 182.3 | 179.9 | 180.6 | 180 | 180.6 | 182.2 | 181.9 | 181.5 | 180.9 | 182.2 | 181.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.8 | 180.4 | 182.3 | 182.3 | 179.9 | 180.6 | 180 | 180.6 | 182.2 | 181.9 | 181.5 | 180.9 | 182.2 | 181.6 |
| CPU used with Omni's own (cores), mean | 1.966 | 1.972 | 2.14 | 2.124 | 1.975 | 1.977 | 1.974 | 1.966 | 2.152 | 2.139 | 2.055 | 2.044 | 2.125 | 2.108 |
| host CPU busy, the real machine under kind (%) | 58.51 | 58.55 | 63.5 | 63.49 | 58.77 | 58.93 | 58.7 | 58.51 | 63.67 | 63.91 | 61.2 | 61.01 | 63.32 | 63.33 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.09143 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1706 | 1690 | -0.9% | -355.3 to +323.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5008 | 5262 | +5.1% | -151.5 to +659.4 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 19.15 | 14.01 | -26.8% | -6.432 to -3.846 | GAIN |
| failed requests (%) | 6.704 | 5.543 | -17.3% | -1.714 to -0.6091 | GAIN |
| HPA replicas, mean | 9.596 | 13.28 | +38.4% | +2.953 to +4.413 | power given |
| pods started | 5.229 | 9.543 | +82.5% | +3.57 to +5.058 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.22e-16 to +6.222e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.8 | 180.4 | +0.3% | +0.2342 to +0.8817 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.8 | 180.4 | +0.3% | +0.2342 to +0.8817 | power given |
| CPU used with Omni's own (cores), mean | 1.966 | 1.972 | +0.3% | -0.004996 to +0.01672 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.51 | 58.55 | +0.1% | -0.2599 to +0.3404 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.978e+05 to +7.995e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.414e-05 to -9.394e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1440 | 1466 | +1.8% | -191.5 to +243 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4764 | 4940 | +3.7% | -335.9 to +688.5 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 27.1 | 18.12 | -33.1% | -11.3 to -6.664 | GAIN |
| failed requests (%) | 11.96 | 9.489 | -20.7% | -3.37 to -1.57 | GAIN |
| HPA replicas, mean | 9.661 | 13.05 | +35.1% | +2.768 to +4.01 | power given |
| pods started | 4.8 | 10.34 | +115.5% | +4.68 to +6.406 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.276e-16 to +3.261e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.3 | 182.3 | +0.0% | -0.3512 to +0.4516 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.3 | 182.3 | +0.0% | -0.3512 to +0.4516 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.14 | 2.124 | -0.7% | -0.03 to -0.001882 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.5 | 63.49 | -0.0% | -0.416 to +0.3997 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.618e+05 to +8.623e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.147e-05 to -8.142e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1646 | 1642 | -0.2% | -358.2 to +351.4 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5241 | 5217 | -0.5% | -429.4 to +382.2 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 18.42 | 13.18 | -28.4% | -6.624 to -3.847 | GAIN |
| failed requests (%) | 5.886 | 4.909 | -16.6% | -1.507 to -0.4469 | GAIN |
| HPA replicas, mean | 9.613 | 13.42 | +39.6% | +3.172 to +4.447 | power given |
| pods started | 5 | 10.29 | +105.7% | +4.463 to +6.109 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.75e-16 to +2.213e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.9 | 180.6 | +0.4% | +0.3566 to +1.003 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.9 | 180.6 | +0.4% | +0.3566 to +1.003 | power given |
| CPU used with Omni's own (cores), mean | 1.975 | 1.977 | +0.1% | -0.009075 to +0.01335 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.77 | 58.93 | +0.3% | -0.0427 to +0.3672 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1645 | 1596 | -2.9% | -353 to +256.1 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5087 | 5112 | +0.5% | -386.5 to +436.2 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 18.72 | 13.52 | -27.8% | -6.586 to -3.821 | GAIN |
| failed requests (%) | 6.332 | 5.462 | -13.7% | -1.346 to -0.3928 | GAIN |
| HPA replicas, mean | 9.599 | 13.33 | +38.9% | +3.03 to +4.435 | power given |
| pods started | 5.2 | 9.8 | +88.5% | +3.836 to +5.364 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.347e-16 to +6.423e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180 | 180.6 | +0.3% | +0.2271 to +0.8303 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180 | 180.6 | +0.3% | +0.2271 to +0.8303 | power given |
| CPU used with Omni's own (cores), mean | 1.974 | 1.966 | -0.5% | -0.02167 to +0.003822 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.7 | 58.51 | -0.3% | -0.5701 to +0.1909 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1638 | 1696 | +3.5% | -194.4 to +310.1 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5041 | 4800 | -4.8% | -577.9 to +96.27 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 27.09 | 18.74 | -30.8% | -10.53 to -6.161 | GAIN |
| failed requests (%) | 8.919 | 8.02 | -10.1% | -1.425 to -0.3742 | GAIN |
| HPA replicas, mean | 9.623 | 13.4 | +39.2% | +3.069 to +4.477 | power given |
| pods started | 4.686 | 9.543 | +103.7% | +3.975 to +5.739 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.907e-16 to +4.952e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.2 | 181.9 | -0.2% | -0.8442 to +0.0696 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.2 | 181.9 | -0.2% | -0.8442 to +0.0696 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.152 | 2.139 | -0.6% | -0.02266 to -0.002961 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.67 | 63.91 | +0.4% | -0.08394 to +0.5641 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.377e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1562 | 1483 | -5.1% | -279.8 to +120.7 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4610 | 4549 | -1.3% | -500 to +379 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 24.74 | 17.46 | -29.4% | -9.508 to -5.064 | GAIN |
| failed requests (%) | 9.675 | 6.739 | -30.3% | -4.13 to -1.743 | GAIN |
| HPA replicas, mean | 9.588 | 12.52 | +30.6% | +2.281 to +3.579 | power given |
| pods started | 5.2 | 10.09 | +94.0% | +4.096 to +5.675 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.979e-16 to +2.441e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.5 | 180.9 | -0.4% | -1.065 to -0.2161 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.5 | 180.9 | -0.4% | -1.065 to -0.2161 | GAIN |
| CPU used with Omni's own (cores), mean | 2.055 | 2.044 | -0.5% | -0.02222 to +0.0002268 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.2 | 61.01 | -0.3% | -0.5555 to +0.1772 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 0

35 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1465 | 1739 | +18.7% | +11.72 to +536.3 | LOSS |
| response time (ms), 99th percentile | 4400 | 5303 | +20.5% | +259 to +1547 | LOSS |
| time over the response line (% of samples) | 26.18 | 18.16 | -30.6% | -10.11 to -5.932 | GAIN |
| failed requests (%) | 11.42 | 8.711 | -23.7% | -3.678 to -1.738 | GAIN |
| HPA replicas, mean | 9.654 | 13 | +34.6% | +2.764 to +3.919 | power given |
| pods started | 4.886 | 9.971 | +104.1% | +4.303 to +5.869 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.744e-16 to +1.146e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.2 | 181.6 | -0.3% | -1.085 to -0.1054 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.2 | 181.6 | -0.3% | -1.085 to -0.1054 | GAIN |
| CPU used with Omni's own (cores), mean | 2.125 | 2.108 | -0.8% | -0.03205 to -0.00154 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.32 | 63.33 | +0.0% | -0.3673 to +0.3833 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.09143 | +0.0914 | +0.07401 to +0.1088 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
