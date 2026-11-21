# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `3178f6f36474`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,945 | 2,943 | -0.1% | -12.7 to 9.4 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,952 | 2,951 | -0.0% | -10.2 to 7.64 | EVEN, no difference beyond the noise |
| queries a second | 2,952 | 2,951 | -0.0% | -10.2 to 7.64 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.336 | 0.334 | -0.6% | -0.0395 to 0.0355 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.456 | 0.451 | -1.2% | -0.0363 to 0.025 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.208 | 0.209 | +0.7% | -0.0195 to 0.0224 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 468 | -8.7% | -92.9 to 4.07 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 422 | -8.9% | -87.3 to 4.94 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,850 | 416,137 | +13.4% | -16,772 to 115,347 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.108 | +1.6% | -0.0179 to 0.0213 | EVEN, no difference beyond the noise |
| host CPU-seconds | 177 | 180 | +1.7% | -30.3 to 36.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.132 | 0.134 | +1.8% | -0.0229 to 0.0275 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 12 |  | 9.52 to 14.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
