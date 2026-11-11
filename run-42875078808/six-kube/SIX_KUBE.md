# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2590 | 3291 | 3190 | 3680 | 2920 | 4406 | 2441 | 3263 |
| response time (ms), 99th percentile | 4869 | 5871 | 5865 | 6311 | 5809 | 6794 | 4578 | 5660 |
| time over the response line (% of samples) | 36.57 | 33.45 | 41.56 | 39.97 | 46.08 | 43.56 | 38.48 | 39.91 |
| failed requests (%) | 15.93 | 16.42 | 26.62 | 26.17 | 26.21 | 25.86 | 18.12 | 21.74 |
| HPA replicas, mean | 9.641 | 13.87 | 9.634 | 14.36 | 9.686 | 13.54 | 9.682 | 13.1 |
| pods started | 5.21 | 11.03 | 4.968 | 10.97 | 4.758 | 10.48 | 4.597 | 9.887 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 184.3 | 184.4 | 184.2 | 184.8 | 185.3 | 184.1 | 184.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 184.3 | 184.4 | 184.2 | 184.8 | 185.3 | 184.1 | 184.2 |
| CPU used with Omni's own (cores), mean | 2.366 | 2.417 | 2.388 | 2.437 | 2.449 | 2.497 | 2.345 | 2.408 |
| host CPU busy, the real machine under kind (%) | 69.26 | 71.54 | 70.57 | 72.55 | 71.61 | 73.79 | 70.31 | 74.79 |
| organism work | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 2.226e+11 | 2.226e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 5.689e+11 | 5.69e+11 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.018 | 1.945 | 4.802 | 4.711 | 2.574 | 2.478 | 2.61 | 2.524 |
| organism work per energy | 1.377 | 1.376 | 1.123 | 1.123 | 0.3913 | 0.3912 | 0.012 | 0.012 |
| organism behind its window (s) | 0.0129 | 0.009677 | 0.01129 | 0.003226 | 0.009677 | 0.0129 | 0.1613 | 0.1677 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2590 | 3291 | +27.1% | +345.4 to +1057 | LOSS |
| response time (ms), 99th percentile | 4869 | 5871 | +20.6% | +583.6 to +1420 | LOSS |
| time over the response line (% of samples) | 36.57 | 33.45 | -8.5% | -4.05 to -2.183 | GAIN |
| failed requests (%) | 15.93 | 16.42 | +3.1% | -0.04112 to +1.035 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.641 | 13.87 | +43.9% | +3.827 to +4.638 | power given |
| pods started | 5.21 | 11.03 | +111.8% | +5.385 to +6.26 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.956e-16 to -2.791e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 184.3 | +0.2% | -0.09781 to +0.6588 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 184.3 | +0.2% | -0.09781 to +0.6588 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.366 | 2.417 | +2.2% | +0.04516 to +0.05787 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.26 | 71.54 | +3.3% | +2.072 to +2.484 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | power given |
| organism behind its window (s) | 0.0129 | 0.009677 | -25.0% | -0.01446 to +0.00801 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3190 | 3680 | +15.4% | -123.3 to +1104 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5865 | 6311 | +7.6% | -19.51 to +911.1 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 41.56 | 39.97 | -3.8% | -2.424 to -0.7618 | GAIN |
| failed requests (%) | 26.62 | 26.17 | -1.7% | -1.251 to +0.3656 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.634 | 14.36 | +49.0% | +4.559 to +4.888 | power given |
| pods started | 4.968 | 10.97 | +120.8% | +5.675 to +6.325 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.412e-16 to -1.776e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184.2 | -0.1% | -0.6738 to +0.2232 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184.2 | -0.1% | -0.6738 to +0.2232 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.388 | 2.437 | +2.1% | +0.03884 to +0.05936 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.57 | 72.55 | +2.8% | +1.687 to +2.281 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | power given |
| organism behind its window (s) | 0.01129 | 0.003226 | -71.4% | -0.0176 to +0.001471 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 1

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2920 | 4406 | +50.9% | +863.5 to +2109 | LOSS |
| response time (ms), 99th percentile | 5809 | 6794 | +17.0% | +446.4 to +1524 | LOSS |
| time over the response line (% of samples) | 46.08 | 43.56 | -5.5% | -3.684 to -1.372 | GAIN |
| failed requests (%) | 26.21 | 25.86 | -1.3% | -1.498 to +0.8062 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.686 | 13.54 | +39.8% | +3.5 to +4.201 | power given |
| pods started | 4.758 | 10.48 | +120.3% | +5.239 to +6.213 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.708e-16 to +8.369e-17 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.8 | 185.3 | +0.3% | +0.1387 to +0.896 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.8 | 185.3 | +0.3% | +0.1387 to +0.896 | power given |
| CPU used with Omni's own (cores), mean | 2.449 | 2.497 | +2.0% | +0.04386 to +0.05377 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.61 | 73.79 | +3.0% | +2.063 to +2.299 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.009677 | 0.0129 | +33.3% | -0.00801 to +0.01446 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2441 | 3263 | +33.7% | +497.2 to +1147 | LOSS |
| response time (ms), 99th percentile | 4578 | 5660 | +23.6% | +559.6 to +1605 | LOSS |
| time over the response line (% of samples) | 38.48 | 39.91 | +3.7% | -0.05814 to +2.915 | STEADY, inside the noise (up) |
| failed requests (%) | 18.12 | 21.74 | +20.0% | +2.234 to +4.999 | LOSS |
| HPA replicas, mean | 9.682 | 13.1 | +35.3% | +2.822 to +4.013 | power given |
| pods started | 4.597 | 9.887 | +115.1% | +4.704 to +5.876 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.674e-16 to +1.522e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 184.2 | +0.1% | -0.1428 to +0.449 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.2 | +0.1% | -0.1428 to +0.449 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.345 | 2.408 | +2.7% | +0.055 to +0.07144 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.31 | 74.79 | +6.4% | +4.265 to +4.699 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.1613 | 0.1677 | +4.0% | -0.01353 to +0.02643 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The spine, the muscles every stack runs on
- Energy / Facility / Industrial
- The whole tower, every muscle once

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
