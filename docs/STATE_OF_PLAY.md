# Omni-Compass: state of play (read this first)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Current facts only. Earlier states, failures and chronology are kept whole in `docs/HISTORY.md`. The release this page
describes is identified by `RELEASE_MANIFEST.json` (commit, fingerprints of the engine, the C++ twins, the GPU protocol,
the live evidence and the verification receipt), which `verify.py` checks against the files.

**Rerun everything:** `pip install -r requirements.txt && python verify.py` ends with `VERIFICATION: PASS`.

<!-- where things stand (tools/summary.py --fix) -->

**Where things stand, read from the result files.** Written by `python3 tools/summary.py --fix` from the files it names; `verify.py` fails a push in which this block no longer matches them. Nothing in it is typed by hand. The live results run on the engines named in their own tables, and every one of them runs again on the newest engine.

- **The engine on this checkout:** omni-v23, fingerprint c96ea4105d8747db (65 files).
- The muscles and the seven organisms on engine omni-v8 at the max (evidence class S, our own models; run 2026-10-17 15:39 UTC, commit 9819a903cba3, 1107 muscles; source: results/realms_v5/REALMS_V5.md):
  - every muscle alone, over its loads: STEADY 577, GAIN 530
  - the organisms under the normal load: the spine: GAIN (fewer misses), misses down 0.145 pp, power given +0.011%; Compute / AI / Cloud: GAIN (fewer misses), misses down 0.070 pp, power given +0.009%; Physics / Robotics / Autonomous: GAIN (fewer misses), misses down 0.121 pp, power given +0.010%; Energy / Facility / Industrial: GAIN (fewer misses), misses down 0.118 pp, energy the same; Distribution / Specialized: GAIN (fewer misses), misses down 0.067 pp, power given +0.002%; the four stacked: GAIN (fewer misses), misses down 0.092 pp, energy the same; the whole tower: GAIN (fewer misses), misses down 0.051 pp, energy the same
  - the organisms under the climb load: the spine: GAIN (fewer misses), misses down 0.632 pp, power given +0.039%; Compute / AI / Cloud: GAIN (fewer misses), misses down 0.390 pp, power given +0.046%; Physics / Robotics / Autonomous: GAIN (fewer misses), misses down 0.317 pp, power given +0.021%; Energy / Facility / Industrial: GAIN (fewer misses), misses down 0.217 pp, energy the same; Distribution / Specialized: GAIN (fewer misses), misses down 0.460 pp, power given +0.026%; the four stacked: GAIN (fewer misses), misses down 0.349 pp, energy the same; the whole tower: GAIN (fewer misses), misses down 0.094 pp, energy the same
  - the organisms under the line load: the spine: GAIN (fewer misses), misses down 0.371 pp, power given +0.038%; Compute / AI / Cloud: GAIN (fewer misses), misses down 0.205 pp, power given +0.045%; Physics / Robotics / Autonomous: GAIN (fewer misses), misses down 0.250 pp, power given +0.030%; Energy / Facility / Industrial: GAIN (fewer misses), misses down 0.117 pp, energy the same; Distribution / Specialized: GAIN (fewer misses), misses down 0.142 pp, power given +0.006%; the four stacked: GAIN (fewer misses), misses down 0.176 pp, energy the same; the whole tower: GAIN (fewer misses), misses down 0.051 pp, energy the same
- The grid (source: results/grid_v5/GRID.md): Across the grid: modelled, 36 of 36 squares of 10 and 100 runs GAIN (fewer misses); the 18 single runs: 18 with fewer misses; work +0.000%; power given +0.000% to +0.065%; with the cluster inside, 54 squares: 18 single repetitions (no reading); of the 36 of 10 and 100 repetitions, by gauge: "organism time over the line (% of steps)" GAIN in 36, LOSS in 0, "time over the response line (% of samples)" GAIN in 36, LOSS in 0, "response time (ms), 95th percentile" GAIN in 26, LOSS in 2, "energy (Wh)" GAIN in 26, power given in 0, "energy, parked workers still on at idle power (Wh)" GAIN in 26, power given in 0, "organism energy (J)" GAIN in 0, power given in 22, "organism work per energy" GAIN in 0, power given in 22, "failed requests (%)" GAIN in 18, LOSS in 0, "response time (ms), 99th percentile" GAIN in 12, LOSS in 2, "HPA replicas, mean" GAIN in 4, power given in 5, "pods started" GAIN in 3, power given in 0; off the clock in 3; invalid in 0.
- The Omni index (evidence class L, real software on real computers: the software end, not bare metal and not the chip; every measure judged across our three runs; the three-run tables of omni-v21, each named in its table): 5.2% GAIN on the resource reading (work, speed, machines, energy), 12.9% GAIN on the service reading (work and speed alone). Source: results/OMNI_INDEX.md.
  - Real Kubernetes (GitHub): 28.4% GAIN
  - Real database (PostgreSQL behind PgBouncer, GitHub): 4.1% GAIN
  - Real database buffer pool (MySQL under sysbench, GitHub): 3.2% GAIN
  - Real cache (Redis, GitHub): 0.0% STEADY
  - Real database cache (MongoDB under YCSB, GitHub): 0.6% LOSS
  - Real messaging (Apache Kafka, GitHub): 1.0% power given

