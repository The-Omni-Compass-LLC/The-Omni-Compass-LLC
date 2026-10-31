# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,945 | 2,939 | -0.2% | -10.3 to -1.39 | LOSS |
| throughput (transactions a second) | 2,957 | 2,951 | -0.2% | -7.11 to -4.48 | LOSS |
| queries a second | 2,957 | 2,951 | -0.2% | -7.11 to -4.48 | LOSS |
| latency, 95th percentile (ms) | 0.353 | 0.346 | -1.8% | -0.0491 to 0.0364 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.502 | 0.493 | -1.7% | -0.046 to 0.0286 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.209 | 0.207 | -1.0% | -0.0124 to 0.00821 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 540 | +5.5% | -93.5 to 150 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 465 | 487 | +4.8% | -96.4 to 141 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 366,957 | 341,979 | -6.8% | -125,877 to 75,921 | shown, not judged |
| host CPU busy (share of the run) | 0.168 | 0.166 | -1.1% | -0.00939 to 0.00584 | EVEN, no difference beyond the noise |
| host CPU-seconds | 296 | 293 | -1.1% | -17 to 10.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.22 | 0.218 | -0.9% | -0.0121 to 0.00814 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
