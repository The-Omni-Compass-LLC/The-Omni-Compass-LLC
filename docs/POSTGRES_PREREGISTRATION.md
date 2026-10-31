# Databases: Omni-Compass on top of a database's own connection pooler, preregistered

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written 2026-10-06, before any counted run. The rules below were set on the tuning workload and are then applied
unchanged to the untouched workloads; every row is reported, losses included; the readings are the three-run readings of
`docs/OMNI_V1.md`. The runner is `tools/run_pgbench.py`, the workflow `.github/workflows/pgbench.yml`.

## Why this benchmark

PostgreSQL is the most used open-source database in the world, and PgBouncer is the connection pooler most of its
deployments put in front of it. The pooler has one setting that matters for capacity, the number of server connections
it keeps open to the database (its pool size), and it has no controller for it: the DBA sets a number once and the
pooler holds it through every quiet hour and every rush. That fixed number is the native controller here, and Omni sits
on top of it.

## What is someone else's

- **PostgreSQL 16** (the PostgreSQL Global Development Group, PostgreSQL License), as the distribution ships it, with
  its own settings untouched (`max_connections` 100, `shared_buffers` 128 MB, `synchronous_commit` on).
- **PgBouncer 1.22** (the PgBouncer project, ISC License), in transaction pooling, with the pool size it ships with,
  **20 server connections** (`default_pool_size`), and every other setting as shipped.
- **pgbench** (PostgreSQL's own benchmark, shipped with PostgreSQL): the TPC-B-like default script and its `-S` and
  `-N` variants, its per-transaction log (`-l`) for the latencies, its rate limiter (`-R`) for the offered load.
- **The machine:** a GitHub Actions runner (4 cores) in the counted runs. There is no watt-meter on it.

Nothing here models a database. Omni writes one setting through PgBouncer's own admin console (`SET default_pool_size`)
and reads what PgBouncer itself reports (`SHOW STATS`, `SHOW POOLS`, `SHOW CONFIG`).

## Arms

- **native:** PostgreSQL behind PgBouncer's shipped pool of 20, pgbench offering the load.
- **omni:** the same, with the compass law (`omnicompass/compass_law.py`) on **one knob, the pool size**, inside the
  cover [2, 90]: never under two server connections (the floor of two), never within ten of PostgreSQL's 100
  connections. Everything else is native's.

## The omni rule (frozen on the tuning workload)

- **Reading.** Once a second, the service time per transaction as the pooler itself reports it: the change in
  `total_xact_time` plus the change in `total_wait_time` (clients waiting for a server) over the change in
  `total_xact_count` since the last second. No transaction in a second reads as calm (0).
- **Band.** From 0 to the response line, **50 ms** a transaction. The compass pulls the reading to 40% of the line
  (20 ms), the service profile of the Kubernetes adapter, with its usual gains (kp 1.0, response time 2 s, smoothing
  0.5, one decision a second).
- **Direction.** Where the time goes decides what a positive force (the service slow) does: if half or more of the
  time was spent **waiting for a server**, the pool grows by ceil(force / 0.10) slots this second (full force adds ten);
  if the time was spent **inside the server**, the pool shrinks by one (fewer backends fighting for the same cores and
  rows). A negative force (calm) gives back **one idle server a second**, and only when PgBouncer shows an idle server
  to give back (`sv_idle` ≥ 1): a server in use is never taken.
- **Cushion.** A force inside ±0.05 moves nothing.
- **Dwell.** No reversal of direction within five seconds.
- **Fail up.** At 95% of the line the knob is handed back to the pooler's own setting (20) at once; the compass then
  resumes.
- **One writer.** If the knob is found at a value Omni did not write, Omni stops writing (the plug contract).
- **Reset.** At the end of every omni arm the knob is restored to the snapshot taken at the start and read back;
  the report says whether every arm was handed back.

Disclosed: the pooler cannot see time a client spends behind its own schedule before it sends a transaction. The compass
reads the pooler's view; the gauges below read the user's view from pgbench's own log, lag included.

## The load

pgbench with **64 client connections** to the pooler (more clients than native's 20 servers, as a pooled deployment
has), rate-limited, the offered rate stepping one notch at a time: **1 2 3 2 3 4 5 6 5 4 3 2 1 2 1**, 20 s a notch,
300 s an arm. The base rate is set **once per workload before the counted runs, in native mode**: one 20 s run with no
rate limit gives native's unlimited capacity, and the peak notch (6) offers nine tenths of it, so native is at its knee
and not past it (past the knee both arms fall behind the schedule, which says nothing about a controller). Each arm
starts from the pooler's own setting after a 5 s uncounted warm-up at the base rate. The two arms alternate order
between repetitions.

## Gauges (from pgbench's log, PgBouncer's `SHOW POOLS`, the host's `/proc/stat`)

| Gauge | Direction |
|---|---|
| work inside the response line: transactions a second whose latency (lag included) was within 50 ms | **the aim is higher** (the product number) |
| throughput (transactions a second) | the aim is higher |
| latency: median, 95th and 99th percentile, mean (ms, lag included) | the aim is lower |
| failed transactions | **any increase is marked** |
| server connections alive, mean and most at once (the machines) | the aim is lower |
| host CPU busy share, host CPU-seconds, CPU-seconds per 1,000 transactions inside the line | the aim is lower; measured, not modelled (evidence class L) |
| pool size, mean | shown, not judged |

**No energy is claimed.** A GitHub runner has no watt-meter; the host's CPU-seconds are a real measurement of the
machine's work and are reported as such, nothing more.

A change under one part in a million reads "same".

## Workloads

- **Tuning workload:** `tpcb`, pgbench's TPC-B-like default script at scale 20 (20 branches). The band, the direction
  rule, the cushion, the dwell and the floor and ceiling above were set on it; nothing else is tuned.
- **Untouched workloads:** `select` (select-only, `-S`, scale 20: read-heavy), `simple_update` (`-N`, scale 20: the
  default script without the branch and teller updates), `tpcb_hot` (the default script at scale 2: two branches,
  every transaction fighting for the same rows).

Each workload gets its own native calibration of the base rate, by the rule above.

## Runs

Each workload: **three paired repetitions** (native and omni, alternating order) in one GitHub Actions job; the
paired difference's 95% interval over the repetitions decides whether a change is beyond the noise within that run.
Three separate runs on the frozen engine (A, B, C); the three-run table reads GAIN or LOSS in all three of our runs (judged by what the gauge is for; a resource spent that rose reads power given) when
the sign holds and every run's interval is clear of zero, no difference beyond the noise when a run's interval includes
zero, the runs disagree when clear runs point different ways. Two workloads run at a time, so the other benchmarks keep
their runners.

## What the first smoke already showed, said before the counted runs

One short repetition on a 4-core box, 64 clients, five notches of 4 s: omni did more work inside the line (1,400 against
1,312 transactions a second), its 95th-percentile latency over the whole profile was lower (24.5 against 77.2 ms) and
it kept 11 server connections alive against native's 20. At the peak notch the pool had been taken back to about 10,
and fewer backends on four cores answered faster than twenty. **At the lightest notch omni's p95 was higher (14.6
against 3.9 ms, inside the line)** because the pool had been given back to two or three: the expected cost of the
take-back at light load, stated here in advance. One repetition proves nothing; the counted runs will show whatever they
show, that row included.

