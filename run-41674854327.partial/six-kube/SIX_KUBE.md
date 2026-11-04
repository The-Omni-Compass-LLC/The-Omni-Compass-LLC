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
| response time (ms), 95th percentile | 3579 | 4564 | 4162 | 3366 | 5106 | 4324 | 4778 | 5893 | 3669 | 5727 |
| response time (ms), 99th percentile | 5536 | 6533 | 5900 | 5348 | 7125 | 5914 | 6579 | 7882 | 5293 | 8331 |
| time over the response line (% of samples) | 53.73 | 57.12 | 54.36 | 48.41 | 67.14 | 50.71 | 59.81 | 71.98 | 50.16 | 72.79 |
| failed requests (%) | 42.28 | 44.89 | 43.03 | 39.35 | 49.82 | 39.3 | 46.28 | 58.76 | 38.73 | 59.25 |
| HPA replicas, mean | 9.905 | 14.66 | 9.901 | 13.17 | 9.915 | 13.92 | 9.909 | 15.05 | 9.911 | 15.18 |
| pods started | 5.24 | 10.17 | 5.44 | 10.36 | 5.2 | 11.28 | 5.24 | 10.9 | 5.6 | 11.04 |
| worker nodes in service, mean | 6 | 6 | 6 | 5.999 | 5.999 | 5.999 | 6 | 5.999 | 6 | 5.998 |
| energy, parked workers still on at idle power (Wh, declared model) | 1377 | 1377 | 1375 | 1373 | 1389 | 1372 | 1380 | 1386 | 1372 | 1388 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1377 | 1376 | 1375 | 1373 | 1388 | 1372 | 1380 | 1386 | 1372 | 1388 |
| CPU used with Omni's own (cores), mean | 2.465 | 2.502 | 2.427 | 2.444 | 2.607 | 2.444 | 2.496 | 2.631 | 2.39 | 2.648 |
| host CPU busy, the real machine under kind (%) | 72.35 | 77.58 | 73.36 | 80.68 | 79.21 | 78.67 | 76.43 | 86.72 | 71.71 | 86.43 |
| organism work | 1.044e+13 | 1.044e+13 | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 3.317e+13 | 3.317e+13 | 1.082e+13 | 1.082e+13 |
| organism energy (J) | 6.905e+12 | 6.909e+12 | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 5.512e+15 | 5.512e+15 | 2.854e+13 | 2.855e+13 |
| organism time over the line (% of steps) | 2.335 | 2.205 | 1.943 | 1.874 | 4.602 | 4.511 | 1.469 | 1.382 | 2.451 | 2.367 |
| organism work per energy | 1.511 | 1.511 | 1.375 | 1.374 | 1.116 | 1.115 | 0.006018 | 0.006018 | 0.3789 | 0.3788 |
| organism behind its window (s) | 2.116 | 2.852 | 4.436 | 5.82 | 3.204 | 3.932 | 3.808 | 4.843 | 3.98 | 5.426 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

