# Omni-Compass: the state of play as it stood on 10 October 2026 (Omni v3), moved here whole on 16 October

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Moved here whole from `docs/STATE_OF_PLAY.md` on 16 October 2026 when the page was rewritten for the engine that stands (omni-v6). Every number below is Omni v3's, named as such; the tables it cites stay in `results/` under their engine's name and run again on the engine that stands.

## In one paragraph (2026-10-10, Omni v3, every table remade)

**The engine is Omni v3, frozen and fingerprinted** (`OMNI_V3.json`, `docs/OMNI_V3.md`: v1's law and controllers byte
for byte, 945 muscles in 59 families, a do-no-harm gate on speed knobs). Every benchmark runs three times as separate
GitHub runs on it (A the result, B and C the replications) and every judged row reads GAIN in all three of our runs, LOSS in all three of our runs,
no difference beyond the noise, or the runs disagree (`docs/OMNI_V1.md`, the rule). On 10 October every benchmark was run
again on one commit (`3aac0ab7`) and every table below was remade from the new runs; the tables they supersede are whole in
`docs/history`. **Real Kubernetes, seven tests, ten pairs each, all seven the same again in all three of our runs on v3** (`results/live/V3_*.md`):
work inside the response line **+54% to +68%** in all three runs of the all-four test; the 95th percentile **−57% to −66%**
in every run of the steady, wandering, all-four and fault tests; failed requests −11% to −18% where load swings and under
faults; machines −1.7% to −2.0% at steady load and −16% to −20% on the batch queue (−26% to −33% after the queue finished),
with the standby-model energy −11% to −14% there; under the Google trace of 2011 machines −7% to −9% and p95 −64% to −67%;
beside a noisy neighbour no difference beyond the noise on every row. **The five live stacks ran for the first time with the
brain's own verdict on the knob** (the amendments of 9 October: every knob starts in watch and is written only inside the
allowance a paired trial on the stack itself has earned under the index's own reading). What they read. **PostgreSQL**
(`results/live/V3_PGBENCH.md`): connections held open **−6% to −11% on `select`, GAIN in all three of our runs**; the add above the
operator's 20 on `simple_update` refused, as expected; everything else inside the noise; no loss anywhere. **MySQL**
(`results/live/V3_SYSBENCH.md`): the pool held **−10% to −20% on `read_write`, GAIN in all three of our runs**, the pages holding data
with it; the earlier set's memory bought for the written working set is gone; the other three workloads inside the noise.
**MongoDB** (`results/live/V3_YCSB.md`): the cache held **−3% to −13% on `f`, GAIN in all three of our runs**; the other three inside the
noise; no LOSS. **Kafka** (`results/live/V3_KAFKA.md`) and **Redis** (`results/live/V3_REDIS.md`) read exactly nothing:
no gain and no loss, every gauge inside the noise under both objectives, because every spend trial on Kafka (36 of 36 arms)
and most on Redis were abandoned before they could be judged. **That is our wiring, found on the first set and amended the
same day** (amendment 3 in all five preregistrations): the rule of 9 October ended a spend trial when the service turned
calm, and a spend that works calms the service within seconds, so no spend could ever be judged; from amendment 3 a spend
trial runs to its samples, and the five stacks run again on it, those runs becoming the result of record when they land.
**The Omni index on the tables as they stand: +4.8%** (`results/OMNI_INDEX.md`: Kubernetes +28.9% over seven tests,
PostgreSQL +0.8%, Kafka +0.1%, Redis exactly nothing, MongoDB +0.7%, MySQL +1.0%, each category weighed the same); the
service reading **+10.7%** (Kubernetes +84.5%, the five stacks nothing). The number is down from +20.5% because the brain
refused, or could not yet judge, the spends that bought the earlier gains at a resource cost: every gain left is one the
brain proved on the stack itself, and no row anywhere is a loss. **Robustness**: the governor killed outright, every setting
handed back within the allowance in every repetition of every run, the whole window's p95 −27% to −48%; the long run, no
leak, every decision valid, no slowing, the service inside the noise in two of three runs. **The six organisms with the real
cluster inside**: the cluster's p95 lower in all 12 cells (−1% to −52%), failed requests lower in 11. **The realms**: the
published table reproduced in 3 of 3. **The simulators** read as their earlier sets (they are deterministic): power grids 67
gauge-rows toward their aims and 14 LOSS or power given, the districts 71 toward their aims, 33 LOSS or power given and 2 where the runs differ, the robot arms 7 toward their aims with
Gen3 moved and UR5e and iiwa left native, the drone swarms 9 toward their aims and 0 LOSS or power given. The v1 tables stay as the first engine's record.

