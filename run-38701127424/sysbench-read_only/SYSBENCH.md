# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 295 | +0.3% | -1.71 to 3.25 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 295 | 295 | +0.3% | -1.67 to 3.17 | EVEN, no difference beyond the noise |
| queries a second | 4,715 | 4,727 | +0.3% | -26.8 to 50.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.18 | 4.1 | -1.8% | -0.258 to 0.11 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.6 | -2.4% | -0.425 to 0.155 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.21 | 3.2 | -0.5% | -0.0476 to 0.0124 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 456 | -10.9% | -146 to 34.1 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 413 | -10.7% | -139 to 40.1 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 652,695 | 807,256 | +23.7% | -183,894 to 493,016 | shown, not judged |
| host CPU busy (share of the run) | 0.193 | 0.194 | +0.8% | 0.000355 to 0.00274 | power given |
| host CPU-seconds | 319 | 322 | +1.0% | 1.03 to 5.29 | power given |
| host CPU-seconds per 1,000 transactions inside the line | 2.37 | 2.39 | +0.7% | -0.00407 to 0.0389 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 16.3 |  | 8.35 to 24.3 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
