# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MySQL as Ubuntu ships it with the operator's InnoDB buffer pool (512 MB) is native; omni is the compass law on the pool size through the server's own console inside [128, 2048] MB in chunks of 128 MB, holding the server's own statement latency at 40% of the 0.6 ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: sysbench oltp_point_select, 1 statements a transaction, 3000 a second offered, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MySQL 8.0.46-0ubuntu0.24.04.4, sysbench 1.0.20; 32 client threads; the transaction line 0.6 ms; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `3e4d20379a2e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 2,942 | 2,940 | -0.0% | -10.2 to 7.5 | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,950 | 2,954 | +0.1% | -5.08 to 11.8 | EVEN, no difference beyond the noise |
| queries a second | 2,950 | 2,954 | +0.1% | -5.08 to 11.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.33 | 0.34 | +2.9% | -0.0453 to 0.0647 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.458 | 0.496 | +8.4% | -0.0458 to 0.123 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.194 | 0.194 | -0.2% | -0.031 to 0.0302 | EVEN, no difference beyond the noise |
| errors (sysbench's ignored errors: deadlocks and retries) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| buffer pool held, mean (MB; the knob, the resource) | 512 | 548 | +7.1% | -120 to 193 | EVEN, no difference beyond the noise |
| pages holding data, mean (MB) | 465 | 494 | +6.2% | -118 to 177 | EVEN, no difference beyond the noise |
| pages read from disk into the pool (misses) | 368,531 | 331,022 | -10.2% | -183,137 to 108,118 | shown, not judged |
| host CPU busy (share of the run) | 0.157 | 0.158 | +0.4% | -0.0173 to 0.0185 | EVEN, no difference beyond the noise |
| host CPU-seconds | 276 | 277 | +0.4% | -29.1 to 31.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.205 | 0.206 | +0.4% | -0.0223 to 0.0241 | EVEN, no difference beyond the noise |
| buffer pool size changes written (the knob's moves) | 0 | 0.333 |  | -1.1 to 1.77 | shown, not judged |

Every omni arm handed back to native's pool size (512 MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