**What is shown and what is not.** Shown: more work inside the response line on the same machines and a faster tail,
on real Kubernetes, three times on a frozen engine, and again on 10 October; a real database, a buffer pool and a
storage-engine cache each giving memory back for the same service, every notch proved on the stack first; a message queue
and a cache on which the brain's first set could not yet judge a spend (amendment 3, the next set running).
Not yet shown: an energy or cloud-bill saving on real machines. Energy on kind is a declared model (the machines are
containers on one runner); Azure's bill on a 4-worker fleet read no difference beyond the noise on every gauge
(`results/live/V1_AKS_STEADY.md`, `V1_AKS_BURST.md`), which is a fleet too small to show one machine; the fleet of 40
workers in nine machine families that can show one is preregistered and dispatched (`docs/K8S_COMPASS_PREREGISTRATION.md`,
the fleet that can show one machine, amendments 1 to 3), waiting on Azure's own capacity in eastus. The real card has
not run on the current governor; every earlier card result is obsolete and is run again by the founder on rented cards.

**Wire in, or watch (9 October).** The founder's order: Omni need not be wired into every muscle; where it cannot beat
native, the muscle stays native and Omni only reads it. `docs/WIRING_VERDICTS.md` (`tools/wiring_verdicts.py`, checked by
`verify.py` against every table it reads) gives every knob in every result one of three words. Real stacks, on the sets of 10 October: 11 of 24
knob-cases **write** (six of the seven Kubernetes demands, PostgreSQL's `select`, MySQL's `read_write`, MongoDB's `f`, and
Kafka's `heavy` and `burst` on a fraction of a consumer); 0 are **the operator's choice**, because the brain's verdict took
no spend the index would read as a trade; 13 **watch** (Kubernetes beside a noisy neighbour, PostgreSQL's `simple_update` and
`tpcb_hot`, Kafka's `light`, Redis's three, MongoDB's `b`, `c` and `burst`, MySQL's `burst`, `read_only` and `update_index`:
nothing moved the same way in all three of our runs). No real stack carries a loss in all three of our runs on these sets. The simulators: 21 write, 15 trades (the
four SimBench grids that export, where the lower voltage costs line losses; the seven 2023 CityLearn districts, where the bill
read power given), 3 watch (two robots the engine itself left native, one grid where nothing was bought). The 945 modelled muscles:
124 write, 13 trades, 808 watch, 746 of them because the native controller kept the reading in band and the law never wrote;
all 255 admission muscles are among the 746. Of the 12 organism cells with the real cluster inside 12 write on the cluster's gauges
(one with a replica cost beside its gains, one watching). The engine is unchanged; the page decides what an operator connects.

**The brain's own verdict, live (built 9 October; the first set landed 10 October; the second set, on amendment 3, running).** The founder's order of 9 October: the verdict must
be the brain's, in real time, on the knob, before it writes; a knob that cannot prove it pays stays native. `tools/knob_verdict.py`
wraps the frozen engine's verdict (`omnicompass/verdict.py`, unchanged) around every live knob of the five database, messaging
and cache harnesses: the knob starts in watch, a paired trial on the stack itself allows one notch at a time under the declared
objective (resource, the index's reading, or service), a refused step is not taken, a trial holds the knob, a fail-up never
spends beyond the allowance, the operator's setting is always free. Declared as amendments in the five preregistrations with the
expectation written before the runs: Redis left native under the resource objective (the first notch refused), Kafka allowed step
by step while each consumer pays, PostgreSQL's add above the operator's setting refused on simple_update, MySQL's read_write
chunks refused, MongoDB's cache given back a notch a trial. The 21 runs (the five stacks under the resource objective; Redis and
Kafka also under the service objective; three runs each) were dispatched on 10 October at 01:28 to 01:29 UTC on commit `3aac0ab7`
(`docs/RERUN_2026-10-10.md`) and landed by midday: PostgreSQL, MySQL and MongoDB gave memory back where it paid (connections −6% to −11% on `select`;
the pool −10% to −20% on `read_write`; the cache −3% to −13% on `f`) and lost nothing; Kafka and Redis read nothing, because every
spend trial on Kafka and most on Redis were abandoned before they were judged: the rule ended a spend trial when the service turned
calm, and a spend that works calms the service within seconds. Amendment 3 (all five preregistrations, 13:05 UTC) lets a spend
trial run to its samples; the five stacks run again on it, and the result of record is that set. Where the brain's verdict stands today, knob by knob
(the five stacks both ways; the cluster's machines, the card's clock, the robots' speed and the drones' cruise by the engine's own
verdict; the grids, the districts and the 945 modelled muscles by the law alone), is the last table of `docs/WIRING_VERDICTS.md`.
Inside the modelled realms the organism still
takes one directive for every muscle; the verdict per muscle there is the next engine, Omni v4, ordered on 10 October and
designed in `docs/OMNI_V4_PLAN.md` as the collective mechanism (one body, one brain); it is built next and every result is run
again on it.

## Measured on real systems (evidence class L), Omni v3

| Test, ten pairs × three runs | Work | Speed (p95) | Machines | Energy (declared model) | Source |
|---|---|---|---|---|---|
| **Newest: on top of KEDA, Kubernetes with its add-ons** (`docs/ADDONS_PREREGISTRATION.md`): KEDA on the CPU target and the requests in flight | service CPU +24% to +32% (closed-loop load: work shown, not judged); failed requests no difference beyond the noise | **−51% to −53%** (time over the line −97% to −100%) | no difference beyond the noise | idle-power model **+1.0% to +1.6%, power given in all three of our runs**; standby model inside the noise in 1 of 3 runs | `results/live/V3_KEDA_CPU_REQUESTS.md` |
| **Newest: on top of KEDA's HTTP add-on** (the requests in flight alone) | service CPU +45% to +54% (shown, not judged); failed requests no difference beyond the noise | **−73% to −76%** (time over the line −96% to −97%) | **−5.9% to −7.8%, GAIN in all three of our runs** (replicas −14%) | idle-power model **+1.4% to +2.6%, power given in all three of our runs**; standby model −1.6% to −4.2%, inside the noise in 1 of 3 runs | `results/live/V3_KEDA_REQUESTS.md` |
| All four in one run | **+54% to +68%** | −57% to −63% | inside the noise | inside the noise | `results/live/V3_ALL_FOUR.md` |
| Steady work in steps | equal by design | −64% to −66% | **−1.7% to −2.0%** | −1.3% to −1.8% | `results/live/V3_STEADY.md` |
| Demand that wanders | failed requests −12% to −13% | −57% to −64% | inside the noise | idle-power model −0.1% to −0.4% | `results/live/V3_WANDERING.md` |
| A public day of demand: the Google cluster trace of 2011 replayed one step at a time (`docs/TRACES_PREREGISTRATION.md`) | failed requests **−11% to −18%**, GAIN in all three of our runs; no pod ever without a machine | **−64% to −67%** (p99 −60% to −62%) | **−7% to −9%, GAIN in all three of our runs** (replicas −4% to −8%) | standby model **−5% to −7%, GAIN in all three of our runs**; idle-power model −0.3% to −0.4% | `results/live/V3_TRACE_GOOGLE2011.md` |
| Faults: machine down, spike, runaway pod, blind probe | failed requests **−14% to −18%**, GAIN in all three of our runs | −58% to −63% | inside the noise | inside the noise | `results/live/V3_FAULTS.md` |
| A queue of batch jobs | queue finished no difference beyond the noise | mean response −11% to −13% | **−16% to −20%** (−26% to −33% after the queue) | **−11% to −14%** | `results/live/V3_BATCH.md` |
| Fairness, a noisy neighbour | inside the noise on every row | inside the noise | inside the noise | inside the noise | `results/live/V3_FAIRNESS.md` |
| PostgreSQL behind PgBouncer, three workloads (the set of 10 October, the brain's verdict on the pool) | inside the noise | inside the noise | connections held open **−6% to −11% on `select`, GAIN in all three of our runs**; `simple_update` and `tpcb_hot` inside the noise (the add above the operator's 20 refused, as expected) | host CPU inside the noise on all three | `results/live/V3_PGBENCH.md` |
| Apache Kafka, a consumer group's size, three workloads (the set of 10 October, the brain's verdict on the count) | inside the noise | inside the noise | consumers 2 → 1.98 to 1.99, GAIN in all three of our runs by a fraction (the trial's reference seconds); every spend trial abandoned unjudged, the group left at the operator's two: amendment 3, the next set running | inside the noise | `results/live/V3_KAFKA.md`, `results/live/V3_KAFKA_SERVICE.md` |
| Redis, a cache's memory ceiling, three workloads (the set of 10 October, the brain's verdict on the ceiling) | inside the noise | inside the noise | the allowance one notch each way (56 to 72 MB), most trials abandoned unjudged, every gauge inside the noise: amendment 3, the next set running | inside the noise | `results/live/V3_REDIS.md`, `results/live/V3_REDIS_SERVICE.md` |
| MongoDB under YCSB, a database's storage-engine cache size, four workloads (the set of 10 October, the brain's verdict on the cache) | inside the noise on all four; no failed operation | inside the noise on all four | cache size held **−3% to −13% on `f`, GAIN in all three of our runs**; `b`, `c` and `burst` inside the noise | inside the noise | `results/live/V3_YCSB.md` |
| MySQL under sysbench, a database's buffer pool size, four workloads (the set of 10 October, the brain's verdict on the pool) | inside the noise on all four; no error | inside the noise on all four | pool held **−10% to −20% on `read_write`, GAIN in all three of our runs**, the pages holding data with it; `burst`, `read_only` and `update_index` inside the noise; handed back on every omni arm | inside the noise | `results/live/V3_SYSBENCH.md` |
| Robustness: the governor killed outright at 40% of the window, 10 pairs × 3 runs | **every setting back within the allowance in every repetition of every run**; a second governor to the end; failed requests inside the noise | the whole window p95 −27% to −48%, mean response −33% to −40%, time over the line −32% to −36%, GAIN in all three of our runs | inside the noise | inside the noise | `results/live/V3_ROBUST_KILL.md` |
| Robustness: the long run, 7,200 s an arm, 3 pairs × 3 runs | decisions valid in every repetition; failed requests inside the noise | inside the noise in 2 of 3 runs (GAIN in all three of our runs in B) | inside the noise; **no leak** (memory under its limit in every repetition); no slowing; every setting handed back | inside the noise | `results/live/V3_ROBUST_LONG.md` |
| The six organisms with the real cluster inside, 10 and 100 copies, 5 pairs a cell (the set of 10 October) | the organisms' work unchanged | the cluster's p95 lower in all 12 cells (−1% to −52%); failed requests lower in 11 | 6 in both arms (no autoscaler under kind) | the organisms' energy lower in every cell | `results/live/V3_SIX_KUBE.md` (v1 at 1 to 1,000 copies: `V1_SIX_KUBE.md`, `V1_BIG_ORGANISM.md`) |

