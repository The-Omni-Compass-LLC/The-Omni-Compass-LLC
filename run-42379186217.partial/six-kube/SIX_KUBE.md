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
| response time (ms), 95th percentile | 4016 | 3428 | 4175 | 4287 | 4162 | 2866 | 4925 | 3273 | 2929 | 3030 |
| response time (ms), 99th percentile | 6278 | 6079 | 6408 | 6365 | 6270 | 5630 | 7146 | 5829 | 4835 | 4963 |
| time over the response line (% of samples) | 56.91 | 57.56 | 55.73 | 56.65 | 55.49 | 54.93 | 64.56 | 62.9 | 49.91 | 49.36 |
| failed requests (%) | 39.35 | 44.71 | 39.94 | 40.32 | 38.04 | 43.23 | 45.76 | 49.52 | 38.31 | 38.25 |
| HPA replicas, mean | 9.806 | 12.67 | 9.797 | 11.57 | 9.799 | 11.81 | 9.817 | 10.94 | 9.783 | 11.78 |
| pods started | 4.1 | 9.42 | 4.52 | 7.46 | 4.38 | 9.14 | 4.1 | 7.78 | 4.5 | 8.1 |
| worker nodes in service, mean | 6 | 6 | 5.999 | 6 | 6 | 6 | 6 | 5.999 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 277.4 | 277.2 | 277 | 277.3 | 277.1 | 277.2 | 278.8 | 278.3 | 276.1 | 276.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.4 | 277.2 | 276.9 | 277.3 | 277.1 | 277.2 | 278.8 | 278.2 | 276.1 | 276.3 |
| CPU used with Omni's own (cores), mean | 2.491 | 2.535 | 2.483 | 2.53 | 2.475 | 2.519 | 2.571 | 2.595 | 2.415 | 2.464 |
| host CPU busy, the real machine under kind (%) | 73.61 | 78.09 | 74.95 | 82.92 | 75.42 | 80.95 | 78.4 | 84.22 | 72.91 | 80.42 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.444 | 0.52 | 0.884 | 1.158 | 0.566 | 0.452 | 0.768 | 0.454 | 0.5 | 1.03 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4016 | 3428 | -14.6% | -1208 to +31.94 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6278 | 6079 | -3.2% | -857.7 to +458.8 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 56.91 | 57.56 | +1.1% | -0.9348 to +2.239 | STEADY, inside the noise (up) |
| failed requests (%) | 39.35 | 44.71 | +13.6% | +3.796 to +6.919 | LOSS |
| HPA replicas, mean | 9.806 | 12.67 | +29.2% | +2.411 to +3.326 | power given |
| pods started | 4.1 | 9.42 | +129.8% | +4.493 to +6.147 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.818e-16 to +1.976e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.4 | 277.2 | -0.1% | -0.7324 to +0.1698 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.4 | 277.2 | -0.1% | -0.7324 to +0.1698 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.491 | 2.535 | +1.8% | +0.03506 to +0.05344 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.61 | 78.09 | +6.1% | +4.207 to +4.759 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.444 | 0.52 | +17.1% | +0.03358 to +0.1184 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4175 | 4287 | +2.7% | -466.7 to +690.5 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6408 | 6365 | -0.7% | -489.7 to +405.4 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 55.73 | 56.65 | +1.6% | -0.3339 to +2.168 | STEADY, inside the noise (up) |
| failed requests (%) | 39.94 | 40.32 | +0.9% | -2.503 to +3.256 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.797 | 11.57 | +18.1% | +1.144 to +2.401 | power given |
| pods started | 4.52 | 7.46 | +65.0% | +1.968 to +3.912 | power given |
| worker nodes in service, mean | 5.999 | 6 | +0.0% | -0.0008679 to +0.002587 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 277 | 277.3 | +0.1% | -0.1226 to +0.8215 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.9 | 277.3 | +0.1% | -0.09593 to +0.8466 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.483 | 2.53 | +1.9% | +0.03181 to +0.06227 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.95 | 82.92 | +10.6% | +7.627 to +8.33 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.884 | 1.158 | +31.0% | +0.2071 to +0.3409 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4162 | 2866 | -31.1% | -1911 to -680.8 | GAIN |
| response time (ms), 99th percentile | 6270 | 5630 | -10.2% | -1164 to -114.1 | GAIN |
| time over the response line (% of samples) | 55.49 | 54.93 | -1.0% | -1.623 to +0.505 | STEADY, inside the noise (cut) |
| failed requests (%) | 38.04 | 43.23 | +13.7% | +3.02 to +7.368 | LOSS |
| HPA replicas, mean | 9.799 | 11.81 | +20.5% | +1.432 to +2.593 | power given |
| pods started | 4.38 | 9.14 | +108.7% | +3.803 to +5.717 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.155e-16 to +7.906e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.1 | 277.2 | +0.0% | -0.3253 to +0.5295 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.1 | 277.2 | +0.0% | -0.3253 to +0.5295 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.475 | 2.519 | +1.8% | +0.03062 to +0.05813 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.42 | 80.95 | +7.3% | +5.165 to +5.885 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.566 | 0.452 | -20.1% | -0.1634 to -0.06459 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 6 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 1

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4925 | 3273 | -33.5% | -2586 to -717.6 | GAIN |
| response time (ms), 99th percentile | 7146 | 5829 | -18.4% | -2122 to -512.9 | GAIN |
| time over the response line (% of samples) | 64.56 | 62.9 | -2.6% | -2.754 to -0.5737 | GAIN |
| failed requests (%) | 45.76 | 49.52 | +8.2% | +1.489 to +6.018 | LOSS |
| HPA replicas, mean | 9.817 | 10.94 | +11.5% | +0.6323 to +1.62 | power given |
| pods started | 4.1 | 7.78 | +89.8% | +2.935 to +4.425 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002837 to +0.0009519 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 278.8 | 278.3 | -0.2% | -0.9217 to -0.07098 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 278.8 | 278.2 | -0.2% | -0.9707 to -0.07865 | GAIN |
| CPU used with Omni's own (cores), mean | 2.571 | 2.595 | +1.0% | +0.01564 to +0.03325 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 78.4 | 84.22 | +7.4% | +5.582 to +6.064 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | power given |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | power given |
| organism behind its window (s) | 0.768 | 0.454 | -40.9% | -0.3657 to -0.2623 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2929 | 3030 | +3.4% | -578.6 to +780.1 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4835 | 4963 | +2.7% | -571.1 to +828.1 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 49.91 | 49.36 | -1.1% | -1.894 to +0.7866 | STEADY, inside the noise (cut) |
| failed requests (%) | 38.31 | 38.25 | -0.2% | -1.959 to +1.841 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.783 | 11.78 | +20.4% | +1.305 to +2.692 | power given |
| pods started | 4.5 | 8.1 | +80.0% | +2.754 to +4.446 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.983e-16 to +8.668e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.1 | 276.3 | +0.1% | -0.1906 to +0.6491 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.1 | 276.3 | +0.1% | -0.1906 to +0.6491 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.415 | 2.464 | +2.0% | +0.03126 to +0.06745 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.91 | 80.42 | +10.3% | +7.089 to +7.944 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.5 | 1.03 | +106.0% | +0.4881 to +0.5719 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
