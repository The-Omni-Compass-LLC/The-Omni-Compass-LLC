# sysbench on MySQL: Omni-Compass on top of a database's buffer pool as shipped

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default (128 MB), is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v26 (digest 75d3c22eed4473b9, 65 files) at `e81cb06c22b0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,929 | 2,933 | +0.2% | -7.78 to 17.3 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 2,936 | 2,935 | -0.0% | -20.3 to 18.7 | STEADY, no difference beyond the noise |
| queries a second | 2,936 | 2,935 | -0.0% | -20.3 to 18.7 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.214 | 0.206 | -3.7% | -0.032 to 0.016 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.43 | 0.419 | -2.4% | -0.0513 to 0.0307 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 0.156 | 0.124 | -20.2% | -0.0977 to 0.0348 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 128 | 366 | +186.1% | 238 to 238 | power given |
| pages holding data, mean (MB) | 121 | 348 | +187.1% | 227 to 227 | power given |
| pages read from disk into the pool (misses) | 1,029,833 | 550,328 | -46.6% | -483,285 to -475,725 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.11 | -4.4% | -0.0142 to 0.00398 | STEADY, no difference beyond the noise |
| host CPU-seconds | 210 | 201 | -4.5% | -25.6 to 6.76 | STEADY, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.156 | 0.149 | -4.6% | -0.0188 to 0.00435 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to native's pool size (128 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
