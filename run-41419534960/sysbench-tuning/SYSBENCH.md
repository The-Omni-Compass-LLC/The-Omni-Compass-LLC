# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v24 (digest 66c8f2d94b3e4725, 65 files) at `7f74bd306bf6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,942 | 2,939 | -0.1% | -12.1 to 4.92 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,945 | 2,942 | -0.1% | -10.5 to 4.57 | STEADY, no difference beyond the noise |
| queries a second | 2,945 | 2,942 | -0.1% | -10.5 to 4.57 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.282 | 0.294 | +4.5% | -0.0211 to 0.0464 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.402 | 0.412 | +2.5% | -0.0115 to 0.0315 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.175 | 0.174 | -0.7% | -0.00678 to 0.00419 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 302 | +136.0% | 24.9 to 323 | power given |
| pages holding data, mean (MB) | 121 | 288 | +137.7% | 28.1 to 306 | power given |
| pages read from disk into the pool (misses) | 1,028,741 | 674,230 | -34.5% | -622,224 to -86,797 | shown, not judged |
| host CPU busy (share of the run) | 0.15 | 0.15 | -0.3% | -0.00667 to 0.00568 | STEADY, no difference beyond the noise |
| host CPU-seconds | 272 | 271 | -0.3% | -12.2 to 10.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.201 | 0.201 | -0.2% | -0.00926 to 0.00858 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
