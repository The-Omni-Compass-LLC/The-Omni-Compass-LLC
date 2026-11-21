# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## update_index: sysbench oltp_update_index, 1 statements a transaction, 1000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 159 | 160 | +0.9% | -48.2 to 51 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 988 | 987 | -0.1% | -4.05 to 1.76 | EVEN, no difference beyond the noise |
| queries a second | 988 | 987 | -0.1% | -4.05 to 1.76 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.41 | 2.19 | -9.3% | -1.35 to 0.9 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.05 | 6.26 | -11.2% | -13.2 to 11.6 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.89 | 1.1 | -41.9% | -4.46 to 2.87 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 135 | +5.8% | -4.72 to 19.7 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 118 | 123 | +4.2% | -3.32 to 13.2 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 415,427 | 410,068 | -1.3% | -20,333 to 9,616 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.138 | -1.1% | -0.012 to 0.00884 | EVEN, no difference beyond the noise |
| host CPU-seconds | 246 | 243 | -1.1% | -21.4 to 15.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 3.46 | 3.35 | -3.4% | -1.31 to 1.08 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4 |  | -0.969 to 8.97 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
