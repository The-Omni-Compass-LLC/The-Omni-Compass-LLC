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
| response time (ms), 95th percentile | 3529 | 2818 | 3168 | 4619 | 4414 | 4314 |
| response time (ms), 99th percentile | 5202 | 5411 | 4727 | 6458 | 6193 | 6300 |
| time over the response line (% of samples) | 53.75 | 50.77 | 49.14 | 54.08 | 60.66 | 53.27 |
| failed requests (%) | 40.61 | 41.09 | 36.72 | 39.32 | 43.81 | 41.23 |
| HPA replicas, mean | 9.902 | 12.36 | 9.897 | 14.04 | 9.911 | 13.69 |
| pods started | 5.488 | 10.8 | 5.561 | 10.51 | 5.171 | 12.05 |
| worker nodes in service, mean | 5.999 | 5.997 | 6 | 5.999 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 1379 | 1376 | 1375 | 1377 | 1384 | 1378 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1379 | 1375 | 1375 | 1377 | 1384 | 1378 |
| CPU used with Omni's own (cores), mean | 2.485 | 2.49 | 2.434 | 2.5 | 2.542 | 2.507 |
| host CPU busy, the real machine under kind (%) | 75.95 | 83.21 | 74.53 | 81.72 | 78.84 | 83.06 |
| organism work | 1.06e+13 | 1.06e+13 | 1.104e+13 | 1.104e+13 | 3.317e+13 | 3.317e+13 |
| organism energy (J) | 7.708e+12 | 7.712e+12 | 9.897e+12 | 9.901e+12 | 5.512e+15 | 5.512e+15 |
| organism time over the line (% of steps) | 1.943 | 1.874 | 4.602 | 4.511 | 1.469 | 1.382 |
| organism work per energy | 1.375 | 1.374 | 1.116 | 1.115 | 0.006018 | 0.006018 |
| organism behind its window (s) | 4.671 | 6.146 | 3.349 | 4.344 | 3.956 | 5.08 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3529 | 2818 | -20.1% | -1835 to +413.8 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5202 | 5411 | +4.0% | -1421 to +1840 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 53.75 | 50.77 | -5.5% | -18.1 to +12.14 | STEADY, inside the noise (cut) |
| failed requests (%) | 40.61 | 41.09 | +1.2% | -12.86 to +13.82 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.902 | 12.36 | +24.8% | +1.64 to +3.278 | power given |
| pods started | 5.488 | 10.8 | +96.9% | +3.957 to +6.677 | power given |
| worker nodes in service, mean | 5.999 | 5.997 | -0.0% | -0.005281 to +0.000817 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1379 | 1376 | -0.2% | -14.42 to +7.57 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1379 | 1375 | -0.3% | -14.73 to +7.213 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.485 | 2.49 | +0.2% | -0.1435 to +0.1521 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.95 | 83.21 | +9.6% | +2.464 to +12.05 | shown, not judged |
| organism work | 1.06e+13 | 1.06e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 7.708e+12 | 7.712e+12 | +0.1% | +4.236e+09 to +4.236e+09 | power given |
| organism time over the line (% of steps) | 1.943 | 1.874 | -3.6% | -0.06938 to -0.06938 | GAIN |
| organism work per energy | 1.375 | 1.374 | -0.1% | -0.0007553 to -0.0007553 | power given |
| organism behind its window (s) | 4.671 | 6.146 | +31.6% | +1.231 to +1.721 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3168 | 4619 | +45.8% | +192.7 to +2709 | LOSS |
| response time (ms), 99th percentile | 4727 | 6458 | +36.6% | +218.6 to +3242 | LOSS |
| time over the response line (% of samples) | 49.14 | 54.08 | +10.1% | -8.057 to +17.94 | STEADY, inside the noise (up) |
| failed requests (%) | 36.72 | 39.32 | +7.1% | -8.8 to +14.01 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.897 | 14.04 | +41.9% | +3.371 to +4.92 | power given |
| pods started | 5.561 | 10.51 | +89.0% | +4.324 to +5.578 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001794 to +8.239e-05 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1375 | 1377 | +0.1% | -9.478 to +12.61 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1375 | 1377 | +0.1% | -9.612 to +12.49 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.434 | 2.5 | +2.7% | -0.08146 to +0.2128 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.53 | 81.72 | +9.6% | +2.626 to +11.75 | shown, not judged |
| organism work | 1.104e+13 | 1.104e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 9.897e+12 | 9.901e+12 | +0.0% | +4.353e+09 to +4.353e+09 | power given |
| organism time over the line (% of steps) | 4.602 | 4.511 | -2.0% | -0.09081 to -0.09081 | GAIN |
| organism work per energy | 1.116 | 1.115 | -0.0% | -0.0004905 to -0.0004905 | power given |
| organism behind its window (s) | 3.349 | 4.344 | +29.7% | +0.8197 to +1.171 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 7

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4414 | 4314 | -2.3% | -1448 to +1247 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6193 | 6300 | +1.7% | -1507 to +1722 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 60.66 | 53.27 | -12.2% | -20.9 to +6.112 | STEADY, inside the noise (cut) |
| failed requests (%) | 43.81 | 41.23 | -5.9% | -14.53 to +9.37 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.911 | 13.69 | +38.2% | +3.041 to +4.524 | power given |
| pods started | 5.171 | 12.05 | +133.0% | +4.33 to +9.426 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.0003615 to +0.0001246 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1384 | 1378 | -0.4% | -15.13 to +3.058 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1384 | 1378 | -0.4% | -15.14 to +3.033 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.542 | 2.507 | -1.4% | -0.1567 to +0.0869 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 78.84 | 83.06 | +5.4% | +0.2199 to +8.216 | shown, not judged |
| organism work | 3.317e+13 | 3.317e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.512e+15 | 5.512e+15 | +0.0% | +4.35e+09 to +4.35e+09 | power given |
| organism time over the line (% of steps) | 1.469 | 1.382 | -5.9% | -0.0869 to -0.0869 | GAIN |
| organism work per energy | 0.006018 | 0.006018 | -0.0% | -4.749e-09 to -4.749e-09 | power given |
| organism behind its window (s) | 3.956 | 5.08 | +28.4% | +0.8713 to +1.377 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The spine, the muscles every stack runs on
- Distribution / Specialized
- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
