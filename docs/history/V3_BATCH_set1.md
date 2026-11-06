# Batch queue: 240 CPU jobs, cruise and the emergency brake: the A/B/C confirmation (Omni v3)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **Confirmed better** or **confirmed WORSE**: all three runs move the same way and every interval is clear of zero. **No difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, losses included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 37568459663 | `69f027ec9387` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| B | 37573759437 | `6aea248b01ec` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| C | 37581021752 | `d1bea5a6ebc4` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -18.5% (-26.5 to -10.5) | -20.2% (-26.1 to -14.4) | -22.7% (-28.3 to -17.1) | **confirmed better** |
| node-hours | -18.4% (-26.6 to -10.3) | -20.3% (-26.0 to -14.7) | -22.5% (-28.2 to -16.7) | **confirmed better** |
| energy, parked workers still on at idle power (Wh, declared model) | +0.1% (-0.2 to +0.4) | -0.1% (-0.4 to +0.2) | -0.1% (-0.6 to +0.5) | no difference beyond the noise (all three runs) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -12.7% (-18.4 to -7.1) | -14.0% (-17.9 to -10.1) | -15.8% (-19.8 to -11.8) | **confirmed better** |
| response time (ms), mean | -11.9% (-16.1 to -7.6) | -10.3% (-12.9 to -7.6) | -13.7% (-18.7 to -8.8) | **confirmed better** |
| response time (ms), 95th percentile | -2.4% (-6.7 to +2.0) | -0.7% (-4.6 to +3.3) | -5.0% (-9.3 to -0.8) | no difference beyond the noise in 2 of 3 runs |
| response time (ms), 99th percentile | -0.8% (-7.5 to +5.8) | +0.2% (-4.7 to +5.2) | -2.8% (-8.3 to +2.7) | no difference beyond the noise (all three runs) |
| time over the response line (% of samples) | -3.8% (-6.4 to -1.2) | -3.6% (-7.2 to -0.1) | -2.4% (-4.6 to -0.1) | **confirmed better** |
| failed requests (%) | -100.0% (-326.2 to +126.2) | -100.0% (-326.2 to +126.2) | +0 (+0 to +0) | no difference beyond the noise (all three runs) |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +1.8% (-1.1 to +4.7) | +0.1% (-2.4 to +2.5) | +1.1% (-2.0 to +4.2) | shown, not judged |
| utilisation (used / allocatable) | +20.9% (+11.2 to +30.6) | +23.8% (+18.0 to +29.6) | +21.2% (+13.0 to +29.5) | shown, not judged |
| CPU used (cores), mean | -1.3% (-3.8 to +1.1) | -1.0% (-3.3 to +1.2) | -5.9% (-10.2 to -1.6) | shown, not judged |
| Omni's own CPU (cores), mean | +0.01917 (+0.01666 to +0.02168) | +0.02 (+0.01689 to +0.02311) | +0.0191 (+0.01583 to +0.02237) | shown, not judged |
| CPU used with Omni's own (cores), mean | +0.0% (-2.4 to +2.4) | +0.3% (-2.0 to +2.6) | -4.6% (-8.9 to -0.2) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | -13.0% (-22.1 to -4.0) | -13.4% (-18.0 to -8.7) | -10.9% (-18.2 to -3.7) | shown, not judged |
| HPA replicas, mean | -1.9% (-15.9 to +12.1) | -2.0% (-13.0 to +8.9) | +8.3% (-3.7 to +20.3) | no difference beyond the noise (all three runs) |
| pods started | +0 (+0 to +0) | +0 (+0 to +0) | +200.0% (-252.4 to +652.4) | no difference beyond the noise (all three runs) |
| pod start wait, total (s) | +0 (+0 to +0) | +0 (+0 to +0) | +129.3% (-255.6 to +514.2) | no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | +0 (+0 to +0) | +0 (+0 to +0) | +129.3% (-255.6 to +514.2) | no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | +1.8% (+0.2 to +3.4) | +1.5% (+0.4 to +2.6) | +1.1% (-0.4 to +2.5) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| batch: queue finished (s) | +0.4% (-1.5 to +2.3) | -0.1% (-0.7 to +0.4) | -0.0% (-1.7 to +1.7) | no difference beyond the noise (all three runs) |
| batch: worker machines in service after the queue finished, mean | -28.5% (-38.9 to -18.1) | -32.6% (-39.9 to -25.4) | -35.4% (-41.8 to -28.9) | **confirmed better** |

Readings: 6 confirmed better, 8 no difference beyond the noise (all three runs), 1 no difference beyond the noise in 2 of 3 runs, 2 same, 8 shown, not judged.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