## Measured on a real cloud (Azure, its own bill), Omni v1

| Test | Reading | Source |
|---|---|---|
| Steady load, 4 workers, 5 pairs | no difference beyond the noise on any gauge; the bill −4.7% with its interval across zero | `results/live/V1_AKS_STEADY.md` |
| A burst sized to the cluster, 4 workers, 5 pairs | the bill +5.0% with its interval across zero; p99 −34% clear of the noise in this one run; the rest inside the noise | `results/live/V1_AKS_BURST.md` |
| The fleet that can show one machine (40 workers, nine families) on v3 | dispatched; two earlier dispatches refused by the subscription's family allowances before any arm ran, the third by Azure's own cluster capacity in eastus; every refusal cost cents and is recorded | `docs/K8S_COMPASS_PREREGISTRATION.md` |

## Modelled (evidence class S: our own models, never counted in the headline), Omni v3

| What | Reading | Source |
|---|---|---|
| The 945 muscles and six organisms, A/B/C | reproduced to the digit in 3 of 3; 0 muscles LOSS or power given; every organism superior within guardrails (work per energy +0.1% to +0.3%) | `results/realms/REALMS.md` |
| The whole tower at 1,000 copies (945,000 modelled muscles) with the real cluster inside, on a rented machine, 3 pairs (v3) | the organism's work unchanged (rounding-level) | the cluster's p95 **6.7 s → 160 ms**, p99 −98%, time over the line **76% → 0**, failed requests **4.8% → 0** | 6 machines in both arms | inside the noise (standby model); the organism's energy −0.4% (model) | `results/live/V3_BIG_ORGANISM.md` |
| The four stacked at 1,000 copies with the real cluster inside, on a rented machine, 3 pairs (v3) | the organism's work unchanged (rounding-level) | the cluster's p95 **2.9 s → 150 ms**, p99 −97%, time over the line **51% → 0**, failed requests **0.14% → 0** | 6 machines in both arms | inside the noise (standby model); the organism's energy −0.4% (model) | `results/live/V3_BIG_ORGANISM.md` |
| The organisms at 1, 10, 100 and 1,000 copies × 1 to 1,000 runs, 84 of 90 cells | every organism superior within guardrails in every cell of 10 runs or more; work per energy +0.07% to +0.37%, the same figure at every size; the six cells left are beyond the machines available | `results/scale/GRID.md` |
| Power grid, 11 SimBench grids in pandapower, A/B/C (v1 and v3 identical) | with ZIP loads energy drawn and net import lower in all 11; losses lower in 7, power given in 4; tap operations fewer in 10, 4 → 8 a year in one (higher, the declared cost) | `results/live/V3_PANDAPOWER.md` |
| Robot arms, MuJoCo Menagerie, A/B/C | Gen3 and Panda: peak torque −29% and −10%, tracking error −21%, energy per takt −0.8% and −0.5%; the Panda's copper +14% higher; UR5e and iiwa left native | `results/live/V3_MUJOCO.md`, `V1_MUJOCO_PANDA.md` |
| CityLearn, every district, A/B/C | electricity bought, peak and unevenness lower in all 11 battery districts, carbon in 8; the bill higher in 7, ramping higher in 7 | `results/live/V3_CITYLEARN.md` |
| Drone swarms, gym-pybullet-drones, 20 drones in three cells, A/B/C | energy a mission −7% to −20% and missions a charge +8% to +25%, GAIN in all three of our runs; no late mission, reserve breach, near miss or collision in any arm | `results/live/V3_SWARM.md` |

