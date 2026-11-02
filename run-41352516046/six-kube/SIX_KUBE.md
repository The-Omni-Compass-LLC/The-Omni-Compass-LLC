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
| response time (ms), 95th percentile | 3667 | 3474 | 2704 | 2001 | 3616 | 4812 | 5613 | 4252 | 3425 | 3863 |
| response time (ms), 99th percentile | 5450 | 6408 | 4462 | 3798 | 5954 | 6950 | 7318 | 6990 | 5613 | 6099 |
| time over the response line (% of samples) | 50.65 | 49.84 | 38.3 | 37.54 | 59.25 | 57.82 | 64.99 | 61.73 | 57.23 | 57.65 |
| failed requests (%) | 34.02 | 36.86 | 28.45 | 32.22 | 45 | 44.24 | 46.68 | 50.93 | 42.22 | 47.28 |
| HPA replicas, mean | 9.812 | 11.84 | 9.754 | 12.25 | 9.837 | 11.52 | 9.859 | 11.44 | 9.83 | 12.08 |
| pods started | 3.9 | 6.2 | 5 | 8 | 3.4 | 5.2 | 3.3 | 5.1 | 3.5 | 6.2 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.5 | 277 | 273.9 | 275.3 | 276.8 | 277.4 | 278.6 | 277.7 | 276.9 | 277.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.5 | 277 | 273.9 | 275.3 | 276.8 | 277.4 | 278.6 | 277.7 | 276.9 | 277.1 |
| CPU used with Omni's own (cores), mean | 2.453 | 2.471 | 2.266 | 2.343 | 2.47 | 2.492 | 2.555 | 2.555 | 2.47 | 2.488 |
| host CPU busy, the real machine under kind (%) | 72.54 | 76.25 | 68.97 | 77.49 | 75.57 | 80.11 | 78.22 | 83.18 | 75.12 | 81.38 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.42 | 0.55 | 0.77 | 1.12 | 0.56 | 0.42 | 0.71 | 0.48 | 0.55 | 1.02 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 3 (HPA replicas, mean; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3667 | 3474 | -5.3% | -1325 to +938.7 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5450 | 6408 | +17.6% | -215.6 to +2132 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 50.65 | 49.84 | -1.6% | -2.944 to +1.317 | STEADY, inside the noise (cut) |
| failed requests (%) | 34.02 | 36.86 | +8.3% | -3.041 to +8.716 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.812 | 11.84 | +20.7% | +0.1406 to +3.922 | power given |
| pods started | 3.9 | 6.2 | +59.0% | -0.0374 to +4.637 | STEADY, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.579e-15 to +5.132e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.5 | 277 | +0.2% | -0.3117 to +1.203 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.5 | 277 | +0.2% | -0.3117 to +1.203 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.453 | 2.471 | +0.8% | -0.00429 to +0.04121 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.54 | 76.25 | +5.1% | +3.202 to +4.211 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.42 | 0.55 | +31.0% | +0.07111 to +0.1889 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2704 | 2001 | -26.0% | -2156 to +747.6 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4462 | 3798 | -14.9% | -2411 to +1081 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 38.3 | 37.54 | -2.0% | -2.528 to +1.004 | STEADY, inside the noise (cut) |
| failed requests (%) | 28.45 | 32.22 | +13.2% | -0.7859 to +8.317 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.754 | 12.25 | +25.6% | +1.148 to +3.846 | power given |
| pods started | 5 | 8 | +60.0% | +0.5684 to +5.432 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.996e-15 to +7.524e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 275.3 | +0.5% | +0.4777 to +2.354 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 275.3 | +0.5% | +0.4777 to +2.354 | power given |
| CPU used with Omni's own (cores), mean | 2.266 | 2.343 | +3.4% | +0.01884 to +0.1346 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.97 | 77.49 | +12.4% | +7.179 to +9.86 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.77 | 1.12 | +45.5% | +0.21 to +0.49 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 3 (HPA replicas, mean; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3616 | 4812 | +33.1% | -145.9 to +2538 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5954 | 6950 | +16.7% | +185.6 to +1807 | LOSS |
| time over the response line (% of samples) | 59.25 | 57.82 | -2.4% | -2.998 to +0.1255 | STEADY, inside the noise (cut) |
| failed requests (%) | 45 | 44.24 | -1.7% | -5.822 to +4.305 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.837 | 11.52 | +17.1% | +0.2377 to +3.126 | power given |
| pods started | 3.4 | 5.2 | +52.9% | -0.6034 to +4.203 | STEADY, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.623e-16 to +1.25e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.8 | 277.4 | +0.2% | -0.5445 to +1.746 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.8 | 277.4 | +0.2% | -0.5445 to +1.746 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.47 | 2.492 | +0.9% | -0.009917 to +0.05452 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.57 | 80.11 | +6.0% | +3.808 to +5.286 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.56 | 0.42 | -25.0% | -0.2366 to -0.04344 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 3 (HPA replicas, mean; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 5613 | 4252 | -24.2% | -4257 to +1535 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 7318 | 6990 | -4.5% | -1865 to +1210 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 64.99 | 61.73 | -5.0% | -5.515 to -1.006 | GAIN |
| failed requests (%) | 46.68 | 50.93 | +9.1% | -2.068 to +10.55 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.859 | 11.44 | +16.0% | +0.2301 to +2.928 | power given |
| pods started | 3.3 | 5.1 | +54.5% | -0.4316 to +4.032 | STEADY, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | +0.0% | +8.825e-16 to +3.025e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 278.6 | 277.7 | -0.3% | -2.01 to +0.2676 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 278.6 | 277.7 | -0.3% | -2.01 to +0.2676 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.555 | 2.555 | -0.0% | -0.01293 to +0.01138 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 78.22 | 83.18 | +6.3% | +4.689 to +5.228 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | power given |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | power given |
| organism behind its window (s) | 0.71 | 0.48 | -32.4% | -0.3257 to -0.1343 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3425 | 3863 | +12.8% | -1260 to +2136 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5613 | 6099 | +8.7% | -688.1 to +1660 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 57.23 | 57.65 | +0.7% | -4.523 to +5.348 | STEADY, inside the noise (up) |
| failed requests (%) | 42.22 | 47.28 | +12.0% | -2.497 to +12.61 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.83 | 12.08 | +22.9% | +0.7339 to +3.767 | power given |
| pods started | 3.5 | 6.2 | +77.1% | +0.3871 to +5.013 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +1.79e-16 to +2.663e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.9 | 277.1 | +0.1% | -0.9031 to +1.328 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.9 | 277.1 | +0.1% | -0.9031 to +1.328 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.47 | 2.488 | +0.7% | -0.005772 to +0.04135 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.12 | 81.38 | +8.3% | +5.821 to +6.696 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.55 | 1.02 | +85.5% | +0.3631 to +0.5769 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
