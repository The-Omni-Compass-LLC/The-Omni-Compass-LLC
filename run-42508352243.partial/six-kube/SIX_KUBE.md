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
| response time (ms), 95th percentile | 3722 | 3151 | 4013 | 3577 | 4249 | 3356 | 4011 | 3099 | 3170 | 3132 |
| response time (ms), 99th percentile | 5500 | 5443 | 6207 | 5614 | 6110 | 5661 | 6309 | 5406 | 5429 | 5223 |
| time over the response line (% of samples) | 49.28 | 49.6 | 55.98 | 56.11 | 51.69 | 51.24 | 57.56 | 56.51 | 54.64 | 54.15 |
| failed requests (%) | 32.96 | 36.09 | 39.82 | 45.46 | 34.56 | 37.88 | 41.23 | 44.74 | 43.29 | 42.06 |
| HPA replicas, mean | 9.777 | 12.84 | 9.809 | 11.23 | 9.795 | 12.07 | 9.821 | 11.35 | 9.812 | 11.79 |
| pods started | 4.72 | 9.62 | 4.06 | 6.52 | 4.32 | 9.28 | 3.88 | 7.34 | 3.96 | 7.64 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 5.999 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.3 | 276.2 | 276.6 | 276.5 | 276.5 | 276.5 | 277.3 | 277.1 | 276.7 | 276.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.3 | 276.2 | 276.6 | 276.5 | 276.5 | 276.5 | 277.3 | 277.1 | 276.7 | 276.7 |
| CPU used with Omni's own (cores), mean | 2.415 | 2.466 | 2.441 | 2.49 | 2.424 | 2.468 | 2.477 | 2.524 | 2.448 | 2.495 |
| host CPU busy, the real machine under kind (%) | 71.14 | 75.82 | 74.14 | 82.47 | 73.68 | 79.18 | 76.05 | 82.48 | 73.92 | 81.52 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.424 | 0.508 | 0.87 | 1.142 | 0.568 | 0.418 | 0.722 | 0.44 | 0.492 | 1.032 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3722 | 3151 | -15.3% | -1245 to +103 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5500 | 5443 | -1.0% | -632.5 to +517.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 49.28 | 49.6 | +0.7% | -1.08 to +1.729 | STEADY, inside the noise (up) |
| failed requests (%) | 32.96 | 36.09 | +9.5% | +1.398 to +4.874 | LOSS |
| HPA replicas, mean | 9.777 | 12.84 | +31.4% | +2.526 to +3.61 | power given |
| pods started | 4.72 | 9.62 | +103.8% | +4.268 to +5.532 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.352e-16 to +1.022e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.3 | 276.2 | -0.0% | -0.4489 to +0.288 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.3 | 276.2 | -0.0% | -0.4489 to +0.288 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.415 | 2.466 | +2.1% | +0.03939 to +0.06156 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.14 | 75.82 | +6.6% | +4.373 to +4.975 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.424 | 0.508 | +19.8% | +0.05133 to +0.1167 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 2 (response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4013 | 3577 | -10.9% | -1026 to +153.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6207 | 5614 | -9.6% | -1167 to -18.53 | GAIN |
| time over the response line (% of samples) | 55.98 | 56.11 | +0.2% | -1.394 to +1.66 | STEADY, inside the noise (up) |
| failed requests (%) | 39.82 | 45.46 | +14.2% | +3.11 to +8.162 | LOSS |
| HPA replicas, mean | 9.809 | 11.23 | +14.5% | +0.7706 to +2.075 | power given |
| pods started | 4.06 | 6.52 | +60.6% | +1.592 to +3.328 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.0008281 to +0.0002779 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.6 | 276.5 | -0.0% | -0.5083 to +0.3368 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.6 | 276.5 | -0.0% | -0.5155 to +0.3274 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.441 | 2.49 | +2.0% | +0.03061 to +0.06712 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.14 | 82.47 | +11.2% | +7.844 to +8.823 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.87 | 1.142 | +31.3% | +0.225 to +0.319 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 2 (response time (ms), 95th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4249 | 3356 | -21.0% | -1459 to -325.7 | GAIN |
| response time (ms), 99th percentile | 6110 | 5661 | -7.4% | -929.1 to +29.43 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 51.69 | 51.24 | -0.9% | -1.51 to +0.5965 | STEADY, inside the noise (cut) |
| failed requests (%) | 34.56 | 37.88 | +9.6% | +0.8755 to +5.765 | LOSS |
| HPA replicas, mean | 9.795 | 12.07 | +23.2% | +1.669 to +2.885 | power given |
| pods started | 4.32 | 9.28 | +114.8% | +3.999 to +5.921 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.573e-16 to +8.679e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.5 | 276.5 | +0.0% | -0.309 to +0.3459 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.5 | 276.5 | +0.0% | -0.309 to +0.3459 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.424 | 2.468 | +1.8% | +0.02873 to +0.05848 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.68 | 79.18 | +7.5% | +5.103 to +5.898 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.568 | 0.418 | -26.4% | -0.1855 to -0.1145 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4011 | 3099 | -22.7% | -1769 to -56.02 | GAIN |
| response time (ms), 99th percentile | 6309 | 5406 | -14.3% | -1678 to -127.5 | GAIN |
| time over the response line (% of samples) | 57.56 | 56.51 | -1.8% | -2.114 to +0.01052 | STEADY, inside the noise (cut) |
| failed requests (%) | 41.23 | 44.74 | +8.5% | +1.536 to +5.497 | LOSS |
| HPA replicas, mean | 9.821 | 11.35 | +15.6% | +0.914 to +2.154 | power given |
| pods started | 3.88 | 7.34 | +89.2% | +2.317 to +4.603 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +1.728e-17 to +1.12e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.3 | 277.1 | -0.1% | -0.7053 to +0.2465 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.3 | 277.1 | -0.1% | -0.7053 to +0.2465 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.477 | 2.524 | +1.9% | +0.0304 to +0.06254 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.05 | 82.48 | +8.5% | +6.004 to +6.871 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | power given |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | power given |
| organism behind its window (s) | 0.722 | 0.44 | -39.1% | -0.3323 to -0.2317 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3170 | 3132 | -1.2% | -792.2 to +717.4 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5429 | 5223 | -3.8% | -959.9 to +547.6 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 54.64 | 54.15 | -0.9% | -1.286 to +0.3035 | STEADY, inside the noise (cut) |
| failed requests (%) | 43.29 | 42.06 | -2.8% | -3.44 to +0.9822 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.812 | 11.79 | +20.2% | +1.301 to +2.664 | power given |
| pods started | 3.96 | 7.64 | +92.9% | +2.851 to +4.509 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003512 to +0.001178 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.7 | 276.8 | +0.0% | -0.3957 to +0.4973 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.7 | 276.7 | +0.0% | -0.4203 to +0.4511 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.448 | 2.495 | +1.9% | +0.02909 to +0.06502 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.92 | 81.52 | +10.3% | +7.174 to +8.03 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.492 | 1.032 | +109.8% | +0.5075 to +0.5725 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
