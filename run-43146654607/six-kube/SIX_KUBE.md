# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads STEADY, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The whole tower, every muscle once, 100 copies: native | The whole tower, every muscle once, 100 copies: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 3405 | 3911 |
| response time (ms), 99th percentile | 6046 | 6135 |
| time over the response line (% of samples) | 53.63 | 55.42 |
| failed requests (%) | 38.39 | 38.62 |
| HPA replicas, mean | 9.818 | 12.28 |
| pods started | 5.5 | 9.684 |
| worker nodes in service, mean | 6 | 5.999 |
| energy, parked workers still on at idle power (Wh, declared model) | 460.6 | 460.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 460.6 | 460.4 |
| CPU used with Omni's own (cores), mean | 2.47 | 2.508 |
| host CPU busy, the real machine under kind (%) | 77.03 | 85.44 |
| organism work | 6.88e+12 | 6.88e+12 |
| organism energy (J) | 1.103e+15 | 1.103e+15 |
| organism time over the line (% of steps) | 2.589 | 2.551 |
| organism work per energy | 0.006235 | 0.006235 |
| organism behind its window (s) | 1.799 | 2.247 |

## Each organism: omni against native, paired by repetition

### The whole tower, every muscle once, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; time over the response line (% of samples)), power given on 4 (HPA replicas, mean; pods started; organism energy (J); organism work per energy), STEADY (inside the noise) on 5

250 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3405 | 3911 | +14.8% | +158.1 to +853.1 | LOSS |
| response time (ms), 99th percentile | 6046 | 6135 | +1.5% | -182.4 to +360.8 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 53.63 | 55.42 | +3.3% | +1.132 to +2.443 | LOSS |
| failed requests (%) | 38.39 | 38.62 | +0.6% | -1.403 to +1.864 | STEADY, inside the noise (up) |
| HPA replicas, mean | 9.818 | 12.28 | +25.1% | +2.211 to +2.713 | power given |
| pods started | 5.5 | 9.684 | +76.1% | +3.909 to +4.459 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001683 to +0.0005497 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 460.6 | 460.5 | -0.0% | -0.4095 to +0.1651 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 460.6 | 460.4 | -0.0% | -0.4465 to +0.145 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.47 | 2.508 | +1.6% | +0.02939 to +0.04797 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.03 | 85.44 | +10.9% | +8.176 to +8.63 | shown, not judged |
| organism work | 6.88e+12 | 6.88e+12 | +0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 1.103e+15 | 1.103e+15 | +0.0% | +8.697e+08 to +8.697e+08 | power given |
| organism time over the line (% of steps) | 2.589 | 2.551 | -1.5% | -0.03826 to -0.03826 | GAIN |
| organism work per energy | 0.006235 | 0.006235 | -0.0% | -4.914e-09 to -4.914e-09 | power given |
| organism behind its window (s) | 1.799 | 2.247 | +24.9% | +0.4161 to +0.4799 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The spine, the muscles every stack runs on
- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- Distribution / Specialized
- The four stacked, duplicates kept

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
