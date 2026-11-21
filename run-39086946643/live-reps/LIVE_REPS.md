# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 12.02 | 12.02 |
| energy, parked workers still on at idle power (Wh, declared model) | 1393 | 1390 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1393 | 1390 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 439.9 | 305.6 |
| response time (ms), 95th percentile | 1485 | 1235 |
| response time (ms), 99th percentile | 4986 | 4457 |
| time over the response line (% of samples) | 31 | 21.38 |
| failed requests (%) | 18.86 | 15.53 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 83 | 67.67 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 131.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 40.43 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.65 | 3.689 |
| utilisation (used / allocatable) | 0.1111 | 0.1086 |
| CPU used (cores), mean | 2.667 | 2.607 |
| Omni's own CPU (cores), mean | 0 | 0.0097 |
| CPU used with Omni's own (cores), mean | 2.667 | 2.617 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 295.8 | 303.3 |
| HPA replicas, mean | 9.9 | 13.14 |
| pods started | 6 | 10.33 |
| pod start wait, total (s) | 24.33 | 27.67 |
| pod start wait, mean (s) | 3.942 | 2.369 |
| host CPU busy, the real machine under kind (%) | 75.32 | 74.41 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 3 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.956e-15 to +3.14e-15 | EVEN, the same (under one part in a million) |
| node-hours | 12.02 | 12.02 | +0.1% | -0.009565 to +0.02179 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1393 | 1390 | -0.2% | -5.673 to -1.034 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1393 | 1390 | -0.2% | -5.673 to -1.034 | yes: GAIN |
| response time (ms), mean | 439.9 | 305.6 | -30.5% | -317.4 to +48.87 | no |
| response time (ms), 95th percentile | 1485 | 1235 | -16.8% | -605 to +105.1 | no |
| response time (ms), 99th percentile | 4986 | 4457 | -10.6% | -1718 to +660.7 | no |
| time over the response line (% of samples) | 31 | 21.38 | -31.0% | -27.77 to +8.516 | no |
| failed requests (%) | 18.86 | 15.53 | -17.6% | -10.51 to +3.851 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 83 | 67.67 | -18.5% | -31.11 to +0.4443 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 131.3 | +131 (native is 0) | +72.06 to +190.6 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.65 | 3.689 | +39.2% | -6.93 to +9.008 | no |
| utilisation (used / allocatable) | 0.1111 | 0.1086 | -2.2% | -0.003201 to -0.001783 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.667 | 2.607 | -2.2% | -0.07684 to -0.04279 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0097 | +0.0097 (native is 0) | +0.004251 to +0.01515 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.667 | 2.617 | -1.9% | -0.06171 to -0.03852 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 295.8 | 303.3 | +2.6% | -9.242 to +24.44 | no |
| HPA replicas, mean | 9.9 | 13.14 | +32.7% | -4.992 to +11.47 | no |
| pods started | 6 | 10.33 | +72.2% | -1.404 to +10.07 | no |
| pod start wait, total (s) | 24.33 | 27.67 | +13.7% | -30.4 to +37.06 | no |
| pod start wait, mean (s) | 3.942 | 2.369 | -39.9% | -3.076 to -0.06869 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 75.32 | 74.41 | -1.2% | -1.655 to -0.1771 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.026 | 117 | 97.5% | 0 | 0.78 | yes |
| omni | 2 | long |  |  |  | 0 | 1.015 | 117 | 97.5% | 0 | 1.08 | yes |
| omni | 3 | long |  |  |  | 0 | 1.051 | 120 | 100.0% | 0 | 1.06 | yes |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*