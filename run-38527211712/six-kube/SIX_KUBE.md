# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The four stacked, duplicates kept, 100 copies: native | The four stacked, duplicates kept, 100 copies: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 2304 | 4191 |
| response time (ms), 99th percentile | 5364 | 6548 |
| time over the response line (% of samples) | 55.37 | 56.46 |
| failed requests (%) | 44.02 | 44.74 |
| HPA replicas, mean | 9.885 | 14.67 |
| pods started | 5.411 | 10.84 |
| worker nodes in service, mean | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 690.7 | 691.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 690.6 | 691.4 |
| CPU used with Omni's own (cores), mean | 2.485 | 2.531 |
| host CPU busy, the real machine under kind (%) | 77.08 | 86.94 |
| organism work | 1.316e+13 | 1.316e+13 |
| organism energy (J) | 1.108e+15 | 1.108e+15 |
| organism time over the line (% of steps) | 2.524 | 2.439 |
| organism work per energy | 0.01188 | 0.01188 |
| organism behind its window (s) | 2.893 | 3.852 |

## Each organism: omni against native, paired by repetition

### The four stacked, duplicates kept, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 3

90 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2304 | 4191 | +81.9% | +1476 to +2297 | LOSS |
| response time (ms), 99th percentile | 5364 | 6548 | +22.1% | +808 to +1559 | LOSS |
| time over the response line (% of samples) | 55.37 | 56.46 | +2.0% | +0.5015 to +1.68 | LOSS |
| failed requests (%) | 44.02 | 44.74 | +1.6% | -0.07792 to +1.517 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.885 | 14.67 | +48.4% | +4.389 to +5.182 | power given |
| pods started | 5.411 | 10.84 | +100.4% | +5.046 to +5.82 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -0.0007849 to +0.0007902 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 690.7 | 691.4 | +0.1% | -0.17 to +1.606 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 690.6 | 691.4 | +0.1% | -0.1811 to +1.617 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.485 | 2.531 | +1.8% | +0.03434 to +0.05684 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.08 | 86.94 | +12.8% | +9.609 to +10.11 | shown, not judged |
| organism work | 1.316e+13 | 1.316e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+15 | 1.108e+15 | +0.0% | +3.476e+09 to +3.476e+09 | power given |
| organism time over the line (% of steps) | 2.524 | 2.439 | -3.4% | -0.08471 to -0.08471 | GAIN |
| organism work per energy | 0.01188 | 0.01188 | -0.0% | -3.73e-08 to -3.73e-08 | LOSS |
| organism behind its window (s) | 2.893 | 3.852 | +33.1% | +0.8559 to +1.062 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- Distribution / Specialized
- The whole tower, every muscle once

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
