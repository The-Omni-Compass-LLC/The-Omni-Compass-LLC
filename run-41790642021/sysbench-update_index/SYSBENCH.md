# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 8.83 | 10.1 | +14.7% | -1.33 to 3.93 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 985 | 984 | -0.1% | -7.87 to 5.36 | STEADY, no difference beyond the noise |
| queries a second | 985 | 984 | -0.1% | -7.87 to 5.36 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.85 | 1.8 | -2.5% | -0.397 to 0.303 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.86 | 3.84 | -0.6% | -0.451 to 0.408 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.09 | 1.09 | -0.0% | -0.0852 to 0.0847 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,236 | +141.4% | 699 to 749 | power given |
| pages holding data, mean (MB) | 457 | 889 | +94.3% | 407 to 456 | power given |
| pages read from disk into the pool (misses) | 192,141 | 71,651 | -62.7% | -128,272 to -112,708 | shown, not judged |
| host CPU busy (share of the run) | 0.237 | 0.232 | -2.1% | -0.032 to 0.0222 | STEADY, no difference beyond the noise |
| host CPU-seconds | 416 | 408 | -2.0% | -56 to 39.2 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 103 | 89 | -13.7% | -47.1 to 18.8 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
