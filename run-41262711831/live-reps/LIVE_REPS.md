# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 120 s | omni, a decision every 90 s | omni, a decision every 75 s | omni, a decision every 30 s | omni, a decision every 15 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.515 | 1.515 | 1.512 | 1.514 | 1.513 | 1.514 | 1.514 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.6 | 158.2 | 158.6 | 158.5 | 158.5 | 158.6 | 158.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.6 | 158.2 | 158.6 | 158.5 | 158.5 | 158.6 | 158.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| response time (ms), mean | 150.8 | 77.82 | 77.62 | 78.13 | 77.66 | 78.16 | 78.48 | 79.56 |
| response time (ms), 95th percentile | 341 | 116.9 | 116.2 | 117 | 116.9 | 117.4 | 118.8 | 122.4 |
| response time (ms), 99th percentile | 536.6 | 161.2 | 155.1 | 164.7 | 156.8 | 162.6 | 164.3 | 165.2 |
| time over the response line (% of samples) | 1.894 | 0.02388 | 0.02403 | 0.02424 | 0.02395 | 0.06003 | 0 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.1 | 16.1 | 17.5 | 17.4 | 18.4 | 20.6 | 19.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | nan | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.275 | 0.215 | 0.185 | 0.27 | 0.1067 | 0.185 | 0.3667 | 0.105 |
| utilisation (used / allocatable) | 0.03794 | 0.03625 | 0.03607 | 0.03632 | 0.03635 | 0.03606 | 0.03653 | 0.03694 |
| CPU used (cores), mean | 0.9105 | 0.87 | 0.8657 | 0.8717 | 0.8723 | 0.8654 | 0.8768 | 0.8866 |
| Omni's own CPU (cores), mean | 0 | 0.00872 | 0.00625 | 0.00698 | 0.00758 | 0.01415 | 0.02507 | 0.06918 |
| CPU used with Omni's own (cores), mean | 0.9105 | 0.8787 | 0.872 | 0.8787 | 0.8799 | 0.8795 | 0.9019 | 0.9558 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 740.4 | 765.1 | 761.8 | 761.5 | 756.3 | 769.2 | 758.6 | 748.6 |
| HPA replicas, mean | 8.388 | 7.971 | 8.244 | 8.414 | 7.654 | 7.508 | 8.433 | 8.453 |
| pods started | 5.4 | 3.6 | 4.6 | 4.2 | 4 | 4.2 | 4.7 | 3.9 |
| pod start wait, total (s) | 9.1 | 5.6 | 7.1 | 6.5 | 5.9 | 6 | 6.4 | 5.8 |
| pod start wait, mean (s) | 1.687 | 1.537 | 1.48 | 1.46 | 1.507 | 1.333 | 1.35 | 1.497 |
| host CPU busy, the real machine under kind (%) | 27.82 | 26.98 | 26.93 | 27.01 | 26.93 | 27.08 | 27.55 | 29.45 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan | nan | nan | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan | nan | nan | nan | nan | nan |

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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.515 | +0.0% | −0.0009 to +0.0019 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.6 | −0.2% | −0.6562 to −0.0507 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.6 | −0.2% | −0.6562 to −0.0507 | yes: GAIN |
| response time (ms), mean | 150.8 | 77.82 | −48.4% | −95.6237 to −50.2513 | yes: GAIN |
| response time (ms), 95th percentile | 341 | 116.9 | −65.7% | −287.8426 to −160.4754 | yes: GAIN |
| response time (ms), 99th percentile | 536.6 | 161.2 | −70.0% | −482.8245 to −268.0735 | yes: GAIN |
| time over the response line (% of samples) | 1.894 | 0.02388 | −98.7% | −3.1674 to −0.5730 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0 | −100.0% | −3.3086 to −0.4914 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.1 | +17.100 (native is 0) | +14.8519 to +19.3481 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.275 | 0.215 | −21.8% | −0.4952 to +0.3752 | no |
| utilisation (used / allocatable) | 0.03794 | 0.03625 | −4.4% | −0.0028 to −0.0006 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9105 | 0.87 | −4.4% | −0.0674 to −0.0136 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00872 | +0.009 (native is 0) | +0.0074 to +0.0101 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9105 | 0.8787 | −3.5% | −0.0577 to −0.0059 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 740.4 | 765.1 | +3.3% | +5.0400 to +44.3552 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.388 | 7.971 | −5.0% | −0.8887 to +0.0544 | no |
| pods started | 5.4 | 3.6 | −33.3% | −2.8003 to −0.7997 | yes: GAIN |
| pod start wait, total (s) | 9.1 | 5.6 | −38.5% | −6.6316 to −0.3684 | yes: GAIN |
| pod start wait, mean (s) | 1.687 | 1.537 | −8.9% | −0.6013 to +0.3013 | no |
| host CPU busy, the real machine under kind (%) | 27.82 | 26.98 | −3.0% | −1.2906 to −0.3815 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.515 | 1.512 | −0.2% | −0.0074 to +0.0014 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.2 | −0.5% | −1.0931 to −0.4180 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.2 | −0.5% | −1.0931 to −0.4180 | yes: GAIN |
| response time (ms), mean | 150.8 | 77.62 | −48.5% | −96.3388 to −49.9258 | yes: GAIN |
| response time (ms), 95th percentile | 341 | 116.2 | −65.9% | −289.3416 to −160.2114 | yes: GAIN |
| response time (ms), 99th percentile | 536.6 | 155.1 | −71.1% | −486.8496 to −276.2110 | yes: GAIN |
| time over the response line (% of samples) | 1.894 | 0.02403 | −98.7% | −3.1676 to −0.5725 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0 | −100.0% | −3.3086 to −0.4914 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.1 | +16.100 (native is 0) | +15.1198 to +17.0802 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.275 | 0.185 | −32.7% | −0.3585 to +0.1785 | no |
| utilisation (used / allocatable) | 0.03794 | 0.03607 | −4.9% | −0.0033 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9105 | 0.8657 | −4.9% | −0.0791 to −0.0105 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00625 | +0.006 (native is 0) | +0.0054 to +0.0071 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9105 | 0.872 | −4.2% | −0.0722 to −0.0049 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 740.4 | 761.8 | +2.9% | −11.1316 to +53.8790 | no |
| HPA replicas, mean | 8.388 | 8.244 | −1.7% | −0.3646 to +0.0769 | no |
| pods started | 5.4 | 4.6 | −14.8% | −1.6793 to +0.0793 | no |
| pod start wait, total (s) | 9.1 | 7.1 | −22.0% | −5.1088 to +1.1088 | no |
| pod start wait, mean (s) | 1.687 | 1.48 | −12.3% | −0.6339 to +0.2206 | no |
| host CPU busy, the real machine under kind (%) | 27.82 | 26.93 | −3.2% | −1.7895 to +0.0140 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.515 | ±0.0% | −0.0019 to +0.0019 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.6 | −0.2% | −0.6568 to −0.1318 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.6 | −0.2% | −0.6568 to −0.1318 | yes: GAIN |
| response time (ms), mean | 150.8 | 78.13 | −48.2% | −95.2935 to −49.9551 | yes: GAIN |
| response time (ms), 95th percentile | 341 | 117 | −65.7% | −287.7617 to −160.1923 | yes: GAIN |
| response time (ms), 99th percentile | 536.6 | 164.7 | −69.3% | −478.8773 to −265.0175 | yes: GAIN |
| time over the response line (% of samples) | 1.894 | 0.02424 | −98.7% | −3.1338 to −0.6058 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0 | −100.0% | −3.3086 to −0.4914 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.5 | +17.500 (native is 0) | +16.1832 to +18.8168 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.275 | 0.27 | −1.8% | −0.4477 to +0.4377 | no |
| utilisation (used / allocatable) | 0.03794 | 0.03632 | −4.3% | −0.0026 to −0.0006 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9105 | 0.8717 | −4.3% | −0.0628 to −0.0148 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00698 | +0.007 (native is 0) | +0.0060 to +0.0080 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9105 | 0.8787 | −3.5% | −0.0549 to −0.0087 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 740.4 | 761.5 | +2.8% | +6.2919 to +35.8581 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.388 | 8.414 | +0.3% | −0.2458 to +0.2975 | no |
| pods started | 5.4 | 4.2 | −22.2% | −2.4526 to +0.0526 | no |
| pod start wait, total (s) | 9.1 | 6.5 | −28.6% | −5.4050 to +0.2050 | no |
| pod start wait, mean (s) | 1.687 | 1.46 | −13.4% | −0.5524 to +0.0991 | no |
| host CPU busy, the real machine under kind (%) | 27.82 | 27.01 | −2.9% | −1.2821 to −0.3318 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.513 | −0.1% | −0.0041 to +0.0007 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.5 | −0.3% | −0.9818 to −0.1054 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.5 | −0.3% | −0.9818 to −0.1054 | yes: GAIN |
| response time (ms), mean | 150.8 | 77.66 | −48.5% | −96.4384 to −49.7541 | yes: GAIN |
| response time (ms), 95th percentile | 341 | 116.9 | −65.7% | −289.4418 to −158.6922 | yes: GAIN |
| response time (ms), 99th percentile | 536.6 | 156.8 | −70.8% | −489.4766 to −270.1988 | yes: GAIN |
| time over the response line (% of samples) | 1.894 | 0.02395 | −98.7% | −3.1565 to −0.5837 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0 | −100.0% | −3.3086 to −0.4914 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 17.4 | +17.400 (native is 0) | +14.6153 to +20.1847 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.275 | 0.1067 | −61.2% | −0.6053 to +0.2687 | no |
| utilisation (used / allocatable) | 0.03794 | 0.03635 | −4.2% | −0.0030 to −0.0002 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9105 | 0.8723 | −4.2% | −0.0711 to −0.0053 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00758 | +0.008 (native is 0) | +0.0064 to +0.0087 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9105 | 0.8799 | −3.4% | −0.0626 to +0.0013 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 740.4 | 756.3 | +2.1% | −18.0882 to +49.7443 | no |
| HPA replicas, mean | 8.388 | 7.654 | −8.7% | −1.3831 to −0.0834 | yes: GAIN |
| pods started | 5.4 | 4 | −25.9% | −2.5285 to −0.2715 | yes: GAIN |
| pod start wait, total (s) | 9.1 | 5.9 | −35.2% | −5.9969 to −0.4031 | yes: GAIN |
| pod start wait, mean (s) | 1.687 | 1.507 | −10.7% | −0.4891 to +0.1296 | no |
| host CPU busy, the real machine under kind (%) | 27.82 | 26.93 | −3.2% | −1.6546 to −0.1101 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.514 | −0.0% | −0.0029 to +0.0016 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.5 | −0.3% | −0.9275 to −0.0936 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.5 | −0.3% | −0.9275 to −0.0936 | yes: GAIN |
| response time (ms), mean | 150.8 | 78.16 | −48.2% | −95.1741 to −50.0221 | yes: GAIN |
| response time (ms), 95th percentile | 341 | 117.4 | −65.6% | −286.6621 to −160.4979 | yes: GAIN |
| response time (ms), 99th percentile | 536.6 | 162.6 | −69.7% | −476.8285 to −271.2551 | yes: GAIN |
| time over the response line (% of samples) | 1.894 | 0.06003 | −96.8% | −3.1313 to −0.5368 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0 | −100.0% | −3.3086 to −0.4914 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.4 | +18.400 (native is 0) | +14.4216 to +22.3784 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.275 | 0.185 | −32.7% | −0.5614 to +0.3814 | no |
| utilisation (used / allocatable) | 0.03794 | 0.03606 | −5.0% | −0.0029 to −0.0009 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9105 | 0.8654 | −5.0% | −0.0686 to −0.0216 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01415 | +0.014 (native is 0) | +0.0119 to +0.0164 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9105 | 0.8795 | −3.4% | −0.0526 to −0.0093 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 740.4 | 769.2 | +3.9% | +18.4767 to +39.0730 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.388 | 7.508 | −10.5% | −1.3821 to −0.3781 | yes: GAIN |
| pods started | 5.4 | 4.2 | −22.2% | −2.4972 to +0.0972 | no |
| pod start wait, total (s) | 9.1 | 6 | −34.1% | −5.5652 to −0.6348 | yes: GAIN |
| pod start wait, mean (s) | 1.687 | 1.333 | −20.9% | −0.6665 to −0.0402 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 27.82 | 27.08 | −2.7% | −1.1326 to −0.3431 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.514 | −0.0% | −0.0026 to +0.0019 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.6 | −0.2% | −0.7261 to −0.0015 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.6 | −0.2% | −0.7261 to −0.0015 | yes: GAIN |
| response time (ms), mean | 150.8 | 78.48 | −47.9% | −94.8076 to −49.7498 | yes: GAIN |
| response time (ms), 95th percentile | 341 | 118.8 | −65.2% | −285.6297 to −158.7473 | yes: GAIN |
| response time (ms), 99th percentile | 536.6 | 164.3 | −69.4% | −474.5934 to −270.0088 | yes: GAIN |
| time over the response line (% of samples) | 1.894 | 0 | −100.0% | −3.1837 to −0.6044 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0 | −100.0% | −3.3086 to −0.4914 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.6 | +20.600 (native is 0) | +19.2854 to +21.9146 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.275 | 0.3667 | +33.3% | −0.4203 to +0.6036 | no |
| utilisation (used / allocatable) | 0.03794 | 0.03653 | −3.7% | −0.0025 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9105 | 0.8768 | −3.7% | −0.0588 to −0.0085 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02507 | +0.025 (native is 0) | +0.0217 to +0.0285 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9105 | 0.9019 | −0.9% | −0.0310 to +0.0138 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 740.4 | 758.6 | +2.5% | +2.0067 to +34.3334 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.388 | 8.433 | +0.5% | −0.1506 to +0.2420 | no |
| pods started | 5.4 | 4.7 | −13.0% | −1.7144 to +0.3144 | no |
| pod start wait, total (s) | 9.1 | 6.4 | −29.7% | −4.7246 to −0.6754 | yes: GAIN |
| pod start wait, mean (s) | 1.687 | 1.35 | −20.0% | −0.6109 to −0.0624 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 27.82 | 27.55 | −0.9% | −0.7797 to +0.2546 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.515 | +0.0% | −0.0017 to +0.0027 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159 | 158.8 | −0.1% | −0.5509 to +0.1645 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159 | 158.8 | −0.1% | −0.5509 to +0.1645 | no |
| response time (ms), mean | 150.8 | 79.56 | −47.2% | −93.4283 to −48.9580 | yes: GAIN |
| response time (ms), 95th percentile | 341 | 122.4 | −64.1% | −280.7371 to −156.4879 | yes: GAIN |
| response time (ms), 99th percentile | 536.6 | 165.2 | −69.2% | −473.1217 to −269.7419 | yes: GAIN |
| time over the response line (% of samples) | 1.894 | 0 | −100.0% | −3.1837 to −0.6044 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.9 | 0 | −100.0% | −3.3086 to −0.4914 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.8 | +19.800 (native is 0) | +18.1899 to +21.4101 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.275 | 0.105 | −61.8% | −0.4968 to +0.1568 | no |
| utilisation (used / allocatable) | 0.03794 | 0.03694 | −2.6% | −0.0021 to +0.0001 | no |
| CPU used (cores), mean | 0.9105 | 0.8866 | −2.6% | −0.0506 to +0.0029 | no |
| Omni's own CPU (cores), mean | 0 | 0.06918 | +0.069 (native is 0) | +0.0600 to +0.0783 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9105 | 0.9558 | +5.0% | +0.0254 to +0.0652 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 740.4 | 748.6 | +1.1% | −11.7681 to +28.1591 | no |
| HPA replicas, mean | 8.388 | 8.453 | +0.8% | −0.2322 to +0.3631 | no |
| pods started | 5.4 | 3.9 | −27.8% | −2.8168 to −0.1832 | yes: GAIN |
| pod start wait, total (s) | 9.1 | 5.8 | −36.3% | −6.1020 to −0.4980 | yes: GAIN |
| pod start wait, mean (s) | 1.687 | 1.497 | −11.3% | −0.5278 to +0.1478 | no |
| host CPU busy, the real machine under kind (%) | 27.82 | 29.45 | +5.9% | +1.3339 to +1.9381 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.512 | −0.2% | −0.0082 to +0.0012 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.2 | −0.3% | −0.8074 to +0.0032 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.2 | −0.3% | −0.8074 to +0.0032 | no |
| response time (ms), mean | 77.82 | 77.62 | −0.3% | −1.0755 to +0.6860 | no |
| response time (ms), 95th percentile | 116.9 | 116.2 | −0.5% | −2.9811 to +1.7461 | no |
| response time (ms), 99th percentile | 161.2 | 155.1 | −3.8% | −11.5486 to −0.6140 | yes: GAIN |
| time over the response line (% of samples) | 0.02388 | 0.02403 | +0.6% | −0.0570 to +0.0573 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.1 | 16.1 | −5.8% | −2.6519 to +0.6519 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.215 | 0.185 | −14.0% | −0.4464 to +0.3864 | no |
| utilisation (used / allocatable) | 0.03625 | 0.03607 | −0.5% | −0.0007 to +0.0004 | no |
| CPU used (cores), mean | 0.87 | 0.8657 | −0.5% | −0.0173 to +0.0087 | no |
| Omni's own CPU (cores), mean | 0.00872 | 0.00625 | −28.3% | −0.0030 to −0.0019 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8787 | 0.872 | −0.8% | −0.0202 to +0.0067 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 765.1 | 761.8 | −0.4% | −21.2495 to +14.6017 | no |
| HPA replicas, mean | 7.971 | 8.244 | +3.4% | −0.2931 to +0.8397 | no |
| pods started | 3.6 | 4.6 | +27.8% | −0.1681 to +2.1681 | no |
| pod start wait, total (s) | 5.6 | 7.1 | +26.8% | −1.1390 to +4.1390 | no |
| pod start wait, mean (s) | 1.537 | 1.48 | −3.7% | −0.4166 to +0.3032 | no |
| host CPU busy, the real machine under kind (%) | 26.98 | 26.93 | −0.2% | −0.5361 to +0.4327 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.515 | −0.0% | −0.0023 to +0.0013 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.6 | −0.0% | −0.3154 to +0.2337 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.6 | −0.0% | −0.3154 to +0.2337 | no |
| response time (ms), mean | 77.82 | 78.13 | +0.4% | −0.3511 to +0.9776 | no |
| response time (ms), 95th percentile | 116.9 | 117 | +0.2% | −1.1153 to +1.4793 | no |
| response time (ms), 99th percentile | 161.2 | 164.7 | +2.2% | −5.3904 to +12.3936 | no |
| time over the response line (% of samples) | 0.02388 | 0.02424 | +1.5% | −0.0570 to +0.0577 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.1 | 17.5 | +2.3% | −1.1155 to +1.9155 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.215 | 0.27 | +25.6% | −0.2798 to +0.3898 | no |
| utilisation (used / allocatable) | 0.03625 | 0.03632 | +0.2% | −0.0003 to +0.0005 | no |
| CPU used (cores), mean | 0.87 | 0.8717 | +0.2% | −0.0083 to +0.0117 | no |
| Omni's own CPU (cores), mean | 0.00872 | 0.00698 | −20.0% | −0.0022 to −0.0013 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8787 | 0.8787 | −0.0% | −0.0102 to +0.0101 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 765.1 | 761.5 | −0.5% | −20.9554 to +13.7102 | no |
| HPA replicas, mean | 7.971 | 8.414 | +5.6% | −0.0784 to +0.9644 | no |
| pods started | 3.6 | 4.2 | +16.7% | −0.5778 to +1.7778 | no |
| pod start wait, total (s) | 5.6 | 6.5 | +16.1% | −1.8280 to +3.6280 | no |
| pod start wait, mean (s) | 1.537 | 1.46 | −5.0% | −0.5477 to +0.3943 | no |
| host CPU busy, the real machine under kind (%) | 26.98 | 27.01 | +0.1% | −0.2884 to +0.3467 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.513 | −0.1% | −0.0039 to −0.0005 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.5 | −0.1% | −0.4246 to +0.0443 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.5 | −0.1% | −0.4246 to +0.0443 | no |
| response time (ms), mean | 77.82 | 77.66 | −0.2% | −1.1703 to +0.8528 | no |
| response time (ms), 95th percentile | 116.9 | 116.9 | +0.1% | −2.1921 to +2.3761 | no |
| response time (ms), 99th percentile | 161.2 | 156.8 | −2.7% | −15.9535 to +7.1761 | no |
| time over the response line (% of samples) | 0.02388 | 0.02395 | +0.3% | −0.0402 to +0.0403 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.1 | 17.4 | +1.8% | −1.7800 to +2.3800 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.215 | 0.1067 | −50.4% | −0.3961 to +0.1794 | no |
| utilisation (used / allocatable) | 0.03625 | 0.03635 | +0.3% | −0.0005 to +0.0007 | no |
| CPU used (cores), mean | 0.87 | 0.8723 | +0.3% | −0.0132 to +0.0178 | no |
| Omni's own CPU (cores), mean | 0.00872 | 0.00758 | −13.1% | −0.0014 to −0.0008 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8787 | 0.8799 | +0.1% | −0.0144 to +0.0167 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 765.1 | 756.3 | −1.2% | −29.5231 to +11.7840 | no |
| HPA replicas, mean | 7.971 | 7.654 | −4.0% | −1.0118 to +0.3795 | no |
| pods started | 3.6 | 4 | +11.1% | −0.3689 to +1.1689 | no |
| pod start wait, total (s) | 5.6 | 5.9 | +5.4% | −0.5953 to +1.1953 | no |
| pod start wait, mean (s) | 1.537 | 1.507 | −1.9% | −0.4047 to +0.3452 | no |
| host CPU busy, the real machine under kind (%) | 26.98 | 26.93 | −0.2% | −0.4637 to +0.3711 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.514 | −0.1% | −0.0028 to +0.0004 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.5 | −0.1% | −0.3603 to +0.0460 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.5 | −0.1% | −0.3603 to +0.0460 | no |
| response time (ms), mean | 77.82 | 78.16 | +0.4% | −0.4508 to +1.1297 | no |
| response time (ms), 95th percentile | 116.9 | 117.4 | +0.5% | −1.4262 to +2.5842 | no |
| response time (ms), 99th percentile | 161.2 | 162.6 | +0.9% | −8.3771 to +11.1915 | no |
| time over the response line (% of samples) | 0.02388 | 0.06003 | +151.4% | −0.0219 to +0.0941 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.1 | 18.4 | +7.6% | −1.9875 to +4.5875 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.215 | 0.185 | −14.0% | −0.3197 to +0.2597 | no |
| utilisation (used / allocatable) | 0.03625 | 0.03606 | −0.5% | −0.0006 to +0.0002 | no |
| CPU used (cores), mean | 0.87 | 0.8654 | −0.5% | −0.0150 to +0.0058 | no |
| Omni's own CPU (cores), mean | 0.00872 | 0.01415 | +62.3% | +0.0045 to +0.0064 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8787 | 0.8795 | +0.1% | −0.0098 to +0.0114 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 765.1 | 769.2 | +0.5% | −14.1499 to +22.3044 | no |
| HPA replicas, mean | 7.971 | 7.508 | −5.8% | −1.0372 to +0.1112 | no |
| pods started | 3.6 | 4.2 | +16.7% | −1.1260 to +2.3260 | no |
| pod start wait, total (s) | 5.6 | 6 | +7.1% | −3.0913 to +3.8913 | no |
| pod start wait, mean (s) | 1.537 | 1.333 | −13.2% | −0.6598 to +0.2532 | no |
| host CPU busy, the real machine under kind (%) | 26.98 | 27.08 | +0.4% | −0.2323 to +0.4288 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.514 | −0.1% | −0.0025 to +0.0009 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.6 | −0.0% | −0.2234 to +0.2027 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.6 | −0.0% | −0.2234 to +0.2027 | no |
| response time (ms), mean | 77.82 | 78.48 | +0.8% | −0.1275 to +1.4452 | no |
| response time (ms), 95th percentile | 116.9 | 118.8 | +1.7% | +0.6821 to +3.2589 | yes: LOSS |
| response time (ms), 99th percentile | 161.2 | 164.3 | +2.0% | −7.3117 to +13.6075 | no |
| time over the response line (% of samples) | 0.02388 | 0 | −100.0% | −0.0599 to +0.0121 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.1 | 20.6 | +20.5% | +1.2569 to +5.7431 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.215 | 0.3667 | +70.5% | −0.1561 to +0.4594 | no |
| utilisation (used / allocatable) | 0.03625 | 0.03653 | +0.8% | −0.0001 to +0.0007 | no |
| CPU used (cores), mean | 0.87 | 0.8768 | +0.8% | −0.0033 to +0.0169 | no |
| Omni's own CPU (cores), mean | 0.00872 | 0.02507 | +187.5% | +0.0143 to +0.0184 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8787 | 0.9019 | +2.6% | +0.0126 to +0.0337 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 765.1 | 758.6 | −0.9% | −17.3391 to +4.2840 | no |
| HPA replicas, mean | 7.971 | 8.433 | +5.8% | −0.0508 to +0.9765 | no |
| pods started | 3.6 | 4.7 | +30.6% | +0.0634 to +2.1366 | yes: power given |
| pod start wait, total (s) | 5.6 | 6.4 | +14.3% | −2.0771 to +3.6771 | no |
| pod start wait, mean (s) | 1.537 | 1.35 | −12.1% | −0.6976 to +0.3243 | no |
| host CPU busy, the real machine under kind (%) | 26.98 | 27.55 | +2.1% | +0.1405 to +1.0066 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs omni at its default, every 60 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.515 | 0.0% | raw −0.0019 to +0.0019 | STEADY, the same (to nine decimal places) |
| energy, parked workers still on at idle power (Wh, declared model) | 158.6 | 158.8 | +0.1% | −0.0896 to +0.4101 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.6 | 158.8 | +0.1% | −0.0896 to +0.4101 | no |
| response time (ms), mean | 77.82 | 79.56 | +2.2% | +0.7286 to +2.7603 | yes: LOSS |
| response time (ms), 95th percentile | 116.9 | 122.4 | +4.7% | +3.5103 to +7.5827 | yes: LOSS |
| response time (ms), 99th percentile | 161.2 | 165.2 | +2.5% | −8.6000 to +16.6344 | no |
| time over the response line (% of samples) | 0.02388 | 0 | −100.0% | −0.0599 to +0.0121 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 17.1 | 19.8 | +15.8% | +0.8826 to +4.5174 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.215 | 0.105 | −51.2% | −0.3331 to +0.1131 | no |
| utilisation (used / allocatable) | 0.03625 | 0.03694 | +1.9% | +0.0002 to +0.0012 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.87 | 0.8866 | +1.9% | +0.0056 to +0.0276 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.00872 | 0.06918 | +693.3% | +0.0526 to +0.0683 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8787 | 0.9558 | +8.8% | +0.0639 to +0.0903 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 765.1 | 748.6 | −2.2% | −30.0268 to −2.9773 | yes, down (shown, not judged) |
| HPA replicas, mean | 7.971 | 8.453 | +6.1% | −0.0140 to +0.9791 | no |
| pods started | 3.6 | 3.9 | +8.3% | −0.8705 to +1.4705 | no |
| pod start wait, total (s) | 5.6 | 5.8 | +3.6% | −2.5353 to +2.9353 | no |
| pod start wait, mean (s) | 1.537 | 1.497 | −2.6% | −0.4009 to +0.3209 | no |
| host CPU busy, the real machine under kind (%) | 26.98 | 29.45 | +9.2% | +2.0124 to +2.9316 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*