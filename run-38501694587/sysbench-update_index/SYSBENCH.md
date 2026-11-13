# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v5 (digest 6093b2b88aa911b9, 44 files) at `69005c7e4868`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 249 | 296 | +18.9% | -104 to 198 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 988 | 987 | -0.1% | -3.79 to 1.71 | EVEN, no difference beyond the noise |
| queries a second | 988 | 987 | -0.1% | -3.79 to 1.71 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.54 | 2.28 | -10.2% | -0.828 to 0.311 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.97 | 4.71 | -5.3% | -0.47 to -0.0537 | GAIN |
| latency, mean (ms) | 0.955 | 0.956 | +0.2% | -0.233 to 0.236 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 285 | -44.4% | -314 to -141 | GAIN |
| pages holding data, mean (MB) | 453 | 244 | -46.1% | -305 to -113 | GAIN |
| pages read from disk into the pool (misses) | 189,130 | 322,653 | +70.6% | 103,639 to 163,408 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.116 | -0.2% | -0.0244 to 0.024 | EVEN, no difference beyond the noise |
| host CPU-seconds | 204 | 204 | -0.2% | -42.5 to 41.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.87 | 1.52 | -18.7% | -1.93 to 1.23 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 7 |  | 7 to 7 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
