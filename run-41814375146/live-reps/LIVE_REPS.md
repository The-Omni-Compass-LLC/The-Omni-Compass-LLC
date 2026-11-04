# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.615 | 5.407 |
| node-hours | 2.517 | 2.514 | 2.351 | 2.263 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.1 | 274.8 | 275.1 | 275 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.1 | 274.8 | 263 | 256.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 494.8 | 472.5 | 503.5 | 442.2 |
| response time (ms), 95th percentile | 1882 | 2114 | 2154 | 2297 |
| response time (ms), 99th percentile | 2694 | 2985 | 3032 | 3106 |
| time over the response line (% of samples) | 23.99 | 18.01 | 23.51 | 16.7 |
| failed requests (%) | 0 | 0 | 0.02204 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 10.9 | 12.3 | 11 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 82.6 | 77 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 40.48 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.78 | 13.32 | 16.89 | 16.56 |
| utilisation (used / allocatable) | 0.06662 | 0.06649 | 0.07273 | 0.07603 |
| CPU used (cores), mean | 1.599 | 1.596 | 1.624 | 1.621 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07559 | 0.07582 |
| CPU used with Omni's own (cores), mean | 1.599 | 1.596 | 1.7 | 1.697 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 417.5 | 418.7 | 390.1 | 379.7 |
| HPA replicas, mean | 2.087 | 2.035 | 2.431 | 2.572 |
| pods started | 0 | 0.3 | 1.8 | 2 |
| pod start wait, total (s) | 0 | 0.6 | 3.5 | 3.4 |
| pod start wait, mean (s) | 0 | 0.45 | 1.717 | 1.242 |
| host CPU busy, the real machine under kind (%) | 45.48 | 45.68 | 49.27 | 49 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 832.7 | 836.7 | 853 | 850 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.349 | 4.948 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 0.075 | 0.2625 | 0.1833 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.4 | 1.8 | 1.1 |
| queue: job turnaround, submitted to done, mean (s) | 138.7 | 144.8 | 157.6 | 156.6 |
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
| worker nodes in service, mean | 6 | 5.407 | −9.9% | −1.2331 to +0.0478 | no |
| node-hours | 2.514 | 2.263 | −10.0% | −0.5169 to +0.0159 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.8 | 275 | +0.1% | −0.6136 to +0.9025 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.8 | 256.4 | −6.7% | −38.3213 to +1.3602 | no |
| response time (ms), mean | 472.5 | 442.2 | −6.4% | −42.3804 to −18.1949 | yes: GAIN |
| response time (ms), 95th percentile | 2114 | 2297 | +8.6% | +66.9416 to +298.3924 | yes: LOSS |
| response time (ms), 99th percentile | 2985 | 3106 | +4.0% | −8.8248 to +249.6664 | no |
| time over the response line (% of samples) | 18.01 | 16.7 | −7.2% | −2.5880 to −0.0227 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 11 | +0.9% | −0.3060 to +0.5060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 77 | +77.000 (native is 0) | +32.2617 to +121.7383 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.32 | 16.56 | +24.3% | +0.2830 to +6.1970 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06649 | 0.07603 | +14.3% | −0.0010 to +0.0201 | no |
| CPU used (cores), mean | 1.596 | 1.621 | +1.6% | +0.0106 to +0.0401 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07582 | +0.076 (native is 0) | +0.0698 to +0.0819 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.596 | 1.697 | +6.3% | +0.0844 to +0.1179 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.7 | 379.7 | −9.3% | −79.3849 to +1.3842 | no |
| HPA replicas, mean | 2.035 | 2.572 | +26.4% | +0.3275 to +0.7465 | yes: power given |
| pods started | 0.3 | 2 | +566.7% | +0.5295 to +2.8705 | yes: power given |
| pod start wait, total (s) | 0.6 | 3.4 | +466.7% | +0.3038 to +5.2962 | yes: LOSS |
| pod start wait, mean (s) | 0.45 | 1.242 | +175.9% | −0.1357 to +1.7191 | no |
| host CPU busy, the real machine under kind (%) | 45.68 | 49 | +7.3% | +2.8607 to +3.7800 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 836.7 | 850 | +1.6% | +5.3129 to +21.2871 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.948 | −17.5% | −1.9496 to −0.1535 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.1833 | +144.4% | −0.0151 to +0.2318 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.1 | +175.0% | +0.1111 to +1.2889 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 144.8 | 156.6 | +8.1% | +3.6172 to +19.9161 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 2.517 | 2.514 | −0.1% | −0.0088 to +0.0028 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.1 | 274.8 | −0.1% | −1.0364 to +0.4535 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.1 | 274.8 | −0.1% | −1.0364 to +0.4535 | no |
| response time (ms), mean | 494.8 | 472.5 | −4.5% | −40.9909 to −3.5996 | yes: GAIN |
| response time (ms), 95th percentile | 1882 | 2114 | +12.3% | +31.2553 to +431.6947 | yes: LOSS |
| response time (ms), 99th percentile | 2694 | 2985 | +10.8% | +61.3741 to +520.6991 | yes: LOSS |
| time over the response line (% of samples) | 23.99 | 18.01 | −25.0% | −8.5155 to −3.4630 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 10.9 | −6.8% | −2.1821 to +0.5821 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.78 | 13.32 | +13.1% | −0.4556 to +3.5356 | no |
| utilisation (used / allocatable) | 0.06662 | 0.06649 | −0.2% | −0.0008 to +0.0005 | no |
| CPU used (cores), mean | 1.599 | 1.596 | −0.2% | −0.0183 to +0.0122 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.599 | 1.596 | −0.2% | −0.0183 to +0.0122 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 417.5 | 418.7 | +0.3% | −2.2662 to +4.7761 | no |
| HPA replicas, mean | 2.087 | 2.035 | −2.5% | −0.1758 to +0.0722 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.600 (native is 0) | −0.3048 to +1.5048 | no |
| pod start wait, mean (s) | 0 | 0.45 | +0.450 (native is 0) | −0.2742 to +1.1742 | no |
| host CPU busy, the real machine under kind (%) | 45.48 | 45.68 | +0.4% | −0.1835 to +0.5819 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 832.7 | 836.7 | +0.5% | −1.3741 to +9.3741 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 0.075 | −14.3% | −0.0652 to +0.0402 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.4 | −33.3% | −0.7642 to +0.3642 | no |
| queue: job turnaround, submitted to done, mean (s) | 138.7 | 144.8 | +4.4% | −1.0427 to +13.1510 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.615 | −6.4% | −0.9445 to +0.1738 | no |
| node-hours | 2.517 | 2.351 | −6.6% | −0.3961 to +0.0638 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.1 | 275.1 | −0.0% | −1.1761 to +1.1363 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.1 | 263 | −4.4% | −29.2733 to +4.9835 | no |
| response time (ms), mean | 494.8 | 503.5 | +1.8% | −19.0037 to +36.4253 | no |
| response time (ms), 95th percentile | 1882 | 2154 | +14.4% | +86.7492 to +456.2948 | yes: LOSS |
| response time (ms), 99th percentile | 2694 | 3032 | +12.6% | +104.4176 to +571.8476 | yes: LOSS |
| time over the response line (% of samples) | 23.99 | 23.51 | −2.0% | −1.2374 to +0.2761 | no |
| failed requests (%) | 0 | 0.02204 | +0.022 (native is 0) | −0.0112 to +0.0553 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 12.3 | +5.1% | −0.0911 to +1.2911 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 82.6 | +82.600 (native is 0) | +31.7274 to +133.4726 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.78 | 16.89 | +43.4% | +1.8205 to +8.3961 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06662 | 0.07273 | +9.2% | −0.0019 to +0.0141 | no |
| CPU used (cores), mean | 1.599 | 1.624 | +1.6% | −0.0033 to +0.0538 | no |
| Omni's own CPU (cores), mean | 0 | 0.07559 | +0.076 (native is 0) | +0.0705 to +0.0807 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.599 | 1.7 | +6.3% | +0.0697 to +0.1320 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 417.5 | 390.1 | −6.6% | −61.8761 to +7.1038 | no |
| HPA replicas, mean | 2.087 | 2.431 | +16.5% | +0.1615 to +0.5258 | yes: power given |
| pods started | 0 | 1.8 | +1.800 (native is 0) | +1.1427 to +2.4573 | yes: power given |
| pod start wait, total (s) | 0 | 3.5 | +3.500 (native is 0) | +1.9826 to +5.0174 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.717 | +1.717 (native is 0) | +1.1061 to +2.3273 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.48 | 49.27 | +8.3% | +3.3139 to +4.2678 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 832.7 | 853 | +2.4% | +9.6312 to +30.9688 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.349 | −10.8% | −1.5346 to +0.2328 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 0.2625 | +200.0% | −0.0908 to +0.4408 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.8 | +200.0% | −1.0570 to +3.4570 | no |
| queue: job turnaround, submitted to done, mean (s) | 138.7 | 157.6 | +13.6% | +8.5690 to +29.1893 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.615 | −6.4% | −0.9445 to +0.1738 | no |
| node-hours | 2.514 | 2.351 | −6.5% | −0.3944 to +0.0681 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.8 | 275.1 | +0.1% | −0.2204 to +0.7635 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.8 | 263 | −4.3% | −29.1298 to +5.4229 | no |
| response time (ms), mean | 472.5 | 503.5 | +6.6% | +4.5417 to +57.4704 | yes: LOSS |
| response time (ms), 95th percentile | 2114 | 2154 | +1.9% | −51.3171 to +131.4111 | no |
| response time (ms), 99th percentile | 2985 | 3032 | +1.6% | −88.1184 to +182.3104 | no |
| time over the response line (% of samples) | 18.01 | 23.51 | +30.6% | +3.3140 to +7.7031 | yes: LOSS |
| failed requests (%) | 0 | 0.02204 | +0.022 (native is 0) | −0.0112 to +0.0553 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 12.3 | +12.8% | −0.1888 to +2.9888 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 82.6 | +82.600 (native is 0) | +31.7274 to +133.4726 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.32 | 16.89 | +26.8% | +0.4976 to +6.6391 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06649 | 0.07273 | +9.4% | −0.0018 to +0.0143 | no |
| CPU used (cores), mean | 1.596 | 1.624 | +1.8% | +0.0038 to +0.0528 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07559 | +0.076 (native is 0) | +0.0705 to +0.0807 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.596 | 1.7 | +6.5% | +0.0770 to +0.1308 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.7 | 390.1 | −6.8% | −63.9125 to +6.6303 | no |
| HPA replicas, mean | 2.035 | 2.431 | +19.4% | +0.2418 to +0.5491 | yes: power given |
| pods started | 0.3 | 1.8 | +500.0% | +0.8921 to +2.1079 | yes: power given |
| pod start wait, total (s) | 0.6 | 3.5 | +483.3% | +1.4516 to +4.3484 | yes: LOSS |
| pod start wait, mean (s) | 0.45 | 1.717 | +281.5% | +0.3993 to +2.1340 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.68 | 49.27 | +7.9% | +3.1990 to +3.9844 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 836.7 | 853 | +1.9% | +7.2016 to +25.3984 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.349 | −10.8% | −1.5346 to +0.2328 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.2625 | +250.0% | −0.0950 to +0.4700 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.8 | +350.0% | −1.0362 to +3.8362 | no |
| queue: job turnaround, submitted to done, mean (s) | 144.8 | 157.6 | +8.9% | +5.9902 to +19.6598 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.407 | −9.9% | −1.2331 to +0.0478 | no |
| node-hours | 2.517 | 2.263 | −10.1% | −0.5178 to +0.0108 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.1 | 275 | −0.1% | −1.2089 to +0.9149 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.1 | 256.4 | −6.8% | −38.3625 to +0.8185 | no |
| response time (ms), mean | 494.8 | 442.2 | −10.6% | −73.2590 to −31.9068 | yes: GAIN |
| response time (ms), 95th percentile | 1882 | 2297 | +22.0% | +137.7072 to +690.5768 | yes: LOSS |
| response time (ms), 99th percentile | 2694 | 3106 | +15.3% | +121.7877 to +701.1271 | yes: LOSS |
| time over the response line (% of samples) | 23.99 | 16.7 | −30.4% | −10.4195 to −4.1696 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 11 | −6.0% | −2.0081 to +0.6081 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 77 | +77.000 (native is 0) | +32.2617 to +121.7383 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.78 | 16.56 | +40.6% | +1.2465 to +8.3135 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06662 | 0.07603 | +14.1% | −0.0010 to +0.0199 | no |
| CPU used (cores), mean | 1.599 | 1.621 | +1.4% | +0.0118 to +0.0328 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07582 | +0.076 (native is 0) | +0.0698 to +0.0819 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.599 | 1.697 | +6.1% | +0.0836 to +0.1126 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 417.5 | 379.7 | −9.0% | −76.9293 to +1.4385 | no |
| HPA replicas, mean | 2.087 | 2.572 | +23.2% | +0.2851 to +0.6853 | yes: power given |
| pods started | 0 | 2 | +2.000 (native is 0) | +0.9884 to +3.0116 | yes: power given |
| pod start wait, total (s) | 0 | 3.4 | +3.400 (native is 0) | +1.2888 to +5.5112 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.242 | +1.242 (native is 0) | +0.6965 to +1.7869 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.48 | 49 | +7.7% | +2.9955 to +4.0435 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 832.7 | 850 | +2.1% | +7.5093 to +27.0907 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.948 | −17.5% | −1.9496 to −0.1535 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 0.1833 | +109.5% | −0.0404 to +0.2321 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.1 | +83.3% | −0.2726 to +1.2726 | no |
| queue: job turnaround, submitted to done, mean (s) | 138.7 | 156.5 | +12.8% | +6.5877 to +29.0540 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*