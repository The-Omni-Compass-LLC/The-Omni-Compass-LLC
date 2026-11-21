# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `c516caeb5f97`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 294 | -0.2% | -2.41 to 1.29 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | -0.2% | -2.64 to 1.4 | EVEN, no difference beyond the noise |
| queries a second | 4,724 | 4,714 | -0.2% | -42.3 to 22.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.13 | 4.1 | -0.6% | -0.133 to 0.0826 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.67 | 5.71 | +0.6% | -0.113 to 0.182 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.23 | 3.21 | -0.7% | -0.0312 to -0.0153 | GAIN |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 139 | +8.2% | 7.37 to 13.7 | power given |
| pages holding data, mean (MB) | 120 | 137 | +13.7% | 11.9 to 21.1 | power given |
| pages read from disk into the pool (misses) | 1,980,194 | 1,885,284 | -4.8% | -159,555 to -30,265 | shown, not judged |
| host CPU busy (share of the run) | 0.199 | 0.198 | -0.9% | -0.00361 to 0.000106 | EVEN, no difference beyond the noise |
| host CPU-seconds | 332 | 329 | -0.9% | -6.29 to 0.314 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.46 | 2.45 | -0.7% | -0.0301 to -0.00467 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 7.33 |  | 4.46 to 10.2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
