# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 100 copies: native | The spine, the muscles every stack runs on, 100 copies: omni | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3681 | 3314 | 4187 | 4436 | 3692 | 2701 |
| response time (ms), 99th percentile | 5693 | 5379 | 6580 | 6659 | 5863 | 5063 |
| time over the response line (% of samples) | 47.51 | 48.34 | 54.85 | 58.31 | 52.9 | 51.97 |
| failed requests (%) | 30.76 | 33.74 | 37.32 | 41.47 | 36.58 | 40.08 |
| HPA replicas, mean | 9.773 | 12.69 | 9.796 | 11.19 | 9.798 | 12.22 |
| pods started | 4.782 | 10.09 | 4.509 | 7.527 | 4.345 | 8.655 |
| worker nodes in service, mean | 5.999 | 5.995 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.6 | 276 | 277.6 | 277.6 | 276.5 | 276.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.6 | 275.9 | 277.6 | 277.6 | 276.5 | 276.6 |
| CPU used with Omni's own (cores), mean | 2.393 | 2.437 | 2.496 | 2.55 | 2.431 | 2.478 |
| host CPU busy, the real machine under kind (%) | 70.87 | 75.39 | 75.7 | 84.26 | 74.49 | 80.26 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 |
| organism behind its window (s) | 0.4255 | 0.5145 | 0.9164 | 1.184 | 0.5709 | 0.4182 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

55 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3681 | 3314 | -10.0% | -856.5 to +123.1 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5693 | 5379 | -5.5% | -661.6 to +33.46 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 47.51 | 48.34 | +1.7% | -0.5221 to +2.184 | STEADY, inside the noise (up) |
| failed requests (%) | 30.76 | 33.74 | +9.7% | +1.342 to +4.629 | LOSS |
| HPA replicas, mean | 9.773 | 12.69 | +29.8% | +2.366 to +3.461 | power given |
| pods started | 4.782 | 10.09 | +111.0% | +4.588 to +6.03 | power given |
| worker nodes in service, mean | 5.999 | 5.995 | -0.1% | -0.01403 to +0.005904 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.6 | 276 | +0.1% | -0.01083 to +0.813 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.6 | 275.9 | +0.1% | -0.123 to +0.6707 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.393 | 2.437 | +1.8% | +0.03571 to +0.05194 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.87 | 75.39 | +6.4% | +4.334 to +4.698 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.4255 | 0.5145 | +20.9% | +0.04992 to +0.1283 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (time over the response line (% of samples); failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 4

55 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4187 | 4436 | +6.0% | -401.6 to +899.9 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6580 | 6659 | +1.2% | -446.7 to +604.9 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 54.85 | 58.31 | +6.3% | +0.8849 to +6.047 | LOSS |
| failed requests (%) | 37.32 | 41.47 | +11.1% | +1.56 to +6.735 | LOSS |
| HPA replicas, mean | 9.796 | 11.19 | +14.2% | +0.8444 to +1.946 | power given |
| pods started | 4.509 | 7.527 | +66.9% | +2.213 to +3.823 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +5.672e-16 to +1.564e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.6 | 277.6 | +0.0% | -0.3579 to +0.5336 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.6 | 277.6 | +0.0% | -0.3579 to +0.5336 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.496 | 2.55 | +2.2% | +0.03488 to +0.07297 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.7 | 84.26 | +11.3% | +8.091 to +9.025 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.9164 | 1.184 | +29.2% | +0.2115 to +0.3231 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 2

55 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3692 | 2701 | -26.8% | -1505 to -477.5 | GAIN |
| response time (ms), 99th percentile | 5863 | 5063 | -13.6% | -1429 to -170.8 | GAIN |
| time over the response line (% of samples) | 52.9 | 51.97 | -1.7% | -1.85 to -0.0004509 | GAIN |
| failed requests (%) | 36.58 | 40.08 | +9.5% | +1.082 to +5.904 | LOSS |
| HPA replicas, mean | 9.798 | 12.22 | +24.8% | +1.868 to +2.985 | power given |
| pods started | 4.345 | 8.655 | +99.2% | +3.332 to +5.286 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.968e-17 to +9.194e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.5 | 276.6 | +0.0% | -0.3717 to +0.5431 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.5 | 276.6 | +0.0% | -0.3717 to +0.5431 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.431 | 2.478 | +2.0% | +0.0345 to +0.06094 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.49 | 80.26 | +7.7% | +5.389 to +6.135 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.5709 | 0.4182 | -26.8% | -0.1956 to -0.1099 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Energy / Facility / Industrial
- Distribution / Specialized
- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
