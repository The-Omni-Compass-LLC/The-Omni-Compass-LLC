# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 6 1 8 1 6 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 287 | 288 | +0.2% | -6.75 to 7.94 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 292 | 291 | -0.2% | -10.9 to 9.93 | EVEN, no difference beyond the noise |
| queries a second | 4,668 | 4,660 | -0.2% | -174 to 159 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 4.6 | 4.42 | -4.1% | -1.64 to 1.26 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 193 | 11.1 | -94.2% | -939 to 576 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.41 | 3.02 | -52.8% | -18.1 to 11.3 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 312 | -39.0% | -513 to 114 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 443 | 256 | -42.3% | -390 to 14.9 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 243,465 | 368,465 | +51.3% | -86,619 to 336,619 | shown, not judged |
| host CPU busy (share of the run) | 0.17 | 0.174 | +2.5% | 0.000965 to 0.00769 | power given |
| host CPU-seconds | 104 | 106 | +2.7% | 0.99 to 4.65 | power given |
| host CPU-seconds per 1,000 transactions inside the line | 2.34 | 2.39 | +2.4% | 0.0393 to 0.0726 | power given |
| buffer pool size changes written (the knob's moves) | 0 | 3.67 |  | 0.798 to 6.54 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
