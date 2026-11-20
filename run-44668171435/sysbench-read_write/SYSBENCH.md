# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.5, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v27 (digest 34548e45437a05bd, 65 files) at `8c3f6f107001`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 158 | 159 | +1.0% | -23.7 to 26.7 | STEADY, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | +0.1% | -1.27 to 1.76 | STEADY, no difference beyond the noise |
| queries a second | 3,935 | 3,940 | +0.1% | -25.3 to 35.2 | STEADY, no difference beyond the noise |
| latency, 95th percentile (ms) | 95.8 | 85.8 | -10.4% | -60.9 to 40.9 | STEADY, no difference beyond the noise |
| latency, 99th percentile (ms) | 229 | 231 | +0.7% | -161 to 164 | STEADY, no difference beyond the noise |
| latency, mean (ms) | 18.1 | 17.5 | -3.0% | -14.1 to 13 | STEADY, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | STEADY, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 1,248 | +143.8% | 706 to 766 | power given |
| pages holding data, mean (MB) | 463 | 1,026 | +121.6% | 541 to 585 | power given |
| pages read from disk into the pool (misses) | 615,446 | 85,156 | -86.2% | -569,014 to -491,566 | shown, not judged |
| host CPU busy (share of the run) | 0.196 | 0.183 | -7.1% | -0.0249 to -0.00291 | GAIN |
| host CPU-seconds | 349 | 324 | -7.1% | -44.2 to -5.24 | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 4.85 | 4.48 | -7.7% | -1.1 to 0.356 | STEADY, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 9 |  | 4.03 to 14 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 7.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
