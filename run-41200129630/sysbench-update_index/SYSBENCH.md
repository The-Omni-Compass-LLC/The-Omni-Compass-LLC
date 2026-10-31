# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 13 | 14.7 | +13.5% | -1.75 to 5.26 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 983 | 985 | +0.3% | -5.03 to 10 | EVEN, no difference beyond the noise |
| queries a second | 983 | 985 | +0.3% | -5.03 to 10 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.02 | 2 | -1.3% | -0.138 to 0.0859 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.51 | 5.51 | -0.1% | -0.248 to 0.242 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.14 | 1.13 | -0.6% | -0.0433 to 0.0294 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,239 | +141.9% | 695 to 758 | power given |
| pages holding data, mean (MB) | 458 | 891 | +94.5% | 406 to 460 | power given |
| pages read from disk into the pool (misses) | 192,723 | 71,821 | -62.7% | -127,893 to -113,913 | shown, not judged |
| host CPU busy (share of the run) | 0.239 | 0.234 | -1.9% | -0.0295 to 0.0204 | EVEN, no difference beyond the noise |
| host CPU-seconds | 419 | 411 | -1.9% | -51.1 to 35.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 78.2 | 64 | -18.1% | -62.7 to 34.4 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
