# The Owner's Manual's results sections 16.4 to 16.6 as they stood on the earlier engines (omni-v1 and omni-v3)

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Kept as the road to the engine that stands: these sections were the Owner's Manual's chapter 16.4 to 16.6 until 17 October 2026, written from the three-run tables of omni-v1 and omni-v3. The chapter now reads the omni-v7 tables; no result here is read across engines. The section numbers below are this text's own.

### 16.4 A real database, a real message broker, a real cache

Three stacks whose knob is a resource an operator sizes once and leaves, run as the same shape of test: three paired
repetitions a run, three runs, the operator's fixed setting as native, the compass on that setting through the stack's own
console as omni, a tuning workload shown and not counted, and untouched workloads judged.

- **PostgreSQL 16 behind PgBouncer** (`V3_PGBENCH.md`, the second counted set of 8 to 9 October on amendment 2; the first
  set's table kept whole in `docs/history/V3_PGBENCH_set1.md`): the first set had read connections held open −61% to −72%
  on `select` and `tpcb_hot` with the host's CPU +14% to +28% and the median latency +15% to +17%, all the same in all three of our runs. The CPU was
  then measured and found to be the harness's own `psql` launches, one per reading, not the pooler (+55.9 CPU-seconds on the
  launches against a +52.8 s host difference on a metered repetition; PgBouncer +1.2 s), and the median was the pool shrunk
  into a queue the pooler itself reported (section 10.2). On the amended harness (one console connection an arm; a server
  taken back only while clients waited under 1% of the pooler's time, servers added back one per percent of waiting up to
  the operator's 20) the costs are gone: host CPU and median latency inside the noise on all three workloads. The gain is
  smaller and real: **connections held open −36% to −38% on `select`, GAIN in all three of our runs**, with p95 inside the noise and the
  tails higher as point estimates in two runs, inside the noise by the rule; the runs disagree on `tpcb_hot` (+5%, −46%, −48%: on one runner
  the add rule fired, on two it did not); on `simple_update` the add rule of amendment 1 bought servers above the operator's
  20 on a slow write workload and **connections most at once read +72% to +80%, power given in all three of our runs**, nothing bought for them,
  as in the first set. 1 gauge-row GAIN, 1 LOSS or power given, 1 where the runs disagree; the category entered the index at +4.0%.
  **The set of 10 October, the first with the brain's own verdict on the pool (amendment 3), is the result of record:**
  connections held open **−6% to −11% on `select`, GAIN in all three of our runs**; the add above the operator's 20 on `simple_update`
  refused by the trial, as the amendment expected, so that workload reads inside the noise with nothing bought and nothing
  lost; `tpcb_hot` inside the noise; work, latency and host CPU inside the noise everywhere; every pool handed back. 1
  gauge-row GAIN, 0 LOSS or power given, 0 disagree; the category enters the index at +0.8%. The second set's table is whole in
  `docs/history/V3_PGBENCH_set2.md`. Amendment 4 (a spend trial runs to its samples) is declared and the next set runs.
- **Apache Kafka 3.9.1** (`V3_KAFKA.md`): on light, heavy and burst, work inside the 500 ms line rose 16% to 21%, the
  end-to-end 95th percentile fell from about 1.6 s to 9 to 14 ms, the mean lag fell 92% to 97%, all GAIN in all three of our runs; no
  message was lost in any arm; consumers running rose from 2 to 5.8 to 7.9, power given in all three of our runs; host CPU-seconds rose 10% to
  20% on light, power given in all three of our runs, and read inside the noise on heavy and burst; CPU per thousand messages inside the line
  fell 10% to 12% on burst. Native sat at nine tenths of its measured capacity by design, so its queue grew at the high
  steps and Omni's did not; the gain is the queue kept short and the cost is the consumers that kept it so. 21 gauge-rows toward
  their aims, 8 LOSS or power given, 0 where the runs disagree. **The set of 10 October, the first with the brain's own verdict on the group's
  size (amendment 2), read exactly nothing under both objectives**: every spend trial in all 36 omni arms was abandoned before
  it could be judged, the group stayed at the operator's two consumers (1.98 to 1.99 on average, the trials' reference seconds
  included, a fraction of a consumer GAIN in all three of our runs), and every other gauge read inside the noise, the earlier set's queue
  and tail gains with them. The cause is ours and is said in amendment 3: the rule ended a spend trial when the service turned
  calm, and a consumer that drains the queue calms the service within seconds, so no spend could reach its samples. From
  amendment 3 a spend trial runs to its samples whatever the compass's force; the next set runs on it and becomes the result
  of record. The first set's table is whole in `docs/history/V3_KAFKA_set1.md`; the category stands at +0.1% meanwhile.
