# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 60 s |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.516 | 1.517 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 171.7 | 171.4 | 171.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.7 | 171.4 | 171.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 486.6 | 451.4 | 451.8 |
| response time (ms), 95th percentile | 2034 | 2007 | 2128 |
| response time (ms), 99th percentile | 4826 | 4753 | 4867 |
| time over the response line (% of samples) | 21.32 | 21.42 | 20.69 |
| failed requests (%) | 2.524 | 2.361 | 2.463 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 7.5 | 7.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 127.5 | 43.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.593 | 2.362 | 2.257 |
| utilisation (used / allocatable) | 0.09291 | 0.09152 | 0.09199 |
| CPU used (cores), mean | 2.23 | 2.196 | 2.208 |
| Omni's own CPU (cores), mean | 0 | 0.05331 | 0.01249 |
| CPU used with Omni's own (cores), mean | 2.23 | 2.25 | 2.22 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 318.5 | 322.3 | 322 |
| HPA replicas, mean | 14.83 | 15.51 | 15.04 |
| pods started | 5.8 | 5.7 | 4.5 |
| pod start wait, total (s) | 8.2 | 11 | 7.6 |
| pod start wait, mean (s) | 1.417 | 1.954 | 1.573 |
| host CPU busy, the real machine under kind (%) | 64.67 | 65.94 | 64.72 |
| host cores (the real machine under kind) | 4 | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan |
| second app: response time (ms), 95th percentile | 277.4 | 290.5 | 291 |
| second app: response time (ms), 99th percentile | 1615 | 1653 | 2121 |
| second app: time over the response line (% of samples) | 13.21 | 13 | 13.21 |
| second app: failed requests (%) | 11.28 | 11.33 | 11.31 |

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
| node-hours | 1.516 | 1.517 | +0.0% | −0.0070 to +0.0083 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 171.7 | 171.4 | −0.1% | −1.1450 to +0.6566 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.7 | 171.4 | −0.1% | −1.1450 to +0.6566 | no |
| response time (ms), mean | 486.6 | 451.4 | −7.2% | −76.4545 to +5.9851 | no |
| response time (ms), 95th percentile | 2034 | 2007 | −1.4% | −281.6645 to +226.0265 | no |
| response time (ms), 99th percentile | 4826 | 4753 | −1.5% | −577.6100 to +433.0598 | no |
| time over the response line (% of samples) | 21.32 | 21.42 | +0.5% | −1.8818 to +2.0752 | no |
| failed requests (%) | 2.524 | 2.361 | −6.4% | −0.9685 to +0.6441 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 7.5 | −6.2% | −1.2726 to +0.2726 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 127.5 | +127.500 (native is 0) | +98.6064 to +156.3936 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.593 | 2.362 | +48.2% | −0.0891 to +1.6258 | no |
| utilisation (used / allocatable) | 0.09291 | 0.09152 | −1.5% | −0.0030 to +0.0002 | no |
| CPU used (cores), mean | 2.23 | 2.196 | −1.5% | −0.0714 to +0.0042 | no |
| Omni's own CPU (cores), mean | 0 | 0.05331 | +0.053 (native is 0) | +0.0432 to +0.0634 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.23 | 2.25 | +0.9% | −0.0183 to +0.0578 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 318.5 | 322.3 | +1.2% | −2.1120 to +9.6291 | no |
| HPA replicas, mean | 14.83 | 15.51 | +4.6% | +0.0559 to +1.2942 | yes: power given |
| pods started | 5.8 | 5.7 | −1.7% | −0.8113 to +0.6113 | no |
| pod start wait, total (s) | 8.2 | 11 | +34.1% | −0.3954 to +5.9954 | no |
| pod start wait, mean (s) | 1.417 | 1.954 | +37.9% | +0.0997 to +0.9741 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 64.67 | 65.94 | +2.0% | +0.4182 to +2.1142 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 277.4 | 290.5 | +4.8% | −1.7986 to +28.1606 | no |
| second app: response time (ms), 99th percentile | 1615 | 1653 | +2.4% | −1360.8320 to +1438.1598 | no |
| second app: time over the response line (% of samples) | 13.21 | 13 | −1.6% | −0.7392 to +0.3239 | no |
| second app: failed requests (%) | 11.28 | 11.33 | +0.5% | −0.5896 to +0.7007 | no |

