# Omni-Compass

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. All patents, copyrights and trademarks filed in the USA. Everything in this repository is subject to change at any time; www.omni-compass.com is the authority of record. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`

**More work, faster, on fewer machines, with less energy, on top of the stack you already run.**

The Omni-Compass LLC · [www.omni-compass.com](https://www.omni-compass.com), the authority of record for Omni-Compass, its
current state and its terms. Every copy, fork, export, report and printout of any part of Omni-Compass carries the notice
above, [`LICENSE`](LICENSE), [`NOTICE`](NOTICE) and [`DISCLOSURES.md`](DISCLOSURES.md) unchanged.

## Latest, newest first

Everything between the markers below is written by the repository itself (`tools/front_page.py`, run by
`.github/workflows/front-page.yml` within minutes of every finished benchmark run, and every hour besides): no person moves
it, and nothing older than the newest result stands in front of it. Earlier front pages are kept whole in `docs/history/`.

<!-- front-page:status:begin -->
- **Engine on main:** omni-v3, fingerprint `b53d05449ee04c4b` (40 files); package 0.3.0. Omni v4 (the reflex rule on every wire) is designed in [`docs/OMNI_V4_PLAN.md`](docs/OMNI_V4_PLAN.md) and not yet built; every result runs again on it when it is.
- **The Omni index now:** +4.8% on the resource reading (work, speed, machines and energy) and +10.7% on the service reading (work and speed), real machines, every test confirmed three times ([`results/OMNI_INDEX.md`](results/OMNI_INDEX.md)).
<!-- front-page:status:end -->

**Tables the repository rebuilt by itself** (the five live products, each from its three newest runs on one engine):

<!-- front-page:begin -->
- 2026-10-10 16:50 UTC: `V3_YCSB` rebuilt from runs 38054777807, 38054782696, 38054787517 (ycsb, the resource objective, omni-v3): 4 untouched workloads; 4 better, 0 worse, 0 disagree
- 2026-10-10 16:50 UTC: `V3_SYSBENCH` rebuilt from runs 38054765202, 38054768832, 38054773573 (sysbench, the resource objective, omni-v3): 4 untouched workloads; 0 better, 0 worse, 0 disagree
- 2026-10-10 16:50 UTC: `V3_REDIS_SERVICE` rebuilt from runs 38054791688, 38054795871, 38054800068 (redis, the service objective, omni-v3): 3 untouched workloads; 5 better, 2 worse, 0 disagree
- 2026-10-10 16:50 UTC: `V3_REDIS` rebuilt from runs 38054731163, 38054735302, 38054739168 (redis, the resource objective, omni-v3): 3 untouched workloads; 0 better, 0 worse, 0 disagree
- 2026-10-10 16:50 UTC: `V3_PGBENCH` rebuilt from runs 38054754511, 38054758150, 38054761503 (pgbench, the resource objective, omni-v3): 3 workloads; 1 better, 1 worse, 1 disagree
- 2026-10-10 16:50 UTC: `V3_KAFKA_SERVICE` rebuilt from runs 38054804459, 38054808912, 38054812962 (kafka, the service objective, omni-v3): 3 untouched workloads; 1 better, 0 worse, 0 disagree
- 2026-10-10 16:50 UTC: `V3_KAFKA` rebuilt from runs 38054742933, 38054746778, 38054750788 (kafka, the resource objective, omni-v3): 3 untouched workloads; 1 better, 0 worse, 0 disagree
<!-- front-page:end -->

**Every result table, by when it last changed:**

<!-- front-page:tables:begin -->
| Last changed (UTC) | Table | Reading |
|---|---|---|
| 2026-10-10 16:50 | [YCSB on MongoDB, a database's operator-set cache size: the A/B/C confirmation](results/live/V3_YCSB.md) | Across 4 untouched workloads: 4 gauge-rows confirmed better, 0 confirmed worse, 0 where the runs disagree. |
| 2026-10-10 16:50 | [sysbench on MySQL, a database's operator-set buffer pool: the A/B/C confirmation](results/live/V3_SYSBENCH.md) | Across 4 untouched workloads: 0 gauge-rows confirmed better, 0 confirmed worse, 0 where the runs disagree. |
| 2026-10-10 16:50 | [Redis, a cache's operator-set memory ceiling: the A/B/C confirmation](results/live/V3_REDIS_SERVICE.md) | Across 3 untouched workloads: 5 gauge-rows confirmed better, 2 confirmed worse, 0 where the runs disagree. |
| 2026-10-10 16:50 | [Redis, a cache's operator-set memory ceiling: the A/B/C confirmation](results/live/V3_REDIS.md) | Across 3 untouched workloads: 0 gauge-rows confirmed better, 0 confirmed worse, 0 where the runs disagree. |
| 2026-10-10 16:50 | [PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C confirmation](results/live/V3_PGBENCH.md) | Across 3 workloads: 1 gauge-rows confirmed better, 1 confirmed worse, 1 where the runs disagree. |
| 2026-10-10 16:50 | [Kafka, a consumer group's operator-set size: the A/B/C confirmation](results/live/V3_KAFKA_SERVICE.md) | Across 3 untouched workloads: 1 gauge-rows confirmed better, 0 confirmed worse, 0 where the runs disagree. |
| 2026-10-10 16:50 | [Kafka, a consumer group's operator-set size: the A/B/C confirmation](results/live/V3_KAFKA.md) | Across 3 untouched workloads: 1 gauge-rows confirmed better, 0 confirmed worse, 0 where the runs disagree. |
| 2026-10-10 16:50 | [The Omni index: more for the same, or the same for less](results/OMNI_INDEX.md) |  |
| 2026-10-10 16:16 | [Public demand traces, turned into load schedules](results/traces/README.md) |  |
| 2026-10-10 16:16 | [The GPU card in simulation: each base alone, and with Omni-Compass on top](results/sim/gpu_two_wire/fresh/RESULT.md) |  |
<!-- front-page:tables:end -->

**Benchmark runs that just finished on GitHub** (a run becomes a result when its three-run set is complete):

<!-- front-page:runs:begin -->
| Finished (UTC) | Benchmark | Outcome | Run |
|---|---|---|---|
| 2026-10-10 19:46 | kwok-scale | success | [38080115336](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/38080115336) |
| 2026-10-10 17:21 | six | success | [38052254140](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/38052254140) |
| 2026-10-10 15:58 | big-organism-detached | success | [38065681492](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/38065681492) |
| 2026-10-10 15:25 | ycsb | success | [38054787517](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/38054787517) |
| 2026-10-10 15:16 | sysbench | success | [38054773573](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/38054773573) |
| 2026-10-10 14:56 | kafka | success | [38054812962](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/38054812962) |
| 2026-10-10 14:53 | pgbench | success | [38054761503](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/38054761503) |
| 2026-10-10 14:52 | redis | success | [38054800068](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/38054800068) |
| 2026-10-10 13:13 | cpu-power | failure | [38054876829](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/38054876829) |
| 2026-10-10 07:15 | robustness | success | [38013471943](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/38013471943) |
<!-- front-page:runs:end -->

**Two names only: native is the system as it runs on its own; omni is Omni-Compass on top of native.** Omni-Compass never
replaces native; every comparison is native against omni.

## The result on real Kubernetes

Omni-Compass on top of native Kubernetes, real clusters, ten paired runs per test, on **Omni v3**, the frozen and
fingerprinted engine ([`docs/OMNI_V3.md`](docs/OMNI_V3.md): v1's law and controllers byte for byte, the muscle catalog grown to 945 and a do-no-harm gate on speed knobs; the v1 tables, [`docs/OMNI_V1.md`](docs/OMNI_V1.md), read the same and stay as the first engine's record). Every test ran three times as separate GitHub runs (A the
result, B and C the replications); a reading below is **confirmed** only when it holds in all three runs with every 95%
interval clear of zero, and otherwise reads no difference beyond the noise. The six tables:
[`V3_ALL_FOUR`](results/live/V3_ALL_FOUR.md), [`V3_STEADY`](results/live/V3_STEADY.md),
[`V3_WANDERING`](results/live/V3_WANDERING.md), [`V3_FAULTS`](results/live/V3_FAULTS.md),
[`V3_BATCH`](results/live/V3_BATCH.md), [`V3_FAIRNESS`](results/live/V3_FAIRNESS.md).

| | native (run A) | omni (run A) | Reading over the three runs |
|---|---:|---:|---|
| **Work handled inside the response line** (all four in one run) | 21.0 req/s | **31.2 req/s** | **+35% to +49% more work on the same machines, confirmed better** |
| **Response time, 95th percentile** (steady, wandering, all four, faults) | 321-820 ms | 111-306 ms | **−47% to −66% in every run of all four tests, confirmed better** |
| **Failed requests** (wandering, all four) | 8.9-12.3% | 7.7-10.9% | **−9% to −14%, confirmed better**; zero in both arms at steady load; under faults lower in all three, clear of the noise in one |
| **Machines in service** | 6 | 5.90 (steady), 4.89 (batch) | steady **−1.5% to −2.9%** and batch **−19% to −23%, confirmed better**; the other tests no difference beyond the noise |
| **Energy** (a declared model: on kind the machines are containers on one runner, so a machine out of service saves modelled watts, not a metered bill) | | | standby model confirmed lower in steady (−1.3% to −2.1%) and batch (−13% to −16%); elsewhere no difference beyond the noise |
| **A noisy neighbour on the same workers** (fairness) | | | no difference beyond the noise on every row, the neighbour's own service included: Omni neither helps nor hurts |
| **Pods left with no machine to take them** | 0 | 0 | same, in every test |

Omni gives a machine back only after a paired trial shows the service is no slower without it (the verdict). On these
clusters one machine fewer made each request 30-45% slower in most trials, so Omni kept the machines and spent them on
speed and work. Earlier engines without that check parked 29-36% of the machines (`docs/history/`); the frozen engine
puts work and speed first.

**Not yet shown**, stated as plainly as the gains: an energy or cloud-bill saving on real machines (Azure's bill did not
move on the earlier engines, [`AKS_BILL`](results/live/AKS_BILL.md) and [`V1_AKS_STEADY`](results/live/V1_AKS_STEADY.md):
every gauge inside the noise), and the current card governor on a real GPU (the one real-card run, on a governor since
replaced, saved 1.6-3.5% of the card's energy and made its 95th percentile 43-84% slower:
[`HIL_RESCORED`](results/hil/run-20261002T082232Z/HIL_RESCORED.md)). The five live products, the index and every row,
losses included, are in [`results/OMNI_INDEX.md`](results/OMNI_INDEX.md), [`docs/BENEFIT_SHEET.md`](docs/BENEFIT_SHEET.md)
and [`docs/WIRING_VERDICTS.md`](docs/WIRING_VERDICTS.md), each rebuilt from the tables by the repository itself.

## The manual: the book for the people who wire it

[`docs/OMNI_COMPASS_MANUAL.pdf`](docs/OMNI_COMPASS_MANUAL.pdf) is Omni-Compass as a printed book, built from the
repository whenever it changes (`docs/book/build_book.py`): front matter with the card for the glove box, the theory of
the mechanism, the wiring instructions level by level and stack by stack (Kubernetes, databases, message brokers, caches,
GPUs, the processor itself, the data center under the servers, robots and drones), operating it, proving it, and back
matter. Its text is [`docs/OMNI_COMPASS_MANUAL.md`](docs/OMNI_COMPASS_MANUAL.md). It is written for the CTO who decides,
the engineer who wires, the operator who runs a data center, and the auditor who checks.

## What is real and what is a model

| Evidence | What runs | Class |
|---|---|---|
| Real Kubernetes on GitHub | Kubernetes itself (API server, scheduler, its own autoscaler), a real web service, real requests, real response times and CPU. The machines are containers on one runner; energy there is a declared formula, not a meter | L |
| Real cloud, Azure AKS | All of the above on real Azure machines, Azure's own autoscaler, Azure's billed machine count | L |
| Real card, NVIDIA A10 on Lambda | The card's power limit and clocks, its own power meter, real GPU work. The first run (2026-10-02) used a card controller since replaced (it answered slower); the current controller's run is next | P |
| The 945 muscles | Software models of real control systems (AI serving, cooling, batteries, robot joints, grids), each from its maker's specification. They show the mechanism; they are labelled as models wherever they appear | S |

## How it works

Omni-Compass is a supervisory governor. It does not replace your autoscaler or your firmware: it sits on top, reads
the meters of each muscle (response time, utilisation, power, heat), holds each muscle's own setting in the middle of
its band with one bounded law, and hands every setting back the moment it stops. As demand rises, the warm machines
take it first; as it falls, the emptiest machine idles first, powered and ready, never switched off, and never below a floor of two (idle). The reset hands every setting back at
the end of a run; the kill switch, a separate security switch, turns Omni-Compass off everywhere at once. The law, its
proof and its wiring: [`docs/MECHANISM_OF_ACTION.md`](docs/MECHANISM_OF_ACTION.md),
[`docs/TRACKING_THEOREM.md`](docs/TRACKING_THEOREM.md), [`docs/CONVEYANCE_LAW.md`](docs/CONVEYANCE_LAW.md).

## Check it yourself

```
pip install -r requirements.txt && python verify.py      # must end: VERIFICATION: PASS
bash scripts/run_live_local.sh 3                          # native against omni on your own kind cluster
sudo bash scripts/gpu_rented_run.sh                       # the card run, on any rented NVIDIA machine
```

`verify.py` reruns every held-out result byte for byte, the Python and C++ twins, the property tests, and checks that
the repository is lined up (`tools/layout_check.py`). Every live result carries its raw files and SHA-256 digests.

## Read next

| For | Read |
|---|---|
| **The register: every muscle wired, every benchmark run, every benchmark still to run** | [`docs/REGISTER.md`](docs/REGISTER.md) |
| **The proof program: every benchmark at full size, every open native engine, the referee-grade package** | [`docs/PROOF_PROGRAM.md`](docs/PROOF_PROGRAM.md) |
| **Omni v3, v2 and v1: the frozen engines, fingerprinted; which version every result ran on; how each is confirmed three times** | [`docs/OMNI_V3.md`](docs/OMNI_V3.md), [`docs/OMNI_V2.md`](docs/OMNI_V2.md), [`docs/OMNI_V1.md`](docs/OMNI_V1.md), `python3 tools/omni_version.py` |
| Every result, every platform, where each stands | [`docs/STATE_OF_PLAY.md`](docs/STATE_OF_PLAY.md), [`results/OMNI_INDEX.md`](results/OMNI_INDEX.md) |
| How to read a result table | [`docs/HOW_TO_READ_THE_RESULTS.md`](docs/HOW_TO_READ_THE_RESULTS.md) |
| The method, written before each run | [`docs/K8S_COMPASS_PREREGISTRATION.md`](docs/K8S_COMPASS_PREREGISTRATION.md), [`docs/GPU_PREREGISTRATION.md`](docs/GPU_PREREGISTRATION.md), [`docs/REALMS_PREREGISTRATION.md`](docs/REALMS_PREREGISTRATION.md) |
| A referee's checklist | [`docs/REFEREE_CHECKLIST.md`](docs/REFEREE_CHECKLIST.md) |
| Every claim with its evidence class, losses kept | [`docs/EVIDENCE_LEDGER.md`](docs/EVIDENCE_LEDGER.md), [`docs/CLAIMS_REGISTER.md`](docs/CLAIMS_REGISTER.md) |
| Due diligence | [`docs/DUE_DILIGENCE.md`](docs/DUE_DILIGENCE.md) |
| The manual (wiring, operating, every result) | [`docs/OMNI_COMPASS_MANUAL.pdf`](docs/OMNI_COMPASS_MANUAL.pdf), [`docs/INTEGRATION_MANUAL.md`](docs/INTEGRATION_MANUAL.md) |
| The 945 muscles | [`docs/MUSCLE_CATALOG.md`](docs/MUSCLE_CATALOG.md) |
| Every command on one page | [`docs/HANDOFF.md`](docs/HANDOFF.md) |

## Repository

| Path | What it is |
|---|---|
| `omnicompass/` | The engine (`core.py`), the compass law (`compass_law.py`), the verdict, the shield, the master switch |
| `omni_controller/` | The live controllers: Kubernetes (`controller.py`) and the card (`gpu_compass.py`) |
| `cpp/` | The C++ twins, sealed equal to the Python laws |
| `realms/` | The 945-muscle catalogue and its models (Omni v2) |
| `scripts/`, `deploy/`, `.github/workflows/` | The benchmarks: kind, AKS, the card, eight cards |
| `tools/` | Report builders, the Omni index, the layout check |
| `results/` | Every result with its raw files and digests |
| `docs/` | Results, method, manual, due diligence |
| `tests/` | The tests `verify.py` runs |

## Find it

Omni-Compass is a **supervisory governor**: a control plane that sits on top of a native controller and never replaces it.
People searching for any of these should find this page: supervisory governor, supervisory control, control plane,
governor, controller, autoscaler, autoscaling, Kubernetes HPA, cluster autoscaler, Karpenter, KEDA, node pool, right-sizing,
conveyance, machinery, engine control, power cap, clock ceiling, DVFS, cpufreq, RAPL, GPU power limit, energy efficiency,
energy per unit of work, data center efficiency, PUE, green computing, FinOps, SRE, SLO, p95, tail latency, do no harm,
paired trial, A/B/C replication, preregistration, Redis maxmemory, Kafka consumer group, PostgreSQL pooler, MySQL buffer
pool, MongoDB WiredTiger cache, HVAC setpoint, building management, chiller plant, UPS, PDU, battery management, microgrid,
grid tap changer, voltage regulator, wind turbine pitch, pipeline compressor, water pump scheduling, robot servo, drone
autopilot, flight software, autonomous driving stack, 5G RAN scheduler, matching engine, game server fleet, build farm,
ledger node, IDS workers, control theory, closed loop, two antagonist forces, tanh law, nervous system, muscles, realms,
organisms, Omni index. The repository's GitHub topics (set by its owner from the About panel, with www.omni-compass.com as its website): `omni-compass`, `governor`, `supervisory-control`, `control-plane`, `control-core`, `control-engine`, `control-theory`, `control-systems`, `feedback-control`, `conveyance`, `machinery`, `autoscaling`, `kubernetes`, `gpu`, `data-center`, `energy-efficiency`, `power-management`, `smart-grid`, `robotics`, `industrial-automation`.

## License

**Proprietary. Evaluation and simulation use only.** You may download, run and modify the software only to evaluate
it and to reproduce the published results, including in shadow or test mode on systems you own or control. Everything
else requires a written **Omni-Compass Enterprise License** signed by The Omni-Compass LLC and paid for. No patent or
trademark license is granted for any other use.

| File | What it says |
|---|---|
| [`LICENSE`](LICENSE) | evaluation and simulation use only; everything else needs a signed, paid Omni-Compass Enterprise License |
| [`NOTICE`](NOTICE) | copyright, the US filings notice, third-party notices |
| [`PATENTS.md`](PATENTS.md) | the nonprovisional utility patent application "The Omni-Compass" filed in the United States (title, inventor, date; the number is withheld on purpose); no patent license is granted |
| [`TRADEMARKS.md`](TRADEMARKS.md) | the Omni-Compass marks; trademark applications filed in the United States |
| [`DISCLOSURES.md`](DISCLOSURES.md) | every declaration, disclosure and disclaimer, made once |
| [`LICENSING_FAQ.md`](LICENSING_FAQ.md) | licensing in plain answers |
| [`.github/CLA.md`](.github/CLA.md) | contributions are assigned to The Omni-Compass LLC |
| [`REUSE.toml`](REUSE.toml), [`sbom/`](sbom), [`.fossa.yml`](.fossa.yml) | machine-readable license declarations for scanners |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. All patents, copyrights and trademarks filed in the USA. Everything in this repository is subject to change at any time; www.omni-compass.com is the authority of record. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
