# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.38 | 6 |
| node-hours | 2.508 | 2.513 | 2.255 | 2.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 272.2 | 273.9 | 271.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 272.2 | 254.4 | 271.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 426.3 | 144 | 425.3 | 120.3 |
| response time (ms), 95th percentile | 1574 | 253.8 | 1821 | 262.2 |
| response time (ms), 99th percentile | 2252 | 375.6 | 2566 | 383.2 |
| time over the response line (% of samples) | 20.18 | 0.2628 | 20.78 | 0.3522 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 0.1 | 11.5 | 0.2222 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 116.3 | 104.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.25 | 1271 | 11.33 | 1337 |
| utilisation (used / allocatable) | 0.06331 | 0.0605 | 0.07206 | 0.0586 |
| CPU used (cores), mean | 1.519 | 1.452 | 1.534 | 1.406 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07694 | 0.07331 |
| CPU used with Omni's own (cores), mean | 1.519 | 1.452 | 1.611 | 1.48 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.5 | 448.4 | 398.5 | 461.1 |
| HPA replicas, mean | 2.009 | 1.972 | 2.413 | 2.365 |
| pods started | 0 | 0.2 | 1.7 | 1.444 |
| pod start wait, total (s) | 0 | 0.4 | 3.7 | 3.889 |
| pod start wait, mean (s) | 0 | 0.4 | 1.942 | 1.37 |
| host CPU busy, the real machine under kind (%) | 43.58 | 46.05 | 46.94 | 47.38 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 799.5 | 1501 | 811 | 1511 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.88 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 174 | 0.06667 | 194.3 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 803.5 | 0.6 | 855.1 |
| queue: job turnaround, submitted to done, mean (s) | 105.1 | 919 | 117.7 | 947 |
| queue: jobs unfinished at the window's end | 0 | 12.8 | 0 | 14.22 |
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
| node-hours | 2.515 | 2.517 | +0.1% | −0.0083 to +0.0131 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 271.9 | −0.2% | −1.7301 to +0.7982 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 271.9 | −0.2% | −1.7301 to +0.7982 | no |
| response time (ms), mean | 141.6 | 120.3 | −15.0% | −26.2067 to −16.3149 | yes: GAIN |
| response time (ms), 95th percentile | 248.2 | 262.2 | +5.6% | +1.5493 to +26.3662 | yes: LOSS |
| response time (ms), 99th percentile | 367.9 | 383.2 | +4.1% | −4.0661 to +34.5754 | no |
| time over the response line (% of samples) | 0.2317 | 0.3522 | +52.0% | +0.0147 to +0.2264 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1111 | 0.2222 | +100.0% | −0.3508 to +0.5730 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 104.2 | +104.222 (native is 0) | +81.6387 to +126.8058 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1255 | 1337 | +6.6% | −5.0655 to +170.1322 | no |
| utilisation (used / allocatable) | 0.06058 | 0.0586 | −3.3% | −0.0047 to +0.0007 | no |
| CPU used (cores), mean | 1.454 | 1.406 | −3.3% | −0.1117 to +0.0162 | no |
| Omni's own CPU (cores), mean | 0 | 0.07331 | +0.073 (native is 0) | +0.0653 to +0.0813 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.454 | 1.48 | +1.8% | −0.0386 to +0.0898 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.9 | 461.1 | +3.0% | −4.6998 to +31.1429 | no |
| HPA replicas, mean | 1.971 | 2.365 | +20.0% | +0.1506 to +0.6372 | yes: power given |
| pods started | 0.2222 | 1.444 | +550.0% | +0.0204 to +2.4240 | yes: power given |
| pod start wait, total (s) | 0.4444 | 3.889 | +775.0% | +0.0045 to +6.8844 | yes: LOSS |
| pod start wait, mean (s) | 0.4444 | 1.37 | +208.3% | −0.3473 to +2.1992 | no |
| host CPU busy, the real machine under kind (%) | 45.96 | 47.38 | +3.1% | +0.1710 to +2.6746 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1500 | 1511 | +0.7% | −5.8120 to +26.7009 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 165.6 | 194.3 | +17.3% | −24.7155 to +82.1507 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 763.2 | 855.1 | +12.0% | −105.7984 to +289.5762 | no |
| queue: job turnaround, submitted to done, mean (s) | 909.1 | 947 | +4.2% | −28.5921 to +104.4903 | no |
| queue: jobs unfinished at the window's end | 12.33 | 14.22 | +15.3% | −1.7256 to +5.5033 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.508 | 2.514 | +0.2% | −0.0024 to +0.0127 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 272.2 | −0.3% | −2.9948 to +1.5773 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 272.2 | −0.3% | −2.9948 to +1.5773 | no |
| response time (ms), mean | 426.3 | 144 | −66.2% | −431.9165 to −132.6570 | yes: GAIN |
| response time (ms), 95th percentile | 1574 | 253.8 | −83.9% | −2031.3462 to −608.9158 | yes: GAIN |
| response time (ms), 99th percentile | 2252 | 375.6 | −83.3% | −2895.8999 to −857.5397 | yes: GAIN |
| time over the response line (% of samples) | 20.18 | 0.2628 | −98.7% | −30.4349 to −9.4015 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 0.1 | −99.1% | −14.3654 to −7.2346 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.25 | 1271 | +12304.3% | +1072.9217 to +1449.4683 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06331 | 0.0605 | −4.4% | −0.0087 to +0.0031 | no |
| CPU used (cores), mean | 1.519 | 1.452 | −4.4% | −0.2095 to +0.0748 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.519 | 1.452 | −4.4% | −0.2095 to +0.0748 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.5 | 448.4 | +2.5% | −30.4263 to +52.0914 | no |
| HPA replicas, mean | 2.009 | 1.972 | −1.8% | −0.1554 to +0.0816 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2032 to +1.0032 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2032 to +1.0032 | no |
| host CPU busy, the real machine under kind (%) | 43.58 | 46.05 | +5.7% | −0.7079 to +5.6640 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 799.5 | 1501 | +87.7% | +660.9096 to +741.4904 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 174 | +417580.0% | +125.4143 to +222.5690 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 803.5 | +267733.3% | +623.5856 to +982.8144 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 105.1 | 919 | +774.6% | +736.3151 to +891.5932 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12.8 | +12.800 (native is 0) | +7.6220 to +17.9780 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.38 | −10.3% | −1.2430 to +0.0034 | no |
| node-hours | 2.508 | 2.255 | −10.1% | −0.5156 to +0.0085 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 273.9 | +0.3% | +0.5633 to +1.3462 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 254.4 | −6.8% | −38.3322 to +1.2833 | no |
| response time (ms), mean | 426.3 | 425.3 | −0.2% | −47.9061 to +45.9039 | no |
| response time (ms), 95th percentile | 1574 | 1821 | +15.7% | −19.4185 to +514.2725 | no |
| response time (ms), 99th percentile | 2252 | 2566 | +13.9% | −30.0921 to +657.8659 | no |
| time over the response line (% of samples) | 20.18 | 20.78 | +3.0% | −1.9731 to +3.1793 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 11.5 | +5.5% | −0.0032 to +1.2032 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 116.3 | +116.300 (native is 0) | +40.9852 to +191.6148 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.25 | 11.33 | +10.5% | −1.0763 to +3.2363 | no |
| utilisation (used / allocatable) | 0.06331 | 0.07206 | +13.8% | +0.0003 to +0.0172 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.519 | 1.534 | +1.0% | −0.0058 to +0.0358 | no |
| Omni's own CPU (cores), mean | 0 | 0.07694 | +0.077 (native is 0) | +0.0709 to +0.0830 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.519 | 1.611 | +6.1% | +0.0676 to +0.1164 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 437.5 | 398.5 | −8.9% | −75.5164 to −2.5126 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.009 | 2.413 | +20.1% | +0.2143 to +0.5940 | yes: power given |
| pods started | 0 | 1.7 | +1.700 (native is 0) | +0.7433 to +2.6567 | yes: power given |
| pod start wait, total (s) | 0 | 3.7 | +3.700 (native is 0) | +1.9790 to +5.4210 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.942 | +1.942 (native is 0) | +1.0611 to +2.8223 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.58 | 46.94 | +7.7% | +2.5611 to +4.1611 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 799.5 | 811 | +1.4% | −2.2478 to +25.2478 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.88 | −18.7% | −2.1024 to −0.1372 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.06667 | +60.0% | −0.0070 to +0.0570 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.6 | +100.0% | −0.1828 to +0.7828 | no |
| queue: job turnaround, submitted to done, mean (s) | 105.1 | 117.7 | +12.0% | −1.2668 to +26.4585 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.38 | −10.3% | −1.2430 to +0.0034 | no |
| node-hours | 2.513 | 2.255 | −10.3% | −0.5181 to +0.0006 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 273.9 | +0.6% | −0.6302 to +3.9572 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 254.4 | −6.5% | −38.7919 to +3.1605 | no |
| response time (ms), mean | 144 | 425.3 | +195.4% | +130.3873 to +432.1840 | yes: LOSS |
| response time (ms), 95th percentile | 253.8 | 1821 | +617.7% | +791.8429 to +2343.2731 | yes: LOSS |
| response time (ms), 99th percentile | 375.6 | 2566 | +583.2% | +1094.7995 to +3286.4139 | yes: LOSS |
| time over the response line (% of samples) | 0.2628 | 20.78 | +7808.7% | +10.8939 to +30.1487 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 11.5 | +11400.0% | +7.9579 to +14.8421 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 116.3 | +116.300 (native is 0) | +40.9852 to +191.6148 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1271 | 11.33 | −99.1% | −1447.5316 to −1072.6984 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0605 | 0.07206 | +19.1% | +0.0052 to +0.0179 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.452 | 1.534 | +5.7% | −0.0660 to +0.2308 | no |
| Omni's own CPU (cores), mean | 0 | 0.07694 | +0.077 (native is 0) | +0.0709 to +0.0830 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.452 | 1.611 | +11.0% | +0.0062 to +0.3124 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.4 | 398.5 | −11.1% | −78.0104 to −21.6837 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.972 | 2.413 | +22.4% | +0.2075 to +0.6746 | yes: power given |
| pods started | 0.2 | 1.7 | +750.0% | +0.5315 to +2.4685 | yes: power given |
| pod start wait, total (s) | 0.4 | 3.7 | +825.0% | +1.5790 to +5.0210 | yes: LOSS |
| pod start wait, mean (s) | 0.4 | 1.942 | +385.4% | +0.6851 to +2.3983 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.05 | 46.94 | +1.9% | −2.2970 to +4.0632 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1501 | 811 | −46.0% | −734.3926 to −645.0074 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 3.844 | −35.9% | −25.5829 to +21.2704 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 174 | 0.06667 | −100.0% | −222.5453 to −125.3880 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 803.5 | 0.6 | −99.9% | −982.5045 to −623.2955 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 919 | 117.7 | −87.2% | −874.8307 to −727.8859 | yes: GAIN |
| queue: jobs unfinished at the window's end | 12.8 | 0 | −100.0% | −17.9780 to −7.6220 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.507 | 2.517 | +0.4% | +0.0017 to +0.0175 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 271.9 | −0.2% | −3.4410 to +2.1355 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 271.9 | −0.2% | −3.4410 to +2.1355 | no |
| response time (ms), mean | 402.5 | 120.3 | −70.1% | −447.1782 to −117.1550 | yes: GAIN |
| response time (ms), 95th percentile | 1464 | 262.2 | −82.1% | −1961.6449 to −442.2906 | yes: GAIN |
| response time (ms), 99th percentile | 2086 | 383.2 | −81.6% | −2782.8080 to −622.9036 | yes: GAIN |
| time over the response line (% of samples) | 18.77 | 0.3522 | −98.1% | −29.8069 to −7.0250 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.44 | 0.2222 | −97.9% | −14.0226 to −6.4218 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 104.2 | +104.222 (native is 0) | +81.6387 to +126.8058 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.715 | 1337 | +13667.3% | +1123.9871 to +1531.5277 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06253 | 0.0586 | −6.3% | −0.0107 to +0.0028 | no |
| CPU used (cores), mean | 1.501 | 1.406 | −6.3% | −0.2565 to +0.0676 | no |
| Omni's own CPU (cores), mean | 0 | 0.07331 | +0.073 (native is 0) | +0.0653 to +0.0813 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.501 | 1.48 | −1.4% | −0.1758 to +0.1335 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 442.7 | 461.1 | +4.1% | −28.3764 to +65.0647 | no |
| HPA replicas, mean | 1.994 | 2.365 | +18.6% | +0.1379 to +0.6031 | yes: power given |
| pods started | 0 | 1.444 | +1.444 (native is 0) | +0.2843 to +2.6045 | yes: power given |
| pod start wait, total (s) | 0 | 3.889 | +3.889 (native is 0) | +0.4633 to +7.3145 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.37 | +1.370 (native is 0) | +0.2576 to +2.4831 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.06 | 47.38 | +10.0% | +0.7044 to +7.9327 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 793.4 | 1511 | +90.4% | +664.4557 to +770.2110 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 194.3 | +466255.6% | +160.2976 to +228.2487 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3333 | 855.1 | +256433.3% | +734.0538 to +975.5018 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 99.03 | 947 | +856.3% | +786.0751 to +909.9527 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 14.22 | +14.222 (native is 0) | +9.1704 to +19.2741 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*