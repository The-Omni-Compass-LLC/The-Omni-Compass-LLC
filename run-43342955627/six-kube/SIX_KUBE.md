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
| response time (ms), 95th percentile | 3213 | 2655 | 3633 | 2768 | 2923 | 4676 | 4987 | 4838 | 2880 | 4162 |
| response time (ms), 99th percentile | 5054 | 4283 | 5488 | 5390 | 4584 | 6647 | 6706 | 6919 | 4261 | 6422 |
| time over the response line (% of samples) | 51.46 | 41.43 | 53.71 | 52.26 | 50.82 | 55.82 | 62.24 | 61.77 | 46.47 | 54.07 |
| failed requests (%) | 39.26 | 30.38 | 40.36 | 43.33 | 38.32 | 41.2 | 46.42 | 47.69 | 37.02 | 42.32 |
| HPA replicas, mean | 9.904 | 13.88 | 9.903 | 13.23 | 9.901 | 13.89 | 9.911 | 15.13 | 9.907 | 13.58 |
| pods started | 5.4 | 10.46 | 5.4 | 10.71 | 5.458 | 10.83 | 5.08 | 10.87 | 5.84 | 11.08 |
| worker nodes in service, mean | 6 | 5.999 | 6 | 5.998 | 6 | 6 | 6 | 6 | 6 | 5.999 |
| energy, parked workers still on at idle power (Wh, declared model) | 1378 | 1369 | 1380 | 1376 | 1382 | 1379 | 1384 | 1384 | 1374 | 1377 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1378 | 1369 | 1380 | 1376 | 1382 | 1379 | 1384 | 1384 | 1374 | 1377 |
| CPU used with Omni's own (cores), mean | 2.466 | 2.395 | 2.497 | 2.492 | 2.51 | 2.527 | 2.548 | 2.59 | 2.421 | 2.505 |
| host CPU busy, the real machine under kind (%) | 72.91 | 74.62 | 75.94 | 83.43 | 76.24 | 82.11 | 79.11 | 85.77 | 72.9 | 82.76 |
| organism work | 1.044e+13 | 1.044e+13 | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 3.317e+13 | 3.317e+13 | 1.082e+13 | 1.082e+13 |
| organism energy (J) | 6.905e+12 | 6.909e+12 | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 5.512e+15 | 5.512e+15 | 2.854e+13 | 2.855e+13 |
| organism time over the line (% of steps) | 2.335 | 2.205 | 1.943 | 1.874 | 4.602 | 4.511 | 1.469 | 1.382 | 2.451 | 2.367 |
| organism work per energy | 1.511 | 1.511 | 1.375 | 1.374 | 1.116 | 1.115 | 0.006018 | 0.006018 | 0.3789 | 0.3788 |
| organism behind its window (s) | 2.276 | 3.15 | 4.62 | 6.096 | 3.325 | 4.361 | 3.852 | 5.078 | 3.988 | 5.538 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

24 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3303 | 2655 | -19.6% | -2101 to +806 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5128 | 4283 | -16.5% | -2748 to +1058 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 51.11 | 41.43 | -18.9% | -26.09 to +6.733 | STEADY, inside the noise (cut) |
| failed requests (%) | 38.73 | 30.38 | -21.6% | -23 to +6.307 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.904 | 13.88 | +40.1% | +2.767 to +5.183 | power given |
| pods started | 5.375 | 10.46 | +94.6% | +3.998 to +6.168 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001278 to +0.0001339 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1377 | 1369 | -0.6% | -22.37 to +6.562 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1377 | 1369 | -0.6% | -22.44 to +6.461 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.456 | 2.395 | -2.5% | -0.2536 to +0.1307 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.7 | 74.62 | +2.6% | -3.91 to +7.749 | shown, not judged |
| organism work | 1.044e+13 | 1.044e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 6.905e+12 | 6.909e+12 | +0.1% | +4.063e+09 to +4.063e+09 | power given |
| organism time over the line (% of steps) | 2.335 | 2.205 | -5.6% | -0.13 to -0.13 | GAIN |
| organism work per energy | 1.511 | 1.511 | -0.1% | -0.0008889 to -0.0008889 | power given |
| organism behind its window (s) | 2.288 | 3.15 | +37.7% | +0.5894 to +1.136 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

