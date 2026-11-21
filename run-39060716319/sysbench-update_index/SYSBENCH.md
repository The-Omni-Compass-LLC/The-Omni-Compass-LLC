# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `2be7b8f0d97f`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 196 | 209 | +6.5% | -57 to 82.3 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 987 | 988 | +0.1% | -8.42 to 10.6 | EVEN, no difference beyond the noise |
| queries a second | 987 | 988 | +0.1% | -8.42 to 10.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.31 | 3.06 | -29.0% | -1.85 to -0.648 | GAIN |
| latency, 99th percentile (ms) | 13.3 | 9.93 | -25.6% | -9.68 to 2.87 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.53 | 1.26 | -17.7% | -0.523 to -0.016 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 361 | -29.5% | -232 to -69.7 | GAIN |
| pages holding data, mean (MB) | 453 | 290 | -36.0% | -243 to -82.8 | GAIN |
| pages read from disk into the pool (misses) | 189,003 | 287,191 | +52.0% | 86,916 to 109,461 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.119 | +2.5% | -0.0113 to 0.017 | EVEN, no difference beyond the noise |
| host CPU-seconds | 205 | 211 | +2.5% | -19.7 to 29.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.35 | 2.24 | -4.8% | -1.18 to 0.951 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16 |  | 7.04 to 25 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
