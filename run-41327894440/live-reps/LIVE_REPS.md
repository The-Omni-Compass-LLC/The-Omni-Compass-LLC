# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.315 | 5.99 |
| node-hours | 2.51 | 2.515 | 2.228 | 2.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 285.8 | 274.9 | 285.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 285.8 | 253.4 | 285.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 514.3 | 711.3 | 463.1 | 707.1 |
| response time (ms), 95th percentile | 2004 | 1429 | 1966 | 1443 |
| response time (ms), 99th percentile | 2881 | 1928 | 2854 | 1963 |
| time over the response line (% of samples) | 23.71 | 63.9 | 23.09 | 64.16 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 23.9 | 11 | 23.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 25.5 | 18 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.78 | 2.152 | 14.42 | 2.488 |
| utilisation (used / allocatable) | 0.06626 | 0.09555 | 0.07583 | 0.0955 |
| CPU used (cores), mean | 1.59 | 2.293 | 1.594 | 2.288 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0166 | 0.00972 |
| CPU used with Omni's own (cores), mean | 1.59 | 2.293 | 1.611 | 2.298 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 423.7 | 298.5 | 380.1 | 298.2 |
| HPA replicas, mean | 2.025 | 2.005 | 2.101 | 2.715 |
| pods started | 0.4 | 0 | 0.4 | 0.5 |
| pod start wait, total (s) | 0.5 | 0 | 0.7 | 1.3 |
| pod start wait, mean (s) | 0.25 | 0 | 0.7 | 1.05 |
| host CPU busy, the real machine under kind (%) | 45.25 | 74.35 | 46.32 | 74.79 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 837.5 | 1439 | 842.2 | 1444 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.838 | 5.773 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 668.5 | 0.1667 | 680 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1148 | 1.5 | 1124 |
| queue: job turnaround, submitted to done, mean (s) | 140.7 | 941.3 | 145.9 | 947.4 |
| queue: jobs unfinished at the window's end | 0 | 15.3 | 0 | 14.8 |
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
| worker nodes in service, mean | 6 | 5.99 | −0.2% | −0.0339 to +0.0131 | no |
| node-hours | 2.515 | 2.512 | −0.1% | −0.0148 to +0.0078 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 285.8 | 285.8 | +0.0% | −0.6275 to +0.6679 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.8 | 285.5 | −0.1% | −1.1117 to +0.5021 | no |
| response time (ms), mean | 711.3 | 707.1 | −0.6% | −52.0568 to +43.5559 | no |
| response time (ms), 95th percentile | 1429 | 1443 | +1.0% | −81.8263 to +109.9203 | no |
| response time (ms), 99th percentile | 1928 | 1963 | +1.8% | −106.6993 to +177.4777 | no |
| time over the response line (% of samples) | 63.9 | 64.16 | +0.4% | −3.4000 to +3.9206 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.9 | 23.9 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18 | +18.000 (native is 0) | +15.1190 to +20.8810 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.152 | 2.488 | +15.6% | −0.1490 to +0.8224 | no |
| utilisation (used / allocatable) | 0.09555 | 0.0955 | −0.0% | −0.0013 to +0.0012 | no |
| CPU used (cores), mean | 2.293 | 2.288 | −0.2% | −0.0281 to +0.0187 | no |
| Omni's own CPU (cores), mean | 0 | 0.00972 | +0.010 (native is 0) | +0.0087 to +0.0107 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.293 | 2.298 | +0.2% | −0.0177 to +0.0276 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 298.5 | 298.2 | −0.1% | −4.0440 to +3.5609 | no |
| HPA replicas, mean | 2.005 | 2.715 | +35.4% | +0.3990 to +1.0219 | yes: power given |
| pods started | 0 | 0.5 | +0.500 (native is 0) | −0.0058 to +1.0058 | no |
| pod start wait, total (s) | 0 | 1.3 | +1.300 (native is 0) | −0.1717 to +2.7717 | no |
| pod start wait, mean (s) | 0 | 1.05 | +1.050 (native is 0) | −0.1475 to +2.2475 | no |
| host CPU busy, the real machine under kind (%) | 74.35 | 74.79 | +0.6% | −0.0356 to +0.9071 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1439 | 1444 | +0.3% | −5.7514 to +14.7514 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.773 | −3.8% | −3.1150 to +2.6605 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 668.5 | 680 | +1.7% | −45.6778 to +68.5886 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1148 | 1124 | −2.1% | −62.1234 to +13.6406 | no |
| queue: job turnaround, submitted to done, mean (s) | 941.3 | 947.4 | +0.6% | −15.3809 to +27.4976 | no |
| queue: jobs unfinished at the window's end | 15.3 | 14.8 | −3.3% | −1.8168 to +0.8168 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.51 | 2.515 | +0.2% | −0.0024 to +0.0120 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 285.8 | +4.2% | +9.3724 to +13.5713 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 285.8 | +4.2% | +9.3724 to +13.5713 | yes: power given |
| response time (ms), mean | 514.3 | 711.3 | +38.3% | +121.6053 to +272.4017 | yes: LOSS |
| response time (ms), 95th percentile | 2004 | 1429 | −28.7% | −1197.7284 to +47.6224 | no |
| response time (ms), 99th percentile | 2881 | 1928 | −33.1% | −1944.7202 to +39.6430 | no |
| time over the response line (% of samples) | 23.71 | 63.9 | +169.5% | +31.5579 to +48.8171 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 23.9 | +111.5% | +9.5615 to +15.6385 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.78 | 2.152 | −83.2% | −13.1655 to −8.0879 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06626 | 0.09555 | +44.2% | +0.0239 to +0.0346 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.59 | 2.293 | +44.2% | +0.5744 to +0.8312 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.59 | 2.293 | +44.2% | +0.5744 to +0.8312 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 423.7 | 298.5 | −29.6% | −169.5684 to −80.8672 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.025 | 2.005 | −1.0% | −0.1983 to +0.1583 | no |
| pods started | 0.4 | 0 | −100.0% | −1.0032 to +0.2032 | no |
| pod start wait, total (s) | 0.5 | 0 | −100.0% | −1.2726 to +0.2726 | no |
| pod start wait, mean (s) | 0.25 | 0 | −100.0% | −0.6363 to +0.1363 | no |
| host CPU busy, the real machine under kind (%) | 45.25 | 74.35 | +64.3% | +26.6267 to +31.5808 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 837.5 | 1439 | +71.8% | +526.6119 to +676.5881 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 668.5 | +844367.6% | +422.3454 to +914.5700 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1148 | +229470.3% | +776.2058 to +1518.4967 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 140.7 | 941.3 | +569.2% | +653.2809 to +948.0941 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 15.3 | +15.300 (native is 0) | +9.4106 to +21.1894 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.315 | −11.4% | −1.4560 to +0.0862 | no |
| node-hours | 2.51 | 2.228 | −11.3% | −0.6062 to +0.0414 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 274.9 | +0.2% | −0.0338 to +1.2931 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 253.4 | −7.6% | −44.9464 to +3.2431 | no |
| response time (ms), mean | 514.3 | 463.1 | −10.0% | −88.4742 to −14.0567 | yes: GAIN |
| response time (ms), 95th percentile | 2004 | 1966 | −1.9% | −203.1635 to +128.5335 | no |
| response time (ms), 99th percentile | 2881 | 2854 | −0.9% | −360.9738 to +307.3408 | no |
| time over the response line (% of samples) | 23.71 | 23.09 | −2.6% | −1.5023 to +0.2459 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 11 | −2.7% | −1.2567 to +0.6567 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.5 | +25.500 (native is 0) | +13.8813 to +37.1187 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.78 | 14.42 | +12.8% | −1.1842 to +4.4642 | no |
| utilisation (used / allocatable) | 0.06626 | 0.07583 | +14.4% | −0.0016 to +0.0208 | no |
| CPU used (cores), mean | 1.59 | 1.594 | +0.2% | −0.0259 to +0.0338 | no |
| Omni's own CPU (cores), mean | 0 | 0.0166 | +0.017 (native is 0) | +0.0152 to +0.0180 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.59 | 1.611 | +1.3% | −0.0086 to +0.0497 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 423.7 | 380.1 | −10.3% | −96.1011 to +8.9461 | no |
| HPA replicas, mean | 2.025 | 2.101 | +3.8% | −0.0905 to +0.2430 | no |
| pods started | 0.4 | 0.4 | ±0.0% | −0.6744 to +0.6744 | no |
| pod start wait, total (s) | 0.5 | 0.7 | +40.0% | −0.8003 to +1.2003 | no |
| pod start wait, mean (s) | 0.25 | 0.7 | +180.0% | −0.3124 to +1.2124 | no |
| host CPU busy, the real machine under kind (%) | 45.25 | 46.32 | +2.4% | +0.3715 to +1.7749 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 837.5 | 842.2 | +0.6% | −6.2163 to +15.6163 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.838 | −19.4% | −2.4124 to +0.0875 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 0.1667 | +110.5% | −0.1851 to +0.3601 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1.5 | +200.0% | −1.5458 to +3.5458 | no |
| queue: job turnaround, submitted to done, mean (s) | 140.7 | 145.9 | +3.7% | −5.5303 to +16.0137 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.315 | −11.4% | −1.4560 to +0.0862 | no |
| node-hours | 2.515 | 2.228 | −11.4% | −0.6080 to +0.0335 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 285.8 | 274.9 | −3.8% | −12.9216 to −8.7629 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.8 | 253.4 | −11.3% | −57.6364 to −7.0106 | yes: GAIN |
| response time (ms), mean | 711.3 | 463.1 | −34.9% | −312.8302 to −183.7077 | yes: GAIN |
| response time (ms), 95th percentile | 1429 | 1966 | +37.6% | −58.4754 to +1133.9514 | no |
| response time (ms), 99th percentile | 1928 | 2854 | +48.0% | +2.7527 to +1848.6915 | yes: LOSS |
| time over the response line (% of samples) | 63.9 | 23.09 | −63.9% | −49.7525 to −31.8789 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.9 | 11 | −54.0% | −16.4277 to −9.3723 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.5 | +25.500 (native is 0) | +13.8813 to +37.1187 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.152 | 14.42 | +570.1% | +7.6783 to +16.8550 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09555 | 0.07583 | −20.6% | −0.0280 to −0.0114 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.293 | 1.594 | −30.5% | −0.8304 to −0.5672 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0166 | +0.017 (native is 0) | +0.0152 to +0.0180 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.293 | 1.611 | −29.8% | −0.8144 to −0.5501 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 298.5 | 380.1 | +27.4% | +65.1729 to +98.1078 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.005 | 2.101 | +4.8% | −0.0376 to +0.2301 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | +0.0306 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 0.7 | +0.700 (native is 0) | +0.0214 to +1.3786 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.7 | +0.700 (native is 0) | +0.0214 to +1.3786 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 74.35 | 46.32 | −37.7% | −30.6803 to −25.3810 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1439 | 842.2 | −41.5% | −671.0266 to −522.7734 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | −4.0000 to −4.0000 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 668.5 | 0.1667 | −100.0% | −914.4395 to −422.3009 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1148 | 1.5 | −99.9% | −1517.0325 to −775.6700 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 941.3 | 145.9 | −84.5% | −941.5218 to −649.3698 | yes: GAIN |
| queue: jobs unfinished at the window's end | 15.3 | 0 | −100.0% | −21.1894 to −9.4106 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.99 | −0.2% | −0.0339 to +0.0131 | no |
| node-hours | 2.51 | 2.512 | +0.1% | −0.0156 to +0.0182 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 285.8 | +4.2% | +8.9753 to +14.0089 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 285.5 | +4.1% | +8.6338 to +13.7003 | yes: power given |
| response time (ms), mean | 514.3 | 707.1 | +37.5% | +124.0483 to +261.4578 | yes: LOSS |
| response time (ms), 95th percentile | 2004 | 1443 | −28.0% | −1201.2103 to +79.1983 | no |
| response time (ms), 99th percentile | 2881 | 1963 | −31.8% | −1894.1814 to +59.8826 | no |
| time over the response line (% of samples) | 23.71 | 64.16 | +170.6% | +34.3647 to +46.5309 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 23.9 | +111.5% | +9.5615 to +15.6385 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18 | +18.000 (native is 0) | +15.1190 to +20.8810 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.78 | 2.488 | −80.5% | −13.1920 to −7.3880 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06626 | 0.0955 | +44.1% | +0.0233 to +0.0352 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.59 | 2.288 | +43.9% | +0.5588 to +0.8374 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00972 | +0.010 (native is 0) | +0.0087 to +0.0107 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.59 | 2.298 | +44.5% | +0.5694 to +0.8462 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 423.7 | 298.2 | −29.6% | −172.7993 to −78.1195 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.025 | 2.715 | +34.1% | +0.3586 to +1.0222 | yes: power given |
| pods started | 0.4 | 0.5 | +25.0% | −0.5263 to +0.7263 | no |
| pod start wait, total (s) | 0.5 | 1.3 | +160.0% | −0.7379 to +2.3379 | no |
| pod start wait, mean (s) | 0.25 | 1.05 | +320.0% | −0.4639 to +2.0639 | no |
| host CPU busy, the real machine under kind (%) | 45.25 | 74.79 | +65.3% | +27.1994 to +31.8797 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 837.5 | 1444 | +72.4% | +536.8645 to +675.3355 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.773 | −3.8% | −3.1150 to +2.6605 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 680 | +858837.6% | +418.2082 to +941.6180 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1124 | +224622.0% | +743.4528 to +1502.7670 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 140.7 | 947.4 | +573.5% | +665.3160 to +948.1757 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 14.8 | +14.800 (native is 0) | +8.9130 to +20.6870 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*