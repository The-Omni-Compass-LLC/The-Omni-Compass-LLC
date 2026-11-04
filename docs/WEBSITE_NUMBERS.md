# The Website's Numbers, Each With Its Receipt

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The website prints only the numbers in `results/WEBSITE_NUMBERS.json`, in its words; this page is the same file for a reader (`python3 tools/website_numbers.py`). The engine that stands: omni-v25. The website prints these numbers in these words and no other. A, B and C of a three-run table are three runs of one test (replications); the four arms are A, B, C and D. A number not in this file is not printed.

## The Omni index

- **GAIN, up 5.0%** — the Omni index: work, speed and machines, every real test weighed together; 26 tests on omni-v21's tables, real software on GitHub's own machines (never called bare metal, never the chip, never the cloud) (`results/OMNI_INDEX.json headline_pct`).
- Its second reading: **GAIN, up 12.9%** — the same index on work and speed alone (its second reading, never the headline).

| Category | Reading |
|---|---|
| Real Kubernetes (GitHub) | GAIN, up 28.0% |
| Real database (PostgreSQL behind PgBouncer, GitHub) | GAIN, up 4.2% |
| Real messaging (Apache Kafka, GitHub) | LOSS, down 1.2% |
| Real cache (Redis, GitHub) | STEADY, under the floor, up 0.1% |
| Real database cache (MongoDB under YCSB, GitHub) | LOSS, down 0.5% |
| Real database buffer pool (MySQL under sysbench, GitHub) | GAIN, up 2.2% |

All six categories are printed together, losses included, or none.

## The four arms

| Arm | What it is | Status | Engine |
|---|---|---|---|
| A | the chip, native | read | omni-v23 (digest c96ea4105d8747db, 65 files) |
| B | the chip with Omni-Compass on native | read | omni-v23 (digest c96ea4105d8747db, 65 files) |
| C | the cloud, native | read | omni-v18 |
| D | the cloud with Omni-Compass on native | read: it holds (no judged gauge reads LOSS) | omni-v18 |

B against A, the work for the bill per run: up 1.5%, up 0.7%, down 0.7%: the runs disagree.

D against C (97 paired repetitions; Omni-Compass on top of native at the tune-down (dial save) on the machines alone (OMNI_MACHINES_ONLY=1), the rule of 14 October struck on 31 October):

