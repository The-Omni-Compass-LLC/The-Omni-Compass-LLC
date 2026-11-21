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
| response time (ms), 95th percentile | 3224 | 3238 | 3650 | 3777 | 4243 | 5109 | 3159 | 3935 | 2598 | 4242 |
| response time (ms), 99th percentile | 5103 | 4903 | 5256 | 6796 | 5911 | 7183 | 4652 | 6309 | 4483 | 6694 |
| time over the response line (% of samples) | 51.66 | 41.06 | 53.18 | 66.19 | 59.84 | 56.34 | 48.52 | 58.05 | 49.46 | 61.78 |
| failed requests (%) | 38.61 | 27.95 | 37.38 | 55.87 | 44.19 | 37.14 | 37.56 | 46.22 | 36.37 | 47.51 |
| HPA replicas, mean | 9.903 | 13.34 | 9.9 | 13.06 | 9.908 | 14.12 | 9.896 | 14.12 | 9.913 | 13.48 |
| pods started | 5.36 | 10.56 | 5.48 | 9.88 | 5.32 | 10.92 | 5.48 | 10.76 | 5.52 | 10.2 |
| worker nodes in service, mean | 6 | 6 | 6 | 5.999 | 6 | 5.998 | 6 | 5.999 | 6 | 5.999 |
| energy, parked workers still on at idle power (Wh, declared model) | 1381 | 1369 | 1381 | 1382 | 1386 | 1382 | 1374 | 1379 | 1380 | 1384 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1381 | 1369 | 1381 | 1382 | 1386 | 1382 | 1374 | 1379 | 1380 | 1384 |
| CPU used with Omni's own (cores), mean | 2.504 | 2.403 | 2.512 | 2.589 | 2.568 | 2.573 | 2.409 | 2.543 | 2.497 | 2.602 |
| host CPU busy, the real machine under kind (%) | 73.7 | 75.05 | 76.31 | 87.41 | 78.44 | 83.37 | 74.34 | 84.14 | 74.95 | 85.66 |
| organism work | 1.044e+13 | 1.044e+13 | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 3.317e+13 | 3.317e+13 | 1.082e+13 | 1.082e+13 |
| organism energy (J) | 6.905e+12 | 6.909e+12 | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 5.512e+15 | 5.512e+15 | 2.854e+13 | 2.855e+13 |
| organism time over the line (% of steps) | 2.335 | 2.205 | 1.943 | 1.874 | 4.602 | 4.511 | 1.469 | 1.382 | 2.451 | 2.367 |
| organism work per energy | 1.511 | 1.511 | 1.375 | 1.374 | 1.116 | 1.115 | 0.006018 | 0.006018 | 0.3789 | 0.3788 |
| organism behind its window (s) | 2.24 | 3.084 | 4.748 | 6.24 | 3.38 | 4.3 | 3.684 | 4.984 | 4.128 | 5.812 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3224 | 3238 | +0.5% | -1713 to +1742 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5103 | 4903 | -3.9% | -2306 to +1905 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 51.66 | 41.06 | -20.5% | -27.74 to +6.546 | STEADY, inside the noise (cut) |
| failed requests (%) | 38.61 | 27.95 | -27.6% | -25.74 to +4.424 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.903 | 13.34 | +34.7% | +2.158 to +4.721 | power given |
| pods started | 5.36 | 10.56 | +97.0% | +4.057 to +6.343 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.146e-17 to +9.241e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 1381 | 1369 | -0.8% | -24.27 to +1.847 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1381 | 1369 | -0.8% | -24.27 to +1.847 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.504 | 2.403 | -4.0% | -0.2834 to +0.0807 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.7 | 75.05 | +1.8% | -4.23 to +6.927 | shown, not judged |
| organism work | 1.044e+13 | 1.044e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 6.905e+12 | 6.909e+12 | +0.1% | +4.063e+09 to +4.063e+09 | power given |
| organism time over the line (% of steps) | 2.335 | 2.205 | -5.6% | -0.13 to -0.13 | GAIN |
| organism work per energy | 1.511 | 1.511 | -0.1% | -0.0008889 to -0.0008889 | power given |
| organism behind its window (s) | 2.24 | 3.084 | +37.7% | +0.6089 to +1.079 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3650 | 3777 | +3.5% | -1627 to +1881 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5256 | 6796 | +29.3% | -402.4 to +3482 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 53.18 | 66.19 | +24.5% | -3.262 to +29.28 | STEADY, inside the noise (up) |
| failed requests (%) | 37.38 | 55.87 | +49.5% | +2.74 to +34.24 | LOSS |
| HPA replicas, mean | 9.9 | 13.06 | +31.9% | +2.276 to +4.038 | power given |
| pods started | 5.48 | 9.88 | +80.3% | +3.276 to +5.524 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001663 to +0.0004432 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1381 | 1382 | +0.1% | -12.28 to +13.82 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1381 | 1382 | +0.0% | -12.39 to +13.74 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.512 | 2.589 | +3.1% | -0.0885 to +0.2426 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.31 | 87.41 | +14.5% | +6.035 to +16.16 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.748 | 6.24 | +31.4% | +1.151 to +1.833 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 2 (worker nodes in service, mean; organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4243 | 5109 | +20.4% | -983.7 to +2717 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5911 | 7183 | +21.5% | -832.7 to +3378 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 59.84 | 56.34 | -5.9% | -21.2 to +14.19 | STEADY, inside the noise (cut) |
| failed requests (%) | 44.19 | 37.14 | -15.9% | -23.2 to +9.107 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.908 | 14.12 | +42.5% | +3.161 to +5.261 | power given |
| pods started | 5.32 | 10.92 | +105.3% | +4.905 to +6.295 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.003144 to -0.0003842 | GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 1386 | 1382 | -0.3% | -16.68 to +9.109 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1386 | 1382 | -0.3% | -16.91 to +8.812 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.568 | 2.573 | +0.2% | -0.1647 to +0.1765 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 78.44 | 83.37 | +6.3% | -0.317 to +10.18 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.38 | 4.3 | +27.2% | +0.6639 to +1.176 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3159 | 3935 | +24.6% | -1061 to +2612 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 4652 | 6309 | +35.6% | -675.9 to +3990 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 48.52 | 58.05 | +19.6% | -12.41 to +31.47 | STEADY, inside the noise (up) |
| failed requests (%) | 37.56 | 46.22 | +23.1% | -9.915 to +27.24 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.896 | 14.12 | +42.7% | +3.294 to +5.159 | power given |
| pods started | 5.48 | 10.76 | +96.4% | +4.4 to +6.16 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002408 to +0.0002891 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1374 | 1379 | +0.4% | -10.8 to +21.72 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1374 | 1379 | +0.4% | -10.96 to +21.56 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.409 | 2.543 | +5.6% | -0.09219 to +0.3602 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.34 | 84.14 | +13.2% | +2.54 to +17.05 | shown, not judged |
| organism work | 3.317e+13 | 3.317e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.512e+15 | 5.512e+15 | +0.0% | +4.35e+09 to +4.35e+09 | power given |
| organism time over the line (% of steps) | 1.469 | 1.382 | -5.9% | -0.0869 to -0.0869 | GAIN |
| organism work per energy | 0.006018 | 0.006018 | -0.0% | -4.749e-09 to -4.749e-09 | power given |
| organism behind its window (s) | 3.684 | 4.984 | +35.3% | +0.9693 to +1.631 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2598 | 4242 | +63.3% | +176.9 to +3111 | LOSS |
| response time (ms), 99th percentile | 4483 | 6694 | +49.3% | +329.8 to +4092 | LOSS |
| time over the response line (% of samples) | 49.46 | 61.78 | +24.9% | -4.302 to +28.94 | STEADY, inside the noise (up) |
| failed requests (%) | 36.37 | 47.51 | +30.6% | -5.138 to +27.42 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.913 | 13.48 | +35.9% | +2.488 to +4.639 | power given |
| pods started | 5.52 | 10.2 | +84.8% | +3.978 to +5.382 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003037 to +0.0009079 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1380 | 1384 | +0.3% | -8.254 to +15.43 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1380 | 1384 | +0.2% | -8.431 to +15.29 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.497 | 2.602 | +4.2% | -0.05362 to +0.2634 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.95 | 85.66 | +14.3% | +5.837 to +15.58 | shown, not judged |
| organism work | 1.082e+13 | 1.082e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.854e+13 | 2.855e+13 | +0.0% | +4.369e+09 to +4.369e+09 | power given |
| organism time over the line (% of steps) | 2.451 | 2.367 | -3.4% | -0.08396 to -0.08396 | GAIN |
| organism work per energy | 0.3789 | 0.3788 | -0.0% | -5.798e-05 to -5.798e-05 | power given |
| organism behind its window (s) | 4.128 | 5.812 | +40.8% | +1.436 to +1.932 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