## Amendment 4 (2026-10-10 13:05 UTC, after the first counted set on amendment 3, before the next): a spend trial runs to its samples

The first counted set on the brain's verdict (runs 38013313943, 38013319893, 38013324861; the table `results/live/V3_PGBENCH.md`) landed at midday on 10 October. What it showed about the trials: the trials were judged on this stack (10 to 28 trials an arm, 3 to 7 allowed, 2 to 4 refused, few abandoned), the pool was given back on `select` (connections held open −6% to −11%, GAIN in all three of our runs) and the add above the operator's 20 on `simple_update` was refused as expected, with every other gauge inside the noise.

**The cause is ours.** Amendment 3 ended a trial when the service swung to the other direction's condition: a give-back trial when the service left calm (the engine's own rule, kept), and a spend trial when the service turned calm. A spend that works calms the service within seconds, so a spend trial could never reach its samples: every successful spend ended its own trial unjudged. Nothing in the stack and nothing in the engine did this; the engine's verdict ends a trial when the condition it is given ends, and we gave it the wrong condition for spending. Found on the first set, corrected before the second, declared here.

**From this amendment** (`tools/knob_verdict.py`, the harness outside the engine; Omni v3 unchanged): a spend trial, once started, runs to its samples whatever the compass's force; only the wall (a fail-up) or the engine's own time limit on a trial ends it early. A give-back trial still ends when the service leaves calm. The conditions to start a trial, the cost, the judge, the allowance and the recheck are unchanged.

**Expected before the runs:** little change: the trials were already judged here; a spend trial that the queue line starts now runs to its samples instead of ending when the queue clears, so a server added while clients waited is judged on what it bought. The first set's table stands as the result of amendment 3 until the set on this amendment lands and supersedes it; it then goes whole to `docs/history`.

**Dispatched (2026-10-10 13:11 UTC, commit `ca745467`).** Runs 38054754511, 38054758150, 38054761503 (A, B, C), the same inputs as the morning's; recorded run by run in `docs/RERUN_2026-10-10.md`.

---

© 2026 The Omni-Compass LLC. Evaluation and Simulation use only; any other use requires a signed, paid Omni-Compass
Enterprise License. All rights reserved. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## The tuning run (2026-10-06, run 37420052827; rules frozen above, nothing changed after it)

Three paired repetitions of `tpcb` on a GitHub runner (4 cores), 64 clients, the base rate from native's own unlimited
capacity (5,626 transactions a second, peak notch 90% of it). Not counted; the untouched workloads follow.