| Gauge | C, native | D, Omni-Compass on native | Change | 95% interval | Reading |
|---|---|---|---|---|---|
| worker nodes in service, mean | 2.814 | 2.832 | +0.7% | −0.0098 to +0.0469 | STEADY, no difference beyond the noise |
| node-hours | 0.7104 | 0.715 | +0.7% | −0.0024 to +0.0117 | STEADY, no difference beyond the noise |
| energy, parked workers still on at idle power (Wh, declared model) | 86.62 | 87.77 | +1.3% | −0.6670 to +2.9702 | STEADY, no difference beyond the noise |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 82.7 | 83.23 | +0.6% | −0.2945 to +1.3550 | STEADY, no difference beyond the noise |
| response time (ms), mean | 517.1 | 503.1 | −2.7% | −29.7566 to +1.8811 | STEADY, no difference beyond the noise |
| response time (ms), 95th percentile | 1245 | 1195 | −4.0% | −128.4729 to +28.5631 | STEADY, no difference beyond the noise |
| response time (ms), 99th percentile | 4744 | 4222 | −11.0% | −1009.6926 to −34.3668 | GAIN |
| time over the response line (% of samples) | 29.06 | 28.81 | −0.9% | −1.1301 to +0.6231 | STEADY, no difference beyond the noise |
| failed requests (%) | 4.758 | 4.945 | +3.9% | −0.4799 to +0.8526 | STEADY, no difference beyond the noise |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.07 | 13.9 | −1.2% | −0.4116 to +0.0611 | STEADY, no difference beyond the noise |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.92 | +24.918 (native is 0) | +24.1653 to +25.6698 | shown, not judged |
| pods with no machine to take them (unschedulable) | 2.598 | 2.392 | −7.9% | −0.5274 to +0.1151 | STEADY, no difference beyond the noise |
| time pods had no machine to take them, pod-minutes | 7.018 | 5.993 | −14.6% | −4.1768 to +2.1273 | STEADY, no difference beyond the noise |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.9 | 5.573 | −5.6% | −0.7542 to +0.0989 | STEADY, no difference beyond the noise |
| utilisation (used / allocatable) | 0.3622 | 0.3605 | −0.5% | −0.0069 to +0.0035 | STEADY, no difference beyond the noise |
| CPU used (cores), mean | 1.935 | 1.937 | +0.1% | −0.0176 to +0.0208 | STEADY, no difference beyond the noise |
| Omni's own CPU (cores), mean | 0 | 0.005163 | +0.005 (native is 0) | +0.0050 to +0.0053 | shown, not judged |
| CPU used with Omni's own (cores), mean | 1.935 | 1.942 | +0.4% | −0.0125 to +0.0260 | STEADY, no difference beyond the noise |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 169.5 | 170.5 | +0.6% | −1.1581 to +3.0914 | STEADY, no difference beyond the noise |
| HPA replicas, mean | 9.371 | 9.348 | −0.2% | −0.0802 to +0.0340 | STEADY, no difference beyond the noise |
| pods started | 5.01 | 4.753 | −5.1% | −0.7001 to +0.1847 | STEADY, no difference beyond the noise |
| pod start wait, total (s) | 525.4 | 455.2 | −13.4% | −278.2501 to +137.6728 | STEADY, no difference beyond the noise |
| pod start wait, mean (s) | 98.43 | 89.88 | −8.7% | −49.2406 to +32.1393 | STEADY, no difference beyond the noise |
| machines billed, machine-hours | 0.586 | 0.5931 | +1.2% | −0.0074 to +0.0216 | STEADY, no difference beyond the noise |
| compute bill at list price ($) | 0.05626 | 0.05694 | +1.2% | −0.0007 to +0.0021 | STEADY, no difference beyond the noise |

D's work per dollar: not read by the meter on this set: its load sent a fixed rate, the same in both arms; the sets with the work meter are queued (docs/K8S_COMPASS_PREREGISTRATION.md, the amendments of 31 October, night, and 4 November). Google and Amazon: wired as Azure is, not yet run (their keys are not in the repository's secrets).

## The people on call

Gain in all three of our runs: the minutes an on-call page would be open, down 28.9%, 13 tests on omni-v21 (`results/OVERSIGHT.json`).

## Never printed

| Number | Where it came from | Why not |
|---|---|---|
| 47.2% | docs/history/model_tables/ABC_TABLE_MODEL.json (was results/ABC_TABLE.json): the web workload's mean response time, 215.1 ms for Kubernetes alone against 146.1 ms for Omni-Compass alone, in our own model (class S) of October; Omni-Compass alone is not an arm, and the same model reads its energy up 26% | a model's speed ratio, never a receipt, never whole-system, never bare metal |
| 49.9% | the same model table, the multi workload (217.9 ms against 145.4 ms) | a model's speed ratio, never a receipt, never the cloud |
| +5.3% GPU energy | the same model table, the gpu workload (194.1 against 184.4 kWh, Omni-Compass alone) | a model, never the card's meter; the card's receipts are arms A and B |
| +28.0% Kubernetes alone | results/OMNI_INDEX.json, one of six categories | a category is printed only with the other five, losses included |
| +12.9% bare metal; +5.0% through the cloud | results/OMNI_INDEX.json | both are the Omni index over real tests on GitHub's own machines; neither is bare metal or the cloud |
| 20% drain, 2.9% stack tax, 7% engineering, $16M, +33% free work, 13.1%, 140% | outside AI text | no record carries them (docs/WEBSITE_CLAIMS.md) |
| three arms | the website's own words | four arms, A, B, C and D; A, B and C of a table are runs |

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
