# A public day of demand: the Google cluster trace of 2011 replayed one step at a time (2 3 3 3 3 4 4 3 2 2 2 2 2 3 2 3 4 4 3 4 5 6 5 4): the A/B/C confirmation (Omni v3)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **Confirmed better** or **confirmed WORSE**: all three runs move the same way and every interval is clear of zero. **No difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, losses included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 37826513664 | `13ee69e8216e` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| B | 37826518868 | `13ee69e8216e` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| C | 37826522419 | `13ee69e8216e` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -9.5% (-16.1 to -2.9) | -5.9% (-10.5 to -1.2) | -6.1% (-8.6 to -3.5) | **confirmed better** |
| node-hours | -9.4% (-15.9 to -2.8) | -5.8% (-10.5 to -1.1) | -6.1% (-8.6 to -3.6) | **confirmed better** |
| energy, parked workers still on at idle power (Wh, declared model) | -0.2% (-0.5 to +0.1) | -0.4% (-0.7 to -0.1) | -0.5% (-0.9 to -0.2) | no difference beyond the noise in 1 of 3 runs |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -6.7% (-11.0 to -2.4) | -4.3% (-7.4 to -1.2) | -4.6% (-6.2 to -3.0) | **confirmed better** |
| response time (ms), mean | -51.2% (-73.7 to -28.6) | -52.5% (-68.9 to -36.1) | -54.8% (-78.4 to -31.3) | **confirmed better** |
| response time (ms), 95th percentile | -65.4% (-93.3 to -37.5) | -67.8% (-87.7 to -48.0) | -70.8% (-100.2 to -41.4) | **confirmed better** |
| response time (ms), 99th percentile | -48.9% (-70.0 to -27.7) | -60.9% (-79.2 to -42.6) | -61.0% (-91.2 to -30.9) | **confirmed better** |
| time over the response line (% of samples) | -81.0% (-131.9 to -30.1) | -81.7% (-116.2 to -47.2) | -83.8% (-130.4 to -37.2) | **confirmed better** |
| failed requests (%) | -12.7% (-25.1 to -0.3) | -8.0% (-14.7 to -1.4) | -17.0% (-31.0 to -3.0) | **confirmed better** |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -19.4% (-79.1 to +40.3) | +16.0% (-24.8 to +56.9) | -3.9% (-68.4 to +60.6) | shown, not judged |
| utilisation (used / allocatable) | +3.8% (-2.5 to +10.1) | +0.7% (-3.9 to +5.4) | +0.4% (-2.5 to +3.3) | shown, not judged |
| CPU used (cores), mean | -4.3% (-5.6 to -3.0) | -4.3% (-5.6 to -3.1) | -5.0% (-7.3 to -2.8) | shown, not judged |
| Omni's own CPU (cores), mean | +0.0096 (+0.008135 to +0.01107) | +0.00972 (+0.008417 to +0.01102) | +0.00909 (+0.00756 to +0.01062) | shown, not judged |
| CPU used with Omni's own (cores), mean | -3.7% (-5.0 to -2.5) | -3.8% (-5.0 to -2.7) | -4.5% (-6.7 to -2.4) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -4.8% (-10.7 to +1.0) | -1.4% (-5.7 to +2.9) | -1.0% (-4.1 to +2.0) | shown, not judged |
| HPA replicas, mean | -6.3% (-10.3 to -2.4) | -4.8% (-7.9 to -1.7) | -6.2% (-9.7 to -2.7) | **confirmed better** |
| pods started | +22.6% (-8.3 to +53.4) | +27.3% (+1.8 to +52.7) | +34.6% (+3.7 to +65.6) | no difference beyond the noise in 1 of 3 runs |
| pod start wait, total (s) | -0.9% (-35.7 to +33.9) | -21.0% (-52.9 to +10.9) | +7.9% (-26.8 to +42.6) | no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | -8.3% (-37.8 to +21.2) | -38.3% (-60.3 to -16.3) | -1.3% (-44.4 to +41.8) | no difference beyond the noise in 2 of 3 runs |
| host CPU busy, the real machine under kind (%) | -3.2% (-4.3 to -2.0) | -2.9% (-4.0 to -1.9) | -4.2% (-6.6 to -1.8) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 9 confirmed better, 1 no difference beyond the noise (all three runs), 2 no difference beyond the noise in 1 of 3 runs, 1 no difference beyond the noise in 2 of 3 runs, 2 same, 8 shown, not judged.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
