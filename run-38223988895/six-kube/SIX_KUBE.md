# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The four stacked, duplicates kept, 100 copies: native | The four stacked, duplicates kept, 100 copies: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 2124 | 2664 |
| response time (ms), 99th percentile | 4602 | 4650 |
| time over the response line (% of samples) | 54.54 | 44.44 |
| failed requests (%) | 40.68 | 33.51 |
| HPA replicas, mean | 9.883 | 9.862 |
| pods started | 5.5 | 5.5 |
| worker nodes in service, mean | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 706.6 | 697.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 706.6 | 697.6 |
| CPU used with Omni's own (cores), mean | 2.897 | 2.516 |
| host CPU busy, the real machine under kind (%) | 88.13 | 89.08 |
| organism work | 1.316e+13 | 1.316e+13 |
| organism energy (J) | 1.108e+15 | 1.108e+15 |
| organism time over the line (% of steps) | 2.53 | 2.523 |
| organism work per energy | 0.01188 | 0.01188 |
| organism behind its window (s) | 4.58 | 59.39 |

## Each organism: omni against native, paired by repetition

### The four stacked, duplicates kept, 100 copies: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5; OFF THE CLOCK in 1 of 8 repetitions (the organism ended up to 206 s after its window: the machine could not step this many muscles in time, and the cell's last steps saw a cluster at rest)

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1714 | 2664 | +55.4% | -137.5 to +2038 | WORSE (inside the noise) |
| response time (ms), 99th percentile | 4360 | 4650 | +6.6% | -807.4 to +1387 | WORSE (inside the noise) |
| time over the response line (% of samples) | 48.11 | 44.44 | -7.6% | -5.692 to -1.654 | better |
| failed requests (%) | 34.14 | 33.51 | -1.8% | -2.024 to +0.7652 | better (inside the noise) |
| HPA replicas, mean | 9.877 | 9.862 | -0.1% | -0.03022 to +0.001682 | better (inside the noise) |
| pods started | 5.75 | 5.5 | -4.3% | -0.6371 to +0.1371 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.858e-16 to +1.618e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 703.5 | 697.6 | -0.8% | -10.37 to -1.466 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 703.5 | 697.6 | -0.8% | -10.37 to -1.466 | better |
| CPU used with Omni's own (cores), mean | 2.638 | 2.516 | -4.6% | -0.2856 to +0.04143 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 85.52 | 89.08 | +4.2% | +0.7662 to +6.358 | shown, not judged (more or less is not better by itself) |
| organism work | 1.316e+13 | 1.316e+13 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.108e+15 | 1.108e+15 | +0.0% | +4.207e+09 to +4.207e+09 | WORSE |
| organism time over the line (% of steps) | 2.53 | 2.523 | -0.3% | -0.007321 to -0.007321 | better |
| organism work per energy | 0.01188 | 0.01188 | -0.0% | -4.513e-08 to -4.513e-08 | WORSE |
| organism behind its window (s) | 4.425 | 59.39 | +1242.1% | -11.04 to +121 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- Distribution / Specialized
- The whole tower, every muscle once

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
