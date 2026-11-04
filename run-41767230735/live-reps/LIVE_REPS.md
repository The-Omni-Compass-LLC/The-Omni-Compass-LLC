# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | omni, a decision every 120 s | omni, a decision every 90 s | omni, a decision every 75 s | omni, a decision every 30 s | omni, a decision every 15 s | omni, a decision every 5 s |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| node-hours | 1.512 | 1.514 | 1.514 | 1.514 | 1.512 | 1.514 | 1.514 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 158.9 | 158.9 | 158.9 | 158.8 | 158.9 | 159 | 159.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 158.9 | 158.9 | 158.9 | 158.8 | 158.9 | 159 | 159.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan | nan | nan | nan | nan |
| response time (ms), mean | 160.4 | 81.79 | 81.11 | 81.17 | 81.09 | 81.81 | 81.95 | 83.17 |
| response time (ms), 95th percentile | 357.2 | 119.9 | 119.6 | 119.1 | 118.8 | 120.1 | 120.6 | 123.4 |
| response time (ms), 99th percentile | 607.7 | 163.2 | 160.2 | 158.8 | 154.4 | 164.6 | 162.3 | 171.1 |
| time over the response line (% of samples) | 2.162 | 0.03622 | 0.01198 | 0 | 0 | 0 | 0 | 0.04841 |
| failed requests (%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19 | 16.6 | 19.1 | 18.4 | 19.3 | 19.6 | 25.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 | nan | nan | nan | nan | 100 | 85 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1583 | 0.455 | 0.5 | 0.2717 | 0.1567 | 0.08 | 0.105 | 0.2633 |
| utilisation (used / allocatable) | 0.03966 | 0.03779 | 0.03772 | 0.03808 | 0.03804 | 0.03806 | 0.0383 | 0.03884 |
| CPU used (cores), mean | 0.9517 | 0.907 | 0.9053 | 0.914 | 0.9129 | 0.9134 | 0.9192 | 0.9321 |
| Omni's own CPU (cores), mean | 0 | 0.03735 | 0.0064 | 0.00727 | 0.00792 | 0.01483 | 0.02623 | 0.07235 |
| CPU used with Omni's own (cores), mean | 0.9517 | 0.9444 | 0.9117 | 0.9213 | 0.9208 | 0.9282 | 0.9454 | 1.004 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 673.8 | 701.8 | 702.6 | 696.5 | 698.1 | 697.2 | 693.2 | 685.1 |
| HPA replicas, mean | 8.767 | 9.015 | 8.577 | 8.533 | 7.846 | 7.848 | 8.874 | 9.347 |
| pods started | 5.4 | 4.5 | 4.9 | 4.5 | 4.2 | 4.3 | 4.3 | 5.6 |
| pod start wait, total (s) | 8.3 | 5.6 | 6.4 | 7.3 | 6.4 | 6.4 | 6.2 | 7.7 |
| pod start wait, mean (s) | 1.533 | 1.267 | 1.328 | 1.613 | 1.47 | 1.547 | 1.397 | 1.293 |
| host CPU busy, the real machine under kind (%) | 29.05 | 29.24 | 28.15 | 28.22 | 28.28 | 28.52 | 29.13 | 30.9 |
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
| node-hours | 1.512 | 1.514 | +0.1% | +0.0005 to +0.0035 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 158.9 | −0.1% | −0.4999 to +0.0753 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 158.9 | −0.1% | −0.4999 to +0.0753 | no |
| response time (ms), mean | 160.4 | 81.79 | −49.0% | −93.5206 to −63.6264 | yes: GAIN |
| response time (ms), 95th percentile | 357.2 | 119.9 | −66.4% | −287.9626 to −186.5004 | yes: GAIN |
| response time (ms), 99th percentile | 607.7 | 163.2 | −73.1% | −547.5197 to −341.3641 | yes: GAIN |
| time over the response line (% of samples) | 2.162 | 0.03622 | −98.3% | −3.3916 to −0.8596 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.3 | 0 | −100.0% | −3.9189 to −0.6811 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19 | +19.000 (native is 0) | +17.5302 to +20.4698 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1583 | 0.455 | +187.4% | −0.0665 to +0.6599 | no |
| utilisation (used / allocatable) | 0.03966 | 0.03779 | −4.7% | −0.0028 to −0.0010 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9517 | 0.907 | −4.7% | −0.0666 to −0.0228 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03735 | +0.037 (native is 0) | +0.0342 to +0.0405 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9517 | 0.9444 | −0.8% | −0.0274 to +0.0127 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 673.8 | 701.8 | +4.2% | +16.2238 to +39.8003 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.767 | 9.015 | +2.8% | +0.0022 to +0.4933 | yes: power given |
| pods started | 5.4 | 4.5 | −16.7% | −2.2676 to +0.4676 | no |
| pod start wait, total (s) | 8.3 | 5.6 | −32.5% | −4.8072 to −0.5928 | yes: GAIN |
| pod start wait, mean (s) | 1.533 | 1.267 | −17.4% | −0.5317 to −0.0016 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 29.05 | 29.24 | +0.7% | −0.1965 to +0.5760 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.512 | 1.514 | +0.1% | +0.0005 to +0.0028 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 158.9 | −0.1% | −0.4924 to +0.0178 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 158.9 | −0.1% | −0.4924 to +0.0178 | no |
| response time (ms), mean | 160.4 | 81.11 | −49.4% | −94.7056 to −63.7966 | yes: GAIN |
| response time (ms), 95th percentile | 357.2 | 119.6 | −66.5% | −289.7870 to −185.4560 | yes: GAIN |
| response time (ms), 99th percentile | 607.7 | 160.2 | −73.6% | −555.1741 to −339.8267 | yes: GAIN |
| time over the response line (% of samples) | 2.162 | 0.01198 | −99.4% | −3.4199 to −0.8798 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.3 | 0 | −100.0% | −3.9189 to −0.6811 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.6 | +16.600 (native is 0) | +15.9089 to +17.2911 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1583 | 0.5 | +215.8% | −0.0612 to +0.7446 | no |
| utilisation (used / allocatable) | 0.03966 | 0.03772 | −4.9% | −0.0030 to −0.0009 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9517 | 0.9053 | −4.9% | −0.0709 to −0.0218 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0064 | +0.006 (native is 0) | +0.0060 to +0.0068 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9517 | 0.9117 | −4.2% | −0.0642 to −0.0158 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 673.8 | 702.6 | +4.3% | +16.7356 to +40.9314 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.767 | 8.577 | −2.2% | −0.4451 to +0.0645 | no |
| pods started | 5.4 | 4.9 | −9.3% | −1.5796 to +0.5796 | no |
| pod start wait, total (s) | 8.3 | 6.4 | −22.9% | −3.7910 to −0.0090 | yes: GAIN |
| pod start wait, mean (s) | 1.533 | 1.328 | −13.4% | −0.5531 to +0.1431 | no |
| host CPU busy, the real machine under kind (%) | 29.05 | 28.15 | −3.1% | −1.3589 to −0.4355 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.514 | +0.1% | +0.0004 to +0.0033 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 158.9 | −0.1% | −0.5973 to +0.2247 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 158.9 | −0.1% | −0.5973 to +0.2247 | no |
| response time (ms), mean | 160.4 | 81.17 | −49.4% | −94.7310 to −63.6576 | yes: GAIN |
| response time (ms), 95th percentile | 357.2 | 119.1 | −66.6% | −289.4402 to −186.6518 | yes: GAIN |
| response time (ms), 99th percentile | 607.7 | 158.8 | −73.9% | −557.0073 to −340.7743 | yes: GAIN |
| time over the response line (% of samples) | 2.162 | 0 | −100.0% | −3.4394 to −0.8842 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.3 | 0 | −100.0% | −3.9189 to −0.6811 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.1 | +19.100 (native is 0) | +18.1198 to +20.0802 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1583 | 0.2717 | +71.6% | −0.1882 to +0.4148 | no |
| utilisation (used / allocatable) | 0.03966 | 0.03808 | −4.0% | −0.0028 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9517 | 0.914 | −4.0% | −0.0668 to −0.0087 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00727 | +0.007 (native is 0) | +0.0066 to +0.0079 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9517 | 0.9213 | −3.2% | −0.0591 to −0.0018 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 673.8 | 696.5 | +3.4% | +6.2505 to +39.2628 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.767 | 8.533 | −2.7% | −0.5618 to +0.0945 | no |
| pods started | 5.4 | 4.5 | −16.7% | −1.9366 to +0.1366 | no |
| pod start wait, total (s) | 8.3 | 7.3 | −12.0% | −3.3362 to +1.3362 | no |
| pod start wait, mean (s) | 1.533 | 1.613 | +5.2% | −0.3014 to +0.4614 | no |
| host CPU busy, the real machine under kind (%) | 29.05 | 28.22 | −2.8% | −1.4719 to −0.1793 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.512 | +0.0% | −0.0011 to +0.0018 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 158.8 | −0.2% | −0.6883 to +0.0216 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 158.8 | −0.2% | −0.6883 to +0.0216 | no |
| response time (ms), mean | 160.4 | 81.09 | −49.4% | −94.5363 to −64.0142 | yes: GAIN |
| response time (ms), 95th percentile | 357.2 | 118.8 | −66.7% | −289.6239 to −187.0751 | yes: GAIN |
| response time (ms), 99th percentile | 607.7 | 154.4 | −74.6% | −559.1991 to −347.2817 | yes: GAIN |
| time over the response line (% of samples) | 2.162 | 0 | −100.0% | −3.4394 to −0.8842 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.3 | 0 | −100.0% | −3.9189 to −0.6811 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 18.4 | +18.400 (native is 0) | +16.1582 to +20.6418 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1583 | 0.1567 | −1.1% | −0.2016 to +0.1983 | no |
| utilisation (used / allocatable) | 0.03966 | 0.03804 | −4.1% | −0.0027 to −0.0005 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9517 | 0.9129 | −4.1% | −0.0652 to −0.0125 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00792 | +0.008 (native is 0) | +0.0072 to +0.0087 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9517 | 0.9208 | −3.2% | −0.0568 to −0.0051 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 673.8 | 698.1 | +3.6% | +8.8390 to +39.8898 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.767 | 7.846 | −10.5% | −1.5552 to −0.2872 | yes: GAIN |
| pods started | 5.4 | 4.2 | −22.2% | −2.3081 to −0.0919 | yes: GAIN |
| pod start wait, total (s) | 8.3 | 6.4 | −22.9% | −4.3187 to +0.5187 | no |
| pod start wait, mean (s) | 1.533 | 1.47 | −4.1% | −0.4391 to +0.3124 | no |
| host CPU busy, the real machine under kind (%) | 29.05 | 28.28 | −2.6% | −1.3288 to −0.1951 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.513 | +0.1% | −0.0009 to +0.0036 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 158.9 | −0.1% | −0.6830 to +0.2518 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 158.9 | −0.1% | −0.6830 to +0.2518 | no |
| response time (ms), mean | 160.4 | 81.81 | −49.0% | −93.6282 to −63.4701 | yes: GAIN |
| response time (ms), 95th percentile | 357.2 | 120.1 | −66.4% | −289.3535 to −184.7745 | yes: GAIN |
| response time (ms), 99th percentile | 607.7 | 164.6 | −72.9% | −545.9900 to −340.1636 | yes: GAIN |
| time over the response line (% of samples) | 2.162 | 0 | −100.0% | −3.4394 to −0.8842 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.3 | 0 | −100.0% | −3.9189 to −0.6811 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.3 | +19.300 (native is 0) | +17.7529 to +20.8471 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1583 | 0.08 | −49.5% | −0.2359 to +0.0792 | no |
| utilisation (used / allocatable) | 0.03966 | 0.03806 | −4.0% | −0.0029 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9517 | 0.9134 | −4.0% | −0.0685 to −0.0082 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01483 | +0.015 (native is 0) | +0.0135 to +0.0161 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9517 | 0.9282 | −2.5% | −0.0529 to +0.0059 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 673.8 | 697.2 | +3.5% | +5.0671 to +41.8530 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.767 | 7.848 | −10.5% | −1.1670 to −0.6715 | yes: GAIN |
| pods started | 5.4 | 4.3 | −20.4% | −1.8872 to −0.3128 | yes: GAIN |
| pod start wait, total (s) | 8.3 | 6.4 | −22.9% | −4.0446 to +0.2446 | no |
| pod start wait, mean (s) | 1.533 | 1.547 | +0.9% | −0.5700 to +0.5966 | no |
| host CPU busy, the real machine under kind (%) | 29.05 | 28.52 | −1.8% | −1.1694 to +0.1080 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.512 | 1.514 | +0.1% | −0.0003 to +0.0046 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 159 | −0.1% | −0.5095 to +0.3248 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 159 | −0.1% | −0.5095 to +0.3248 | no |
| response time (ms), mean | 160.4 | 81.95 | −48.9% | −93.5445 to −63.2856 | yes: GAIN |
| response time (ms), 95th percentile | 357.2 | 120.6 | −66.2% | −288.2411 to −184.9789 | yes: GAIN |
| response time (ms), 99th percentile | 607.7 | 162.3 | −73.3% | −546.2047 to −344.5001 | yes: GAIN |
| time over the response line (% of samples) | 2.162 | 0 | −100.0% | −3.4394 to −0.8842 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.3 | 0 | −100.0% | −3.9189 to −0.6811 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.6 | +19.600 (native is 0) | +18.5231 to +20.6769 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1583 | 0.105 | −33.7% | −0.1971 to +0.0905 | no |
| utilisation (used / allocatable) | 0.03966 | 0.0383 | −3.4% | −0.0023 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9517 | 0.9192 | −3.4% | −0.0558 to −0.0093 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02623 | +0.026 (native is 0) | +0.0241 to +0.0284 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9517 | 0.9454 | −0.7% | −0.0283 to +0.0156 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 673.8 | 693.2 | +2.9% | +6.3314 to +32.4326 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.767 | 8.874 | +1.2% | −0.0245 to +0.2388 | no |
| pods started | 5.4 | 4.3 | −20.4% | −2.2898 to +0.0898 | no |
| pod start wait, total (s) | 8.3 | 6.2 | −25.3% | −4.7647 to +0.5647 | no |
| pod start wait, mean (s) | 1.533 | 1.397 | −8.9% | −0.5729 to +0.2996 | no |
| host CPU busy, the real machine under kind (%) | 29.05 | 29.13 | +0.3% | −0.5117 to +0.6816 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs native, 10 paired repetitions

| Gauge | native | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.513 | +0.1% | −0.0047 to +0.0073 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.1 | 159.1 | −0.0% | −0.7245 to +0.6173 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.1 | 159.1 | −0.0% | −0.7245 to +0.6173 | no |
| response time (ms), mean | 160.4 | 83.17 | −48.1% | −91.2554 to −63.1281 | yes: GAIN |
| response time (ms), 95th percentile | 357.2 | 123.4 | −65.5% | −282.9222 to −184.6408 | yes: GAIN |
| response time (ms), 99th percentile | 607.7 | 171.1 | −71.8% | −533.8242 to −339.3116 | yes: GAIN |
| time over the response line (% of samples) | 2.162 | 0.04841 | −97.8% | −3.3578 to −0.8690 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.3 | 0 | −100.0% | −3.9189 to −0.6811 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.2 | +25.200 (native is 0) | +18.5768 to +31.8232 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1583 | 0.2633 | +66.3% | −0.1336 to +0.3436 | no |
| utilisation (used / allocatable) | 0.03966 | 0.03884 | −2.1% | −0.0016 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9517 | 0.9321 | −2.1% | −0.0377 to −0.0016 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07235 | +0.072 (native is 0) | +0.0655 to +0.0792 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9517 | 1.004 | +5.5% | +0.0353 to +0.0701 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 673.8 | 685.1 | +1.7% | −1.6039 to +24.2736 | no |
| HPA replicas, mean | 8.767 | 9.347 | +6.6% | −0.5186 to +1.6795 | no |
| pods started | 5.4 | 5.6 | +3.7% | −1.2226 to +1.6226 | no |
| pod start wait, total (s) | 8.3 | 7.7 | −7.2% | −5.0505 to +3.8505 | no |
| pod start wait, mean (s) | 1.533 | 1.293 | −15.7% | −0.7779 to +0.2979 | no |
| host CPU busy, the real machine under kind (%) | 29.05 | 30.9 | +6.4% | +1.4384 to +2.2637 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 120 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 120 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.514 | −0.0% | −0.0020 to +0.0013 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.9 | −0.0% | −0.2051 to +0.1551 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.9 | −0.0% | −0.2051 to +0.1551 | no |
| response time (ms), mean | 81.79 | 81.11 | −0.8% | −1.4500 to +0.0948 | no |
| response time (ms), 95th percentile | 119.9 | 119.6 | −0.3% | −2.6794 to +1.8994 | no |
| response time (ms), 99th percentile | 163.2 | 160.2 | −1.9% | −13.2844 to +7.1674 | no |
| time over the response line (% of samples) | 0.03622 | 0.01198 | −66.9% | −0.0922 to +0.0437 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19 | 16.6 | −12.6% | −3.7146 to −1.0854 | yes, down (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.455 | 0.5 | +9.9% | −0.4613 to +0.5513 | no |
| utilisation (used / allocatable) | 0.03779 | 0.03772 | −0.2% | −0.0004 to +0.0002 | no |
| CPU used (cores), mean | 0.907 | 0.9053 | −0.2% | −0.0085 to +0.0052 | no |
| Omni's own CPU (cores), mean | 0.03735 | 0.0064 | −82.9% | −0.0337 to −0.0282 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9444 | 0.9117 | −3.5% | −0.0416 to −0.0236 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 701.8 | 702.6 | +0.1% | −4.2228 to +5.8658 | no |
| HPA replicas, mean | 9.015 | 8.577 | −4.9% | −0.6593 to −0.2169 | yes: GAIN |
| pods started | 4.5 | 4.9 | +8.9% | −0.5048 to +1.3048 | no |
| pod start wait, total (s) | 5.6 | 6.4 | +14.3% | −1.2732 to +2.8732 | no |
| pod start wait, mean (s) | 1.267 | 1.328 | +4.9% | −0.2323 to +0.3556 | no |
| host CPU busy, the real machine under kind (%) | 29.24 | 28.15 | −3.7% | −1.3852 to −0.7887 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 90 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 90 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.514 | −0.0% | −0.0018 to +0.0015 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.9 | +0.0% | −0.2425 to +0.2945 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.9 | +0.0% | −0.2425 to +0.2945 | no |
| response time (ms), mean | 81.79 | 81.17 | −0.8% | −1.7059 to +0.4643 | no |
| response time (ms), 95th percentile | 119.9 | 119.1 | −0.7% | −2.7302 to +1.1012 | no |
| response time (ms), 99th percentile | 163.2 | 158.8 | −2.7% | −20.0392 to +11.1414 | no |
| time over the response line (% of samples) | 0.03622 | 0 | −100.0% | −0.0944 to +0.0220 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19 | 19.1 | +0.5% | −1.6011 to +1.8011 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.455 | 0.2717 | −40.3% | −0.5598 to +0.1932 | no |
| utilisation (used / allocatable) | 0.03779 | 0.03808 | +0.8% | −0.0003 to +0.0009 | no |
| CPU used (cores), mean | 0.907 | 0.914 | +0.8% | −0.0067 to +0.0207 | no |
| Omni's own CPU (cores), mean | 0.03735 | 0.00727 | −80.5% | −0.0327 to −0.0275 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9444 | 0.9213 | −2.4% | −0.0383 to −0.0079 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 701.8 | 696.5 | −0.7% | −15.6608 to +5.1500 | no |
| HPA replicas, mean | 9.015 | 8.533 | −5.3% | −0.9040 to −0.0589 | yes: GAIN |
| pods started | 4.5 | 4.5 | ±0.0% | −1.2617 to +1.2617 | no |
| pod start wait, total (s) | 5.6 | 7.3 | +30.4% | +0.3491 to +3.0509 | yes: LOSS |
| pod start wait, mean (s) | 1.267 | 1.613 | +27.4% | −0.0456 to +0.7390 | no |
| host CPU busy, the real machine under kind (%) | 29.24 | 28.22 | −3.5% | −1.3843 to −0.6464 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 75 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 75 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.514 | 1.512 | −0.1% | −0.0033 to −0.0001 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.8 | −0.1% | −0.3802 to +0.1381 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.8 | −0.1% | −0.3802 to +0.1381 | no |
| response time (ms), mean | 81.79 | 81.09 | −0.9% | −1.9203 to +0.5168 | no |
| response time (ms), 95th percentile | 119.9 | 118.8 | −0.9% | −2.9914 to +0.7554 | no |
| response time (ms), 99th percentile | 163.2 | 154.4 | −5.4% | −18.5253 to +0.9283 | no |
| time over the response line (% of samples) | 0.03622 | 0 | −100.0% | −0.0944 to +0.0220 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19 | 18.4 | −3.2% | −3.5435 to +2.3435 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.455 | 0.1567 | −65.6% | −0.6154 to +0.0188 | no |
| utilisation (used / allocatable) | 0.03779 | 0.03804 | +0.6% | −0.0003 to +0.0008 | no |
| CPU used (cores), mean | 0.907 | 0.9129 | +0.6% | −0.0081 to +0.0199 | no |
| Omni's own CPU (cores), mean | 0.03735 | 0.00792 | −78.8% | −0.0319 to −0.0269 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9444 | 0.9208 | −2.5% | −0.0385 to −0.0086 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 701.8 | 698.1 | −0.5% | −15.1182 to +7.8230 | no |
| HPA replicas, mean | 9.015 | 7.846 | −13.0% | −1.7341 to −0.6039 | yes: GAIN |
| pods started | 4.5 | 4.2 | −6.7% | −1.5639 to +0.9639 | no |
| pod start wait, total (s) | 5.6 | 6.4 | +14.3% | −1.3539 to +2.9539 | no |
| pod start wait, mean (s) | 1.267 | 1.47 | +16.1% | −0.1880 to +0.5947 | no |
| host CPU busy, the real machine under kind (%) | 29.24 | 28.28 | −3.3% | −1.2696 to −0.6338 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 30 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 30 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.514 | −0.0% | −0.0028 to +0.0015 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 158.9 | −0.0% | −0.3063 to +0.2998 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 158.9 | −0.0% | −0.3063 to +0.2998 | no |
| response time (ms), mean | 81.79 | 81.81 | +0.0% | −0.8179 to +0.8666 | no |
| response time (ms), 95th percentile | 119.9 | 120.1 | +0.1% | −2.4669 to +2.8019 | no |
| response time (ms), 99th percentile | 163.2 | 164.6 | +0.8% | −6.0276 to +8.7578 | no |
| time over the response line (% of samples) | 0.03622 | 0 | −100.0% | −0.0944 to +0.0220 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19 | 19.3 | +1.6% | −2.2691 to +2.8691 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.455 | 0.08 | −82.4% | −0.7006 to −0.0494 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03779 | 0.03806 | +0.7% | −0.0003 to +0.0009 | no |
| CPU used (cores), mean | 0.907 | 0.9134 | +0.7% | −0.0076 to +0.0204 | no |
| Omni's own CPU (cores), mean | 0.03735 | 0.01483 | −60.3% | −0.0244 to −0.0206 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9444 | 0.9282 | −1.7% | −0.0306 to −0.0017 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 701.8 | 697.2 | −0.6% | −14.4643 to +5.3604 | no |
| HPA replicas, mean | 9.015 | 7.848 | −12.9% | −1.4327 to −0.9014 | yes: GAIN |
| pods started | 4.5 | 4.3 | −4.4% | −1.7379 to +1.3379 | no |
| pod start wait, total (s) | 5.6 | 6.4 | +14.3% | −1.9765 to +3.5765 | no |
| pod start wait, mean (s) | 1.267 | 1.547 | +22.1% | −0.3019 to +0.8619 | no |
| host CPU busy, the real machine under kind (%) | 29.24 | 28.52 | −2.5% | −1.0331 to −0.4078 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 15 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 15 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.514 | +0.0% | −0.0014 to +0.0017 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 159 | +0.1% | −0.1013 to +0.3413 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 159 | +0.1% | −0.1013 to +0.3413 | no |
| response time (ms), mean | 81.79 | 81.95 | +0.2% | −0.7636 to +1.0805 | no |
| response time (ms), 95th percentile | 119.9 | 120.6 | +0.5% | −1.6429 to +2.8859 | no |
| response time (ms), 99th percentile | 163.2 | 162.3 | −0.6% | −9.1694 to +7.3484 | no |
| time over the response line (% of samples) | 0.03622 | 0 | −100.0% | −0.0944 to +0.0220 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19 | 19.6 | +3.2% | −1.7410 to +2.9410 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 90 | 100 | +11.1% | −12.6200 to +32.6200 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.455 | 0.105 | −76.9% | −0.6617 to −0.0383 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03779 | 0.0383 | +1.3% | +0.0001 to +0.0009 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.907 | 0.9192 | +1.3% | +0.0029 to +0.0214 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.03735 | 0.02623 | −29.8% | −0.0124 to −0.0099 | yes, down (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9444 | 0.9454 | +0.1% | −0.0087 to +0.0108 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 701.8 | 693.2 | −1.2% | −15.2500 to −2.0101 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.015 | 8.874 | −1.6% | −0.3483 to +0.0671 | no |
| pods started | 4.5 | 4.3 | −4.4% | −1.2556 to +0.8556 | no |
| pod start wait, total (s) | 5.6 | 6.2 | +10.7% | −0.8385 to +2.0385 | no |
| pod start wait, mean (s) | 1.267 | 1.397 | +10.3% | −0.2783 to +0.5383 | no |
| host CPU busy, the real machine under kind (%) | 29.24 | 29.13 | −0.4% | −0.5461 to +0.3365 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni deciding every 5 s vs omni at its default, every 10 s, 10 paired repetitions

| Gauge | omni | omni, a decision every 5 s | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw +0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.514 | −0.0% | −0.0070 to +0.0056 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.9 | 159.1 | +0.1% | −0.5440 to +0.8614 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.9 | 159.1 | +0.1% | −0.5440 to +0.8614 | no |
| response time (ms), mean | 81.79 | 83.17 | +1.7% | +0.2132 to +2.5502 | yes: LOSS |
| response time (ms), 95th percentile | 119.9 | 123.4 | +2.9% | +1.3064 to +5.5936 | yes: LOSS |
| response time (ms), 99th percentile | 163.2 | 171.1 | +4.8% | −2.6080 to +18.3560 | no |
| time over the response line (% of samples) | 0.03622 | 0.04841 | +33.7% | −0.0368 to +0.0612 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 19 | 25.2 | +32.6% | −1.1707 to +13.5707 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 90 | 85 | −5.6% | −16.3100 to +6.3100 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.455 | 0.2633 | −42.1% | −0.5141 to +0.1308 | no |
| utilisation (used / allocatable) | 0.03779 | 0.03884 | +2.8% | +0.0006 to +0.0015 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.907 | 0.9321 | +2.8% | +0.0133 to +0.0368 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.03735 | 0.07235 | +93.7% | +0.0311 to +0.0389 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9444 | 1.004 | +6.4% | +0.0454 to +0.0748 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 701.8 | 685.1 | −2.4% | −23.5691 to −9.7852 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.015 | 9.347 | +3.7% | −0.6303 to +1.2956 | no |
| pods started | 4.5 | 5.6 | +24.4% | −0.9909 to +3.1909 | no |
| pod start wait, total (s) | 5.6 | 7.7 | +37.5% | −2.3152 to +6.5152 | no |
| pod start wait, mean (s) | 1.267 | 1.293 | +2.1% | −0.4750 to +0.5283 | no |
| host CPU busy, the real machine under kind (%) | 29.24 | 30.9 | +5.7% | +1.2546 to +2.0680 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*