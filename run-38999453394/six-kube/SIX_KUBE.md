# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The whole tower, every muscle once, 100 copies: native | The whole tower, every muscle once, 100 copies: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 2559 | 3651 |
| response time (ms), 99th percentile | 5073 | 5863 |
| time over the response line (% of samples) | 57.25 | 56.14 |
| failed requests (%) | 47.63 | 46.31 |
| HPA replicas, mean | 9.828 | 10.23 |
| pods started | 5.311 | 5.856 |
| worker nodes in service, mean | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 460.4 | 461 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 460.4 | 461 |
| CPU used with Omni's own (cores), mean | 2.456 | 2.494 |
| host CPU busy, the real machine under kind (%) | 77.03 | 84.66 |
| organism work | 6.88e+12 | 6.88e+12 |
| organism energy (J) | 1.103e+15 | 1.103e+15 |
| organism time over the line (% of steps) | 2.589 | 2.551 |
| organism work per energy | 0.006235 | 0.006235 |
| organism behind its window (s) | 1.747 | 2.139 |

## Each organism: omni against native, paired by repetition

### The whole tower, every muscle once, 100 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 4 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this)), EVEN (inside the noise) on 1

90 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2559 | 3651 | +42.7% | +723.4 to +1462 | LOSS |
| response time (ms), 99th percentile | 5073 | 5863 | +15.6% | +348.2 to +1231 | LOSS |
| time over the response line (% of samples) | 57.25 | 56.14 | -1.9% | -1.603 to -0.6098 | GAIN |
| failed requests (%) | 47.63 | 46.31 | -2.8% | -1.885 to -0.7529 | GAIN |
| HPA replicas, mean | 9.828 | 10.23 | +4.1% | +0.1525 to +0.6479 | power given |
| pods started | 5.311 | 5.856 | +10.3% | +0.1897 to +0.8991 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -0.0004437 to +0.001368 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 460.4 | 461 | +0.1% | +0.23 to +0.978 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 460.4 | 461 | +0.1% | +0.2486 to +1.006 | power given |
| CPU used with Omni's own (cores), mean | 2.456 | 2.494 | +1.6% | +0.02893 to +0.0473 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.03 | 84.66 | +9.9% | +7.429 to +7.843 | shown, not judged |
| organism work | 6.88e+12 | 6.88e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+15 | 1.103e+15 | +0.0% | +8.697e+08 to +8.697e+08 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.589 | 2.551 | -1.5% | -0.03826 to -0.03826 | GAIN |
| organism work per energy | 0.006235 | 0.006235 | -0.0% | -4.914e-09 to -4.914e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 1.747 | 2.139 | +22.5% | +0.3054 to +0.479 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- Distribution / Specialized
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
