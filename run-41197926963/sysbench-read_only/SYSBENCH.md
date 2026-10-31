# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.1% | -0.89 to 0.237 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 294 | -0.1% | -0.804 to 0.108 | EVEN, no difference beyond the noise |
| queries a second | 4,717 | 4,711 | -0.1% | -12.9 to 1.73 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.93 | 3.84 | -2.4% | -0.194 to 0.0071 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.5 | 5.41 | -1.8% | -0.102 to -0.0937 | GAIN |
| latency, mean (ms) | 2.99 | 2.96 | -1.2% | -0.0785 to 0.00676 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 670 | +30.9% | 0.323 to 317 | power given |
| pages holding data, mean (MB) | 464 | 605 | +30.3% | -12.7 to 294 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 655,012 | 397,935 | -39.2% | -505,171 to -8,983 | shown, not judged |
| host CPU busy (share of the run) | 0.236 | 0.234 | -0.9% | -0.00544 to 0.00132 | EVEN, no difference beyond the noise |
| host CPU-seconds | 420 | 416 | -0.9% | -9.71 to 2.29 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.12 | 3.09 | -0.8% | -0.0735 to 0.0263 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1.67 |  | 0.232 to 3.1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
