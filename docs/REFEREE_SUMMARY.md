# The referee's summary: what Omni-Compass claims, what has been measured, and what is undetermined

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Two pages for a CTO, an engineer, a CFO or an attorney who needs the standing of every claim before reading anything else.
Every number names its engine and its evidence class: L is live software, the real thing; S is our own models, never
proof; P is a physical meter, and there is none yet. Every reading is GAIN, STEADY or LOSS, decided by what the gauge is for,
and holds only when all three of our runs (A, B and C) agree with every 95% interval clear of zero
(`docs/HOW_TO_READ_THE_RESULTS.md`). Beside every gain stands what it cost. Where no proof exists yet, the word is
**undetermined**.

## 1. What it is

A supervisory governor. It sits on top of a system's own controller (Kubernetes' autoscaler, a database's pool, a battery's
controller), reads the system, and moves the same settings native moves, inside bounds the system and its operator set. It
hands every setting back to native's value when it stops, dies or is switched off (`docs/SAFETY_CASE.md`).

## 2. Each claim and its standing

| Claim | Standing | Evidence |
|---|---|---|
| It sits on top of native and never replaces it | **Shown** | Every live test runs native, and Omni-Compass on top of the same native; the setting is read back at native's value at the end of every arm |
| It does no harm: never a LOSS against native | **Shown on omni-v11's counted runs; two faults found since, each fixed in the next version, their runs under way; one row awaits a written ruling** | 0 LOSS rows in the 23 omni-v11 three-run tables (1,039 judged rows: Kubernetes, the robustness kill test and long run, the five data stores, four outside simulators); the omni-v10 LOSS, the pod start wait under KEDA's HTTP add-on, reads STEADY on omni-v11 now that the kind rig pre-pulls the served image (`docs/POD_START_WAIT.md`); on real Kubernetes Omni-Compass's 95th and 99th percentiles were below native's in all 90 paired repetitions (`docs/TAIL_LATENCY.md`). The fault: in the drone swarm (class S) the omni-v11 wire spent the closest-approach margin in the counted cells (no near miss, no collision) and, on a mission draw outside them, let drones collide where native did not; its proximity reflex slowed over a second instead of at once. The fix held every drone outside the keep-out on every draw tried and landed in omni-v12, whose swarm runs judge a collision as a LOSS and fly three draws never flown (`docs/OMNI_V12.md`; `docs/LIMITATIONS.md`, section 3; `results/model_gate/V12_SWARM_REFLEX.md`). The governors' first tables, on omni-v12, read two LOSS rows. KubeRay with the organism alone: the queue 0.6% to 0.8% later and the tail 4% to 13% higher, because CPU limits the conveyance gave stayed on a saturated shared host; fixed in omni-v13 (`docs/OMNI_V13.md`; `docs/BATCH_QUEUE_PREREGISTRATION.md`, amendment 11). Crane: the total pod start wait, a sum of the pods Omni-Compass chose to start and the wait per pod, which the metric-aims audit rules on in writing before any table is read by it |
| More work, faster, on real Kubernetes | **Shown** (L, omni-v10 and omni-v11, each test on its newest table) | See section 3 |
| More work, faster, on databases and caches | **Small or STEADY** (L, omni-v11) | Redis at the operator's ceiling: 4 gauge-rows GAIN at the tune-down, 6 at the max (work inside the line and hit rate up about 1%, for about 2% memory); Kafka 1 GAIN at each objective; MongoDB 1; PostgreSQL and MySQL 0, with every other gauge STEADY; native exactly as shipped: 0 GAIN, 0 LOSS (the knob at its limit on native or untouched). MySQL's update workload reads "the runs disagree" on throughput (±0.4%, a run-level effect: `docs/LIMITATIONS.md`). The runs at the max for MySQL, MongoDB and PostgreSQL are archiving |
| Fewer machines | **Shown in one test** (L, omni-v10) | A queue of jobs: machines in service and node-hours cut 6% to 14%, the machines after the queue finished 10% to 22%, the queue finished STEADY |
| A smaller cloud bill | **Undetermined** | Azure, the engine of 13 October: no difference in the bill (`results/live/AKS_BILL.md`); the Azure sets run one at a time on the engine that stands; Google and Amazon have not run |
| Less energy | **Undetermined** | No physical meter yet; every energy figure in a live test is a declared model, not a measurement |
| More work per watt on a GPU | **Undetermined** | No run on the engine that stands |
| One governor over every muscle and organism | **Modelled** (S) | 1,107 muscles in our own models: 527 GAIN, 580 STEADY, 0 LOSS (`results/realms_v5/REALMS_V5.md`); a few dozen knobs on real systems |
| Its mathematics | **Machine-checked where stated** | 24 of 24 theorems proved by SMT and interval arithmetic on the engine as it executes: the compass law, the plug's clip, the verdict, the invariance of E, I and S, the tracking bound inside the basin and the steps to reach it, the bath's stability (`docs/ENGINE_PROOFS.md`); open: CERT-10 for every fixture, convergence of the whole six-state system (`docs/FORMAL_STATUS.md`) |

