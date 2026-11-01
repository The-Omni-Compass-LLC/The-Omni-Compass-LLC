# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.285 | 5.985 |
| node-hours | 2.517 | 2.515 | 2.216 | 2.505 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 286.5 | 273.4 | 286 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 286.5 | 251 | 285.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 451.8 | 702.5 | 420.8 | 697.8 |
| response time (ms), 95th percentile | 1724 | 1412 | 1797 | 1417 |
| response time (ms), 99th percentile | 2502 | 1911 | 2528 | 1908 |
| time over the response line (% of samples) | 20.51 | 62.21 | 20 | 61.13 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 24.4 | 9.7 | 24.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 31.2 | 17.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.29 | 2.27 | 13.64 | 2.255 |
| utilisation (used / allocatable) | 0.06286 | 0.09786 | 0.07126 | 0.09765 |
| CPU used (cores), mean | 1.509 | 2.349 | 1.5 | 2.338 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01555 | 0.00941 |
| CPU used with Omni's own (cores), mean | 1.509 | 2.349 | 1.515 | 2.348 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 452.1 | 292 | 406.5 | 292.7 |
| HPA replicas, mean | 1.992 | 2.002 | 2.108 | 2.684 |
| pods started | 0 | 0.3 | 0.5 | 1 |
| pod start wait, total (s) | 0 | 0.8 | 0.9 | 3.5 |
| pod start wait, mean (s) | 0 | 0.5 | 0.7 | 1.55 |
| host CPU busy, the real machine under kind (%) | 42.84 | 75.78 | 43.81 | 76.02 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 823.3 | 1473 | 826.8 | 1470 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.823 | 5.659 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 613.6 | 0.1625 | 647.4 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1103 | 0.7 | 1027 |
| queue: job turnaround, submitted to done, mean (s) | 129.7 | 943 | 132 | 956.9 |
| queue: jobs unfinished at the window's end | 0 | 12.9 | 0 | 14.7 |
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
| worker nodes in service, mean | 6 | 5.985 | −0.3% | −0.0502 to +0.0194 | no |
| node-hours | 2.515 | 2.505 | −0.4% | −0.0273 to +0.0075 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 286.5 | 286 | −0.2% | −1.8301 to +0.7875 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 286.5 | 285.5 | −0.3% | −2.7089 to +0.7038 | no |
| response time (ms), mean | 702.5 | 697.8 | −0.7% | −49.1416 to +39.7909 | no |
| response time (ms), 95th percentile | 1412 | 1417 | +0.4% | −75.8318 to +86.7598 | no |
| response time (ms), 99th percentile | 1911 | 1908 | −0.2% | −130.1038 to +124.0882 | no |
| time over the response line (% of samples) | 62.21 | 61.13 | −1.7% | −4.1906 to +2.0471 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.4 | 24.3 | −0.4% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.1 | +17.100 (native is 0) | +14.8519 to +19.3481 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.27 | 2.255 | −0.7% | −0.3600 to +0.3300 | no |
| utilisation (used / allocatable) | 0.09786 | 0.09765 | −0.2% | −0.0007 to +0.0003 | no |
| CPU used (cores), mean | 2.349 | 2.338 | −0.4% | −0.0234 to +0.0030 | no |
| Omni's own CPU (cores), mean | 0 | 0.00941 | +0.009 (native is 0) | +0.0082 to +0.0106 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.349 | 2.348 | −0.0% | −0.0144 to +0.0127 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 292 | 292.7 | +0.2% | −0.4350 to +1.8321 | no |
| HPA replicas, mean | 2.002 | 2.684 | +34.1% | +0.3705 to +0.9939 | yes: power given |
| pods started | 0.3 | 1 | +233.3% | +0.0214 to +1.3786 | yes: power given |
| pod start wait, total (s) | 0.8 | 3.5 | +337.5% | −0.2599 to +5.6599 | no |
| pod start wait, mean (s) | 0.5 | 1.55 | +210.0% | +0.0182 to +2.0818 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 75.78 | 76.02 | +0.3% | −0.2213 to +0.6879 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1473 | 1470 | −0.2% | −13.5169 to +8.1169 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.659 | −5.7% | −4.6725 to +3.9907 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 613.6 | 647.4 | +5.5% | −37.1089 to +104.7632 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1103 | 1027 | −6.9% | −186.7310 to +35.1547 | no |
| queue: job turnaround, submitted to done, mean (s) | 943 | 956.9 | +1.5% | −23.8380 to +51.6463 | no |
| queue: jobs unfinished at the window's end | 12.9 | 14.7 | +14.0% | −0.1015 to +3.7015 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.517 | 2.515 | −0.1% | −0.0105 to +0.0052 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 286.5 | +4.7% | +7.7713 to +17.7718 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 286.5 | +4.7% | +7.7713 to +17.7718 | yes: power given |
| response time (ms), mean | 451.8 | 702.5 | +55.5% | +174.4311 to +326.8433 | yes: LOSS |
| response time (ms), 95th percentile | 1724 | 1412 | −18.1% | −984.1229 to +359.2139 | no |
| response time (ms), 99th percentile | 2502 | 1911 | −23.6% | −1610.4307 to +429.5919 | no |
| time over the response line (% of samples) | 20.51 | 62.21 | +203.2% | +34.6014 to +48.7809 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 24.4 | +162.4% | +10.3022 to +19.8978 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.29 | 2.27 | −79.9% | −12.7449 to −5.3051 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06286 | 0.09786 | +55.7% | +0.0232 to +0.0468 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.509 | 2.349 | +55.7% | +0.5571 to +1.1225 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.509 | 2.349 | +55.7% | +0.5571 to +1.1225 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 452.1 | 292 | −35.4% | −238.4150 to −81.8049 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.992 | 2.002 | +0.5% | −0.0846 to +0.1058 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 0.8 | +0.800 (native is 0) | −0.5821 to +2.1821 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −0.2726 to +1.2726 | no |
| host CPU busy, the real machine under kind (%) | 42.84 | 75.78 | +76.9% | +27.0128 to +38.8772 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 823.3 | 1473 | +78.9% | +579.4745 to +719.1255 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 613.6 | +507700.0% | +345.3339 to +881.6076 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1103 | +183779.5% | +726.6659 to +1478.6875 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 129.7 | 943 | +626.8% | +706.3126 to +920.1541 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12.9 | +12.900 (native is 0) | +6.4099 to +19.3901 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.285 | −11.9% | −1.5482 to +0.1173 | no |
| node-hours | 2.517 | 2.216 | −12.0% | −0.6514 to +0.0483 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 273.4 | −0.1% | −1.3204 to +0.6505 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 251 | −8.3% | −49.2888 to +3.7814 | no |
| response time (ms), mean | 451.8 | 420.8 | −6.9% | −45.9420 to −16.0145 | yes: GAIN |
| response time (ms), 95th percentile | 1724 | 1797 | +4.2% | −8.1658 to +153.1688 | no |
| response time (ms), 99th percentile | 2502 | 2528 | +1.1% | −180.1448 to +232.7300 | no |
| time over the response line (% of samples) | 20.51 | 20 | −2.5% | −1.2932 to +0.2555 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 9.7 | +4.3% | −0.2911 to +1.0911 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.2 | +31.200 (native is 0) | +14.2768 to +48.1232 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.29 | 13.64 | +20.7% | +0.0550 to +4.6317 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06286 | 0.07126 | +13.4% | −0.0010 to +0.0177 | no |
| CPU used (cores), mean | 1.509 | 1.5 | −0.6% | −0.0529 to +0.0348 | no |
| Omni's own CPU (cores), mean | 0 | 0.01555 | +0.016 (native is 0) | +0.0145 to +0.0166 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.509 | 1.515 | +0.4% | −0.0379 to +0.0509 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 452.1 | 406.5 | −10.1% | −96.2309 to +5.0793 | no |
| HPA replicas, mean | 1.992 | 2.108 | +5.8% | −0.0438 to +0.2766 | no |
| pods started | 0 | 0.5 | +0.500 (native is 0) | −0.0058 to +1.0058 | no |
| pod start wait, total (s) | 0 | 0.9 | +0.900 (native is 0) | −0.0802 to +1.8802 | no |
| pod start wait, mean (s) | 0 | 0.7 | +0.700 (native is 0) | +0.0214 to +1.3786 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.84 | 43.81 | +2.3% | +0.6152 to +1.3334 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 823.3 | 826.8 | +0.4% | −1.1265 to +8.1265 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.823 | −19.6% | −2.5335 to +0.1794 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 0.1625 | +34.5% | −0.0967 to +0.1800 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.7 | +16.7% | −0.1262 to +0.3262 | no |
| queue: job turnaround, submitted to done, mean (s) | 129.7 | 132 | +1.8% | −4.1325 to +8.6825 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.285 | −11.9% | −1.5482 to +0.1173 | no |
| node-hours | 2.515 | 2.216 | −11.9% | −0.6520 to +0.0542 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 286.5 | 273.4 | −4.6% | −18.1858 to −8.0272 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 286.5 | 251 | −12.4% | −65.6590 to −5.3915 | yes: GAIN |
| response time (ms), mean | 702.5 | 420.8 | −40.1% | −356.2773 to −206.9536 | yes: GAIN |
| response time (ms), 95th percentile | 1412 | 1797 | +27.3% | −311.6990 to +1081.6110 | no |
| response time (ms), 99th percentile | 1911 | 2528 | +32.3% | −387.5898 to +1621.0138 | no |
| time over the response line (% of samples) | 62.21 | 20 | −67.9% | −49.4247 to −34.9953 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.4 | 9.7 | −60.2% | −19.1741 to −10.2259 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.2 | +31.200 (native is 0) | +14.2768 to +48.1232 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.27 | 13.64 | +500.8% | +6.6989 to +16.0378 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09786 | 0.07126 | −27.2% | −0.0348 to −0.0184 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.349 | 1.5 | −36.1% | −1.1337 to −0.5641 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01555 | +0.016 (native is 0) | +0.0145 to +0.0166 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.349 | 1.515 | −35.5% | −1.1189 to −0.5478 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 292 | 406.5 | +39.2% | +75.9055 to +153.1628 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.002 | 2.108 | +5.3% | −0.0648 to +0.2763 | no |
| pods started | 0.3 | 0.5 | +66.7% | −0.6121 to +1.0121 | no |
| pod start wait, total (s) | 0.8 | 0.9 | +12.5% | −1.8209 to +2.0209 | no |
| pod start wait, mean (s) | 0.5 | 0.7 | +40.0% | −1.0064 to +1.4064 | no |
| host CPU busy, the real machine under kind (%) | 75.78 | 43.81 | −42.2% | −37.7103 to −26.2312 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1473 | 826.8 | −43.9% | −716.4589 to −575.1411 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.076 | −65.4% | −4.2523 to −3.5949 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 613.6 | 0.1625 | −100.0% | −881.5450 to −345.3132 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1103 | 0.7 | −99.9% | −1478.5456 to −726.6078 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 943 | 132 | −86.0% | −917.4471 to −704.4696 | yes: GAIN |
| queue: jobs unfinished at the window's end | 12.9 | 0 | −100.0% | −19.3901 to −6.4099 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.985 | −0.3% | −0.0502 to +0.0194 | no |
| node-hours | 2.517 | 2.505 | −0.5% | −0.0297 to +0.0045 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 286 | +4.5% | +7.6477 to +16.8528 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 285.5 | +4.3% | +6.9350 to +16.6030 | yes: power given |
| response time (ms), mean | 451.8 | 697.8 | +54.4% | +172.6031 to +319.3205 | yes: LOSS |
| response time (ms), 95th percentile | 1724 | 1417 | −17.8% | −943.9241 to +329.9431 | no |
| response time (ms), 99th percentile | 2502 | 1908 | −23.7% | −1559.9994 to +373.1450 | no |
| time over the response line (% of samples) | 20.51 | 61.13 | +198.0% | +32.6701 to +48.5687 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 24.3 | +161.3% | +10.2552 to +19.7448 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.1 | +17.100 (native is 0) | +14.8519 to +19.3481 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.29 | 2.255 | −80.0% | −12.6741 to −5.4059 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06286 | 0.09765 | +55.3% | +0.0231 to +0.0465 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.509 | 2.338 | +55.0% | +0.5479 to +1.1113 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00941 | +0.009 (native is 0) | +0.0082 to +0.0106 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.509 | 2.348 | +55.6% | +0.5584 to +1.1196 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 452.1 | 292.7 | −35.3% | −237.5759 to −81.2469 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.992 | 2.684 | +34.8% | +0.3823 to +1.0033 | yes: power given |
| pods started | 0 | 1 | +1.000 (native is 0) | +0.1740 to +1.8260 | yes: power given |
| pod start wait, total (s) | 0 | 3.5 | +3.500 (native is 0) | −0.5499 to +7.5499 | no |
| pod start wait, mean (s) | 0 | 1.55 | +1.550 (native is 0) | +0.1051 to +2.9949 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.84 | 76.02 | +77.4% | +27.1147 to +39.2419 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 823.3 | 1470 | +78.5% | +571.1780 to +722.0220 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.659 | −5.7% | −4.6725 to +3.9907 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 647.4 | +535694.9% | +335.3610 to +959.2349 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1027 | +171148.1% | +590.0844 to +1463.6927 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 129.7 | 956.9 | +637.5% | +718.9930 to +935.2820 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 14.7 | +14.700 (native is 0) | +7.7154 to +21.6846 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*