# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.512 | 1.512 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 158.8 | 159.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 158.8 | 159.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 166.5 | 83.17 | 84.26 |
| response time (ms), 95th percentile | 383.8 | 129.7 | 124.3 |
| response time (ms), 99th percentile | 638.1 | 174.5 | 156.6 |
| time over the response line (% of samples) | 2.752 | 0.01198 | 0.2674 |
| failed requests (%) | 0 | 0 | 0.1355 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.1 | 0 | 0.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.8 | 16.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.185 | 0.5683 |
| utilisation (used / allocatable) | 0.04028 | 0.03833 | 0.03908 |
| CPU used (cores), mean | 0.9667 | 0.9198 | 0.9379 |
| Omni's own CPU (cores), mean | 0 | 0.00916 | 0.0089 |
| CPU used with Omni's own (cores), mean | 0.9667 | 0.929 | 0.9468 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 686.3 | 716.4 | 699.6 |
| HPA replicas, mean | 8.613 | 8.328 | 9.723 |
| pods started | 5.3 | 4.3 | 9 |
| pod start wait, total (s) | 7.8 | 5.8 | 16.2 |
| pod start wait, mean (s) | 1.497 | 1.427 | 1.8 |
| host CPU busy, the real machine under kind (%) | 29.31 | 28.5 | 29.02 |
| host cores (the real machine under kind) | 4 | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan |

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
| node-hours | 1.512 | 1.512 | +0.0% | −0.0017 to +0.0021 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 158.8 | −0.3% | −0.8325 to +0.0114 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 158.8 | −0.3% | −0.8325 to +0.0114 | no |
| response time (ms), mean | 166.5 | 83.17 | −50.1% | −103.1965 to −63.5133 | yes: GAIN |
| response time (ms), 95th percentile | 383.8 | 129.7 | −66.2% | −309.2887 to −198.8783 | yes: GAIN |
| response time (ms), 99th percentile | 638.1 | 174.5 | −72.7% | −562.9169 to −364.2333 | yes: GAIN |
| time over the response line (% of samples) | 2.752 | 0.01198 | −99.6% | −3.8933 to −1.5866 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.1 | 0 | −100.0% | −4.4676 to −1.7324 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.8 | +18.800 (native is 0) | +16.6461 to +20.9539 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.185 | +38.8% | −0.2407 to +0.3440 | no |
| utilisation (used / allocatable) | 0.04028 | 0.03833 | −4.8% | −0.0032 to −0.0007 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9667 | 0.9198 | −4.8% | −0.0769 to −0.0169 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00916 | +0.009 (native is 0) | +0.0080 to +0.0104 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9667 | 0.929 | −3.9% | −0.0673 to −0.0082 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 686.3 | 716.4 | +4.4% | +15.1824 to +45.1243 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.613 | 8.328 | −3.3% | −0.6674 to +0.0971 | no |
| pods started | 5.3 | 4.3 | −18.9% | −2.0116 to +0.0116 | no |
| pod start wait, total (s) | 7.8 | 5.8 | −25.6% | −4.3117 to +0.3117 | no |
| pod start wait, mean (s) | 1.497 | 1.427 | −4.7% | −0.4777 to +0.3377 | no |
| host CPU busy, the real machine under kind (%) | 29.31 | 28.5 | −2.8% | −1.6714 to +0.0349 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.515 | +0.2% | −0.0028 to +0.0094 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 159.3 | +0.0% | −0.5916 to +0.6800 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 159.3 | +0.0% | −0.5916 to +0.6800 | no |
| response time (ms), mean | 166.5 | 84.26 | −49.4% | −102.9782 to −61.5412 | yes: GAIN |
| response time (ms), 95th percentile | 383.8 | 124.3 | −67.6% | −316.3594 to −202.6636 | yes: GAIN |
| response time (ms), 99th percentile | 638.1 | 156.6 | −75.5% | −590.1727 to −372.7923 | yes: GAIN |
| time over the response line (% of samples) | 2.752 | 0.2674 | −90.3% | −3.6599 to −1.3091 | yes: GAIN |
| failed requests (%) | 0 | 0.1355 | +0.136 (native is 0) | +0.0581 to +0.2129 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.1 | 0.4 | −87.1% | −4.1717 to −1.2283 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.8 | +16.800 (native is 0) | +14.2143 to +19.3857 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.5683 | +326.3% | +0.0108 to +0.8592 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.04028 | 0.03908 | −3.0% | −0.0020 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9667 | 0.9379 | −3.0% | −0.0482 to −0.0094 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0089 | +0.009 (native is 0) | +0.0081 to +0.0097 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9667 | 0.9468 | −2.1% | −0.0388 to −0.0011 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 686.3 | 699.6 | +1.9% | −3.4683 to +30.0742 | no |
| HPA replicas, mean | 8.613 | 9.723 | +12.9% | +0.7353 to +1.4828 | yes: power given |
| pods started | 5.3 | 9 | +69.8% | +3.3545 to +4.0455 | yes: power given |
| pod start wait, total (s) | 7.8 | 16.2 | +107.7% | +6.5165 to +10.2835 | yes: LOSS |
| pod start wait, mean (s) | 1.497 | 1.8 | +20.3% | +0.0812 to +0.5255 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 29.31 | 29.02 | −1.0% | −0.7852 to +0.1899 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.512 | 1.515 | +0.2% | −0.0027 to +0.0090 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.8 | 159.3 | +0.3% | −0.1537 to +1.0632 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.8 | 159.3 | +0.3% | −0.1537 to +1.0632 | no |
| response time (ms), mean | 83.17 | 84.26 | +1.3% | −0.1406 to +2.3310 | no |
| response time (ms), 95th percentile | 129.7 | 124.3 | −4.2% | −13.8255 to +2.9695 | no |
| response time (ms), 99th percentile | 174.5 | 156.6 | −10.3% | −31.1886 to −4.6262 | yes: GAIN |
| time over the response line (% of samples) | 0.01198 | 0.2674 | +2133.1% | +0.1701 to +0.3409 | yes: LOSS |
| failed requests (%) | 0 | 0.1355 | +0.136 (native is 0) | +0.0581 to +0.2129 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.4 | +0.400 (native is 0) | +0.0306 to +0.7694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 18.8 | 16.8 | −10.6% | −6.3836 to +2.3836 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.185 | 0.5683 | +207.2% | +0.0887 to +0.6780 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03833 | 0.03908 | +2.0% | −0.0005 to +0.0020 | no |
| CPU used (cores), mean | 0.9198 | 0.9379 | +2.0% | −0.0108 to +0.0470 | no |
| Omni's own CPU (cores), mean | 0.00916 | 0.0089 | −2.8% | −0.0007 to +0.0002 | no |
| CPU used with Omni's own (cores), mean | 0.929 | 0.9468 | +1.9% | −0.0111 to +0.0467 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 716.4 | 699.6 | −2.4% | −38.1618 to +4.4610 | no |
| HPA replicas, mean | 8.328 | 9.723 | +16.7% | +0.8532 to +1.9352 | yes: power given |
| pods started | 4.3 | 9 | +109.3% | +3.5295 to +5.8705 | yes: power given |
| pod start wait, total (s) | 5.8 | 16.2 | +179.3% | +7.0415 to +13.7585 | yes: LOSS |
| pod start wait, mean (s) | 1.427 | 1.8 | +26.2% | +0.0641 to +0.6825 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 28.5 | 29.02 | +1.8% | −0.2953 to +1.3366 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*