## The card (evidence class P)

Every earlier card result ran on a controller since replaced and is obsolete. The one-card, card-inside-the-organisms
and eight-card runs are the founder's, on rented cards, after the CPU and cloud work, at one named commit
(`docs/GPU_RUN_GUIDE.md`, `docs/GPU_PREREGISTRATION.md`).

## Verified in code

| Property | Where |
|---|---|
| The canonical engine is `symmetric_verified`; the printed chart is a named variant, not benchmarked | `docs/CANONICAL_ENGINE.md` |
| Nine laws twinned in C++20 and proven equal to the Python; sealed by fingerprint | `results/SEAL.json`, `tools/seal.py` |
| The conveyance law conserves its budget and converges (proof and 20,000 random systems) | `docs/CONVEYANCE_LAW.md`, `tests/test_conveyance.py` |
| Safety shield: 2,000,000 adversarial cases, 0 violations; C++ engine: 100,000,000 decisions, no failures | `tests/test_shield_properties.py`, `results/SOAK.json` |


## Open

1. **Azure, the fleet that can show one machine**: steady and burst on 40 workers, v3; waiting on Azure's cluster
   capacity in eastus (the only region where this subscription has more than 10 cores). Then B and C.
2. **The four stacked and the tower at 1,000 copies with the real cluster inside, on v3: both done, 3 of 3 on the clock**
   (`results/live/V3_BIG_ORGANISM.md`). The stack: the cluster's p95 2.9 s → 150 ms, time over the line 51% → 0, failed
   requests 0.14% → 0, machines and energy unchanged, 22 s behind a 10,800 s window. The tower (945,000 modelled muscles,
   collected 9 October by run 37945866426 after 25 hours on its rented machine): the cluster's **p95 6.7 s → 160 ms (−98%)**,
   p99 9.1 s → 187 ms, **time over the line 76% → 0, failed requests 4.8% → 0**, all clear of zero; replicas, pods started
   and machines (6 in both arms) the same; energy inside the noise; 14 s behind the window in both arms; the organism's own
   model (shown, never in the index) energy −0.4% and work rounding-level lower by rule. Both machines deleted.
