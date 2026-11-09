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
| response time (ms), 95th percentile | 3579 | 2491 | 4156 | 3488 | 4311 | 3140 | 4411 | 2544 | 3048 | 3536 |
| response time (ms), 99th percentile | 6028 | 5237 | 6639 | 5806 | 6372 | 5473 | 6332 | 4924 | 5344 | 5766 |
| time over the response line (% of samples) | 51.24 | 50.73 | 59.34 | 59.54 | 52.51 | 52.56 | 51.72 | 50.49 | 49.49 | 51.27 |
| failed requests (%) | 35.31 | 39.92 | 43.49 | 47.04 | 34.59 | 39.71 | 36.22 | 38.69 | 36.27 | 37.28 |
| HPA replicas, mean | 9.814 | 12.94 | 9.83 | 11.11 | 9.793 | 12.18 | 9.791 | 11.73 | 9.773 | 12.12 |
| pods started | 3.85 | 9.65 | 3.95 | 6.675 | 4.45 | 9.949 | 4.35 | 9.75 | 4.725 | 8.075 |
| worker nodes in service, mean | 6 | 6 | 6 | 5.997 | 6 | 5.999 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.7 | 276.9 | 277.7 | 277.4 | 276.7 | 276.8 | 276.9 | 276.5 | 276.1 | 276.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.7 | 276.9 | 277.7 | 277.3 | 276.7 | 276.8 | 276.9 | 276.5 | 276.1 | 276.5 |
| CPU used with Omni's own (cores), mean | 2.447 | 2.5 | 2.511 | 2.555 | 2.453 | 2.498 | 2.426 | 2.472 | 2.424 | 2.485 |
| host CPU busy, the real machine under kind (%) | 72.27 | 77.07 | 75.93 | 84.15 | 74.6 | 80.22 | 73.91 | 80.18 | 72.95 | 80.9 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.445 | 0.515 | 0.92 | 1.15 | 0.5575 | 0.4308 | 0.7325 | 0.4175 | 0.475 | 1.08 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 2 (response time (ms), 95th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3579 | 2491 | -30.4% | -1767 to -409.8 | GAIN |
| response time (ms), 99th percentile | 6028 | 5237 | -13.1% | -1592 to +9.273 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 51.24 | 50.73 | -1.0% | -1.939 to +0.9249 | STEADY, inside the noise (cut) |
| failed requests (%) | 35.31 | 39.92 | +13.1% | +2.783 to +6.443 | LOSS |
| HPA replicas, mean | 9.814 | 12.94 | +31.9% | +2.521 to +3.737 | power given |
| pods started | 3.85 | 9.65 | +150.6% | +5.043 to +6.557 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.049e-16 to +2.276e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.7 | 276.9 | +0.1% | -0.274 to +0.7169 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.7 | 276.9 | +0.1% | -0.274 to +0.7169 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.447 | 2.5 | +2.2% | +0.03807 to +0.06812 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.27 | 77.07 | +6.6% | +4.358 to +5.227 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.445 | 0.515 | +15.7% | +0.02295 to +0.1171 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 2 (response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4156 | 3488 | -16.1% | -1439 to +103.6 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6639 | 5806 | -12.5% | -1536 to -128.5 | GAIN |
| time over the response line (% of samples) | 59.34 | 59.54 | +0.3% | -1.287 to +1.698 | STEADY, inside the noise (up) |
| failed requests (%) | 43.49 | 47.04 | +8.2% | +0.6562 to +6.456 | LOSS |
| HPA replicas, mean | 9.83 | 11.11 | +13.0% | +0.5825 to +1.974 | power given |
| pods started | 3.95 | 6.675 | +69.0% | +1.753 to +3.697 | power given |
| worker nodes in service, mean | 6 | 5.997 | -0.0% | -0.007953 to +0.002691 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.7 | 277.4 | -0.1% | -0.7831 to +0.1968 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.7 | 277.3 | -0.1% | -0.8918 to +0.1462 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.511 | 2.555 | +1.7% | +0.02378 to +0.06275 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.93 | 84.15 | +10.8% | +7.759 to +8.677 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.92 | 1.15 | +25.0% | +0.1601 to +0.2999 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

39 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4316 | 3140 | -27.2% | -1874 to -478 | GAIN |
| response time (ms), 99th percentile | 6347 | 5473 | -13.8% | -1502 to -246.3 | GAIN |
| time over the response line (% of samples) | 51.9 | 52.56 | +1.3% | -0.845 to +2.176 | STEADY, inside the noise (up) |
| failed requests (%) | 34.03 | 39.71 | +16.7% | +2.73 to +8.635 | LOSS |
| HPA replicas, mean | 9.789 | 12.18 | +24.5% | +1.698 to +3.09 | power given |
| pods started | 4.538 | 9.949 | +119.2% | +4.276 to +6.545 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003621 to +0.001226 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.6 | 276.8 | +0.1% | -0.2626 to +0.795 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.6 | 276.8 | +0.1% | -0.2936 to +0.7533 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.448 | 2.498 | +2.1% | +0.03483 to +0.06598 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.43 | 80.22 | +7.8% | +5.39 to +6.178 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.5564 | 0.4308 | -22.6% | -0.1908 to -0.06052 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4411 | 2544 | -42.3% | -2801 to -935 | GAIN |
| response time (ms), 99th percentile | 6332 | 4924 | -22.2% | -2136 to -680.3 | GAIN |
| time over the response line (% of samples) | 51.72 | 50.49 | -2.4% | -2.579 to +0.1062 | STEADY, inside the noise (cut) |
| failed requests (%) | 36.22 | 38.69 | +6.8% | -0.1944 to +5.133 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.791 | 11.73 | +19.8% | +1.217 to +2.664 | power given |
| pods started | 4.35 | 9.75 | +124.1% | +4.093 to +6.707 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +3.258e-16 to +1.317e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.9 | 276.5 | -0.1% | -0.814 to +0.165 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.9 | 276.5 | -0.1% | -0.814 to +0.165 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.426 | 2.472 | +1.9% | +0.02744 to +0.06476 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.91 | 80.18 | +8.5% | +5.8 to +6.751 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | power given |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | power given |
| organism behind its window (s) | 0.7325 | 0.4175 | -43.0% | -0.3655 to -0.2645 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3048 | 3536 | +16.0% | -373 to +1348 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5344 | 5766 | +7.9% | -335.6 to +1179 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 49.49 | 51.27 | +3.6% | -0.4415 to +4.001 | STEADY, inside the noise (up) |
| failed requests (%) | 36.27 | 37.28 | +2.8% | -2.587 to +4.597 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.773 | 12.12 | +24.0% | +1.609 to +3.077 | power given |
| pods started | 4.725 | 8.075 | +70.9% | +2.231 to +4.469 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +1.04e-16 to +1.273e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.1 | 276.5 | +0.1% | -0.006626 to +0.8318 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.1 | 276.5 | +0.1% | -0.006626 to +0.8318 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.424 | 2.485 | +2.5% | +0.04067 to +0.0806 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.95 | 80.9 | +10.9% | +7.454 to +8.447 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.475 | 1.08 | +127.4% | +0.5355 to +0.6745 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