| Gauge | native | omni | reading |
|---|---:|---:|---|
| server connections alive, mean (the machines) | 20.0 | 9.3 | GAIN, cut (−53%, interval −57% to −50%) |
| work inside the 50 ms line (tps) | 2,137 | 2,152 | STEADY, no difference beyond the noise |
| throughput (tps) | 2,437 | 2,474 | STEADY, no difference beyond the noise |
| latency p95 (ms) | 1,361 | 433 | STEADY, no difference beyond the noise (native's own p95 swung from 86 to 3,331 ms between repetitions) |
| latency p99 / median (ms) | 2,888 / 0.98 | 862 / 1.09 | STEADY, no difference beyond the noise |
| failed transactions | 0 | 0 | STEADY, the same |
| host CPU-seconds | 433 | 480 | **power given** (+11%, interval +8% to +14%) |
| CPU-seconds per 1,000 transactions inside the line | 0.68 | 0.74 | STEADY, no difference beyond the noise |
| pool size, mean (the knob) | 20 | 9.5 | shown |

The knob was handed back and read back at the end of every omni arm; Omni wrote 161 to 175 times an arm and failed up
9 times an arm. Read: on a shared 4-core runner the latencies are too noisy for three repetitions to tell the arms
apart, native's own p95 varying forty-fold between repetitions; what did separate is the machines, half as many database
connections held open for the same work, and the host's CPU, 11% more of it, which is the cost of PgBouncer queueing
(*corrected by amendment 2 below: measured, the CPU was the harness's own `psql` launches, not the pooler's queueing*)
clients behind a smaller pool. Both go into the untouched runs as they are; nothing in the rule changes.

## The first untouched run, and amendment 1 (2026-10-06, run 37425853293; declared before the counted runs)

The three untouched workloads ran once on the rule above (run 37425853293, three paired repetitions each). The result is
kept here as it came, and it is a LOSS:

| Workload | Work inside the line | Throughput | p95 (ms) | Servers alive | Host CPU-seconds |
|---|---|---|---|---|---|
| `select` (read-only) | 11,423 → 5,995 tps, **LOSS** | 11,428 → 10,373, **LOSS** | 4 → 3,886, **LOSS** | 19.2 → 2.5, GAIN | −1%, GAIN |
| `simple_update` | STEADY, no difference beyond the noise | STEADY, no difference beyond the noise | 65 → 554, STEADY, no difference beyond the noise | 20 → 8.1, GAIN | +10%, **power given** |
| `tpcb_hot` (two branches) | STEADY, no difference beyond the noise | STEADY, no difference beyond the noise | 8 → 54, STEADY, no difference beyond the noise | 19 → 5.3, GAIN | +18%, **power given** |

**What happened on `select`.** The compass read the pooler's service time per transaction, 0.11 ms against a 50 ms
line, and gave back one idle connection a second until the pool stood at its floor of two (18 writes an arm, no fail-up).
Two connections serve about 15,500 read-only transactions a second; the peak notch offered 23,400. The backlog did not
show at the pooler: a client with a transaction in flight is served in 0.1 ms, and the time it spent behind its own
schedule waiting to send is not the pooler's to see. So the pooler's clock said calm while the users' p95 went from
4 ms to 3.9 s. The rule was blind to the one thing that mattered, and the preregistration had said so in one line
("the pooler cannot see time a client spends behind its own schedule") without drawing the consequence.

**Amendment 1 (`tools/run_pgbench.py`, `service_reading`, `decide`).** Two changes, declared here before any counted run:

1. **The reading** is the pooler's service time per transaction **or the share of its clients queued for a server**
   (`SHOW POOLS`, `cl_waiting / (cl_active + cl_waiting)`) scaled to the line, whichever read LOSS. A pool too small for
   the offered rate shows at the pooler as clients waiting; with every client waiting the position is past the wall and
   the knob is handed back to the pooler's own setting at once. The waiting share also decides the direction with the
   wait-time share: half or more waiting means the pool grows.
2. **The dwell holds only the brake.** Adding connections is never held, not even two seconds after a take-back (the
   gas is never held, as in every other Omni adapter); taking back waits five seconds after an add. The first rule held
   the needed add for five seconds once in the local check.

Nothing else changes: the band, the centre, the gains, the cushion, the cover [2, 90], one idle server a second on the
way down, the fail-up, the one-writer rule and the hand-back are as frozen above. Local check of the amended rule on
`select` (one short repetition, 16 clients): at the peak notch the pool held near 11 and the work inside the line and
the p95 matched native's; at the light notches the pool eased to 3. The counted runs are three new untouched runs (A, B,
C) on the amended rule; run 37425853293 stays in this file as the result the first rule produced and is not counted.

## The counted runs (2026-10-06, runs 37435740735, 37435751322, 37435761371, on amendment 1)

The three untouched workloads, three separate GitHub runs, three paired repetitions each; the table by rule is
`results/live/V3_PGBENCH.md` (`tools/pgbench_abc.py`).