3. **The real card**: the founder's runs on Lambda, one exact commit.
4. **Robustness** (`docs/ROBUSTNESS_PREREGISTRATION.md`, no engine file changes): the kill scenario is done
   (`results/live/V3_ROBUST_KILL.md`: every setting back 7 to 11 s after the kill in 30 of 30 repetitions) and the
   governor's own CPU is tabulated (`results/live/V3_OWN_COST.md`); the long run is done (`results/live/V3_ROBUST_LONG.md`, 3 pairs × 3 runs, 7,200 s an arm: no leak, the decisions valid, no slowing, every setting handed back at the end; service inside the noise in two of three runs);
   the 24-hour run on three rented machines (scenario 2b, started 8 October 10:15 UTC) ends about 10:15 UTC on 10 October and is
   collected by the scheduled collect; the kill and long scenarios were dispatched again on 10 October (`docs/RERUN_2026-10-10.md`).
5. **YCSB on MongoDB, done** (`docs/YCSB_PREREGISTRATION.md`, `results/live/V3_YCSB.md`): the operator's WiredTiger cache
   as native, Omni on the cache size through the server's own console; four smoke runs recorded, then A, B and C on v3; the
   cache held given back by about half on two untouched workloads at no measurable cost in work, p95 or CPU, one loss in all three of our runs
    (the burst mean latency, +2% to +4%) that the second counted set of 9 October removed (item 6); the index spans six
   real categories at +20.5%. Cassandra and Redis under YCSB and HammerDB are next in row 24.
