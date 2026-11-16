# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 319.8 | 184.8 |
| response time (ms), 99th percentile | 527.5 | 387.9 |
| time over the response line (% of samples) | 1.496 | 0.6818 |
| failed requests (%) | 0 | 0 |
| HPA replicas, mean | 9.624 | 13.94 |
| pods started | 7 | 18 |
| worker nodes in service, mean | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 266.6 | 269.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 266.6 | 269.4 |
| CPU used with Omni's own (cores), mean | 1.815 | 1.903 |
| host CPU busy, the real machine under kind (%) | 55.31 | 61.11 |
| organism work | 2.214e+12 | 2.214e+12 |
| organism energy (J) | 1.98e+12 | 1.981e+12 |
| organism time over the line (% of steps) | 4.564 | 4.47 |
| organism work per energy | 1.118 | 1.117 |
| organism behind its window (s) | 0.5 | 0.3 |

## Each organism: omni against native, paired by repetition

### Physics / Robotics / Autonomous, 100 copies: ONE REPETITION

1 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 319.8 | 184.8 | -42.2% |  | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 527.5 | 387.9 | -26.5% |  | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 1.496 | 0.6818 | -54.4% |  | EVEN, inside the noise (cut) |
| failed requests (%) | 0 | 0 | +0 |  | EVEN, the same |
| HPA replicas, mean | 9.624 | 13.94 | +44.8% |  | EVEN, inside the noise (up) |
| pods started | 7 | 18 | +157.1% |  | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | +0.0% |  | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 266.6 | 269.4 | +1.1% |  | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 266.6 | 269.4 | +1.1% |  | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.815 | 1.903 | +4.8% |  | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.31 | 61.11 | +10.5% |  | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% |  | EVEN, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% |  | EVEN, inside the noise (up) |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% |  | EVEN, inside the noise (cut) |
| organism work per energy | 1.118 | 1.117 | -0.0% |  | EVEN, inside the noise (cut) |
| organism behind its window (s) | 0.5 | 0.3 | -40.0% |  | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Energy / Facility / Industrial
- Distribution / Specialized
- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
