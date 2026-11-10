# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 500 copies: native | The spine, the muscles every stack runs on, 500 copies: omni | Compute / AI / Cloud, 500 copies: native | Compute / AI / Cloud, 500 copies: omni | Physics / Robotics / Autonomous, 500 copies: native | Physics / Robotics / Autonomous, 500 copies: omni | Energy / Facility / Industrial, 500 copies: native | Energy / Facility / Industrial, 500 copies: omni | Distribution / Specialized, 500 copies: native | Distribution / Specialized, 500 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2772 | 4127 | 5045 | 3414 | 4700 | 4459 | 4070 | 4563 | 3853 | 4159 |
| response time (ms), 99th percentile | 4390 | 6465 | 6927 | 6920 | 6709 | 6227 | 5846 | 6763 | 6085 | 6496 |
| time over the response line (% of samples) | 46.11 | 60.05 | 63.42 | 63.68 | 59.89 | 55.82 | 61.46 | 62.63 | 57.27 | 63.31 |
| failed requests (%) | 34.92 | 43.71 | 47.61 | 54 | 46.07 | 44.11 | 49.07 | 50.6 | 44.51 | 51.42 |
| HPA replicas, mean | 9.893 | 14.9 | 9.912 | 13.6 | 9.906 | 14.34 | 9.907 | 14.65 | 9.921 | 14.32 |
| pods started | 5.52 | 10.83 | 5.208 | 10.29 | 5.32 | 10.6 | 5.44 | 10.4 | 5.48 | 10.38 |
| worker nodes in service, mean | 6 | 5.999 | 6 | 5.999 | 6 | 5.998 | 6 | 5.998 | 6 | 5.998 |
| energy, parked workers still on at idle power (Wh, declared model) | 1374 | 1386 | 1386 | 1385 | 1380 | 1375 | 1383 | 1381 | 1382 | 1383 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1374 | 1386 | 1386 | 1385 | 1380 | 1375 | 1383 | 1380 | 1382 | 1383 |
| CPU used with Omni's own (cores), mean | 2.411 | 2.622 | 2.577 | 2.61 | 2.494 | 2.482 | 2.538 | 2.553 | 2.514 | 2.586 |
| host CPU busy, the real machine under kind (%) | 70.46 | 80.44 | 77.99 | 85.7 | 76.05 | 80.26 | 77.33 | 83.29 | 75.01 | 84.22 |
| organism work | 1.044e+13 | 1.044e+13 | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 3.317e+13 | 3.317e+13 | 1.082e+13 | 1.082e+13 |
| organism energy (J) | 6.905e+12 | 6.909e+12 | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 5.512e+15 | 5.512e+15 | 2.854e+13 | 2.855e+13 |
| organism time over the line (% of steps) | 2.335 | 2.205 | 1.943 | 1.874 | 4.602 | 4.511 | 1.469 | 1.382 | 2.451 | 2.367 |
| organism work per energy | 1.511 | 1.511 | 1.375 | 1.374 | 1.116 | 1.115 | 0.006018 | 0.006018 | 0.3789 | 0.3788 |
| organism behind its window (s) | 2.112 | 3.071 | 4.617 | 5.958 | 3.252 | 4.035 | 3.748 | 4.776 | 3.992 | 5.383 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

