# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.271 | 5.29 |
| node-hours | 2.515 | 2.514 | 2.203 | 2.219 |
| energy, parked workers still on at idle power (Wh, declared model) | 275 | 275.1 | 274.5 | 275.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275 | 275.1 | 251.6 | 253 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 493.2 | 575.4 | 494.8 | 565.5 |
| response time (ms), 95th percentile | 1850 | 2632 | 2106 | 2681 |
| response time (ms), 99th percentile | 2645 | 3576 | 3050 | 3694 |
| time over the response line (% of samples) | 23.59 | 20.11 | 23.54 | 20.95 |
| failed requests (%) | 0 | 0.02326 | 0 | 0.1163 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.1 | 12 | 11.9 | 13.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 84.7 | 59.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 41.64 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.43 | 32.88 | 17.02 | 42.63 |
| utilisation (used / allocatable) | 0.06672 | 0.06727 | 0.07767 | 0.07659 |
| CPU used (cores), mean | 1.601 | 1.615 | 1.613 | 1.623 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07931 | 0.084 |
| CPU used with Omni's own (cores), mean | 1.601 | 1.615 | 1.692 | 1.707 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 417.5 | 415.1 | 373.6 | 373.6 |
| HPA replicas, mean | 2.008 | 2.057 | 2.462 | 2.304 |
| pods started | 0.2 | 0.2 | 2 | 1.4 |
| pod start wait, total (s) | 0.4 | 0.4 | 4.7 | 3.1 |
| pod start wait, mean (s) | 0.2 | 0.2 | 1.883 | 1.267 |
| host CPU busy, the real machine under kind (%) | 45.54 | 49 | 49.37 | 53.11 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 832.9 | 890.3 | 849.9 | 915.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.86 | 4.473 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 1.233 | 0.2167 | 1.421 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 3.7 | 1.2 | 4.4 |
| queue: job turnaround, submitted to done, mean (s) | 137.9 | 190.9 | 153.6 | 209.8 |
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
| worker nodes in service, mean | 6 | 5.29 | −11.8% | −1.2520 to −0.1681 | yes: GAIN |
| node-hours | 2.514 | 2.219 | −11.7% | −0.5200 to −0.0691 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 275.1 | 275.3 | +0.1% | −1.0267 to +1.4512 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.1 | 253 | −8.0% | −38.8433 to −5.4155 | yes: GAIN |
| response time (ms), mean | 575.4 | 565.5 | −1.7% | −45.4896 to +25.6522 | no |
| response time (ms), 95th percentile | 2632 | 2681 | +1.8% | −85.8767 to +182.0427 | no |
| response time (ms), 99th percentile | 3576 | 3694 | +3.3% | −35.9501 to +272.9699 | no |
| time over the response line (% of samples) | 20.11 | 20.95 | +4.1% | −0.6282 to +2.2918 | no |
| failed requests (%) | 0.02326 | 0.1163 | +400.0% | −0.1809 to +0.3669 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 13.3 | +10.8% | −0.1717 to +2.7717 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 59.2 | +59.200 (native is 0) | +27.0938 to +91.3062 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 32.88 | 42.63 | +29.7% | +4.3450 to +15.1550 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06727 | 0.07659 | +13.8% | +0.0021 to +0.0165 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.615 | 1.623 | +0.5% | −0.0192 to +0.0365 | no |
| Omni's own CPU (cores), mean | 0 | 0.084 | +0.084 (native is 0) | +0.0773 to +0.0907 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.615 | 1.707 | +5.7% | +0.0659 to +0.1195 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 415.1 | 373.6 | −10.0% | −76.3198 to −6.7555 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.057 | 2.304 | +12.0% | +0.0359 to +0.4577 | yes: power given |
| pods started | 0.2 | 1.4 | +600.0% | +0.3207 to +2.0793 | yes: power given |
| pod start wait, total (s) | 0.4 | 3.1 | +675.0% | +0.6200 to +4.7800 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.267 | +533.3% | +0.3756 to +1.7577 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 49 | 53.11 | +8.4% | +3.6920 to +4.5236 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 890.3 | 915.1 | +2.8% | +14.1699 to +35.4301 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.473 | −25.4% | −2.5551 to −0.4985 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.233 | 1.421 | +15.2% | −0.0464 to +0.4214 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.7 | 4.4 | +18.9% | −1.1174 to +2.5174 | no |
| queue: job turnaround, submitted to done, mean (s) | 190.9 | 209.8 | +9.9% | +10.7125 to +27.0959 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.515 | 2.514 | −0.1% | −0.0087 to +0.0050 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275 | 275.1 | +0.0% | −0.7751 to +0.9345 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275 | 275.1 | +0.0% | −0.7751 to +0.9345 | no |
| response time (ms), mean | 493.2 | 575.4 | +16.7% | +33.4618 to +131.0872 | yes: LOSS |
| response time (ms), 95th percentile | 1850 | 2632 | +42.3% | +365.7615 to +1199.4785 | yes: LOSS |
| response time (ms), 99th percentile | 2645 | 3576 | +35.2% | +471.7738 to +1390.5758 | yes: LOSS |
| time over the response line (% of samples) | 23.59 | 20.11 | −14.7% | −5.4824 to −1.4619 | yes: GAIN |
| failed requests (%) | 0 | 0.02326 | +0.023 (native is 0) | −0.0293 to +0.0759 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.1 | 12 | +8.1% | +0.4940 to +1.3060 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.43 | 32.88 | +144.8% | +7.3733 to +31.5267 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06672 | 0.06727 | +0.8% | −0.0000 to +0.0011 | no |
| CPU used (cores), mean | 1.601 | 1.615 | +0.8% | −0.0003 to +0.0267 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.601 | 1.615 | +0.8% | −0.0003 to +0.0267 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 417.5 | 415.1 | −0.6% | −5.5988 to +0.9272 | no |
| HPA replicas, mean | 2.008 | 2.057 | +2.4% | −0.1009 to +0.1993 | no |
| pods started | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| pod start wait, total (s) | 0.4 | 0.4 | ±0.0% | −1.3488 to +1.3488 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 45.54 | 49 | +7.6% | +2.5396 to +4.3834 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 832.9 | 890.3 | +6.9% | +30.4342 to +84.3658 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 1.233 | +1133.3% | +0.8514 to +1.4153 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 3.7 | +640.0% | +1.4544 to +4.9456 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 137.9 | 190.9 | +38.4% | +28.5997 to +77.3419 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.271 | −12.1% | −1.5053 to +0.0474 | no |
| node-hours | 2.515 | 2.203 | −12.4% | −0.6363 to +0.0120 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275 | 274.5 | −0.2% | −1.4521 to +0.4340 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275 | 251.6 | −8.5% | −47.6844 to +0.9205 | no |
| response time (ms), mean | 493.2 | 494.8 | +0.3% | −23.5675 to +26.8038 | no |
| response time (ms), 95th percentile | 1850 | 2106 | +13.9% | +87.9959 to +425.0801 | yes: LOSS |
| response time (ms), 99th percentile | 2645 | 3050 | +15.3% | +168.6660 to +642.4538 | yes: LOSS |
| time over the response line (% of samples) | 23.59 | 23.54 | −0.2% | −0.5632 to +0.4770 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.1 | 11.9 | +7.2% | −0.0793 to +1.6793 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 84.7 | +84.700 (native is 0) | +32.9248 to +136.4752 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.43 | 17.02 | +26.7% | −0.0691 to +7.2358 | no |
| utilisation (used / allocatable) | 0.06672 | 0.07767 | +16.4% | −0.0003 to +0.0222 | no |
| CPU used (cores), mean | 1.601 | 1.613 | +0.7% | −0.0158 to +0.0386 | no |
| Omni's own CPU (cores), mean | 0 | 0.07931 | +0.079 (native is 0) | +0.0747 to +0.0840 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.601 | 1.692 | +5.7% | +0.0647 to +0.1167 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 417.5 | 373.6 | −10.5% | −88.0797 to +0.2451 | no |
| HPA replicas, mean | 2.008 | 2.462 | +22.6% | +0.1955 to +0.7122 | yes: power given |
| pods started | 0.2 | 2 | +900.0% | +0.8583 to +2.7417 | yes: power given |
| pod start wait, total (s) | 0.4 | 4.7 | +1075.0% | +1.6438 to +6.9562 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.883 | +841.7% | +0.6164 to +2.7503 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.54 | 49.37 | +8.4% | +3.3120 to +4.3508 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 832.9 | 849.9 | +2.0% | +5.5303 to +28.4697 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.86 | −19.0% | −2.2592 to −0.0205 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 0.2167 | +116.7% | −0.0230 to +0.2563 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1.2 | +140.0% | −0.3690 to +1.7690 | no |
| queue: job turnaround, submitted to done, mean (s) | 137.9 | 153.6 | +11.4% | +4.6769 to +26.7981 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.271 | −12.1% | −1.5053 to +0.0474 | no |
| node-hours | 2.514 | 2.203 | −12.3% | −0.6326 to +0.0120 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.1 | 274.5 | −0.2% | −1.2873 to +0.1099 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.1 | 251.6 | −8.5% | −47.5087 to +0.5854 | no |
| response time (ms), mean | 575.4 | 494.8 | −14.0% | −119.1215 to −42.1912 | yes: GAIN |
| response time (ms), 95th percentile | 2632 | 2106 | −20.0% | −834.9088 to −217.2552 | yes: GAIN |
| response time (ms), 99th percentile | 3576 | 3050 | −14.7% | −825.2929 to −225.9369 | yes: GAIN |
| time over the response line (% of samples) | 20.11 | 23.54 | +17.0% | +1.7115 to +5.1465 | yes: LOSS |
| failed requests (%) | 0.02326 | 0 | −100.0% | −0.0759 to +0.0293 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 11.9 | −0.8% | −1.1366 to +0.9366 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 84.7 | +84.700 (native is 0) | +32.9248 to +136.4752 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 32.88 | 17.02 | −48.3% | −26.0013 to −5.7321 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06727 | 0.07767 | +15.5% | −0.0012 to +0.0220 | no |
| CPU used (cores), mean | 1.615 | 1.613 | −0.1% | −0.0265 to +0.0230 | no |
| Omni's own CPU (cores), mean | 0 | 0.07931 | +0.079 (native is 0) | +0.0747 to +0.0840 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.615 | 1.692 | +4.8% | +0.0552 to +0.0998 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 415.1 | 373.6 | −10.0% | −87.3678 to +4.2048 | no |
| HPA replicas, mean | 2.057 | 2.462 | +19.7% | +0.1420 to +0.6674 | yes: power given |
| pods started | 0.2 | 2 | +900.0% | +0.9879 to +2.6121 | yes: power given |
| pod start wait, total (s) | 0.4 | 4.7 | +1075.0% | +2.0118 to +6.5882 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.883 | +841.7% | +0.7288 to +2.6378 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 49 | 49.37 | +0.8% | −0.5835 to +1.3233 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 890.3 | 849.9 | −4.5% | −62.0549 to −18.7451 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.86 | −19.0% | −2.2592 to −0.0205 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.233 | 0.2167 | −82.4% | −1.2398 to −0.7935 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.7 | 1.2 | −67.6% | −3.9005 to −1.0995 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 190.9 | 153.6 | −19.5% | −55.5766 to −18.8901 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.29 | −11.8% | −1.2520 to −0.1681 | yes: GAIN |
| node-hours | 2.515 | 2.219 | −11.8% | −0.5247 to −0.0681 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 275 | 275.3 | +0.1% | −1.1864 to +1.7702 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275 | 253 | −8.0% | −39.1731 to −4.9264 | yes: GAIN |
| response time (ms), mean | 493.2 | 565.5 | +14.7% | +17.7492 to +126.9624 | yes: LOSS |
| response time (ms), 95th percentile | 1850 | 2681 | +44.9% | +424.5831 to +1236.8229 | yes: LOSS |
| response time (ms), 99th percentile | 2645 | 3694 | +39.7% | +570.5797 to +1528.7897 | yes: LOSS |
| time over the response line (% of samples) | 23.59 | 20.95 | −11.2% | −5.3036 to +0.0230 | no |
| failed requests (%) | 0 | 0.1163 | +0.116 (native is 0) | −0.1467 to +0.3793 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.1 | 13.3 | +19.8% | +0.8179 to +3.5821 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 59.2 | +59.200 (native is 0) | +27.0938 to +91.3062 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.43 | 42.63 | +217.4% | +14.1737 to +44.2263 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06672 | 0.07659 | +14.8% | +0.0030 to +0.0167 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.601 | 1.623 | +1.4% | −0.0045 to +0.0483 | no |
| Omni's own CPU (cores), mean | 0 | 0.084 | +0.084 (native is 0) | +0.0773 to +0.0907 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.601 | 1.707 | +6.6% | +0.0784 to +0.1333 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 417.5 | 373.6 | −10.5% | −76.6880 to −11.0589 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.008 | 2.304 | +14.7% | −0.0002 to +0.5922 | no |
| pods started | 0.2 | 1.4 | +600.0% | −0.0064 to +2.4064 | no |
| pod start wait, total (s) | 0.4 | 3.1 | +675.0% | −0.2790 to +5.6790 | no |
| pod start wait, mean (s) | 0.2 | 1.267 | +533.3% | +0.2270 to +1.9063 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.54 | 53.11 | +16.6% | +6.4944 to +8.6442 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 832.9 | 915.1 | +9.9% | +47.2909 to +117.1091 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.473 | −25.4% | −2.5551 to −0.4985 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 1.421 | +1320.8% | +0.9381 to +1.7036 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 4.4 | +780.0% | +1.7821 to +6.0179 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 137.9 | 209.8 | +52.1% | +42.8161 to +100.9339 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*