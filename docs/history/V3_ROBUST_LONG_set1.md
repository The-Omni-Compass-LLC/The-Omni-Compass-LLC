# Robustness: the long run, 7,200 s an arm, the governor's memory and decisions watched: the A/B/C confirmation (Omni v3)

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Three separate GitHub runs of the same preregistered test on the same frozen engine: A is the result, B and C are the replications. Each cell is omni against native, the paired change in percent of native with its 95% interval. Every judged row gets one of three readings. **Confirmed better** or **confirmed WORSE**: all three runs move the same way and every interval is clear of zero. **No difference beyond the noise**: in the runs counted, the interval includes zero, so native and omni could not be told apart on that measure; that is the result. **The runs disagree**: runs clear of the noise point different ways, so the test itself is unstable there. Every row is shown, losses included.

| Run | GitHub run | Commit | Engine | Paired repetitions |
|---|---|---|---|---:|
| A | 37716886448 | `bd389c409ad9` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 3 |
| B | 37716900258 | `bd389c409ad9` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 3 |
| C | 37716913526 | `bd389c409ad9` | omni-v3 (digest b53d05449ee04c4b, 40 files) | 3 |

| Measure | A | B | C | Reading |
|---|---|---|---|---|
| worker nodes in service, mean | -0.2% (-1.0 to +0.6) | -2.7% (-14.6 to +9.1) | -0.2% (-1.0 to +0.6) | no difference beyond the noise (all three runs) |
| node-hours | -0.2% (-1.1 to +0.6) | -2.8% (-14.5 to +9.0) | -0.2% (-1.1 to +0.7) | no difference beyond the noise (all three runs) |
| energy, parked workers still on at idle power (Wh, declared model) | -0.4% (-1.2 to +0.4) | -0.2% (-0.7 to +0.2) | -0.2% (-0.6 to +0.2) | no difference beyond the noise (all three runs) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | -0.5% (-1.5 to +0.5) | -2.0% (-10.0 to +6.0) | -0.3% (-1.2 to +0.6) | no difference beyond the noise (all three runs) |
| response time (ms), mean | -46.0% (-80.1 to -11.9) | -38.9% (-96.5 to +18.7) | -42.1% (-91.9 to +7.7) | no difference beyond the noise in 2 of 3 runs |
| response time (ms), 95th percentile | -59.1% (-115.7 to -2.5) | -40.3% (-109.3 to +28.7) | -53.8% (-140.7 to +33.2) | no difference beyond the noise in 2 of 3 runs |
| response time (ms), 99th percentile | -30.6% (-46.3 to -15.0) | -13.9% (-29.7 to +1.9) | -21.6% (-55.6 to +12.4) | no difference beyond the noise in 2 of 3 runs |
| time over the response line (% of samples) | -48.5% (-95.9 to -1.1) | -30.2% (-88.3 to +28.0) | -35.2% (-84.4 to +14.1) | no difference beyond the noise in 2 of 3 runs |
| failed requests (%) | -11.2% (-44.2 to +21.7) | -12.7% (-41.3 to +16.0) | -14.0% (-49.1 to +21.2) | no difference beyond the noise (all three runs) |
| pods with no machine to take them (unschedulable) | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| time pods had no machine to take them, pod-minutes | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | same |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | +7.9% (-103.1 to +118.9) | -18.9% (-139.0 to +101.2) | +14.1% (-155.1 to +183.4) | shown, not judged |
| utilisation (used / allocatable) | -2.3% (-6.7 to +2.1) | -0.2% (-3.9 to +3.5) | -1.3% (-4.8 to +2.1) | shown, not judged |
| CPU used (cores), mean | -2.5% (-6.8 to +1.9) | -1.7% (-4.8 to +1.5) | -1.5% (-5.2 to +2.2) | shown, not judged |
| Omni's own CPU (cores), mean | +0.0099 (+nan to +nan) | +0.00825 (-0.008903 to +0.0254) | +0.0095 (+nan to +nan) | shown, not judged |
| CPU used with Omni's own (cores), mean | -2.1% (+nan to +nan) | -1.9% (-13.0 to +9.2) | +0.6% (+nan to +nan) | shown, not judged |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | +2.4% (-2.1 to +7.0) | +0.1% (-1.6 to +1.9) | +1.6% (-2.8 to +6.0) | shown, not judged |
| HPA replicas, mean | -0.1% (-1.0 to +0.7) | -7.2% (-37.6 to +23.2) | -0.2% (-0.5 to +0.1) | no difference beyond the noise (all three runs) |
| pods started | +20.0% (-129.1 to +169.1) | +53.3% (-50.1 to +156.8) | +35.7% (-45.6 to +117.0) | no difference beyond the noise (all three runs) |
| pod start wait, total (s) | +19.6% (-199.3 to +238.5) | +20.4% (-55.6 to +96.4) | +24.1% (-91.7 to +139.8) | no difference beyond the noise (all three runs) |
| pod start wait, mean (s) | -9.6% (-86.6 to +67.4) | -8.2% (-144.6 to +128.3) | +3.4% (-136.0 to +142.8) | no difference beyond the noise (all three runs) |
| host CPU busy, the real machine under kind (%) | -1.7% (-5.6 to +2.2) | -1.2% (-3.7 to +1.4) | -0.9% (-4.0 to +2.2) | shown, not judged |
| host cores (the real machine under kind) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | shown, not judged |
| robust: governor resident memory, mean of the last ten minutes over the first ten, the most over the repetitions | 1.048 | 1.067 | 1.052 | no leak (every repetition under 1.25) |
| robust: decisions made, the fewest repetition's share of the count the configured interval predicts for the window (120) | 97.5% | 97.5% | 97.5% | valid (every repetition at 95% of the expected or more) |
| robust: failed decisions over the whole window (the governor could not read the cluster that second), with the API's own reason | 2 | 3 | 3 | shown, not judged: API 500 for apis/autoscaling/v2/horizontalpodautoscalers; the governor held and resumed |
| robust: the governor's decision time, mean of the last hour over the first (the gap between decisions less the configured interval), the most over the repetitions | 1.20 | 1.14 | 1.07 | no growth beyond the limit (every repetition under 1.5) |
| robust: every setting handed back at the end and read back at the operator's, no record left, every repetition | yes | yes | yes | **confirmed: every setting handed back at the end of every repetition** |

Readings: 1 confirmed: every setting handed back at the end of every repetition, 9 no difference beyond the noise (all three runs), 4 no difference beyond the noise in 2 of 3 runs, 1 no growth beyond the limit (every repetition under 1.5), 1 no leak (every repetition under 1.25), 2 same, 8 shown, not judged, 1 shown, not judged: API 500 for apis/autoscaling/v2/horizontalpodautoscalers; the governor held and resumed, 1 valid (every repetition at 95% of the expected or more).

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