**On the engine that stands (omni-v23): 0 of 26 benchmarks so far.** Every other row is that engine's own result, named in its Engine column, and runs again on the engine that stands (`scripts/reruns.txt`); results are never read across engines.

| Benchmark | Engine | Its one number | Its word | Class |
|---|---|---:|---|---|
| Every real test together: the Omni index | omni-v21 | 5.2% | GAIN AND LOSS | L |
| The six organisms with the real cluster inside, 10 and 100 copies | omni-v3 | 5.3% | GAIN, power given | L, the cluster; S, the organism around it |
| The big organisms with the real cluster inside, 1,000 copies on Azure | omni-v3 | 155.0% | GAIN | L, the cluster; S, the organism around it |
| The 945 modelled muscles as one tower, every muscle written at once | omni-v3 | 0.3% | GAIN | S |
| Robustness: the two-hour run | omni-v21 | 3.8% | GAIN AND LOSS | L |
| Robustness: the governor killed outright mid-run | omni-v21 | 8.1% | GAIN AND LOSS | L |
| Robot arms (MuJoCo), the three untouched robots | omni-v21 | 3.8% | GAIN | S |
| Redis, the cache's memory ceiling | omni-v21 | 0.0% | GAIN AND LOSS | L |
| Real Kubernetes, steady work | omni-v21 | 30.9% | GAIN | L |
| Real Kubernetes, faults | omni-v21 | 30.2% | GAIN, power given | L |
| Real Kubernetes, demand that wanders | omni-v21 | 33.6% | GAIN, power given | L |
| Real Kubernetes, all four at once | omni-v21 | 33.5% | GAIN AND LOSS | L |
| Real Kubernetes, a service rightsized by Goldilocks and the VPA's recommender, Omni-Compass on top, ten pairs, three runs | omni-v21 | 34.7% | GAIN AND LOSS | L |
| Real Kubernetes, a service rightsized by CruiseKube applying its own recommendations, Omni-Compass on top, ten pairs, three runs | omni-v21 | 0.4% | LOSS | L |
| Real Kubernetes, a queue of jobs | omni-v21 | 13.7% | GAIN AND LOSS | L |
| Real Kubernetes, a public day of demand (Google 2011) | omni-v21 | 37.6% | GAIN AND LOSS | L |
| Real Kubernetes, a noisy neighbour | omni-v21 | 2.2% | GAIN AND LOSS | L |
| Real Kubernetes, With its add-ons: KEDA's HTTP add-on on the live requests in flight, Omni-Compass on top, ten pairs, three runs | omni-v21 | 94.7% | GAIN, power given | L |
| Real Kubernetes, With its add-ons: KEDA on the CPU target and the live requests in flight, Omni-Compass on top, ten pairs, three runs | omni-v21 | 29.8% | GAIN AND LOSS | L |
| Power grids (SimBench), both load models | omni-v21 | 5.8% | GAIN, power given | S |
| PostgreSQL, the pooler's pool size | omni-v21 | 4.1% | GAIN, power given | L |
| MySQL, the buffer pool's size | omni-v21 | 3.2% | GAIN, power given | L |
| MongoDB, the storage engine's cache size | omni-v21 | 0.6% | GAIN AND LOSS | L |
| Kafka, the consumer group's size | omni-v21 | 1.0% | GAIN AND LOSS | L |
| Drone swarms, the three untouched cells | omni-v21 | 3.0% | GAIN | S |
| Buildings and batteries (CityLearn), the districts with batteries | omni-v21 | 1.5% | GAIN | S |

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

<!-- end of where things stand -->

## The engine that stands

