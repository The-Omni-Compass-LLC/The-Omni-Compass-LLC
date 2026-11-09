# The report card: every section and piece of the repository, graded on its record

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Graded again on 7 November 2026, evening, on the founder's order ("You need to be A++ repo, and you need to update yourself, push it,
and critique it, and let me see the grading and where it needs to be fixed ... it's got to be on us"), from the repository on main at
the commit this page is pushed with and from GitHub's own run records of the day. The grading of 3 November (on omni-v25) is in this
page's history. The engine that stands is **omni-v26** (`OMNI_V26.json`, digest `75d3c22eed4473b9`, 65 files), landed today:
omni-v25 with one fault fixed in the Kubernetes governor (`docs/OMNI_V26.md`). A second fix, omni-v27 (the conveyance's step sized to
the band, no raise into processor another workload is owed), read no LOSS in its model gate and is **held on its study branch
`v27-convey-study`**, on the founder's order of the same evening ("Don't go so far with a version that you can't carry my GPU and CPU
and Kubernetes and clouds"). Every count in section 1 is computed by `python3 tools/report_card.py` at that commit, never typed;
every reading is the record's own, by the one key (`tools/readings.py`), and names the file that holds it. Which results carry to
omni-v26 because nothing they run has moved is computed by `python3 tools/carry.py` (`results/CARRY.md`). A grading is dated: its
counts and readings are true at its commit, and the next grading replaces them. Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code.
No outside party has reviewed or approved these results.

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
| Engine files in the fingerprint (omni-v26) | 65, 64 of them omni-v25's bytes |
| Unit test cases collected under `tests/` | 863 |
| Function-test files (`tools/function_tests.py --list`) | 68 |
| C++ parity test files (the sealed twins) | 14 |
| Checks in `verify.py --quick` at the receipt's commit (b81a641ea066) | 157 PASS, 0 FAIL |
| GitHub workflows (`.github/workflows/`) | 71 |
| Three-run tables in `results/live/`, all engines | 345 |
| Of them, by engine, newest first | omni-v25: 95; omni-v21: 31; omni-v18: 8; omni-v17: 13; omni-v16: 13 |
| Three-run tables on the engine that stands (omni-v26) | 0 (the newest are omni-v25's) |
| Model gate pages (`results/model_gate/`) | 35 |
| Pages in `docs/` (top level), preregistrations, engine pages, history pages | 162, 31, 26, 125 |
| Drawn figures (`docs/book/figures/`) | 77 |
| The Operator's, Owner's and Live Engine Manuals (PDF pages) | 661, 2,072, 355 |
| Files carrying the legal notice (`tools/legal.py --check`) | 2,036 |
| Muscles in the catalog, in our own models: GAIN, STEADY, LOSS | 1,107: 530, 577, 0 (70 families) |
| Benchmarks on the benefit board, by the engine of their newest table | 26: omni-v25 23, omni-v3 3 |
| LOSS rows against Omni-Compass's own native (the ledger), by engine; of them without a cause written | omni-v25: 281, 74 without (67 more with a cause found and a second suspected, not yet measured); omni-v12: 6, 6 without |
<!-- end of the repository in numbers -->

## 2. The grades, piece by piece

| # | Piece | Where | Grade | The record now | What moves it up |
|---:|---|---|---|---|---|
| 1 | The engine on main, omni-v26 | `omni_controller/`, `OMNI_V26.json`, `docs/OMNI_V26.md` | **A−** | 65 fingerprinted files, 64 of them omni-v25's bytes; one fault fixed (another workload's waiting pods hold native's target); its model gate identical on all 104 readings. No three-run table on it yet | Its Kubernetes tables (the only ones that run again: `results/CARRY.md`) |
| 2 | The C++ twin | `cpp/`, `results/SEAL.json` | **A−** | All 17 twins sealed and proven equal (14 parity test files); untouched by omni-v26 | The store brain's twin (`tools/store_brain.py` is Python only) |
| 3 | The Kubernetes governor | `omni_controller/` | **B+** | On omni-v25's tables the single services read GAIN; the batch and multi-cluster rigs carry LOSS rows, most now caused (the target's flips, fixed in omni-v26; the conveyance's cycle and Koordinator's reclaimed processor, fixed in the held omni-v27 candidate) | omni-v26's three runs; the 74 rows still without a cause; omni-v27 once omni-v26's tables stand |
| 4 | Omni-Compass's own orchestrator, three arms | `omni_orchestrator/`, `results/orchestrator/V21_THREE_ARMS_ABC.md` | **A−** | Work GAIN in all three runs; the table carries to omni-v26 (nothing it runs has moved since omni-v21) | Hold it |
| 5 | Kubernetes, single services | `docs/BENEFIT_SHEET.md` | **A−** (omni-v25) | Steady 30.8% GAIN, power given; faults 25.2%, wandering demand 23.4%, KEDA's HTTP add-on 28.0%, GAIN AND LOSS | Their omni-v26 tables; the LOSS rows of faults and wandering demand caused or fixed |
| 6 | Kubernetes, combined and governed | `docs/BENEFIT_SHEET.md`, `docs/LOSS_LEDGER.md` | **B** | GAIN AND LOSS in each (all four 29.1%, Goldilocks 22.6%, the queue 9.0%, Google 2011 35.3%, KEDA on CPU 9.0%, the noisy neighbour 2.3%); pod start waits and failed requests among the rows still without a cause | Their omni-v26 tables; every LOSS row caused |
| 7 | CruiseKube on top | `results/live/V25_CRUISEKUBE.md` | **C** | 0.9% by the index's rule, GAIN AND LOSS; 3 rows without a cause on omni-v25 (on omni-v21 the governor wrote nothing in 30 repetitions) | Its rows read from omni-v25's files |
| 8 | Robustness: the two-hour run and the kill | `results/live/V25_ROBUST_LONG.md`, `V25_ROBUST_KILL.md` | **C+** | GAIN AND LOSS in both; the kill's failed requests in the 300 s after it read LOSS in all three runs, its cause not yet written | The kill's failed requests traced from its raw files and fixed |
| 9 | PostgreSQL and MySQL | `results/live/V25_PGBENCH*.md`, `V25_SYSBENCH*.md` | **A−** | MySQL 9.5% GAIN, power given; PostgreSQL 1.4% GAIN AND LOSS; both carry to omni-v26 | PostgreSQL's LOSS rows caused |
| 10 | Redis | `results/live/V25_REDIS*.md` | **A−** | 6.8% GAIN, power given; carries to omni-v26 | Hold it |
| 11 | MongoDB (YCSB) | `results/live/V25_YCSB*.md` | **B** | 4.8% GAIN AND LOSS; its service table's LOSS rows not yet caused; carries to omni-v26 | Its LOSS rows caused |
| 12 | Kafka | `results/live/V25_KAFKA*.md` | **A−** | 218.6% GAIN, power given, its first full tables since omni-v22 (the omni-v25 fix); carries to omni-v26 | Hold it |
| 13 | The models: robots, swarms, buildings, grids | `results/live/V25_MUJOCO.md`, `V25_SWARM.md`, `V25_CITYLEARN.md`, `V25_PANDAPOWER.md` | **A−** (class S) | GAIN in each (MuJoCo 3.8%, swarms 2.9%, CityLearn 1.4%, SimBench 5.8%); all carry to omni-v26 | Our own models and independent simulators, never proof: hold them as such |
| 14 | The seven organisms with the real cluster inside (the grid) | `results/grid_v26/`, `scripts/dispatch_grid.py` | **Incomplete** | The benefit sheet still reads omni-v3 here; the grid runs on GitHub's machines, no report of its newer runs written | The grid's report on the engine that stands |
| 15 | The orchestra and the governors live | `results/live/GOVERNORS.md`, `results/live/V25_*_4W_*.md` | **B−** | Live on omni-v25 four ways; their web and queue rows caused (`docs/LOSS_CAUSES_2026-11-06.md`, `docs/LOSS_CAUSES_2026-11-07.md`), the target's flips fixed in omni-v26; Koordinator's four ways only on omni-v12 | omni-v26's four-ways tables; Koordinator's four ways on the engine that stands |
| 16 | The card, an A10 on omni-v23 | `results/gpu/V23_A10_*_ABC.md` | **B** | Energy for each request served GAIN in all three runs at full load (class P); carries to omni-v26 (the card governor's code unchanged since omni-v23) | More work for the bill on the card |
| 17 | The card, an A100 on omni-v21 | `results/gpu/V21_A100_*_ABC.md` | **C** | STEADY at the factory dial; does not carry (`omni_controller/muscles.py` moved since omni-v21) | One run on the card on the engine that stands (the founder's next rental) |
| 18 | The stacked boxes (three A10s on omni-v21; eight A100s on omni-v23) | `results/gpu/V21_STACKS_A10_ABC.md`, `V23_A100_8CARD_STACKS_ABC.md` | **B** | The three-card set: 260 rows, the card STEADY in 63, GAIN in 1, power given in 2, LOSS in 3 (its own table); it does not carry (`omni_controller/muscles.py` moved since omni-v21); the eight-card set's table carries to omni-v26 | The three-card set on the engine that stands |
| 19 | Azure, the bill | `scripts/azure_queue.txt`, `results/TWO_BILLS.md` | **Incomplete** | No three-run table of the bill on a recent engine; sets queued behind the $0 check | Azure's work-meter set's three runs |
| 20 | Google Cloud, Amazon | `scripts/google_queue.txt`, `scripts/amazon_queue.txt` | **Not run** | Wired as Azure's sets run, each behind its own $0 check | The founder's word on each key and plan |
| 21 | The CPU package on bare metal | `tools/run_cpu_power.py` | **Not run** | GitHub's machines are virtual: no frequency governor, no energy meter; the runner's code unchanged, ready | A bare-metal machine |
| 22 | The Omni index and the benefit sheet | `results/OMNI_INDEX.md`, `docs/BENEFIT_SHEET.md` | **A−** | GAIN 20.4% on omni-v25 (work, speed and machines across the real tests); 23 of 26 benchmarks on omni-v25, 3 on omni-v3 | The index on the engine that stands, carried results counted as carried |
| 23 | The whole system composed | `results/WHOLE_SYSTEM.md` | **B+** | A composition across engines and classes, said so | The stacked run that replaces the composition |
| 24 | Every level on one page | `docs/LEVELS.md` | **B** | Nine levels; the cloud has no three-run table; a group of clusters not run | A cloud three-run table; a run at the group level |
| 25 | The register of every muscle and benchmark | `docs/REGISTER.md` | **A−** | 1,107 muscles in 70 families; every benchmark's place written, those not yet run marked so | The ones not yet run, one or two at a time |
| 26 | The LOSS ledger | `docs/LOSS_LEDGER.md` | **B+** | 281 omni-v25 rows against Omni-Compass's own native: 140 with a cause found, 67 with a cause found and a second suspected, 74 with none; omni-v12's 6 without | A cause for each of the 74, the second suspicion measured |
| 27 | Deviations and change control | `docs/DEVIATIONS.md`, `docs/CHANGE_CONTROL.md` | **A−** | Every engine change through a version and its gate; the held omni-v27 kept on its study branch with its gate | Hold it |
| 28 | The three manuals | `docs/OMNI_COMPASS_*MANUAL.pdf` | **A** | 661, 2,072 and 355 pages, rebuilt on omni-v26; every reference resolves; the faces embedded | Hold it |
| 29 | The live engine page | `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html` | **A−** | Rebuilt by its own job; today its headline section lagged one rebase (the verify on 62f1779a70 failed on it) and was written again | Hold it, the page's writers rerun after every rebase |
| 30 | The documentation set | `docs/` | **B+** | 161 pages up front, 31 preregistrations, 26 engine pages; every page naming the engine that stands checked on each push | The cause pages' numbers carried by committed code (item 43) |
| 31 | Legal, licensing, the SBOM | `LICENSE`, `NOTICE`, `DISCLOSURES.md`, `sbom/` | **A** | The notice on 2,032 files, 0 problems | Hold it |
| 32 | Security | `results/SECURITY_SCAN.json`, `docs/THREAT_MODEL.md` | **A−** | Every finding reviewed (unchanged since 3 November) | Hold it |
| 33 | Tests and the verify check | `tests/`, `verify.py`, `tools/release_manifest.py` | **A−** | The unit cases, function-test files and parity files counted in section 1; the release check passes on the commit pushed | Hold it |
| 34 | Engine coverage | `docs/ENGINE_COVERAGE.md` | **B+** | 71% of the engine's statements, measured on omni-v23 | A measure on the engine that stands; the runners raised |
| 35 | Continuous checks on GitHub | `.github/workflows/` | **B−** | verify failed once today on our own push (run 42397521880, the headline section after a rebase): our error, fixed in the next push | Every push green; the page writers rerun after any rebase before a push |
| 36 | The conductor and the campaign | `scripts/dispatch_grid.py`, `scripts/reruns.txt` | **B** | The omni-v26 campaign releases every benchmark again, though 23 of them run exactly the code their tables measured (`results/CARRY.md`) | The campaign releases only the benchmarks that do not carry |
| 37 | The raw branch and the archive | `raw`, `archive-run.yml` | **A** | Every finished run swept with its hashes and signed | Hold it |
| 38 | Branches | `main`, `v7` to `v26`, `gpu-omni-v26` | **A−** | Every version branch level with main at the last push; `v26` and `gpu-omni-v26` made at omni-v26's push | Hold it |
| 39 | The side packages | `reference/`, `omnilab/`, `k8s_fleet/`, `fleet/`, `pilot/`, `hardware/` | **B** | In use, each with its tests; none in the fingerprint | Each named in the register or the levels page |
| 40 | Omni-Compass 1.0 | — | **Not yet declared** | The engine that stands is published as 1.0 on the founder's word | The founder's word |
| 41 | The oversight line (the babysitting tax) | `results/OVERSIGHT.md` | **A−** | Counted in both arms of every Kubernetes receipt and read as one line | Hold it |
| 42 | Results carried where nothing moved | `tools/carry.py`, `results/CARRY.md` | **B+** | New today: each benchmark's newest table, the engine files its runner imports and whether any moved; on omni-v26, 23 carry and 93 run again; checked on every push | The conductor and the index read it (items 36 and 22) |
| 43 | The cause pages' own numbers | `docs/LOSS_CAUSES_2026-11-06.md`, `docs/LOSS_CAUSES_2026-11-07.md` | **B** | Every number names the runs and files it was read from; the 7 November page's numbers are read again by `tools/koordinator_causes.py` (one count corrected by it: the target written 0 to 7 times an arm, not 0 to 13); the 6 November page's scripts were not kept | The 6 November page's reading written as a tool and its numbers read again by it |

## 3. Read whole

**Overall: B+, not A++.** The software end carries the proof and reads strongly on omni-v25's tables: on real Kubernetes the single
services read GAIN, the index reads GAIN 20.4%, Kafka's fault is fixed and its tables read GAIN, and every judged row is shown, LOSS
included. What holds the grade down is on us, not on the software we measured:

1. **Versions faster than the runs.** Three engines stood today (omni-v25, omni-v26 and a held omni-v27), and no three-run table
   has landed on omni-v26. omni-v26 changed one file, the Kubernetes governor, yet the campaign releases every benchmark again; 23 of
   them run exactly the code their tables measured (`results/CARRY.md`). Fixed today: the carry rule, its page and its check, and
   omni-v27 held until omni-v26's tables stand. Next: the conductor releases only what does not carry, and the index says what it
   carried.
2. **Our own push went red.** GitHub's verify on 62f1779a70 failed on one check: the live page's headline section was not written
   again after a rebase onto the page bot's rebuild. Fixed in the next push. From now on the page's writers rerun after any rebase,
   and the full release check runs on the commit that is pushed.
3. **LOSS rows without a cause.** 74 rows on omni-v25 against Omni-Compass's own native have none written, the kill test's failed
   requests among them (LOSS in all three runs); 67 more carry a found cause and a second suspected one, not yet measured.
4. **Cause numbers not yet all carried by code.** The 7 November page's numbers are now read again by a committed tool, which
   corrected one count on it; the 6 November page's scripts were not kept, so a referee cannot yet rerun them. It becomes a tool next.
5. **The hardware end and the clouds remain thin.** One card shows less energy for each request served in all three runs (class P);
   no card and no cloud has yet shown more work for the bill; the A100's tables do not carry; Azure's newer sets are not read;
   Google, Amazon and the CPU on bare metal are not run.
6. **No outside review.** Every result is run and scored by our own code; nothing is implied beyond that.

What is strong is what is automated: the fingerprint, the gate before every engine change, the legal notice, the manuals, the
archive and its signatures, the pages written from their records, and now the carry rule. What is weak is what still waits on a
person or on a run: the rows without a cause, the campaign on the new engine, the hardware and the clouds.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