- **Redis 7.0.15** (`V3_REDIS.md`): on small, large and burst, work inside the 2 ms line rose 14% to 27%, the hit rate
  14% to 27% and the mean latency fell 30% to 61%, all GAIN in all three of our runs; no request failed; the 95th percentile stayed
  within a hair of native's, because a miss costs the declared 5 ms trip in both arms and 5% of requests still miss; the
  memory ceiling held rose from 64 MB to 200 to 270 MB and the memory used with it, both power given in all three of our runs, the resource the
  gain costs; the host's CPU-seconds read inside the noise on all three; keys evicted fell 76% to 92% (shown); every
  ceiling was handed back. 12 gauge-rows toward their aims, 6 LOSS or power given, 0 where the runs disagree. The tuning workload, shown and not
  counted, read the same way (hit rate 75% to 87%, the ceiling 64 to 299 MB). **The set of 10 October, the first with the
  brain's own verdict on the ceiling (amendment 2), read exactly nothing under both objectives**: the allowance stayed at one
  notch each way (56 to 72 MB), most trials were abandoned before they were judged (the same trial rule as Kafka's, amendment
  3), and every gauge read inside the noise. The next set runs on amendment 3 and becomes the result of record; the first
  set's table is whole in `docs/history/V3_REDIS_set1.md`; the category stands at exactly nothing meanwhile.
