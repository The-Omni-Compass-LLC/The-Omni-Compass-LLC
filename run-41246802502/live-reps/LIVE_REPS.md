# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.333 | 4.332 |
| energy, parked workers still on at idle power (Wh, declared model) | 482.9 | 480.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 482.9 | 480.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 283.5 | 137.2 |
| response time (ms), 95th percentile | 752.6 | 295.4 |
| response time (ms), 99th percentile | 1379 | 662.9 |
| time over the response line (% of samples) | 13.91 | 3.265 |
| failed requests (%) | 1.287 | 1.111 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.4 | 8.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 54.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5067 | 0.5967 |
| utilisation (used / allocatable) | 0.08123 | 0.07819 |
| CPU used (cores), mean | 1.95 | 1.877 |
| Omni's own CPU (cores), mean | 0 | 0.01046 |
| CPU used with Omni's own (cores), mean | 1.95 | 1.887 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 369.1 | 381.4 |
| HPA replicas, mean | 9.751 | 11.26 |
| pods started | 5.7 | 13.5 |
| pod start wait, total (s) | 9.1 | 23.8 |
| pod start wait, mean (s) | 1.638 | 1.762 |
| host CPU busy, the real machine under kind (%) | 56.39 | 54.93 |
| host cores (the real machine under kind) | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |

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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 4.333 | 4.332 | −0.0% | −0.0080 to +0.0053 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 482.9 | 480.9 | −0.4% | −2.9564 to −1.0582 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 482.9 | 480.9 | −0.4% | −2.9564 to −1.0582 | yes: GAIN |
| response time (ms), mean | 283.5 | 137.2 | −51.6% | −188.1743 to −104.4803 | yes: GAIN |
| response time (ms), 95th percentile | 752.6 | 295.4 | −60.8% | −573.5946 to −340.9314 | yes: GAIN |
| response time (ms), 99th percentile | 1379 | 662.9 | −51.9% | −905.7847 to −526.0395 | yes: GAIN |
| time over the response line (% of samples) | 13.91 | 3.265 | −76.5% | −15.1389 to −6.1460 | yes: GAIN |
| failed requests (%) | 1.287 | 1.111 | −13.7% | −0.3091 to −0.0429 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.4 | 8.9 | −62.0% | −19.1388 to −9.8612 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 54.2 | +54.200 (native is 0) | +38.4820 to +69.9180 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5067 | 0.5967 | +17.8% | −0.2282 to +0.4082 | no |
| utilisation (used / allocatable) | 0.08123 | 0.07819 | −3.7% | −0.0038 to −0.0023 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.95 | 1.877 | −3.7% | −0.0914 to −0.0548 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01046 | +0.010 (native is 0) | +0.0084 to +0.0125 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.95 | 1.887 | −3.2% | −0.0796 to −0.0456 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 369.1 | 381.4 | +3.3% | +8.5263 to +15.9153 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.751 | 11.26 | +15.5% | +0.0198 to +3.0049 | yes: power given |
| pods started | 5.7 | 13.5 | +136.8% | +4.5517 to +11.0483 | yes: power given |
| pod start wait, total (s) | 9.1 | 23.8 | +161.5% | +9.0975 to +20.3025 | yes: LOSS |
| pod start wait, mean (s) | 1.638 | 1.762 | +7.5% | −0.1974 to +0.4447 | no |
| host CPU busy, the real machine under kind (%) | 56.39 | 54.93 | −2.6% | −1.8789 to −1.0434 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*