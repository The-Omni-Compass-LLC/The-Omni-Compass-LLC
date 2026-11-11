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
| response time (ms), 95th percentile | 3245 | 5601 | 2937 | 4221 |
| response time (ms), 99th percentile | 6208 | 7423 | 5595 | 6882 |
| time over the response line (% of samples) | 51.05 | 50.08 | 42.9 | 44.61 |
| failed requests (%) | 27.97 | 30.3 | 21.74 | 25.66 |
| HPA replicas, mean | 9.737 | 13.27 | 9.73 | 12.95 |
| pods started | 3.667 | 10.5 | 3.833 | 9.167 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 185.7 | 186.8 | 184.6 | 184.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.7 | 186.8 | 184.6 | 184.5 |
| CPU used with Omni's own (cores), mean | 2.537 | 2.586 | 2.405 | 2.455 |
| host CPU busy, the real machine under kind (%) | 74.52 | 76.73 | 72.07 | 75.84 |
| organism work | 2.226e+11 | 2.226e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 5.689e+11 | 5.69e+11 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.574 | 2.478 | 2.61 | 2.524 |
| organism work per energy | 0.3913 | 0.3912 | 0.012 | 0.012 |
| organism behind its window (s) | 0.01667 | 0 | 0.15 | 0.15 |

## Each organism: omni against native, paired by repetition

### Distribution / Specialized, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

6 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3245 | 5601 | +72.6% | -238 to +4950 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 6208 | 7423 | +19.6% | -1537 to +3966 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 51.05 | 50.08 | -1.9% | -11.24 to +9.287 | STEADY, inside the noise (cut) |
| failed requests (%) | 27.97 | 30.3 | +8.3% | -0.6643 to +5.313 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.737 | 13.27 | +36.3% | +2.2 to +4.865 | power given |
| pods started | 3.667 | 10.5 | +186.4% | +5.606 to +8.06 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.329e-16 to +1.425e-15 | STEADY, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.7 | 186.8 | +0.6% | -0.8467 to +3.08 | STEADY, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.7 | 186.8 | +0.6% | -0.8467 to +3.08 | STEADY, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.537 | 2.586 | +1.9% | +0.04041 to +0.05662 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.52 | 76.73 | +3.0% | +1.617 to +2.803 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | power given |
| organism behind its window (s) | 0.01667 | 0 | -100.0% | -0.05952 to +0.02618 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 6

6 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2937 | 4221 | +43.7% | -1549 to +4118 | STEADY, inside the noise (up) |
| response time (ms), 99th percentile | 5595 | 6882 | +23.0% | -1511 to +4085 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 42.9 | 44.61 | +4.0% | -4.942 to +8.373 | STEADY, inside the noise (up) |
| failed requests (%) | 21.74 | 25.66 | +18.0% | -0.02307 to +7.864 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.73 | 12.95 | +33.1% | +0.5572 to +5.887 | power given |
| pods started | 3.833 | 9.167 | +139.1% | +3.619 to +7.047 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.179e-15 to +1.179e-15 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 184.6 | 184.5 | -0.1% | -1.135 to +0.9285 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.6 | 184.5 | -0.1% | -1.135 to +0.9285 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.405 | 2.455 | +2.0% | +0.02685 to +0.07167 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.07 | 75.84 | +5.2% | +3.044 to +4.516 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | power given |
| organism behind its window (s) | 0.15 | 0.15 | +0.0% | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The spine, the muscles every stack runs on
- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- The whole tower, every muscle once

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
