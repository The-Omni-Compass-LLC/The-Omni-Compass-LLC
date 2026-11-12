# The census: every run, every file, every table

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Read from both ends, from GitHub's own run records of every workflow that hands in files, read through GitHub's API on 11 November 2026, and the branch raw's tree read the same day. Forward: every run GitHub recorded for the workflows that hand in files, whether it finished, whether its files are on the branch `raw`, which table counts it. Backward: every run a three-run table names, whether its folder is on `raw`. Written by `python3 tools/census.py` from `results/CENSUS_RECORDS.json`; `verify.py` fails a push where the page differs from its records. Counts, not readings: nothing here reads GAIN, STEADY or LOSS.

## 1. The runs GitHub holds

28,225 runs of 53 workflows. 21,838 were skipped: a push that changed no file the workflow watches, so it never started and nothing ran. 395 were cancelled (most waited behind a running set and never started). 5,984 finished: 5,559 succeeded and 425 failed. 8 were still going when the records were read.

## 2. The archive (the branch `raw`)

4,111 run folders holding 4,006,760 files. Every folder carries its checksum list (4,111 of 4,111); 1,423 lists are signed with GitHub's own identity (Sigstore; the signing began on 26 October, and the folders before it carry the checksums alone); 1,495 folders hold a paired receipt (`LIVE_REPS.json`), the rest the files their own test writes (the grid's squares, the organisms, the models).

## 3. Every finished run and its files

Of the 5,984 finished runs, 3,944 have their folder on `raw` (66%). Of the rest, 1,016 still have their files on GitHub (26.1 GB; the first of them expire on 2026-12-26): every one is on the archive's request list, oldest first, and is copied to `raw` by `archive-run.yml` before GitHub lets it go. 1,024 handed in no files at all: a launch refused before anything ran, a set stopped at its login, or a workflow that records its result another way (named below).

