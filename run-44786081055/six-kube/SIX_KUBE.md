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
| response time (ms), 95th percentile | 2543 | 5077 | 1902 | 4321 | 3902 | 5917 | 3518 | 4697 | 4716 | 4107 |
| response time (ms), 99th percentile | 3892 | 7020 | 2977 | 7712 | 5615 | 7854 | 5359 | 6030 | 6478 | 6016 |
| time over the response line (% of samples) | 45.07 | 66.07 | 27.7 | 75.87 | 56.76 | 70.49 | 66.27 | 52.42 | 61.26 | 50.68 |
| failed requests (%) | 33.65 | 51.47 | 16.93 | 63.92 | 40.7 | 56.24 | 50.92 | 39.92 | 41.91 | 38.94 |
| HPA replicas, mean | 9.892 | 14.76 | 9.875 | 13.34 | 9.903 | 15.68 | 9.919 | 12.43 | 9.928 | 12.64 |
| pods started | 5.7 | 10.5 | 6.2 | 9.1 | 5.4 | 10.9 | 4.9 | 10.7 | 5.1 | 10.3 |
| worker nodes in service, mean | 5.999 | 6 | 6 | 6 | 6 | 5.996 | 6 | 6 | 6 | 5.999 |
| energy, parked workers still on at idle power (Wh, declared model) | 1372 | 1387 | 1360 | 1390 | 1383 | 1387 | 1393 | 1375 | 1387 | 1374 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1371 | 1387 | 1360 | 1390 | 1383 | 1387 | 1393 | 1375 | 1387 | 1374 |
| CPU used with Omni's own (cores), mean | 2.382 | 2.63 | 2.226 | 2.67 | 2.523 | 2.64 | 2.666 | 2.468 | 2.577 | 2.465 |
| host CPU busy, the real machine under kind (%) | 69.96 | 83.04 | 67.36 | 89.88 | 77.26 | 86.82 | 81.79 | 82.12 | 78.25 | 81.5 |
| organism work | 1.044e+13 | 1.044e+13 | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 3.317e+13 | 3.317e+13 | 1.082e+13 | 1.082e+13 |
| organism energy (J) | 6.905e+12 | 6.909e+12 | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 5.512e+15 | 5.512e+15 | 2.854e+13 | 2.855e+13 |
| organism time over the line (% of steps) | 2.335 | 2.205 | 1.943 | 1.874 | 4.602 | 4.511 | 1.469 | 1.382 | 2.451 | 2.367 |
| organism work per energy | 1.511 | 1.511 | 1.375 | 1.374 | 1.116 | 1.115 | 0.006018 | 0.006018 | 0.3789 | 0.3788 |
| organism behind its window (s) | 2.19 | 3.08 | 4.56 | 6.41 | 3.39 | 4.43 | 4.04 | 4.91 | 4.34 | 5.56 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2543 | 5077 | +99.7% | -306.5 to +5375 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 3892 | 7020 | +80.4% | -552.9 to +6809 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 45.07 | 66.07 | +46.6% | -11.7 to +53.7 | STEADY, inside the noise (up) |
| failed requests (%) | 33.65 | 51.47 | +52.9% | -9.012 to +44.64 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.892 | 14.76 | +49.2% | +3.159 to +6.58 | power given |
| pods started | 5.7 | 10.5 | +84.2% | +3.692 to +5.908 | power given |
| worker nodes in service, mean | 5.999 | 6 | +0.0% | -0.0008397 to +0.00217 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 1372 | 1387 | +1.1% | -13.93 to +44.54 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1371 | 1387 | +1.1% | -13.8 to +44.61 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.382 | 2.63 | +10.4% | -0.137 to +0.6333 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.96 | 83.04 | +18.7% | +2.34 to +23.82 | shown, not judged |
| organism work | 1.044e+13 | 1.044e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 6.905e+12 | 6.909e+12 | +0.1% | +4.063e+09 to +4.063e+09 | power given |
| organism time over the line (% of steps) | 2.335 | 2.205 | -5.6% | -0.13 to -0.13 | GAIN |
| organism work per energy | 1.511 | 1.511 | -0.1% | -0.0008889 to -0.0008889 | power given |
| organism behind its window (s) | 2.19 | 3.08 | +40.6% | +0.5876 to +1.192 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 0

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1902 | 4321 | +127.1% | +856.5 to +3981 | LOSS |
| response time (ms), 99th percentile | 2977 | 7712 | +159.0% | +2418 to +7051 | LOSS |
| time over the response line (% of samples) | 27.7 | 75.87 | +173.9% | +23.8 to +72.53 | LOSS |
| failed requests (%) | 16.93 | 63.92 | +277.5% | +22.16 to +71.81 | LOSS |
| HPA replicas, mean | 9.875 | 13.34 | +35.1% | +2.363 to +4.572 | power given |
| pods started | 6.2 | 9.1 | +46.8% | +1.532 to +4.268 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.242e-16 to +5.794e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 1360 | 1390 | +2.2% | +6.315 to +53.97 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1360 | 1390 | +2.2% | +6.315 to +53.97 | power given |
| CPU used with Omni's own (cores), mean | 2.226 | 2.67 | +19.9% | +0.1259 to +0.7615 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.36 | 89.88 | +33.4% | +12.96 to +32.07 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.56 | 6.41 | +40.6% | +1.277 to +2.423 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3902 | 5917 | +51.6% | +52.1 to +3978 | LOSS |
| response time (ms), 99th percentile | 5615 | 7854 | +39.9% | -139.7 to +4619 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 56.76 | 70.49 | +24.2% | -3.237 to +30.69 | STEADY, inside the noise (up) |
| failed requests (%) | 40.7 | 56.24 | +38.2% | -0.7913 to +31.87 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.903 | 15.68 | +58.4% | +5.546 to +6.017 | power given |
| pods started | 5.4 | 10.9 | +101.9% | +4.892 to +6.108 | power given |
| worker nodes in service, mean | 6 | 5.996 | -0.1% | -0.008818 to +0.0005243 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1383 | 1387 | +0.3% | -8.166 to +16.8 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1383 | 1387 | +0.3% | -9.036 to +16.42 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.523 | 2.64 | +4.6% | -0.05314 to +0.2858 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.26 | 86.82 | +12.4% | +4.769 to +14.35 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.39 | 4.43 | +30.7% | +0.7636 to +1.316 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3518 | 4697 | +33.5% | -1554 to +3911 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5359 | 6030 | +12.5% | -2399 to +3742 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 66.27 | 52.42 | -20.9% | -41.77 to +14.07 | STEADY, inside the noise (cut) |
| failed requests (%) | 50.92 | 39.92 | -21.6% | -37.59 to +15.59 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.919 | 12.43 | +25.3% | +0.2342 to +4.795 | power given |
| pods started | 4.9 | 10.7 | +118.4% | +4.087 to +7.513 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.02e-16 to +1.823e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 1393 | 1375 | -1.3% | -36.59 to +0.7123 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1393 | 1375 | -1.3% | -36.59 to +0.7123 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.666 | 2.468 | -7.4% | -0.4518 to +0.05598 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 81.79 | 82.12 | +0.4% | -7.298 to +7.972 | shown, not judged |
| organism work | 3.317e+13 | 3.317e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.512e+15 | 5.512e+15 | +0.0% | +4.35e+09 to +4.35e+09 | power given |
| organism time over the line (% of steps) | 1.469 | 1.382 | -5.9% | -0.0869 to -0.0869 | GAIN |
| organism work per energy | 0.006018 | 0.006018 | -0.0% | -4.749e-09 to -4.749e-09 | power given |
| organism behind its window (s) | 4.04 | 4.91 | +21.5% | +0.3943 to +1.346 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4716 | 4107 | -12.9% | -4125 to +2906 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6478 | 6016 | -7.1% | -4538 to +3615 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 61.26 | 50.68 | -17.3% | -43.57 to +22.42 | STEADY, inside the noise (cut) |
| failed requests (%) | 41.91 | 38.94 | -7.1% | -30.84 to +24.92 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.928 | 12.64 | +27.3% | +0.3364 to +5.079 | power given |
| pods started | 5.1 | 10.3 | +102.0% | +3.521 to +6.879 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001505 to +0.0003109 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1387 | 1374 | -0.9% | -36.37 to +11.98 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1387 | 1374 | -0.9% | -36.45 to +11.88 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.577 | 2.465 | -4.3% | -0.4408 to +0.2174 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 78.25 | 81.5 | +4.2% | -7.124 to +13.63 | shown, not judged |
| organism work | 1.082e+13 | 1.082e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.854e+13 | 2.855e+13 | +0.0% | +4.369e+09 to +4.369e+09 | power given |
| organism time over the line (% of steps) | 2.451 | 2.367 | -3.4% | -0.08396 to -0.08396 | GAIN |
| organism work per energy | 0.3789 | 0.3788 | -0.0% | -5.798e-05 to -5.798e-05 | power given |
| organism behind its window (s) | 4.34 | 5.56 | +28.1% | +0.6142 to +1.826 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
