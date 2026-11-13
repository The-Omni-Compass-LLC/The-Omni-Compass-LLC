# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 60 s |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.51 | 1.512 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 160 | 160 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 160 | 160 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 106 | 74.89 | 67.09 |
| response time (ms), 95th percentile | 220.7 | 124.1 | 96.91 |
| response time (ms), 99th percentile | 326.4 | 216.5 | 122.9 |
| time over the response line (% of samples) | 0.1653 | 0.02469 | 0 |
| failed requests (%) | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 289.2 | 21.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.3467 | 0.3983 |
| utilisation (used / allocatable) | 0.03509 | 0.04338 | 0.04389 |
| CPU used (cores), mean | 0.842 | 1.041 | 1.053 |
| Omni's own CPU (cores), mean | 0 | 0.08084 | 0.01235 |
| CPU used with Omni's own (cores), mean | 0.842 | 1.122 | 1.066 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 745.8 | 616.8 | 610.8 |
| HPA replicas, mean | 8.791 | 9.706 | 9.139 |
| pods started | 5 | 6.3 | 5.8 |
| pod start wait, total (s) | 7.4 | 10.3 | 9.3 |
| pod start wait, mean (s) | 1.48 | 1.637 | 1.634 |
| host CPU busy, the real machine under kind (%) | 26.81 | 35.1 | 33.17 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw +0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.512 | +0.2% | −0.0051 to +0.0101 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 160 | +1.4% | +1.5556 to +2.7547 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 160 | +1.4% | +1.5556 to +2.7547 | yes: power given |
| response time (ms), mean | 106 | 74.89 | −29.3% | −41.6099 to −20.5933 | yes: GAIN |
| response time (ms), 95th percentile | 220.7 | 124.1 | −43.8% | −113.2944 to −79.8136 | yes: GAIN |
| response time (ms), 99th percentile | 326.4 | 216.5 | −33.7% | −139.2596 to −80.5690 | yes: GAIN |
| time over the response line (% of samples) | 0.1653 | 0.02469 | −85.1% | −0.2894 to +0.0081 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 289.2 | +289.200 (native is 0) | +199.9697 to +378.4303 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.3467 | +550.0% | −0.0239 to +0.6106 | no |
| utilisation (used / allocatable) | 0.03509 | 0.04338 | +23.6% | +0.0055 to +0.0110 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.842 | 1.041 | +23.6% | +0.1330 to +0.2650 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.08084 | +0.081 (native is 0) | +0.0627 to +0.0990 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.842 | 1.122 | +33.2% | +0.1973 to +0.3624 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 745.8 | 616.8 | −17.3% | −160.7913 to −97.1225 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.791 | 9.706 | +10.4% | +0.3971 to +1.4317 | yes: power given |
| pods started | 5 | 6.3 | +26.0% | +0.6214 to +1.9786 | yes: power given |
| pod start wait, total (s) | 7.4 | 10.3 | +39.2% | +0.9498 to +4.8502 | yes: LOSS |
| pod start wait, mean (s) | 1.48 | 1.637 | +10.6% | −0.1164 to +0.4307 | no |
| host CPU busy, the real machine under kind (%) | 26.81 | 35.1 | +30.9% | +5.9218 to +10.6622 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 60 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw +0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.51 | 1.512 | +0.1% | −0.0083 to +0.0123 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.8 | 160 | +1.4% | +1.1734 to +3.2652 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.8 | 160 | +1.4% | +1.1734 to +3.2652 | yes: power given |
| response time (ms), mean | 106 | 67.09 | −36.7% | −52.1569 to −25.6440 | yes: GAIN |
| response time (ms), 95th percentile | 220.7 | 96.91 | −56.1% | −149.1147 to −98.3933 | yes: GAIN |
| response time (ms), 99th percentile | 326.4 | 122.9 | −62.3% | −242.3219 to −164.5111 | yes: GAIN |
| time over the response line (% of samples) | 0.1653 | 0 | −100.0% | −0.3646 to +0.0340 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 21.1 | +21.100 (native is 0) | +17.4612 to +24.7388 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05333 | 0.3983 | +646.9% | −0.0452 to +0.7352 | no |
| utilisation (used / allocatable) | 0.03509 | 0.04389 | +25.1% | +0.0059 to +0.0117 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.842 | 1.053 | +25.1% | +0.1408 to +0.2816 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01235 | +0.012 (native is 0) | +0.0102 to +0.0145 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.842 | 1.066 | +26.6% | +0.1514 to +0.2957 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 745.8 | 610.8 | −18.1% | −167.6494 to −102.3840 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.791 | 9.139 | +4.0% | −0.6103 to +1.3060 | no |
| pods started | 5 | 5.8 | +16.0% | −0.2556 to +1.8556 | no |
| pod start wait, total (s) | 7.4 | 9.3 | +25.7% | −0.8487 to +4.6487 | no |
| pod start wait, mean (s) | 1.48 | 1.634 | +10.4% | −0.2316 to +0.5400 | no |
| host CPU busy, the real machine under kind (%) | 26.81 | 33.17 | +23.7% | +4.3026 to +8.4236 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 60 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 60 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.512 | −0.0% | −0.0070 to +0.0060 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160 | 160 | +0.0% | −0.7545 to +0.8828 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160 | 160 | +0.0% | −0.7545 to +0.8828 | no |
| response time (ms), mean | 74.89 | 67.09 | −10.4% | −11.5331 to −4.0645 | yes: GAIN |
| response time (ms), 95th percentile | 124.1 | 96.91 | −21.9% | −39.9128 to −14.4872 | yes: GAIN |
| response time (ms), 99th percentile | 216.5 | 122.9 | −43.2% | −119.4356 to −67.5688 | yes: GAIN |
| time over the response line (% of samples) | 0.02469 | 0 | −100.0% | −0.0805 to +0.0312 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 289.2 | 21.1 | −92.7% | −355.8809 to −180.3191 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3467 | 0.3983 | +14.9% | −0.4363 to +0.5396 | no |
| utilisation (used / allocatable) | 0.04338 | 0.04389 | +1.2% | −0.0004 to +0.0014 | no |
| CPU used (cores), mean | 1.041 | 1.053 | +1.2% | −0.0089 to +0.0334 | no |
| Omni's own CPU (cores), mean | 0.08084 | 0.01235 | −84.7% | −0.0848 to −0.0521 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.122 | 1.066 | −5.0% | −0.0792 to −0.0333 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 616.8 | 610.8 | −1.0% | −17.6568 to +5.5372 | no |
| HPA replicas, mean | 9.706 | 9.139 | −5.8% | −1.3094 to +0.1764 | no |
| pods started | 6.3 | 5.8 | −7.9% | −1.5256 to +0.5256 | no |
| pod start wait, total (s) | 10.3 | 9.3 | −9.7% | −3.4316 to +1.4316 | no |
| pod start wait, mean (s) | 1.637 | 1.634 | −0.2% | −0.2840 to +0.2781 | no |
| host CPU busy, the real machine under kind (%) | 35.1 | 33.17 | −5.5% | −2.5773 to −1.2806 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*