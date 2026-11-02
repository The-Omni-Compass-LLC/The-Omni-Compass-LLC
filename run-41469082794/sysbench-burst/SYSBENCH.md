# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `d9c26a64b846`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 293 | +0.3% | -6.9 to 8.45 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | +0.3% | -6.47 to 8.17 | STEADY, no difference beyond the noise |
| queries a second | 4,681 | 4,694 | +0.3% | -104 to 131 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.1 | 4.13 | +0.6% | -0.256 to 0.302 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.71 | -0.6% | -0.426 to 0.354 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 2.67 | 2.66 | -0.6% | -0.0533 to 0.0224 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 678 | +32.5% | 22.5 to 310 | power given |
| pages holding data, mean (MB) | 452 | 611 | +35.4% | 26.8 to 293 | power given |
| pages read from disk into the pool (misses) | 247,307 | 190,215 | -23.1% | -110,272 to -3,913 | shown, not judged |
| host CPU busy (share of the run) | 0.214 | 0.213 | -0.4% | -0.00925 to 0.00769 | STEADY, no difference beyond the noise |
| host CPU-seconds | 128 | 128 | -0.5% | -5.61 to 4.24 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.87 | 2.85 | -0.7% | -0.0602 to 0.0224 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
