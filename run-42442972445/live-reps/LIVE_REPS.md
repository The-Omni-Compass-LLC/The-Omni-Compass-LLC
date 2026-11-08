# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.837 | 6 |
| node-hours | 2.51 | 2.513 | 2.027 | 2.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.1 | 272.6 | 271.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 272.1 | 236 | 271.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 334 | 134.8 | 330.8 | 113.1 |
| response time (ms), 95th percentile | 1164 | 232.9 | 1361 | 258.2 |
| response time (ms), 99th percentile | 1628 | 350.2 | 1897 | 374.6 |
| time over the response line (% of samples) | 15.09 | 0.2378 | 16.63 | 0.3184 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 0.1 | 10.2 | 0.1111 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 125.2 | 101.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.46 | 1132 | 10.34 | 1281 |
| utilisation (used / allocatable) | 0.06021 | 0.06042 | 0.07591 | 0.05882 |
| CPU used (cores), mean | 1.445 | 1.45 | 1.436 | 1.412 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.074 | 0.07091 |
| CPU used with Omni's own (cores), mean | 1.445 | 1.45 | 1.51 | 1.483 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459 | 448.2 | 393.2 | 459.3 |
| HPA replicas, mean | 1.949 | 2.038 | 2.288 | 2.002 |
| pods started | 0 | 0 | 1.3 | 0.1111 |
| pod start wait, total (s) | 0 | 0 | 3.3 | 0.1111 |
| pod start wait, mean (s) | 0 | 0 | 1.2 | 0.1111 |
| host CPU busy, the real machine under kind (%) | 41.26 | 45.19 | 44.21 | 46.97 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 775.7 | 1459 | 783.8 | 1490 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.083 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 158.1 | 0.04583 | 196.6 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 756.1 | 0.3 | 797 |
| queue: job turnaround, submitted to done, mean (s) | 82.22 | 849.7 | 92.03 | 891.4 |
| queue: jobs unfinished at the window's end | 0 | 10.7 | 0 | 12.11 |
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

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 9 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.514 | 2.516 | +0.0% | −0.0065 to +0.0087 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.8 | −0.1% | −1.1603 to +0.3781 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 271.8 | −0.1% | −1.1603 to +0.3781 | no |
| response time (ms), mean | 135.1 | 113.1 | −16.3% | −26.2056 to −17.9462 | yes: GAIN |
| response time (ms), 95th percentile | 236.6 | 258.2 | +9.1% | +5.3413 to +37.8487 | yes: LOSS |
| response time (ms), 99th percentile | 357.2 | 374.6 | +4.9% | −7.5560 to +42.4240 | no |
| time over the response line (% of samples) | 0.2642 | 0.3184 | +20.5% | −0.0709 to +0.1793 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1111 | 0.1111 | ±0.0% | −0.3843 to +0.3843 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 101.6 | +101.556 (native is 0) | +92.0003 to +111.1108 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1164 | 1281 | +10.1% | +46.5807 to +189.1230 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06032 | 0.05882 | −2.5% | −0.0028 to −0.0002 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.448 | 1.412 | −2.5% | −0.0683 to −0.0038 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07091 | +0.071 (native is 0) | +0.0630 to +0.0788 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.448 | 1.483 | +2.4% | +0.0069 to +0.0629 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.9 | 459.3 | +2.3% | +0.8726 to +19.7550 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.047 | 2.002 | −2.2% | −0.1703 to +0.0816 | no |
| pods started | 0 | 0.1111 | +0.111 (native is 0) | −0.1451 to +0.3673 | no |
| pod start wait, total (s) | 0 | 0.1111 | +0.111 (native is 0) | −0.1451 to +0.3673 | no |
| pod start wait, mean (s) | 0 | 0.1111 | +0.111 (native is 0) | −0.1451 to +0.3673 | no |
| host CPU busy, the real machine under kind (%) | 45.27 | 46.97 | +3.8% | +1.0785 to +2.3353 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1454 | 1490 | +2.5% | −15.0848 to +86.8626 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 158.3 | 196.6 | +24.2% | +7.3566 to +69.1342 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 740.2 | 797 | +7.7% | −159.5865 to +273.1420 | no |
| queue: job turnaround, submitted to done, mean (s) | 869.6 | 891.4 | +2.5% | −46.8661 to +90.3568 | no |
| queue: jobs unfinished at the window's end | 11.33 | 12.11 | +6.9% | −2.3629 to +3.9185 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.51 | 2.514 | +0.1% | −0.0043 to +0.0106 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.1 | −0.0% | −2.0807 to +2.0678 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 272.1 | −0.0% | −2.0807 to +2.0678 | no |
| response time (ms), mean | 334 | 134.8 | −59.6% | −337.6739 to −60.6329 | yes: GAIN |
| response time (ms), 95th percentile | 1164 | 232.9 | −80.0% | −1591.1890 to −271.0560 | yes: GAIN |
| response time (ms), 99th percentile | 1628 | 350.2 | −78.5% | −2171.1610 to −384.3868 | yes: GAIN |
| time over the response line (% of samples) | 15.09 | 0.2378 | −98.4% | −25.2853 to −4.4125 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 0.1 | −98.9% | −13.2894 to −4.5106 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.46 | 1132 | +11870.9% | +872.1297 to +1373.8436 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06021 | 0.06042 | +0.3% | −0.0056 to +0.0060 | no |
| CPU used (cores), mean | 1.445 | 1.45 | +0.3% | −0.1345 to +0.1446 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.445 | 1.45 | +0.3% | −0.1345 to +0.1446 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459 | 448.2 | −2.4% | −51.6485 to +30.0230 | no |
| HPA replicas, mean | 1.949 | 2.038 | +4.6% | −0.0347 to +0.2132 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 41.26 | 45.19 | +9.5% | +0.8537 to +7.0086 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 775.7 | 1459 | +88.1% | +613.2262 to +754.1738 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 158.1 | +474087.5% | +123.8158 to +192.2426 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 756.1 | +377950.0% | +579.9876 to +931.8124 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 82.22 | 849.7 | +933.4% | +644.9410 to +889.9757 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 10.7 | +10.700 (native is 0) | +4.6959 to +16.7041 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.837 | −19.4% | −1.9992 to −0.3270 | yes: GAIN |
| node-hours | 2.51 | 2.027 | −19.2% | −0.8341 to −0.1319 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.6 | +0.2% | −0.5223 to +1.5607 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 236 | −13.3% | −62.7266 to −9.4100 | yes: GAIN |
| response time (ms), mean | 334 | 330.8 | −0.9% | −18.9354 to +12.6384 | no |
| response time (ms), 95th percentile | 1164 | 1361 | +16.9% | +73.2532 to +320.9028 | yes: LOSS |
| response time (ms), 99th percentile | 1628 | 1897 | +16.5% | +85.5998 to +452.6558 | yes: LOSS |
| time over the response line (% of samples) | 15.09 | 16.63 | +10.2% | −0.8605 to +3.9416 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 10.2 | +13.3% | −0.0972 to +2.4972 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 125.2 | +125.200 (native is 0) | +51.0861 to +199.3139 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.46 | 10.34 | +9.3% | −0.7997 to +2.5597 | no |
| utilisation (used / allocatable) | 0.06021 | 0.07591 | +26.1% | +0.0043 to +0.0271 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.445 | 1.436 | −0.6% | −0.0359 to +0.0181 | no |
| Omni's own CPU (cores), mean | 0 | 0.074 | +0.074 (native is 0) | +0.0663 to +0.0817 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.445 | 1.51 | +4.5% | +0.0327 to +0.0975 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459 | 393.2 | −14.3% | −111.6008 to −20.0310 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.949 | 2.288 | +17.4% | +0.0774 to +0.6003 | yes: power given |
| pods started | 0 | 1.3 | +1.300 (native is 0) | +0.0819 to +2.5181 | yes: power given |
| pod start wait, total (s) | 0 | 3.3 | +3.300 (native is 0) | +0.1002 to +6.4998 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.2 | +1.200 (native is 0) | +0.2735 to +2.1265 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.26 | 44.21 | +7.1% | +2.4375 to +3.4622 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 775.7 | 783.8 | +1.0% | +2.5546 to +13.6454 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.083 | −31.9% | −3.1607 to −0.6731 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.04583 | +37.5% | −0.0221 to +0.0471 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.3 | +50.0% | −0.3060 to +0.5060 | no |
| queue: job turnaround, submitted to done, mean (s) | 82.22 | 92.03 | +11.9% | +3.0397 to +16.5686 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.837 | −19.4% | −1.9992 to −0.3270 | yes: GAIN |
| node-hours | 2.513 | 2.027 | −19.3% | −0.8371 to −0.1353 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.6 | +0.2% | −2.0790 to +3.1304 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 236 | −13.3% | −64.3727 to −7.7510 | yes: GAIN |
| response time (ms), mean | 134.8 | 330.8 | +145.4% | +53.0648 to +338.9450 | yes: LOSS |
| response time (ms), 95th percentile | 232.9 | 1361 | +484.4% | +382.0948 to +1874.3062 | yes: LOSS |
| response time (ms), 99th percentile | 350.2 | 1897 | +441.7% | +524.0755 to +2569.7279 | yes: LOSS |
| time over the response line (% of samples) | 0.2378 | 16.63 | +6892.9% | +6.6774 to +26.1015 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 10.2 | +10100.0% | +6.2635 to +13.9365 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 125.2 | +125.200 (native is 0) | +51.0861 to +199.3139 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1132 | 10.34 | −99.1% | −1371.8796 to −872.3337 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06042 | 0.07591 | +25.6% | +0.0077 to +0.0233 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.45 | 1.436 | −1.0% | −0.1749 to +0.1471 | no |
| Omni's own CPU (cores), mean | 0 | 0.074 | +0.074 (native is 0) | +0.0663 to +0.0817 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.45 | 1.51 | +4.1% | −0.1047 to +0.2248 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.2 | 393.2 | −12.3% | −79.1447 to −30.8617 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.038 | 2.288 | +12.2% | −0.0499 to +0.5491 | no |
| pods started | 0 | 1.3 | +1.300 (native is 0) | +0.0819 to +2.5181 | yes: power given |
| pod start wait, total (s) | 0 | 3.3 | +3.300 (native is 0) | +0.1002 to +6.4998 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.2 | +1.200 (native is 0) | +0.2735 to +2.1265 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.19 | 44.21 | −2.2% | −4.3150 to +2.3524 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1459 | 783.8 | −46.3% | −746.1699 to −605.0301 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | −4.0000 to −4.0000 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 158.1 | 0.04583 | −100.0% | −192.2165 to −123.8168 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 756.1 | 0.3 | −100.0% | −931.6644 to −579.9356 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 849.7 | 92.03 | −89.2% | −875.2173 to −640.0910 | yes: GAIN |
| queue: jobs unfinished at the window's end | 10.7 | 0 | −100.0% | −16.7041 to −4.6959 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.51 | 2.516 | +0.2% | −0.0026 to +0.0141 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 271.8 | −0.2% | −3.0537 to +2.0260 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 271.8 | −0.2% | −3.0537 to +2.0260 | no |
| response time (ms), mean | 351.1 | 113.1 | −67.8% | −391.6428 to −84.3637 | yes: GAIN |
| response time (ms), 95th percentile | 1245 | 258.2 | −79.3% | −1702.2544 to −271.0045 | yes: GAIN |
| response time (ms), 99th percentile | 1741 | 374.6 | −78.5% | −2334.6561 to −398.8853 | yes: GAIN |
| time over the response line (% of samples) | 16.41 | 0.3184 | −98.1% | −27.4341 to −4.7404 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.222 | 0.1111 | −98.8% | −14.0396 to −4.1826 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 101.6 | +101.556 (native is 0) | +92.0003 to +111.1108 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.624 | 1281 | +13215.3% | +1013.6984 to +1529.9979 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06086 | 0.05882 | −3.4% | −0.0091 to +0.0050 | no |
| CPU used (cores), mean | 1.461 | 1.412 | −3.4% | −0.2191 to +0.1211 | no |
| Omni's own CPU (cores), mean | 0 | 0.07091 | +0.071 (native is 0) | +0.0630 to +0.0788 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.461 | 1.483 | +1.5% | −0.1414 to +0.1852 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.1 | 459.3 | +0.9% | −46.0099 to +54.3196 | no |
| HPA replicas, mean | 1.953 | 2.002 | +2.5% | −0.0939 to +0.1924 | no |
| pods started | 0 | 0.1111 | +0.111 (native is 0) | −0.1451 to +0.3673 | no |
| pod start wait, total (s) | 0 | 0.1111 | +0.111 (native is 0) | −0.1451 to +0.3673 | no |
| pod start wait, mean (s) | 0 | 0.1111 | +0.111 (native is 0) | −0.1451 to +0.3673 | no |
| host CPU busy, the real machine under kind (%) | 41.73 | 46.97 | +12.6% | +1.7591 to +8.7365 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 781.6 | 1490 | +90.7% | +657.3341 to +759.9993 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02778 | 196.6 | +707566.7% | +149.1688 to +243.9238 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1111 | 797 | +717200.0% | +579.4131 to +1014.3647 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 88.04 | 891.4 | +912.5% | +692.7843 to +913.9101 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12.11 | +12.111 (native is 0) | +5.7673 to +18.4549 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*