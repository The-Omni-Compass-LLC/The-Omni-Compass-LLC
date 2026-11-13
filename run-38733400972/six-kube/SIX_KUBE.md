# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The four stacked, duplicates kept, 100 copies: native | The four stacked, duplicates kept, 100 copies: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 1966 | 4340 |
| response time (ms), 99th percentile | 5213 | 7087 |
| time over the response line (% of samples) | 61.94 | 60.79 |
| failed requests (%) | 49.87 | 48.27 |
| HPA replicas, mean | 9.895 | 9.876 |
| pods started | 5.2 | 5.1 |
| worker nodes in service, mean | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 693.4 | 694.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 693.4 | 694.5 |
| CPU used with Omni's own (cores), mean | 2.562 | 2.599 |
| host CPU busy, the real machine under kind (%) | 79.59 | 89.43 |
| organism work | 1.316e+13 | 1.316e+13 |
| organism energy (J) | 1.108e+15 | 1.108e+15 |
| organism time over the line (% of steps) | 2.524 | 2.439 |
| organism work per energy | 0.01188 | 0.01188 |
| organism behind its window (s) | 3.23 | 3.96 |

## Each organism: omni against native, paired by repetition

### The four stacked, duplicates kept, 100 copies: GAIN on 2 (HPA replicas, mean; organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; organism work per energy), power given on 1 (organism energy (J)), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1966 | 4340 | +120.8% | +767.9 to +3980 | LOSS |
| response time (ms), 99th percentile | 5213 | 7087 | +36.0% | -228.7 to +3978 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 61.94 | 60.79 | -1.9% | -2.885 to +0.5859 | EVEN, inside the noise (cut) |
| failed requests (%) | 49.87 | 48.27 | -3.2% | -4.869 to +1.67 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.895 | 9.876 | -0.2% | -0.02929 to -0.008467 | GAIN |
| pods started | 5.2 | 5.1 | -1.9% | -0.3262 to +0.1262 | EVEN, inside the noise (cut) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.063e-16 to +7.286e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 693.4 | 694.5 | +0.1% | -1.031 to +3.107 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 693.4 | 694.5 | +0.1% | -1.031 to +3.107 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.562 | 2.599 | +1.4% | +0.0009645 to +0.07277 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 79.59 | 89.43 | +12.4% | +8.578 to +11.1 | shown, not judged |
| organism work | 1.316e+13 | 1.316e+13 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+15 | 1.108e+15 | +0.0% | +3.476e+09 to +3.476e+09 | power given |
| organism time over the line (% of steps) | 2.524 | 2.439 | -3.4% | -0.08471 to -0.08471 | GAIN |
| organism work per energy | 0.01188 | 0.01188 | -0.0% | -3.73e-08 to -3.73e-08 | LOSS |
| organism behind its window (s) | 3.23 | 3.96 | +22.6% | +0.4209 to +1.039 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- Distribution / Specialized
- The whole tower, every muscle once

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
