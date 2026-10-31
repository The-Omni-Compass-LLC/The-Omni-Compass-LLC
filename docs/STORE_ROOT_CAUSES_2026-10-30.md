# Why the data stores read as they do on omni-v21: the causes, from their own files

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The founder's order of 30 October: "find out why they went one way or the other and tweak it and turn it and tune it to the
best possible way for an Omni Compass engine to interact with this as a system governor". The five data-store benchmarks
carry 33 of the 50 LOSS rows on the engine that stands (`docs/LOSS_LEDGER.md`). Every number below is printed from the raw
runs on the branch `raw` by `tools/store_causes.py` (its command is beside each table), and the model readings are class S,
our own model, never a benchmark result.

## 1. The verdict's gate refused the brain exactly when the store needed it

Each store's wire lets the compass move its knob only inside an allowance that a paired trial on the store has earned
(`tools/knob_verdict.py`, amendment 2 of 9 October). Two of the gate's rules met in every overload:

- The wall abandons every trial: at 95% of the line (the fail-up) every spend trial in progress ends unjudged.
- The fail-up is clamped to the allowance: "a fail-up never spends beyond the allowance".

A spend trial needs about ten seconds of holding at the old setting before it tries a new one. An overload reaches the wall
in about six. So the trial that would have earned the spend was always ended by the wall, and the wall's own reflex was then
held at the operator's setting by the allowance that trial never earned.

`python3 tools/store_causes.py gate run-40256717947 run-40279909158 run-40400868003 run-40254205224 run-40276907808 run-40400989005 run-40258018856 run-40281464587 run-40401032384`

| Store (the resource objective) | Seconds over its line, Omni-Compass's arms, three runs | Of them, the brain's own rule asked to go up and the verdict kept it from going there | Allowance at the end (the operator's setting first) |
|---|---:|---:|---|
| Kafka | 1,428 | 1,428 | 2 consumers in 29 of 36 arms; 3 or 4 in the rest |
| Redis | 4,581 | 4,426 | 64 MB in 12 of 36 arms; 72 or 80 MB in the rest |
| MySQL | 3,697 | 3,139 | 512 MB at the top in 24 of 45 arms; 640 MB in the rest |
| MongoDB | 32 | 21 | rarely over its line |
| PostgreSQL | 28 | 0 | rarely over its line |

How the trials ended (`python3 tools/store_causes.py trials RUN`): Kafka's run A, 12 of its 13 spend trials ended by the wall,
none allowed; Redis's run A, 62 of its 68 ended by the wall, 5 allowed. The service objective's runs show the same: Kafka
1,625 seconds over its line, every one refused. The objective is not the lock; the wall is.

## 2. Kafka: the hand-back gave back a consumer the load still needed

Each consumer change rebalances the whole group: every member stops until each has rejoined, and a member learns of a
rebalance at its next heartbeat (every 3 s, kafka-python's own default). Measured on every change made in calm
(`python3 tools/store_causes.py stalls .`):

| Change | Changes | The extra wait the messages saw (s) |
|---|---:|---|
| A consumer added | 41 | median 1.237 (quartiles 0.334 and 2.487; at most 3.346) |
| A consumer removed | 52 | median 2.578 (quartiles 1.598 and 2.858; at most 3.010) |

The hand-back of 25 October gives a consumer back 30 s after the last change once nothing waits beyond one poll round, with no
look at whether the members left can carry the arrivals. In the light workload the brain gave a consumer back, the removal's
2 to 3 s stall built a queue, the brain added it back 1 to 3 s later, and again 30 s on (run 40279909158, light, repetition 1:
removals at 310, 355, 413 and 444 s, each re-added within 3 s). That churn is where the light and heavy workloads' latency
LOSS rows come from.

## 3. Kafka: the keys land on six partitions, so a fourth consumer buys nothing

The harness's producer keys each message `str(seq % 8)`, and Kafka places a key by murmur2 (the model's own murmur2, on the branch v22-stores, checked
against Kafka's own test vectors). The eight keys land on six partitions: 6 and 7 two keys each, 2 and 5 none. Kafka's range
assignor then gives the members these shares of the load:

| Consumers | The busiest member's share | What the group sustains (μ, one member's rate) |
|---|---|---|
| 2 (native) | 5/8 | 1.6 μ: 792 a second at 2 ms of work; offered the burst's 880, the group serves 825 (the 5/8 member at μ, the 3/8 member its arrivals), as the runs read |
| 3 | 4/8 | 2.0 μ |
| 4 | 4/8 | 2.0 μ: no more than 3 |
| 5 to 8 | 2/8 | 4.0 μ |

A backlogged consumer serves 495 messages a second at 2 ms of work, 199 at 5 ms and 981 at 1 ms, in its own record
(`python3 tools/store_causes.py rate .`). The harness measured the group's "capacity" from a backlog it had filled first
(975 a second at 2 ms, which is 2 μ) and set each workload's peak at 90% of it. Under keyed arrivals two consumers keep up
with at most 1.6 μ (792 a second at 2 ms), so every peak offers about 111% of what the operator's two consumers keep up with. Both arms face the same peak: it is a fair
test of a governor, and the governor that adds the third consumer in time wins it. A wire that adds one consumer at a time
wastes the fourth, and the verdict's trials cannot tell why.

## 4. Five tables are two settings

Run C of all five resource-objective store tables (40400868003, 40401042132, 40400989005, 40400963499, 40401032384) ran at the
workflows' default of 20 s a notch; runs A and B at the counted 30 s (`scripts/reruns.txt`). A table mixing them is not one
benchmark run three times. Every store workflow's default is now the counted 30 s (`tests/test_audit_2026_10_30.py`), and on the
next engine every store table runs again at one setting.

## 5. Redis, MySQL and MongoDB: where a miss costs the service, and where it does not

Redis's 95th percentile stands at 5.2 to 5.7 ms in both arms against its 2 ms line: a miss costs the trip to the store (5 ms).
Only a larger cache cuts the misses, and the allowance held the cache at 64 to 80 MB while the working set needs more. In our own
model of the cache (class S; its hit and miss latencies the omni-v21 native arms' own records; redis_model.py on the branch
v22-stores, not on main until the model gate reads no LOSS) a ceiling the working set fits under raises the small workload's hit share from 63% to 72% at 256 MB; the misses
that remain are each notch's first touch of a new keyspace, which no ceiling mends.

MySQL and MongoDB are the other case. Their omni arms' own seconds (`tools/store_causes.py` over the raw runs; the pool or cache,
the misses and the latency of each second):

