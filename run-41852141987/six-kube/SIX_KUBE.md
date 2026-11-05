# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 500 copies: native | The spine, the muscles every stack runs on, 500 copies: omni | Compute / AI / Cloud, 500 copies: native | Compute / AI / Cloud, 500 copies: omni | Physics / Robotics / Autonomous, 500 copies: native | Physics / Robotics / Autonomous, 500 copies: omni | Energy / Facility / Industrial, 500 copies: native | Energy / Facility / Industrial, 500 copies: omni | Distribution / Specialized, 500 copies: native | Distribution / Specialized, 500 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 5142 | 4485 | 2907 | 3015 | 5071 | 6383 | 3706 | 6357 | 4673 | 3807 |
| response time (ms), 99th percentile | 7464 | 6484 | 4398 | 5482 | 7134 | 8568 | 4862 | 8766 | 6762 | 5855 |
| time over the response line (% of samples) | 69.01 | 58.57 | 45.54 | 49.11 | 63.78 | 70.34 | 39.37 | 74.85 | 63.07 | 52.75 |
| failed requests (%) | 52.41 | 47.03 | 33.73 | 42.33 | 48.41 | 53.78 | 30.44 | 58.47 | 47.71 | 43.58 |
| HPA replicas, mean | 9.92 | 14.36 | 9.892 | 13.44 | 9.914 | 15.24 | 9.887 | 15.57 | 9.931 | 13 |
| pods started | 4.9 | 9.556 | 5.7 | 13.78 | 5.1 | 11 | 5.7 | 11.12 | 5.3 | 9.8 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 5.997 |
| energy, parked workers still on at idle power (Wh, declared model) | 1392 | 1376 | 1375 | 1374 | 1385 | 1385 | 1364 | 1391 | 1384 | 1374 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1392 | 1376 | 1375 | 1374 | 1385 | 1385 | 1364 | 1391 | 1384 | 1374 |
| CPU used with Omni's own (cores), mean | 2.652 | 2.495 | 2.429 | 2.455 | 2.562 | 2.605 | 2.274 | 2.681 | 2.546 | 2.467 |
| host CPU busy, the real machine under kind (%) | 77.99 | 78.03 | 72.5 | 80.63 | 78.48 | 84.75 | 69.42 | 87.74 | 76.51 | 80.39 |
| organism work | 1.044e+13 | 1.044e+13 | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 3.317e+13 | 3.317e+13 | 1.082e+13 | 1.082e+13 |
| organism energy (J) | 6.905e+12 | 6.909e+12 | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 5.512e+15 | 5.512e+15 | 2.854e+13 | 2.855e+13 |
| organism time over the line (% of steps) | 2.335 | 2.205 | 1.943 | 1.874 | 4.602 | 4.511 | 1.469 | 1.382 | 2.451 | 2.367 |
| organism work per energy | 1.511 | 1.511 | 1.375 | 1.374 | 1.116 | 1.115 | 0.006018 | 0.006018 | 0.3789 | 0.3788 |
| organism behind its window (s) | 2.16 | 2.922 | 4.24 | 5.8 | 3.29 | 4.21 | 3.62 | 4.738 | 3.99 | 5.42 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

9 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4867 | 4485 | -7.8% | -3260 to +2496 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 7259 | 6484 | -10.7% | -4011 to +2461 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 68.16 | 58.57 | -14.1% | -31.13 to +11.96 | STEADY, inside the noise (cut) |
| failed requests (%) | 51.33 | 47.03 | -8.4% | -20.6 to +12.01 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.919 | 14.36 | +44.8% | +2.276 to +6.609 | power given |
| pods started | 5 | 9.556 | +91.1% | +2.875 to +6.236 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.596e-16 to +1.839e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 1392 | 1376 | -1.1% | -34.62 to +3.803 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1392 | 1376 | -1.1% | -34.62 to +3.803 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.652 | 2.495 | -5.9% | -0.4151 to +0.1004 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.89 | 78.03 | +0.2% | -8.158 to +8.445 | shown, not judged |
| organism work | 1.044e+13 | 1.044e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 6.905e+12 | 6.909e+12 | +0.1% | +4.063e+09 to +4.063e+09 | power given |
| organism time over the line (% of steps) | 2.335 | 2.205 | -5.6% | -0.13 to -0.13 | GAIN |
| organism work per energy | 1.511 | 1.511 | -0.1% | -0.0008889 to -0.0008889 | power given |
| organism behind its window (s) | 2.156 | 2.922 | +35.6% | +0.4294 to +1.104 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

