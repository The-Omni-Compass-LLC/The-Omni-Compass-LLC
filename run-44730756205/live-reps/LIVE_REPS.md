# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.512 | 1.513 | 1.511 | 1.509 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 159.4 | 158.4 | 159.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 159.4 | 158.4 | 159.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 116.7 | 118.8 | 119.3 | 119.8 |
| response time (ms), 95th percentile | 247.5 | 246.5 | 248.6 | 241.8 |
| response time (ms), 99th percentile | 354.5 | 352.2 | 362.2 | 337.2 |
| time over the response line (% of samples) | 0.3089 | 0.2835 | 0.3365 | 0.219 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.3 | 0.2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 5.7 | 5.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.32 | 0.1267 | 0.265 | 0.2733 |
| utilisation (used / allocatable) | 0.03688 | 0.04064 | 0.03714 | 0.04148 |
| CPU used (cores), mean | 0.885 | 0.9753 | 0.8913 | 0.9955 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.02781 | 0.04359 |
| CPU used with Omni's own (cores), mean | 0.885 | 0.9753 | 0.9191 | 1.039 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.6 | 651.3 | 709.5 | 639.1 |
| HPA replicas, mean | 8.893 | 8.849 | 9.579 | 9.662 |
| pods started | 4.6 | 4.9 | 6.6 | 6.3 |
| pod start wait, total (s) | 6.2 | 8.3 | 9.8 | 9.1 |
| pod start wait, mean (s) | 1.33 | 1.675 | 1.473 | 1.386 |
| host CPU busy, the real machine under kind (%) | 26.46 | 29.81 | 27.59 | 31.95 |
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
| node-hours | 1.513 | 1.509 | −0.2% | −0.0118 to +0.0048 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.4 | 159.2 | −0.1% | −1.0153 to +0.6029 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.4 | 159.2 | −0.1% | −1.0153 to +0.6029 | no |
| response time (ms), mean | 118.8 | 119.8 | +0.9% | −1.1686 to +3.2335 | no |
| response time (ms), 95th percentile | 246.5 | 241.8 | −1.9% | −18.4324 to +8.8744 | no |
| response time (ms), 99th percentile | 352.2 | 337.2 | −4.3% | −45.3207 to +15.2643 | no |
| time over the response line (% of samples) | 0.2835 | 0.219 | −22.8% | −0.2555 to +0.1263 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.3 | 0 | −100.0% | −0.7828 to +0.1828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.3 | +5.300 (native is 0) | +4.0361 to +6.5639 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1267 | 0.2733 | +115.8% | −0.1292 to +0.4226 | no |
| utilisation (used / allocatable) | 0.04064 | 0.04148 | +2.1% | +0.0004 to +0.0013 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9753 | 0.9955 | +2.1% | +0.0090 to +0.0315 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04359 | +0.044 (native is 0) | +0.0353 to +0.0518 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9753 | 1.039 | +6.5% | +0.0480 to +0.0797 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 651.3 | 639.1 | −1.9% | −18.7186 to −5.6916 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.849 | 9.662 | +9.2% | +0.0675 to +1.5596 | yes: power given |
| pods started | 4.9 | 6.3 | +28.6% | +0.2222 to +2.5778 | yes: power given |
| pod start wait, total (s) | 8.3 | 9.1 | +9.6% | −2.2868 to +3.8868 | no |
| pod start wait, mean (s) | 1.675 | 1.386 | −17.2% | −0.6265 to +0.0487 | no |
| host CPU busy, the real machine under kind (%) | 29.81 | 31.95 | +7.2% | +1.6414 to +2.6463 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.513 | +0.0% | −0.0096 to +0.0106 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 159.4 | +0.6% | −0.2137 to +1.9615 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 159.4 | +0.6% | −0.2137 to +1.9615 | no |
| response time (ms), mean | 116.7 | 118.8 | +1.8% | −1.4333 to +5.7209 | no |
| response time (ms), 95th percentile | 247.5 | 246.5 | −0.4% | −10.3585 to +8.3535 | no |
| response time (ms), 99th percentile | 354.5 | 352.2 | −0.7% | −25.8661 to +21.2357 | no |
| time over the response line (% of samples) | 0.3089 | 0.2835 | −8.2% | −0.3402 to +0.2895 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.3 | +50.0% | −0.4278 to +0.6278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.32 | 0.1267 | −60.4% | −0.6142 to +0.2275 | no |
| utilisation (used / allocatable) | 0.03688 | 0.04064 | +10.2% | +0.0030 to +0.0045 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.885 | 0.9753 | +10.2% | +0.0722 to +0.1083 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 0.885 | 0.9753 | +10.2% | +0.0722 to +0.1083 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.6 | 651.3 | −8.7% | −73.7191 to −50.8878 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.893 | 8.849 | −0.5% | −0.1979 to +0.1098 | no |
| pods started | 4.6 | 4.9 | +6.5% | −0.3786 to +0.9786 | no |
| pod start wait, total (s) | 6.2 | 8.3 | +33.9% | −0.1733 to +4.3733 | no |
| pod start wait, mean (s) | 1.33 | 1.675 | +25.9% | −0.0355 to +0.7255 | no |
| host CPU busy, the real machine under kind (%) | 26.46 | 29.81 | +12.6% | +2.7826 to +3.9070 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.511 | −0.1% | −0.0062 to +0.0042 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.4 | −0.0% | −0.6272 to +0.4724 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.4 | −0.0% | −0.6272 to +0.4724 | no |
| response time (ms), mean | 116.7 | 119.3 | +2.2% | −3.6558 to +8.8496 | no |
| response time (ms), 95th percentile | 247.5 | 248.6 | +0.4% | −18.7837 to +20.9607 | no |
| response time (ms), 99th percentile | 354.5 | 362.2 | +2.2% | −51.9250 to +67.3370 | no |
| time over the response line (% of samples) | 0.3089 | 0.3365 | +8.9% | −0.5063 to +0.5615 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.7 | +5.700 (native is 0) | +3.6475 to +7.7525 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.32 | 0.265 | −17.2% | −0.3504 to +0.2404 | no |
| utilisation (used / allocatable) | 0.03688 | 0.03714 | +0.7% | −0.0006 to +0.0011 | no |
| CPU used (cores), mean | 0.885 | 0.8913 | +0.7% | −0.0136 to +0.0261 | no |
| Omni's own CPU (cores), mean | 0 | 0.02781 | +0.028 (native is 0) | +0.0229 to +0.0327 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.885 | 0.9191 | +3.9% | +0.0120 to +0.0562 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.6 | 709.5 | −0.6% | −20.0733 to +11.9342 | no |
| HPA replicas, mean | 8.893 | 9.579 | +7.7% | +0.0054 to +1.3676 | yes: power given |
| pods started | 4.6 | 6.6 | +43.5% | +0.0925 to +3.9075 | yes: power given |
| pod start wait, total (s) | 6.2 | 9.8 | +58.1% | −0.0035 to +7.2035 | no |
| pod start wait, mean (s) | 1.33 | 1.473 | +10.8% | −0.2383 to +0.5246 | no |
| host CPU busy, the real machine under kind (%) | 26.46 | 27.59 | +4.3% | +0.7029 to +1.5580 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.511 | −0.1% | −0.0120 to +0.0090 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.4 | 158.4 | −0.6% | −2.1021 to +0.1995 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.4 | 158.4 | −0.6% | −2.1021 to +0.1995 | no |
| response time (ms), mean | 118.8 | 119.3 | +0.4% | −5.0391 to +5.9452 | no |
| response time (ms), 95th percentile | 246.5 | 248.6 | +0.8% | −15.7701 to +19.9521 | no |
| response time (ms), 99th percentile | 352.2 | 362.2 | +2.8% | −35.8902 to +55.9326 | no |
| time over the response line (% of samples) | 0.2835 | 0.3365 | +18.7% | −0.2405 to +0.3464 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.3 | 0.2 | −33.3% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.7 | +5.700 (native is 0) | +3.6475 to +7.7525 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1267 | 0.265 | +109.2% | −0.1874 to +0.4641 | no |
| utilisation (used / allocatable) | 0.04064 | 0.03714 | −8.6% | −0.0041 to −0.0029 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9753 | 0.8913 | −8.6% | −0.0993 to −0.0686 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02781 | +0.028 (native is 0) | +0.0229 to +0.0327 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9753 | 0.9191 | −5.8% | −0.0713 to −0.0410 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 651.3 | 709.5 | +8.9% | +46.1756 to +70.2922 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.849 | 9.579 | +8.3% | +0.0132 to +1.4479 | yes: power given |
| pods started | 4.9 | 6.6 | +34.7% | +0.2283 to +3.1717 | yes: power given |
| pod start wait, total (s) | 8.3 | 9.8 | +18.1% | −1.8762 to +4.8762 | no |
| pod start wait, mean (s) | 1.675 | 1.473 | −12.1% | −0.5994 to +0.1957 | no |
| host CPU busy, the real machine under kind (%) | 29.81 | 27.59 | −7.4% | −2.5559 to −1.8728 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.512 | 1.509 | −0.2% | −0.0106 to +0.0046 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 159.2 | +0.4% | −0.1116 to +1.4469 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 159.2 | +0.4% | −0.1116 to +1.4469 | no |
| response time (ms), mean | 116.7 | 119.8 | +2.7% | −0.9730 to +7.3256 | no |
| response time (ms), 95th percentile | 247.5 | 241.8 | −2.3% | −20.0682 to +8.5052 | no |
| response time (ms), 99th percentile | 354.5 | 337.2 | −4.9% | −45.9929 to +11.3061 | no |
| time over the response line (% of samples) | 0.3089 | 0.219 | −29.1% | −0.3498 to +0.1699 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.3 | +5.300 (native is 0) | +4.0361 to +6.5639 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.32 | 0.2733 | −14.6% | −0.3999 to +0.3065 | no |
| utilisation (used / allocatable) | 0.03688 | 0.04148 | +12.5% | +0.0037 to +0.0055 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.885 | 0.9955 | +12.5% | +0.0893 to +0.1317 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04359 | +0.044 (native is 0) | +0.0353 to +0.0518 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.885 | 1.039 | +17.4% | +0.1263 to +0.1819 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.6 | 639.1 | −10.4% | −86.7070 to −62.3102 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.893 | 9.662 | +8.7% | +0.0702 to +1.4689 | yes: power given |
| pods started | 4.6 | 6.3 | +37.0% | +0.0123 to +3.3877 | yes: power given |
| pod start wait, total (s) | 6.2 | 9.1 | +46.8% | −0.7854 to +6.5854 | no |
| pod start wait, mean (s) | 1.33 | 1.386 | +4.2% | −0.2656 to +0.3778 | no |
| host CPU busy, the real machine under kind (%) | 26.46 | 31.95 | +20.7% | +4.5857 to +6.3916 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*