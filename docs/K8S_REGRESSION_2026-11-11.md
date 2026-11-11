# Real Kubernetes, omni-v21's campaign beside omni-v25's: where the category's fall sits

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written by `tools/k8s_regression.py` from the two campaigns' own three-run tables (`results/live/V21_*.json`, `results/live/V25_*.json`) and the kind rig at every run's own commit. Class L (live software on GitHub's machines). Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

## 1. Both readings stand, each on its own engine

- **omni-v21**: the real-Kubernetes category of the Omni index reads GAIN, up 28.0351%, from its nine three-run tables (the index of 31 October, commit `3ad522226b`). It is omni-v21's historical reading and is labelled so.
- **omni-v25**: the same category reads GAIN, up 20.4633%, from its nine three-run tables (`results/OMNI_INDEX.json` on main). It is the latest measured reading of the category.
- **omni-v26** stands as the engine on main; its Kubernetes tables are not yet whole, so it has no category reading yet.
- The two differ by 7.5718 points. Neither number is moved into the other's record: the index file on main keeps omni-v25's numbers, and no omni-v21 table is read as omni-v25's. Every number on this page is each engine's own; setting them side by side is a diagnosis of what to test, never a result.

## 2. Test by test: native held, the Omni-Compass arm moved

The index's speed is native's response time over the Omni-Compass arm's (the 95th percentile; the mean for the queue of jobs). Each campaign's arms are its own; every change below is raw, across the two campaigns. The sixth column compares the two arms' own changes: how much the Omni-Compass arm's response time moved from one campaign to the other over and above native's, which is the change in the index's speed ratio, turned the other way up. A busier host slows both arms, so the column reads where the change sits, not its cause.

| test | index, omni-v21 | index, omni-v25 | native's response time (ms) | Omni-Compass arm's (ms) | the arm's response time, over and above native's | settings written by the Omni-Compass arm | pods it started |
|---|---|---|---|---|---|---|---|
| Steady same work: the load in steps at a fixed rate, ten pairs, three runs | GAIN, up 30.9% | GAIN, up 30.8% | 328.1 to 336.9 (up 2.7%) | 111.6 to 115.2 (up 3.3%) | up 0.6% | 15.9 to 19.3 (up 21.2%) | 3.4 to 4.5 (up 33.7%) |
| Demand that wanders: up and down one step at a time, ten pairs, three runs | GAIN, up 33.6% | GAIN, up 23.4% | 720.0 to 791.6 (up 9.9%) | 302.0 to 422.3 (up 39.9%) | up 27.2% | 37.4 to 51.8 (up 38.7%) | 5.6 to 9.7 (up 72.2%) |
| All four in one run: load up and down one step at a time, ten pairs, three runs | GAIN, up 33.5% | GAIN, up 29.1% | 755.9 to 782.0 (up 3.5%) | 332.8 to 407.7 (up 22.5%) | up 18.4% | 34.7 to 52.9 (up 52.5%) | 6.6 to 10.0 (up 51.0%) |
| Fairness: a noisy neighbour, ten pairs, three runs | GAIN, up 2.2% | LOSS, down 2.3% | 2,276.5 to 2,197.9 (down 3.5%) | 2,137.8 to 2,365.6 (up 10.7%) | up 14.6% | 46.6 to 127.9 (up 174.4%) | 4.3 to 5.9 (up 36.9%) |
| Faults: machine down, spike, runaway pod, blind probe, ten pairs, three runs | GAIN, up 30.0% | GAIN, up 25.2% | 433.7 to 406.0 (down 6.4%) | 198.0 to 209.2 (up 5.7%) | up 12.9% | 27.9 to 47.6 (up 70.6%) | 6.4 to 10.6 (up 66.0%) |
| A queue of jobs: cruise, then the emergency brake, ten pairs, three runs | GAIN, up 9.9% | GAIN, up 9.0% | 445.5 to 596.9 (up 34.0%) | 390.2 to 548.3 (up 40.5%) | up 4.9% | 12.7 to 9.8 (down 22.9%) | 0.7 to 0.0 (down 100.0%) |
| A public day of demand: the Google cluster trace of 2011 replayed one step at a time, ten pairs, three runs | GAIN, up 37.6% | GAIN, up 35.3% | 672.5 to 690.3 (up 2.7%) | 260.3 to 278.5 (up 7.0%) | up 4.2% | 51.4 to 72.6 (up 41.3%) | 13.7 to 16.0 (up 16.3%) |
| With its add-ons: KEDA on the CPU target and the live requests in flight, Omni-Compass on top, ten pairs, three runs | GAIN, up 27.3% | GAIN, up 16.0% | 276.4 to 281.8 (up 2.0%) | 134.1 to 181.0 (up 35.0%) | up 32.4% | 33.3 to 452.9 (up 1258.6%) | 7.0 to 8.0 (up 13.3%) |
| With its add-ons: KEDA's HTTP add-on on the live requests in flight, Omni-Compass on top, ten pairs, three runs | GAIN, up 54.7% | GAIN, up 22.5% | 477.2 to 489.2 (up 2.5%) | 128.8 to 266.0 (up 106.5%) | up 101.4% | 5.2 to 87.6 (up 1596.1%) | 2.2 to 2.5 (up 13.4%) |

Every value is the mean of the three runs' means, read from the table named in the first column's file (`results/live/V21_<table>.json`, `results/live/V25_<table>.json`).

| table | omni-v21's runs | omni-v25's runs | beat of the Omni-Compass arm, omni-v21 | omni-v25 | host cores | workers in service | native's pods started | native's host busy (%) |
|---|---|---|---|---|---|---|---|---|
| STEADY | 40223431219, 40246652453, 40269968227 | 41751085804, 41767220817, 41778758086 | 60 s | 10 s (the factory beat on site) | 4.0 and 4.0 | 6.0 and 6.0 | 5.4 and 5.3 | 26.9 and 27.8 |
| WANDERING | 40227141899, 40250378687, 40271292066 | 41751107237, 41768852229, 41780370478 | 60 s | 10 s (the factory beat on site) | 4.0 and 4.0 | 6.0 and 6.0 | 5.3 and 5.1 | 67.5 and 72.1 |
| ALL_FOUR | 40227146512, 40250382783, 40272629580 | 41751114338, 41768859003, 41780376170 | 60 s | 10 s (the factory beat on site) | 4.0 and 4.0 | 6.0 and 6.0 | 5.5 and 5.4 | 67.6 and 68.6 |
| FAIRNESS | 40227151053, 40250387280, 40272634568 | 41751121984, 41768864707, 41780381804 | 60 s | 10 s (the factory beat on site) | 4.0 and 4.0 | 6.0 and 6.0 | 5.4 and 5.6 | 68.2 and 67.6 |
| FAULTS | 40229598467, 40250391552, 40272639170 | 41753024820, 41768870890, 41781962156 | 60 s | 10 s (the factory beat on site) | 4.0 and 4.0 | 5.9 and 5.9 | 5.4 and 5.6 | 45.8 and 47.2 |
| BATCH | 40230821800, 40251625381, 40274018452 | 41753030885, 41768876462, 41781968016 | 60 s | 10 s (the factory beat on site) | 4.0 and 4.0 | 6.0 and 6.0 | 0.0 and 0.0 | 39.8 and 47.5 |
| TRACE_GOOGLE2011 | 40232036723, 40252903510, 40275448206 | 41753037941, 41768881626, 41781973989 | 60 s | 10 s (the factory beat on site) | 4.0 and 4.0 | 6.0 and 6.0 | 6.0 and 6.6 | 53.1 and 53.7 |
| KEDA_CPU_REQUESTS | 40232040937, 40254201062, 40276902708 | 41753044221, 41770442526, 41781979744 | 60 s | 10 s (the factory beat on site) | 4.0 and 4.0 | 6.0 and 6.0 | 5.1 and 4.9 | 27.2 and 28.0 |
| KEDA_REQUESTS | 40232040937, 40254201062, 40276902708 | 41753044221, 41770442526, 41781979744 | 60 s | 10 s (the factory beat on site) | 4.0 and 4.0 | 6.0 and 6.0 | 2.9 and 2.9 | 23.0 and 23.8 |

## 3. What differs between the two campaigns

- **The engine.** Seven of omni-v25's 65 fingerprinted files differ from omni-v21's (`OMNI_V21.json`, `OMNI_V25.json`); two of them touch Kubernetes, `omni_controller/controller.py` and `omni_controller/muscles.py`; the brain (`omnicompass/`) is byte for byte the same. Their changes: the hand-back tried five times against the API's failures (omni-v22; it runs only at the reset, after the window), the guard of the pod muscle of its own (omni-v23; it runs only in the arm by itself, not in these tests) and the factory beat (omni-v24). On these rigs only the beat changes a decision.
- **The beat.** Every omni-v21 run's rig gives the Omni-Compass arm a full decision every 60 s; every omni-v25 run's rig reads the factory beat, 10 s on kind (the table above, read at each run's own commit). The raw receipts agree: `run-40227141899/paired-1/bench-compass-1/omni_interval.txt` reads 60, `run-41751107237/paired-1/bench-compass-1/omni_interval.txt` reads 10 (the branch `raw`).
- **The rig, the same for both arms.** Between the two campaigns the kind rig came to read pods through its own collector (`tools/bench_integrity.py`) in place of a `kubectl` watch, seals every arm's files and refuses an arm that failed, restores the workload's rollout after each arm and grants the rights the arm by itself needs; the add-on rig (`scripts/kind_addons.sh`, `scripts/kubectl_keda.py`) is unchanged. The scorer (`tools/live_reps.py`) added the metered-work rows and a stricter test of "the same"; the 95th percentile and the mean are computed as before.
- **The machines.** Both campaigns ran on GitHub's four-core runners with six kind workers in service. Native's own response time moved under 10% in eight of the nine tests. The queue of jobs is the exception: native's mean response time rose with a busier host in omni-v25's campaign, and the arm's rose with it, so that test's small fall is mostly the machine's, not the engine's.

## 4. What the record says, and what it does not yet prove

- The fall sits in the Omni-Compass arm: native held, the arm's own response time rose in all nine tests, most over and above native's in KEDA's HTTP add-on, KEDA on the CPU target, the demand that wanders, all four in one run, the noisy neighbour and the faults (up 12.9% to 101.4%), least in the steady load, the queue of jobs and the public day (up 0.6% to 4.9%); in eight of the nine it also wrote more settings and started more pods.
- That is the signature of a faster beat on a moving load: a decision every 10 s follows each step of the load and moves the autoscaler's target and the pod count more often, where a decision every 60 s rides through them. It is the leading cause, not yet a proven one.
- The steady-load pace runs on omni-v25 (`results/pace/PACE.md`) read every slower beat against 10 s by small amounts on the response time; they do not cover a moving load, where the two campaigns part most.
- The direct test is preregistered and dispatched on GitHub's free machines: `docs/PACE_PREREGISTRATION.md`, amendment 7, the demand that wanders, native and the Omni-Compass arm at 10, 60 and 90 s, one engine, one rig, paired, three runs (runs 42977431782, 42977442687 and 42977447533). No paid card or cloud run is needed.
- What follows from it: if a slower beat reads better than 10 s there, the on-site factory beat is picked by amendment 4's frozen rule on those runs and lands as the next version through the model gate, keeping every repair made since omni-v21 (the hand-back retries, the pod muscle's guard, the Kafka wire's fix, the neighbour hold); every Kubernetes benchmark then runs again on it, read by its own engine. If not, the cause is looked for again in the files, and this page says so.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
