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
| response time (ms), 95th percentile | 3649 | 4558 | 3833 | 2952 | 4077 | 4495 | 4939 | 5344 | 4268 | 5169 |
| response time (ms), 99th percentile | 6030 | 6449 | 5425 | 5120 | 5837 | 6728 | 7030 | 7372 | 6319 | 6964 |
| time over the response line (% of samples) | 57.68 | 57.08 | 51.94 | 45.89 | 55.82 | 61.27 | 64.93 | 64.65 | 60.02 | 60.38 |
| failed requests (%) | 46.47 | 45.52 | 39.97 | 39.01 | 42.72 | 48.73 | 50.83 | 53.33 | 47.97 | 48.65 |
| HPA replicas, mean | 9.905 | 13.99 | 9.899 | 13.15 | 9.9 | 14.62 | 9.916 | 14.13 | 9.923 | 14.56 |
| pods started | 5.32 | 10.43 | 5.4 | 11.3 | 5.48 | 11.33 | 5.08 | 10.74 | 5.4 | 10.75 |
| worker nodes in service, mean | 6 | 5.999 | 6 | 5.999 | 6 | 5.999 | 6 | 5.997 | 6 | 5.999 |
| energy, parked workers still on at idle power (Wh, declared model) | 1380 | 1378 | 1375 | 1371 | 1377 | 1382 | 1387 | 1384 | 1381 | 1380 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1380 | 1378 | 1375 | 1370 | 1377 | 1382 | 1387 | 1383 | 1381 | 1380 |
| CPU used with Omni's own (cores), mean | 2.5 | 2.518 | 2.425 | 2.413 | 2.46 | 2.566 | 2.589 | 2.592 | 2.512 | 2.537 |
| host CPU busy, the real machine under kind (%) | 73.34 | 78 | 73.02 | 79.49 | 74.75 | 82.38 | 79.03 | 84.57 | 75.25 | 82.89 |
| organism work | 1.044e+13 | 1.044e+13 | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 3.317e+13 | 3.317e+13 | 1.082e+13 | 1.082e+13 |
| organism energy (J) | 6.905e+12 | 6.909e+12 | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 5.512e+15 | 5.512e+15 | 2.854e+13 | 2.855e+13 |
| organism time over the line (% of steps) | 2.335 | 2.205 | 1.943 | 1.874 | 4.602 | 4.511 | 1.469 | 1.382 | 2.451 | 2.367 |
| organism work per energy | 1.511 | 1.511 | 1.375 | 1.374 | 1.116 | 1.115 | 0.006018 | 0.006018 | 0.3789 | 0.3788 |
| organism behind its window (s) | 2.176 | 2.93 | 4.412 | 5.67 | 3.116 | 4.1 | 3.78 | 4.77 | 3.976 | 5.242 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

23 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3904 | 4558 | +16.7% | -818.7 to +2125 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6414 | 6449 | +0.5% | -1817 to +1887 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 60.01 | 57.08 | -4.9% | -20.35 to +14.48 | STEADY, inside the noise (cut) |
| failed requests (%) | 48.26 | 45.52 | -5.7% | -17.12 to +11.65 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.908 | 13.99 | +41.2% | +2.838 to +5.332 | power given |
| pods started | 5.217 | 10.43 | +100.0% | +4.469 to +5.966 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001461 to +0.0003755 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1382 | 1378 | -0.3% | -18.3 to +11.24 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1382 | 1378 | -0.3% | -18.37 to +11.14 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.523 | 2.518 | -0.2% | -0.2026 to +0.1932 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.06 | 78 | +5.3% | -1.986 to +9.858 | shown, not judged |
| organism work | 1.044e+13 | 1.044e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 6.905e+12 | 6.909e+12 | +0.1% | +4.063e+09 to +4.063e+09 | power given |
| organism time over the line (% of steps) | 2.335 | 2.205 | -5.6% | -0.13 to -0.13 | GAIN |
| organism work per energy | 1.511 | 1.511 | -0.1% | -0.0008889 to -0.0008889 | power given |
| organism behind its window (s) | 2.191 | 2.93 | +33.7% | +0.5153 to +0.963 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

