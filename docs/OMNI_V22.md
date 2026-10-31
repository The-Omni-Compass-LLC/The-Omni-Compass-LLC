# Omni v22: the data stores' wires at the max, through each store's own account of a miss

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v22 (`OMNI_V22.json`, digest `0e23a0bc561b900a`, 65 files) stood on main from 30 October to 31 October, 16:30 UTC, when
omni-v23 (`docs/OMNI_V23.md`) landed on it; its runs stand as its own record. It is omni-v21 with the five data stores' wires brought
to the max, the founder's order of 30 October:

> "Anything that has a problem is what your job is ... find out why they went one way or the other and tweak it and turn it and tune
> it to the best possible way for an Omni Compass engine to interact with this as a system governor, convergence control core plane
> that it is ... bring to a solid A mechanism."

The store wires were written on 9 and 10 October with the brain's verdict judging every move under the resource objective, before the
founder's order of 12 October that the max is the default brain, and were never brought to it. On omni-v21 they carried 33 of the 50
LOSS rows (`docs/LOSS_LEDGER.md`); their causes, read from the runs' own files, are on `docs/STORE_ROOT_CAUSES_2026-10-30.md`: the
wall abandoned every spend trial and the fail-up was clamped to the allowance those trials never earned, so in 4,426 of the 4,581
seconds Redis stood over its line the brain asked for memory and was refused, and Kafka's hand-back gave back a consumer the load
still needed.

## The rule, in plain words

