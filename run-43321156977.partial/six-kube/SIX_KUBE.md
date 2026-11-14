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
| response time (ms), 95th percentile | 3950 | 3956 | 2979 | 2784 | 3375 | 3460 | 3593 | 3214 | 3033 | 3593 |
| response time (ms), 99th percentile | 6056 | 5758 | 4626 | 5209 | 5146 | 5420 | 5286 | 5021 | 4655 | 5377 |
| time over the response line (% of samples) | 58.12 | 55.97 | 52.98 | 45.62 | 54.7 | 48.64 | 55.73 | 45.36 | 48.03 | 49.42 |
| failed requests (%) | 46.44 | 43.53 | 36.04 | 33.51 | 39.09 | 37.11 | 42.33 | 36.01 | 37.22 | 38.87 |
| HPA replicas, mean | 9.908 | 14.5 | 9.899 | 13.73 | 9.902 | 13.59 | 9.903 | 12.98 | 9.911 | 12.95 |
| pods started | 5.28 | 10.27 | 5.56 | 11.76 | 5.44 | 10.6 | 5.32 | 13.65 | 5.56 | 10 |
| worker nodes in service, mean | 6 | 6 | 6 | 5.998 | 6 | 5.997 | 6 | 5.999 | 6 | 5.999 |
| energy, parked workers still on at idle power (Wh, declared model) | 1380 | 1379 | 1382 | 1376 | 1383 | 1374 | 1380 | 1371 | 1375 | 1372 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1380 | 1379 | 1382 | 1376 | 1383 | 1373 | 1380 | 1371 | 1375 | 1371 |
| CPU used with Omni's own (cores), mean | 2.49 | 2.529 | 2.512 | 2.483 | 2.537 | 2.455 | 2.484 | 2.414 | 2.421 | 2.423 |
| host CPU busy, the real machine under kind (%) | 73.89 | 79.2 | 75.95 | 82.18 | 77.19 | 79.87 | 76.69 | 80.23 | 73.08 | 80.25 |
| organism work | 1.044e+13 | 1.044e+13 | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 3.317e+13 | 3.317e+13 | 1.082e+13 | 1.082e+13 |
| organism energy (J) | 6.905e+12 | 6.909e+12 | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 5.512e+15 | 5.512e+15 | 2.854e+13 | 2.855e+13 |
| organism time over the line (% of steps) | 2.335 | 2.205 | 1.943 | 1.874 | 4.602 | 4.511 | 1.469 | 1.382 | 2.451 | 2.367 |
| organism work per energy | 1.511 | 1.511 | 1.375 | 1.374 | 1.116 | 1.115 | 0.006018 | 0.006018 | 0.3789 | 0.3788 |
| organism behind its window (s) | 2.256 | 3.168 | 4.636 | 6.072 | 3.34 | 4.264 | 3.856 | 4.896 | 4.096 | 5.625 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

