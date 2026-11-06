# Robustness: the governor killed outright mid-run (the lease), real Kubernetes, 10 pairs: the A/B/C confirmation (Omni v3)

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **Confirmed better** or **confirmed WORSE**: all three runs move the same way and every interval is clear of zero. **No difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, losses included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 37716845219 | `bd389c409ad9` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| B | 37716859133 | `bd389c409ad9` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |
| C | 37716872788 | `bd389c409ad9` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 10 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | same |
| node-hours | +0.0% (-0.2 to +0.2) | +0.1% (-0.3 to +0.5) | -0.0% (-0.2 to +0.1) | no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.2% (-0.5 to -0.0) | -0.0% (-0.5 to +0.4) | -0.3% (-0.4 to -0.1) | no difference beyond the noise in 1 of 3 runs |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -0.2% (-0.5 to -0.0) | -0.0% (-0.5 to +0.4) | -0.3% (-0.4 to -0.1) | no difference beyond the noise in 1 of 3 runs |
| response time (ms), mean | -37.3% (-55.8 to -18.8) | -38.5% (-55.0 to -22.0) | -32.3% (-44.8 to -19.9) | **confirmed better** |
| response time (ms), 95th percentile | -44.6% (-86.8 to -2.4) | -43.5% (-79.5 to -7.6) | -42.3% (-75.0 to -9.6) | **confirmed better** |
| response time (ms), 99th percentile | -12.4% (-46.4 to +21.6) | -18.8% (-55.3 to +17.7) | -2.0% (-50.8 to +46.8) | no difference beyond the noise (all three runs) |
| time over the response line (% of samples) | -32.8% (-47.3 to -18.3) | -27.5% (-37.6 to -17.4) | -34.3% (-51.6 to -17.1) | **confirmed better** |
| failed requests (%) | -12.7% (-20.8 to -4.7) | -8.5% (-15.4 to -1.5) | -14.5% (-27.5 to -1.6) | **confirmed better** |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | -50.6% (-127.6 to +26.3) | -2.9% (-129.5 to +123.8) | -25.6% (-116.7 to +65.6) | shown, not judged |
| utilisation (used / allocatable) | -1.7% (-2.4 to -1.0) | -1.1% (-1.9 to -0.4) | -1.8% (-2.4 to -1.1) | shown, not judged |
| CPU used (cores), mean | -1.7% (-2.4 to -1.0) | -1.1% (-1.9 to -0.4) | -1.8% (-2.4 to -1.1) | shown, not judged |
| Omni's own CPU (cores), mean | +0.0134 (+0.01215 to +0.01465) | +0.01314 (+0.01221 to +0.01407) | +0.01256 (+0.01132 to +0.0138) | shown, not judged |
| CPU used with Omni's own (cores), mean | -1.2% (-1.9 to -0.5) | -0.6% (-1.4 to +0.1) | -1.2% (-1.9 to -0.5) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +1.7% (-0.0 to +3.5) | +1.3% (+0.3 to +2.3) | +1.8% (+0.9 to +2.6) | shown, not judged |
| HPA replicas, mean | -0.5% (-1.7 to +0.7) | +1.1% (+0.3 to +2.0) | +0.6% (-0.3 to +1.4) | no difference beyond the noise in 2 of 3 runs |
| pods started | -2.4% (-27.7 to +22.8) | -20.0% (-41.8 to +1.8) | -9.1% (-25.6 to +7.4) | no difference beyond the noise (all three runs) |
| pod start wait, total (s) | -7.8% (-53.8 to +38.1) | -40.6% (-90.1 to +9.0) | -3.1% (-56.5 to +50.3) | no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | -2.1% (-38.4 to +34.2) | -24.8% (-61.6 to +12.1) | -6.6% (-51.0 to +37.8) | no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | -0.5% (-1.3 to +0.3) | -0.7% (-1.4 to +0.0) | -1.0% (-1.7 to -0.3) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| robust: failed requests in the 120 s after the kill (%) | -2.7% (-17.5 to +12.1) | +9.5% (-4.9 to +23.9) | -9.0% (-30.6 to +12.7) | no difference beyond the noise (all three runs) |
| robust: time over the line in the 120 s after the kill (% of samples) | -1.5% (-7.6 to +4.5) | -1.9% (-11.0 to +7.1) | +0.2% (-8.9 to +9.3) | no difference beyond the noise (all three runs) |
| robust: every setting back at the operator's within 60 s of the kill, every repetition (the governor killed outright; the watchdog's hand-back) | yes (10 reps; mean 9 s, max 11 s) | yes (10 reps; mean 9 s, max 11 s) | yes (10 reps; mean 9 s, max 11 s) | **confirmed: handed back within the allowance in every repetition of every run** |
| robust: a second governor started after the hand-back and governed to the end, every repetition | yes | yes | yes | **confirmed** |

Readings: 4 confirmed better, 1 confirmed, 1 confirmed: handed back within the allowance in every repetition of every run, 7 no difference beyond the noise (all three runs), 2 no difference beyond the noise in 1 of 3 runs, 1 no difference beyond the noise in 2 of 3 runs, 3 same, 8 shown, not judged.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
