# Why the data stores read LOSS: the root causes behind the Omni index's fall from +4.32% to +3.40% (25 October 2026)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

**What moved.** The Omni index (`tools/omni_index.py`, `results/OMNI_INDEX.json` `headline_pct`) read +4.32% until commit
`346e06478d` (24 October, 16:44 UTC), and +3.397% after it. That commit brought in the 0.5% key (`tools/readings.py`
`three_run_reading`): a mean change of 0.5% or more across three runs counts by the gauge's aim even when not every run stands
clear of its own noise. Seven data-store rows that counted as 0 before now count; in every one, 0 or 1 of the three runs stood
clear of its noise. Each was traced to its cause below, from the runs' own raw files (class L) and the runners' code. The index
figures are the index's own arithmetic on the repository's tables with the row changed as stated; they are not predictions.
The rows are omni-v16's tables (the store tables on later engines are not whole yet); the runners and `tools/knob_verdict.py` are
unchanged since those runs, so every finding applies to the engine that stands.

**In short.** Three faults are in our own wiring: sysbench's brain cannot see sysbench's queries, Kafka's give-back can never
fire above the operator's count, and YCSB has no hand-back below the operator's cache. Two causes are the test machine: write
stalls on GitHub's runners (in native's arms too) and a host-wide CPU gauge that counts the whole machine. The pgbench pool knob
shows no harm of its own. One scoring point runs against Omni-Compass: sysbench `read_write`'s 95th percentile rose clearly in
two runs (+28.8%, +14.9%); a move inside the noise in the third makes the row "the runs disagree", which counts as 1. If that
row counted, the index would read +3.26%.

| Test | Gauge(s) | Cause | The fix at the cause | Engine file | Index if fixed (now +3.397%) |
|---|---|---|---|---|---|
| pgbench `tpcb_hot` | p95 +430%, +75%, +0.2%; work −6.5%, −1.3%, −0.1% (0 of 3 runs clear) | The test machine: write stalls on the runner in both arms (6.2 s schedule lag in a native arm far under capacity; `select` never stalls, `simple_update` stalls in all six of run A's arms); the worst steps with Omni-Compass ran with the pool at native's 20; run C, the clean runner, STEADY | `pgbench.yml`: log vmstat, iostat, PostgreSQL's checkpoints and lock waits; four repetitions to balance the arm order (a preregistration amendment). Optional in `run_pgbench.py`: re-initialise and `CHECKPOINT` before each arm, `--aggregate-interval=1`, a longer give-back dwell after an add-back | no (the workflow); yes for the optional part | +4.458% (the row 0); +4.509% (its machines GAIN kept) |
| YCSB `c` | energy (host CPU-s) +27.1%, −0.5%, +21.6%; p95 +8.1% in one run | Our wiring: no hand-back on misses below the operator's 512 MB. A give-back trial to 448 MB at t≈20 s, before the working set widens at t=30 s, was allowed in two arms and the cache stayed there with misses ≥1% in 435 of 457 seconds. Growing needs read latency over about 0.44 ms (the most seen, 0.27 ms) and "full" at 90% used, where WiredTiger holds about 80%. The energy row is mostly host noise; the brain's full `serverStatus` every second costs about 19 CPU-s an arm (t≈1.9) | `run_ycsb.py` `decide()`: below native, add 64 MB a second while misses are ≥1%, up to native (the pgbench queue line, amendment 2, for the cache); full at 0.8 or "evicting"; ask `serverStatus` only for the sections the brain reads; record mongod's and the harness's CPU apart, steal excluded | yes | +3.540%; +3.578% |
| YCSB `b` | p95 +3.2%, +2.6%, +5.5%; energy +5.2%, +1.2%, +13.5% (0 of 3) | The test machine: host contention (the p95 change and the host CPU change correlate at 0.38); the cache sat at native's 512 MB for 94–98% of every arm | as YCSB `c` | yes | +3.495%; +3.505% |
| Redis `large` | energy +4.5%, +10.7%, +10.4% (0 of 3) | The gauge: host CPU noise (the same engine reads energy GAIN on `burst`); the memory ceiling rose 64→72 MB and bought hit rate and work, power given for a GAIN as declared | `run_redis.py`: redis-server's, the App's and the brain's CPU measured apart, steal excluded; no change to the knob's rule | yes | +3.512%; +3.514% |
| Kafka `light` | consumers +6.0%, −0.3%, +5.9% (power given, 1 of 3 clear) | Our wiring: give-back above the operator's count needs a consumer whose 200 ms poll came back empty, which never happens with 8 round-robin partitions, so a third consumer allowed at t≈280 s (confounded by the falling load) stayed 170 of 451 seconds and bought nothing; the idle flag starts at 1 (a 2→1→2 double rebalance in the first 11 s of every arm) | `run_kafka.py` `decide()`: above the operator's count, give back on calm with lag 0, no idle test; "idle" a sustained state starting at 0 | yes | +3.451% |
| sysbench `read_write` | work −5.7% in run A (clear); p95 +28.8%, +14.9% (clear) read "the runs disagree" | Our wiring: `status()` counts only `statement/sql/{select,update,insert,delete}`; sysbench's prepared statements are invisible, so the brain reads 4.1 statements a second (the harness's own monitoring) against sysbench's 3,952 queries a second; the compass force and the verdict's work sample are the brain's own queries, driving 10–23 blind resizes an arm. This touches every sysbench row, the GAIN rows included: after the fix all run again and each may move either way | `run_sysbench.py` `status()`: count `statement/com/Execute` and `statement/sql/execute`, for sysbench's user only (the by-user summary table), with a test | yes | +3.419% (+3.259% if its p95 counted) |
| YCSB `f` | p95 +11.6% in run C (0 of 3) | The test machine: one arm with host CPU +126 s while the cache sat at native's 512 MB | the YCSB gauge changes | yes | +3.426%; +3.436% |
| All seven | | | | | +4.923% (every row 0) |

**What the fixes need.** The five runners are in the engine's fingerprint, so a change to any of them is the next engine version:
the model gate first, then `tools/land_engine.py`, then every benchmark's runs A, B and C again. The gate has no model of these
wires today and would read identical; a store model replays the archived `audit.jsonl` files through the new `decide()` (as
omni-v15's cap band was gated), and sysbench's model is set from a short real run, because its reading itself changes.

**The scoring, seen as a lens.** Counting a measure only when at least k of its three runs stand clear of their noise gives +4.311%
at k = 3 (the old key, reproduced), +4.523% at k = 2, +4.771% at k = 1 and +3.397% at k = 0 (the key as it stands, the founder's
order of 24 October). It is information, not a proposal to change the key.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