23 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3868 | 2952 | -23.7% | -2989 to +1156 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5482 | 5120 | -6.6% | -3156 to +2433 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 53.03 | 45.89 | -13.5% | -31.12 to +16.84 | STEADY, inside the noise (cut) |
| failed requests (%) | 40.87 | 39.01 | -4.5% | -21.35 to +17.64 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.901 | 13.15 | +32.8% | +2.051 to +4.441 | power given |
| pods started | 5.348 | 11.3 | +111.4% | +3.99 to +7.923 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001768 to +0.000466 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1376 | 1371 | -0.4% | -23.95 to +12.73 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1376 | 1370 | -0.4% | -24.05 to +12.63 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.442 | 2.413 | -1.2% | -0.274 to +0.2163 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.46 | 79.49 | +8.2% | -1.895 to +13.96 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.417 | 5.67 | +28.3% | +0.9021 to +1.602 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

24 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4193 | 4495 | +7.2% | -1175 to +1779 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5940 | 6728 | +13.3% | -1250 to +2825 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 55.5 | 61.27 | +10.4% | -12.74 to +24.29 | STEADY, inside the noise (up) |
| failed requests (%) | 42.3 | 48.73 | +15.2% | -9.991 to +22.85 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.9 | 14.62 | +47.7% | +3.837 to +5.612 | power given |
| pods started | 5.458 | 11.33 | +107.6% | +4.486 to +7.264 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003051 to +0.0008886 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1377 | 1382 | +0.4% | -9.583 to +19.64 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1377 | 1382 | +0.4% | -9.737 to +19.47 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.451 | 2.566 | +4.7% | -0.0785 to +0.3094 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.55 | 82.38 | +10.5% | +1.77 to +13.9 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.1 | 4.1 | +32.3% | +0.7566 to +1.243 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

23 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 5000 | 5344 | +6.9% | -1580 to +2267 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 7194 | 7372 | +2.5% | -1952 to +2307 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 66.98 | 64.65 | -3.5% | -19.45 to +14.79 | STEADY, inside the noise (cut) |
| failed requests (%) | 52.52 | 53.33 | +1.5% | -14.96 to +16.57 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.918 | 14.13 | +42.5% | +3.087 to +5.338 | power given |
| pods started | 5 | 10.74 | +114.8% | +4.797 to +6.681 | power given |
| worker nodes in service, mean | 6 | 5.997 | -0.0% | -0.006451 to +0.0008068 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1389 | 1384 | -0.4% | -15.05 to +5.233 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1389 | 1383 | -0.4% | -15.49 to +4.826 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.607 | 2.592 | -0.6% | -0.1536 to +0.1242 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 79.61 | 84.57 | +6.2% | +0.3004 to +9.622 | shown, not judged |
| organism work | 3.317e+13 | 3.317e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.512e+15 | 5.512e+15 | +0.0% | +4.35e+09 to +4.35e+09 | power given |
| organism time over the line (% of steps) | 1.469 | 1.382 | -5.9% | -0.0869 to -0.0869 | GAIN |
| organism work per energy | 0.006018 | 0.006018 | -0.0% | -4.749e-09 to -4.749e-09 | power given |
| organism behind its window (s) | 3.796 | 4.77 | +25.7% | +0.7826 to +1.165 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

24 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4433 | 5169 | +16.6% | -1015 to +2487 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6563 | 6964 | +6.1% | -1600 to +2403 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 62.49 | 60.38 | -3.4% | -20.37 to +16.15 | STEADY, inside the noise (cut) |
| failed requests (%) | 49.97 | 48.65 | -2.6% | -17.19 to +14.55 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.926 | 14.56 | +46.7% | +3.601 to +5.668 | power given |
| pods started | 5.333 | 10.75 | +101.6% | +4.511 to +6.323 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003066 to +0.001068 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1383 | 1380 | -0.2% | -15.16 to +8.815 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1383 | 1380 | -0.2% | -15.32 to +8.674 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.539 | 2.537 | -0.1% | -0.1612 to +0.1582 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.07 | 82.89 | +9.0% | +1.593 to +12.05 | shown, not judged |
| organism work | 1.082e+13 | 1.082e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.854e+13 | 2.855e+13 | +0.0% | +4.369e+09 to +4.369e+09 | power given |
| organism time over the line (% of steps) | 2.451 | 2.367 | -3.4% | -0.08396 to -0.08396 | GAIN |
| organism work per energy | 0.3789 | 0.3788 | -0.0% | -5.798e-05 to -5.798e-05 | power given |
| organism behind its window (s) | 3.988 | 5.242 | +31.5% | +1.055 to +1.453 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
