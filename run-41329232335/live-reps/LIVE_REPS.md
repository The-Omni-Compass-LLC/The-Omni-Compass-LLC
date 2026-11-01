# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.576 | 5.447 |
| node-hours | 2.517 | 2.513 | 2.339 | 2.281 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.1 | 273.9 | 274.2 | 273.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.1 | 273.9 | 260.8 | 256.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 425.2 | 430.5 | 413.7 | 418.7 |
| response time (ms), 95th percentile | 1573 | 1674 | 1533 | 1630 |
| response time (ms), 99th percentile | 2192 | 2492 | 2170 | 2388 |
| time over the response line (% of samples) | 18.42 | 17.2 | 17.92 | 16.68 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 11 | 11.5 | 11.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 10.5 | 11.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.08 | 18.56 | 13.48 | 21.31 |
| utilisation (used / allocatable) | 0.06488 | 0.06522 | 0.0704 | 0.07057 |
| CPU used (cores), mean | 1.557 | 1.565 | 1.551 | 1.537 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01216 | 0.01365 |
| CPU used with Omni's own (cores), mean | 1.557 | 1.565 | 1.563 | 1.55 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 427.2 | 425.3 | 404.8 | 403.9 |
| HPA replicas, mean | 2.078 | 2.097 | 2.265 | 2.136 |
| pods started | 0 | 0.1 | 0.2 | 0.2 |
| pod start wait, total (s) | 0 | 0.2 | 0.3 | 0.2 |
| pod start wait, mean (s) | 0 | 0.2 | 0.3 | 0.2 |
| host CPU busy, the real machine under kind (%) | 44.72 | 45.64 | 45.06 | 46.1 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 812.6 | 823.5 | 811.1 | 820.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.273 | 4.946 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3333 | 0.3875 | 0.3417 | 1.242 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 1 | 0.5 | 3.8 |
| queue: job turnaround, submitted to done, mean (s) | 118.2 | 132.9 | 116 | 128.1 |
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
| worker nodes in service, mean | 6 | 5.447 | −9.2% | −1.0867 to −0.0184 | yes: GAIN |
| node-hours | 2.513 | 2.281 | −9.2% | −0.4521 to −0.0122 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 273.5 | −0.2% | −1.4908 to +0.6586 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 256.1 | −6.5% | −34.8218 to −0.7562 | yes: GAIN |
| response time (ms), mean | 430.5 | 418.7 | −2.7% | −64.0938 to +40.4349 | no |
| response time (ms), 95th percentile | 1674 | 1630 | −2.6% | −364.0600 to +276.4530 | no |
| response time (ms), 99th percentile | 2492 | 2388 | −4.2% | −589.3367 to +381.4205 | no |
| time over the response line (% of samples) | 17.2 | 16.68 | −3.0% | −2.4774 to +1.4304 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 | 11.2 | +1.8% | −0.6121 to +1.0121 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.4 | +11.400 (native is 0) | +7.8442 to +14.9558 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.56 | 21.31 | +14.8% | −0.2404 to +5.7471 | no |
| utilisation (used / allocatable) | 0.06522 | 0.07057 | +8.2% | +0.0009 to +0.0098 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.565 | 1.537 | −1.8% | −0.0823 to +0.0252 | no |
| Omni's own CPU (cores), mean | 0 | 0.01365 | +0.014 (native is 0) | +0.0122 to +0.0151 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.565 | 1.55 | −1.0% | −0.0689 to +0.0392 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 425.3 | 403.9 | −5.0% | −38.2092 to −4.5443 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.097 | 2.136 | +1.8% | −0.1701 to +0.2469 | no |
| pods started | 0.1 | 0.2 | +100.0% | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0.2 | 0.2 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | −0.3372 to +0.3372 | no |
| host CPU busy, the real machine under kind (%) | 45.64 | 46.1 | +1.0% | −0.4590 to +1.3834 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 823.5 | 820.9 | −0.3% | −17.9090 to +12.7090 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.946 | −17.6% | −2.0141 to −0.0932 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3875 | 1.242 | +220.4% | −0.6514 to +2.3597 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 3.8 | +280.0% | −0.7813 to +6.3813 | no |
| queue: job turnaround, submitted to done, mean (s) | 132.9 | 128.1 | −3.6% | −23.7053 to +14.0470 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.517 | 2.513 | −0.1% | −0.0138 to +0.0071 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.1 | 273.9 | −0.1% | −1.1302 to +0.6792 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.1 | 273.9 | −0.1% | −1.1302 to +0.6792 | no |
| response time (ms), mean | 425.2 | 430.5 | +1.3% | −40.9744 to +51.6381 | no |
| response time (ms), 95th percentile | 1573 | 1674 | +6.4% | −175.4769 to +377.4599 | no |
| response time (ms), 99th percentile | 2192 | 2492 | +13.7% | −145.9758 to +747.2808 | no |
| time over the response line (% of samples) | 18.42 | 17.2 | −6.6% | −2.5202 to +0.0882 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 11 | −8.3% | −2.2617 to +0.2617 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.08 | 18.56 | +15.4% | −1.9938 to +6.9471 | no |
| utilisation (used / allocatable) | 0.06488 | 0.06522 | +0.5% | −0.0012 to +0.0019 | no |
| CPU used (cores), mean | 1.557 | 1.565 | +0.5% | −0.0293 to +0.0455 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.557 | 1.565 | +0.5% | −0.0293 to +0.0455 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 427.2 | 425.3 | −0.5% | −11.5066 to +7.5434 | no |
| HPA replicas, mean | 2.078 | 2.097 | +0.9% | −0.1181 to +0.1565 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 44.72 | 45.64 | +2.0% | −0.1013 to +1.9305 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.6 | 823.5 | +1.3% | −5.6518 to +27.4518 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3333 | 0.3875 | +16.2% | −0.0583 to +0.1666 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 1 | −33.3% | −2.4444 to +1.4444 | no |
| queue: job turnaround, submitted to done, mean (s) | 118.2 | 132.9 | +12.5% | −5.4026 to +34.9776 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.576 | −7.1% | −0.9986 to +0.1497 | no |
| node-hours | 2.517 | 2.339 | −7.1% | −0.4190 to +0.0629 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.1 | 274.2 | +0.0% | −0.7038 to +0.8343 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.1 | 260.8 | −4.9% | −31.2288 to +4.5801 | no |
| response time (ms), mean | 425.2 | 413.7 | −2.7% | −32.2539 to +9.2907 | no |
| response time (ms), 95th percentile | 1573 | 1533 | −2.6% | −174.4922 to +93.4432 | no |
| response time (ms), 99th percentile | 2192 | 2170 | −1.0% | −80.6430 to +36.6062 | no |
| time over the response line (% of samples) | 18.42 | 17.92 | −2.7% | −1.4885 to +0.4794 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 11.5 | −4.2% | −1.2726 to +0.2726 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 10.5 | +10.500 (native is 0) | +6.8023 to +14.1977 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.08 | 13.48 | −16.2% | −5.6503 to +0.4503 | no |
| utilisation (used / allocatable) | 0.06488 | 0.0704 | +8.5% | −0.0031 to +0.0142 | no |
| CPU used (cores), mean | 1.557 | 1.551 | −0.4% | −0.0223 to +0.0105 | no |
| Omni's own CPU (cores), mean | 0 | 0.01216 | +0.012 (native is 0) | +0.0110 to +0.0133 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.557 | 1.563 | +0.4% | −0.0103 to +0.0229 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 427.2 | 404.8 | −5.3% | −56.1275 to +11.2231 | no |
| HPA replicas, mean | 2.078 | 2.265 | +9.0% | −0.0566 to +0.4306 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| host CPU busy, the real machine under kind (%) | 44.72 | 45.06 | +0.8% | −0.2003 to +0.8795 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.6 | 811.1 | −0.2% | −9.0268 to +6.0268 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.273 | −12.1% | −1.5862 to +0.1318 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3333 | 0.3417 | +2.5% | −0.3462 to +0.3629 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 0.5 | −66.7% | −2.8159 to +0.8159 | no |
| queue: job turnaround, submitted to done, mean (s) | 118.2 | 116 | −1.8% | −10.1158 to +5.8158 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.576 | −7.1% | −0.9986 to +0.1497 | no |
| node-hours | 2.513 | 2.339 | −7.0% | −0.4135 to +0.0641 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 274.2 | +0.1% | −0.5712 to +1.1526 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 260.8 | −4.8% | −30.8334 to +4.6357 | no |
| response time (ms), mean | 430.5 | 413.7 | −3.9% | −66.9923 to +33.3654 | no |
| response time (ms), 95th percentile | 1674 | 1533 | −8.5% | −452.8890 to +169.8570 | no |
| response time (ms), 99th percentile | 2492 | 2170 | −12.9% | −791.3729 to +146.0311 | no |
| time over the response line (% of samples) | 17.2 | 17.92 | +4.1% | −1.3615 to +2.7843 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 | 11.5 | +4.5% | −0.9405 to +1.9405 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 10.5 | +10.500 (native is 0) | +6.8023 to +14.1977 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.56 | 13.48 | −27.4% | −9.5035 to −0.6498 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06522 | 0.0704 | +7.9% | −0.0035 to +0.0139 | no |
| CPU used (cores), mean | 1.565 | 1.551 | −0.9% | −0.0503 to +0.0223 | no |
| Omni's own CPU (cores), mean | 0 | 0.01216 | +0.012 (native is 0) | +0.0110 to +0.0133 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.565 | 1.563 | −0.1% | −0.0378 to +0.0341 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 425.3 | 404.8 | −4.8% | −54.8034 to +13.8623 | no |
| HPA replicas, mean | 2.097 | 2.265 | +8.0% | −0.1127 to +0.4484 | no |
| pods started | 0.1 | 0.2 | +100.0% | −0.3060 to +0.5060 | no |
| pod start wait, total (s) | 0.2 | 0.3 | +50.0% | −0.6113 to +0.8113 | no |
| pod start wait, mean (s) | 0.2 | 0.3 | +50.0% | −0.6113 to +0.8113 | no |
| host CPU busy, the real machine under kind (%) | 45.64 | 45.06 | −1.3% | −1.4709 to +0.3209 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 823.5 | 811.1 | −1.5% | −28.1303 to +3.3303 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.273 | −12.1% | −1.5862 to +0.1318 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3875 | 0.3417 | −11.8% | −0.3966 to +0.3050 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 0.5 | −50.0% | −0.8770 to −0.1230 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 132.9 | 116 | −12.7% | −37.9538 to +4.0788 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.447 | −9.2% | −1.0867 to −0.0184 | yes: GAIN |
| node-hours | 2.517 | 2.281 | −9.4% | −0.4605 to −0.0104 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.1 | 273.5 | −0.2% | −1.7754 to +0.4924 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.1 | 256.1 | −6.6% | −35.3877 to −0.6412 | yes: GAIN |
| response time (ms), mean | 425.2 | 418.7 | −1.5% | −16.9826 to +3.9874 | no |
| response time (ms), 95th percentile | 1573 | 1630 | +3.6% | −63.7723 to +178.1483 | no |
| response time (ms), 99th percentile | 2192 | 2388 | +9.0% | −18.2078 to +411.5966 | no |
| time over the response line (% of samples) | 18.42 | 16.68 | −9.4% | −3.0208 to −0.4581 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 11.2 | −6.7% | −1.8556 to +0.2556 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.4 | +11.400 (native is 0) | +7.8442 to +14.9558 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.08 | 21.31 | +32.5% | −1.0667 to +11.5267 | no |
| utilisation (used / allocatable) | 0.06488 | 0.07057 | +8.8% | +0.0004 to +0.0110 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.557 | 1.537 | −1.3% | −0.0664 to +0.0257 | no |
| Omni's own CPU (cores), mean | 0 | 0.01365 | +0.014 (native is 0) | +0.0122 to +0.0151 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.557 | 1.55 | −0.4% | −0.0538 to +0.0403 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 427.2 | 403.9 | −5.5% | −44.6549 to −2.0618 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.078 | 2.136 | +2.8% | −0.0700 to +0.1852 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| host CPU busy, the real machine under kind (%) | 44.72 | 46.1 | +3.1% | +1.1431 to +1.6105 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.6 | 820.9 | +1.0% | +2.2299 to +14.3701 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.946 | −17.6% | −2.0141 to −0.0932 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3333 | 1.242 | +272.5% | −0.5774 to +2.3941 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 3.8 | +153.3% | −0.3775 to +4.9775 | no |
| queue: job turnaround, submitted to done, mean (s) | 118.2 | 128.1 | +8.4% | +3.0759 to +16.8408 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*