## 3. Real Kubernetes, each gain beside its cost (L, three runs of ten pairs, kind on one GitHub runner)

The rows marked omni-v11 are the newest tables; the others are omni-v10's. omni-v23, the engine that stands since 31 October, runs every test again, and each test's three runs on it replace its row as they land (the conductor is running them).

| Test | Gain, the same in all three of our runs | What it cost |
|---|---|---|
| Steady work in steps | 95th percentile cut 64% to 65%; time over the line cut 98% to 100%; alert minutes cut 100% | Machines and node-hours STEADY; CPU used, the governor's own included, −4.3% to −5.2% |
| Demand that wanders | 95th percentile cut 57% to 66%; time over the line cut 38% to 45%; energy cut 0.3% to 0.4% | Machines STEADY; CPU used, the governor's own included, −1.3% to −2.1% |
| The load stepping up and down (all four at once) | Work inside the response line +47% to +79%; 95th percentile cut 56% to 61% | Machines and node-hours STEADY; CPU used, the governor's own included, −0.5% to −2.6% |
| A public day of demand (Google 2011) | 95th percentile cut 56% to 62%; time over the line cut 74% to 77% | Machines STEADY; pods started +120% to +193% (power given); CPU used, the governor's own included, −3.1% to −3.3% |
| Faults injected | 95th percentile cut 54% to 63%; 99th cut 43% to 51% | Replicas +14% to +20% (power given) |
| KEDA's HTTP add-on underneath (omni-v11) | 95th percentile cut 72% to 74%; time over the line cut 98% to 99%; alert minutes cut 100%; replicas cut 11% to 20% | CPU used, the governor's own included, +49% to +57% (shown, not judged: idle processor given to the service); the pod start wait STEADY |
| KEDA on CPU and requests underneath (omni-v11) | 95th percentile cut 52% to 53%; time over the line cut 97% to 100% | CPU used, the governor's own included, +29% to +31% (shown, not judged); replicas +2% to +3% (power given) |
| Goldilocks and the VPA underneath (omni-v11) | 95th percentile cut 61% to 64%; time over the line cut 98% to 100%; alert minutes cut 100%; pods started cut 53% to 61% | CPU used, the governor's own included, +44% to +52% (shown, not judged); parked-worker energy +1.7% to +2.3% (power given) |
| A queue of jobs | Machines cut 6% to 14%; machines after the queue finished cut 10% to 22% | Queue finish time STEADY |
| Fixed capacity (omni-v11) | STEADY at every cap | — |
| A noisy neighbour | Time over the line cut 11%; the neighbour's own rows STEADY | — |
| CruiseKube underneath | STEADY | — |

The processor given in the add-on tests was idle on machines already running. Where machines are billed by the hour, idle
processor put to work costs nothing more unless it raises the machine count, and in these tests the machine count did not
rise. Where processor is billed by use, it is a cost, and the table shows it.

## 4. What is undetermined, and what decides it

- **The cloud bill**: the Azure sets on the engine that stands (one at a time); Google once its key is stored whole; Amazon once its account is on the
  Paid plan.
- **Energy**: a rented machine with the processor's own energy counters and a wall meter.
- **The GPU**: the Lambda runs from one exact commit.
- **Production**: a deployment on a customer's system with their sign-off.
- **Outside review**: no outside party has reviewed, replicated or approved any result here.

## 5. How to check any number yourself

Every table names its runs; `scripts/raw_archive.sh open /run-<id>/` places the run's raw files at the path the table
names, with their SHA-256 sums, and the table's own tool rebuilds the table from them (`tools/confirm_abc.py`,
`tools/redis_abc.py`, and the like). `python3 tools/omni_version.py --commit <sha>` names the engine a run's commit carries.
`python3 verify.py` runs every test and check the repository holds.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
