# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.518 | 1.514 | 1.514 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159.9 | 159 | 159.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159.9 | 159 | 159.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 136.9 | 141.1 | 136.6 | 142.3 |
| response time (ms), 95th percentile | 284.1 | 283.6 | 277.5 | 287.1 |
| response time (ms), 99th percentile | 416.7 | 401.6 | 387.8 | 389.8 |
| time over the response line (% of samples) | 0.5035 | 0.3735 | 0.3467 | 0.3099 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.4 | 0 | 0.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 6.2 | 6.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2717 | 0.1333 | 0.1867 | 0.1883 |
| utilisation (used / allocatable) | 0.03766 | 0.04204 | 0.03851 | 0.04314 |
| CPU used (cores), mean | 0.9038 | 1.009 | 0.9242 | 1.035 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.03088 | 0.04869 |
| CPU used with Omni's own (cores), mean | 0.9038 | 1.009 | 0.955 | 1.084 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 697.9 | 629.3 | 685 | 615.6 |
| HPA replicas, mean | 8.903 | 8.92 | 10.4 | 10.16 |
| pods started | 4.7 | 4.4 | 7.8 | 7.4 |
| pod start wait, total (s) | 7.5 | 5.6 | 10.4 | 10.3 |
| pod start wait, mean (s) | 1.59 | 1.26 | 1.315 | 1.371 |
| host CPU busy, the real machine under kind (%) | 27.16 | 30.88 | 28.66 | 33.41 |
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
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.514 | 1.512 | −0.2% | −0.0105 to +0.0051 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.9 | 159.8 | −0.0% | −0.8148 to +0.7309 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.9 | 159.8 | −0.0% | −0.8148 to +0.7309 | no |
| response time (ms), mean | 141.1 | 142.3 | +0.8% | −1.8063 to +4.0694 | no |
| response time (ms), 95th percentile | 283.6 | 287.1 | +1.2% | −15.3765 to +22.3765 | no |
| response time (ms), 99th percentile | 401.6 | 389.8 | −2.9% | −32.5954 to +9.1332 | no |
| time over the response line (% of samples) | 0.3735 | 0.3099 | −17.0% | −0.2763 to +0.1493 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 6.4 | +6.400 (native is 0) | +5.1293 to +7.6707 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.1883 | +41.2% | −0.1970 to +0.3070 | no |
| utilisation (used / allocatable) | 0.04204 | 0.04314 | +2.6% | +0.0002 to +0.0020 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.009 | 1.035 | +2.6% | +0.0048 to +0.0476 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04869 | +0.049 (native is 0) | +0.0414 to +0.0560 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.009 | 1.084 | +7.4% | +0.0474 to +0.1025 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 629.3 | 615.6 | −2.2% | −25.7455 to −1.5799 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.92 | 10.16 | +13.9% | +0.5874 to +1.9006 | yes: power given |
| pods started | 4.4 | 7.4 | +68.2% | +1.4920 to +4.5080 | yes: power given |
| pod start wait, total (s) | 5.6 | 10.3 | +83.9% | +1.8980 to +7.5020 | yes: LOSS |
| pod start wait, mean (s) | 1.26 | 1.371 | +8.8% | −0.0762 to +0.2977 | no |
| host CPU busy, the real machine under kind (%) | 30.88 | 33.41 | +8.2% | +1.5590 to +3.5132 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.518 | 1.514 | −0.3% | −0.0140 to +0.0057 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159.9 | +0.3% | −0.5467 to +1.6368 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159.9 | +0.3% | −0.5467 to +1.6368 | no |
| response time (ms), mean | 136.9 | 141.1 | +3.1% | +0.6815 to +7.8309 | yes: LOSS |
| response time (ms), 95th percentile | 284.1 | 283.6 | −0.2% | −13.6983 to +12.7153 | no |
| response time (ms), 99th percentile | 416.7 | 401.6 | −3.6% | −46.9495 to +16.7003 | no |
| time over the response line (% of samples) | 0.5035 | 0.3735 | −25.8% | −0.5244 to +0.2643 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.4 | 0 | −100.0% | −1.0911 to +0.2911 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2717 | 0.1333 | −50.9% | −0.4355 to +0.1588 | no |
| utilisation (used / allocatable) | 0.03766 | 0.04204 | +11.6% | +0.0036 to +0.0051 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9038 | 1.009 | +11.6% | +0.0873 to +0.1231 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 0.9038 | 1.009 | +11.6% | +0.0873 to +0.1231 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 697.9 | 629.3 | −9.8% | −79.3515 to −57.9283 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.903 | 8.92 | +0.2% | −0.1253 to +0.1589 | no |
| pods started | 4.7 | 4.4 | −6.4% | −0.8889 to +0.2889 | no |
| pod start wait, total (s) | 7.5 | 5.6 | −25.3% | −3.4249 to −0.3751 | yes: GAIN |
| pod start wait, mean (s) | 1.59 | 1.26 | −20.8% | −0.5891 to −0.0709 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 27.16 | 30.88 | +13.7% | +3.2447 to +4.1877 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.518 | 1.514 | −0.3% | −0.0137 to +0.0044 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159 | −0.2% | −1.2893 to +0.6274 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159 | −0.2% | −1.2893 to +0.6274 | no |
| response time (ms), mean | 136.9 | 136.6 | −0.2% | −4.7618 to +4.1546 | no |
| response time (ms), 95th percentile | 284.1 | 277.5 | −2.3% | −20.1754 to +6.9884 | no |
| response time (ms), 99th percentile | 416.7 | 387.8 | −6.9% | −60.6869 to +2.8411 | no |
| time over the response line (% of samples) | 0.5035 | 0.3467 | −31.2% | −0.4389 to +0.1252 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.4 | 0.1 | −75.0% | −0.7828 to +0.1828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 6.2 | +6.200 (native is 0) | +4.6996 to +7.7004 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2717 | 0.1867 | −31.3% | −0.4139 to +0.2439 | no |
| utilisation (used / allocatable) | 0.03766 | 0.03851 | +2.3% | −0.0000 to +0.0017 | no |
| CPU used (cores), mean | 0.9038 | 0.9242 | +2.3% | −0.0012 to +0.0419 | no |
| Omni's own CPU (cores), mean | 0 | 0.03088 | +0.031 (native is 0) | +0.0263 to +0.0354 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9038 | 0.955 | +5.7% | +0.0262 to +0.0763 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 697.9 | 685 | −1.9% | −27.7999 to +1.8415 | no |
| HPA replicas, mean | 8.903 | 10.4 | +16.8% | +0.4925 to +2.4965 | yes: power given |
| pods started | 4.7 | 7.8 | +66.0% | +0.9291 to +5.2709 | yes: power given |
| pod start wait, total (s) | 7.5 | 10.4 | +38.7% | −0.4796 to +6.2796 | no |
| pod start wait, mean (s) | 1.59 | 1.315 | −17.3% | −0.5197 to −0.0297 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 27.16 | 28.66 | +5.5% | +0.8636 to +2.1475 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.514 | −0.0% | −0.0108 to +0.0098 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.9 | 159 | −0.5% | −1.9244 to +0.1724 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.9 | 159 | −0.5% | −1.9244 to +0.1724 | no |
| response time (ms), mean | 141.1 | 136.6 | −3.2% | −7.6547 to −1.4649 | yes: GAIN |
| response time (ms), 95th percentile | 283.6 | 277.5 | −2.2% | −18.9449 to +6.7409 | no |
| response time (ms), 99th percentile | 401.6 | 387.8 | −3.4% | −38.0781 to +10.4815 | no |
| time over the response line (% of samples) | 0.3735 | 0.3467 | −7.2% | −0.2498 to +0.1962 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 6.2 | +6.200 (native is 0) | +4.6996 to +7.7004 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.1867 | +40.0% | −0.1656 to +0.2723 | no |
| utilisation (used / allocatable) | 0.04204 | 0.03851 | −8.4% | −0.0042 to −0.0029 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.009 | 0.9242 | −8.4% | −0.1012 to −0.0686 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03088 | +0.031 (native is 0) | +0.0263 to +0.0354 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.009 | 0.955 | −5.4% | −0.0733 to −0.0346 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 629.3 | 685 | +8.8% | +41.6246 to +69.6968 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.92 | 10.4 | +16.6% | +0.4752 to +2.4801 | yes: power given |
| pods started | 4.4 | 7.8 | +77.3% | +1.2356 to +5.5644 | yes: power given |
| pod start wait, total (s) | 5.6 | 10.4 | +85.7% | +1.8642 to +7.7358 | yes: LOSS |
| pod start wait, mean (s) | 1.26 | 1.315 | +4.4% | −0.0698 to +0.1804 | no |
| host CPU busy, the real machine under kind (%) | 30.88 | 28.66 | −7.2% | −2.7658 to −1.6556 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw +0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.518 | 1.512 | −0.5% | −0.0158 to +0.0021 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159.8 | +0.3% | −0.4918 to +1.4981 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159.8 | +0.3% | −0.4918 to +1.4981 | no |
| response time (ms), mean | 136.9 | 142.3 | +3.9% | +1.3767 to +9.3989 | yes: LOSS |
| response time (ms), 95th percentile | 284.1 | 287.1 | +1.1% | −12.6273 to +18.6443 | no |
| response time (ms), 99th percentile | 416.7 | 389.8 | −6.4% | −57.9958 to +4.2844 | no |
| time over the response line (% of samples) | 0.5035 | 0.3099 | −38.4% | −0.5271 to +0.1399 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.4 | 0 | −100.0% | −1.0911 to +0.2911 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 6.4 | +6.400 (native is 0) | +5.1293 to +7.6707 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2717 | 0.1883 | −30.7% | −0.4833 to +0.3166 | no |
| utilisation (used / allocatable) | 0.03766 | 0.04314 | +14.5% | +0.0044 to +0.0065 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9038 | 1.035 | +14.5% | +0.1061 to +0.1569 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04869 | +0.049 (native is 0) | +0.0414 to +0.0560 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9038 | 1.084 | +19.9% | +0.1481 to +0.2122 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 697.9 | 615.6 | −11.8% | −92.9977 to −71.6075 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.903 | 10.16 | +14.2% | +0.6382 to +1.8835 | yes: power given |
| pods started | 4.7 | 7.4 | +57.4% | +0.9462 to +4.4538 | yes: power given |
| pod start wait, total (s) | 7.5 | 10.3 | +37.3% | −0.6684 to +6.2684 | no |
| pod start wait, mean (s) | 1.59 | 1.371 | −13.8% | −0.5124 to +0.0740 | no |
| host CPU busy, the real machine under kind (%) | 27.16 | 33.41 | +23.0% | +5.1233 to +7.3813 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*