23 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3399 | 4564 | +34.3% | -797.3 to +3128 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5271 | 6533 | +23.9% | -1333 to +3857 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 51.62 | 57.12 | +10.7% | -15.64 to +26.64 | STEADY, inside the noise (up) |
| failed requests (%) | 40.61 | 44.89 | +10.5% | -13.87 to +22.44 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.903 | 14.66 | +48.0% | +3.761 to +5.75 | power given |
| pods started | 5.261 | 10.17 | +93.4% | +4.001 to +5.825 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.000544 to +9.775e-05 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1377 | 1377 | -0.0% | -17.27 to +17.24 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1377 | 1376 | -0.0% | -17.3 to +17.21 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.45 | 2.502 | +2.1% | -0.1762 to +0.2808 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.77 | 77.58 | +8.1% | -1.314 to +12.93 | shown, not judged |
| organism work | 1.044e+13 | 1.044e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 6.905e+12 | 6.909e+12 | +0.1% | +4.063e+09 to +4.063e+09 | power given |
| organism time over the line (% of steps) | 2.335 | 2.205 | -5.6% | -0.13 to -0.13 | GAIN |
| organism work per energy | 1.511 | 1.511 | -0.1% | -0.0008889 to -0.0008889 | power given |
| organism behind its window (s) | 2.109 | 2.852 | +35.3% | +0.6113 to +0.8757 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4162 | 3366 | -19.1% | -2581 to +989.5 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5900 | 5348 | -9.4% | -2811 to +1706 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 54.36 | 48.41 | -10.9% | -27.55 to +15.66 | STEADY, inside the noise (cut) |
| failed requests (%) | 43.03 | 39.35 | -8.6% | -21.73 to +14.36 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.901 | 13.17 | +33.1% | +1.879 to +4.666 | power given |
| pods started | 5.44 | 10.36 | +90.4% | +3.461 to +6.379 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002024 to +0.0005603 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1375 | 1373 | -0.2% | -17.48 to +13.28 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1375 | 1373 | -0.2% | -17.53 to +13.1 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.427 | 2.444 | +0.7% | -0.1917 to +0.2258 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.36 | 80.68 | +10.0% | +0.5359 to +14.11 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.436 | 5.82 | +31.2% | +1.065 to +1.703 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 3 (energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

25 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 5106 | 4324 | -15.3% | -2679 to +1115 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 7125 | 5914 | -17.0% | -3652 to +1230 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 67.14 | 50.71 | -24.5% | -36.3 to +3.428 | STEADY, inside the noise (cut) |
| failed requests (%) | 49.82 | 39.3 | -21.1% | -28.65 to +7.592 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.915 | 13.92 | +40.4% | +2.932 to +5.083 | power given |
| pods started | 5.2 | 11.28 | +116.9% | +4.836 to +7.324 | power given |
| worker nodes in service, mean | 5.999 | 5.999 | -0.0% | -0.002149 to +0.001704 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1389 | 1372 | -1.2% | -29.92 to -3.153 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1388 | 1372 | -1.2% | -29.88 to -3.257 | GAIN |
| CPU used with Omni's own (cores), mean | 2.607 | 2.444 | -6.2% | -0.3427 to +0.01703 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 79.21 | 78.67 | -0.7% | -6.442 to +5.363 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.204 | 3.932 | +22.7% | +0.558 to +0.898 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

21 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4948 | 5893 | +19.1% | -575.5 to +2464 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6792 | 7882 | +16.1% | -747.5 to +2928 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 62.04 | 71.98 | +16.0% | -3.633 to +23.51 | STEADY, inside the noise (up) |
| failed requests (%) | 48.75 | 58.76 | +20.5% | -2.217 to +22.23 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.91 | 15.05 | +51.8% | +4.32 to +5.954 | power given |
| pods started | 5.19 | 10.9 | +110.1% | +5.173 to +6.256 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003416 to +0.0009464 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1381 | 1386 | +0.4% | -5.55 to +16.11 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1381 | 1386 | +0.4% | -5.793 to +15.98 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.502 | 2.631 | +5.2% | -0.014 to +0.2726 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.72 | 86.72 | +13.0% | +5.231 to +14.76 | shown, not judged |
| organism work | 3.317e+13 | 3.317e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.512e+15 | 5.512e+15 | +0.0% | +4.35e+09 to +4.35e+09 | power given |
| organism time over the line (% of steps) | 1.469 | 1.382 | -5.9% | -0.0869 to -0.0869 | GAIN |
| organism work per energy | 0.006018 | 0.006018 | -0.0% | -4.749e-09 to -4.749e-09 | power given |
| organism behind its window (s) | 3.781 | 4.843 | +28.1% | +0.7928 to +1.331 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 500 copies: GAIN on 2 (worker nodes in service, mean; organism time over the line (% of steps)), LOSS on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 0

23 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3636 | 5727 | +57.5% | +280.9 to +3901 | LOSS |
| response time (ms), 99th percentile | 5190 | 8331 | +60.5% | +861.3 to +5420 | LOSS |
| time over the response line (% of samples) | 48.33 | 72.79 | +50.6% | +5.15 to +43.77 | LOSS |
| failed requests (%) | 37.15 | 59.25 | +59.5% | +5.48 to +38.73 | LOSS |
| HPA replicas, mean | 9.909 | 15.18 | +53.2% | +4.577 to +5.968 | power given |
| pods started | 5.609 | 11.04 | +96.9% | +4.884 to +5.985 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.003303 to -7.262e-05 | GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 1371 | 1388 | +1.3% | +2.554 to +32.44 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1371 | 1388 | +1.3% | +2.281 to +32.21 | power given |
| CPU used with Omni's own (cores), mean | 2.366 | 2.648 | +11.9% | +0.08186 to +0.4806 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.03 | 86.43 | +21.7% | +8.925 to +21.86 | shown, not judged |
| organism work | 1.082e+13 | 1.082e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.854e+13 | 2.855e+13 | +0.0% | +4.369e+09 to +4.369e+09 | power given |
| organism time over the line (% of steps) | 2.451 | 2.367 | -3.4% | -0.08396 to -0.08396 | GAIN |
| organism work per energy | 0.3789 | 0.3788 | -0.0% | -5.798e-05 to -5.798e-05 | power given |
| organism behind its window (s) | 3.978 | 5.426 | +36.4% | +1.169 to +1.727 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
