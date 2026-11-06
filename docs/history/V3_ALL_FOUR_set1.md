# All four in one run: more work, faster, fewer machines, less energy (load rising 1 to 8 and back): the A/B/C confirmation (Omni v3)

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **Confirmed better** or **confirmed WORSE**: all three runs move the same way and every interval is clear of zero. **No difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, losses included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 37568440904 | `69f027ec9387` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| B | 37578875988 | `3edcfb68a6c6` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| C | 37583092384 | `03cef9868c3e` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| work inside the response line (requests a second; the capacity test's own gauge, higher is better) | +48.6% (+38.7 to +58.4) | +43.8% (+32.2 to +55.3) | +34.9% (+26.1 to +43.7) | **confirmed better** |
| worker nodes in service, mean | -1.8% (-5.1 to +1.6) | -1.7% (-5.0 to +1.6) | -2.5% (-5.8 to +0.8) | no difference beyond the noise (all three runs) |
| node-hours | -1.7% (-5.0 to +1.7) | -1.8% (-5.0 to +1.4) | -2.4% (-5.7 to +0.8) | no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.3% (-0.5 to -0.1) | -0.3% (-0.5 to -0.0) | -0.0% (-0.3 to +0.2) | no difference beyond the noise in 1 of 3 runs |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -1.4% (-3.7 to +0.9) | -1.4% (-3.4 to +0.6) | -1.7% (-3.9 to +0.5) | no difference beyond the noise (all three runs) |
| response time (ms), mean | -46.1% (-58.3 to -34.0) | -45.4% (-57.3 to -33.6) | -45.2% (-63.1 to -27.3) | **confirmed better** |
| response time (ms), 95th percentile | -61.6% (-74.8 to -48.4) | -61.1% (-76.6 to -45.5) | -65.8% (-94.6 to -37.0) | **confirmed better** |
| response time (ms), 99th percentile | -40.0% (-71.8 to -8.2) | -40.1% (-60.3 to -20.0) | -32.1% (-79.6 to +15.4) | no difference beyond the noise in 1 of 3 runs |
| time over the response line (% of samples) | -45.5% (-61.0 to -30.0) | -39.1% (-52.7 to -25.4) | -41.3% (-64.4 to -18.2) | **confirmed better** |
| failed requests (%) | -13.8% (-23.0 to -4.7) | -12.1% (-19.5 to -4.7) | -10.8% (-21.0 to -0.6) | **confirmed better** |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +10.9% (-44.4 to +66.3) | -6.5% (-56.4 to +43.4) | -3.2% (-58.5 to +52.2) | shown, not judged |
| utilisation (used / allocatable) | -1.9% (-3.4 to -0.3) | -0.7% (-3.0 to +1.6) | +0.3% (-2.0 to +2.6) | shown, not judged |
| CPU used (cores), mean | -3.0% (-4.1 to -1.9) | -1.8% (-2.4 to -1.1) | -1.7% (-3.2 to -0.1) | shown, not judged |
| Omni's own CPU (cores), mean | +0.00885 (+0.00754 to +0.01016) | +0.00909 (+0.007768 to +0.01041) | +0.00796 (+0.006568 to +0.009352) | shown, not judged |
| CPU used with Omni's own (cores), mean | -2.6% (-3.8 to -1.5) | -1.4% (-2.1 to -0.7) | -1.3% (-2.9 to +0.2) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +2.1% (-0.1 to +4.4) | -0.1% (-3.5 to +3.3) | -0.4% (-2.7 to +1.9) | shown, not judged |
| HPA replicas, mean | -2.5% (-3.3 to -1.6) | -1.2% (-3.2 to +0.7) | -3.5% (-7.5 to +0.5) | no difference beyond the noise in 2 of 3 runs |
| pods started | +8.3% (-10.5 to +27.2) | -17.4% (-36.5 to +1.7) | -1.9% (-17.7 to +14.0) | no difference beyond the noise (all three runs) |
| pod start wait, total (s) | +6.0% (-28.7 to +40.7) | -31.0% (-65.8 to +3.9) | +7.7% (-28.8 to +44.3) | no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | +1.9% (-29.9 to +33.7) | -19.1% (-47.5 to +9.3) | +6.3% (-23.2 to +35.9) | no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | -2.5% (-3.6 to -1.3) | -1.1% (-1.6 to -0.7) | -1.2% (-2.7 to +0.2) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |

Readings: 5 confirmed better, 6 no difference beyond the noise (all three runs), 2 no difference beyond the noise in 1 of 3 runs, 1 no difference beyond the noise in 2 of 3 runs, 2 same, 8 shown, not judged.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
