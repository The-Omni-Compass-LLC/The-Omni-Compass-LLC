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
| response time (ms), 95th percentile | 4070 | 3624 | 4166 | 4248 | 3092 | 2909 | 3937 | 3237 | 2779 | 3330 |
| response time (ms), 99th percentile | 6423 | 6225 | 6614 | 6727 | 5725 | 5363 | 5992 | 5328 | 5358 | 5451 |
| time over the response line (% of samples) | 48.36 | 49.29 | 54.17 | 56.53 | 42.13 | 43.22 | 48.77 | 48.07 | 48.4 | 50.16 |
| failed requests (%) | 30.52 | 32.84 | 37.03 | 42.23 | 26.51 | 28.75 | 33.34 | 36.09 | 35.19 | 36.69 |
| HPA replicas, mean | 9.782 | 13.07 | 9.805 | 11.31 | 9.758 | 12.76 | 9.778 | 11.78 | 9.764 | 11.8 |
| pods started | 4.6 | 10.44 | 4.4 | 7.48 | 5.14 | 10.82 | 4.58 | 9.28 | 4.98 | 8.8 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.7 | 276.8 | 277.7 | 277.5 | 275.8 | 275.8 | 276.1 | 276 | 276.4 | 276.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.7 | 276.8 | 277.7 | 277.5 | 275.8 | 275.8 | 276.1 | 276 | 276.4 | 276.5 |
| CPU used with Omni's own (cores), mean | 2.452 | 2.504 | 2.512 | 2.558 | 2.381 | 2.436 | 2.4 | 2.445 | 2.43 | 2.482 |
| host CPU busy, the real machine under kind (%) | 72.42 | 77.2 | 75.95 | 84.06 | 72.66 | 78.5 | 73.5 | 79.85 | 73.1 | 80.89 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.442 | 0.516 | 0.794 | 1.174 | 0.654 | 0.398 | 0.726 | 0.452 | 0.498 | 1.05 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4070 | 3624 | -11.0% | -996.8 to +104.3 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6423 | 6225 | -3.1% | -607.5 to +212.1 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 48.36 | 49.29 | +1.9% | -0.3905 to +2.253 | STEADY, inside the noise (up) |
| failed requests (%) | 30.52 | 32.84 | +7.6% | +0.2802 to +4.373 | LOSS |
| HPA replicas, mean | 9.782 | 13.07 | +33.6% | +2.828 to +3.752 | power given |
| pods started | 4.6 | 10.44 | +127.0% | +5.122 to +6.558 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.163e-15 to -2.934e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.7 | 276.8 | +0.1% | -0.2431 to +0.5515 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.7 | 276.8 | +0.1% | -0.2431 to +0.5515 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.452 | 2.504 | +2.1% | +0.04109 to +0.06346 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.42 | 77.2 | +6.6% | +4.462 to +5.106 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.442 | 0.516 | +16.7% | +0.02567 to +0.1223 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (time over the response line (% of samples); failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4166 | 4248 | +2.0% | -613.6 to +777.7 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6614 | 6727 | +1.7% | -372.5 to +599.8 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 54.17 | 56.53 | +4.3% | +0.3304 to +4.38 | LOSS |
| failed requests (%) | 37.03 | 42.23 | +14.0% | +2.29 to +8.105 | LOSS |
| HPA replicas, mean | 9.805 | 11.31 | +15.3% | +0.8915 to +2.113 | power given |
| pods started | 4.4 | 7.48 | +70.0% | +2.238 to +3.922 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +3.284e-16 to +1.27e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.7 | 277.5 | -0.1% | -0.5845 to +0.2989 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.7 | 277.5 | -0.1% | -0.5845 to +0.2989 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.512 | 2.558 | +1.8% | +0.02839 to +0.06387 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.95 | 84.06 | +10.7% | +7.655 to +8.552 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.794 | 1.174 | +47.9% | +0.324 to +0.436 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3092 | 2909 | -5.9% | -760.4 to +396.1 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5725 | 5363 | -6.3% | -899.8 to +176.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 42.13 | 43.22 | +2.6% | -0.4341 to +2.617 | STEADY, inside the noise (up) |
| failed requests (%) | 26.51 | 28.75 | +8.5% | +0.1378 to +4.35 | LOSS |
| HPA replicas, mean | 9.758 | 12.76 | +30.7% | +2.448 to +3.545 | power given |
| pods started | 5.14 | 10.82 | +110.5% | +4.67 to +6.69 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +2.313e-16 to +1.296e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.8 | 275.8 | -0.0% | -0.5282 to +0.3984 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.8 | 275.8 | -0.0% | -0.5282 to +0.3984 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.381 | 2.436 | +2.3% | +0.04291 to +0.06706 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.66 | 78.5 | +8.0% | +5.5 to +6.172 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.654 | 0.398 | -39.1% | -0.3044 to -0.2076 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 2 (response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3937 | 3237 | -17.8% | -1574 to +175.5 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5992 | 5328 | -11.1% | -1305 to -23.26 | GAIN |
| time over the response line (% of samples) | 48.77 | 48.07 | -1.4% | -1.873 to +0.4817 | STEADY, inside the noise (cut) |
| failed requests (%) | 33.34 | 36.09 | +8.3% | +0.5908 to +4.916 | LOSS |
| HPA replicas, mean | 9.778 | 11.78 | +20.5% | +1.341 to +2.666 | power given |
| pods started | 4.58 | 9.28 | +102.6% | +3.671 to +5.729 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +3.202e-16 to +1.385e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.1 | 276 | -0.0% | -0.6345 to +0.3987 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.1 | 276 | -0.0% | -0.6345 to +0.3987 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.4 | 2.445 | +1.9% | +0.02711 to +0.06318 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.5 | 79.85 | +8.6% | +5.861 to +6.836 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | power given |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | power given |
| organism behind its window (s) | 0.726 | 0.452 | -37.7% | -0.3448 to -0.2032 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2779 | 3330 | +19.8% | -165.5 to +1268 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5358 | 5451 | +1.7% | -680.3 to +866.4 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 48.4 | 50.16 | +3.6% | -0.4665 to +3.986 | STEADY, inside the noise (up) |
| failed requests (%) | 35.19 | 36.69 | +4.3% | -1.463 to +4.464 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.764 | 11.8 | +20.8% | +1.354 to +2.709 | power given |
| pods started | 4.98 | 8.8 | +76.7% | +2.965 to +4.675 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +4.924e-16 to +1.462e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.4 | 276.5 | +0.1% | -0.2969 to +0.6218 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.4 | 276.5 | +0.1% | -0.2969 to +0.6218 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.43 | 2.482 | +2.1% | +0.03366 to +0.06921 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.1 | 80.89 | +10.7% | +7.311 to +8.27 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.498 | 1.05 | +110.8% | +0.4925 to +0.6115 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
