# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The spine, the muscles every stack runs on, 100 copies: native | The spine, the muscles every stack runs on, 100 copies: omni | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3335 | 2582 | 4115 | 3415 | 5144 | 3450 | 3407 | 2743 | 4349 | 4128 |
| response time (ms), 99th percentile | 5431 | 5161 | 6227 | 5412 | 7614 | 6158 | 5614 | 4823 | 6727 | 6609 |
| time over the response line (% of samples) | 50.82 | 49.93 | 54.15 | 54.06 | 68.3 | 66.53 | 52.58 | 51.16 | 65.33 | 64.91 |
| failed requests (%) | 37.11 | 40.5 | 40.12 | 42.49 | 48.28 | 52.82 | 38.4 | 41.08 | 50.05 | 51.93 |
| HPA replicas, mean | 9.797 | 12.76 | 9.805 | 11.28 | 9.86 | 10.91 | 9.799 | 11.75 | 9.865 | 10.83 |
| pods started | 4.1 | 9.5 | 4.2 | 7.175 | 3.325 | 7.375 | 4.2 | 8.4 | 3.05 | 5.65 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 5.999 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.1 | 275.6 | 276.4 | 276.5 | 279.1 | 278.8 | 276 | 276.1 | 278.4 | 278.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.1 | 275.6 | 276.4 | 276.5 | 279.1 | 278.7 | 276 | 276.1 | 278.4 | 278.4 |
| CPU used with Omni's own (cores), mean | 2.377 | 2.428 | 2.435 | 2.475 | 2.605 | 2.622 | 2.4 | 2.452 | 2.56 | 2.599 |
| host CPU busy, the real machine under kind (%) | 70.54 | 75.3 | 73.68 | 81.46 | 79.38 | 84.41 | 73.72 | 80.05 | 77.8 | 85.23 |
| organism work | 2.094e+12 | 2.094e+12 | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.383e+12 | 1.384e+12 | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 2.369 | 2.235 | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.514 | 1.513 | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.43 | 0.5025 | 0.885 | 1.155 | 0.59 | 0.4275 | 0.74 | 0.4225 | 0.5 | 1.097 |

## Each organism: omni against native, paired by repetition

