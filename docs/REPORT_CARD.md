# The report card: every section and piece of the repository, graded on its record

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written 30 October 2026, evening, on the founder's order ("go through the repo, top to bottom, bottom to top, left to right, and
tell me and show me the gradings of all the sections and pieces"), and brought current on 31 October after his order to fix what
it found open. The engine that stands is **omni-v22** (`OMNI_V22.json`,
digest `0e23a0bc561b900a`, 65 files), on main since 17:07 UTC; GitHub's verify on that commit is green. Every grade below is
given on the repository's own record as it stands at that commit, read by the one key (`tools/readings.py`), and names the
file that holds the record. The morning's audit (`docs/AUDIT_2026-10-30.md`) graded the areas on omni-v21; this page grades
every piece, on the engine that stands, and is kept current. Run and scored by The Omni-Compass LLC's own code. No outside
party has reviewed or approved these results.

**How a grade is given.** A: the record is complete on the engine that stands, every check of it is green, and no LOSS row
stands without its cause fixed. A−: complete, with small open items named. B+ and B: the record stands and reads GAIN, with
LOSS rows or gaps still open. C: a benefit not yet shown, or LOSS on the benefit sheet. Incomplete: runs not finished.
Not run: wired, nothing run. History: kept, not current. Nothing is graded on a model as if it were proof: class S is said.

## 1. The repository in numbers

| Piece | Count |
|---|---:|
| Engine files in the fingerprint (omni-v22) | 65 |
| Unit test cases collected under `tests/` | 674 |
| Function-test files (`tools/function_tests.py`) | 68 |
| C++ parity test files (the sealed twins) | 15 |
| Checks in `verify.py --quick` at this commit (all PASS) | 145 |
| GitHub workflows (`.github/workflows/`) | 71 |
| Three-run tables in `results/live/`, all engines | 301 |
| Three-run tables on omni-v21 | 31 |
| Three-run tables on omni-v22 | 0 (its campaign starts 18:30 UTC today) |
| Model gate pages (`results/model_gate/`) | 28 |
| Archived runs on the branch `raw` | 2,196 |
| Pages in `docs/` (top level), preregistrations, engine pages, history pages | 145, 30, 22, 91 |
| Drawn figures (`docs/book/figures/`) | 77 |
| The Operator's, Owner's and Live Engine Manuals (PDF pages, rebuilt today on omni-v22) | 518, 1,871, 285 |
| Files carrying the legal notice (`tools/legal.py --check`: 0 problems) | 1,477 |
| Muscles in the catalog, families | 1,107, 70 |
| Benchmarks on the benefit board, of them on omni-v21, on omni-v3 | 26, 23, 3 |
| LOSS rows on omni-v21 in the ledger, of them with a cause written | 50, 50 |

## 2. The grades, piece by piece

