# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `dc661a710157`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 293 | 290 | -0.7% | -4.99 to 0.652 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 296 | 297 | +0.2% | -4.45 to 5.37 | EVEN, no difference beyond the noise |
| queries a second | 4,737 | 4,745 | +0.2% | -71.3 to 86 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4 | 4.2 | +4.9% | -0.181 to 0.574 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 15.6 | 34.3 | +119.8% | -35.4 to 72.7 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.81 | 3.16 | +12.4% | -1.39 to 2.09 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 135 | +5.7% | 6.89 to 7.83 | power given |
| pages holding data, mean (MB) | 120 | 131 | +8.8% | 6.09 to 14.9 | power given |
| pages read from disk into the pool (misses) | 580,654 | 557,572 | -4.0% | -95,524 to 49,362 | shown, not judged |
| host CPU busy (share of the run) | 0.167 | 0.169 | +0.7% | -0.00508 to 0.00757 | EVEN, no difference beyond the noise |
| host CPU-seconds | 100 | 101 | +0.8% | -3.01 to 4.57 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.24 | 2.28 | +1.5% | -0.0562 to 0.125 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
