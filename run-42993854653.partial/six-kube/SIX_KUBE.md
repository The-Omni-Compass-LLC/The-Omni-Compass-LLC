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
| response time (ms), 95th percentile | 4973 | 4337 | 4402 | 3949 | 4574 | 3025 | 4147 | 2676 | 4001 | 3909 |
| response time (ms), 99th percentile | 6968 | 6896 | 6508 | 6237 | 6584 | 5304 | 6341 | 4970 | 6599 | 6608 |
| time over the response line (% of samples) | 55.89 | 56.97 | 55.14 | 56.95 | 56.5 | 54.92 | 57.95 | 55.31 | 63.08 | 62.97 |
| failed requests (%) | 35.19 | 38.35 | 38.68 | 41.32 | 38.76 | 41.26 | 42.78 | 45.95 | 47.97 | 47.6 |
| HPA replicas, mean | 9.796 | 12.38 | 9.794 | 11.69 | 9.811 | 11.93 | 9.824 | 11.3 | 9.828 | 11.3 |
| pods started | 4.52 | 9.74 | 4.68 | 7.62 | 4.12 | 8.88 | 3.7 | 8.143 | 3.9 | 6.58 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 5.999 | 6 | 6 | 5.998 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 277.8 | 278 | 276.9 | 277.2 | 277.3 | 276.9 | 276.9 | 276.7 | 278.3 | 277.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.8 | 278 | 276.9 | 277.2 | 277.3 | 276.9 | 276.9 | 276.6 | 278.3 | 277.8 |
| CPU used with Omni's own (cores), mean | 2.521 | 2.564 | 2.464 | 2.523 | 2.477 | 2.511 | 2.446 | 2.477 | 2.548 | 2.581 |
| host CPU busy, the real machine under kind (%) | 74.42 | 79.01 | 74.97 | 83.62 | 75.74 | 81.09 | 75.81 | 81.66 | 77.45 | 84.83 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.44 | 0.532 | 0.894 | 1.18 | 0.612 | 0.406 | 0.79 | 0.4571 | 0.51 | 1.214 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 2 (response time (ms), 95th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4973 | 4337 | -12.8% | -1188 to -84.41 | GAIN |
| response time (ms), 99th percentile | 6968 | 6896 | -1.0% | -519.3 to +375.2 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 55.89 | 56.97 | +1.9% | -0.1683 to +2.341 | STEADY, inside the noise (up) |
| failed requests (%) | 35.19 | 38.35 | +9.0% | +1.148 to +5.176 | LOSS |
| HPA replicas, mean | 9.796 | 12.38 | +26.3% | +2.094 to +3.067 | power given |
| pods started | 4.52 | 9.74 | +115.5% | +4.379 to +6.061 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.937e-16 to +5.424e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.8 | 278 | +0.1% | -0.2474 to +0.6641 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.8 | 278 | +0.1% | -0.2474 to +0.6641 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.521 | 2.564 | +1.7% | +0.03319 to +0.05402 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.42 | 79.01 | +6.2% | +4.283 to +4.9 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.44 | 0.532 | +20.9% | +0.05228 to +0.1317 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4402 | 3949 | -10.3% | -992.9 to +85.85 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6508 | 6237 | -4.2% | -787.7 to +247 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 55.14 | 56.95 | +3.3% | -0.09524 to +3.719 | STEADY, inside the noise (up) |
| failed requests (%) | 38.68 | 41.32 | +6.8% | -0.472 to +5.766 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.794 | 11.69 | +19.4% | +1.266 to +2.534 | power given |
| pods started | 4.68 | 7.62 | +62.8% | +2.091 to +3.789 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +1.816e-16 to +1.168e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.9 | 277.2 | +0.1% | -0.2668 to +0.7728 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.9 | 277.2 | +0.1% | -0.2668 to +0.7728 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.464 | 2.523 | +2.4% | +0.03524 to +0.08159 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.97 | 83.62 | +11.5% | +8.028 to +9.267 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.894 | 1.18 | +32.0% | +0.252 to +0.32 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4574 | 3025 | -33.9% | -2199 to -898.4 | GAIN |
| response time (ms), 99th percentile | 6584 | 5304 | -19.4% | -1957 to -603.3 | GAIN |
| time over the response line (% of samples) | 56.5 | 54.92 | -2.8% | -2.793 to -0.3786 | GAIN |
| failed requests (%) | 38.76 | 41.26 | +6.4% | -0.1978 to +5.181 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.811 | 11.93 | +21.6% | +1.49 to +2.741 | power given |
| pods started | 4.12 | 8.88 | +115.5% | +3.931 to +5.589 | power given |
| worker nodes in service, mean | 5.999 | 6 | +0.0% | -0.0007144 to +0.002129 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.3 | 276.9 | -0.1% | -0.8617 to +0.08501 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.3 | 276.9 | -0.1% | -0.8509 to +0.1167 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.477 | 2.511 | +1.4% | +0.02374 to +0.04458 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.74 | 81.09 | +7.1% | +5.053 to +5.647 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.612 | 0.406 | -33.7% | -0.2464 to -0.1656 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

49 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4104 | 2676 | -34.8% | -2113 to -743.1 | GAIN |
| response time (ms), 99th percentile | 6315 | 4970 | -21.3% | -1985 to -705.2 | GAIN |
| time over the response line (% of samples) | 57.3 | 55.31 | -3.5% | -2.858 to -1.136 | GAIN |
| failed requests (%) | 41.97 | 45.95 | +9.5% | +1.857 to +6.111 | LOSS |
| HPA replicas, mean | 9.82 | 11.3 | +15.0% | +0.8534 to +2.101 | power given |
| pods started | 3.776 | 8.143 | +115.7% | +3.329 to +5.406 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.007369 to +0.002474 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.9 | 276.7 | -0.1% | -0.654 to +0.2352 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.9 | 276.6 | -0.1% | -0.771 to +0.2042 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.447 | 2.477 | +1.3% | +0.01799 to +0.04358 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.49 | 81.66 | +8.2% | +5.871 to +6.467 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | power given |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | power given |
| organism behind its window (s) | 0.7776 | 0.4571 | -41.2% | -0.3873 to -0.2536 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4001 | 3909 | -2.3% | -824.7 to +641.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6599 | 6608 | +0.1% | -585.8 to +603.6 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 63.08 | 62.97 | -0.2% | -2.036 to +1.819 | STEADY, inside the noise (cut) |
| failed requests (%) | 47.97 | 47.6 | -0.8% | -2.925 to +2.192 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.828 | 11.3 | +15.0% | +0.9199 to +2.024 | power given |
| pods started | 3.9 | 6.58 | +68.7% | +1.736 to +3.624 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +6.067e-16 to +1.667e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 278.3 | 277.8 | -0.2% | -1.24 to +0.2362 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 278.3 | 277.8 | -0.2% | -1.24 to +0.2362 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.548 | 2.581 | +1.3% | +0.01994 to +0.04617 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.45 | 84.83 | +9.5% | +7.091 to +7.664 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.51 | 1.214 | +138.0% | +0.464 to +0.944 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
