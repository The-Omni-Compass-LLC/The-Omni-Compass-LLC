# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.976 |
| node-hours | 2.514 | 2.508 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 271 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 119.8 | 90.6 |
| response time (ms), 95th percentile | 208.9 | 197.9 |
| response time (ms), 99th percentile | 305.8 | 296.7 |
| time over the response line (% of samples) | 0.1538 | 0.1334 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 979.9 | 984.1 |
| utilisation (used / allocatable) | 0.05809 | 0.05837 |
| CPU used (cores), mean | 1.394 | 1.396 |
| Omni's own CPU (cores), mean | 0 | 0.01141 |
| CPU used with Omni's own (cores), mean | 1.394 | 1.407 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.6 | 463.4 |
| HPA replicas, mean | 2.012 | 1.971 |
| pods started | 0.1 | 0 |
| pod start wait, total (s) | 0.2 | 0 |
| pod start wait, mean (s) | 0.2 | 0 |
| host CPU busy, the real machine under kind (%) | 43.19 | 43.79 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1396 | 1395 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.694 |
| queue: job wait, submitted to its first pod running, mean (s) | 129.3 | 123.9 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 620.7 | 594.5 |
| queue: job turnaround, submitted to done, mean (s) | 740.5 | 730.9 |
| queue: jobs unfinished at the window's end | 8.4 | 6.8 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.976 | −0.4% | −0.0490 to +0.0019 | no |
| node-hours | 2.514 | 2.508 | −0.2% | −0.0218 to +0.0101 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.7 | +0.2% | −0.6071 to +1.8682 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 271 | −0.0% | −1.5934 to +1.3754 | no |
| response time (ms), mean | 119.8 | 90.6 | −24.4% | −38.2591 to −20.2356 | yes: GAIN |
| response time (ms), 95th percentile | 208.9 | 197.9 | −5.3% | −21.3137 to −0.6253 | yes: GAIN |
| response time (ms), 99th percentile | 305.8 | 296.7 | −3.0% | −25.6220 to +7.4884 | no |
| time over the response line (% of samples) | 0.1538 | 0.1334 | −13.2% | −0.0825 to +0.0419 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.7 | +13.700 (native is 0) | +11.1531 to +16.2469 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 979.9 | 984.1 | +0.4% | −97.8691 to +106.3925 | no |
| utilisation (used / allocatable) | 0.05809 | 0.05837 | +0.5% | −0.0011 to +0.0016 | no |
| CPU used (cores), mean | 1.394 | 1.396 | +0.1% | −0.0311 to +0.0340 | no |
| Omni's own CPU (cores), mean | 0 | 0.01141 | +0.011 (native is 0) | +0.0103 to +0.0125 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.394 | 1.407 | +0.9% | −0.0198 to +0.0455 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.6 | 463.4 | −0.2% | −11.2555 to +8.9402 | no |
| HPA replicas, mean | 2.012 | 1.971 | −2.0% | −0.1634 to +0.0815 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 43.19 | 43.79 | +1.4% | −0.1145 to +1.3151 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1396 | 1395 | −0.0% | −23.6315 to +22.4315 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.694 | −5.1% | −0.4671 to −0.1457 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 129.3 | 123.9 | −4.1% | −43.5213 to +32.8046 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 620.7 | 594.5 | −4.2% | −172.5672 to +120.1672 | no |
| queue: job turnaround, submitted to done, mean (s) | 740.5 | 730.9 | −1.3% | −96.7197 to +77.4031 | no |
| queue: jobs unfinished at the window's end | 8.4 | 6.8 | −19.0% | −4.2807 to +1.0807 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*