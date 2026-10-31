# Omni v20: the data stores' wires fixed at their causes

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v20 stood on main on 25 October until omni-v21 landed that evening (`docs/OMNI_V21.md`).

Omni v20 (`OMNI_V20.json`, digest `1df07f8e36a97985`, 62 files) lands on 25 October, 13:24 UTC, under the founder's words of
25 October ("Fix, fix, fix ... The SYS bench, Kafka, whatever ... has got a problem, you got to fucking fix it ... it can be
fixed") and the standing order that every fault found is fixed and lands as the next version, told, not asked. It is omni-v19
(`docs/OMNI_V19.md`) with five of its wires changed: the data stores' runners `tools/run_sysbench.py`, `tools/run_kafka.py`,
`tools/run_ycsb.py`, `tools/run_redis.py` and `tools/run_pgbench.py`. 57 of its 62 files are omni-v19's bytes. The faults were
found by tracing why the Omni index read +4.32% before the 0.5% key of 24 October and +3.397% after it
(`docs/STORE_LOSS_ROOT_CAUSES_2026-10-25.md`): seven data-store rows, each with 0 or 1 of its three runs clear of the noise, that
the new key now counts. Three were faults in our own wiring, two were the test machine. The fixes were read in the store gate
(`tools/store_gate.py`, `results/model_gate/STORE_GATE.md`) before they were committed. The gate's readings are our own model
(evidence class S), never a benchmark result. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed
or approved these results.

## What changed

- **sysbench: the brain reads its own workload.** `status()` counted only `statement/sql/{select,update,insert,delete}`.
  sysbench sends prepared statements, which those counters never see, so the brain read 4.1 statements a second (the harness's
  own monitoring queries) while sysbench sent 999 to 4,198. The compass force and the verdict's work sample were the brain's own
  queries, and it resized the buffer pool blind, 10 to 23 times an arm. Now sysbench connects as its own account (`omni_load`,
  created by `--setup` with rights on `sbtest` only), and the brain reads that account's statements from the per-user summary
  table, prepared ones included (`statement/com/Execute`, `statement/sql/execute`, `execute_sql`, and the four plain ones).
  Every sysbench row, the GAIN rows included, stood on the blind reading and runs again on omni-v20.
- **Kafka: an extra consumer is handed back.** Above the operator's count, the hand-back needed a consumer whose 200 ms poll
  came back empty, which never happens with 8 round-robin partitions: a third consumer allowed after a load peak stayed 170 of 451
  seconds and bought nothing. Now, above the operator's count, calm gives one consumer back while the backlog is within one poll
  round (50 messages a consumer), 30 s after the last change, because every change pauses the whole group. "Idle" is a full
  second with nothing consumed, and a consumer starts busy; no trial starts on the seconds before the producer begins (the
  2→1→2 double rebalance at the start of every arm is gone).
- **YCSB: the cache grows back below native.** Below the operator's size, nothing grew the cache on misses; a give-back trial
  allowed before the working set widened left two arms 64 MB short with misses at 1% or more for 435 of 457 seconds. Now, below
  native, the cache takes 64 MB a second back while misses are 1% or more, up to native's size, and an open give-back trial is
  abandoned. "Full" is WiredTiger's own 80%, or evicting in the last second (it was 90%, a level WiredTiger never holds).
  `serverStatus` is read in full once, then only for the sections the brain reads. mongod's CPU and the harness's are recorded
  apart, steal apart, beside the host's.
- **Redis: the CPU apart.** redis-server's, the App's, the brain's and the sampler's CPU are recorded apart, steal apart, beside
  the host's. The knob's rule is unchanged.
- **pgbench: the same state every arm.** Each arm starts from `pgbench -i` and a CHECKPOINT; the give-back waits 30 s after an
  add-back (5 s before); one aggregate line a second is kept from the per-transaction log. The workflow logs vmstat, iostat and
  PostgreSQL's checkpoints, lock waits and autovacuum into the run's files, so the runner's write stalls (6.2 s of schedule lag
  in a native arm far under capacity on the omni-v16 runs) can be told from the engine.
- **The readers.** `tools/omni_index.py`, `tools/ycsb_abc.py` and `tools/redis_abc.py` prefer the stack's own CPU where a run
  recorded it; older tables read as before (the index stays +3.397% on them).

## The gate

The store gate replays every archived omni arm of the omni-v16 three-run tables, second by second, through omni-v19's wires and
omni-v20's, each with its own verdict fed the recorded cost samples and its own knob, and reads the pair by the gauge's aim. It
is open-loop: it shows what each wire decides on the same seconds, not how the store would have answered.

| Wire | Arms | What omni-v20 does against omni-v19 |
|---|---:|---|
| Kafka | 27 | rebalances in the first 15 s 2.0 → 0, GAIN +100%; writes GAIN +92.9%; seconds below native while short GAIN +100%; seconds above native while calm (light) 37.6 → 6.3, GAIN +83.1% inside the arms' noise; consumers held +0.6%, inside the noise |
| YCSB | 36 | seconds below native while short 38.9 → 2.2, GAIN +94.4%; cache held power given +5.2%; writes power given +76.6% |
| pgbench | 26 | writes GAIN +21.0%; seconds below native while clients waited GAIN +12.7%; pool size =0.4%, under the floor |
| Redis | 9,728 seconds | the two wires decide differently 0 times; the new CPU figures exist only in new runs |
| sysbench | | the decisions cannot be replayed: the archived files hold only the old reading's counter (4.1 to 4.2 a second against sysbench's 999 to 4,198); a short real run reads the new one |

No LOSS on any wire. The YCSB cache rise is a real change of behaviour: the new "full" opens the grow path on seconds that were
slow, missing and evicting, which omni-v19 refused as "slow with room to spare". It is power given, and the replay cannot show
what the extra memory buys; the real runs on omni-v20 read it. One pgbench arm (select, run C rep 3) is left out of the gate
because omni-v19's own replay matched only 32% of its record there; every other arm reproduces its record in 97% or more of the
seconds.

## What runs again

Every benchmark runs again on omni-v20 (`scripts/reruns.txt`, the conductor's campaign from 13:24 UTC on 25 October), the data
stores first in meaning: sysbench, Kafka, YCSB, Redis and pgbench. A fourth pgbench repetition, balancing the arm order against
the runner's drift, is written as a proposed amendment in `docs/POSTGRES_PREREGISTRATION.md`, not yet in force. Tests:
`tests/test_store_wires.py` (each check fails on omni-v19's runners and passes on omni-v20's) and `tests/test_store_gate.py`.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
