# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 100 copies: native | The spine, the muscles every stack runs on, 100 copies: omni | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 4085 | 4097 | 4140 | 3742 | 4793 | 3718 | 4394 | 3278 | 3945 | 3535 |
| response time (ms), 99th percentile | 6396 | 6496 | 6590 | 6028 | 6981 | 6467 | 6706 | 6079 | 6149 | 6179 |
| time over the response line (% of samples) | 54.33 | 55.36 | 57.82 | 58.83 | 64.6 | 63.64 | 58.46 | 57.26 | 61.91 | 60.7 |
| failed requests (%) | 35.6 | 39.91 | 41.66 | 46.6 | 46.74 | 49.69 | 41.07 | 43.51 | 47.61 | 48.8 |
| HPA replicas, mean | 9.797 | 12.91 | 9.835 | 10.97 | 9.841 | 11.3 | 9.826 | 11.2 | 9.841 | 11.18 |
| pods started | 4.3 | 9.575 | 3.675 | 6.65 | 3.475 | 7.4 | 3.9 | 8.075 | 3.5 | 5.975 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 5.998 | 5.998 |
| energy, parked workers still on at idle power (Wh, declared model) | 277.2 | 277.4 | 277.1 | 277.2 | 278.3 | 278.1 | 277.8 | 277.2 | 277.3 | 277.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.2 | 277.4 | 277.1 | 277.2 | 278.3 | 278.1 | 277.8 | 277.2 | 277.2 | 277.3 |
| CPU used with Omni's own (cores), mean | 2.487 | 2.533 | 2.479 | 2.533 | 2.55 | 2.583 | 2.496 | 2.541 | 2.5 | 2.553 |
| host CPU busy, the real machine under kind (%) | 73.37 | 77.92 | 75.42 | 83.89 | 77.75 | 82.96 | 76.56 | 82.82 | 76.09 | 83.81 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.445 | 0.5525 | 0.855 | 1.137 | 0.6125 | 0.41 | 0.7375 | 0.4375 | 0.5125 | 1.055 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4085 | 4097 | +0.3% | -671.3 to +694.9 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6396 | 6496 | +1.6% | -403.3 to +602 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 54.33 | 55.36 | +1.9% | -0.9955 to +3.054 | STEADY, inside the noise (up) |
| failed requests (%) | 35.6 | 39.91 | +12.1% | +2.336 to +6.269 | LOSS |
| HPA replicas, mean | 9.797 | 12.91 | +31.7% | +2.501 to +3.718 | power given |
| pods started | 4.3 | 9.575 | +122.7% | +4.592 to +5.958 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.125e-16 to +2.428e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.2 | 277.4 | +0.1% | -0.2007 to +0.6314 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.2 | 277.4 | +0.1% | -0.2007 to +0.6314 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.487 | 2.533 | +1.8% | +0.03485 to +0.05644 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.37 | 77.92 | +6.2% | +4.215 to +4.879 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.445 | 0.5525 | +24.2% | +0.04983 to +0.1652 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4140 | 3742 | -9.6% | -1281 to +485.1 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6590 | 6028 | -8.5% | -1312 to +188.9 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 57.82 | 58.83 | +1.8% | -1.121 to +3.148 | STEADY, inside the noise (up) |
| failed requests (%) | 41.66 | 46.6 | +11.9% | +2.217 to +7.66 | LOSS |
| HPA replicas, mean | 9.835 | 10.97 | +11.5% | +0.4765 to +1.793 | power given |
| pods started | 3.675 | 6.65 | +81.0% | +2.005 to +3.945 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.383e-16 to +8.268e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.1 | 277.2 | +0.0% | -0.417 to +0.6747 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.1 | 277.2 | +0.0% | -0.417 to +0.6747 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.479 | 2.533 | +2.2% | +0.03219 to +0.07662 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.42 | 83.89 | +11.2% | +7.804 to +9.135 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.855 | 1.138 | +33.0% | +0.2119 to +0.3531 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 2 (response time (ms), 95th percentile; organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4793 | 3718 | -22.4% | -1723 to -426.6 | GAIN |
| response time (ms), 99th percentile | 6981 | 6467 | -7.4% | -1152 to +122.9 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 64.6 | 63.64 | -1.5% | -2.302 to +0.3741 | STEADY, inside the noise (cut) |
| failed requests (%) | 46.74 | 49.69 | +6.3% | -0.01556 to +5.921 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.841 | 11.3 | +14.8% | +0.8907 to +2.024 | power given |
| pods started | 3.475 | 7.4 | +112.9% | +2.895 to +4.955 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +4.602e-16 to +1.538e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 278.3 | 278.1 | -0.1% | -0.6087 to +0.2309 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 278.3 | 278.1 | -0.1% | -0.6087 to +0.2309 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.55 | 2.583 | +1.3% | +0.02258 to +0.04268 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.75 | 82.96 | +6.7% | +4.948 to +5.481 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.6125 | 0.41 | -33.1% | -0.262 to -0.143 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 5 (response time (ms), 95th percentile; time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4394 | 3278 | -25.4% | -1871 to -360.6 | GAIN |
| response time (ms), 99th percentile | 6706 | 6079 | -9.3% | -1392 to +138.3 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 58.46 | 57.26 | -2.0% | -2.39 to -0.005433 | GAIN |
| failed requests (%) | 41.07 | 43.51 | +5.9% | -0.3227 to +5.204 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.826 | 11.2 | +14.0% | +0.7566 to +2.001 | power given |
| pods started | 3.9 | 8.075 | +107.1% | +3.259 to +5.091 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -0.0002992 to +0.0008842 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.8 | 277.2 | -0.2% | -1.057 to -0.05339 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.8 | 277.2 | -0.2% | -1.044 to -0.04873 | GAIN |
| CPU used with Omni's own (cores), mean | 2.496 | 2.541 | +1.8% | +0.02846 to +0.06111 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.56 | 82.82 | +8.2% | +5.841 to +6.688 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | power given |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | power given |
| organism behind its window (s) | 0.7375 | 0.4375 | -40.7% | -0.3619 to -0.2381 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3945 | 3535 | -10.4% | -1093 to +272.5 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6149 | 6179 | +0.5% | -607.7 to +668.5 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 61.91 | 60.7 | -2.0% | -2.598 to +0.1725 | STEADY, inside the noise (cut) |
| failed requests (%) | 47.61 | 48.8 | +2.5% | -0.8152 to +3.21 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.841 | 11.18 | +13.6% | +0.6598 to +2.01 | power given |
| pods started | 3.5 | 5.975 | +70.7% | +1.398 to +3.552 | power given |
| worker nodes in service, mean | 5.998 | 5.998 | +0.0% | -0.006091 to +0.006606 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.3 | 277.4 | +0.0% | -0.4338 to +0.6396 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.2 | 277.3 | +0.0% | -0.4333 to +0.6557 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.5 | 2.553 | +2.1% | +0.02813 to +0.07724 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.09 | 83.81 | +10.1% | +7.146 to +8.299 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.5125 | 1.055 | +105.9% | +0.4716 to +0.6134 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