- **MongoDB 8.0.32 under YCSB 0.17.0** (`V3_YCSB.md`, `docs/YCSB_PREREGISTRATION.md`): the knob is the storage engine's
  cache size, the operator's 512 MB as native, and the question is the opposite of the Redis one: not whether the governor
  will buy service with memory, but whether it will give memory back without losing service. On workloads c and burst the
  cache held fell by about half (512 to about 260 MB) and on f by 13% to 37%, GAIN in all three of our runs; on b it fell 27% to 50% but
  one run's interval included zero, so that row reads no difference beyond the noise; work inside the 1 ms line, p95 and
  p99 read inside the noise on all four workloads (work between −2.7% and +1.1%, every interval over zero); no operation
  failed in any arm; the host's CPU-seconds read inside the noise on all four, +12% to +15% on c with intervals over zero;
  pages read into the cache rose 14% to 58% (shown, not judged: the misses the smaller cache costs); and one row is a
  loss in all three of our runs, the mean latency on burst, +2.2% to +3.7% in all three runs, clear of zero, which stands. Every cache
  size was handed back in every arm. 6 gauge-rows toward their aims, 1 LOSS or power given, 0 where the runs disagree. The tuning workload, shown
  and not counted, read the same way (the cache 12% to 15% smaller, everything else inside the noise). The disclosure made
  before the run held: on this machine the data sits in the operating system's page cache too, so a storage-engine miss
  costs a memory read and a decompression, not a disk read, which is why half the cache could be given back at no
  measurable cost in work or p95 and a few percent of mean latency; on a machine whose data does not fit in memory the
  same knob would be asked a harder question, and this table does not answer it. That was the first counted set, kept
  whole in `docs/history/V3_YCSB_set1.md`. Its audits showed the memory given back in the first five seconds of every
  burst and c arm, before the first eviction, because a cold cache evicts nothing while it fills (amendment 1, section 10.8:
  the give-back gate is now the miss share under 1% of requests, as MySQL's). **The second counted set (8 to 9 October) is
  the result of record:** the cache held **−21% to −36% on all four untouched workloads, GAIN in all three of our runs**, settling at
  330 to 405 MB, where the gate finds the working set, instead of at the floor; the burst mean latency inside the noise (the
  cost gone); work, p95, p99 and CPU inside the noise everywhere; every cache handed back. 8 gauge-rows toward their aims, 0 LOSS or power given, 0
  where the runs disagree; the category entered the index at +8.5% (the first set's +10.2% included the artefact). **The set
  of 10 October, the first with the brain's own verdict on the cache (amendment 2), is the result of record:** the cache held
  **−3% to −13% on `f`, GAIN in all three of our runs**, with `b`, `c` and `burst` inside the noise (two or three trials an arm, one or two
  allowed, the rest refused or abandoned), work, p95, p99, mean latency and CPU inside the noise on all four, no failed
  operation, every cache handed back. 2 gauge-rows toward their aims, 0 LOSS or power given, 0 disagree; the category enters the index at +0.7%. The
  second set's table is whole in `docs/history/V3_YCSB_set2.md`; amendment 3 is declared and the next set runs.

- **MySQL 8.0.46 under sysbench 1.0.20** (`V3_SYSBENCH.md`, `docs/MYSQL_PREREGISTRATION.md`): the knob is the InnoDB buffer
  pool, 512 MB at the operator's setting, moved in the server's own 128 MB chunks inside [128, 2,048] MB through the server's
  own console. Two counted sets were run on the same engine. The first (runs 37757840760, 37757850988, 37757861572) read every
  gauge inside the noise and its hand-back row read NO on 15 of 45 omni arms, because the plug's restore was issued while the
  server was still carrying out a shrink the law had asked for, which MySQL ignores; the plug, not the law, was fixed (the
  restore waits for the server's resize and writes again), the fix was declared as an amendment, and the first set's table is
  kept whole in `docs/history/V3_SYSBENCH_set1.md`. The second set on the amended plug (runs 37770617236, 37770620582,
  37770624805, commit `a033fd09`) is the result: on the four untouched workloads **the pool held fell −67% on burst and −50% to
  −56% on read_only, GAIN in all three of our runs**, with the pages holding data falling the same; work inside the line, throughput, p95,
  p99 and host CPU inside the noise on every workload; on read_write, where the working set is written as well as read, the
  compass bought pool for the wide notches and **the pages holding data rose +53% to +70%, power given in all three of our runs**, the pool held
  +59% to +79% as point estimates (one run clear of zero), while p95 read −11% to −18% and CPU −4% to −5% inside the noise;
  update_index inside the noise on every row; no error in any arm; **the pool handed back and read back on all 45 omni arms**.
  4 gauge-rows toward their aims, 1 LOSS or power given, 0 disagree; the category enters the index at +12.2%. The update_index "work inside the line"
  row counts almost nothing in either arm (a single update's client round trip exceeds the server-side 0.6 ms line) and is
  disclosed as such. That was the second counted set, kept whole in `docs/history/V3_SYSBENCH_set2.md`. Amendment 2 (8
  October, section 10.9) followed its read_write row: 36 of that workload's 82 grows bought chunks while the pool missed under
  1% of its reads, for slow writes the pool cannot mend, so the pool now grows only while missing, and no chunk goes back in
  a second without a read request. **The third counted set (8 to 9 October) is the result of record:** burst pool held
  **−49% to −56%, GAIN in all three of our runs**; read_write pages holding data **+44% to +52%, power given in all three of our runs**, with host CPU **−4% to
  −6%, GAIN in all three of our runs**, a trade of memory for CPU with latency unchanged; read_only inside the noise (the second set's
  −50% to −56% was in part the first chunk given back before any read, a cold-start artefact now refused, and the pool is
  then bought back on real misses as the notches widen); update_index the runs disagree; every pool handed back. 4
  gauge-rows toward their aims, 1 LOSS or power given, 1 where the runs disagree; the category entered the index at +5.2%. **The set of 10 October,
  the first with the brain's own verdict on the pool (amendment 3), is the result of record:** the pool held **−10% to −20% on
  `read_write`, GAIN in all three of our runs**, the pages holding data with it, the earlier set's memory bought for the written working set
  gone; `burst`, `read_only` and `update_index` inside the noise (the give-back trials judged, the grow trials mostly abandoned
  by the trial rule amendment 4 corrects); work, p95, p99 and CPU inside the noise on every workload; no error; every pool
  handed back. 2 gauge-rows toward their aims, 0 LOSS or power given, 0 disagree; the category enters the index at +1.0%. The third set's table is
  whole in `docs/history/V3_SYSBENCH_set3.md`; amendment 4 is declared and the next set runs.

### 16.4b Robustness: the governor killed outright, and its own cost

The robustness benchmark (`docs/ROBUSTNESS_PREREGISTRATION.md`) is a test of Omni-Compass itself, not of a gain. In the
kill scenario (`V3_ROBUST_KILL.md`, ten pairs in each of three runs), the governor received SIGKILL at 40% of a 900 s
window on the wandering load, with the watchdog running beside it from the start as it would in service. In all thirty
repetitions the watchdog found the dead lease on its next pass, ran the governor's recorded restore command, and every
setting (the HPA target, the replica range, every pod's CPU limit, every worker, the records on the objects) was back at
the operator's **7 to 11 s after the kill**, mean 9 s against a preregistered allowance of 60 s; a second governor started
at 50% and governed to the end in every repetition; and the 120 s after the kill read no difference beyond the noise
against native's same window in all three runs, so the service did not measurably notice the governor's death. The whole
window, with a kill and a restart inside it, still read mean response 32% to 39% faster, p95 42% to 45% faster, time over
the line 28% to 34% lower and failed requests 9% to 15% fewer, GAIN in all three of our runs, with machines and energy inside the noise.
Run again on 10 October (`V3_ROBUST_KILL.md`, the set of record): every setting back within the allowance in every repetition
of every run, a second governor to the end in every one, and the whole window read mean response 33% to 40% faster, p95 27% to
48%, time over the line 32% to 36% lower, GAIN in all three of our runs, with failed requests, machines and energy inside the noise; the
first set's table is whole in `docs/history/V3_ROBUST_KILL_set1.md`.
The governor's own CPU over every archived run with the real cluster inside (`V3_OWN_COST.md`) is 0.006 to 0.013 of one
core at every size from 1 to 1,000 copies, 0.1% to 0.3% of the host's cores, each run under its own engine; the cost of
governing a real cluster does not grow with the modelled organism around it.

**The long run** (`V3_ROBUST_LONG.md`, three pairs of 7,200 s an arm in each of three runs) asks whether the governor
drifts, leaks or slows over hours. Its resident memory after two hours was at most 1.048, 1.067 and 1.052 times its first
ten minutes in the three runs, against a preregistered limit of a quarter: no leak. It made 117 to 119 of the 120
decisions its 60-second interval predicts in every repetition, 97.5% at the fewest against a threshold of 95%: valid. Its
decision time, read as the gap between consecutive decisions less the interval it sleeps, was at most 1.20 times in the
last hour what it was in the first: no slowing. Every setting was handed back at the end of every repetition and read
back at the operator's with no record left. Two things are shown rather than judged, as the preregistration said they
would be. First, failed decisions: 2, 3 and 3 in the three runs, all in one repetition's omni arm, all the same cause, the
cluster's own API answering 500 to the governor's read of the HPA for two or three decisions in a row; the governor held,
wrote nothing, and resumed on the next good read, which is the blind-means-hold rule doing what section 7.3 says it does.
Second, the whole window's service: with three pairs a run the intervals are wide, and mean response, p95, p99 and time
over the line read GAIN in all three of our runs in run A and inside the noise in B and C, so the reading is no difference beyond the
noise in two of three runs; machines, energy and failed requests read inside the noise in all three. The long run is a
test of the governor's constancy, and on that question every row answered as the preregistration required. Run again on 10
October (`V3_ROBUST_LONG.md`, the set of record): no leak (memory under its limit in every repetition), every decision valid,
no slowing, every setting handed back; the service GAIN in all three of our runs in run B and inside the noise in A and C; the first set's
table is whole in `docs/history/V3_ROBUST_LONG_set1.md`. The 24-hour run on three rented machines was collected the same day
and its table follows.

### 16.5 The modelled realms and the independent simulators

Every result here is evidence class S: a statement about a published model under its own native controller, never about
hardware, and never counted in the Omni index.


- **The 945 muscles and six organisms** (`results/realms/REALMS.md`, A/B/C on v3): reproduced to the last digit in three
  of three runs; zero muscles LOSS or power given; every organism superior within guardrails, with work per energy +0.1% to +0.3%, work
  unchanged and time over the line not above native's. On v2 the Physics realm and the tower had read a service tradeoff;
  the slack gate on speed knobs corrected it and made v3.
- **The grid of copies and runs** (`results/scale/GRID.md`, 84 of 90 cells on v3): every organism superior within
  guardrails in every cell of ten runs or more; work per energy +0.07% (Physics) to +0.37% (Energy, the four stacked, the
  tower), the same figure at every size; every knob handed back; the six cells left are beyond the machines available.
- **The power grid** (`V1_PANDAPOWER.md`, `V3_PANDAPOWER.md`, the same table to the digit): eleven SimBench grids solved
  by pandapower, the tap changer's own controller as native, one whole tap per move as the knob. With ZIP loads the energy
  the loads drew fell 1.3% to 1.5% and the net import fell in all eleven grids; losses fell in seven and **rose in four**
  (the rural and semi-urban grids with their own generation, +0.6% to +1.5%); tap operations fell in ten grids and rose
  from 4 to 8 a year in one, the declared cost, power given in all three of our runs; no grid was more often outside its voltage band. 67
  gauge-rows toward their aims, 14 LOSS or power given.
- **Robot arms** (`V1_MUJOCO.md`, `V1_MUJOCO_PANDA.md`, `V3_MUJOCO.md`): four arms from the MuJoCo Menagerie with their
  shipped controllers as native and the joint speed of an axis with slack as the knob, after a paired physics trial. The
  trial left the UR5e and the iiwa 14 native ("nothing for Omni to move"); on the Gen3 and the Panda, peak torque fell 29%
  and 10%, tracking error 21%, energy per takt 0.8% and 0.5%, GAIN in all three of our runs; the Panda's copper loss **rose 14%**,
  power given in all three of our runs.
- **Buildings with batteries** (`V1_CITYLEARN.md`, `V3_CITYLEARN.md`): every district CityLearn ships, its own rule-based
  control as native, each building's battery charge and discharge inside the simulator's limits as the knob. In the
  eleven battery districts electricity bought, the daily peak and the daily unevenness fell in all eleven and carbon in
  eight, GAIN in all three of our runs; the bill **rose in seven** (the 2023 districts) and ramping rose in seven, power given in all three of our runs; 71
  score-rows toward their aims, 33 LOSS or power given, 1 where the runs differ by the simulator's own variation; three districts had nothing to
  move and eight the simulator cannot run.
- **Drone swarms** (`V3_SWARM.md`): twenty Crazyflie 2.x quadrotors in gym-pybullet-drones with the shipped position
  controller as native and the cruise override inside the autopilot's limits as the knob, three untouched cells. Energy a
  mission fell 7% (short), 18% (mixed) and 20% (long) and missions a charge rose 8%, 22% and 25%, GAIN in all three of our runs; no late
  mission, reserve breach, near miss or collision in any arm; the tracking error rose from 0.07 to 0.13 m inside its
  0.25 m band, shown; every override handed back. PyBullet reproduced to a part in a thousand across GitHub's machines and
  not to the bit, so the table's reproduction tolerance was set to one part in a thousand after the runs were seen, and
  the preregistration's amendment 1 says so with its time.

### 16.6 The one number, and the table

**The one number.** The Omni index over the real categories the same in all three of our runs, on the sets of 10 October: **+4.8%** (real
Kubernetes on v3 +28.9% over seven tests, the real database on v3 +0.8%, real messaging on v3 +0.1%, the real cache on v3
exactly nothing, the real database's storage-engine cache on v3 +0.7%, the real database's buffer pool on v3 +1.0%, each
category weighed the same; Azure and the card join as their three-run tables land). How it got here, set by set, follows; the
figures of 7 to 9 October below are history, kept in the tables of `docs/history`. The fifth category lowered the headline from +30.2% to +25.9% when it joined
on 8 October; the sixth, MySQL's buffer pool, entered the same day at exactly nothing on its first counted set (every row
inside the noise, the headline at +21.2%) and at +12.2% on the second set run the same afternoon on the amended plug, the
headline at +23.5%; the public-trace test (section 16.1) joined the Kubernetes category as its seventh test the same
evening, moving that category from +25.5% to +28.8% and the headline to +24.1%; and on 9 October the three database
categories were re-read on their second or third counted sets, after the costs the first sets had charged to the governor
were measured and found to be our own harness (section 16.4): the database fell from +14.2% to +4.0%, the storage-engine
cache from +10.2% to +8.5%, the buffer pool from +12.2% to +5.2%, and the headline from +24.1% to +20.5%. The number went
down because the costs came out and took the gains they had been propping up with them; what is left is smaller and has
nothing of ours under it. The same day a **second reading** was declared beside the first, at the founder's question about
what a cache is for (`docs/K8S_COMPASS_PREREGISTRATION.md`, the service reading): the same tests and the same three-run
rule scored on work and speed only, the resources spent or saved shown and not scored, computed for every test alike. It
stood, on the day it was declared, at **+71.8%**: Kubernetes +83%, Kafka +1,193% (its hundredfold tail), Redis +8.8% where the
resource reading said −24.9%, and the three database stacks exactly nothing, because their gains are resources given back for
the same service; on the sets of 10 October it stands at **+10.7%** (Kubernetes +84.5%, the five stacks nothing).
The two readings are two true sentences about the same tables: one says what the governor did for the service, the other
what it cost or saved in resources to do it. The resource reading stays the headline because it was the one preregistered;
the service reading is printed in the same file, in the same tables, as a second column. A category enters at whatever its tables
show in all three of our runs, nothing included, which is the reader's guarantee
that the number is not built from the categories that happened to work. That is how the number is meant to move: every real category enters at equal weight as its table lands, whatever it does to the mean.



**10 October: every table remade, the stacks under the brain's own verdict.** Every benchmark was run again on one commit and
every table read from the new runs. The five stacks ran for the first time with the brain's verdict on the knob (section 9.4),
and the headline moved from +20.5% to **+4.8%**, the service reading from +71.8% to **+10.7%**. The number came down for one
reason: the spends that had bought the earlier gains at a resource cost were refused by the verdict where they did not pay
(MySQL's pool for the written working set, PostgreSQL's add on the slow write workload) and, on Kafka and Redis, not yet judged
at all, because the trial rule of 9 October ended a spend trial on the calm the spend itself produced (amendment 3, section
16.4; the next set runs on the corrected rule). What is left is smaller than before and has two properties the earlier number
did not: every gain in it was proved on the stack itself before the knob was written, and no category carries a loss in all three of our runs.
The storage-engine cache's figure is positive for the reason the Redis figure is negative, read the other way: there the
governor gave memory back (the cache held halved on two workloads) while work, p95 and CPU stayed inside the noise, so
its resource column is a gain and its other columns are exactly one; its one loss in all three of our runs, the burst mean latency, is
not an index column and stands in its table. The messaging figure is large because its speed ratio is:
native sat at nine tenths of its measured capacity by design, so its queue grew at the high steps and its slowest 5%
waited 1.6 s, while Omni's waited 9 to 14 ms; the resource that bought it, three to four times the consumers, stands
beside it as a loss in all three of our runs. The cache's figure is negative because the memory held is its resource column: the ceiling
rose from 64 MB to 200 to 270 MB (a ratio of about 0.25 in the index's "fewer machines" sense) while work and the hit rate
rose 14% to 27%, and a geometric mean of those four columns is below one. That is the arithmetic of a resource bought,
reported as such; a reader who weighs memory as cheaper than a consumer or a machine will read the cache's rows for
themselves, which is why every row is in its table.

| Result | Engine | Class | Reading | Source |
|---|---|---|---|---|
| **Real Kubernetes, all four in one run** (load up and down one step at a time, 10 pairs × 3 runs) | v1 | L | work inside the response line **+42% to +48% in all three runs, GAIN in all three of our runs**; p95 −57% to −63% GAIN in all three of our runs; failed requests −12% to −13% GAIN in all three of our runs; machines no difference beyond the noise | `results/live/V1_ALL_FOUR.md` |
| **Real Kubernetes, steady work in steps** (10 pairs × 3 runs) | v1 | L | p95 **−65% to −69%** and time over the line GAIN in all three of our runs; machines −1.5% to −3.4% GAIN in all three of our runs; failed requests zero in both arms | `results/live/V1_STEADY.md` |
| **Real Kubernetes, demand that wanders** (10 pairs × 3 runs) | v1 | L | p95 **−56% to −60%** GAIN in all three of our runs; failed requests GAIN in all three of our runs; modelled standby energy −0.4% to −0.8%, GAIN in all three of our runs | `results/live/V1_WANDERING.md` |
| **Real Kubernetes, faults** (a machine down, a spike, a runaway pod, a blind probe, 10 pairs × 3 runs) | v1 | L | p95 **−61% to −64%** GAIN in all three of our runs; failed requests, machines and energy no difference beyond the noise | `results/live/V1_FAULTS.md` |
| **Real Kubernetes, a queue of batch jobs** (cruise, then idle, 10 pairs × 3 runs) | v1 | L | machines **−15% to −24%** and modelled energy −11% to −17% GAIN in all three of our runs; p95 no difference beyond the noise | `results/live/V1_BATCH.md` |
| **Real Kubernetes, fairness** (a noisy neighbour on the same workers, 10 pairs × 3 runs) | v1 | L | no difference beyond the noise on every row: Omni-Compass neither helps nor hurts the neighbour | `results/live/V1_FAIRNESS.md` |
| **The same six Kubernetes tests on v3** (10 pairs × 3 runs each) | v3 | L | the same readings as v1, the controllers being v1's bytes: all four work inside the line +35% to +49%, p95 −47% to −66% across steady, wandering, all four and faults, failed requests −9% to −14% where they occur, steady machines −1.5% to −2.9%, batch machines −19% to −23% and standby-model energy −13% to −16%, all GAIN in all three of our runs; fairness no difference beyond the noise on every row | `results/live/V3_STEADY.md`, `V3_WANDERING.md`, `V3_ALL_FOUR.md`, `V3_FAIRNESS.md`, `V3_FAULTS.md`, `V3_BATCH.md` |
| **Real Kubernetes under a public day of demand** (the Google cluster trace of 2011 replayed one step at a time, 10 pairs × 3 runs) | v3 | L | p95 **−65% to −71%**, p99 −49% to −61%, time over the line −81% to −84%, failed requests −8% to −17%, machines in service **−6% to −10%**, replicas −5% to −6%, standby-model energy −4% to −7%, all GAIN in all three of our runs; pods started +23% to +35% as point estimates, inside the noise in one run; 9 rows toward their aims, 0 LOSS or power given | `results/live/V3_TRACE_GOOGLE2011.md` |
| **Real Kubernetes with its add-ons: Omni-Compass on top of KEDA** (KEDA 2.21 and its HTTP add-on 0.16, two native setups, 10 pairs × 3 runs each) | v3 | L (energy S) | p95 **−51% to −53%** (KEDA on CPU and requests) and **−73% to −76%** (the HTTP add-on alone), time over the line −96% to −100%, GAIN in all three of our runs; machines **−5.9% to −7.8%** with the HTTP add-on, GAIN in all three of our runs, inside the noise with the CPU target; idle-power energy **+1.0% to +2.6%, power given in all three of our runs** in both (more work put through by the closed-loop load, shown, not judged) | `results/live/V3_KEDA_CPU_REQUESTS.md`, `results/live/V3_KEDA_REQUESTS.md` |
| **The six organisms with the real cluster inside**, 1 to 1,000 copies, 5 paired repetitions a cell (3 at 1,000) | v1 | L + S | 98 of 100 cells: p95 and time over the line GAIN in every cell; 0 gauges LOSS beyond the noise except a rounding-level work loss (−0.0003%) and HPA replicas +0.7% in one cell; machines stay at 6 in both arms (no autoscaler under kind); the Physics realm and the tower at 1,000 copies off the clock in 2 of 3 repetitions (marked) | `results/live/V1_SIX_KUBE.md` |
| The same at 10 and 100 copies | v3 | L + S | 12 cells, 5 pairs each: every cell GAIN on 4 to 6 gauges, LOSS on none beyond the noise except a rounding-level work loss in 4 cells; the stack at 100 copies off the clock in 4 of 5 repetitions (marked) | `results/live/V3_SIX_KUBE.md` |
| **The big organisms at 1,000 copies on rented machines, on v3**: the tower (3 of 3) and the four stacked (3 of 3), each on its own machine with a 10,800 s window, every repetition on the clock | v3 | L + S | tower: the cluster's p95 **6.7 s → 160 ms (−98%)**, p99 −98%, time over the line 76% → 0, failed requests 4.8% → 0, clear of zero; stack: p95 **2.9 s → 150 ms (−95%)**, p99 −97%, time over the line 51% → 0, failed requests 0.14% → 0, clear of zero; machines 6 in both arms of both; energy inside the noise; the organisms' model work rounding-level lower by rule, energy −0.4% | `results/live/V3_BIG_ORGANISM.md` |
| **The big organisms at 1,000 copies on a rented machine**: the tower (3 of 3) and the four stacked (3 of 3, detached) | v1 | L + S | tower: p95 **−95%** (4.1 s → 0.2 s) and time over the line −99.7% clear of the noise, machines 6 in both arms, energy −0.2%, work rounding-level lower, repetition 3 off the clock; stack: p95 **−74%** and p99 −83% clear of the noise, the compass arm 300 to 615 s past the 2,880 s window in all three (marked OFF THE CLOCK; native kept the clock), which is why the v3 stack runs with a 10,800 s window | `results/live/V1_BIG_ORGANISM.md` |
| **Azure AKS, the bill, steady load**, 4 workers, 5 pairs | v1 | L (a real bill) | no difference beyond the noise on any gauge; the bill −4.7% with its interval across zero; a fleet of 4 cannot show the lever (10.1) | `results/live/V1_AKS_STEADY.md` |
| **Azure AKS, the bill, a burst sized to the cluster**, 4 workers, 5 pairs (repetition 4 lost its native cluster to an Azure API error in the first attempt and was run again by itself) | v1 | L (a real bill) | the bill +5.0% with its interval across zero; machines, p95 and failed requests inside the noise; p99 −34% clear of the noise in this one run; B and C to follow | `results/live/V1_AKS_BURST.md` |
| **PostgreSQL behind PgBouncer, the three untouched workloads**, 3 pairs × 3 runs (the set of 10 October, the brain's verdict on the pool, amendment 3) | v3 | L | connections held open **−6% to −11% on `select`, GAIN in all three of our runs**; the add above the operator's 20 on `simple_update` refused, nothing bought, nothing lost; `tpcb_hot` inside the noise; work, latency and host CPU inside the noise everywhere; every pool handed back; the earlier sets whole in `docs/history` | `results/live/V3_PGBENCH.md` |
| **MySQL under sysbench, the four untouched workloads**, 3 pairs × 3 runs (the set of 10 October, the brain's verdict on the pool, amendment 3) | v3 | L | the pool held **−10% to −20% on `read_write`, GAIN in all three of our runs**, the pages holding data with it; `burst`, `read_only` and `update_index` inside the noise; work, p95, p99 and CPU inside the noise on every workload; no error; every pool handed back; the three earlier sets whole in `docs/history` | `results/live/V3_SYSBENCH.md` |
| **The 945 muscles and six organisms, modelled**, A/B/C | v3 | S | reproduced to the last digit in 3 of 3; 0 muscles LOSS or power given; **every organism superior within guardrails** (work per energy +0.1% to +0.3%, work unchanged, time over the line not above native's); on v2 Physics and the tower read a service tradeoff, which the slack gate corrected | `results/realms/REALMS.md` |
| **The organisms at 1, 10, 100 and 1,000 copies**, 1 to 1,000 paired runs a cell, 84 of 90 cells | v3 | S | every organism superior within guardrails in every cell of 10 runs or more; work per energy +0.07% to +0.37%, the same figure at every size; the six cells left (100 and 1,000 runs at 1,000 copies) are beyond the machines available | `results/scale/GRID.md`, `results/scale/receipts/` |
| **Power grid: 11 SimBench grids solved by pandapower**, both load models, A/B/C | v1 and v3 (the same table to the digit) | S | with ZIP loads the energy the loads drew GAIN in all three of our runs in all 11 (−1.3% to −1.5%) and the net import in all 11; losses GAIN in all three of our runs in 7 and **power given in 4** (the rural and semi-urban grids with their own generation, +0.6% to +1.5%); tap operations fewer in 10 grids, 4 → 8 a year in one (power given in all three of our runs, the declared cost); no grid more often outside its band | `results/live/V1_PANDAPOWER.md`, `V3_PANDAPOWER.md` |
| **Robot arms, MuJoCo Menagerie**, A/B/C | v1 and v3 | S | where Omni-Compass moved (Gen3, Panda): peak torque −29% and −10%, tracking error −21%, energy per takt −0.8% and −0.5%, GAIN in all three of our runs; the Panda's copper loss +14% **power given in all three of our runs**; UR5e and iiwa 14 left native by the paired physics trial | `results/live/V1_MUJOCO.md`, `V1_MUJOCO_PANDA.md`, `V3_MUJOCO.md` |
| **CityLearn, every district it ships**, A/B/C | v1 and v3 | S | 11 battery districts: electricity bought, daily peak and daily unevenness GAIN in all three of our runs in all 11, carbon in 8; the bill **power given in 7** (the 2023 districts) and ramping higher in 7; 71 score-rows toward their aims, 33 LOSS or power given, 1 where the runs differ (the simulator's own variation); 3 districts with nothing to move; 8 the simulator cannot run | `results/live/V1_CITYLEARN.md`, `V3_CITYLEARN.md` |
| **Drone swarms, gym-pybullet-drones** (Crazyflie 2.x, the shipped autopilot as native; Omni on the cruise override inside the autopilot's limits), 20 drones × 4 missions, three cells, A/B/C | v3 | S | energy a mission −7% (short), −18% (mixed), −20% (long) and missions a charge +8% to +25%, GAIN in all three of our runs; no late mission, reserve breach, near miss or collision in any arm; tracking error 0.07 → 0.13 m inside its 0.25 m band | `results/live/V3_SWARM.md` |
| **Apache Kafka as shipped, a consumer group's operator-set size** (one broker, 8 partitions; the group at the operator's 2 consumers as native; Omni on the count inside [1, 8]), three untouched workloads, 3 pairs × 3 runs, under both objectives (the set of 10 October, the brain's verdict on the count, amendment 2) | v3 | L | exactly nothing: every spend trial abandoned before it was judged, the group at the operator's two, every gauge inside the noise; our trial rule, amended as amendment 3, the next set running; the first set (work inside the line +16% to +21%, p95 1.6 s → 9 to 14 ms, consumers 2 → 6 to 8 power given in all three of our runs) whole in `docs/history/V3_KAFKA_set1.md` | `results/live/V3_KAFKA.md`, `results/live/V3_KAFKA_SERVICE.md` |
| **Redis as shipped, a cache's operator-set memory ceiling** (64 MB, allkeys-lru as native; Omni on the ceiling inside [16, 512] MB through Redis's own console), three untouched workloads, 3 pairs × 3 runs, under both objectives (the set of 10 October, the brain's verdict on the ceiling, amendment 2) | v3 | L | exactly nothing: the allowance one notch each way, most trials abandoned before they were judged, every gauge inside the noise; amendment 3, the next set running; the first set (work inside the line +14% to +27%, the ceiling 64 → 200 to 270 MB power given in all three of our runs) whole in `docs/history/V3_REDIS_set1.md` | `results/live/V3_REDIS.md`, `results/live/V3_REDIS_SERVICE.md` |
| **MongoDB as its publisher ships it, a database's operator-set storage-engine cache size** (512 MB as native; Omni on the cache size inside [256, 2,048] MB through the server's own console), YCSB's workloads b, c, f and burst untouched, 3 pairs × 3 runs (the set of 10 October, the brain's verdict on the cache, amendment 2) | v3 | L | the cache held **−3% to −13% on `f`, GAIN in all three of our runs**; `b`, `c` and `burst` inside the noise; work, p95, p99, mean latency and CPU inside the noise on all four; no failed operation; every cache handed back; the two earlier sets whole in `docs/history` | `results/live/V3_YCSB.md` |
| **Robustness: the governor killed outright mid-run** (SIGKILL at 40% of the window, the watchdog beside it), 10 pairs × 3 runs (the set of 10 October) | v3 | L | every setting back within the allowance in every repetition of every run, a second governor to the end in every one; the whole window mean response −33% to −40%, p95 −27% to −48%, time over the line −32% to −36%, GAIN in all three of our runs; failed requests, machines and energy inside the noise; the first set (7 to 11 s to hand back) whole in `docs/history/V3_ROBUST_KILL_set1.md` | `results/live/V3_ROBUST_KILL.md` |
| **The governor's own cost** at 1, 10, 100 and 1,000 copies with the real cluster inside | v3 and v1, each under its own engine | L | 0.006 to 0.013 of one core at every size, 0.1% to 0.3% of the host's cores; shown, not judged | `results/live/V3_OWN_COST.md` |
| **Scale**: the controller governing 50, 500 and 1,000 stand-in nodes (KWOK's nodes, no machines behind them), decision time and correctness | every push | L | runs on every push | `results/scale/` |
| GPU, one card and the card inside the organisms | earlier card controller | P | **obsolete**: every earlier card result ran on a controller since replaced; the one-card, card-inside-1,000-copies and eight-card runs are run again by the founder on rented cards after the CPU and cloud work, at one named commit | `docs/GPU_PREREGISTRATION.md`, `docs/GPU_RUN_GUIDE.md` |

**Running now** (9 October): both big organisms at 1,000 copies done on rented machines (the four stacked and the whole
tower, 3 of 3 on the clock each, section 16.2); the three database tables re-read on their second or third counted sets
after the costs the first sets charged to the governor were traced to our own harness and removed (section 16.4; the
amendments in sections 10.2, 10.8 and 10.9); the robustness test
(`docs/ROBUSTNESS_PREREGISTRATION.md`), the kill scenario and the two-hour long run both done (section 16.4b), the
24-hour run on three rented machines in its second (omni) arm (one pair a machine, two arms of a day each, collected on
10 October);
the real cluster under a public demand trace done (the Google cluster trace of 2011, `V3_TRACE_GOOGLE2011.md`, section
16.1), the Azure Functions trace next by the same rule;
the real cluster with its add-ons done for KEDA and its HTTP add-on (`V3_KEDA_CPU_REQUESTS.md`, `V3_KEDA_REQUESTS.md`,
section 16.1), Karpenter on Azure next;
YCSB on MongoDB done (`V3_YCSB.md`, section 16.4), MySQL's buffer pool under sysbench done (`V3_SYSBENCH.md`, section 16.4),
the other stores of register row 24 after; and Azure steady and burst on the fleet of several machine families (seven
dispatches refused by Azure's own cluster capacity in eastus or held by our own machines' quota, 34 refusals, amendments 5
to 8; the eighth dispatch follows the 24-hour machines' collect). **Queued, in order, in `docs/REGISTER.md` section 4**: drone swarms and
defense edge (PX4 and ArduPilot multi-vehicle, Crazyswarm), databases and caches at large (YCSB, HammerDB), Spark,
OpenSearch, fio, Open-RMF, the 24-hour robustness run, spacecraft attitude and thrusters (Basilisk),
station-keeping (Orekit, GMAT), constellations, rockets (RocketPy, OpenRocket) and combustion (Cantera). Pure physics
solvers (OpenFOAM, SU2, REBOUND, GADGET, MESA) are not benchmarked: they have no controller and no knob, so Omni-Compass
has no place on them; their value is the HPC cluster that runs them.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
