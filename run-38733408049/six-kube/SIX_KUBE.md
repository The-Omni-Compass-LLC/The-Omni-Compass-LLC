# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The whole tower, every muscle once, 100 copies: native | The whole tower, every muscle once, 100 copies: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 3226 | 5096 |
| response time (ms), 99th percentile | 6336 | 7718 |
| time over the response line (% of samples) | 67.8 | 65.21 |
| failed requests (%) | 51.76 | 50.88 |
| HPA replicas, mean | 9.844 | 9.837 |
| pods started | 5.2 | 5.1 |
| worker nodes in service, mean | 6 | 5.999 |
| energy, parked workers still on at idle power (Wh, declared model) | 462.9 | 463.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 462.9 | 463.1 |
| CPU used with Omni's own (cores), mean | 2.56 | 2.592 |
| host CPU busy, the real machine under kind (%) | 80.57 | 88.28 |
| organism work | 6.88e+12 | 6.88e+12 |
| organism energy (J) | 1.103e+15 | 1.103e+15 |
| organism time over the line (% of steps) | 2.589 | 2.551 |
| organism work per energy | 0.006235 | 0.006235 |
| organism behind its window (s) | 1.8 | 2.23 |

## Each organism: omni against native, paired by repetition

### The whole tower, every muscle once, 100 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 0, EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3226 | 5096 | +58.0% | +628.9 to +3111 | LOSS |
| response time (ms), 99th percentile | 6336 | 7718 | +21.8% | +167.8 to +2595 | LOSS |
| time over the response line (% of samples) | 67.8 | 65.21 | -3.8% | -4.963 to -0.2162 | GAIN |
| failed requests (%) | 51.76 | 50.88 | -1.7% | -6.937 to +5.181 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.844 | 9.837 | -0.1% | -0.01541 to +0.001493 | EVEN, inside the noise (cut) |
| pods started | 5.2 | 5.1 | -1.9% | -0.3262 to +0.1262 | EVEN, inside the noise (cut) |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002581 to +0.0009987 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 462.9 | 463.2 | +0.1% | -0.8737 to +1.382 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 462.9 | 463.1 | +0.0% | -0.9119 to +1.341 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.56 | 2.592 | +1.2% | +0.009952 to +0.05392 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 80.57 | 88.28 | +9.6% | +7.238 to +8.177 | shown, not judged |
| organism work | 6.88e+12 | 6.88e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+15 | 1.103e+15 | +0.0% | +8.697e+08 to +8.697e+08 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.589 | 2.551 | -1.5% | -0.03826 to -0.03826 | GAIN |
| organism work per energy | 0.006235 | 0.006235 | -0.0% | -4.914e-09 to -4.914e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 1.8 | 2.23 | +23.9% | +0.1438 to +0.7162 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- Distribution / Specialized
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
