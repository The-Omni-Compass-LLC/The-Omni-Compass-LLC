# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 297 | +0.3% | -3.05 to 4.75 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 297 | +0.3% | -3.28 to 4.83 | EVEN, no difference beyond the noise |
| queries a second | 4,738 | 4,750 | +0.3% | -52.4 to 77.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 1.73 | 1.68 | -3.0% | -0.285 to 0.183 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.19 | 3.1 | -2.9% | -0.679 to 0.492 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.22 | 1.22 | -0.2% | -0.166 to 0.162 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 363 | -29.0% | -316 to 19.1 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 331 | -28.2% | -282 to 21.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 653,743 | 1,077,694 | +64.8% | -125,703 to 973,605 | shown, not judged |
| host CPU busy (share of the run) | 0.0966 | 0.0962 | -0.5% | -0.0133 to 0.0124 | EVEN, no difference beyond the noise |
| host CPU-seconds | 174 | 173 | -0.5% | -23.9 to 22.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.29 | 1.28 | -0.7% | -0.186 to 0.167 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10.3 |  | 5.16 to 15.5 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
