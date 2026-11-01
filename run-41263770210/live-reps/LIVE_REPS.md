# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 171.9 | 171.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.9 | 171.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 503.4 | 451.7 |
| response time (ms), 95th percentile | 2180 | 2123 |
| response time (ms), 99th percentile | 4942 | 5414 |
| time over the response line (% of samples) | 23.71 | 20.94 |
| failed requests (%) | 3.451 | 2.93 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 7.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.068 | 2.02 |
| utilisation (used / allocatable) | 0.09478 | 0.09383 |
| CPU used (cores), mean | 2.275 | 2.252 |
| Omni's own CPU (cores), mean | 0 | 0.01282 |
| CPU used with Omni's own (cores), mean | 2.275 | 2.265 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 312.5 | 315.3 |
| HPA replicas, mean | 14.88 | 15.46 |
| pods started | 5.6 | 3.7 |
| pod start wait, total (s) | 9.7 | 7 |
| pod start wait, mean (s) | 1.705 | 1.605 |
| host CPU busy, the real machine under kind (%) | 66.23 | 65.93 |
| host cores (the real machine under kind) | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |
| second app: response time (ms), 95th percentile | 302.5 | 288 |
| second app: response time (ms), 99th percentile | 1459 | 1142 |
| second app: time over the response line (% of samples) | 14.09 | 13.5 |
| second app: failed requests (%) | 11.98 | 11.91 |

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
| node-hours | 1.514 | 1.514 | −0.0% | −0.0086 to +0.0073 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 171.9 | 171.6 | −0.2% | −1.0738 to +0.5073 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.9 | 171.6 | −0.2% | −1.0738 to +0.5073 | no |
| response time (ms), mean | 503.4 | 451.7 | −10.3% | −96.0570 to −7.3200 | yes: GAIN |
| response time (ms), 95th percentile | 2180 | 2123 | −2.6% | −505.3216 to +390.4436 | no |
| response time (ms), 99th percentile | 4942 | 5414 | +9.5% | −430.6826 to +1374.6034 | no |
| time over the response line (% of samples) | 23.71 | 20.94 | −11.7% | −4.4750 to −1.0742 | yes: GAIN |
| failed requests (%) | 3.451 | 2.93 | −15.1% | −1.2322 to +0.1902 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 7.4 | −11.9% | −1.3372 to −0.6628 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.3 | +41.300 (native is 0) | +31.1781 to +51.4219 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.068 | 2.02 | −2.3% | −1.0359 to +0.9392 | no |
| utilisation (used / allocatable) | 0.09478 | 0.09383 | −1.0% | −0.0018 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.275 | 2.252 | −1.0% | −0.0437 to −0.0017 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01282 | +0.013 (native is 0) | +0.0117 to +0.0139 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.275 | 2.265 | −0.4% | −0.0308 to +0.0110 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 312.5 | 315.3 | +0.9% | −1.4011 to +7.1416 | no |
| HPA replicas, mean | 14.88 | 15.46 | +3.9% | −0.0062 to +1.1603 | no |
| pods started | 5.6 | 3.7 | −33.9% | −3.6011 to −0.1989 | yes: GAIN |
| pod start wait, total (s) | 9.7 | 7 | −27.8% | −7.4454 to +2.0454 | no |
| pod start wait, mean (s) | 1.705 | 1.605 | −5.9% | −0.8197 to +0.6202 | no |
| host CPU busy, the real machine under kind (%) | 66.23 | 65.93 | −0.5% | −1.1235 to +0.5234 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 302.5 | 288 | −4.8% | −71.8768 to +42.9848 | no |
| second app: response time (ms), 99th percentile | 1459 | 1142 | −21.7% | −1252.1623 to +617.8481 | no |
| second app: time over the response line (% of samples) | 14.09 | 13.5 | −4.2% | −1.2643 to +0.0898 | no |
| second app: failed requests (%) | 11.98 | 11.91 | −0.6% | −0.5177 to +0.3767 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*