## omni deciding every 60 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.516 | 1.514 | −0.1% | −0.0072 to +0.0035 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 171.7 | 171.3 | −0.2% | −1.1522 to +0.3686 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.7 | 171.3 | −0.2% | −1.1522 to +0.3686 | no |
| response time (ms), mean | 486.6 | 451.8 | −7.2% | −70.7020 to +1.1022 | no |
| response time (ms), 95th percentile | 2034 | 2128 | +4.6% | −146.6721 to +333.6371 | no |
| response time (ms), 99th percentile | 4826 | 4867 | +0.9% | −450.2827 to +532.5005 | no |
| time over the response line (% of samples) | 21.32 | 20.69 | −3.0% | −1.5622 to +0.2998 | no |
| failed requests (%) | 2.524 | 2.463 | −2.4% | −0.4843 to +0.3626 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 7.3 | −8.8% | −1.3786 to −0.0214 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.6 | +43.600 (native is 0) | +31.8647 to +55.3353 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.593 | 2.257 | +41.6% | −0.5274 to +1.8541 | no |
| utilisation (used / allocatable) | 0.09291 | 0.09199 | −1.0% | −0.0024 to +0.0005 | no |
| CPU used (cores), mean | 2.23 | 2.208 | −1.0% | −0.0564 to +0.0119 | no |
| Omni's own CPU (cores), mean | 0 | 0.01249 | +0.012 (native is 0) | +0.0111 to +0.0139 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.23 | 2.22 | −0.4% | −0.0442 to +0.0246 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 318.5 | 322 | +1.1% | −1.0736 to +7.9494 | no |
| HPA replicas, mean | 14.83 | 15.04 | +1.4% | −0.0989 to +0.5020 | no |
| pods started | 5.8 | 4.5 | −22.4% | −2.3690 to −0.2310 | yes: GAIN |
| pod start wait, total (s) | 8.2 | 7.6 | −7.3% | −3.6942 to +2.4942 | no |
| pod start wait, mean (s) | 1.417 | 1.573 | +11.1% | −0.2070 to +0.5203 | no |
| host CPU busy, the real machine under kind (%) | 64.67 | 64.72 | +0.1% | −0.5185 to +0.6089 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 277.4 | 291 | +4.9% | −4.6858 to +31.9498 | no |
| second app: response time (ms), 99th percentile | 1615 | 2121 | +31.4% | −1300.1343 to +2313.8597 | no |
| second app: time over the response line (% of samples) | 13.21 | 13.21 | −0.1% | −0.6017 to +0.5881 | no |
| second app: failed requests (%) | 11.28 | 11.31 | +0.3% | −0.6681 to +0.7316 | no |

## omni deciding every 60 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.517 | 1.514 | −0.2% | −0.0106 to +0.0056 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 171.4 | 171.3 | −0.1% | −0.9818 to +0.6867 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.4 | 171.3 | −0.1% | −0.9818 to +0.6867 | no |
| response time (ms), mean | 451.4 | 451.8 | +0.1% | −35.6596 to +36.5292 | no |
| response time (ms), 95th percentile | 2007 | 2128 | +6.0% | −103.5669 to +346.1699 | no |
| response time (ms), 99th percentile | 4753 | 4867 | +2.4% | −303.0384 to +529.8064 | no |
| time over the response line (% of samples) | 21.42 | 20.69 | −3.4% | −2.4011 to +0.9452 | no |
| failed requests (%) | 2.361 | 2.463 | +4.3% | −0.4827 to +0.6854 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 7.3 | −2.7% | −0.6524 to +0.2524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 127.5 | 43.6 | −65.8% | −113.9702 to −53.8298 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.362 | 2.257 | −4.4% | −0.8186 to +0.6086 | no |
| utilisation (used / allocatable) | 0.09152 | 0.09199 | +0.5% | −0.0008 to +0.0018 | no |
| CPU used (cores), mean | 2.196 | 2.208 | +0.5% | −0.0202 to +0.0428 | no |
| Omni's own CPU (cores), mean | 0.05331 | 0.01249 | −76.6% | −0.0498 to −0.0319 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.25 | 2.22 | −1.3% | −0.0611 to +0.0021 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 322.3 | 322 | −0.1% | −5.7375 to +5.0962 | no |
| HPA replicas, mean | 15.51 | 15.04 | −3.1% | −0.9994 to +0.0525 | no |
| pods started | 5.7 | 4.5 | −21.1% | −2.3583 to −0.0417 | yes: GAIN |
| pod start wait, total (s) | 11 | 7.6 | −30.9% | −7.2328 to +0.4328 | no |
| pod start wait, mean (s) | 1.954 | 1.573 | −19.5% | −0.8656 to +0.1052 | no |
| host CPU busy, the real machine under kind (%) | 65.94 | 64.72 | −1.9% | −2.1039 to −0.3381 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 290.5 | 291 | +0.2% | −12.1038 to +13.0058 | no |
| second app: response time (ms), 99th percentile | 1653 | 2121 | +28.3% | −572.0103 to +1508.4079 | no |
| second app: time over the response line (% of samples) | 13 | 13.21 | +1.5% | −0.1022 to +0.5039 | no |
| second app: failed requests (%) | 11.33 | 11.31 | −0.2% | −0.3947 to +0.3471 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*