6. **The costs in the database tables, traced and amended with the engine locked** (8 October; `docs/POSTGRES_PREREGISTRATION.md`
   amendment 2, `docs/MYSQL_PREREGISTRATION.md` amendment 2, `docs/YCSB_PREREGISTRATION.md` amendment 1; Omni v3 before and
   after, the harnesses are outside the fingerprint). PostgreSQL's +14% to +28% host CPU was our harness launching a `psql`
   process for every reading (measured: 52 ms of CPU a launch, 7,956 console logins in one workload's pooler log, +55.9 CPU-s
   on the launches against a +52.8 s host difference on a metered repetition; the pooler +1.2 s), and its +15% to +17% median
   latency was the pool shrunk into a queue the pooler itself reported: one console connection an arm and the queue line (a
   server taken back only while clients waited under 1% of the pooler's time, servers added back one per percent of
   waiting, up to the operator's 20). MySQL's read_write pool was bought for slow writes the pool cannot mend (36 of 82 grows at a miss share under
   1%): the pool grows only while missing. MongoDB's memory saving on b, c and burst was a cold cache given back before its
   first eviction (four notches in the first five seconds of every arm) and held at the floor evicting: the give-back gate is
   the miss share, as MySQL's, and the saving may fall to the noise, said beforehand. The second (PostgreSQL, MongoDB) and
   third (MySQL) counted sets run on these rules, dispatched 23:16 UTC on commit `310cf318` (PostgreSQL 37858494179,
   37858496620, 37858499033; MySQL 37858501997, 37858505059, 37858509109; MongoDB 37858512907, 37858515717, 37858519010).
   **Done, 9 October; the earlier tables are whole in `docs/history`.** PostgreSQL: CPU and median latency inside the noise on
   all three workloads, connections −36% to −38% on `select` GAIN in all three of our runs, the runs disagree on `tpcb_hot`, and on
   `simple_update` the add rule of amendment 1 buys connections above the operator's 20 (most at once +72% to +80%,
   power given in all three of our runs, nothing bought): category +4.0% from +14.2%. MongoDB: the cache −21% to −36% on all four workloads,
   GAIN in all three of our runs, the latency cost gone, 8 rows toward their aims and 0 LOSS or power given: category +8.5% from +10.2%. MySQL: burst −49% to −56%
   GAIN in all three of our runs; read_write memory +44% to +52% higher with CPU −4% to −6% lower, a trade; read_only inside the noise
   (its earlier saving was in part the cold-start give-back); update_index disagree: category +5.2% from +12.2%. The index
   headline moves from +24.1% to **+20.5%**: smaller, and every number in it is now a gain without a harness cost under it.
7. **The queue** (`docs/REGISTER.md` section 4, `docs/PROOF_PROGRAM.md`): drone swarms on PX4 and ArduPilot (gym-pybullet-drones done), YCSB on
   Cassandra and Redis and HammerDB, Spark, OpenSearch, fio, Open-RMF, the 24-hour robustness run, Basilisk, Orekit and GMAT,
   RocketPy, Cantera (Kafka and Redis done); one or two at a time, each preregistered.
