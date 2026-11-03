# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.124 | 5.128 |
| node-hours | 2.512 | 2.516 | 2.15 | 2.148 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 274.1 | 274.2 | 273.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 274.1 | 246.6 | 246.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 433.8 | 383.9 | 414.8 | 358.4 |
| response time (ms), 95th percentile | 1621 | 1576 | 1722 | 1646 |
| response time (ms), 99th percentile | 2286 | 2261 | 2368 | 2322 |
| time over the response line (% of samples) | 18.02 | 13.99 | 17.85 | 13.86 |
| failed requests (%) | 0.01149 | 0 | 0.01111 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 7.7 | 9.8 | 8.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 136 | 113.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 25 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.21 | 22.93 | 18.8 | 26.61 |
| utilisation (used / allocatable) | 0.0634 | 0.06425 | 0.07523 | 0.07543 |
| CPU used (cores), mean | 1.522 | 1.542 | 1.521 | 1.534 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07505 | 0.0756 |
| CPU used with Omni's own (cores), mean | 1.522 | 1.542 | 1.596 | 1.61 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 442.3 | 437.4 | 390.9 | 386.6 |
| HPA replicas, mean | 1.952 | 1.981 | 2.496 | 2.33 |
| pods started | 0.1 | 0.3 | 2 | 1 |
| pod start wait, total (s) | 0.3 | 0.6 | 4.3 | 2.1 |
| pod start wait, mean (s) | 0.3 | 0.4 | 2.158 | 0.8667 |
| host CPU busy, the real machine under kind (%) | 43.66 | 44.57 | 46.77 | 47.79 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 819.6 | 832.1 | 828.2 | 837.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.66 | 4.47 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2875 | 0.9083 | 0.4833 | 1.046 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 2.4 | 1.9 | 2.5 |
| queue: job turnaround, submitted to done, mean (s) | 123.6 | 142.9 | 133.4 | 147.7 |
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
| worker nodes in service, mean | 6 | 5.128 | −14.5% | −1.6324 to −0.1107 | yes: GAIN |
| node-hours | 2.516 | 2.148 | −14.6% | −0.6898 to −0.0453 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.1 | 273.8 | −0.1% | −1.4616 to +0.9216 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.1 | 246.5 | −10.1% | −52.1077 to −3.1406 | yes: GAIN |
| response time (ms), mean | 383.9 | 358.4 | −6.6% | −62.1548 to +11.2009 | no |
| response time (ms), 95th percentile | 1576 | 1646 | +4.4% | −115.5727 to +255.3897 | no |
| response time (ms), 99th percentile | 2261 | 2322 | +2.7% | −280.0123 to +403.5839 | no |
| time over the response line (% of samples) | 13.99 | 13.86 | −0.9% | −1.5396 to +1.2842 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 8.3 | +7.8% | −0.6251 to +1.8251 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 113.4 | +113.400 (native is 0) | +53.8968 to +172.9032 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 22.93 | 26.6 | +16.0% | +1.4302 to +5.9231 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06425 | 0.07543 | +17.4% | +0.0007 to +0.0217 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.542 | 1.534 | −0.5% | −0.0313 to +0.0160 | no |
| Omni's own CPU (cores), mean | 0 | 0.0756 | +0.076 (native is 0) | +0.0692 to +0.0820 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.542 | 1.61 | +4.4% | +0.0419 to +0.0940 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.4 | 386.6 | −11.6% | −95.3633 to −6.2638 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.981 | 2.33 | +17.6% | +0.0942 to +0.6042 | yes: power given |
| pods started | 0.3 | 1 | +233.3% | −0.4209 to +1.8209 | no |
| pod start wait, total (s) | 0.6 | 2.1 | +250.0% | −0.7932 to +3.7932 | no |
| pod start wait, mean (s) | 0.4 | 0.8667 | +116.7% | −0.4734 to +1.4067 | no |
| host CPU busy, the real machine under kind (%) | 44.57 | 47.79 | +7.2% | +2.6958 to +3.7454 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 832.1 | 837.7 | +0.7% | −2.1717 to +13.3717 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.47 | −25.5% | −2.7866 to −0.2730 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9083 | 1.046 | +15.1% | −0.0607 to +0.3357 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.4 | 2.5 | +4.2% | −0.5263 to +0.7263 | no |
| queue: job turnaround, submitted to done, mean (s) | 142.9 | 147.7 | +3.3% | −4.5245 to +13.9911 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.512 | 2.516 | +0.2% | −0.0027 to +0.0110 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 274.1 | +0.3% | −0.1252 to +1.6229 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 274.1 | +0.3% | −0.1252 to +1.6229 | no |
| response time (ms), mean | 433.8 | 383.9 | −11.5% | −87.8743 to −11.8256 | yes: GAIN |
| response time (ms), 95th percentile | 1621 | 1576 | −2.8% | −211.7773 to +121.8843 | no |
| response time (ms), 99th percentile | 2286 | 2261 | −1.1% | −292.5684 to +241.1810 | no |
| time over the response line (% of samples) | 18.02 | 13.99 | −22.4% | −6.4169 to −1.6454 | yes: GAIN |
| failed requests (%) | 0.01149 | 0 | −100.0% | −0.0375 to +0.0145 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 7.7 | −20.6% | −4.0232 to +0.0232 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.21 | 22.93 | +50.7% | +2.3112 to +13.1254 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0634 | 0.06425 | +1.3% | +0.0001 to +0.0016 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.522 | 1.542 | +1.3% | +0.0013 to +0.0393 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.522 | 1.542 | +1.3% | +0.0013 to +0.0393 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 442.3 | 437.4 | −1.1% | −11.3456 to +1.4708 | no |
| HPA replicas, mean | 1.952 | 1.981 | +1.5% | −0.1208 to +0.1779 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0.3 | 0.6 | +100.0% | −0.1828 to +0.7828 | no |
| pod start wait, mean (s) | 0.3 | 0.4 | +33.3% | −0.4278 to +0.6278 | no |
| host CPU busy, the real machine under kind (%) | 43.66 | 44.57 | +2.1% | +0.5166 to +1.3123 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 819.6 | 832.1 | +1.5% | +2.8544 to +22.1456 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2875 | 0.9083 | +215.9% | +0.4468 to +0.7949 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 2.4 | +26.3% | −1.1259 to +2.1259 | no |
| queue: job turnaround, submitted to done, mean (s) | 123.6 | 142.9 | +15.7% | +4.9256 to +33.7744 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.124 | −14.6% | −1.6901 to −0.0611 | yes: GAIN |
| node-hours | 2.512 | 2.15 | −14.4% | −0.7016 to −0.0212 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 274.2 | +0.3% | +0.1510 to +1.5250 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 246.6 | −9.8% | −52.3945 to −1.1878 | yes: GAIN |
| response time (ms), mean | 433.8 | 414.8 | −4.4% | −36.1004 to −1.8468 | yes: GAIN |
| response time (ms), 95th percentile | 1621 | 1722 | +6.2% | −17.6516 to +219.9566 | no |
| response time (ms), 99th percentile | 2286 | 2368 | +3.6% | −3.2877 to +167.3321 | no |
| time over the response line (% of samples) | 18.02 | 17.85 | −0.9% | −0.8778 to +0.5395 | no |
| failed requests (%) | 0.01149 | 0.01111 | −3.3% | −0.0385 to +0.0377 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 9.8 | +1.0% | −0.8204 to +1.0204 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 136 | +136.000 (native is 0) | +58.1070 to +213.8930 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.21 | 18.8 | +23.6% | −0.8056 to +7.9956 | no |
| utilisation (used / allocatable) | 0.0634 | 0.07523 | +18.7% | +0.0008 to +0.0228 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.522 | 1.521 | −0.1% | −0.0226 to +0.0208 | no |
| Omni's own CPU (cores), mean | 0 | 0.07505 | +0.075 (native is 0) | +0.0680 to +0.0821 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.522 | 1.596 | +4.9% | +0.0497 to +0.0985 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 442.3 | 390.9 | −11.6% | −98.1043 to −4.6578 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.952 | 2.496 | +27.8% | +0.3013 to +0.7862 | yes: power given |
| pods started | 0.1 | 2 | +1900.0% | +1.0436 to +2.7564 | yes: power given |
| pod start wait, total (s) | 0.3 | 4.3 | +1333.3% | +1.9489 to +6.0511 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 2.158 | +619.4% | +1.0566 to +2.6601 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.66 | 46.77 | +7.1% | +2.7555 to +3.4639 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 819.6 | 828.2 | +1.0% | −0.0838 to +17.2838 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.66 | −22.3% | −2.5902 to −0.0898 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2875 | 0.4833 | +68.1% | −0.2509 to +0.6426 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 1.9 | ±0.0% | −3.0720 to +3.0720 | no |
| queue: job turnaround, submitted to done, mean (s) | 123.6 | 133.4 | +7.9% | +1.2502 to +18.3331 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.124 | −14.6% | −1.6901 to −0.0611 | yes: GAIN |
| node-hours | 2.516 | 2.15 | −14.5% | −0.7074 to −0.0237 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.1 | 274.2 | +0.0% | −0.5434 to +0.7218 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.1 | 246.6 | −10.0% | −53.3734 to −1.7066 | yes: GAIN |
| response time (ms), mean | 383.9 | 414.8 | +8.0% | −5.5696 to +67.3223 | no |
| response time (ms), 95th percentile | 1576 | 1722 | +9.3% | +62.8523 to +229.3457 | yes: LOSS |
| response time (ms), 99th percentile | 2261 | 2368 | +4.8% | −92.2931 to +307.7249 | no |
| time over the response line (% of samples) | 13.99 | 17.85 | +27.6% | +1.8565 to +5.8676 | yes: LOSS |
| failed requests (%) | 0 | 0.01111 | +0.011 (native is 0) | −0.0140 to +0.0362 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 9.8 | +27.3% | +0.4327 to +3.7673 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 136 | +136.000 (native is 0) | +58.1070 to +213.8930 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 22.93 | 18.8 | −18.0% | −6.4618 to −1.7849 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06425 | 0.07523 | +17.1% | +0.0001 to +0.0219 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.542 | 1.521 | −1.4% | −0.0426 to +0.0001 | no |
| Omni's own CPU (cores), mean | 0 | 0.07505 | +0.075 (native is 0) | +0.0680 to +0.0821 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.542 | 1.596 | +3.5% | +0.0267 to +0.0809 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.4 | 390.9 | −10.6% | −90.1931 to −2.6943 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.981 | 2.496 | +26.0% | +0.2639 to +0.7664 | yes: power given |
| pods started | 0.3 | 2 | +566.7% | +0.6856 to +2.7144 | yes: power given |
| pod start wait, total (s) | 0.6 | 4.3 | +616.7% | +1.5660 to +5.8340 | yes: LOSS |
| pod start wait, mean (s) | 0.4 | 2.158 | +439.6% | +1.1781 to +2.3386 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.57 | 46.77 | +4.9% | +1.7634 to +2.6272 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 832.1 | 828.2 | −0.5% | −10.0851 to +2.2851 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.66 | −22.3% | −2.5902 to −0.0898 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9083 | 0.4833 | −46.8% | −0.8623 to +0.0123 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.4 | 1.9 | −20.8% | −3.0956 to +2.0956 | no |
| queue: job turnaround, submitted to done, mean (s) | 142.9 | 133.4 | −6.7% | −18.0382 to −1.0785 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.128 | −14.5% | −1.6324 to −0.1107 | yes: GAIN |
| node-hours | 2.512 | 2.148 | −14.5% | −0.6839 to −0.0429 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 273.8 | +0.2% | −0.5450 to +1.5027 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 246.5 | −9.8% | −51.1731 to −2.5775 | yes: GAIN |
| response time (ms), mean | 433.8 | 358.4 | −17.4% | −102.8733 to −47.7804 | yes: GAIN |
| response time (ms), 95th percentile | 1621 | 1646 | +1.5% | −125.1552 to +175.0792 | no |
| response time (ms), 99th percentile | 2286 | 2322 | +1.6% | −157.0709 to +229.2551 | no |
| time over the response line (% of samples) | 18.02 | 13.86 | −23.1% | −6.7373 to −1.5805 | yes: GAIN |
| failed requests (%) | 0.01149 | 0 | −100.0% | −0.0375 to +0.0145 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 8.3 | −14.4% | −3.4566 to +0.6566 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 113.4 | +113.400 (native is 0) | +53.8968 to +172.9032 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.21 | 26.6 | +74.9% | +5.2486 to +17.5414 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0634 | 0.07543 | +19.0% | +0.0016 to +0.0225 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.522 | 1.534 | +0.8% | −0.0086 to +0.0339 | no |
| Omni's own CPU (cores), mean | 0 | 0.0756 | +0.076 (native is 0) | +0.0692 to +0.0820 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.522 | 1.61 | +5.8% | +0.0663 to +0.1102 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 442.3 | 386.6 | −12.6% | −102.0139 to −9.4880 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.952 | 2.33 | +19.3% | +0.0641 to +0.6914 | yes: power given |
| pods started | 0.1 | 1 | +900.0% | −0.1366 to +1.9366 | no |
| pod start wait, total (s) | 0.3 | 2.1 | +600.0% | −0.4820 to +4.0820 | no |
| pod start wait, mean (s) | 0.3 | 0.8667 | +188.9% | −0.6376 to +1.7710 | no |
| host CPU busy, the real machine under kind (%) | 43.66 | 47.79 | +9.5% | +3.7475 to +4.5226 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 819.6 | 837.7 | +2.2% | +5.7222 to +30.4778 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.47 | −25.5% | −2.7866 to −0.2730 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2875 | 1.046 | +263.8% | +0.4948 to +1.0219 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 2.5 | +31.6% | −0.8775 to +2.0775 | no |
| queue: job turnaround, submitted to done, mean (s) | 123.6 | 147.7 | +19.5% | +9.0257 to +39.1410 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*