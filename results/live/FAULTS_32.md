# The fault test on kind, set 32 F: run again under the amendment of 2026-10-03 evening, 10 paired repetitions

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Source: GitHub Actions workflow `benchmark-reps` (`faults` 1, arms native / omni / compass, order rotated, 900 measured
seconds per arm, open-loop load), run 37162459956, commit `199f350`, 2026-10-04, job `aggregate` (job 111327606574).
Transcribed from the job's printed receipt; artifact `live-reps` (zip SHA-256
`6ee05b4889a9690ab3252488e5917f545a651a079edcf44ae2a6201e415c464d`). The same four faults at the same moments of every
arm (`scripts/kind_faults.sh`). Evidence class **L**.

**Result. No measure is significantly behind native under either law.** The amendment leaves the fault behaviour
intact (set 31 F, `FAULTS_31.md`): the compass law recovers from a lost machine 58% faster, starts 34% fewer pods, and
cuts the 95th percentile by 61%, failed requests by 12.9% and time over the line by 27.6%. The 99th percentile reads
higher in both arms with intervals far across zero, as in set 31 F.

## Recovery from each fault

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 98 | 16.0 |  |
| machine down | omni | 45 | 9.1 | -53 s (-54%) |
| machine down | compass | 41 | 9.8 | -57 s (-58%) |
| spike | native | 277 | 68.7 |  |
| spike | omni | 256 | 45.7 | -21 s (-8%) |
| spike | compass | 269 | 65.8 | -8 s (-3%) |
| runaway pod started | native | 130 | 11.7 |  |
| runaway pod started | omni | 82 | 5.6 | -48 s (-37%) |
| runaway pod started | compass | 116 | 9.7 | -14 s (-11%) |
| probe blind | native | 62 | 0.1 |  |
| probe blind | omni | 60 | 0.1 | -2 s (-3%) |
| probe blind | compass | 60 | 0.1 | -2 s (-4%) |

## B: the allocation law vs native, whole run with the faults

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.914 | 5.624 | -4.9% | -0.7601 to +0.1809 | no |
| node-hours | 1.498 | 1.425 | -4.9% | -0.1939 to +0.0465 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 167.1 | 166.2 | -0.5% | -1.274 to -0.4633 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 165.4 | 159.1 | -3.9% | -15.17 to +2.426 | no |
| response time (ms), mean | 203.6 | 135.9 | -33.3% | -90.43 to -45.04 | yes: GAIN |
| response time (ms), 95th percentile | 417.9 | 150.7 | -63.9% | -310 to -224.4 | yes: GAIN |
| response time (ms), 99th percentile | 936.9 | 1017 | +8.6% | -750.2 to +910.9 | no |
| time over the response line (% of samples) | 8.648 | 5.19 | -40.0% | -4.202 to -2.714 | yes: GAIN |
| failed requests (%) | 5.595 | 4.265 | -23.8% | -2.104 to -0.5556 | yes: GAIN |
| pending pods, pod-minutes | 0.6717 | 0.36 | -46.4% | -1.044 to +0.4206 | no |
| utilisation (used / allocatable) | 0.07428 | 0.07344 | -1.1% | -0.007099 to +0.005415 | no |
| CPU used (cores), mean | 1.757 | 1.661 | -5.5% | -0.1281 to -0.06366 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01907 | +0.0191 (native is 0) | +0.01664 to +0.0215 | yes: power given |
| CPU used with Omni's own (cores), mean | 1.757 | 1.68 | -4.4% | -0.1079 to -0.04577 | yes: GAIN |
| energy per core-hour (Wh, the 25 W standby model) | 380.8 | 381.4 | +0.2% | -30.82 to +32.05 | no |
| HPA replicas, mean | 8.962 | 9.267 | +3.4% | -0.08126 to +0.6906 | no |
| pods started | 4.1 | 2.4 | -41.5% | -3.21 to -0.1901 | yes: GAIN |
| pod start wait, total (s) | 26.9 | 5.1 | -81.0% | -45.33 to +1.726 | no |
| pod start wait, mean (s) | 5.841 | 1.511 | -74.1% | -9.464 to +0.8035 | no |

## B with the compass law vs native, whole run with the faults

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.914 | 5.908 | -0.1% | -0.02353 to +0.01182 | no |
| node-hours | 1.498 | 1.492 | -0.4% | -0.01752 to +0.004077 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 167.1 | 166.2 | -0.5% | -1.56 to -0.09146 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 165.4 | 164.5 | -0.6% | -1.842 to -0.01792 | yes: GAIN |
| response time (ms), mean | 203.6 | 153 | -24.9% | -101.8 to +0.5159 | no |
| response time (ms), 95th percentile | 417.9 | 162.2 | -61.2% | -295.4 to -216 | yes: GAIN |
| response time (ms), 99th percentile | 936.9 | 1059 | +13.1% | -400.1 to +644.9 | no |
| time over the response line (% of samples) | 8.648 | 6.265 | -27.6% | -3.235 to -1.531 | yes: GAIN |
| failed requests (%) | 5.595 | 4.874 | -12.9% | -1.154 to -0.2864 | yes: GAIN |
| pending pods, pod-minutes | 0.6717 | 0.23 | -65.8% | -1.13 to +0.2462 | no |
| utilisation (used / allocatable) | 0.07428 | 0.07328 | -1.3% | -0.003161 to +0.001162 | no |
| CPU used (cores), mean | 1.757 | 1.733 | -1.4% | -0.07451 to +0.02529 | no |
| Omni's own CPU (cores), mean | 0 | 0.00969 | +0.00969 (native is 0) | +0.009102 to +0.01028 | yes: power given |
| CPU used with Omni's own (cores), mean | 1.757 | 1.742 | -0.8% | -0.06477 to +0.03493 | no |
| energy per core-hour (Wh, the 25 W standby model) | 380.8 | 384 | +0.9% | -6.41 to +12.96 | no |
| HPA replicas, mean | 8.962 | 9.15 | +2.1% | -0.164 to +0.5386 | no |
| pods started | 4.1 | 2.7 | -34.1% | -2.757 to -0.0428 | yes: GAIN |
| pod start wait, total (s) | 26.9 | 8.5 | -68.4% | -43.92 to +7.116 | no |
| pod start wait, mean (s) | 5.841 | 2.136 | -63.4% | -9.057 to +1.647 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