**omni-v23** (`OMNI_V23.json`, digest `c96ea4105d8747db`, 65 files; `docs/OMNI_V23.md`), on main from 31 October: omni-v22 with one
guard in the Kubernetes governor's pod muscle of its own, on the founder's order of that day that Omni direct keeps every muscle
Omni-Compass cannot be. A write of a workload's own scale that the cluster refuses is recorded and the decision goes on; at three
refusals in a row the knob goes back to native's own pod autoscaler, made from the operator's target and range recorded on the
workload, and the muscle leaves the workload to it, so the organism never runs with a knob nobody moves. 64 of its 65 files are
omni-v22's bytes; the model gate against omni-v22 (`results/model_gate/V23_VS_V22.md`, class S) read identical on every gauge of every
model, no LOSS. Every benchmark runs again on it from 20:00 UTC on 31 October (`scripts/reruns.txt`); the omni-v22 runs started before
run to their end as omni-v22's record.

**omni-v22** (`OMNI_V22.json`, digest `0e23a0bc561b900a`, 65 files; `docs/OMNI_V22.md`), on main from 30 to 31 October: the five data
stores' wires brought to the max. What a wire's own rule asks goes through unclamped, up to the operator's cover and never below
native; memory is spent only where the store's own account of a miss (MySQL's performance schema timer on the data files' reads,
WiredTiger's page-read time for the application's threads, the Redis application's own split) says the misses are at least the one
key's floor of the service's time, and only while the host keeps its 5% cushion; a hand-back never goes below the working set's
floor; Kafka's group has a twin of its arrivals and a reflex; PostgreSQL's pool is never taken below the pooler's own setting
(`tools/store_brain.py`, the five `tools/run_*.py` wires, `tools/knob_verdict.py`, all in the fingerprint). The model gate against
omni-v21 (class S) read no LOSS at the counted setting on every store wire; the Kubernetes governor's models read omni-v21's own
numbers on every gauge (the one governor change, the hand-back tried five times against a transient failure of the cluster's API, moves
no decision). Every benchmark runs again on it from the moment it reached main (`scripts/reruns.txt`,
released by the conductor), the five stores first. omni-v21 (`docs/OMNI_V21.md`, the immune system knows itself, knob by knob) stood
from the evening of 25 October to 30 October; its tables stand as its own record until omni-v22's three runs of each benchmark land.
The block above is written from the result files on every push: each row names the engine its
table ran on, and every three-run table of omni-v21 is rebuilt byte for byte from its archived runs by `tools/reproduce.py`
(all 31 on 27 October). Each earlier engine is on its own page (`docs/OMNI_V<n>.md`); the chronology this page carried until
27 October is whole in `docs/history/STATE_OF_PLAY_2026-10-27.md`.

## The whole system, every layer composed

`results/WHOLE_SYSTEM.md` (built by `tools/whole_system.py`) composes the layers from the tables that stand: each layer's ratio
toward its gauge's aim, Rℓ(g) = oℓ/nℓ or nℓ/oℓ, measured with the layer under it as native runs it, composed by the product law
R(g) = ∏ℓ Rℓ(g), every run's paired interval carried by the delta method, the three runs pooled by inverse variance. It is
class S over class P and L tables and across engines, and says so; the stacked run, Omni-Compass at every layer at once on one
machine (the GPU's stacks mode, `lambda-gpu.yml`), is the measurement that replaces it. The numbers stand on that page, never
copied here.

## Open

Each with its receipt, run by run, in `docs/RUN_LEDGER.md`.

1. **The card.** omni-v21 on an A100, three runs each (`results/gpu/V21_A100_SAVE_ABC.md`, `V21_A100_CAP_ABC.md`,
   `V21_A100_CAP_FULL_ABC.md`). At the factory dial (the max) STEADY with no write: native already runs both knobs at their top.
   The tune-down (dial save): work per energy GAIN by the mean of our three runs (up 0.75%, beyond the noise in 1 of 3), every
   service gauge STEADY. The cap at 70%: the mean response time LOSS by the mean (beyond the noise in 0 of 3, run A alone). The
   tune-down as the card's factory dial goes through the model gate as the next version on the founder's word; the cap's rows
   are on the next version's list. The stacked box (three A10s, `results/gpu/V21_STACKS_A10_ABC.md`): at 1 and 10 copies, complete in all
   three runs, the card STEADY in every organism; 100 copies one repetition a run, shown, not judged. Where the chip proof stands,
   what the card's own files say about the mechanism, and what it still needs, step by step with its cost: `docs/THE_CHIPS.md`.
2. **The three-arm showing on omni-v21** landed (`results/orchestrator/V21_THREE_ARMS_ABC.md`, runs 40474220398,
   40474223636, 40474227699): Omni-Compass on top of native against native, work GAIN in all three of our runs (up 8.5%), the
   95th percentile GAIN in all three (down 13.0%); the answer at the top of the README reads it.
3. **Azure**: the omni-v18 set of 100 paired repetitions finished 29 October (97 passed, 3 failed) as omni-v18's record; the
   omni-v21 steady set runs (16 of 100 by 30 October, 16:27 UTC: 14 passed, 2 failed, about 68 minutes a repetition); the
   omni-v22 sets queue behind it, one at a time, each behind Azure's own $0 check (`scripts/azure_queue.txt`;
   `docs/THE_CHIPS.md` section 6).
