# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.392 | 5.147 |
| node-hours | 2.51 | 2.515 | 2.256 | 2.161 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.5 | 275 | 274.4 | 275.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.5 | 275 | 255.3 | 248.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 499 | 427.4 | 464 | 431.4 |
| response time (ms), 95th percentile | 1915 | 1818 | 1974 | 1972 |
| response time (ms), 99th percentile | 2615 | 2694 | 2636 | 2859 |
| time over the response line (% of samples) | 21.66 | 16.1 | 21.48 | 17.04 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 9.1 | 11.6 | 10.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 63 | 70.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 50 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.22 | 25.33 | 18.54 | 32.99 |
| utilisation (used / allocatable) | 0.06709 | 0.06691 | 0.07411 | 0.07797 |
| CPU used (cores), mean | 1.61 | 1.606 | 1.585 | 1.592 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07411 | 0.07991 |
| CPU used with Omni's own (cores), mean | 1.61 | 1.606 | 1.659 | 1.672 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 417.2 | 417.4 | 388.4 | 373.9 |
| HPA replicas, mean | 2.065 | 2.022 | 2.257 | 2.279 |
| pods started | 0.1 | 0.1 | 1.1 | 0.9 |
| pod start wait, total (s) | 0.2 | 0.2 | 2.5 | 1.8 |
| pod start wait, mean (s) | 0.2 | 0.2 | 1.35 | 0.775 |
| host CPU busy, the real machine under kind (%) | 45.92 | 46.84 | 48.74 | 50.27 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 840.6 | 851.6 | 843.6 | 869.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.993 | 4.515 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4833 | 0.9833 | 0.5875 | 1.179 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.5 | 2.8 | 2.6 | 3.5 |
| queue: job turnaround, submitted to done, mean (s) | 143.3 | 163.5 | 146.9 | 179.1 |
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
| worker nodes in service, mean | 6 | 5.147 | −14.2% | −1.6176 to −0.0882 | yes: GAIN |
| node-hours | 2.515 | 2.161 | −14.1% | −0.6723 to −0.0354 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 275 | 275.4 | +0.1% | −0.1341 to +0.8531 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275 | 248.5 | −9.6% | −50.5709 to −2.4393 | yes: GAIN |
| response time (ms), mean | 427.4 | 431.4 | +0.9% | −69.1609 to +77.1529 | no |
| response time (ms), 95th percentile | 1818 | 1972 | +8.4% | −153.4954 to +460.4174 | no |
| response time (ms), 99th percentile | 2694 | 2859 | +6.1% | −94.0512 to +424.4108 | no |
| time over the response line (% of samples) | 16.1 | 17.04 | +5.9% | −0.6801 to +2.5721 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 10.1 | +11.0% | +0.1079 to +1.8921 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 70.7 | +70.700 (native is 0) | +11.6410 to +129.7590 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 25.33 | 32.99 | +30.2% | −5.2713 to +20.5779 | no |
| utilisation (used / allocatable) | 0.06691 | 0.07797 | +16.5% | +0.0012 to +0.0209 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.606 | 1.592 | −0.9% | −0.0596 to +0.0317 | no |
| Omni's own CPU (cores), mean | 0 | 0.07991 | +0.080 (native is 0) | +0.0759 to +0.0839 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.606 | 1.672 | +4.1% | +0.0190 to +0.1129 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 417.4 | 373.9 | −10.4% | −82.3422 to −4.7200 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.022 | 2.279 | +12.7% | −0.0619 to +0.5757 | no |
| pods started | 0.1 | 0.9 | +800.0% | −0.2556 to +1.8556 | no |
| pod start wait, total (s) | 0.2 | 1.8 | +800.0% | −0.6920 to +3.8920 | no |
| pod start wait, mean (s) | 0.2 | 0.775 | +287.5% | −0.4083 to +1.5583 | no |
| host CPU busy, the real machine under kind (%) | 46.84 | 50.27 | +7.3% | +2.5371 to +4.3148 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 851.6 | 869.2 | +2.1% | −0.1156 to +35.3156 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.515 | −24.8% | −2.7543 to −0.2167 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9833 | 1.179 | +19.9% | −0.1437 to +0.5354 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.8 | 3.5 | +25.0% | −1.6374 to +3.0374 | no |
| queue: job turnaround, submitted to done, mean (s) | 163.5 | 179.1 | +9.5% | −5.5141 to +36.5975 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.51 | 2.515 | +0.2% | −0.0039 to +0.0139 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.5 | 275 | +0.2% | −0.5007 to +1.4195 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.5 | 275 | +0.2% | −0.5007 to +1.4195 | no |
| response time (ms), mean | 499 | 427.4 | −14.4% | −115.6659 to −27.6352 | yes: GAIN |
| response time (ms), 95th percentile | 1915 | 1818 | −5.0% | −271.4607 to +78.1737 | no |
| response time (ms), 99th percentile | 2615 | 2694 | +3.0% | −224.3714 to +382.5856 | no |
| time over the response line (% of samples) | 21.66 | 16.1 | −25.7% | −8.1925 to −2.9297 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 9.1 | −18.7% | −4.1077 to −0.0923 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.22 | 25.33 | +47.1% | +4.5433 to +11.6834 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06709 | 0.06691 | −0.3% | −0.0010 to +0.0007 | no |
| CPU used (cores), mean | 1.61 | 1.606 | −0.3% | −0.0245 to +0.0160 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.61 | 1.606 | −0.3% | −0.0245 to +0.0160 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 417.2 | 417.4 | +0.1% | −4.9519 to +5.3983 | no |
| HPA replicas, mean | 2.065 | 2.022 | −2.0% | −0.1645 to +0.0800 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 45.92 | 46.84 | +2.0% | +0.4738 to +1.3711 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 840.6 | 851.6 | +1.3% | +2.2328 to +19.7672 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4833 | 0.9833 | +103.4% | −0.2064 to +1.2064 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.5 | 2.8 | −20.0% | −6.3429 to +4.9429 | no |
| queue: job turnaround, submitted to done, mean (s) | 143.3 | 163.5 | +14.1% | +9.4858 to +30.9642 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.392 | −10.1% | −1.2980 to +0.0826 | no |
| node-hours | 2.51 | 2.256 | −10.1% | −0.5429 to +0.0350 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.5 | 274.4 | −0.1% | −1.0499 to +0.6943 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.5 | 255.3 | −7.0% | −41.0503 to +2.5280 | no |
| response time (ms), mean | 499 | 464 | −7.0% | −58.6744 to −11.3094 | yes: GAIN |
| response time (ms), 95th percentile | 1915 | 1974 | +3.1% | −80.8043 to +198.6263 | no |
| response time (ms), 99th percentile | 2615 | 2636 | +0.8% | −116.5120 to +159.7300 | no |
| time over the response line (% of samples) | 21.66 | 21.48 | −0.8% | −0.6128 to +0.2521 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 11.6 | +3.6% | +0.0306 to +0.7694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 63 | +63.000 (native is 0) | +1.3940 to +124.6060 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.22 | 18.53 | +7.6% | −2.9155 to +5.5455 | no |
| utilisation (used / allocatable) | 0.06709 | 0.07411 | +10.5% | −0.0025 to +0.0166 | no |
| CPU used (cores), mean | 1.61 | 1.585 | −1.6% | −0.0510 to +0.0003 | no |
| Omni's own CPU (cores), mean | 0 | 0.07411 | +0.074 (native is 0) | +0.0690 to +0.0792 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.61 | 1.659 | +3.0% | +0.0197 to +0.0778 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 417.2 | 388.4 | −6.9% | −65.3779 to +7.7269 | no |
| HPA replicas, mean | 2.065 | 2.257 | +9.3% | −0.0843 to +0.4692 | no |
| pods started | 0.1 | 1.1 | +1000.0% | +0.0463 to +1.9537 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.5 | +1150.0% | +0.1396 to +4.4604 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.35 | +575.0% | +0.1955 to +2.1045 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.92 | 48.74 | +6.2% | +2.2220 to +3.4320 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 840.6 | 843.6 | +0.4% | −5.0998 to +11.0998 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.993 | −16.8% | −2.0324 to +0.0189 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4833 | 0.5875 | +21.6% | −0.2497 to +0.4580 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.5 | 2.6 | −25.7% | −6.7836 to +4.9836 | no |
| queue: job turnaround, submitted to done, mean (s) | 143.3 | 146.9 | +2.5% | −2.7934 to +9.8768 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.392 | −10.1% | −1.2980 to +0.0826 | no |
| node-hours | 2.515 | 2.256 | −10.3% | −0.5461 to +0.0282 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275 | 274.4 | −0.2% | −1.6580 to +0.3836 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275 | 255.3 | −7.2% | −41.3601 to +1.9190 | no |
| response time (ms), mean | 427.4 | 464 | +8.6% | +3.8849 to +69.4323 | yes: LOSS |
| response time (ms), 95th percentile | 1818 | 1974 | +8.6% | +53.5346 to +257.5744 | yes: LOSS |
| response time (ms), 99th percentile | 2694 | 2636 | −2.1% | −262.6858 to +147.6896 | no |
| time over the response line (% of samples) | 16.1 | 21.48 | +33.4% | +2.8688 to +7.8927 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 11.6 | +27.5% | +0.2068 to +4.7932 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 63 | +63.000 (native is 0) | +1.3940 to +124.6060 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 25.33 | 18.54 | −26.8% | −11.0785 to −2.5182 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06691 | 0.07411 | +10.8% | −0.0023 to +0.0167 | no |
| CPU used (cores), mean | 1.606 | 1.585 | −1.3% | −0.0508 to +0.0085 | no |
| Omni's own CPU (cores), mean | 0 | 0.07411 | +0.074 (native is 0) | +0.0690 to +0.0792 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.606 | 1.659 | +3.3% | +0.0199 to +0.0860 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 417.4 | 388.4 | −7.0% | −65.7884 to +7.6910 | no |
| HPA replicas, mean | 2.022 | 2.257 | +11.6% | −0.0458 to +0.5152 | no |
| pods started | 0.1 | 1.1 | +1000.0% | −0.0116 to +2.0116 | no |
| pod start wait, total (s) | 0.2 | 2.5 | +1150.0% | +0.0367 to +4.5633 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.35 | +575.0% | −0.0187 to +2.3187 | no |
| host CPU busy, the real machine under kind (%) | 46.84 | 48.74 | +4.1% | +1.2867 to +2.5223 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 851.6 | 843.6 | −0.9% | −20.9416 to +4.9416 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.993 | −16.8% | −2.0324 to +0.0189 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9833 | 0.5875 | −40.3% | −0.9971 to +0.2054 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.8 | 2.6 | −7.1% | −3.1933 to +2.7933 | no |
| queue: job turnaround, submitted to done, mean (s) | 163.5 | 146.9 | −10.2% | −28.3914 to −4.9753 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.147 | −14.2% | −1.6176 to −0.0882 | yes: GAIN |
| node-hours | 2.51 | 2.161 | −13.9% | −0.6702 to −0.0275 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.5 | 275.4 | +0.3% | −0.2654 to +1.9033 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.5 | 248.5 | −9.5% | −50.3617 to −1.7296 | yes: GAIN |
| response time (ms), mean | 499 | 431.4 | −13.6% | −136.6606 to +1.3515 | no |
| response time (ms), 95th percentile | 1915 | 1972 | +3.0% | −278.9780 to +392.6130 | no |
| response time (ms), 99th percentile | 2615 | 2859 | +9.3% | −11.5389 to +500.1127 | no |
| time over the response line (% of samples) | 21.66 | 17.04 | −21.3% | −7.4509 to −1.7792 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 10.1 | −9.8% | −2.9299 to +0.7299 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 70.7 | +70.700 (native is 0) | +11.6410 to +129.7590 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.22 | 32.99 | +91.6% | +2.4594 to +29.0739 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06709 | 0.07797 | +16.2% | +0.0007 to +0.0211 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.61 | 1.592 | −1.1% | −0.0522 to +0.0159 | no |
| Omni's own CPU (cores), mean | 0 | 0.07991 | +0.080 (native is 0) | +0.0759 to +0.0839 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.61 | 1.672 | +3.8% | +0.0260 to +0.0975 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 417.2 | 373.9 | −10.4% | −84.1401 to −2.4757 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.065 | 2.279 | +10.4% | −0.0834 to +0.5126 | no |
| pods started | 0.1 | 0.9 | +800.0% | −0.1417 to +1.7417 | no |
| pod start wait, total (s) | 0.2 | 1.8 | +800.0% | −0.5905 to +3.7905 | no |
| pod start wait, mean (s) | 0.2 | 0.775 | +287.5% | −0.2849 to +1.4349 | no |
| host CPU busy, the real machine under kind (%) | 45.92 | 50.27 | +9.5% | +3.5371 to +5.1599 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 840.6 | 869.2 | +3.4% | +11.4485 to +45.7515 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.515 | −24.8% | −2.7543 to −0.2167 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4833 | 1.179 | +144.0% | +0.1836 to +1.2080 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.5 | 3.5 | ±0.0% | −4.9443 to +4.9443 | no |
| queue: job turnaround, submitted to done, mean (s) | 143.3 | 179.1 | +25.0% | +12.1565 to +59.3768 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*