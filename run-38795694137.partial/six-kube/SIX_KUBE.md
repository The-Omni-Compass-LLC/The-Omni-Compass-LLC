# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The four stacked, duplicates kept, 100 copies: native | The four stacked, duplicates kept, 100 copies: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 2160 | 4174 |
| response time (ms), 99th percentile | 4945 | 6516 |
| time over the response line (% of samples) | 55.21 | 55.46 |
| failed requests (%) | 45.15 | 44.6 |
| HPA replicas, mean | 9.886 | 10.15 |
| pods started | 5.433 | 6.089 |
| worker nodes in service, mean | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 689.4 | 690.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 689.4 | 690.7 |
| CPU used with Omni's own (cores), mean | 2.455 | 2.498 |
| host CPU busy, the real machine under kind (%) | 76.66 | 86.19 |
| organism work | 1.316e+13 | 1.316e+13 |
| organism energy (J) | 1.108e+15 | 1.108e+15 |
| organism time over the line (% of steps) | 2.524 | 2.439 |
| organism work per energy | 0.01188 | 0.01188 |
| organism behind its window (s) | 2.92 | 3.782 |

## Each organism: omni against native, paired by repetition

### The four stacked, duplicates kept, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism work per energy), power given on 5 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J)), EVEN (inside the noise) on 2

90 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2160 | 4174 | +93.3% | +1593 to +2435 | LOSS |
| response time (ms), 99th percentile | 4945 | 6516 | +31.8% | +1167 to +1974 | LOSS |
| time over the response line (% of samples) | 55.21 | 55.46 | +0.5% | -0.2675 to +0.7684 | EVEN, inside the noise (up) |
| failed requests (%) | 45.15 | 44.6 | -1.2% | -1.454 to +0.3579 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.886 | 10.15 | +2.7% | +0.05648 to +0.4817 | power given |
| pods started | 5.433 | 6.089 | +12.1% | +0.2735 to +1.038 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.531e-16 to +2.136e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 689.4 | 690.7 | +0.2% | +0.8195 to +1.843 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 689.4 | 690.7 | +0.2% | +0.8195 to +1.843 | power given |
| CPU used with Omni's own (cores), mean | 2.455 | 2.498 | +1.7% | +0.0307 to +0.05481 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.66 | 86.19 | +12.4% | +9.214 to +9.84 | shown, not judged |
| organism work | 1.316e+13 | 1.316e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+15 | 1.108e+15 | +0.0% | +3.476e+09 to +3.476e+09 | power given |
| organism time over the line (% of steps) | 2.524 | 2.439 | -3.4% | -0.08471 to -0.08471 | GAIN |
| organism work per energy | 0.01188 | 0.01188 | -0.0% | -3.73e-08 to -3.73e-08 | LOSS |
| organism behind its window (s) | 2.92 | 3.782 | +29.5% | +0.7601 to +0.9644 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- Distribution / Specialized
- The whole tower, every muscle once

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
