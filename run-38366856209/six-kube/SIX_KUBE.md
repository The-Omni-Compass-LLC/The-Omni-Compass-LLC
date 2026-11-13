# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 4717 | 3628 |
| response time (ms), 99th percentile | 7933 | 7149 |
| time over the response line (% of samples) | 36.92 | 19.55 |
| failed requests (%) | 7.436 | 7.191 |
| HPA replicas, mean | 9.818 | 9.934 |
| pods started | 3 | 1 |
| worker nodes in service, mean | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 188.6 | 189.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 188.6 | 189.2 |
| CPU used with Omni's own (cores), mean | 2.876 | 2.872 |
| host CPU busy, the real machine under kind (%) | 83.6 | 83.5 |
| organism work | 6.708e+10 | 6.708e+10 |
| organism energy (J) | 1.016e+13 | 1.016e+13 |
| organism time over the line (% of steps) | 1.42 | 1.367 |
| organism work per energy | 0.006603 | 0.006603 |
| organism behind its window (s) | 0 | 0 |

## Each organism: omni against native, paired by repetition

### Energy / Facility / Industrial: ONE REPETITION

1 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4717 | 3628 | -23.1% |  | better (inside the noise) |
| response time (ms), 99th percentile | 7933 | 7149 | -9.9% |  | better (inside the noise) |
| time over the response line (% of samples) | 36.92 | 19.55 | -47.1% |  | better (inside the noise) |
| failed requests (%) | 7.436 | 7.191 | -3.3% |  | better (inside the noise) |
| HPA replicas, mean | 9.818 | 9.934 | +1.2% |  | WORSE (inside the noise) |
| pods started | 3 | 1 | -66.7% |  | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% |  | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 188.6 | 189.2 | +0.3% |  | WORSE (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 188.6 | 189.2 | +0.3% |  | WORSE (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.876 | 2.872 | -0.2% |  | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 83.6 | 83.5 | -0.1% |  | shown, not judged (more or less is not better by itself) |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% |  | same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% |  | same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% |  | better (inside the noise) |
| organism work per energy | 0.006603 | 0.006603 | -0.0% |  | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 |  | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Distribution / Specialized
- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
