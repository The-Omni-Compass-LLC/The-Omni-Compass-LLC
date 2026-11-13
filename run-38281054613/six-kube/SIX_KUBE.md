# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The whole tower, every muscle once, 100 copies: native | The whole tower, every muscle once, 100 copies: omni |
|---|---:|---:|
| response time (ms), 95th percentile | 2386 | 3069 |
| response time (ms), 99th percentile | 4032 | 4383 |
| time over the response line (% of samples) | 41.97 | 37.79 |
| failed requests (%) | 26.77 | 26.55 |
| HPA replicas, mean | 9.817 | 9.813 |
| pods started | 5.7 | 5.6 |
| worker nodes in service, mean | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 465.2 | 462.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 465.2 | 462.5 |
| CPU used with Omni's own (cores), mean | 2.655 | 2.558 |
| host CPU busy, the real machine under kind (%) | 81.47 | 84.74 |
| organism work | 6.879e+12 | 6.879e+12 |
| organism energy (J) | 1.103e+15 | 1.103e+15 |
| organism time over the line (% of steps) | 2.592 | 2.589 |
| organism work per energy | 0.006234 | 0.006234 |
| organism behind its window (s) | 2.34 | 3.02 |

## Each organism: omni against native, paired by repetition

### The whole tower, every muscle once, 100 copies: better on 4, worse on 0, inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2386 | 3069 | +28.6% | -704.5 to +2070 | WORSE (inside the noise) |
| response time (ms), 99th percentile | 4032 | 4383 | +8.7% | -840.4 to +1544 | WORSE (inside the noise) |
| time over the response line (% of samples) | 41.97 | 37.79 | -10.0% | -6.518 to -1.838 | better |
| failed requests (%) | 26.77 | 26.55 | -0.8% | -3.497 to +3.055 | better (inside the noise) |
| HPA replicas, mean | 9.817 | 9.813 | -0.0% | -0.01686 to +0.008423 | better (inside the noise) |
| pods started | 5.7 | 5.6 | -1.8% | -0.506 to +0.306 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.255e-16 to +1.614e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 465.2 | 462.5 | -0.6% | -5.264 to -0.02884 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 465.2 | 462.5 | -0.6% | -5.264 to -0.02884 | better |
| CPU used with Omni's own (cores), mean | 2.655 | 2.558 | -3.7% | -0.1736 to -0.0206 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 81.47 | 84.74 | +4.0% | +1.337 to +5.208 | shown, not judged (more or less is not better by itself) |
| organism work | 6.879e+12 | 6.879e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.103e+15 | 1.103e+15 | +0.0% | +1.052e+09 to +1.052e+09 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.592 | 2.589 | -0.1% | -0.003582 to -0.003582 | better |
| organism work per energy | 0.006234 | 0.006234 | -0.0% | -5.942e-09 to -5.942e-09 | same (under one part in a million) |
| organism behind its window (s) | 2.34 | 3.02 | +29.1% | +0.1375 to +1.222 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- Distribution / Specialized
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
