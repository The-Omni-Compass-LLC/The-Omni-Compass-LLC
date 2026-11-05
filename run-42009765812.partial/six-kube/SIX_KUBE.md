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
| response time (ms), 95th percentile | 4265 | 4882 | 3392 | 3926 | 3918 | 5525 | 3664 | 4889 | 3363 | 4454 |
| response time (ms), 99th percentile | 6259 | 7008 | 5170 | 6828 | 5647 | 7864 | 5313 | 6898 | 5258 | 6355 |
| time over the response line (% of samples) | 57.09 | 62.04 | 52.1 | 68.06 | 49.96 | 70.64 | 47.62 | 63.25 | 56.11 | 54.77 |
| failed requests (%) | 44.99 | 46.94 | 37.09 | 58.22 | 38.79 | 55.68 | 36.37 | 52.14 | 44.1 | 42.7 |
| HPA replicas, mean | 9.905 | 14.91 | 9.899 | 14.62 | 9.895 | 15.39 | 9.891 | 14.78 | 9.922 | 13.95 |
| pods started | 5.25 | 11.08 | 5.56 | 10.74 | 5.56 | 10.91 | 5.64 | 12.04 | 5.4 | 12.65 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 5.999 | 6 | 5.997 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 1380 | 1383 | 1380 | 1388 | 1373 | 1387 | 1371 | 1381 | 1382 | 1377 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1380 | 1383 | 1380 | 1388 | 1373 | 1386 | 1371 | 1381 | 1382 | 1377 |
| CPU used with Omni's own (cores), mean | 2.502 | 2.591 | 2.5 | 2.645 | 2.396 | 2.648 | 2.368 | 2.571 | 2.521 | 2.505 |
| host CPU busy, the real machine under kind (%) | 73.87 | 80.25 | 74.77 | 86.93 | 73.12 | 85.28 | 72.2 | 84.02 | 74.94 | 81.52 |
| organism work | 1.044e+13 | 1.044e+13 | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 3.317e+13 | 3.317e+13 | 1.082e+13 | 1.082e+13 |
| organism energy (J) | 6.905e+12 | 6.909e+12 | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 5.512e+15 | 5.512e+15 | 2.854e+13 | 2.855e+13 |
| organism time over the line (% of steps) | 2.335 | 2.205 | 1.943 | 1.874 | 4.602 | 4.511 | 1.469 | 1.382 | 2.451 | 2.367 |
| organism work per energy | 1.511 | 1.511 | 1.375 | 1.374 | 1.116 | 1.115 | 0.006018 | 0.006018 | 0.3789 | 0.3788 |
| organism behind its window (s) | 2.2 | 2.938 | 4.428 | 5.865 | 3.16 | 4.243 | 3.684 | 4.9 | 4.056 | 5.309 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

23 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4418 | 5088 | +15.2% | -977.7 to +2317 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6474 | 7301 | +12.8% | -1257 to +2911 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 58.99 | 64.74 | +9.8% | -11.91 to +23.41 | STEADY, inside the noise (up) |
| failed requests (%) | 46.95 | 48.98 | +4.3% | -14.25 to +18.31 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.906 | 15.22 | +53.7% | +4.598 to +6.039 | power given |
| pods started | 5.217 | 11.04 | +111.7% | +5.048 to +6.605 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.000946 to +0.0003305 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1381 | 1385 | +0.4% | -8.592 to +18.37 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1381 | 1385 | +0.4% | -8.642 to +18.33 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.504 | 2.621 | +4.7% | -0.06369 to +0.2975 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.03 | 81.19 | +9.7% | +1.564 to +12.76 | shown, not judged |
| organism work | 1.044e+13 | 1.044e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 6.905e+12 | 6.909e+12 | +0.1% | +4.063e+09 to +4.063e+09 | power given |
| organism time over the line (% of steps) | 2.335 | 2.205 | -5.6% | -0.13 to -0.13 | GAIN |
| organism work per energy | 1.511 | 1.511 | -0.1% | -0.0008889 to -0.0008889 | power given |
| organism behind its window (s) | 2.2 | 2.952 | +34.2% | +0.6059 to +0.8985 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

