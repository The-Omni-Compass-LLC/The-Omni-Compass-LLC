# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.999 |
| node-hours | 4.516 | 4.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 521.3 | 521 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 521.3 | 521 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 306.7 | 196.4 |
| response time (ms), 95th percentile | 862 | 462 |
| response time (ms), 99th percentile | 3070 | 2795 |
| time over the response line (% of samples) | 22.61 | 16.97 |
| failed requests (%) | 13.02 | 13.26 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 31.1 | 26 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 52.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 58.33 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.42 | 0.5633 |
| utilisation (used / allocatable) | 0.1078 | 0.1077 |
| CPU used (cores), mean | 2.588 | 2.584 |
| Omni's own CPU (cores), mean | 0 | 0.04677 |
| CPU used with Omni's own (cores), mean | 2.588 | 2.631 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 286.7 | 290.3 |
| HPA replicas, mean | 9.479 | 10.91 |
| pods started | 5.3 | 10.4 |
| pod start wait, total (s) | 7.5 | 18.6 |
| pod start wait, mean (s) | 1.412 | 1.757 |
| host CPU busy, the real machine under kind (%) | 72.64 | 74.14 |
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
| worker nodes in service, mean | 6 | 5.999 | −0.0% | −0.0046 to +0.0018 | no |
| node-hours | 4.516 | 4.513 | −0.1% | −0.0130 to +0.0069 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 521.3 | 521 | −0.1% | −1.5181 to +0.9729 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 521.3 | 521 | −0.1% | −1.6438 to +0.9402 | no |
| response time (ms), mean | 306.7 | 196.4 | −36.0% | −153.2296 to −67.4319 | yes: GAIN |
| response time (ms), 95th percentile | 862 | 462 | −46.4% | −525.6540 to −274.4360 | yes: GAIN |
| response time (ms), 99th percentile | 3070 | 2795 | −9.0% | −1699.3906 to +1149.1076 | no |
| time over the response line (% of samples) | 22.61 | 16.97 | −24.9% | −7.6248 to −3.6497 | yes: GAIN |
| failed requests (%) | 13.02 | 13.26 | +1.8% | −0.1957 to +0.6632 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 31.1 | 26 | −16.4% | −6.6977 to −3.5023 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 52.3 | +52.300 (native is 0) | +41.4359 to +63.1641 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.42 | 0.5633 | +34.1% | −0.3750 to +0.6617 | no |
| utilisation (used / allocatable) | 0.1078 | 0.1077 | −0.1% | −0.0014 to +0.0012 | no |
| CPU used (cores), mean | 2.588 | 2.584 | −0.1% | −0.0348 to +0.0274 | no |
| Omni's own CPU (cores), mean | 0 | 0.04677 | +0.047 (native is 0) | +0.0394 to +0.0541 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.588 | 2.631 | +1.7% | +0.0053 to +0.0808 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 286.7 | 290.3 | +1.3% | −3.2080 to +10.5020 | no |
| HPA replicas, mean | 9.479 | 10.91 | +15.1% | +0.1107 to +2.7543 | yes: power given |
| pods started | 5.3 | 10.4 | +96.2% | +2.7049 to +7.4951 | yes: power given |
| pod start wait, total (s) | 7.5 | 18.6 | +148.0% | +5.7957 to +16.4043 | yes: LOSS |
| pod start wait, mean (s) | 1.412 | 1.757 | +24.4% | +0.1023 to +0.5878 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 72.64 | 74.14 | +2.1% | +0.4353 to +2.5596 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 18.0 |  |  | 10 |
| compass | 25.8 | +43.3% | +5.7 to +9.9 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*