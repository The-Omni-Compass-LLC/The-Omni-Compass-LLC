# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The whole tower, every muscle once, 100 copies: native | The whole tower, every muscle once, 100 copies: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 2508 | 2394 |
| response time (ms), 99th percentile | 4116 | 4671 |
| time over the response line (% of samples) | 46.88 | 41.85 |
| failed requests (%) | 26.75 | 27.79 |
| HPA replicas, mean | 9.823 | 9.817 |
| pods started | 5.3 | 5.5 |
| worker nodes in service, mean | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 470.2 | 466.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 470.2 | 466.5 |
| CPU used with Omni's own (cores), mean | 2.845 | 2.718 |
| host CPU busy, the real machine under kind (%) | 86.38 | 90.11 |
| organism work | 6.88e+12 | 6.88e+12 |
| organism energy (J) | 1.103e+15 | 1.103e+15 |
| organism time over the line (% of steps) | 2.589 | 2.551 |
| organism work per energy | 0.006235 | 0.006235 |
| organism behind its window (s) | 2.56 | 3.06 |

## Each organism: omni against native, paired by repetition

### The whole tower, every muscle once, 100 copies: better on 4, worse on 0, inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2508 | 2394 | -4.5% | -1056 to +827.8 | better (inside the noise) |
| response time (ms), 99th percentile | 4116 | 4671 | +13.5% | -420.2 to +1531 | WORSE (inside the noise) |
| time over the response line (% of samples) | 46.88 | 41.85 | -10.7% | -7.144 to -2.921 | better |
| failed requests (%) | 26.75 | 27.79 | +3.9% | -2.073 to +4.149 | WORSE (inside the noise) |
| HPA replicas, mean | 9.823 | 9.817 | -0.1% | -0.01663 to +0.004751 | better (inside the noise) |
| pods started | 5.3 | 5.5 | +3.8% | -0.1016 to +0.5016 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.057e-15 to +8.793e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 470.2 | 466.5 | -0.8% | -6.511 to -0.8246 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 470.2 | 466.5 | -0.8% | -6.511 to -0.8246 | better |
| CPU used with Omni's own (cores), mean | 2.845 | 2.718 | -4.5% | -0.2303 to -0.02406 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 86.38 | 90.11 | +4.3% | +1.483 to +5.974 | shown, not judged (more or less is not better by itself) |
| organism work | 6.88e+12 | 6.88e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.103e+15 | 1.103e+15 | +0.0% | +8.697e+08 to +8.697e+08 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.589 | 2.551 | -1.5% | -0.03826 to -0.03826 | better |
| organism work per energy | 0.006235 | 0.006235 | -0.0% | -4.914e-09 to -4.914e-09 | same (under one part in a million) |
| organism behind its window (s) | 2.56 | 3.06 | +19.5% | +0.08427 to +0.9157 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- Distribution / Specialized
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
