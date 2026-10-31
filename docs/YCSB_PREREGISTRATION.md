# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size, preregistered

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written 2026-10-08, before any counted run. The rules below are set on the tuning workload (run on one machine, never counted)
and are then applied unchanged to the untouched workloads; every row is reported, losses included; the readings are the three-run
readings of `docs/OMNI_V1.md`. The runner is `tools/run_ycsb.py`, the workflow `.github/workflows/ycsb.yml`, the three-run table
`tools/ycsb_abc.py`. This is register row 24 (databases and caches at large), the first of its three stores.

## Why this benchmark

A database's storage engine keeps a cache of the pages it works on, and an operator sizes that cache once, at installation, for
the machine it had and the working set it expected. The working set moves: a report widens it, a quiet hour narrows it. Too small
a cache reads pages from the file system on every touch; too large a cache holds memory the machine's other tenants could use. The
fixed cache size is the native controller here, and Omni-Compass sits on top of it with YCSB, the published cloud-serving
benchmark, asking the questions.

## What is someone else's

- **MongoDB** (MongoDB, Inc.; the 8.0 series as its publisher distributes it for Ubuntu, installed from the publisher's own
  repository signed by the publisher's key), one server on the machine, its configuration as shipped but for the one setting an
  operator sets for the storage engine: the WiredTiger cache, **512 MB** (`storage.wiredTiger.engineConfig.cacheSizeGB`). The
  version the runner installs is recorded in every result.
- **YCSB 0.17.0, the MongoDB binding** (the Yahoo! Cloud Serving Benchmark, Apache License 2.0), fetched from the project's
  GitHub release and checked against the SHA-256 recorded here before any run:
  `6a054a706812269c80bfc6ed1e83457990c1c60b01f5083c873aaed05577e30d`. Its core workloads are run as the project ships them
  (record size, field counts, read and update mixes, the zipfian request distribution); only the key space, the rate, the thread
  count and the measurement type are set from the command line.
- **The machine:** a GitHub Actions runner (4 cores, 16 GB): the server and YCSB share it. There is no watt-meter on it.

Nothing here models a database. Omni-Compass writes one setting through the server's own console (`setParameter
wiredTigerEngineRuntimeConfig cache_size`) and reads what the server itself reports (`serverStatus`: the cache configured, the bytes
in it, the pages read into it, and its own operation latencies) and what YCSB itself records.

## The load

For each workload the dataset is loaded once (YCSB's own `load`, 1 KB records, as many as the highest notch needs), and both
arms read the same records. Before every arm the server is restarted at the operator's configured cache and the operating
system's page cache is dropped, so both arms start cold alike. The **key space** then steps one notch at a time, **1 2 3 2 3 4 5 6 5
4 3 2 1 2 1**, 20 s a notch (the burst workload steps **1 6 1 8 1 6**): notch n lets YCSB range over the first n × 250,000
records, **drawn uniformly**, about 275 MB in the cache at notch 1 and 1.6 GB at notch 6, so the working set is the key space and
fits the operator's cache at the low notches and outgrows it at the high ones (the workloads' read, update and read-modify-write
mixes stay as YCSB ships them; the request distribution is the one setting changed, for the reason the smoke run gave below). YCSB
offers **3,000 operations a second from 32 threads** at every notch, the same in both arms, and records every operation's latency
(`measurementtype=raw`).

## Arms

- **native:** MongoDB at the operator's cache, 512 MB, for the whole run.
- **omni:** the same, with the compass law (`omnicompass/compass_law.py`) on **one knob, the cache size**, inside the cover
  **[256 MB, 2,048 MB]** (the server's own floor; a quarter of the machine). Everything else, the dataset, the operations and the
  server's settings, stays the same.

## The omni rule (frozen on the tuning workload)

- **Reading.** Once a second, the server's own mean read latency over the last second: `serverStatus().opLatencies.reads`, the
  latency total and the operation count, differenced; a second with no reads reads as calm (0).
- **Band.** From 0 to the response line, **1 ms** (a read served from the cache is well inside; a read that misses the cache
  and comes from the file system is slower). The compass pulls the reading to 40% of the line (0.4 ms), the service profile of
  the Kubernetes adapter, with its usual gains (kp 1.0, response time 2 s, smoothing 0.5, one decision a second). *Set at 1 ms on
  the tuning workload's fourth smoke run, from the 2 ms first written; the figures that set it are under "What the smoke run
  shows" below.*
- **Direction, and the do-no-harm gate.** A positive force (slow reads) grows the cache by ceil(force / 0.10) notches of
  **64 MB**, **only while the cache is full** (bytes in the cache at 90% of its size or more): slow reads in a cache with room to
  spare are not the cache's to mend, and the knob is left alone. A negative force (calm) with **no page evicted in the last second**
  gives back one notch of 64 MB a second, after a five-second dwell since the last growth.
- **Cushion.** A force inside ±0.05 moves nothing.
- **Fail up.** At 95% of the line with the cache full, a quarter of the cover (448 MB) is added at once, and again the next
  second if the service is still past the wall; never past the cover.
- **One writer.** The cache size is read once before the first write (the operator's 512 MB) and read back after every write; a
  size found at a value Omni did not write stops Omni writing (the plug contract).
- **Reset.** At the end of every omni arm the cache size is handed back to the operator's 512 MB and read back; the report says
  whether every arm was handed back.

Disclosed: on this machine the data files sit in the operating system's own page cache as well, so a WiredTiger cache miss is a
read from memory and a decompression, not a disk read; the gain available to the knob is accordingly smaller than on a machine
whose data does not fit in memory, and the result will say what it is.

## Gauges (from YCSB's own records, the server's own serverStatus, the host's `/proc/stat`)

| Gauge | Direction |
|---|---|
| work inside the response line: operations a second answered within 1 ms (YCSB's own client-side latency) | **the aim is higher** (the product number) |
| throughput (operations a second) | the aim is higher |
| latency p95, p99, mean | the aim is lower |
| failed operations (YCSB's own count) | **any increase is marked** |
| cache size held, mean (the knob, the resource); bytes in the cache, mean | the aim is lower (Omni will hold more under a wide working set, and that reads higher) |
| host CPU busy share, CPU-seconds, CPU-seconds per 1,000 operations inside the line (the compass's own cost included) | the aim is lower |
| pages read into the cache (misses), cache size changes written | shown, not judged |

Memory held is the resource this benchmark trades; no energy is claimed beyond the host's CPU seconds (evidence class L).

## Workloads

- **Tuning workload:** YCSB workload A (50% reads, 50% updates, zipfian), base 250,000 records, the standard steps. The band,
  the direction rule and its gate, the dwell, the notch and the fail-up above were set on it; nothing else is tuned. It is run
  and shown, and not counted.
- **Untouched workloads:** **b** (workload B, 95% reads), **c** (workload C, 100% reads), **f** (workload F, read-modify-write),
  **burst** (workload B on the burst steps 1 6 1 8 1 6).

## Runs

Each workload: three paired repetitions in one GitHub Actions job, order alternating, YCSB's per-operation records, the audit
and the server log archived with the code (raw files over 20 MB are left out of the artifact; their gauges are in the arm's
record). Three separate runs on the frozen engine (A, B, C); the table (`tools/ycsb_abc.py`) reads GAIN or LOSS in all three of our runs (judged by what the gauge is for; a resource spent that rose reads power given)
when all three runs move the same way with every 95% interval clear of zero, no difference beyond the noise when a run's interval
includes zero, and the runs disagree when clear runs point different ways. `tests/test_run_ycsb.py` and `tests/test_ycsb_abc.py`,
run by `verify.py`, prove the rules without a server.

## What the smoke run shows, said before the counted runs

A one-repetition run of the tuning workload on GitHub's machine exercises the harness end to end before any counted run; its
result is recorded here when it has run, and it is not counted.

- **First smoke run (37718548245, 2026-10-08 02:35 UTC): failed before any arm ran**, on two harness faults, both fixed
  before the second smoke: YCSB was given a relative path for its raw measurements while it runs from its own directory, so
  the load phase could not open the file (the path is now absolute); and the server's log was copied into the artifact as a
  root-owned file the upload step could not read. MongoDB 8.0.32 installed from its publisher's repository and YCSB's
  checksum matched. Nothing in the rules, the gauges or the workloads changed.
- **Second smoke run (37720412929, 03:00 UTC): ran end to end, and showed the design did not touch the cache.** With YCSB's
  shipped zipfian distribution (constant 0.99) the hot set stayed in a few megabytes whatever the notch's key space: at the
  top notch of 1.5 million records the cache held **36 MB** of its 512 MB, 1,300 pages were read into it over the whole arm,
  both arms answered 2,890 operations a second inside the line with p95 0.20 ms, and omni, seeing calm and nothing evicted,
  gave memory back to 258 MB with no cost and nothing to mend. A benchmark in which the working set never reaches the
  operator's cache has nothing for the knob to do and would read as a free memory saving, which is not the question. The
  one change, made here before any counted run: **the requests are drawn uniformly over the notch's key space**, so the
  working set is the key space (`requestdistribution=uniform`); the workloads' operation mixes stay as shipped. The runner
  also prints each notch's mean, p95 and cache figures, so the third smoke shows where the line should sit; if the tuning
  workload shows the 2 ms line or the 0.4 center to be wrong for this stack, the change is written here before the
  counted runs, with the figures that led to it. The host's CPU-seconds in this smoke read 239 s native against 188 s
  omni on one repetition, a difference the counted runs will judge.
- **Third smoke run (37723201831, 03:32 UTC): ran end to end with the uniform draw, and the cache still held 38 MB at the top
  notch with 1,300 pages read in the whole arm, every operation inside the line at a mean of 0.09 ms.** The per-notch figures
  showed why: the dataset was loaded with ordered keys (`insertorder=ordered`) but the run phase used YCSB's default, hashed
  keys, so the reads asked for records that were not there and were answered from the index alone, which fits in a few
  megabytes. The run phase now names ordered keys too, so every read is of a record that exists. The fault is the harness's,
  found and fixed before any counted run; nothing in the rules, the gauges or the workloads changed. A fourth smoke run
  follows, and the line and center are kept or changed here on its figures before the counted runs.
- **Fourth smoke run (37725541273, 04:02 UTC): the working set reached the cache, and the figures set the line.** Native held
  336 to 481 MB of its 512 MB cache across the notches and read 452,928 pages into it over the arm; omni's cache held 251 to
  350 MB. The server's mean read latency, by notch, in native: **0.15 to 0.24 ms** while the cache held the working set (the
  low notches on the way down, warm), **0.23 to 0.33 ms** while it did not (the first pass up, cold, and notches 4 to 6);
  p95 never above 0.42 ms; 99.3% to 99.9% of operations inside 2 ms in every notch of both arms. Against the 2 ms line
  these readings sit between 0.08 and 0.23 of the band, under the 0.4 center in every notch, so the compass could only ever
  read calm: the cache could shrink, under the eviction gate, and could grow only through a single second's spike (it grew
  one notch, at the top notch). That is a mis-set band, the same fault as a Kubernetes line set at ten times the service's
  normal response. **The line is set at 1 ms**, with the center unchanged at 0.4 (0.4 ms): native's hit range (0.15 to 0.24
  ms) is calm, and a full cache reading past 0.4 ms (omni's top notch read 0.457 ms at 350 MB in a 384 MB cache) is slow and
  grows. The work-inside-the-line gauge uses the same 1 ms line (p95 was 0.21 to 0.42 ms, so most operations remain inside
  it in both arms; the gauge is now more discriminating). The one repetition's whole-arm figures are recorded, not counted:
  work inside 2 ms 2,860/s native against 2,805/s omni (−1.9%); p95 0.34 ms in both; cache held 512 MB against 353 MB
  (−31%); pages read in 452,928 against 597,707 (+32%); host CPU-seconds 251 against 272 (+8%); both arms handed back. The
  shape to expect on this machine is therefore memory given back at a cost in misses that the page cache makes cheap, as
  disclosed above; the counted runs judge whether the work inside the line and the CPU pay for it. This is the last change
  before the counted runs; everything else in this document stands as written. The ordered-keys fix of the third smoke
  worked: the dataset is now what the run reads.

## The result (2026-10-08, runs 37727968670, 37727976107, 37727983746, on the rules above unchanged after the fourth smoke)

`results/live/V3_YCSB.md` (`tools/ycsb_abc.py`), all three runs at commit `7ee471b4` on Omni v3, three paired repetitions a
run. On the four untouched workloads: the **cache size held** fell by about half on c (512 to about 259 MB, −49% in every
run) and on burst (−41% to −49%), and by 13% to 37% on f, **GAIN in all three of our runs**; on b it fell 27% to 50% but run A's interval
included zero, so the row reads **no difference beyond the noise (1 of 3 runs)**, and that is the result there. **Work
inside the 1 ms line, p95 and p99 read inside the noise on all four** (work between −2.7% and +1.1%, every interval over
zero); **no operation failed** in any arm; **host CPU-seconds inside the noise on all four** (c read +12% to +15% with every
interval over zero); pages read into the cache rose 14% to 58% (shown, not judged: the misses the smaller cache costs); and
the **mean latency on burst read +2.2% to +3.7% in all three runs, clear of zero: LOSS in all three of our runs**, the one loss, which
stands. Every cache size was handed back to the operator's 512 MB and read back in every arm of every run. 6 gauge-rows
GAIN in all three of our runs, 1 power given in all three of our runs, 0 where the runs disagree. The tuning workload, shown and not counted, read the same
way (the cache 12% to 15% smaller, the same in all three of our runs; everything else inside the noise).

What the result means, within the disclosure made above before any run: on this machine the data files sit in the
operating system's page cache as well, so a storage-engine miss is a memory read and a decompression, and the governor
could give half the cache back at no measurable cost in work or tail latency and a few percent of mean latency. That is the
answer to the question this benchmark can ask on a 16 GB runner whose dataset is 1.6 GB. The harder question, the same
knob on a machine whose data does not fit in memory, where a miss is a disk read, is not answered here and is not claimed.
In the Omni index the category enters as the work, p95, cache size and CPU-seconds columns by rule (`tools/omni_index.py`):
the cache given back is its gain, and the mean-latency loss, not an index column, is in the table where it belongs.

## Amendment 1 (2026-10-08, declared before the second counted set): the give-back asks whether the cache holds its working set

**The question.** The founder asked for every cost in the counted tables to be traced to its mechanism and removed where the
mechanism is ours, with the engine locked (Omni v3; `tools/run_ycsb.py` is a harness outside the engine's fingerprint, and
`tools/omni_version.py` prints omni-v3 before and after this amendment). The one cost in `V3_YCSB.md` is **burst: the mean
latency +2.2% to +3.7%, LOSS in all three of our runs**.

**The mechanism, read from the counted runs' own audits** (`results/live/raw/run-37727968670`, `-37727976107`, `-37727983746`,
every omni arm's `audit.jsonl`). The give-back rule was "calm, and no page evicted in the last second". A cache that is
still filling evicts nothing, so the rule was satisfied by every cold cache from its first second. In **all 9 burst arms** the
compass gave back four notches in the first five seconds of the arm, with the cache 0% to 69% used, and the first eviction
came one second after the last give-back, when the cache had already been taken from 512 MB to its floor of 256 MB; it then
sat at the floor, evicting, for 115 to 118 of the arm's 124 decisions, and the rule never gave anything else back (one arm gave
back a fifth notch at 57 s). **All 9 c arms** read the same way (four notches by the fifth second, the first eviction a
second later, 301 to 303 of 306 to 309 decisions evicting at the floor), and 6 of the 9 b arms; on f and the tuning workload
the cache was taken down one to four notches over minutes. So the memory the table credits on b, c and burst was not a
working set measured and found small: it was a cold cache shrunk before its working set had arrived, held at the floor by
the evictions that followed. On c (reads only, every record in the operating system's page cache) that cost nothing the
table could see; on burst it cost +2% to +4% of mean latency, which is the row that stands. The reading that would have
said so was already in the harness: the arm records carry "pages read into the cache" (the misses), and WiredTiger reports the
pages requested from the cache beside them.

**The amendment (`decide` and `cache_stats` in `tools/run_ycsb.py`), three parts, nothing else.**

1. **The give-back gate is the miss share.** A notch is given back only while **the cache's misses (pages read into it) are
   under one percent of the pages requested from it in the last second**: the cache holds its working set. This is the MySQL
   test's gate, adopted there on its third smoke run for the same reason (`docs/MYSQL_PREREGISTRATION.md`: a store keeps stale
   pages resident, so neither "pages free" nor "nothing evicted" says whether it holds its working set, and the miss share
   does); one line for both stores. A cold cache misses on nearly every request, so it is not given back while it fills.
2. **Growth is gated on missing** the same way: slow reads with the cache full grow it only while the misses are one percent
   or more; a full cache that holds its working set cannot mend a slow read. The fail-up is unchanged.
3. **No give-back in a second without a request** (a second with no page requested says nothing about the working set).

Unchanged: the reading (the server's own mean read latency), the band, the 1 ms line, the centre, the gains, the cushion, the
notch, the cover, the dwell, the full gate, the fail-up, the one-writer rule, the hand-back, the load (uniform over the notch's
key space, ordered keys), the gauges, the workloads, the three-run rule. `tests/test_run_ycsb.py` holds the new cases (misses
under one percent: a notch given back, full or not; one percent or more: nothing taken; no request: nothing taken; slow with
the cache full but holding its working set: nothing grown).

**What is expected, said before the runs, and it is not flattering.** The cache given back on b, c and burst should fall, and
may fall to nothing beyond the noise, because the saving the first set showed was the cold-start artefact and not a working set
found small; where the working set at the light notches (one notch, about 250 MB of records plus indexes) does fit under the
operator's 512 MB with room, the cache should ease toward it and stop when misses pass one percent. The burst mean-latency row
should return to the noise, because the cache is no longer held under its working set. If the memory rows are no longer
the same in all three of our runs, that is the result, and the index reads it: a knob that cannot give memory back without a cost in service stays
at native, which is the rule this program runs under.

**The second counted set (A2, B2, C2)** runs on this rule, the same inputs as the first (every workload, three paired
repetitions, 20 s a notch, three separate dispatches on one commit); its table replaces the first in `results/live/V3_YCSB.md`,
and the first set's table moves to `docs/history` with this note, every row kept. The index reads the second set when it lands
and says so.

**Dispatched 2026-10-08 23:16 UTC on commit `310cf318`** (Omni v3 by `tools/omni_version.py --commit`; the amended rule and
this text are in it, nothing in the engine): runs **A2 37858512907, B2 37858515717, C2 37858519010**, every workload, three
paired repetitions each, 20 s a notch. The harness refuses to run if the server does not report the pages requested from its
cache, so a server that lacked the figure would stop the run rather than run native in Omni's name. Nothing above this line
changed after the dispatch.

## The second counted set (runs A2, B2 and C2 of 2026-10-08/09, on amendment 1): the result

Runs 37858512907, 37858515717 and 37858519010, commit `310cf318`, Omni v3, five workloads, three paired repetitions each; the
table by rule is `results/live/V3_YCSB.md`, and the first set's table is kept whole in `docs/history/V3_YCSB_set1.md`.

**The cache given back is smaller, and it is real.** Cache size held: **b −28% to −36%, burst −21% to −26%, c −24% in all three
runs, f −28% to −36%, all GAIN in all three of our runs**, and the bytes in the cache the same. The cache settled between 330 and 405 MB,
where the gate found the working set, instead of the first set's floor of 256 MB; the knob moved two or three times an arm
instead of four or five. **The cost is gone:** the mean latency reads inside the noise on all four workloads (burst +1.4%,
+1.1%, −8.2%, where the first set read +2% to +4% LOSS in all three of our runs; c +2.3%, +2.3%, +1.1% with one run across zero); work
inside the 1 ms line, p95, p99 and host CPU inside the noise on all four; no operation failed; pages read into the cache
+12% to +44% (shown, not judged: the misses a smaller cache costs, served from the page cache); every cache handed back and
read back. **8 gauge-rows GAIN in all three of our runs, 0 power given in all three of our runs, 0 where the runs disagree.** The tuning workload, shown and
not counted, read the same way (the cache −20% to −24%, the same in all three of our runs; everything else inside the noise).

**Read.** The expectation written before the runs, that the memory rows might fall to the noise, did not come true: a quarter
to a third of the cache is given back without a measurable cost, where the first set gave half back with one. The category
enters the index at **+8.5%** (the first set's +10.2% included the floor-pinned artefact). Said in the founder's words: a yes
on all four workloads, no cost. The disclosure made before the first run still bounds the claim: on this machine a miss is a
memory read, and the same knob on a disk-bound store is not answered here.

## Amendment 2 (2026-10-09, declared before any run on it): the brain's own verdict on the cache

**Why, and when.** Written after the second counted set was read (the section above: the cache −21% to −36% on all four workloads,
no LOSS), at the founder's order of 9 October: Omni need not be wired into every muscle; a knob that cannot prove it pays
stays native and Omni only reads it. The brain must decide that on the muscle itself, in real time, by a measurement, and the
same rule must stand on every live knob, the ones that win included.

The rule, the same in the five live harnesses (`tools/knob_verdict.py`, a wrapper around the frozen engine's own
verdict, `omnicompass/verdict.py`, which is unchanged: the engine stays Omni v3): **the knob starts in watch**, one wire out
and nothing written, and the compass's moves are clamped to the allowance a paired trial on the stack itself has earned. Two
directions from the operator's setting, each with its own allowance: **spend** (more of the resource) and **give back**
(less). A trial is one notch past the deepest step already allowed: the reference phase holds the knob at that deepest step
(the operator's setting at first) until 8 one-second samples are in, then the trial phase holds it one notch further for 8
more; the first 2 s after any change are not sampled. The judge is the engine's: the trial's median cost no higher
than the reference's within 2%, and no higher than the cost first measured at the operator's setting. The cost is one sample
a second from the stack's own readings: under the **resource objective** (the Omni index's preregistered reading, the
default) cost = the cache size held (MB) × the host's CPU busy share × the mean read latency on the server in the last second / the reads the server counted in the last second, so a step passes only if the service gained
outweighs the resource and CPU spent by the index's own arithmetic; under the **service objective** (`--objective service`)
cost = the mean read latency on the server in the last second / the reads the server counted in the last second, the resources shown and not judged. A spend step is tried only while the compass asks to spend
and the cache is full and missing at 1% of its requests or more (amendment 1's condition); a give-back step only while the service is calm and pages were requested and the misses were under 1% of them. A trial once started runs on until its
samples are in unless the service swings to the other direction's condition, when it is abandoned; a refused step is not
tried again for 60 s; a trial is started at most every 20 s. During a trial the knob stands at the phase's value whatever
the compass asks; between trials the compass moves it by its own law inside the allowance. The fail-up (a quarter of the cover at the wall) is clamped to the allowance like every other move. Restoring the
operator's setting is always free. Every trial, allowance, refusal and abandonment is written to the audit (`cost`,
`cpu_share`, `verdict_phase`, `verdict_direction`, `allowed_low`, `allowed_high` on every line) and summed in the arm's
record (`verdict`: the objective, the state, the allowance, the counts, the events); the three-run table prints the
brain's verdict per workload and run. The counted runs on this amendment will use 30 s a notch (a whole trial inside one
notch of traffic), declared here; the native arm runs the same ladder. Nothing is typed in; the rule is in the code the
runs execute.

**Expected before the runs.** The cache given back one notch a trial while calm and holding its working set: −10% to −25% on the four
workloads, less than the second set's −21% to −36% because each notch now waits for its trial; work, p95, mean latency and CPU inside
the noise; no failed operation. The second counted set stays in `docs/history` as the result of the rule before this amendment.

**Dispatched (2026-10-10 01:29 UTC, commit `3aac0ab7`, Omni v3 by `tools/omni_version.py --commit`).** At the founder's order of
10 October that every benchmark be run again on the current code, native and omni, the counted runs on this amendment were
dispatched with `workloads=all`, `reps=3`, `step_s=30`, the resource objective: runs 38013343689 (A), 38013348512 (B) and 38013353044 (C), 01:29:03 to 01:29:13 UTC. The whole day's dispatch, run by run, is
`docs/RERUN_2026-10-10.md`. The expectation above stands as written before the runs; when they land the table is read from them
(`tools/ycsb_abc.py`), the index, the wiring page and the benefit sheet are read again, and the set this one supersedes goes whole to
`docs/history`.

## Amendment 3 (2026-10-10 13:05 UTC, after the first counted set on amendment 2, before the next): a spend trial runs to its samples

The first counted set on the brain's verdict (runs 38013343689, 38013348512, 38013353044; the table `results/live/V3_YCSB.md`) landed at midday on 10 October. What it showed about the trials: the trials were judged on this stack (2 or 3 trials an arm, 1 or 2 allowed, 0 or 1 refused, at most 1 abandoned) and the cache size held fell 3% to 13% on `workloadb` and `burst`, GAIN in all three of our runs, with every other gauge inside the noise.

**The cause is ours.** Amendment 2 ended a trial when the service swung to the other direction's condition: a give-back trial when the service left calm (the engine's own rule, kept), and a spend trial when the service turned calm. A spend that works calms the service within seconds, so a spend trial could never reach its samples: every successful spend ended its own trial unjudged. Nothing in the stack and nothing in the engine did this; the engine's verdict ends a trial when the condition it is given ends, and we gave it the wrong condition for spending. Found on the first set, corrected before the second, declared here.

**From this amendment** (`tools/knob_verdict.py`, the harness outside the engine; Omni v3 unchanged): a spend trial, once started, runs to its samples whatever the compass's force; only the wall (a fail-up) or the engine's own time limit on a trial ends it early. A give-back trial still ends when the service leaves calm. The conditions to start a trial, the cost, the judge, the allowance and the recheck are unchanged.

**Expected before the runs:** little change: the trials were already judged here; a grow trial started by misses now runs to its samples. The first set's table stands as the result of amendment 2 until the set on this amendment lands and supersedes it; it then goes whole to `docs/history`.

**Dispatched (2026-10-10 13:11 UTC, commit `ca745467`).** Runs 38054777807, 38054782696, 38054787517 (A, B, C), the same inputs as the morning's; recorded run by run in `docs/RERUN_2026-10-10.md`.

---

© 2026 The Omni-Compass LLC. Evaluation and Simulation use only; any other use requires a signed, paid Omni-Compass
Enterprise License. All rights reserved. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## Amendment 4 (2026-10-17, declared before any run on it): native as shipped, beside the operator's cache

The founder's order of 17 October: every native muscle also runs exactly as it is shipped. A second set runs beside the
preregistered one with every rule unchanged but native's cache: MongoDB exactly as shipped, its WiredTiger cache at the server's
own default (half of the machine's memory less 1 GB, at least 256 MB: about 7.5 GB on GitHub's 16 GB machines;
`tools/run_ycsb.py --native shipped`, workflow input `native: shipped`). That is above the cover's top (2,048 MB): the knob is at
its limit on native, and any size Omni-Compass wrote would sit below native, which the max never does. So in the shipped set
omni reads the server, writes nothing and says so in its audit, and every row reads STEADY; that is the result, said before the
run. The record carries native's size as the server reported it. The preregistered set keeps its name; the shipped set's tables
are named for it (`…_YCSB_SHIPPED.md`).

## Amendment 5 (2026-10-21, declared before any run on it): the machine's operating system, Linux 6.8

**What happened.** All three omni-v12 runs of the preregistered set (39379934444, 39410606870, 39461506751, 20 October) failed
partway, so their table (`results/live/V12_YCSB.md`) holds no workload in all three runs and judges nothing. Every failed job
(9 of 15) ran on GitHub's ubuntu-24.04 image of 18 October (20261018.339.1), whose kernel is Linux 7.0.0-1017-azure; every job
that passed, in these runs and in the omni-v11 runs before them, ran on the image of 12 October (20261012.334.1, Linux 6.17).
MongoDB 8.0 (8.0.34, the series this preregistration names) refuses or fails to start on Linux 6.19 to 7.0.13 (MongoDB's own
issue SERVER-121912: the TCMalloc bundled with the server and the kernel's restartable sequences); on the new image the server
died before its first log line (`mongod.log` empty in all nine), the setup's wait ended without saying so, and the workload
stopped at its first restart ("mongod did not come back after the restart"). The cause is the test machine, not the engine
and not the rule.

**From this amendment** (`.github/workflows/ycsb.yml`, `tools/run_ycsb.py`): the workload jobs run on GitHub's ubuntu-22.04
machine (Linux 6.8; the same 4 cores and 16 GB), MongoDB 8.0 from its publisher's repository for that release, signed by the
publisher's key. The setup stops the job at once, with the kernel, the server's status and its journal, when the server does not
answer, and the runner refuses to run a workload on a server whose version it cannot read; every run's files carry the kernel,
the release and the runner image (`machine.txt`) and the server's journal (`mongod-journal.log`). Nothing else changes: the
engine, the rule, the gauges, the workloads, the steps, native's setting.

**The runs.** Every set of this preregistration runs on this machine from this amendment, beginning with the omni-v13 campaign
(`scripts/reruns.txt`, A, B and C of each). The three failed omni-v12 runs stay as they are, listed in their table; omni-v11's
table (`results/live/V11_YCSB.md`) stands as MongoDB's result, named as omni-v11's, until three runs on a newer engine land whole
(`tools/readings.py`, `landed`). The shipped and the service sets' omni-v12 tables, whose runs all ran on the earlier image,
stand as they are.

## Amendment 6 (2026-10-30, declared before any run on it): the max on the cache, through the server's own account of a miss (the next engine's candidate)

**The cause, from the omni-v21 runs' own files** (`docs/STORE_ROOT_CAUSES_2026-10-30.md`, `tools/store_causes.py`). MongoDB stood
over its line in 32 seconds of the omni-v21 resource set and amendment 2's allowance refused the brain's own rule in 21 of them;
the cache stood at the operator's 512 MB or one notch above it. The runs across cache sizes (15.8% of pages missing at 512 MB in
workload b; 12.6%, 12.1% and 11.7% at 512, 576 and 640 MB in the tuning workload, the read 0.073 to 0.082 ms) were first read as
misses that cost the read nothing; that reading is withdrawn, as on MySQL (a notch moves the miss share half a point, nothing the
arms' spread could show). The server's own meter is used instead.

**From this amendment** (`tools/run_ycsb.py` `Brain`, `tools/store_brain.py`):

- the account of a miss: WiredTiger counts and times the pages its application threads read from disk
  (`serverStatus().wiredTiger.cache`, `application threads page read from disk to cache time (usecs)` and its count), the reads
  that stood in a request's way, beside the server's own read latency (`opLatencies.reads`, microseconds); their ratio over the
  last 10 s is the share of the reads' own time spent on pages the cache did not hold. The runner's attach check stops a run on a
  server that lacks either key, as it already stops one that lacks the cache's own sizes: no run ever runs native in Omni's name;
- the spend: slow reads with the cache full (WiredTiger's own 80%, or evicting) and missing (1% or more of the pages requested)
  grow the cache by the compass's own law (ceil(force / 0.1) notches of 64 MB a second; at the wall a quarter of the cover at
  once), never clamped by an allowance, up to the cover's top (2,048 MB), where that account says the misses are at least the one
  key's floor (a half of one percent, `tools/readings.py` `SIZE_FLOOR`) of the reads' time and the host keeps 5% of its memory
  available after the notch (`/proc/meminfo`); the memory is power given, shown beside the misses it bought off;
- the hold: where the misses are under the floor the cache holds and the audit says why; where the account or the host's memory
  is unread this second, nothing is known and nothing is taken;
- the hand-back: calm with the misses under 1% (amendment 1) gives one notch back after the dwell, never below the most the cache
  held in the last 60 s (with the fullness margin, rounded up to a notch) and never below the operator's 512 MB; the operator's
  cache handed back at the end as before; the notch added back below the operator's size while missing (omni-v20's rule) is moot
  under the max, which never goes below it;
- the record: every second's disk reads and their time, the misses' share of the reads' time, the floor and the host's room in the
  audit; the arm's record carries the max's counts where it carried the verdict's allowance; every workload record carries its
  `dial`; `OMNI_DIAL=save` keeps omni-v21's loop (the tune-down); `tools/store_brain.py` and `tools/knob_verdict.py` join the
  fingerprint with this version.

**The model gate** (`tools/store_gate.py`, class S, the omni-v21 arms' recorded seconds replayed open-loop through the candidate).
omni-v21's audits carry neither WiredTiger's account nor the host's memory, so the candidate holds at the operator's cache in every
replayed arm: seconds below native 12.5 → 0 an arm (shown), seconds below native while missing 2.1 → 0 (GAIN +100.0%), the knob's
moves 5.6 → 0 (GAIN +100.0%), the cache held 520.6 → 512.0 MB (+1.7%, GAIN, a cut); no LOSS. MongoDB's own account could not be
read on the machine this amendment was written on (its publisher's download hosts are not reachable from it), so what the misses
cost on the rig is read for real on the first run of the next engine, and a closed-loop model of the cache, set from those files,
follows before any further change to the rule.

**Expected before the runs**, at the counted 30 s a notch, three paired repetitions a run: where the account reads the misses at the
floor or above, the cache rising toward the working set (power given) and the misses falling with it, the read latency and the work
inside the line GAIN or EVEN; where it reads them under the floor, the cache holding at the operator's size and every gauge EVEN; the
knob's moves shown; no second below the operator's cache. A LOSS row is a fault to fix, never a number to accept. The counted runs
on this amendment run on the next engine version, which lands only when the model gate reads no LOSS for every store wire it changes.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
