# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Distribution / Specialized: native | Distribution / Specialized: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 1170 | 1025 |
| response time (ms), 99th percentile | 5007 | 4363 |
| time over the response line (% of samples) | 14.53 | 10 |
| failed requests (%) | 1.562 | 1.304 |
| HPA replicas, mean | 9.562 | 14.54 |
| pods started | 6 | 12 |
| worker nodes in service, mean | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 180.8 | 180.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.8 | 180.9 |
| CPU used with Omni's own (cores), mean | 2.078 | 2.05 |
| host CPU busy, the real machine under kind (%) | 60.84 | 60.67 |
| organism work | 2.138e+10 | 2.138e+10 |
| organism energy (J) | 5.596e+10 | 5.596e+10 |
| organism time over the line (% of steps) | 2.303 | 2.262 |
| organism work per energy | 0.382 | 0.382 |
| organism behind its window (s) | 0 | 0 |

## Each organism: omni against native, paired by repetition

### Distribution / Specialized: ONE REPETITION

1 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1170 | 1025 | -12.4% |  | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5007 | 4363 | -12.9% |  | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 14.53 | 10 | -31.2% |  | EVEN, inside the noise (cut) |
| failed requests (%) | 1.562 | 1.304 | -16.5% |  | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.562 | 14.54 | +52.0% |  | EVEN, inside the noise (up) |
| pods started | 6 | 12 | +100.0% |  | EVEN, inside the noise (up) |
| worker nodes in service, mean | 6 | 6 | +0.0% |  | EVEN, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 180.8 | 180.9 | +0.1% |  | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.8 | 180.9 | +0.1% |  | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.078 | 2.05 | -1.4% |  | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.84 | 60.67 | -0.3% |  | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% |  | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% |  | EVEN, inside the noise (up) |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% |  | EVEN, inside the noise (cut) |
| organism work per energy | 0.382 | 0.382 | -0.0% |  | EVEN, inside the noise (cut) |
| organism behind its window (s) | 0 | 0 | +0 |  | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
