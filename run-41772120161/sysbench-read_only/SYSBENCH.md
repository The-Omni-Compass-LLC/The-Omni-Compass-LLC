# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 294 | 294 | +0.1% | -1.58 to 2.42 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 294 | 295 | +0.2% | -0.886 to 2.26 | STEADY, no difference beyond the noise |
| queries a second | 4,705 | 4,716 | +0.2% | -14.2 to 36.2 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 3.4 | 3.32 | -2.4% | -0.254 to 0.0929 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.54 | 4.57 | +0.6% | -0.443 to 0.496 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.67 | 2.54 | -4.7% | -0.289 to 0.0363 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 674 | +426.7% | 177 to 915 | power given |
| pages holding data, mean (MB) | 120 | 582 | +385.5% | 196 to 728 | power given |
| pages read from disk into the pool (misses) | 1,967,387 | 428,338 | -78.2% | -2,037,565 to -1,040,533 | shown, not judged |
| host CPU busy (share of the run) | 0.215 | 0.206 | -4.3% | -0.0168 to -0.00189 | GAIN |
| host CPU-seconds | 385 | 369 | -4.3% | -29.8 to -3.63 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.87 | 2.74 | -4.5% | -0.245 to -0.0116 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 5 |  | 2.52 to 7.48 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
