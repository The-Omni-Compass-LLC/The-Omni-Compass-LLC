# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The four stacked, duplicates kept, 100 copies: native | The four stacked, duplicates kept, 100 copies: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 2577 | 3940 |
| response time (ms), 99th percentile | 6226 | 7108 |
| time over the response line (% of samples) | 56.9 | 57.22 |
| failed requests (%) | 45.85 | 47.38 |
| HPA replicas, mean | 9.884 | 9.96 |
| pods started | 5.3 | 5.9 |
| worker nodes in service, mean | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 690.9 | 692.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 690.9 | 692.2 |
| CPU used with Omni's own (cores), mean | 2.502 | 2.538 |
| host CPU busy, the real machine under kind (%) | 77.37 | 86.79 |
| organism work | 1.316e+13 | 1.316e+13 |
| organism energy (J) | 1.108e+15 | 1.108e+15 |
| organism time over the line (% of steps) | 2.524 | 2.439 |
| organism work per energy | 0.01188 | 0.01188 |
| organism behind its window (s) | 3 | 3.74 |

## Each organism: omni against native, paired by repetition

### The four stacked, duplicates kept, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 1 (organism energy (J)), EVEN (inside the noise) on 8

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2577 | 3940 | +52.9% | -32.83 to +2760 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 6226 | 7108 | +14.2% | -159.1 to +1922 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 56.9 | 57.22 | +0.6% | -0.7829 to +1.436 | EVEN, inside the noise (up) |
| failed requests (%) | 45.85 | 47.38 | +3.3% | -0.1575 to +3.222 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.884 | 9.96 | +0.8% | -0.1581 to +0.3112 | EVEN, inside the noise (up) |
| pods started | 5.3 | 5.9 | +11.3% | -0.7985 to +1.998 | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.087e-17 to +1.147e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 690.9 | 692.2 | +0.2% | -0.1975 to +2.746 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 690.9 | 692.2 | +0.2% | -0.1975 to +2.746 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.502 | 2.538 | +1.4% | +0.002122 to +0.06984 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.37 | 86.79 | +12.2% | +8.619 to +10.23 | shown, not judged |
| organism work | 1.316e+13 | 1.316e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+15 | 1.108e+15 | +0.0% | +3.476e+09 to +3.476e+09 | power given |
| organism time over the line (% of steps) | 2.524 | 2.439 | -3.4% | -0.08471 to -0.08471 | GAIN |
| organism work per energy | 0.01188 | 0.01188 | -0.0% | -3.73e-08 to -3.73e-08 | LOSS |
| organism behind its window (s) | 3 | 3.74 | +24.7% | +0.4987 to +0.9813 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- Distribution / Specialized
- The whole tower, every muscle once

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
