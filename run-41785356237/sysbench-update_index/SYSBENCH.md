# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 3.66 | 5.99 | +63.5% | -1.57 to 6.22 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 983 | 984 | +0.2% | -0.265 to 3.22 | STEADY, no difference beyond the noise |
| queries a second | 983 | 984 | +0.2% | -0.265 to 3.22 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.28 | 1.88 | -17.5% | -0.619 to -0.179 | GAIN |
| latency, 99th percentile (ms) | 4.2 | 3.93 | -6.4% | -0.551 to 0.0123 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.2 | 1.1 | -7.6% | -0.209 to 0.0256 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,248 | +874.8% | 991 to 1,248 | power given |
| pages holding data, mean (MB) | 118 | 856 | +623.2% | 684 to 791 | power given |
| pages read from disk into the pool (misses) | 416,868 | 93,149 | -77.7% | -391,345 to -256,093 | shown, not judged |
| host CPU busy (share of the run) | 0.266 | 0.238 | -10.7% | -0.0577 to 0.000781 | STEADY, no difference beyond the noise |
| host CPU-seconds | 467 | 417 | -10.6% | -99.9 to 0.731 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 280 | 157 | -43.9% | -281 to 35.7 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3 |  | 3 to 3 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
