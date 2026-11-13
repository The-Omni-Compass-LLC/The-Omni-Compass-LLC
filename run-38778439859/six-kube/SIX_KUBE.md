# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 2676 | 3564 |
| response time (ms), 99th percentile | 5708 | 5399 |
| time over the response line (% of samples) | 53.52 | 50.53 |
| failed requests (%) | 36.17 | 36.47 |
| HPA replicas, mean | 9.69 | 13.73 |
| pods started | 4.75 | 9.25 |
| worker nodes in service, mean | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 184.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 184.7 |
| CPU used with Omni's own (cores), mean | 2.367 | 2.403 |
| host CPU busy, the real machine under kind (%) | 69.83 | 71.95 |
| organism work | 2.226e+11 | 2.226e+11 |
| organism energy (J) | 5.689e+11 | 5.69e+11 |
| organism time over the line (% of steps) | 2.574 | 2.478 |
| organism work per energy | 0.3913 | 0.3912 |
| organism behind its window (s) | 0 | 0.0125 |

## Each organism: omni against native, paired by repetition

### Distribution / Specialized, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 6

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2676 | 3564 | +33.2% | -496.2 to +2272 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5708 | 5399 | -5.4% | -1984 to +1368 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 53.52 | 50.53 | -5.6% | -9.839 to +3.861 | EVEN, inside the noise (cut) |
| failed requests (%) | 36.17 | 36.47 | +0.8% | -3.923 to +4.519 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.69 | 13.73 | +41.7% | +1.974 to +6.115 | power given |
| pods started | 4.75 | 9.25 | +94.7% | +2.093 to +6.907 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.635e-15 to +7.468e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 184.7 | +0.4% | -0.5103 to +1.876 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 184.7 | +0.4% | -0.5103 to +1.876 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.367 | 2.403 | +1.5% | -0.003087 to +0.07577 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.83 | 71.95 | +3.0% | +1.101 to +3.137 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | LOSS |
| organism behind its window (s) | 0 | 0.0125 | +0.0125 | -0.01706 to +0.04206 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
