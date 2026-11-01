# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v23 (digest c96ea4105d8747db, 65 files) at `09b65edc31ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,940 | 2,939 | -0.0% | -11.7 to 10.7 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,950 | 2,954 | +0.1% | -2.26 to 9.4 | STEADY, no difference beyond the noise |
| queries a second | 2,950 | 2,954 | +0.1% | -2.26 to 9.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.324 | 0.339 | +4.5% | -0.0551 to 0.0845 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.475 | 0.509 | +7.2% | -0.0549 to 0.123 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.194 | 0.203 | +4.4% | -0.0143 to 0.0316 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 804 | +57.0% | -446 to 1,029 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 682 | +47.1% | -287 to 724 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,475 | 246,048 | -32.9% | -392,074 to 151,221 | shown, not judged |
| host CPU busy (share of the run) | 0.155 | 0.162 | +4.3% | -0.00841 to 0.0217 | STEADY, no difference beyond the noise |
| host CPU-seconds | 274 | 285 | +4.3% | -14.5 to 37.8 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.204 | 0.212 | +4.3% | -0.0115 to 0.0288 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | -1.48 to 3.48 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
