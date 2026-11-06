# The replica cap as a lever (the fourth amendment): capacity test with `replica_ceiling` 30, 10 paired repetitions

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Source: GitHub Actions workflow `benchmark-reps` (`load_steps` 1 to 8, 1,600 s, `replica_ceiling` 30, arms native /
omni / compass), run 37185767115, commit `2101c3d`, 2026-10-04, job `aggregate` (job 111402300427); artifact `live-reps`
(zip SHA-256 `289cc8bf221314e87ff01503b877b7e1d5a6bfb16f16febf815e4095460de05d`). Native keeps the cap of 10; only the compass
law is given the lever (the allocation law never moves the cap). Evidence class **L**.

**Result. The cap was not what limited the service.** With the cap free to rise to 30, the compass law served **24.6
requests a second, the same as without the lever** (24.0 and 24.6 in the runs without it); against this run's native
15.0 that is +64.0% (+7.4 to +11.8), and the whole of the difference from earlier runs is native's own variation. To
get it the compass law ran **78% more pods (16.5 against 9.2)** and **started 26.2 against 4.6**, both significant: the cap
rose, pods were added that the machine could not turn into served requests, and the cap came back. The real machine
under kind was **69% busy on its 4 cores** in both arms: the limit is the machine doing the work, not the replica cap
and not the "10% used" that kind's per-worker accounting shows.

The lever stays in the controller as the operator's to grant (off by default, `--replica-ceiling 0`), because on a
cluster whose machines do have room the cap can bind; it is not used in any setting reported as Omni-Compass's
default, and by the one rule this setting is not labelled GAIN.

## Capacity

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 15.0 |  |  | 10 |
| omni | 27.6 | +84.0% | +9.4 to +15.8 | 10 |
| compass | 24.6 | +64.0% | +7.4 to +11.8 | 10 |

## B with the compass law and the replica lever (ceiling 30) vs native (cap 10)

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.863 | -2.3% | -0.2597 to -0.01329 | yes: GAIN |
| node-hours | 2.683 | 2.621 | -2.3% | -0.113 to -0.0115 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 306.7 | 305.7 | -0.3% | -2.096 to +0.06092 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 306.7 | 301.1 | -1.8% | -9.33 to -1.867 | yes: GAIN |
| response time (ms), mean | 334.4 | 209.7 | -37.3% | -155.6 to -93.73 | yes: GAIN |
| response time (ms), 95th percentile | 890.3 | 445.1 | -50.0% | -517.3 to -373.1 | yes: GAIN |
| response time (ms), 99th percentile | 3305 | 3408 | +3.1% | -995 to +1202 | no |
| time over the response line (% of samples) | 19.64 | 10.86 | -44.7% | -9.975 to -7.577 | yes: GAIN |
| failed requests (%) | 6.893 | 6.613 | -4.1% | -0.5916 to +0.03216 | no |
| pending pods, pod-minutes | 0.3533 | 1.597 | +351.9% | -0.2235 to +2.71 | no |
| utilisation (used / allocatable) | 0.1003 | 0.1003 | -0.0% | -0.001908 to +0.001852 | no |
| CPU used (cores), mean | 2.408 | 2.351 | -2.3% | -0.06866 to -0.04374 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01391 | +0.0139 (native is 0) | +0.0122 to +0.01562 | yes: power given |
| CPU used with Omni's own (cores), mean | 2.408 | 2.365 | -1.8% | -0.05498 to -0.0296 | yes: GAIN |
| energy per core-hour (Wh, the 25 W standby model) | 289.3 | 291.2 | +0.6% | -2.034 to +5.732 | no |
| HPA replicas, mean | 9.243 | 16.49 | +78.4% | +4.263 to +10.23 | yes: power given |
| pods started | 4.6 | 26.2 | +469.6% | +20.2 to +23 | yes: power given |
| pod start wait, total (s) | 14.8 | 105.4 | +612.2% | +79.51 to +101.7 | yes: LOSS |
| pod start wait, mean (s) | 2.955 | 4.017 | +35.9% | +0.1717 to +1.952 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 69.36 | 68.7 | -0.9% | -1.179 to -0.1367 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
