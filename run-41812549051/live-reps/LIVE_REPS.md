# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.304 | 5.332 |
| node-hours | 2.519 | 2.515 | 2.221 | 2.23 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 274.6 | 274.4 | 274.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 274.6 | 252.5 | 253.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 464.6 | 424.4 | 459.7 | 386.1 |
| response time (ms), 95th percentile | 1738 | 1867 | 1925 | 1866 |
| response time (ms), 99th percentile | 2408 | 2696 | 2691 | 2735 |
| time over the response line (% of samples) | 22.12 | 16.62 | 22.71 | 15.49 |
| failed requests (%) | 0 | 0 | 0.0117 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 10.3 | 11.5 | 10.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 96 | 80.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 3.704 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14 | 14.14 | 16.75 | 14.92 |
| utilisation (used / allocatable) | 0.06522 | 0.06536 | 0.07492 | 0.07627 |
| CPU used (cores), mean | 1.565 | 1.569 | 1.576 | 1.594 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07643 | 0.07451 |
| CPU used with Omni's own (cores), mean | 1.565 | 1.569 | 1.652 | 1.668 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 427.9 | 427.3 | 385.7 | 380.7 |
| HPA replicas, mean | 1.941 | 2.032 | 2.498 | 2.606 |
| pods started | 0 | 0.3 | 2.3 | 2.2 |
| pod start wait, total (s) | 0 | 0.4 | 5.4 | 5 |
| pod start wait, mean (s) | 0 | 0.3 | 2.103 | 1.732 |
| host CPU busy, the real machine under kind (%) | 44.67 | 44.92 | 48.21 | 48.29 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 825.2 | 825.9 | 837.9 | 839 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.851 | 4.946 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2042 | 0.225 | 0.1708 | 0.3917 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 1.2 | 1 | 2 |
| queue: job turnaround, submitted to done, mean (s) | 130.7 | 133.8 | 145.4 | 144.6 |
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
| worker nodes in service, mean | 6 | 5.332 | −11.1% | −1.4757 to +0.1396 | no |
| node-hours | 2.515 | 2.23 | −11.3% | −0.6260 to +0.0552 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274.4 | −0.1% | −1.1202 to +0.7324 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 253.4 | −7.7% | −46.6912 to +4.3742 | no |
| response time (ms), mean | 424.4 | 386.1 | −9.0% | −65.3478 to −11.2645 | yes: GAIN |
| response time (ms), 95th percentile | 1867 | 1866 | −0.1% | −171.9234 to +169.5074 | no |
| response time (ms), 99th percentile | 2696 | 2735 | +1.4% | −89.3679 to +166.6177 | no |
| time over the response line (% of samples) | 16.62 | 15.49 | −6.8% | −2.5123 to +0.2434 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 10.8 | +4.9% | −0.1952 to +1.1952 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 80.5 | +80.500 (native is 0) | +38.6109 to +122.3891 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.14 | 14.92 | +5.6% | −1.4653 to +3.0353 | no |
| utilisation (used / allocatable) | 0.06536 | 0.07627 | +16.7% | −0.0016 to +0.0235 | no |
| CPU used (cores), mean | 1.569 | 1.594 | +1.6% | +0.0039 to +0.0459 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07451 | +0.075 (native is 0) | +0.0678 to +0.0812 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.569 | 1.668 | +6.3% | +0.0747 to +0.1241 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 427.3 | 380.7 | −10.9% | −98.1200 to +4.9631 | no |
| HPA replicas, mean | 2.032 | 2.606 | +28.2% | +0.2890 to +0.8578 | yes: power given |
| pods started | 0.3 | 2.2 | +633.3% | +0.4914 to +3.3086 | yes: power given |
| pod start wait, total (s) | 0.4 | 5 | +1150.0% | +1.3975 to +7.8025 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.732 | +477.2% | +0.5102 to +2.3532 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.92 | 48.29 | +7.5% | +2.7114 to +4.0328 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 825.9 | 839 | +1.6% | +5.8722 to +20.3278 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.946 | −17.6% | −2.2684 to +0.1603 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.225 | 0.3917 | +74.1% | −0.2048 to +0.5381 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 2 | +66.7% | −1.5313 to +3.1313 | no |
| queue: job turnaround, submitted to done, mean (s) | 133.8 | 144.6 | +8.1% | +2.8171 to +18.8829 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 2.519 | 2.515 | −0.1% | −0.0083 to +0.0009 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 274.6 | −0.1% | −0.8382 to +0.1648 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 274.6 | −0.1% | −0.8382 to +0.1648 | no |
| response time (ms), mean | 464.6 | 424.4 | −8.6% | −71.2474 to −9.0628 | yes: GAIN |
| response time (ms), 95th percentile | 1738 | 1867 | +7.4% | −25.9600 to +284.0320 | no |
| response time (ms), 99th percentile | 2408 | 2696 | +12.0% | +74.6108 to +501.0888 | yes: LOSS |
| time over the response line (% of samples) | 22.12 | 16.62 | −24.9% | −8.4779 to −2.5146 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 10.3 | −3.7% | −1.3656 to +0.5656 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14 | 14.14 | +1.0% | −1.3351 to +1.6151 | no |
| utilisation (used / allocatable) | 0.06522 | 0.06536 | +0.2% | −0.0003 to +0.0006 | no |
| CPU used (cores), mean | 1.565 | 1.569 | +0.2% | −0.0081 to +0.0151 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.565 | 1.569 | +0.2% | −0.0081 to +0.0151 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 427.9 | 427.3 | −0.1% | −3.9968 to +2.7924 | no |
| HPA replicas, mean | 1.941 | 2.032 | +4.7% | +0.0207 to +0.1620 | yes: power given |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2032 to +1.0032 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| host CPU busy, the real machine under kind (%) | 44.67 | 44.92 | +0.6% | +0.0031 to +0.4899 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 825.2 | 825.9 | +0.1% | −3.6972 to +5.0972 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2042 | 0.225 | +10.2% | −0.0303 to +0.0720 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 1.2 | +20.0% | −0.3642 to +0.7642 | no |
| queue: job turnaround, submitted to done, mean (s) | 130.7 | 133.8 | +2.4% | −1.0841 to +7.2841 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.304 | −11.6% | −1.3644 to −0.0275 | yes: GAIN |
| node-hours | 2.519 | 2.221 | −11.8% | −0.5777 to −0.0182 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 274.4 | −0.2% | −1.5791 to +0.5501 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 252.5 | −8.1% | −43.5657 to −1.2340 | yes: GAIN |
| response time (ms), mean | 464.6 | 459.7 | −1.1% | −17.4254 to +7.6374 | no |
| response time (ms), 95th percentile | 1738 | 1925 | +10.8% | +48.1543 to +326.1957 | yes: LOSS |
| response time (ms), 99th percentile | 2408 | 2691 | +11.7% | +77.0884 to +488.6006 | yes: LOSS |
| time over the response line (% of samples) | 22.12 | 22.71 | +2.7% | −0.0002 to +1.1841 | no |
| failed requests (%) | 0 | 0.0117 | +0.012 (native is 0) | −0.0148 to +0.0382 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 11.5 | +7.5% | −0.4064 to +2.0064 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 96 | +96.000 (native is 0) | +36.1123 to +155.8877 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14 | 16.75 | +19.7% | −0.7587 to +6.2720 | no |
| utilisation (used / allocatable) | 0.06522 | 0.07492 | +14.9% | +0.0003 to +0.0191 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.565 | 1.576 | +0.7% | −0.0057 to +0.0266 | no |
| Omni's own CPU (cores), mean | 0 | 0.07643 | +0.076 (native is 0) | +0.0703 to +0.0826 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.565 | 1.652 | +5.5% | +0.0668 to +0.1070 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 427.9 | 385.7 | −9.9% | −82.5929 to −1.7398 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.941 | 2.498 | +28.7% | +0.2867 to +0.8268 | yes: power given |
| pods started | 0 | 2.3 | +2.300 (native is 0) | +1.1791 to +3.4209 | yes: power given |
| pod start wait, total (s) | 0 | 5.4 | +5.400 (native is 0) | +2.6772 to +8.1228 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.103 | +2.103 (native is 0) | +1.4166 to +2.7900 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.67 | 48.21 | +7.9% | +3.0389 to +4.0305 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 825.2 | 837.9 | +1.5% | +4.4538 to +20.9462 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.851 | −19.2% | −2.1082 to −0.1905 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2042 | 0.1708 | −16.3% | −0.1737 to +0.1070 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 1 | ±0.0% | −0.8921 to +0.8921 | no |
| queue: job turnaround, submitted to done, mean (s) | 130.7 | 145.4 | +11.3% | +6.6424 to +22.8743 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.304 | −11.6% | −1.3644 to −0.0275 | yes: GAIN |
| node-hours | 2.515 | 2.221 | −11.7% | −0.5773 to −0.0113 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 274.4 | −0.1% | −1.3158 to +0.9603 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 252.5 | −8.0% | −43.5713 to −0.5550 | yes: GAIN |
| response time (ms), mean | 424.4 | 459.7 | +8.3% | +2.8978 to +67.6244 | yes: LOSS |
| response time (ms), 95th percentile | 1867 | 1925 | +3.1% | −21.2078 to +137.4858 | no |
| response time (ms), 99th percentile | 2696 | 2691 | −0.2% | −210.0739 to +200.0633 | no |
| time over the response line (% of samples) | 16.62 | 22.71 | +36.6% | +3.3020 to +8.8744 | yes: LOSS |
| failed requests (%) | 0 | 0.0117 | +0.012 (native is 0) | −0.0148 to +0.0382 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 11.5 | +11.7% | −0.7604 to +3.1604 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 96 | +96.000 (native is 0) | +36.1123 to +155.8877 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.14 | 16.75 | +18.5% | −0.4441 to +5.6775 | no |
| utilisation (used / allocatable) | 0.06536 | 0.07492 | +14.6% | +0.0001 to +0.0190 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.569 | 1.576 | +0.4% | −0.0125 to +0.0264 | no |
| Omni's own CPU (cores), mean | 0 | 0.07643 | +0.076 (native is 0) | +0.0703 to +0.0826 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.569 | 1.652 | +5.3% | +0.0597 to +0.1070 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 427.3 | 385.7 | −9.7% | −82.3163 to −0.8119 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.032 | 2.498 | +22.9% | +0.1492 to +0.7815 | yes: power given |
| pods started | 0.3 | 2.3 | +666.7% | +0.9884 to +3.0116 | yes: power given |
| pod start wait, total (s) | 0.4 | 5.4 | +1250.0% | +2.4766 to +7.5234 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 2.103 | +601.1% | +0.9700 to +2.6366 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.92 | 48.21 | +7.3% | +2.6774 to +3.8989 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 825.9 | 837.9 | +1.5% | +3.7129 to +20.2871 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.851 | −19.2% | −2.1082 to −0.1905 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.225 | 0.1708 | −24.1% | −0.1995 to +0.0912 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 1 | −16.7% | −0.8573 to +0.4573 | no |
| queue: job turnaround, submitted to done, mean (s) | 133.8 | 145.4 | +8.7% | +2.6634 to +20.6533 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.332 | −11.1% | −1.4757 to +0.1396 | no |
| node-hours | 2.519 | 2.23 | −11.5% | −0.6268 to +0.0487 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 274.4 | −0.2% | −1.4711 to +0.4098 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 253.4 | −7.8% | −46.7516 to +3.7612 | no |
| response time (ms), mean | 464.6 | 386.1 | −16.9% | −112.4829 to −44.4395 | yes: GAIN |
| response time (ms), 95th percentile | 1738 | 1866 | +7.4% | −40.6414 to +296.2974 | no |
| response time (ms), 99th percentile | 2408 | 2735 | +13.6% | +95.2070 to +557.7424 | yes: LOSS |
| time over the response line (% of samples) | 22.12 | 15.49 | −30.0% | −10.0687 to −3.1927 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 10.8 | +0.9% | −0.3060 to +0.5060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 80.5 | +80.500 (native is 0) | +38.6109 to +122.3891 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14 | 14.92 | +6.6% | −1.6013 to +3.4513 | no |
| utilisation (used / allocatable) | 0.06522 | 0.07627 | +16.9% | −0.0014 to +0.0235 | no |
| CPU used (cores), mean | 1.565 | 1.594 | +1.8% | +0.0105 to +0.0463 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07451 | +0.075 (native is 0) | +0.0678 to +0.0812 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.565 | 1.668 | +6.6% | +0.0816 to +0.1243 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 427.9 | 380.7 | −11.0% | −97.8312 to +3.4698 | no |
| HPA replicas, mean | 1.941 | 2.606 | +34.3% | +0.4101 to +0.9195 | yes: power given |
| pods started | 0 | 2.2 | +2.200 (native is 0) | +0.9474 to +3.4526 | yes: power given |
| pod start wait, total (s) | 0 | 5 | +5.000 (native is 0) | +2.0029 to +7.9971 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.732 | +1.732 (native is 0) | +0.9988 to +2.4645 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.67 | 48.29 | +8.1% | +3.0660 to +4.1712 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 825.2 | 839 | +1.7% | +6.2993 to +21.3007 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.946 | −17.6% | −2.2684 to +0.1603 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2042 | 0.3917 | +91.8% | −0.1880 to +0.5630 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1 | 2 | +100.0% | −1.0511 to +3.0511 | no |
| queue: job turnaround, submitted to done, mean (s) | 130.7 | 144.6 | +10.7% | +6.2671 to +21.6329 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*