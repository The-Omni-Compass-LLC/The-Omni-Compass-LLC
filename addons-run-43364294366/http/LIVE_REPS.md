# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 60 s |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.514 | 1.516 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.3 | 160.5 | 161 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.3 | 160.5 | 161 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 190.4 | 99.94 | 78.41 |
| response time (ms), 95th percentile | 448.7 | 255.4 | 116 |
| response time (ms), 99th percentile | 604.5 | 492.4 | 184 |
| time over the response line (% of samples) | 3.807 | 1.073 | 0.08529 |
| failed requests (%) | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.7 | 1.3 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 82.5 | 4.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.1567 | 0.08167 |
| utilisation (used / allocatable) | 0.02996 | 0.04317 | 0.04571 |
| CPU used (cores), mean | 0.7191 | 1.036 | 1.097 |
| Omni's own CPU (cores), mean | 0 | 0.05745 | 0.00998 |
| CPU used with Omni's own (cores), mean | 0.7191 | 1.094 | 1.107 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 869.7 | 617.3 | 587.7 |
| HPA replicas, mean | 2.915 | 2.528 | 2.365 |
| pods started | 2.9 | 2.4 | 2 |
| pod start wait, total (s) | 3.6 | 3.2 | 3 |
| pod start wait, mean (s) | 1.25 | 1.283 | 1.533 |
| host CPU busy, the real machine under kind (%) | 23.72 | 34.66 | 34.58 |
| host cores (the real machine under kind) | 4 | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan |

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
| node-hours | 1.514 | 1.516 | +0.2% | −0.0064 to +0.0111 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.3 | 160.5 | +2.1% | +2.5346 to +4.0139 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.3 | 160.5 | +2.1% | +2.5346 to +4.0139 | yes: power given |
| response time (ms), mean | 190.4 | 99.94 | −47.5% | −107.2069 to −73.6662 | yes: GAIN |
| response time (ms), 95th percentile | 448.7 | 255.4 | −43.1% | −244.1282 to −142.6338 | yes: GAIN |
| response time (ms), 99th percentile | 604.5 | 492.4 | −18.5% | −174.6211 to −49.5841 | yes: GAIN |
| time over the response line (% of samples) | 3.807 | 1.073 | −71.8% | −4.6066 to −0.8620 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.7 | 1.3 | −64.9% | −4.5644 to −0.2356 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 82.5 | +82.500 (native is 0) | +66.8638 to +98.1362 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.1567 | +17.5% | −0.2183 to +0.2649 | no |
| utilisation (used / allocatable) | 0.02996 | 0.04317 | +44.1% | +0.0116 to +0.0148 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7191 | 1.036 | +44.1% | +0.2787 to +0.3553 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05745 | +0.057 (native is 0) | +0.0495 to +0.0654 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7191 | 1.094 | +52.1% | +0.3322 to +0.4167 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 869.7 | 617.3 | −29.0% | −270.2902 to −234.3654 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.915 | 2.528 | −13.3% | −0.7241 to −0.0499 | yes: GAIN |
| pods started | 2.9 | 2.4 | −17.2% | −1.1079 to +0.1079 | no |
| pod start wait, total (s) | 3.6 | 3.2 | −11.1% | −1.8775 to +1.0775 | no |
| pod start wait, mean (s) | 1.25 | 1.283 | +2.7% | −0.3672 to +0.4339 | no |
| host CPU busy, the real machine under kind (%) | 23.72 | 34.66 | +46.1% | +9.3944 to +12.4918 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 60 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.514 | 1.514 | +0.0% | −0.0077 to +0.0091 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.3 | 161 | +2.3% | +2.8334 to +4.5558 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.3 | 161 | +2.3% | +2.8334 to +4.5558 | yes: power given |
| response time (ms), mean | 190.4 | 78.41 | −58.8% | −131.1402 to −92.7960 | yes: GAIN |
| response time (ms), 95th percentile | 448.7 | 116 | −74.1% | −384.2248 to −281.2462 | yes: GAIN |
| response time (ms), 99th percentile | 604.5 | 184 | −69.6% | −471.2797 to −369.6631 | yes: GAIN |
| time over the response line (% of samples) | 3.807 | 0.08529 | −97.8% | −6.0166 to −1.4277 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.7 | 0 | −100.0% | −6.1790 to −1.2210 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4.6 | +4.600 (native is 0) | +3.1615 to +6.0385 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.08167 | −38.7% | −0.2490 to +0.1456 | no |
| utilisation (used / allocatable) | 0.02996 | 0.04571 | +52.5% | +0.0134 to +0.0181 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7191 | 1.097 | +52.5% | +0.3220 to +0.4337 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00998 | +0.010 (native is 0) | +0.0086 to +0.0114 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7191 | 1.107 | +53.9% | +0.3309 to +0.4448 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 869.7 | 587.7 | −32.4% | −300.3220 to −263.6451 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.915 | 2.365 | −18.9% | −0.8756 to −0.2235 | yes: GAIN |
| pods started | 2.9 | 2 | −31.0% | −1.4278 to −0.3722 | yes: GAIN |
| pod start wait, total (s) | 3.6 | 3 | −16.7% | −1.8251 to +0.6251 | no |
| pod start wait, mean (s) | 1.25 | 1.533 | +22.7% | −0.2559 to +0.8225 | no |
| host CPU busy, the real machine under kind (%) | 23.72 | 34.58 | +45.8% | +9.1673 to +12.5510 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 60 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.516 | 1.514 | −0.1% | −0.0036 to +0.0003 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.5 | 161 | +0.3% | +0.0853 to +0.7555 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.5 | 161 | +0.3% | +0.0853 to +0.7555 | yes: power given |
| response time (ms), mean | 99.94 | 78.41 | −21.5% | −27.8837 to −15.1794 | yes: GAIN |
| response time (ms), 95th percentile | 255.4 | 116 | −54.6% | −187.7903 to −90.9187 | yes: GAIN |
| response time (ms), 99th percentile | 492.4 | 184 | −62.6% | −357.1113 to −259.6263 | yes: GAIN |
| time over the response line (% of samples) | 1.073 | 0.08529 | −92.1% | −1.4890 to −0.4867 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.3 | 0 | −100.0% | −2.1294 to −0.4706 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 82.5 | 4.6 | −94.4% | −92.4678 to −63.3322 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1567 | 0.08167 | −47.9% | −0.1939 to +0.0439 | no |
| utilisation (used / allocatable) | 0.04317 | 0.04571 | +5.9% | +0.0011 to +0.0040 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.036 | 1.097 | +5.9% | +0.0265 to +0.0952 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.05745 | 0.00998 | −82.6% | −0.0540 to −0.0409 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.094 | 1.107 | +1.2% | −0.0160 to +0.0428 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 617.3 | 587.7 | −4.8% | −45.4024 to −13.9092 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.528 | 2.365 | −6.4% | −0.5185 to +0.1933 | no |
| pods started | 2.4 | 2 | −16.7% | −1.0911 to +0.2911 | no |
| pod start wait, total (s) | 3.2 | 3 | −6.3% | −1.7744 to +1.3744 | no |
| pod start wait, mean (s) | 1.283 | 1.533 | +19.5% | −0.1404 to +0.6404 | no |
| host CPU busy, the real machine under kind (%) | 34.66 | 34.58 | −0.2% | −0.6872 to +0.5193 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*