23 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3119 | 3926 | +25.9% | -882.6 to +2497 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4824 | 6828 | +41.5% | -90.29 to +4098 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 49.93 | 68.06 | +36.3% | -0.2966 to +36.55 | STEADY, inside the noise (up) |
| failed requests (%) | 35.16 | 58.22 | +65.6% | +5.448 to +40.68 | LOSS |
| HPA replicas, mean | 9.896 | 14.62 | +47.8% | +4.058 to +5.399 | power given |
| pods started | 5.652 | 10.74 | +90.0% | +4.362 to +5.812 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.0003152 to +0.0001101 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1380 | 1388 | +0.6% | -4.091 to +20.3 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1380 | 1388 | +0.6% | -4.109 to +20.29 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.488 | 2.645 | +6.3% | -0.007151 to +0.3221 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.26 | 86.93 | +17.1% | +7.378 to +17.96 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.413 | 5.865 | +32.9% | +1.257 to +1.647 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 2 (worker nodes in service, mean; organism time over the line (% of steps)), LOSS on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 0

23 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3943 | 5525 | +40.1% | +350.9 to +2814 | LOSS |
| response time (ms), 99th percentile | 5697 | 7864 | +38.0% | +539.9 to +3795 | LOSS |
| time over the response line (% of samples) | 50.88 | 70.64 | +38.8% | +4.747 to +34.77 | LOSS |
| failed requests (%) | 39.41 | 55.68 | +41.3% | +2.506 to +30.04 | LOSS |
| HPA replicas, mean | 9.897 | 15.39 | +55.5% | +5.13 to +5.855 | power given |
| pods started | 5.522 | 10.91 | +97.6% | +4.926 to +5.857 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002849 to -5.887e-05 | GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 1374 | 1387 | +0.9% | +0.5223 to +25.15 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1374 | 1386 | +0.9% | +0.3038 to +24.93 | power given |
| CPU used with Omni's own (cores), mean | 2.407 | 2.648 | +10.0% | +0.08648 to +0.3957 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.44 | 85.28 | +16.1% | +7.115 to +16.57 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.165 | 4.243 | +34.1% | +0.8582 to +1.298 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 500 copies: GAIN on 2 (worker nodes in service, mean; organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

24 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3498 | 4889 | +39.8% | -538.8 to +3321 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5145 | 6898 | +34.1% | -623.6 to +4131 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 46.34 | 63.25 | +36.5% | -4.8 to +38.61 | STEADY, inside the noise (up) |
| failed requests (%) | 35.38 | 52.14 | +47.4% | -0.08783 to +33.62 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.889 | 14.78 | +49.5% | +4.105 to +5.686 | power given |
| pods started | 5.708 | 12.04 | +110.9% | +5.029 to +7.638 | power given |
| worker nodes in service, mean | 6 | 5.997 | -0.0% | -0.00559 to -6.321e-06 | GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 1370 | 1381 | +0.8% | -6.107 to +29.2 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1370 | 1381 | +0.8% | -6.521 to +28.77 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.356 | 2.571 | +9.1% | -0.0195 to +0.4485 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.78 | 84.02 | +17.1% | +4.873 to +19.61 | shown, not judged |
| organism work | 3.317e+13 | 3.317e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.512e+15 | 5.512e+15 | +0.0% | +4.35e+09 to +4.35e+09 | power given |
| organism time over the line (% of steps) | 1.469 | 1.382 | -5.9% | -0.0869 to -0.0869 | GAIN |
| organism work per energy | 0.006018 | 0.006018 | -0.0% | -4.749e-09 to -4.749e-09 | power given |
| organism behind its window (s) | 3.654 | 4.9 | +34.1% | +0.9621 to +1.53 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

23 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3339 | 4454 | +33.4% | -900.2 to +3132 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5216 | 6355 | +21.8% | -1367 to +3644 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 54.94 | 54.77 | -0.3% | -21.18 to +20.84 | STEADY, inside the noise (cut) |
| failed requests (%) | 43.22 | 42.7 | -1.2% | -18.76 to +17.72 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.921 | 13.95 | +40.6% | +2.914 to +5.15 | power given |
| pods started | 5.435 | 12.65 | +132.8% | +4.157 to +10.28 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.0009112 to +0.0001874 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1381 | 1377 | -0.3% | -19.06 to +11.03 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1381 | 1377 | -0.3% | -19.12 to +10.98 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.509 | 2.505 | -0.2% | -0.2069 to +0.1991 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.57 | 81.52 | +9.3% | +0.4477 to +13.45 | shown, not judged |
| organism work | 1.082e+13 | 1.082e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.854e+13 | 2.855e+13 | +0.0% | +4.369e+09 to +4.369e+09 | power given |
| organism time over the line (% of steps) | 2.451 | 2.367 | -3.4% | -0.08396 to -0.08396 | GAIN |
| organism work per energy | 0.3789 | 0.3788 | -0.0% | -5.798e-05 to -5.798e-05 | power given |
| organism behind its window (s) | 4.061 | 5.309 | +30.7% | +1.007 to +1.488 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
