# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2.03 | 1.95 | -3.6% | -3.66 to 3.52 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 983 | 983 | -0.1% | -5.03 to 3.76 | EVEN, no difference beyond the noise |
| queries a second | 983 | 983 | -0.1% | -5.03 to 3.76 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.39 | 2.53 | +6.0% | -0.453 to 0.741 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.11 | 4.34 | +5.6% | -1.1 to 1.56 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.26 | 1.28 | +2.2% | -0.151 to 0.205 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 146 | +13.9% | 13.3 to 22.3 | power given |
| pages holding data, mean (MB) | 118 | 129 | +9.2% | 7.23 to 14.6 | power given |
| pages read from disk into the pool (misses) | 415,718 | 402,508 | -3.2% | -18,874 to -7,547 | shown, not judged |
| host CPU busy (share of the run) | 0.211 | 0.317 | +50.8% | -0.0427 to 0.256 | EVEN, no difference beyond the noise |
| host CPU-seconds | 326 | 494 | +51.7% | -63.4 to 400 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 408 | 712 | +74.5% | -1,033 to 1,641 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
