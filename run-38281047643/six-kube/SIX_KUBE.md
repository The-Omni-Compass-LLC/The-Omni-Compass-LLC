# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The four stacked, duplicates kept, 100 copies: native | The four stacked, duplicates kept, 100 copies: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 3063 | 4524 |
| response time (ms), 99th percentile | 5551 | 7387 |
| time over the response line (% of samples) | 63.92 | 57.18 |
| failed requests (%) | 40.14 | 40.43 |
| HPA replicas, mean | 9.899 | 9.88 |
| pods started | 4.8 | 4.8 |
| worker nodes in service, mean | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 713.4 | 704.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 713.4 | 704.8 |
| CPU used with Omni's own (cores), mean | 3.097 | 2.865 |
| host CPU busy, the real machine under kind (%) | 93.16 | 95.14 |
| organism work | 1.316e+13 | 1.316e+13 |
| organism energy (J) | 1.108e+15 | 1.108e+15 |
| organism time over the line (% of steps) | 2.53 | 2.523 |
| organism work per energy | 0.01188 | 0.01188 |
| organism behind its window (s) | 4.82 | 58.61 |

## Each organism: omni against native, paired by repetition

### The four stacked, duplicates kept, 100 copies: better on 5, worse on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism energy (J); organism work per energy), inside the noise on 1; OFF THE CLOCK in 1 of 10 repetitions (the organism ended up to 315 s after its window: the machine could not step this many muscles in time, and the cell's last steps saw a cluster at rest)

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3063 | 4524 | +47.7% | +2.778 to +2921 | WORSE |
| response time (ms), 99th percentile | 5551 | 7387 | +33.1% | +170.9 to +3499 | WORSE |
| time over the response line (% of samples) | 63.92 | 57.18 | -10.6% | -11.7 to -1.793 | better |
| failed requests (%) | 40.14 | 40.43 | +0.7% | -3.24 to +3.819 | WORSE (inside the noise) |
| HPA replicas, mean | 9.899 | 9.88 | -0.2% | -0.03253 to -0.005233 | better |
| pods started | 4.8 | 4.8 | +0.0% | -0.3372 to +0.3372 | same |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.585e-16 to +9.69e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 713.4 | 704.8 | -1.2% | -11.06 to -6.149 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 713.4 | 704.8 | -1.2% | -11.06 to -6.149 | better |
| CPU used with Omni's own (cores), mean | 3.097 | 2.865 | -7.5% | -0.3038 to -0.1608 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 93.16 | 95.14 | +2.1% | +0.3955 to +3.545 | shown, not judged (more or less is not better by itself) |
| organism work | 1.316e+13 | 1.316e+13 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.108e+15 | 1.108e+15 | +0.0% | +4.207e+09 to +4.207e+09 | WORSE |
| organism time over the line (% of steps) | 2.53 | 2.523 | -0.3% | -0.007321 to -0.007321 | better |
| organism work per energy | 0.01188 | 0.01188 | -0.0% | -4.513e-08 to -4.513e-08 | WORSE |
| organism behind its window (s) | 4.82 | 58.61 | +1116.0% | -17.84 to +125.4 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- Distribution / Specialized
- The whole tower, every muscle once

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
