# The report card: every section and piece of the repository, graded on its record

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Graded again on 3 November 2026, evening, on the founder's order ("go into the GitHub ... grade and see where it's at, where
we're at"), from the repository on main at the commit this page is pushed with and from GitHub's own run records of the day.
The first grading (30 October, on omni-v22) and its update of 31 October are in this page's history. The engine that stands is
**omni-v25** (`OMNI_V25.json`, digest `cf56fc0a7b707452`, 65 files), landed with this grading on 3 November: omni-v24 with the Kafka fault
of item 12 fixed (`docs/OMNI_V25.md`); GitHub's verify on the push before it (run 41704705283, the second batch of the number
sweep) is the last one read here. Every count in section 1 is computed by
`python3 tools/report_card.py` at that commit, never typed; every reading is the record's own, by the one key
(`tools/readings.py`), and names the file that holds it. A grading is dated: its counts and readings are true at its commit, and
the next grading replaces them. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved
these results.

**How a grade is given.** A: the record is complete on the engine that stands, every check of it is green, and no LOSS row
stands without its cause fixed. A−: complete, with small open items named. B+ and B: the record stands and reads GAIN, with
LOSS rows or gaps still open. C: a benefit not yet shown, or LOSS on the benefit sheet. Incomplete: runs not finished.
Not run: wired, nothing run. A fault: something that should work does not, named with what is known of its cause. Nothing is
graded on a model as if it were proof: class S is said. No three-run table has landed on omni-v24 yet, so every result below is
read from the newest table of its test (omni-v21's for most), and an A on a result means A on that table.

## 1. The repository in numbers

<!-- the repository in numbers (tools/report_card.py) -->
| Piece | Count |
|---|---:|
| Engine files in the fingerprint (omni-v25) | 65, 63 of them omni-v24's bytes |
| Unit test cases collected under `tests/` | 789 |
| Function-test files (`tools/function_tests.py --list`) | 68 |
| C++ parity test files (the sealed twins) | 14 |
| Checks in `verify.py --quick` at the receipt's commit (903c5043869f) | 150 PASS, 0 FAIL |
| GitHub workflows (`.github/workflows/`) | 71 |
| Three-run tables in `results/live/`, all engines | 250 |
| Of them, by engine, newest first | omni-v21: 31; omni-v18: 8; omni-v17: 13; omni-v16: 13; omni-v14: 4 |
| Three-run tables on the engine that stands (omni-v25) | 0 (the newest are omni-v21's) |
| Model gate pages (`results/model_gate/`) | 33 |
| Pages in `docs/` (top level), preregistrations, engine pages, history pages | 155, 30, 25, 92 |
| Drawn figures (`docs/book/figures/`) | 77 |
| The Operator's, Owner's and Live Engine Manuals (PDF pages) | 660, 2,028, 320 |
| Files carrying the legal notice (`tools/legal.py --check`) | 1,745 |
| Muscles in the catalog, in our own models: GAIN, STEADY, LOSS | 1,107: 530, 577, 0 (70 families) |
| Benchmarks on the benefit board, by the engine of their newest table | 26: omni-v21 23, omni-v3 3 |
| LOSS rows against Omni-Compass's own native (the ledger), by engine; of them without a cause written | omni-v21: 50, 0 without; omni-v12: 113, 101 without |
<!-- end of the repository in numbers -->

## 2. The grades, piece by piece

| # | Piece | Where | Grade | The record now | What moves it up |
|---:|---|---|---|---|---|
| 1 | The engine on main, omni-v25 | `omnicompass/`, `omni_controller/`, `tools/run_kafka.py`, `OMNI_V25.json`, `docs/OMNI_V25.md` | **A−** | 65 fingerprinted files, 63 of them omni-v24's bytes; the Kafka wire's fault fixed (item 12) and a comment in the Kubernetes governor corrected to name the corrected ladder's file; the governor's decisions byte for byte omni-v24's; omni-v24's change, the factory beat for its place (10 s on site, 60 s through a cloud), carried; the model gate against omni-v24 (`results/model_gate/V25_VS_V24.md`); every page names it (`tools/land_engine.py --check`) | Its first three-run tables |
| 2 | The C++ twin | `cpp/`, `results/SEAL.json` | **A−** | Every twin that exists proven equal to its Python by its parity test (14 parity test files) | The store brain (`tools/store_brain.py`, omni-v22) is Python only; its twin with a version |
| 3 | The Kubernetes governor | `omni_controller/` | **A−** | On real Kubernetes the work and the 95th percentile read GAIN in all three of our runs (omni-v21); every LOSS row on its tables has its cause written (50 of 50, `docs/LOSS_LEDGER.md`) | Its omni-v24 tables; the pod start on a host at its top through the model gate |
| 4 | Omni-Compass's own orchestrator, three arms | `omni_orchestrator/`, `results/orchestrator/V21_THREE_ARMS_ABC.md` | **A−** | Omni on native against native: work GAIN in all three of our runs (up 7.0% to 10.3%), the 95th percentile GAIN in all three (down 12.0% to 14.2%) | Omni direct against Omni on native reads work LOSS by the mean of our three runs (beyond the noise in 1 of 3) and the 95th percentile the runs disagree |
| 5 | Kubernetes, single services (steady, faults, wandering demand, KEDA's HTTP add-on) | `docs/BENEFIT_SHEET.md` | **A** (omni-v21) | GAIN, or GAIN with power given, no LOSS row: steady 30.9%, faults 30.0%, wandering demand 33.6%, KEDA's HTTP add-on 94.7% GAIN by the index's rule | Their omni-v24 tables |
| 6 | Kubernetes, combined and governed (all four, Goldilocks, the queue, Google 2011, the noisy neighbour, KEDA on CPU, the capacity test) | `docs/BENEFIT_SHEET.md`, `docs/LOSS_LEDGER.md` | **B+** | On the benefit sheet GAIN AND LOSS in each: 9.9% to 37.6% GAIN by the index's rule (the noisy neighbour 2.2%), with 1 to 3 LOSS rows each, every one with its cause written; the capacity test (`results/live/V21_CAPACITY.md`), not on the sheet: 1 LOSS row (its cause written, the rig's noise at its cap) and 6 rows where the runs disagree | The pod start rows read beside the host's busy share; their omni-v24 tables |
| 7 | CruiseKube on top | `results/live/V21_CRUISEKUBE.md` | **C** | LOSS on the benefit sheet (0.4% LOSS by the index's rule; 3 LOSS rows), the cause written: the governor wrote nothing in 30 repetitions, so the two arms are one system and the rows are the rig's noise | A load that takes the service to its line, where the replica range has work to do |
| 8 | Robustness: the two-hour run and the kill | `results/live/V21_ROBUST_LONG.md`, `V21_ROBUST_KILL.md` | **B** | The kill: 8.1% GAIN by the index's rule, every setting handed back; the two-hour run: 3.8% LOSS by the index's rule, its 2 LOSS rows the pod start wait on the shared test machine, with their cause written | The host's busy share read beside the row; their omni-v24 tables |
| 9 | PostgreSQL and MySQL | `results/live/V21_PGBENCH*.md`, `V21_SYSBENCH*.md` | **A−** | GAIN, power given: PostgreSQL 4.2%, MySQL 2.2% GAIN by the index's rule, no LOSS row in their main tables; MySQL as shipped 3 LOSS rows, each with its cause written | Their omni-v24 tables |
| 10 | Redis | `results/live/V21_REDIS*.md` | **C+** | GAIN AND LOSS, 0.1% GAIN by the index's rule (under the floor); 1 LOSS row and 1 more in its service table, both with their cause written | Its omni-v24 tables |
| 11 | MongoDB (YCSB) | `results/live/V21_YCSB*.md` | **C** | GAIN AND LOSS, 0.5% LOSS by the index's rule; 13 LOSS rows across its three tables, each with its cause written | Its omni-v24 tables |
| 12 | Kafka | `results/live/V21_KAFKA*.md`, `.github/workflows/kafka.yml`, `tools/run_kafka.py` | **C; the fault fixed in omni-v25** | GAIN AND LOSS, 1.2% LOSS by the index's rule; 15 LOSS rows, each with its cause written. Since omni-v22's Kafka wire (30 October) no Kafka run has finished: every workload stops at the job's 150-minute limit inside "Run the workload" (8 runs on 3 November, among them 41601163807, whose four workloads each ran past 150 minutes), where omni-v21's took 14 to 32 minutes a workload (run 40400868003). The runner prints its progress only to a file the job uploads, so the job logs do not show where it stalls | Found and fixed at this grading: reproduced on Kafka 3.9.1 as the workflow installs it, the omni arm's producer single-threaded and waiting on a lock it inherited when it was forked while the governor's thread opened its own Kafka client (from omni-v22); omni-v25 forks the producer first, and a producer that overruns its schedule stops its workload with the reason; the job's log now shows the runner's progress. Its first tables on omni-v25 |
| 13 | The models: robots, swarms, buildings, grids | `results/live/V21_MUJOCO.md`, `V21_SWARM.md`, `V21_CITYLEARN.md`, `V21_PANDAPOWER.md` | **A−** | GAIN in each, no LOSS row (MuJoCo 3.8%, swarms 3.0%, CityLearn 1.5%, SimBench 5.8%); our own models and independent simulators, class S, never proof | Their omni-v24 runs |
| 14 | The seven organisms with the real cluster inside (the grid) | `results/grid_v24/`, `scripts/dispatch_grid.py` | **Incomplete** | The benefit sheet still reads omni-v3 here. The omni-v24 grid runs on GitHub's machines: every grid run among GitHub's last 100 finished runs on 3 November passed but one (`six-kube x100`, the compute and physics realms) | The omni-v24 grid's table; that run's cause |
| 15 | The orchestra and the governors live | `results/orchestra/ORCHESTRA.md`, `results/live/GOVERNORS.md` | **C** | Modelled (class S) and live on omni-v12; their four-ways tables carry 113 LOSS rows against Omni-Compass's own native, 101 of them without a cause written | Their runs on the engine that stands; a cause for every row |
| 16 | The card, an A10 on omni-v23 | `results/gpu/V23_A10_*_ABC.md`, `results/TWO_BILLS.md` | **B** | At the power cap's full load the energy for each request served reads GAIN in all three of our runs (class P, the card's own meter); requests served, the response times and the work for each dollar read "the runs disagree" (of its 13 gauges 7 GAIN, 1 STEADY, 5 the runs disagree); at the cap's usual load 3 GAIN, 7 STEADY, 3 the runs disagree; on the compute run 12 STEADY, 1 the runs disagree | More work for the bill shown, or not, in three runs that agree |
| 17 | The card, an A100 on omni-v21 | `results/gpu/V21_A100_*_ABC.md`, `docs/THE_CHIPS.md` | **C** | At the factory dial STEADY with no write (native already at both knobs' top); the tune-down: work per energy GAIN by the mean of our three runs (beyond the noise in 1 of 3); the cap: 2 gauges LOSS by the mean of our three runs at each of its two loads, none beyond the noise in any run (`V21_A100_CAP_ABC.md`, `V21_A100_CAP_FULL_ABC.md`) | The cap's cause; its run on the engine that stands |
| 18 | The stacked box (three A10 cards, omni-v21) | `results/gpu/V21_STACKS_A10_ABC.md` | **B** | 260 rows: the card STEADY in 63, GAIN in 1, power given in 2, LOSS in 3, the runs disagree in 1, 30 shown and not judged (one repetition a run); the stacks (class S) STEADY in every judged row | The 100 copies run again on their own |
| 19 | Azure, the bill | `results/live/AKS_STEADY_100_OMNI_V18.md`, `scripts/azure_queue.txt` | **Incomplete** | The omni-v18 set: the bill up 1.2% by the mean of 97 pairs, inside the noise, power given, the work not counted. The omni-v21 steady set (run 40940616527, at the tune-down) runs its repetitions one at a time: 73 passed, 25 failed, the 98th running at this grading; the sets at the max with the work meter, which read the work for each dollar, start when it ends | Its table at its end; the failed repetitions' cause (on the open list); the work meter's three runs |
| 20 | Google Cloud, Amazon | `scripts/google_queue.txt`, `scripts/amazon_queue.txt`, `cloud-check.yml` | **Not run** | Wired as Azure's sets run; both queues on behind their $0 check, and the check fails every hour for each (12 times each in GitHub's last 100 finished runs): Google's key not stored whole, Amazon's account on the Free plan; nothing rented | Google's key stored whole; Amazon's account on the Paid plan; until then the hourly check's red is expected |
| 21 | The CPU package on bare metal (`cpu-power`) | `tools/run_cpu_power.py` | **Not run** | GitHub's machines are virtual: no frequency governor, no energy meter | A bare-metal machine |
| 22 | The Omni index and the benefit sheet | `results/OMNI_INDEX.md`, `docs/BENEFIT_SHEET.md`, `tools/headline.py` | **A−** | 26 benchmarks, 23 on omni-v21 and 3 on omni-v3; the index GAIN AND LOSS, 5.0% GAIN by its rule (work, speed and machines), 12.9% GAIN on work and speed alone, on real software on GitHub's own machines; every row's words beside its number | The 3 rows on omni-v3; every row on omni-v24 as its tables land |
| 23 | The whole system composed, every layer | `results/WHOLE_SYSTEM.md` | **B+** | A composition across engines and classes, said so on the page | The stacked run that replaces the composition |
| 24 | Every level on one page | `docs/LEVELS.md` | **B** | Nine levels; the cloud has no three-run table; a group of clusters is not run | A cloud three-run table; a run at the group level |
| 25 | The register of every muscle and benchmark | `docs/REGISTER.md` | **A−** | 1,107 muscles in 70 families; 207 numbered rows, 15 written as not yet run | The 15, one or two at a time |
| 26 | The LOSS ledger | `docs/LOSS_LEDGER.md` | **B+** | 163 LOSS rows against Omni-Compass's own native: omni-v21's 50, every one with its cause written; the orchestrators' omni-v12 rows 113, 101 of them without one | A cause for each omni-v12 row, or their runs on the engine that stands |
| 27 | The deviations register and change control | `docs/DEVIATIONS.md`, `docs/CHANGE_CONTROL.md` | **A−** | 98 numbered deviations, each with its amendment; every engine change through a version, omni-v5 to omni-v24 in one table | Hold it |
| 28 | The three manuals | `docs/OMNI_COMPASS_MANUAL.pdf`, `OMNI_COMPASS_OWNERS_MANUAL.pdf`, `OMNI_COMPASS_LIVE_ENGINE_MANUAL.pdf` | **A−** | 660, 2,025 and 320 pages, 77 drawn figures, the faces embedded and checked; the Owner's results chapter, its referee summary and its receipts written from the newest table of each test (`tools/results_chapter.py`); its version table brought through omni-v24 at this grading | Three cross-references in the Owner's and six in the Live Engine Manual still resolve to no section number (the build names them) |
| 29 | The live engine page | `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html` | **A−** | Rebuilt every hour by its own workflow on omni-v24; the heartbeat dial reads the corrected ladder from this grading's push (it had read the ladder of the model's faulty stand-in); the tuning bench, the switchboard, Restore factory, Return to native and the kill switch on the page | Its lights on Omni-Compass's side worn against native (open) |
| 30 | The documentation set and its numbers | `docs/` | **B+** | 154 pages up front, 30 preregistrations, 24 engine pages, 92 pages of history. The number sweep of 2 and 3 November: the front page's modelled section, the Owner's results chapter, the referee summary, the receipts and the work for the bill now written from their records and checked on every push; figures read from the model's faulty stand-in corrected on ten pages, the live page among them; the bill's worked arithmetic recomputed (a $10.9 M said of a $101 M bill is $12 M) | The hand-written pages not yet swept (the version pages; the preregistrations are dated records and keep their readings, with dated notes) |
| 31 | Legal, licensing, the SBOM | `LICENSE`, `NOTICE`, `DISCLOSURES.md`, `REUSE.toml`, `sbom/` | **A** | The notice on 1,742 files, 0 problems; SPDX on every file | Hold it |
| 32 | Security | `results/SECURITY_SCAN.json`, `docs/THREAT_MODEL.md` | **B+** | 50,895 lines scanned: 2 high, 39 medium, 410 low, every finding reviewed; the two high findings the operator's own commands run through a shell only when they hold a pipe, a redirect or a variable | A command form of its own for those two, as a version |
| 33 | Tests and the verify check | `tests/`, `verify.py`, `tools/release_manifest.py` | **A−** | 789 unit cases, 68 function-test files, 14 parity files; 149 checks PASS at the last receipt; the safety shield's four properties held over 2,000,000 cases run on their own on 3 November (0 violations) | Engine coverage measured on omni-v24 |
| 34 | Engine coverage | `docs/ENGINE_COVERAGE.md` | **B+** | 71% of the engine's 11,424 statements run under the tests, measured on omni-v23; the eight runners 51% | The runners' coverage raised; a measure on omni-v24 |
| 35 | Continuous checks on GitHub | `.github/workflows/` | **B** | verify green on every push to main. GitHub's last 100 finished runs (04:27 to 18:52 UTC, 3 November): 65 passed, 25 failed, 10 cancelled; of the failures 24 are the hourly Google and Amazon $0 checks (item 20) and 1 a grid run; of the cancellations 8 are Kafka runs stopped at their time limit (item 12) and 2 live-page builds | The Kafka fault fixed; the two clouds' keys |
| 36 | The conductor and the campaign | `.github/workflows/grid.yml`, `scripts/dispatch_grid.py`, `scripts/reruns.txt` | **B** | Ticking every 15 minutes; the omni-v24 campaign running, its grid runs passing; Kafka blocked (item 12); Azure one set at a time behind its $0 check | The campaign's first omni-v24 tables |
| 37 | The raw branch and the archive | `raw`, `archive-run.yml` | **A** | Every finished run swept hourly with its hashes, signed with Sigstore from 31 October | Hold it |
| 38 | Repository hygiene and the branches | `main`, `v11` to `v24`, `v7` to `v10` | **A−** | Every version branch level with main at the last push (2 November), the older five carrying main's tree; the hourly jobs commit to main between pushes | Hold it |
| 39 | The side packages | `reference/`, `omnilab/`, `k8s_fleet/`, `fleet/`, `pilot/`, `hardware/`, `k8s_controlplane/` | **B** | In use, each with its tests; none in the fingerprint | Each named in the register or the levels page for what it is |
| 40 | Omni-Compass 1.0 | — | **Not yet declared** | The engine that stands is published as 1.0 on the founder's word | The founder's word |

## 3. Read whole

The software end carries the proof, and on omni-v21's tables it reads strongly: on real Kubernetes the work and the 95th
percentile read GAIN in all three runs in every single-service test, the index reads 5.0% GAIN (12.9% on work and speed), and
every LOSS row on those tables has its cause written. Three things hold the grade down. First, nothing has landed on omni-v24:
the engine that stands has no three-run table of its own yet, so every result above is a table of an earlier engine, read as
that engine's. Second, a fault: the Kafka wire since omni-v22 never finishes a run, so Kafka has had no table for three
versions; it is the first fix of the next version. Third, the hardware end and the clouds remain thin: one card shows less energy
for each request served in all three runs (P), but no card and no cloud has yet shown more work for the bill; Azure's work-meter
sets wait behind a set that is about to end, and Google and Amazon wait on their keys. The bookkeeping is strong where it is
automated (the fingerprint, the legal notice, the manuals, the archive, the pages now written from their records), and weaker where
a person still has to act (the 101 omni-v12 LOSS rows without a cause, the pages not yet swept, coverage on the engine that stands).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
