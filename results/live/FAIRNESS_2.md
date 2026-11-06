# The fairness test, run again under the amendment of 2026-10-03 evening, 10 paired repetitions

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Source: GitHub Actions workflow `benchmark-reps` (`two_app` 1, arms native / omni / compass, order rotated, 900 measured
seconds per arm, open-loop load, the neighbour's load 0, 0, 6, 0, 6, 0 generators), run 37162458834, commit `199f350`,
2026-10-04, job `aggregate` (job 111327654178). Transcribed from the job's printed receipt; artifact `live-reps` (zip
SHA-256 `73bb69ca72e6fec291e184aed577efde60194719a4628c6a44b7aeef36d35451`). Under the amendment only php-apache's HPA
(the service the probe measures, `--sensed default/php-apache`) is moved; the neighbour's stays at the operator's
target. Evidence class **L**.

**Result.** **The compass law's failure problem is gone:** php-apache's failed requests 2.91% against native's
3.38% (−14.0%, not significant; first run +26.0%, significant), pending pods −10.5% (first run +65.2%). **The
neighbour is unharmed** under both laws (no row significant). With the neighbour's HPA left to the operator, the compass
law's response-time gains in this test are no longer significant. **Still higher under both laws: the mean pod start
wait, +1.1 s with the compass law (1.99 to 3.09 s) and +1.7 s with the allocation law.** By the one rule neither arm is
labelled GAIN while that row stands. The allocation law: response times −35% to −45%, time over the line −39%, on
9.1% fewer machines in service.

## B: Omni-Compass on top (the allocation law) vs native

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.455 | -9.1% | -1.017 to -0.07196 | yes: GAIN |
| node-hours | 1.517 | 1.379 | -9.1% | -0.2571 to -0.01922 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 172.5 | 172.7 | +0.1% | -0.573 to +0.9667 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.5 | 162.4 | -5.9% | -19.13 to -1.174 | yes: GAIN |
| response time (ms), mean | 490.8 | 318.6 | -35.1% | -240.5 to -103.9 | yes: GAIN |
| response time (ms), 95th percentile | 2009 | 1104 | -45.1% | -1392 to -417.9 | yes: GAIN |
| response time (ms), 99th percentile | 5133 | 4529 | -11.8% | -2059 to +851.3 | no |
| time over the response line (% of samples) | 22.47 | 13.65 | -39.3% | -12.02 to -5.625 | yes: GAIN |
| failed requests (%) | 3.381 | 2.291 | -32.2% | -2.649 to +0.4704 | no |
| pending pods, pod-minutes | 1.17 | 1.247 | +6.6% | -0.8766 to +1.03 | no |
| utilisation (used / allocatable) | 0.09626 | 0.1074 | +11.6% | +0.002143 to +0.02017 | yes, up (shown, not judged) |
| CPU used (cores), mean | 2.31 | 2.329 | +0.8% | -0.05402 to +0.09144 | no |
| Omni's own CPU (cores), mean | 0 | 0.02518 | +0.0252 (native is 0) | +0.02157 to +0.02879 | yes: power given |
| CPU used with Omni's own (cores), mean | 2.31 | 2.354 | +1.9% | -0.02717 to +0.1149 | no |
| energy per core-hour (Wh, the 25 W standby model) | 301.7 | 279 | -7.5% | -42.63 to -2.766 | yes, down (shown, not judged) |
| HPA replicas, mean | 15.19 | 14.14 | -6.9% | -1.399 to -0.6942 | yes: GAIN |
| pods started | 4.8 | 5.3 | +10.4% | -0.2726 to +1.273 | no |
| pod start wait, total (s) | 10.3 | 19.4 | +88.3% | +3.742 to +14.46 | yes: LOSS |
| pod start wait, mean (s) | 1.994 | 3.706 | +85.8% | +0.8551 to +2.569 | yes: LOSS |
| second app: response time (ms), 95th percentile | 299.5 | 480 | +60.3% | -223.9 to +585.1 | no |
| second app: response time (ms), 99th percentile | 1037 | 1270 | +22.4% | -1429 to +1894 | no |
| second app: time over the response line (% of samples) | 14.7 | 15.22 | +3.5% | -0.2167 to +1.247 | no |
| second app: failed requests (%) | 12.43 | 13.02 | +4.8% | -0.06773 to +1.255 | no |

## B with the compass law vs native

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.979 | -0.4% | -0.04552 to +0.003211 | no |
| node-hours | 1.517 | 1.506 | -0.7% | -0.02127 to -0.00106 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 172.5 | 171.9 | -0.4% | -1.623 to +0.2955 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.5 | 171.5 | -0.6% | -2.077 to -0.05104 | yes: GAIN |
| response time (ms), mean | 490.8 | 458.3 | -6.6% | -88.33 to +23.42 | no |
| response time (ms), 95th percentile | 2009 | 2158 | +7.4% | -184.9 to +483.5 | no |
| response time (ms), 99th percentile | 5133 | 5762 | +12.3% | -159.3 to +1417 | no |
| time over the response line (% of samples) | 22.47 | 20.97 | -6.7% | -3.779 to +0.7831 | no |
| failed requests (%) | 3.381 | 2.908 | -14.0% | -1.579 to +0.634 | no |
| pending pods, pod-minutes | 1.17 | 1.047 | -10.5% | -1.022 to +0.7751 | no |
| utilisation (used / allocatable) | 0.09626 | 0.0966 | +0.3% | -0.001832 to +0.002493 | no |
| CPU used (cores), mean | 2.31 | 2.311 | +0.0% | -0.04638 to +0.04847 | no |
| Omni's own CPU (cores), mean | 0 | 0.01384 | +0.0138 (native is 0) | +0.01166 to +0.01602 | yes: power given |
| CPU used with Omni's own (cores), mean | 2.31 | 2.325 | +0.6% | -0.03162 to +0.0614 | no |
| energy per core-hour (Wh, the 25 W standby model) | 301.7 | 299.6 | -0.7% | -8.958 to +4.8 | no |
| HPA replicas, mean | 15.19 | 14.64 | -3.6% | -0.95 to -0.1394 | yes: GAIN |
| pods started | 4.8 | 5.1 | +6.2% | -0.5294 to +1.129 | no |
| pod start wait, total (s) | 10.3 | 16.4 | +59.2% | +2.161 to +10.04 | yes: LOSS |
| pod start wait, mean (s) | 1.994 | 3.085 | +54.7% | +0.5732 to +1.609 | yes: LOSS |
| second app: response time (ms), 95th percentile | 299.5 | 318.5 | +6.4% | -25.98 to +64.05 | no |
| second app: response time (ms), 99th percentile | 1037 | 1770 | +70.7% | -760.3 to +2226 | no |
| second app: time over the response line (% of samples) | 14.7 | 14.8 | +0.7% | -0.6134 to +0.8133 | no |
| second app: failed requests (%) | 12.43 | 12.51 | +0.6% | -0.2666 to +0.4187 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
