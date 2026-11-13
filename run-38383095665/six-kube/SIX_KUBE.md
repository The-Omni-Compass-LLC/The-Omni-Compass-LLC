# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The whole tower, every muscle once, 100 copies: native | The whole tower, every muscle once, 100 copies: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 2610 | 3013 |
| response time (ms), 99th percentile | 4486 | 5113 |
| time over the response line (% of samples) | 51.48 | 45.98 |
| failed requests (%) | 32.71 | 32.92 |
| HPA replicas, mean | 9.832 | 9.815 |
| pods started | 5.211 | 5.289 |
| worker nodes in service, mean | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 470.2 | 466.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 470.2 | 466.1 |
| CPU used with Omni's own (cores), mean | 2.852 | 2.697 |
| host CPU busy, the real machine under kind (%) | 86.97 | 89.82 |
| organism work | 6.88e+12 | 6.88e+12 |
| organism energy (J) | 1.103e+15 | 1.103e+15 |
| organism time over the line (% of steps) | 2.589 | 2.551 |
| organism work per energy | 0.006235 | 0.006235 |
| organism behind its window (s) | 2.836 | 9.177 |

## Each organism: omni against native, paired by repetition

### The whole tower, every muscle once, 100 copies: better on 5, worse on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), inside the noise on 2; OFF THE CLOCK in 1 of 90 repetitions (the organism ended up to 167 s after its window: the machine could not step this many muscles in time, and the cell's last steps saw a cluster at rest)

90 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2610 | 3013 | +15.4% | +105.8 to +700.6 | WORSE |
| response time (ms), 99th percentile | 4486 | 5113 | +14.0% | +238.7 to +1016 | WORSE |
| time over the response line (% of samples) | 51.48 | 45.98 | -10.7% | -6.35 to -4.65 | better |
| failed requests (%) | 32.71 | 32.92 | +0.6% | -1.031 to +1.449 | WORSE (inside the noise) |
| HPA replicas, mean | 9.832 | 9.815 | -0.2% | -0.02511 to -0.007772 | better |
| pods started | 5.211 | 5.289 | +1.5% | -0.03904 to +0.1946 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.044e-16 to +3.61e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 470.2 | 466.1 | -0.9% | -4.783 to -3.317 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 470.2 | 466.1 | -0.9% | -4.783 to -3.317 | better |
| CPU used with Omni's own (cores), mean | 2.852 | 2.697 | -5.4% | -0.1805 to -0.1303 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 86.97 | 89.82 | +3.3% | +2.281 to +3.434 | shown, not judged (more or less is not better by itself) |
| organism work | 6.88e+12 | 6.88e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.103e+15 | 1.103e+15 | +0.0% | +8.697e+08 to +8.697e+08 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.589 | 2.551 | -1.5% | -0.03826 to -0.03826 | better |
| organism work per energy | 0.006235 | 0.006235 | -0.0% | -4.914e-09 to -4.914e-09 | same (under one part in a million) |
| organism behind its window (s) | 2.836 | 9.177 | +223.6% | +1.902 to +10.78 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- Distribution / Specialized
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
