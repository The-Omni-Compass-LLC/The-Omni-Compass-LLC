# Steady load: the same fixed-rate work sent to both arms: the A/B/C confirmation (Omni v3)

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **Confirmed better** or **confirmed WORSE**: all three runs move the same way and every interval is clear of zero. **No difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, losses included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 37568428903 | `69f027ec9387` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| B | 37573736336 | `6aea248b01ec` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| C | 37578883344 | `3edcfb68a6c6` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -1.7% (-2.1 to -1.2) | -2.9% (-4.9 to -0.9) | -1.5% (-2.0 to -0.9) | **confirmed better** |
| node-hours | -1.6% (-2.4 to -0.9) | -2.7% (-4.9 to -0.6) | -1.5% (-2.1 to -0.9) | **confirmed better** |
| energy, parked workers still on at idle power (Wh, declared model) | -0.2% (-0.9 to +0.5) | -0.0% (-0.3 to +0.3) | -0.3% (-0.4 to -0.1) | no difference beyond the noise in 2 of 3 runs |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -1.4% (-2.1 to -0.7) | -2.1% (-3.6 to -0.6) | -1.3% (-1.8 to -0.8) | **confirmed better** |
| response time (ms), mean | -48.2% (-64.0 to -32.5) | -46.7% (-63.0 to -30.4) | -47.6% (-59.7 to -35.5) | **confirmed better** |
| response time (ms), 95th percentile | -65.5% (-85.5 to -45.4) | -65.2% (-86.2 to -44.2) | -64.8% (-81.0 to -48.5) | **confirmed better** |
| response time (ms), 99th percentile | -71.7% (-97.0 to -46.4) | -67.5% (-90.0 to -45.1) | -68.0% (-84.1 to -51.8) | **confirmed better** |
| time over the response line (% of samples) | -99.3% (-180.6 to -18.1) | -99.1% (-191.7 to -6.5) | -97.1% (-160.8 to -33.3) | **confirmed better** |
| failed requests (%) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +6.8% (-63.3 to +76.9) | -28.6% (-64.5 to +7.4) | -14.3% (-67.3 to +38.7) | shown, not judged |
| utilisation (used / allocatable) | -3.3% (-6.7 to +0.0) | -1.9% (-5.5 to +1.7) | -3.0% (-5.7 to -0.2) | shown, not judged |
| CPU used (cores), mean | -4.9% (-8.4 to -1.4) | -4.5% (-7.9 to -1.1) | -4.4% (-7.3 to -1.5) | shown, not judged |
| Omni's own CPU (cores), mean | +0.0098 (+0.008469 to +0.01113) | +0.00949 (+0.008148 to +0.01083) | +0.00968 (+0.008418 to +0.01094) | shown, not judged |
| CPU used with Omni's own (cores), mean | -3.8% (-7.3 to -0.4) | -3.4% (-6.7 to -0.1) | -3.3% (-6.1 to -0.6) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +2.4% (-0.1 to +4.9) | +1.0% (-1.9 to +3.9) | +2.0% (-0.9 to +5.0) | shown, not judged |
| HPA replicas, mean | -3.8% (-7.5 to -0.1) | -4.4% (-10.4 to +1.6) | -7.4% (-11.2 to -3.6) | no difference beyond the noise in 1 of 3 runs |
| pods started | -6.7% (-27.9 to +14.6) | -18.5% (-39.2 to +2.2) | -8.7% (-33.2 to +15.8) | no difference beyond the noise (all three runs) |
| pod start wait, total (s) | -11.1% (-53.0 to +30.8) | -30.4% (-63.8 to +3.1) | -14.8% (-58.2 to +28.6) | no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | -7.3% (-39.9 to +25.2) | -21.4% (-45.4 to +2.5) | -5.3% (-37.9 to +27.3) | no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | -3.0% (-6.2 to +0.1) | -2.5% (-5.5 to +0.5) | -2.8% (-5.3 to -0.3) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 7 confirmed better, 3 no difference beyond the noise (all three runs), 1 no difference beyond the noise in 1 of 3 runs, 1 no difference beyond the noise in 2 of 3 runs, 3 same, 8 shown, not judged.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