| Workflow | Runs | Finished | On `raw` | Files still on GitHub, requested | No files handed in | How it records |
|---|---:|---:|---:|---:|---:|---|
| `six.yml` | 2,241 | 925 | 506 | 318 | 101 | its files, on `raw` |
| `benchmark-reps.yml` | 2,217 | 704 | 583 | 114 | 7 | its files, on `raw` |
| `six-kube.yml` | 735 | 668 | 512 | 154 | 2 | its files, on `raw` |
| `kwok-scale.yml` | 1,368 | 598 | 43 | 16 | 539 | a model of a large cluster: its result is printed in the run and recorded on main |
| `kind-orchestrators.yml` | 362 | 362 | 362 | 0 | 0 | its files, on `raw` |
| `big-organism-detached.yml` | 206 | 204 | 96 | 51 | 57 | its files, on `raw` |
| `engine-runs.yml` | 184 | 184 | 0 | 0 | 184 | commits its record to main (the Python's runs and the core's Monte Carlo) |
| `redis.yml` | 175 | 169 | 139 | 30 | 0 | its files, on `raw` |
| `sysbench.yml` | 157 | 154 | 133 | 21 | 0 | its files, on `raw` |
| `ycsb.yml` | 155 | 151 | 130 | 20 | 1 | its files, on `raw` |
| `robustness.yml` | 139 | 133 | 104 | 29 | 0 | its files, on `raw` |
| `kafka.yml` | 201 | 109 | 84 | 25 | 0 | its files, on `raw` |
| `pgbench.yml` | 114 | 108 | 95 | 13 | 0 | its files, on `raw` |
| `kind-cruisekube.yml` | 113 | 107 | 105 | 2 | 0 | its files, on `raw` |
| `kind-group.yml` | 84 | 84 | 84 | 0 | 0 | its files, on `raw` |
| `realms.yml` | 1,502 | 76 | 51 | 25 | 0 | its files, on `raw` |
| `citylearn.yml` | 75 | 72 | 55 | 17 | 0 | its files, on `raw` |
| `lambda-gpu.yml` | 870 | 71 | 25 | 0 | 46 | its files, on `raw` |
| `mujoco.yml` | 73 | 70 | 57 | 13 | 0 | its files, on `raw` |
| `kind-goldilocks.yml` | 837 | 69 | 69 | 0 | 0 | its files, on `raw` |
| `capacity.yml` | 838 | 66 | 66 | 0 | 0 | its files, on `raw` |
| `cpu-power.yml` | 66 | 66 | 0 | 0 | 66 | hands in its receipt as the run's summary and the record on main |
| `pandapower.yml` | 69 | 66 | 53 | 13 | 0 | its files, on `raw` |
| `realms-v5.yml` | 859 | 66 | 42 | 24 | 0 | its files, on `raw` |
| `kind-addons.yml` | 878 | 65 | 65 | 0 | 0 | its files, on `raw` |
| `swarm.yml` | 66 | 63 | 50 | 13 | 0 | its files, on `raw` |
| `live-kind-levers.yml` | 1,569 | 62 | 47 | 15 | 0 | its files, on `raw` |
| `benchmark.yml` | 1,568 | 61 | 47 | 14 | 0 | its files, on `raw` |
| `live-kind.yml` | 1,567 | 61 | 45 | 16 | 0 | its files, on `raw` |
| `live-kind-full.yml` | 1,566 | 59 | 44 | 15 | 0 | its files, on `raw` |
| `live-shadow.yml` | 1,565 | 58 | 43 | 15 | 0 | its files, on `raw` |
| `injection-grid.yml` | 59 | 53 | 49 | 0 | 4 | its files, on `raw` |
| `aks-metered.yml` | 100 | 39 | 25 | 13 | 1 | its files, on `raw` |
| `orchestrator.yml` | 38 | 38 | 38 | 0 | 0 | its files, on `raw` |
| `kind-godel.yml` | 37 | 37 | 37 | 0 | 0 | its files, on `raw` |
| `kind-crane.yml` | 29 | 29 | 29 | 0 | 0 | its files, on `raw` |
| `big-organism.yml` | 20 | 14 | 6 | 8 | 0 | its files, on `raw` |
| `aks-metered-full.yml` | 15 | 11 | 8 | 3 | 0 | its files, on `raw` |
| `monte-carlo.yml` | 10 | 10 | 0 | 0 | 10 | commits its record to main |
| `eks-metered.yml` | 796 | 8 | 0 | 8 | 0 | its files, on `raw` |
| `orchestra.yml` | 5 | 5 | 5 | 0 | 0 | its files, on `raw` |
| `gke-metered.yml` | 792 | 4 | 0 | 4 | 0 | its files, on `raw` |
| `reproduce.yml` | 4 | 4 | 0 | 0 | 4 | rebuilds a published table from the archive; hands in nothing new |
| `restart-aks.yml` | 5 | 4 | 0 | 4 | 0 | its files, on `raw` |
| `six-pool.yml` | 791 | 4 | 3 | 1 | 0 | its files, on `raw` |
| `kind-vpa.yml` | 3 | 3 | 3 | 0 | 0 | its files, on `raw` |
| `lambda-attach.yml` | 48 | 3 | 1 | 0 | 2 | its files, on `raw` |
| `six-kube-pool.yml` | 746 | 3 | 3 | 0 | 0 | its files, on `raw` |
| `kind-trial.yml` | 2 | 2 | 2 | 0 | 0 | its files, on `raw` |
| `quota-convey-trial.yml` | 2 | 2 | 0 | 2 | 0 | its files, on `raw` |
| `byoc-metered.yml` | 32 | 0 | 0 | 0 | 0 | its files, on `raw` |
| `cloud-organism.yml` | 788 | 0 | 0 | 0 | 0 | its files, on `raw` |
| `gpu-bench.yml` | 1,484 | 0 | 0 | 0 | 0 | its files, on `raw` |

## 4. Backward: every run a table names

The three-run tables' records name 718 runs; 718 have their folder on `raw`. None is missing.


## 5. The engine that stands

On omni-v26: 22 carries, 2 on the engine that stands, 93 runs again (`results/CARRY.md`: a benchmark stands when its three runs on this engine are tabled, carries when no file it runs changed since its last engine, and runs again otherwise; the conductor releases the reruns, A of every benchmark, then B, then C).

## 6. The catalog

1,107 muscles in 70 families (`realms/catalog_v5.csv`); 70 of the 70 families carry their physical wiring (`docs/wiring_recipes.csv`); 364 muscles carry a card of their own (`realms/muscle_cards_v5.csv`, kept only where it won twice and never fell behind native), and every other muscle runs on the engine's setting.

## 7. The website feed

`results/SITE_NUMBERS.json` holds 11 numbers for the site and 9 kept off it (each with the reason), every one with the record it is read from; `results/WEBSITE_SURFACE_CONTRACT.json` names which page may show which, and `verify.py` fails a push where either differs from its records.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
