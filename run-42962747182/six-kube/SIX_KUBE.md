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
| response time (ms), 95th percentile | 4561 | 3997 | 3823 | 3530 | 4574 | 3538 | 4238 | 3207 | 2628 | 3044 |
| response time (ms), 99th percentile | 7000 | 6709 | 5696 | 5443 | 6732 | 5851 | 6092 | 5358 | 4671 | 5224 |
| time over the response line (% of samples) | 51.89 | 54.66 | 47.88 | 48.14 | 56.18 | 55.54 | 48.39 | 48.01 | 49.05 | 49.23 |
| failed requests (%) | 31.68 | 35.13 | 33.83 | 35.95 | 37.56 | 42.13 | 31.96 | 35.13 | 37.69 | 37.49 |
| HPA replicas, mean | 9.785 | 12.7 | 9.769 | 11.73 | 9.805 | 11.77 | 9.76 | 12.07 | 9.769 | 11.98 |
| pods started | 4.56 | 9.72 | 4.84 | 8.2 | 4.2 | 8.3 | 5.16 | 9.88 | 4.88 | 8.46 |
| worker nodes in service, mean | 6 | 5.997 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 277.2 | 277.5 | 276 | 275.7 | 277.4 | 277.1 | 276 | 275.7 | 276.1 | 276.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.2 | 277.4 | 276 | 275.7 | 277.4 | 277.1 | 276 | 275.7 | 276.1 | 276.1 |
| CPU used with Omni's own (cores), mean | 2.489 | 2.539 | 2.389 | 2.439 | 2.482 | 2.519 | 2.388 | 2.442 | 2.404 | 2.457 |
| host CPU busy, the real machine under kind (%) | 73.43 | 78.26 | 72.21 | 80.35 | 75.73 | 81.19 | 72.97 | 79.53 | 72.65 | 80.42 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.424 | 0.63 | 0.918 | 1.166 | 0.596 | 0.41 | 0.718 | 0.434 | 0.516 | 1.062 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 2 (response time (ms), 95th percentile; organism time over the line (% of steps)), LOSS on 2 (time over the response line (% of samples); failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4561 | 3997 | -12.4% | -1064 to -64.53 | GAIN |
| response time (ms), 99th percentile | 7000 | 6709 | -4.2% | -710.3 to +126.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 51.89 | 54.66 | +5.3% | +1.095 to +4.436 | LOSS |
| failed requests (%) | 31.68 | 35.13 | +10.9% | +1.207 to +5.7 | LOSS |
| HPA replicas, mean | 9.785 | 12.7 | +29.8% | +2.431 to +3.404 | power given |
| pods started | 4.56 | 9.72 | +113.2% | +4.482 to +5.838 | power given |
| worker nodes in service, mean | 6 | 5.997 | -0.1% | -0.01027 to +0.003445 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.2 | 277.5 | +0.1% | -0.2125 to +0.8465 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.2 | 277.4 | +0.1% | -0.2295 to +0.6502 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.489 | 2.539 | +2.0% | +0.03778 to +0.06254 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.43 | 78.26 | +6.6% | +4.498 to +5.155 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.424 | 0.63 | +48.6% | -0.0007756 to +0.4128 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3823 | 3530 | -7.7% | -836 to +250.5 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5696 | 5443 | -4.4% | -746.3 to +240.6 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 47.88 | 48.14 | +0.5% | -0.8346 to +1.361 | STEADY, inside the noise (up) |
| failed requests (%) | 33.83 | 35.95 | +6.3% | -0.44 to +4.673 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.769 | 11.73 | +20.1% | +1.276 to +2.643 | power given |
| pods started | 4.84 | 8.2 | +69.4% | +2.44 to +4.28 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +1.795e-16 to +1.313e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276 | 275.7 | -0.1% | -0.7192 to +0.06886 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276 | 275.7 | -0.1% | -0.7192 to +0.06886 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.389 | 2.439 | +2.1% | +0.03252 to +0.06742 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.21 | 80.35 | +11.3% | +7.766 to +8.516 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.918 | 1.166 | +27.0% | +0.1751 to +0.3209 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4574 | 3538 | -22.7% | -1547 to -526.6 | GAIN |
| response time (ms), 99th percentile | 6732 | 5851 | -13.1% | -1483 to -280.7 | GAIN |
| time over the response line (% of samples) | 56.18 | 55.54 | -1.1% | -1.879 to +0.5942 | STEADY, inside the noise (cut) |
| failed requests (%) | 37.56 | 42.13 | +12.2% | +1.947 to +7.188 | LOSS |
| HPA replicas, mean | 9.805 | 11.77 | +20.0% | +1.374 to +2.555 | power given |
| pods started | 4.2 | 8.3 | +97.6% | +3.435 to +4.765 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +5.222e-16 to +1.325e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.4 | 277.1 | -0.1% | -0.7481 to +0.03066 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.4 | 277.1 | -0.1% | -0.7481 to +0.03066 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.482 | 2.519 | +1.5% | +0.02357 to +0.05004 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.73 | 81.19 | +7.2% | +5.125 to +5.783 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.596 | 0.41 | -31.2% | -0.2286 to -0.1434 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4238 | 3207 | -24.3% | -1808 to -253 | GAIN |
| response time (ms), 99th percentile | 6092 | 5358 | -12.1% | -1403 to -66.72 | GAIN |
| time over the response line (% of samples) | 48.39 | 48.01 | -0.8% | -1.575 to +0.805 | STEADY, inside the noise (cut) |
| failed requests (%) | 31.96 | 35.13 | +9.9% | +0.4191 to +5.937 | LOSS |
| HPA replicas, mean | 9.76 | 12.07 | +23.7% | +1.677 to +2.941 | power given |
| pods started | 5.16 | 9.88 | +91.5% | +3.782 to +5.658 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +3.441e-16 to +1.397e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276 | 275.7 | -0.1% | -0.7747 to +0.2367 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276 | 275.7 | -0.1% | -0.7747 to +0.2367 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.388 | 2.442 | +2.3% | +0.03226 to +0.07598 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.97 | 79.53 | +9.0% | +5.923 to +7.189 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | power given |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | power given |
| organism behind its window (s) | 0.718 | 0.434 | -39.6% | -0.3339 to -0.2341 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2628 | 3044 | +15.8% | -240.2 to +1072 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4671 | 5224 | +11.8% | -68.77 to +1174 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 49.05 | 49.23 | +0.4% | -1.179 to +1.541 | STEADY, inside the noise (up) |
| failed requests (%) | 37.69 | 37.49 | -0.5% | -3.093 to +2.692 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.769 | 11.98 | +22.7% | +1.534 to +2.892 | power given |
| pods started | 4.88 | 8.46 | +73.4% | +2.67 to +4.49 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +7.564e-16 to +1.837e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.1 | 276.1 | +0.0% | -0.4138 to +0.4218 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.1 | 276.1 | +0.0% | -0.4138 to +0.4218 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.404 | 2.457 | +2.2% | +0.03444 to +0.07244 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.65 | 80.42 | +10.7% | +7.278 to +8.264 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.516 | 1.062 | +105.8% | +0.4921 to +0.5999 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