22 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3893 | 3956 | +1.6% | -1736 to +1861 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5837 | 5758 | -1.4% | -2504 to +2346 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 56.29 | 55.97 | -0.6% | -20.86 to +20.21 | STEADY, inside the noise (cut) |
| failed requests (%) | 44.87 | 43.53 | -3.0% | -17.83 to +15.14 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.905 | 14.5 | +46.4% | +3.563 to +5.628 | power given |
| pods started | 5.364 | 10.27 | +91.5% | +4.101 to +5.718 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.0008503 to +0.0007497 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1378 | 1379 | +0.1% | -15.24 to +17.86 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1378 | 1379 | +0.1% | -15.24 to +17.85 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.464 | 2.529 | +2.6% | -0.1583 to +0.2877 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.17 | 79.2 | +8.2% | -0.8554 to +12.93 | shown, not judged |
| organism work | 1.044e+13 | 1.044e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 6.905e+12 | 6.909e+12 | +0.1% | +4.063e+09 to +4.063e+09 | power given |
| organism time over the line (% of steps) | 2.335 | 2.205 | -5.6% | -0.13 to -0.13 | GAIN |
| organism work per energy | 1.511 | 1.511 | -0.1% | -0.0008889 to -0.0008889 | power given |
| organism behind its window (s) | 2.268 | 3.168 | +39.7% | +0.6934 to +1.107 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2979 | 2784 | -6.6% | -1492 to +1102 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 4626 | 5209 | +12.6% | -1315 to +2481 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 52.98 | 45.62 | -13.9% | -24.68 to +9.951 | STEADY, inside the noise (cut) |
| failed requests (%) | 36.04 | 33.51 | -7.0% | -15.95 to +10.89 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.899 | 13.73 | +38.7% | +2.687 to +4.981 | power given |
| pods started | 5.56 | 11.76 | +111.5% | +4.697 to +7.703 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.004308 to +0.0007996 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1382 | 1376 | -0.4% | -21.01 to +9.626 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1382 | 1376 | -0.4% | -21.28 to +9.367 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.512 | 2.483 | -1.2% | -0.2365 to +0.1771 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.95 | 82.18 | +8.2% | +0.1575 to +12.32 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.636 | 6.072 | +31.0% | +1.08 to +1.792 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3375 | 3460 | +2.5% | -1508 to +1679 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5146 | 5420 | +5.3% | -1754 to +2301 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 54.7 | 48.64 | -11.1% | -24.15 to +12.04 | STEADY, inside the noise (cut) |
| failed requests (%) | 39.09 | 37.11 | -5.1% | -18.67 to +14.7 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.902 | 13.59 | +37.2% | +2.481 to +4.896 | power given |
| pods started | 5.44 | 10.6 | +94.9% | +4.263 to +6.057 | power given |
| worker nodes in service, mean | 6 | 5.997 | -0.0% | -0.006232 to +0.0008305 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1383 | 1374 | -0.7% | -23.07 to +3.652 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1383 | 1373 | -0.7% | -23.47 to +3.237 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.537 | 2.455 | -3.2% | -0.2589 to +0.09533 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.19 | 79.87 | +3.5% | -3.016 to +8.373 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.34 | 4.264 | +27.7% | +0.6535 to +1.195 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

23 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3546 | 3214 | -9.4% | -2024 to +1359 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5234 | 5021 | -4.1% | -2527 to +2102 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 54.43 | 45.36 | -16.7% | -31.19 to +13.06 | STEADY, inside the noise (cut) |
| failed requests (%) | 41.02 | 36.01 | -12.2% | -24.7 to +14.67 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.901 | 12.98 | +31.1% | +2.087 to +4.067 | power given |
| pods started | 5.304 | 13.65 | +157.4% | +6.121 to +10.57 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.00163 to +0.0005695 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1378 | 1371 | -0.5% | -24.25 to +9.57 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1378 | 1371 | -0.5% | -24.27 to +9.431 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.468 | 2.414 | -2.2% | -0.2806 to +0.1718 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.2 | 80.23 | +5.3% | -3.158 to +11.23 | shown, not judged |
| organism work | 3.317e+13 | 3.317e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.512e+15 | 5.512e+15 | +0.0% | +4.35e+09 to +4.35e+09 | power given |
| organism time over the line (% of steps) | 1.469 | 1.382 | -5.9% | -0.0869 to -0.0869 | GAIN |
| organism work per energy | 0.006018 | 0.006018 | -0.0% | -4.749e-09 to -4.749e-09 | power given |
| organism behind its window (s) | 3.835 | 4.896 | +27.7% | +0.7574 to +1.364 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

24 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3142 | 3593 | +14.4% | -1462 to +2365 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4823 | 5377 | +11.5% | -2037 to +3145 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 49.92 | 49.42 | -1.0% | -24.9 to +23.9 | STEADY, inside the noise (cut) |
| failed requests (%) | 38.78 | 38.87 | +0.3% | -20.64 to +20.84 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.914 | 12.95 | +30.6% | +1.64 to +4.435 | power given |
| pods started | 5.5 | 10 | +81.8% | +3.488 to +5.512 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003258 to +0.0003449 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1375 | 1372 | -0.3% | -22.83 to +14.98 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1375 | 1371 | -0.3% | -22.99 to +14.71 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.434 | 2.423 | -0.5% | -0.2644 to +0.2416 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.57 | 80.25 | +9.1% | -1.469 to +14.83 | shown, not judged |
| organism work | 1.082e+13 | 1.082e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.854e+13 | 2.855e+13 | +0.0% | +4.369e+09 to +4.369e+09 | power given |
| organism time over the line (% of steps) | 2.451 | 2.367 | -3.4% | -0.08396 to -0.08396 | GAIN |
| organism work per energy | 0.3789 | 0.3788 | -0.0% | -5.798e-05 to -5.798e-05 | power given |
| organism behind its window (s) | 4.138 | 5.625 | +36.0% | +1.025 to +1.95 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
