# Faults: a machine down, a spike, a runaway pod, a blind probe: the A/B/C confirmation (Omni v3)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **Confirmed better** or **confirmed WORSE**: all three runs move the same way and every interval is clear of zero. **No difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, losses included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 37568453602 | `69f027ec9387` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| B | 37573751219 | `6aea248b01ec` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| C | 37578899103 | `3edcfb68a6c6` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -1.1% (-3.6 to +1.5) | -0.3% (-0.6 to +0.1) | -0.1% (-0.4 to +0.2) | no difference beyond the noise (all three runs) |
| node-hours | -1.2% (-3.7 to +1.4) | -0.3% (-0.8 to +0.2) | +0.1% (-0.4 to +0.6) | no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.2% (-0.7 to +0.4) | -0.2% (-0.8 to +0.5) | +0.1% (-0.5 to +0.6) | no difference beyond the noise (all three runs) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -0.9% (-2.7 to +0.8) | -0.3% (-0.9 to +0.2) | -0.0% (-0.5 to +0.5) | no difference beyond the noise (all three runs) |
| response time (ms), mean | -36.8% (-64.4 to -9.2) | -40.8% (-70.5 to -11.1) | -50.8% (-71.5 to -30.0) | **confirmed better** |
| response time (ms), 95th percentile | -58.7% (-70.7 to -46.8) | -46.7% (-71.5 to -22.0) | -61.7% (-72.4 to -51.1) | **confirmed better** |
| response time (ms), 99th percentile | -39.4% (-69.1 to -9.6) | -45.9% (-60.9 to -30.9) | -62.5% (-88.9 to -36.1) | **confirmed better** |
| time over the response line (% of samples) | -33.6% (-47.2 to -20.0) | -22.4% (-40.0 to -4.9) | -41.7% (-58.5 to -24.9) | **confirmed better** |
| failed requests (%) | -14.4% (-26.3 to -2.6) | -7.3% (-23.1 to +8.5) | -7.1% (-21.2 to +7.0) | no difference beyond the noise in 2 of 3 runs |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -6.0% (-132.3 to +120.3) | +41.9% (-95.4 to +179.1) | +24.3% (-30.7 to +79.2) | shown, not judged |
| utilisation (used / allocatable) | -0.5% (-4.1 to +3.1) | -0.7% (-2.9 to +1.6) | -1.4% (-4.0 to +1.2) | shown, not judged |
| CPU used (cores), mean | -1.4% (-4.3 to +1.5) | -0.9% (-3.0 to +1.3) | -1.5% (-4.1 to +1.1) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00846 (+0.007346 to +0.009574) | +0.00912 (+0.008378 to +0.009862) | +0.00812 (+0.006961 to +0.009279) | shown, not judged |
| CPU used with Omni's own (cores), mean | -0.8% (-3.7 to +2.1) | -0.3% (-2.4 to +1.8) | -1.0% (-3.5 to +1.6) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -0.8% (-4.5 to +2.9) | +0.1% (-2.0 to +2.1) | +1.0% (-1.1 to +3.1) | shown, not judged |
| HPA replicas, mean | -1.5% (-5.0 to +2.1) | -0.1% (-4.1 to +3.9) | -1.4% (-3.2 to +0.5) | no difference beyond the noise (all three runs) |
| pods started | +8.9% (-21.3 to +39.0) | -12.2% (-39.9 to +15.5) | -3.8% (-9.5 to +1.9) | no difference beyond the noise (all three runs) |
| pod start wait, total (s) | +2.5% (-124.0 to +128.9) | +15.3% (-108.8 to +139.5) | -13.5% (-27.1 to +0.2) | no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | -8.8% (-128.7 to +111.0) | +27.7% (-102.0 to +157.3) | -13.4% (-27.6 to +0.8) | no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | -0.4% (-2.3 to +1.6) | -0.1% (-1.9 to +1.6) | -1.0% (-3.1 to +1.1) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 4 confirmed better, 8 no difference beyond the noise (all three runs), 1 no difference beyond the noise in 2 of 3 runs, 2 same, 8 shown, not judged.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
