# Set 16 on real Kubernetes: native against me on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run: benchmark-reps 36354068590, commit 2d6fccc (prefer-not idle mark, conveyed CPU, the promise in queue terms,
machines empty one at a time). Five paired repetitions, 15 minutes each, kind with 1 control plane and 6 workers.

A change is significant when its paired 95% interval excludes zero. A response time that fell is GAIN.

| Gauge | Native | Me on top | Verdict |
|---|---:|---:|---|
| workers in service, mean | 6 | 3.77 | −37.1%, GAIN, significant |
| node-hours | 1.513 | 0.952 | −37.1%, GAIN, significant |
| energy (Wh) | 158.5 | 118.3 | −25.4%, GAIN, significant |
| energy per unit of work (Wh per core-hour) | 722 | 452 | −37.4%, GAIN, significant |
| work done (CPU used, cores) | 0.875 | 1.051 | +20.0%, GAIN, significant |
| response time, mean (ms) | 116.2 | 82.4 | −29.1%, GAIN, significant |
| response time, 95th percentile (ms) | 244.3 | 144.7 | −40.8%, GAIN, significant |
| response time, 99th percentile (ms) | 367.7 | 234.1 | −36.4%, GAIN, significant |
| failed requests (%) | 0 | 0 | STEADY |
| pods not yet running, pod-minutes | 0.207 | 0.54 | +161%, not significant (set 15: +488%) |
| replicas, mean | 8.80 | 9.24 | +5.0%, not significant |

## What the trail shows

**Pods not yet running.** With the prefer-not mark no pod waited for a place. What is left is pod starts native never
makes: my pod reflex still raised and released the replica floor. The autoscaler alone makes pods from set 18 on; the
reflex gauges and writes nothing.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