| Store | Working set | Knob | Misses | Latency |
|---|---|---|---|---|
| MySQL, read-only, 6 tables | about 1.3 GB | pool 384 MB | 12.4% of page reads | 0.138 ms a statement |
| | | pool 512 MB | 10.9% | 0.138 ms |
| | | pool 640 MB | 9.1% | 0.141 ms |
| MongoDB, workload b, 6 × 250,000 records | | cache 512 MB | 15.8% of pages | 0.082 ms a read |
| MongoDB, tuning, 6 × 250,000 records | | cache 512 MB | 12.6% | 0.073 ms |
| | | cache 576 MB | 12.1% | 0.074 ms |
| | | cache 640 MB | 11.7% | 0.075 ms |

Read across the pool sizes, a third of the misses gone with the latency unmoved looked, this morning, like misses that cost the
statement nothing (the data files in the machine's page cache). That reading was too coarse, and it is withdrawn here. The change
one notch of pool makes to the miss share (about three points) is worth about 5% of the statement time, inside the arms' own spread,
so the level comparison could not have seen it. A slope of latency on miss share inside the arms was tried next as the price of a
miss and read 0.5 to 1.3 ms a unit of miss share (MySQL) and 0.4 to 2.0 (MongoDB), which overstates it several times over: the
host's noise moves the misses and the latency together, and a regression reads that as a price. It is not used anywhere.

What is used is the store's own account of its misses. MySQL's performance schema times every read of the data files
(`file_summary_by_event_name`, `wait/io/file/innodb/innodb_data_file`, enabled and timed as MySQL 8.0 ships) beside the workload's
statement timer; WiredTiger counts and times the pages its application threads read from disk (`application threads page read from
disk to cache time (usecs)`) beside the server's own read latency; the Redis harness's application records each request as a hit
or a miss. The ratio, the misses' time over the service's time, read over the last 10 s, is the share of the service's own time that
its misses are. Read on this machine on 30 October with MySQL 8.0.46 and sysbench's own workloads at their six-table notch, the
operator's 512 MB pool (a tuning-bench reading on this host, class L, no benchmark result; `tools/store_brain.py` names the meter):

| Workload on this machine | Statements a second | A statement | Page reads missing | A data file read | The misses' share of the statements' time |
|---|---:|---:|---:|---:|---|
| point selects, 6 tables, pool 512 MB (the first arm, the dataset just written and still flushing) | 3,001 | 137 µs | 17.3% | 70 µs | median 32% (quartiles 24% and 37%) |
| read-only transactions, 6 tables, 512 MB | 4,484 | 95 µs | 10.9% | 14 µs | median 12% (quartiles 8% and 19%) |
| point selects, 3 tables, 512 MB | 3,017 | 95 µs | 8.8% | 9 µs | median 2.8% (quartiles 2.3% and 3.9%) |
| point selects, 6 tables, 128 MB (MySQL as shipped) | 2,997 | 93 µs | 23.4% | 7 µs | median 7.0% (quartiles 6.2% and 7.9%) |
| read-only transactions, 6 tables, 128 MB | 4,455 | 80 µs | 15.3% | 5 µs | median 7.3% (quartiles 7.1% and 7.5%) |
| point selects, 3 tables, 128 MB | 3,005 | 92 µs | 21.8% | 6 µs | median 5.7% (quartiles 5.5% and 6.2%) |

The miss shares are the rig's own (10.9% at 512 MB on the read-only workload), and the first arm's statement latency is the rig's
(0.138 ms): the rig, like that arm, runs each workload straight after its dataset is prepared, while the host is still writing it
out, and a data file read then costs 70 µs; once the host has settled a read costs 5 to 14 µs. The misses are not nothing: 3% to
32% of what a statement waits for is a page the pool did not hold, every arm above the key's floor, and only the pool can cut it.
The account is read live, second by second, so the brain reads what the misses cost on the machine it runs on, not this one. So the store wires need the wall never clamped by an allowance (every store), the spend gated on the store's own
account at the one key's floor (a half of one percent of the service's time: under it the misses are nothing the record could read,
and memory could buy nothing it could read), the host's room (a notch only while the host keeps 5% of its memory available), and
the hand-back never below what the working set occupied. The five candidates carry them (section 6).