8. **The gaps the tree shows (the founder's reading, 10 October).** The index's six real categories are the cluster, PostgreSQL,
   Kafka, Redis, MongoDB and MySQL; Azure waits on its three-run close (item 1) and the card on its run on the current controller
   (item 3); the power grids and the districts are in as modelled results, never in the index by rule. Not yet a category: **a second
   and a third cloud**, AWS and Google Cloud under Azure's method (`docs/REGISTER.md` row 38; each needs its own account credential
   in a GitHub secret and an allowance of about 90 cores, about $12 a steady and $22 a burst run, nothing spent until the account
   exists); **CPU power through Linux's own governor with the RAPL meter**: **built and preregistered the same day**
   (`docs/CPU_POWER_PREREGISTRATION.md`; `tools/run_cpu_power.py`, one command `scripts/cpu_power_run.sh`, workflow `cpu-power`,
   the three-run table `tools/cpu_power_abc.py`): the kernel's governor stays native, Omni moves the frequency ceiling on top
   inside [half the top clock, the top], every notch down tried on the machine first by the brain's verdict, energy from the
   processor's own meter and a wall plug where fitted; it waits for a machine on the metal, the founder's own tower or laptop on
   Linux (free) or a rented bare-metal server (about $10), because GitHub's machines are virtual and expose neither the governor
   nor the meter (the workflow's probe says so on every dispatch); **the card's energy meter**, which the card harness already
   has (the integral of the device's power draw, the CPU package by RAPL, the wall plug where fitted, `tools/gpu_reps.py`) and
   which reads on the founder's run. **The founder's sweep of the same day** (nothing with value left out: operating systems,
   television and telecom, satellites and signals, energy, oil and minerals, finance, the platforms and social media, science and
   physics, robotics to the top) added rows 39 to 57 to the register's queue and section 3.5 to the proof program, each an open
   benchmark with a shipped controller for native and one knob for Omni, each to be preregistered before its first run; aerospace
   and rockets were already rows 32 to 36. **The second check the same night** (cars, self-driving, batteries, nuclear, power plants,
   medicine, surgery named) is written as `docs/COVERAGE_MAP.md`: every domain in the world of controllers against the register,
   with the abbreviations (AKS, CPU, UPS, GPU, AWS and the rest) each given its place; it added rows 58 to 73 (self-driving stacks,
   the EV powertrain, mobility fleets, stream processing, storage clusters, AI batch admission, games, thermal plants with nuclear as
   the model only, fabs, surgical robot servos, the other Kubernetes scalers, distributed SQL, the other brokers, CDN caches, air
   traffic, observability pipelines) and wrote the exclusions by rule: safety reserves, clinical dosing, trading decisions, weapons, a
   person's command, solvers without a controller.
9. **Omni-Compass 1.0**: when the founder declares the engine final, v3 as it stands is published as 1.0 and the older
   fingerprints go to `docs/history` as the road to it.

## Where things are

| Path | What it is |
|---|---|
| `docs/OMNI_COMPASS_MANUAL.md` (PDF: `docs/OMNI_COMPASS_MANUAL.pdf`) | the manual: the governor, its mechanism, the wiring stack by stack, the frozen engines, the three-run rule, every result |
| `docs/RERUN_2026-10-10.md` | every benchmark dispatched again on 10 October 2026 on one commit: the record, run by run |
| `docs/OMNI_V3.md`, `docs/OMNI_V1.md` | what each engine is and every result read on it |
| `docs/REGISTER.md`, `docs/PROOF_PROGRAM.md` | every muscle, every benchmark run and still to run; the program to full size |
| `results/live/V3_*.md`, `V1_*.md`, `results/live/raw/` | the three-run tables and every archived run's files |
| `results/OMNI_INDEX.md` | the one combined number |
| `docs/BENEFIT_SHEET.md` | one number per benchmark, plus always toward the system's own aims and minus away from them, whatever the gauge measures; yes, no, none or trade beside it |
| `docs/WIRING_VERDICTS.md`, `results/WIRING_VERDICTS.csv` | which knobs earn a wire in: write, watch or the operator's choice, per knob and per muscle, from every table, every loss with its cause |
| `docs/INTEGRATION_MANUAL.md`, `docs/WIRING_GUIDE.md` | wiring it in yourself |
| `docs/METRICS_CATALOG.md` | every gauge, and whether it is measured or modelled |
| `omnicompass/`, `omni_controller/`, `realms/`, `cpp/` | the engine, the controllers, the muscles, the C++20 twins |
| `docs/HISTORY.md` | earlier states of play, kept whole |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
