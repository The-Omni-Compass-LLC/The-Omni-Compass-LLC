# Dated records

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each page here is kept as written on its date. None is current: where one differs from
[`../STATE_OF_PLAY.md`](../STATE_OF_PLAY.md) or [`../../results/OMNI_INDEX.md`](../../results/OMNI_INDEX.md), those govern.

| Page | What it was |
|---|---|
| [`BENCHMARK_REPORT.md`](BENCHMARK_REPORT.md) | The September 2026 benchmark report |
| [`OMNICOMPASS_ABC_REPORT.md`](OMNICOMPASS_ABC_REPORT.md) | Omni-Compass against other cluster platforms, before the on-top design |
| [`OMNICOMPASS_BUYER_EDITION.md`](OMNICOMPASS_BUYER_EDITION.md) | The buyer edition of that report |
| [`CONSENSUS_AUDIT.md`](CONSENSUS_AUDIT.md) | The five-reviewer consensus audit |
| [`ENGINE_AUDIT.md`](ENGINE_AUDIT.md) | The engine read line by line against what runs |
| [`HANDOFF_CHAPTER.md`](HANDOFF_CHAPTER.md), [`HANDOFF_EARLIER.md`](HANDOFF_EARLIER.md) | Earlier handoff notes |
| [`PROBLEM_MAP_2026-09.md`](PROBLEM_MAP_2026-09.md) | The September 2026 problem map |
| [`AMENDMENT_RISING_STEP_CAP.md`](AMENDMENT_RISING_STEP_CAP.md) | A proposed amendment, declined |
| [`V3_SYSBENCH_set1.md`](V3_SYSBENCH_set1.md) | MySQL under sysbench, the first counted set (8 October 2026): every row inside the noise; the hand-back read NO on 15 of 45 omni arms through the plug's restore, fixed and rerun as the second set, which `results/live/V3_SYSBENCH.md` carries |
| [`V3_SYSBENCH_set2.md`](V3_SYSBENCH_set2.md) | MySQL under sysbench, the second counted set (8 October 2026): the pool −67% on burst and −50% to −56% on read_only, read_write's pages holding data +53% to +70% worse; superseded by the third set on amendment 2 (the pool grows only while missing) |
| [`V3_PGBENCH_set1.md`](V3_PGBENCH_set1.md) | PostgreSQL behind PgBouncer, the first counted set (6 October 2026): connections −61% to −72% with host CPU +14% to +28% worse; the CPU was later measured as the harness's own psql launches and the set was superseded by the second on amendment 2 (one console connection, the queue line) |
| [`V3_YCSB_set1.md`](V3_YCSB_set1.md) | MongoDB under YCSB, the first counted set (8 October 2026): the cache −41% to −49% on c and burst with the burst mean latency +2% to +4% worse; the give-back had emptied a cold cache before its first eviction, and the set was superseded by the second on amendment 1 (the miss-share gate) |
| [`V3_STEADY_set1.md`](V3_STEADY_set1.md) | Real Kubernetes, steady work in steps, the first v3 set (7 October 2026): p95 −65% to −66%, machines −1.5% to −2.9%; superseded by the set of 10 October, which `results/live/V3_STEADY.md` carries |
| [`V3_WANDERING_set1.md`](V3_WANDERING_set1.md) | Real Kubernetes, demand that wanders, the first v3 set (7 October 2026); superseded by the set of 10 October |
| [`V3_ALL_FOUR_set1.md`](V3_ALL_FOUR_set1.md) | Real Kubernetes, all four in one run, the first v3 set (7 October 2026): work inside the line +35% to +49%; superseded by the set of 10 October (+54% to +68%) |
| [`V3_FAIRNESS_set1.md`](V3_FAIRNESS_set1.md) | Real Kubernetes, a noisy neighbour, the first v3 set (7 October 2026); superseded by the set of 10 October |
| [`V3_FAULTS_set1.md`](V3_FAULTS_set1.md) | Real Kubernetes, faults, the first v3 set (7 October 2026); superseded by the set of 10 October |
| [`V3_BATCH_set1.md`](V3_BATCH_set1.md) | Real Kubernetes, the batch queue, the first v3 set (7 October 2026): machines −19% to −23%; superseded by the set of 10 October (−16% to −20%) |
| [`V3_TRACE_GOOGLE2011_set1.md`](V3_TRACE_GOOGLE2011_set1.md) | Real Kubernetes under the Google trace of 2011, the first v3 set (8 October 2026); superseded by the set of 10 October |
| [`V3_ROBUST_KILL_set1.md`](V3_ROBUST_KILL_set1.md) | Robustness, the governor killed outright, the first v3 set (8 October 2026): every setting back 7 to 11 s after the kill; superseded by the set of 10 October |
| [`V3_ROBUST_LONG_set1.md`](V3_ROBUST_LONG_set1.md) | Robustness, the long run, the first v3 set (8 October 2026): memory at most 1.07 of its first ten minutes; superseded by the set of 10 October |
| [`V3_REDIS_set1.md`](V3_REDIS_set1.md) | Redis, the first counted set (7 to 8 October 2026), before the brain's verdict on the ceiling: work inside the line +14% to +27% with the ceiling held 64 → 200 to 270 MB, confirmed worse; superseded by the set of 10 October on amendment 2, which read nothing (every spend trial abandoned unjudged), itself to be superseded by the set on amendment 3 |
| [`V3_KAFKA_set1.md`](V3_KAFKA_set1.md) | Apache Kafka, the first counted set (7 October 2026), before the brain's verdict on the group's size: work inside the 500 ms line +16% to +21%, p95 1.6 s → 9 to 14 ms, consumers 2 → 6 to 8, confirmed worse; superseded by the set of 10 October on amendment 2, which read nothing (every spend trial abandoned unjudged), itself to be superseded by the set on amendment 3 |
| [`V3_PGBENCH_set2.md`](V3_PGBENCH_set2.md) | PostgreSQL behind PgBouncer, the second counted set (8 to 9 October 2026, amendment 2): connections −36% to −38% on `select`, the `simple_update` add confirmed worse; superseded by the set of 10 October on the brain's verdict (amendment 3) |
| [`V3_SYSBENCH_set3.md`](V3_SYSBENCH_set3.md) | MySQL under sysbench, the third counted set (8 to 9 October 2026, amendment 2): the pool −49% to −56% on burst, read_write's pages +44% to +52% worse; superseded by the set of 10 October on the brain's verdict (amendment 3) |
| [`V3_YCSB_set2.md`](V3_YCSB_set2.md) | MongoDB under YCSB, the second counted set (8 to 9 October 2026, amendment 1): the cache −21% to −36% on all four workloads; superseded by the set of 10 October on the brain's verdict (amendment 2) |
| [`V3_MUJOCO_set1.md`](V3_MUJOCO_set1.md) | Robot arms, the first v3 set (7 October 2026); superseded by the set of 10 October, the same readings |
| [`V3_PANDAPOWER_set1.md`](V3_PANDAPOWER_set1.md) | Power grids, the first v3 set (7 October 2026); superseded by the set of 10 October, the same table |
| [`V3_CITYLEARN_set1.md`](V3_CITYLEARN_set1.md) | Buildings and batteries, the first v3 set (7 October 2026); superseded by the set of 10 October |
| [`V3_SWARM_set1.md`](V3_SWARM_set1.md) | Drone swarms, the first v3 set (8 October 2026); superseded by the set of 10 October |
| [`V3_SIX_KUBE_set1.md`](V3_SIX_KUBE_set1.md) | The six organisms with the real cluster inside, the first v3 set (7 October 2026); superseded by the set of 10 October |
| [`OMNI_COMPASS_TECHNICAL_MANUAL.pdf`](OMNI_COMPASS_TECHNICAL_MANUAL.pdf) | The earlier technical manual |
| `../../results/scale/receipts/v3-1x_set1.md`, `v3-10x_set1.md`, `v3-100x_set1.md` | The grid receipts of the first v3 runs at 1, 10 and 100 copies (7 to 8 October 2026), kept beside the receipts of 10 October |
| [`xpass/`](xpass) | The earlier XPASS package indexes |
| [`SCENARIOS_30_2026-10-24.md`](SCENARIOS_30_2026-10-24.md), [`SCENARIOS_30_2026-10-24.json`](SCENARIOS_30_2026-10-24.json) | The thirty scenarios of 24 October 2026: ten organisms each native, Omni-Compass on native and Omni-Compass by itself (named direct there), with its 32 LOSS rows, every one Omni-Compass by itself; the third way was taken out by the founder's order of 25 October (Omni-Compass is never by itself), and the record of the two ways that stand is `results/scenarios/SCENARIOS_20.md` |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
