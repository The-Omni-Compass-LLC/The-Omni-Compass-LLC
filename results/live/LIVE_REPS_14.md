# Set 14 on real Kubernetes: idle CPU conveyed to the work

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run: benchmark-reps 36346848307, commit 7d07754. Five paired repetitions (native, me on top, me alone back to back on
one runner, order rotated), 15 minutes each, kind with 1 control plane and 6 workers.

A change is significant when its paired 95% interval excludes zero. A response time that fell is GAIN.

| Gauge | Native | Me on top | Me alone |
|---|---:|---:|---:|
| response time, mean (ms) | 162.1 | 98.7 (−39.1%, GAIN, significant) | 97.4 (−39.9%, GAIN, significant) |
| response time, 95th percentile (ms) | 328.5 | 152.3 (−53.6%, GAIN, significant) | 150.7 (−54.1%, GAIN, significant) |
| response time, 99th percentile (ms) | 473.9 | 204.3 (−56.9%, GAIN, significant) | 179.5 (−62.1%, GAIN, significant) |
| failed requests (%) | 0 | 0 (STEADY) | 0 (STEADY) |
| utilisation, work done (used / allocatable) | 0.0386 | 0.0529 (+36.8%, GAIN, significant) | 0.0519 (+34.3%, GAIN, significant) |
| workers in service, mean | 6 | 6 (STEADY) | 6 (equal; the interval is a rounding artefact) |
| node-hours | 1.516 | 1.515 (−0.1%, STEADY, not significant) | 1.524 (+0.5%, GAIN, significant) |
| energy (Wh) | 159.3 | 162.4 (+1.9%, power given, significant) | 163.2 (+2.4%, power given, significant) |
| pods not yet running, pod-minutes | 0.053 | 0.32 (+500%, STEADY, not significant) | 0.107 (+100%, STEADY, not significant) |

**Useful work per unit of energy** (work done ÷ energy, from the means above, not itself paired-tested): +34% on top, +31% alone. The clients wait for
each answer before asking again, so faster answers bring more requests: 37% more work for 2% more energy.

## What the trail shows

**Response time.** Each machine's idle CPU reached the pods serving on it: 1850m per pod where two pods share a
machine, against the operator's 500m, in place, with no pod restarted.

**Machines.**
- I closed five of six machines to new work (6 → 1 open), but none emptied.
- Each pod now ran busier against its 200m request, because its limit was 1850m. The autoscaler, which sizes against
  the request, held replicas at its maximum of 10, and my own decision in the alone column did the same, so no pod left.
- With every closed machine's pods marked equally, each scale-down would have taken one pod from each machine and
  emptied none.

**What I do about it.**
- **Replicas.** The operator's promise, in queue terms, is busy = target × request ÷ limit. While I convey g times the
  operator's limit, the target that keeps each pod exactly as busy is g times higher, and my replica decision in the
  alone column reads the same promise.
- **Machines.** The closed machine with the least work is marked first to go, the next after it, so each scale-down
  empties whole machines, one at a time.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
