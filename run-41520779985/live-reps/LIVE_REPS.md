# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.43 | 5.299 |
| node-hours | 2.52 | 2.516 | 2.274 | 2.219 |
| energy, parked workers still on at idle power (Wh, declared model) | 275 | 274.6 | 274.4 | 274.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275 | 274.6 | 256.6 | 252.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 459.4 | 423.9 | 466.2 | 415.1 |
| response time (ms), 95th percentile | 1725 | 1878 | 1948 | 2077 |
| response time (ms), 99th percentile | 2490 | 2696 | 2759 | 2888 |
| time over the response line (% of samples) | 21.15 | 15.42 | 21.03 | 14.9 |
| failed requests (%) | 0.01093 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 10 | 11.4 | 10.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 94.7 | 74.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 15 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.47 | 13.02 | 16.92 | 16.22 |
| utilisation (used / allocatable) | 0.06533 | 0.06503 | 0.07321 | 0.07558 |
| CPU used (cores), mean | 1.568 | 1.561 | 1.582 | 1.579 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07592 | 0.07321 |
| CPU used with Omni's own (cores), mean | 1.568 | 1.561 | 1.658 | 1.652 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 426.2 | 428.3 | 391.6 | 383.5 |
| HPA replicas, mean | 1.957 | 1.957 | 2.463 | 2.272 |
| pods started | 0 | 0 | 1.9 | 0.6 |
| pod start wait, total (s) | 0 | 0 | 3.9 | 1.1 |
| pod start wait, mean (s) | 0 | 0 | 1.633 | 0.7 |
| host CPU busy, the real machine under kind (%) | 44.48 | 44.7 | 48.36 | 48 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 823.4 | 823.1 | 839.9 | 837.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.022 | 4.785 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1583 | 0.0875 | 0.4542 | 0.4 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 0.7 | 3.2 | 2.5 |
| queue: job turnaround, submitted to done, mean (s) | 127.5 | 129.3 | 142.7 | 144 |
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
| worker nodes in service, mean | 6 | 5.299 | −11.7% | −1.4410 to +0.0392 | no |
| node-hours | 2.516 | 2.219 | −11.8% | −0.6079 to +0.0144 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274.5 | −0.0% | −0.7920 to +0.5976 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 252.5 | −8.1% | −45.6402 to +1.4124 | no |
| response time (ms), mean | 423.9 | 415.1 | −2.1% | −45.2548 to +27.6043 | no |
| response time (ms), 95th percentile | 1878 | 2077 | +10.6% | −21.1826 to +419.1506 | no |
| response time (ms), 99th percentile | 2696 | 2888 | +7.1% | −13.3492 to +397.0804 | no |
| time over the response line (% of samples) | 15.42 | 14.9 | −3.4% | −1.7661 to +0.7313 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 10.1 | +1.0% | −0.8204 to +1.0204 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 74.6 | +74.600 (native is 0) | +37.9767 to +111.2233 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.02 | 16.22 | +24.6% | −0.8215 to +7.2248 | no |
| utilisation (used / allocatable) | 0.06503 | 0.07558 | +16.2% | −0.0001 to +0.0212 | no |
| CPU used (cores), mean | 1.561 | 1.579 | +1.2% | −0.0061 to +0.0430 | no |
| Omni's own CPU (cores), mean | 0 | 0.07321 | +0.073 (native is 0) | +0.0652 to +0.0812 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.561 | 1.652 | +5.9% | +0.0623 to +0.1211 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 428.3 | 383.5 | −10.5% | −88.2937 to −1.4604 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.957 | 2.272 | +16.1% | +0.0869 to +0.5440 | yes: power given |
| pods started | 0 | 0.6 | +0.600 (native is 0) | −0.0032 to +1.2032 | no |
| pod start wait, total (s) | 0 | 1.1 | +1.100 (native is 0) | −0.0898 to +2.2898 | no |
| pod start wait, mean (s) | 0 | 0.7 | +0.700 (native is 0) | +0.0214 to +1.3786 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.7 | 48 | +7.4% | +2.6876 to +3.9073 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 823.1 | 837.9 | +1.8% | +3.8745 to +25.7255 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.785 | −20.2% | −2.3782 to −0.0517 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 0.4 | +357.1% | −0.0129 to +0.6379 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 2.5 | +257.1% | −1.0172 to +4.6172 | no |
| queue: job turnaround, submitted to done, mean (s) | 129.3 | 144 | +11.4% | +3.7627 to +25.6040 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.52 | 2.516 | −0.2% | −0.0099 to +0.0009 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275 | 274.6 | −0.2% | −1.2279 to +0.3170 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275 | 274.6 | −0.2% | −1.2279 to +0.3170 | no |
| response time (ms), mean | 459.4 | 423.9 | −7.7% | −70.6274 to −0.4220 | yes: GAIN |
| response time (ms), 95th percentile | 1725 | 1878 | +8.8% | −80.4833 to +385.7603 | no |
| response time (ms), 99th percentile | 2490 | 2696 | +8.3% | −66.8247 to +478.4729 | no |
| time over the response line (% of samples) | 21.15 | 15.42 | −27.1% | −9.0851 to −2.3763 | yes: GAIN |
| failed requests (%) | 0.01093 | 0 | −100.0% | −0.0357 to +0.0138 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 10 | −8.3% | −1.8204 to +0.0204 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.47 | 13.02 | −3.3% | −3.4916 to +2.5916 | no |
| utilisation (used / allocatable) | 0.06533 | 0.06503 | −0.5% | −0.0010 to +0.0003 | no |
| CPU used (cores), mean | 1.568 | 1.561 | −0.5% | −0.0229 to +0.0082 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.568 | 1.561 | −0.5% | −0.0229 to +0.0082 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 426.2 | 428.3 | +0.5% | −2.8935 to +7.1090 | no |
| HPA replicas, mean | 1.957 | 1.957 | −0.0% | −0.1402 to +0.1401 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 44.48 | 44.7 | +0.5% | −0.2370 to +0.6905 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 823.4 | 823.1 | −0.0% | −9.4979 to +8.8979 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1583 | 0.0875 | −44.7% | −0.2557 to +0.1140 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 0.7 | −46.2% | −2.4835 to +1.2835 | no |
| queue: job turnaround, submitted to done, mean (s) | 127.5 | 129.3 | +1.4% | −6.8895 to +10.4978 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.43 | −9.5% | −1.1854 to +0.0445 | no |
| node-hours | 2.52 | 2.274 | −9.8% | −0.5074 to +0.0145 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275 | 274.4 | −0.2% | −1.7009 to +0.5481 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275 | 256.6 | −6.7% | −38.4486 to +1.5541 | no |
| response time (ms), mean | 459.4 | 466.2 | +1.5% | −21.6314 to +35.1681 | no |
| response time (ms), 95th percentile | 1725 | 1948 | +13.0% | +38.4247 to +408.5783 | yes: LOSS |
| response time (ms), 99th percentile | 2490 | 2759 | +10.8% | +92.6463 to +445.8391 | yes: LOSS |
| time over the response line (% of samples) | 21.15 | 21.03 | −0.5% | −1.0343 to +0.8042 | no |
| failed requests (%) | 0.01093 | 0 | −100.0% | −0.0357 to +0.0138 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 11.4 | +4.6% | −0.1079 to +1.1079 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 94.7 | +94.700 (native is 0) | +29.3233 to +160.0767 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.47 | 16.92 | +25.7% | −1.0913 to +8.0013 | no |
| utilisation (used / allocatable) | 0.06533 | 0.07321 | +12.1% | +0.0005 to +0.0153 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.568 | 1.582 | +0.9% | −0.0177 to +0.0454 | no |
| Omni's own CPU (cores), mean | 0 | 0.07592 | +0.076 (native is 0) | +0.0700 to +0.0819 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.568 | 1.658 | +5.7% | +0.0533 to +0.1263 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 426.2 | 391.6 | −8.1% | −65.7850 to −3.3821 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.957 | 2.463 | +25.9% | +0.1819 to +0.8309 | yes: power given |
| pods started | 0 | 1.9 | +1.900 (native is 0) | +0.8634 to +2.9366 | yes: power given |
| pod start wait, total (s) | 0 | 3.9 | +3.900 (native is 0) | +1.5049 to +6.2951 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.633 | +1.633 (native is 0) | +0.8803 to +2.3864 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.48 | 48.36 | +8.7% | +3.3646 to +4.4044 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 823.4 | 839.9 | +2.0% | +3.4175 to +29.5825 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.022 | −16.3% | −1.9033 to −0.0522 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1583 | 0.4542 | +186.8% | −0.0359 to +0.6276 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 3.2 | +146.2% | −1.1987 to +4.9987 | no |
| queue: job turnaround, submitted to done, mean (s) | 127.5 | 142.7 | +11.9% | +4.4747 to +25.9670 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.43 | −9.5% | −1.1854 to +0.0445 | no |
| node-hours | 2.516 | 2.274 | −9.6% | −0.5047 to +0.0209 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274.4 | −0.0% | −1.6440 to +1.4021 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 256.6 | −6.6% | −38.2986 to +2.3150 | no |
| response time (ms), mean | 423.9 | 466.2 | +10.0% | −12.3887 to +96.9749 | no |
| response time (ms), 95th percentile | 1878 | 1948 | +3.8% | −162.9028 to +304.6288 | no |
| response time (ms), 99th percentile | 2696 | 2759 | +2.4% | −142.0132 to +268.8504 | no |
| time over the response line (% of samples) | 15.42 | 21.03 | +36.4% | +2.6280 to +8.6034 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 11.4 | +14.0% | +0.1749 to +2.6251 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 94.7 | +94.700 (native is 0) | +29.3233 to +160.0767 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.02 | 16.92 | +30.0% | −2.6897 to +10.4997 | no |
| utilisation (used / allocatable) | 0.06503 | 0.07321 | +12.6% | +0.0005 to +0.0158 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.561 | 1.582 | +1.4% | −0.0088 to +0.0513 | no |
| Omni's own CPU (cores), mean | 0 | 0.07592 | +0.076 (native is 0) | +0.0700 to +0.0819 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.561 | 1.658 | +6.2% | +0.0620 to +0.1323 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 428.3 | 391.6 | −8.6% | −70.6741 to −2.7084 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.957 | 2.463 | +25.9% | +0.2767 to +0.7361 | yes: power given |
| pods started | 0 | 1.9 | +1.900 (native is 0) | +0.8634 to +2.9366 | yes: power given |
| pod start wait, total (s) | 0 | 3.9 | +3.900 (native is 0) | +1.5049 to +6.2951 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.633 | +1.633 (native is 0) | +0.8803 to +2.3864 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.7 | 48.36 | +8.2% | +3.0323 to +4.2832 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 823.1 | 839.9 | +2.0% | +0.1136 to +33.4864 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.022 | −16.3% | −1.9033 to −0.0522 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 0.4542 | +419.0% | −0.0767 to +0.8100 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 3.2 | +357.1% | −0.7909 to +5.7909 | no |
| queue: job turnaround, submitted to done, mean (s) | 129.3 | 142.7 | +10.4% | −0.6921 to +27.5254 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.299 | −11.7% | −1.4410 to +0.0392 | no |
| node-hours | 2.52 | 2.219 | −12.0% | −0.6102 to +0.0077 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275 | 274.5 | −0.2% | −1.4942 to +0.3889 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275 | 252.5 | −8.2% | −45.7255 to +0.5869 | no |
| response time (ms), mean | 459.4 | 415.1 | −9.7% | −74.3171 to −14.3828 | yes: GAIN |
| response time (ms), 95th percentile | 1725 | 2077 | +20.4% | +37.3649 to +665.8801 | yes: LOSS |
| response time (ms), 99th percentile | 2490 | 2888 | +16.0% | +104.8945 to +690.4849 | yes: LOSS |
| time over the response line (% of samples) | 21.15 | 14.9 | −29.5% | −9.9245 to −2.5718 | yes: GAIN |
| failed requests (%) | 0.01093 | 0 | −100.0% | −0.0357 to +0.0138 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.9 | 10.1 | −7.3% | −2.0526 to +0.4526 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 74.6 | +74.600 (native is 0) | +37.9767 to +111.2233 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.47 | 16.22 | +20.4% | −1.9483 to +7.4517 | no |
| utilisation (used / allocatable) | 0.06533 | 0.07558 | +15.7% | −0.0003 to +0.0208 | no |
| CPU used (cores), mean | 1.568 | 1.579 | +0.7% | −0.0204 to +0.0427 | no |
| Omni's own CPU (cores), mean | 0 | 0.07321 | +0.073 (native is 0) | +0.0652 to +0.0812 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.568 | 1.652 | +5.4% | +0.0489 to +0.1198 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 426.2 | 383.5 | −10.0% | −84.1457 to −1.3929 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.957 | 2.272 | +16.1% | +0.0909 to +0.5399 | yes: power given |
| pods started | 0 | 0.6 | +0.600 (native is 0) | −0.0032 to +1.2032 | no |
| pod start wait, total (s) | 0 | 1.1 | +1.100 (native is 0) | −0.0898 to +2.2898 | no |
| pod start wait, mean (s) | 0 | 0.7 | +0.700 (native is 0) | +0.0214 to +1.3786 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.48 | 48 | +7.9% | +2.6606 to +4.3878 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 823.4 | 837.9 | +1.8% | −0.0709 to +29.0709 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.785 | −20.2% | −2.3782 to −0.0517 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1583 | 0.4 | +152.6% | +0.0071 to +0.4763 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 2.5 | +92.3% | −1.2962 to +3.6962 | no |
| queue: job turnaround, submitted to done, mean (s) | 127.5 | 144 | +12.9% | +1.1902 to +31.7848 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*