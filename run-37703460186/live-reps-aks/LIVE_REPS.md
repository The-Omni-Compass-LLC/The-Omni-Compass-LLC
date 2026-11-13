# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge |  |
|---|
| worker nodes in service, mean |  |
| node-hours |  |
| energy, parked workers still on at idle power (Wh, declared model) |  |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) |  |
| response time (ms), mean |  |
| response time (ms), 95th percentile |  |
| response time (ms), 99th percentile |  |
| time over the response line (% of samples) |  |
| failed requests (%) |  |
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


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*