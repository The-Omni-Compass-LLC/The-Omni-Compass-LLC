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
| response time (ms), 95th percentile | 3581 | 3411 | 4633 | 3919 | 3992 | 3383 | 3604 | 3098 | 3155 | 2878 |
| response time (ms), 99th percentile | 5946 | 6017 | 7075 | 6841 | 6213 | 5773 | 5784 | 5529 | 5728 | 5128 |
| time over the response line (% of samples) | 49.65 | 50.62 | 60.1 | 61.72 | 53.13 | 52.63 | 54.36 | 53.48 | 51.16 | 52.69 |
| failed requests (%) | 32.93 | 36.23 | 42.74 | 47.04 | 36.08 | 39.46 | 38.76 | 40.21 | 37.62 | 41.31 |
| HPA replicas, mean | 9.798 | 12.92 | 9.826 | 10.97 | 9.809 | 11.8 | 9.829 | 11.48 | 9.8 | 11.39 |
| pods started | 4.24 | 9.52 | 3.96 | 7.02 | 4.16 | 8.16 | 3.714 | 7.49 | 4.143 | 8.367 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 5.999 | 5.998 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.3 | 276.5 | 278.5 | 278.1 | 276.5 | 276.6 | 276.9 | 276.8 | 277 | 277.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.3 | 276.5 | 278.5 | 278.1 | 276.5 | 276.5 | 276.9 | 276.8 | 277 | 277.2 |
| CPU used with Omni's own (cores), mean | 2.428 | 2.478 | 2.551 | 2.598 | 2.431 | 2.475 | 2.443 | 2.496 | 2.45 | 2.514 |
| host CPU busy, the real machine under kind (%) | 72.55 | 77.38 | 77.57 | 86.01 | 74.7 | 80.36 | 75.81 | 82.71 | 74.39 | 82.8 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.482 | 6.778 | 0.844 | 1.234 | 0.68 | 0.414 | 0.7735 | 0.5163 | 0.5041 | 1.08 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5; OFF THE CLOCK in 1 of 50 repetitions (the organism ended up to 312 s after its window: the machine could not step this many muscles in time, and the cell's last steps saw a cluster at rest)

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3581 | 3411 | -4.8% | -873.9 to +532.9 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5946 | 6017 | +1.2% | -571.9 to +714.7 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 49.65 | 50.62 | +2.0% | -0.4048 to +2.341 | STEADY, inside the noise (up) |
| failed requests (%) | 32.93 | 36.23 | +10.0% | +1.358 to +5.233 | LOSS |
| HPA replicas, mean | 9.798 | 12.92 | +31.8% | +2.571 to +3.663 | power given |
| pods started | 4.24 | 9.52 | +124.5% | +4.667 to +5.893 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7e-16 to +1.671e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.3 | 276.5 | +0.1% | -0.203 to +0.7135 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.3 | 276.5 | +0.1% | -0.203 to +0.7135 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.428 | 2.478 | +2.1% | +0.03951 to +0.06158 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.55 | 77.38 | +6.7% | +4.468 to +5.191 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.482 | 6.778 | +1306.2% | -6.17 to +18.76 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 2 (response time (ms), 95th percentile; organism time over the line (% of steps)), LOSS on 2 (time over the response line (% of samples); failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4633 | 3919 | -15.4% | -1363 to -63.83 | GAIN |
| response time (ms), 99th percentile | 7075 | 6841 | -3.3% | -743.1 to +276.6 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 60.1 | 61.72 | +2.7% | +0.08068 to +3.169 | LOSS |
| failed requests (%) | 42.74 | 47.04 | +10.0% | +1.96 to +6.63 | LOSS |
| HPA replicas, mean | 9.826 | 10.97 | +11.6% | +0.5689 to +1.712 | power given |
| pods started | 3.96 | 7.02 | +77.3% | +2.306 to +3.814 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.0007024 to +0.0002357 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 278.5 | 278.1 | -0.2% | -1.042 to +0.1822 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 278.5 | 278.1 | -0.2% | -1.048 to +0.1733 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.551 | 2.598 | +1.8% | +0.0232 to +0.06984 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.57 | 86.01 | +10.9% | +7.865 to +9.023 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.844 | 1.234 | +46.2% | +0.3205 to +0.4595 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3992 | 3383 | -15.3% | -1263 to +44.35 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6213 | 5773 | -7.1% | -1116 to +237.2 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 53.13 | 52.63 | -0.9% | -1.458 to +0.4705 | STEADY, inside the noise (cut) |
| failed requests (%) | 36.08 | 39.46 | +9.4% | +0.9805 to +5.782 | LOSS |
| HPA replicas, mean | 9.809 | 11.8 | +20.3% | +1.399 to +2.578 | power given |
| pods started | 4.16 | 8.16 | +96.2% | +3.276 to +4.724 | power given |
| worker nodes in service, mean | 5.999 | 5.998 | -0.0% | -0.005175 to +0.003518 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.5 | 276.6 | +0.0% | -0.4206 to +0.5686 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.5 | 276.5 | +0.0% | -0.4309 to +0.5271 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.431 | 2.475 | +1.8% | +0.03129 to +0.05748 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.7 | 80.36 | +7.6% | +5.308 to +6.01 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.68 | 0.414 | -39.1% | -0.3039 to -0.2281 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

49 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3604 | 3098 | -14.0% | -1082 to +69.94 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5784 | 5529 | -4.4% | -912 to +402.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 54.36 | 53.48 | -1.6% | -2.025 to +0.2683 | STEADY, inside the noise (cut) |
| failed requests (%) | 38.76 | 40.21 | +3.7% | -1.057 to +3.95 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.829 | 11.48 | +16.8% | +1 to +2.295 | power given |
| pods started | 3.714 | 7.49 | +101.6% | +2.738 to +4.813 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.0007592 to +0.0002549 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.9 | 276.8 | -0.0% | -0.4982 to +0.3978 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.9 | 276.8 | -0.0% | -0.5061 to +0.3904 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.443 | 2.496 | +2.1% | +0.03345 to +0.07122 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.81 | 82.71 | +9.1% | +6.438 to +7.367 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | power given |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | power given |
| organism behind its window (s) | 0.7735 | 0.5163 | -33.2% | -0.3258 to -0.1885 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

49 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3155 | 2878 | -8.8% | -802.2 to +248.1 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5728 | 5128 | -10.5% | -1273 to +72.41 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 51.16 | 52.69 | +3.0% | -0.6518 to +3.712 | STEADY, inside the noise (up) |
| failed requests (%) | 37.62 | 41.31 | +9.8% | +1.456 to +5.918 | LOSS |
| HPA replicas, mean | 9.8 | 11.39 | +16.3% | +0.9491 to +2.238 | power given |
| pods started | 4.143 | 8.367 | +102.0% | +3.36 to +5.089 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +2.735e-16 to +1.322e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277 | 277.2 | +0.1% | -0.3253 to +0.6822 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277 | 277.2 | +0.1% | -0.3253 to +0.6822 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.45 | 2.514 | +2.6% | +0.04089 to +0.08778 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.39 | 82.8 | +11.3% | +7.79 to +9.036 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.5041 | 1.08 | +114.2% | +0.5355 to +0.6155 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
