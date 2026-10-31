# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 293 | -0.3% | -3.53 to 1.95 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | -0.3% | -3.38 to 1.71 | EVEN, no difference beyond the noise |
| queries a second | 4,695 | 4,682 | -0.3% | -54.1 to 27.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.48 | 2.48 | -0.0% | -0.112 to 0.111 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.96 | 3.96 | +0.0% | -0.176 to 0.176 | EVEN, the same |
| latency, mean (ms) | 1.86 | 1.85 | -0.2% | -0.145 to 0.136 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 549 | +7.2% | -122 to 195 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 492 | +6.3% | -118 to 176 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 657,063 | 587,394 | -10.6% | -347,372 to 208,035 | shown, not judged |
| host CPU busy (share of the run) | 0.159 | 0.159 | +0.0% | -0.0114 to 0.0116 | EVEN, no difference beyond the noise |
| host CPU-seconds | 295 | 295 | +0.1% | -21.3 to 21.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.18 | 2.19 | +0.3% | -0.164 to 0.178 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
