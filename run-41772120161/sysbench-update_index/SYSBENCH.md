# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `db6e040b4584`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 237 | 289 | +21.9% | -51.9 to 156 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 988 | 987 | -0.1% | -7.88 to 5.51 | STEADY, no difference beyond the noise |
| queries a second | 988 | 987 | -0.1% | -7.88 to 5.51 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 29.9 | 32.3 | +8.3% | -75.1 to 80.1 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 176 | 152 | -13.8% | -372 to 324 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 7.91 | 6.74 | -14.9% | -16.7 to 14.3 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,300 | +915.6% | 1,160 to 1,184 | power given |
| pages holding data, mean (MB) | 118 | 884 | +648.8% | 759 to 773 | power given |
| pages read from disk into the pool (misses) | 419,290 | 70,851 | -83.1% | -361,635 to -335,244 | shown, not judged |
| host CPU busy (share of the run) | 0.16 | 0.133 | -16.9% | -0.0526 to -0.00164 | GAIN |
| host CPU-seconds | 281 | 233 | -16.8% | -92.2 to -2.34 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.68 | 1.78 | -33.6% | -2.48 to 0.676 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 9.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
