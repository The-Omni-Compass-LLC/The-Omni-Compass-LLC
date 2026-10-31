# Azure Kubernetes Service, the steady set of 100 paired repetitions on omni-v18: the bill, the machines, the service

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run 40069633316 (`aks-metered`, dispatched 24 October 2026, repetitions run one at a time from 24 October 20:06 UTC to 29 October 15:12 UTC), engine **omni-v18**, Omni-Compass on top of native at the tune-down (`dial save`) on the machines alone (`OMNI_MACHINES_ONLY=1`: no pod autoscaler moved, no processor conveyed, no power capped; the governor only parks a machine the cloud already made, after its own trial, and wakes it on a breach), eastus, Standard_D2s_v4, the steady load, replica room 0 to the cap. 100 paired repetitions were planned; **97 ran to their end and 3 failed** (repetitions 82, 90 and 93, each a failed job of the run: their files are in the run's artifacts on the branch `raw`, `run-40069633316/aks-82/`, `aks-90/`, `aks-93/`). This page is the run's own receipt, written by the run's own code at its end (`tools/live_reps.py` as omni-v18 shipped it; `run-40069633316/live-reps-aks/LIVE_REPS.md` and `.json` on `raw`, copied here byte for byte in its judged section), and the preregistered stopping rule's looks (`tools/stop_rule.py`; `docs/K8S_COMPASS_PREREGISTRATION.md`, 19 October). It is omni-v18's record: read in no omni-v21 or omni-v22 table, kept because every result is shown.

**Read by the one key** (`tools/readings.py`, a change of 0.5% or more is a change; a resource spent that rose is power given; the cloud's declared aim is the same work for a smaller bill, never a bigger one, the founder's order of 14 October): the compute bill at list price up 1.2% by the mean of the 97 pairs, its 95% interval across zero (−$0.0007 to +$0.0021 a repetition): power given, not beyond the noise; machines billed up 1.2%, the same; the response time's 99th percentile GAIN (down 11.0%, its interval clear of zero); every other service gauge EVEN or not beyond the noise; failed requests up 3.9% by the mean, its interval across zero. The stopping rule read the bill at every look and never decided it, so the set ran to the paid cap of 100.

## The stopping rule's looks

```
Stopping rule: looks at 10, 20, 40, 70 paired repetitions, 99% intervals, precision ±2% of native's bill.
- look after 10: bill +2.23% (99% interval -6.14% to +10.60%) not decided; the bill's 99% interval is wider than the precision and holds zero: not yet read
- look after 20: bill +0.46% (99% interval -5.50% to +6.43%) not decided; the bill's 99% interval is wider than the precision and holds zero: not yet read
- look after 40: bill +3.77% (99% interval -2.40% to +9.95%) not decided; the bill's 99% interval is wider than the precision and holds zero: not yet read
- look after 70: bill +2.02% (99% interval -2.24% to +6.28%) not decided; the bill's 99% interval is wider than the precision and holds zero: not yet read
```

## omni (compass law, the cloud mode): Omni-Compass on top of native, on the machines alone (no pod autoscaler moved, no processor conveyed, no power capped) vs native, 97 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 2.814 | 2.832 | +0.7% | −0.0098 to +0.0469 | no |
| node-hours | 0.7104 | 0.715 | +0.7% | −0.0024 to +0.0117 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 86.62 | 87.77 | +1.3% | −0.6670 to +2.9702 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 82.7 | 83.23 | +0.6% | −0.2945 to +1.3550 | no |
| response time (ms), mean | 517.1 | 503.1 | −2.7% | −29.7566 to +1.8811 | no |
| response time (ms), 95th percentile | 1245 | 1195 | −4.0% | −128.4729 to +28.5631 | no |
| response time (ms), 99th percentile | 4744 | 4222 | −11.0% | −1009.6926 to −34.3668 | yes: GAIN |
| time over the response line (% of samples) | 29.06 | 28.81 | −0.9% | −1.1301 to +0.6231 | no |
| failed requests (%) | 4.758 | 4.945 | +3.9% | −0.4799 to +0.8526 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.07 | 13.9 | −1.2% | −0.4116 to +0.0611 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.92 | +24.918 (native is 0) | +24.1653 to +25.6698 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 2.598 | 2.392 | −7.9% | −0.5274 to +0.1151 | no |
| time pods had no machine to take them, pod-minutes | 7.018 | 5.993 | −14.6% | −4.1768 to +2.1273 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.9 | 5.573 | −5.6% | −0.7542 to +0.0989 | no |
| utilisation (used / allocatable) | 0.3622 | 0.3605 | −0.5% | −0.0069 to +0.0035 | no |
| CPU used (cores), mean | 1.935 | 1.937 | +0.1% | −0.0176 to +0.0208 | no |
| Omni's own CPU (cores), mean | 0 | 0.005163 | +0.005 (native is 0) | +0.0050 to +0.0053 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.935 | 1.942 | +0.4% | −0.0125 to +0.0260 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 169.5 | 170.5 | +0.6% | −1.1581 to +3.0914 | no |
| HPA replicas, mean | 9.371 | 9.348 | −0.2% | −0.0802 to +0.0340 | no |
| pods started | 5.01 | 4.753 | −5.1% | −0.7001 to +0.1847 | no |
| pod start wait, total (s) | 525.4 | 455.2 | −13.4% | −278.2501 to +137.6728 | no |
| pod start wait, mean (s) | 98.43 | 89.88 | −8.7% | −49.2406 to +32.1393 | no |
| machines billed, machine-hours | 0.586 | 0.5931 | +1.2% | −0.0074 to +0.0216 | no |
| compute bill at list price ($) | 0.05626 | 0.05694 | +1.2% | −0.0007 to +0.0021 | no |

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