### The spine, the muscles every stack runs on, 100 copies: GAIN on 3 (energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3335 | 2582 | -22.6% | -1518 to +13.58 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 5431 | 5161 | -5.0% | -797.7 to +257.8 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 50.82 | 49.93 | -1.8% | -2.044 to +0.2651 | STEADY, inside the noise (cut) |
| failed requests (%) | 37.11 | 40.5 | +9.2% | +1.61 to +5.186 | LOSS |
| HPA replicas, mean | 9.797 | 12.76 | +30.2% | +2.356 to +3.566 | power given |
| pods started | 4.1 | 9.5 | +131.7% | +4.575 to +6.225 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.786e-16 to +4.898e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.1 | 275.6 | -0.2% | -0.9597 to -0.04442 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.1 | 275.6 | -0.2% | -0.9597 to -0.04442 | GAIN |
| CPU used with Omni's own (cores), mean | 2.377 | 2.428 | +2.1% | +0.03662 to +0.06518 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.54 | 75.3 | +6.8% | +4.38 to +5.153 | shown, not judged |
| organism work | 2.094e+12 | 2.094e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.383e+12 | 1.384e+12 | +0.1% | +8.159e+08 to +8.159e+08 | power given |
| organism time over the line (% of steps) | 2.369 | 2.235 | -5.7% | -0.1341 to -0.1341 | GAIN |
| organism work per energy | 1.514 | 1.513 | -0.1% | -0.0008926 to -0.0008926 | power given |
| organism behind its window (s) | 0.43 | 0.5025 | +16.9% | +0.0309 to +0.1141 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Compute / AI / Cloud, 100 copies: GAIN on 2 (response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4115 | 3415 | -17.0% | -1531 to +131.6 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6227 | 5412 | -13.1% | -1488 to -140.5 | GAIN |
| time over the response line (% of samples) | 54.15 | 54.06 | -0.2% | -1.565 to +1.395 | STEADY, inside the noise (cut) |
| failed requests (%) | 40.12 | 42.49 | +5.9% | -0.1168 to +4.861 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.805 | 11.28 | +15.1% | +0.7411 to +2.214 | power given |
| pods started | 4.2 | 7.175 | +70.8% | +2.007 to +3.943 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +1.688e-16 to +1.163e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.4 | 276.5 | +0.0% | -0.3407 to +0.5283 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.4 | 276.5 | +0.0% | -0.3407 to +0.5283 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.435 | 2.475 | +1.6% | +0.02383 to +0.05627 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.68 | 81.46 | +10.6% | +7.394 to +8.165 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | power given |
| organism behind its window (s) | 0.885 | 1.155 | +30.5% | +0.2024 to +0.3376 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 5144 | 3450 | -32.9% | -2322 to -1066 | GAIN |
| response time (ms), 99th percentile | 7614 | 6158 | -19.1% | -2199 to -714.3 | GAIN |
| time over the response line (% of samples) | 68.3 | 66.53 | -2.6% | -3.182 to -0.3557 | GAIN |
| failed requests (%) | 48.28 | 52.82 | +9.4% | +1.718 to +7.373 | LOSS |
| HPA replicas, mean | 9.86 | 10.91 | +10.6% | +0.5375 to +1.553 | power given |
| pods started | 3.325 | 7.375 | +121.8% | +3.103 to +4.997 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.003758 to +0.001272 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 279.1 | 278.8 | -0.1% | -0.7842 to +0.02763 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 279.1 | 278.7 | -0.1% | -0.8512 to +0.01956 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.605 | 2.622 | +0.6% | +0.002713 to +0.03073 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 79.38 | 84.41 | +6.3% | +4.76 to +5.308 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | power given |
| organism behind its window (s) | 0.59 | 0.4275 | -27.5% | -0.2115 to -0.1135 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3407 | 2743 | -19.5% | -1294 to -34.77 | GAIN |
| response time (ms), 99th percentile | 5614 | 4823 | -14.1% | -1428 to -154.3 | GAIN |
| time over the response line (% of samples) | 52.58 | 51.16 | -2.7% | -2.754 to -0.09099 | GAIN |
| failed requests (%) | 38.4 | 41.08 | +7.0% | -0.1296 to +5.487 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.799 | 11.75 | +19.9% | +1.244 to +2.649 | power given |
| pods started | 4.2 | 8.4 | +100.0% | +2.86 to +5.54 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +1.595e-17 to +9.61e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276 | 276.1 | +0.0% | -0.4654 to +0.5629 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276 | 276.1 | +0.0% | -0.4654 to +0.5629 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.4 | 2.452 | +2.1% | +0.02781 to +0.07514 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.72 | 80.05 | +8.6% | +5.711 to +6.961 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | power given |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | power given |
| organism behind its window (s) | 0.74 | 0.4225 | -42.9% | -0.3763 to -0.2587 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4349 | 4128 | -5.1% | -946.1 to +504.6 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6727 | 6609 | -1.8% | -735.2 to +499.1 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 65.33 | 64.91 | -0.6% | -2.294 to +1.448 | STEADY, inside the noise (cut) |
| failed requests (%) | 50.05 | 51.93 | +3.8% | -0.9611 to +4.722 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.865 | 10.83 | +9.8% | +0.3688 to +1.558 | power given |
| pods started | 3.05 | 5.65 | +85.2% | +1.637 to +3.563 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | +3.824e-16 to +1.35e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 278.4 | 278.4 | -0.0% | -0.4571 to +0.3731 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 278.4 | 278.4 | -0.0% | -0.4571 to +0.3731 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.56 | 2.599 | +1.5% | +0.02211 to +0.05528 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.8 | 85.23 | +9.6% | +7.072 to +7.791 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | power given |
| organism behind its window (s) | 0.5 | 1.097 | +119.5% | +0.5282 to +0.6668 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