4. **Google and Amazon**: wired as Azure's sets are and switched off; GitHub's own check of 27 October (`cloud-check`) reads
   their four keys absent from this repository's secrets (`GCP_CREDENTIALS`, `GCP_PROJECT`, `AWS_ACCESS_KEY_ID`,
   `AWS_SECRET_ACCESS_KEY`; `docs/GOOGLE_SETUP.md` section 4, `docs/AMAZON_SETUP.md` sections 1a to 3).
5. **The CPU package** (`cpu-power`): needs a bare-metal machine; GitHub's are virtual, with no frequency governor and no energy
   meter, and the workflow fails rather than hide it.
6. **The three rows still on omni-v3** in the block above, until their omni-v21 runs land.
7. **Every LOSS row on omni-v21**, each with its cause in `docs/LOSS_LEDGER.md`: the next version's work, through the model
   gate first.
8. **Omni-Compass 1.0**: when the founder declares the engine final, the engine that stands then is published as 1.0 and the
   older fingerprints go to `docs/history` as the road to it.

## Where things are

| Path | What it is |
|---|---|
| `docs/OMNI_COMPASS_MANUAL.md` (PDF: `docs/OMNI_COMPASS_MANUAL.pdf`) | the Operator's Manual: how to embed, wire, tune, run and check Omni-Compass; every muscle's wiring and card (Appendix E) |
| `docs/OMNI_COMPASS_OWNERS_MANUAL.md` (PDF: `docs/OMNI_COMPASS_OWNERS_MANUAL.pdf`) | the Owner's Manual: the theory, the mechanism, the engine's source, every result, every muscle (Appendix G) |
| `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md` (PDF: `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.pdf`) | the Live Engine Manual: how to read the live engine page, its monitors, gauges and knobs, native beside Omni-Compass; what to do when a tile reads LOSS |
| `docs/BENEFIT_SHEET.md` | one number per benchmark, its word, its engine, every change in words |
| `docs/LEVELS.md` | every level on one page (muscle, organism, cluster, add-ons, service, plant, cloud, group of clusters), its counts of GAIN, STEADY, power given and LOSS, and any level whose gauges go the other way |
| `docs/REGISTER.md` | every muscle family wired, every benchmark run, every benchmark still to run |
| `docs/WIRING_VERDICTS.md` | write, watch or the operator's choice, per knob, from every result |
| `docs/OMNI_V22.md` | the engine that stands, what changed and how it was read; each earlier engine's page beside it (`docs/OMNI_V<n>.md`) |
| `docs/RUN_LEDGER.md` | every chip, cloud and machine run, what it cost, whether it finished, and where its receipt is |
| `docs/THE_CHIPS.md` | the chips: every GPU run, what the card shows by the one key, what its own files say about the mechanism, and what the chip proof still needs with each step's cost |
| `docs/AUDIT_2026-10-27.md` | the repository audited top to bottom on 27 October: every finding, its fix at its source, and what holds it |
| `docs/AUDIT_2026-10-30.md` | the repository graded top to bottom on 30 October: every area's grade on its record, what broke and was fixed, the founder's week, and what is open |
| `docs/REPORT_CARD.md` | the report card: every section and piece of the repository graded on its record on the engine that stands, with the count of everything and what moves each grade up |
| `docs/history/STATE_OF_PLAY_2026-10-10.md` | this page as it stood on 10 October, on Omni v3, moved here whole |
| `docs/history/STATE_OF_PLAY_2026-10-27.md` | this page's chronology as it stood on 27 October, moved here whole |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
