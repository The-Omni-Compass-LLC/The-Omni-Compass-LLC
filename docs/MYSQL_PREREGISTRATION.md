# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool, preregistered

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written 2026-10-08, before any counted run. The rules below are set on the tuning workload (run on one machine, never counted)
and are then applied unchanged to the untouched workloads; every row is reported, losses included; the readings are the three-run
readings of `docs/OMNI_V1.md`. The runner is `tools/run_sysbench.py`, the workflow `.github/workflows/sysbench.yml`, the three-run
table `tools/sysbench_abc.py`. This is register row 24 (databases and caches at large), its second store after MongoDB; the row
named HammerDB's TPC-C for MySQL, and sysbench's published OLTP workloads are run first because Ubuntu ships sysbench as its own
package (one less thing fetched from outside), with TPC-C through HammerDB to follow.

## Why this benchmark

The InnoDB buffer pool is the one cache every MySQL operator sizes, once, at installation, for the machine they had and the
working set they expected; MySQL's own shipped default is 128 MB, and the setting is changed online, in whole chunks, by one
statement through the server's own console. The working set moves: a report widens it, a quiet hour narrows it. Too small a pool
reads pages from the file system on every touch; too large a pool holds memory the machine's other tenants could use. The fixed
pool is the native controller here, and Omni-Compass sits on top of it with sysbench's published OLTP workloads asking the
questions. It is the mirror of the MongoDB test with the most common database in the world: the same plug, the same rule, a
different engine's console.

## What is someone else's

