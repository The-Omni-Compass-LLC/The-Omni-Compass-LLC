# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.05 | 4.92 |
| node-hours | 2.514 | 2.516 | 2.115 | 2.066 |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273.4 | 272.9 | 273.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 273.4 | 243.1 | 239.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 371.5 | 314.8 | 356.5 | 309.6 |
| response time (ms), 95th percentile | 1331 | 1180 | 1451 | 1398 |
| response time (ms), 99th percentile | 1884 | 1803 | 1985 | 1962 |
| time over the response line (% of samples) | 16.05 | 11.14 | 16.39 | 11.58 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 7.1 | 8.5 | 7.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 125.2 | 105.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 16.67 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.37 | 17.75 | 13.43 | 19.99 |
| utilisation (used / allocatable) | 0.06199 | 0.06246 | 0.07441 | 0.0763 |
| CPU used (cores), mean | 1.488 | 1.499 | 1.472 | 1.476 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0727 | 0.07592 |
| CPU used with Omni's own (cores), mean | 1.488 | 1.499 | 1.544 | 1.552 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.8 | 445.1 | 397.7 | 389.1 |
| HPA replicas, mean | 1.928 | 1.969 | 2.323 | 2.029 |
| pods started | 0.2 | 0 | 1.5 | 0.3 |
| pod start wait, total (s) | 0.5 | 0 | 3.3 | 0.4 |
| pod start wait, mean (s) | 0.5 | 0 | 1.45 | 0.3 |
| host CPU busy, the real machine under kind (%) | 42.63 | 43.48 | 45.72 | 46.68 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 795.8 | 806 | 802.9 | 816 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.454 | 4.183 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2208 | 0.8625 | 0.2083 | 0.8 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 2 | 1 | 1.7 |
| queue: job turnaround, submitted to done, mean (s) | 100.4 | 117.8 | 108.6 | 127.1 |
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
| worker nodes in service, mean | 6 | 4.92 | −18.0% | −1.9033 to −0.2561 | yes: GAIN |
| node-hours | 2.516 | 2.066 | −17.9% | −0.7999 to −0.1008 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.5 | +0.0% | −1.0289 to +1.1767 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 239.6 | −12.4% | −60.5185 to −7.1670 | yes: GAIN |
| response time (ms), mean | 314.8 | 309.6 | −1.7% | −26.3715 to +15.9037 | no |
| response time (ms), 95th percentile | 1180 | 1398 | +18.4% | +3.6336 to +431.4064 | yes: LOSS |
| response time (ms), 99th percentile | 1803 | 1962 | +8.8% | +13.0006 to +303.9166 | yes: LOSS |
| time over the response line (% of samples) | 11.14 | 11.58 | +4.0% | −0.3752 to +1.2646 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 7.3 | +2.8% | −0.2524 to +0.6524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 105.2 | +105.200 (native is 0) | +40.9365 to +169.4635 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.75 | 19.99 | +12.6% | −1.0849 to +5.5716 | no |
| utilisation (used / allocatable) | 0.06246 | 0.0763 | +22.2% | +0.0031 to +0.0246 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.499 | 1.476 | −1.5% | −0.0594 to +0.0136 | no |
| Omni's own CPU (cores), mean | 0 | 0.07592 | +0.076 (native is 0) | +0.0700 to +0.0819 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.499 | 1.552 | +3.5% | +0.0124 to +0.0937 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.1 | 389.1 | −12.6% | −96.9896 to −14.8844 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.969 | 2.029 | +3.0% | −0.1337 to +0.2536 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2032 to +1.0032 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| host CPU busy, the real machine under kind (%) | 43.48 | 46.68 | +7.4% | +2.8947 to +3.5111 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 806 | 816 | +1.2% | +2.4827 to +17.5173 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.183 | −30.3% | −3.0428 to −0.5911 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8625 | 0.8 | −7.2% | −0.3277 to +0.2027 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2 | 1.7 | −15.0% | −1.5181 to +0.9181 | no |
| queue: job turnaround, submitted to done, mean (s) | 117.8 | 127.1 | +7.9% | +2.9531 to +15.6969 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.514 | 2.516 | +0.1% | −0.0059 to +0.0099 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273.4 | +0.1% | −0.2304 to +0.9493 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 273.4 | +0.1% | −0.2304 to +0.9493 | no |
| response time (ms), mean | 371.5 | 314.8 | −15.3% | −88.1187 to −25.3166 | yes: GAIN |
| response time (ms), 95th percentile | 1331 | 1180 | −11.3% | −297.1333 to −3.7057 | yes: GAIN |
| response time (ms), 99th percentile | 1884 | 1803 | −4.3% | −310.0178 to +148.1018 | no |
| time over the response line (% of samples) | 16.05 | 11.14 | −30.6% | −8.5164 to −1.3062 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 7.1 | −17.4% | −3.1259 to +0.1259 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.37 | 17.75 | +43.5% | +2.4478 to +8.3088 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06199 | 0.06246 | +0.8% | −0.0007 to +0.0016 | no |
| CPU used (cores), mean | 1.488 | 1.499 | +0.8% | −0.0170 to +0.0395 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.488 | 1.499 | +0.8% | −0.0170 to +0.0395 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.8 | 445.1 | −0.8% | −11.4001 to +3.9379 | no |
| HPA replicas, mean | 1.928 | 1.969 | +2.1% | −0.0568 to +0.1383 | no |
| pods started | 0.2 | 0 | −100.0% | −0.5016 to +0.1016 | no |
| pod start wait, total (s) | 0.5 | 0 | −100.0% | −1.2726 to +0.2726 | no |
| pod start wait, mean (s) | 0.5 | 0 | −100.0% | −1.2726 to +0.2726 | no |
| host CPU busy, the real machine under kind (%) | 42.63 | 43.48 | +2.0% | +0.2051 to +1.5014 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 795.8 | 806 | +1.3% | −1.6922 to +22.0922 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2208 | 0.8625 | +290.6% | +0.2707 to +1.0126 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 2 | +81.8% | −0.6617 to +2.4617 | no |
| queue: job turnaround, submitted to done, mean (s) | 100.4 | 117.8 | +17.3% | +2.0900 to +32.6183 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.05 | −15.8% | −1.7684 to −0.1317 | yes: GAIN |
| node-hours | 2.514 | 2.115 | −15.9% | −0.7433 to −0.0541 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 272.9 | −0.0% | −1.0249 to +0.8154 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 243.1 | −11.0% | −56.0829 to −3.8558 | yes: GAIN |
| response time (ms), mean | 371.5 | 356.5 | −4.0% | −32.0269 to +1.9794 | no |
| response time (ms), 95th percentile | 1331 | 1451 | +9.0% | +39.1374 to +201.5276 | yes: LOSS |
| response time (ms), 99th percentile | 1884 | 1985 | +5.4% | −15.1201 to +216.7839 | no |
| time over the response line (% of samples) | 16.05 | 16.39 | +2.2% | −0.4687 to +1.1635 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 8.5 | −1.2% | −0.7263 to +0.5263 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 125.2 | +125.200 (native is 0) | +50.6014 to +199.7986 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.37 | 13.43 | +8.6% | −1.4304 to +3.5471 | no |
| utilisation (used / allocatable) | 0.06199 | 0.07441 | +20.0% | +0.0009 to +0.0239 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.488 | 1.472 | −1.1% | −0.0464 to +0.0142 | no |
| Omni's own CPU (cores), mean | 0 | 0.0727 | +0.073 (native is 0) | +0.0678 to +0.0776 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.488 | 1.544 | +3.8% | +0.0223 to +0.0910 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.8 | 397.7 | −11.4% | −95.7369 to −6.3978 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.928 | 2.323 | +20.5% | +0.2238 to +0.5655 | yes: power given |
| pods started | 0.2 | 1.5 | +650.0% | +0.4047 to +2.1953 | yes: power given |
| pod start wait, total (s) | 0.5 | 3.3 | +560.0% | +0.6996 to +4.9004 | yes: LOSS |
| pod start wait, mean (s) | 0.5 | 1.45 | +190.0% | +0.2064 to +1.6936 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.63 | 45.72 | +7.3% | +2.6768 to +3.5059 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 795.8 | 802.9 | +0.9% | −0.5482 to +14.7482 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.454 | −25.8% | −2.7432 to −0.3480 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2208 | 0.2083 | −5.7% | −0.1788 to +0.1538 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 1 | −9.1% | −0.9564 to +0.7564 | no |
| queue: job turnaround, submitted to done, mean (s) | 100.4 | 108.6 | +8.1% | +0.6410 to +15.6007 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.05 | −15.8% | −1.7684 to −0.1317 | yes: GAIN |
| node-hours | 2.516 | 2.115 | −15.9% | −0.7430 to −0.0584 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 272.9 | −0.2% | −1.1288 to +0.2004 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 243.1 | −11.1% | −56.2919 to −4.3656 | yes: GAIN |
| response time (ms), mean | 314.8 | 356.5 | +13.2% | +13.0222 to +70.3656 | yes: LOSS |
| response time (ms), 95th percentile | 1180 | 1451 | +22.9% | +154.0289 to +387.4751 | yes: LOSS |
| response time (ms), 99th percentile | 1803 | 1985 | +10.1% | −17.0304 to +380.6102 | no |
| time over the response line (% of samples) | 11.14 | 16.39 | +47.2% | +1.2482 to +9.2692 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 8.5 | +19.7% | +0.0854 to +2.7146 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 125.2 | +125.200 (native is 0) | +50.6014 to +199.7986 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.75 | 13.43 | −24.3% | −6.4856 to −2.1544 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06246 | 0.07441 | +19.1% | +0.0008 to +0.0231 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.499 | 1.472 | −1.8% | −0.0596 to +0.0049 | no |
| Omni's own CPU (cores), mean | 0 | 0.0727 | +0.073 (native is 0) | +0.0678 to +0.0776 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.499 | 1.544 | +3.0% | +0.0089 to +0.0818 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.1 | 397.7 | −10.6% | −88.8102 to −5.8623 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.969 | 2.323 | +18.0% | +0.1504 to +0.5573 | yes: power given |
| pods started | 0 | 1.5 | +1.500 (native is 0) | +0.5315 to +2.4685 | yes: power given |
| pod start wait, total (s) | 0 | 3.3 | +3.300 (native is 0) | +0.9145 to +5.6855 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.45 | +1.450 (native is 0) | +0.6336 to +2.2664 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.48 | 45.72 | +5.1% | +1.9071 to +2.5691 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 806 | 802.9 | −0.4% | −9.6337 to +3.4337 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.454 | −25.8% | −2.7432 to −0.3480 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8625 | 0.2083 | −75.8% | −0.9063 to −0.4020 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2 | 1 | −50.0% | −1.8921 to −0.1079 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 117.8 | 108.6 | −7.8% | −18.1294 to −0.3373 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.92 | −18.0% | −1.9033 to −0.2561 | yes: GAIN |
| node-hours | 2.514 | 2.066 | −17.8% | −0.8006 to −0.0962 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273.5 | +0.2% | −0.8501 to +1.7168 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 239.6 | −12.3% | −60.3610 to −6.6056 | yes: GAIN |
| response time (ms), mean | 371.5 | 309.6 | −16.7% | −76.2249 to −47.6782 | yes: GAIN |
| response time (ms), 95th percentile | 1331 | 1398 | +5.0% | −195.6227 to +329.8237 | no |
| response time (ms), 99th percentile | 1884 | 1962 | +4.1% | −178.9488 to +333.9500 | no |
| time over the response line (% of samples) | 16.05 | 11.58 | −27.8% | −7.6065 to −1.3268 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.6 | 7.3 | −15.1% | −2.8099 to +0.2099 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 105.2 | +105.200 (native is 0) | +40.9365 to +169.4635 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.37 | 19.99 | +61.6% | +3.9643 to +11.2790 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06199 | 0.0763 | +23.1% | +0.0032 to +0.0254 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.488 | 1.476 | −0.8% | −0.0449 to +0.0216 | no |
| Omni's own CPU (cores), mean | 0 | 0.07592 | +0.076 (native is 0) | +0.0700 to +0.0819 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.488 | 1.552 | +4.3% | +0.0268 to +0.1018 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.8 | 389.1 | −13.3% | −103.7082 to −15.6279 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.928 | 2.029 | +5.2% | −0.0907 to +0.2921 | no |
| pods started | 0.2 | 0.3 | +50.0% | −0.3060 to +0.5060 | no |
| pod start wait, total (s) | 0.5 | 0.4 | −20.0% | −0.9564 to +0.7564 | no |
| pod start wait, mean (s) | 0.5 | 0.3 | −40.0% | −1.0793 to +0.6793 | no |
| host CPU busy, the real machine under kind (%) | 42.63 | 46.68 | +9.5% | +3.4283 to +4.6839 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 795.8 | 816 | +2.5% | +5.2077 to +35.1923 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.183 | −30.3% | −3.0428 to −0.5911 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2208 | 0.8 | +262.3% | +0.1606 to +0.9977 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 1.7 | +54.5% | −1.4566 to +2.6566 | no |
| queue: job turnaround, submitted to done, mean (s) | 100.4 | 127.1 | +26.6% | +7.0186 to +46.3397 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*