9 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3028 | 3015 | -0.4% | -4060 to +4033 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4537 | 5482 | +20.8% | -4318 to +6209 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 43.48 | 49.11 | +12.9% | -40.47 to +51.73 | STEADY, inside the noise (up) |
| failed requests (%) | 31.81 | 42.33 | +33.1% | -27.82 to +48.85 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.889 | 13.44 | +35.9% | +1.266 to +5.837 | power given |
| pods started | 5.778 | 13.78 | +138.5% | +2.93 to +13.07 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.297e-16 to +1.511e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 1373 | 1374 | +0.1% | -33.92 to +36.49 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1373 | 1374 | +0.1% | -33.92 to +36.49 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.403 | 2.455 | +2.2% | -0.4272 to +0.5327 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.77 | 80.63 | +12.3% | -6.483 to +24.19 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.256 | 5.8 | +36.3% | +1.027 to +2.062 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 5071 | 6383 | +25.9% | -1495 to +4119 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 7134 | 8568 | +20.1% | -1898 to +4767 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 63.78 | 70.34 | +10.3% | -23.53 to +36.63 | STEADY, inside the noise (up) |
| failed requests (%) | 48.41 | 53.78 | +11.1% | -21.24 to +31.99 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.914 | 15.24 | +53.7% | +4.387 to +6.261 | power given |
| pods started | 5.1 | 11 | +115.7% | +4.452 to +7.348 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.779e-16 to +1.599e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 1385 | 1385 | -0.0% | -17.28 to +16.65 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1385 | 1385 | -0.0% | -17.28 to +16.65 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.562 | 2.605 | +1.7% | -0.1883 to +0.2733 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 78.48 | 84.75 | +8.0% | -1.903 to +14.44 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.29 | 4.21 | +28.0% | +0.6681 to +1.172 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (time over the response line (% of samples)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 3

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3716 | 6357 | +71.1% | -791.4 to +6075 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4819 | 8766 | +81.9% | -89.78 to +7984 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 39.54 | 74.85 | +89.3% | +0.7717 to +69.84 | LOSS |
| failed requests (%) | 30.69 | 58.47 | +90.5% | -1.173 to +56.74 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.889 | 15.57 | +57.5% | +5.28 to +6.087 | power given |
| pods started | 5.625 | 11.12 | +97.8% | +4.317 to +6.683 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.108e-15 to +1.331e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 1363 | 1391 | +2.0% | +2.047 to +53.3 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1363 | 1391 | +2.0% | +2.047 to +53.3 | power given |
| CPU used with Omni's own (cores), mean | 2.27 | 2.681 | +18.1% | +0.06218 to +0.7609 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.38 | 87.74 | +26.5% | +7.073 to +29.64 | shown, not judged |
| organism work | 3.317e+13 | 3.317e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.512e+15 | 5.512e+15 | +0.0% | +4.35e+09 to +4.35e+09 | power given |
| organism time over the line (% of steps) | 1.469 | 1.382 | -5.9% | -0.0869 to -0.0869 | GAIN |
| organism work per energy | 0.006018 | 0.006018 | -0.0% | -4.749e-09 to -4.749e-09 | power given |
| organism behind its window (s) | 3.587 | 4.738 | +32.1% | +0.7527 to +1.547 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4673 | 3807 | -18.5% | -3810 to +2078 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6762 | 5855 | -13.4% | -5049 to +3236 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 63.07 | 52.75 | -16.4% | -48.63 to +28 | STEADY, inside the noise (cut) |
| failed requests (%) | 47.71 | 43.58 | -8.7% | -38.27 to +30.01 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.931 | 13 | +30.9% | +0.9963 to +5.144 | power given |
| pods started | 5.3 | 9.8 | +84.9% | +2.839 to +6.161 | power given |
| worker nodes in service, mean | 6 | 5.997 | -0.1% | -0.01006 to +0.003891 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1384 | 1374 | -0.7% | -36.12 to +16.76 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1384 | 1374 | -0.7% | -36.54 to +16.25 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.546 | 2.467 | -3.1% | -0.442 to +0.2844 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.51 | 80.39 | +5.1% | -8.195 to +15.94 | shown, not judged |
| organism work | 1.082e+13 | 1.082e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.854e+13 | 2.855e+13 | +0.0% | +4.369e+09 to +4.369e+09 | power given |
| organism time over the line (% of steps) | 2.451 | 2.367 | -3.4% | -0.08396 to -0.08396 | GAIN |
| organism work per energy | 0.3789 | 0.3788 | -0.0% | -5.798e-05 to -5.798e-05 | power given |
| organism behind its window (s) | 3.99 | 5.42 | +35.8% | +0.9011 to +1.959 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
