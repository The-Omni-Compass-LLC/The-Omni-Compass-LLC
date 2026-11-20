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
| response time (ms), 95th percentile | 3447 | 3189 | 4285 | 5243 | 3336 | 2189 | 4086 | 3489 | 3164 | 2956 |
| response time (ms), 99th percentile | 5749 | 6021 | 6999 | 7506 | 5201 | 4271 | 6596 | 5410 | 5333 | 5038 |
| time over the response line (% of samples) | 48.89 | 49.76 | 53.49 | 58.71 | 44.32 | 43.13 | 55.94 | 57.22 | 49.39 | 49.36 |
| failed requests (%) | 29.97 | 32.68 | 33.61 | 43.65 | 30.61 | 33.19 | 38 | 43.5 | 36.02 | 39.08 |
| HPA replicas, mean | 9.77 | 13.06 | 9.813 | 10.59 | 9.785 | 12.45 | 9.808 | 11.89 | 9.818 | 11.71 |
| pods started | 4.8 | 10.5 | 4.3 | 7.2 | 4.2 | 10.1 | 4.1 | 7.2 | 3.8 | 8.5 |
| worker nodes in service, mean | 5.999 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.8 | 276.9 | 277.6 | 278.1 | 275.2 | 275.4 | 277.5 | 278 | 276.4 | 276.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.8 | 276.9 | 277.6 | 278.1 | 275.2 | 275.4 | 277.5 | 278 | 276.4 | 276.8 |
| CPU used with Omni's own (cores), mean | 2.447 | 2.497 | 2.521 | 2.568 | 2.306 | 2.376 | 2.504 | 2.565 | 2.405 | 2.465 |
| host CPU busy, the real machine under kind (%) | 72.27 | 77.25 | 76.18 | 84.5 | 71.08 | 77.13 | 77.34 | 84.31 | 73.12 | 81.39 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.44 | 0.56 | 0.93 | 1.19 | 0.78 | 0.37 | 0.72 | 0.53 | 0.51 | 1.12 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3447 | 3189 | -7.5% | -1509 to +992.3 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5749 | 6021 | +4.7% | -1250 to +1793 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 48.89 | 49.76 | +1.8% | -4.166 to +5.901 | STEADY, inside the noise (up) |
| failed requests (%) | 29.97 | 32.68 | +9.1% | -2.118 to +7.547 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.77 | 13.06 | +33.7% | +1.827 to +4.763 | power given |
| pods started | 4.8 | 10.5 | +118.8% | +3.791 to +7.609 | power given |
| worker nodes in service, mean | 5.999 | 6 | +0.0% | -0.00139 to +0.003592 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.8 | 276.9 | +0.0% | -0.8683 to +0.9614 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.8 | 276.9 | +0.0% | -0.8125 to +0.9723 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.447 | 2.497 | +2.0% | +0.0154 to +0.08426 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.27 | 77.25 | +6.9% | +4.21 to +5.751 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.44 | 0.56 | +27.3% | +0.009185 to +0.2308 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 3 (pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4285 | 5243 | +22.4% | -884.3 to +2800 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6999 | 7506 | +7.3% | -1286 to +2301 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 53.49 | 58.71 | +9.8% | -3.997 to +14.43 | STEADY, inside the noise (up) |
| failed requests (%) | 33.61 | 43.65 | +29.9% | +1.11 to +18.97 | LOSS |
| HPA replicas, mean | 9.813 | 10.59 | +7.9% | -0.4263 to +1.97 | STEADY, inside the noise (up) |
| pods started | 4.3 | 7.2 | +67.4% | +0.6267 to +5.173 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +6.141e-16 to +3.116e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.6 | 278.1 | +0.2% | -0.5215 to +1.617 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.6 | 278.1 | +0.2% | -0.5215 to +1.617 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.521 | 2.568 | +1.9% | +0.007608 to +0.08793 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.18 | 84.5 | +10.9% | +7.195 to +9.453 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.93 | 1.19 | +28.0% | +0.0308 to +0.4892 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3336 | 2189 | -34.4% | -2753 to +459.1 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5201 | 4271 | -17.9% | -2344 to +483.5 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 44.32 | 43.13 | -2.7% | -3.082 to +0.7098 | STEADY, inside the noise (cut) |
| failed requests (%) | 30.61 | 33.19 | +8.4% | -3.149 to +8.301 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.785 | 12.45 | +27.2% | +0.9027 to +4.419 | power given |
| pods started | 4.2 | 10.1 | +140.5% | +3.322 to +8.478 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +2.732e-16 to +2.747e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.2 | 275.4 | +0.1% | -0.9298 to +1.364 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.2 | 275.4 | +0.1% | -0.9298 to +1.364 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.306 | 2.376 | +3.0% | +0.02633 to +0.113 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.08 | 77.13 | +8.5% | +5.002 to +7.109 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.78 | 0.37 | -52.6% | -0.67 to -0.15 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4086 | 3489 | -14.6% | -3335 to +2141 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6596 | 5410 | -18.0% | -3444 to +1073 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 55.94 | 57.22 | +2.3% | -3.655 to +6.199 | STEADY, inside the noise (up) |
| failed requests (%) | 38 | 43.5 | +14.5% | +0.5957 to +10.42 | LOSS |
| HPA replicas, mean | 9.808 | 11.89 | +21.2% | +0.76 to +3.406 | power given |
| pods started | 4.1 | 7.2 | +75.6% | +0.4783 to +5.722 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.737e-16 to +1.695e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.5 | 278 | +0.2% | -0.3831 to +1.451 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.5 | 278 | +0.2% | -0.3831 to +1.451 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.504 | 2.565 | +2.4% | +0.02149 to +0.09925 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.34 | 84.31 | +9.0% | +6.007 to +7.941 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | power given |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | power given |
| organism behind its window (s) | 0.72 | 0.53 | -26.4% | -0.3498 to -0.03023 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3164 | 2956 | -6.6% | -1690 to +1275 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5333 | 5038 | -5.5% | -2094 to +1503 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 49.39 | 49.36 | -0.1% | -4.07 to +4.018 | STEADY, inside the noise (cut) |
| failed requests (%) | 36.02 | 39.08 | +8.5% | -4.237 to +10.35 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.818 | 11.71 | +19.3% | +0.06387 to +3.722 | power given |
| pods started | 3.8 | 8.5 | +123.7% | +1.627 to +7.773 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.344e-15 to +1.699e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.4 | 276.8 | +0.2% | -0.6357 to +1.523 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.4 | 276.8 | +0.2% | -0.6357 to +1.523 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.405 | 2.465 | +2.5% | +0.01759 to +0.1033 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.12 | 81.39 | +11.3% | +7.386 to +9.153 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.51 | 1.12 | +119.6% | +0.5474 to +0.6726 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