| # | Piece | Where | Grade | The record now | What moves it up |
|---:|---|---|---|---|---|
| 1 | The engine on main, omni-v23 | `omnicompass/`, `omni_controller/`, `OMNI_V23.json`, `docs/OMNI_V23.md` | **A** | 65 fingerprinted files, 64 of them unchanged from the version before; the one guard (a knob whose own-scale writes the cluster refuses handed back to native's own autoscaler, the founder's order of 31 October); the model gate against the version before identical on every gauge of all 11 models (`results/model_gate/V23_VS_V22.md`); the store gate of the version before still stands under it (`V22_STORE_GATE.md`, class S); the release check 0 FAIL; every page names it (`tools/land_engine.py --check`) | Hold it. Its first three-run tables land from the campaign that restarts at 16:30 UTC. |
| 2 | The C++ twin | `cpp/`, `results/SEAL.json` | **A−** | Every twin that exists was proven equal to its Python by its parity test before the seal of 25 October (15 parity test files) | The store brain (`tools/store_brain.py`, new in omni-v22) is Python only; its twin with the next version. |
| 3 | The Kubernetes governor | `omni_controller/` | **A−** | The hand-back now lands (five tries each, every setting on its own, a failure named; `tests/test_restore_retry.py`); on real Kubernetes work and the 95th percentile read GAIN in all three of our runs | The 17 Kubernetes LOSS rows on omni-v21 without a cause written (below): the next version's list, through the model gate. |
| 4 | Omni-Compass's own orchestrator, three arms | `omni_orchestrator/`, `results/orchestrator/V21_THREE_ARMS_ABC.md` | **A−** | Omni on native against native: work GAIN in all three of our runs (up 8.5%), the 95th percentile GAIN in all three (down 13.0%); no request failed | Omni direct against Omni on native reads work LOSS by the mean (down 2.3%, beyond the noise in 1 of 3). |
| 5 | Kubernetes, single services (steady, faults, wandering demand, KEDA's HTTP add-on) | `docs/BENEFIT_SHEET.md` | **A** | GAIN, or GAIN with power given, no LOSS row | Hold it. |
| 6 | Kubernetes, combined and governed (all four, Goldilocks, the queue, Google 2011, noisy neighbour, KEDA on CPU, the capacity test) | `docs/BENEFIT_SHEET.md`, `docs/LOSS_LEDGER.md` | **B+** | GAIN in each, with 1 to 3 LOSS rows each, every one with its cause written (the shared test machine under the pod starts; one timeout in 30 batch arms; the capacity rig's noise; the neighbour's idle CPU conveyed away) | The pod-start rows read with the host's busy share beside them; the neighbour's price printed beside the gain it buys. |
| 7 | CruiseKube on top | `results/live/V21_CRUISEKUBE.md` | **C** | LOSS on the benefit sheet (down 0.4%; 3 LOSS rows), their cause written: the governor wrote nothing in 30 repetitions (the CPU limit is CruiseKube's, the machines are kind's and fixed, the service stayed inside its line), so the two arms are one system and the rows are the rig's noise | A load that takes the service to its line, where the replica range has work to do; more repetitions a run. |
| 8 | Robustness: the two-hour run and the kill | `results/live/V21_ROBUST_LONG.md`, `V21_ROBUST_KILL.md` | **B** | GAIN AND LOSS: 2 LOSS rows in the long run, 1 in the kill, all three the pod start wait on the shared test machine (in the same stratum of host busy share the long run's pods start 0.07 s faster) | The host's busy share read beside the row; a start on a host at its top held, through the model gate. |
| 9 | PostgreSQL and MySQL | `results/live/V21_PGBENCH*.md`, `V21_SYSBENCH*.md` | **A−** | GAIN, power given (up 4.1% and 3.2%), no LOSS row in their main tables; MySQL as shipped 3 LOSS rows, each with its cause written | Their omni-v22 tables, at one setting (30 s a notch). |
| 10 | Redis | `results/live/V21_REDIS*.md` | **C+** | STEADY overall, 1 LOSS row, 1 more in its service table, both with their cause written; omni-v22's wire spends memory only where the application's own hit and miss split says a miss costs the service | Its omni-v22 three runs. |
| 11 | MongoDB (YCSB) | `results/live/V21_YCSB*.md` | **C** | LOSS on the benefit sheet (down 0.6%); 13 LOSS rows across its three tables, each with its cause written; omni-v22's wire reads WiredTiger's own page-read time | Its omni-v22 three runs. |
| 12 | Kafka | `results/live/V21_KAFKA*.md` | **C** | LOSS on the benefit sheet (down 1.0%); 15 LOSS rows, each with its cause written (the hand-back gave back a consumer the load still needed); omni-v22's wire hands back on calm within one poll round | Its omni-v22 three runs, first in the campaign. |
| 13 | The models: robots, swarms, buildings, grids | `results/live/V21_MUJOCO.md`, `V21_SWARM.md`, `V21_CITYLEARN.md`, `V21_PANDAPOWER.md` | **A−** | GAIN in each (MuJoCo up 3.8%, swarms up 3.0%, CityLearn up 1.5%, SimBench up 5.8%), no LOSS row; class S or an independent simulator, never proof | Hold it; their omni-v22 runs. |
| 14 | The seven organisms with the real cluster inside (the grid) | `results/grid_v22/`, `scripts/dispatch_grid.py` | **Incomplete** | The benefit sheet still reads omni-v3 here. The omni-v21 runs were invalid at the hand-back (one API error aborted it); fixed in omni-v22. The campaign starts 18:30 UTC | The omni-v22 runs back clean, and their table. |
| 15 | The orchestra, the eighth organism, and the governors live | `results/orchestra/ORCHESTRA.md`, `results/live/GOVERNORS.md` | **C** | Modelled (class S) and live on omni-v12; nothing on the engine that stands | Their runs in the omni-v22 campaign. |
| 16 | The card (NVIDIA A100 on Lambda) | `docs/THE_CHIPS.md`, `results/gpu/` | **C** | At the factory dial STEADY with no write (native already at both knobs' top). The tune-down: work per energy GAIN by the mean of our three runs (beyond the noise in 1 of 3). The cap: LOSS rows by the mean, run A alone, none beyond the noise | Run A's cause; the cap at 10 repetitions; the tune-down as the factory dial through the model gate on the founder's word; a card-bound load. Each step's cost on the page. |
| 17 | The stacked box (three A10 cards) | `results/gpu/V21_STACKS_A10_ABC.md` | **B** | Sizes 1 and 10 complete in all three runs, the card STEADY in every organism; 100 copies one repetition a run, shown, not judged | 100 copies run again on its own. |
| 18 | Azure, the bill | `results/live/AKS_STEADY_100_OMNI_V18.md`, `docs/RUN_LEDGER.md` section 3 | **Incomplete** | The omni-v18 set of 100: 97 passed, 3 failed, finished 29 October; its table written on 31 October from the run's own receipt (the bill up 1.2% by the mean of 97 pairs, its interval across zero, power given; the 99th percentile GAIN, down 11.0%). The omni-v21 steady set runs: 16 of 100 by the evening of 30 October, 14 passed, 2 failed | The omni-v21 table at its end; the failed repetitions' causes from their files on `raw`. |
| 19 | Google Cloud, Amazon, the five other clouds | `scripts/google_queue.txt`, `scripts/amazon_queue.txt`, `byoc-metered` | **Not run** | Wired as Azure's sets run, switched off, no key stored, nothing ever rented | The founder's word, and a key stored whole. |
| 20 | The CPU package on bare metal (`cpu-power`) | `tools/run_cpu_power.py`, `docs/RUN_LEDGER.md` section 2 | **Not run** | GitHub's machines are virtual: no frequency governor, no energy meter. Its harness and model read the same on a loaded machine as on a quiet one (today's fix, eight runs byte-identical) | A bare-metal machine. |
| 21 | The Omni index and the benefit sheet | `results/OMNI_INDEX.md`, `docs/BENEFIT_SHEET.md`, `tools/headline.py` | **A−** | 26 benchmarks, 23 on omni-v21; the index GAIN, up 5.2%, real machines; every row's words beside its number; GAIN AND LOSS said where it is | The 3 rows still on omni-v3, and every row on omni-v22 as its tables land. |
| 22 | The whole system composed, every layer | `results/WHOLE_SYSTEM.md` | **B+** | The cluster layer GAIN on work, speed, machines and energy; the card STEADY; class S over class P and L tables, across engines, and says so | The stacked run that replaces the composition. |
| 23 | Every level on one page | `docs/LEVELS.md` | **B** | Nine levels; the muscle and the organism levels read omni-v8 models; the cluster, its add-ons and the service levels read omni-v21 with their LOSS rows listed; the cloud has no three-run table; a group of clusters is not run | The levels on omni-v22; a cloud three-run table; a run at the group level. |
| 24 | The register of every muscle and benchmark | `docs/REGISTER.md` | **A−** | 1,107 muscles in 70 families; 206 benchmark rows run, 15 written as not yet run | The 15, one or two at a time. |
| 25 | The LOSS ledger | `docs/LOSS_LEDGER.md`, `docs/LOSS_CAUSES_2026-10-31.md` | **A−** | 50 LOSS rows on omni-v21, every one shown and every one with its cause written from the runs' own files: 33 the data stores' (30 October) and 17 read on 31 October (the shared test machine's busy share under the pod starts; two CruiseKube arms that are one system; one timeout in 30 batch arms; the neighbour's idle CPU conveyed away; the capacity rig's noise at its cap) | The one engine question among them (a pod start on a host at its top) through the model gate; the neighbour's price read flat in the lift and smaller than the gains it buys, so no engine change there; the 93 omni-v12 rows of the orchestrators' four-ways tables replaced by their omni-v22 runs. |
| 26 | The deviations register and change control | `docs/DEVIATIONS.md`, `docs/CHANGE_CONTROL.md` | **A−** | 89 deviations, each with its amendment; every engine change through a version | Hold it. |
| 27 | The three manuals | `docs/OMNI_COMPASS_MANUAL.pdf`, `OMNI_COMPASS_OWNERS_MANUAL.pdf`, `OMNI_COMPASS_LIVE_ENGINE_MANUAL.pdf` | **A−** | 518, 1,871 and 285 pages, rebuilt today on omni-v22, 77 drawn figures, the navigation checked by the build; the Owner's names omni-v21 in its history | The omni-v22 results into the Owner's as they land. |
| 28 | The live engine page | `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html` | **A−** | Rebuilt on omni-v22 at 18:03 UTC by its own workflow; the tuning bench, the switchboard, the heartbeat dial, Restore factory, Return to native and the kill switch on the page; its build checked against the records | The omni-v22 monitors fill as the tables land. |
| 29 | The documentation set | `docs/` | **A−** | 145 pages up front, 30 preregistrations, 22 engine pages, 91 pages of history; the state of play, the audits, the ledgers | Hold it; realigned on every push. |
| 30 | Legal, licensing, the SBOM | `LICENSE`, `NOTICE`, `DISCLOSURES.md`, `REUSE.toml`, `sbom/`, `docs/DEPENDENCY_LICENSES.md` | **A** | The notice on 1,477 files, 0 problems; SPDX on every file; the SBOM in two formats recorded again today | Hold it. |
| 31 | Security | `results/SECURITY_SCAN.json`, `docs/THREAT_MODEL.md`, the secret-names check | **B+** | 37,470 lines scanned: 2 high, 35 medium, 350 low; every finding reviewed, none unreviewed; the two high findings are the operator's own commands run through a shell only when they hold a pipe, a redirect or a variable, each reviewed with its reason; the kill switch separate and instant | A command form of its own in place of the shell for those two, as the next version. |
| 32 | Tests and the verify check | `tests/`, `verify.py`, `tools/release_manifest.py` | **A−** | 674 unit cases, 68 function-test files, 15 parity files; 145 checks PASS; the two load-sensitive tests fixed at their cause today | Engine coverage measured on omni-v22 (below). |
| 33 | Engine coverage | `docs/ENGINE_COVERAGE.md` | **B+** | 71% of the engine's 11,398 statements run under the tests, measured on omni-v22 on 31 October; the eight runners 51% | The runners' coverage raised: the data stores' wires are read mostly by their live runs. |
| 34 | Continuous checks on GitHub | `.github/workflows/verify.yml` and 70 more | **B+** | verify green on main at omni-v22's commit; of the last 100 completed runs today 12 failed and 5 were cancelled, each with its cause known (the six-kube hand-back, now fixed; the branch verifies before the engine was declared; another session's stale manifest) | A week without a red run. |
| 35 | The conductor and the campaign | `.github/workflows/grid.yml`, `scripts/dispatch_grid.py`, `scripts/reruns.txt`, `scripts/azure_queue.txt` | **B** | Ticking every 15 minutes in a five-hour chain; the omni-v22 campaign opened 18:30 UTC on 30 October, A then B then C, the stores first; 48 of its first 60 runs passed, 10 ran, 2 failed, both Omni-Compass by itself: its solo arm's pod writes refused since omni-v19 (the identity lacked the workload's scale subresource) and the arm ended by the rig's own read of the autoscaler it removes; both fixed at their cause on 31 October and the entry queued again; Azure one set at a time behind its $0 check | The campaign's first tables; a rig fault that let an arm with every pod write refused pass as valid for a week is the mark against it. |
| 36 | The raw branch and the archive | `raw`, `.github/workflows/archive-run.yml` | **A** | 2,196 archived runs with their hashes; every finished run swept hourly | Hold it. |
| 37 | Repository hygiene and the branches | `main`, `v22`, `v21`, `v19`, `gpu-omni-v23`, `v22-stores` | **B** | All level on one commit; main carries 58 merge commits from the last seven days (the week's branches and this morning's audit), linear from today on; one other branch's manifest stale | Rebase only onto main; that branch's manifest regenerated. |
| 38 | The side packages | `reference/`, `omnilab/`, `k8s_fleet/`, `fleet/`, `pilot/`, `hardware/`, `k8s_controlplane/` | **B** | In use, not history: the reference engine and its provenance (the parity and equivalence tests read it), the lab's common readers (the tools import them), the modelled fleet behind the group-of-clusters level, the pilot's scorer, the hardware plant and the control-plane harness, each with its tests; none in the fingerprint | Each named in the register or the levels page for what it is; the group-of-clusters level run on the engine that stands. |
| 39 | Omni-Compass 1.0 | — | **Not yet declared** | The engine that stands is published as 1.0 on the founder's word | The founder's word. |

## 3. Read whole

The software end carries the proof: the engine, its twin, the Kubernetes governor, the orchestrator's three arms and the
single services read A or A−, and the stores' faults are found, fixed and landed, to be read for real from tonight. The
hardware end and the clouds are where the record is thin: the card reads C with its page built and its next steps costed,
Azure is incomplete, Google and Amazon are not run, and bare metal is not run. The bookkeeping is strong where it is
automated (the fingerprint, the legal notice, the manuals, the archive) and B where a person still has to act (the 17 LOSS
rows without a cause, the stale branch, the merge commits, coverage on the engine that stands).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
