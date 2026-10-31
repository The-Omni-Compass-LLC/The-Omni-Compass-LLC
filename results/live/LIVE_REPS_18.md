# Set 18 on real Kubernetes: native against me on top; the autoscaler alone makes pods

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run: benchmark-reps 36358460215, commit f5bff2b. Five paired repetitions, 15 minutes each, kind with 1 control plane
and 6 workers. I gauge the queue and write no replica floor; the target I hold uses the CPU each pod is guaranteed.

A change is significant when its paired 95% interval excludes zero. A response time that fell is GAIN.

| Gauge | Native | Me on top | Verdict |
|---|---:|---:|---|
| workers in service, mean | 6 | 4.92 | −18.0%, GAIN, significant |
| node-hours | 1.517 | 1.244 | −18.0%, GAIN, significant |
| energy (Wh) | 158.9 | 140.8 | −11.3%, GAIN, significant |
| energy per unit of work (Wh per core-hour) | 722 | 503 | −30.3%, GAIN, significant |
| work done (CPU used, cores) | 0.874 | 1.125 | +28.7%, GAIN, significant |
| replicas, mean | 8.89 | 6.73 | −24.3%, GAIN, significant |
| response time, mean (ms) | 129.9 | 83.7 | −35.6%, GAIN, significant |
| response time, 95th percentile (ms) | 267.4 | 126.9 | −52.6%, GAIN, significant |
| response time, 99th percentile (ms) | 371.5 | 170.9 | −54.0%, GAIN, significant |
| failed requests (%) | 0 | 0 | STEADY |
| pods not yet running, pod-minutes | 0.203 | 0.52 | +156%, not significant (set 17: +365%, significant) |

## What the trail shows (repetition 1)

- **Pod reflex:** no writes; it gauged only.
- **Pods:** the autoscaler ran 24% fewer pods than native, each with more CPU.
- **Machines:** I closed five of six to new work by the sixth decision. They idle as their pods leave, so machines in
  service fell by 18%, against 36% in sets 15–17, where the extra pod churn also emptied them faster.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
