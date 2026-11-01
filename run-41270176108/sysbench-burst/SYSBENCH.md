# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `501d230193c0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 295 | 296 | +0.4% | -4.07 to 6.17 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 295 | 296 | +0.3% | -4.3 to 6.01 | STEADY, no difference beyond the noise |
| queries a second | 4,727 | 4,741 | +0.3% | -68.9 to 96.1 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.83 | 2.88 | +1.8% | -0.077 to 0.179 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.46 | 4.44 | -0.6% | -0.257 to 0.206 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.34 | -1.0% | -0.0289 to 0.00118 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 512 | +0.0% | 0 to 0 | STEADY, the same |
| pages holding data, mean (MB) | 447 | 448 | +0.1% | -1.1 to 1.58 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 246,762 | 248,512 | +0.7% | -4,384 to 7,885 | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.103 | -0.3% | -0.00512 to 0.00459 | STEADY, no difference beyond the noise |
| host CPU-seconds | 61.8 | 61.6 | -0.3% | -3.19 to 2.84 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.37 | 1.37 | -0.6% | -0.0606 to 0.0443 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