| Workload | Connections held open (the machines) | Host CPU-seconds | Work inside the line, throughput, p50, p95, p99 |
|---|---|---|---|
| `select` | 19.3 → 7.5, **GAIN in all three of our runs** (−61% to −63% in the three runs) | **LOSS in all three of our runs** (+14% to +27%) | no difference beyond the noise (3 of 3 runs) |
| `simple_update` | **the runs disagree** (+12% in one run, −34% and −35% in two) | **LOSS in all three of our runs** (+18% to +28%) | no difference beyond the noise (2 or 3 of 3 runs) |
| `tpcb_hot` | 19.4 → 6.0, **GAIN in all three of our runs** (−69% to −72%) | **LOSS in all three of our runs** (+15% to +25%) | no difference beyond the noise (2 or 3 of 3 runs) |

Failed transactions 0 and 0 in every run; the knob handed back and read back in every arm. Read: with the amended
reading the read-only collapse of the first run did not recur (work inside the line and throughput within the noise of
native's in all three runs), and Omni held a third of the connections open for the same work. The cost is real and
the same in all three of our runs: the host spent 14% to 28% more CPU, which is PgBouncer queuing clients behind a smaller pool. The latencies
cannot be told apart on GitHub's shared runner, where native's own p95 moved from 3 ms to 3 s between repetitions; that
is the runner, and it is said so. Nothing in the rule changes after these runs.

*Correction, 2026-10-08 (amendment 2 below): the sentence "which is PgBouncer queuing clients behind a smaller pool" was an
explanation written without a measurement, and the measurement shows it was wrong. The CPU was our own harness launching a
`psql` process for every reading. The sentence stays as written; the amendment says what was found.*

## Amendment 2 (2026-10-08, declared before the second counted set): where the CPU went, and the take-back gate

**The question.** The founder asked for every cost in the counted tables to be traced to its mechanism and removed where
the mechanism is ours, with the engine locked (Omni v3; `tools/omni_version.py` prints omni-v3 before and after this
amendment: `tools/run_pgbench.py` is a harness, outside the engine's fingerprint). Two rows of `V3_PGBENCH.md` are costs:
**host CPU +14% to +28%, power given in all three of our runs on all three workloads**, and **median latency +15% to +17%, LOSS in all three of our runs on
`select` and `tpcb_hot`** (the p95 moved from 2.7 ms to 143 ms on `select` as a point estimate, inside the noise only
because one repetition read 367 ms and another 17 ms).

**Where the CPU went: measured, not guessed.** Three measurements, all repeatable from the files in the repository or
from the harness itself.

1. *The pooler's own log of the counted set* (`results/live/raw/run-37435740735/pgbench-select/pgbench-select/pgb/pgbouncer.log`,
   one workload, six arms): **7,956 logins to the admin console**, about 110 a minute in the native arms' minutes and 400 to
   450 a minute in the omni arms' minutes, against 269 server connections opened and 267 closed over the whole workload.
   Every console login was one `psql` process the harness launched: two a second from the sampler in both arms, and in the
   omni arm four more a second from the brain (SHOW STATS, SHOW POOLS, SHOW POOLS again for the idle count, SHOW CONFIG for
   the lever) plus three per write (read the lever, SET, read it back). The server churn that would have supported the
   "queuing" explanation is small: about 70 reconnects an omni arm.
2. *The cost of one launch.* 100 launches of `psql --csv -c "select 1"` from Python on a four-core Ubuntu 24.04 machine of
   the runner's class: **52 ms of CPU each** (4.27 s user, 0.95 s system, 6.1 s of wall). psql loads libpq, OpenSSL, GSSAPI
   and LDAP and opens a connection before it runs one command; that is where the time goes.
3. *A paired repetition of `select` on the unchanged harness with a per-process meter* (`/proc` read every 0.25 s; PgBouncer,
   every PostgreSQL process with the postmaster's reaped children, pgbench by process, the harness's Python and its reaped
   children; the same machine as 2):

   | CPU-seconds over the 302 s arm | native | omni | omni − native |
   |---|---:|---:|---:|
   | the whole host (the gauge the table reports) | 573.5 | 626.3 | **+52.8** |
   | PgBouncer | 138.0 | 139.2 | +1.2 |
   | PostgreSQL, every process | 307.5 | 302.8 | −4.7 |
   | pgbench | 128.7 | 121.6 | −7.1 |
   | the harness's Python itself | 2.3 | 3.9 | +1.6 |
   | `psql` launches (the harness's children less pgbench) | 21.3 | 77.2 | **+55.9** |

   The pooler did not spend the CPU (+1.2 s), nor did the database (−4.7 s): **the `psql` launches did (+55.9 s against a
   +52.8 s host difference)**, about 35 ms each at the console. On GitHub's runner the omni arms' extra was 95 CPU-seconds
   for about 1,570 extra launches, about 60 ms each; a slower runner, the same cause. In this repetition the omni arm also
   read servers alive 7.8 against 20.0, median latency 0.656 ms against 0.554 ms (+18%, the counted set's +17%), p95 23.5 ms
   against 4.3 ms, work inside the line 7,859 against 8,088 tps.

**Where the median latency went.** The take-back rule gave back one idle server a second whenever the pooler's service time
read calm, and with 0.4 ms transactions against a 50 ms line it always read calm: the pool went from 20 to the floor of 2 in
the light notches and held near 8 on average (`audit.jsonl`: 100 to 117 writes an arm, 89 to 104 of them take-backs), and the
users' queue behind it is the +17% on the median and the 143 ms p95. The pool was shrunk into demand that the pooler
itself was reporting (`total_wait_time`, clients waiting for a server) and the rule did not ask.

**The amendment, three parts, nothing else.**

1. **One console connection an arm** (`tools/run_pgbench.py`, class `Console`): the harness speaks the server's own wire
   protocol (PostgreSQL's protocol, version 3, the simple query) over one connection held for the whole arm, in both arms
   alike, for the sampler and the brain; no process is launched for a reading; the brain reads SHOW POOLS once a decision
   and takes its idle count from that row. The parsing is tested without a server (`tests/test_run_pgbench.py`). The console's
   logins per arm are written into the arm's record.
2. **The queue line.** The share of the pooler's time its clients spent waiting for a server in the last second
   (`total_wait_time` against `total_xact_time + total_wait_time`, differenced) is read every second. A server is taken
   back, by the calm give-back and by the slow-inside-the-server shrink alike, only while that share is **under one percent
   and a transaction was served in that second**; while it is **at one percent or above, servers are added back, one for
   every percent of waiting (rounded up), up to the pooler's own setting** (20), so a take-back that put clients in the
   queue is undone the next second and a rising load gets its servers back at once (waiting 6% of the time adds six). Above
   the pooler's own setting only slowness adds, by the force, as amendment 1 wrote it; adding is never held, and the fail-up
   is unchanged. One percent is the line the two other database tests already use for their give-back (misses under one
   percent of reads), and it is the unit of the add-back; no new number. At the smallest pool that serves the load without
   waiting the rule probes down one server and comes back, no oftener than the five-second dwell allows (one connection
   closed and reopened every six seconds or so, written in the audit as the knob's moves): that is how it finds the knee,
   and it is said here so the writes count in the table is read for what it is. Said plainly: the pool is only ever taken
   from idle servers, and it is given back the moment anyone waits; the saving comes from the hours when the pool was bigger
   than the demand, and from nowhere else.

   *Disclosed: this mechanism was found in the counted set's own audits, which are the untouched workloads' audits; the rule
   it fixes was frozen on the tuning workload, but the fix was designed with the untouched workloads' failures in view, and
   its one number is borrowed, not fitted. The second counted set is therefore read as a test of the amended rule on the
   same three workloads, not as a fresh untouched test; a referee who wants an untouched test of this rule needs a workload
   none of these runs has seen, and that is noted for the register.*
3. **The harness's own CPU is recorded** beside the host's (`harness_cpu_seconds`, the Python process's own time: the
   compass's brain in the omni arm, the sampler in both; shown, not judged), so the next table says what the governor
   itself costs instead of leaving it inside the host's figure.

Unchanged: the reading of amendment 1, the band, the centre, the gains, the cushion, the direction rule, the dwell, the
cover [2, 90], the fail-up, the one-writer rule, the hand-back, the load, the gauges, the workloads, the three-run rule.
`tests/test_run_pgbench.py` holds the gate's cases (clients waiting 2% of the time: nothing taken; under 1%: an idle server
given back; nothing served: nothing taken; adding never gated) and the console parsing.

**Local check of the amended harness (8 October, the four-core machine above, one paired repetition each, the per-process
meter running; not counted).** Three versions of the queue line were tried in the order written, and all three are recorded:

| Pair (select unless named) | host CPU-s, native → omni | `psql` CPU-s | servers alive | p50 (ms) | p95 (ms) | p99 (ms) | work inside the line (tps) |
|---|---|---|---|---|---|---|---|
| the unchanged harness (the meter's pair above) | 573.5 → 626.3 (+9%) | 21.3 → 77.2 | 20 → 7.8 | 0.554 → 0.656 | 4.3 → 23.5 | | 8,088 → 7,859 |
| console held, take-back gated, no add-back | 564.1 → 530.0 (−6%) | 0.9 → 0.8 | 20 → 8.0 | 0.562 → 0.490 | 4.1 → 3.0 | 12.2 → 43.6 | 8,110 → 8,037 |
| the same, one server a second added back | 592.7 → 591.1 (0%) | 1.0 → 1.2 | 20 → 17.7 | 0.582 → 0.590 | 6.9 → 8.0 | 19.3 → 23.2 | 9,052 → 9,051 |
| the same, `tpcb` (the tuning workload) | 513.9 → 520.8 (+1%) | 0.7 → 0.8 | 20 → 14.7 | 3.17 → 3.25 | 74.1 → 46.4 | 213 → 204 | 1,045 → 1,078 |
| **the rule above: one server per percent added back** | 604.7 → 603.3 (0%) | 1.2 → 1.0 | 20 → 18.2 | 0.575 → 0.598 | 8.1 → 12.6 | 24.4 → 40.9 | 9,489 → 9,446 |

Read: the CPU cost is gone in every amended pair (the `psql` line is the sampler's one login and the brain's one), with
PgBouncer and PostgreSQL within a few seconds of native in each (second pair: 139.3 → 136.4 and 315.6 → 290.5; third: 143.1 →
142.7 and 329.1 → 333.7; fifth: 146.7 → 146.6 and 340.2 → 343.5), and the harness's own CPU with the brain running is 0.5 to
0.6 CPU-seconds over a 300 s arm. The gate without an add-back (second pair) let the pool slip one server at every step
boundary, where a second with no waiting is read, and never come back: by the light notches at the end of the arm it stood
at 2 with clients waiting 8% to 28% of the time, which is the harm the amendment is meant to remove, so the add-back was
written. With the add-back the pool follows the demand (at 20 through the peak notches in both arms, 13 to 19 at the light
ones) and the saving is 9% to 11% of the servers on `select` and 27% on `tpcb`, where the pool also rose above 20 on the
force's own add at the peak and fell to 3 at the light notches. The p95 and p99 of the last pair read LOSS or power given in the omni arm,
and the difference sits in the peak notches (45.6 against 27.3 ms at notch 6) where the pool was 20 in both arms for the
whole notch: at nine tenths of the machine's capacity a pair on this box swings by that much on its own (the unchanged
harness's pair read 761 against 15 ms there, and two native-equivalent arms of `tpcb`, below, read 2,688 against 26 ms), so
these single pairs cannot settle the tail and are not asked to; the three-run set is. One fault found by the check and fixed
before the dispatch: in the `tpcb` pair of the second version the brain died at its first read, because the sampler and the
brain shared the one console connection without a lock and a garbled message was read; that arm ran as native in Omni's
name, and the record would have said nothing. The console now takes one query at a time, a garbled message reconnects once,
and a brain that cannot attach writes the fault into its audit and into the arm's record (`controller_error`), so such an
arm reads NO on the hand-back line and says why.

**What is expected, said before the runs.** The host CPU rows should come down to the noise, because the cost was ours; the
median and p95 rows should come back toward native's, because the pool is no longer shrunk into a queue; the connections
held open should still fall, by much less than the 61% to 72% of the first set (the local pairs say 9% to 27%), because the
pool is now taken only from idle servers and given back the moment anyone waits. If the CPU rows stay power given in all three of our runs after
this, the cost is the pooler's or the database's after all and the next amendment is not ours to make; if the connections
row is no longer the same in all three of our runs, that is the result; if the tail rows read LOSS in all three of our runs over three runs, the probing itself
costs service and the rule is not good enough, and that too is the result.

**The second counted set (A2, B2, C2)** runs on this harness, the same inputs as the first (the three untouched workloads,
three paired repetitions, 20 s a notch, three separate dispatches on one commit); its table replaces the first in
`results/live/V3_PGBENCH.md`, and the first set's table moves to `docs/history` with this note, every row kept. The index
reads the second set when it lands and says so.

**Dispatched 2026-10-08 23:16 UTC on commit `310cf318`** (Omni v3 by `tools/omni_version.py --commit`; the amended harness
and this text are in it, nothing in the engine): runs **A2 37858494179, B2 37858496620, C2 37858499033**, the three untouched
workloads, three paired repetitions each, 20 s a notch, dispatched within ten seconds of one another. Nothing above this line
changed after the dispatch.

## The second counted set (runs A2, B2 and C2 of 2026-10-08/09, on amendment 2): the result

Runs 37858494179, 37858496620 and 37858499033, commit `310cf318`, Omni v3, the three untouched workloads, three paired
repetitions each; the table by rule is `results/live/V3_PGBENCH.md` (`tools/pgbench_abc.py`), and the first set's table is
kept whole in `docs/history/V3_PGBENCH_set1.md`.

**The two costs are gone.** Host CPU reads inside the noise on all three workloads (`select` −3.2%, +0.9%, +2.8%;
`simple_update` +1.6% to +2.7%; `tpcb_hot` +2.4% to +6.1%; the first set read +14% to +28%, LOSS in all three of our runs). The median
latency reads inside the noise on all three (`select` −3.8%, +0.9%, +0.7%; the first set read +15% to +17%, LOSS in all three of our runs
on `select` and `tpcb_hot`). The harness's own CPU, now in the table, is 0.4 to 2.5 CPU-seconds an arm with the sampler
included, the brain's share about half a second; every arm made one console login; no arm reported a controller fault; every
pool was handed back and read back.

**What the governor did, workload by workload.**

- `select`: the pool moved between 2 and 20 (170 to 193 take-backs and 29 to 41 queue-line adds an arm, no force add), mean
  13 to 15. **Connections held open 19.3 → 11.9, −36% to −38%, GAIN in all three of our runs** (the first set's −61% to −63% was bought
  with the queue). Work and throughput equal; p95 inside the noise (−12%, +23%, +18%); p99 and mean inside the noise by the
  rule (one run's interval across zero) but higher as point estimates in two runs (p99 +30% and +175%, mean +16% and +46%):
  the probing of the knee shows in the tails and reads inside the noise by the rule. It is in the table.
- `simple_update`: the force rule of amendment 1 ("slow, clients waiting for a server: add") fired 4 to 15 times an arm and
  took the pool to 33 to 38 at its peak. **Connections most at once 20 → 36, +72% to +80%, power given in all three of our runs** (the first set
  read the same, +80%); connections held open +8% to +10%, two runs inside the noise; work, latencies and CPU inside the
  noise. Nothing was bought for the connections added. This cost is not the queue line's and not the console's: it is the
  add rule of amendment 1 buying servers above the operator's setting on a slow write workload, and it stands as written.
- `tpcb_hot`: **the runs disagree** on connections held open (+5% in A, −46% and −48% in B and C). In A the force rule fired 12
  to 19 times an arm and the pool stood near 20 (native's own p95 was 2.4 s on that runner); in B and C it never fired and
  the pool went down to the queue line. Latencies, work and CPU inside the noise.

**Read.** 1 gauge-row GAIN in all three of our runs, 1 power given in all three of our runs, 1 where the runs disagree. The category enters the index at
**+4.0%** (the first set's +14.2% was the connections saving bought with the CPU and the queue the amendment removed). Said
in the founder's words: `select` is a yes with no cost, a third fewer connections and no LOSS; `simple_update` is a no,
more connections at the peak and nothing bought; `tpcb_hot` shows no settled value. What was expected before the runs came
true in three parts of four: the CPU rows came down to the noise, the median came back, the connections saving fell to a
third; the fourth, that the tail rows might read LOSS in all three of our runs, did not happen, and the point estimates say the probing
costs something in the tail that three runs could not settle.

## Amendment 3 (2026-10-09, declared before any run on it): the brain's own verdict on the pool

**Why, and when.** Written after the second counted set was read (the section above: `select` −36% to −38% connections with nothing
power given; `simple_update` connections most at once +72% to +80% power given in all three of our runs with nothing bought; `tpcb_hot` the runs disagree), at
the founder's order of 9 October: Omni need not be wired into every muscle; a knob that cannot prove it pays stays native and Omni
only reads it. The brain must decide that on the muscle itself, in real time, by a measurement.

The rule, the same in the five live harnesses (`tools/knob_verdict.py`, a wrapper around the frozen engine's own
verdict, `omnicompass/verdict.py`, which is unchanged: the engine stays Omni v3): **the knob starts in watch**, one wire out
and nothing written, and the compass's moves are clamped to the allowance a paired trial on the stack itself has earned. Two
directions from the operator's setting, each with its own allowance: **spend** (more of the resource) and **give back**
(less). A trial is one notch past the deepest step already allowed: the reference phase holds the knob at that deepest step
(the operator's setting at first) until 8 one-second samples are in, then the trial phase holds it one notch further for 8
more; the first 2 s after any change are not sampled. The judge is the engine's: the trial's median cost no higher
than the reference's within 2%, and no higher than the cost first measured at the operator's setting. The cost is one sample
a second from the stack's own readings: under the **resource objective** (the Omni index's preregistered reading, the
default) cost = the pool size (server connections) × the host's CPU busy share × the mean transaction time including the wait for a server, from the pooler's own counters / the transactions the pooler counted in the last second, so a step passes only if the service gained
outweighs the resource and CPU spent by the index's own arithmetic; under the **service objective** (`--objective service`)
cost = the mean transaction time including the wait for a server, from the pooler's own counters / the transactions the pooler counted in the last second, the resources shown and not judged. A spend step is tried only while the compass asks to spend
and clients are waiting for a server half the time or more (amendment 1's add condition); a give-back step only while the service is calm and the pooler served transactions, its clients waited under 1% of its time (amendment 2's line) and a server is idle. A trial once started runs on until its
samples are in unless the service swings to the other direction's condition, when it is abandoned; a refused step is not
tried again for 60 s; a trial is started at most every 20 s. During a trial the knob stands at the phase's value whatever
the compass asks; between trials the compass moves it by its own law inside the allowance. The fail-up (back to the pooler's own setting) is always free; a spend above the operator's setting is taken only one notch at a time and only when its trial has shown it pays. Restoring the
operator's setting is always free. Every trial, allowance, refusal and abandonment is written to the audit (`cost`,
`cpu_share`, `verdict_phase`, `verdict_direction`, `allowed_low`, `allowed_high` on every line) and summed in the arm's
record (`verdict`: the objective, the state, the allowance, the counts, the events); the three-run table prints the
brain's verdict per workload and run. The counted runs on this amendment will use 30 s a notch (a whole trial inside one
notch of traffic), declared here; the native arm runs the same ladder. Nothing is typed in; the rule is in the code the
runs execute.

**Expected before the runs.** `select`: connections given back one a trial while calm, −20% to −35% held open, less than the second
set's −36% to −38%, with work, latency and CPU inside the noise. `simple_update`: the add above the operator's 20 is tried once and
refused (a server more buys nothing on a workload the disk bounds), so connections most at once read 20 in both arms and every
gauge inside the noise: the loss in all three of our runs of the second set is gone because the brain refused the move, not because the table
was changed. `tpcb_hot`: inside the noise or a smaller saving. The second counted set stays in `docs/history` as the result of
the rule before this amendment.

**Dispatched (2026-10-10 01:28 UTC, commit `3aac0ab7`, Omni v3 by `tools/omni_version.py --commit`).** At the founder's order of
10 October that every benchmark be run again on the current code, native and omni, the counted runs on this amendment were
dispatched with `workloads=untouched`, `reps=3`, `step_s=30`, the resource objective: runs 38013313943 (A), 38013319893 (B) and 38013324861 (C), 01:28:36 to 01:28:45 UTC. The whole day's dispatch, run by run, is
`docs/RERUN_2026-10-10.md`. The expectation above stands as written before the runs; when they land the table is read from them
(`tools/pgbench_abc.py`), the index, the wiring page and the benefit sheet are read again, and the set this one supersedes goes whole to
`docs/history`.


## Proposed amendment (25 October 2026, not yet in force): a fourth paired repetition

Proposed with omni-v20, to be declared before the next counted set and not applied to any run until then: each pgbench workload
runs four paired repetitions a run instead of three, in the order native/omni, omni/native, native/omni, omni/native. With three,
Omni-Compass always takes arm positions 2, 3 and 6 and native 1, 4 and 5, so a drift of the runner across the arm sequence is not
balanced; the omni-v16 `tpcb_hot` runs showed write stalls of 1 to 6 s landing in either arm by position
(`docs/STORE_LOSS_ROOT_CAUSES_2026-10-25.md`). A fourth pair balances the order and narrows the interval of a stall-driven gauge.
Each run takes about a third longer per workload (eight arms of about 7.5 minutes instead of six). The rules, the gauges, the line,
the notches and the three-run reading are unchanged.

## Amendment 4 (2026-10-30, declared before any run on it): the max on the pooler's pool (the next engine's candidate)

**The cause, from the omni-v21 runs' own files** (`docs/STORE_ROOT_CAUSES_2026-10-30.md`). The pooler stood over its line in 28
seconds of the omni-v21 resource set and amendment 3's allowance refused none of the brain's own rule there; what the allowance
did do, in every arm, was let the calm give-back take the pool below the pooler's own 20 servers (seconds below native, 223 an arm
on average), where a rising load found fewer servers than the operator had set and the queue line (amendment 2) added them back.
The store wires were written on 9 and 10 October, before the founder's order of 12 October that the max is the default brain, and
never brought to it; this brings the pool's wire to it.

**From this amendment** (`tools/run_pgbench.py` `Brain`):

- the spend: clients waiting for a server (amendment 2's rule, ceil(force / 0.1) servers a second) is never clamped by an
  allowance, up to the cover (90 servers; the fail-up to the pooler's own setting as before); the servers held are power given,
  shown beside the waiting they cut;
- the hand-back: the calm give-back and the slow-inside-the-server shrink take a server back only down to the pooler's own
  setting, never below it (the max never goes below native); above it the queue line of amendment 2 and the dwell stand as written;
- the record: the arm's record carries the max's counts (servers added, hand-backs, holds at the pooler's setting) where it carried
  the verdict's allowance; every workload record carries its `dial`; `OMNI_DIAL=save` keeps omni-v21's loop, the verdict under the
  resource objective, where giving servers back is the aim; `tools/knob_verdict.py` joins the fingerprint with this version.

**The model gate** (`tools/store_gate.py`, class S, the omni-v21 arms' recorded seconds replayed open-loop through the candidate,
26 arms): seconds below the pooler's setting 223.5 → 0 an arm (shown), seconds below it while clients waited 7.5 → 0 (GAIN +100.0%),
the pool held 19.3 → 24.7 servers (+28.2%, power given), the knob's moves 18.4 → 23.7 (+28.8%, power given, inside the arms' noise);
no LOSS. The replay cannot show what the servers buy; the first runs on the next engine read it.

**Expected before the runs**, three paired repetitions a run (the proposed fourth repetition stays proposed): the server connections
alive power given; the time clients waited for a server and the latency GAIN or EVEN; the work inside the line GAIN or EVEN; no
second below the pooler's own setting. A LOSS row is a fault to fix, never a number to accept. The counted runs on this amendment run
on the next engine version, which lands only when the model gate reads no LOSS for every store wire it changes.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
