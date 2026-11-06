# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.063 | 6 |
| node-hours | 2.513 | 2.52 | 2.123 | 2.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.7 | 272.9 | 272.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 272.7 | 243.4 | 272.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 366.5 | 130.7 | 354.2 | 109.7 |
| response time (ms), 95th percentile | 1307 | 229.6 | 1480 | 241.7 |
| response time (ms), 99th percentile | 1921 | 325.6 | 2192 | 352.3 |
| time over the response line (% of samples) | 16.83 | 0.2312 | 16.46 | 0.2642 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 0 | 9.4 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 136.6 | 116.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 50 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.42 | 1127 | 11.12 | 1286 |
| utilisation (used / allocatable) | 0.06025 | 0.06012 | 0.07274 | 0.05891 |
| CPU used (cores), mean | 1.446 | 1.443 | 1.452 | 1.414 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07123 | 0.07021 |
| CPU used with Omni's own (cores), mean | 1.446 | 1.443 | 1.523 | 1.484 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.9 | 450.6 | 404 | 458.5 |
| HPA replicas, mean | 1.945 | 2.02 | 2.416 | 2.253 |
| pods started | 0.1 | 0 | 1.6 | 0.9 |
| pod start wait, total (s) | 0.2 | 0 | 4 | 1.6 |
| pod start wait, mean (s) | 0.2 | 0 | 1.675 | 0.8667 |
| host CPU busy, the real machine under kind (%) | 41.3 | 44.94 | 44.33 | 46.94 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 786.3 | 1454 | 796.2 | 1508 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.453 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 153.6 | 0.05417 | 180.3 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 755.6 | 0.4 | 754.5 |
| queue: job turnaround, submitted to done, mean (s) | 92.84 | 819.8 | 102.1 | 902 |
| queue: jobs unfinished at the window's end | 0 | 10.7 | 0 | 12.2 |
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
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 2.52 | 2.519 | −0.0% | −0.0109 to +0.0089 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.1 | −0.2% | −1.5110 to +0.3786 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 272.1 | −0.2% | −1.5110 to +0.3786 | no |
| response time (ms), mean | 130.7 | 109.7 | −16.1% | −30.3432 to −11.7499 | yes: GAIN |
| response time (ms), 95th percentile | 229.6 | 241.7 | +5.3% | −3.5980 to +27.8000 | no |
| response time (ms), 99th percentile | 325.6 | 352.3 | +8.2% | +1.0366 to +52.3252 | yes: LOSS |
| time over the response line (% of samples) | 0.2312 | 0.2642 | +14.3% | −0.0934 to +0.1595 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 116.1 | +116.100 (native is 0) | +99.6274 to +132.5726 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1127 | 1286 | +14.1% | +78.6300 to +239.8433 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06012 | 0.05891 | −2.0% | −0.0027 to +0.0003 | no |
| CPU used (cores), mean | 1.443 | 1.414 | −2.0% | −0.0641 to +0.0062 | no |
| Omni's own CPU (cores), mean | 0 | 0.07021 | +0.070 (native is 0) | +0.0625 to +0.0779 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.443 | 1.484 | +2.9% | +0.0069 to +0.0757 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.6 | 458.5 | +1.8% | −2.6127 to +18.4968 | no |
| HPA replicas, mean | 2.02 | 2.253 | +11.5% | +0.0571 to +0.4090 | yes: power given |
| pods started | 0 | 0.9 | +0.900 (native is 0) | −0.0204 to +1.8204 | no |
| pod start wait, total (s) | 0 | 1.6 | +1.600 (native is 0) | +0.0845 to +3.1155 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.8667 | +0.867 (native is 0) | −0.0950 to +1.8283 | no |
| host CPU busy, the real machine under kind (%) | 44.94 | 46.94 | +4.4% | +1.2885 to +2.7104 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1454 | 1508 | +3.7% | −19.9187 to +128.7187 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 153.6 | 180.3 | +17.4% | −1.1446 to +54.6030 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 755.6 | 754.5 | −0.1% | −176.8915 to +174.6915 | no |
| queue: job turnaround, submitted to done, mean (s) | 819.8 | 902 | +10.0% | +10.2468 to +154.1032 | yes: LOSS |
| queue: jobs unfinished at the window's end | 10.7 | 12.2 | +14.0% | −1.1817 to +4.1817 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.513 | 2.52 | +0.3% | −0.0000 to +0.0137 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.7 | +0.1% | −2.5189 to +3.2096 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 272.7 | +0.1% | −2.5189 to +3.2096 | no |
| response time (ms), mean | 366.5 | 130.7 | −64.3% | −382.1909 to −89.4536 | yes: GAIN |
| response time (ms), 95th percentile | 1307 | 229.6 | −82.4% | −1775.3616 to −379.6484 | yes: GAIN |
| response time (ms), 99th percentile | 1921 | 325.6 | −83.0% | −2639.0674 to −551.7336 | yes: GAIN |
| time over the response line (% of samples) | 16.83 | 0.2312 | −98.6% | −28.2269 to −4.9773 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 0 | −100.0% | −12.9673 to −3.0327 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.42 | 1127 | +10719.8% | +834.2738 to +1399.3695 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06025 | 0.06012 | −0.2% | −0.0071 to +0.0069 | no |
| CPU used (cores), mean | 1.446 | 1.443 | −0.2% | −0.1713 to +0.1650 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.446 | 1.443 | −0.2% | −0.1713 to +0.1650 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.9 | 450.6 | −2.4% | −61.4464 to +38.8422 | no |
| HPA replicas, mean | 1.945 | 2.02 | +3.9% | −0.0388 to +0.1889 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 41.3 | 44.94 | +8.8% | +0.1650 to +7.1185 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 786.3 | 1454 | +84.9% | +599.4039 to +735.1961 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 153.6 | +230287.5% | +111.9200 to +195.1300 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 755.6 | +188800.0% | +547.6960 to +962.7040 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 92.84 | 819.8 | +783.1% | +598.7410 to +855.2507 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 10.7 | +10.700 (native is 0) | +3.9894 to +17.4106 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.063 | −15.6% | −1.6962 to −0.1781 | yes: GAIN |
| node-hours | 2.513 | 2.123 | −15.5% | −0.7075 to −0.0733 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.9 | +0.2% | −0.4128 to +1.5818 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 243.4 | −10.6% | −52.7398 to −5.0786 | yes: GAIN |
| response time (ms), mean | 366.5 | 354.2 | −3.4% | −33.3787 to +8.5979 | no |
| response time (ms), 95th percentile | 1307 | 1480 | +13.2% | +52.8326 to +292.0264 | yes: LOSS |
| response time (ms), 99th percentile | 1921 | 2192 | +14.1% | +64.1812 to +478.0006 | yes: LOSS |
| time over the response line (% of samples) | 16.83 | 16.46 | −2.2% | −1.2662 to +0.5263 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 9.4 | +17.5% | +0.1293 to +2.6707 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 136.6 | +136.600 (native is 0) | +62.2867 to +210.9133 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.42 | 11.12 | +6.7% | −0.8575 to +2.2508 | no |
| utilisation (used / allocatable) | 0.06025 | 0.07274 | +20.7% | +0.0018 to +0.0231 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.446 | 1.452 | +0.4% | −0.0300 to +0.0411 | no |
| Omni's own CPU (cores), mean | 0 | 0.07123 | +0.071 (native is 0) | +0.0648 to +0.0776 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.446 | 1.523 | +5.3% | +0.0374 to +0.1161 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.9 | 404 | −12.5% | −104.3970 to −11.2746 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.945 | 2.416 | +24.2% | +0.1758 to +0.7648 | yes: power given |
| pods started | 0.1 | 1.6 | +1500.0% | +0.4204 to +2.5796 | yes: power given |
| pod start wait, total (s) | 0.2 | 4 | +1900.0% | +0.9229 to +6.6771 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.675 | +737.5% | +0.6052 to +2.3448 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.3 | 44.33 | +7.3% | +2.4064 to +3.6585 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 786.3 | 796.2 | +1.3% | +1.2869 to +18.5131 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.453 | −25.8% | −2.6717 to −0.4218 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.05417 | −18.7% | −0.0722 to +0.0472 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 | ±0.0% | −0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 92.84 | 102.1 | +9.9% | +1.7727 to +16.6856 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.063 | −15.6% | −1.6962 to −0.1781 | yes: GAIN |
| node-hours | 2.52 | 2.123 | −15.8% | −0.7145 to −0.0800 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.9 | +0.1% | −2.5513 to +3.0298 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 243.4 | −10.7% | −55.4308 to −3.0783 | yes: GAIN |
| response time (ms), mean | 130.7 | 354.2 | +170.9% | +67.1465 to +379.7171 | yes: LOSS |
| response time (ms), 95th percentile | 229.6 | 1480 | +544.4% | +450.9244 to +2048.9446 | yes: LOSS |
| response time (ms), 99th percentile | 325.6 | 2192 | +573.2% | +675.7543 to +3057.2285 | yes: LOSS |
| time over the response line (% of samples) | 0.2312 | 16.46 | +7021.6% | +5.3341 to +27.1302 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 9.4 | +9.400 (native is 0) | +5.0660 to +13.7340 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 136.6 | +136.600 (native is 0) | +62.2867 to +210.9133 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1127 | 11.12 | −99.0% | −1398.4292 to −833.8208 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06012 | 0.07274 | +21.0% | +0.0063 to +0.0190 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.443 | 1.452 | +0.6% | −0.1754 to +0.1928 | no |
| Omni's own CPU (cores), mean | 0 | 0.07123 | +0.071 (native is 0) | +0.0648 to +0.0776 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.443 | 1.523 | +5.5% | −0.1102 to +0.2700 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.6 | 404 | −10.3% | −69.4724 to −23.5950 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.02 | 2.416 | +19.6% | +0.0613 to +0.7291 | yes: power given |
| pods started | 0 | 1.6 | +1.600 (native is 0) | +0.5231 to +2.6769 | yes: power given |
| pod start wait, total (s) | 0 | 4 | +4.000 (native is 0) | +1.1190 to +6.8810 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.675 | +1.675 (native is 0) | +0.8151 to +2.5349 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.94 | 44.33 | −1.4% | −4.4877 to +3.2691 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1454 | 796.2 | −45.2% | −726.2094 to −588.5906 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.781 | −53.7% | −4.6034 to −1.8351 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 153.6 | 0.05417 | −100.0% | −195.1524 to −111.9226 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 755.6 | 0.4 | −99.9% | −962.7073 to −547.6927 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 819.8 | 102.1 | −87.6% | −840.9115 to −594.6218 | yes: GAIN |
| queue: jobs unfinished at the window's end | 10.7 | 0 | −100.0% | −17.4106 to −3.9894 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.513 | 2.519 | +0.2% | −0.0031 to +0.0148 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.1 | −0.1% | −3.0245 to +2.5828 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 272.1 | −0.1% | −3.0245 to +2.5828 | no |
| response time (ms), mean | 366.5 | 109.7 | −70.1% | −408.1951 to −105.5424 | yes: GAIN |
| response time (ms), 95th percentile | 1307 | 241.7 | −81.5% | −1756.1388 to −374.6692 | yes: GAIN |
| response time (ms), 99th percentile | 1921 | 352.3 | −81.7% | −2603.4981 to −533.9411 | yes: GAIN |
| time over the response line (% of samples) | 16.83 | 0.2642 | −98.4% | −28.1591 to −4.9791 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 0.1 | −98.8% | −12.8033 to −2.9967 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 116.1 | +116.100 (native is 0) | +99.6274 to +132.5726 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.42 | 1286 | +12248.2% | +1029.0555 to +1523.0612 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06025 | 0.05891 | −2.2% | −0.0087 to +0.0061 | no |
| CPU used (cores), mean | 1.446 | 1.414 | −2.2% | −0.2094 to +0.1453 | no |
| Omni's own CPU (cores), mean | 0 | 0.07021 | +0.070 (native is 0) | +0.0625 to +0.0779 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.446 | 1.484 | +2.6% | −0.1319 to +0.2082 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.9 | 458.5 | −0.7% | −56.6720 to +49.9519 | no |
| HPA replicas, mean | 1.945 | 2.253 | +15.8% | +0.0992 to +0.5170 | yes: power given |
| pods started | 0.1 | 0.9 | +800.0% | −0.2003 to +1.8003 | no |
| pod start wait, total (s) | 0.2 | 1.6 | +700.0% | −0.2927 to +3.0927 | no |
| pod start wait, mean (s) | 0.2 | 0.8667 | +333.3% | −0.4851 to +1.8184 | no |
| host CPU busy, the real machine under kind (%) | 41.3 | 46.94 | +13.7% | +2.0134 to +9.2690 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 786.3 | 1508 | +91.8% | +676.1581 to +767.2419 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 180.3 | +270381.2% | +145.9577 to +214.5507 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 754.5 | +188525.0% | +618.6943 to +889.5057 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 92.84 | 902 | +871.6% | +736.7929 to +881.5488 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12.2 | +12.200 (native is 0) | +6.5798 to +17.8202 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*