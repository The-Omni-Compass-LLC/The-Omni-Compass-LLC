# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 296 | 294 | -0.5% | -4.29 to 1.43 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 295 | -0.5% | -4.2 to 1.36 | EVEN, no difference beyond the noise |
| queries a second | 4,738 | 4,715 | -0.5% | -67.2 to 21.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.2 | 4.18 | -0.6% | -0.134 to 0.0837 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.74 | +0.0% | -0.256 to 0.256 | EVEN, the same |
| latency, mean (ms) | 3.26 | 3.24 | -0.6% | -0.071 to 0.0293 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 138 | +7.6% | 9.45 to 10.1 | power given |
| pages holding data, mean (MB) | 120 | 136 | +13.0% | 12.5 to 18.7 | power given |
| pages read from disk into the pool (misses) | 1,994,148 | 1,900,649 | -4.7% | -205,393 to 18,395 | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.201 | -1.2% | -0.00951 to 0.00458 | EVEN, no difference beyond the noise |
| host CPU-seconds | 339 | 335 | -1.2% | -15.8 to 7.44 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.5 | 2.49 | -0.7% | -0.0838 to 0.0473 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 8 |  | 8 to 8 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
