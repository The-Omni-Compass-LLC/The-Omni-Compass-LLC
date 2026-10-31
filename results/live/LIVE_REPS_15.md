# Set 15 on real Kubernetes: conveyed CPU, the promise in queue terms, machines empty one at a time

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run: benchmark-reps 36351987055, commit 82d46a7. Five paired repetitions (native, me on top, me alone back to back on
one runner, order rotated), 15 minutes each, kind with 1 control plane and 6 workers.

A change is significant when its paired 95% interval excludes zero. A response time that fell is GAIN.

| Gauge | Native | Me on top | Me alone |
|---|---:|---:|---:|
| workers in service, mean | 6 | 3.87 (−35.5%, GAIN, significant) | 6 (STEADY) |
| node-hours | 1.516 | 0.980 (−35.3%, GAIN, significant) | 1.519 (+0.2%, STEADY, not significant) |
| energy (Wh) | 159.2 | 121.9 (−23.4%, GAIN, significant) | 162.5 (+2.1%, GAIN, significant) |
| energy per unit of work (Wh per core-hour) | 683 | 413 (−39.5%, GAIN, significant) | 520 (−24.0%, GAIN, significant) |
| work done (CPU used, cores) | 0.923 | 1.166 (+26.3%, GAIN, significant) | 1.236 (+33.9%, GAIN, significant) |
| response time, mean (ms) | 153.9 | 110.6 (−28.2%, GAIN, significant) | 94.2 (−38.8%, GAIN, significant) |
| response time, 95th percentile (ms) | 320.8 | 204.7 (−36.2%, GAIN, significant) | 151.5 (−52.8%, GAIN, significant) |
| response time, 99th percentile (ms) | 475.4 | 293.3 (−38.3%, GAIN, significant) | 185.5 (−61.0%, GAIN, significant) |
| failed requests (%) | 0 | 0 (STEADY) | 0 (STEADY) |
| pods not yet running, pod-minutes | 0.16 | 0.94 (+488%, STEADY, not significant) | 0.52 (+227%, STEADY, not significant) |
| replicas, mean | 8.94 | 9.22 (+3.1%, STEADY, not significant) | 9.83 (+10.0%, power given, significant) |

## What the trail shows

**On top.**
- Machines emptied as the autoscaler scaled down, the machine with the least work first.
- No pod was moved or restarted.

**Alone.**
- My replica floor stayed at 10 for the whole run, so no pod left and no machine emptied.
- The pod reflex set that floor: "floor 10 (queue busy 0.44 vs promise 0.20, R 130 ms, S 73 ms)".
- Its bare service time S was the fastest ever seen, 73 ms, answered while one pod held 3700m.
- Once pods shared a machine at 1850m, their ordinary response read as a queue against that record.
- **Fix:** S and R now come from the same window, the pods as they are now. A change of a pod's CPU limit is no longer
  read as a queue (`tests/test_pod_reflex.py`).

**Pods not yet running.**
- A new pod could wait up to 5 s for me to open a machine I had closed with a cordon.
- **Fix, running as set 16:** the prefer-not mark. A pod that finds the open machines full is placed on a marked one
  at once.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
