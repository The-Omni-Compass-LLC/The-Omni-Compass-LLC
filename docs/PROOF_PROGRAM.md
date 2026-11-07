# The proof program: every benchmark at full size, every open native engine, the referee-grade package

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written 2026-10-07 on the founder's order: the strongest evidence that can be built, at the largest size each platform
allows, on open native engines the industry itself runs, so that the only step left to a buyer is to run the same
harness on their own system and read the same table. This document is the program of record. Each line of it becomes a
preregistration before it runs, then a workflow, then a report with every row shown, losses included, then a line in the
register (`docs/REGISTER.md`) and a chapter in the manual (`docs/OMNI_COMPASS_MANUAL.md`).

## 1. The rules every item obeys

1. **Two arms, no third.** Native is the system on its own controller, as shipped or as its operator set it. Omni is
   Omni-Compass on top of that same controller. Omni never replaces native and is never run alone.
2. **Do no harm.** The organism is never left turning out less than native, nor less healthy (`DISCLOSURES.md`, section 3).
   On the engine that stands, where Omni cannot improve a knob, the knob stays native. The 2% verdict is the engine's
   trigger.
3. **The engine is frozen.** Omni v3 (`OMNI_V3.json`, digest `b53d05449ee04c4b`), the engine of this program's day; the engine that
   stands is now omni-v26 (`OMNI_V26.json`), and every v3 result below is v3's own, never read across engines. Nothing in this program changes a
   rule, a gain, a guard, a preset or a muscle. A change would make the next version and every result would run again.
4. **Preregistered.** Rules frozen on one tuning case, written down and pushed before the untouched cases run.
5. **Three runs, three readings.** A, B and C as separate GitHub runs on the same commit. Every judged row reads
   *GAIN in all three of our runs*, *LOSS in all three of our runs*, *no difference beyond the noise* (with the count of runs it holds in) or *the
   runs disagree*. Never "not confirmed".
6. **Every row shown.** Losses included. A benchmark may be left unpublished; it is never published with rows cut out.
7. **Evidence classes.** P (a physical meter), L (live software), S (our own models). S is never presented as proof.
8. **The clock.** An organism keeps its measured window's clock; a repetition where either arm ended more than 5% of the
   window late is marked OFF THE CLOCK and the window is lengthened for that size on that machine.
9. **Handed back.** Every knob returns to the snapshot taken at the start, checked at the end of every arm.
10. **Raw files kept.** Every artifact archived with the code under `results/live/raw/run-<id>/` with SHA-256 sums.

## 2. The sizes

| Platform | Free size (GitHub) | Paid size | How |
|---|---|---|---|
| Kubernetes, real cluster (kind) | 6 workers, 10 pairs × 3 runs; the seven organisms at 1, 10 and 100 copies | the organisms at 1,000 copies on a rented machine, the window set to keep the clock | `six-kube`, `benchmark-reps`, `big-organism-detached` |
| Kubernetes, simulated nodes (KWOK) | 50, 500 and 1,000 nodes | | `kwok-scale` |
| The modelled organisms | 1, 10, 100 and 500 copies × 1 to 500 runs (the grid) | | `six` |
| Azure's managed Kubernetes | | the largest fleet the allowance gives: 15 workers today (32 cores), 96 at 200 cores once a machine family is granted; the app's ceiling 9 pods a worker | `aks-metered` (`max_workers`, `hpa_max`), `azure-quota` |
| GPU | | one card; one card inside 1,000 copies; eight cards; vLLM serving (Lambda) | `scripts/gpu_*.sh`, `tools/run_hil.py` |
| CPU power, a real meter | | one rented bare-metal machine, RAPL energy counters | to build |
| Drone swarms | 20 drones | 100 and more on a rented machine | **done, A/B/C on v3** (`results/live/V3_SWARM.md`): GAIN in all three of our runs, energy a mission down 7% to 20% (less energy for each mission), missions a charge up 8% to 25%; no near miss in either arm; 100 drones on a rented machine next |
| Databases, messaging, caches, search, storage, big data | the service in a container on a 4-core runner, three untouched workloads each | | `pgbench` done; the rest to build |
| Independent simulators (grid, buildings, robots, batteries, process, water, wind, traffic) | every case the simulator ships | | `pandapower`, `citylearn`, `mujoco` done; the rest to build |

