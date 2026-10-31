# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 292 | -0.3% | -3.19 to 1.24 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 294 | 294 | -0.3% | -2.93 to 1.45 | EVEN, no difference beyond the noise |
| queries a second | 4,711 | 4,699 | -0.3% | -46.8 to 23.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.97 | 4.97 | -0.0% | -0.222 to 0.218 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.04 | 7.13 | +1.2% | -0.29 to 0.465 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.22 | 3.21 | -0.2% | -0.0991 to 0.0846 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 779 | +52.1% | 122 to 412 | power given |
| pages holding data, mean (MB) | 453 | 704 | +55.4% | 124 to 378 | power given |
| pages read from disk into the pool (misses) | 248,257 | 161,563 | -34.9% | -118,869 to -54,520 | shown, not judged |
| host CPU busy (share of the run) | 0.251 | 0.248 | -1.1% | -0.0136 to 0.00807 | EVEN, no difference beyond the noise |
| host CPU-seconds | 149 | 147 | -1.2% | -8.78 to 5.15 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.32 | 3.29 | -0.8% | -0.145 to 0.095 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
