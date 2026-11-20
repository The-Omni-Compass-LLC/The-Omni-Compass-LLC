# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The whole tower, every muscle once, 100 copies: native | The whole tower, every muscle once, 100 copies: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 2777 | 3217 |
| response time (ms), 99th percentile | 5395 | 5532 |
| time over the response line (% of samples) | 55.89 | 53.87 |
| failed requests (%) | 46.11 | 44.85 |
| HPA replicas, mean | 9.829 | 10.23 |
| pods started | 5.278 | 5.811 |
| worker nodes in service, mean | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 460.4 | 461.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 460.4 | 461.2 |
| CPU used with Omni's own (cores), mean | 2.468 | 2.509 |
| host CPU busy, the real machine under kind (%) | 77.14 | 84.97 |
| organism work | 6.88e+12 | 6.88e+12 |
| organism energy (J) | 1.103e+15 | 1.103e+15 |
| organism time over the line (% of steps) | 2.589 | 2.551 |
| organism work per energy | 0.006235 | 0.006235 |
| organism behind its window (s) | 1.761 | 2.182 |

## Each organism: omni against native, paired by repetition

### The whole tower, every muscle once, 100 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 4 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this)), EVEN (inside the noise) on 2

90 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2777 | 3217 | +15.8% | +40.39 to +838.8 | LOSS |
| response time (ms), 99th percentile | 5395 | 5532 | +2.5% | -292.5 to +566.7 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 55.89 | 53.87 | -3.6% | -2.557 to -1.476 | GAIN |
| failed requests (%) | 46.11 | 44.85 | -2.7% | -1.837 to -0.6851 | GAIN |
| HPA replicas, mean | 9.829 | 10.23 | +4.1% | +0.1307 to +0.6695 | power given |
| pods started | 5.278 | 5.811 | +10.1% | +0.145 to +0.9216 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.001147 to +0.0003719 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 460.4 | 461.2 | +0.2% | +0.4497 to +1.313 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 460.4 | 461.2 | +0.2% | +0.4247 to +1.299 | power given |
| CPU used with Omni's own (cores), mean | 2.468 | 2.509 | +1.6% | +0.02971 to +0.05121 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.14 | 84.97 | +10.1% | +7.57 to +8.072 | shown, not judged |
| organism work | 6.88e+12 | 6.88e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+15 | 1.103e+15 | +0.0% | +8.697e+08 to +8.697e+08 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.589 | 2.551 | -1.5% | -0.03826 to -0.03826 | GAIN |
| organism work per energy | 0.006235 | 0.006235 | -0.0% | -4.914e-09 to -4.914e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 1.761 | 2.182 | +23.9% | +0.3498 to +0.4924 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- Distribution / Specialized
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
