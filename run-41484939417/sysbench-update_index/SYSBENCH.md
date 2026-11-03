# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `f8696510a222`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 81.3 | 93.4 | +14.9% | -16.9 to 41.1 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 985 | 986 | +0.1% | -5.7 to 8.06 | STEADY, no difference beyond the noise |
| queries a second | 985 | 986 | +0.1% | -5.7 to 8.06 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 277 | 281 | +1.2% | -352 to 359 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 759 | 724 | -4.7% | -1,458 to 1,387 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 59.7 | 57.9 | -3.0% | -78.2 to 74.6 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,241 | +142.4% | 694 to 765 | power given |
| pages holding data, mean (MB) | 458 | 895 | +95.5% | 403 to 472 | power given |
| pages read from disk into the pool (misses) | 191,118 | 69,763 | -63.5% | -129,800 to -112,910 | shown, not judged |
| host CPU busy (share of the run) | 0.129 | 0.123 | -4.8% | -0.0314 to 0.0189 | STEADY, no difference beyond the noise |
| host CPU-seconds | 229 | 218 | -4.8% | -52.6 to 30.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 6.4 | 5.15 | -19.6% | -5.23 to 2.73 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 6.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
