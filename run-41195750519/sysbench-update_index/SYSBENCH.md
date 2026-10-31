# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 21.1 | 23.8 | +13.2% | -7.2 to 12.8 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 982 | 985 | +0.3% | -0.179 to 5.62 | EVEN, no difference beyond the noise |
| queries a second | 982 | 985 | +0.3% | -0.179 to 5.62 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.67 | 1.62 | -3.2% | -0.366 to 0.26 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.68 | 3.68 | +0.0% | -0.286 to 0.286 | EVEN, the same |
| latency, mean (ms) | 1.01 | 1 | -0.7% | -0.0946 to 0.08 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,236 | +141.4% | 702 to 746 | power given |
| pages holding data, mean (MB) | 457 | 889 | +94.5% | 411 to 453 | power given |
| pages read from disk into the pool (misses) | 192,730 | 71,608 | -62.8% | -130,912 to -111,332 | shown, not judged |
| host CPU busy (share of the run) | 0.224 | 0.219 | -2.1% | -0.0329 to 0.0236 | EVEN, no difference beyond the noise |
| host CPU-seconds | 393 | 385 | -2.1% | -57.6 to 41.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 42.9 | 35.4 | -17.4% | -38.3 to 23.4 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