- **MySQL 8.0 as Ubuntu ships it** (Oracle's MySQL Community Server from Ubuntu's own `mysql-server` package), one server on the
  machine, its configuration as shipped but for the settings an operator sets for InnoDB: the buffer pool, **512 MB**
  (`innodb_buffer_pool_size`; MySQL's own default is 128 MB, and 512 MB is set here so that the first notches of the working set fit
  the pool and the last do not, the same shape as the MongoDB test), the chunk the server resizes in, 128 MB (the shipped
  `innodb_buffer_pool_chunk_size`), one buffer pool instance, and the performance schema on (it is on by default; it is named so
  the reading's source is plain). The version the runner finds is recorded in every result.
- **sysbench** (Alexey Kopytov's sysbench, GPL, as Ubuntu's own `sysbench` package ships it, version 1.0 series) with its published
  OLTP scripts as shipped (`oltp_point_select`, `oltp_read_only`, `oltp_read_write`, `oltp_update_index`); only the table count, the
  table size, the thread count, the offered rate, the run time and the request distribution (uniform, for the reason the first
  smoke run gave below) are set from the command line.
- **The machine:** a GitHub Actions runner (4 cores, 16 GB): the server and sysbench share it. There is no watt-meter on it.

Nothing here models a database. Omni-Compass writes one setting through the server's own console (`SET GLOBAL
innodb_buffer_pool_size`) and reads what the server itself reports (`SHOW GLOBAL STATUS`: the pool's pages, the pages holding data,
the pages read from disk, the resize status; `performance_schema`: the statements' own timer) and what sysbench itself records.

## The load

For each workload six tables of 1,000,000 rows each are prepared once by sysbench (about 240 MB of data and index a table), and
both arms read the same rows. Before every arm the server is restarted at the operator's configured pool and the operating
system's page cache is dropped, so both arms start cold alike. The **working set** then steps one notch at a time, **1 2 3 2 3 4 5
6 5 4 3 2 1 2 1**, 20 s a notch (the burst workload steps **1 6 1 8 1 6**): notch n lets sysbench range over the first n tables,
**drawn uniformly** (`--rand-type=uniform`), about 240 MB at notch 1 and 1.4 GB at notch 6, so the working set is the tables in
use and fits the operator's pool at the low notches and outgrows it at the high ones. sysbench offers transactions at a **fixed rate** (its `--rate`, open-loop: the next transaction is due whatever the
last one took) **from 32 threads**, the same in both arms, and counts every transaction's latency into its own histogram (buckets
about 2% apart), from which the gauges are read.

| Workload | sysbench script, as shipped | Statements a transaction | Offered a second |
|---|---|---:|---:|
| **tuning** | `oltp_point_select` (one primary-key read) | 1 | 3,000 |
| read_only | `oltp_read_only` (10 point reads, 4 range reads) | 14 | 300 |
| read_write | `oltp_read_write` (the read-only mix, 2 updates, a delete, an insert) | 18 | 200 |
| update_index | `oltp_update_index` (one indexed update) | 1 | 1,000 |
| burst | `oltp_read_only` on the burst steps | 14 | 300 |

The offered rates are chosen under the runner's capacity for each script so that the pool, not the processor, is the thing being
asked about; they are declared here and are the same in both arms.

## Arms

- **native:** MySQL at the operator's pool, 512 MB, for the whole run.
- **omni:** the same, with the compass law (`omnicompass/compass_law.py`) on **one knob, the buffer pool size**, inside the cover
  **[128 MB, 2,048 MB]** (one chunk, the server's own floor; about an eighth of the machine), moved in whole chunks of 128 MB.
  Everything else, the dataset, the transactions and the server's settings, stays the same.

## The omni rule (frozen on the tuning workload)

- **Reading.** Once a second, the server's own mean statement latency over the last second: the performance schema's statement
  summary (`events_statements_summary_global_by_event_name`, the select, update, insert and delete rows), the timer total and the
  statement count, differenced; a second with no statements reads as calm (0).
- **Band.** From 0 to the **statement line, 0.6 ms** (a statement served from the pool is well inside; one that reads pages from
  the file system is slower). The compass pulls the reading to 40% of the line (0.24 ms), the service profile of the Kubernetes
  adapter, with its usual gains (kp 1.0, response time 2 s, smoothing 0.5, one decision a second). *Written as 1 ms before the
  first smoke run, set at 0.5 ms on the tuning workload's second smoke run and at 0.6 ms on its third, on their figures, before
  any counted run, as the MongoDB preregistration did; the figures are under "What the smoke run shows" below.*
- **Direction, and the do-no-harm gate.** A positive force (slow statements) grows the pool by ceil(force / 0.10) chunks of
  **128 MB**, **only while the pool is full** (pages holding data at 90% of its pages or more): slow statements in a pool with room to
  spare are not the pool's to mend, and the knob is left alone. A negative force (calm) **while the pool's misses are under one
  percent of its read requests in the last second** (the pool holds the working set) gives back one chunk, after a ten-second
  dwell since the last change (a shrink evicts pages, and the server's resize itself takes seconds). *Written as "no page read
  from disk in the last second" and changed on the third smoke run: InnoDB keeps stale pages resident, so a pool once filled
  never reads empty and a few new-page reads a second never stop; the operator's question is whether the pool holds the working
  set, and the miss share answers it.*
- **Cushion.** A force inside ±0.05 moves nothing.
- **Fail up.** At 95% of the line with the pool full, four chunks (512 MB, about a quarter of the cover) are added at once, and
  again the next second if the service is still past the wall; never past the cover.
- **One writer, and the server's own pace.** The pool size is read once before the first write (the operator's 512 MB) and read
  back after every write; the server carries a resize out asynchronously and says so (`Innodb_buffer_pool_resize_status`), and the
  plug waits for it to complete before reading back; a size found at a value Omni did not write, with no resize in progress, stops
  Omni writing (the plug contract).
- **Reset.** At the end of every omni arm the pool is handed back to the operator's 512 MB and read back; the report says whether
  every arm was handed back.

Disclosed: on this machine the data files sit in the operating system's own page cache as well, so a buffer-pool miss is a read
from memory, not a disk read; the gain available to the knob is accordingly smaller than on a machine whose data does not fit in
memory, and the result will say what it is. The MongoDB test on the same kind of machine found exactly this (`docs/YCSB_PREREGISTRATION.md`).

## Gauges (from sysbench's own histogram and summary, the server's own status, the host's `/proc/stat`)

| Gauge | Direction |
|---|---|
| work inside the response line: transactions a second answered within the **transaction line**, the statement line times the statements a transaction as the script ships it (0.6 ms for the point select and the indexed update, 8.4 ms for read-only, 10.8 ms for read-write) | **the aim is higher** (the product number) |
| throughput (transactions a second); queries a second | the aim is higher |
| latency p95, p99, mean (from the histogram) | the aim is lower |
| errors (sysbench's ignored errors: deadlocks and retries) | **any increase is marked** |
| buffer pool held, mean (the knob, the resource); pages holding data, mean | the aim is lower (Omni will hold more under a wide working set, and that reads higher) |
| host CPU busy share, CPU-seconds, CPU-seconds per 1,000 transactions inside the line (the compass's own cost included) | the aim is lower |
| pages read from disk into the pool (misses), pool size changes written | shown, not judged |

Memory held is the resource this benchmark trades; no energy is claimed beyond the host's CPU seconds (evidence class L).

## Workloads

- **Tuning workload:** `oltp_point_select`, the standard steps. The band, the direction rule and its gate, the dwell, the chunk and
  the fail-up above were set on it; nothing else is tuned. It is run and shown, and not counted.
- **Untouched workloads:** **read_only**, **read_write**, **update_index**, **burst** (read-only on the burst steps 1 6 1 8 1 6).

## Runs

Each workload: three paired repetitions in one GitHub Actions job, order alternating, sysbench's own output for every notch, the
audit and the server's error log archived with the code. Three separate runs on the frozen engine (A, B, C); the table
(`tools/sysbench_abc.py`) reads GAIN or LOSS in all three of our runs (judged by what the gauge is for; a resource spent that rose reads power given) when all three runs move the same way with every 95% interval clear of
zero, no difference beyond the noise when a run's interval includes zero, and the runs disagree when clear runs point different
ways. `tests/test_run_sysbench.py` and `tests/test_sysbench_abc.py`, run by `verify.py`, prove the rules without a server.

## What the smoke run shows, said before the counted runs

A one-repetition run of the tuning workload on GitHub's machine exercises the harness end to end before any counted run; its
result is recorded here when it has run, and it is not counted.

- **First smoke run (37745096028, 2026-10-08 07:42 UTC): ran end to end on the first try, and showed the design did not
  reach the pool.** MySQL 8.0.46 from Ubuntu's package, sysbench 1.0.20; both arms answered about 2,930 transactions a second
  inside the line with a mean of 0.18 to 0.22 ms and a p95 of 0.24 to 0.39 ms at every notch; native's pages holding data
  reached 496 MB of its 512 MB only at the top notch and its pages read from disk were 34,524 over the whole arm, 3.8% of its
  900,194 reads; omni, seeing calm and nothing read from disk, gave one chunk back in the first notch (512 to 384 MB) and
  then held, its own misses 31,220, and handed the pool back. The cause is sysbench's shipped request distribution,
  `special`, which sends three quarters of the requests to one percent of the rows, so the hot set stayed in a few dozen
  megabytes whatever the tables in use; a benchmark in which the working set never reaches the operator's pool has nothing
  for the knob to do and would read as a free memory saving, which is not the question. The same fault the YCSB test met
  in its zipfian draw, met here in sysbench's. The one change, made here before any counted run: **rows are drawn
  uniformly over the tables in use** (`--rand-type=uniform`), so the working set is the tables in use; the scripts' operation
  mixes stay as shipped. A second smoke run follows; the statement line is kept or changed here on its figures before
  the counted runs. Nothing in the rules, the gauges or the workloads changed.
- **Second smoke run (37748144365, 08:10 UTC): the working set reached the pool, and the figures set the line.** With the
  uniform draw native's pages holding data reached 493 MB of 512 MB from the second notch on and stayed there, and its pages
  read from disk were 269,370 over the arm, 30% of its reads; omni gave one chunk back in the first notch (512 to 384 MB), held
  there with the pool full for the whole run but one chunk added and given back near the end, and read 349,742 pages from disk.
  The server's mean statement latency, by notch, in native: **0.14 to 0.17 ms** at the low notches once warm (the pool holding
  the working set), **0.20 to 0.22 ms** at the notches whose working set outgrew it (30% misses, each a read from the operating
  system's page cache); p95 0.20 to 0.23 ms when the pool held the working set and 0.47 to 0.50 ms when it did not. Against
  the 1 ms line every reading sat under 0.22 of the band, below the 0.4 center in every notch, so the compass could only ever
  read calm, the same mis-set band the MongoDB test found. **The statement line is set at 0.5 ms**, with the center unchanged
  at 0.4 (0.2 ms): the hit range (0.14 to 0.17 ms) is calm and a full pool missing a third of its reads (0.20 to 0.22 ms) is at
  or past the center and grows. The transaction lines scale with it (0.5 ms a point select or indexed update, 7 ms the
  read-only transaction, 9 ms read-write). The one repetition's whole-arm figures are recorded, not counted: work inside the
  line 2,901 a second in both arms; p95 0.40 ms in both; pool held 512 MB against 408 MB; disk reads 269,370 against 349,742;
  CPU-seconds 172.3 against 171.7; both arms handed back. A third smoke run follows to show the band at work.
- **Third smoke run (37751313605, 08:39 UTC): the band worked one way and not the other, and the figures set the gate.** With
  the 0.5 ms line omni grew the pool as the working set widened, 384 to 640, 768, 896 and 1,024 MB over the first ten notches,
  and read 116,437 pages from disk against native's 268,450 (−57%); work inside the line (2,887 against 2,885 a second), p95
  (0.41 ms in both) and the host's CPU (135.8 against 140.6 s) did not move, because a miss on this machine is a read from
  the page cache. But at the low notches on the way down, where the working set was one or two tables (240 to 480 MB), the
  pool went on growing, to 1,408 MB at a notch whose working set was 240 MB, and ended the run at 1,152 MB: the pool held
  877 MB on average against native's 512. Two causes, both in the rule as written, both fixed here on the tuning workload.
  First, the give-back gate, "no page read from disk in the last second", was never satisfied: InnoDB keeps stale pages
  resident, so a pool once filled reads full forever, and a few new-page reads a second never stop even when the working set
  fits; **the gate is now the pool's miss share, under one percent of its read requests in the last second**, which is the
  operator's own question (does the pool hold the working set?) asked of the server's own counters. Second, this runner's hit
  latency (0.20 to 0.22 ms) sat at the 0.5 ms line's center (0.20 ms), so calm reads drew a small upward force; the second
  smoke's runner read hits at 0.14 to 0.17 ms, and the difference between runners is as large as the difference a notch of
  misses makes (0.05 to 0.06 ms). **The statement line is set at 0.6 ms** (center 0.24 ms), above the hit range seen on both
  runners and under the miss-heavy range of this one (0.25 to 0.27 ms); on a runner like the second smoke's the compass will
  read calm throughout and the miss-share gate will hold the pool at the working set, which is the right answer there. The
  transaction lines scale with it (0.6 ms a point select or indexed update, 8.4 ms read-only, 10.8 ms read-write). The one
  repetition's whole-arm figures are recorded, not counted. A fourth smoke run follows; the counted runs begin on its figures
  if the pool follows the working set both ways. Nothing else in this document changed.
- **Fourth smoke run (37754681298, 09:09 UTC): the pool followed the working set both ways, and the rules stand.** On a
  faster runner than the first three (hits 0.06 to 0.08 ms, miss-heavy notches 0.11 to 0.13 ms, every reading well under the
  0.24 ms center), omni gave the pool back to 256 MB at the first notch, grew it to 896 MB on the cold start of the second
  (the first reads of each table come from the file system before the page cache has them, and those are slow: a fail-up on
  a real stall), gave back to 512 MB as the misses fell under one percent, grew again to 640 and then 1,024 MB as the tables
  in use widened to four, five and six, and gave back chunk by chunk to 256 MB as they narrowed to one, ending where the
  working set was. The one repetition's whole-arm figures, recorded and not counted: work inside the line 2,936 against
  2,945 a second (−0.3%); p95 0.24 against 0.23 ms; pool held 672 against 512 MB (+31%); pages read from disk 189,773 against
  268,721 (−29%); host CPU-seconds 86.3 against 92.1 (−6%); both arms handed back. One figure is the knob's own cost and the
  gauges will carry it: at one notch the mean latency read 0.57 ms against a p95 of 0.26 ms, a heavy tail from the server's
  own stall while it resized the pool; the mean-latency row is where that shows, and it will be judged like every other row.
  Two things are declared on these figures before the counted runs. The hit latency of GitHub's runners ranges from 0.06 to
  0.22 ms across the four smoke runs, so on a fast runner the compass reads calm throughout and the pool is governed by the
  miss-share gate and the fail-up alone; on a slow runner the center also bites; both are the same rule applied to what the
  server reports, and the counted runs will pool them as they come. And the memory the governor holds over a whole run may
  read above native's (it buys pool for the wide notches and gives it back for the narrow ones), which the resource row will
  show as higher if it does; the question the benchmark asks is whether the misses it saves bought any service, and the work,
  p95 and CPU rows answer it. **The counted runs A, B and C begin on these rules, unchanged from here.**

## The first counted set (runs A, B and C of 2026-10-08): the result, a hand-back finding, and the amendment it forces

**The result, every row.** Runs 37757840760, 37757850988 and 37757861572, commit `23f6ca4c`, Omni v3, each run five workloads of
three paired repetitions (`results/live/V3_SYSBENCH.md`). On the four untouched workloads **no gauge-row is GAIN or LOSS in all three of our runs (judged by what the gauge is for; a resource spent that rose reads power given) and none disagrees**: work inside the line, throughput, p95, p99, mean, CPU and the pool held are all inside the
noise in every run or in two of three (the pool held read −45% to −71% on burst, −4% to −36% on read_only, +38% to +84% on
read_write and +7% to +29% on update_index as the runs' point estimates, with at most one run of three clear of zero on any
workload, so none of them is the same in all three of our runs); no error in any arm. The compass moved the pool 3 to 26 times an arm and never met another writer. The tuning workload
read the same. Two readings in that table need the explanation a referee would ask for, and both are given here, not in the
table's favour.

**The hand-back row reads NO on four of the five workloads, and the cause is our plug, not the law.** 15 of the 45 omni arms did
not read the operator's 512 MB back at the end. The audits show why: in 12 of them the server was still carrying out a shrink
the law had asked for (the status `buffer pool 0 : withdrawing blocks. (8173/8191)`: InnoDB withdraws the last blocks of a
shrink only when the pages pinned by the load are released, so under load the withdrawal does not finish), and MySQL ignores a
new `innodb_buffer_pool_size` while a resize is in progress, so the restore the plug issued at that moment was dropped, and 90 s
later the pool still read 128 or 256 MB; in the other 3 the last decision's own write and the restore collided in the same way.
Every following arm began from a fresh server at 512 MB (`fresh_server`), so no native arm and no later omni arm was affected,
and the decision loop itself never wrote during a resize (its writes are gated on the status); only the restore was. The rows
stand as they are: a hand-back that did not read back is a NO, whatever its cause.

**The amendment (a plug fix, declared here before the second set).** `BufferPool.restore` now waits, up to the same 90 s, for
any resize the server is still carrying out (the load has stopped by then, so a stalled withdrawal finishes), then writes the
snapshot, and if the server did not take it, waits once more and writes once more; its receipt (what was in flight when the arm
ended, the seconds waited, the writes, the final read-back) is written into every omni arm's record, and the table reports how
many arms were not handed back and in how many the server was mid-resize. `tests/test_run_sysbench.py` proves the three cases
against the stand-in console (a withdrawal that eases inside the wait; one that eases after the first write is ignored; one that
never eases, which still reads NO). Nothing in the law, the gates, the line, the cover, the chunk, the dwell or the gauges
changes; `tools/omni_version.py` still prints omni-v3. **The second counted set (A2, B2, C2) runs on this plug; its table
replaces the first in `results/live/V3_SYSBENCH.md`, and the first set's table moves to `docs/history` with this note, every
row kept.** Dispatched 2026-10-08 11:31 UTC on commit `a033fd09` (Omni v3 by `tools/omni_version.py --commit`; the plug fix and
this note are in it, nothing in the engine): runs **A2 37770617236, B2 37770620582, C2 37770624805**, the same inputs as the
first set (every workload, three repetitions, 20 s a notch). Nothing above this line changed after the dispatch.

## The second counted set (runs A2, B2 and C2 of 2026-10-08): the result

Runs 37770617236, 37770620582 and 37770624805, commit `a033fd09`, Omni v3 (the same 40 engine files as the first set), five
workloads of three paired repetitions each, on the amended plug (`results/live/V3_SYSBENCH.md`; the first set's table is kept
whole in `docs/history/V3_SYSBENCH_set1.md`). **The pool handed back and read back on all 45 omni arms.** On the four untouched
workloads:

- **burst:** the pool held **−67% in all three runs, GAIN in all three of our runs** (512 → 170 MB), the pages holding data −66%, GAIN in all three of our runs; work inside the line, throughput, p95, p99 and host CPU inside the noise; misses from disk about double (shown);
  three writes an arm.
- **read_only:** the pool held **−50% to −56%, GAIN in all three of our runs** (512 → 258 MB), the pages holding data −50% to −54%,
  GAIN in all three of our runs; work, latency and CPU inside the noise; misses +123% to +142% (shown).
- **read_write:** the compass bought pool for the written working set: the pool held +59% to +79% as point estimates, one run
  clear of zero (no difference beyond the noise in 2 of 3), and **the pages holding data +53% to +70%, power given in all three of our runs**; p95
  −11% to −18% and host CPU −4% to −5% as point estimates, inside the noise in two runs; misses −40% to −47% (shown); work
  inside the line inside the noise.
- **update_index:** every row inside the noise (run A2's omni arm used 78% more host CPU than its native arm, with an
  interval of −59% to +215%; the other two runs read −1%); the "inside the line" row counts almost nothing in either arm, as
  disclosed below.

No error in any arm; no other writer seen. **4 gauge-rows GAIN in all three of our runs, 1 LOSS in all three of our runs, 0 where the runs disagree.**
The category enters the index at +12.2% (the first set had entered at +0.0%), the headline moving from +21.2% to +23.5%.
What the two sets together say: the knob does what the law asks on read-mostly working sets that fit in less pool than the
operator gave (the memory is given back, with no measurable cost in work, latency or CPU on these runners, where the data
files sit in the operating system's page cache as well); on a written working set the compass buys pool, and the rule counts
the memory held as higher whatever the latency did. A referee should read both sets, and the Redis result, as the same
lesson: a memory knob trades memory, and the index charges for it.

**The update_index line, disclosed and left as it is.** The transaction line is the statement line times the statements a
transaction (0.6 ms × 1 for update_index), and it is the server's own statement latency that the compass reads; sysbench's
histogram, which the "work inside the line" gauge is counted from, is client-side and includes the round trip, which for a
single-statement update is about 1.1 ms on these runners. So on update_index almost nothing in either arm counted as inside the
line (1 to 2 transactions a second of about 975) and that row reads no difference by construction; the throughput, latency,
pool and CPU rows of that workload are unaffected and are the rows to read. The rule is kept for the second set so that the two
sets are read on the same line; a line set from the client's own round trip is a change for a later version, declared when made.

## Amendment 2 (2026-10-08, declared before the third counted set): the pool grows only while it is missing

**The question.** The founder asked for every cost in the counted tables to be traced to its mechanism and removed where the
mechanism is ours, with the engine locked (Omni v3; `tools/run_sysbench.py` is a harness outside the engine's fingerprint, and
`tools/omni_version.py` prints omni-v3 before and after this amendment). The one cost in `V3_SYSBENCH.md` is **read_write: the
pages holding data +53% to +70%, power given in all three of our runs** (the pool held +59% to +79% as point estimates), with nothing bought for it
beyond the noise (p95 −11% to −18%, two runs inside the noise).

**The mechanism, read from the second set's own audits** (`results/live/raw/run-37770617236`, `-37770620582`, `-37770624805`,
every omni arm's `audit.jsonl`, 9 arms a workload). The growth rule fired on slow statements with the pool full, and asked no
further question. Where it fired, and the pool's miss share of its read requests at that second:

| Workload | grows in 9 arms | at a miss share under 1% | at 1% to 5% | at 5% or more | pool held, mean |
|---|---:|---:|---:|---:|---:|
| tuning (point select) | 18 | 2 | 7 | 9 | 503 MB |
| read_only | 36 | 3 | 0 | 33 | 245 MB |
| burst | 17 | 1 | 0 | 16 | 169 MB |
| **read_write** | **82** | **36** | 29 | 17 | **876 MB** |
| update_index | 84 | 28 | 56 | 0 | 602 MB |

On the read-mostly workloads the pool grew when it was missing (33 of 36 read_only grows and 16 of 17 burst grows at five
percent or more). On read_write **36 of the 82 grows came with the pool missing under one percent of its reads**: the
statements were slow for a reason the pool cannot mend (a written transaction waits on the redo log and on locks, not on a
page), and the rule bought 128 MB chunks for them anyway, up to 1.4 to 1.7 GB; the same on update_index (28 of 84), whose pool
row read inside the noise. The give-back side already carried the question the growth side lacked: a chunk is given back only
while the pool's misses are under one percent of its reads (the pool holds the working set). One more thing the audits show: in
every one of the 45 omni arms the very first decision, in a second with no read request yet counted, read a miss share of zero
and gave a chunk back before any statement had run; a second with no reads says nothing about the working set.

**The amendment (`decide` in `tools/run_sysbench.py`), two parts, nothing else.**

1. **Growth is gated on missing.** Slow statements with the pool full grow the pool only while **the pool's misses are one
   percent of its read requests or more** in the last second; a full pool that holds its working set (misses under one
   percent) cannot mend a slow statement, and the knob is left alone. One percent is the line the give-back already uses, so
   the rule has one line, used both ways; no new number. The fail-up (95% of the line with the pool full: four chunks at
   once) is unchanged.
2. **No give-back in a second without a read request.** The give-back needs a second that saw read requests; a second with
   none moves nothing.

Unchanged: the reading, the band, the 0.6 ms statement line, the centre, the gains, the cushion, the chunk, the cover, the
dwell, the full gate, the fail-up, the one-writer rule, the plug's restore (amendment 1), the load, the gauges, the workloads,
the three-run rule. `tests/test_run_sysbench.py` holds the new cases (slow with the pool full but holding its working set:
nothing grown; a second with no read request: nothing taken; the two gates share one line).

**What is expected, said before the runs.** The replay above cannot predict the pool's path, because a chunk not bought changes
the misses that follow; it says only which decisions the gate would have refused. On read_write the pages-holding-data row
should move toward native's, and may or may not leave "LOSS in all three of our runs": 46 of its 82 grows came at one percent or more and
stay allowed. If it stays LOSS in all three of our runs, the remaining growth is on real misses, the trade is the knob's, and the table says
so. The read-mostly workloads should read as before (3 of 36 and 1 of 17 grows refused). The tuning workload's two refused grows
are shown and not counted, as always.

**The third counted set (A3, B3, C3)** runs on this rule, the same inputs as the second (every workload, three paired
repetitions, 20 s a notch, three separate dispatches on one commit); its table replaces the second in
`results/live/V3_SYSBENCH.md`, and the second set's table moves to `docs/history` beside the first, every row kept. The index
reads the third set when it lands and says so.

**Dispatched 2026-10-08 23:16 UTC on commit `310cf318`** (Omni v3 by `tools/omni_version.py --commit`; the amended rule and
this text are in it, nothing in the engine): runs **A3 37858501997, B3 37858505059, C3 37858509109**, every workload, three
paired repetitions each, 20 s a notch. Nothing above this line changed after the dispatch.

## The third counted set (runs A3, B3 and C3 of 2026-10-08/09, on amendment 2): the result

Runs 37858501997, 37858505059 and 37858509109, commit `310cf318`, Omni v3, five workloads, three paired repetitions each; the
table by rule is `results/live/V3_SYSBENCH.md`, and the second set's table is kept whole in `docs/history/V3_SYSBENCH_set2.md`
beside the first set's.

- **burst**: the pool held **−49% to −56%** and the pages holding data −52% to −57%, **GAIN in all three of our runs** (the second set read
  −67%); work, latencies and CPU inside the noise.
- **read_only**: every row inside the noise. The pool held read +1%, −25% and +1% as the runs' means, with intervals of ±40
  to ±80 points: the second set's −50% to −56% is not reproduced. The audits say why. In the second set the very first
  decision of every arm gave a chunk back before any read had been counted (the gate read a miss share of zero on zero
  reads), and the pool cascaded to the floor of 128 MB inside the first minute, where it sat at 12% to 15% misses for most of
  the arm, because misses served from the operating system's page cache never made a statement slow enough to grow it. In
  the third set that first give-back is refused; the pool keeps the operator's 512 MB until the first table is in it, gives
  chunks back once misses fall under one percent, and by then the notches of two to six tables have arrived, so the pool is
  bought back on real misses (4 to 12 grows an arm in six of the nine arms). The second set's read_only saving was in part the
  cold-start artefact the MongoDB amendment names, and it is gone with it; what remains is inside the noise.
- **read_write**: the pages holding data **+44% to +52%, power given in all three of our runs** (the second set read +53% to +70%); **host CPU −4% to
  −6%, GAIN in all three of our runs**, new; the pool held +59%, +62% and +63% as means with one run's interval across zero (inside the
  noise by the rule); p95 −13%, −24%, +2% and work inside the noise. The growth gate refused 0 to 6 grows an arm; the grows at
  one to five percent of misses stayed allowed, as the replay above said they would, and the pool still grew to 1.1 to 1.6 GB
  in the wide notches. The row stands as a trade: memory bought on real misses, CPU saved, latency unchanged.
- **update_index**: the pool held **the runs disagree** (+13% in A, −4% and −12% in B and C); everything else inside the noise.
- **tuning**: shown and not counted, as always.
- Every pool handed back and read back in every arm; no error; no controller fault.

**Read.** 4 gauge-rows GAIN in all three of our runs, 1 power given in all three of our runs, 1 where the runs disagree. The category enters the index at
**+5.2%** (the second set's +12.2% included the read_only saving that was in part the artefact). Said in the founder's words:
burst is a yes with no cost (half the memory, no LOSS); read_write is a trade (more memory, less CPU; the index nets it
at about +1%); read_only and update_index show no settled value. The expectation written before the runs held: the read_write
memory row moved toward native and stayed power given in all three of our runs on real misses, and the read-mostly workloads were not meant to
change, but read_only did, for the reason given, and that is the result.

## Amendment 3 (2026-10-09, declared before any run on it): the brain's own verdict on the pool

**Why, and when.** Written after the third counted set was read (the section above: `burst` pool −49% to −56% with no LOSS;
`read_write` pages holding data +44% to +52% power given in all three of our runs with CPU −4% to −6% lower; `read_only` inside the noise; `update_index`
the runs disagree), at the founder's order of 9 October: Omni need not be wired into every muscle; a knob that cannot prove it
pays stays native and Omni only reads it. The brain must decide that on the muscle itself, in real time, by a measurement.

The rule, the same in the five live harnesses (`tools/knob_verdict.py`, a wrapper around the frozen engine's own
verdict, `omnicompass/verdict.py`, which is unchanged: the engine stays Omni v3): **the knob starts in watch**, one wire out
and nothing written, and the compass's moves are clamped to the allowance a paired trial on the stack itself has earned. Two
directions from the operator's setting, each with its own allowance: **spend** (more of the resource) and **give back**
(less). A trial is one notch past the deepest step already allowed: the reference phase holds the knob at that deepest step
(the operator's setting at first) until 8 one-second samples are in, then the trial phase holds it one notch further for 8
more; the first 2 s after any change are not sampled. The judge is the engine's: the trial's median cost no higher
than the reference's within 2%, and no higher than the cost first measured at the operator's setting. The cost is one sample
a second from the stack's own readings: under the **resource objective** (the Omni index's preregistered reading, the
default) cost = the buffer pool held (MB) × the host's CPU busy share × the mean statement latency on the server in the last second / the statements the server counted in the last second, so a step passes only if the service gained
outweighs the resource and CPU spent by the index's own arithmetic; under the **service objective** (`--objective service`)
cost = the mean statement latency on the server in the last second / the statements the server counted in the last second, the resources shown and not judged. A spend step is tried only while the compass asks to spend
and the pool is full and missing at 1% of its read requests or more (amendment 2's condition); a give-back step only while the service is calm and the pool saw read requests and its misses were under 1% of them. A trial once started runs on until its
samples are in unless the service swings to the other direction's condition, when it is abandoned; a refused step is not
tried again for 60 s; a trial is started at most every 20 s. During a trial the knob stands at the phase's value whatever
the compass asks; between trials the compass moves it by its own law inside the allowance. No sample is taken while the server is still carrying out a resize, and a trial may take up to 120 s before it is abandoned, because a chunk takes seconds to add or withdraw. The fail-up (four chunks at the wall) is clamped to the allowance like every other move. Restoring the
operator's setting is always free. Every trial, allowance, refusal and abandonment is written to the audit (`cost`,
`cpu_share`, `verdict_phase`, `verdict_direction`, `allowed_low`, `allowed_high` on every line) and summed in the arm's
record (`verdict`: the objective, the state, the allowance, the counts, the events); the three-run table prints the
brain's verdict per workload and run. The counted runs on this amendment will use 30 s a notch (a whole trial inside one
notch of traffic), declared here; the native arm runs the same ladder. Nothing is typed in; the rule is in the code the
runs execute.

**Expected before the runs.** `burst`: the pool given back a chunk a trial while calm, −25% to −50%, less than the third set's −49%
to −56%, with no LOSS. `read_write`: each chunk above 512 MB must pass its trial under the resource objective (memory × CPU ×
latency / work no higher); a chunk that buys a few percent of CPU for a quarter more memory fails it, so the pages holding data are
expected inside the noise and the CPU saving of the third set with them: no loss, no gain. `read_only` and `update_index`: inside
the noise. The third counted set stays in `docs/history` as the result of the rule before this amendment.

**Dispatched (2026-10-10 01:28 UTC, commit `3aac0ab7`, Omni v3 by `tools/omni_version.py --commit`).** At the founder's order of
10 October that every benchmark be run again on the current code, native and omni, the counted runs on this amendment were
dispatched with `workloads=all`, `reps=3`, `step_s=30`, the resource objective: runs 38013329351 (A), 38013334121 (B) and 38013338730 (C), 01:28:50 to 01:28:59 UTC. The whole day's dispatch, run by run, is
`docs/RERUN_2026-10-10.md`. The expectation above stands as written before the runs; when they land the table is read from them
(`tools/sysbench_abc.py`), the index, the wiring page and the benefit sheet are read again, and the set this one supersedes goes whole to
`docs/history`.

## Amendment 4 (2026-10-10 13:05 UTC, after the first counted set on amendment 3, before the next): a spend trial runs to its samples

The first counted set on the brain's verdict (runs 38013329351, 38013334121, 38013338730; the table `results/live/V3_SYSBENCH.md`) landed at midday on 10 October. What it showed about the trials: the give-back trials were judged (the pool held −10% to −20% on `burst` and `read_only`, GAIN in all three of our runs, read_write and update_index left native or one chunk given back) but the grow trials were mostly abandoned (for example 15 trials, 2 allowed, 0 refused, 13 abandoned on an arm): a chunk added while the pool was missing cut the misses within seconds, the service turned calm, and the trial ended unjudged.

**The cause is ours.** Amendment 3 ended a trial when the service swung to the other direction's condition: a give-back trial when the service left calm (the engine's own rule, kept), and a spend trial when the service turned calm. A spend that works calms the service within seconds, so a spend trial could never reach its samples: every successful spend ended its own trial unjudged. Nothing in the stack and nothing in the engine did this; the engine's verdict ends a trial when the condition it is given ends, and we gave it the wrong condition for spending. Found on the first set, corrected before the second, declared here.

**From this amendment** (`tools/knob_verdict.py`, the harness outside the engine; Omni v3 unchanged): a spend trial, once started, runs to its samples whatever the compass's force; only the wall (a fail-up) or the engine's own time limit on a trial ends it early. A give-back trial still ends when the service leaves calm. The conditions to start a trial, the cost, the judge, the allowance and the recheck are unchanged.

**Expected before the runs:** the grow trials are judged: a chunk is allowed on `read_write` only where the misses it stops lower the latency and raise the work inside the line by more than the memory it costs (the index's arithmetic), otherwise refused; the give-back results stand. The first set's table stands as the result of amendment 3 until the set on this amendment lands and supersedes it; it then goes whole to `docs/history`.

**Dispatched (2026-10-10 13:11 UTC, commit `ca745467`).** Runs 38054765202, 38054768832, 38054773573 (A, B, C), the same inputs as the morning's; recorded run by run in `docs/RERUN_2026-10-10.md`.

---

© 2026 The Omni-Compass LLC. Evaluation and Simulation use only; any other use requires a signed, paid Omni-Compass
Enterprise License. All rights reserved. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## Amendment 5 (2026-10-17, declared before any run on it): native as shipped, beside the operator's pool

The founder's order of 17 October: every native muscle also runs exactly as it is shipped, and Omni-Compass goes beyond it if
it can. A second set runs beside the preregistered one, with every rule of this file unchanged but one: native's buffer pool is
MySQL 8.0's own default, 128 MB (`innodb_buffer_pool_size` unset; `tools/run_sysbench.py --native shipped`, workflow input
`native: shipped`), and omni starts from the same 128 MB. The cover stays [128 MB, 2,048 MB], so omni can only add to native's
pool, never take from it. The operator's set (512 MB) keeps its name and its tables; the shipped set's tables are named for it
(`…_SYSBENCH_SHIPPED.md`). Nothing about the shipped set is tuned: it was written before any run on it, on no data.

## Amendment 6 (2026-10-30, declared before any run on it): the max on the buffer pool, through the server's own account of a miss (the next engine's candidate)

**The cause, from the omni-v21 runs' own files** (`docs/STORE_ROOT_CAUSES_2026-10-30.md`, `tools/store_causes.py`). In 3,139 of
the 3,697 seconds the statements stood over their line in the omni-v21 resource set (runs 40258018856, 40281464587, 40401032384),
the brain's own rule asked for pool and amendment 3's allowance kept it from it: the wall abandoned the spend trials before their
samples were in, and the fail-up itself was clamped to the allowance they never earned, so the pool stood at the operator's 512 MB
at the end of 24 of the 45 arms and at 640 MB in the rest, while the six-table workloads' working set is about 1.3 GB.

**What a miss costs, read from the server itself.** The root-cause page first read the omni-v21 arms across pool sizes (12.4% of
page reads missing at 384 MB, 10.9% at 512 MB, 9.1% at 640 MB, the statement 0.138 to 0.141 ms) as misses that cost the statement
nothing. That reading is withdrawn: one notch of pool moves the miss share about three points, worth about 5% of the statement time,
inside the arms' own spread. The server's own meter is used instead: the performance schema times every read of the data files
(`file_summary_by_event_name`, `wait/io/file/innodb/innodb_data_file`, enabled and timed as MySQL 8.0 ships; checked on 8.0.46),
and the workload's statement timer (the reading since the store fix of 25 October) times the statements; their ratio over the last
10 s is the share of the statements' own time spent reading pages the pool did not hold. On this machine (MySQL 8.0.46, sysbench's
own workloads, six arms of 60 s; a tuning-bench reading, class L, this host, no benchmark result; the table in
`docs/STORE_ROOT_CAUSES_2026-10-30.md`, section 5): at the operator's 512 MB pool, point selects over six tables at 3,000 a second,
137 µs a statement (the rig's 138), 17% of page reads missing, a data file read 70 µs while the host was still writing out the
dataset it had just prepared (as the rig's arms run), the misses 32% of the statements' time (quartiles 24% and 37%); read-only
transactions at 300 a second, 95 µs a statement, 11% missing (the rig's 10.9%), a file read 14 µs, the misses 12% (quartiles 8% and
19%); point selects over three tables, 9% missing, a read 9 µs, the misses 2.8%; at MySQL's shipped 128 MB pool, 15% to 23% missing,
a read 5 to 7 µs, the misses 5.7% to 7.3%. In every arm the misses are above the key's floor, 3% to 32% of what a statement waits
for, and only the pool can cut them; the account is read live on the machine the brain runs on.

**From this amendment** (`tools/run_sysbench.py` `Brain`, `tools/store_brain.py`; the store wires were written on 9 and 10 October,
before the founder's order of 12 October that the max is the default brain, and never brought to it; this brings the pool's wire to it):

- the spend: slow statements with the pool full and missing (amendment 2's rule) grow the pool by the compass's own law (ceil(force /
  0.1) chunks of 128 MB a second; at the wall four chunks at once), never clamped by an allowance, up to the cover's top (2,048 MB),
  where the server's own account says the misses are at least the one key's floor (a half of one percent, `tools/readings.py`
  `SIZE_FLOOR`) of the statements' time over the last 10 s and the host keeps 5% of its memory available after the chunk
  (`/proc/meminfo`, the compass's cushion); the memory is power given, shown beside the misses it bought off;
- the hold: where the misses are under the floor the pool holds and the audit says why (memory would buy nothing the key could
  read); where the server's account or the host's memory is unread this second, nothing is known and nothing is taken;
- the hand-back: calm with the misses under 1% (amendment 2) gives one chunk back after the dwell, never below the most the pool's
  data pages occupied in the last 60 s (with the fullness margin, rounded up to a chunk) and never below the operator's 512 MB; the
  operator's pool handed back at the end as before;
- the record: every second's data file reads and their time, the misses' share of the statements' time, the floor and the host's
  room in the audit; the arm's record carries the max's counts (spends, holds by their reason, hand-backs) where it carried the
  verdict's allowance; every workload record carries its `dial`;
- the tune-down (`OMNI_DIAL=save`): omni-v21's loop unchanged, the verdict under the resource objective, where giving memory
  back is the aim;
- the fingerprint: `tools/store_brain.py` and `tools/knob_verdict.py` join it with this version (`tools/omni_version.py`,
  `STORE_WIRES`), so no rule of the store wires changes without the version changing.

**The model gate** (`tools/store_gate.py`, class S: the omni-v21 arms' recorded seconds replayed open-loop through the candidate).
omni-v21's audits carry neither the data files' timer nor the host's memory, so the candidate holds at the operator's pool in every
replayed arm: seconds below native 97.9 → 0 an arm (shown), seconds below native while missing 65.4 → 0 (GAIN +100.0%), the knob's
moves 7.5 → 0 (GAIN +100.0%), the pool held 480 → 512 MB (+6.7%, power given); no LOSS. The replay cannot show what the pool buys:
the first runs on the next engine read the server's account for real, and a closed-loop model of the pool, set from their files,
follows before any further change to the rule.

**Expected before the runs**, at the counted 30 s a notch, three paired repetitions a run: in the six-table notches the pool rising
toward the working set (power given) and the misses falling with it; the statement latency and the work inside the line GAIN or
EVEN; the knob's moves shown; no second below the operator's pool. A LOSS row is a fault to fix, never a number to accept. The
counted runs on this amendment run on the next engine version, which lands only when the model gate reads no LOSS for every store
wire it changes.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
