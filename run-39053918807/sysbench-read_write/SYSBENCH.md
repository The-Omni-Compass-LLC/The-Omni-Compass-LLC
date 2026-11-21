# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_write: sysbench oltp_read_write, 18 statements a transaction, 200 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 10.8 ms; 3 paired repetitions; engine omni-v8 (digest f93d233136a1f902, 46 files) at `b02d3a212d40`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 192 | 192 | -0.3% | -2.26 to 1.2 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 197 | 196 | -0.5% | -3.3 to 1.43 | EVEN, no difference beyond the noise |
| queries a second | 3,937 | 3,918 | -0.5% | -66.1 to 28.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 8.54 | 8.33 | -2.4% | -0.798 to 0.39 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.5 | 12.5 | -0.6% | -0.721 to 0.575 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.41 | 5.36 | -0.9% | -0.299 to 0.198 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 541 | +5.6% | -41.2 to 98.4 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 462 | 487 | +5.3% | -30.7 to 79.5 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 616,489 | 554,077 | -10.1% | -264,581 to 139,756 | shown, not judged |
| host CPU busy (share of the run) | 0.221 | 0.217 | -1.9% | -0.0209 to 0.0123 | EVEN, no difference beyond the noise |
| host CPU-seconds | 356 | 350 | -1.8% | -33.5 to 20.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 4.04 | 3.98 | -1.6% | -0.333 to 0.207 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 14.7 |  | 10.9 to 18.5 | shown, not judged |

Every omni arm handed back to the operator's pool size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