## 3. The benchmarks, in the order they run

Status words: **done** (A, B, C in the repo), **running**, **queued** (dispatched or next in line), **to build** (harness
and preregistration not yet written). Every "to build" item names the open native engine Omni will sit on top of.

### 3.1 Compute, AI and cloud

| # | Benchmark | Native engine | Omni's lever | Gauges | Size and cost | Status |
|---:|---|---|---|---|---|---|
| 1 | Kubernetes, six tests (steady, wandering, all four, fairness, faults, batch) | Kubernetes HPA | replicas, floor, machines | p95, p99, work inside the line, failed requests, machines, declared energy | 10 pairs × 3 runs, free | v1 done; v3 runs A and B in progress |
| 2 | The organisms with the real cluster inside | HPA and the organisms' native settings | every muscle | the cluster's gauges and the organism's work, energy, time over the line, behind its window | 1, 10, 100 copies free; 1,000 on Azure, about $25 | v1 done; v3 10 and 100 done, 1,000 running |
| 3 | Azure managed Kubernetes, steady and burst | Azure's cluster autoscaler and the HPA | the HPA target inside its range, the node pool | the bill (Azure's own machine count), machines, p95, failed requests | 4 workers done (v1); the fleet of 40 workers in nine machine families preregistered and dispatched, waiting on Azure's allowance; about $12 a steady run and $22 a burst run, six runs | v1 done at 4 workers; v3 on the fleet waiting on the allowance; then the same method on AWS (EKS) and Google Cloud (GKE), one cloud at a time, each with its own credential in a GitHub secret and its own allowance (register row 38) |
| 4 | Real traffic traces on Kubernetes (Google cluster trace 2011 first, then the Azure Functions trace, Alibaba later) replayed on kind, KWOK later | Kubernetes HPA and scheduler | replicas, machines | as 1 | free | **Google 2011 done, A/B/C on v3** (`docs/TRACES_PREREGISTRATION.md`, `results/live/V3_TRACE_GOOGLE2011.md`): a day of job submissions turned into the wandering test's schedule by a declared rule, the receipt committed (`results/traces/google2011/`); GAIN in all three of our runs (ten pairs each): p95 down 64% to 67% (less waiting), machines down 7% to 9%, failed requests down 11% to 18%; 0 rows LOSS or power given; the Azure Functions trace next | free | to build, first |
| 5 | Kubernetes with Karpenter-class node scaling and KEDA event-driven scaling underneath | Karpenter or the Cluster Autoscaler; KEDA | the same levers, the autoscaler left in charge of machines | as 1 | free on kind where the autoscaler runs; Azure for the real one | **KEDA done, A/B/C on v3** (`results/live/V3_KEDA_CPU_REQUESTS.md`, `results/live/V3_KEDA_REQUESTS.md`): GAIN in all three of our runs: p95 down 51% to 76% (less waiting), machines down 5.9% to 7.8% with the HTTP add-on; power given in all three of our runs: idle-power energy up 1.0% to 2.6%; Karpenter next on Azure |
| 6 | CPU power with a real meter | Linux cpufreq, schedutil governor | frequency ceiling and power cap inside the governor | energy from RAPL (class P), work, p95 | the founder's own tower or laptop on Linux (free), or one rented bare-metal machine at about $10 for the three runs (GitHub's runners and cloud machines allow neither the governor nor the meter) | **built and preregistered 2026-10-10** (`docs/CPU_POWER_PREREGISTRATION.md`, `tools/run_cpu_power.py`): ready for a machine on the metal |
| 7 | GPU: one card; the card inside 1,000 copies; eight cards; vLLM serving (MLPerf-style) | the card's own power limit and clocks; vLLM as shipped | power limit, clock ceiling, admission | the card's own meter (class P), work, p95 | Lambda, about $60 | ready; founder runs |
| 8 | HPC job scheduling | Batsim with EASY backfilling on Parallel Workloads Archive logs | node power-down, admission | makespan, wait, node-hours, energy | free | queued |
| 9 | Robustness, every platform | as the platform | none: the test is of Omni itself | the governor killed mid-run and the lease (seconds to hand back, the 120 s after the kill); the long run (memory, decisions); Omni's own CPU at 1, 10, 100 and 1,000 copies | free (the 24-hour run on a rented machine about $3) | **the kill scenario done, A/B/C on v3** (`results/live/V3_ROBUST_KILL.md`): every setting back within 11 s of the kill (9 s on average) in 30 of 30 repetitions, a second Omni-Compass process to the end, the 120 s after the kill inside the noise; the own-cost table done (`results/live/V3_OWN_COST.md`); **the long run done, A/B/C on v3** (`results/live/V3_ROBUST_LONG.md`, 3 pairs × 7,200 s an arm): memory at most 1.07 of its first ten minutes after two hours (no leak), 97.5% or more of the expected decisions (valid), 1 to 5 failed decisions a run on the cluster's own API 500, held and resumed (shown with the reason), decision time at most 1.30 of its first hour (no growth beyond the 1.5 limit), every setting handed back at the end; the 24-hour run on a rented machine next |

