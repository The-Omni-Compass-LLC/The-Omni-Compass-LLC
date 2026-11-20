# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.723 | 4.888 |
| node-hours | 2.513 | 2.518 | 1.979 | 2.048 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 274.2 | 273.4 | 272.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 274.2 | 233.2 | 237.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 445.4 | 443.3 | 456.1 | 471 |
| response time (ms), 95th percentile | 1720 | 1779 | 1751 | 1887 |
| response time (ms), 99th percentile | 2420 | 2516 | 2586 | 2726 |
| time over the response line (% of samples) | 17.88 | 17.27 | 18.08 | 17.23 |
| failed requests (%) | 0 | 0 | 0.0236 | 0.0236 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 9.1 | 9.7 | 9.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 14.9 | 13.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 44.44 | 75 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.45 | 21.98 | 19 | 24.82 |
| utilisation (used / allocatable) | 0.06432 | 0.06446 | 0.08121 | 0.074 |
| CPU used (cores), mean | 1.544 | 1.547 | 1.508 | 1.462 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06107 | 0.06633 |
| CPU used with Omni's own (cores), mean | 1.544 | 1.547 | 1.569 | 1.528 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 436.5 | 434.8 | 371.7 | 401 |
| HPA replicas, mean | 2.033 | 2.086 | 2.342 | 2.207 |
| pods started | 0.2 | 0.1 | 1.3 | 0.3 |
| pod start wait, total (s) | 0.6 | 0.2 | 2.4 | 0.6 |
| pod start wait, mean (s) | 0.3 | 0.2 | 1.267 | 0.4 |
| host CPU busy, the real machine under kind (%) | 44.04 | 44.53 | 45.99 | 46.99 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 824.9 | 831 | 830.9 | 840.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.928 | 3.998 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3708 | 0.5042 | 0.5417 | 0.4542 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 0.7 | 4 | 1.6 |
| queue: job turnaround, submitted to done, mean (s) | 130.1 | 139.9 | 136.3 | 146.4 |
| queue: jobs unfinished at the window's end | 0 | 0 | 0 | 0 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan | nan |

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
| worker nodes in service, mean | 6 | 4.888 | −18.5% | −1.8884 to −0.3364 | yes: GAIN |
| node-hours | 2.518 | 2.048 | −18.7% | −0.7943 to −0.1463 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.2 | 272.7 | −0.5% | −3.0426 to +0.1698 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.2 | 237.8 | −13.3% | −61.7563 to −11.0332 | yes: GAIN |
| response time (ms), mean | 443.3 | 471 | +6.2% | −0.9235 to +56.2981 | no |
| response time (ms), 95th percentile | 1779 | 1887 | +6.0% | −18.9783 to +234.0473 | no |
| response time (ms), 99th percentile | 2516 | 2726 | +8.3% | −15.5138 to +435.5222 | no |
| time over the response line (% of samples) | 17.27 | 17.23 | −0.2% | −0.7843 to +0.7069 | no |
| failed requests (%) | 0 | 0.0236 | +0.024 (native is 0) | −0.0120 to +0.0592 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9.8 | +7.7% | −0.0578 to +1.4578 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.3 | +13.300 (native is 0) | +8.8899 to +17.7101 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.98 | 24.82 | +12.9% | −1.5252 to +7.1985 | no |
| utilisation (used / allocatable) | 0.06446 | 0.074 | +14.8% | +0.0037 to +0.0154 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.547 | 1.462 | −5.5% | −0.1828 to +0.0117 | no |
| Omni's own CPU (cores), mean | 0 | 0.06633 | +0.066 (native is 0) | +0.0570 to +0.0757 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.547 | 1.528 | −1.2% | −0.1244 to +0.0860 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 434.8 | 401 | −7.8% | −56.5943 to −11.0944 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.086 | 2.207 | +5.8% | −0.0625 to +0.3042 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.3642 to +0.7642 | no |
| pod start wait, total (s) | 0.2 | 0.6 | +200.0% | −0.7285 to +1.5285 | no |
| pod start wait, mean (s) | 0.2 | 0.4 | +100.0% | −0.6121 to +1.0121 | no |
| host CPU busy, the real machine under kind (%) | 44.53 | 46.99 | +5.5% | +1.9424 to +2.9788 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 831 | 840.1 | +1.1% | +3.0169 to +15.1831 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.998 | −33.4% | −3.2538 to −0.7493 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5042 | 0.4542 | −9.9% | −0.9307 to +0.8307 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1.6 | +128.6% | −1.3982 to +3.1982 | no |
| queue: job turnaround, submitted to done, mean (s) | 139.9 | 146.3 | +4.6% | +0.4881 to +12.4536 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.513 | 2.518 | +0.2% | −0.0041 to +0.0144 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 274.2 | +0.2% | −0.2749 to +1.5181 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 274.2 | +0.2% | −0.2749 to +1.5181 | no |
| response time (ms), mean | 445.4 | 443.3 | −0.5% | −22.6883 to +18.6015 | no |
| response time (ms), 95th percentile | 1720 | 1779 | +3.4% | −68.9038 to +186.5478 | no |
| response time (ms), 99th percentile | 2420 | 2516 | +4.0% | −159.9938 to +352.7662 | no |
| time over the response line (% of samples) | 17.88 | 17.27 | −3.4% | −1.3748 to +0.1612 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 9.1 | −4.2% | −1.1689 to +0.3689 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.45 | 21.98 | +33.6% | −0.5002 to +11.5669 | no |
| utilisation (used / allocatable) | 0.06432 | 0.06446 | +0.2% | −0.0006 to +0.0009 | no |
| CPU used (cores), mean | 1.544 | 1.547 | +0.2% | −0.0153 to +0.0223 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.544 | 1.547 | +0.2% | −0.0153 to +0.0223 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 436.5 | 434.8 | −0.4% | −7.9990 to +4.6839 | no |
| HPA replicas, mean | 2.033 | 2.086 | +2.6% | −0.0808 to +0.1874 | no |
| pods started | 0.2 | 0.1 | −50.0% | −0.6278 to +0.4278 | no |
| pod start wait, total (s) | 0.6 | 0.2 | −66.7% | −1.8775 to +1.0775 | no |
| pod start wait, mean (s) | 0.3 | 0.2 | −33.3% | −0.9564 to +0.7564 | no |
| host CPU busy, the real machine under kind (%) | 44.04 | 44.53 | +1.1% | −0.0483 to +1.0116 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 824.9 | 831 | +0.7% | −0.6309 to +12.8309 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3708 | 0.5042 | +36.0% | −0.5857 to +0.8523 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 0.7 | −50.0% | −1.7690 to +0.3690 | no |
| queue: job turnaround, submitted to done, mean (s) | 130.1 | 139.9 | +7.5% | −1.2350 to +20.7600 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.723 | −21.3% | −2.1716 to −0.3831 | yes: GAIN |
| node-hours | 2.513 | 1.979 | −21.3% | −0.9103 to −0.1587 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 273.4 | −0.1% | −1.2515 to +0.8942 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 233.2 | −14.7% | −68.6533 to −11.9749 | yes: GAIN |
| response time (ms), mean | 445.4 | 456.1 | +2.4% | −1.7710 to +23.2384 | no |
| response time (ms), 95th percentile | 1720 | 1751 | +1.8% | −51.8453 to +113.1663 | no |
| response time (ms), 99th percentile | 2420 | 2586 | +6.9% | +11.4626 to +321.1888 | yes: LOSS |
| time over the response line (% of samples) | 17.88 | 18.08 | +1.1% | −0.4964 to +0.9044 | no |
| failed requests (%) | 0 | 0.0236 | +0.024 (native is 0) | −0.0120 to +0.0592 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 9.7 | +2.1% | −0.6121 to +1.0121 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.9 | +14.900 (native is 0) | +11.5037 to +18.2963 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.45 | 19 | +15.5% | −0.2726 to +5.3792 | no |
| utilisation (used / allocatable) | 0.06432 | 0.08121 | +26.3% | +0.0040 to +0.0297 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.544 | 1.508 | −2.3% | −0.0636 to −0.0083 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06107 | +0.061 (native is 0) | +0.0523 to +0.0699 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.544 | 1.569 | +1.6% | −0.0090 to +0.0593 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 436.5 | 371.7 | −14.8% | −114.4227 to −15.0709 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.033 | 2.342 | +15.2% | +0.0902 to +0.5285 | yes: power given |
| pods started | 0.2 | 1.3 | +550.0% | +0.3128 to +1.8872 | yes: power given |
| pod start wait, total (s) | 0.6 | 2.4 | +300.0% | −0.1604 to +3.7604 | no |
| pod start wait, mean (s) | 0.3 | 1.267 | +322.2% | +0.0149 to +1.9184 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.04 | 45.99 | +4.4% | +1.4113 to +2.4862 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 824.9 | 830.9 | +0.7% | +0.3980 to +11.6020 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.928 | −34.5% | −3.3130 to −0.8312 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3708 | 0.5417 | +46.1% | −0.3262 to +0.6679 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 4 | +185.7% | −2.2303 to +7.4303 | no |
| queue: job turnaround, submitted to done, mean (s) | 130.1 | 136.3 | +4.8% | −0.4285 to +12.8285 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.723 | −21.3% | −2.1716 to −0.3831 | yes: GAIN |
| node-hours | 2.518 | 1.979 | −21.4% | −0.9136 to −0.1657 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.2 | 273.4 | −0.3% | −1.8860 to +0.2855 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.2 | 233.2 | −14.9% | −69.1432 to −12.7282 | yes: GAIN |
| response time (ms), mean | 443.3 | 456.1 | +2.9% | +0.5953 to +24.9589 | yes: LOSS |
| response time (ms), 95th percentile | 1779 | 1751 | −1.6% | −86.8222 to +30.4992 | no |
| response time (ms), 99th percentile | 2516 | 2586 | +2.8% | −192.0592 to +331.9382 | no |
| time over the response line (% of samples) | 17.27 | 18.08 | +4.7% | +0.0874 to +1.5341 | yes: LOSS |
| failed requests (%) | 0 | 0.0236 | +0.024 (native is 0) | −0.0120 to +0.0592 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9.7 | +6.6% | −0.0911 to +1.2911 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.9 | +14.900 (native is 0) | +11.5037 to +18.2963 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.98 | 19 | −13.6% | −6.5488 to +0.5888 | no |
| utilisation (used / allocatable) | 0.06446 | 0.08121 | +26.0% | +0.0042 to +0.0293 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.547 | 1.508 | −2.5% | −0.0760 to −0.0028 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06107 | +0.061 (native is 0) | +0.0523 to +0.0699 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.547 | 1.569 | +1.4% | −0.0207 to +0.0641 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 434.8 | 371.7 | −14.5% | −109.8152 to −16.3633 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.086 | 2.342 | +12.3% | +0.0589 to +0.4532 | yes: power given |
| pods started | 0.1 | 1.3 | +1200.0% | +0.3207 to +2.0793 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.4 | +1100.0% | +0.4221 to +3.9779 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.267 | +533.3% | +0.0579 to +2.0754 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.53 | 45.99 | +3.3% | +1.1209 to +1.8133 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 831 | 830.9 | −0.0% | −4.8978 to +4.6978 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.928 | −34.5% | −3.3130 to −0.8312 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5042 | 0.5417 | +7.4% | −0.8464 to +0.9214 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 4 | +471.4% | −2.0957 to +8.6957 | no |
| queue: job turnaround, submitted to done, mean (s) | 139.9 | 136.3 | −2.5% | −11.4342 to +4.3092 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.888 | −18.5% | −1.8884 to −0.3364 | yes: GAIN |
| node-hours | 2.513 | 2.048 | −18.5% | −0.7914 to −0.1388 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 272.7 | −0.3% | −2.4733 to +0.8436 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 237.8 | −13.1% | −61.3149 to −10.2314 | yes: GAIN |
| response time (ms), mean | 445.4 | 471 | +5.8% | −2.3724 to +53.6601 | no |
| response time (ms), 95th percentile | 1720 | 1887 | +9.7% | +9.5502 to +323.1628 | yes: LOSS |
| response time (ms), 99th percentile | 2420 | 2726 | +12.7% | +35.3073 to +577.4735 | yes: LOSS |
| time over the response line (% of samples) | 17.88 | 17.23 | −3.6% | −1.3062 to +0.0153 | no |
| failed requests (%) | 0 | 0.0236 | +0.024 (native is 0) | −0.0120 to +0.0592 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 9.8 | +3.2% | −0.5953 to +1.1953 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.3 | +13.300 (native is 0) | +8.8899 to +17.7101 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.45 | 24.82 | +50.9% | +1.4108 to +15.3292 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06432 | 0.074 | +15.1% | +0.0037 to +0.0156 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.544 | 1.462 | −5.3% | −0.1683 to +0.0041 | no |
| Omni's own CPU (cores), mean | 0 | 0.06633 | +0.066 (native is 0) | +0.0570 to +0.0757 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.544 | 1.528 | −1.0% | −0.1103 to +0.0788 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 436.5 | 401 | −8.1% | −58.6632 to −12.3406 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.033 | 2.207 | +8.6% | +0.0494 to +0.2988 | yes: power given |
| pods started | 0.2 | 0.3 | +50.0% | −0.6113 to +0.8113 | no |
| pod start wait, total (s) | 0.6 | 0.6 | ±0.0% | −1.7843 to +1.7843 | no |
| pod start wait, mean (s) | 0.3 | 0.4 | +33.3% | −0.8802 to +1.0802 | no |
| host CPU busy, the real machine under kind (%) | 44.04 | 46.99 | +6.7% | +2.1616 to +3.7230 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 824.9 | 840.1 | +1.8% | +4.0837 to +26.3163 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.998 | −33.4% | −3.2538 to −0.7493 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3708 | 0.4542 | +22.5% | −0.1636 to +0.3303 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.6 | +14.3% | −1.7015 to +2.1015 | no |
| queue: job turnaround, submitted to done, mean (s) | 130.1 | 146.3 | +12.5% | +2.6354 to +29.8313 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*