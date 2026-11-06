# Fairness: a noisy neighbour on the same workers: the A/B/C confirmation (Omni v3)

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **Confirmed better** or **confirmed WORSE**: all three runs move the same way and every interval is clear of zero. **No difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, losses included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 37568447257 | `69f027ec9387` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| B | 37573744350 | `6aea248b01ec` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| C | 37578890876 | `3edcfb68a6c6` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -0.1% (-0.4 to +0.1) | -0.1% (-0.4 to +0.1) | -0.0% (-0.0 to +0.0) | no difference beyond the noise (all three runs) |
| node-hours | -0.2% (-0.5 to +0.2) | -0.1% (-0.4 to +0.2) | -0.0% (-0.2 to +0.2) | no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.0% (-0.4 to +0.3) | -0.2% (-0.3 to -0.0) | -0.0% (-0.3 to +0.3) | no difference beyond the noise in 2 of 3 runs |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -0.1% (-0.5 to +0.3) | -0.2% (-0.5 to +0.0) | -0.0% (-0.3 to +0.3) | no difference beyond the noise (all three runs) |
| response time (ms), mean | -7.2% (-20.5 to +6.0) | -11.0% (-19.0 to -3.0) | -3.2% (-14.3 to +7.8) | no difference beyond the noise in 2 of 3 runs |
| response time (ms), 95th percentile | -0.3% (-25.5 to +24.9) | -3.6% (-14.7 to +7.5) | +10.8% (-2.8 to +24.3) | no difference beyond the noise (all three runs) |
| response time (ms), 99th percentile | +10.5% (-7.5 to +28.5) | +3.0% (-15.6 to +21.7) | +13.0% (+2.1 to +24.0) | no difference beyond the noise in 2 of 3 runs |
| time over the response line (% of samples) | -7.1% (-16.2 to +1.9) | -8.5% (-17.7 to +0.7) | -1.6% (-16.1 to +12.9) | no difference beyond the noise (all three runs) |
| failed requests (%) | -16.5% (-54.7 to +21.6) | -13.9% (-36.6 to +8.8) | -30.0% (-62.1 to +2.1) | no difference beyond the noise (all three runs) |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +21.4% (-49.7 to +92.4) | +77.7% (-1.3 to +156.7) | +61.5% (-11.4 to +134.5) | shown, not judged |
| utilisation (used / allocatable) | -0.4% (-1.6 to +0.7) | -1.3% (-1.8 to -0.8) | -0.1% (-2.1 to +1.8) | shown, not judged |
| CPU used (cores), mean | -0.5% (-1.6 to +0.5) | -1.4% (-2.0 to -0.7) | -0.1% (-2.1 to +1.8) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01274 (+0.01021 to +0.01527) | +0.01451 (+0.01214 to +0.01688) | +0.01362 (+0.01131 to +0.01593) | shown, not judged |
| CPU used with Omni's own (cores), mean | +0.1% (-0.9 to +1.0) | -0.8% (-1.5 to -0.1) | +0.5% (-1.5 to +2.4) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +0.1% (-0.8 to +1.1) | +1.4% (+0.3 to +2.5) | +0.0% (-2.0 to +2.0) | shown, not judged |
| HPA replicas, mean | -1.0% (-2.4 to +0.4) | +1.3% (-1.4 to +4.0) | -0.4% (-2.9 to +2.1) | no difference beyond the noise (all three runs) |
| pods started | -2.1% (-20.3 to +16.1) | -31.1% (-60.3 to -1.9) | -7.8% (-34.5 to +18.8) | no difference beyond the noise in 2 of 3 runs |
| pod start wait, total (s) | +28.6% (-1.0 to +58.2) | +6.5% (-70.6 to +83.6) | -12.0% (-36.8 to +12.7) | no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | +22.7% (-13.2 to +58.6) | +29.7% (-17.6 to +76.9) | -12.0% (-32.0 to +7.9) | no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | +0.4% (-0.5 to +1.3) | -0.6% (-1.5 to +0.3) | +0.9% (-0.5 to +2.4) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| second app: response time (ms), 95th percentile | -8.7% (-60.0 to +42.6) | +6.6% (-4.7 to +17.9) | +20.9% (-56.8 to +98.7) | no difference beyond the noise (all three runs) |
| second app: response time (ms), 99th percentile | -19.5% (-79.9 to +40.9) | +57.0% (-45.9 to +160.0) | +2.5% (-56.5 to +61.4) | no difference beyond the noise (all three runs) |
| second app: time over the response line (% of samples) | +0.2% (-6.4 to +6.7) | -0.0% (-4.5 to +4.4) | +0.1% (-6.3 to +6.4) | no difference beyond the noise (all three runs) |
| second app: failed requests (%) | +1.5% (-3.1 to +6.1) | -2.3% (-4.5 to +0.0) | +5.1% (-3.2 to +13.5) | no difference beyond the noise (all three runs) |

Readings: 13 no difference beyond the noise (all three runs), 4 no difference beyond the noise in 2 of 3 runs, 2 same, 8 shown, not judged.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
