# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 1157 | 816.1 |
| response time (ms), 99th percentile | 6002 | 7387 |
| time over the response line (% of samples) | 12.36 | 7.846 |
| failed requests (%) | 2.114 | 1.692 |
| HPA replicas, mean | 9.631 | 14.3 |
| pods started | 6 | 11 |
| worker nodes in service, mean | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 179.9 | 180.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.9 | 180.4 |
| CPU used with Omni's own (cores), mean | 2.045 | 2.02 |
| host CPU busy, the real machine under kind (%) | 59.5 | 59.6 |
| organism work | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 2.401 | 2.345 |
| organism work per energy | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 |

## Each organism: omni against native, paired by repetition

### The four stacked, duplicates kept: ONE REPETITION

1 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1157 | 816.1 | -29.4% |  | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 6002 | 7387 | +23.1% |  | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 12.36 | 7.846 | -36.5% |  | EVEN, inside the noise (cut) |
| failed requests (%) | 2.114 | 1.692 | -19.9% |  | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.631 | 14.3 | +48.5% |  | EVEN, inside the noise (up) |
| pods started | 6 | 11 | +83.3% |  | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | +0.0% |  | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.9 | 180.4 | +0.3% |  | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.9 | 180.4 | +0.3% |  | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.045 | 2.02 | -1.2% |  | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.5 | 59.6 | +0.2% |  | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% |  | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% |  | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% |  | EVEN, inside the noise (cut) |
| organism work per energy | 0.01277 | 0.01277 | -0.0% |  | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 |  | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- Distribution / Specialized
- The whole tower, every muscle once

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
