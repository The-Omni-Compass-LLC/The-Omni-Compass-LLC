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
| response time (ms), 95th percentile | 4007 | 3634 | 4035 | 3794 | 3856 | 2884 | 3936 | 2838 | 2788 | 2678 |
| response time (ms), 99th percentile | 6250 | 5947 | 6012 | 5889 | 6078 | 5113 | 5959 | 5162 | 4904 | 4773 |
| time over the response line (% of samples) | 50.98 | 52 | 54.6 | 54.6 | 53.33 | 51.97 | 50.02 | 49.34 | 49.96 | 49.81 |
| failed requests (%) | 33 | 36.14 | 39.5 | 40.46 | 37.21 | 42.1 | 34.46 | 37.08 | 38.48 | 37.95 |
| HPA replicas, mean | 9.784 | 12.35 | 9.8 | 11.58 | 9.811 | 11.75 | 9.786 | 11.62 | 9.778 | 11.82 |
| pods started | 4.5 | 9.3 | 4.4 | 7.18 | 4 | 8.62 | 4.64 | 9.48 | 4.68 | 8.531 |
| worker nodes in service, mean | 6 | 5.999 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.3 | 276.3 | 276.6 | 276.8 | 276.8 | 276.7 | 276.1 | 276.3 | 276.4 | 276.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.3 | 276.2 | 276.6 | 276.8 | 276.8 | 276.7 | 276.1 | 276.3 | 276.4 | 276.3 |
| CPU used with Omni's own (cores), mean | 2.428 | 2.471 | 2.44 | 2.485 | 2.434 | 2.483 | 2.406 | 2.457 | 2.411 | 2.465 |
| host CPU busy, the real machine under kind (%) | 71.9 | 76.58 | 74.18 | 82.35 | 74.71 | 80.54 | 73.85 | 80.41 | 73.04 | 80.98 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.482 | 0.536 | 0.922 | 1.2 | 0.638 | 0.438 | 0.73 | 0.446 | 0.522 | 1.084 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4007 | 3634 | -9.3% | -915.9 to +170.1 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6250 | 5947 | -4.8% | -977 to +371 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 50.98 | 52 | +2.0% | -0.4426 to +2.476 | STEADY, inside the noise (up) |
| failed requests (%) | 33 | 36.14 | +9.5% | +1.265 to +5.012 | LOSS |
| HPA replicas, mean | 9.784 | 12.35 | +26.2% | +1.965 to +3.157 | power given |
| pods started | 4.5 | 9.3 | +106.7% | +4.034 to +5.566 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.00321 to +0.001077 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.3 | 276.3 | -0.0% | -0.464 to +0.4377 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.3 | 276.2 | -0.0% | -0.525 to +0.4338 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.428 | 2.471 | +1.8% | +0.03317 to +0.05359 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.9 | 76.58 | +6.5% | +4.407 to +4.946 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.482 | 0.536 | +11.2% | -0.005185 to +0.1132 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4035 | 3794 | -6.0% | -800.1 to +318.1 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6012 | 5889 | -2.0% | -646.9 to +402.4 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 54.6 | 54.6 | -0.0% | -1.252 to +1.247 | STEADY, inside the noise (cut) |
| failed requests (%) | 39.5 | 40.46 | +2.4% | -1.357 to +3.279 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.8 | 11.58 | +18.2% | +1.127 to +2.433 | power given |
| pods started | 4.4 | 7.18 | +63.2% | +1.85 to +3.71 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.645e-17 to +1.082e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.6 | 276.8 | +0.0% | -0.3964 to +0.6628 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.6 | 276.8 | +0.0% | -0.3964 to +0.6628 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.44 | 2.485 | +1.8% | +0.02621 to +0.06333 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.18 | 82.35 | +11.0% | +7.743 to +8.593 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.922 | 1.2 | +30.2% | +0.2199 to +0.3361 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3856 | 2884 | -25.2% | -1663 to -281.5 | GAIN |
| response time (ms), 99th percentile | 6078 | 5113 | -15.9% | -1625 to -304.6 | GAIN |
| time over the response line (% of samples) | 53.33 | 51.97 | -2.5% | -2.393 to -0.3164 | GAIN |
| failed requests (%) | 37.21 | 42.1 | +13.1% | +2.716 to +7.064 | LOSS |
| HPA replicas, mean | 9.811 | 11.75 | +19.8% | +1.31 to +2.57 | power given |
| pods started | 4 | 8.62 | +115.5% | +3.616 to +5.624 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +2.284e-17 to +1.043e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.8 | 276.7 | -0.0% | -0.4942 to +0.3549 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.8 | 276.7 | -0.0% | -0.4942 to +0.3549 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.434 | 2.483 | +2.0% | +0.03276 to +0.06351 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.71 | 80.54 | +7.8% | +5.433 to +6.221 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.638 | 0.438 | -31.3% | -0.2542 to -0.1458 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3936 | 2838 | -27.9% | -1831 to -364.7 | GAIN |
| response time (ms), 99th percentile | 5959 | 5162 | -13.4% | -1344 to -248.6 | GAIN |
| time over the response line (% of samples) | 50.02 | 49.34 | -1.4% | -1.879 to +0.5083 | STEADY, inside the noise (cut) |
| failed requests (%) | 34.46 | 37.08 | +7.6% | +0.2673 to +4.975 | LOSS |
| HPA replicas, mean | 9.786 | 11.62 | +18.7% | +1.191 to +2.467 | power given |
| pods started | 4.64 | 9.48 | +104.3% | +3.671 to +6.009 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +1.987e-16 to +1.116e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.1 | 276.3 | +0.1% | -0.2568 to +0.7309 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.1 | 276.3 | +0.1% | -0.2568 to +0.7309 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.406 | 2.457 | +2.1% | +0.0345 to +0.06808 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.85 | 80.41 | +8.9% | +6.143 to +6.975 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | power given |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | power given |
| organism behind its window (s) | 0.73 | 0.446 | -38.9% | -0.3256 to -0.2424 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

49 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2706 | 2678 | -1.0% | -602.3 to +547.1 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4819 | 4773 | -1.0% | -618.2 to +525.1 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 49.45 | 49.81 | +0.7% | -0.9902 to +1.705 | STEADY, inside the noise (up) |
| failed requests (%) | 38.03 | 37.95 | -0.2% | -2.368 to +2.192 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.776 | 11.82 | +21.0% | +1.347 to +2.751 | power given |
| pods started | 4.714 | 8.531 | +81.0% | +2.873 to +4.759 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.281e-16 to +9.169e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.3 | 276.3 | +0.0% | -0.4899 to +0.4942 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.3 | 276.3 | +0.0% | -0.4899 to +0.4942 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.406 | 2.465 | +2.4% | +0.0373 to +0.07959 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.88 | 80.98 | +11.1% | +7.529 to +8.662 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.5224 | 1.084 | +107.4% | +0.5066 to +0.6159 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