24 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2876 | 4127 | +43.5% | -528.6 to +3029 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4557 | 6465 | +41.9% | -376.5 to +4193 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 48.01 | 60.05 | +25.1% | -6.964 to +31.03 | STEADY, inside the noise (up) |
| failed requests (%) | 36.38 | 43.71 | +20.2% | -11.02 to +25.68 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.895 | 14.9 | +50.6% | +4.225 to +5.793 | power given |
| pods started | 5.458 | 10.83 | +98.5% | +4.56 to +6.19 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001785 to +0.0003871 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1376 | 1386 | +0.8% | -5.387 to +26.58 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1376 | 1386 | +0.8% | -5.507 to +26.49 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.44 | 2.622 | +7.5% | -0.03156 to +0.3958 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.32 | 80.44 | +12.8% | +2.61 to +15.63 | shown, not judged |
| organism work | 1.044e+13 | 1.044e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 6.905e+12 | 6.909e+12 | +0.1% | +4.063e+09 to +4.063e+09 | power given |
| organism time over the line (% of steps) | 2.335 | 2.205 | -5.6% | -0.13 to -0.13 | GAIN |
| organism work per energy | 1.511 | 1.511 | -0.1% | -0.0008889 to -0.0008889 | power given |
| organism behind its window (s) | 2.133 | 3.071 | +43.9% | +0.7124 to +1.163 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 500 copies: GAIN on 2 (response time (ms), 95th percentile; organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

23 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 5018 | 3354 | -33.2% | -2978 to -350.8 | GAIN |
| response time (ms), 99th percentile | 6825 | 6904 | +1.2% | -1312 to +1469 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 62.77 | 63.66 | +1.4% | -9.275 to +11.06 | STEADY, inside the noise (up) |
| failed requests (%) | 46.91 | 54.65 | +16.5% | -2.936 to +18.41 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.912 | 13.54 | +36.6% | +2.796 to +4.467 | power given |
| pods started | 5.217 | 10.3 | +97.5% | +4.362 to +5.812 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001909 to +0.0004246 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1386 | 1385 | -0.1% | -7.135 to +5.17 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1386 | 1385 | -0.1% | -7.252 to +5.064 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.574 | 2.606 | +1.3% | -0.05042 to +0.1154 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.87 | 85.68 | +10.0% | +4.968 to +10.66 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.613 | 5.97 | +29.4% | +1.117 to +1.596 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

20 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4705 | 4459 | -5.2% | -2271 to +1780 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6812 | 6227 | -8.6% | -3131 to +1962 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 61.28 | 55.82 | -8.9% | -27.47 to +16.56 | STEADY, inside the noise (cut) |
| failed requests (%) | 48.55 | 44.11 | -9.1% | -22.17 to +13.29 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.906 | 14.34 | +44.8% | +3.267 to +5.605 | power given |
| pods started | 5.35 | 10.6 | +98.1% | +4.135 to +6.365 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.003715 to +0.0002732 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1380 | 1375 | -0.4% | -22.07 to +11.39 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1380 | 1375 | -0.4% | -22.3 to +11.1 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.497 | 2.482 | -0.6% | -0.2389 to +0.2091 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.2 | 80.26 | +5.3% | -3.275 to +11.4 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.185 | 4.035 | +26.7% | +0.6471 to +1.053 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4070 | 4563 | +12.1% | -942.2 to +1929 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5846 | 6763 | +15.7% | -911 to +2746 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 61.46 | 62.63 | +1.9% | -14.38 to +16.72 | STEADY, inside the noise (up) |
| failed requests (%) | 49.07 | 50.6 | +3.1% | -11.89 to +14.94 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.907 | 14.65 | +47.9% | +3.852 to +5.629 | power given |
| pods started | 5.44 | 10.4 | +91.2% | +4.041 to +5.879 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.005774 to +0.001096 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1383 | 1381 | -0.2% | -14.93 to +9.732 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1383 | 1380 | -0.2% | -15.31 to +9.41 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.538 | 2.553 | +0.6% | -0.1488 to +0.1773 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.33 | 83.29 | +7.7% | +0.5911 to +11.32 | shown, not judged |
| organism work | 3.317e+13 | 3.317e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.512e+15 | 5.512e+15 | +0.0% | +4.35e+09 to +4.35e+09 | power given |
| organism time over the line (% of steps) | 1.469 | 1.382 | -5.9% | -0.0869 to -0.0869 | GAIN |
| organism work per energy | 0.006018 | 0.006018 | -0.0% | -4.749e-09 to -4.749e-09 | power given |
| organism behind its window (s) | 3.748 | 4.776 | +27.4% | +0.7968 to +1.259 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

24 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3969 | 4159 | +4.8% | -1144 to +1524 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6180 | 6496 | +5.1% | -1297 to +1930 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 57.04 | 63.31 | +11.0% | -6.725 to +19.25 | STEADY, inside the noise (up) |
| failed requests (%) | 44.18 | 51.42 | +16.4% | -4.743 to +19.22 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.921 | 14.32 | +44.4% | +3.331 to +5.476 | power given |
| pods started | 5.458 | 10.38 | +90.1% | +4.037 to +5.797 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.005189 to +0.000553 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1381 | 1383 | +0.2% | -7.465 to +11.63 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1381 | 1383 | +0.1% | -7.705 to +11.17 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.506 | 2.586 | +3.2% | -0.05527 to +0.2145 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.86 | 84.22 | +12.5% | +5.122 to +13.6 | shown, not judged |
| organism work | 1.082e+13 | 1.082e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.854e+13 | 2.855e+13 | +0.0% | +4.369e+09 to +4.369e+09 | power given |
| organism time over the line (% of steps) | 2.451 | 2.367 | -3.4% | -0.08396 to -0.08396 | GAIN |
| organism work per energy | 0.3789 | 0.3788 | -0.0% | -5.798e-05 to -5.798e-05 | power given |
| organism behind its window (s) | 3.996 | 5.383 | +34.7% | +1.141 to +1.634 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
