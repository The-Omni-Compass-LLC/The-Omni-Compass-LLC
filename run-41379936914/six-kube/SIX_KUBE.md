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
| response time (ms), 95th percentile | 1577 | 1786 | 1302 | 1316 | 1459 | 1801 | 1631 | 1818 | 1459 | 1442 | 2028 | 1458 | 1179 | 1366 |
| response time (ms), 99th percentile | 4943 | 5273 | 4183 | 4773 | 4443 | 4225 | 5435 | 5738 | 4497 | 4224 | 4524 | 4407 | 3997 | 4131 |
| time over the response line (% of samples) | 16.79 | 12.96 | 23.59 | 17.36 | 16.14 | 11.8 | 18.94 | 14.3 | 22.96 | 16.63 | 26.14 | 18.1 | 19.23 | 13.63 |
| failed requests (%) | 5.486 | 4.537 | 10.4 | 8.139 | 5.344 | 4.546 | 6.446 | 5.266 | 7.604 | 7.021 | 10.34 | 7.608 | 7.851 | 6.111 |
| HPA replicas, mean | 9.592 | 13.18 | 9.661 | 12.67 | 9.555 | 13.03 | 9.607 | 13.38 | 9.534 | 12.81 | 9.608 | 12.69 | 9.607 | 12.4 |
| pods started | 5.25 | 9.65 | 5 | 10.1 | 5.5 | 9.9 | 5.15 | 9.05 | 5.65 | 9.5 | 4.9 | 10.15 | 5.45 | 10.1 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 179.5 | 180.1 | 181.9 | 182.1 | 179.2 | 179.3 | 180.2 | 181 | 180.9 | 180.7 | 181.9 | 181 | 180.2 | 180.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.5 | 180.1 | 181.9 | 182.1 | 179.2 | 179.3 | 180.2 | 181 | 180.9 | 180.7 | 181.9 | 181 | 180.2 | 180.1 |
| CPU used with Omni's own (cores), mean | 1.924 | 1.923 | 2.101 | 2.096 | 1.879 | 1.877 | 1.991 | 2.01 | 2.013 | 2.014 | 2.082 | 2.063 | 1.943 | 1.94 |
| host CPU busy, the real machine under kind (%) | 57.24 | 57.48 | 62.31 | 62.4 | 56.19 | 56.53 | 59.2 | 59.72 | 60.04 | 60.25 | 61.85 | 61.67 | 58.06 | 58.24 |
| organism work | 2.05e+10 | 2.05e+10 | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.319e+10 | 1.319e+10 | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.311 | 2.222 | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.554 | 1.554 | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.085 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1577 | 1786 | +13.3% | -136.7 to +554.7 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4943 | 5273 | +6.7% | -245.7 to +905.5 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 16.79 | 12.96 | -22.8% | -5.11 to -2.55 | GAIN |
| failed requests (%) | 5.486 | 4.537 | -17.3% | -1.55 to -0.3479 | GAIN |
| HPA replicas, mean | 9.592 | 13.18 | +37.4% | +2.581 to +4.593 | power given |
| pods started | 5.25 | 9.65 | +83.8% | +3.153 to +5.647 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.988e-16 to +3.876e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.5 | 180.1 | +0.3% | +0.3293 to +0.9169 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.5 | 180.1 | +0.3% | +0.3293 to +0.9169 | power given |
| CPU used with Omni's own (cores), mean | 1.924 | 1.923 | -0.0% | -0.01491 to +0.013 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.24 | 57.48 | +0.4% | +0.002487 to +0.4811 | shown, not judged |
| organism work | 2.05e+10 | 2.05e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.319e+10 | 1.319e+10 | +0.0% | +7.974e+05 to +7.987e+05 | power given |
| organism time over the line (% of steps) | 2.311 | 2.222 | -3.8% | -0.08895 to -0.08895 | GAIN |
| organism work per energy | 1.554 | 1.554 | -0.0% | -9.405e-05 to -9.39e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1302 | 1316 | +1.1% | -198.9 to +228.4 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4183 | 4773 | +14.1% | -165.6 to +1345 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 23.59 | 17.36 | -26.4% | -8.879 to -3.588 | GAIN |
| failed requests (%) | 10.4 | 8.139 | -21.7% | -3.492 to -1.028 | GAIN |
| HPA replicas, mean | 9.661 | 12.67 | +31.1% | +2.21 to +3.801 | power given |
| pods started | 5 | 10.1 | +102.0% | +3.925 to +6.275 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.729e-16 to +2.4e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.9 | 182.1 | +0.1% | -0.4207 to +0.6923 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.9 | 182.1 | +0.1% | -0.4207 to +0.6923 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.101 | 2.096 | -0.3% | -0.02019 to +0.009448 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.31 | 62.4 | +0.1% | -0.3289 to +0.5038 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.62e+05 to +8.625e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.149e-05 to -8.145e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1459 | 1801 | +23.5% | -147 to +832.5 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4443 | 4225 | -4.9% | -802.8 to +366.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 16.14 | 11.8 | -26.9% | -6.071 to -2.61 | GAIN |
| failed requests (%) | 5.344 | 4.546 | -14.9% | -1.553 to -0.042 | GAIN |
| HPA replicas, mean | 9.555 | 13.03 | +36.3% | +2.538 to +4.403 | power given |
| pods started | 5.5 | 9.9 | +80.0% | +3.411 to +5.389 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.395e-16 to +4.507e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.2 | 179.3 | +0.0% | -0.4913 to +0.5479 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.2 | 179.3 | +0.0% | -0.4913 to +0.5479 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.879 | 1.877 | -0.1% | -0.01522 to +0.01237 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.19 | 56.53 | +0.6% | -0.06299 to +0.7478 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.244e-05 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1631 | 1818 | +11.5% | -238.6 to +613.2 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5435 | 5738 | +5.6% | -224.9 to +829.5 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 18.94 | 14.3 | -24.5% | -6.205 to -3.067 | GAIN |
| failed requests (%) | 6.446 | 5.266 | -18.3% | -1.791 to -0.5689 | GAIN |
| HPA replicas, mean | 9.607 | 13.38 | +39.2% | +2.847 to +4.688 | power given |
| pods started | 5.15 | 9.05 | +75.7% | +2.686 to +5.114 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.965e-17 to +1.095e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.2 | 181 | +0.4% | +0.4049 to +1.085 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.2 | 181 | +0.4% | +0.4049 to +1.085 | power given |
| CPU used with Omni's own (cores), mean | 1.991 | 2.01 | +1.0% | -0.001085 to +0.04044 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.2 | 59.72 | +0.9% | -0.02621 to +1.076 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | power given |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1459 | 1442 | -1.2% | -178.9 to +144.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4497 | 4224 | -6.1% | -903.1 to +357.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 22.96 | 16.63 | -27.6% | -8.668 to -3.989 | GAIN |
| failed requests (%) | 7.604 | 7.021 | -7.7% | -1.142 to -0.02417 | GAIN |
| HPA replicas, mean | 9.534 | 12.81 | +34.4% | +2.209 to +4.348 | power given |
| pods started | 5.65 | 9.5 | +68.1% | +2.614 to +5.086 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.687e-16 to +5.575e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.9 | 180.7 | -0.1% | -0.8392 to +0.4261 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.9 | 180.7 | -0.1% | -0.8392 to +0.4261 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.013 | 2.014 | +0.0% | -0.01474 to +0.01571 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.04 | 60.25 | +0.4% | -0.1512 to +0.5741 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 6 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 1

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2028 | 1458 | -28.1% | -988.5 to -150.9 | GAIN |
| response time (ms), 99th percentile | 4524 | 4407 | -2.6% | -721.4 to +487.5 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 26.14 | 18.1 | -30.8% | -11.85 to -4.251 | GAIN |
| failed requests (%) | 10.34 | 7.608 | -26.4% | -4.853 to -0.6133 | GAIN |
| HPA replicas, mean | 9.608 | 12.69 | +32.1% | +2.065 to +4.1 | power given |
| pods started | 4.9 | 10.15 | +107.1% | +4.156 to +6.344 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.639e-16 to +8.08e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.9 | 181 | -0.5% | -1.494 to -0.3005 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.9 | 181 | -0.5% | -1.494 to -0.3005 | GAIN |
| CPU used with Omni's own (cores), mean | 2.082 | 2.063 | -0.9% | -0.04045 to +0.003805 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.85 | 61.67 | -0.3% | -0.8329 to +0.4601 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | power given |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | power given |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1179 | 1366 | +15.9% | -131.4 to +506.2 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3997 | 4131 | +3.3% | -615.5 to +882.9 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 19.23 | 13.63 | -29.2% | -8.485 to -2.729 | GAIN |
| failed requests (%) | 7.851 | 6.111 | -22.2% | -3.037 to -0.4426 | GAIN |
| HPA replicas, mean | 9.607 | 12.4 | +29.1% | +1.838 to +3.747 | power given |
| pods started | 5.45 | 10.1 | +85.3% | +3.617 to +5.683 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.127e-15 to +6.11e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.2 | 180.1 | -0.1% | -0.7068 to +0.4733 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.2 | 180.1 | -0.1% | -0.7068 to +0.4733 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.943 | 1.94 | -0.2% | -0.02064 to +0.01474 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.06 | 58.24 | +0.3% | -0.2613 to +0.6164 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | power given |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | power given |
| organism behind its window (s) | 0 | 0.085 | +0.085 | +0.0621 to +0.1079 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