## 6. The fix, the next version's, through the model gate first

**Kafka** (a candidate written on the study branch v22-stores: the wire's `Brain`, and the closed-loop model kafka_model.py,
every input set from these runs' own files; neither is on main until the model gate reads no LOSS):

- **The rate twin**: each partition's arrivals (the topic's log-end offsets, read from the broker once a second) placed on the
  members by the range assignor; one member's rate learned from a second in which the queue grew (the group consumed
  Σ min(load, μ), solved for μ); a change's own stall learned the same way, the heartbeat interval its bound before one is seen.
- **The reflex**: when the twin says the count cannot carry the arrivals and the backlog (its own and the one a change's stall
  would add) at nine tenths of a member's rate, the count goes at once to the smallest one that can, up to the partitions:
  never clamped by the allowance, which keeps judging the compass's own moves.
- **The hold**: handed back only to a count that carries the last 60 s's arrival peak at seven tenths of its rate, 30 s after
  the last change, in calm, in one move (one rebalance); never below the operator's count; the immune system's hand-back to
  native when Omni-Compass's count redlines, stuck, and native's twin reads lower (`omnicompass/immune.py`).

In the model, against omni-v21's own loop on the same seeds (class S):

| Notches | Seeds | Every workload |
|---|---|---|
| 30 s, the counted setting | development 101 to 108, and untouched 201 to 208 | no LOSS row; work inside the line GAIN (up 16% to 21%), the 95th percentile GAIN (down 92% to 98%), the 99th GAIN (down 57% to 81%), the most messages waiting at once GAIN (down 19% to 43%), consumers power given (up 42% to 71%) |
| 20 s, run C's setting | untouched 201 to 208 | one LOSS row: the burst's most messages waiting at once, up 30.6% inside the seeds' spread; every other row GAIN or power given |

The 20 s row is the physics of a change, not a tuning to be hidden: native's peak is the queue one notch grows (about 55 a
second, 1,100 in 20 s and 1,650 in 30 s); any added consumer costs one rebalance's worth of arrivals (880 a second × 1.24 s
median, about 1,100). It is on the next version's list with its cause.

**Redis, MySQL, MongoDB and PostgreSQL** (candidates on the same branch; `tools/store_brain.py` is what the three cache wires
share; each wire's `Brain` keeps its own compass law and its own rule): the max on each knob. The spend the wire's own rule asks
for goes through unclamped, up to the cover, where the store's own account says the misses are at least the key's floor of the
service's time and the host keeps its 5% cushion after the notch; it holds, and says why, where the misses are under the floor,
where the account or the host's memory is unread, or where the host has no room; a hand-back never goes below the most the working
set occupied in the last 60 s nor below native; the pooler's pool is never taken below the pooler's own setting. `OMNI_DIAL=save`
keeps omni-v21's loop on every wire (the tune-down, where giving the resource back is the aim), and every record carries its dial.
`tools/store_brain.py` and `tools/knob_verdict.py` join the fingerprint with the version that carries this (`tools/omni_version.py`).

The store gate (`tools/store_gate.py`, class S, the omni-v21 arms' recorded seconds replayed open-loop through each candidate;
`results/model_gate/V22_STORE_GATE.md` on the branch): no LOSS on any wire or workload. omni-v21's audits carry neither the stores'
accounts of their misses nor the host's memory, so the three cache candidates hold at native in the replay (seconds below native
97.9 → 0 an arm on MySQL, 12.5 → 0 on MongoDB, 36.6 → 0 on Redis; the knob's moves 7.5, 5.6 and 12.3 → 0, GAIN +100.0%); the
pooler's candidate holds servers +28.2% (power given) and its seconds below native while clients waited fall 7.5 → 0 (GAIN
+100.0%); Kafka's twin as in the table above. The replay cannot show what the memory buys; the closed-loop Redis model (class S,
`tools/redis_model.py --compare`, seeds 101 to 103) can: against omni-v21's own loop, work inside the line GAIN in every workload
(small up 22.9%, burst up 17.6%, tuning up 10.3%, large up 7.7%), the mean latency GAIN (down 36% to 59%), the 95th and 99th
percentiles GAIN or STEADY, the memory held power given (201 to 304 MB against 62 to 66 MB); no LOSS row. MySQL's and MongoDB's
accounts are read for real on the first runs of the next engine, and a closed-loop model of each is set from those files.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
