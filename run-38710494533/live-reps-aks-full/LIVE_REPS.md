# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge |  |
|---|
| worker nodes in service, mean |  |
| node-hours |  |
| energy, parked workers still on at idle power (Wh, declared model) |  |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) |  |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) |  |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) |  |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) |  |
| response time (ms), mean |  |
| response time (ms), 95th percentile |  |
| response time (ms), 99th percentile |  |
| time over the response line (% of samples) |  |
| failed requests (%) |  |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) |  |
| settings commands the governor wrote on its own (no person touched either arm) |  |
| governor's additions decided while the service was still inside its line (% of its additions) |  |
| pods with no machine to take them (unschedulable) |  |
| time pods had no machine to take them, pod-minutes |  |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) |  |
| utilisation (used / allocatable) |  |
| CPU used (cores), mean |  |
| Omni's own CPU (cores), mean |  |
| CPU used with Omni's own (cores), mean |  |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) |  |
| HPA replicas, mean |  |
| pods started |  |
| pod start wait, total (s) |  |
| pod start wait, mean (s) |  |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*