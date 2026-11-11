# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2727 | 3543 | 2466 | 3394 |
| response time (ms), 99th percentile | 5483 | 6062 | 4531 | 5423 |
| time over the response line (% of samples) | 45.23 | 41.63 | 38.49 | 40.04 |
| failed requests (%) | 26.38 | 27.22 | 18.5 | 22.23 |
| HPA replicas, mean | 9.663 | 13.08 | 9.695 | 12.73 |
| pods started | 4.856 | 10.28 | 4.352 | 9.568 |
| worker nodes in service, mean | 6 | 6 | 5.999 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 184.7 | 183.8 | 183.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.7 | 183.8 | 183.8 |
| CPU used with Omni's own (cores), mean | 2.403 | 2.448 | 2.344 | 2.388 |
| host CPU busy, the real machine under kind (%) | 70.51 | 72.65 | 70.29 | 74.18 |
| organism work | 2.226e+11 | 2.226e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 5.689e+11 | 5.69e+11 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.574 | 2.478 | 2.61 | 2.524 |
| organism work per energy | 0.3913 | 0.3912 | 0.012 | 0.012 |
| organism behind its window (s) | 0.0072 | 0.0112 | 0.156 | 0.1776 |

## Each organism: omni against native, paired by repetition

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 6 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J); organism work per energy), STEADY (inside the noise) on 0

125 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2727 | 3543 | +29.9% | +462.8 to +1168 | LOSS |
| response time (ms), 99th percentile | 5483 | 6062 | +10.6% | +234.5 to +922.9 | LOSS |
| time over the response line (% of samples) | 45.23 | 41.63 | -8.0% | -4.408 to -2.806 | GAIN |
| failed requests (%) | 26.38 | 27.22 | +3.2% | +0.1129 to +1.553 | LOSS |
| HPA replicas, mean | 9.663 | 13.08 | +35.3% | +3.09 to +3.736 | power given |
| pods started | 4.856 | 10.28 | +111.7% | +5.038 to +5.81 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.59e-16 to +1.174e-16 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 184.7 | +0.3% | +0.3292 to +0.8501 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.7 | +0.3% | +0.3292 to +0.8501 | power given |
| CPU used with Omni's own (cores), mean | 2.403 | 2.448 | +1.9% | +0.03906 to +0.04996 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.51 | 72.65 | +3.0% | +1.985 to +2.298 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.0072 | 0.0112 | +55.6% | -0.00359 to +0.01159 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 3

125 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2466 | 3394 | +37.6% | +701.9 to +1153 | LOSS |
| response time (ms), 99th percentile | 4531 | 5423 | +19.7% | +574 to +1210 | LOSS |
| time over the response line (% of samples) | 38.49 | 40.04 | +4.0% | +0.5846 to +2.519 | LOSS |
| failed requests (%) | 18.5 | 22.23 | +20.1% | +3.019 to +4.432 | LOSS |
| HPA replicas, mean | 9.695 | 12.73 | +31.3% | +2.639 to +3.439 | power given |
| pods started | 4.352 | 9.568 | +119.9% | +4.794 to +5.638 | power given |
| worker nodes in service, mean | 5.999 | 6 | +0.0% | -0.0007661 to +0.002331 | STEADY, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.8 | 183.8 | +0.0% | -0.2089 to +0.25 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.8 | 183.8 | +0.0% | -0.2011 to +0.2735 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.344 | 2.388 | +1.9% | +0.03722 to +0.05141 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.29 | 74.18 | +5.5% | +3.658 to +4.119 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.156 | 0.1776 | +13.8% | +0.008003 to +0.0352 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The spine, the muscles every stack runs on
- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- The whole tower, every muscle once

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
