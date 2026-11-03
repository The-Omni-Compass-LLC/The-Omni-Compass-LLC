# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | Native tuned, HPA target 40 | Native tuned, HPA target 30 | Native tuned, HPA target 20 | omni |
|---|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.51 | 1.51 | 1.51 | 1.509 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 159.8 | 159.8 | 159.7 | 159.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 159.8 | 159.8 | 159.7 | 159.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan |
| response time (ms), mean | 183.8 | 176.4 | 177.6 | 173 | 90.63 |
| response time (ms), 95th percentile | 413.6 | 394.2 | 410.1 | 369 | 135 |
| response time (ms), 99th percentile | 679.4 | 646.4 | 649.2 | 613.6 | 188.5 |
| time over the response line (% of samples) | 3.269 | 2.931 | 3.159 | 2.403 | 0.02432 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 2.6 | 3.2 | 2.6 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 0 | 0 | 22.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | 80 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3567 | 0.41 | 0.16 | 0.1617 | 0.3567 |
| utilisation (used / allocatable) | 0.04371 | 0.04365 | 0.04367 | 0.04355 | 0.04171 |
| CPU used (cores), mean | 1.049 | 1.047 | 1.048 | 1.045 | 1.001 |
| Omni's own CPU (cores), mean | 0 | 0 | 0 | 0 | 0.04089 |
| CPU used with Omni's own (cores), mean | 1.049 | 1.047 | 1.048 | 1.045 | 1.042 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 638.5 | 640 | 636.9 | 637.8 | 661.5 |
| HPA replicas, mean | 8.774 | 9.245 | 9.707 | 9.939 | 9.903 |
| pods started | 4.7 | 3.4 | 1.7 | 0.4 | 3.9 |
| pod start wait, total (s) | 7.9 | 5.9 | 2.2 | 0.4 | 6.1 |
| pod start wait, mean (s) | 1.683 | 1.623 | 0.8733 | 0.1 | 1.625 |
| host CPU busy, the real machine under kind (%) | 31.85 | 31.65 | 31.74 | 31.51 | 32.09 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan | nan | nan |

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
| node-hours | 1.51 | 1.511 | +0.1% | −0.0000 to +0.0027 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 159.5 | −0.2% | −0.5325 to −0.0872 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 159.5 | −0.2% | −0.5325 to −0.0872 | yes: GAIN |
| response time (ms), mean | 183.8 | 90.63 | −50.7% | −114.8429 to −71.4560 | yes: GAIN |
| response time (ms), 95th percentile | 413.6 | 135 | −67.4% | −341.2887 to −215.9873 | yes: GAIN |
| response time (ms), 99th percentile | 679.4 | 188.5 | −72.2% | −605.3301 to −376.4177 | yes: GAIN |
| time over the response line (% of samples) | 3.269 | 0.02432 | −99.3% | −4.4477 to −2.0411 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 0 | −100.0% | −4.5403 to −1.8597 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 22.1 | +22.100 (native is 0) | +19.5220 to +24.6780 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3567 | 0.3567 | 0.0% | raw −0.3681 to +0.3681 | STEADY, the same (to nine decimal places) |
| utilisation (used / allocatable) | 0.04371 | 0.04171 | −4.6% | −0.0030 to −0.0010 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.049 | 1.001 | −4.6% | −0.0717 to −0.0245 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04089 | +0.041 (native is 0) | +0.0360 to +0.0458 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.049 | 1.042 | −0.7% | −0.0278 to +0.0134 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 638.5 | 661.5 | +3.6% | +7.0815 to +38.8639 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.774 | 9.903 | +12.9% | +0.6606 to +1.5974 | yes: power given |
| pods started | 4.7 | 3.9 | −17.0% | −1.8003 to +0.2003 | no |
| pod start wait, total (s) | 7.9 | 6.1 | −22.8% | −3.6096 to +0.0096 | no |
| pod start wait, mean (s) | 1.683 | 1.625 | −3.5% | −0.4420 to +0.3254 | no |
| host CPU busy, the real machine under kind (%) | 31.85 | 32.09 | +0.8% | −0.2323 to +0.7188 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The cost to match: native tuned harder by its operator, against native with Omni-Compass on top

Kubernetes alone with its HPA target lowered (more pods, faster answers), as an operator would tune it without Omni-Compass, against the same Kubernetes with Omni-Compass on top. Same work in every arm; means over the repetitions.

| Arm | p95 (ms) | p99 (ms) | HPA replicas | CPU used incl. Omni's own (cores) | Machines in service |
|---|---:|---:|---:|---:|---:|
| native | 413.6 | 679.4 | 8.774 | 1.049 | 6 |
| Native tuned, HPA target 40 | 394.2 | 646.4 | 9.245 | 1.047 | 6 |
| Native tuned, HPA target 30 | 410.1 | 649.2 | 9.707 | 1.048 | 6 |
| Native tuned, HPA target 20 | 369 | 613.6 | 9.939 | 1.045 | 6 |
| omni | 135 | 188.5 | 9.903 | 1.042 | 6 |

- omni (p95 135 ms): no native setting tried reached it; the lowest native p95 is 369 ms (Native tuned, HPA target 20).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*