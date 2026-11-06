# Wandering demand: load that steps up and down by one (1 2 3 2 3 4 5 6 5 4 5 6 7 8 7 6 5 4 3 4 3 2 1 2 1): the A/B/C confirmation (Omni v3)

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **Confirmed better** or **confirmed WORSE**: all three runs move the same way and every interval is clear of zero. **No difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, losses included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 37568434811 | `69f027ec9387` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| B | 37578868385 | `3edcfb68a6c6` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| C | 37583079914 | `03cef9868c3e` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -0.5% (-1.3 to +0.4) | -1.9% (-5.2 to +1.4) | -3.5% (-7.9 to +0.8) | no difference beyond the noise (all three runs) |
| node-hours | -0.5% (-1.3 to +0.4) | -1.8% (-5.1 to +1.4) | -3.4% (-7.8 to +1.0) | no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.3% (-0.4 to -0.1) | -0.1% (-0.3 to +0.1) | -0.0% (-0.3 to +0.3) | no difference beyond the noise in 2 of 3 runs |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -0.6% (-1.2 to +0.0) | -1.4% (-3.4 to +0.6) | -2.4% (-5.4 to +0.6) | no difference beyond the noise (all three runs) |
| response time (ms), mean | -47.7% (-59.7 to -35.7) | -48.8% (-67.0 to -30.6) | -46.2% (-62.1 to -30.2) | **confirmed better** |
| response time (ms), 95th percentile | -62.7% (-75.6 to -49.8) | -63.1% (-91.4 to -34.8) | -57.2% (-73.5 to -41.0) | **confirmed better** |
| response time (ms), 99th percentile | -40.1% (-70.4 to -9.9) | -45.7% (-69.7 to -21.7) | -50.8% (-86.6 to -15.1) | **confirmed better** |
| time over the response line (% of samples) | -38.8% (-49.5 to -28.2) | -39.9% (-54.8 to -24.9) | -38.7% (-55.4 to -21.9) | **confirmed better** |
| failed requests (%) | -11.7% (-16.9 to -6.5) | -8.5% (-16.8 to -0.1) | -9.9% (-18.4 to -1.4) | **confirmed better** |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -6.5% (-61.8 to +48.7) | +7.2% (-95.7 to +110.1) | +5.9% (-72.9 to +84.8) | shown, not judged |
| utilisation (used / allocatable) | -1.8% (-2.3 to -1.4) | -0.7% (-3.5 to +2.2) | +0.5% (-2.3 to +3.4) | shown, not judged |
| CPU used (cores), mean | -2.1% (-2.5 to -1.8) | -1.9% (-2.7 to -1.1) | -1.7% (-3.5 to +0.2) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00975 (+0.008677 to +0.01082) | +0.00912 (+0.007949 to +0.01029) | +0.0086 (+0.007269 to +0.009931) | shown, not judged |
| CPU used with Omni's own (cores), mean | -1.7% (-2.1 to -1.4) | -1.5% (-2.3 to -0.7) | -1.3% (-3.1 to +0.5) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +1.8% (+1.1 to +2.6) | -0.3% (-4.5 to +3.9) | -1.4% (-4.2 to +1.4) | shown, not judged |
| HPA replicas, mean | -0.2% (-1.7 to +1.3) | -1.6% (-3.3 to +0.1) | -0.7% (-2.8 to +1.4) | no difference beyond the noise (all three runs) |
| pods started | -32.6% (-62.1 to -3.0) | +0.0% (-30.0 to +30.0) | -25.0% (-56.4 to +6.4) | no difference beyond the noise in 2 of 3 runs |
| pod start wait, total (s) | -32.3% (-66.2 to +1.6) | -1.4% (-60.9 to +58.0) | -24.9% (-62.7 to +12.9) | no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | -22.9% (-49.9 to +4.1) | -4.4% (-50.6 to +41.9) | -23.8% (-50.1 to +2.5) | no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | -1.8% (-2.0 to -1.6) | -1.0% (-2.1 to +0.0) | -1.0% (-2.7 to +0.7) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 5 confirmed better, 6 no difference beyond the noise (all three runs), 2 no difference beyond the noise in 2 of 3 runs, 2 same, 8 shown, not judged.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
