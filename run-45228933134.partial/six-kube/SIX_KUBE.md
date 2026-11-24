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
| response time (ms), 95th percentile | 3783 | 3052 | 4119 | 3541 | 3613 | 3098 | 4303 | 2932 | 3905 | 3539 |
| response time (ms), 99th percentile | 6131 | 5468 | 6316 | 5938 | 6254 | 5897 | 6774 | 5279 | 6147 | 5781 |
| time over the response line (% of samples) | 53.79 | 53.62 | 52.98 | 54.35 | 57.51 | 56.54 | 55.7 | 54.9 | 59.03 | 59.02 |
| failed requests (%) | 38.88 | 42.22 | 37.06 | 41.69 | 40.46 | 44.91 | 38.41 | 43.97 | 43.9 | 46.37 |
| HPA replicas, mean | 9.809 | 12.85 | 9.793 | 11.33 | 9.821 | 11.35 | 9.795 | 10.99 | 9.816 | 11.06 |
| pods started | 4.06 | 8.98 | 4.612 | 7.878 | 3.98 | 8.62 | 4.4 | 7.96 | 4.02 | 6.96 |
| worker nodes in service, mean | 6 | 5.999 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 277 | 276.8 | 277 | 277.1 | 277.5 | 277.5 | 277.3 | 277.1 | 277.9 | 277.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277 | 276.8 | 277 | 277.1 | 277.5 | 277.5 | 277.3 | 277.1 | 277.9 | 277.7 |
| CPU used with Omni's own (cores), mean | 2.463 | 2.511 | 2.453 | 2.512 | 2.491 | 2.536 | 2.474 | 2.519 | 2.507 | 2.55 |
| host CPU busy, the real machine under kind (%) | 73.3 | 78.03 | 74.44 | 83.27 | 76.62 | 82.52 | 76.17 | 82.63 | 76.33 | 84.3 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.424 | 0.582 | 0.8082 | 1.239 | 0.712 | 0.44 | 0.748 | 0.43 | 0.53 | 1.11 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3783 | 3052 | -19.3% | -1494 to +32.86 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6131 | 5468 | -10.8% | -1407 to +80.96 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 53.79 | 53.62 | -0.3% | -1.366 to +1.027 | STEADY, inside the noise (cut) |
| failed requests (%) | 38.88 | 42.22 | +8.6% | +1.24 to +5.444 | LOSS |
| HPA replicas, mean | 9.809 | 12.85 | +31.0% | +2.511 to +3.569 | power given |
| pods started | 4.06 | 8.98 | +121.2% | +4.187 to +5.653 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001997 to +0.0006701 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 277 | 276.8 | -0.1% | -0.6589 to +0.2709 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277 | 276.8 | -0.1% | -0.6846 to +0.2566 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.463 | 2.511 | +2.0% | +0.03726 to +0.06049 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.3 | 78.03 | +6.5% | +4.393 to +5.063 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.424 | 0.582 | +37.3% | +0.1053 to +0.2107 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

49 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4119 | 3541 | -14.0% | -1217 to +61.07 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6316 | 5938 | -6.0% | -902.9 to +147.1 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 52.98 | 54.35 | +2.6% | -0.4525 to +3.199 | STEADY, inside the noise (up) |
| failed requests (%) | 37.06 | 41.69 | +12.5% | +1.808 to +7.46 | LOSS |
| HPA replicas, mean | 9.793 | 11.33 | +15.7% | +0.8854 to +2.194 | power given |
| pods started | 4.612 | 7.878 | +70.8% | +2.339 to +4.192 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +4.875e-16 to +1.216e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277 | 277.1 | +0.0% | -0.4562 to +0.7017 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277 | 277.1 | +0.0% | -0.4562 to +0.7017 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.453 | 2.512 | +2.4% | +0.03595 to +0.08274 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.44 | 83.27 | +11.9% | +8.238 to +9.409 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.8082 | 1.239 | +53.3% | +0.3607 to +0.5005 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3613 | 3098 | -14.2% | -1183 to +154.5 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6254 | 5897 | -5.7% | -992.7 to +279.2 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 57.51 | 56.54 | -1.7% | -2.236 to +0.3126 | STEADY, inside the noise (cut) |
| failed requests (%) | 40.46 | 44.91 | +11.0% | +2.371 to +6.526 | LOSS |
| HPA replicas, mean | 9.821 | 11.35 | +15.5% | +0.9265 to +2.126 | power given |
| pods started | 3.98 | 8.62 | +116.6% | +3.762 to +5.518 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +5.035e-16 to +1.415e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.5 | 277.5 | -0.0% | -0.5095 to +0.3823 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.5 | 277.5 | -0.0% | -0.5095 to +0.3823 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.491 | 2.536 | +1.8% | +0.03131 to +0.0591 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.62 | 82.52 | +7.7% | +5.554 to +6.248 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.712 | 0.44 | -38.2% | -0.3289 to -0.2151 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4303 | 2932 | -31.9% | -2173 to -569.6 | GAIN |
| response time (ms), 99th percentile | 6774 | 5279 | -22.1% | -2285 to -705.7 | GAIN |
| time over the response line (% of samples) | 55.7 | 54.9 | -1.4% | -2.062 to +0.4567 | STEADY, inside the noise (cut) |
| failed requests (%) | 38.41 | 43.97 | +14.5% | +3.12 to +7.997 | LOSS |
| HPA replicas, mean | 9.795 | 10.99 | +12.2% | +0.6605 to +1.721 | power given |
| pods started | 4.4 | 7.96 | +80.9% | +2.592 to +4.528 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +5.985e-16 to +1.498e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.3 | 277.1 | -0.1% | -0.7485 to +0.2468 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.3 | 277.1 | -0.1% | -0.7485 to +0.2468 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.474 | 2.519 | +1.8% | +0.02886 to +0.0601 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.17 | 82.63 | +8.5% | +6.051 to +6.865 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | power given |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | power given |
| organism behind its window (s) | 0.748 | 0.43 | -42.5% | -0.3652 to -0.2708 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3905 | 3539 | -9.4% | -1008 to +274.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6147 | 5781 | -6.0% | -1035 to +302.5 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 59.03 | 59.02 | -0.0% | -1.773 to +1.746 | STEADY, inside the noise (cut) |
| failed requests (%) | 43.9 | 46.37 | +5.6% | +0.3572 to +4.585 | LOSS |
| HPA replicas, mean | 9.816 | 11.06 | +12.6% | +0.6544 to +1.825 | power given |
| pods started | 4.02 | 6.96 | +73.1% | +1.96 to +3.92 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +2.003e-16 to +1.043e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.9 | 277.7 | -0.1% | -0.6545 to +0.2908 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.9 | 277.7 | -0.1% | -0.6545 to +0.2908 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.507 | 2.55 | +1.7% | +0.02491 to +0.06095 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.33 | 84.3 | +10.4% | +7.559 to +8.38 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.53 | 1.11 | +109.4% | +0.5123 to +0.6477 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