| Term | What it is |
|---|---|
| **The max on a store's knob** | The wire's own rule asks; what it asks goes through unclamped, up to the operator's cover, never below native. The resource it takes (memory, consumers, servers) is power given, shown beside what it bought. |
| **The store's own account of a miss** | MySQL: the performance schema's timer on the data files' reads against the workload's statement timer. MongoDB: WiredTiger's time reading pages from disk for the application's threads against the server's own read latency. Redis: the application's own split of each request into hits and misses. Over the last 10 s, the misses' share of the service's own time. |
| **The gate** | Memory is spent only where that share is at least the one key's floor, a half of one percent (`tools/readings.py`): under it the misses are nothing the record could read, so memory could buy nothing it could read, and the knob holds and says why. Where the account is not read this second, nothing is known and nothing is taken. |
| **The host's room** | A notch is taken only while the host keeps 5% of its memory available after it (`/proc/meminfo`, the compass's cushion). Unread, nothing is taken. |
| **The working set's floor** | A hand-back never goes below the most memory the store held in the last 60 s (with the fullness margin, rounded up to a notch), nor below native: a knob handed back into its working set evicts what the service still asks for and buys it back at the store's price. |
| **Kafka's twin and reflex** | Each partition's arrivals (the topic's log-end offsets, once a second) placed on the members by the range assignor; a member's rate learned from the seconds the queue grew; the count goes at once to the smallest one that carries the arrivals and the backlog at nine tenths of a member's rate, never clamped; handed back in one move only to a count that carries the last minute's peak at seven tenths, 30 s after the last change; never below the operator's count; the immune hand-back to native when Omni-Compass's count redlines, stuck, and native's twin reads lower. |
| **PostgreSQL's pool** | A server added while clients wait is never clamped; the pool is never taken below the pooler's own setting. |
| **The dial** | `OMNI_DIAL=save` keeps omni-v21's loop on every wire (the tune-down, where giving the resource back is the aim); every record carries its dial. |
| **The fingerprint** | `tools/store_brain.py` (what the three cache wires share) and `tools/knob_verdict.py` (the tune-down's verdict) join it: no rule of the store wires changes without the version changing. |
| **The hand-back lands** (the Kubernetes governor, the same version) | Every step of the governor's hand-back (the autoscalers' ranges and targets, the operator's own counts, every muscle's lever, the node pool) is tried 5 times against a transient failure of the cluster's API, 1 s apart doubling to 4 s, each on its own, and what did not land is raised and audited, never left silent. On 30 October (six-kube run 41044680505, repetition 346) one 500 from the API on the autoscaler list, at the reset, ended the whole hand-back on its first read: the conveyed CPU limits (1230m, 1850m) and the replica range (1 to 13) stayed behind and the arm was marked invalid. `omni_controller/controller.py` `_persist`, `omni_controller/muscles.py` `_guard_restore`, `RESTORE_TRIES`; `tests/test_restore_retry.py`. |

What was tried and withdrawn: a slope of latency on miss share inside the arms as the price of a miss. It read 0.5 to 1.3 ms a unit
of miss share on MySQL while the controlled comparison across pool sizes read none; the host's noise moves the misses and the latency
together, and a regression reads that as a price. The root-cause page's first reading of the MySQL and MongoDB runs, that a miss cost
the statement nothing, is withdrawn on the same page: the server's own meter, read on a machine of our own, puts the misses at 3% to
32% of what a statement waits for (a tuning-bench reading, class L on that host, no benchmark result).

## Where it is written

| Place | What |
|---|---|
| `tools/store_brain.py` | the working set's floor, the store's account of its misses, the gate, the host's room, the max's record |
| `tools/run_sysbench.py`, `tools/run_ycsb.py`, `tools/run_redis.py` | each cache wire's `Brain`: its own compass law and rule around the shared max; the server's account read each second; the attach check that stops a MongoDB run on a server without the account |
| `tools/run_kafka.py` | the group's twin, the reflex, the hold, the immune hand-back; the tune-down under the dial |
| `tools/run_pgbench.py` | the pool's `Brain`: never clamped upward, never below the pooler's own setting |
| `tools/knob_verdict.py` | the tune-down's verdict, now in the fingerprint; its summary reads the max's records |
| `omni_controller/controller.py`, `omni_controller/muscles.py` | the hand-back that lands: every step tried 5 times against the API's weather, each muscle on its own, what did not land raised |
| `tools/store_gate.py` | the store gate: every candidate replayed on omni-v21's archived seconds (class S) |
| `tools/kafka_model.py`, `tools/redis_model.py` | the two closed-loop models (class S), every input set from omni-v21's runs' own files |
| `docs/MYSQL_PREREGISTRATION.md` (amendment 6), `docs/YCSB_PREREGISTRATION.md` (6), `docs/POSTGRES_PREREGISTRATION.md` (4), `docs/REDIS_PREREGISTRATION.md` (5), `docs/KAFKA_PREREGISTRATION.md` (4) | declared before any run on them |

## What the model gate read

Our own models, evidence class S, never a benchmark result.

| Gate | Against omni-v21 |
|---|---|
| the store gate, every store wire's candidate on omni-v21's archived seconds, open-loop (`results/model_gate/V22_STORE_GATE.md`) | no LOSS on any wire or workload; the seconds below native fall to none on every wire (MySQL 97.9 → 0 an arm, MongoDB 12.5 → 0, Redis 36.6 → 0, PostgreSQL 223.5 → 0); the three cache candidates hold at native in the replay because omni-v21's audits carry neither the stores' accounts nor the host's memory; the pooler's servers +28.2% and Kafka's consumers +130.6%, power given |
| the Redis cache, closed loop (`results/model_gate/V22_REDIS_MODEL.md`) | work inside the line GAIN in every workload (up 7.7% to 22.9%), the mean latency GAIN (down 36% to 59%), the 95th and 99th percentiles GAIN or STEADY, the memory held power given (201 to 304 MB against 62 to 66 MB); no LOSS |
| the Kafka group, closed loop, 30 s a notch, the development seeds 101 to 108 (`results/model_gate/V22_KAFKA_MODEL.md`) and the untouched seeds 201 to 208 (`…_UNTOUCHED.md`) | no LOSS row; work inside the line GAIN, the 95th and 99th percentiles GAIN, the most messages waiting at once GAIN, consumers power given |
| the Kafka group at 20 s a notch (run C's setting, not the counted one; `…_20S.md`) | one LOSS row: the burst's most messages waiting at once, up 30.6% inside the seeds' spread (native's queue grows about 1,100 messages in a 20 s notch and one rebalance costs about the same); on the next version's list with its cause |
| the Kubernetes governor's models (`results/model_gate/V22_VS_V21.md`, `tools/model_gate.py`) | omni-v22's one change to the governor, the hand-back tried five times against the API's weather, moves no decision: every model reads omni-v21's own numbers on every gauge, STEADY, identical |

MySQL's and MongoDB's accounts of a miss are read for real on the first runs of omni-v22 (omni-v21's audits do not carry them), and a
closed-loop model of each store, set from those runs' own files, is the next model gate's work.

Every benchmark runs again on omni-v22 from the moment it reaches main; nothing is read across engines. The store benchmarks run
first, every table at the counted 30 s a notch (`scripts/reruns.txt`).

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
