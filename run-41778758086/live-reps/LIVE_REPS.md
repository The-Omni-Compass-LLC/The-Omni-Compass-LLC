# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.511 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 158.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 143.4 | 75.62 |
| response time (ms), 95th percentile | 330.7 | 112.6 |
| response time (ms), 99th percentile | 550.6 | 152.2 |
| time over the response line (% of samples) | 2.169 | 0.0241 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.1867 |
| utilisation (used / allocatable) | 0.03669 | 0.03539 |
| CPU used (cores), mean | 0.8806 | 0.8493 |
| Omni's own CPU (cores), mean | 0 | 0.03584 |
| CPU used with Omni's own (cores), mean | 0.8806 | 0.8851 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 769.8 | 783.9 |
| HPA replicas, mean | 8.41 | 8.694 |
| pods started | 5.5 | 4.7 |
| pod start wait, total (s) | 7.6 | 6.4 |
| pod start wait, mean (s) | 1.395 | 1.424 |
| host CPU busy, the real machine under kind (%) | 27.13 | 27.47 |
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
| node-hours | 1.511 | 1.512 | +0.1% | −0.0010 to +0.0030 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.4 | 158.2 | −0.1% | −0.4970 to +0.1424 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.4 | 158.2 | −0.1% | −0.4970 to +0.1424 | no |
| response time (ms), mean | 143.4 | 75.62 | −47.3% | −92.5981 to −42.8912 | yes: GAIN |
| response time (ms), 95th percentile | 330.7 | 112.6 | −65.9% | −288.3908 to −147.7772 | yes: GAIN |
| response time (ms), 99th percentile | 550.6 | 152.2 | −72.4% | −539.6535 to −257.2355 | yes: GAIN |
| time over the response line (% of samples) | 2.169 | 0.0241 | −98.9% | −3.5358 to −0.7536 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.1 | 0 | −100.0% | −3.7673 to −0.4327 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.8 | +19.800 (native is 0) | +18.2996 to +21.3004 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.1867 | +16.7% | −0.1358 to +0.1892 | no |
| utilisation (used / allocatable) | 0.03669 | 0.03539 | −3.6% | −0.0026 to −0.0000 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.8806 | 0.8493 | −3.6% | −0.0621 to −0.0005 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03584 | +0.036 (native is 0) | +0.0306 to +0.0411 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8806 | 0.8851 | +0.5% | −0.0214 to +0.0304 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 769.8 | 783.9 | +1.8% | −6.7794 to +34.9265 | no |
| HPA replicas, mean | 8.41 | 8.694 | +3.4% | −0.0886 to +0.6571 | no |
| pods started | 5.5 | 4.7 | −14.5% | −2.0526 to +0.4526 | no |
| pod start wait, total (s) | 7.6 | 6.4 | −15.8% | −3.7636 to +1.3636 | no |
| pod start wait, mean (s) | 1.395 | 1.424 | +2.0% | −0.3117 to +0.3688 | no |
| host CPU busy, the real machine under kind (%) | 27.13 | 27.47 | +1.3% | −0.0715 to +0.7593 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*