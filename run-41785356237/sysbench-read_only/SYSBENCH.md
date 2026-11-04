# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `0a92e09fe669`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 290 | 290 | -0.2% | -3.46 to 2.1 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 296 | 296 | +0.3% | 0.154 to 1.64 | GAIN |
| queries a second | 4,729 | 4,743 | +0.3% | 2.47 to 26.3 | GAIN |
| latency, 95th percentile (ms) | 3.06 | 2.85 | -6.9% | -0.343 to -0.0818 | GAIN |
| latency, 99th percentile (ms) | 53.5 | 66.5 | +24.2% | -70.7 to 96.6 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 3.74 | 3.92 | +4.9% | -1.54 to 1.91 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 1,204 | +840.8% | 1,016 to 1,137 | power given |
| pages holding data, mean (MB) | 120 | 956 | +694.3% | 825 to 847 | power given |
| pages read from disk into the pool (misses) | 2,006,240 | 81,753 | -95.9% | -2,003,760 to -1,845,214 | shown, not judged |
| host CPU busy (share of the run) | 0.168 | 0.154 | -7.9% | -0.0176 to -0.00899 | GAIN |
| host CPU-seconds | 300 | 276 | -7.9% | -31.6 to -15.7 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 2.27 | 2.1 | -7.7% | -0.211 to -0.137 | GAIN |
| buffer pool size changes written (the knob's moves) | 0 | 19 |  | 16.5 to 21.5 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 11.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
