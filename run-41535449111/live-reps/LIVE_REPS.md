# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.512 | 1.516 | 1.509 | 1.509 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 160 | 158.5 | 159.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 160 | 158.5 | 159.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 130.4 | 135.9 | 129.8 | 135.3 |
| response time (ms), 95th percentile | 273.5 | 282.6 | 262.3 | 273.3 |
| response time (ms), 99th percentile | 375.2 | 386.2 | 371.1 | 378 |
| time over the response line (% of samples) | 0.333 | 0.4008 | 0.2429 | 0.2843 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.4 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 6 | 6.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 90 | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.48 | 0.2417 | 0.5933 | 0.365 |
| utilisation (used / allocatable) | 0.0372 | 0.04172 | 0.03806 | 0.04252 |
| CPU used (cores), mean | 0.8929 | 1.001 | 0.9135 | 1.02 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.03011 | 0.0478 |
| CPU used with Omni's own (cores), mean | 0.8929 | 1.001 | 0.9436 | 1.068 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 706.2 | 634.2 | 691.9 | 624 |
| HPA replicas, mean | 8.863 | 8.884 | 9.957 | 10.05 |
| pods started | 4.7 | 4.8 | 7 | 6.5 |
| pod start wait, total (s) | 7.2 | 7.9 | 10.1 | 10.1 |
| pod start wait, mean (s) | 1.545 | 1.64 | 1.471 | 1.494 |
| host CPU busy, the real machine under kind (%) | 26.85 | 30.94 | 28.47 | 32.86 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.516 | 1.509 | −0.5% | −0.0145 to +0.0002 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160 | 159.5 | −0.4% | −1.2903 to +0.1625 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160 | 159.5 | −0.4% | −1.2903 to +0.1625 | no |
| response time (ms), mean | 135.9 | 135.3 | −0.4% | −4.3533 to +3.1475 | no |
| response time (ms), 95th percentile | 282.6 | 273.3 | −3.3% | −26.2631 to +7.6841 | no |
| response time (ms), 99th percentile | 386.2 | 378 | −2.1% | −38.1799 to +21.7433 | no |
| time over the response line (% of samples) | 0.4008 | 0.2843 | −29.1% | −0.3706 to +0.1377 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.4 | 0 | −100.0% | −0.9001 to +0.1001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 6.4 | +6.400 (native is 0) | +4.5469 to +8.2531 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2417 | 0.365 | +51.0% | −0.1862 to +0.4329 | no |
| utilisation (used / allocatable) | 0.04172 | 0.04252 | +1.9% | +0.0002 to +0.0014 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.001 | 1.02 | +1.9% | +0.0043 to +0.0341 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0478 | +0.048 (native is 0) | +0.0410 to +0.0546 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.001 | 1.068 | +6.7% | +0.0462 to +0.0878 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 634.2 | 624 | −1.6% | −18.9421 to −1.4972 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.884 | 10.05 | +13.1% | +0.5029 to +1.8231 | yes: power given |
| pods started | 4.8 | 6.5 | +35.4% | +0.0811 to +3.3189 | yes: power given |
| pod start wait, total (s) | 7.9 | 10.1 | +27.8% | −1.1686 to +5.5686 | no |
| pod start wait, mean (s) | 1.64 | 1.494 | −8.9% | −0.4093 to +0.1165 | no |
| host CPU busy, the real machine under kind (%) | 30.94 | 32.86 | +6.2% | +1.1742 to +2.6750 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.517 | +0.3% | −0.0059 to +0.0152 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 160 | +1.0% | +0.3716 to +2.6586 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 160 | +1.0% | +0.3716 to +2.6586 | yes: power given |
| response time (ms), mean | 130.4 | 135.9 | +4.2% | +0.6932 to +10.2894 | yes: LOSS |
| response time (ms), 95th percentile | 273.5 | 282.6 | +3.3% | −9.3132 to +27.4732 | no |
| response time (ms), 99th percentile | 375.2 | 386.2 | +2.9% | −19.4147 to +41.5393 | no |
| time over the response line (% of samples) | 0.333 | 0.4008 | +20.3% | −0.1256 to +0.2612 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.4 | +300.0% | −0.1828 to +0.7828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.48 | 0.2417 | −49.7% | −0.5707 to +0.0940 | no |
| utilisation (used / allocatable) | 0.0372 | 0.04172 | +12.1% | +0.0035 to +0.0055 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8929 | 1.001 | +12.1% | +0.0841 to +0.1325 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 0.8929 | 1.001 | +12.1% | +0.0841 to +0.1325 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 706.2 | 634.2 | −10.2% | −87.9186 to −56.1056 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.863 | 8.884 | +0.2% | −0.0678 to +0.1084 | no |
| pods started | 4.7 | 4.8 | +2.1% | −0.3060 to +0.5060 | no |
| pod start wait, total (s) | 7.2 | 7.9 | +9.7% | −1.2676 to +2.6676 | no |
| pod start wait, mean (s) | 1.545 | 1.64 | +6.1% | −0.2420 to +0.4320 | no |
| host CPU busy, the real machine under kind (%) | 26.85 | 30.94 | +15.2% | +3.3652 to +4.8059 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.509 | −0.2% | −0.0101 to +0.0051 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.5 | −0.0% | −0.8559 to +0.7866 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.5 | −0.0% | −0.8559 to +0.7866 | no |
| response time (ms), mean | 130.4 | 129.8 | −0.5% | −5.2526 to +4.0535 | no |
| response time (ms), 95th percentile | 273.5 | 262.3 | −4.1% | −28.0340 to +5.6330 | no |
| response time (ms), 99th percentile | 375.2 | 371.1 | −1.1% | −36.8824 to +28.7720 | no |
| time over the response line (% of samples) | 0.333 | 0.2429 | −27.1% | −0.3477 to +0.1674 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 6 | +6.000 (native is 0) | +4.4184 to +7.5816 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.48 | 0.5933 | +23.6% | −0.3389 to +0.5656 | no |
| utilisation (used / allocatable) | 0.0372 | 0.03806 | +2.3% | +0.0001 to +0.0016 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8929 | 0.9135 | +2.3% | +0.0036 to +0.0375 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03011 | +0.030 (native is 0) | +0.0264 to +0.0338 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8929 | 0.9436 | +5.7% | +0.0316 to +0.0697 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 706.2 | 691.9 | −2.0% | −26.2733 to −2.1960 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.863 | 9.957 | +12.3% | +0.2856 to +1.9027 | yes: power given |
| pods started | 4.7 | 7 | +48.9% | +0.4515 to +4.1485 | yes: power given |
| pod start wait, total (s) | 7.2 | 10.1 | +40.3% | +0.5772 to +5.2228 | yes: LOSS |
| pod start wait, mean (s) | 1.545 | 1.471 | −4.8% | −0.4032 to +0.2543 | no |
| host CPU busy, the real machine under kind (%) | 26.85 | 28.47 | +6.0% | +1.1802 to +2.0653 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.516 | 1.509 | −0.5% | −0.0158 to +0.0015 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160 | 158.5 | −1.0% | −2.4669 to −0.6325 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160 | 158.5 | −1.0% | −2.4669 to −0.6325 | yes: GAIN |
| response time (ms), mean | 135.9 | 129.8 | −4.5% | −12.0669 to −0.1146 | yes: GAIN |
| response time (ms), 95th percentile | 282.6 | 262.3 | −7.2% | −44.1476 to +3.5866 | no |
| response time (ms), 99th percentile | 386.2 | 371.1 | −3.9% | −49.9459 to +19.7109 | no |
| time over the response line (% of samples) | 0.4008 | 0.2429 | −39.4% | −0.5040 to +0.1882 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.4 | 0 | −100.0% | −0.9001 to +0.1001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 6 | +6.000 (native is 0) | +4.4184 to +7.5816 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2417 | 0.5933 | +145.5% | +0.0583 to +0.6451 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.04172 | 0.03806 | −8.8% | −0.0045 to −0.0028 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.001 | 0.9135 | −8.8% | −0.1075 to −0.0680 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03011 | +0.030 (native is 0) | +0.0264 to +0.0338 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.001 | 0.9436 | −5.8% | −0.0780 to −0.0373 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 634.2 | 691.9 | +9.1% | +42.6770 to +72.8779 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.884 | 9.957 | +12.1% | +0.2957 to +1.8521 | yes: power given |
| pods started | 4.8 | 7 | +45.8% | +0.4544 to +3.9456 | yes: power given |
| pod start wait, total (s) | 7.9 | 10.1 | +27.8% | −0.2733 to +4.6733 | no |
| pod start wait, mean (s) | 1.64 | 1.471 | −10.3% | −0.5002 to +0.1613 | no |
| host CPU busy, the real machine under kind (%) | 30.94 | 28.47 | −8.0% | −3.0026 to −1.9229 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.509 | −0.2% | −0.0081 to +0.0031 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 159.5 | +0.6% | +0.2731 to +1.6294 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 159.5 | +0.6% | +0.2731 to +1.6294 | yes: power given |
| response time (ms), mean | 130.4 | 135.3 | +3.7% | +1.1021 to +8.6746 | yes: LOSS |
| response time (ms), 95th percentile | 273.5 | 273.3 | −0.1% | −14.4699 to +14.0509 | no |
| response time (ms), 99th percentile | 375.2 | 378 | +0.8% | −11.9692 to +17.6572 | no |
| time over the response line (% of samples) | 0.333 | 0.2843 | −14.6% | −0.1802 to +0.0827 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 6.4 | +6.400 (native is 0) | +4.5469 to +8.2531 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.48 | 0.365 | −24.0% | −0.4417 to +0.2117 | no |
| utilisation (used / allocatable) | 0.0372 | 0.04252 | +14.3% | +0.0042 to +0.0065 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8929 | 1.02 | +14.3% | +0.1002 to +0.1548 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0478 | +0.048 (native is 0) | +0.0410 to +0.0546 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8929 | 1.068 | +19.6% | +0.1426 to +0.2080 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 706.2 | 624 | −11.6% | −96.1949 to −68.2686 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.863 | 10.05 | +13.4% | +0.5069 to +1.8596 | yes: power given |
| pods started | 4.7 | 6.5 | +38.3% | +0.0872 to +3.5128 | yes: power given |
| pod start wait, total (s) | 7.2 | 10.1 | +40.3% | −0.3597 to +6.1597 | no |
| pod start wait, mean (s) | 1.545 | 1.494 | −3.3% | −0.3014 to +0.1987 | no |
| host CPU busy, the real machine under kind (%) | 26.85 | 32.86 | +22.4% | +4.9452 to +7.0751 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*