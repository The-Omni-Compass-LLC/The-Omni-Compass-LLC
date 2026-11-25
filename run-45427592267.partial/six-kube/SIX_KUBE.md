# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 500 copies: native | Compute / AI / Cloud, 500 copies: omni | Physics / Robotics / Autonomous, 500 copies: native | Physics / Robotics / Autonomous, 500 copies: omni | Energy / Facility / Industrial, 500 copies: native | Energy / Facility / Industrial, 500 copies: omni |
|---|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3860 | 3422 | 4475 | 4262 | 3130 | 4885 |
| response time (ms), 99th percentile | 5797 | 5900 | 6260 | 6044 | 4555 | 7320 |
| time over the response line (% of samples) | 54.51 | 55.23 | 59.09 | 49.89 | 47.32 | 63.68 |
| failed requests (%) | 40.24 | 44.28 | 44.99 | 35.04 | 35.14 | 51.03 |
| HPA replicas, mean | 9.902 | 12.33 | 9.905 | 13.96 | 9.896 | 13.88 |
| pods started | 5.39 | 9.878 | 5.366 | 11.07 | 5.575 | 10.39 |
| worker nodes in service, mean | 6 | 5.996 | 6 | 5.999 | 6 | 5.998 |
| energy, parked workers still on at idle power (Wh, declared model) | 1380 | 1377 | 1379 | 1375 | 1374 | 1383 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1380 | 1377 | 1379 | 1374 | 1374 | 1383 |
| CPU used with Omni's own (cores), mean | 2.492 | 2.512 | 2.486 | 2.471 | 2.408 | 2.589 |
| host CPU busy, the real machine under kind (%) | 76.19 | 84.44 | 76.86 | 80.6 | 74.37 | 86.02 |
| organism work | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 3.317e+13 | 3.317e+13 |
| organism energy (J) | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 5.512e+15 | 5.512e+15 |
| organism time over the line (% of steps) | 1.943 | 1.874 | 4.602 | 4.511 | 1.469 | 1.382 |
| organism work per energy | 1.375 | 1.374 | 1.116 | 1.115 | 0.006018 | 0.006018 |
| organism behind its window (s) | 4.673 | 6.185 | 3.407 | 4.252 | 3.825 | 5.217 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 500 copies: GAIN on 2 (worker nodes in service, mean; organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3860 | 3422 | -11.3% | -1817 to +941.8 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5797 | 5900 | +1.8% | -1687 to +1894 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 54.51 | 55.23 | +1.3% | -14.5 to +15.94 | STEADY, inside the noise (up) |
| failed requests (%) | 40.24 | 44.28 | +10.1% | -8.848 to +16.94 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.902 | 12.33 | +24.5% | +1.543 to +3.307 | power given |
| pods started | 5.39 | 9.878 | +83.3% | +3.367 to +5.608 | power given |
| worker nodes in service, mean | 6 | 5.996 | -0.1% | -0.006455 to -0.0009487 | GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 1380 | 1377 | -0.2% | -13.49 to +8.354 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1380 | 1377 | -0.2% | -13.99 to +7.748 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.492 | 2.512 | +0.8% | -0.1267 to +0.1658 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.19 | 84.44 | +10.8% | +3.586 to +12.92 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.673 | 6.185 | +32.4% | +1.227 to +1.797 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4419 | 4262 | -3.5% | -1337 to +1023 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6195 | 6044 | -2.4% | -1626 to +1325 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 58.67 | 49.89 | -15.0% | -20.75 to +3.189 | STEADY, inside the noise (cut) |
| failed requests (%) | 44.69 | 35.04 | -21.6% | -20.3 to +0.9972 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.905 | 13.96 | +40.9% | +3.23 to +4.878 | power given |
| pods started | 5.375 | 11.07 | +106.0% | +5.187 to +6.213 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001809 to +0.0007276 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1379 | 1375 | -0.3% | -13.94 to +4.902 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1379 | 1374 | -0.3% | -14.03 to +4.825 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.481 | 2.471 | -0.4% | -0.1361 to +0.1163 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.74 | 80.6 | +5.0% | -0.1671 to +7.887 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.413 | 4.252 | +24.6% | +0.635 to +1.045 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%)), power given on 5 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); organism energy (J); organism work per energy), STEADY (inside the noise) on 2

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3130 | 5001 | +59.8% | +637.5 to +3103 | LOSS |
| response time (ms), 99th percentile | 4555 | 7492 | +64.5% | +1387 to +4489 | LOSS |
| time over the response line (% of samples) | 47.32 | 65.26 | +37.9% | +4.276 to +31.6 | LOSS |
| failed requests (%) | 35.14 | 52.3 | +48.8% | +4.95 to +29.37 | LOSS |
| HPA replicas, mean | 9.896 | 14.01 | +41.6% | +3.406 to +4.831 | power given |
| pods started | 5.575 | 10.3 | +84.8% | +4.169 to +5.281 | power given |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.003867 to +0.0008941 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1374 | 1384 | +0.8% | +0.15 to +21.31 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1374 | 1384 | +0.8% | -0.1227 to +21.14 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.408 | 2.601 | +8.0% | +0.05067 to +0.3353 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.37 | 86.45 | +16.2% | +7.536 to +16.62 | shown, not judged |
| organism work | 3.317e+13 | 3.317e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.512e+15 | 5.512e+15 | +0.0% | +4.35e+09 to +4.35e+09 | power given |
| organism time over the line (% of steps) | 1.469 | 1.382 | -5.9% | -0.0869 to -0.0869 | GAIN |
| organism work per energy | 0.006018 | 0.006018 | -0.0% | -4.749e-09 to -4.749e-09 | power given |
| organism behind its window (s) | 3.825 | 5.238 | +36.9% | +1.145 to +1.68 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The spine, the muscles every stack runs on
- Distribution / Specialized
- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
