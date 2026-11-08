# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 100 copies: native | The spine, the muscles every stack runs on, 100 copies: omni | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2113 | 1965 | 4347 | 4359 | 5350 | 2717 | 3068 | 2920 | 2343 | 2650 |
| response time (ms), 99th percentile | 4260 | 3449 | 6126 | 6153 | 7712 | 5184 | 5721 | 4837 | 4360 | 4450 |
| time over the response line (% of samples) | 31.13 | 23.43 | 56.88 | 57.63 | 66.94 | 63.27 | 42.03 | 40.64 | 35.15 | 38.93 |
| failed requests (%) | 22.54 | 17.36 | 40.19 | 44.35 | 48.47 | 53.56 | 27.73 | 26.56 | 23.57 | 26.6 |
| HPA replicas, mean | 9.717 | 14.51 | 9.791 | 11.08 | 9.815 | 11.03 | 9.804 | 12.06 | 9.733 | 12.98 |
| pods started | 5.375 | 11.14 | 4.8 | 8.6 | 4.375 | 6.375 | 4.3 | 10.44 | 5.5 | 10.5 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 5.991 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 272 | 278.1 | 278.1 | 276.9 | 277.3 | 276.3 | 275.8 | 274.4 | 275.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 272 | 278.1 | 278.1 | 276.9 | 277 | 276.3 | 275.8 | 274.4 | 275.5 |
| CPU used with Omni's own (cores), mean | 2.188 | 2.201 | 2.522 | 2.564 | 2.517 | 2.546 | 2.358 | 2.421 | 2.308 | 2.386 |
| host CPU busy, the real machine under kind (%) | 64.91 | 68.19 | 75.76 | 83.47 | 76.98 | 82.12 | 72.47 | 78.77 | 69.16 | 77.54 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.375 | 0.4571 | 0.94 | 1.17 | 0.5375 | 0.3875 | 0.78 | 0.4111 | 0.47 | 1.08 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

7 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1628 | 1965 | +20.7% | -787 to +1461 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3548 | 3449 | -2.8% | -495 to +297 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 24.62 | 23.43 | -4.8% | -2.73 to +0.3594 | STEADY, inside the noise (cut) |
| failed requests (%) | 17.27 | 17.36 | +0.5% | -4.305 to +4.489 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.695 | 14.51 | +49.6% | +3.906 to +5.717 | power given |
| pods started | 5.714 | 11.14 | +95.0% | +3.37 to +7.487 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.571e-15 to +1.063e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 272 | +0.1% | -1.118 to +1.504 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 272 | +0.1% | -1.118 to +1.504 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.121 | 2.201 | +3.8% | +0.03673 to +0.1234 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.89 | 68.19 | +8.4% | +4.347 to +6.25 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.3714 | 0.4571 | +23.1% | +0.02189 to +0.1495 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 3 (pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4347 | 4359 | +0.3% | -2355 to +2378 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6126 | 6153 | +0.4% | -2325 to +2378 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 56.88 | 57.63 | +1.3% | -1.17 to +2.656 | STEADY, inside the noise (up) |
| failed requests (%) | 40.19 | 44.35 | +10.3% | -2.44 to +10.74 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.791 | 11.08 | +13.2% | -0.3241 to +2.91 | STEADY, inside the noise (up) |
| pods started | 4.8 | 8.6 | +79.2% | +1.84 to +5.76 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.325e-16 to +2.464e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 278.1 | 278.1 | -0.0% | -0.9864 to +0.9633 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 278.1 | 278.1 | -0.0% | -0.9864 to +0.9633 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.522 | 2.564 | +1.7% | +0.007381 to +0.07708 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.76 | 83.47 | +10.2% | +7.075 to +8.34 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.94 | 1.17 | +24.5% | +0.0421 to +0.4179 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 2 (organism energy (J); organism work per energy), STEADY (inside the noise) on 5

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 5350 | 2717 | -49.2% | -4613 to -653 | GAIN |
| response time (ms), 99th percentile | 7712 | 5184 | -32.8% | -4306 to -749 | GAIN |
| time over the response line (% of samples) | 66.94 | 63.27 | -5.5% | -6.073 to -1.26 | GAIN |
| failed requests (%) | 48.47 | 53.56 | +10.5% | +0.1972 to +9.997 | LOSS |
| HPA replicas, mean | 9.815 | 11.03 | +12.4% | -0.5959 to +3.029 | STEADY, inside the noise (up) |
| pods started | 4.375 | 6.375 | +45.7% | -0.5283 to +4.528 | STEADY, inside the noise (up) |
| worker nodes in service, mean | 6 | 5.991 | -0.2% | -0.03139 to +0.01273 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.9 | 277.3 | +0.1% | -0.896 to +1.609 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.9 | 277 | +0.0% | -1.661 to +1.811 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.517 | 2.546 | +1.1% | +0.01132 to +0.04569 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.98 | 82.12 | +6.7% | +4.779 to +5.495 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.5375 | 0.3875 | -27.9% | -0.2274 to -0.07259 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

9 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2727 | 2920 | +7.1% | -1921 to +2307 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5399 | 4837 | -10.4% | -2335 to +1211 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 38.17 | 40.64 | +6.5% | -2.027 to +6.973 | STEADY, inside the noise (up) |
| failed requests (%) | 24.33 | 26.56 | +9.2% | -1.816 to +6.287 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.783 | 12.06 | +23.2% | +0.1879 to +4.361 | power given |
| pods started | 4.778 | 10.44 | +118.6% | +2.544 to +8.789 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.325e-16 to +2.604e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.9 | 275.8 | -0.0% | -1.293 to +1.256 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.9 | 275.8 | -0.0% | -1.293 to +1.256 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.329 | 2.421 | +3.9% | +0.04165 to +0.1421 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.43 | 78.77 | +10.3% | +6.128 to +8.547 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | power given |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | power given |
| organism behind its window (s) | 0.7333 | 0.4111 | -43.9% | -0.4596 to -0.1848 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2343 | 2650 | +13.1% | -1249 to +1862 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4360 | 4450 | +2.1% | -1166 to +1346 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 35.15 | 38.93 | +10.7% | -3.682 to +11.23 | STEADY, inside the noise (up) |
| failed requests (%) | 23.57 | 26.6 | +12.9% | -4.962 to +11.04 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.733 | 12.98 | +33.4% | +1.55 to +4.943 | power given |
| pods started | 5.5 | 10.5 | +90.9% | +3.569 to +6.431 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.16e-15 to +1.16e-15 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 274.4 | 275.5 | +0.4% | +0.04394 to +2.117 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.4 | 275.5 | +0.4% | +0.04394 to +2.117 | power given |
| CPU used with Omni's own (cores), mean | 2.308 | 2.386 | +3.4% | +0.02619 to +0.1297 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.16 | 77.54 | +12.1% | +6.698 to +10.05 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.47 | 1.08 | +129.8% | +0.4863 to +0.7337 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
