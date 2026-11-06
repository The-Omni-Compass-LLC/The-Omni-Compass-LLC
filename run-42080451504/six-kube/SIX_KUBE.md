# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Energy / Facility / Industrial, 500 copies: native | Energy / Facility / Industrial, 500 copies: omni | Distribution / Specialized, 500 copies: native | Distribution / Specialized, 500 copies: omni |
|---|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3148 | 5990 | 4213 | 4168 |
| response time (ms), 99th percentile | 4642 | 8458 | 6091 | 6407 |
| time over the response line (% of samples) | 48.44 | 72.3 | 57.76 | 60.94 |
| failed requests (%) | 38.64 | 58.7 | 43.8 | 48.44 |
| HPA replicas, mean | 9.895 | 15.01 | 9.923 | 14.79 |
| pods started | 5.533 | 10.6 | 5.267 | 11.62 |
| worker nodes in service, mean | 6 | 5.999 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 1372 | 1387 | 1381 | 1383 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1372 | 1387 | 1381 | 1383 |
| CPU used with Omni's own (cores), mean | 2.396 | 2.632 | 2.496 | 2.58 |
| host CPU busy, the real machine under kind (%) | 72.81 | 86.46 | 74.87 | 83.38 |
| organism work | 3.317e+13 | 3.317e+13 | 1.082e+13 | 1.082e+13 |
| organism energy (J) | 5.512e+15 | 5.512e+15 | 2.854e+13 | 2.855e+13 |
| organism time over the line (% of steps) | 1.469 | 1.382 | 2.451 | 2.367 |
| organism work per energy | 0.006018 | 0.006018 | 0.3789 | 0.3788 |
| organism behind its window (s) | 3.533 | 4.787 | 4.1 | 5.508 |

## Each organism: omni against native, paired by repetition

### Energy / Facility / Industrial, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

15 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3148 | 5990 | +90.3% | +1083 to +4601 | LOSS |
| response time (ms), 99th percentile | 4642 | 8458 | +82.2% | +1505 to +6128 | LOSS |
| time over the response line (% of samples) | 48.44 | 72.3 | +49.3% | +0.5877 to +47.13 | LOSS |
| failed requests (%) | 38.64 | 58.7 | +51.9% | +0.5557 to +39.55 | LOSS |
| HPA replicas, mean | 9.895 | 15.01 | +51.7% | +4.254 to +5.977 | power given |
| pods started | 5.533 | 10.6 | +91.6% | +4.298 to +5.835 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003377 to +0.001474 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 1372 | 1387 | +1.0% | -5.837 to +34.28 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1372 | 1387 | +1.0% | -5.856 to +34.02 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.396 | 2.632 | +9.8% | -0.03359 to +0.5055 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.81 | 86.46 | +18.7% | +5.509 to +21.79 | shown, not judged |
| organism work | 3.317e+13 | 3.317e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.512e+15 | 5.512e+15 | +0.0% | +4.35e+09 to +4.35e+09 | power given |
| organism time over the line (% of steps) | 1.469 | 1.382 | -5.9% | -0.0869 to -0.0869 | GAIN |
| organism work per energy | 0.006018 | 0.006018 | -0.0% | -4.749e-09 to -4.749e-09 | power given |
| organism behind its window (s) | 3.533 | 4.787 | +35.5% | +0.9837 to +1.523 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 500 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

13 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4346 | 4168 | -4.1% | -2953 to +2597 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6299 | 6407 | +1.7% | -3465 to +3680 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 60.79 | 60.94 | +0.2% | -27.93 to +28.23 | STEADY, inside the noise (up) |
| failed requests (%) | 46.1 | 48.44 | +5.1% | -22.03 to +26.71 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.927 | 14.79 | +49.0% | +3.771 to +5.96 | power given |
| pods started | 5.154 | 11.62 | +125.4% | +4.851 to +8.072 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.537e-17 to +1.042e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 1383 | 1383 | -0.0% | -20.22 to +19.63 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1383 | 1383 | -0.0% | -20.22 to +19.63 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.532 | 2.58 | +1.9% | -0.2183 to +0.315 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.93 | 83.38 | +9.8% | -0.8816 to +15.79 | shown, not judged |
| organism work | 1.082e+13 | 1.082e+13 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.854e+13 | 2.855e+13 | +0.0% | +4.369e+09 to +4.369e+09 | power given |
| organism time over the line (% of steps) | 2.451 | 2.367 | -3.4% | -0.08396 to -0.08396 | GAIN |
| organism work per energy | 0.3789 | 0.3788 | -0.0% | -5.798e-05 to -5.798e-05 | power given |
| organism behind its window (s) | 4.115 | 5.508 | +33.8% | +1.035 to +1.749 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The spine, the muscles every stack runs on
- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