### 3.2 Distribution and specialized

| # | Benchmark | Native engine | Omni's lever | Gauges | Size and cost | Status |
|---:|---|---|---|---|---|---|
| 10 | PostgreSQL behind PgBouncer (pgbench) | the pooler's shipped pool, the DBA's fixed setting | the pool size | work inside the line, p95, connections held, host CPU | free | v3 done |
| 11 | YCSB on Cassandra, MongoDB and Redis; HammerDB TPC-C on MySQL | each store as shipped | the storage engine's cache; pools, admission, replicas | throughput inside the line, p95, resources held, host CPU | free | **MongoDB done, A/B/C on v3** (`results/live/V3_YCSB.md`, the set of record, read again on 24 October): GAIN in all three of our runs on burst and f, the cache held down 10% to 15% (less memory held for the same service); every other row STEADY (40 rows), no LOSS; the first set's larger cuts and its burst-latency LOSS are kept whole in `docs/history/V3_YCSB_set1.md`; **MySQL preregistered and built** (`docs/MYSQL_PREREGISTRATION.md`: the InnoDB buffer pool in the server's own chunks, sysbench's OLTP scripts from Ubuntu's own package, before HammerDB); **MySQL done, A/B/C on v3** (`results/live/V3_SYSBENCH.md`, the set of record, read again on 24 October): every row STEADY on the four untouched workloads (48 rows), 0 GAIN, 0 LOSS; the earlier sets, the pool cuts of the second among them, are kept whole in `docs/history/V3_SYSBENCH_set1.md` to `docs/history/V3_SYSBENCH_set4.md`; the other stores later |
| 12 | Apache Kafka as shipped, a producer at a stepped rate (the OpenMessaging benchmark later) | the operator's fixed consumer count | consumer count inside [1, partitions] | work inside the line, end-to-end p95, lag, consumers held, lost messages, host CPU | free | **done, A/B/C on v3** (`results/live/V3_KAFKA.md`, the set of record, read again on 24 October): 41 rows STEADY on the three untouched workloads and one GAIN in all three of our runs, the consumers held on burst down 0.8% (a fraction of a consumer given back); 0 LOSS; the first set's queue and tail gains, bought with 5.8 to 7.9 consumers, are kept whole in `docs/history/V3_KAFKA_set1.md`; the OpenMessaging benchmark next |
| 13 | Redis as shipped, an application in front with a declared store trip on a miss | the operator's memory ceiling and eviction rule | the memory ceiling inside [16, 512] MB | work inside the line, hit rate, p95, memory held, CPU | free | **done, A/B/C on v3** (`results/live/V3_REDIS.md`, the set of record, read again on 24 October): every row STEADY on the three untouched workloads (36 rows), 0 GAIN, 0 LOSS; the first set's gains, bought with a memory ceiling of 200 to 270 MB against native's 64, are kept whole in `docs/history/V3_REDIS_set1.md`; YCSB on Redis next (row 11) |
| 14 | OpenSearch with Rally | the cluster's own shard allocator | replicas, refresh interval, admission | query p95, indexing throughput, nodes busy | free | to build |
| 15 | Storage with fio | the store's own queue depth and cache | queue depth, admission, power | IOPS, p95, power | free | to build |
| 16 | Spark on TPC-DS | Spark's dynamic allocation | executors, admission | query time, executor-hours | free | to build |
| 17 | Networks | ns-3 data-centre and 5G-LENA cell sleep | pacing, cell sleep | throughput, latency, energy | free | queued |

### 3.3 Energy, facility and industrial

| # | Benchmark | Native engine | Omni's lever | Gauges | Size and cost | Status |
|---:|---|---|---|---|---|---|
| 18 | Power grid, SimBench grids in pandapower | the substation tap changer | the tap setpoint | energy drawn, losses, import, taps, buses outside the band | free | v1 done; v3 queued |
| 19 | Buildings and batteries, CityLearn | CityLearn's rule-based controller | battery setpoints | cost, peak, unevenness, carbon, comfort | free | v1 done; v3 running |
| 20 | Building HVAC and data-centre cooling | BOPTEST baselines; Sinergym on EnergyPlus | setpoints | energy, comfort, time outside the band | free | to build |
| 21 | Battery physics | PyBaMM, CC-CV charging | charge rate | energy throughput, temperature, degradation proxies | free | to build |
| 22 | Microgrids | pymgrid rule-based dispatch | dispatch | cost, unmet load, battery cycling | free | queued |
| 23 | Wind farms | FLORIS, greedy yaw | yaw offsets | farm power | free | queued |
| 24 | Water networks | WNTR/EPANET pump and tank rules | pump schedules | energy, pressure violations | free | queued |
| 25 | Chemical process | Tennessee Eastman, Ricker's controller | setpoints inside limits | cost, constraint violations | free | queued |
| 26 | Transmission and distribution feeders | Grid2Op baselines; OpenDSS regulators | redispatch timing; regulator setpoints | overloads, losses, voltage | free | queued |
| 27 | EV charging | ACN-Sim with ACN-Data | charging rate | energy delivered, peak, deadlines met | free | queued |

### 3.4 Physics, robotics and autonomous

| # | Benchmark | Native engine | Omni's lever | Gauges | Size and cost | Status |
|---:|---|---|---|---|---|---|
| 28 | Robot arms, MuJoCo Menagerie | each robot's shipped position servos | the speed override inside the takt | torque, tracking error, energy per takt, cycles over the line | free | v1 and v3 done |
| 29 | Drone swarms | PX4 and ArduPilot multi-vehicle simulation (the shipped flight code); Crazyswarm; gym-pybullet-drones first | drones airborne at once, cruise and climb margins inside the autopilot's limits, battery reserve, mission admission | missions per charge, late missions, reserve breaches, near misses, energy per mission; collisions zero in both arms or the cell is void | 20 drones free; 100 on a rented machine, about $10 | **done, A/B/C on v3** (gym-pybullet-drones; PX4 and ArduPilot next) |
| 30 | Fixed-wing aircraft | JSBSim | speed and climb margins | fuel, time, envelope violations | free | to build |
| 31 | Spacecraft attitude | Basilisk | wheel effort cap | pointing error, wheel energy | free | queued |
| 32 | Legged robots | MuJoCo Playground, Unitree Go2 | gait speed, effort | energy per metre, falls | free | queued |
| 33 | Driving | highway-env, IDM and MOBIL | speed and spacing margins | travel time, energy, collisions zero | free | queued |
| 34 | Warehouse robot fleets | Open-RMF fleet manager | fleet size in service, task admission | tasks per hour, battery, idle robots | free | to build |
| 35 | Traffic signals | SUMO with RESCO | phase timing | delay, stops, emissions | free | queued |
| 36 | Supply chains | OR-Gym base-stock | order quantities | cost, stockouts | free | queued |
| 37 | Defense edge | K3s on constrained hardware with the Kubernetes six tests | HPA | as 1 | free | to build |
| 38 | Spacecraft attitude, momentum and thrusters | Basilisk: its attitude law, reaction wheels, thruster dumping | wheel effort cap, dump timing, thruster duty | pointing error, wheel energy, propellant, dumps | free | to build |
| 39 | Orbit station-keeping | Orekit, GMAT: the deadband law | deadband timing, burn sizing inside the box | propellant a year; box violations zero | free | to build |
| 40 | Satellite constellations | Basilisk multi-vehicle | fleet power and pointing admission | as 38, fleet-wide | free | to build |
| 41 | Rockets | RocketPy, OpenRocket: air-brake and recovery controllers | brake deployment inside limits | apogee error, loads, recovery margin | free | to build |
| 42 | Combustion and thruster chambers | Cantera: a shipped setpoint loop | setpoints inside the stable band | efficiency, excursions zero, emissions | free | to build |
| - | Pure physics solvers (OpenFOAM, SU2, REBOUND, GADGET, MESA) | none: no controller, no knob | | | | not a benchmark, by design; their HPC cluster is row 8 |

### 3.5 Added 10 October 2026 at the founder's sweep: nothing with value left out

The founder asked that no domain with value be missed, and asked again the same day with cars, self-driving, batteries, nuclear
energy, power plants, medicine and surgery named; the second check is written as `docs/COVERAGE_MAP.md`, every domain against the
register. Aerospace and rockets were already there (the register's rows 32 to 36),
operating systems, television and telecom, satellites and signals, energy, oil and minerals, finance, the platforms and social
media, science and physics, robotics to the top. Each row below is an open benchmark anyone can run, with a shipped controller
for native and one knob for Omni; each gets its own preregistration before its first run; the register's section 4 carries the
same rows (38 to 57) with their owners. Where no open source with a shipped controller is found yet, the row says
"candidate" and names nothing.

| # | Benchmark | Native | Omni's lever | Gauges | Cost | Status |
|---|---|---|---|---|---|---|
| 34 | A second and a third cloud: AWS (EKS) and Google Cloud (GKE), Azure's method unchanged | each cloud's autoscaler and the HPA | the HPA target and the node pool, as on Azure | the bill, machines, p95, failed requests | about $12 a steady and $22 a burst run; free credits cover it where the account's allowance does | queued; each needs its own credential in a GitHub secret and about 90 cores of allowance |
| 35 | The Linux kernel's other knobs: the CPU scheduler, the network stack, memory | the kernel's defaults | the scheduler's slice and migration cost; socket buffers and the queue's target; huge pages and swap | work inside the line, p95, CPU, energy where a meter is present | free (GitHub's machines, as root) | queued; the row-18 harness pattern |
| 36 | Windows processor power management on the founder's own laptop | the Balanced plan | the maximum processor state | work inside the line, p95, battery discharge (a real meter), the processor's counter | free | queued; harness to build |
| 37 | Television and streaming: adaptive bitrate (dash.js) over recorded network traces | the player's own rule | the ladder's cap and the buffer target | rebuffering, bitrate, bytes, switches | free | queued |
| 38 | Telecom: a software 5G cell (srsRAN over ZeroMQ) | the gNB's scheduler and sleep timers | bandwidth part and sleep timers | throughput, latency, modelled radio power | free | queued; the knob to check |
| 39 | Web platforms and social media: the serving layer (nginx, Envoy) and the data layer (LDBC Social Network Benchmark on a graph database) | the servers' own limits; the database's page cache | admission and workers; the page cache size | requests inside the line, p95, CPU, memory | free | queued |
| 40 | Financial trading infrastructure: an open matching engine and a FIX gateway | their shipped pools and throttles | admission and pool sizes | orders a second, p99, rejects (never more) | free | queued; Omni governs machinery, never a trade |
| 41 | Serverless: Knative's own autoscaler on kind with the Azure Functions trace | Knative's autoscaler | the concurrency target | requests inside the line, p95, pods, energy (declared model) | free | queued |
| 42 | Distributed compute: Ray and Dask autoscalers | their autoscalers | minimum and maximum workers | jobs inside the line, worker-hours | free | queued |
| 43 | HPC: Slurm's own power saving in a container cluster; scientific workflows (Nextflow, Snakemake) | Slurm's scheduler and power saving; the executors | suspend timing and admission; parallelism | makespan, wait, node-hours; core-hours | free | queued |
| 44 | Oil, gas and heat networks (pandapipes); one wind turbine (OpenFAST with ROSCO) | their shipped controllers | compressor and pump setpoints; pitch and torque caps | energy, violations zero, deliveries; power, loads | free | queued |
| 45 | Agriculture and irrigation (AquaCrop-OSPy, pyfao56) | the shipped irrigation rule | triggers and amounts | yield, water, stress days | free | queued |
| 46 | Healthcare systems (a FHIR server under load; a MONAI imaging pipeline) | their pools and batch sizes | admission, pool, batch | requests inside the line, p95, CPU; images an hour | free | queued |
| 47 | Robotics: ROS 2 navigation (Nav2 on a TurtleBot in Gazebo); humanoids (MuJoCo Playground); marine vehicles (Stonefish, UUV Simulator) | the shipped controllers and policies | velocity and acceleration limits; speed and effort margins | time to goal, energy, collisions zero; falls zero | free | queued |
| 48 | Mining and mineral processing | a shipped circuit controller | setpoints inside the band | throughput, specific energy, grade | free | candidate: no open source with a shipped controller found yet |
| 49 | Video platforms: transcoding queues (FFmpeg) | the worker pool | parallelism and admission | jobs an hour, queue wait, energy where a meter is present | free | queued |
| 50 | Self-driving stacks: Autoware on CARLA; openpilot in its simulation bridge | the stack's planner and velocity controller | speed, acceleration and jerk margins | trip time, energy, comfort, collisions and near misses zero | free | queued (register row 58) |
| 51 | The EV powertrain: FASTSim on standard drive cycles | the shipped energy management | power split, charge and thermal setpoints | energy a mile, battery stress, range | free | queued (row 59) |
| 52 | Mobility fleets: AMoDeus | the shipped dispatchers | fleet in service, rebalancing rate | wait time, empty distance, energy | free | queued (row 60) |
| 53 | Stream processing: Flink's Kubernetes operator autoscaler | the autoscaler | target utilization, parallelism bounds | lag, p95, task slots | free | queued (row 61) |
| 54 | Storage clusters: Ceph's recovery and scrub throttles | Ceph's balancer and throttles | recovery and backfill limits | client p95, recovery time, IOPS | free | queued (row 62) |
| 55 | AI batch on Kubernetes: Kueue and Volcano with KWOK accelerators | their quotas and admission | admission and quota | job wait, idle accelerator-hours, makespan | free | queued (row 63) |
| 56 | Games: Godot's resolution scale under its frame pacing | the engine's frame pacing | resolution scale, quality tier | frame time inside the line, GPU energy | on the card | candidate (row 64) |
| 57 | Thermal power plants (nuclear as the model only): the open Modelica plant libraries | the plants' shipped controllers | load ramps and setpoints | fuel or energy, thermal stress, excursions zero | free | candidate (row 65) |
| 58 | Semiconductor fabs: the SMT2020 testbed | the shipped dispatching | lot release and admission | cycle time, throughput, work in process | free | candidate (row 66) |
| 59 | Surgical robot simulation: AMBF, SurRoL, the dVRK software | the shipped servos | servo speed and force margins only | task time, tracking error, force breaches zero | free | candidate (row 67) |
| 60 | Kubernetes with Karpenter-class node scaling, the Cluster Autoscaler, KEDA and VPA underneath | each scaler as shipped | the HPA target, the node pool, the event thresholds, the vertical bounds | p95, machines, energy (declared model), failed requests | free on kind with KWOK; Karpenter itself needs a cloud | KEDA done on v3 (row 5); Karpenter, the Cluster Autoscaler and VPA queued (register row 68) |
| 61 | Distributed SQL (CockroachDB, TiDB); the other brokers (RabbitMQ, NATS, Pulsar); CDN caches (Varnish, nginx); observability pipelines (OpenTelemetry Collector, Prometheus) | their shipped rebalancing, flow control, cache size, queue and sampling limits | the YCSB, Kafka, Redis and serving patterns | as those rows | free | queued (rows 69, 70, 71, 73) |
| 62 | Air traffic management: BlueSky with its shipped conflict detection and resolution | the shipped resolution | spacing and admission margins inside the rules | delays, conflicts zero, fuel | free | queued (row 72) |


## 4. The defensibility package

| Item | What it is | Status |
|---|---|---|
| One-command replication kit | from any pushed commit, one command reruns any benchmark above on GitHub and prints the same table; the commit, the engine fingerprint and the raw files' sums are in the table's head | to build |
| Evidence dossier, one per benchmark | preregistration, commit, engine, run ids, raw files and sums, the table, the losses, the index line | mostly in place; to be made uniform and indexed from `docs/REGISTER.md` |
| Reviewer protocol | the written path a human auditor follows from the register to a raw file and back | to write |
| Outside AI readers | ChatGPT and Grok were given results to read (`results/external_review/`); an AI's reading is not an outside review, approved nothing and produces no result | in place |
| Security review of the controllers | what Omni can touch, what it provably cannot, the kill switch, the dead-man lease, the permissions it holds | to write |
| The manual | every chapter above, the wiring stack by stack, the readings, the results, the file map | to rewrite (`docs/OMNI_COMPASS_MANUAL.md`, PDF rebuilt) |

## 5. Schedule and budget

| Weeks | Work | Compute cost |
|---|---|---|
| 1 | finish the running work; Azure at the largest fleet granted; the manual rewrite; traces (4); robustness (9) | about $200 |
| 2 | swarms (29), Kafka (12), YCSB (11), the real meter (6) | about $20 |
| 3 | Redis, OpenSearch, Spark, fio, Karpenter and KEDA (5), BOPTEST (20), PyBaMM (21) | about $20 |
| 4 | the rest of the queue, the replication kit, the reviewer protocol, the security review; the GPU runs on Lambda when the founder gives the go | about $60 |

Build time is the binding cost: two to three days per new benchmark, several in parallel on GitHub. Every result is
pushed as it lands, wins and losses alike, and reported to the founder in plain tables.

## 6. Disclosures

- Omni-Compass is a supervisory governor evaluated on top of native controllers. Nothing here is a production
  deployment, a product warranty, or advice to operate any system.
- Results of class S are models. They are labelled as such everywhere they appear and are never presented as proof.
- Results of class L and P are measured on the named open systems at the named sizes and commits. They do not by
  themselves establish the same effect on any other system; the replication kit exists so that a buyer can establish it
  on theirs.
- Negative and null results are published with the same prominence as positive ones. A benchmark may be withheld by the
  founder; it is never published with rows removed.
- The engine's version fingerprints are bookkeeping. The engine that stands when the founder declares it final is
  published as Omni-Compass 1.0; earlier fingerprints go to `docs/history`.
- All patents, copyrights and trademarks have been filed in the United States by The
  Omni-Compass LLC. Numbers are not given here.
-

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