24 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3482 | 2768 | -20.5% | -2569 to +1141 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5344 | 5390 | +0.9% | -2521 to +2614 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 52.63 | 52.26 | -0.7% | -23.2 to +22.46 | STEADY, inside the noise (cut) |
| failed requests (%) | 39.49 | 43.33 | +9.7% | -16.41 to +24.09 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.902 | 13.23 | +33.6% | +2.249 to +4.407 | power given |
| pods started | 5.417 | 10.71 | +97.7% | +3.919 to +6.664 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.004375 to +0.0003897 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1380 | 1376 | -0.3% | -19.87 to +12.53 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1380 | 1376 | -0.3% | -20.09 to +12.15 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.491 | 2.492 | +0.0% | -0.2204 to +0.2222 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.67 | 83.43 | +10.2% | +0.506 to +15 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.621 | 6.096 | +31.9% | +1.187 to +1.763 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

22 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2859 | 4882 | +70.8% | +480.2 to +3566 | LOSS |
| response time (ms), 99th percentile | 4468 | 6937 | +55.3% | +365 to +4574 | LOSS |
| time over the response line (% of samples) | 49.07 | 58.35 | +18.9% | -9.639 to +28.2 | STEADY, inside the noise (up) |
| failed requests (%) | 36.67 | 43.07 | +17.5% | -10.56 to +23.36 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.899 | 13.86 | +40.0% | +2.721 to +5.206 | power given |
| pods started | 5.5 | 10.77 | +95.9% | +4.484 to +6.061 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.314e-16 to +7.158e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 1380 | 1382 | +0.1% | -14.63 to +17.27 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1380 | 1382 | +0.1% | -14.63 to +17.27 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.496 | 2.558 | +2.5% | -0.1501 to +0.2739 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.74 | 83.08 | +9.7% | +0.8111 to +13.86 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.314 | 4.395 | +32.6% | +0.7428 to +1.421 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

23 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4885 | 4838 | -0.9% | -1612 to +1520 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6545 | 6919 | +5.7% | -1425 to +2174 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 60.88 | 61.77 | +1.5% | -15.38 to +17.17 | STEADY, inside the noise (up) |
| failed requests (%) | 45.18 | 47.69 | +5.5% | -13.58 to +18.58 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.91 | 15.13 | +52.6% | +4.666 to +5.768 | power given |
| pods started | 5.087 | 10.87 | +113.7% | +5.158 to +6.407 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.0004511 to +0.0003424 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1383 | 1384 | +0.0% | -10.69 to +11 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1383 | 1384 | +0.0% | -10.7 to +11 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.537 | 2.59 | +2.1% | -0.09688 to +0.2018 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 78.77 | 85.77 | +8.9% | +1.827 to +12.16 | shown, not judged |
| organism work | 3.317e+13 | 3.317e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.512e+15 | 5.512e+15 | +0.0% | +4.35e+09 to +4.35e+09 | power given |
| organism time over the line (% of steps) | 1.469 | 1.382 | -5.9% | -0.0869 to -0.0869 | GAIN |
| organism work per energy | 0.006018 | 0.006018 | -0.0% | -4.749e-09 to -4.749e-09 | power given |
| organism behind its window (s) | 3.839 | 5.078 | +32.3% | +0.8814 to +1.597 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

24 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2954 | 4162 | +40.9% | -600.7 to +3017 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4338 | 6422 | +48.0% | -223.6 to +4391 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 45.76 | 54.07 | +18.2% | -12.6 to +29.23 | STEADY, inside the noise (up) |
| failed requests (%) | 36.33 | 42.32 | +16.5% | -12.42 to +24.4 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.906 | 13.58 | +37.1% | +2.599 to +4.75 | power given |
| pods started | 5.875 | 11.08 | +88.7% | +4.319 to +6.098 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002144 to +0.0005716 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1373 | 1377 | +0.3% | -12.02 to +19.97 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1373 | 1377 | +0.3% | -12.16 to +19.87 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.409 | 2.505 | +4.0% | -0.1175 to +0.3099 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.61 | 82.76 | +14.0% | +3.7 to +16.58 | shown, not judged |
| organism work | 1.082e+13 | 1.082e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.854e+13 | 2.855e+13 | +0.0% | +4.369e+09 to +4.369e+09 | power given |
| organism time over the line (% of steps) | 2.451 | 2.367 | -3.4% | -0.08396 to -0.08396 | GAIN |
| organism work per energy | 0.3789 | 0.3788 | -0.0% | -5.798e-05 to -5.798e-05 | power given |
| organism behind its window (s) | 3.988 | 5.538 | +38.9% | +1.275 to +1.825 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
