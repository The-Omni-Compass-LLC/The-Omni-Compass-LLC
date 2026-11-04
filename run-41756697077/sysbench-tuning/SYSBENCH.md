# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v25 (digest cf56fc0a7b707452, 65 files) at `198314d551ea`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,927 | 2,927 | -0.0% | -7.45 to 6.59 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,931 | 2,931 | +0.0% | -6.07 to 6.4 | STEADY, no difference beyond the noise |
| queries a second | 2,931 | 2,931 | +0.0% | -6.07 to 6.4 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.222 | 0.25 | +12.8% | 0.00525 to 0.0514 | LOSS |
| latency, 99th percentile (ms) | 0.404 | 0.43 | +6.3% | -0.0191 to 0.0698 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.158 | 0.165 | +4.0% | -0.0407 to 0.0533 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 909 | +77.5% | 183 to 611 | power given |
| pages holding data, mean (MB) | 465 | 798 | +71.7% | 188 to 479 | power given |
| pages read from disk into the pool (misses) | 367,617 | 170,536 | -53.6% | -277,971 to -116,191 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.131 | +4.9% | -0.00824 to 0.0205 | STEADY, no difference beyond the noise |
| host CPU-seconds | 231 | 243 | +5.0% | -15.5 to 38.5 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.172 | 0.18 | +5.0% | -0.0116 to 0.0289 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
