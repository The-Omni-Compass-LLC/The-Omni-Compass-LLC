# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## read_only: sysbench oltp_read_only, 14 statements a transaction, 300 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 8.4 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 292 | 292 | +0.3% | -1.51 to 3.32 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 293 | 293 | +0.3% | -2.11 to 3.64 | EVEN, no difference beyond the noise |
| queries a second | 4,682 | 4,695 | +0.3% | -33.7 to 58.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 2.74 | 2.76 | +0.6% | -0.127 to 0.16 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.63 | 4.54 | -1.9% | -0.644 to 0.471 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.82 | 2.11 | -25.3% | -3.73 to 2.31 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 753 | +47.2% | 183 to 300 | power given |
| pages holding data, mean (MB) | 463 | 647 | +39.9% | 173 to 196 | power given |
| pages read from disk into the pool (misses) | 654,812 | 315,162 | -51.9% | -357,494 to -321,806 | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.162 | -1.0% | -0.00831 to 0.00487 | EVEN, no difference beyond the noise |
| host CPU-seconds | 300 | 297 | -1.1% | -15.2 to 8.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 2.23 | 2.2 | -1.3% | -0.103 to 0.043 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 3.67 |  | -1.5 to 8.84 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 1.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
