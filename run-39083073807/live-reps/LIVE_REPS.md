# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.359 |
| node-hours | 2.516 | 2.245 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.2 | 274.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.2 | 254.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 573.4 | 513.4 |
| response time (ms), 95th percentile | 3460 | 3446 |
| response time (ms), 99th percentile | 5044 | 5013 |
| time over the response line (% of samples) | 16.36 | 15.56 |
| failed requests (%) | 0.02139 | 0.01047 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 10.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 196.4 | 202.4 |
| utilisation (used / allocatable) | 0.06456 | 0.07336 |
| CPU used (cores), mean | 1.55 | 1.566 |
| Omni's own CPU (cores), mean | 0 | 0.02221 |
| CPU used with Omni's own (cores), mean | 1.55 | 1.588 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 428.6 | 390.2 |
| HPA replicas, mean | 2.287 | 2.387 |
| pods started | 0.5 | 0.6 |
| pod start wait, total (s) | 13.6 | 7.7 |
| pod start wait, mean (s) | 5.817 | 2.833 |
| host CPU busy, the real machine under kind (%) | 44.48 | 45.3 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 611.3 | 615.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.952 |

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
| worker nodes in service, mean | 6 | 5.359 | -10.7% | -1.125 to -0.1571 | yes: GAIN |
| node-hours | 2.516 | 2.245 | -10.7% | -0.4751 to -0.06558 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.2 | 274.7 | +0.2% | -0.1609 to +1.298 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.2 | 254.6 | -7.1% | -34.78 to -4.387 | yes: GAIN |
| response time (ms), mean | 573.4 | 513.4 | -10.5% | -75.49 to -44.59 | yes: GAIN |
| response time (ms), 95th percentile | 3460 | 3446 | -0.4% | -162.2 to +134.6 | no |
| response time (ms), 99th percentile | 5044 | 5013 | -0.6% | -290.8 to +228.6 | no |
| time over the response line (% of samples) | 16.36 | 15.56 | -4.9% | -1.281 to -0.3283 | yes: GAIN |
| failed requests (%) | 0.02139 | 0.01047 | -51.0% | -0.0671 to +0.04527 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 10.5 | +0.0% | +0 to +0 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.7 | +11.7 (native is 0) | +11.11 to +12.29 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 196.4 | 202.4 | +3.1% | -0.1596 to +12.21 | no |
| utilisation (used / allocatable) | 0.06456 | 0.07336 | +13.6% | +0.002121 to +0.01548 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.55 | 1.566 | +1.0% | -0.02428 to +0.05653 | no |
| Omni's own CPU (cores), mean | 0 | 0.02221 | +0.0222 (native is 0) | +0.01775 to +0.02667 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.55 | 1.588 | +2.5% | -0.002068 to +0.07874 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 428.6 | 390.2 | -9.0% | -75.34 to -1.606 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.287 | 2.387 | +4.4% | -0.2473 to +0.4482 | no |
| pods started | 0.5 | 0.6 | +20.0% | -1.09 to +1.29 | no |
| pod start wait, total (s) | 13.6 | 7.7 | -43.4% | -34.51 to +22.71 | no |
| pod start wait, mean (s) | 5.817 | 2.833 | -51.3% | -14.61 to +8.644 | no |
| host CPU busy, the real machine under kind (%) | 44.48 | 45.3 | +1.8% | +0.4709 to +1.159 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 611.3 | 615.8 | +0.7% | +0.2715 to +8.728 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.952 | -17.5% | -1.769 to -0.3268 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*