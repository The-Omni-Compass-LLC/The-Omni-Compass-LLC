# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The four stacked, duplicates kept, 100 copies: native | The four stacked, duplicates kept, 100 copies: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 2756 | 4110 |
| response time (ms), 99th percentile | 5460 | 6589 |
| time over the response line (% of samples) | 61.24 | 56.72 |
| failed requests (%) | 44.25 | 43.82 |
| HPA replicas, mean | 9.896 | 9.864 |
| pods started | 5.067 | 5.044 |
| worker nodes in service, mean | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 709.3 | 701 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 709.3 | 701 |
| CPU used with Omni's own (cores), mean | 2.984 | 2.771 |
| host CPU busy, the real machine under kind (%) | 90.63 | 93.28 |
| organism work | 1.316e+13 | 1.316e+13 |
| organism energy (J) | 1.108e+15 | 1.108e+15 |
| organism time over the line (% of steps) | 2.524 | 2.439 |
| organism work per energy | 0.01188 | 0.01188 |
| organism behind its window (s) | 4.652 | 215.6 |

## Each organism: omni against native, paired by repetition

### The four stacked, duplicates kept, 100 copies: better on 5, worse on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism energy (J); organism work per energy), inside the noise on 2; OFF THE CLOCK in 47 of 90 repetitions (the organism ended up to 635 s after its window: the machine could not step this many muscles in time, and the cell's last steps saw a cluster at rest)

90 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2756 | 4110 | +49.1% | +1052 to +1657 | WORSE |
| response time (ms), 99th percentile | 5460 | 6589 | +20.7% | +795 to +1462 | WORSE |
| time over the response line (% of samples) | 61.24 | 56.72 | -7.4% | -5.519 to -3.536 | better |
| failed requests (%) | 44.25 | 43.82 | -1.0% | -1.448 to +0.5896 | better (inside the noise) |
| HPA replicas, mean | 9.896 | 9.864 | -0.3% | -0.04093 to -0.02367 | better |
| pods started | 5.067 | 5.044 | -0.4% | -0.1248 to +0.08039 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | +2.234e-16 to +6.845e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 709.3 | 701 | -1.2% | -9.494 to -7.203 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 709.3 | 701 | -1.2% | -9.494 to -7.203 | better |
| CPU used with Omni's own (cores), mean | 2.984 | 2.771 | -7.2% | -0.2425 to -0.1848 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 90.63 | 93.28 | +2.9% | +1.921 to +3.374 | shown, not judged (more or less is not better by itself) |
| organism work | 1.316e+13 | 1.316e+13 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.108e+15 | 1.108e+15 | +0.0% | +3.476e+09 to +3.476e+09 | WORSE |
| organism time over the line (% of steps) | 2.524 | 2.439 | -3.4% | -0.08471 to -0.08471 | better |
| organism work per energy | 0.01188 | 0.01188 | -0.0% | -3.73e-08 to -3.73e-08 | WORSE |
| organism behind its window (s) | 4.652 | 215.6 | +4535.4% | +171.6 to +250.4 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- Distribution / Specialized
- The whole tower, every muscle once

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
