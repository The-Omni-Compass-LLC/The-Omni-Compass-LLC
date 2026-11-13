# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v6 (digest df6147466ef18046, 45 files) at `9a499b137e78`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 193 | 194 | +0.6% | -4.37 to 6.7 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 197 | -0.4% | -2.44 to 0.959 | EVEN, no difference beyond the noise |
| queries a second | 3,950 | 3,935 | -0.4% | -48.9 to 19.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 6.64 | 5.95 | -10.3% | -3.36 to 1.99 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 20.4 | 13.4 | -34.4% | -30.7 to 16.7 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.37 | 3.24 | -3.9% | -1.31 to 1.05 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 441 | -13.9% | -231 to 88.6 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 389 | -15.8% | -175 to 29.1 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 617,340 | 863,672 | +39.9% | -164,831 to 657,495 | shown, not judged |
| host CPU busy (share of the run) | 0.132 | 0.139 | +4.8% | 0.00433 to 0.00824 | power given |
| host CPU-seconds | 236 | 247 | +4.8% | 7.48 to 14.9 | power given |
| host CPU-seconds per 1,000 transactions inside the line | 2.68 | 2.79 | +4.1% | -0.0076 to 0.228 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 15 |  | 1.85 to 28.1 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
