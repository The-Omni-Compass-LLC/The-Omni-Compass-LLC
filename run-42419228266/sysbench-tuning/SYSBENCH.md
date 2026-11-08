# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `84462b32eacc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,948 | 2,945 | -0.1% | -14.7 to 9.95 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,954 | 2,953 | -0.1% | -11.3 to 7.58 | STEADY, no difference beyond the noise |
| queries a second | 2,954 | 2,953 | -0.1% | -11.3 to 7.58 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.303 | 0.305 | +0.5% | -0.0266 to 0.0299 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.448 | 0.451 | +0.6% | -0.0387 to 0.044 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.189 | 0.193 | +2.0% | -0.0133 to 0.021 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 569 | +11.1% | -187 to 300 | STEADY, no difference beyond the noise |
| pages holding data, mean (MB) | 464 | 514 | +10.7% | -155 to 254 | STEADY, no difference beyond the noise |
| pages read from disk into the pool (misses) | 368,243 | 324,036 | -12.0% | -236,906 to 148,492 | shown, not judged |
| host CPU busy (share of the run) | 0.152 | 0.155 | +1.8% | -0.00907 to 0.0147 | STEADY, no difference beyond the noise |
| host CPU-seconds | 268 | 273 | +1.8% | -16.1 to 25.7 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.199 | 0.203 | +1.9% | -0.0125 to 0.02 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
