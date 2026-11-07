# The capacity test, run again under the amendment of 2026-10-03 evening, 10 paired repetitions

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Source: GitHub Actions workflow `benchmark-reps` (`load_steps` 1 to 8, 200 s a step, 1,600 measured seconds per arm,
arms native / omni / compass, order rotated, open-loop load), run 37162457542, commit `199f350`, 2026-10-04, job
`aggregate` (job 111332953338, `python tools/live_reps.py reps`). Transcribed from the job's printed receipt; the run's
artifact `live-reps` (zip SHA-256 `3fe93f2d5ef23a44a3442fcfd24f5c5b14501ca9711c3fab3b53440e4d578d7b`) holds the same
tables. Design: `docs/K8S_COMPASS_PREREGISTRATION.md`, "The capacity test" and its amendment. Evidence class **L**.

**Result.** With the compass law on top, the same six machines served **24.6 requests a second within the line against
native's 16.2: +51.9%, 95% interval of the paired difference +6.2 to +10.6 requests a second.** The first run
(`CAPACITY.md`, commit `422d60c`) measured the same paired difference, +8.4 requests a second, on runners where native
served 24.6; GitHub's runners were slower this time for every arm (native's failures 7.3% against 3.5%), the gap the
same. Response times −28% to −56%, time over the line −49%, failed requests −9.6%, mean HPA replicas −10.7%, all
significant. **Still higher: pods started, 5.1 against 3.8 (+34.2%, interval +0.29 to +2.31)**; the amendment's hold
on a growing demand did not remove it (first run +30.4%). Read with the replicas 10.7% lower, the extra starts are
pods started earlier on a rising load, the mechanism of the added capacity; it is reported here as measured and the
compass arm is not labelled GAIN by the one rule while it stands. The allocation law: capacity unchanged (+0.0%), pods
started +76.3%.

## Capacity

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 16.2 |  |  | 10 |
| omni | 16.2 | +0.0% | -2.0 to +2.0 | 10 |
| compass | 24.6 | +51.9% | +6.2 to +10.6 | 10 |

## B: Omni-Compass on top (the allocation law) vs native

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 3.164 | -47.3% | -3.182 to -2.489 | yes: GAIN |
| node-hours | 2.679 | 1.413 | -47.2% | -1.42 to -1.111 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 306.5 | 306.4 | -0.0% | -1.342 to +1.115 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 306.5 | 211.4 | -31.0% | -106.6 to -83.69 | yes: GAIN |
| response time (ms), mean | 340.4 | 262 | -23.0% | -104.9 to -52.03 | yes: GAIN |
| response time (ms), 95th percentile | 924.3 | 798.6 | -13.6% | -210.2 to -41.08 | yes: GAIN |
| response time (ms), 99th percentile | 3606 | 3666 | +1.7% | -867.5 to +987.5 | no |
| time over the response line (% of samples) | 19.58 | 15.5 | -20.9% | -5.934 to -2.238 | yes: GAIN |
| failed requests (%) | 7.298 | 6.885 | -5.7% | -0.9184 to +0.09272 | no |
| pending pods, pod-minutes | 0.245 | 0.2683 | +9.5% | -0.2981 to +0.3448 | no |
| utilisation (used / allocatable) | 0.101 | 0.1877 | +85.8% | +0.06874 to +0.1047 | yes, up (shown, not judged) |
| CPU used (cores), mean | 2.424 | 2.35 | -3.1% | -0.1092 to -0.04016 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01481 | +0.0148 (native is 0) | +0.01306 to +0.01656 | yes: power given |
| CPU used with Omni's own (cores), mean | 2.424 | 2.365 | -2.5% | -0.09289 to -0.02684 | yes: GAIN |
| energy per core-hour (Wh, the 25 W standby model) | 292 | 205 | -29.8% | -114.7 to -59.42 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.336 | 8.752 | -6.3% | -0.8815 to -0.2865 | yes: GAIN |
| pods started | 3.8 | 6.7 | +76.3% | +1.759 to +4.041 | yes: power given |
| pod start wait, total (s) | 9.1 | 10.9 | +19.8% | -6.085 to +9.685 | no |
| pod start wait, mean (s) | 2.024 | 1.625 | -19.7% | -1.401 to +0.6028 | no |

## B with the compass law vs native

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.75 | -4.2% | -0.4304 to -0.06983 | yes: GAIN |
| node-hours | 2.679 | 2.573 | -3.9% | -0.181 to -0.02997 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 306.5 | 306.5 | +0.0% | -1.101 to +1.106 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 306.5 | 298.1 | -2.7% | -13.93 to -2.863 | yes: GAIN |
| response time (ms), mean | 340.4 | 198.4 | -41.7% | -186.4 to -97.73 | yes: GAIN |
| response time (ms), 95th percentile | 924.3 | 411.5 | -55.5% | -612.7 to -412.8 | yes: GAIN |
| response time (ms), 99th percentile | 3606 | 2600 | -27.9% | -2501 to +488.2 | no |
| time over the response line (% of samples) | 19.58 | 9.925 | -49.3% | -11.99 to -7.331 | yes: GAIN |
| failed requests (%) | 7.298 | 6.6 | -9.6% | -1.086 to -0.3102 | yes: GAIN |
| pending pods, pod-minutes | 0.245 | 0.2367 | -3.4% | -0.2333 to +0.2166 | no |
| utilisation (used / allocatable) | 0.101 | 0.1027 | +1.7% | -0.0004573 to +0.003853 | no |
| CPU used (cores), mean | 2.424 | 2.373 | -2.1% | -0.06372 to -0.0399 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01051 | +0.0105 (native is 0) | +0.009172 to +0.01185 | yes: power given |
| CPU used with Omni's own (cores), mean | 2.424 | 2.383 | -1.7% | -0.05355 to -0.02905 | yes: GAIN |
| energy per core-hour (Wh, the 25 W standby model) | 292 | 288.8 | -1.1% | -9.197 to +2.776 | no |
| HPA replicas, mean | 9.336 | 8.334 | -10.7% | -1.453 to -0.5509 | yes: GAIN |
| pods started | 3.8 | 5.1 | +34.2% | +0.2856 to +2.314 | yes: power given |
| pod start wait, total (s) | 9.1 | 10.2 | +12.1% | -3.826 to +6.026 | no |
| pod start wait, mean (s) | 2.024 | 1.886 | -6.8% | -0.788 to +0.5108 | no |

Energy on kind is a declared model, not a meter (see `CAPACITY.md`).

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
