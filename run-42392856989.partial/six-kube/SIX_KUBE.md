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
| response time (ms), 95th percentile | 3638 | 2770 | 3978 | 4602 | 4249 | 3327 | 3655 | 3060 | 2845 | 2747 |
| response time (ms), 99th percentile | 5801 | 4994 | 6311 | 6375 | 6285 | 5671 | 6006 | 5591 | 5113 | 4934 |
| time over the response line (% of samples) | 44.99 | 45.77 | 52.44 | 54.89 | 53.26 | 52.51 | 54.31 | 53.41 | 50.15 | 49.58 |
| failed requests (%) | 29.07 | 32.05 | 36.64 | 38.26 | 35.34 | 37.66 | 37.84 | 41.08 | 38.66 | 38.43 |
| HPA replicas, mean | 9.775 | 13.07 | 9.785 | 11.43 | 9.781 | 11.91 | 9.798 | 11.18 | 9.792 | 11.78 |
| pods started | 4.56 | 10.44 | 4.8 | 7.68 | 4.74 | 9.12 | 4.24 | 8.1 | 4.38 | 8.54 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.4 | 275.8 | 276.9 | 277.1 | 276.8 | 276.6 | 276.7 | 276.5 | 276 | 276.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.4 | 275.8 | 276.9 | 277.1 | 276.8 | 276.6 | 276.7 | 276.4 | 276 | 276.5 |
| CPU used with Omni's own (cores), mean | 2.369 | 2.424 | 2.464 | 2.516 | 2.438 | 2.477 | 2.44 | 2.481 | 2.417 | 2.471 |
| host CPU busy, the real machine under kind (%) | 69.76 | 74.41 | 74.27 | 82.36 | 74.06 | 79.35 | 75 | 81.21 | 72.68 | 80.44 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.402 | 0.524 | 0.898 | 1.144 | 0.586 | 0.416 | 0.708 | 0.438 | 0.478 | 1.05 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3638 | 2770 | -23.9% | -1445 to -290.9 | GAIN |
| response time (ms), 99th percentile | 5801 | 4994 | -13.9% | -1335 to -278.6 | GAIN |
| time over the response line (% of samples) | 44.99 | 45.77 | +1.7% | -0.6579 to +2.199 | STEADY, inside the noise (up) |
| failed requests (%) | 29.07 | 32.05 | +10.3% | +0.976 to +4.984 | LOSS |
| HPA replicas, mean | 9.775 | 13.07 | +33.7% | +2.738 to +3.851 | power given |
| pods started | 4.56 | 10.44 | +128.9% | +5.019 to +6.741 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.73e-16 to -8.554e-18 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.4 | 275.8 | +0.1% | -0.05256 to +0.7878 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.4 | 275.8 | +0.1% | -0.05256 to +0.7878 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.369 | 2.424 | +2.3% | +0.04232 to +0.06727 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.76 | 74.41 | +6.7% | +4.302 to +5.01 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.402 | 0.524 | +30.3% | +0.0756 to +0.1684 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (time over the response line (% of samples)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3978 | 4602 | +15.7% | -25.09 to +1273 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6311 | 6375 | +1.0% | -434.9 to +563.4 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 52.44 | 54.89 | +4.7% | +0.1041 to +4.804 | LOSS |
| failed requests (%) | 36.64 | 38.26 | +4.4% | -1.364 to +4.6 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.785 | 11.43 | +16.8% | +1.008 to +2.274 | power given |
| pods started | 4.8 | 7.68 | +60.0% | +2.039 to +3.721 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +2.964e-16 to +1.302e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.9 | 277.1 | +0.1% | -0.2757 to +0.5847 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.9 | 277.1 | +0.1% | -0.2757 to +0.5847 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.464 | 2.516 | +2.1% | +0.03286 to +0.07017 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.27 | 82.36 | +10.9% | +7.614 to +8.563 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.898 | 1.144 | +27.4% | +0.1863 to +0.3057 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4249 | 3327 | -21.7% | -1458 to -386.4 | GAIN |
| response time (ms), 99th percentile | 6285 | 5671 | -9.8% | -1126 to -102.4 | GAIN |
| time over the response line (% of samples) | 53.26 | 52.51 | -1.4% | -1.947 to +0.4588 | STEADY, inside the noise (cut) |
| failed requests (%) | 35.34 | 37.66 | +6.6% | -0.2932 to +4.943 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.781 | 11.91 | +21.8% | +1.578 to +2.689 | power given |
| pods started | 4.74 | 9.12 | +92.4% | +3.491 to +5.269 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +2.089e-16 to +1.248e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.8 | 276.6 | -0.0% | -0.553 to +0.2838 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.8 | 276.6 | -0.0% | -0.553 to +0.2838 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.438 | 2.477 | +1.6% | +0.02718 to +0.0523 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.06 | 79.35 | +7.1% | +4.927 to +5.65 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.586 | 0.416 | -29.0% | -0.2205 to -0.1195 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3655 | 3060 | -16.3% | -1226 to +36.7 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6006 | 5591 | -6.9% | -1020 to +192.2 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 54.31 | 53.41 | -1.7% | -2.278 to +0.4649 | STEADY, inside the noise (cut) |
| failed requests (%) | 37.84 | 41.08 | +8.6% | +0.9816 to +5.5 | LOSS |
| HPA replicas, mean | 9.798 | 11.18 | +14.1% | +0.8191 to +1.935 | power given |
| pods started | 4.24 | 8.1 | +91.0% | +2.772 to +4.948 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.0007478 to +0.0002509 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.7 | 276.5 | -0.1% | -0.734 to +0.2177 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.7 | 276.4 | -0.1% | -0.7423 to +0.211 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.44 | 2.481 | +1.7% | +0.02437 to +0.05697 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75 | 81.21 | +8.3% | +5.802 to +6.614 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | power given |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | power given |
| organism behind its window (s) | 0.708 | 0.438 | -38.1% | -0.3181 to -0.2219 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 4

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2845 | 2747 | -3.4% | -695.4 to +499.2 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5113 | 4934 | -3.5% | -954.2 to +595.9 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 50.15 | 49.58 | -1.1% | -1.854 to +0.7057 | STEADY, inside the noise (cut) |
| failed requests (%) | 38.66 | 38.43 | -0.6% | -2.075 to +1.603 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.792 | 11.78 | +20.3% | +1.294 to +2.677 | power given |
| pods started | 4.38 | 8.54 | +95.0% | +3.165 to +5.155 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +3.314e-17 to +1.033e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276 | 276.5 | +0.2% | +0.01694 to +0.8794 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276 | 276.5 | +0.2% | +0.01694 to +0.8794 | power given |
| CPU used with Omni's own (cores), mean | 2.417 | 2.471 | +2.2% | +0.03261 to +0.07497 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.68 | 80.44 | +10.7% | +7.243 to +8.269 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.478 | 1.05 | +119.7% | +0.5302 to +0.6138 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
