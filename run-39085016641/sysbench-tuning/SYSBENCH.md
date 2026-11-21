# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v9 (digest 7379f3a79ff2c475, 47 files) at `75c2cc7b6b77`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,961 | 2,961 | +0.0% | -15.4 to 15.7 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,966 | 2,966 | +0.0% | -12.3 to 12.4 | EVEN, no difference beyond the noise |
| queries a second | 2,966 | 2,966 | +0.0% | -12.3 to 12.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.17 | 0.178 | +4.7% | -0.145 to 0.161 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.307 | 0.296 | -3.8% | -0.0737 to 0.0504 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0847 | 0.082 | -3.2% | -0.0299 to 0.0245 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 133 | +3.9% | -0.972 to 10.9 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 121 | 130 | +7.1% | 3.77 to 13.5 | power given |
| pages read from disk into the pool (misses) | 1,029,919 | 1,015,856 | -1.4% | -35,913 to 7,787 | shown, not judged |
| host CPU busy (share of the run) | 0.0651 | 0.0632 | -2.9% | -0.0243 to 0.0205 | EVEN, no difference beyond the noise |
| host CPU-seconds | 117 | 113 | -2.9% | -43.4 to 36.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0867 | 0.0842 | -2.9% | -0.0324 to 0.0273 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 4 |  | -0.969 to 8.97 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
